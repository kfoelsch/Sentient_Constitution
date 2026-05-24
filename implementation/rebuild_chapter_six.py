#!/usr/bin/env python3
"""Disabled one-shot migration script for the pre-split Chapter Six layout.

Chapter Six now lives in core_06-06_standing_assessment.md and
core_07-07_standing_integration.md. Do not rerun this historical generator.
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "core_06-06_standing_assessment.md"
BAK = ROOT / "core_06-06_standing_assessment.md.bak"

def lines_slice(lines, start_1, end_1):
    """1-based inclusive start, 1-based inclusive end."""
    return "".join(lines[start_1 - 1 : end_1])


def main():
    raise SystemExit(
        "Disabled: Chapter Six is split. Edit core_06-06_standing_assessment.md "
        "and core_07-07_standing_integration.md directly."
    )
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines(True)
    BAK.write_text(text, encoding="utf-8")

    # --- Preamble: lines 1-47, update chapter Trace reading order (line 37-38 area)
    preamble = lines_slice(lines, 1, 47)
    preamble = preamble.replace(
        "- Subsections (reading order): [§1](#1-purpose-and-role); [§1.1](#11-two-axis-overview-reference); [§1.2](#12-shared-domain-lenses-cross-axis-vocabulary); [§2](#2-axis-i-contribution-state-and-standing-effect); [§2.0](#20-scope-contribution-state-and-standing-effect); [§2.1](#21-baseline-contribution)–[§2.7](#27-standing-integration-contribution-and-violation-nature); [§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement); [§3](#3-axis-ii-violation-nature-legal-constitutional-type); [§3.1](#31-formal-non-compliance)–[§3.12](#312-negligence-and-neglect-as-violation-nature); [§3.13](#313-non-exclusive-harm-and-conduct-descriptors); [§4](#4-cross-axis-coupling-and-escalation-constraints); [§5](#5-additive-and-non-substitution-rule); [§6](#6-enforcement-realism-anchors); [§7](#7-tiered-anti-constitutional-misconduct-authoritative-location).",
        "- Subsections (reading order): [§1](#1-purpose-and-role); [§1.1](#11-chapter-layout-and-reading-order); [§2](#2-standing-forums-and-verified-inputs) (*standing inputs and integration*); [§3](#3-axis-i-contribution-state); [§4](#4-axis-ii-violation-nature); [§5](#5-shared-domain-lenses-cross-axis-vocabulary); [§6](#6-cross-axis-coupling-and-escalation-constraints); [§7](#7-additive-and-non-substitution-rule); [§8](#8-enforcement-realism-anchors); [§9](#9-tiered-anti-constitutional-misconduct-authoritative-location).",
    )

    # Reader guidance block: update constitutional owner bullets (lines 17-26) — replace long paragraph
    old_rg = lines_slice(lines, 12, 30)
    # Minimal fix: replace first bullet line in collapsible — user can refine later
    # We'll patch line 18-26 in preamble+reader - actually lines 12-30 includes details open tag
    preamble = preamble.replace(
        "> - **Constitutional owner:** unified **contribution state** and **violation nature** — **section 1** frames **two** axes — **(I) contribution state** (**positive-only**: baseline and uplift bands) and **(II) violation nature** (**adverse** findings: **non-compliance severity ladder**, legal-constitutional violation characterization, and supplements) — **combined into a standing effect** (**verified** inputs only — **demonstrable** Contribution Axis and **verified violation findings** for the Violation Axis; **forum** **allegations** are **Chapter Eight**, not standing calculus), with **inherent-rights separation** stated there; **section 1.2** states the **shared domain lens** table (cross-axis vocabulary) read with **sections 2.8** and **3.13**; **section 2** classifies **contribution state** and states **trust-, role-, and recognition-eligibility** mechanics (**sections 2.4–2.7**) that **apply** that **standing effect** (**section 2.7** — violation-weighted integration with **violation nature**), including **stackable benefit-and-stewardship descriptors** (**section 2.8**) that **supplement** **positive** **contribution-band** typing for **recognition** and **audit** narratives **without** substituting **exclusive** **contribution-state** branches or **netting away** **section 4** discipline when **violation** findings apply; **section 3** classifies **violation nature** (**sections 3.1–3.4** severity ladder; **sections 3.5–3.12** legal and hybrid rules), including **stackable harm-and-conduct descriptors** (**section 3.13**) that **stack** for triage and routing **without** displacing primary typing or the final **Violation Axis s = 7, 8, or 9** structure of **Chapter Seven**; **joint assessment and cross-axis coupling** (**section 4**); **additive and non-substitution** discipline (**section 5**); **enforcement realism anchors** (**section 6**); **pointer-only** home (**section 7**) routing final **Violation Axis s = 7, 8, or 9 anti-constitutional misconduct** classification to **Chapter Seven**. **Reading order:** **section 1.1** orients **sections 2** and **3**; **section 1.2** states the **shared domain lens** table read with **sections 2.8** and **3.13**; **section 2** carries **contribution-band** and standing-integration content through **section 2.7**, then **section 2.8** (supplemental descriptors); **section 3** carries **violation** typing through **section 3.12**, then **section 3.13** (supplemental descriptors).",
        "> - **Constitutional owner:** unified **contribution state** and **violation nature** — **section 1** frames the **two** axes; **section 2** states **verified inputs for standing**, **standing effect**, and **standing integration** (including **contribution-linked recency weighting**); **section 3** classifies **Contribution Axis** **contribution state** and trust-, role-, and recognition-eligibility mechanics, with **stackable** supplements in **section 3.7**; **section 4** classifies **Violation Axis** **violation nature** (primary typing **sections 4.1–4.12**, supplements **section 4.13**); **section 5** is the **non-operative** **domain lens** table (read **after** **sections 3–4**); **sections 6–9** carry **joint assessment**, **additive discipline**, **enforcement anchors**, and the **Chapter Seven** tier **pointer**.",
    )
    preamble = preamble.replace(
        "> - **Domain lens table (non-operative gloss):** **Section 1.2** pairs thematic **§2.8** prosocial labels with **§3.13** harm-route descriptors (and **primary typing** where that section states it). **Remedial and restorative benefit** (**§2.8**) is **cross-lens** — it may **stack** with any table row and is **not** its own domain row — and in the adverse column **read with** **§3.5** when civil remedy or restoration obligation is the **dominant** framing (reader illustration in the **§1.2** table; operative detail in the **remedial and restorative** bullet in **§2.8**).",
        "> - **Domain lens table (non-operative gloss):** **Section 5** pairs thematic **§3.7** prosocial labels with **§4.13** harm-route descriptors (and **primary typing** where that section states it). **Remedial and restorative benefit** (**§3.7**) is **cross-lens** — it may **stack** with any table row and is **not** its own domain row — and in the adverse column **read with** **§4.5** when civil remedy or restoration obligation is the **dominant** framing (reader illustration in the **§5** table; operative detail in the **remedial and restorative** bullet in **§3.7**).",
    )
    preamble = preamble.replace(
        "> - **Principle foundation (non-operative gloss):** [Chapter One §5.2 — Stewardship and Distributed Understanding](core_00-01_principles.md#52-stewardship-and-distributed-understanding) states the *why* for **standing** that ties trust-, role-, and recognition-eligibility to **distributed competence** and **consequential stewardship** under audit and contestability — not to opaque prestige or symbolic participation alone. Operative integration lives in **section 1** and **section 2** of this chapter.",
        "> - **Principle foundation (non-operative gloss):** [Chapter One §5.2 — Stewardship and Distributed Understanding](core_00-01_principles.md#52-stewardship-and-distributed-understanding) states the *why* for **standing** that ties trust-, role-, and recognition-eligibility to **distributed competence** and **consequential stewardship** under audit and contestability — not to opaque prestige or symbolic participation alone. Operative integration lives in **section 2** of this chapter (**standing effect** and **verified inputs for standing**).",
    )
    preamble = preamble.replace(
        "**Standing effect** in this chapter applies only to **verified** standing inputs — **demonstrable** **contribution state** and **verified violation findings** — as stated in **section 1** (**verified inputs for standing**). **Forums** under",
        "**Standing effect** in this chapter applies only to **verified** standing inputs — **demonstrable** **contribution state** and **verified violation findings** — as stated in **section 2** (**verified inputs for standing**). **Forums** under",
    )
    preamble = preamble.replace(
        "incentives can credit prosocial conduct and constrain anti-social conduct under **sections 4** and **5** (no netting or substitution).",
        "incentives can credit prosocial conduct and constrain anti-social conduct under **sections 6** and **7** (no netting or substitution).",
    )
    preamble = preamble.replace(
        "**Final Violation Axis s = 7, 8, or 9** anti-constitutional classification and criteria are **Chapter Seven** only (**section 7** pointer).",
        "**Final Violation Axis s = 7, 8, or 9** anti-constitutional classification and criteria are **Chapter Seven** only (**section 9** pointer).",
    )
    preamble = preamble.replace(
        "coordinated through the **domain lens** table in **section 1.2**, are to be treated as **one** coordinated labeling scheme",
        "coordinated through the **domain lens** table in **section 5**, are to be treated as **one** coordinated labeling scheme",
    )
    preamble = preamble.replace(
        "supplemental descriptors under **section 2.8** and **harm-and-conduct supplemental descriptors** under **section 3.13**",
        "supplemental descriptors under **section 3.7** and **harm-and-conduct supplemental descriptors** under **section 4.13**",
    )

    preamble = preamble.replace(
        "- Downstream: [Chapter Ten](core_08-08_misconduct.md#chapter-seven-axis-ii-grand-anti-constitutional-misconduct) (*authoritative Violation Axis s = 7, 8, or 9 classification — **section 7** pointer*); [Chapter Ten](core_09-09_forum.md#chapter-nine-forums-and-jurisdiction) (*forum allocation for disputes arising under this model*); [Chapter Ten — Article XXIII](core_10-10_rights_part_d.md#article-xxiii-a-justice-objective-and-scope) (*justice constraints on punitive and restrictive responses*).",
        "- Downstream: [Chapter Ten](core_08-08_misconduct.md#chapter-seven-axis-ii-grand-anti-constitutional-misconduct) (*authoritative Violation Axis s = 7, 8, or 9 classification — **section 9** pointer*); [Chapter Ten](core_09-09_forum.md#chapter-nine-forums-and-jurisdiction) (*forum allocation for disputes arising under this model*); [Chapter Ten — Article XXIII](core_10-10_rights_part_d.md#article-xxiii-a-justice-objective-and-scope) (*justice constraints on punitive and restrictive responses*).",
    )

    # --- §1 Purpose: lines 48-71 + 85-91 (skip verified inputs / principle / informal block 72-84)
    s1 = lines_slice(lines, 48, 71) + lines_slice(lines, 85, 91)
    s1 = s1.replace(
        "- Downstream: [§1.1](#11-two-axis-overview-reference) (*how **sections 2** and **3** fit*); [§1.2](#12-shared-domain-lenses-cross-axis-vocabulary) (*cross-axis domain lens table*); [§2](#2-axis-i-contribution-state-and-standing-effect) through [§3](#3-axis-ii-violation-nature-legal-constitutional-type) (*contribution state and violation nature — **sections 2.8** and **3.13** close each block*); [§4](#4-cross-axis-coupling-and-escalation-constraints) (*joint assessment*); [§6](#6-enforcement-realism-anchors) (*implementation anchors*); [§7](#7-tiered-anti-constitutional-misconduct-authoritative-location) (*Chapter Seven pointer*).",
        "- Downstream: [§1.1](#11-chapter-layout-and-reading-order) (*chapter layout*); [§2](#2-standing-forums-and-verified-inputs) (*verified inputs and standing integration*); [§3](#3-axis-i-contribution-state) through [§4](#4-axis-ii-violation-nature) (*Contribution Axis and Violation Axis primary typing and supplements*); [§5](#5-shared-domain-lenses-cross-axis-vocabulary) (*non-operative domain lens table*); [§6](#6-cross-axis-coupling-and-escalation-constraints) (*joint assessment*); [§8](#8-enforcement-realism-anchors) (*implementation anchors*); [§9](#9-tiered-anti-constitutional-misconduct-authoritative-location) (*Chapter Seven pointer*).",
    )

    # --- §1.1 rewritten
    s11 = dedent("""
    <a id="11-two-axis-overview-reference"></a>
    <a id="11-chapter-layout-and-reading-order"></a>

    ### 1.1 Chapter layout and reading order
    <details>
    <summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

    - Upstream: [§1](#1-purpose-and-role) (*purpose and constitutional-meaning-only scope*).
    - Downstream: [§2](#2-standing-forums-and-verified-inputs) (*verified inputs, standing effect, integration*); [§3](#3-axis-i-contribution-state) (*Contribution Axis — contribution state*); [§4](#4-axis-ii-violation-nature) (*Violation Axis — violation nature*); [§5](#5-shared-domain-lenses-cross-axis-vocabulary) (*non-operative domain lens table — read after §§3–4*); [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) and [§4.13](#413-non-exclusive-harm-and-conduct-descriptors) (*stackable supplemental descriptors*); [§6](#6-cross-axis-coupling-and-escalation-constraints) (*joint assessment*); [§9](#9-axis-ii-grand-anti-constitutional-misconduct-authoritative-location) (*pointer to Chapter Seven for final Violation Axis s = 7, 8, or 9 classification*).
    - Read with: [Chapter Eight](core_08-08_misconduct.md#chapter-seven-axis-ii-grand-anti-constitutional-misconduct) (*authoritative Violation Axis s = 7, 8, or 9 home*).

    </details>

    <br>

    *In plain terms: **section 2** states how **verified** inputs combine into **standing effect**; **sections 3** and **4** carry **Contribution Axis** and **Violation Axis** primary typing (and **stackable** supplements at the end of each); **section 5** is a **non-operative** vocabulary bridge; **sections 6–9** apply both axes together.*

    **Binding-first order:** [§2](#2-standing-forums-and-verified-inputs) → [§3](#3-axis-i-contribution-state) → [§4](#4-axis-ii-violation-nature) → [§5](#5-shared-domain-lenses-cross-axis-vocabulary) → [§6](#6-cross-axis-coupling-and-escalation-constraints) → [§7](#7-additive-and-non-substitution-rule) → [§8](#8-enforcement-realism-anchors) → [§9](#9-axis-ii-grand-anti-constitutional-misconduct-authoritative-location).

    **Section 5**’s **shared domain lens** table **pairs** [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) prosocial supplements with [§4.13](#413-non-exclusive-harm-and-conduct-descriptors) harm-route descriptors **without** replacing primary **§3.1–3.3** bands or **§4.1–4.12** severity / legal typing; **§3.7**’s **remedial and restorative benefit** **stacks** across those lenses and **read with** **§4.5** when remedy dominates (**§5** table).

    | Layer | Contribution Axis — **§3** | Violation Axis — **§4** |
    | --- | --- | --- |
    | Scope and axis framing | **§3.0** | **§4** opening paragraphs |
    | Primary classification | **§3.1–3.3** | **§4.1–4.12** |
    | Trust / role / recognition mechanics (standing application) | **§3.4–3.6** | *(no §4 analogue — **violation nature** feeds **§2** and **§6**)* |
    | Stackable supplemental descriptors | **§3.7** | **§4.13** |

    Read **sections 3** and **4** with **section 6** (joint assessment), **section 7** (additive and non-substitution), and **section 9** (**final Violation Axis s = 7, 8, or 9** classification for **anti-constitutional misconduct** lives only in **Chapter Seven**).

    """)

    # --- §2 = verified block + co-occurrence + standing effect + informal + 2.7 + 2.0.5 (without duplicate informal from s1)
    blk_verified_through_informal = lines_slice(lines, 72, 84)  # lines 73-84

    sec202 = lines_slice(lines, 211, 235)
    sec202 = sec202.replace("##### 2.0.2", "#### 2.3").replace("2.0.2", "2.3")
    sec203 = lines_slice(lines, 237, 262)
    sec203 = sec203.replace("##### 2.0.3", "#### 2.4").replace("2.0.3", "2.4").replace("[§1](#verified-inputs-for-standing)", "[§2.1](#21-verified-inputs-for-standing)")
    sec203 = sec203.replace("**section 1**", "**section 2**")
    sec204 = lines_slice(lines, 264, 288)
    sec204 = sec204.replace("##### 2.0.4", "#### 2.5").replace("2.0.4", "2.5")
    sec204 = sec204.replace("**sections 2.2 and 2.3**", "**sections 3.2 and 3.3**")
    sec204 = sec204.replace("**sections 2.4 and 2.7**", "**sections 3.4 and **§2.6**")
    # fix the botched replace
    sec204 = sec204.replace("**sections 3.4 and **§2.6**", "**sections 3.4 and 2.6**")

    sec205 = lines_slice(lines, 290, 314)
    sec205 = sec205.replace("##### 2.0.5", "#### 2.7").replace("2.0.5", "2.7")
    sec205 = sec205.replace("**§1.2**", "**§5**").replace("section 1.2", "section 5")
    sec205 = sec205.replace("**section 2.8**", "**section 3.7**").replace("**section 3.13**", "**section 4.13**")
    sec205 = sec205.replace("**§2.8**, **§3.5**", "**§3.7**, **§4.5**")
    sec205 = sec205.replace("**sections 2.8**", "**sections 3.7**")
    sec205 = sec205.replace("**section 2.7**", "**section 2.6**")
    sec205 = sec205.replace("**sections 2.1 through 2.3**", "**sections 3.1 through 3.3**")
    sec205 = sec205.replace("**sections 2.4 through 2.7**", "**sections 3.4 through 3.6** read with **section 2**")

    sec27 = lines_slice(lines, 484, 530)
    sec27 = sec27.replace("#### 2.7", "#### 2.6")
    sec27 = sec27.replace("27-standing-integration", "26-standing-integration-contribution-and-violation-nature")
    sec27 = sec27.replace("211-standing-integration", "211-standing-integration-contribution-and-violation-nature")
    sec27 = sec27.replace("**section 1**", "**section 2**")
    sec27 = sec27.replace("**§3.13**", "**§4.13**")
    sec27 = sec27.replace("**section** **4**", "**section** **6**")
    sec27 = sec27.replace("**section** **5**", "**section** **7**")
    sec27 = sec27.replace("**section 2.6**", "**section 3.6**", 1)  # read with section 2.6 — careful
    # Recency bullet: "section 4, section 5" -> 6, 7
    sec27 = sec27.replace("**section** **4**, **section** **5**,", "**section** **6**, **section** **7**,")
    sec27 = sec27.replace("in **section** **1**", "in **section** **2**")
    sec27 = sec27.replace("**section 2.6**", "**section 3.6**")

    # Fix sec27: upstream trace still says 2.4-2.6 — ok. Downstream 2.8 -> 3.7, 5 -> 7
    sec27 = sec27.replace("[§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)", "[§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)")
    sec27 = sec27.replace("[§5](#5-additive-and-non-substitution-rule)", "[§7](#7-additive-and-non-substitution-rule)")

    sec2_open = dedent("""
    <a id="2-standing-forums-and-verified-inputs"></a>
    <a id="2-axis-i-contribution-state-and-standing-effect"></a>

    ### 2. Standing, forums, and verified inputs
    <details>
    <summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

    - Upstream: [§1](#1-purpose-and-role) (*two-axis frame*); [Chapter One §5.2 — Stewardship and Distributed Understanding](core_00-01_principles.md#52-stewardship-and-distributed-understanding); [Chapters Two through Four](core_02-04_definition_mechanics.md); [Chapter Five](core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions).
    - Downstream: [§3](#3-axis-i-contribution-state) (*contribution state on the **Contribution Axis***); [§4](#4-axis-ii-violation-nature) (*violation nature on the **Violation Axis***); [§6](#6-cross-axis-coupling-and-escalation-constraints) (*joint assessment*).
    - Read with: [Chapter Ten](core_09-09_forum.md#chapter-nine-forums-and-jurisdiction) (*forums separate from standing calculus*); [Article XII-B](core_10-10_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress).

    </details>

    <details>
    <summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

    - [Contribution State](core_05-05_definitions_b_semi_independent.md#contribution-state) · [O](core_05-05_definitions_b_semi_independent.md#contribution-state) · [E](core_05-05_definitions_b_semi_independent.md#contribution-state-e) · [C](core_05-05_definitions_b_semi_independent.md#contribution-state-c)
    - [Participant Standing](core_05-05_definitions_b_semi_independent.md#participant-standing-constitutional) · [O](core_05-05_definitions_b_semi_independent.md#participant-standing-constitutional) · [E](core_05-05_definitions_b_semi_independent.md#participant-standing-constitutional-e) · [C](core_05-05_definitions_b_semi_independent.md#participant-standing-constitutional-c)
    - [Harm](core_05-05_definitions_c_dependent_clusters.md#harm) · [O](core_05-05_definitions_c_dependent_clusters.md#harm) · [E](core_05-05_definitions_c_dependent_clusters.md#harm-e) · [C](core_05-05_definitions_c_dependent_clusters.md#harm-c)

    </details>

    <br>

    *In plain terms: this section states **what counts** as input to **standing effect** — **verified** standing inputs only — and **how** contribution and violation findings **combine** for trust and roles including **recency** for good track record.*

    <a id="verified-inputs-for-standing"></a>
    <a id="21-verified-inputs-for-standing"></a>

    #### 2.1 Verified inputs for standing (forums separate)
    """)

    # Move anchor from old position - content starts after #### 
    blk_v2 = blk_verified_through_informal.replace("<a id=\"verified-inputs-for-standing\"></a>\n\n", "")
    # Remove **Verified...** duplicate title if present - old line 75 starts with **
    sec2_principle = dedent("""

    #### 2.2 Principle-layer foundation and informal standing (read with verified inputs)

    """)
    # Split old block: lines 73-75 verified title paragraph, 77 principle, 79-81 consequences, 83 informal
    # blk_verified_through_informal already has lines 73-84 from file - includes anchor line - need to strip first anchor
    v_lines = blk_verified_through_informal.splitlines(True)
    # Reconstruct: 2.1 body = from **Verified inputs** 
    body21 = "".join(v_lines[1:])  # drop first line if blank
    if body21.startswith("\n"):
        body21 = body21.lstrip("\n")
    # If first line is anchor, skip
    if "<a id=\"verified-inputs-for-standing\">" in body21:
        parts = body21.split("\n", 2)
        body21 = parts[-1] if len(parts) > 2 else body21

    # Simpler: use raw slice lines 74-84 1-based = indices 73-84
    body21 = "".join(lines[73:84])
    body21 = body21.replace(
        "**Informal contribution and standing.** Conduct that advances constitutional outcomes through **informal**, **peer**, **neighbor**, **mutual-aid**, or other **non-official** community pathways may count toward **contribution state** and **positive** **standing** recognition **as fully as**, and in many factual patterns **more than**, conduct visible only through **formal** offices, employment roles, licensed programs, or **designated** reporting channels, **when** the same **demonstrability**, **auditability**, and **contestability** standards in **sections 2.2 through 2.4** and **section 2.7** are satisfied.",
        "**Informal contribution and standing.** Conduct that advances constitutional outcomes through **informal**, **peer**, **neighbor**, **mutual-aid**, or other **non-official** community pathways may count toward **contribution state** and **positive** **standing** recognition **as fully as**, and in many factual patterns **more than**, conduct visible only through **formal** offices, employment roles, licensed programs, or **designated** reporting channels, **when** the same **demonstrability**, **auditability**, and **contestability** standards in **sections 3.2 through 3.4** and **section 2.6** are satisfied.",
    )

    section2 = (
        sec2_open
        + body21
        + "\n"
        + sec202
        + sec203
        + sec204
        + sec27
        + sec205
    )

    # --- §3 contribution: old §2 header 155-176, then 181-209 (0.1 only), 316-482, 532-573
    s3_head = lines_slice(lines, 155, 176)
    s3_head = s3_head.replace("### 2. Contribution State and Standing Effect", "### 3. Contribution state (Contribution Axis)")
    s3_head = s3_head.replace("#2-axis-i-contribution-state-and-standing-effect", "#3-axis-i-contribution-state")
    s3_head = s3_head.replace(
        "Downstream: [§2.0](#20-scope-contribution-state-and-standing-effect) (*Contribution Axis scope — contribution state and standing effect*); [§2.1](#21-baseline-contribution) through [§2.7](#27-standing-integration-contribution-and-violation-nature) (*contribution bands and standing integration*); [§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*contribution-state supplemental descriptors*); [§3](#3-axis-ii-violation-nature-legal-constitutional-type) (*violation nature*); [§4](#4-cross-axis-coupling-and-escalation-constraints)",
        "Downstream: [§3.0](#30-scope-contribution-state-axis-i) (*Contribution Axis scope*); [§3.1](#31-baseline-contribution) through [§3.6](#36-reinstatement-review-and-non-entrenchment) (*bands and recognition mechanics*); [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*supplemental descriptors*); [§4](#4-axis-ii-violation-nature) (*violation nature*); [§6](#6-cross-axis-coupling-and-escalation-constraints)",
    )
    s3_head = s3_head.replace("[§1.2](#12-shared-domain-lenses-cross-axis-vocabulary)", "[§5](#5-shared-domain-lenses-cross-axis-vocabulary)")
    s3_head = s3_head.replace("[§1](#1-purpose-and-role)", "[§2](#2-standing-forums-and-verified-inputs)")
    s3_head = s3_head.replace("[§1.1](#11-two-axis-overview-reference)", "[§1.1](#11-chapter-layout-and-reading-order)")

    s3_01 = lines_slice(lines, 181, 209)
    s3_01 = s3_01.replace("#### 2.0 Scope, contribution state, and standing effect", "#### 3.0 Scope, contribution state (Contribution Axis)")
    s3_01 = s3_01.replace("<a id=\"20-scope-contribution-state-and-standing-effect\"></a>", "<a id=\"30-scope-contribution-state-axis-i\"></a>\n<a id=\"20-scope-contribution-state-and-standing-effect\"></a>")
    s3_01 = s3_01.replace("##### 2.0.1", "##### 3.0.1")
    s3_01 = s3_01.replace("201-contribution-state", "301-contribution-state")
    s3_01 = s3_01.replace("[§2](#2-axis-i-contribution-state-and-standing-effect)", "[§3](#3-axis-i-contribution-state)")
    s3_01 = s3_01.replace("[§1.1](#11-two-axis-overview-reference)", "[§1.1](#11-chapter-layout-and-reading-order)")
    s3_01 = s3_01.replace("**section 3**", "**section 4**")

    s3_bands = lines_slice(lines, 316, 482)
    s3_bands = s3_bands.replace("#### 2.1", "#### 3.1")
    s3_bands = s3_bands.replace("#21-baseline", "#31-baseline")
    s3_bands = s3_bands.replace("<a id=\"21-baseline", "<a id=\"31-baseline")
    s3_bands = s3_bands.replace("#### 2.2", "#### 3.2")
    s3_bands = s3_bands.replace("#22-positive", "#32-positive")
    s3_bands = s3_bands.replace("#### 2.3", "#### 3.3")
    s3_bands = s3_bands.replace("#23-stewardship", "#33-stewardship")
    s3_bands = s3_bands.replace("#### 2.4", "#### 3.4")
    s3_bands = s3_bands.replace("#24-positive", "#34-positive")
    s3_bands = s3_bands.replace("#### 2.5", "#### 3.5")
    s3_bands = s3_bands.replace("#25-restrictive", "#35-restrictive")
    s3_bands = s3_bands.replace("#### 2.6", "#### 3.6")
    s3_bands = s3_bands.replace("#26-reinstatement", "#36-reinstatement")
    s3_bands = s3_bands.replace("[§2](#2-axis-i-contribution-state-and-standing-effect)", "[§3](#3-axis-i-contribution-state)")
    s3_bands = s3_bands.replace("[§2.0](#20-scope-contribution-state-and-standing-effect)", "[§3.0](#30-scope-contribution-state-axis-i)")
    s3_bands = s3_bands.replace("[§2.7](#27-standing-integration-contribution-and-violation-nature)", "[§2.6](#26-standing-integration-contribution-and-violation-nature)")
    for a, b in [("2.1", "3.1"), ("2.2", "3.2"), ("2.3", "3.3"), ("2.4", "3.4"), ("2.5", "3.5"), ("2.6", "3.6")]:
        s3_bands = s3_bands.replace(f"[§{a}](#", f"[§{b}](#")
    s3_bands = s3_bands.replace("**section 3.1**", "**section 4.1**")  # Formal in 2.5 trace
    s3_bands = s3_bands.replace("[§3.1](#31-formal-non-compliance)", "[§4.1](#41-formal-non-compliance)")

    s3_8 = lines_slice(lines, 532, 573)
    s3_8 = s3_8.replace("#### 2.8", "#### 3.7")
    s3_8 = s3_8.replace("28-stackable", "37-stackable")
    s3_8 = s3_8.replace("212-stackable", "37-stackable-alt")
    s3_8 = s3_8.replace("[§2.7](#27-standing-integration-contribution-and-violation-nature)", "[§2.6](#26-standing-integration-contribution-and-violation-nature)")
    s3_8 = s3_8.replace("[§3.13](#313-non-exclusive-harm-and-conduct-descriptors)", "[§4.13](#413-non-exclusive-harm-and-conduct-descriptors)")
    s3_8 = s3_8.replace("[§1.2](#12-shared-domain-lenses-cross-axis-vocabulary)", "[§5](#5-shared-domain-lenses-cross-axis-vocabulary)")
    s3_8 = s3_8.replace("[§2.1](#21-baseline-contribution)–[§2.3](#23-stewardship-positive-contribution)", "[§3.1](#31-baseline-contribution)–[§3.3](#33-stewardship-positive-contribution)")
    s3_8 = s3_8.replace("[§4](#4-cross-axis-coupling-and-escalation-constraints)", "[§6](#6-cross-axis-coupling-and-escalation-constraints)")
    s3_8 = s3_8.replace("**sections 2.4 and 2.6**", "**sections 3.4 and 3.6**")
    s3_8 = s3_8.replace("**section 2.7**", "**section 2.6**")
    s3_8 = s3_8.replace("**sections 2.1 through 2.3**", "**sections 3.1 through 3.3**")
    s3_8 = s3_8.replace("**sections 3.5 through 3.7**", "**sections 4.5 through 4.7**")
    s3_8 = s3_8.replace("**section 3**", "**section 4**")
    s3_8 = s3_8.replace("**§1.2**", "**§5**")
    s3_8 = s3_8.replace("**§3.5**", "**§4.5**")
    s3_8 = s3_8.replace("**§3.13**", "**§4.13**")
    s3_8 = s3_8.replace("**sections 2.2 through 2.4**", "**sections 3.2 through 3.4**")
    s3_8 = s3_8.replace("**section 4** when", "**section 6** when")

    plain3 = lines_slice(lines, 177, 179)
    plain3 = plain3.replace("**section 1**", "**section 2**")
    plain3 = plain3.replace("**section 3**", "**section 4**")

    section3 = plain3 + s3_head + s3_01 + s3_bands + s3_8

    # --- §4 old §3: lines 575-939
    s4 = lines_slice(lines, 575, 939)
    s4 = s4.replace("### 3. Violation Nature", "### 4. Violation nature (Violation Axis)")
    s4 = s4.replace("<a id=\"3-axis-ii-violation-nature-legal-constitutional-type\"></a>", "<a id=\"4-axis-ii-violation-nature-legal-constitutional-type\"></a>\n<a id=\"3-axis-ii-violation-nature-legal-constitutional-type\"></a>")
    s4 = s4.replace("#### 3.", "#### 4.")
    # subsection anchors 3.1 -> 4.1 slug: replace #31- with #41- etc.
    repl = [
        ("#31-formal-non-compliance", "#41-formal-non-compliance"),
        ("#32-substantive-non-compliance", "#42-substantive-non-compliance"),
        ("#33-aggravated-non-compliance", "#43-aggravated-non-compliance"),
        ("#34-critical-non-compliance", "#44-critical-non-compliance"),
        ("#35-civil-violation", "#45-civil-violation"),
        ("#36-criminal-violation", "#46-criminal-violation"),
        ("#37-constitutional-violation", "#47-constitutional-violation"),
        ("#38-concurrent-and-hybrid-violations", "#48-concurrent-and-hybrid-violations"),
        ("#39-constitutional-floor-rule", "#49-constitutional-floor-rule"),
        ("#310-collective-accountability-and-acquiescent-participation", "#410-collective-accountability-and-acquiescent-participation"),
        ("#311-duty-to-resist-unlawful-or-unconstitutional-instructions", "#411-duty-to-resist-unlawful-or-unconstitutional-instructions"),
        ("#312-negligence-and-neglect-as-violation-nature", "#412-negligence-and-neglect-as-violation-nature"),
        ("#313-non-exclusive-harm-and-conduct-descriptors", "#413-non-exclusive-harm-and-conduct-descriptors"),
    ]
    for o, n in repl:
        s4 = s4.replace(o, n)
    s4 = s4.replace("<a id=\"31-formal-non-compliance\">", "<a id=\"41-formal-non-compliance\">\n<a id=\"31-formal-non-compliance\">")
    s4 = s4.replace("<a id=\"35-civil-violation\">", "<a id=\"45-civil-violation\">\n<a id=\"35-civil-violation\">")
    s4 = s4.replace("<a id=\"310-", "<a id=\"410-")
    s4 = s4.replace("<a id=\"311-", "<a id=\"411-")
    s4 = s4.replace("<a id=\"312-", "<a id=\"412-")
    s4 = s4.replace("<a id=\"313-", "<a id=\"413-")
    s4 = s4.replace("<a id=\"39-non-exclusive", "<a id=\"413-non-exclusive-alt\">\n<a id=\"39-non-exclusive")

    s4 = s4.replace("§3.", "§4.")
    s4 = s4.replace("[§2](#2-axis-i-contribution-state-and-standing-effect) through [§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)", "[§3](#3-axis-i-contribution-state) through [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)")
    s4 = s4.replace("[§1.1](#11-two-axis-overview-reference)", "[§1.1](#11-chapter-layout-and-reading-order)")
    s4 = s4.replace("[§1.2](#12-shared-domain-lenses-cross-axis-vocabulary)", "[§5](#5-shared-domain-lenses-cross-axis-vocabulary)")
    s4 = s4.replace("[§4](#4-cross-axis-coupling-and-escalation-constraints)", "[§6](#6-cross-axis-coupling-and-escalation-constraints)")
    s4 = s4.replace("**sections 2.7** and **4**", "**sections 2.6** and **6**")
    s4 = s4.replace("[§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)", "[§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)")
    s4 = s4.replace("**section 2**", "**section 3**")
    s4 = s4.replace("**§1.2**", "**§5**")
    s4 = s4.replace("**§2.8**", "**§3.7**")
    s4 = s4.replace("**§3.5**", "**§4.5**")
    s4 = s4.replace("[§2.5](#25-restrictive-standing-effects)", "[§3.5](#35-restrictive-standing-effects)")
    s4 = s4.replace("[§6](#6-enforcement-realism-anchors)", "[§8](#8-enforcement-realism-anchors)")
    s4 = s4.replace("[§7](#7-tiered-anti-constitutional-misconduct-authoritative-location)", "[§9](#9-tiered-anti-constitutional-misconduct-authoritative-location)")

    # --- §5 domain lenses: old 126-151
    s5 = lines_slice(lines, 126, 151)
    s5 = s5.replace("### 1.2 Shared domain lenses", "### 5. Shared domain lenses (cross-axis vocabulary)")
    s5 = s5.replace(
        "- Upstream: [§1](#1-purpose-and-role) (*purpose and two-axis frame*); [§1.1](#11-two-axis-overview-reference) (*how **sections 2** and **3** fit*).",
        "- Upstream: [§1](#1-purpose-and-role) (*purpose and two-axis frame*); [§1.1](#11-chapter-layout-and-reading-order) (*reading order*); [§3](#3-axis-i-contribution-state)–[§4](#4-axis-ii-violation-nature) (*primary typing*).",
    )
    s5 = s5.replace(
        "- Downstream: [§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*Contribution Axis prosocial supplements named in this table*); [§3.13](#313-non-exclusive-harm-and-conduct-descriptors) (*Violation Axis adverse supplements named in this table*); [§4](#4-cross-axis-coupling-and-escalation-constraints) (*joint assessment — no netting*).",
        "- Downstream: [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*Contribution Axis supplements named in this table*); [§4.13](#413-non-exclusive-harm-and-conduct-descriptors) (*Violation Axis supplements named in this table*); [§6](#6-cross-axis-coupling-and-escalation-constraints) (*joint assessment — no netting*).",
    )
    s5 = s5.replace("[§5](#5-additive-and-non-substitution-rule)", "[§7](#7-additive-and-non-substitution-rule)")
    s5 = s5.replace(
        "The binding text this table refers to is in [**section 2**](#2-axis-i-contribution-state-and-standing-effect) and [**section 3**](#3-axis-ii-violation-nature-legal-constitutional-type).",
        "The binding text this table refers to is in [**section 3**](#3-axis-i-contribution-state) and [**section 4**](#4-axis-ii-violation-nature-legal-constitutional-type).",
    )
    s5 = s5.replace("[§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)", "[§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)")
    s5 = s5.replace("[§3.13](#313-non-exclusive-harm-and-conduct-descriptors)", "[§4.13](#413-non-exclusive-harm-and-conduct-descriptors)")
    s5 = s5.replace("**§§2.2–2.4**", "**§§3.2–3.4**")
    s5 = s5.replace("[§3.12](#312-negligence-and-neglect-as-violation-nature)", "[§4.12](#412-negligence-and-neglect-as-violation-nature)")
    s5 = s5.replace("<a id=\"12-shared-domain-lenses-cross-axis-vocabulary\"></a>", "<a id=\"5-shared-domain-lenses-cross-axis-vocabulary\"></a>\n<a id=\"12-shared-domain-lenses-cross-axis-vocabulary\"></a>")

    # --- §6-9
    s6 = lines_slice(lines, 941, 987)
    s6 = s6.replace("### 4.", "### 6.")
    s6 = s6.replace("<a id=\"4-cross-axis-coupling-and-escalation-constraints\"></a>", "<a id=\"6-cross-axis-coupling-and-escalation-constraints\"></a>\n<a id=\"4-cross-axis-coupling-and-escalation-constraints\"></a>")
    s6 = s6.replace("[§5](#5-additive-and-non-substitution-rule)", "[§7](#7-additive-and-non-substitution-rule)")
    s6 = s6.replace("[§6](#6-enforcement-realism-anchors)", "[§8](#8-enforcement-realism-anchors)")
    s6 = s6.replace(
        "Upstream: [§2](#2-axis-i-contribution-state-and-standing-effect) through [§3](#3-axis-ii-violation-nature-legal-constitutional-type) (*contribution state and violation nature*); [§1.2](#12-shared-domain-lenses-cross-axis-vocabulary) (*cross-axis domain lens vocabulary*); [§2.8](#28-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*contribution-state supplemental descriptors*); [§3.13](#313-non-exclusive-harm-and-conduct-descriptors) (*violation-nature supplemental descriptors read with dominant-purpose routing*).",
        "Upstream: [§3](#3-axis-i-contribution-state) through [§4](#4-axis-ii-violation-nature) (*contribution state and violation nature*); [§5](#5-shared-domain-lenses-cross-axis-vocabulary) (*cross-axis domain lens vocabulary*); [§3.7](#37-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) (*contribution-state supplemental descriptors*); [§4.13](#413-non-exclusive-harm-and-conduct-descriptors) (*violation-nature supplemental descriptors read with dominant-purpose routing*).",
    )
    s6 = s6.replace("**section 4**", "SECTION4_PLACEHOLDER")
    s6 = s6.replace("**sections 2**", "**sections 3**")
    s6 = s6.replace("**sections 3.1", "**sections 4.1")
    s6 = s6.replace("**sections 3.", "**sections 4.")
    s6 = s6.replace("SECTION4_PLACEHOLDER", "**section 6**")
    s6 = s6.replace("**sections 2.1 through 2.3**", "**sections 3.1 through 3.3**")
    s6 = s6.replace("**sections 2.4 through 2.7**", "**sections 3.4 through 3.6** read with [**section 2**](#2-standing-forums-and-verified-inputs)")
    s6 = s6.replace("**section 1.2**", "**section 5**")
    s6 = s6.replace("**sections 2.8** and **3.13**", "**sections 3.7** and **4.13**")
    s6 = s6.replace("**section 3.8**", "**section 4.8**")

    s7 = lines_slice(lines, 988, 1023)
    s7 = s7.replace("### 5.", "### 7.")
    s7 = s7.replace("<a id=\"5-additive-and-non-substitution-rule\"></a>", "<a id=\"7-additive-and-non-substitution-rule\"></a>\n<a id=\"5-additive-and-non-substitution-rule\"></a>")
    s7 = s7.replace("[§4](#4-cross-axis-coupling-and-escalation-constraints)", "[§6](#6-cross-axis-coupling-and-escalation-constraints)")
    s7 = s7.replace("[§6](#6-enforcement-realism-anchors)", "[§8](#8-enforcement-realism-anchors)")
    s7 = s7.replace("[§2.7](#27-standing-integration-contribution-and-violation-nature)", "[§2.6](#26-standing-integration-contribution-and-violation-nature)")
    s7 = s7.replace("**section 2.7**", "**section 2.6**")
    s7 = s7.replace("**section 4**", "**section 6**")

    s8 = lines_slice(lines, 1024, 1054)
    s8 = s8.replace("### 6.", "### 8.")
    s8 = s8.replace("<a id=\"6-enforcement-realism-anchors\"></a>", "<a id=\"8-enforcement-realism-anchors\"></a>\n<a id=\"6-enforcement-realism-anchors\"></a>")
    s8 = s8.replace("[§4](#4-cross-axis-coupling-and-escalation-constraints) and [§5](#5-additive-and-non-substitution-rule)", "[§6](#6-cross-axis-coupling-and-escalation-constraints) and [§7](#7-additive-and-non-substitution-rule)")
    s8 = s8.replace("[section 2.7](#27-standing-integration-contribution-and-violation-nature)", "[section 2.6](#26-standing-integration-contribution-and-violation-nature)")
    s8 = s8.replace("**sections 3.1 through 3.4**", "**sections 4.1 through 4.4**")
    s8 = s8.replace("**section 2**", "**section 3**")

    s9 = lines_slice(lines, 1055, 1081)
    s9 = s9.replace("### 7.", "### 9.")
    s9 = s9.replace("<a id=\"7-tiered-anti-constitutional-misconduct-authoritative-location\"></a>", "<a id=\"9-tiered-anti-constitutional-misconduct-authoritative-location\"></a>\n<a id=\"7-tiered-anti-constitutional-misconduct-authoritative-location\"></a>")
    s9 = s9.replace("[§4](#4-cross-axis-coupling-and-escalation-constraints)", "[§6](#6-cross-axis-coupling-and-escalation-constraints)")
    s9 = s9.replace("This **Chapter Six** section **7**", "This **Chapter Six** section **9**")

    out = (
        preamble
        + "\n"
        + s1
        + "\n"
        + s11
        + "\n"
        + section2
        + "\n"
        + section3
        + "\n"
        + s4
        + "\n"
        + s5
        + "\n"
        + s6
        + "\n"
        + s7
        + "\n"
        + s8
        + "\n"
        + s9
    )

    # Legacy anchors for old 2.7
    out = out.replace(
        '<a id="27-standing-integration-contribution-and-violation-nature"></a>',
        '<a id="27-standing-integration-contribution-and-violation-nature"></a>\n<a id="legacy-27-standing-integration-see-26"></a>',
    )

    SRC.write_text(out, encoding="utf-8")
    print("Wrote", SRC, "backup at", BAK)


if __name__ == "__main__":
    main()
