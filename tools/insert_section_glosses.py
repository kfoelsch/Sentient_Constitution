#!/usr/bin/env python3
"""Add the missing ``*In plain terms:*`` line to companion sections.

Every core file opens each section with a one-line plain-language gloss, and
the companion files gained the same convention for the sections that existed at
the time. Sections created or promoted afterwards have none, so a reader
arriving from a citation meets the operative text with no orientation.

Glosses are written per section rather than generated, because a generated
summary of a rule tends to restate its hardest sentence. They are non-operative
and add no obligation.

Usage: ``python3 tools/insert_section_glosses.py --file <name> --write``.
Glosses live in ``tools/section_glosses.json`` keyed by file name, then by the
heading text without its number.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOSSES = Path(__file__).resolve().with_name("section_glosses.json")

HEADING_RE = re.compile(r"^##\s+(?:\d+\.\s+)?(?P<title>.+?)\s*$")


def insert(text: str, glosses: dict[str, str]) -> tuple[str, int, list[str]]:
    lines = text.splitlines()
    out: list[str] = []
    used: set[str] = set()
    added = 0

    index = 0
    while index < len(lines):
        line = lines[index]
        out.append(line)
        index += 1

        match = HEADING_RE.match(line)
        if not match:
            continue
        title = match.group("title")
        gloss = glosses.get(title)
        if gloss is None:
            continue
        used.add(title)

        # The gloss belongs at the first line a reader actually reads, which
        # is after any Trace or definitions widget the section carries.
        cursor, depth = index, 0
        while cursor < len(lines):
            stripped = lines[cursor].strip()
            if "<details>" in stripped:
                depth += 1
            elif "</details>" in stripped:
                depth = max(0, depth - 1)
            elif depth == 0 and stripped and stripped != "<br>" and not stripped.startswith("<a id="):
                break
            cursor += 1

        if cursor < len(lines) and lines[cursor].strip().startswith("*In plain terms"):
            continue

        out.extend(lines[index:cursor])
        while out and not out[-1].strip():
            out.pop()
        out.append("")
        out.append(f"*In plain terms: {gloss}*")
        out.append("")
        added += 1
        index = cursor

    result = "\n".join(out)
    if not result.endswith("\n"):
        result += "\n"
    return result, added, sorted(set(glosses) - used)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--layer", default="corpus_systems")
    parser.add_argument("--file", help="Restrict to one file name.")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    table = json.loads(GLOSSES.read_text(encoding="utf-8"))
    names = [args.file] if args.file else sorted(table)
    status = 0

    for name in names:
        glosses = table.get(name)
        if glosses is None:
            print(f"no glosses listed for {name}", file=sys.stderr)
            return 2
        path = root / args.layer / name
        text = path.read_text(encoding="utf-8")
        new_text, added, unmatched = insert(text, glosses)
        print(f"{'wrote' if args.write else 'would gloss'} {name}: {added}")
        for title in unmatched:
            print(f"  NO SUCH SECTION: {title}", file=sys.stderr)
            status = 1
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
