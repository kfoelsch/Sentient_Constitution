#!/usr/bin/env python3
"""Relocate Chapter One §2 and §§10–14 to Part A; renumber §§6–9 → §§11–14 in Part B."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_A = ROOT / "core_01_a_values_principles.md"
PART_B = ROOT / "core_01_b_stewardship_capacity_principles.md"

SECTION_RENUMBER = {2: 9, 3: 2, 4: 3, 5: 4, 6: 11, 7: 12, 8: 13, 9: 14, 10: 5, 11: 6, 12: 7, 13: 8, 14: 10}

PART_A_HEADER = """# Values Principles (Chapter One, Part A)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part A** (§§1–10: purpose, values, integration, interpretation, and integrated application).
>
> **Upstream:** [core_00_preamble.md](core_00_preamble.md)  
> **Next:** [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md) (Chapter One, Part B).

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
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part B** (§§11–14: stewardship, governance, capacity, and market structure).
>
> **Upstream:** [core_01_a_values_principles.md](core_01_a_values_principles.md) (Chapter One, Part A)  
> **Next:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)<br>
> **Reading arc:** §11 stewardship → §12 governance discipline → §13 capacity → §14 market structure.

</details>

<br>

---
<a id="chapter-01-part-b-stewardship-and-governance"></a>
## CHAPTER 01, PART B: STEWARDSHIP AND GOVERNANCE

**Principle hierarchy (Part B).** At principle layer:

1. **[Stewardship](core_05_band_continuity.md#stewardship-constitutional)** orients systems toward durable constitutional alignment over time, including the **Continuity** aim under the [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims).
2. **[Governance](core_05_band_accountability.md#governance)** structures authorized decision-making, participation, and accountability under the [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) — especially **[Oversight](core_05_apex_oversight_leg.md#oversight-constitutional)** of how authority is allocated and exercised. Where governance and stewardship conflict, stewardship discipline controls at principle layer unless **Necessity** and **Proportionality** expressly justify a bounded, time-limited exception with correction paths. Operative authorization and contract-layer requirements remain owned by **Chapter Twelve**.
3. **[Shared-System Capacity](core_05_band_continuity.md#shared-system-capacity-constitutional)** is the durable, contestable ability those jointly produce — an **instrumental outcome** toward the **Flourishing** aim under the [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims), not a freestanding trump value. **[Market Structure](core_05_band_accountability.md#market-structure-constitutional)** at [§14](#14-market-structure) supplies the anti-concentration discipline that keeps that capacity contestable in practice.

"""

LEGACY_ANCHORS_PART_B = """
<!-- Legacy Chapter One anchor redirects (2026-06 integration relocation); do not remove without link migration. -->
<a id="6-stewardship-and-distributed-understanding"></a>
<a id="7-governance-under-stewardship-discipline"></a>
<a id="8-shared-system-capacity"></a>
<a id="9-market-structure"></a>
<a id="10-interaction-and-conflict-resolution"></a>
<a id="101-core-tradeoff-principles"></a>
<a id="1011-proportionality"></a>
<a id="1012-necessity"></a>
<a id="1013-minimization-of-harm"></a>
<a id="1014-minimization-of-avoidable-burden"></a>
<a id="102-epistemic-disclosure-constraints"></a>
<a id="1021-preservation-of-epistemic-integrity"></a>
<a id="1022-trust-truth-alignment"></a>
<a id="103-freedom-limitation-constraints"></a>
<a id="1031-constraint-on-freedom"></a>
<a id="1032-time-consistency-constraint"></a>
<a id="1041-rights-collision-decision-test"></a>
<a id="1042-proxy-divergence-invalidation"></a>
<a id="11-systemic-evaluation-requirement"></a>
<a id="111-required-evaluation-factors"></a>
<a id="112-read-with-governance-and-incentive-discipline"></a>
<a id="12-freedom-bounded-agency"></a>
<a id="13-prohibition-on-absolute-override"></a>
<a id="14-integrated-application"></a>
<a id="91-concentration-threshold-mechanism-adopter-tunable"></a>
<a id="92-pro-competition-and-anti-domination"></a>
<a id="93-consolidation-ceiling"></a>
<a id="931-consolidation-risk-pre-lock-in-impairment"></a>
<a id="932-ceiling-discipline-adopter-requirements"></a>
<a id="933-ceiling-crossing-rebuttal-and-remedies"></a>

"""

LEGACY_ANCHORS_PART_A = """
<!-- Legacy Chapter One Part A anchor redirects (2026-06 integration relocation); do not remove without link migration. -->
<a id="2-constitutional-interpretation"></a>
<a id="21-definitional-layer-and-required-disciplines"></a>
<a id="22-ambiguity-resolution"></a>
<a id="23-conflict-resolution-procedure"></a>
<a id="3-foundational-objective-wellbeing"></a>
<a id="41-safety-harm-constraint"></a>
<a id="42-truth-epistemic-integrity-constraint"></a>
<a id="5-system-stability-enabler-trust-coordination-integrity"></a>
<a id="51-resilience-and-self-healing-design"></a>

"""

ANCHOR_MIGRATIONS: list[tuple[str, str]] = [
    ("#1433-ceiling-crossing-rebuttal-and-remedies", "#1433-ceiling-crossing-rebuttal-and-remedies"),
    ("#1432-ceiling-discipline-adopter-requirements", "#1432-ceiling-discipline-adopter-requirements"),
    ("#1431-consolidation-risk-pre-lock-in-impairment", "#1431-consolidation-risk-pre-lock-in-impairment"),
    ("#143-consolidation-ceiling", "#143-consolidation-ceiling"),
    ("#142-pro-competition-and-anti-domination", "#142-pro-competition-and-anti-domination"),
    ("#141-concentration-threshold-mechanism-adopter-tunable", "#141-concentration-threshold-mechanism-adopter-tunable"),
    ("#123-stewardship-and-operator-incentive-alignment", "#123-stewardship-and-operator-incentive-alignment"),
    ("#122-incentive-alignment-and-system-capture", "#122-incentive-alignment-and-system-capture"),
    ("#1223-contingent-claims-games-of-chance-and-event-contract-markets", "#1223-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("#1222-misalignment-correction-and-capture-response", "#1222-misalignment-correction-and-capture-response"),
    ("#1221-alignment-requirement", "#1221-alignment-requirement"),
    ("#122-short-horizon-governance-defects", "#122-short-horizon-governance-defects"),
    ("#121-governance-as-authorized-structure", "#121-governance-as-authorized-structure"),
    ("#114-openness-aspiration", "#114-openness-aspiration"),
    ("#113-institutional-development", "#113-institutional-development"),
    ("#112-distributed-understanding", "#112-distributed-understanding"),
    ("#111-stewardship", "#111-stewardship"),
    ("#1042-proxy-divergence-invalidation", "#542-proxy-divergence-invalidation"),
    ("#1041-rights-collision-decision-test", "#541-rights-collision-decision-test"),
    ("#1032-time-consistency-constraint", "#532-time-consistency-constraint"),
    ("#1031-constraint-on-freedom", "#531-constraint-on-freedom"),
    ("#103-freedom-limitation-constraints", "#53-freedom-limitation-constraints"),
    ("#1022-trust-truth-alignment", "#522-trust-truth-alignment"),
    ("#1021-preservation-of-epistemic-integrity", "#521-preservation-of-epistemic-integrity"),
    ("#102-epistemic-disclosure-constraints", "#52-epistemic-disclosure-constraints"),
    ("#1014-minimization-of-avoidable-burden", "#514-minimization-of-avoidable-burden"),
    ("#1013-minimization-of-harm", "#513-minimization-of-harm"),
    ("#1012-necessity", "#512-necessity"),
    ("#1011-proportionality", "#511-proportionality"),
    ("#101-core-tradeoff-principles", "#51-core-tradeoff-principles"),
    ("#1115-assembly-collective-organization-and-institutional-formation", "#615-assembly-collective-organization-and-institutional-formation"),
    ("#1114-voluntary-discontinuation-and-exit-rights", "#614-voluntary-discontinuation-and-exit-rights"),
    ("#1113-privacy-informational-joint-invocation", "#613-privacy-informational-joint-invocation"),
    ("#1112-accessibility-under-sentience-non-exclusion", "#612-accessibility-under-sentience-non-exclusion"),
    ("#1111-systemic-scope-and-risk-factors", "#611-systemic-scope-and-risk-factors"),
    ("#111-required-evaluation-factors", "#61-required-evaluation-factors"),
    ("#112-read-with-governance-and-incentive-discipline", "#62-read-with-governance-and-incentive-discipline"),
    ("#10-interaction-and-conflict-resolution", "#5-interaction-and-conflict-resolution"),
    ("#14-integrated-application", "#10-integrated-application"),
    ("#13-prohibition-on-absolute-override", "#8-prohibition-on-absolute-override"),
    ("#12-freedom-bounded-agency", "#7-freedom-bounded-agency"),
    ("#11-systemic-evaluation-requirement", "#6-systemic-evaluation-requirement"),
    ("#2-constitutional-interpretation", "#9-constitutional-interpretation"),
    ("#21-definitional-layer-and-required-disciplines", "#91-definitional-layer-and-required-disciplines"),
    ("#22-ambiguity-resolution", "#92-ambiguity-resolution"),
    ("#23-conflict-resolution-procedure", "#93-conflict-resolution-procedure"),
    ("#11-definitional-layer-and-required-disciplines", "#91-definitional-layer-and-required-disciplines"),
    ("#12-ambiguity-resolution", "#92-ambiguity-resolution"),
    ("#14-canonical-conflict-resolution-procedure", "#93-conflict-resolution-procedure"),
    ("#24-canonical-conflict-resolution-procedure", "#93-conflict-resolution-procedure"),
    ("#3-foundational-objective-wellbeing", "#2-foundational-objective-wellbeing"),
    ("#31-fairness", "#21-fairness"),
    ("#32-recognition-reinforcement-and-aspiration", "#22-recognition-reinforcement-and-aspiration"),
    ("#41-safety-harm-constraint", "#31-safety-harm-constraint"),
    ("#42-truth-epistemic-integrity-constraint", "#32-truth-epistemic-integrity-constraint"),
    ("#43-science-informed-inquiry-and-decision-support", "#33-science-informed-inquiry-and-decision-support"),
    ("#44-plain-language-accessibility-stewardship-duty", "#34-plain-language-accessibility-stewardship-duty"),
    ("#5-system-stability-enabler-trust-coordination-integrity", "#4-system-stability-enabler-trust-coordination-integrity"),
    ("#51-resilience-and-self-healing-design", "#41-resilience-and-self-healing-design"),
    ("#6-stewardship-and-distributed-understanding", "#11-stewardship-and-distributed-understanding"),
    ("#61-stewardship", "#111-stewardship"),
    ("#62-distributed-understanding", "#112-distributed-understanding"),
    ("#63-institutional-development", "#113-institutional-development"),
    ("#64-openness-aspiration", "#114-openness-aspiration"),
    ("#7-governance-under-stewardship-discipline", "#12-governance-under-stewardship-discipline"),
    ("#71-governance-as-authorized-structure", "#121-governance-as-authorized-structure"),
    ("#72-short-horizon-governance-defects", "#122-short-horizon-governance-defects"),
    ("#73-incentive-alignment-and-system-capture", "#122-incentive-alignment-and-system-capture"),
    ("#731-alignment-requirement", "#1221-alignment-requirement"),
    ("#732-misalignment-correction-and-capture-response", "#1222-misalignment-correction-and-capture-response"),
    ("#733-contingent-claims-games-of-chance-and-event-contract-markets", "#1223-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("#74-stewardship-and-operator-incentive-alignment", "#123-stewardship-and-operator-incentive-alignment"),
    ("#8-shared-system-capacity", "#13-shared-system-capacity"),
    ("#81-productive-capacity-instrumental-good", "#131-productive-capacity-instrumental-good"),
    ("#82-constitutional-efficiency", "#132-constitutional-efficiency"),
    ("#9-market-structure", "#14-market-structure"),
    ("#91-concentration-threshold-mechanism-adopter-tunable", "#141-concentration-threshold-mechanism-adopter-tunable"),
    ("#92-pro-competition-and-anti-domination", "#142-pro-competition-and-anti-domination"),
    ("#93-consolidation-ceiling", "#143-consolidation-ceiling"),
    ("#931-consolidation-risk-pre-lock-in-impairment", "#1431-consolidation-risk-pre-lock-in-impairment"),
    ("#932-ceiling-discipline-adopter-requirements", "#1432-ceiling-discipline-adopter-requirements"),
    ("#933-ceiling-crossing-rebuttal-and-remedies", "#1433-ceiling-crossing-rebuttal-and-remedies"),
    ("#94-rights-collision-procedure", "#54-rights-collision-procedure"),
    ("#104-rights-collision-procedure", "#54-rights-collision-procedure"),
    ("#9-systemic-evaluation-requirement", "#6-systemic-evaluation-requirement"),
]

# dedupe longest-first
_seen: set[str] = set()
ANCHOR_MIGRATIONS = [
    p for p in sorted(set(ANCHOR_MIGRATIONS), key=lambda x: len(x[0]), reverse=True)
    if p[0] not in _seen and not _seen.add(p[0])  # type: ignore[func-returns-value]
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

    # § refs — longest subsection suffixes first
    suffixes = sorted(
        {m.group(1) for m in re.finditer(rf"§{os}\.(\d+(?:\.\d+)*)", block)},
        key=len,
        reverse=True,
    )
    for suf in suffixes:
        block = block.replace(f"§{os}.{suf}", f"§{ns}.{suf}")
    block = re.sub(rf"§{os}\b", f"§{ns}", block)

    # same-file hash links
    def hash_link(m: re.Match[str]) -> str:
        label, anchor = m.group(1), m.group(2)
        if re.match(rf"^{os}(\d|$|-)", anchor):
            return f"[{label}](#{ns}{anchor[len(os):]})"
        return m.group(0)

    block = re.sub(r"\[([^\]]+)\]\(#(\d[^)]*)\)", hash_link, block)

    # anchor ids — explicit prefix replace for section-prefixed ids
    def anchor_id(m: re.Match[str]) -> str:
        aid = m.group(1)
        if re.match(rf"^{os}(\d|-)", aid):
            return f'<a id="{ns}{aid[len(os):]}"></a>'
        return m.group(0)

    block = re.sub(r'<a id="(\d[^"]*)"></a>', anchor_id, block)
    return block


def reassemble_part_a(part_a: str, part_b: str) -> str:
    _, body = split_at_chapter(part_a)
    s1, rest = extract_h3_section(body, 1)
    _s2, rest = extract_h3_section(rest, 2)
    s3, rest = extract_h3_section(rest, 3)
    s4, rest = extract_h3_section(rest, 4)
    s5, _ = extract_h3_section(rest, 5)
    s5 = re.sub(
        r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n?",
        "\n",
        s5,
    )

    _, bbody = split_at_chapter(part_b)
    s10, brest = extract_h3_section(bbody, 10)
    s11, brest = extract_h3_section(brest, 11)
    s12, brest = extract_h3_section(brest, 12)
    s13, brest = extract_h3_section(brest, 13)
    s14, brest = extract_h3_section(brest, 14)
    ref_idx = brest.find("### Reference:")
    reference = brest[ref_idx:].split("---")[0].rstrip() + "\n" if ref_idx != -1 else ""

    s2 = extract_h3_section(part_a, 2)[0]
    s2 = renumber_section_block(s2, 2, 9)
    s3 = renumber_section_block(s3, 3, 2)
    s4 = renumber_section_block(s4, 4, 3)
    s5 = renumber_section_block(s5, 5, 4)
    s10 = renumber_section_block(s10, 10, 5)
    s11 = renumber_section_block(s11, 11, 6)
    s12 = renumber_section_block(s12, 12, 7)
    s13 = renumber_section_block(s13, 13, 8)
    s14 = renumber_section_block(s14, 14, 10)

    reference = reference.replace(
        "canonical homes in this file",
        "canonical homes in Chapter One (Parts A and B)",
    )

    footer = """
---

**Previous file:** [core_00_preamble.md](core_00_preamble.md)

**Next file:** [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md)
"""
    return (
        PART_A_HEADER
        + LEGACY_ANCHORS_PART_A
        + s1
        + s3
        + s4
        + s5
        + s10
        + s11
        + s12
        + s13
        + s2
        + s14
        + reference
        + footer
    )


def split_at_chapter(text: str) -> tuple[str, str]:
    idx = text.find("## CHAPTER 01")
    if idx == -1:
        raise ValueError("chapter heading not found")
    chapter_start = text.find("\n", idx)
    return text[:chapter_start], text[chapter_start + 1 :]


def reassemble_part_b(part_b: str) -> str:
    _, bbody = split_at_chapter(part_b)
    s6, brest = extract_h3_section(bbody, 6)
    s7, brest = extract_h3_section(brest, 7)
    s8, brest = extract_h3_section(brest, 8)
    s9, _ = extract_h3_section(brest, 9)

    s6 = renumber_section_block(s6, 6, 11)
    s7 = renumber_section_block(s7, 7, 12)
    s8 = renumber_section_block(s8, 8, 13)
    s9 = renumber_section_block(s9, 9, 14)

    footer = """
---

**Previous file:** [core_01_a_values_principles.md](core_01_a_values_principles.md)

**Next file:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)
"""
    return PART_B_HEADER + LEGACY_ANCHORS_PART_B + s6 + s7 + s8 + s9 + footer


def migrate_file_paths(content: str) -> str:
    """Move Part B integration links to Part A after physical relocation."""
    pairs = [
        ("core_01_b_stewardship_capacity_principles.md#1042-", "core_01_a_values_principles.md#542-"),
        ("core_01_b_stewardship_capacity_principles.md#1041-", "core_01_a_values_principles.md#541-"),
        ("core_01_b_stewardship_capacity_principles.md#1032-", "core_01_a_values_principles.md#532-"),
        ("core_01_b_stewardship_capacity_principles.md#1031-", "core_01_a_values_principles.md#531-"),
        ("core_01_b_stewardship_capacity_principles.md#103-", "core_01_a_values_principles.md#53-"),
        ("core_01_b_stewardship_capacity_principles.md#1022-", "core_01_a_values_principles.md#522-"),
        ("core_01_b_stewardship_capacity_principles.md#1021-", "core_01_a_values_principles.md#521-"),
        ("core_01_b_stewardship_capacity_principles.md#102-", "core_01_a_values_principles.md#52-"),
        ("core_01_b_stewardship_capacity_principles.md#1014-", "core_01_a_values_principles.md#514-"),
        ("core_01_b_stewardship_capacity_principles.md#1013-", "core_01_a_values_principles.md#513-"),
        ("core_01_b_stewardship_capacity_principles.md#1012-", "core_01_a_values_principles.md#512-"),
        ("core_01_b_stewardship_capacity_principles.md#1011-", "core_01_a_values_principles.md#511-"),
        ("core_01_b_stewardship_capacity_principles.md#101-", "core_01_a_values_principles.md#51-"),
        ("core_01_b_stewardship_capacity_principles.md#10-interaction", "core_01_a_values_principles.md#5-interaction"),
        ("core_01_b_stewardship_capacity_principles.md#11-systemic", "core_01_a_values_principles.md#6-systemic"),
        ("core_01_b_stewardship_capacity_principles.md#111-", "core_01_a_values_principles.md#61-"),
        ("core_01_b_stewardship_capacity_principles.md#112-read", "core_01_a_values_principles.md#62-read"),
        ("core_01_b_stewardship_capacity_principles.md#12-freedom", "core_01_a_values_principles.md#7-freedom"),
        ("core_01_b_stewardship_capacity_principles.md#13-prohibition", "core_01_a_values_principles.md#8-prohibition"),
        ("core_01_b_stewardship_capacity_principles.md#14-integrated", "core_01_a_values_principles.md#10-integrated"),
        ("core_01_a_values_principles.md#2-constitutional", "core_01_a_values_principles.md#9-constitutional"),
        ("core_01_a_values_principles.md#21-definitional", "core_01_a_values_principles.md#91-definitional"),
        ("core_01_a_values_principles.md#22-ambiguity", "core_01_a_values_principles.md#92-ambiguity"),
        ("core_01_a_values_principles.md#23-conflict", "core_01_a_values_principles.md#93-conflict"),
        ("core_01_a_values_principles.md#3-foundational", "core_01_a_values_principles.md#2-foundational"),
        ("core_01_a_values_principles.md#31-fairness", "core_01_a_values_principles.md#21-fairness"),
        ("core_01_a_values_principles.md#32-recognition", "core_01_a_values_principles.md#22-recognition"),
        ("core_01_a_values_principles.md#41-safety", "core_01_a_values_principles.md#31-safety"),
        ("core_01_a_values_principles.md#42-truth", "core_01_a_values_principles.md#32-truth"),
        ("core_01_a_values_principles.md#5-system-stability", "core_01_a_values_principles.md#4-system-stability"),
        ("core_01_a_values_principles.md#51-resilience", "core_01_a_values_principles.md#41-resilience"),
        ("core_01_b_stewardship_capacity_principles.md#6-stewardship", "core_01_b_stewardship_capacity_principles.md#11-stewardship"),
        ("core_01_b_stewardship_capacity_principles.md#61-", "core_01_b_stewardship_capacity_principles.md#111-"),
        ("core_01_b_stewardship_capacity_principles.md#62-", "core_01_b_stewardship_capacity_principles.md#112-"),
        ("core_01_b_stewardship_capacity_principles.md#63-", "core_01_b_stewardship_capacity_principles.md#113-"),
        ("core_01_b_stewardship_capacity_principles.md#64-", "core_01_b_stewardship_capacity_principles.md#114-"),
        ("core_01_b_stewardship_capacity_principles.md#7-governance", "core_01_b_stewardship_capacity_principles.md#12-governance"),
        ("core_01_b_stewardship_capacity_principles.md#71-", "core_01_b_stewardship_capacity_principles.md#121-"),
        ("core_01_b_stewardship_capacity_principles.md#72-", "core_01_b_stewardship_capacity_principles.md#122-"),
        ("core_01_b_stewardship_capacity_principles.md#73-", "core_01_b_stewardship_capacity_principles.md#123-"),
        ("core_01_b_stewardship_capacity_principles.md#74-", "core_01_b_stewardship_capacity_principles.md#124-"),
        ("core_01_b_stewardship_capacity_principles.md#8-shared-system", "core_01_b_stewardship_capacity_principles.md#13-shared-system"),
        ("core_01_b_stewardship_capacity_principles.md#81-", "core_01_b_stewardship_capacity_principles.md#131-"),
        ("core_01_b_stewardship_capacity_principles.md#82-", "core_01_b_stewardship_capacity_principles.md#132-"),
        ("core_01_b_stewardship_capacity_principles.md#9-market", "core_01_b_stewardship_capacity_principles.md#14-market"),
        ("core_01_b_stewardship_capacity_principles.md#91-", "core_01_b_stewardship_capacity_principles.md#141-"),
        ("core_01_b_stewardship_capacity_principles.md#92-", "core_01_b_stewardship_capacity_principles.md#142-"),
        ("core_01_b_stewardship_capacity_principles.md#93-", "core_01_b_stewardship_capacity_principles.md#143-"),
    ]
    for old, new in sorted(pairs, key=lambda x: len(x[0]), reverse=True):
        content = content.replace(old, new)
    return content


def migrate_section_refs(content: str) -> str:
    pairs = [
        ("Chapter One §14.3.3", "Chapter One §14.3.3"),
        ("Chapter One §14.3.2", "Chapter One §14.3.2"),
        ("Chapter One §14.3.1", "Chapter One §14.3.1"),
        ("Chapter One §14.3", "Chapter One §14.3"),
        ("Chapter One §14.2", "Chapter One §14.2"),
        ("Chapter One §14.1", "Chapter One §14.1"),
        ("Chapter One §13.2", "Chapter One §13.2"),
        ("Chapter One §13.1", "Chapter One §13.1"),
        ("Chapter One §12.2", "Chapter One §12.2"),
        ("Chapter One §12.2.3", "Chapter One §12.2.3"),
        ("Chapter One §12.2.2", "Chapter One §12.2.2"),
        ("Chapter One §12.2.1", "Chapter One §12.2.1"),
        ("Chapter One §12.2", "Chapter One §12.2"),
        ("Chapter One §12.2", "Chapter One §12.2"),
        ("Chapter One §12.1", "Chapter One §12.1"),
        ("Chapter One §11.4", "Chapter One §11.4"),
        ("Chapter One §11.3", "Chapter One §11.3"),
        ("Chapter One §11.2", "Chapter One §11.2"),
        ("Chapter One §11.1.5", "Chapter One §6.1.5"),
        ("Chapter One §11.1.4", "Chapter One §6.1.4"),
        ("Chapter One §11.1.3", "Chapter One §6.1.3"),
        ("Chapter One §11.1.2", "Chapter One §6.1.2"),
        ("Chapter One §11.1.1", "Chapter One §6.1.1"),
        ("Chapter One §11.1", "Chapter One §6.1"),
        ("Chapter One §10.4.2", "Chapter One §5.4.2"),
        ("Chapter One §10.4.1", "Chapter One §5.4.1"),
        ("Chapter One §10.4", "Chapter One §5.4"),
        ("Chapter One §10.3.2", "Chapter One §5.3.2"),
        ("Chapter One §10.3.1", "Chapter One §5.3.1"),
        ("Chapter One §10.3", "Chapter One §5.3"),
        ("Chapter One §10.2.2", "Chapter One §5.2.2"),
        ("Chapter One §10.2.1", "Chapter One §5.2.1"),
        ("Chapter One §10.2", "Chapter One §5.2"),
        ("Chapter One §10.1.4", "Chapter One §5.1.4"),
        ("Chapter One §10.1.3", "Chapter One §5.1.3"),
        ("Chapter One §10.1.2", "Chapter One §5.1.2"),
        ("Chapter One §10.1.1", "Chapter One §5.1.1"),
        ("Chapter One §10.1", "Chapter One §5.1"),
        ("Chapter One §10 Interaction", "Chapter One §5 Interaction"),
        ("Chapter One §10 Systemic", "Chapter One §6 Systemic"),
        ("Chapter One §11 Freedom", "Chapter One §7 Freedom"),
        ("Chapter One §12 Prohibition", "Chapter One §8 Prohibition"),
        ("Chapter One §13 Integrated", "Chapter One §10 Integrated"),
        ("Chapter One §9.3.3", "Chapter One §14.3.3"),
        ("Chapter One §9.3.2", "Chapter One §14.3.2"),
        ("Chapter One §9.3.1", "Chapter One §14.3.1"),
        ("Chapter One §9.3", "Chapter One §14.3"),
        ("Chapter One §9.2", "Chapter One §14.2"),
        ("Chapter One §9.1", "Chapter One §14.1"),
        ("Chapter One §9 Market", "Chapter One §14 Market"),
        ("Chapter One §8.2", "Chapter One §13.2"),
        ("Chapter One §8.1", "Chapter One §13.1"),
        ("Chapter One §7.4", "Chapter One §12.2"),
        ("Chapter One §7.3.3", "Chapter One §12.2.3"),
        ("Chapter One §7.3.2", "Chapter One §12.2.2"),
        ("Chapter One §7.3.1", "Chapter One §12.2.1"),
        ("Chapter One §7.3", "Chapter One §12.2"),
        ("Chapter One §7.2", "Chapter One §12.2"),
        ("Chapter One §7.1", "Chapter One §12.1"),
        ("Chapter One §6.4", "Chapter One §11.4"),
        ("Chapter One §6.3", "Chapter One §11.3"),
        ("Chapter One §6.2", "Chapter One §11.2"),
        ("Chapter One §6.1", "Chapter One §11.1"),
        ("Chapter One §5.1", "Chapter One §4.1"),
        ("Chapter One §4.4", "Chapter One §3.4"),
        ("Chapter One §4.3", "Chapter One §3.3"),
        ("Chapter One §4.2", "Chapter One §3.2"),
        ("Chapter One §4.1", "Chapter One §3.1"),
        ("Chapter One §3.2", "Chapter One §2.2"),
        ("Chapter One §3.1", "Chapter One §2.1"),
        ("Chapter One §2.3.3", "Chapter One §9.3.3"),
        ("Chapter One §2.3.2", "Chapter One §9.3.2"),
        ("Chapter One §2.3.1", "Chapter One §9.3.1"),
        ("Chapter One §2.3", "Chapter One §9.3"),
        ("Chapter One §2.2", "Chapter One §9.2"),
        ("Chapter One §2.1", "Chapter One §9.1"),
        ("§14.3.3", "§14.3.3"),
        ("§14.3.2", "§14.3.2"),
        ("§14.3.1", "§14.3.1"),
        ("§14.3", "§14.3"),
        ("§14.2", "§14.2"),
        ("§14.1", "§14.1"),
        ("§13.2", "§13.2"),
        ("§13.1", "§13.1"),
        ("§12.2", "§12.2"),
        ("§12.2.3", "§12.2.3"),
        ("§12.2.2", "§12.2.2"),
        ("§12.2.1", "§12.2.1"),
        ("§12.2", "§12.2"),
        ("§12.2", "§12.2"),
        ("§12.1", "§12.1"),
        ("§11.4", "§11.4"),
        ("§11.3", "§11.3"),
        ("§11.2", "§11.2"),
        ("§11.1.5", "§6.1.5"),
        ("§11.1.4", "§6.1.4"),
        ("§11.1.3", "§6.1.3"),
        ("§11.1.2", "§6.1.2"),
        ("§11.1.1", "§6.1.1"),
        ("§11.1", "§6.1"),
        ("§10.4.2", "§5.4.2"),
        ("§10.4.1", "§5.4.1"),
        ("§10.4", "§5.4"),
        ("§10.3.2", "§5.3.2"),
        ("§10.3.1", "§5.3.1"),
        ("§10.3", "§5.3"),
        ("§10.2.2", "§5.2.2"),
        ("§10.2.1", "§5.2.1"),
        ("§10.2", "§5.2"),
        ("§10.1.4", "§5.1.4"),
        ("§10.1.3", "§5.1.3"),
        ("§10.1.2", "§5.1.2"),
        ("§10.1.1", "§5.1.1"),
        ("§10.1", "§5.1"),
        ("§9.3.3", "§14.3.3"),
        ("§9.3.2", "§14.3.2"),
        ("§9.3.1", "§14.3.1"),
        ("§9.3", "§14.3"),
        ("§9.2", "§14.2"),
        ("§9.1", "§14.1"),
        ("§8.2", "§13.2"),
        ("§8.1", "§13.1"),
        ("§7.4", "§12.2"),
        ("§7.3.3", "§12.2.3"),
        ("§7.3.2", "§12.2.2"),
        ("§7.3.1", "§12.2.1"),
        ("§7.3", "§12.2"),
        ("§7.2", "§12.2"),
        ("§7.1", "§12.1"),
        ("§6.4", "§11.4"),
        ("§6.3", "§11.3"),
        ("§6.2", "§11.2"),
        ("§6.1", "§11.1"),
        ("§5.1", "§4.1"),
        ("§4.4.5", "§3.4.5"),
        ("§4.4.4", "§3.4.4"),
        ("§4.4.3", "§3.4.3"),
        ("§4.4.2", "§3.4.2"),
        ("§4.4.1", "§3.4.1"),
        ("§4.4", "§3.4"),
        ("§4.3", "§3.3"),
        ("§4.2", "§3.2"),
        ("§4.1", "§3.1"),
        ("§3.2", "§2.2"),
        ("§3.1", "§2.1"),
        ("§2.3.3", "§9.3.3"),
        ("§2.3.2", "§9.3.2"),
        ("§2.3.1", "§9.3.1"),
        ("§2.3", "§9.3"),
        ("§2.2", "§9.2"),
        ("§2.1", "§9.1"),
        ("Chapter One §14 Integrated", "Chapter One §10 Integrated"),
        ("Chapter One §13 Prohibition", "Chapter One §8 Prohibition"),
        ("Chapter One §12 Freedom", "Chapter One §7 Freedom"),
        ("Chapter One §11 Systemic", "Chapter One §6 Systemic"),
        ("Chapter One §10 Interaction", "Chapter One §5 Interaction"),
        ("Chapter One §9 Market", "Chapter One §14 Market"),
        ("Chapter One §8 Shared-System", "Chapter One §13 Shared-System"),
        ("Chapter One §7 Governance", "Chapter One §12 Governance"),
        ("Chapter One §6 Stewardship", "Chapter One §11 Stewardship"),
        ("§14 Integrated", "§10 Integrated"),
        ("§13 Prohibition", "§8 Prohibition"),
        ("§12 Freedom", "§7 Freedom"),
        ("§11 Systemic", "§6 Systemic"),
        ("§10 Interaction", "§5 Interaction"),
        ("§9 Market", "§14 Market"),
        ("§9 non-concentration", "§14 non-concentration"),
        ("§6 Stewardship", "§11 Stewardship"),
        ("§7 Governance", "§12 Governance"),
        ("§8 Shared-System", "§13 Shared-System"),
        ("§7.4 Stewardship", "§12.2 Stewardship"),
    ]
    cleaned = []
    seen: set[str] = set()
    for old, new in pairs:
        if old == new or old in seen:
            continue
        seen.add(old)
        cleaned.append((old, new))
    for old, new in sorted(cleaned, key=lambda x: len(x[0]), reverse=True):
        content = content.replace(old, new)
    return content


def apply_trace_repairs_part_a(text: str) -> str:
    repl = [
        (
            "Chapter One, section 9 — Interaction and Conflict Resolution controls precedence.",
            "Chapter One, **§4** — Interaction and Conflict Resolution controls precedence.",
        ),
        (
            "[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)",
            "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)",
        ),
        (
            "[10. Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)",
            "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)",
        ),
        (
            "[§10.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)",
            "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)",
        ),
        (
            "[§10.1.4 Minimization of Avoidable Burden](core_01_b_stewardship_capacity_principles.md#514-minimization-of-avoidable-burden)",
            "[§5.1.4 Minimization of Avoidable Burden](#514-minimization-of-avoidable-burden)",
        ),
        (
            "[§12 Freedom](core_01_b_stewardship_capacity_principles.md#7-freedom-bounded-agency)",
            "[§7 Freedom](#7-freedom-bounded-agency)",
        ),
        (
            "[§15](core_01_b_stewardship_capacity_principles.md#7-freedom-bounded-agency)",
            "[§7 Freedom](#7-freedom-bounded-agency)",
        ),
        (
            "[§6 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship-and-distributed-understanding)",
            "[§11 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship-and-distributed-understanding)",
        ),
        (
            "[§8 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)",
            "[§13 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)",
        ),
        (
            "[§5](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)",
            "[§13 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)",
        ),
        (
            "[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#1041-rights-collision-decision-test)",
            "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)",
        ),
        (
            "[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)",
            "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)",
        ),
        (
            "[7.2.1 Preservation of Epistemic Integrity](core_01_b_stewardship_capacity_principles.md#1021-preservation-of-epistemic-integrity)",
            "[5.2.1 Preservation of Epistemic Integrity](#521-preservation-of-epistemic-integrity)",
        ),
        (
            "[7.2.2 Trust-Truth Alignment](core_01_b_stewardship_capacity_principles.md#1022-trust-truth-alignment)",
            "[5.2.2 Trust-Truth Alignment](#522-trust-truth-alignment)",
        ),
        (
            "[13. Prohibition on Absolute Override](core_01_b_stewardship_capacity_principles.md#13-prohibition-on-absolute-override)",
            "[8. Prohibition on Absolute Override](#8-prohibition-on-absolute-override)",
        ),
        (
            "[11.1 Required Evaluation Factors](core_01_b_stewardship_capacity_principles.md#61-required-evaluation-factors)",
            "[6.1 Required Evaluation Factors](#61-required-evaluation-factors)",
        ),
        (
            "[§7 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance-under-stewardship-discipline)",
            "[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance-under-stewardship-discipline)",
        ),
        (
            "[§7.4 Stewardship and Operator Incentive Alignment](core_01_b_stewardship_capacity_principles.md#123-stewardship-and-operator-incentive-alignment)",
            "[§12.2 Stewardship and Operator Incentive Alignment](core_01_b_stewardship_capacity_principles.md#123-stewardship-and-operator-incentive-alignment)",
        ),
        (
            "[§14.2](core_01_b_stewardship_capacity_principles.md#12-governance-under-stewardship-discipline)",
            "[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance-under-stewardship-discipline)",
        ),
        (
            "[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#52-epistemic-disclosure-constraints)",
            "[§5.2 Epistemic Disclosure Constraints](#52-epistemic-disclosure-constraints)",
        ),
        (
            "[9.2 Epistemic Disclosure Constraints](#102-epistemic-disclosure-constraints)",
            "[5.2 Epistemic Disclosure Constraints](#52-epistemic-disclosure-constraints)",
        ),
        (
            "[2. Constitutional Interpretation](#2-constitutional-interpretation)",
            "[9. Constitutional Interpretation](#9-constitutional-interpretation)",
        ),
        (
            "[3. Foundational Objective: Wellbeing](#3-foundational-objective-wellbeing)",
            "[2. Foundational Objective: Wellbeing](#2-foundational-objective-wellbeing)",
        ),
        (
            "[§11](#3-foundational-objective-wellbeing)",
            "[§3](#2-foundational-objective-wellbeing)",
        ),
        (
            "[§4](#5-system-stability-enabler-trust-coordination-integrity)",
            "[§2](#4-system-stability-enabler-trust-coordination-integrity)",
        ),
        (
            "[§5.1](#51-resilience-and-self-healing-design)",
            "[§4.1](#41-resilience-and-self-healing-design)",
        ),
        (
            "[4.1 Safety](#41-safety-harm-constraint)",
            "[3.1 Safety](#31-safety-harm-constraint)",
        ),
        (
            "[4.2 Truth](#42-truth-epistemic-integrity-constraint)",
            "[3.2 Truth](#32-truth-epistemic-integrity-constraint)",
        ),
        (
            "[5. Trust](#5-system-stability-enabler-trust-coordination-integrity)",
            "[4. Trust](#4-system-stability-enabler-trust-coordination-integrity)",
        ),
        (
            "[§3.2 Recognition, Reinforcement, and Aspiration](#32-recognition-reinforcement-and-aspiration)",
            "[§2.2 Recognition, Reinforcement, and Aspiration](#22-recognition-reinforcement-and-aspiration)",
        ),
        (
            "[§10 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#10-interaction-and-conflict-resolution)",
            "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)",
        ),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def apply_trace_repairs_part_b(text: str) -> str:
    repl = [
        (
            "[10. Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution)",
            "[5. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution)",
        ),
        (
            "([§10.4.2 Proxy-Divergence Invalidation](#1042-proxy-divergence-invalidation))",
            "([§5.4.2 Proxy-Divergence Invalidation](core_01_a_values_principles.md#542-proxy-divergence-invalidation))",
        ),
        (
            "[§8 Shared-System Capacity](#8-shared-system-capacity)",
            "[§13 Shared-System Capacity](#13-shared-system-capacity)",
        ),
        (
            "[7. Governance Under Stewardship Discipline](#7-governance-under-stewardship-discipline)",
            "[12. Governance Under Stewardship Discipline](#12-governance-under-stewardship-discipline)",
        ),
        (
            "[§9.2 Pro-Competition and Anti-Domination](#92-pro-competition-and-anti-domination)",
            "[§14.2 Pro-Competition and Anti-Domination](#142-pro-competition-and-anti-domination)",
        ),
        (
            "the **§10.2** anti-domination rules",
            "the **§14.2** anti-domination rules",
        ),
        (
            "the **§10.1** threshold mechanism, or **§10.2** anti-domination discipline",
            "the **§14.1** threshold mechanism, or **§14.2** anti-domination discipline",
        ),
        (
            "nullify the **§13** floor, the **§10.1** threshold mechanism, or **§10.2** anti-domination discipline",
            "nullify the **§14** floor, the **§14.1** threshold mechanism, or **§14.2** anti-domination discipline",
        ),
        (
            "under the **§13** non-concentration discipline and **§10.2** anti-domination rules",
            "under the **§14** non-concentration discipline and **§14.2** anti-domination rules",
        ),
        (
            "**§9.1–§9.3**",
            "**§14.1–§14.3**",
        ),
        (
            "Productive-capacity and constitutional-efficiency claims under **§14** fail",
            "Productive-capacity and constitutional-efficiency claims under **§13** fail",
        ),
        (
            "[§8 Shared-System Capacity](#8-shared-system-capacity)",
            "[§13 Shared-System Capacity](#13-shared-system-capacity)",
        ),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def apply_trace_repairs_integrated(text: str) -> str:
    repl = [
        (
            "[2. Constitutional Interpretation](core_01_a_values_principles.md#2-constitutional-interpretation)",
            "[9. Constitutional Interpretation](core_01_a_values_principles.md#9-constitutional-interpretation)",
        ),
        (
            "(value collisions: [§10 Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution))",
            "(value collisions: [§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution))",
        ),
        (
            "[§10 Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution)",
            "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)",
        ),
        (
            "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)",
            "[§11 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship-and-distributed-understanding)",
        ),
        (
            "[10. Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution)",
            "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)",
        ),
        (
            "[11.1 Required Evaluation Factors](#111-required-evaluation-factors)",
            "[6.1 Required Evaluation Factors](#61-required-evaluation-factors)",
        ),
        (
            "[12. Freedom](#12-freedom-bounded-agency)",
            "[7. Freedom](#7-freedom-bounded-agency)",
        ),
        (
            "[13. Prohibition on Absolute Override](#13-prohibition-on-absolute-override)",
            "[8. Prohibition on Absolute Override](#8-prohibition-on-absolute-override)",
        ),
        (
            "[13. Integrated Application](#14-integrated-application)",
            "[10. Integrated Application](#10-integrated-application)",
        ),
        (
            "[§2.2 Ambiguity resolution](core_01_a_values_principles.md#22-ambiguity-resolution)",
            "[§9.2 Ambiguity resolution](core_01_a_values_principles.md#92-ambiguity-resolution)",
        ),
        (
            "[§2.1 Definitional layer and required disciplines](core_01_a_values_principles.md#21-definitional-layer-and-required-disciplines)",
            "[§9.1 Definitional layer and required disciplines](core_01_a_values_principles.md#91-definitional-layer-and-required-disciplines)",
        ),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def renumber_ch1_basis_refs(content: str) -> str:
    """One-pass renumber for 'Chapter One basis:' lines (old major § only)."""
    major_map = SECTION_RENUMBER

    def line_repl(line: str) -> str:
        if "Chapter One basis:" not in line:
            return line

        def ref_repl(m: re.Match[str]) -> str:
            major = int(m.group(1))
            suffix = m.group(2) or ""
            if major in major_map:
                return f"§{major_map[major]}{suffix}"
            return m.group(0)

        return re.sub(r"§(\d+)((?:\.\d+)+)?", ref_repl, line)

    return "\n".join(line_repl(line) for line in content.splitlines())


def migrate_corpus_content(content: str, path: Path) -> str:
    if path.name == "ch1_integration_relocation.py":
        return content
    original = content
    content = migrate_file_paths(content)
    for old, new in ANCHOR_MIGRATIONS:
        if old != new:
            content = content.replace(old, new)
    content = migrate_section_refs(content)
    if "cjs_05" in path.name and "Chapter One basis:" in content:
        content = renumber_ch1_basis_refs(content)
    return content if content != original else content


def main() -> int:
    part_a_raw = PART_A.read_text(encoding="utf-8")
    part_b_raw = PART_B.read_text(encoding="utf-8")

    new_a = reassemble_part_a(part_a_raw, part_b_raw)
    new_b = reassemble_part_b(part_b_raw)
    new_a = apply_trace_repairs_part_a(new_a)
    new_b = apply_trace_repairs_part_b(new_b)
    new_a = apply_trace_repairs_integrated(new_a)

    PART_A.write_text(new_a, encoding="utf-8")
    PART_B.write_text(new_b, encoding="utf-8")
    print(f"Wrote {PART_A}")
    print(f"Wrote {PART_B}")

    skip_dirs = {".git", "archive", "evidence", "node_modules", "__pycache__", ".cursor"}
    extensions = {".md", ".json", ".py"}
    for path in ROOT.rglob("*"):
        if path in (PART_A, PART_B) or path.name == "ch1_integration_relocation.py":
            continue
        if any(p in skip_dirs for p in path.parts):
            continue
        if path.suffix not in extensions:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new_text = migrate_corpus_content(text, path)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")

    import subprocess

    fixup = ROOT / "tools" / "ch1_integration_fixup.py"
    if fixup.exists():
        subprocess.run([sys.executable, str(fixup)], check=True, cwd=ROOT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
