#!/usr/bin/env python3
"""Renumber Chapter One Part B §§11–16 → §§9–14 (consecutive after Part A §§1–8)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_A = ROOT / "core_01_a_values_principles.md"
PART_B = ROOT / "core_01_b_stewardship_capacity_principles.md"

SECTION_MAP = {11: 9, 12: 10, 13: 11, 14: 12, 15: 13, 16: 14}

LEGACY_ANCHOR_STUBS = """
<!-- Legacy Part B §§11–16 anchor redirects (2026-06 consecutive renumber); do not remove without link migration. -->
<a id="11-stewardship-and-distributed-understanding"></a>
<a id="111-stewardship"></a>
<a id="112-distributed-understanding"></a>
<a id="113-institutional-development"></a>
<a id="114-openness-aspiration"></a>
<a id="12-governance-under-stewardship-discipline"></a>
<a id="12-governance-as-authorized-structure"></a>
<a id="122-incentive-alignment-and-system-capture"></a>
<a id="1221-alignment-requirement"></a>
<a id="122-alignment-requirement"></a>
<a id="1222-misalignment-correction-and-capture-response"></a>
<a id="1223-contingent-claims-games-of-chance-and-event-contract-markets"></a>
<a id="123-stewardship-and-operator-incentive-alignment"></a>
<a id="13-shared-system-capacity"></a>
<a id="131-productive-capacity-instrumental-good"></a>
<a id="132-constitutional-efficiency"></a>
<a id="14-market-structure"></a>
<a id="141-concentration-threshold-mechanism-adopter-tunable"></a>
<a id="142-pro-competition-and-anti-domination"></a>
<a id="143-consolidation-ceiling"></a>
<a id="1431-consolidation-risk-pre-lock-in-impairment"></a>
<a id="1432-ceiling-discipline-adopter-requirements"></a>
<a id="15-systemic-evaluation-requirement"></a>
<a id="151-required-evaluation-factors"></a>
<a id="1511-systemic-scope-and-risk-factors"></a>
<a id="1512-accessibility-under-sentience-non-exclusion"></a>
<a id="1513-privacy-informational-joint-invocation"></a>
<a id="1514-voluntary-discontinuation-and-exit-rights"></a>
<a id="1515-assembly-collective-organization-and-institutional-formation"></a>
<a id="1516-time-consistency-constraint"></a>
<a id="152-read-with-governance-and-incentive-discipline"></a>
<a id="16-integrated-application"></a>
"""

_TO_PH: list[tuple[str, str]] = [
    ("Chapter One §16 Integrated Application", "__CH1PB14INT__"),
    ("Chapter One §15.2 Read-with", "__CH1PB132RW__"),
    ("Chapter One §15.2", "__CH1PB132__"),
    ("Chapter One §15.1.6", "__CH1PB1316__"),
    ("Chapter One §15.1.5", "__CH1PB1315__"),
    ("Chapter One §15.1.4", "__CH1PB1314__"),
    ("Chapter One §15.1.3", "__CH1PB1313__"),
    ("Chapter One §15.1.2", "__CH1PB1312__"),
    ("Chapter One §15.1.1", "__CH1PB1311__"),
    ("Chapter One §15.1 Required Evaluation Factors", "__CH1PB131__"),
    ("Chapter One §15 Systemic Evaluation Requirement", "__CH1PB13EV__"),
    ("Chapter One §14.3.2", "__CH1PB1232__"),
    ("Chapter One §14.3.1", "__CH1PB1231__"),
    ("Chapter One §14.3 Consolidation Ceiling", "__CH1PB123__"),
    ("Chapter One §14.3", "__CH1PB123__"),
    ("Chapter One §14.2 Pro-Competition and Anti-Domination", "__CH1PB122PC__"),
    ("Chapter One §14.2", "__CH1PB122__"),
    ("Chapter One §14.1 Concentration Threshold Mechanism", "__CH1PB121CT__"),
    ("Chapter One §14.1", "__CH1PB121__"),
    ("Chapter One §14 Market Structure", "__CH1PB12MS__"),
    ("Chapter One §13.2 Constitutional Efficiency", "__CH1PB112CE__"),
    ("Chapter One §13.2", "__CH1PB112__"),
    ("Chapter One §13.1 Productive Capacity", "__CH1PB111PC__"),
    ("Chapter One §13.1", "__CH1PB111__"),
    ("Chapter One §13 Shared-System Capacity", "__CH1PB11CAP__"),
    ("Chapter One §12.3 Stewardship and Operator Incentive Alignment", "__CH1PB103SO__"),
    ("Chapter One §12.3", "__CH1PB103__"),
    ("Chapter One §12.2.3", "__CH1PB1023__"),
    ("Chapter One §12.2.2", "__CH1PB1022__"),
    ("Chapter One §12.2.1", "__CH1PB1021__"),
    ("Chapter One §12.2 Incentive Alignment and System Capture", "__CH1PB102IA__"),
    ("Chapter One §12.2", "__CH1PB102__"),
    ("Chapter One §12.1 Governance as Authorized Structure", "__CH1PB101GAS__"),
    ("Chapter One §12.1", "__CH1PB101__"),
    ("Chapter One §12 Governance Under Stewardship Discipline", "__CH1PB10GOV__"),
    ("Chapter One §11.4 Openness Aspiration", "__CH1PB094OA__"),
    ("Chapter One §11.4", "__CH1PB094__"),
    ("Chapter One §11.3 Institutional Development", "__CH1PB093ID__"),
    ("Chapter One §11.3", "__CH1PB093__"),
    ("Chapter One §11.2 Distributed Understanding", "__CH1PB092DU__"),
    ("Chapter One §11.2", "__CH1PB092__"),
    ("Chapter One §11.1 Stewardship", "__CH1PB091ST__"),
    ("Chapter One §11.1", "__CH1PB091__"),
    ("Chapter One §11 Stewardship and Distributed Understanding", "__CH1PB09STEW__"),
]

_FROM_PH: list[tuple[str, str]] = [
    ("__CH1PB14INT__", "Chapter One §14 Integrated Application"),
    ("__CH1PB132RW__", "Chapter One §13.2 Read-with"),
    ("__CH1PB132__", "Chapter One §13.2"),
    ("__CH1PB1316__", "Chapter One §13.1.6"),
    ("__CH1PB1315__", "Chapter One §13.1.5"),
    ("__CH1PB1314__", "Chapter One §13.1.4"),
    ("__CH1PB1313__", "Chapter One §13.1.3"),
    ("__CH1PB1312__", "Chapter One §13.1.2"),
    ("__CH1PB1311__", "Chapter One §13.1.1"),
    ("__CH1PB131__", "Chapter One §13.1 Required Evaluation Factors"),
    ("__CH1PB13EV__", "Chapter One §13 Systemic Evaluation Requirement"),
    ("__CH1PB1232__", "Chapter One §12.3.2"),
    ("__CH1PB1231__", "Chapter One §12.3.1"),
    ("__CH1PB123__", "Chapter One §12.3"),
    ("__CH1PB122PC__", "Chapter One §12.2 Pro-Competition and Anti-Domination"),
    ("__CH1PB122__", "Chapter One §12.2"),
    ("__CH1PB121CT__", "Chapter One §12.1 Concentration Threshold Mechanism"),
    ("__CH1PB121__", "Chapter One §12.1"),
    ("__CH1PB12MS__", "Chapter One §12 Market Structure"),
    ("__CH1PB112CE__", "Chapter One §11.2 Constitutional Efficiency"),
    ("__CH1PB112__", "Chapter One §11.2"),
    ("__CH1PB111PC__", "Chapter One §11.1 Productive Capacity"),
    ("__CH1PB111__", "Chapter One §11.1"),
    ("__CH1PB11CAP__", "Chapter One §11 Shared-System Capacity"),
    ("__CH1PB103SO__", "Chapter One §10.3 Stewardship and Operator Incentive Alignment"),
    ("__CH1PB103__", "Chapter One §10.3"),
    ("__CH1PB1023__", "Chapter One §10.2.3"),
    ("__CH1PB1022__", "Chapter One §10.2.2"),
    ("__CH1PB1021__", "Chapter One §10.2.1"),
    ("__CH1PB102IA__", "Chapter One §10.2 Incentive Alignment and System Capture"),
    ("__CH1PB102__", "Chapter One §10.2"),
    ("__CH1PB101GAS__", "Chapter One §10.1 Governance as Authorized Structure"),
    ("__CH1PB101__", "Chapter One §10.1"),
    ("__CH1PB10GOV__", "Chapter One §10 Governance Under Stewardship Discipline"),
    ("__CH1PB094OA__", "Chapter One §9.4 Openness Aspiration"),
    ("__CH1PB094__", "Chapter One §9.4"),
    ("__CH1PB093ID__", "Chapter One §9.3 Institutional Development"),
    ("__CH1PB093__", "Chapter One §9.3"),
    ("__CH1PB092DU__", "Chapter One §9.2 Distributed Understanding"),
    ("__CH1PB092__", "Chapter One §9.2"),
    ("__CH1PB091ST__", "Chapter One §9.1 Stewardship"),
    ("__CH1PB091__", "Chapter One §9.1"),
    ("__CH1PB09STEW__", "Chapter One §9 Stewardship and Distributed Understanding"),
]

ANCHOR_PATH_MIGRATIONS: list[tuple[str, str]] = [
    ("core_01_b_stewardship_capacity_principles.md#16-integrated-application", "core_01_b_stewardship_capacity_principles.md#14-integrated-application"),
    ("core_01_b_stewardship_capacity_principles.md#15-systemic-evaluation-requirement", "core_01_b_stewardship_capacity_principles.md#13-systemic-evaluation-requirement"),
    ("core_01_b_stewardship_capacity_principles.md#152-read-with-governance-and-incentive-discipline", "core_01_b_stewardship_capacity_principles.md#132-read-with-governance-and-incentive-discipline"),
    ("core_01_b_stewardship_capacity_principles.md#1516-time-consistency-constraint", "core_01_b_stewardship_capacity_principles.md#1316-time-consistency-constraint"),
    ("core_01_b_stewardship_capacity_principles.md#1515-assembly-collective-organization-and-institutional-formation", "core_01_b_stewardship_capacity_principles.md#1315-assembly-collective-organization-and-institutional-formation"),
    ("core_01_b_stewardship_capacity_principles.md#1514-voluntary-discontinuation-and-exit-rights", "core_01_b_stewardship_capacity_principles.md#1314-voluntary-discontinuation-and-exit-rights"),
    ("core_01_b_stewardship_capacity_principles.md#1513-privacy-informational-joint-invocation", "core_01_b_stewardship_capacity_principles.md#1313-privacy-informational-joint-invocation"),
    ("core_01_b_stewardship_capacity_principles.md#1512-accessibility-under-sentience-non-exclusion", "core_01_b_stewardship_capacity_principles.md#1312-accessibility-under-sentience-non-exclusion"),
    ("core_01_b_stewardship_capacity_principles.md#1511-systemic-scope-and-risk-factors", "core_01_b_stewardship_capacity_principles.md#1311-systemic-scope-and-risk-factors"),
    ("core_01_b_stewardship_capacity_principles.md#151-required-evaluation-factors", "core_01_b_stewardship_capacity_principles.md#131-required-evaluation-factors"),
    ("core_01_b_stewardship_capacity_principles.md#1432-ceiling-discipline-adopter-requirements", "core_01_b_stewardship_capacity_principles.md#1232-ceiling-discipline-adopter-requirements"),
    ("core_01_b_stewardship_capacity_principles.md#1431-consolidation-risk-pre-lock-in-impairment", "core_01_b_stewardship_capacity_principles.md#1231-consolidation-risk-pre-lock-in-impairment"),
    ("core_01_b_stewardship_capacity_principles.md#143-consolidation-ceiling", "core_01_b_stewardship_capacity_principles.md#123-consolidation-ceiling"),
    ("core_01_b_stewardship_capacity_principles.md#142-pro-competition-and-anti-domination", "core_01_b_stewardship_capacity_principles.md#122-pro-competition-and-anti-domination"),
    ("core_01_b_stewardship_capacity_principles.md#141-concentration-threshold-mechanism-adopter-tunable", "core_01_b_stewardship_capacity_principles.md#121-concentration-threshold-mechanism-adopter-tunable"),
    ("core_01_b_stewardship_capacity_principles.md#14-market-structure", "core_01_b_stewardship_capacity_principles.md#12-market-structure"),
    ("core_01_b_stewardship_capacity_principles.md#132-constitutional-efficiency", "core_01_b_stewardship_capacity_principles.md#112-constitutional-efficiency"),
    ("core_01_b_stewardship_capacity_principles.md#131-productive-capacity-instrumental-good", "core_01_b_stewardship_capacity_principles.md#111-productive-capacity-instrumental-good"),
    ("core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity", "core_01_b_stewardship_capacity_principles.md#11-shared-system-capacity"),
    ("core_01_b_stewardship_capacity_principles.md#123-stewardship-and-operator-incentive-alignment", "core_01_b_stewardship_capacity_principles.md#103-stewardship-and-operator-incentive-alignment"),
    ("core_01_b_stewardship_capacity_principles.md#1223-contingent-claims-games-of-chance-and-event-contract-markets", "core_01_b_stewardship_capacity_principles.md#1023-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("core_01_b_stewardship_capacity_principles.md#1222-misalignment-correction-and-capture-response", "core_01_b_stewardship_capacity_principles.md#1022-misalignment-correction-and-capture-response"),
    ("core_01_b_stewardship_capacity_principles.md#1221-alignment-requirement", "core_01_b_stewardship_capacity_principles.md#1021-alignment-requirement"),
    ("core_01_b_stewardship_capacity_principles.md#122-alignment-requirement", "core_01_b_stewardship_capacity_principles.md#1021-alignment-requirement"),
    ("core_01_b_stewardship_capacity_principles.md#122-incentive-alignment-and-system-capture", "core_01_b_stewardship_capacity_principles.md#102-incentive-alignment-and-system-capture"),
    ("core_01_b_stewardship_capacity_principles.md#12-governance-as-authorized-structure", "core_01_b_stewardship_capacity_principles.md#101-governance-as-authorized-structure"),
    ("core_01_b_stewardship_capacity_principles.md#12-governance-under-stewardship-discipline", "core_01_b_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline"),
    ("core_01_b_stewardship_capacity_principles.md#114-openness-aspiration", "core_01_b_stewardship_capacity_principles.md#94-openness-aspiration"),
    ("core_01_b_stewardship_capacity_principles.md#113-institutional-development", "core_01_b_stewardship_capacity_principles.md#93-institutional-development"),
    ("core_01_b_stewardship_capacity_principles.md#112-distributed-understanding", "core_01_b_stewardship_capacity_principles.md#92-distributed-understanding"),
    ("core_01_b_stewardship_capacity_principles.md#111-stewardship", "core_01_b_stewardship_capacity_principles.md#91-stewardship"),
    ("core_01_b_stewardship_capacity_principles.md#11-stewardship-and-distributed-understanding", "core_01_b_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding"),
    ("#16-integrated-application", "#14-integrated-application"),
    ("#15-systemic-evaluation-requirement", "#13-systemic-evaluation-requirement"),
    ("#152-read-with-governance-and-incentive-discipline", "#132-read-with-governance-and-incentive-discipline"),
    ("#1516-time-consistency-constraint", "#1316-time-consistency-constraint"),
    ("#1515-assembly-collective-organization-and-institutional-formation", "#1315-assembly-collective-organization-and-institutional-formation"),
    ("#1514-voluntary-discontinuation-and-exit-rights", "#1314-voluntary-discontinuation-and-exit-rights"),
    ("#1513-privacy-informational-joint-invocation", "#1313-privacy-informational-joint-invocation"),
    ("#1512-accessibility-under-sentience-non-exclusion", "#1312-accessibility-under-sentience-non-exclusion"),
    ("#1511-systemic-scope-and-risk-factors", "#1311-systemic-scope-and-risk-factors"),
    ("#151-required-evaluation-factors", "#131-required-evaluation-factors"),
    ("#1432-ceiling-discipline-adopter-requirements", "#1232-ceiling-discipline-adopter-requirements"),
    ("#1431-consolidation-risk-pre-lock-in-impairment", "#1231-consolidation-risk-pre-lock-in-impairment"),
    ("#143-consolidation-ceiling", "#123-consolidation-ceiling"),
    ("#142-pro-competition-and-anti-domination", "#122-pro-competition-and-anti-domination"),
    ("#141-concentration-threshold-mechanism-adopter-tunable", "#121-concentration-threshold-mechanism-adopter-tunable"),
    ("#14-market-structure", "#12-market-structure"),
    ("#132-constitutional-efficiency", "#112-constitutional-efficiency"),
    ("#131-productive-capacity-instrumental-good", "#111-productive-capacity-instrumental-good"),
    ("#13-shared-system-capacity", "#11-shared-system-capacity"),
    ("#123-stewardship-and-operator-incentive-alignment", "#103-stewardship-and-operator-incentive-alignment"),
    ("#1223-contingent-claims-games-of-chance-and-event-contract-markets", "#1023-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("#1222-misalignment-correction-and-capture-response", "#1022-misalignment-correction-and-capture-response"),
    ("#1221-alignment-requirement", "#1021-alignment-requirement"),
    ("#122-alignment-requirement", "#1021-alignment-requirement"),
    ("#122-incentive-alignment-and-system-capture", "#102-incentive-alignment-and-system-capture"),
    ("#12-governance-as-authorized-structure", "#101-governance-as-authorized-structure"),
    ("#12-governance-under-stewardship-discipline", "#10-governance-under-stewardship-discipline"),
    ("#114-openness-aspiration", "#94-openness-aspiration"),
    ("#113-institutional-development", "#93-institutional-development"),
    ("#112-distributed-understanding", "#92-distributed-understanding"),
    ("#111-stewardship", "#91-stewardship"),
    ("#11-stewardship-and-distributed-understanding", "#9-stewardship-and-distributed-understanding"),
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


def renumber_part_b_body(text: str) -> str:
    """Single-pass §11–§16 → §9–§14 on assembled Part B body (16 down to 11)."""
    order = sorted(SECTION_MAP.items(), reverse=True)
    for old, new in order:
        ph = f"__R{new}__"
        for level in ("#####", "####", "###"):
            text = re.sub(rf"^{level} {old}\.", f"{level} {ph}.", text, flags=re.M)
        text = re.sub(rf"§{old}\.(\d+(?:\.\d+)*)", rf"§{ph}.\1", text)
        text = re.sub(rf"§{old}\b", f"§{ph}", text)

        def anchor_repl(m: re.Match[str], o: int = old, p: str = ph) -> str:
            aid = m.group(1)
            if re.match(rf"^{o}(\d|-)", aid):
                return f'<a id="{p}{aid[len(str(o)):]}"></a>'
            return m.group(0)

        text = re.sub(r'<a id="(\d[^"]*)"></a>', anchor_repl, text)

        def link_repl(m: re.Match[str], o: int = old, p: str = ph) -> str:
            label, anchor = m.group(1), m.group(2)
            if re.match(rf"^{o}(\d|-)", anchor):
                return f"[{label}](#{p}{anchor[len(str(o)):]})"
            return m.group(0)

        text = re.sub(r"\[([^\]]+)\]\(#(\d[^)]*)\)", link_repl, text)

    for _, new in order:
        text = text.replace(f"__R{new}__", str(new))
    return text


def update_metadata(text: str) -> str:
    repl = [
        ("§§11–16", "§§9–14"),
        ("§§11-16", "§§9-14"),
        ("§§11–15", "§§9–13"),
        ("§§11-15", "§§9-13"),
        (
            "§11 stewardship → §12 governance → §13 capacity → §14 market structure → §15 systemic evaluation → **§16 integrated application**",
            "§9 stewardship → §10 governance → §11 capacity → §12 market structure → §13 systemic evaluation → **§14 integrated application**",
        ),
        ("**[§9 Market Structure](#9-market-structure)**", "**[§12 Market Structure](#12-market-structure)**"),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    return text


def reassemble_part_b(part_b: str) -> str:
    file_top, body = part_b.split("## CHAPTER 01, PART B", 1)
    file_top = update_metadata(file_top)
    body = "## CHAPTER 01, PART B" + body

    idx = body.find("### 11.")
    intro, rest = body[:idx], body[idx:]
    rest = re.sub(
        r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n?",
        "\n",
        rest,
    )

    s11, rest = extract_h3_section(rest, 11)
    s12, rest = extract_h3_section(rest, 12)
    s13, rest = extract_h3_section(rest, 13)
    s14, rest = extract_h3_section(rest, 14)
    s15, rest = extract_h3_section(rest, 15)
    s16, _ = extract_h3_section(rest, 16)

    assembled = intro + s11 + s12 + s13 + s14 + s15 + s16
    assembled = renumber_part_b_body(assembled)
    assembled = update_metadata(assembled)

    # Principle hierarchy: align list numbers with §9–§14
    assembled = re.sub(
        r"^1\. (\*\*\[Stewardship\])",
        r"9. \1",
        assembled,
        count=1,
        flags=re.M,
    )
    assembled = re.sub(r"^2\. (\*\*\[Governance\])", r"10. \1", assembled, count=1, flags=re.M)
    assembled = re.sub(
        r"^3\. (\*\*\[Shared-System Capacity\])",
        r"11. \1",
        assembled,
        count=1,
        flags=re.M,
    )
    assembled = re.sub(
        r"^4\. (\*\*\[Systemic Evaluation Requirement\])",
        r"13. \1",
        assembled,
        count=1,
        flags=re.M,
    )
    assembled = re.sub(
        r"^5\. (\*\*\[Integrated Application\])",
        r"14. \1",
        assembled,
        count=1,
        flags=re.M,
    )
    if "12. **[Market Structure]" not in assembled:
        assembled = assembled.replace(
            "not a freestanding trump value. **[Market Structure]",
            "not a freestanding trump value.\n12. **[Market Structure]",
            1,
        )

    if "Legacy Part B §§11–16 anchor redirects" not in assembled:
        legacy_start = assembled.find("<!-- Legacy Chapter One anchor redirects")
        if legacy_start != -1:
            assembled = assembled[:legacy_start] + LEGACY_ANCHOR_STUBS + assembled[legacy_start:]

    footer = """
---

**Previous file:** [core_01_a_values_principles.md](core_01_a_values_principles.md)

**Next file:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)
"""
    return file_top + assembled + footer


def update_part_a_next_pointer(text: str) -> str:
    return text.replace(
        "Chapter One, Part B — §§11–16, including systemic evaluation and integrated application capstone",
        "Chapter One, Part B — §§9–14, including systemic evaluation and integrated application capstone",
    )


def migrate_section_refs(content: str) -> str:
    for old, new in sorted(_TO_PH, key=lambda x: len(x[0]), reverse=True):
        content = content.replace(old, new)
    for old, new in _FROM_PH:
        content = content.replace(old, new)
    return content


def migrate_corpus(content: str, path: Path) -> str:
    if path.name in (
        "ch1_part_b_consecutive_renumber.py",
        "ch1_reading_arc_b.py",
        "ch1_integration_relocation.py",
        "ch1_integration_fixup.py",
        "ch1_market_structure_split.py",
    ):
        return content
    orig = content
    for old, new in sorted(ANCHOR_PATH_MIGRATIONS, key=lambda x: len(x[0]), reverse=True):
        if old != new:
            content = content.replace(old, new)
    content = migrate_section_refs(content)
    simple = [
        ("§§11–16", "§§9–14"),
        ("§§11-16", "§§9-14"),
        ("§§11–15", "§§9–13"),
        ("§§11-15", "§§9-13"),
        ("Part B (§§11–16", "Part B (§§9–14"),
        ("Part B (§§11-16", "Part B (§§9-14"),
        ("→ Part B (§§11–15", "→ Part B (§§9–13"),
        ("→ **§16 Integrated Application**", "→ **§14 Integrated Application**"),
        ("Continuity aim** when linking to Chapter One §13", "Continuity aim** when linking to Chapter One §11"),
        ("**[§9 Market Structure](#9-market-structure)**", "**[§12 Market Structure](#12-market-structure)**"),
        ("[§14 Market Structure]", "[§12 Market Structure]"),
        ("[§14.1 ", "[§12.1 "),
        ("[§14.2 ", "[§12.2 "),
        ("[§14.3 ", "[§12.3 "),
        ("Chapter One §14.3", "Chapter One §12.3"),
        ("Chapter One §14.2", "Chapter One §12.2"),
        ("Chapter One §14.1", "Chapter One §12.1"),
        ("§12.3 Stewardship and Operator", "§10.3 Stewardship and Operator"),
        ("§12 Governance Under", "§10 Governance Under"),
    ]
    for old, new in simple:
        content = content.replace(old, new)
    return content if content != orig else content


def main() -> int:
    part_a = PART_A.read_text(encoding="utf-8")
    part_b = PART_B.read_text(encoding="utf-8")

    new_b = reassemble_part_b(part_b)
    new_a = update_part_a_next_pointer(part_a)

    PART_B.write_text(new_b, encoding="utf-8")
    PART_A.write_text(new_a, encoding="utf-8")
    print(f"Wrote {PART_B}")
    print(f"Wrote {PART_A}")

    skip = {".git", "archive", "evidence", "node_modules", "__pycache__", ".cursor"}
    for path in ROOT.rglob("*"):
        if path in (PART_A, PART_B):
            continue
        if any(p in skip for p in path.parts):
            continue
        if path.suffix not in {".md", ".json", ".py"}:
            continue
        if path.name == "ch1_part_b_consecutive_renumber.py":
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
