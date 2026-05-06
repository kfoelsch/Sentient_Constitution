#!/usr/bin/env python3
"""Disabled one-shot migration script for the pre-split Chapter Six layout.

Chapter Six now lives in core_06-06_standing_classification.md and
core_06-06_standing_integration.md. Do not rerun this historical renumberer.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "core_06-06_standing_classification.md"


def dual(html_id: str, new_first: str) -> str:
    return f'<a id="{new_first}"></a>\n<a id="{html_id}"></a>'


def main() -> None:
    raise SystemExit(
        "Disabled: Chapter Six is split. Edit core_06-06_standing_classification.md "
        "and core_06-06_standing_integration.md directly."
    )
    text = SRC.read_text(encoding="utf-8")

    # --- A) Extract standing block from §1 ---
    s_marker = '<a id="verified-inputs-for-standing"></a>'
    e_marker = "\n\nIt establishes constitutional meaning only."
    i0 = text.find(s_marker)
    i1 = text.find(e_marker, i0)
    if i0 < 0 or i1 < 0:
        raise SystemExit("standing extract markers not found")
    standing_inner = text[i0:i1]
    text = text[:i0] + text[i1:]

    standing_inner = standing_inner.replace(
        "**sections 2.2 through 2.4** and **section 2.7**",
        "**sections 3.2 through 3.4** and **section 3.7**",
    )
    standing_inner = standing_inner.replace(
        '<a id="verified-inputs-for-standing"></a>',
        '<a id="2-standing-effect-verified-inputs-forums"></a>\n<a id="verified-inputs-for-standing"></a>',
        1,
    )

    trace_s2 = """### 2. Standing Effect — Verified Inputs and Forums
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [§1](#1-purpose-and-role) (*two-axis frame*).
- Downstream: [§3](#3-axis-i-contribution-state-and-standing-effect) (*Axis I*); [§4](#4-axis-ii-violation-nature-legal-constitutional-type) (*Axis II*); [§6](#6-cross-axis-coupling-and-escalation-constraints) (*joint assessment*).
- Read with: [Chapter Eight](core_08-08_forum.md#chapter-eight-forums-and-jurisdiction) (*forums separate*).

</details>

<br>

*In plain terms: **standing** uses **verified** inputs only — **Chapter Eight** processes **claims** that may later support those inputs.*

"""

    standing_section = trace_s2 + standing_inner + "\n\n"
    insert_after = "**Chapter Seven**).\n\n"
    idx = text.find(insert_after)
    if idx < 0:
        raise SystemExit("insert point not found")
    idx_end = idx + len(insert_after)
    text = text[:idx_end] + standing_section + text[idx_end:]

    # --- B) Violation #### 3.13 .. 3.10 then 3.9 .. 3.1 ---
    for head in ("3.13", "3.12", "3.11", "3.10"):
        text = text.replace(f"#### {head} ", f"#### 4.{head[2:]} ", 999)
    for d in range(9, 0, -1):
        text = text.replace(f"#### 3.{d} ", f"#### 4.{d} ", 999)
    text = text.replace("### 3. Violation Nature", "### 4. Violation Nature", 1)

    # --- C) Axis I #### 2.8 .. 2.0, ##### 2.0.n, ### 2. Contribution ---
    for d in range(8, -1, -1):
        text = text.replace(f"#### 2.{d} ", f"#### 3.{d} ", 999)
    for d in range(5, 0, -1):
        text = text.replace(f"##### 2.0.{d} ", f"##### 3.0.{d} ", 999)
    text = text.replace("### 2. Contribution State and Standing Effect", "### 3. Contribution State and Standing Effect", 1)

    # --- D) §3.N -> §4.N (violation) ---
    for n in range(13, 0, -1):
        text = re.sub(rf"§3\.{n}\b", f"§4.{n}", text)

    # --- E) §2.N -> §3.N (Axis I), §2.0.x ---
    for n in range(8, 0, -1):
        text = re.sub(rf"§2\.{n}\b", f"§3.{n}", text)
    text = re.sub(r"§2\.0\.(\d)\b", r"§3.0.\1", text)
    text = re.sub(r"\b§2\.0\b", "§3.0", text)

    # --- F) Markdown (#fragments) ---
    viol_frags = [
        ("313-non-exclusive-harm-and-conduct-descriptors", "413-non-exclusive-harm-and-conduct-descriptors"),
        ("312-negligence-and-neglect-as-violation-nature", "412-negligence-and-neglect-as-violation-nature"),
        ("311-duty-to-resist-unlawful-or-unconstitutional-instructions", "411-duty-to-resist-unlawful-or-unconstitutional-instructions"),
        ("310-collective-accountability-and-acquiescent-participation", "410-collective-accountability-and-acquiescent-participation"),
        ("39-non-exclusive-harm-and-conduct-descriptors", "49-non-exclusive-harm-and-conduct-descriptors"),
        ("39-constitutional-floor-rule", "49-constitutional-floor-rule"),
        ("38-concurrent-and-hybrid-violations", "48-concurrent-and-hybrid-violations"),
        ("37-constitutional-violation", "47-constitutional-violation"),
        ("37-duty-to-resist-unlawful-or-unconstitutional-instructions", "47-duty-to-resist-unlawful-or-unconstitutional-instructions"),
        ("36-criminal-violation", "46-criminal-violation"),
        ("35-civil-violation", "45-civil-violation"),
        ("34-critical-non-compliance", "44-critical-non-compliance"),
        ("33-aggravated-non-compliance", "43-aggravated-non-compliance"),
        ("32-substantive-non-compliance", "42-substantive-non-compliance"),
        ("31-formal-non-compliance", "41-formal-non-compliance"),
    ]
    for old, new in viol_frags:
        text = text.replace(f"(#{old})", f"(#{new})")

    ai_frags = [
        ("28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement", "38-stackable-benefit-and-stewardship-descriptors-axis-i-supplement"),
        ("27-standing-integration-contribution-and-violation-nature", "37-standing-integration-contribution-and-violation-nature"),
        ("26-reinstatement-review-and-non-entrenchment", "36-reinstatement-review-and-non-entrenchment"),
        ("25-restrictive-standing-effects", "35-restrictive-standing-effects"),
        ("24-positive-standing-recognition", "34-positive-standing-recognition"),
        ("23-stewardship-positive-contribution", "33-stewardship-positive-contribution"),
        ("22-positive-contribution", "32-positive-contribution"),
        ("21-baseline-contribution", "31-baseline-contribution"),
        ("212-stackable-benefit-and-stewardship-descriptors-axis-i-supplement", "312-stackable-benefit-and-stewardship-descriptors-axis-i-supplement"),
        ("211-standing-integration-contribution-and-violation-nature", "311-standing-integration-contribution-and-violation-nature"),
        ("20-scope-contribution-state-and-standing-effect", "30-scope-contribution-state-and-standing-effect"),
        ("205-relationship-to-section-5-domain-lenses", "305-relationship-to-section-5-domain-lenses"),
        ("205-relationship-to-section-12-domain-lenses", "305-relationship-to-section-12-domain-lenses"),
        ("204-informal-and-non-institutional-contribution", "304-informal-and-non-institutional-contribution"),
        ("203-standing-effect", "303-standing-effect"),
        ("202-co-occurrence-with-violation-nature", "302-co-occurrence-with-violation-nature"),
        ("201-contribution-state-axis-i-positive-only", "301-contribution-state-axis-i-positive-only"),
    ]
    for old, new in ai_frags:
        text = text.replace(f"(#{old})", f"(#{new})")

    text = text.replace(
        "[§3](#3-axis-ii-violation-nature-legal-constitutional-type)",
        "[§4](#4-axis-ii-violation-nature-legal-constitutional-type)",
    )
    text = text.replace("(#3-axis-ii-violation-nature-legal-constitutional-type)", "(#4-axis-ii-violation-nature-legal-constitutional-type)")
    text = text.replace(
        "[§2](#2-axis-i-contribution-state-and-standing-effect)",
        "[§3](#3-axis-i-contribution-state-and-standing-effect)",
    )
    text = text.replace("(#2-axis-i-contribution-state-and-standing-effect)", "(#3-axis-i-contribution-state-and-standing-effect)")

    text = text.replace("[§2.0](#", "[§3.0](#")

    # --- G) HTML id lines: new id + legacy ---
    repl_html = [
        ("<a id=\"2-axis-i-contribution-state-and-standing-effect\"></a>", dual("2-axis-i-contribution-state-and-standing-effect", "3-axis-i-contribution-state-and-standing-effect")),
        ("<a id=\"3-axis-ii-violation-nature-legal-constitutional-type\"></a>", dual("3-axis-ii-violation-nature-legal-constitutional-type", "4-axis-ii-violation-nature-legal-constitutional-type")),
        ("<a id=\"20-scope-contribution-state-and-standing-effect\"></a>", dual("20-scope-contribution-state-and-standing-effect", "30-scope-contribution-state-and-standing-effect")),
        ("<a id=\"201-contribution-state-axis-i-positive-only\"></a>", dual("201-contribution-state-axis-i-positive-only", "301-contribution-state-axis-i-positive-only")),
        ("<a id=\"202-co-occurrence-with-violation-nature\"></a>", dual("202-co-occurrence-with-violation-nature", "302-co-occurrence-with-violation-nature")),
        ("<a id=\"203-standing-effect\"></a>", dual("203-standing-effect", "303-standing-effect")),
        ("<a id=\"204-informal-and-non-institutional-contribution\"></a>", dual("204-informal-and-non-institutional-contribution", "304-informal-and-non-institutional-contribution")),
        ("<a id=\"205-relationship-to-section-5-domain-lenses\"></a>", dual("205-relationship-to-section-5-domain-lenses", "305-relationship-to-section-5-domain-lenses")),
        ("<a id=\"205-relationship-to-section-12-domain-lenses\"></a>", dual("205-relationship-to-section-12-domain-lenses", "305-relationship-to-section-12-domain-lenses")),
        ("<a id=\"21-baseline-contribution\"></a>", dual("21-baseline-contribution", "31-baseline-contribution")),
        ("<a id=\"27-standing-integration-contribution-and-violation-nature\"></a>", dual("27-standing-integration-contribution-and-violation-nature", "37-standing-integration-contribution-and-violation-nature")),
        ("<a id=\"211-standing-integration-contribution-and-violation-nature\"></a>", dual("211-standing-integration-contribution-and-violation-nature", "311-standing-integration-contribution-and-violation-nature")),
        ("<a id=\"28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement\"></a>", dual("28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement", "38-stackable-benefit-and-stewardship-descriptors-axis-i-supplement")),
        ("<a id=\"212-stackable-benefit-and-stewardship-descriptors-axis-i-supplement\"></a>", dual("212-stackable-benefit-and-stewardship-descriptors-axis-i-supplement", "312-stackable-benefit-and-stewardship-descriptors-axis-i-supplement")),
        ("<a id=\"31-formal-non-compliance\"></a>", dual("31-formal-non-compliance", "41-formal-non-compliance")),
        ("<a id=\"35-civil-violation\"></a>", dual("35-civil-violation", "45-civil-violation")),
        ("<a id=\"310-collective-accountability-and-acquiescent-participation\"></a>", dual("310-collective-accountability-and-acquiescent-participation", "410-collective-accountability-and-acquiescent-participation")),
        ("<a id=\"311-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>", dual("311-duty-to-resist-unlawful-or-unconstitutional-instructions", "411-duty-to-resist-unlawful-or-unconstitutional-instructions")),
        ("<a id=\"37-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>", dual("37-duty-to-resist-unlawful-or-unconstitutional-instructions", "47-duty-to-resist-unlawful-or-unconstitutional-instructions")),
        ("<a id=\"312-negligence-and-neglect-as-violation-nature\"></a>", dual("312-negligence-and-neglect-as-violation-nature", "412-negligence-and-neglect-as-violation-nature")),
        ("<a id=\"313-non-exclusive-harm-and-conduct-descriptors\"></a>", dual("313-non-exclusive-harm-and-conduct-descriptors", "413-non-exclusive-harm-and-conduct-descriptors")),
        ("<a id=\"39-non-exclusive-harm-and-conduct-descriptors\"></a>", dual("39-non-exclusive-harm-and-conduct-descriptors", "49-non-exclusive-harm-and-conduct-descriptors")),
    ]
    for old, new in repl_html:
        if old not in text:
            continue
        text = text.replace(old, new, 1)

    # --- H) Prose: Contribution State / Ch5 pointers ---
    text = text.replace(
        "operative Axis I text in **section 2**",
        "operative Axis I text in **section 3**",
    )
    text = text.replace(
        "**section 2**](#3-axis-i-contribution-state-and-standing-effect)",
        "**section 3**](#3-axis-i-contribution-state-and-standing-effect)",
    )

    # Violation nature previously "section 3"
    text = re.sub(
        r"violation nature\*\* \(\*\*section 3\*\*\)",
        r"violation nature** (**section 4**)",
        text,
    )
    text = text.replace(
        "typing under **section 3**",
        "typing under **section 4**",
    )
    text = text.replace(
        "classified under **violation nature** (**section 3**)",
        "classified under **violation nature** (**section 4**)",
    )
    text = text.replace(
        "violation-nature** typing under **section 3**",
        "violation-nature** typing under **section 4**",
    )
    text = text.replace("under **section 3** (including", "under **section 4** (including")

    # Domain lens / shorthand sections 2.8 / 3.13 -> 3.8 / 4.13
    text = text.replace("**sections 2.8** and **3.13**", "**sections 3.8** and **4.13**")
    text = text.replace("**section 2.8** and **harm-and-conduct supplemental descriptors** under **section 3.13**", "**section 3.8** and **harm-and-conduct supplemental descriptors** under **section 4.13**")
    text = text.replace("**§2.8**", "**§3.8**")
    text = text.replace("**§3.13**", "**§4.13**")
    text = text.replace("§3.5** when", "§4.5** when")  # careful - might double-replace wrong

    # Chapter trace + §1.1 reading order
    text = text.replace(
        "(*non-operative lens table — after **§§2–3***)",
        "(*non-operative lens table — after **§§3–4***)",
    )
    text = text.replace(
        "Subsections (reading order): [§1](#1-purpose-and-role); [§1.1](#11-two-axis-overview-reference); [§3](#3-axis-i-contribution-state-and-standing-effect);",
        "Subsections (reading order): [§1](#1-purpose-and-role); [§1.1](#11-two-axis-overview-reference); [§2](#2-standing-effect-verified-inputs-forums); [§3](#3-axis-i-contribution-state-and-standing-effect);",
    )

    # Constitutional owner block (single long line) — replace key phrases
    text = text.replace(
        "**section 5** states the **shared domain lens** table (cross-axis vocabulary) read with **sections 2.8** and **3.13**; **section 2** classifies **contribution state**",
        "**section 5** states the **shared domain lens** table (cross-axis vocabulary) read with **sections 3.8** and **4.13**; **section 3** classifies **contribution state**",
    )
    text = text.replace(
        "**sections 2.4–2.7**) that **apply** that **standing effect** (**section 2.7**",
        "**sections 3.4–3.7**) that **apply** that **standing effect** (**section 3.7**",
    )
    text = text.replace(
        "**stackable benefit-and-stewardship descriptors** (**section 2.8**)",
        "**stackable benefit-and-stewardship descriptors** (**section 3.8**)",
    )
    text = text.replace(
        "**section 3** classifies **violation nature** (**sections 3.1–3.4** severity ladder; **sections 3.5–3.12**",
        "**section 4** classifies **violation nature** (**sections 4.1–4.4** severity ladder; **sections 4.5–4.12**",
    )
    text = text.replace(
        "**stackable harm-and-conduct descriptors** (**section 3.13**)",
        "**stackable harm-and-conduct descriptors** (**section 4.13**)",
    )
    text = text.replace(
        "**Reading order:** **section 1.1** maps **sections 2** and **3**; **section 5** states the **shared domain lens** table read with **sections 2.8** and **3.13** (**after** **sections 2** and **3** in document order); **section 2** carries **contribution-band**",
        "**Reading order:** **section 1.1** maps **sections 3** and **4**; **section 2** states **verified inputs for standing**; **section 5** states the **shared domain lens** table read with **sections 3.8** and **4.13** (**after** **sections 3** and **4** in document order); **section 3** carries **contribution-band**",
    )
    text = text.replace(
        "through **section 2.7**, then **section 2.8** (supplemental descriptors); **section 3** carries **violation** typing through **section 3.12**, then **section 3.13** (supplemental descriptors).",
        "through **section 3.7**, then **section 3.8** (supplemental descriptors); **section 4** carries **violation** typing through **section 4.12**, then **section 4.13** (supplemental descriptors).",
    )
    text = text.replace(
        "Operative integration lives in **section 1** and **section 2** of this chapter.",
        "Operative integration lives in **sections 1–2** (frame and **verified inputs**) and in **sections 3–4** (the two classification axes) of this chapter.",
    )
    text = text.replace(
        "**Standing effect** in this chapter applies only to **verified** standing inputs — **demonstrable** **contribution state** and **verified violation findings** — as stated in **section 1** (**verified inputs for standing**).",
        "**Standing effect** in this chapter applies only to **verified** standing inputs — **demonstrable** **contribution state** and **verified violation findings** — as stated in **section 2** (**verified inputs for standing**).",
    )

    # Domain gloss line 19
    text = text.replace(
        "**Section 5** pairs thematic **§2.8** prosocial labels with **§3.13** harm-route descriptors",
        "**Section 5** pairs thematic **§3.8** prosocial labels with **§4.13** harm-route descriptors",
    )
    text = text.replace(
        "reader illustration in the **§5** table; operative detail in the **remedial and restorative** bullet in **§2.8**).",
        "reader illustration in the **§5** table; operative detail in the **remedial and restorative** bullet in **§3.8**).",
    )

    # §1.1 title
    text = text.replace(
        "### 1.1 Contribution state and violation nature — reading map (§§2–3, then §5)",
        "### 1.1 Contribution state and violation nature — reading map (§§2–4, then §5)",
    )

    # De-dup legacy if script re-run
    text = re.sub(
        r'(<a id="3-axis-i-contribution-state-and-standing-effect"></a>\s*){2,}',
        r'<a id="3-axis-i-contribution-state-and-standing-effect"></a>\n',
        text,
    )

    SRC.write_text(text, encoding="utf-8")
    print("OK", SRC)


if __name__ == "__main__":
    main()
