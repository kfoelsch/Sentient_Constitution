#!/usr/bin/env python3
"""Renumber Chapter Six §4 → §3; §4.0 → §3.1; §4.1 → §3.2; §4.2 → §3.3; §4.3 → §3.4."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH06 = ROOT / "core_06-06_standing_assessment.md"

ANCHOR_REMAP = {
    "4-primary-axis-categories-slot-grammar-and-defaults": "3-primary-axis-categories-slot-grammar-and-defaults",
    "40-slot-grammar-and-display-labels": "31-slot-grammar-and-display-labels",
    "401-what-the-slot-grammar-does": "311-what-the-slot-grammar-does",
    "402-table-1-slot-display-labels": "312-table-1-slot-display-labels",
    "403-how-to-read-table-1": "313-how-to-read-table-1",
    "41-constitutional-outcome-baseline-for-slots": "32-constitutional-outcome-baseline-for-slots",
    "42-primary-category-defaults-and-lequ-slot-baseline": "33-primary-category-defaults-and-lequ-slot-baseline",
    "43-violation-axis-rules-violation-nature-adverse-findings-and-severity": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
}

HEADING_REMAP = [
    ("### 4. Primary axis categories, slot grammar, and defaults", "### 3. Primary axis categories, slot grammar, and defaults"),
    ("#### 4.0 Slot grammar and display labels", "#### 3.1 Slot grammar and display labels"),
    ("##### 4.0.1 What the slot grammar does", "##### 3.1.1 What the slot grammar does"),
    ("##### 4.0.2 Table 1 — slot display labels", "##### 3.1.2 Table 1 — slot display labels"),
    ("##### 4.0.3 How to read Table 1", "##### 3.1.3 How to read Table 1"),
    ("#### 4.1 LEQU baseline — measuring impact in lifetime-equivalent units", "#### 3.2 LEQU baseline — measuring impact in lifetime-equivalent units"),
    ("#### 4.2 Primary category defaults — how the nine slots map to real-world contributions and violations", "#### 3.3 Primary category defaults — how the nine slots map to real-world contributions and violations"),
    ("#### 4.3 Accountability measure — Violation Axis rules (adverse findings and severity)", "#### 3.4 Accountability measure — Violation Axis rules (adverse findings and severity)"),
]

CROSS_FILE = [
    ("Chapter Six §4.0", "Chapter Six §3.1"),
    ("Chapter Six §4.1", "Chapter Six §3.2"),
    ("Chapter Six §4.2", "Chapter Six §3.3"),
    ("Chapter Six §4.3", "Chapter Six §3.4"),
    ("Chapter Six — §4.0", "Chapter Six — §3.1"),
    ("Chapter Six — §4.1", "Chapter Six — §3.2"),
    ("Chapter Six — §4.2", "Chapter Six — §3.3"),
    ("Chapter Six — §4.3", "Chapter Six — §3.4"),
    ("Chapter Six — section 4.2", "Chapter Six — section 3.3"),
    ("Chapter Six — section 4.3", "Chapter Six — section 3.4"),
    ("Chapter Six section 4.3", "Chapter Six section 3.4"),
    ("Chapter Six section 4.2", "Chapter Six section 3.3"),
    ("Chapter Six section 4.1", "Chapter Six section 3.2"),
    ("Chapter Six section 4.0", "Chapter Six section 3.1"),
    ("sections 4.2** and **4.3", "sections 3.3** and **3.4"),
    ("sections **4.2** and **4.3", "sections **3.3** and **3.4"),
    ("under Chapter Six section 4.3", "under Chapter Six section 3.4"),
    (
        "The Violation Axis remains a separate slot display scale under Chapter Six section 4.3",
        "The Violation Axis remains a separate slot display scale under Chapter Six section 3.4",
    ),
    (
        "V(s)` weights are ordinal analytics for verified constitutional loss under core **§4.1**.",
        "V(s)` weights are ordinal analytics for verified constitutional loss under core **§3.2**.",
    ),
    ("do not replace **section 4.3** severity typing", "do not replace **section 3.4** severity typing"),
    ("(*sections **1–4**, including", "(*sections **1–3**, including"),
    ("Chapter Six **§4.1**", "Chapter Six **§3.2**"),
    ("Chapter Six **§4.3**", "Chapter Six **§3.4**"),
    ("Chapter Six **§§4.2–4.3**", "Chapter Six **§§3.3–3.4**"),
    ("Chapter Six **§3.5** and **§4.3**", "Chapter Six **§2.3.2** and **§3.4**"),
    (
        "Chapter Six **§3.5** and violation classification rules are in Chapter Six **§4.3**",
        "Chapter Six **§2.3.2** and violation classification rules are in Chapter Six **§3.4**",
    ),
    (
        "canonical Axis II classification rules are in Chapter Six **§4.3** and **§5**",
        "canonical Axis II classification rules are in Chapter Six **§3.4** and [Chapter Seven **§5**](core_07-07_standing_integration.md#8-enforcement-realism-anchors)",
    ),
    (
        "[§4.1](core_06-06_standing_assessment.md#42-primary-category-defaults-and-lequ-slot-baseline)",
        "[§3.3](core_06-06_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline)",
    ),
    (
        "[§4.3](core_06-06_standing_assessment.md#43-violation-axis-rules-violation-nature-adverse-findings-and-severity)",
        "[§3.4](core_06-06_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)",
    ),
    (
        "[§4.3, Formal Non-Compliance](core_06-06_standing_assessment.md#41-formal-non-compliance)",
        "[§3.4, Formal Non-Compliance](core_06-06_standing_assessment.md#41-formal-non-compliance)",
    ),
    (
        "[§4.3, Duty-Based or Negligent-Harm Violation](core_06-06_standing_assessment.md#44-duty-based-or-negligent-harm-violation)",
        "[§3.4, Duty-Based or Negligent-Harm Violation](core_06-06_standing_assessment.md#44-duty-based-or-negligent-harm-violation)",
    ),
    (
        "verified violation assessment from **section 4.2** into **standing locks**",
        "verified violation assessment from **Chapter Six section 3.3** into **standing locks**",
    ),
    (
        "It supplements the primary Violation Axis ladder in **[§4.3](core_06-06_standing_assessment.md#43-violation-axis-rules-violation-nature-adverse-findings-and-severity)**. It does not replace the **section 4.3** severity ladder, **section 4.2**,",
        "It supplements the primary Violation Axis ladder in **[§3.4](core_06-06_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)**. It does not replace the **Chapter Six section 3.4** severity ladder, **Chapter Six section 3.3**,",
    ),
    (
        "[**section 3**](core_06-06_standing_assessment.md#42-primary-category-defaults-and-lequ-slot-baseline)",
        "[**section 3.3**](core_06-06_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline)",
    ),
]

CH06_PROSE = [
    ("sections **1–4**", "sections **1–3**"),
    ("sections **1–4***", "sections **1–3***"),
    ("Triad / Aims map for §2 and §4", "Triad / Aims map for §2 and §3"),
    ("How §2 and §4 relate", "How §2 and §3 relate"),
    ("Part of §4", "Part of §3"),
    ("§§4.0–4.2", "§§3.1–3.3"),
    ("§§4.0–4.3", "§§3.1–3.4"),
    ("§§4.2–4.3", "§§3.3–3.4"),
    ("§4.0", "§3.1"),
    ("§4.1", "§3.2"),
    ("§4.2", "§3.3"),
    ("§4.3", "§3.4"),
    ("[§4](#3-primary-axis-categories-slot-grammar-and-defaults)", "[§3](#3-primary-axis-categories-slot-grammar-and-defaults)"),
    ("section 4.0", "section 3.1"),
    ("section 4.1", "section 3.2"),
    ("section 4.2", "section 3.3"),
    ("section 4.3", "section 3.4"),
    ("Sections 4.0–4.2", "Sections 3.1–3.3"),
    ("Section 4.3", "Section 3.4"),
    ("Section 4.0", "Section 3.1"),
    ("before section 4 categories", "before section 3 categories"),
    ("section 4 categories", "section 3 categories"),
    ("section 4 does not", "section 3 does not"),
    ("section 4 **measures**", "section 3 **measures**"),
    ("so **section 4** can measure", "so **section 3** can measure"),
    ("Sections 4.1 through 4.3", "Sections 3.2 through 3.4"),
    ("sections 4.2 and 4.3", "sections 3.3 and 3.4"),
    ("sections 4.2 and 4.3,", "sections 3.3 and 3.4,"),
]

CH7_GUARDS = [
    ("Chapter Seven §4.1", "@@CH7-41@@"),
    ("Chapter Seven §4.2", "@@CH7-42@@"),
    ("Chapter Seven §4.3", "@@CH7-43@@"),
    ("Chapter Seven section 4.3", "@@CH7-S43@@"),
    ("Chapter Seven section 4.2", "@@CH7-S42@@"),
    ("Chapter Seven section 4", "@@CH7-S4@@"),
    ("§§4.1–4.3 — mechanics", "@@CH7-SS413@@"),
]


def remap_anchors(text: str) -> str:
    for old, new in ANCHOR_REMAP.items():
        text = text.replace(f'id="{old}"', f'id="{new}"')
        text = text.replace(f"#{old}", f"#{new}")
    return text


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        text = text.replace(old, new)
    return text


def renumber_ch06(text: str) -> str:
    for old, guard in CH7_GUARDS:
        text = text.replace(old, guard)
    text = remap_anchors(text)
    for old, new in HEADING_REMAP:
        text = text.replace(old, new)
    text = apply_replacements(text, CH06_PROSE)
    text = re.sub(r"\[§4\.3, ([^\]]+)\]", r"[§3.4, \1]", text)
    for old, guard in CH7_GUARDS:
        text = text.replace(guard, old)
    return text


def update_file(path: Path) -> bool:
    original = path.read_text()
    if path == CH06:
        updated = renumber_ch06(original)
    else:
        updated = apply_replacements(original, CROSS_FILE)
        updated = remap_anchors(updated)
    if updated != original:
        path.write_text(updated)
        return True
    return False


def main() -> None:
    changed: list[str] = []
    if update_file(CH06):
        changed.append(str(CH06.relative_to(ROOT)))

    for path in ROOT.rglob("*"):
        if path == CH06 or "archive/" in str(path) or "tools/ch06_renumber" in str(path):
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        if update_file(path):
            changed.append(str(path.relative_to(ROOT)))

    print(f"Renumbered Chapter Six §4→§3 in {len(changed)} file(s).")
    for name in sorted(changed):
        print(f"  - {name}")


if __name__ == "__main__":
    main()
