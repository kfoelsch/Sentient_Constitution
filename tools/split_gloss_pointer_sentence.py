#!/usr/bin/env python3
"""Break the three-clause pointer sentence at the end of companion glosses.

The Phase 3 glosses close with one semicolon-chained sentence naming the shared
floor, the constitutional home, and the local addition. At sixty-plus words it
is the longest sentence in most of these files, and it is the last thing a
reader sees before the rules start. This splits it into three plain sentences.

Glosses are non-operative, so no obligation moves. The wording of each named
source is carried across unchanged.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Each clause of the chain becomes its own sentence. Applied in order, so a
# three-clause gloss splits twice and a two-clause gloss once.
SPLITS = (
    (
        re.compile(r"; constitutional meaning lives in "),
        ". The constitutional meaning sits in ",
    ),
    (
        re.compile(r"; this file states what each institution must "),
        ". What this file adds is local: what each institution must ",
    ),
)


def rewrite(text: str) -> tuple[str, int]:
    total = 0
    for pattern, replacement in SPLITS:
        text, count = pattern.subn(replacement, text)
        total += count
    return text, total


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    changed = 0
    for subdir in ("corpus_institutions", "corpus_forum", "corpus_systems",
                   "corpus_joint_structure"):
        base = root / subdir
        if not base.is_dir():
            continue
        for path in sorted(base.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            new_text, count = rewrite(text)
            if not count:
                continue
            changed += 1
            rel = path.relative_to(root).as_posix()
            print(f"{'wrote' if args.write else 'would split'} {rel} ({count})")
            if args.write:
                path.write_text(new_text, encoding="utf-8")
    print(f"\n{changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
