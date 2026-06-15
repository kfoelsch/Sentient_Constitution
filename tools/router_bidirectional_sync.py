#!/usr/bin/env python3
"""Insert standardized **Router read:** blocks for CJS-2.1 bidirectional routing."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from router_table_lib import (
    ROUTER_READ_RE,
    build_section_index,
    extract_section,
    load_router_rows,
    primary_owner_line,
    read_with_line,
)

LEGACY_PRIMARY_RE = re.compile(
    r"^.*(?:\*\*Joint read:\*\*|for cross-implementation routing, read this section with).*\*\*CJS-R[^*]+\*\*.*$",
    re.I | re.M,
)


def repair_heading_markdown(content: str) -> str:
    content = content.replace("---##", "---\n\n##")
    content = re.sub(r"([.!?])(###)", r"\1\n\n\2", content)
    content = re.sub(r"(\S) (###)", r"\1\n\n\2", content)
    content = re.sub(r"(<br>\n)\n{3,}", r"\1\n\n", content)
    return content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply updates to corpus files.",
    )
    return parser.parse_args()


def after_widget_insert_index(section_text: str) -> int:
    parts = section_text.split("</details>", 2)
    if len(parts) < 3:
        return 0
    prefix = parts[0] + "</details>" + parts[1] + "</details>"
    tail = parts[2]
    match = re.search(r"\n*<br>\s*\n*", tail)
    if match:
        return len(prefix) + match.end()
    return len(prefix)


def strip_router_lines(section_text: str) -> str:
    lines = section_text.splitlines()
    kept: list[str] = []
    for line in lines:
        if ROUTER_READ_RE.match(line):
            continue
        if LEGACY_PRIMARY_RE.match(line):
            continue
        kept.append(line)
    return "\n".join(kept)


def apply_router_lines(section_text: str, router_lines: list[str]) -> str:
    cleaned = strip_router_lines(section_text)
    if not router_lines:
        return cleaned
    block = "\n".join(router_lines) + "\n\n"
    insert_at = after_widget_insert_index(cleaned)
    tail = cleaned[insert_at:]
    return cleaned[:insert_at] + block + tail.lstrip("\n")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    rows = load_router_rows(root)
    index = build_section_index(root)

    primary_lines: dict[str, list[str]] = defaultdict(list)
    read_with_lines: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        for attach in row.primary_attach:
            line = primary_owner_line(row)
            if line not in primary_lines[attach]:
                primary_lines[attach].append(line)
        primary_label = (
            row.primary_attach[0] if len(row.primary_attach) == 1 else ", ".join(row.primary_attach)
        )
        for attach in row.read_with_attach:
            if attach in row.primary_attach:
                continue
            line = read_with_line(row)
            if line not in read_with_lines[attach]:
                read_with_lines[attach].append(line)

    all_sections = sorted(set(primary_lines) | set(read_with_lines))
    changed_files: dict[Path, str] = {}

    for section_id in all_sections:
        path = index.get(section_id)
        if not path:
            print(f"skip missing section {section_id}")
            continue
        original = changed_files.get(path, path.read_text(encoding="utf-8"))
        section_text = extract_section(original, section_id)
        if not section_text:
            print(f"skip unextracted section {section_id}")
            continue
        lines = sorted(primary_lines.get(section_id, []) + read_with_lines.get(section_id, []))
        updated_section = apply_router_lines(section_text, lines)
        if updated_section == section_text:
            continue
        changed_files[path] = original.replace(section_text, updated_section, 1)
        print(f"update {path.relative_to(root)} :: {section_id} ({len(lines)} router lines)")

    if args.write:
        for path, content in changed_files.items():
            path.write_text(repair_heading_markdown(content), encoding="utf-8")
        print(f"Wrote {len(changed_files)} files.")
    else:
        print(f"Dry run: {len(changed_files)} files would change. Pass --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
