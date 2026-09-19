#!/usr/bin/env python3
"""Split long Chapter Three - O:/- E:/- C: lines at the first '. ' boundary.

Default word threshold is 25 to match readability_audit long-sentence default.
"""
from __future__ import annotations

import argparse
import pathlib
import re

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
PREFIX_RE = re.compile(r"^(- [OEC]: )(.*)$")


def word_count(s: str) -> int:
    return len(WORD_RE.findall(s))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--min-words",
        type=int,
        default=25,
        help="Minimum words in the full O/E/C line to attempt a split (default: 25).",
    )
    p.add_argument(
        "--min-tail-words",
        type=int,
        default=5,
        help="Minimum words required in the segment after the first '. ' (default: 5).",
    )
    args = p.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]
    path = root / "core_constitution.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_ch3 = False

    for line in lines:
        if line.startswith("## CHAPTER THREE:"):
            in_ch3 = True
            out.append(line)
            continue
        if line.startswith("## CHAPTER FOUR:"):
            in_ch3 = False
            out.append(line)
            continue

        m = PREFIX_RE.match(line)
        if in_ch3 and m and not line.startswith("  "):
            prefix, rest = m.group(1), m.group(2)
            wc = word_count(rest)
            if wc >= args.min_words and ". " in rest:
                first, second = rest.split(". ", 1)
                if word_count(first) >= 4 and word_count(second) >= args.min_tail_words:
                    tail = first.rstrip()
                    if not any(tail.endswith(s) for s in ("e.g", "i.e", "etc")):
                        out.append(prefix + first + ".")
                        out.append("  " + second)
                        continue
            # No sentence break: split at first '; ' when both sides stay substantive.
            if wc >= 26 and "; " in rest and ". " not in rest:
                first, second = rest.split("; ", 1)
                if word_count(first) >= 6 and word_count(second) >= args.min_tail_words:
                    out.append(prefix + first + ";")
                    out.append("  " + second)
                    continue
        out.append(line)

    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
