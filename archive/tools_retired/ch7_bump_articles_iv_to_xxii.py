#!/usr/bin/env python3
"""
Bump Sentient Constitution Chapter Seven references: Article IX..XXII -> V..XXIII.
Leaves Article V, II, III (and III-*) unchanged. Uses placeholders to avoid chaining.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROMANS = {
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX",
    21: "XXI",
    22: "XXII",
    23: "XXIII",
}


def bump_text(text: str) -> str:
    # Longest roman numerals first within same length class — process XXII before XXI, etc.
    for n in range(22, 3, -1):
        old = ROMANS[n]
        token = f"«A{n}»"
        # Hyphenated subsection refs (must precede bare ### Article IX: handled below)
        text = text.replace(f"Article {old}-", f"Article {token}-")
        text = text.replace(f"article {old}-", f"article {token}-")
        text = text.replace(f"Articles {old}-", f"Articles {token}-")
        text = text.replace(f"Art {old}-", f"Art {token}-")
        text = text.replace(f"art {old}-", f"art {token}-")
    for n in range(22, 3, -1):
        old = ROMANS[n]
        new = ROMANS[n + 1]
        token = f"«A{n}»"
        text = text.replace(f"Article {token}-", f"Article {new}-")
        text = text.replace(f"article {token}-", f"article {new}-")
        text = text.replace(f"Articles {token}-", f"Articles {new}-")
        text = text.replace(f"Art {token}-", f"Art {new}-")
        text = text.replace(f"art {token}-", f"art {new}-")
    # Top-level headings ### Article IX: through ### Article XX:
    for n in range(22, 3, -1):
        old = ROMANS[n]
        token = f"«A{n}»"
        text = text.replace(f"### Article {old}:", f"### Article {token}:")
    for n in range(22, 3, -1):
        new = ROMANS[n + 1]
        token = f"«A{n}»"
        text = text.replace(f"### Article {token}:", f"### Article {new}:")
    return text


def main() -> None:
    paths = list(ROOT.rglob("*.md"))
    for path in sorted(paths):
        if "/.git/" in str(path):
            continue
        raw = path.read_text(encoding="utf-8")
        out = bump_text(raw)
        if out != raw:
            path.write_text(out, encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
