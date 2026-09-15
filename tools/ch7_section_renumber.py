#!/usr/bin/env python3
"""Renumber Chapter Seven: §1A → §2; shift §2–§10 up by one (§2→§3 … §10→§11)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH7 = ROOT / "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation"

ANCHOR_REMAP: dict[str, str] = {
    "1a-whole-system-certification-evaluation": "2-whole-system-certification-evaluation",
    "1a1-systemic-scope-and-risk-factors": "21-systemic-scope-and-risk-factors",
    "1a2-accessibility-under-sentience-non-exclusion": "22-accessibility-under-sentience-non-exclusion",
    "1a3-privacy-informational-joint-invocation": "23-privacy-informational-joint-invocation",
    "1a4-voluntary-discontinuation-and-exit-rights": "24-voluntary-discontinuation-and-exit-rights",
    "1a5-assembly-collective-organization-and-institutional-formation": (
        "25-assembly-collective-organization-and-institutional-formation"
    ),
    "1a6-time-consistency-constraint": "26-time-consistency-constraint",
    "1a7-governance-incentive-and-contestability-discipline": "27-governance-incentive-and-contestability-discipline",
    "2-certification-record": "3-certification-record",
    "3-system-class-evaluation": "4-system-class-evaluation",
    "4-data-types-and-handling-evaluation": "5-data-types-and-handling-evaluation",
    "5-ecological-footprint-evaluation": "6-ecological-footprint-evaluation",
    "5a-proportionate-cross-system-support-evaluation": "6a-proportionate-cross-system-support-evaluation",
    "5b-nondiscrimination-evaluation": "6b-nondiscrimination-evaluation",
    "5c-accessibility-evaluation": "6c-accessibility-evaluation",
    "5d-educational-capability-and-learning-system-integrity-evaluation": (
        "6d-educational-capability-and-learning-system-integrity-evaluation"
    ),
    "5e-trustworthiness-and-system-reliance-integrity-evaluation": (
        "6e-trustworthiness-and-system-reliance-integrity-evaluation"
    ),
    "6-transparency-auditability-and-contestability": "7-transparency-auditability-and-contestability",
    "7-supervisory-sequence-and-contestability-chain": "8-supervisory-sequence-and-contestability-chain",
    "8-forum-supervision-and-component-roles": "9-forum-supervision-and-component-roles",
    "9-relationship-to-standing": "10-relationship-to-standing",
    "10-reopening-drift-and-non-evasion": "11-reopening-drift-and-non-evasion",
}

HEADING_REMAP: list[tuple[str, str]] = [
    ("### 1A. Whole-System Certification Evaluation", "### 2. Whole-System Certification Evaluation"),
    ("#### 1A.7 Governance, Incentive, and Contestability Discipline", "#### 2.7 Governance, Incentive, and Contestability Discipline"),
    ("#### 1A.6 Time-Consistency Constraint", "#### 2.6 Time-Consistency Constraint"),
    ("#### 1A.5 Assembly, Collective Organization, and Institutional Formation", "#### 2.5 Assembly, Collective Organization, and Institutional Formation"),
    ("#### 1A.4 Voluntary Discontinuation and Exit Rights", "#### 2.4 Voluntary Discontinuation and Exit Rights"),
    ("#### 1A.3 Privacy (Informational) Joint Invocation", "#### 2.3 Privacy (Informational) Joint Invocation"),
    ("#### 1A.2 Accessibility Under Sentience Non-Exclusion", "#### 2.2 Accessibility Under Sentience Non-Exclusion"),
    ("#### 1A.1 Systemic Scope and Risk Factors", "#### 2.1 Systemic Scope and Risk Factors"),
    ("### 10. Reopening, Misalignment, and Non-Evasion", "### 11. Reopening, Misalignment, and Non-Evasion"),
    ("### 9. Relationship to Standing", "### 10. Relationship to Standing"),
    ("### 8. Forum Supervision and Component Roles", "### 9. Forum Supervision and Component Roles"),
    ("### 7. Supervisory Sequence and Contestability Chain", "### 8. Supervisory Sequence and Contestability Chain"),
    ("#### 7.3 Anti-bypass", "#### 8.3 Anti-bypass"),
    ("#### 7.2 Contestability chain", "#### 8.2 Contestability chain"),
    ("#### 7.1 Supervisory sequence", "#### 8.1 Supervisory sequence"),
    ("### 6. Transparency, Auditability, and Contestability", "### 7. Transparency, Auditability, and Contestability"),
    ("### 5E. Trustworthiness and System-Reliance Integrity Evaluation", "### 6E. Trustworthiness and System-Reliance Integrity Evaluation"),
    ("### 5D. Educational Capability and Learning-System Integrity Evaluation", "### 6D. Educational Capability and Learning-System Integrity Evaluation"),
    ("### 5C. Accessibility Evaluation", "### 6C. Accessibility Evaluation"),
    ("### 5B. Nondiscrimination Evaluation", "### 6B. Nondiscrimination Evaluation"),
    ("### 5A. Proportionate Cross-System Support Evaluation", "### 6A. Proportionate Cross-System Support Evaluation"),
    ("### 5. Ecological Footprint Evaluation", "### 6. Ecological Footprint Evaluation"),
    ("### 4. Data Types and Handling Evaluation", "### 5. Data Types and Handling Evaluation"),
    ("### 3. System Class Evaluation", "### 4. System Class Evaluation"),
    ("#### 3.2 Initial recognition, ongoing recertification, and defects", "#### 4.2 Initial recognition, ongoing recertification, and defects"),
    ("#### 3.1 Recertification regression requirement", "#### 4.1 Recertification regression requirement"),
    ("### 2. Certification Record", "### 3. Certification Record"),
]

# Prose / trace section refs — longest match first.
SECTION_REF_REMAP: list[tuple[str, str]] = [
    ("Chapter Seven §1A.7", "Chapter Seven §2.7"),
    ("Chapter Seven §1A.6", "Chapter Seven §2.6"),
    ("Chapter Seven §1A.5", "Chapter Seven §2.5"),
    ("Chapter Seven §1A.4", "Chapter Seven §2.4"),
    ("Chapter Seven §1A.3", "Chapter Seven §2.3"),
    ("Chapter Seven §1A.2", "Chapter Seven §2.2"),
    ("Chapter Seven §1A.1", "Chapter Seven §2.1"),
    ("Chapter Seven §1A Whole-System Certification Evaluation", "Chapter Seven §2 Whole-System Certification Evaluation"),
    ("Chapter Seven §1A", "Chapter Seven §2"),
    ("Chapter Seven §10", "Chapter Seven §11"),
    ("Chapter Seven §9", "Chapter Seven §10"),
    ("Chapter Seven §8", "Chapter Seven §9"),
    ("Chapter Seven §7.3", "Chapter Seven §8.3"),
    ("Chapter Seven §7.2", "Chapter Seven §8.2"),
    ("Chapter Seven §7.1", "Chapter Seven §8.1"),
    ("Chapter Seven §7", "Chapter Seven §8"),
    ("Chapter Seven §6", "Chapter Seven §7"),
    ("Chapter Seven §5E", "Chapter Seven §6E"),
    ("Chapter Seven §5D", "Chapter Seven §6D"),
    ("Chapter Seven §5C", "Chapter Seven §6C"),
    ("Chapter Seven §5B", "Chapter Seven §6B"),
    ("Chapter Seven §5A", "Chapter Seven §6A"),
    ("Chapter Seven §5", "Chapter Seven §6"),
    ("Chapter Seven §4", "Chapter Seven §5"),
    ("Chapter Seven §3.2", "Chapter Seven §4.2"),
    ("Chapter Seven §3.1", "Chapter Seven §4.1"),
    ("Chapter Seven §3", "Chapter Seven §4"),
    ("Chapter Seven §2", "Chapter Seven §3"),
    ("Chapter Seven — §10", "Chapter Seven — §11"),
    ("Chapter Seven — §9", "Chapter Seven — §10"),
    ("Chapter Seven — §8", "Chapter Seven — §9"),
    ("Chapter Seven — §7", "Chapter Seven — §8"),
    ("Chapter Seven — §6", "Chapter Seven — §7"),
    ("Chapter Seven — §5", "Chapter Seven — §6"),
    ("Chapter Seven — §4", "Chapter Seven — §5"),
    ("Chapter Seven — §3", "Chapter Seven — §4"),
    ("Chapter Seven — §2", "Chapter Seven — §3"),
]

# Internal [§…] links inside ch7 only — applied after headings/anchors.
INTERNAL_LINK_REMAP: list[tuple[str, str]] = [
    ("[§1A](#1a-whole-system-certification-evaluation)", "[§2](#2-whole-system-certification-evaluation)"),
    ("[§1A.1](#1a1-systemic-scope-and-risk-factors)", "[§2.1](#21-systemic-scope-and-risk-factors)"),
    ("[§1A.2](#1a2-accessibility-under-sentience-non-exclusion)", "[§2.2](#22-accessibility-under-sentience-non-exclusion)"),
    ("[§1A.3](#1a3-privacy-informational-joint-invocation)", "[§2.3](#23-privacy-informational-joint-invocation)"),
    ("[§1A.4](#1a4-voluntary-discontinuation-and-exit-rights)", "[§2.4](#24-voluntary-discontinuation-and-exit-rights)"),
    ("[§1A.5](#1a5-assembly-collective-organization-and-institutional-formation)", "[§2.5](#25-assembly-collective-organization-and-institutional-formation)"),
    ("[§1A.6](#1a6-time-consistency-constraint)", "[§2.6](#26-time-consistency-constraint)"),
    ("[§1A.7](#1a7-governance-incentive-and-contestability-discipline)", "[§2.7](#27-governance-incentive-and-contestability-discipline)"),
    ("[§10](#10-reopening-drift-and-non-evasion)", "[§11](#11-reopening-drift-and-non-evasion)"),
    ("[§9](#9-relationship-to-standing)", "[§10](#10-relationship-to-standing)"),
    ("[§8](#8-forum-supervision-and-component-roles)", "[§9](#9-forum-supervision-and-component-roles)"),
    ("[§7](#7-supervisory-sequence-and-contestability-chain)", "[§8](#8-supervisory-sequence-and-contestability-chain)"),
    ("[§6](#6-transparency-auditability-and-contestability)", "[§7](#7-transparency-auditability-and-contestability)"),
    ("[§5E](#5e-trustworthiness-and-system-reliance-integrity-evaluation)", "[§6E](#6e-trustworthiness-and-system-reliance-integrity-evaluation)"),
    ("[§5D](#5d-educational-capability-and-learning-system-integrity-evaluation)", "[§6D](#6d-educational-capability-and-learning-system-integrity-evaluation)"),
    ("[§5C](#5c-accessibility-evaluation)", "[§6C](#6c-accessibility-evaluation)"),
    ("[§5B](#5b-nondiscrimination-evaluation)", "[§6B](#6b-nondiscrimination-evaluation)"),
    ("[§5A](#5a-proportionate-cross-system-support-evaluation)", "[§6A](#6a-proportionate-cross-system-support-evaluation)"),
    ("[§5](#5-ecological-footprint-evaluation)", "[§6](#6-ecological-footprint-evaluation)"),
    ("[§4](#4-data-types-and-handling-evaluation)", "[§5](#5-data-types-and-handling-evaluation)"),
    ("[§3](#3-system-class-evaluation)", "[§4](#4-system-class-evaluation)"),
    ("[§2](#2-certification-record)", "[§3](#3-certification-record)"),
]

INTERNAL_BARE_REF_REMAP: list[tuple[str, str]] = [
    ("**Chapter Seven §3.1** and **§3.2**", "**Chapter Seven §4.1** and **§4.2**"),
    ("under **§3**", "under **§4**"),
    ("under **§4**", "under **§5**"),
    ("under **§5**", "under **§6**"),
    ("under **§5A**", "under **§6A**"),
    ("under **§5B**", "under **§6B**"),
    ("under **§5C**", "under **§6C**"),
    ("under **§5D**", "under **§6D**"),
    ("under **§5E**", "under **§6E**"),
    ("under **§6**", "under **§7**"),
    ("under **§7**", "under **§8**"),
    ("under **§8**", "under **§9**"),
    ("under **§9**", "under **§10**"),
    ("under **§10**", "under **§11**"),
    ("**§3.1**", "**§4.1**"),
    ("**§3.2**", "**§4.2**"),
    ("**§7.1**", "**§8.1**"),
    ("**§7.2**", "**§8.2**"),
    ("**§7.3**", "**§8.3**"),
    ("[§1A.1]", "[§2.1]"),
    ("[§1A.2]", "[§2.2]"),
    ("[§1A.3]", "[§2.3]"),
    ("[§1A.4]", "[§2.4]"),
    ("[§1A.5]", "[§2.5]"),
    ("[§1A.6]", "[§2.6]"),
    ("[§1A.7]", "[§2.7]"),
]

SKIP_GLOBS = {"archive/**", "evidence/**", ".git/**"}


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if any(Path(rel).match(g.replace("**", "*")) for g in SKIP_GLOBS):
            continue
        if rel.startswith("archive/") or rel.startswith("evidence/"):
            continue
        files.append(path)
    json_path = ROOT / "ai_corpus/indexes/crossref_matrix.json"
    if json_path.exists():
        files.append(json_path)
    return sorted(set(files))


def remap_anchors(text: str) -> str:
    for old, new in ANCHOR_REMAP.items():
        text = text.replace(f'<a id="{old}"></a>', f'<a id="{new}"></a>\n<a id="{old}"></a>')
    return text


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        text = text.replace(old, new)
    return text


def remap_markdown_links(text: str) -> str:
    for old, new in ANCHOR_REMAP.items():
        text = text.replace(
            f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation#{old}",
            f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation#{new}",
        )
    return text


def remap_bare_section_refs_in_ch7(text: str) -> str:
    """Remap bare [§N] and section N prose inside ch7 after protected §1 / §1.1."""
    # Protect §1 and §1.1 from numeric shifts.
    text = text.replace("[§1.1]", "⟦§1.1⟧")
    text = text.replace("[§1](#1-purpose-and-role)", "⟦§1-LINK⟧")
    text = text.replace("**§1.1**", "⟦§1.1-BOLD⟧")
    text = text.replace("in **§1.1**", "in ⟦§1.1-IN⟧")
    text = text.replace("#### 1.1 ", "⟦H1.1⟧")
    text = apply_replacements(text, INTERNAL_LINK_REMAP)
    text = apply_replacements(text, INTERNAL_BARE_REF_REMAP)
    # section 3 / section 4 prose (lowercase)
    section_word = [
        ("section 10", "section 11"),
        ("section 9", "section 10"),
        ("section 8", "section 9"),
        ("section 7", "section 8"),
        ("section 6", "section 7"),
        ("section 5", "section 6"),
        ("section 4", "section 5"),
        ("section 3", "section 4"),
        ("section 2", "section 3"),
    ]
    text = apply_replacements(text, section_word)
    text = text.replace("⟦§1.1⟧", "[§1.1]")
    text = text.replace("⟦§1-LINK⟧", "[§1](#1-purpose-and-role)")
    text = text.replace("⟦§1.1-BOLD⟧", "**§1.1**")
    text = text.replace("⟦§1.1-IN⟧", "in **§1.1**")
    text = text.replace("⟦H1.1⟧", "#### 1.1 ")
    return text


def process_ch7(text: str) -> str:
    text = apply_replacements(text, HEADING_REMAP)
    text = remap_anchors(text)
    text = remap_bare_section_refs_in_ch7(text)
    text = process_ch7_self_refs(text)
    return text


DOUBLE_SHIFT_FIXES: list[tuple[str, str]] = [
    ("Chapter Seven §3 Whole-System Certification Evaluation", "Chapter Seven §2 Whole-System Certification Evaluation"),
    ("Chapter Seven §3.7 ", "Chapter Seven §2.7 "),
    ("Chapter Seven §3.6 ", "Chapter Seven §2.6 "),
    ("Chapter Seven §3.5 ", "Chapter Seven §2.5 "),
    ("Chapter Seven §3.4 ", "Chapter Seven §2.4 "),
    ("Chapter Seven §3.3 ", "Chapter Seven §2.3 "),
    ("Chapter Seven §3.2 ", "Chapter Seven §2.2 "),
    ("Chapter Seven §3.1 ", "Chapter Seven §2.1 "),
    ("Chapter Seven §3.6", "Chapter Seven §2.6"),
    ("Chapter Seven §3.2", "Chapter Seven §2.2"),
    ("under **Chapter Seven §3**", "under **Chapter Seven §2**"),
    ("apply **Chapter Seven §3** evaluation", "apply **Chapter Seven §2** evaluation"),
    (
        "[Chapter Seven §3](core_07_a_system_alignment_certification_evaluation.md#2-whole-system-certification-evaluation)",
        "[Chapter Seven §2](core_07_a_system_alignment_certification_evaluation.md#2-whole-system-certification-evaluation)",
    ),
]


def process_ch7_self_refs(text: str) -> str:
    text = text.replace(
        "[Chapter Seven §1A.2](core_07_a_system_alignment_certification_evaluation.md#1a2-accessibility-under-sentience-non-exclusion)",
        "[Chapter Seven §2.2](core_07_a_system_alignment_certification_evaluation.md#22-accessibility-under-sentience-non-exclusion)",
    )
    text = text.replace(
        "**§9** states the standing bridge boundary explicitly.",
        "**§10** states the standing bridge boundary explicitly.",
    )
    return text


def process_other_file(text: str) -> str:
    text = remap_markdown_links(text)
    text = apply_replacements(text, SECTION_REF_REMAP)
    text = apply_replacements(text, DOUBLE_SHIFT_FIXES)
    return text


def main() -> None:
    changed: list[str] = []

    ch7_text = CH7.read_text(encoding="utf-8")
    new_ch7 = process_ch7(ch7_text)
    if new_ch7 != ch7_text:
        CH7.write_text(new_ch7, encoding="utf-8")
        changed.append(CH7.relative_to(ROOT).as_posix())

    for path in iter_markdown_files():
        if path == CH7:
            continue
        old = path.read_text(encoding="utf-8")
        new = process_other_file(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    print(f"Updated {len(changed)} files:")
    for name in changed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
