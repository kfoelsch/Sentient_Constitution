#!/usr/bin/env python3
"""Reorder Chapter Seven sections and renumber (drop 6A–6E letter suffixes).

New order:
  1 Purpose | 2 System Class | 3 Whole-System | 4 Data | 5 Ecological |
  6 Cross-System | 7 Nondiscrimination | 8 Accessibility | 9 Educational |
  10 Trustworthiness | 11 Certification Record | 12 Transparency |
  13 Forum Roles | 14 Supervisory Sequence | 15 Standing | 16 Reopening
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH7 = ROOT / "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation"

# Section heading regex -> logical key (physical reorder uses these keys)
SECTION_HEADING = re.compile(
    r"^### (1\. Purpose and Role|"
    r"2\. Whole-System Certification Evaluation|"
    r"3\. Certification Record|"
    r"4\. System Class Evaluation|"
    r"5\. Data Types and Handling Evaluation|"
    r"6\. Ecological Footprint Evaluation|"
    r"6A\. Proportionate Cross-System Support Evaluation|"
    r"6B\. Nondiscrimination Evaluation|"
    r"6C\. Accessibility Evaluation|"
    r"6D\. Educational Capability and Learning-System Integrity Evaluation|"
    r"6E\. Trustworthiness and System-Reliance Integrity Evaluation|"
    r"7\. Transparency, Auditability, and Contestability|"
    r"8\. Supervisory Sequence and Contestability Chain|"
    r"9\. Forum Supervision and Component Roles|"
    r"10\. Relationship to Standing|"
    r"11\. Reopening, Misalignment, and Non-Evasion)\s*$",
    re.MULTILINE,
)

KEY_FROM_TITLE = {
    "1. Purpose and Role": "s1",
    "2. Whole-System Certification Evaluation": "s2",
    "3. Certification Record": "s3",
    "4. System Class Evaluation": "s4",
    "5. Data Types and Handling Evaluation": "s5",
    "6. Ecological Footprint Evaluation": "s6",
    "6A. Proportionate Cross-System Support Evaluation": "s6a",
    "6B. Nondiscrimination Evaluation": "s6b",
    "6C. Accessibility Evaluation": "s6c",
    "6D. Educational Capability and Learning-System Integrity Evaluation": "s6d",
    "6E. Trustworthiness and System-Reliance Integrity Evaluation": "s6e",
    "7. Transparency, Auditability, and Contestability": "s7",
    "8. Supervisory Sequence and Contestability Chain": "s8",
    "9. Forum Supervision and Component Roles": "s9",
    "10. Relationship to Standing": "s10",
    "11. Reopening, Misalignment, and Non-Evasion": "s11",
}

NEW_ORDER = ["s1", "s4", "s2", "s5", "s6", "s6a", "s6b", "s6c", "s6d", "s6e", "s3", "s7", "s9", "s8", "s10", "s11"]

NEW_NUM = {
    "s1": "1",
    "s4": "2",
    "s2": "3",
    "s5": "4",
    "s6": "5",
    "s6a": "6",
    "s6b": "7",
    "s6c": "8",
    "s6d": "9",
    "s6e": "10",
    "s3": "11",
    "s7": "12",
    "s9": "13",
    "s8": "14",
    "s10": "15",
    "s11": "16",
}

NEW_TITLE_SUFFIX = {
    "s1": "1. Purpose and Role",
    "s4": "2. System Class Evaluation",
    "s2": "3. Whole-System Certification Evaluation",
    "s5": "4. Data Types and Handling Evaluation",
    "s6": "5. Ecological Footprint Evaluation",
    "s6a": "6. Proportionate Cross-System Support Evaluation",
    "s6b": "7. Nondiscrimination Evaluation",
    "s6c": "8. Accessibility Evaluation",
    "s6d": "9. Educational Capability and Learning-System Integrity Evaluation",
    "s6e": "10. Trustworthiness and System-Reliance Integrity Evaluation",
    "s3": "11. Certification Record",
    "s7": "12. Transparency, Auditability, and Contestability",
    "s9": "13. Forum Supervision and Component Roles",
    "s8": "14. Supervisory Sequence and Contestability Chain",
    "s10": "15. Relationship to Standing",
    "s11": "16. Reopening, Misalignment, and Non-Evasion",
}

# Primary anchor slug per logical section (old -> new primary)
ANCHOR_PRIMARY: dict[str, str] = {
    "1-purpose-and-role": "1-purpose-and-role",
    "2-whole-system-certification-evaluation": "3-whole-system-certification-evaluation",
    "3-certification-record": "11-certification-record",
    "4-system-class-evaluation": "2-system-class-evaluation",
    "5-data-types-and-handling-evaluation": "4-data-types-and-handling-evaluation",
    "6-ecological-footprint-evaluation": "5-ecological-footprint-evaluation",
    "6a-proportionate-cross-system-support-evaluation": "6-proportionate-cross-system-support-evaluation",
    "6b-nondiscrimination-evaluation": "7-nondiscrimination-evaluation",
    "6c-accessibility-evaluation": "8-accessibility-evaluation",
    "6d-educational-capability-and-learning-system-integrity-evaluation": (
        "9-educational-capability-and-learning-system-integrity-evaluation"
    ),
    "6e-trustworthiness-and-system-reliance-integrity-evaluation": (
        "10-trustworthiness-and-system-reliance-integrity-evaluation"
    ),
    "7-transparency-auditability-and-contestability": "12-transparency-auditability-and-contestability",
    "8-supervisory-sequence-and-contestability-chain": "14-supervisory-sequence-and-contestability-chain",
    "9-forum-supervision-and-component-roles": "13-forum-supervision-and-component-roles",
    "10-relationship-to-standing": "15-relationship-to-standing",
    "11-reopening-drift-and-non-evasion": "16-reopening-drift-and-non-evasion",
    # Whole-system subs 2.x -> 3.x
    "21-systemic-scope-and-risk-factors": "31-systemic-scope-and-risk-factors",
    "22-accessibility-under-sentience-non-exclusion": "32-accessibility-under-sentience-non-exclusion",
    "23-privacy-informational-joint-invocation": "33-privacy-informational-joint-invocation",
    "24-voluntary-discontinuation-and-exit-rights": "34-voluntary-discontinuation-and-exit-rights",
    "25-assembly-collective-organization-and-institutional-formation": (
        "35-assembly-collective-organization-and-institutional-formation"
    ),
    "26-time-consistency-constraint": "36-time-consistency-constraint",
    "27-governance-incentive-and-contestability-discipline": "37-governance-incentive-and-contestability-discipline",
    # Record subs 3.x -> 11.x
    "31-minimum-record-contents": "111-minimum-record-contents",
    "32-cross-section-record-requirements": "112-cross-section-record-requirements",
    "33-rights-floor-record-evaluation-non-substitution": "113-rights-floor-record-evaluation-non-substitution",
    # Supervisory subs 8.x -> 14.x
    "81-supervisory-sequence": "141-supervisory-sequence",
    "82-contestability-chain": "142-contestability-chain",
    "83-anti-bypass": "143-anti-bypass",
}

SKIP_GLOBS = ("archive/", "evidence/")


def split_sections(text: str) -> tuple[str, dict[str, str]]:
    matches = list(SECTION_HEADING.finditer(text))
    if not matches:
        raise RuntimeError("No Chapter Seven sections found")
    preamble = text[: matches[0].start()]
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(1)
        key = KEY_FROM_TITLE[title]
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.start() : end]
        sections[key] = body
    return preamble, sections


def renumber_section_body(key: str, body: str) -> str:
    n = NEW_NUM[key]
    old_title = [t for t, k in KEY_FROM_TITLE.items() if k == key][0]
    new_title = NEW_TITLE_SUFFIX[key]
    body = body.replace(f"### {old_title}", f"### {new_title}", 1)

    if key == "s2":
        for i in range(7, 0, -1):
            body = body.replace(f"#### 2.{i} ", f"#### 3.{i} ")
    elif key == "s3":
        for i in range(3, 0, -1):
            body = body.replace(f"#### 3.{i} ", f"#### 11.{i} ")
    elif key == "s8":
        for i in range(3, 0, -1):
            body = body.replace(f"#### 8.{i} ", f"#### 14.{i} ")

  # Lettered top-level headings
    for letter_key, old_letter in [
        ("s6a", "6A"),
        ("s6b", "6B"),
        ("s6c", "6C"),
        ("s6d", "6D"),
        ("s6e", "6E"),
    ]:
        if key == letter_key:
            body = re.sub(
                rf"^### {old_letter}\. ",
                f"### {NEW_NUM[letter_key]}. ",
                body,
                count=1,
                flags=re.MULTILINE,
            )
    return body


def add_legacy_anchor_pairs(text: str) -> str:
    """After primary anchor lines, keep old ids as aliases."""
    for old, new in ANCHOR_PRIMARY.items():
        if old == new:
            continue
        needle = f'<a id="{new}"></a>'
        alias = f'<a id="{old}"></a>'
        if needle in text and alias not in text:
            text = text.replace(needle, f"{needle}\n{alias}", 1)
    return text


def build_section_ref_table() -> list[tuple[str, str]]:
    """Global prose/link replacements — longest match first."""
    pairs: list[tuple[str, str]] = []

    def add(old: str, new: str) -> None:
        pairs.append((old, new))

    # Letter sections (before bare numbers)
    add("Chapter Seven §6E", "Chapter Seven §10")
    add("Chapter Seven §6D", "Chapter Seven §9")
    add("Chapter Seven §6C", "Chapter Seven §8")
    add("Chapter Seven §6B", "Chapter Seven §7")
    add("Chapter Seven §6A", "Chapter Seven §6")
    add("[§6E]", "[§10]")
    add("[§6D]", "[§9]")
    add("[§6C]", "[§8]")
    add("[§6B]", "[§7]")
    add("[§6A]", "[§6]")
    add("**§6E**", "**§10**")
    add("**§6D**", "**§9**")
    add("**§6C**", "**§8**")
    add("**§6B**", "**§7**")
    add("**§6A**", "**§6**")
    add("under **§6E**", "under **§10**")
    add("under **§6D**", "under **§9**")
    add("under **§6C**", "under **§8**")
    add("under **§6B**", "under **§7**")
    add("under **§6A**", "under **§6**")

    # Subsections — whole-system 2.x -> 3.x
    for i in range(7, 0, -1):
        add(f"Chapter Seven §2.{i}", f"Chapter Seven §3.{i}")
        add(f"**§2.{i}**", f"**§3.{i}**")
        add(f"[§2.{i}]", f"[§3.{i}]")

    # Record 3.x -> 11.x (after 2.x to avoid collision)
    for i in range(3, 0, -1):
        add(f"Chapter Seven §3.{i}", f"Chapter Seven §11.{i}")
        add(f"**§3.{i}**", f"**§11.{i}**")
        add(f"[§3.{i}]", f"[§11.{i}]")

    # Supervisory 8.x -> 14.x
    for i in range(3, 0, -1):
        add(f"Chapter Seven §8.{i}", f"Chapter Seven §14.{i}")
        add(f"**§8.{i}**", f"**§14.{i}**")
        add(f"[§8.{i}]", f"[§14.{i}]")

    # Top-level sections high -> low (16 down) with placeholders to avoid double remap
    section_map = [
        ("11", "⟦16⟧"),
        ("10", "⟦15⟧"),
        ("9", "⟦13⟧"),
        ("8", "⟦14⟧"),
        ("7", "⟦12⟧"),
        ("6", "⟦5⟧"),  # ecological only; 6A-E handled above
        ("5", "⟦4⟧"),
        ("4", "⟦2⟧"),
        ("3", "⟦11⟧"),
        ("2", "⟦3⟧"),
    ]
    for old, ph in section_map:
        add(f"Chapter Seven §{old} ", f"Chapter Seven {ph} ")
        add(f"Chapter Seven §{old}.", f"Chapter Seven {ph}.")
        add(f"Chapter Seven §{old},", f"Chapter Seven {ph},")
        add(f"Chapter Seven §{old})", f"Chapter Seven {ph})")
        add(f"Chapter Seven §{old}—", f"Chapter Seven {ph}—")
        add(f"Chapter Seven §{old}\n", f"Chapter Seven {ph}\n")
        add(f"Chapter Seven §{old}", f"Chapter Seven {ph}")
        add(f"[§{old}]", f"[{ph}]")
        add(f"**§{old}**", f"**{ph}**")
        add(f"under **§{old}**", f"under **{ph}**")
        add(f"through [§{old}]", f"through [{ph}]")

    # Named section titles in Chapter Seven §N Title form
    title_map = [
        ("Chapter Seven §2 Whole-System Certification Evaluation", "Chapter Seven §3 Whole-System Certification Evaluation"),
        ("Chapter Seven §4 System Class Evaluation", "Chapter Seven §2 System Class Evaluation"),
        ("Chapter Seven §3 Certification Record", "Chapter Seven §11 System Certification Record"),
        ("Chapter Seven §5 Data Types and Handling Evaluation", "Chapter Seven §4 Data Types and Handling Evaluation"),
        ("Chapter Seven §6 Ecological Footprint Evaluation", "Chapter Seven §5 Ecological Footprint Evaluation"),
        (
            "Chapter Seven §6A Proportionate Cross-System Support Evaluation",
            "Chapter Seven §6 Proportionate Cross-System Support Evaluation",
        ),
        ("Chapter Seven §6B Nondiscrimination Evaluation", "Chapter Seven §7 Nondiscrimination Evaluation"),
        ("Chapter Seven §6C Accessibility Evaluation", "Chapter Seven §8 Accessibility Evaluation"),
        (
            "Chapter Seven §6D Educational Capability and Learning-System Integrity Evaluation",
            "Chapter Seven §9 Educational Capability and Learning-System Integrity Evaluation",
        ),
        (
            "Chapter Seven §6E Trustworthiness and System-Reliance Integrity Evaluation",
            "Chapter Seven §10 Trustworthiness and System-Reliance Integrity Evaluation",
        ),
        (
            "Chapter Seven §7 Transparency, Auditability, and Contestability",
            "Chapter Seven §12 Transparency, Auditability, and Contestability",
        ),
        (
            "Chapter Seven §9 Forum Supervision and Component Roles",
            "Chapter Seven §13 Forum Supervision and Component Roles",
        ),
        (
            "Chapter Seven §8 Supervisory Sequence and Contestability Chain",
            "Chapter Seven §14 Supervisory Sequence and Contestability Chain",
        ),
        ("Chapter Seven §10 Relationship to Standing", "Chapter Seven §15 Relationship to Standing"),
        ("Chapter Seven §11 Reopening", "Chapter Seven §16 Reopening"),
    ]
    for old, new in title_map:
        add(old, new)

    placeholder_final = {
        "⟦16⟧": "§16",
        "⟦15⟧": "§15",
        "⟦14⟧": "§14",
        "⟦13⟧": "§13",
        "⟦12⟧": "§12",
        "⟦11⟧": "§11",
        "⟦5⟧": "§5",
        "⟦4⟧": "§4",
        "⟦3⟧": "§3",
        "⟦2⟧": "§2",
    }
    for ph, final in placeholder_final.items():
        add(ph, final)

    # Sort longest first
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs


def build_link_ref_table() -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for old, new in ANCHOR_PRIMARY.items():
        pairs.append(
            (
                f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation#{old}",
                f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation#{new}",
            )
        )
    # Legacy §5B style links still pointing at old slugs
    legacy = [
        ("#6a-proportionate-cross-system-support-evaluation", "#6-proportionate-cross-system-support-evaluation"),
        ("#6b-nondiscrimination-evaluation", "#7-nondiscrimination-evaluation"),
        ("#6c-accessibility-evaluation", "#8-accessibility-evaluation"),
        ("#6d-educational-capability-and-learning-system-integrity-evaluation", "#9-educational-capability-and-learning-system-integrity-evaluation"),
        ("#6e-trustworthiness-and-system-reliance-integrity-evaluation", "#10-trustworthiness-and-system-reliance-integrity-evaluation"),
        ("#2-whole-system-certification-evaluation", "#3-whole-system-certification-evaluation"),
        ("#3-certification-record", "#11-certification-record"),
        ("#4-system-class-evaluation", "#2-system-class-evaluation"),
        ("#5-data-types-and-handling-evaluation", "#4-data-types-and-handling-evaluation"),
        ("#6-ecological-footprint-evaluation", "#5-ecological-footprint-evaluation"),
        ("#7-transparency-auditability-and-contestability", "#12-transparency-auditability-and-contestability"),
        ("#8-supervisory-sequence-and-contestability-chain", "#14-supervisory-sequence-and-contestability-chain"),
        ("#9-forum-supervision-and-component-roles", "#13-forum-supervision-and-component-roles"),
        ("#10-relationship-to-standing", "#15-relationship-to-standing"),
        ("#11-reopening-drift-and-non-evasion", "#16-reopening-drift-and-non-evasion"),
        ("#21-systemic-scope-and-risk-factors", "#31-systemic-scope-and-risk-factors"),
        ("#22-accessibility-under-sentience-non-exclusion", "#32-accessibility-under-sentience-non-exclusion"),
        ("#23-privacy-informational-joint-invocation", "#33-privacy-informational-joint-invocation"),
        ("#24-voluntary-discontinuation-and-exit-rights", "#34-voluntary-discontinuation-and-exit-rights"),
        ("#25-assembly-collective-organization-and-institutional-formation", "#35-assembly-collective-organization-and-institutional-formation"),
        ("#26-time-consistency-constraint", "#36-time-consistency-constraint"),
        ("#27-governance-incentive-and-contestability-discipline", "#37-governance-incentive-and-contestability-discipline"),
        ("#31-minimum-record-contents", "#111-minimum-record-contents"),
        ("#32-cross-section-record-requirements", "#112-cross-section-record-requirements"),
        ("#33-rights-floor-record-evaluation-non-substitution", "#113-rights-floor-record-evaluation-non-substitution"),
        ("#81-supervisory-sequence", "#141-supervisory-sequence"),
        ("#82-contestability-chain", "#142-contestability-chain"),
        ("#83-anti-bypass", "#143-anti-bypass"),
    ]
    for old, new in legacy:
        pairs.append(
            (
                f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation{old}",
                f"core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation{new}",
            )
        )
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs


INTERNAL_LINK_REMAP = [
    # Built dynamically after we know anchors — see remap_ch7_internal_links
]


def remap_ch7_internal_links(text: str) -> str:
    """Remap [§N](#anchor) inside ch7."""
    protect = {
        "[§1.1]": "⟦P11⟧",
        "[§1](#1-purpose-and-role)": "⟦P1⟧",
        "**§1.1**": "⟦B11⟧",
        "#### 1.1 ": "⟦H11⟧",
        "**§10** states the standing bridge": "⟦STAND⟧",
    }
    for k, v in protect.items():
        text = text.replace(k, v)

    link_pairs: list[tuple[str, str]] = []
    for old_slug, new_slug in ANCHOR_PRIMARY.items():
        old_num_guess = old_slug.split("-")[0]
        new_num_guess = new_slug.split("-")[0]
        # Build § ref from slug prefix heuristics
        ref_map = {
            "2-whole-system": ("§2", "§3"),
            "3-certification": ("§3", "§11"),
            "4-system-class": ("§4", "§2"),
            "5-data-types": ("§5", "§4"),
            "6-ecological": ("§6", "§5"),
            "6a-proportionate": ("§6A", "§6"),
            "6b-nondiscrimination": ("§6B", "§7"),
            "6c-accessibility": ("§6C", "§8"),
            "6d-educational": ("§6D", "§9"),
            "6e-trustworthiness": ("§6E", "§10"),
            "7-transparency": ("§7", "§12"),
            "8-supervisory": ("§8", "§14"),
            "9-forum": ("§9", "§13"),
            "10-relationship": ("§10", "§15"),
            "11-reopening": ("§11", "§16"),
        }
        for prefix, (old_ref, new_ref) in ref_map.items():
            if old_slug.startswith(prefix.replace("-", "-")) or old_slug == prefix + "-evaluation":
                pass
        link_pairs.append((f"](#{old_slug})", f"TEMP_{old_slug}_]"))

    # Explicit internal link table
    explicit = [
        ("[§2](#2-whole-system-certification-evaluation)", "[§3](#3-whole-system-certification-evaluation)"),
        ("[§2.1](#21-systemic-scope-and-risk-factors)", "[§3.1](#31-systemic-scope-and-risk-factors)"),
        ("[§2.2](#22-accessibility-under-sentience-non-exclusion)", "[§3.2](#32-accessibility-under-sentience-non-exclusion)"),
        ("[§2.3](#23-privacy-informational-joint-invocation)", "[§3.3](#33-privacy-informational-joint-invocation)"),
        ("[§2.4](#24-voluntary-discontinuation-and-exit-rights)", "[§3.4](#34-voluntary-discontinuation-and-exit-rights)"),
        ("[§2.5](#25-assembly-collective-organization-and-institutional-formation)", "[§3.5](#35-assembly-collective-organization-and-institutional-formation)"),
        ("[§2.6](#26-time-consistency-constraint)", "[§3.6](#36-time-consistency-constraint)"),
        ("[§2.7](#27-governance-incentive-and-contestability-discipline)", "[§3.7](#37-governance-incentive-and-contestability-discipline)"),
        ("[§3](#3-certification-record)", "[§11](#11-certification-record)"),
        ("[§3.1](#31-minimum-record-contents)", "[§11.1](#111-minimum-record-contents)"),
        ("[§3.2](#32-cross-section-record-requirements)", "[§11.2](#112-cross-section-record-requirements)"),
        ("[§3.3](#33-rights-floor-record-evaluation-non-substitution)", "[§11.3](#113-rights-floor-record-evaluation-non-substitution)"),
        ("[§4](#4-system-class-evaluation)", "[§2](#2-system-class-evaluation)"),
        ("[§5](#5-data-types-and-handling-evaluation)", "[§4](#4-data-types-and-handling-evaluation)"),
        ("[§6](#6-ecological-footprint-evaluation)", "[§5](#5-ecological-footprint-evaluation)"),
        ("[§6A](#6a-proportionate-cross-system-support-evaluation)", "[§6](#6-proportionate-cross-system-support-evaluation)"),
        ("[§6B](#6b-nondiscrimination-evaluation)", "[§7](#7-nondiscrimination-evaluation)"),
        ("[§6C](#6c-accessibility-evaluation)", "[§8](#8-accessibility-evaluation)"),
        ("[§6D](#6d-educational-capability-and-learning-system-integrity-evaluation)", "[§9](#9-educational-capability-and-learning-system-integrity-evaluation)"),
        ("[§6E](#6e-trustworthiness-and-system-reliance-integrity-evaluation)", "[§10](#10-trustworthiness-and-system-reliance-integrity-evaluation)"),
        ("[§7](#7-transparency-auditability-and-contestability)", "[§12](#12-transparency-auditability-and-contestability)"),
        ("[§8](#8-supervisory-sequence-and-contestability-chain)", "[§14](#14-supervisory-sequence-and-contestability-chain)"),
        ("[§8.1](#81-supervisory-sequence)", "[§14.1](#141-supervisory-sequence)"),
        ("[§8.2](#82-contestability-chain)", "[§14.2](#142-contestability-chain)"),
        ("[§8.3](#83-anti-bypass)", "[§14.3](#143-anti-bypass)"),
        ("[§9](#9-forum-supervision-and-component-roles)", "[§13](#13-forum-supervision-and-component-roles)"),
        ("[§10](#10-relationship-to-standing)", "[§15](#15-relationship-to-standing)"),
        ("[§11](#11-reopening-drift-and-non-evasion)", "[§16](#16-reopening-drift-and-non-evasion)"),
        ("through [§4](#4-system-class-evaluation) through [§6E](#6e-trustworthiness-and-system-reliance-integrity-evaluation)", "through [§2](#2-system-class-evaluation) through [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation)"),
        ("[§3](#3-certification-record) through [§9](#9-forum-supervision-and-component-roles)", "[§11](#11-certification-record) through [§13](#13-forum-supervision-and-component-roles)"),
        ("**§10** states the standing bridge boundary explicitly.", "**§15** states the standing bridge boundary explicitly."),
        ("[§11](#11-reopening-drift-and-non-evasion) (*reopening and anti-evasion*)", "[§16](#16-reopening-drift-and-non-evasion) (*reopening and anti-evasion*)"),
        ("[§4](#4-system-class-evaluation) (*system class evaluation*)", "[§2](#2-system-class-evaluation) (*system class evaluation*)"),
        ("[§2](#2-whole-system-certification-evaluation) (*whole-system certification evaluation factors*)", "[§3](#3-whole-system-certification-evaluation) (*whole-system certification evaluation factors*)"),
        ("[§3](#3-certification-record) (*certification record contents*)", "[§11](#11-certification-record) (*certification record contents*)"),
        ("[§4](#4-system-class-evaluation) (*system class evaluation*)", "[§2](#2-system-class-evaluation) (*system class evaluation*)"),
        ("Revalidation cadence** — how often records must be renewed ([§4](#4-system-class-evaluation))", "Revalidation cadence** — how often records must be renewed ([§2](#2-system-class-evaluation))"),
        ("[§7](#7-transparency-auditability-and-contestability), [§8](#8-supervisory-sequence-and-contestability-chain)", "[§12](#12-transparency-auditability-and-contestability), [§14](#14-supervisory-sequence-and-contestability-chain)"),
        ("[§11](#11-reopening-drift-and-non-evasion)", "[§16](#16-reopening-drift-and-non-evasion)"),
    ]
    explicit.sort(key=lambda x: len(x[0]), reverse=True)
    for old, new in explicit:
        text = text.replace(old, new)

    for k, v in protect.items():
        if k == "**§10** states the standing bridge":
            text = text.replace("⟦STAND⟧", "**§15** states the standing bridge")
        else:
            text = text.replace(v, k)
    return text


def update_primary_anchors(text: str) -> str:
    for old, new in ANCHOR_PRIMARY.items():
        if old == new:
            continue
        text = text.replace(f'<a id="{old}"></a>', f'<a id="{new}"></a>', 1)
    return add_legacy_anchor_pairs(text)


def apply_pairs(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        text = text.replace(old, new)
    return text


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(rel.startswith(p) for p in SKIP_GLOBS):
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        if path == Path(__file__):
            continue
        files.append(path)
    return sorted(set(files))


def rebuild_ch7() -> str:
    raw = CH7.read_text(encoding="utf-8")
    preamble, sections = split_sections(raw)
    parts = [preamble.rstrip(), ""]
    for key in NEW_ORDER:
        body = renumber_section_body(key, sections[key])
        parts.append(body.rstrip())
        parts.append("")
    text = "\n".join(parts).rstrip() + "\n"
    text = update_primary_anchors(text)
    text = remap_ch7_internal_links(text)
    # Corpus placement anti-relocation pointer
    text = text.replace(
        "**§10** states the standing bridge boundary explicitly.",
        "**§15** states the standing bridge boundary explicitly.",
    )
    return text


def main() -> None:
    section_pairs = build_section_ref_table()
    link_pairs = build_link_ref_table()
    changed: list[str] = []

    new_ch7 = rebuild_ch7()
    old_ch7 = CH7.read_text(encoding="utf-8")
    if new_ch7 != old_ch7:
        CH7.write_text(new_ch7, encoding="utf-8")
        changed.append(CH7.name)

    for path in iter_files():
        if path == CH7:
            continue
        old = path.read_text(encoding="utf-8")
        new = apply_pairs(old, link_pairs)
        new = apply_pairs(new, section_pairs)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    print(f"Updated {len(changed)} files")
    for name in changed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
