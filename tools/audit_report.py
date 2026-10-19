#!/usr/bin/env python3
"""Run the audit targets quietly and report one line per category (AUDIT-REGISTRY-01).

`make regression` stays the gate. This script runs the same targets, hides their output, and prints a
short table: one row per category in tools/architecture/audit_registry.json, with each failing target
expanded to the lines that matter. Passing targets cost one table row.

    python3 tools/audit_report.py --root .                    # the regression gate, grouped
    python3 tools/audit_report.py --root . --scope all        # also the audits outside the gate
    python3 tools/audit_report.py --root . --category links   # one category
    python3 tools/audit_report.py --root . --only-failing     # hide passing categories
    python3 tools/audit_report.py --root . --json             # machine-readable
    python3 tools/audit_report.py --root . --list             # categories and targets, nothing run
    python3 tools/audit_report.py --root . --check-registry   # every audit target has a category

Exit status is 1 when a gate target fails (or, with --strict, any target), or when the registry is out of date.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REGISTRY_REL = "tools/architecture/audit_registry.json"
AUDIT_LIKE = re.compile(r"audit|check|validate|-test$|freshness")
_KEY = re.compile(r"\bFAIL(?:ED)?\b|\bERROR\b|\bError\b|error:|Traceback|MISMATCH|TIMEOUT|\bstale\b|\bviolations?\b|\bREVIEW\b|\bUNTRACKED\b")


# ---------------------------------------------------------------- Makefile reading

def regression_targets(makefile_text: str) -> list[str]:
    """Targets of the `regression` recipe, in Makefile order."""
    if "\nregression:\n" not in makefile_text:
        return []
    body = makefile_text.split("\nregression:\n", 1)[1].split("\nregression-full:", 1)[0]
    return re.findall(r"^\t\t([a-z0-9-]+)(?: \\|;)", body, re.M)


def phony_targets(makefile_text: str) -> set[str]:
    joined = re.sub(r"\\\n\s*", " ", makefile_text)
    names: set[str] = set()
    for m in re.finditer(r"^\.PHONY:(.*)$", joined, re.M):
        names |= set(m.group(1).split())
    return names


def defined_targets(makefile_text: str) -> set[str]:
    return set(re.findall(r"^([A-Za-z0-9_.-]+):(?!=)", makefile_text, re.M))


def audit_like_targets(makefile_text: str) -> set[str]:
    like = {t for t in phony_targets(makefile_text) if AUDIT_LIKE.search(t)}
    return like | set(regression_targets(makefile_text))


# ---------------------------------------------------------------- registry

def load_registry(root: Path) -> dict:
    return json.loads((root / REGISTRY_REL).read_text(encoding="utf-8"))


def check_registry(registry: dict, makefile_text: str) -> list[str]:
    """Problems that keep the registry from matching the Makefile (empty when it matches)."""
    problems: list[str] = []
    categories = {c["id"] for c in registry.get("categories", [])}
    targets = registry.get("targets", {})
    ignored = set(registry.get("ignored", {}))
    defined = defined_targets(makefile_text) | phony_targets(makefile_text)
    for name in sorted(audit_like_targets(makefile_text) - ignored - set(targets)):
        problems.append(f"{name}: audit target with no registry entry (add it to {REGISTRY_REL} with a category)")
    for name, entry in sorted(targets.items()):
        if name not in defined:
            problems.append(f"{name}: in the registry but not defined in the Makefile (remove it)")
        if entry.get("category") not in categories:
            problems.append(f"{name}: unknown category {entry.get('category')!r}")
        if entry.get("run") not in ("auto", "never"):
            problems.append(f"{name}: run must be 'auto' or 'never'")
        if not isinstance(entry.get("writes"), bool):
            problems.append(f"{name}: writes must be true or false")
    return problems


def select_targets(registry: dict, regression: list[str], scope: str, categories: set[str]) -> list[str]:
    order = {name: i for i, name in enumerate(regression)}
    names = []
    for name, entry in registry["targets"].items():
        if entry["run"] == "never":
            continue
        if scope == "regression" and name not in order:
            continue
        if categories and entry["category"] not in categories:
            continue
        names.append(name)
    return sorted(names, key=lambda n: (order.get(n, 10**6), n))


# ---------------------------------------------------------------- running

def run_target(root: Path, name: str, timeout: float) -> dict:
    start = time.monotonic()
    try:
        proc = subprocess.run(
            ["make", "--no-print-directory", "-s", name],
            cwd=root, capture_output=True, text=True, timeout=timeout,
        )
        rc, output = proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except subprocess.TimeoutExpired:
        rc, output = 124, f"TIMEOUT after {timeout:.0f}s"
    return {"target": name, "rc": rc, "seconds": round(time.monotonic() - start, 1), "output": output}


def run_all(root: Path, names: list[str], registry: dict, jobs: int, timeout: float) -> dict[str, dict]:
    """Run read-only targets in parallel, then the targets that write files one at a time."""
    results: dict[str, dict] = {}
    parallel = [n for n in names if not registry["targets"][n]["writes"]] if jobs > 1 else []
    serial = [n for n in names if n not in set(parallel)]
    if parallel:
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            for res in pool.map(lambda n: run_target(root, n, timeout), parallel):
                results[res["target"]] = res
    for name in serial:
        results[name] = run_target(root, name, timeout)
    return results


def failure_excerpt(output: str, max_lines: int) -> list[str]:
    """The lines of a failing target's output that say what failed.

    A Python traceback is shown by its last lines (the exception). Otherwise the lines that carry a failure word
    are kept, with the detail lines under them: indented lines, and the next two lines after a FAIL line.
    """
    lines = [ln.rstrip() for ln in output.splitlines() if ln.strip() and not ln.startswith(("make[", "make:"))]
    if any(ln.startswith("Traceback (most recent call last)") for ln in lines):
        return [ln[:220] for ln in lines[-min(max_lines, 6):]]
    picked: list[str] = []
    i = 0
    while i < len(lines) and len(picked) < max_lines:
        if not _KEY.search(lines[i]):
            i += 1
            continue
        picked.append(lines[i])
        is_fail = re.search(r"\bFAIL(?:ED)?\b", lines[i]) is not None
        j = i + 1
        while j < len(lines) and len(picked) < max_lines:
            gap = j - i
            indented = lines[j][:1] in (" ", "\t")
            if (indented and gap <= 3) or (is_fail and gap <= 2):
                picked.append(lines[j])
                j += 1
            else:
                break
        i = j
    if not picked:
        picked = lines[-max_lines:]
    return [ln[:220] for ln in picked]


# ---------------------------------------------------------------- reporting

def summarize(results: dict[str, dict], registry: dict, regression: list[str]) -> list[dict]:
    rows = []
    gate = set(regression)
    for cat in registry["categories"]:
        names = [n for n in results if registry["targets"][n]["category"] == cat["id"]]
        if not names:
            continue
        failed = [n for n in names if results[n]["rc"] != 0]
        rows.append({
            "id": cat["id"], "title": cat["title"], "total": len(names),
            "passed": len(names) - len(failed),
            "failed": failed, "failed_in_gate": [n for n in failed if n in gate],
            "seconds": round(sum(results[n]["seconds"] for n in names), 1),
        })
    return rows


def render_text(rows: list[dict], results: dict[str, dict], regression: list[str], registry: dict, *,
                scope: str, jobs: int, elapsed: float, only_failing: bool, verbose: bool,
                max_lines: int, slowest: int) -> str:
    gate = set(regression)
    total = sum(r["total"] for r in rows)
    passed = sum(r["passed"] for r in rows)
    out = [f"Audit report: scope {scope}, {total} targets, {jobs} job{'s' if jobs != 1 else ''}, {elapsed:.0f}s"]
    width = max((len(r["title"]) for r in rows), default=20) + 2
    for r in rows:
        if only_failing and not r["failed"]:
            continue
        label = (r["title"] + " ").ljust(width, ".")
        line = f"  {label} {r['passed']}/{r['total']}"
        if r["failed"]:
            line += "  FAIL: " + ", ".join(n + ("" if n in gate else "*") for n in r["failed"])
        out.append(line)
    failed_gate = [n for n in results if results[n]["rc"] != 0 and n in gate]
    failed_other = [n for n in results if results[n]["rc"] != 0 and n not in gate]
    if verbose:
        out.append("")
        for n, res in results.items():
            out.append(f"  {'PASS' if res['rc'] == 0 else 'FAIL'} {n} ({res['seconds']}s)")
    if slowest:
        out.append("")
        out.append(f"Slowest {slowest}:")
        for n, res in sorted(results.items(), key=lambda kv: -kv[1]["seconds"])[:slowest]:
            out.append(f"  {res['seconds']:>6}s  {n}")
    for n in failed_gate + failed_other:
        res = results[n]
        cat = next(c["title"] for c in registry["categories"] if c["id"] == registry["targets"][n]["category"])
        out.append("")
        out.append(f"-- {n} ({cat}), exit {res['rc']}, {res['seconds']}s{'' if n in gate else ', outside make regression'}")
        out.extend("   " + ln for ln in failure_excerpt(res["output"], max_lines))
        out.append(f"   re-run: make {n}")
    out.append("")
    if failed_gate:
        out.append(f"Result: FAIL ({len(failed_gate)} gate target{'s' if len(failed_gate) != 1 else ''} failing; {passed}/{total} pass)")
    elif failed_other:
        out.append(f"Result: gate passes; {len(failed_other)} target{'s' if len(failed_other) != 1 else ''} outside the gate failing* ({passed}/{total} pass)")
    else:
        out.append(f"Result: PASS ({passed}/{total})")
    if failed_other:
        out.append("* not part of make regression")
    return "\n".join(out)


def render_json(rows, results, regression, *, scope, jobs, elapsed, max_lines) -> str:
    gate = set(regression)
    return json.dumps({
        "scope": scope, "jobs": jobs, "seconds": round(elapsed, 1),
        "passed": all(r["rc"] == 0 for n, r in results.items() if n in gate),
        "categories": rows,
        "targets": {
            n: {"rc": r["rc"], "seconds": r["seconds"], "in_gate": n in gate,
                **({"excerpt": failure_excerpt(r["output"], max_lines)} if r["rc"] else {})}
            for n, r in results.items()
        },
    }, indent=2)


def render_list(registry: dict, regression: list[str]) -> str:
    gate = set(regression)
    out = []
    for cat in registry["categories"]:
        names = [n for n, e in registry["targets"].items() if e["category"] == cat["id"]]
        out.append(f"{cat['id']}: {cat['title']} ({len(names)})")
        for n in names:
            e = registry["targets"][n]
            flags = ["gate" if n in gate else "outside gate"]
            if e["run"] == "never":
                flags.append("not run (writes a report)")
            elif e["writes"]:
                flags.append("writes files")
            out.append(f"    {n}  [{', '.join(flags)}]")
    return "\n".join(out)


# ---------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--scope", choices=("regression", "all"), default="regression")
    ap.add_argument("--category", action="append", default=[], help="category id (repeat or comma-separate)")
    ap.add_argument("--jobs", type=int, default=4, help="parallel read-only targets (1 = one at a time)")
    ap.add_argument("--timeout", type=float, default=900.0, help="seconds allowed per target")
    ap.add_argument("--max-lines", type=int, default=12, help="lines shown per failing target")
    ap.add_argument("--only-failing", action="store_true")
    ap.add_argument("--verbose", action="store_true", help="list every target")
    ap.add_argument("--slowest", type=int, default=0, metavar="N", help="list the N slowest targets")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--strict", action="store_true", help="fail on any failing target, not only gate targets")
    ap.add_argument("--check-registry", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    makefile_text = (root / "Makefile").read_text(encoding="utf-8")
    registry = load_registry(root)
    regression = regression_targets(makefile_text)

    problems = check_registry(registry, makefile_text)
    if args.check_registry:
        if problems:
            print(f"FAIL: audit registry out of date ({len(problems)} problem{'s' if len(problems) != 1 else ''})")
            for p in problems:
                print("  " + p)
            return 1
        print(f"PASS: audit registry covers every audit target ({len(registry['targets'])} targets, {len(registry['categories'])} categories)")
        return 0
    if problems:
        print("Registry problems (run with --check-registry):", file=sys.stderr)
        for p in problems[:5]:
            print("  " + p, file=sys.stderr)

    if args.list:
        print(render_list(registry, regression))
        return 0

    wanted = {c for item in args.category for c in item.split(",") if c}
    unknown = wanted - {c["id"] for c in registry["categories"]}
    if unknown:
        print(f"unknown category: {', '.join(sorted(unknown))}; known: {', '.join(c['id'] for c in registry['categories'])}", file=sys.stderr)
        return 2
    names = select_targets(registry, regression, args.scope, wanted)
    if not names:
        print("no targets selected", file=sys.stderr)
        return 2

    start = time.monotonic()
    results = run_all(root, names, registry, max(1, args.jobs), args.timeout)
    elapsed = time.monotonic() - start
    results = {n: results[n] for n in names}
    rows = summarize(results, registry, regression)
    if args.json:
        print(render_json(rows, results, regression, scope=args.scope, jobs=args.jobs, elapsed=elapsed, max_lines=args.max_lines))
    else:
        print(render_text(rows, results, regression, registry, scope=args.scope, jobs=args.jobs, elapsed=elapsed,
                          only_failing=args.only_failing, verbose=args.verbose, max_lines=args.max_lines, slowest=args.slowest))
    gate = set(regression)
    failing = [n for n, r in results.items() if r["rc"] != 0 and (args.strict or n in gate)]
    return 1 if failing or problems else 0


if __name__ == "__main__":
    sys.exit(main())
