#!/usr/bin/env python3
"""Promote CS numeric headings to CS-n.m form and drop self-only section Traces.

Keeps existing ``<a id>`` aliases and adds a slug id for the new heading.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING_RE = re.compile(r"^(#{2,3})\s+(\d+(?:\.\d+)*)\.\s+(.*)$")
SELF_TRACE_BLOCK_RE = re.compile(
    r"\n<details>\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\n\n"
    r"- Read with: \*\*CS-(\d+)\*\*; \*\*CS-\1 §(\d+)\*\*\.\n\n"
    r"</details>\n\n(?:<br>\n\n)?",
)
FAMILY_FROM_NAME = re.compile(r"^cs_(\d+)")
SKIP = {
    "cs_00_registry_and_reading_rules.md",
    "cs_01_scope_purpose_identifier_rules.md",
}


def family_id(path: Path) -> str | None:
    match = FAMILY_FROM_NAME.match(path.name)
    return f"CS-{int(match.group(1))}" if match else None


def slug_id(family: str, number: str, title: str) -> str:
    token = f"{family}.{number} {title}".lower()
    return re.sub(r"[^a-z0-9]+", "-", token).strip("-")


def promote_text(text: str, family: str) -> str:
    text = SELF_TRACE_BLOCK_RE.sub("\n", text)
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        match = HEADING_RE.match(line.rstrip("\n"))
        if not match:
            out.append(line)
            continue
        hashes, number, title = match.groups()
        if title.startswith(f"{family}."):
            out.append(line)
            continue
        new_id = slug_id(family, number, title)
        recent = "".join(out[-4:])
        if f'id="{new_id}"' not in recent:
            out.append(f'<a id="{new_id}"></a>\n')
        newline = "\n" if line.endswith("\n") else ""
        out.append(f"{hashes} {family}.{number} {title}{newline}")
    return "".join(out)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    changed = 0
    for path in sorted((root / "corpus_systems").glob("cs_*.md")):
        if path.name in SKIP:
            continue
        family = family_id(path)
        if not family:
            continue
        original = path.read_text(encoding="utf-8")
        updated = promote_text(original, family)
        if updated == original:
            continue
        changed += 1
        rel = path.relative_to(root).as_posix()
        if args.write:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {rel}")
        else:
            print(f"would update {rel}")
    print(f"{'Wrote' if args.write else 'Would update'} {changed} CS file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
