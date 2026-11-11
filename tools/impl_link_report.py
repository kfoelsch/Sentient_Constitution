#!/usr/bin/env python3
"""Report which implementation files their core chapter links (report only, never fails).

Each ``corpus_*`` subfile carries ``Core home: NN``. ``tools/architecture/chapter_numbers.json``
maps that home to its ``core_*`` files, so the report never derives a chapter number from a
file name. For every implementation file it records the best status among the core files of
its home chapter:

* ``widget``   - linked in an Implementation widget or inline ``Implementation:`` line;
* ``trace``    - linked inside a Trace widget;
* ``body``     - linked, but only outside a Trace widget;
* ``id-only``  - named by its ID (for example ``CF-15.425``) but never linked;
* ``none``     - neither linked nor named.

A file whose status is ``none`` is then split: named in some other core chapter, or named by no
core file at all (an orphan from the core's side).

Registry and scope annexes (section family 00 of each layer) are listed apart: the Preamble
is not expected to link them. The exit status is always 0.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from collections import defaultdict
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)\s#]+?\.md)(?:#[^)\s]*)?\)")
HOME_RE = re.compile(r"^Core home: (\d+)", re.MULTILINE)
NAME_RE = re.compile(r"^(cjs|cs|ci|cf)_(\d+)\.(\d+)_")
RANK = {"none": 0, "id-only": 1, "body": 2, "trace": 3, "widget": 4}


def impl_id(name: str) -> str | None:
    match = NAME_RE.match(name)
    if not match:
        return None
    return f"{match.group(1).upper()}-{int(match.group(2))}.{match.group(3)}"


def trace_and_rest(lines: list[str]) -> tuple[list[str], list[str]]:
    trace: list[str] = []
    rest: list[str] = []
    depth = 0
    is_trace = False
    for raw in lines:
        stripped = raw.strip()
        if stripped == "<details>":
            depth += 1
            is_trace = False
            continue
        if depth and "<summary" in stripped and ">Trace<" in stripped:
            is_trace = True
        if stripped == "</details>":
            depth = max(0, depth - 1)
            if depth == 0:
                is_trace = False
            continue
        (trace if depth and is_trace else rest).append(raw)
    return trace, rest


def implementation_lines(lines: list[str]) -> list[str]:
    """Lines of Implementation (non-operative) widgets and inline ``Implementation:`` lines."""
    out: list[str] = []
    inside = False
    for raw in lines:
        if raw.strip() == "<details>":
            inside = False
        elif "Implementation (non-operative)" in raw and "<summary>" in raw:
            inside = True
        elif raw.strip() == "</details>":
            inside = False
        if inside or raw.startswith("Implementation: "):
            out.append(raw)
    return out


def links_in(lines: list[str], base: str = "") -> set[str]:
    return {posixpath.normpath(posixpath.join(base, m)) for raw in lines for m in LINK_RE.findall(raw)}


def build(root: Path) -> dict:
    chapters = json.loads((root / "tools/architecture/chapter_numbers.json").read_text(encoding="utf-8"))["chapters"]
    core_by_home: dict[str, list[str]] = defaultdict(list)
    for entry in chapters:
        if entry.get("layer") == "CORE" and entry.get("status") == "active":
            core_by_home[entry["core_home"]].append(entry["destination_file"])
    core_info: dict[str, dict] = {}
    for files in core_by_home.values():
        for name in files:
            path = root / name
            if not path.is_file():
                continue
            lines = path.read_text(encoding="utf-8").split("\n")
            trace, rest = trace_and_rest(lines)
            core_info[name] = {
                "widget": links_in(implementation_lines(lines)),
                "trace": links_in(trace),
                "rest": links_in(rest),
                "text": "\n".join(lines),
            }
    all_core: dict[str, dict] = {}
    for path in sorted(root.glob("core_*.md")):
        lines = path.read_text(encoding="utf-8").split("\n")
        all_core[path.name] = {"links": links_in(lines), "text": "\n".join(lines)}
    rows = []
    annexes = []
    for path in sorted(root.glob("corpus_*/*.md")):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        home_match = HOME_RE.search(text)
        ident = impl_id(path.name)
        if not home_match or not ident:
            rows.append({"file": rel, "id": ident or path.name, "home": None, "status": "no Core home line", "where": [], "elsewhere": []})
            continue
        home = home_match.group(1)
        if path.name.split("_")[1].split(".")[0] == "00":
            annexes.append(rel)
            continue
        best, where = "none", []
        for core in core_by_home.get(home, []):
            info = core_info.get(core)
            if not info:
                continue
            if rel in info["widget"]:
                status = "widget"
            elif rel in info["trace"]:
                status = "trace"
            elif rel in info["rest"]:
                status = "body"
            elif re.search(re.escape(ident) + r"(?![\d.]*\d)", info["text"]):
                status = "id-only"
            else:
                status = "none"
            if RANK[status] > RANK[best]:
                best, where = status, [core]
            elif status == best and status != "none":
                where.append(core)
        home_files = set(core_by_home.get(home, []))
        pattern = re.compile(re.escape(ident) + r"(?![\d.]*\d)")
        elsewhere = [
            name
            for name, info in all_core.items()
            if name not in home_files and (rel in info["links"] or pattern.search(info["text"]))
        ]
        rows.append({"file": rel, "id": ident, "home": home, "status": best, "where": where, "elsewhere": elsewhere})
    return {"rows": rows, "annexes": annexes, "core_by_home": dict(core_by_home)}


def render(data: dict) -> str:
    rows = data["rows"]
    out = ["# Implementation-file links from core chapters (report only)", ""]
    by_home: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_home[row["home"] or "-"].append(row)
    out += ["| Core home | Files | widget | trace | body only | ID only | none in home chapter | of which named by no core file |", "|---|---|---|---|---|---|---|---|"]
    for home in sorted(by_home):
        group = by_home[home]
        count = lambda s: sum(1 for r in group if r["status"] == s)
        orphans = sum(1 for r in group if r["status"] == "none" and not r["elsewhere"])
        out.append(f"| {home} | {len(group)} | {count('widget')} | {count('trace')} | {count('body')} | {count('id-only')} | {count('none')} | {orphans} |")
    total = lambda s: sum(1 for r in rows if r["status"] == s)
    orphan_total = sum(1 for r in rows if r["status"] == "none" and not r["elsewhere"])
    out += ["", f"Totals: {len(rows)} files; widget {total('widget')}, trace {total('trace')}, body only {total('body')}, ID only {total('id-only')}, none in home chapter {total('none')} ({orphan_total} named by no core file).", ""]
    sections = (
        ("Named by ID but never linked", lambda r: r["status"] == "id-only"),
        ("Named by no core file at all", lambda r: r["status"] == "none" and not r["elsewhere"]),
        ("Not named in the home chapter, but named in other core chapters", lambda r: r["status"] == "none" and r["elsewhere"]),
        ("Linked, but not in a Trace widget", lambda r: r["status"] == "body"),
    )
    for label, keep in sections:
        group = [r for r in rows if keep(r)]
        out += [f"## {label} ({len(group)})", ""]
        for home in sorted({r["home"] or "-" for r in group}):
            ids = ", ".join(
                r["id"] + (f" (also in {len(r['elsewhere'])} other core file{'s' if len(r['elsewhere']) != 1 else ''})" if r["status"] == "none" and r["elsewhere"] else "")
                for r in group
                if (r["home"] or "-") == home
            )
            out.append(f"- Core home {home}: {ids}")
        out.append("")
    odd = [r for r in rows if r["home"] is None]
    if odd:
        out += ["## No Core home line", ""] + [f"- {r['file']}" for r in odd] + [""]
    out += [f"Registry and scope annexes (not expected to be linked from the core): {len(data['annexes'])} files.", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root (default: .).")
    parser.add_argument("--out", help="Also write the report to this file.")
    args = parser.parse_args()
    report = render(build(Path(args.root).resolve()))
    print(report)
    if args.out:
        Path(args.out).write_text(report + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
