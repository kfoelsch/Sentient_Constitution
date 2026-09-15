#!/usr/bin/env python3
"""Remove emphasis that has stopped carrying meaning in the CS protocol files.

Several CS files bold so much that emphasis conveys nothing. The clearest case
is a bolded sentence-opening pronoun or bare verb -- ``**They** include ...``,
``**It** must ...``, ``**Apply** adversarial stress ...`` -- which appears to
have come from mechanically splitting long sentences and bolding whatever word
started each fragment. Those words are not defined terms and gain nothing from
emphasis.

Only a fixed list of function words and bare imperatives is unbolded, and only
where the word opens a sentence. Bold spans covering defined terms, class
labels, tier names, and multi-word phrases are left untouched, because there
the emphasis is doing real work.

This changes formatting only; no word is added, removed, or reordered.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Sentence-opening words that carry no emphasis value.
OPENERS = (
    "They", "It", "That", "Those", "These", "This", "Its", "Their",
    "Also", "Alternatively", "Additionally", "Apply", "Provide", "Use",
    "Design", "Assess", "Justify", "Periodically", "Preference", "Ensure",
    "Maintain", "Include", "Track", "Publish", "Record", "Document",
)

# Bold span at the start of a line, or just after a sentence end.
PATTERN = re.compile(
    r"(?P<lead>^|(?<=[.;:!?])\s|(?<=—)\s|(?<=\()|(?<=- ))"
    r"\*\*(?P<word>" + "|".join(OPENERS) + r")\*\*(?P<tail>\s|$)",
    re.M,
)


def debold(text: str) -> tuple[str, int]:
    out_lines: list[str] = []
    count = 0
    fenced = False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if fenced or line.lstrip().startswith("|"):
            out_lines.append(line)
            continue
        new_line, hits = PATTERN.subn(
            lambda m: f"{m.group('lead')}{m.group('word')}{m.group('tail')}", line
        )
        count += hits
        out_lines.append(new_line)
    result = "\n".join(out_lines)
    if text.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result, count


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
    base = root / args.layer
    if not base.is_dir():
        print(f"No such layer: {args.layer}", file=sys.stderr)
        return 2

    paths = [base / args.file] if args.file else sorted(base.glob("*.md"))
    total = changed = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        new_text, count = debold(text)
        if not count:
            continue
        changed += 1
        total += count
        rel = path.relative_to(root).as_posix()
        print(f"{'wrote' if args.write else 'would unbold'} {rel}: {count}")
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    print(f"\n{total} spans across {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
