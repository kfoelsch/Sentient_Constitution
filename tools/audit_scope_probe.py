#!/usr/bin/env python3
"""Measure which corpus files each audit actually reads (AUDIT-SCOPE-01).

Runs each audit target under a Python audit hook that records every Markdown file the
process opens, then compares that with the whole corpus (``binding_corpus_scope``, the numbered
chapters, the four implementation families and their wrappers). The expected scope of every
target is declared in ``tools/architecture/audit_scope_registry.json``:

* ``corpus``: reads every corpus file, apart from the wrapper and support files listed in
  the registry's ``corpus_basis_exempt``;
* ``corpus-except``: reads every corpus file except the globs in ``except`` (``reason`` says why);
* ``format-owned``: checks a format that exists only in the named files; the files are listed
  in ``files`` (globs) and must all be read; ``reason`` says why the format is local;
* ``generator``: freshness check of a generated file, not a rule about corpus text;
* ``not-file-based``: no corpus Markdown involved (JSON registries, tests, scenarios).

A target that reads fewer files than it declares fails. A target missing from the registry fails.
Usage: ``python3 tools/audit_scope_probe.py [--jobs N] [--only target,...] [--list-gaps]``.
It runs the audits, so it is slower than the gate and is not part of ``make regression``.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from corpus_paths import binding_corpus_scope  # noqa: E402

REGISTRY = ROOT / "tools" / "architecture" / "audit_scope_registry.json"
AUDIT_REGISTRY = ROOT / "tools" / "architecture" / "audit_registry.json"

HOOK = """
import os, sys
_out = os.environ.get("SCOPE_PROBE_OUT")
if _out:
    _seen = set()
    def _hook(event, args):
        if event == "open":
            p = args[0]
            if isinstance(p, str) and p.split("#", 1)[0].endswith(".md") and p not in _seen:
                _seen.add(p)
                try:
                    with open(_out, "a") as f:
                        f.write(os.path.abspath(p.split("#", 1)[0]) + "\\n")
                except Exception:
                    pass
    sys.addaudithook(_hook)
"""


def audit_targets() -> list[str]:
    data = json.loads(AUDIT_REGISTRY.read_text(encoding="utf-8"))
    out = []
    for name, meta in data["targets"].items():
        if meta.get("run") == "never" or meta.get("writes") or meta.get("category") in {"tests", "translations"}:
            continue
        out.append(name)
    return out


def probe(target: str, hookdir: Path, outdir: Path) -> set[str]:
    out = outdir / f"{target}.txt"
    out.unlink(missing_ok=True)
    env = dict(os.environ, SCOPE_PROBE_OUT=str(out), PYTHONPATH=str(hookdir))
    subprocess.run(["make", target], cwd=ROOT, env=env, capture_output=True, timeout=240)
    seen: set[str] = set()
    if out.exists():
        for line in out.read_text().splitlines():
            try:
                seen.add(Path(line).resolve().relative_to(ROOT).as_posix())
            except ValueError:
                pass
    return seen


def static_check() -> int:
    """Fast gate (``make audit-scope-check``): the registry is complete and the hand-kept lists match the files."""
    import re

    import ch5_paths
    import corpus_paths

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    problems: list[str] = []
    wanted = set(audit_targets())
    for t in sorted(wanted - set(reg["targets"])):
        problems.append(f"{t}: audit target is not classified in audit_scope_registry.json")
    for t in sorted(set(reg["targets"]) - wanted):
        problems.append(f"{t}: classified in audit_scope_registry.json but is not a probed audit target")
    for t, meta in reg["targets"].items():
        if meta["scope"] != "corpus" and not meta.get("reason"):
            problems.append(f"{t}: scope {meta['scope']} needs a reason")
        for pattern in meta.get("files", []):
            if not any(ROOT.glob(pattern)):
                problems.append(f"{t}: declared file glob matches nothing: {pattern}")

    core_glob = sorted(p.name for p in ROOT.glob("core_*.md") if not re.search(r" \d+\.md$", p.name))
    if core_glob != sorted(corpus_paths.CORE_FILES):
        diff = sorted(set(core_glob) ^ set(corpus_paths.CORE_FILES))
        problems.append(f"corpus_paths.CORE_FILES differs from core_*.md on disk: {diff}")
    ch5_glob = sorted(p.name for p in ROOT.glob("core_05.*.md"))
    if ch5_glob != sorted(ch5_paths.CH5_ALL):
        problems.append(f"ch5_paths.CH5_ALL differs from core_05.*.md on disk: {sorted(set(ch5_glob) ^ set(ch5_paths.CH5_ALL))}")

    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for name in sorted(wanted):
        match = re.search(r"^" + re.escape(name) + r":[^\n]*\n((?:\t[^\n]*\n)+)", makefile, re.M)
        if match and "--changed-only" in match.group(1):
            problems.append(f"{name}: the gate recipe uses --changed-only; audits check the whole corpus (AUDIT-SCOPE-01)")

    if problems:
        print("AUDIT-SCOPE-01 static check: FAIL")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"PASS: AUDIT-SCOPE-01 — {len(reg['targets'])} audits classified; hand-kept file lists match the files; no gate recipe is changed-only.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--static", action="store_true", help="Fast registry and file-list check (the gate).")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    if args.static:
        return static_check()

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    corpus = set(binding_corpus_scope(ROOT))
    basis_exempt = set(reg.get("corpus_basis_exempt", []))
    all_markdown = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*.md")
        if not any(part in {".git", "node_modules", "translations", "_pages_site", "evidence"} for part in p.relative_to(ROOT).parts)
    }
    targets = [t for t in audit_targets() if not args.only or t in args.only.split(",")]
    problems: list[str] = []
    for t in targets:
        if t not in reg["targets"]:
            problems.append(f"{t}: not classified in audit_scope_registry.json")

    with tempfile.TemporaryDirectory() as tmp:
        hookdir = Path(tmp) / "hook"
        outdir = Path(tmp) / "out"
        hookdir.mkdir()
        outdir.mkdir()
        (hookdir / "sitecustomize.py").write_text(HOOK, encoding="utf-8")
        todo = [t for t in targets if t in reg["targets"]]
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            seen_by = dict(zip(todo, pool.map(lambda t: probe(t, hookdir, outdir), todo)))

    print(f"{'target':<52} {'declared':<13} {'corpus files read':>17}")
    for t in todo:
        meta = reg["targets"][t]
        scope = meta["scope"]
        seen = seen_by[t]
        read = len(seen & corpus)
        print(f"{t:<52} {scope:<13} {read:>10}/{len(corpus)}")
        if scope == "corpus":
            missing = sorted(corpus - seen - basis_exempt)
        elif scope == "corpus-except":
            missing = sorted(
                f for f in corpus - seen if not any(fnmatch.fnmatch(f, g) for g in meta.get("except", []))
            )
        elif scope == "format-owned":
            want = {
                f
                for f in all_markdown
                if any(fnmatch.fnmatch(f, g) for g in meta.get("files", []))
            }
            missing = sorted(want - seen) or ([] if want else ["(no file matches the declared globs)"])
        else:
            missing = []
        if scope in {"corpus-except", "format-owned", "generator", "not-file-based"} and not meta.get("reason"):
            problems.append(f"{t}: scope {scope} needs a reason")
        for f in missing[:5]:
            problems.append(f"{t}: declared {scope} but did not read {f}")
        if len(missing) > 5:
            problems.append(f"{t}: … and {len(missing) - 5} more unread file(s)")

    if problems:
        print("\nAUDIT-SCOPE-01 problems:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nAUDIT-SCOPE-01: every audit reads what its registry entry declares.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
