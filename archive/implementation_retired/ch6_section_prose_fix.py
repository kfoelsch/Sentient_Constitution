#!/usr/bin/env python3
"""Disabled one-shot prose migration script for the pre-split Chapter Six layout.

Chapter Six now lives in core_06-06_standing_assessment.md and
core_07-07_standing_integration.md. Do not rerun this historical fixer.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
raise SystemExit(
    "Disabled: Chapter Six is split. Edit core_06-06_standing_assessment.md "
    "and core_07-07_standing_integration.md directly."
)
p = ROOT / "core_06-06_standing_assessment.md"
t = p.read_text(encoding="utf-8")

for i in range(8, 0, -1):
    t = t.replace(f"sections 2.{i}", f"sections 3.{i}")
    t = t.replace(f"section 2.{i}", f"section 3.{i}")

repls = [
    ("2.1 through 2.3", "3.1 through 3.3"),
    ("2.1 through 2.4", "3.1 through 3.4"),
    ("2.2 through 2.4", "3.2 through 3.4"),
    ("2.2 and 2.3", "3.2 and 3.3"),
    ("2.4 and 2.6", "3.4 and 3.6"),
    ("2.4 and 2.7", "3.4 and 3.7"),
    ("2.4 through 2.7", "3.4 through 3.7"),
    ("2.6 and 2.7", "3.6 and 3.7"),
    ("§2.4–2.7", "§3.4–3.7"),
    ("§2.4–2.6", "§3.4–3.6"),
    # Violation severity / typing (already wrongly says 3.x in some places = Axis I overlap)
]
for a, b in repls:
    t = t.replace(a, b)

# Non-compliance ladder references (violation) — use 4.x
t = t.replace("non-compliance ladder** severity under **sections 3.1 through 3.4**", "non-compliance ladder** severity under **sections 4.1 through 4.4**")
t = t.replace("legal-constitutional typing under **sections 3.5 through 3.7**", "legal-constitutional typing under **sections 4.5 through 4.7**")
t = t.replace("**sections 3.5 through 3.7**", "**sections 4.5 through 4.7**")
t = t.replace("sections 3.5 through 3.7", "sections 4.5 through 4.7")

# Concurrent/hybrid: section 3.8 on Axis II -> 4.8 (pattern: co-occur across concurrent **section 3.8**)
t = t.replace("concurrent types (**section 3.8**)", "concurrent types (**section 4.8**)")
t = t.replace("where **section 3.8** applies", "where **section 4.8** applies")
t = t.replace("including **non-compliance ladder** severity under **sections 3.1 through 3.4**", "including **non-compliance ladder** severity under **sections 4.1 through 4.4**")

# Verified inputs parenthetical
t = t.replace("(**section 1**). **Routing**", "(**section 2**). **Routing**")
t = t.replace("**contribution state** under **section 2**; **adverse**", "**contribution state** under **section 3**; **adverse**")
t = t.replace("contribution state** under **section 2** and may", "contribution state** under **section 3** and may")
t = t.replace("recognition under **section 2**.", "recognition under **section 3**.")

p.write_text(t, encoding="utf-8")
print("ok")
