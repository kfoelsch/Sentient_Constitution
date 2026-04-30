#!/usr/bin/env python3
"""Renumber Chapter Seven in core from Info-Sphere (Article IX) through EOF: subsections III..XXI -> IV..XXII, ### Articles III..XXI -> VI..XXII, leave ### Article IX: Info unchanged."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "core_constitution.md"
text = path.read_text(encoding="utf-8")
marker = "### Article IX: Info-Sphere Integrity"
idx = text.find(marker)
if idx < 0:
    raise SystemExit(f"marker not found: {marker}")
head, tail = text[:idx], text[idx:]

ROMANS = {
    3: "III",
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
}

# Subsections Article VIII- through Article XIX-
for n in range(21, 2, -1):
    o, ne = ROMANS[n], ROMANS[n + 1]
    tail = tail.replace(f"Article {o}-", f"Article {ne}-")
    tail = tail.replace(f"article {o}-", f"article {ne}-")

# ### Article III through XXI (not IV — Info stays Article IX)
for n in range(21, 4, -1):
    o, ne = ROMANS[n], ROMANS[n + 1]
    tail = tail.replace(f"### Article {o}:", f"### Article {ne}:")

tail = tail.replace(
    "### Article IX: Right to Reliable and Trustworthy Systems",
    "### Article III: Right to Reliable and Trustworthy Systems",
    1,
)

path.write_text(head + tail, encoding="utf-8", newline="\n")
print("ok")
