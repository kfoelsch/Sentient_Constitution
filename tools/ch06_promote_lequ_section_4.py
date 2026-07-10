#!/usr/bin/env python3
"""Promote Chapter Eight LEQU from Chapter One §8.2 to top-level §4; renumber §3.3→§5, §3.4→§6."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH06 = ROOT / "core_08-08_standing_assessment.md"

# Visible heading / section-number renames (longest match first in application order)
CH06_HEADINGS = [
    ("#### 3.4 Accountability measure", "#### 6. Accountability measure"),
    ("#### 3.3 Primary category defaults", "#### 5. Primary category defaults"),
    ("#### 3.2 LEQU baseline", "### 4. LEQU baseline"),
    ("#### 3.1 Slot grammar", "#### 3.1 Slot grammar"),  # unchanged label; section 3 narrows
    ("### 3. Primary axis categories, slot grammar, and defaults", "### 3. Slot grammar and display labels"),
]

CH06_PROSE = [
    ("sections **1–3**", "sections **1–6**"),
    ("sections **1–3***", "sections **1–6***"),
    ("(*§Chapter One §8.1–3.4 — slot grammar, LEQU constitutional-outcome baseline, primary category defaults, Contribution Axis rules, and Violation Axis rules*)",
     "(*§§3–6 — slot grammar, LEQU constitutional-outcome baseline, primary category defaults, Contribution Axis rules, and Violation Axis rules*)"),
    ("**Triad / Aims map for §2 and §3:**", "**Triad / Aims map for §2 and §§3–6:**"),
    ("[§11](#3-primary-axis-categories-slot-grammar-and-defaults) slot grammar and axis rules",
     "[§§3–6](#3-slot-grammar-and-display-labels) slot grammar, LEQU baseline, and axis categories"),
    ("[§Chapter One §8.1–3.3](#3-primary-axis-categories-slot-grammar-and-defaults) | **Classification layer** — slot grammar, LEQU baseline, Contribution Axis bands",
     "[§§3–5](#3-slot-grammar-and-display-labels) | **Classification layer** — slot grammar, LEQU baseline, Contribution Axis bands"),
    ("[§3.4](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) | **Classification layer** — Violation Axis severity ladder",
     "[§5](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) | **Classification layer** — Violation Axis severity ladder"),
    ("**How §2 and §3 relate:**", "**How §2 and §§3–6 relate:**"),
    ("[§11](#3-primary-axis-categories-slot-grammar-and-defaults) states *how verified standing records map to axis categories* — Flourishing-side contribution under **§Chapter One §8.1–3.3**, Accountability-side violation under **§3.4**. Section 2 must be satisfied before section 3 categories bind; section 3 does not merge",
     "[§§3–6](#3-slot-grammar-and-display-labels) state *how verified standing records map to axis categories* — Flourishing-side contribution under **§§3–5**, Accountability-side violation under **§5**. Section 2 must be satisfied before section 3 categories bind; sections 3–6 do not merge"),
    ("[§11](#3-primary-axis-categories-slot-grammar-and-defaults) (*slot grammar, primary axis categories, and LEQU slot baseline*);",
     "[§§3–6](#3-slot-grammar-and-display-labels) (*slot grammar, LEQU baseline, primary axis categories*);"),
    ("[§11](#3-primary-axis-categories-slot-grammar-and-defaults) (*slot grammar and axis classification — Flourishing measure at **§Chapter One §8.1–3.3**, Accountability measure at **§3.4***);",
     "[§§3–6](#3-slot-grammar-and-display-labels) (*slot grammar, LEQU baseline, and axis classification — Flourishing measure at **§§3–5**, Accountability measure at **§5***);"),
    ("so **section 3** can measure", "so **sections 3–6** can measure"),
    ("Part of §3", "Part of §§3–6"),
    ("Section 3 **measures**", "Sections **3–6** **measure**"),
    ("section 3 **measures**", "sections **3–6** **measure**"),
    ("**Sections 3.1–3.3** classify", "**Sections 3–5** classify"),
    ("**Section 3.4** classifies", "**Section 6** classifies"),
    ("**§Chapter One §8.1–3.3** — **oversight**", "**§§3–5** — **oversight**"),
    ("**§3.4** — **accountability**", "**§5** — **accountability**"),
    ("Primary aim(s): **§Chapter One §8.1–3.3**", "Primary aim(s): **§§3–5**"),
    ("**§3.4** — **Accountability**", "**§5** — **Accountability**"),
    ("Sections 3.2 through 3.4 state", "Sections 4 through 6 state"),
    ("section 3.4", "section 6"),
    ("section 3.3", "section 5"),
    ("section 3.2", "section 4"),
    ("section 3.1", "section 3.1"),
    ("sections 3.3 and 3.4", "sections 5 and 6"),
    ("Sections 4.1 through 4.3", "Sections 4.1 through 4.3"),  # Ch7 guard noop
    ("[§Chapter One §8.1–3.3](#31-slot-grammar-and-display-labels)", "[§§3–5](#3-slot-grammar-and-display-labels)"),
    ("[§3.4](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)", "[§5](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)"),
    ("[Chapter One §8.1](#31-slot-grammar-and-display-labels)", "[Chapter One §8.1](#31-slot-grammar-and-display-labels)"),
    ("[Chapter One §8.2](#32-constitutional-outcome-baseline-for-slots)", "[§2](#32-constitutional-outcome-baseline-for-slots)"),
    ("[§11.3](#33-primary-category-defaults-and-lequ-slot-baseline)", "[§4](#33-primary-category-defaults-and-lequ-slot-baseline)"),
    ("[§3.4, ", "[§6, "),
    ("under **section 4.2**", "under **Chapter Nine section 4.2**"),
    ("For this subsection,", "For this section,"),
    ("subordinate to this subsection,", "subordinate to this section,"),
    ("Apply the highest **section 6** level", "Apply the highest **section 6** level"),
    ("under **section 5** and applicable attachments", "under **section 6** and applicable attachments"),
    ("classifies verified **contribution state** under **section 5**.", "classifies verified **contribution state** under **section 5**."),
    ("classifies verified **violation nature** under **section 6**", "classifies verified **violation nature** under **section 6**"),
]

CH7_GUARDS = [
    ("Chapter Nine section 4.3", "@@CH7-S43@@"),
    ("Chapter Nine section 4.2", "@@CH7-S42@@"),
    ("Chapter Nine section 4", "@@CH7-S4@@"),
    ("Chapter Nine §3.3", "@@CH7-43@@"),
    ("Chapter Nine Chapter One §8.2", "@@CH7-42@@"),
    ("Chapter Nine Chapter One §8.1", "@@CH7-41@@"),
    ("Chapter Nine §4", "@@CH7-4@@"),
    ("§Chapter One §8.1–4.3", "@@CH7-SS413@@"),
]

CROSS_FILE = [
    ("Chapter Eight Chapter One §8.2", "Chapter Eight §4"),
    ("Chapter Eight — Chapter One §8.2", "Chapter Eight — §4"),
    ("Chapter Eight section 3.2", "Chapter Eight section 4"),
    ("Chapter Eight — section 3.2", "Chapter Eight — section 4"),
    ("Chapter Eight §3.3", "Chapter Eight §5"),
    ("Chapter Eight — §3.3", "Chapter Eight — §5"),
    ("Chapter Eight section 3.3", "Chapter Eight section 5"),
    ("Chapter Eight — section 3.3", "Chapter Eight — section 5"),
    ("Chapter Eight §3.4", "Chapter Eight §6"),
    ("Chapter Eight — §3.4", "Chapter Eight — §6"),
    ("Chapter Eight section 3.4", "Chapter Eight section 6"),
    ("Chapter Eight — section 3.4", "Chapter Eight — section 6"),
    ("sections 3.3** and **3.4", "sections 5** and **6"),
    ("sections **3.3** and **3.4", "sections **5** and **6"),
    ("Chapter Eight **Chapter One §8.2**", "Chapter Eight **§2**"),
    ("Chapter Eight **§3.4**", "Chapter Eight **§5**"),
    ("Chapter Eight **§§3.3–3.4**", "Chapter Eight **§§5–6**"),
    ("Chapter Eight **§14.3.2** and **§3.4**", "Chapter Eight **§14.3.2** and **§5**"),
    ("canonical Axis II classification rules are in Chapter Eight **§3.4**", "canonical Axis II classification rules are in Chapter Eight **§5**"),
    ("under Chapter Eight section 3.4", "under Chapter Eight section 6"),
    ("under Chapter Eight section 3.3", "under Chapter Eight section 5"),
    ("Chapter Eight section 3.4 severity", "Chapter Eight section 6 severity"),
    ("Chapter Eight section 3.3** into", "Chapter Eight section 5** into"),
    ("Chapter Eight section 3.4** severity", "Chapter Eight section 6** severity"),
    ("Chapter Eight section 3.3**,", "Chapter Eight section 5**,"),
    ("core **Chapter One §8.2**.", "core **§2**."),
    ("core **Chapter One §8.2**", "core **§2**"),
    ("**section 3.4** severity typing", "**section 6** severity typing"),
    ("(*sections **1–3**, including", "(*sections **1–6**, including"),
    ("Chapter Eight **§§2–3**", "Chapter Eight **§§2–6**"),
    ("[§11.3](core_08-08_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline)", "[§4](core_08-08_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline)"),
    ("[§3.4](core_08-08_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)", "[§5](core_08-08_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)"),
    ("[Chapter One §8.2](core_08-08_standing_assessment.md#32-constitutional-outcome-baseline-for-slots)", "[§2](core_08-08_standing_assessment.md#32-constitutional-outcome-baseline-for-slots)"),
    ("[§3.4, Formal Non-Compliance]", "[§6, Formal Non-Compliance]"),
    ("[§3.4, Duty-Based or Negligent-Harm Violation]", "[§6, Duty-Based or Negligent-Harm Violation]"),
    ("Chapter Eight §Chapter One §8.1–3.3 read with Chapter Nine", "Chapter Eight §§3–5 read with Chapter Nine"),
    ("**section 3.1** standing-slot grammar and **section 3.3** primary slot defaults", "**section 3.1** standing-slot grammar and **section 5** primary slot defaults"),
    ("the Chapter Eight **section 3.4** severity ladder", "the Chapter Eight **section 6** severity ladder"),
    ("[§§3–5](#3-slot-grammar-and-display-labels)", "[§§3–5](#3-slot-grammar-and-display-labels)"),
    ("#3-primary-axis-categories-slot-grammar-and-defaults", "#3-slot-grammar-and-display-labels"),
]


def guard_ch7(text: str) -> str:
    for old, guard in CH7_GUARDS:
        text = text.replace(old, guard)
    return text


def unguard_ch7(text: str) -> str:
    for old, guard in CH7_GUARDS:
        text = text.replace(guard, old)
    return text


def apply_pairs(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        if old != new:
            text = text.replace(old, new)
    return text


def restructure_ch06(text: str) -> str:
    text = text.replace(
        '<a id="3-primary-axis-categories-slot-grammar-and-defaults"></a>',
        '<a id="3-slot-grammar-and-display-labels"></a>\n<a id="3-primary-axis-categories-slot-grammar-and-defaults"></a>',
    )
    text = guard_ch7(text)

    lequ_start = text.index('<a id="32-constitutional-outcome-baseline-for-slots"></a>')
    lequ_end = text.index('<a id="33-primary-category-defaults-and-lequ-slot-baseline"></a>')
    lequ_block = text[lequ_start:lequ_end]
    lequ_block = lequ_block.replace(
        "#### 3.2 LEQU baseline — measuring impact in lifetime-equivalent units",
        "### 4. LEQU baseline — measuring impact in lifetime-equivalent units",
    )

    without_lequ = text[:lequ_start] + text[lequ_end:]
    insert_marker = (
        "For axis-pure record separation and the rule that shared slot numbers do not create a net score, "
        "blended score, or tradeoff between axes, see **section 2.2** and **sections 2.3.1–2.3.2**.\n"
    )
    insert_pos = without_lequ.index(insert_marker) + len(insert_marker)
    text = without_lequ[:insert_pos] + "\n" + lequ_block + without_lequ[insert_pos:]

    text = text.replace(
        "### 3. Primary axis categories, slot grammar, and defaults",
        "### 3. Slot grammar and display labels",
    )
    text = text.replace("#### 3.3 Primary category defaults", "#### 5. Primary category defaults")
    text = text.replace("#### 3.4 Accountability measure", "#### 6. Accountability measure")

    # Renumber internal section refs (most specific first)
    for old, new in [
        ("section 3.4", "section 6"),
        ("section 3.3", "section 5"),
        ("section 3.2", "section 4"),
    ]:
        text = text.replace(old, new)

    text = apply_pairs(text, CH06_PROSE)
    text = re.sub(r"\[§3\.4, ([^\]]+)\]", r"[§6, \1]", text)
    text = unguard_ch7(text)
    return text


def update_other(path: Path, text: str) -> str:
    text = guard_ch7(text)
    text = apply_pairs(text, CROSS_FILE)
    text = unguard_ch7(text)
    return text


def main() -> None:
    ch06 = CH06.read_text()
    CH06.write_text(restructure_ch06(ch06))

    changed = [str(CH06.relative_to(ROOT))]
    for path in ROOT.rglob("*"):
        if path == CH06 or "archive/" in str(path) or "tools/ch06_promote" in str(path):
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        original = path.read_text()
        updated = update_other(path, original)
        if updated != original:
            path.write_text(updated)
            changed.append(str(path.relative_to(ROOT)))

    print(f"Promoted LEQU to §4; renumbered classification in {len(changed)} file(s).")
    for name in sorted(changed):
        print(f"  - {name}")


if __name__ == "__main__":
    main()
