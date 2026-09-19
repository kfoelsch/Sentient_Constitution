#!/usr/bin/env python3
"""Advisory audit for the optional `**Depends on:**` sub-bullet under O.

Chapter Two §1.1 introduces an optional `**Depends on:**` sub-bullet under the
Ontological (O) component for *constitutive* prerequisites (bounds, floors,
classifiers, alignment targets). To keep that line distinct from assessment
routing, `**Depends on:**` must NOT merely restate the definition's own
Measurement co-measures (`**Secondary measure:**` / `**Tertiary measure:**`, or
legacy `*Measurements:*` `**Secondary:**` / `**Tertiary:**`).

This audit is ADVISORY by default: it reports overlaps and exits 0 so it never
blocks a publication cut on its own. Pass --strict to exit non-zero when any
overlap is found (useful for a focused clean-up pass).
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_AIMS, CH5_BANDS

SCOPE_FILES = (*CH5_BANDS, *CH5_AIMS)

# Entry header (canonical leaf definitions use #### / #####).
ENTRY_HEADER = re.compile(r"^#{4,5} \S", re.MULTILINE)

# O component start (guidepost or legacy marker).
O_START = re.compile(r"^(- \*\*O:\*\*|- O:|- \*\*What it is\*\*)", re.MULTILINE)
# O component end: start of the measure/assess region.
O_END = re.compile(
    r"^- \*\*A:\*\*|^- A:|^- \*\*E:\*\*|^- E:"
    r"|^- \*\*How to measure and assess\*\*|^\*Measurements:\*"
    r"|^\s*<a id=\".*-(?:a|e)\"></a>\s*$",
    re.MULTILINE,
)

DEPENDS_ON = re.compile(r"^\s*- \*{0,2}Depends on:?\*{0,2}[:\s]", re.MULTILINE)
SECONDARY_TERTIARY = re.compile(
    r"^\s*-? ?\*\*(?:Secondary|Tertiary)(?: measure)?:\*\*",
    re.MULTILINE,
)

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def title_before(text: str, pos: int) -> str:
    for line in reversed(text[:pos].splitlines()):
        stripped = line.strip()
        if stripped.startswith("#### ") or stripped.startswith("##### "):
            return stripped.lstrip("#").strip()
    return "(unknown term)"


def entry_bounds(text: str, o_start: int) -> int:
    """Return the end offset of the entry containing O (next entry header)."""
    next_header = ENTRY_HEADER.search(text, o_start)
    return next_header.start() if next_header else len(text)


def links_in(fragment: str) -> set[str]:
    return {m.group(1) for m in LINK.finditer(fragment)}


def depends_line(o_block: str) -> str | None:
    match = DEPENDS_ON.search(o_block)
    if not match:
        return None
    # Grab the single logical line (up to next newline).
    tail = o_block[match.start() :]
    return tail.split("\n", 1)[0]


def measure_region_links(text: str, o_end: int, entry_end: int) -> set[str]:
    region = text[o_end:entry_end]
    found: set[str] = set()
    for line_match in SECONDARY_TERTIARY.finditer(region):
        line = region[line_match.start() :].split("\n", 1)[0]
        found |= links_in(line)
    return found


def audit_file(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    warnings: list[str] = []
    for match in O_START.finditer(text):
        o_start = match.start()
        end_match = O_END.search(text, match.end())
        entry_end = entry_bounds(text, o_start)
        o_block = text[o_start : end_match.start()] if end_match else text[o_start:entry_end]
        dep = depends_line(o_block)
        if not dep:
            continue
        dep_links = links_in(dep)
        if not dep_links:
            continue
        o_end = end_match.start() if end_match else o_start
        measure_links = measure_region_links(text, o_end, entry_end)
        overlap = dep_links & measure_links
        if overlap:
            title = title_before(text, o_start)
            lineno = line_number(text, o_start)
            pretty = ", ".join(sorted(overlap))
            warnings.append(
                f"{path}:{lineno}: {title} — Depends on duplicates Measure "
                f"co-measure link(s): {pretty}"
            )
    return warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when any overlap is found (default: advisory, exit 0).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    warnings: list[str] = []
    for rel in SCOPE_FILES:
        path = root / rel
        if path.exists():
            warnings.extend(audit_file(path))
    if warnings:
        print("\n".join(warnings))
        print(
            f"\n{len(warnings)} Depends-on/Measure overlap warning(s). "
            "Depends on should carry constitutive prerequisites, not assessment "
            "co-measures (Chapter Two §1.1)."
        )
        return 1 if args.strict else 0
    print("ch5-depends-on-audit: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
