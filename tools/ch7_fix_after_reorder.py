#!/usr/bin/env python3
"""Fix Chapter Seven anchors after § reorder and update corpus cross-references."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH7 = ROOT / "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation"

HEADING_ANCHORS: list[tuple[str, list[str]]] = [
    (
        r"### 2\. System Class Evaluation",
        ["2-system-class-evaluation", "4-system-class-evaluation", "3-system-class-evaluation"],
    ),
    (
        r"### 3\. Whole-System Certification Evaluation",
        [
            "3-whole-system-certification-evaluation",
            "2-whole-system-certification-evaluation",
            "1a-whole-system-certification-evaluation",
        ],
    ),
    (
        r"### 4\. Data Types and Handling Evaluation",
        ["4-data-types-and-handling-evaluation", "5-data-types-and-handling-evaluation"],
    ),
    (
        r"### 5\. Ecological Footprint Evaluation",
        ["5-ecological-footprint-evaluation", "6-ecological-footprint-evaluation"],
    ),
    (
        r"### 6\. Proportionate Cross-System Support Evaluation",
        [
            "6-proportionate-cross-system-support-evaluation",
            "6a-proportionate-cross-system-support-evaluation",
            "5a-proportionate-cross-system-support-evaluation",
        ],
    ),
    (
        r"### 7\. Nondiscrimination Evaluation",
        ["7-nondiscrimination-evaluation", "6b-nondiscrimination-evaluation", "5b-nondiscrimination-evaluation"],
    ),
    (
        r"### 8\. Accessibility Evaluation",
        ["8-accessibility-evaluation", "6c-accessibility-evaluation", "5c-accessibility-evaluation"],
    ),
    (
        r"### 9\. Educational Capability and Learning-System Integrity Evaluation",
        [
            "9-educational-capability-and-learning-system-integrity-evaluation",
            "6d-educational-capability-and-learning-system-integrity-evaluation",
            "5d-educational-capability-and-learning-system-integrity-evaluation",
        ],
    ),
    (
        r"### 10\. Trustworthiness and System-Reliance Integrity Evaluation",
        [
            "10-trustworthiness-and-system-reliance-integrity-evaluation",
            "6e-trustworthiness-and-system-reliance-integrity-evaluation",
            "5e-trustworthiness-and-system-reliance-integrity-evaluation",
        ],
    ),
    (
        r"### 11\. Certification Record",
        ["11-certification-record", "3-certification-record", "2-certification-record"],
    ),
    (
        r"### 12\. Transparency, Auditability, and Contestability",
        [
            "12-transparency-auditability-and-contestability",
            "7-transparency-auditability-and-contestability",
            "6-transparency-auditability-and-contestability",
        ],
    ),
    (
        r"### 13\. Forum Supervision and Component Roles",
        [
            "13-forum-supervision-and-component-roles",
            "9-forum-supervision-and-component-roles",
            "8-forum-supervision-and-component-roles",
        ],
    ),
    (
        r"### 14\. Supervisory Sequence and Contestability Chain",
        [
            "14-supervisory-sequence-and-contestability-chain",
            "8-supervisory-sequence-and-contestability-chain",
            "7-supervisory-sequence-and-contestability-chain",
        ],
    ),
    (
        r"### 15\. Relationship to Standing",
        ["15-relationship-to-standing", "10-relationship-to-standing", "9-relationship-to-standing"],
    ),
    (
        r"### 16\. Reopening, Misalignment, and Non-Evasion",
        ["16-reopening-drift-and-non-evasion", "11-reopening-drift-and-non-evasion", "10-reopening-drift-and-non-evasion"],
    ),
]

ANCHOR_LINE = re.compile(r'^<a id="[^"]+"></a>\s*$', re.MULTILINE)

# Longest-first explicit replacements for corpus-wide refs (old committed -> new).
CORPUS_REPLACEMENTS: list[tuple[str, str]] = [
    # Fix double-remap errors from partial migration
    ("Chapter Seven §11 Whole-System Certification Evaluation", "Chapter Seven §3 Whole-System Certification Evaluation"),
    ("Chapter Seven §3 System Class Evaluation", "Chapter Seven §2 System Class Evaluation"),
    ("Chapter Seven §16 Certification Record", "Chapter Seven §11 Certification Record"),
    ("Chapter Seven §16.2", "Chapter Seven §3.2"),
    ("Chapter Seven §16.1", "Chapter Seven §3.1"),
    # Letter sections
    ("Chapter Seven §6E", "Chapter Seven §10"),
    ("Chapter Seven §6D", "Chapter Seven §9"),
    ("Chapter Seven §6C", "Chapter Seven §8"),
    ("Chapter Seven §6B", "Chapter Seven §7"),
    ("Chapter Seven §6A", "Chapter Seven §6"),
    ("[§6E]", "[§10]"),
    ("[§6D]", "[§9]"),
    ("[§6C]", "[§8]"),
    ("[§6B]", "[§7]"),
    ("[§6A]", "[§6]"),
    ("**§6E**", "**§10**"),
    ("**§6D**", "**§9**"),
    ("**§6C**", "**§8**"),
    ("**§6B**", "**§7**"),
    ("**§6A**", "**§6**"),
    ("under **§6E**", "under **§10**"),
    ("under **§6D**", "under **§9**"),
    ("under **§6C**", "under **§8**"),
    ("under **§6B**", "under **§7**"),
    ("under **§6A**", "under **§6**"),
    ("[§5E]", "[§10]"),
    ("[§5D]", "[§9]"),
    ("[§5C]", "[§8]"),
    ("[§5B]", "[§7]"),
    ("[§5A]", "[§6]"),
    # Named titles (old numbering)
    ("Chapter Seven §11 Reopening", "Chapter Seven §16 Reopening"),
    ("Chapter Seven §10 Relationship to Standing", "Chapter Seven §15 Relationship to Standing"),
    ("Chapter Seven §9 Forum Supervision", "Chapter Seven §13 Forum Supervision"),
    ("Chapter Seven §8 Supervisory Sequence", "Chapter Seven §14 Supervisory Sequence"),
    ("Chapter Seven §7 Transparency", "Chapter Seven §12 Transparency"),
    ("Chapter Seven §3 Certification Record", "Chapter Seven §11 Certification Record"),
    ("Chapter Seven §2 Whole-System Certification Evaluation", "Chapter Seven §3 Whole-System Certification Evaluation"),
    ("Chapter Seven §4 System Class Evaluation", "Chapter Seven §2 System Class Evaluation"),
    ("Chapter Seven §5 Data Types", "Chapter Seven §4 Data Types"),
    ("Chapter Seven §6 Ecological Footprint", "Chapter Seven §5 Ecological Footprint"),
    ("Chapter Seven §6A Proportionate Cross-System", "Chapter Seven §6 Proportionate Cross-System"),
    ("Chapter Seven §6B Nondiscrimination", "Chapter Seven §7 Nondiscrimination"),
    ("Chapter Seven §6C Accessibility", "Chapter Seven §8 Accessibility"),
    ("Chapter Seven §6D Educational", "Chapter Seven §9 Educational"),
    ("Chapter Seven §6E Trustworthiness", "Chapter Seven §10 Trustworthiness"),
    # Subsections whole-system 2.x -> 3.x
    ("Chapter Seven §2.7", "Chapter Seven §3.7"),
    ("Chapter Seven §2.6", "Chapter Seven §3.6"),
    ("Chapter Seven §2.5", "Chapter Seven §3.5"),
    ("Chapter Seven §2.4", "Chapter Seven §3.4"),
    ("Chapter Seven §2.3", "Chapter Seven §3.3"),
    ("Chapter Seven §2.2", "Chapter Seven §3.2"),
    ("Chapter Seven §2.1", "Chapter Seven §3.1"),
    # Record 3.x -> 11.x
    ("Chapter Seven §3.3", "Chapter Seven §11.3"),
    ("Chapter Seven §3.2", "Chapter Seven §11.2"),
    ("Chapter Seven §3.1", "Chapter Seven §11.1"),
    # Supervisory 8.x -> 14.x
    ("Chapter Seven §8.3", "Chapter Seven §14.3"),
    ("Chapter Seven §8.2", "Chapter Seven §14.2"),
    ("Chapter Seven §8.1", "Chapter Seven §14.1"),
    # Anchors in links
    ("#6e-trustworthiness-and-system-reliance-integrity-evaluation", "#10-trustworthiness-and-system-reliance-integrity-evaluation"),
    ("#6d-educational-capability-and-learning-system-integrity-evaluation", "#9-educational-capability-and-learning-system-integrity-evaluation"),
    ("#6c-accessibility-evaluation", "#8-accessibility-evaluation"),
    ("#6b-nondiscrimination-evaluation", "#7-nondiscrimination-evaluation"),
    ("#6a-proportionate-cross-system-support-evaluation", "#6-proportionate-cross-system-support-evaluation"),
    ("#5e-trustworthiness-and-system-reliance-integrity-evaluation", "#10-trustworthiness-and-system-reliance-integrity-evaluation"),
    ("#5d-educational-capability-and-learning-system-integrity-evaluation", "#9-educational-capability-and-learning-system-integrity-evaluation"),
    ("#5c-accessibility-evaluation", "#8-accessibility-evaluation"),
    ("#5b-nondiscrimination-evaluation", "#7-nondiscrimination-evaluation"),
    ("#5a-proportionate-cross-system-support-evaluation", "#6-proportionate-cross-system-support-evaluation"),
    ("#11-reopening-drift-and-non-evasion", "#16-reopening-drift-and-non-evasion"),
    ("#10-reopening-drift-and-non-evasion", "#16-reopening-drift-and-non-evasion"),
    ("#10-relationship-to-standing", "#15-relationship-to-standing"),
    ("#9-relationship-to-standing", "#15-relationship-to-standing"),
    ("#9-forum-supervision-and-component-roles", "#13-forum-supervision-and-component-roles"),
    ("#8-forum-supervision-and-component-roles", "#13-forum-supervision-and-component-roles"),
    ("#8-supervisory-sequence-and-contestability-chain", "#14-supervisory-sequence-and-contestability-chain"),
    ("#7-supervisory-sequence-and-contestability-chain", "#14-supervisory-sequence-and-contestability-chain"),
    ("#7-transparency-auditability-and-contestability", "#12-transparency-auditability-and-contestability"),
    ("#6-transparency-auditability-and-contestability", "#12-transparency-auditability-and-contestability"),
    ("#3-certification-record", "#11-certification-record"),
    ("#2-certification-record", "#11-certification-record"),
    ("#2-whole-system-certification-evaluation", "#3-whole-system-certification-evaluation"),
    ("#1a-whole-system-certification-evaluation", "#3-whole-system-certification-evaluation"),
    ("#4-system-class-evaluation", "#2-system-class-evaluation"),
    ("#3-system-class-evaluation", "#2-system-class-evaluation"),
    ("#5-data-types-and-handling-evaluation", "#4-data-types-and-handling-evaluation"),
    ("#6-ecological-footprint-evaluation", "#5-ecological-footprint-evaluation"),
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
    # Bare section numbers via placeholders (old HEAD -> new)
    ("Chapter Seven §11", "Chapter Seven ⟦S16⟧"),
    ("Chapter Seven §10", "Chapter Seven ⟦S15⟧"),
    ("Chapter Seven §9", "Chapter Seven ⟦S13⟧"),
    ("Chapter Seven §8", "Chapter Seven ⟦S14⟧"),
    ("Chapter Seven §7", "Chapter Seven ⟦S12⟧"),
    ("Chapter Seven §6", "Chapter Seven ⟦S5⟧"),
    ("Chapter Seven §5", "Chapter Seven ⟦S4⟧"),
    ("Chapter Seven §4", "Chapter Seven ⟦S2⟧"),
    ("Chapter Seven §3", "Chapter Seven ⟦S11⟧"),
    ("Chapter Seven §2", "Chapter Seven ⟦S3⟧"),
    ("⟦S16⟧", "Chapter Seven §16"),
    ("⟦S15⟧", "Chapter Seven §15"),
    ("⟦S13⟧", "Chapter Seven §13"),
    ("⟦S14⟧", "Chapter Seven §14"),
    ("⟦S12⟧", "Chapter Seven §12"),
    ("⟦S5⟧", "Chapter Seven §5"),
    ("⟦S4⟧", "Chapter Seven §4"),
    ("⟦S2⟧", "Chapter Seven §2"),
    ("⟦S11⟧", "Chapter Seven §11"),
    ("⟦S3⟧", "Chapter Seven §3"),
]

CORPUS_REPLACEMENTS.sort(key=lambda x: len(x[0]), reverse=True)


def strip_orphan_anchors_before_heading(text: str, heading_pattern: str) -> str:
    """Remove <a id> lines immediately preceding a ### heading."""
    pat = re.compile(
        rf"((?:<a id=\"[^\"]+\"></a>\s*\n)+)({heading_pattern}\s*\n)",
        re.MULTILINE,
    )

    def repl(m: re.Match[str]) -> str:
        return m.group(2)

    return pat.sub(repl, text)


def insert_anchors_before_heading(text: str, heading_pattern: str, anchor_ids: list[str]) -> str:
    block = "".join(f'<a id="{aid}"></a>\n' for aid in anchor_ids)
    pat = re.compile(rf"(?<!\n)({heading_pattern}\s*\n)", re.MULTILINE)
    return pat.sub(rf"{block}\1", text, count=1)


def fix_ch7_anchors(text: str) -> str:
    for heading_pat, anchors in HEADING_ANCHORS:
        text = strip_orphan_anchors_before_heading(text, heading_pat)
        text = insert_anchors_before_heading(text, heading_pat, anchors)

    # §2 System Class: record is downstream, not upstream
    text = text.replace(
        "- Upstream: [§11](#11-certification-record) (*record contents*); Threshold and Scaling",
        "- Upstream: [§1](#1-purpose-and-role) (*purpose and role*); Threshold and Scaling",
        1,
    )
    # §13 Forum: roles before sequence
    text = text.replace(
        "- Upstream: [§11](#11-certification-record) (*certification record contents*); [§14](#14-supervisory-sequence-and-contestability-chain) (*supervisory sequence and contestability chain*);",
        "- Upstream: [§11](#11-certification-record) (*certification record contents*); [§12](#12-transparency-auditability-and-contestability) (*record integrity requirements*);",
        1,
    )
    text = text.replace(
        "- Downstream: [§15](#15-relationship-to-standing) (*standing-record bridge*).",
        "- Downstream: [§14](#14-supervisory-sequence-and-contestability-chain) (*supervisory sequence and contestability chain*); [§15](#15-relationship-to-standing) (*standing-record bridge*).",
        1,
    )
    text = text.replace(
        "It implements the supervisory sequence and contestability chain in [§14](#14-supervisory-sequence-and-contestability-chain).",
        "It assigns component roles used by the supervisory sequence in [§14](#14-supervisory-sequence-and-contestability-chain).",
        1,
    )
    return text


def apply_replacements(text: str) -> str:
    for old, new in CORPUS_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def iter_md_json() -> list[Path]:
    out: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("archive/") or rel.startswith("evidence/"):
            continue
        if path.name == "ch7_fix_after_reorder.py":
            continue
        out.append(path)
    return sorted(out)


def main() -> None:
    changed: list[str] = []

    ch7 = CH7.read_text(encoding="utf-8")
    fixed = fix_ch7_anchors(ch7)
    fixed = apply_replacements(fixed)
    if fixed != ch7:
        CH7.write_text(fixed, encoding="utf-8")
        changed.append(CH7.name)

    for path in iter_md_json():
        if path == CH7:
            continue
        old = path.read_text(encoding="utf-8")
        new = apply_replacements(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    print(f"Updated {len(changed)} files")
    for name in changed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
