#!/usr/bin/env python3
"""Reading Arc B: Freedom after Trust; Evaluation §15 + Integrated §16 capstone in Part B."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_A = ROOT / "core_01_a_values_principles.md"
PART_B = ROOT / "core_01_b_stewardship_capacity_principles.md"

PART_A_HEADER = """# Values Principles (Chapter One, Part A)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part A** (§§1–8: purpose, values, bounded agency, tradeoffs, override prohibition, and constitutional interpretation).
>
> **Upstream:** [core_00_preamble.md](core_00_preamble.md)  
> **Next:** [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md) (Chapter One, Part B — §§11–16, including systemic evaluation and integrated application capstone).

</details>

<br>

---
## CHAPTER 01, PART A: VALUES PRINCIPLES

"""

PART_B_HEADER = """# Stewardship and Governance (Chapter One, Part B)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part B** (§§11–16: stewardship, governance, capacity, market structure, systemic evaluation, and integrated application capstone).
>
> **Upstream:** [core_01_a_values_principles.md](core_01_a_values_principles.md) (Chapter One, Part A)  
> **Next:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)<br>
> **Reading arc:** §11 stewardship → §12 governance → §13 capacity → §14 market structure → §15 systemic evaluation → **§16 integrated application** (chapter capstone).

</details>

<br>

---
<a id="chapter-01-part-b-stewardship-and-governance"></a>
## CHAPTER 01, PART B: STEWARDSHIP AND GOVERNANCE

**Principle hierarchy (Part B).** At principle layer:

1. **[Stewardship](core_05defs_continuity.md#stewardship-constitutional)** orients systems toward durable constitutional alignment over time, including the **Continuity** aim under the [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims).
2. **[Governance](core_05defs_accountability.md#governance)** structures authorized decision-making, participation, and accountability under the [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) — especially **[Oversight](core_05apex_oversight_leg.md#oversight-constitutional)** of how authority is allocated and exercised. Where governance and stewardship conflict, stewardship discipline controls at principle layer unless **Necessity** and **Proportionality** expressly justify a bounded, time-limited exception with correction paths. Operative authorization and contract-layer requirements remain owned by **Chapter Twelve**.
3. **[Shared-System Capacity](core_05defs_continuity.md#shared-system-capacity-constitutional)** is the durable, contestable ability those jointly produce — an **instrumental outcome** toward the **Flourishing** aim under the [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims), not a freestanding trump value. **[Market Structure](core_05defs_accountability.md#market-structure-constitutional)** at [§14](#14-market-structure) supplies the anti-concentration discipline that keeps that capacity contestable in practice.
4. **[Systemic Evaluation Requirement](#15-systemic-evaluation-requirement)** verifies whole-system scope, dependency, and incentive alignment before compliance or governance claims stand.
5. **[Integrated Application](#16-integrated-application)** is the chapter capstone: later chapters are read through this chapter's integrated-value framework.

"""

LEGACY_PART_A = """
<!-- Legacy Chapter One Part A anchor redirects; do not remove without link migration. -->
<a id="2-constitutional-interpretation"></a>
<a id="21-definitional-layer-and-required-disciplines"></a>
<a id="22-ambiguity-resolution"></a>
<a id="23-conflict-resolution-procedure"></a>
<a id="3-foundational-objective-wellbeing"></a>
<a id="41-safety-harm-constraint"></a>
<a id="42-truth-epistemic-integrity-constraint"></a>
<a id="5-system-stability-enabler-trust-coordination-integrity"></a>
<a id="51-resilience-and-self-healing-design"></a>
<a id="5-interaction-and-conflict-resolution"></a>
<a id="51-core-tradeoff-principles"></a>
<a id="511-proportionality"></a>
<a id="512-necessity"></a>
<a id="513-minimization-of-harm"></a>
<a id="514-minimization-of-avoidable-burden"></a>
<a id="52-epistemic-disclosure-constraints"></a>
<a id="521-preservation-of-epistemic-integrity"></a>
<a id="522-trust-truth-alignment"></a>
<a id="53-freedom-limitation-constraints"></a>
<a id="531-constraint-on-freedom"></a>
<a id="532-time-consistency-constraint"></a>
<a id="54-rights-collision-procedure"></a>
<a id="541-rights-collision-decision-test"></a>
<a id="542-proxy-divergence-invalidation"></a>
<a id="6-systemic-evaluation-requirement"></a>
<a id="61-required-evaluation-factors"></a>
<a id="62-read-with-governance-and-incentive-discipline"></a>
<a id="7-freedom-bounded-agency"></a>
<a id="8-prohibition-on-absolute-override"></a>
<a id="9-constitutional-interpretation"></a>
<a id="91-definitional-layer-and-required-disciplines"></a>
<a id="92-ambiguity-resolution"></a>
<a id="93-conflict-resolution-procedure"></a>
<a id="10-integrated-application"></a>

"""

_TO_PH: list[tuple[str, str]] = [
    ("Chapter One §10 Integrated Application", "__CH1S16INT__"),
    ("Chapter One §10 Integrated", "__CH1S16INT__"),
    ("Chapter One §9.3.3", "__CH1S833__"),
    ("Chapter One §9.3.2", "__CH1S832__"),
    ("Chapter One §9.3.1", "__CH1S831__"),
    ("Chapter One §9.3", "__CH1S83__"),
    ("Chapter One §9.2", "__CH1S82__"),
    ("Chapter One §9.1", "__CH1S81__"),
    ("Chapter One §9 Constitutional Interpretation", "__CH1S8INT__"),
    ("Chapter One §9 Constitutional", "__CH1S8INT__"),
    ("Chapter One §8 Prohibition on Absolute Override", "__CH1S7PROH__"),
    ("Chapter One §8 Prohibition", "__CH1S7PROH__"),
    ("Chapter One §7 Freedom (Bounded Agency)", "__CH1S5FREE__"),
    ("Chapter One §7 Freedom", "__CH1S5FREE__"),
    ("Chapter One §6.2", "__CH1S152__"),
    ("Chapter One §6.1.5", "__CH1S1515__"),
    ("Chapter One §6.1.4", "__CH1S1514__"),
    ("Chapter One §6.1.3", "__CH1S1513__"),
    ("Chapter One §6.1.2", "__CH1S1512__"),
    ("Chapter One §6.1.1", "__CH1S1511__"),
    ("Chapter One §6.1", "__CH1S151__"),
    ("Chapter One §6 Systemic Evaluation Requirement", "__CH1S15EV__"),
    ("Chapter One §6 Systemic Evaluation", "__CH1S15EV__"),
    ("Chapter One §6 Systemic", "__CH1S15EV__"),
    ("Chapter One §5.4.2", "__CH1S642__"),
    ("Chapter One §5.4.1", "__CH1S641__"),
    ("Chapter One §5.4", "__CH1S64__"),
    ("Chapter One §5.3.2", "__CH1S632__"),
    ("Chapter One §5.3.1", "__CH1S631__"),
    ("Chapter One §5.3", "__CH1S63__"),
    ("Chapter One §5.2.2", "__CH1S622__"),
    ("Chapter One §5.2.1", "__CH1S621__"),
    ("Chapter One §5.2", "__CH1S62__"),
    ("Chapter One §5.1.4", "__CH1S614__"),
    ("Chapter One §5.1.3", "__CH1S613__"),
    ("Chapter One §5.1.2", "__CH1S612__"),
    ("Chapter One §5.1.1", "__CH1S611__"),
    ("Chapter One §5.1", "__CH1S61__"),
    ("Chapter One §5 Interaction and Conflict Resolution", "__CH1S6INT__"),
    ("Chapter One §5 Interaction", "__CH1S6INT__"),
    ("§10 Integrated Application", "__CH1S16INT__"),
    ("§10 Integrated", "__CH1S16INT__"),
    ("§9.3.3", "__CH1S833__"),
    ("§9.3.2", "__CH1S832__"),
    ("§9.3.1", "__CH1S831__"),
    ("§9.3", "__CH1S83__"),
    ("§9.2", "__CH1S82__"),
    ("§9.1", "__CH1S81__"),
    ("§9 Constitutional Interpretation", "__CH1S8INT__"),
    ("§9 Constitutional", "__CH1S8INT__"),
    ("§8 Prohibition on Absolute Override", "__CH1S7PROH__"),
    ("§8 Prohibition", "__CH1S7PROH__"),
    ("§7 Freedom (Bounded Agency)", "__CH1S5FREE__"),
    ("§7 Freedom", "__CH1S5FREE__"),
    ("§6.2", "__CH1S152__"),
    ("§6.1.5", "__CH1S1515__"),
    ("§6.1.4", "__CH1S1514__"),
    ("§6.1.3", "__CH1S1513__"),
    ("§6.1.2", "__CH1S1512__"),
    ("§6.1.1", "__CH1S1511__"),
    ("§6.1", "__CH1S151__"),
    ("§6 Systemic Evaluation Requirement", "__CH1S15EV__"),
    ("§6 Systemic Evaluation", "__CH1S15EV__"),
    ("§6 Systemic", "__CH1S15EV__"),
    ("§5.4.2", "__CH1S642__"),
    ("§5.4.1", "__CH1S641__"),
    ("§5.4", "__CH1S64__"),
    ("§5.3.2", "__CH1S632__"),
    ("§5.3.1", "__CH1S631__"),
    ("§5.3", "__CH1S63__"),
    ("§5.2.2", "__CH1S622__"),
    ("§5.2.1", "__CH1S621__"),
    ("§5.2", "__CH1S62__"),
    ("§5.1.4", "__CH1S614__"),
    ("§5.1.3", "__CH1S613__"),
    ("§5.1.2", "__CH1S612__"),
    ("§5.1.1", "__CH1S611__"),
    ("§5.1", "__CH1S61__"),
    ("§5 Interaction and Conflict Resolution", "__CH1S6INT__"),
    ("§5 Interaction", "__CH1S6INT__"),
]

_FROM_PH: list[tuple[str, str]] = [
    ("__CH1S16INT__", "Chapter One §16 Integrated Application"),
    ("__CH1S833__", "Chapter One §8.3.3"),
    ("__CH1S832__", "Chapter One §8.3.2"),
    ("__CH1S831__", "Chapter One §8.3.1"),
    ("__CH1S83__", "Chapter One §8.3"),
    ("__CH1S82__", "Chapter One §8.2"),
    ("__CH1S81__", "Chapter One §8.1"),
    ("__CH1S8INT__", "Chapter One §8 Constitutional Interpretation"),
    ("__CH1S7PROH__", "Chapter One §7 Prohibition on Absolute Override"),
    ("__CH1S5FREE__", "Chapter One §5 Freedom"),
    ("__CH1S152__", "Chapter One §15.2"),
    ("__CH1S1515__", "Chapter One §15.1.5"),
    ("__CH1S1514__", "Chapter One §15.1.4"),
    ("__CH1S1513__", "Chapter One §15.1.3"),
    ("__CH1S1512__", "Chapter One §15.1.2"),
    ("__CH1S1511__", "Chapter One §15.1.1"),
    ("__CH1S151__", "Chapter One §15.1"),
    ("__CH1S15EV__", "Chapter One §15 Systemic Evaluation Requirement"),
    ("__CH1S642__", "Chapter One §6.4.2"),
    ("__CH1S641__", "Chapter One §6.4.1"),
    ("__CH1S64__", "Chapter One §6.4"),
    ("__CH1S632__", "Chapter One §6.3.2"),
    ("__CH1S631__", "Chapter One §6.3.1"),
    ("__CH1S63__", "Chapter One §6.3"),
    ("__CH1S622__", "Chapter One §6.2.2"),
    ("__CH1S621__", "Chapter One §6.2.1"),
    ("__CH1S62__", "Chapter One §6.2"),
    ("__CH1S614__", "Chapter One §6.1.4"),
    ("__CH1S613__", "Chapter One §6.1.3"),
    ("__CH1S612__", "Chapter One §6.1.2"),
    ("__CH1S611__", "Chapter One §6.1.1"),
    ("__CH1S61__", "Chapter One §6.1"),
    ("__CH1S6INT__", "Chapter One §6 Interaction and Conflict Resolution"),
]

ANCHOR_PATH_MIGRATIONS: list[tuple[str, str]] = [
    ("core_01_a_values_principles.md#10-integrated-application", "core_01_b_stewardship_capacity_principles.md#16-integrated-application"),
    ("core_01_a_values_principles.md#6-systemic-evaluation-requirement", "core_01_b_stewardship_capacity_principles.md#15-systemic-evaluation-requirement"),
    ("core_01_a_values_principles.md#61-required-evaluation-factors", "core_01_b_stewardship_capacity_principles.md#151-required-evaluation-factors"),
    ("core_01_a_values_principles.md#62-read-with-governance-and-incentive-discipline", "core_01_b_stewardship_capacity_principles.md#152-read-with-governance-and-incentive-discipline"),
    ("core_01_a_values_principles.md#5-interaction-and-conflict-resolution", "core_01_a_values_principles.md#6-interaction-and-conflict-resolution"),
    ("core_01_a_values_principles.md#7-freedom-bounded-agency", "core_01_a_values_principles.md#5-freedom-bounded-agency"),
    ("core_01_a_values_principles.md#8-prohibition-on-absolute-override", "core_01_a_values_principles.md#7-prohibition-on-absolute-override"),
    ("core_01_a_values_principles.md#9-constitutional-interpretation", "core_01_a_values_principles.md#8-constitutional-interpretation"),
    ("#10-integrated-application", "#16-integrated-application"),
    ("#6-systemic-evaluation-requirement", "#15-systemic-evaluation-requirement"),
    ("#61-required-evaluation-factors", "#151-required-evaluation-factors"),
    ("#62-read-with-governance-and-incentive-discipline", "#152-read-with-governance-and-incentive-discipline"),
    ("#611-systemic-scope-and-risk-factors", "#1511-systemic-scope-and-risk-factors"),
    ("#612-accessibility-under-sentience-non-exclusion", "#1512-accessibility-under-sentience-non-exclusion"),
    ("#613-privacy-informational-joint-invocation", "#1513-privacy-informational-joint-invocation"),
    ("#614-voluntary-discontinuation-and-exit-rights", "#1514-voluntary-discontinuation-and-exit-rights"),
    ("#615-assembly-collective-organization-and-institutional-formation", "#1515-assembly-collective-organization-and-institutional-formation"),
    ("#5-interaction-and-conflict-resolution", "#6-interaction-and-conflict-resolution"),
    ("#51-core-tradeoff-principles", "#61-core-tradeoff-principles"),
    ("#511-proportionality", "#611-proportionality"),
    ("#512-necessity", "#612-necessity"),
    ("#513-minimization-of-harm", "#613-minimization-of-harm"),
    ("#514-minimization-of-avoidable-burden", "#614-minimization-of-avoidable-burden"),
    ("#52-epistemic-disclosure-constraints", "#62-epistemic-disclosure-constraints"),
    ("#521-preservation-of-epistemic-integrity", "#621-preservation-of-epistemic-integrity"),
    ("#522-trust-truth-alignment", "#622-trust-truth-alignment"),
    ("#53-freedom-limitation-constraints", "#63-freedom-limitation-constraints"),
    ("#531-constraint-on-freedom", "#631-constraint-on-freedom"),
    ("#532-time-consistency-constraint", "#632-time-consistency-constraint"),
    ("#54-rights-collision-procedure", "#64-rights-collision-procedure"),
    ("#541-rights-collision-decision-test", "#641-rights-collision-decision-test"),
    ("#542-proxy-divergence-invalidation", "#642-proxy-divergence-invalidation"),
    ("#7-freedom-bounded-agency", "#5-freedom-bounded-agency"),
    ("#8-prohibition-on-absolute-override", "#7-prohibition-on-absolute-override"),
    ("#9-constitutional-interpretation", "#8-constitutional-interpretation"),
    ("#91-definitional-layer-and-required-disciplines", "#81-definitional-layer-and-required-disciplines"),
    ("#92-ambiguity-resolution", "#82-ambiguity-resolution"),
    ("#93-conflict-resolution-procedure", "#83-conflict-resolution-procedure"),
    ("#931-integrated-reading", "#831-integrated-reading"),
    ("#932-last-resort-internal-hierarchy", "#832-last-resort-internal-hierarchy"),
    ("#933-incorporation-layer", "#833-incorporation-layer"),
]


def extract_h3_section(text: str, section_num: int) -> tuple[str, str]:
    pattern = re.compile(rf"^### {section_num}\. .+$", re.M)
    m = pattern.search(text)
    if not m:
        raise ValueError(f"section ### {section_num}. not found")
    start = m.start()
    rest = text[m.end() :]
    next_m = re.search(r"^### (?:\d+\.|Reference:)", rest, re.M)
    end = m.end() + (next_m.start() if next_m else len(rest))
    return text[start:end], text[end:]


def renumber_section_block(block: str, old_sec: int, new_sec: int) -> str:
    if old_sec == new_sec:
        return block
    os, ns = str(old_sec), str(new_sec)
    for level in ("#####", "####", "###"):
        block = re.sub(rf"^{level} {os}\.", f"{level} {ns}.", block, flags=re.M)
    suffixes = sorted(
        {m.group(1) for m in re.finditer(rf"§{os}\.(\d+(?:\.\d+)*)", block)},
        key=len,
        reverse=True,
    )
    for suf in suffixes:
        block = block.replace(f"§{os}.{suf}", f"§{ns}.{suf}")
    block = re.sub(rf"§{os}\b", f"§{ns}", block)

    def hash_link(m: re.Match[str]) -> str:
        label, anchor = m.group(1), m.group(2)
        if re.match(rf"^{os}(\d|$|-)", anchor):
            return f"[{label}](#{ns}{anchor[len(os):]})"
        return m.group(0)

    block = re.sub(r"\[([^\]]+)\]\(#(\d[^)]*)\)", hash_link, block)

    def anchor_id(m: re.Match[str]) -> str:
        aid = m.group(1)
        if re.match(rf"^{os}(\d|-)", aid):
            return f'<a id="{ns}{aid[len(os):]}"></a>'
        return m.group(0)

    block = re.sub(r'<a id="(\d[^"]*)"></a>', anchor_id, block)
    return block


def split_at_chapter(text: str) -> tuple[str, str]:
    idx = text.find("## CHAPTER 01")
    if idx == -1:
        raise ValueError("chapter heading not found")
    chapter_start = text.find("\n", idx)
    return text[:chapter_start], text[chapter_start + 1 :]


def strip_file_footer(block: str) -> str:
    return re.sub(
        r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n?",
        "\n",
        block,
    )


def reassemble_part_a(part_a: str) -> str:
    _, body = split_at_chapter(part_a)
    s1, rest = extract_h3_section(body, 1)
    s2, rest = extract_h3_section(rest, 2)
    s3, rest = extract_h3_section(rest, 3)
    s4, rest = extract_h3_section(rest, 4)
    s5_int, rest = extract_h3_section(rest, 5)
    _s6, rest = extract_h3_section(rest, 6)
    s7_free, rest = extract_h3_section(rest, 7)
    s8_ov, rest = extract_h3_section(rest, 8)
    s9_intp, rest = extract_h3_section(rest, 9)
    _s10, rest = extract_h3_section(rest, 10)
    ref_idx = rest.find("### Reference:")
    reference = rest[ref_idx:].split("---")[0].rstrip() + "\n" if ref_idx != -1 else ""

    s7_free = renumber_section_block(s7_free, 7, 5)
    s5_int = renumber_section_block(s5_int, 5, 6)
    s8_ov = renumber_section_block(s8_ov, 8, 7)
    s9_intp = renumber_section_block(s9_intp, 9, 8)

    footer = """
---

**Previous file:** [core_00_preamble.md](core_00_preamble.md)

**Next file:** [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md)
"""
    return PART_A_HEADER + LEGACY_PART_A + s1 + s2 + s3 + s4 + s7_free + s5_int + s8_ov + s9_intp + reference + footer


def reassemble_part_b(part_a: str, part_b: str) -> str:
    _, abody = split_at_chapter(part_a)
    s6_eval, _ = extract_h3_section(abody, 6)
    s10_int, _ = extract_h3_section(abody, 10)

    _, bbody = split_at_chapter(part_b)
    idx = bbody.find("### 11.")
    bbody = bbody[idx:] if idx != -1 else bbody
    bbody = strip_file_footer(bbody)
    bbody = re.sub(r"\n<a id=\"10-interaction-and-conflict-resolution\"></a>\n?", "\n", bbody)

    s6_eval = renumber_section_block(s6_eval, 6, 15)
    s10_int = renumber_section_block(s10_int, 10, 16)

    legacy = part_b.split("### 11.")[0]
    legacy_block = legacy[legacy.find("<!-- Legacy") :] if "<!-- Legacy" in legacy else ""

    footer = """
---

**Previous file:** [core_01_a_values_principles.md](core_01_a_values_principles.md)

**Next file:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)
"""
    return PART_B_HEADER + legacy_block + bbody.rstrip() + "\n\n" + s6_eval + s10_int + footer


def apply_trace_repairs_part_a(text: str) -> str:
    repl = [
        ("§§1–10", "§§1–8"),
        ("[§5 Interaction and Conflict Resolution](#5-interaction", "[§6 Interaction and Conflict Resolution](#6-interaction"),
        ("[5. Interaction and Conflict Resolution](#5-interaction", "[6. Interaction and Conflict Resolution](#6-interaction"),
        ("[§7 Freedom](#7-freedom", "[§5 Freedom](#5-freedom"),
        ("[7. Freedom](#7-freedom", "[5. Freedom](#5-freedom"),
        ("[§8 Prohibition", "[§7 Prohibition"),
        ("[8. Prohibition", "[7. Prohibition"),
        ("[§9 Constitutional", "[§8 Constitutional"),
        ("[9. Constitutional Interpretation](#9-constitutional", "[8. Constitutional Interpretation](#8-constitutional"),
        ("[10. Integrated Application](#10-integrated", "[16. Integrated Application](core_01_b_stewardship_capacity_principles.md#16-integrated-application)"),
        ("[6.1 Required Evaluation Factors](#61-", "[15.1 Required Evaluation Factors](core_01_b_stewardship_capacity_principles.md#151-"),
        ("[§6 Systemic Evaluation Requirement](#6-systemic", "[§15 Systemic Evaluation Requirement](core_01_b_stewardship_capacity_principles.md#15-systemic"),
        ("Downstream: [7.2.1 Preservation", "Downstream: [6.2.1 Preservation"),
        ("[7.2.1 Preservation", "[6.2.1 Preservation"),
        ("[7.2.2 Trust-Truth", "[6.2.2 Trust-Truth"),
        ("[§7.3 Preservation", "[§6.2.1 Preservation"),
        ("[§7.4 Trust-Truth", "[§6.2.2 Trust-Truth"),
        ("[§5.4.1 Rights-Collision Decision Test](#541-", "[§6.4.1 Rights-Collision Decision Test](#641-"),
        ("[5.4.1 Rights-Collision Decision Test](#541-", "[6.4.1 Rights-Collision Decision Test](#641-"),
        ("**§5.1–§5.4**", "**§6.1–§6.4**"),
        ("**§5.3**", "**§6.3**"),
        ("Section 11** tells decision-makers **how**", "**§6 Interaction** tells decision-makers **how**"),
        ("**Section 11** tells them **what**", "**§15 Systemic Evaluation** tells them **what**"),
        ("**§§6–11**", "**§§11–15**"),
        ("under **§5** tradeoffs can still fail **§15**", "under **§6 Interaction** tradeoffs can still fail **§15**"),
        ("[§7 Governance Under Stewardship Discipline](#7-governance", "[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance"),
        ("[§6 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#6-stewardship", "[§11 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship"),
        ("[§2 Constitutional Interpretation](core_01_a_values_principles.md#2-constitutional-interpretation)", "[§8 Constitutional Interpretation](#8-constitutional-interpretation)"),
        ("[§2 Constitutional Interpretation](core_01_a_values_principles.md#9-constitutional-interpretation)", "[§8 Constitutional Interpretation](#8-constitutional-interpretation)"),
        ("value collisions: [§5 Interaction and Conflict Resolution](#5-interaction", "value collisions: [§6 Interaction and Conflict Resolution](#6-interaction"),
        ("[§9.2 Ambiguity resolution](core_01_a_values_principles.md#92-ambiguity-resolution)", "[§8.2 Ambiguity resolution](#82-ambiguity-resolution)"),
        ("[§9.1 Definitional layer and required disciplines](core_01_a_values_principles.md#91-definitional-layer", "[§8.1 Definitional layer and required disciplines](#81-definitional-layer"),
        ("Downstream: [7. Freedom](#7-freedom", "Downstream: [5. Freedom](#5-freedom"),
        ("[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#1041", "[§6.4.1 Rights-Collision Decision Test](#641"),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def apply_trace_repairs_part_b(text: str) -> str:
    repl = [
        ("§§11–14", "§§11–16"),
        ("[5. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction", "[6. Interaction and Conflict Resolution](core_01_a_values_principles.md#6-interaction"),
        ("[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction", "[§6 Interaction and Conflict Resolution](core_01_a_values_principles.md#6-interaction"),
        ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-", "[§6.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#641-"),
        ("[§5.1.4 Minimization of Avoidable Burden](#514-", "[§6.1.4 Minimization of Avoidable Burden](core_01_a_values_principles.md#614-"),
        ("[§6.1 Required Evaluation Factors](#61-required", "[§15.1 Required Evaluation Factors](#151-required"),
        ("[§7 Freedom (Bounded Agency)](core_01_a_values_principles.md#7-freedom", "[§5 Freedom (Bounded Agency)](core_01_a_values_principles.md#5-freedom"),
        ("[§8 Prohibition on Absolute Override](core_01_a_values_principles.md#8-prohibition", "[§7 Prohibition on Absolute Override](core_01_a_values_principles.md#7-prohibition"),
        ("[§5.2 Epistemic Disclosure Constraints](#52-", "[§6.2 Epistemic Disclosure Constraints](core_01_a_values_principles.md#62-"),
        ("[§5 Interaction and Conflict Resolution](#5-interaction", "[§6 Interaction and Conflict Resolution](core_01_a_values_principles.md#6-interaction"),
        ("[§5.4.1 Rights-Collision Decision Test](#541-", "[§6.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#641-"),
        ("[§5.4.2 Proxy-Divergence Invalidation](#542-", "[§6.4.2 Proxy-Divergence Invalidation](core_01_a_values_principles.md#642-"),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def apply_trace_repairs_integrated(text: str) -> str:
    repl = [
        ("[9. Constitutional Interpretation](core_01_a_values_principles.md#9-constitutional-interpretation)", "[8. Constitutional Interpretation](core_01_a_values_principles.md#8-constitutional-interpretation)"),
        ("[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)", "[6. Interaction and Conflict Resolution](core_01_a_values_principles.md#6-interaction-and-conflict-resolution)"),
        ("[6.1 Required Evaluation Factors](#61-required-evaluation-factors)", "[15.1 Required Evaluation Factors](#151-required-evaluation-factors)"),
        ("[7. Freedom](#7-freedom-bounded-agency)", "[5. Freedom](core_01_a_values_principles.md#5-freedom-bounded-agency)"),
        ("[8. Prohibition on Absolute Override](#8-prohibition-on-absolute-override)", "[7. Prohibition on Absolute Override](core_01_a_values_principles.md#7-prohibition-on-absolute-override)"),
        ("[§9.2 Ambiguity resolution](core_01_a_values_principles.md#92-ambiguity-resolution)", "[§8.2 Ambiguity resolution](core_01_a_values_principles.md#82-ambiguity-resolution)"),
        ("[§9.1 Definitional layer and required disciplines](core_01_a_values_principles.md#91-definitional-layer-and-required-disciplines)", "[§8.1 Definitional layer and required disciplines](core_01_a_values_principles.md#81-definitional-layer-and-required-disciplines)"),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def migrate_section_refs(content: str) -> str:
    for old, new in sorted(_TO_PH, key=lambda x: len(x[0]), reverse=True):
        content = content.replace(old, new)
    for old, new in _FROM_PH:
        content = content.replace(old, new)
    inline = [(a.replace("Chapter One ", ""), b.replace("Chapter One ", "")) for a, b in _FROM_PH]
    for old, new in inline:
        content = content.replace(old, new)
    return content


def renumber_ch1_basis_refs(content: str) -> str:
    basis_map = {5: 6, 6: 15, 7: 5, 8: 7, 9: 8, 10: 16}

    def line_repl(line: str) -> str:
        if "Chapter One basis:" not in line:
            return line

        def ref_repl(m: re.Match[str]) -> str:
            major = int(m.group(1))
            suffix = m.group(2) or ""
            if major in basis_map:
                return f"§{basis_map[major]}{suffix}"
            return m.group(0)

        line = re.sub(r"§(\d+)((?:\.\d+)+)?", ref_repl, line)
        line = line.replace(
            "(see [CJS-5.1](#cjs-51-constitutional-compass-and-cluster-map) map)",
            "(see [cluster map](#cjs-51-constitutional-compass-and-cluster-map))",
        )
        return line

    return "\n".join(line_repl(ln) for ln in content.splitlines())


def migrate_corpus(content: str, path: Path) -> str:
    if path.name in ("ch1_reading_arc_b.py", "ch1_integration_relocation.py", "ch1_integration_fixup.py"):
        return content
    orig = content
    for old, new in sorted(ANCHOR_PATH_MIGRATIONS, key=lambda x: len(x[0]), reverse=True):
        if old != new:
            content = content.replace(old, new)
    content = migrate_section_refs(content)
    if "cjs_05" in path.name and "Chapter One basis:" in content:
        content = renumber_ch1_basis_refs(content)
    return content if content != orig else content


def main() -> int:
    part_a_raw = PART_A.read_text(encoding="utf-8")
    part_b_raw = PART_B.read_text(encoding="utf-8")

    new_a = apply_trace_repairs_part_a(reassemble_part_a(part_a_raw))
    new_b = apply_trace_repairs_integrated(
        apply_trace_repairs_part_b(reassemble_part_b(part_a_raw, part_b_raw))
    )

    PART_A.write_text(new_a, encoding="utf-8")
    PART_B.write_text(new_b, encoding="utf-8")
    print(f"Wrote {PART_A}")
    print(f"Wrote {PART_B}")

    skip = {".git", "archive", "evidence", "node_modules", "__pycache__", ".cursor"}
    for path in ROOT.rglob("*"):
        if path in (PART_A, PART_B):
            continue
        if any(p in skip for p in path.parts):
            continue
        if path.suffix not in {".md", ".json", ".py"}:
            continue
        if path.name in ("ch1_reading_arc_b.py", "ch1_integration_relocation.py", "ch1_integration_fixup.py"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new_text = migrate_corpus(text, path)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
