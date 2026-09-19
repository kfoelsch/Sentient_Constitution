#!/usr/bin/env python3
"""Give every companion section heading an explicit anchor.

``cs_02_a_information_types_and_handling.md`` places an ``<a id="...">`` line
above each heading, so a citation keeps working even if the heading text is
later reworded. Sections added or promoted elsewhere in the systems corpus
inherited the auto-generated slug instead.

The anchor written here is the slug the renderer already derives from the
heading text, so nothing that currently resolves changes; the link simply stops
depending on the wording. Headings that already carry an anchor are left alone.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING_RE = re.compile(r"^(?P<hashes>#{2,3})\s+(?P<title>.+?)\s*$")
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>\s*$')


def slug(text: str) -> str:
    """The slug GitHub derives from heading text."""
    lowered = text.lower().replace("—", " ").replace("–", " ").replace("/", " ")
    kept = re.sub(r"[^\w\s-]", "", lowered)
    return re.sub(r"[-\s]+", "-", kept).strip("-")


def annotate(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    added = 0
    fenced = False
    seen: set[str] = set()

    for index, line in enumerate(lines):
        if line.startswith("```"):
            fenced = not fenced
        match = None if fenced else HEADING_RE.match(line)
        if not match:
            out.append(line)
            continue

        previous = lines[index - 1].strip() if index else ""
        if ANCHOR_RE.match(previous):
            out.append(line)
            continue

        name = slug(match.group("title"))
        # A duplicate id would make the link ambiguous, so leave the second
        # heading on its auto-generated slug.
        if not name or name in seen:
            out.append(line)
            continue
        seen.add(name)
        out.append(f'<a id="{name}"></a>')
        out.append(line)
        added += 1

    result = "\n".join(out)
    if not result.endswith("\n"):
        result += "\n"
    return result, added


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--layer", default="corpus_systems")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    base = root / args.layer
    if not base.is_dir():
        print(f"No such layer: {args.layer}", file=sys.stderr)
        return 2

    total = changed = 0
    for path in sorted(base.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        new_text, added = annotate(text)
        if not added:
            continue
        changed += 1
        total += added
        rel = path.relative_to(root).as_posix()
        print(f"{'wrote' if args.write else 'would anchor'} {rel}: {added}")
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    print(f"\n{total} anchors across {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
