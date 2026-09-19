#!/usr/bin/env python3
"""Move operative-prose ``Read it with:`` blocks into the owning Trace widget.

Maintenance helper for CJS-3 cluster files. Converts each routing bullet to
``- Read with: …`` inside the section's Trace ``<details>`` block and removes
the operative-prose header and bullets.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CJS3_CLUSTER_FILES = [
    "corpus_joint_structure/cjs_03o_oversight_operations.md",
    "corpus_joint_structure/cjs_03p_participation_operations.md",
    "corpus_joint_structure/cjs_03a_accountability_operations.md",
    "corpus_joint_structure/cjs_03c_continuity_operations.md",
    "corpus_joint_structure/cjs_03i_integrative_operations.md",
]

SECTION_HEADING_RE = re.compile(r"^## CJS-3\.\d+\b")
READ_IT_WITH_RE = re.compile(r"^Read it with:\s*$", re.IGNORECASE)
TRACE_SUMMARY_RE = re.compile(r"<summary>.*Trace.*</summary>", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true", help="Report only; do not write files.")
    return parser.parse_args()


def split_sections(lines: list[str]) -> list[list[str]]:
    sections: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        if SECTION_HEADING_RE.match(line):
            if current:
                sections.append(current)
            current = [line]
        elif current:
            current.append(line)
        else:
            sections.append([line])

    if current:
        sections.append(current)
    return sections


def is_routing_bullet(line: str) -> bool:
    return line.startswith("- ") and not line.startswith("- OP-")


def process_section(section: list[str]) -> tuple[list[str], int]:
    if not section or not SECTION_HEADING_RE.match(section[0]):
        return section, 0

    trace_close_idx: int | None = None
    in_trace = False
    read_start: int | None = None
    read_end: int | None = None
    read_bullets: list[str] = []

    for idx, line in enumerate(section):
        stripped = line.strip()

        if stripped == "<details>" and trace_close_idx is None:
            for look in section[idx + 1 : idx + 4]:
                if TRACE_SUMMARY_RE.search(look):
                    in_trace = True
                    break
            continue

        if in_trace and stripped == "</details>":
            trace_close_idx = idx
            in_trace = False
            continue

        if READ_IT_WITH_RE.match(stripped):
            read_start = idx
            continue

        if read_start is not None and read_end is None:
            if is_routing_bullet(line):
                read_bullets.append(line[2:].strip())
                continue
            if not stripped:
                continue
            read_end = idx

    if read_start is None or not read_bullets or trace_close_idx is None:
        return section, 0

    trace_inserts = [f"- Read with: {bullet}" for bullet in read_bullets]
    body_end = read_end if read_end is not None else read_start + 1
    new_section = (
        section[:trace_close_idx]
        + trace_inserts
        + section[trace_close_idx:read_start]
        + section[body_end:]
    )
    return new_section, 1


def relocate_file(path: Path, dry_run: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    moved = 0
    out_lines: list[str] = []

    for section in split_sections(lines):
        new_section, count = process_section(section)
        out_lines.extend(new_section)
        moved += count

    if moved and not dry_run:
        path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    return moved


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    total = 0

    for rel in CJS3_CLUSTER_FILES:
        path = root / rel
        count = relocate_file(path, args.dry_run)
        if count:
            action = "would move" if args.dry_run else "moved"
            print(f"{rel}: {action} {count} Read it with block(s)")
        total += count

    if total == 0:
        print("No operative Read it with blocks found.")
        return 0

    if args.dry_run:
        print(f"Dry run: {total} block(s) would be relocated.")
    else:
        print(f"Relocated {total} Read it with block(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
