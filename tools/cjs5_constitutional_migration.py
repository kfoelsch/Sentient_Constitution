#!/usr/bin/env python3
"""Migrate CJS-5 clusters to constitutional Triad / Aims organization.

Renumbers CJS-5.2–CJS-5.23, regroups family files, writes CJS-5.1 compass content,
and updates corpus-wide references. Run from repository root:

  python3 tools/cjs5_constitutional_migration.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CJS_DIR = ROOT / "corpus_joint_structure"

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules", "ai_corpus"}
EXTENSIONS = {".md", ".py", ".json", ".csv", ".mmd"}

# old cluster ID -> new cluster ID (5.16–5.19 unchanged)
CLUSTER_RENUMBER: dict[str, str] = {
    "CJS-5.2": "CJS-5.11",
    "CJS-5.3": "CJS-5.14",
    "CJS-5.4": "CJS-5.2",
    "CJS-5.5": "CJS-5.12",
    "CJS-5.6": "CJS-5.22",
    "CJS-5.7": "CJS-5.13",
    "CJS-5.8": "CJS-5.6",
    "CJS-5.9": "CJS-5.3",
    "CJS-5.10": "CJS-5.4",
    "CJS-5.11": "CJS-5.5",
    "CJS-5.12": "CJS-5.7",
    "CJS-5.13": "CJS-5.8",
    "CJS-5.14": "CJS-5.9",
    "CJS-5.15": "CJS-5.10",
    "CJS-5.20": "CJS-5.23",
    "CJS-5.21": "CJS-5.20",
    "CJS-5.22": "CJS-5.21",
    "CJS-5.23": "CJS-5.15",
}

OLD_PRINCIPLE_MAP: dict[str, list[str]] = {
    "CJS-5.2": ["2.1", "4", "5.2", "7.2", "10"],
    "CJS-5.3": ["3.1", "6.1", "6.4", "7.1", "9"],
    "CJS-5.4": ["3.2", "4", "5.2", "7.1", "7.2"],
    "CJS-5.5": ["6.1", "6.3", "6.4", "7.1", "8", "9"],
    "CJS-5.6": ["3.2", "6.2", "6.4", "7.1", "8", "9"],
    "CJS-5.7": ["2.1", "3.4", "6.4", "7.1", "8", "10"],
    "CJS-5.8": ["3.1", "3.2", "4.1", "7.1", "7.2"],
    "CJS-5.9": ["3.2", "4", "7.1", "7.2"],
    "CJS-5.10": ["3.2", "6.2", "6.4", "7.1", "8"],
    "CJS-5.11": ["3.2", "3.3", "4", "7.1", "7.2"],
    "CJS-5.12": ["2.1", "4", "5.2", "6.4", "8", "10"],
    "CJS-5.13": ["3.4", "5.2", "7.1", "8"],
    "CJS-5.14": ["2", "3.2", "4", "7.1", "8"],
    "CJS-5.15": ["3.2", "6.2", "7.1", "8"],
    "CJS-5.16": ["3.1", "4.1", "5.1", "7.1", "9"],
    "CJS-5.17": ["5.1", "6.1", "7.1", "8", "9"],
    "CJS-5.18": ["3.2", "6.2", "7.1", "8", "9"],
    "CJS-5.19": ["3.1", "4.1", "5.1", "6.1", "7", "9"],
    "CJS-5.20": ["3.1", "6.1", "6.4", "7.1", "9"],
    "CJS-5.21": ["3.1", "4.1", "6.1", "7.1", "9"],
    "CJS-5.22": ["3.1", "3.2", "4.1", "7.1", "7.2", "9"],
    "CJS-5.23": ["3.1", "3.2", "4.1", "5.2", "7.1", "7.2"],
}

# new ID metadata after migration
CLUSTER_META: dict[str, dict[str, str]] = {
    "CJS-5.2": {
        "title": "reflexive transparency and accountability terms",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.3": {
        "title": "auditability and reconstructability terms",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.4": {
        "title": "tiered transparency and audit-access terms",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.5": {
        "title": "independent verification and claim-integrity terms",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.6": {
        "title": "integrity assurance and resilience operations",
        "leg": "Oversight",
        "aim": "Continuity",
        "cross": "integrative with **Accountability** where contest, correction, and assurance routing are implicated",
        "continuity_note": "Distinguish constitutional **Continuity** aim from operational resilience or protocol continuity.",
    },
    "CJS-5.7": {
        "title": "quorum and participatory legitimacy terms",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.8": {
        "title": "comprehensibility and cognitive accessibility terms",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.9": {
        "title": "salience integrity and attention-allocation terms",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.10": {
        "title": "disclosure sufficiency and observability terms",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.11": {
        "title": "distributed and proportional authority terms",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.12": {
        "title": "burden-of-justification and constraint terms",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.13": {
        "title": "procedural integrity and adjudication terms",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
    },
    "CJS-5.14": {
        "title": "intervention governance and override-authorization terms",
        "leg": "Accountability",
        "aim": "Continuity",
        "cross": "pairs with **CJS-5.23** for governance authorization versus technical intervention integrity",
        "continuity_note": "Distinguish constitutional **Continuity** aim from emergency or operational continuity modes.",
    },
    "CJS-5.15": {
        "title": "structural review, correction urgency, and disclosure terms",
        "leg": "Accountability",
        "aim": "Continuity",
        "cross": "pairs with **CJS-5.6** for evolution, revalidation, and non-entrenchment",
        "continuity_note": "Distinguish constitutional **Continuity** aim from operational continuity reporting.",
    },
    "CJS-5.16": {
        "title": "dependency integrity and disclosure terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Constitutional **Continuity** aim — not protocol or forum continuity alone.",
    },
    "CJS-5.17": {
        "title": "interoperability, portability, and exit-integrity terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Constitutional **Continuity** aim — exit paths preserve lawful agency and system survivability.",
    },
    "CJS-5.18": {
        "title": "data-retention and lifecycle-integrity terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Constitutional **Continuity** aim — lifecycle rules must not narrow the Continuity aim.",
    },
    "CJS-5.19": {
        "title": "graceful degradation and failure-mode integrity terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Operational degradation discipline serves constitutional **Continuity**; not a substitute for it.",
    },
    "CJS-5.20": {
        "title": "reversibility and containment terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Constitutional **Continuity** aim — reversibility protects against irreversible constitutional harm.",
    },
    "CJS-5.21": {
        "title": "adversarial robustness and abuse-resistance terms",
        "leg": "Continuity band",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Adversarial resilience serves constitutional **Continuity** under material stake.",
    },
    "CJS-5.22": {
        "title": "constrained-secrecy and protected-investigation terms",
        "leg": "Integrative",
        "aim": "Flourishing",
        "cross": "**Oversight** and **Accountability** — secrecy limits must remain auditable and challengeable",
        "continuity_note": "",
    },
    "CJS-5.23": {
        "title": "intervention and override integrity terms",
        "leg": "Integrative",
        "aim": "Continuity",
        "cross": "**Accountability** and **Continuity** — technical complement to **CJS-5.14** governance authorization",
        "continuity_note": "Distinguish technical intervention integrity from constitutional **Continuity** aim language.",
    },
}

# old ID -> source file
OLD_SOURCE: dict[str, str] = {
    "CJS-5.2": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.3": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.4": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.5": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.6": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.7": "cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "CJS-5.8": "cjs_05b_00_evidence_audit_claim_integrity.md",
    "CJS-5.9": "cjs_05b_00_evidence_audit_claim_integrity.md",
    "CJS-5.10": "cjs_05b_00_evidence_audit_claim_integrity.md",
    "CJS-5.11": "cjs_05b_00_evidence_audit_claim_integrity.md",
    "CJS-5.12": "cjs_05c_00_participation_comprehension_disclosure.md",
    "CJS-5.13": "cjs_05c_00_participation_comprehension_disclosure.md",
    "CJS-5.14": "cjs_05c_00_participation_comprehension_disclosure.md",
    "CJS-5.15": "cjs_05c_00_participation_comprehension_disclosure.md",
    "CJS-5.16": "cjs_05d_00_dependency_exit_lifecycle_integrity.md",
    "CJS-5.17": "cjs_05d_00_dependency_exit_lifecycle_integrity.md",
    "CJS-5.18": "cjs_05d_00_dependency_exit_lifecycle_integrity.md",
    "CJS-5.19": "cjs_05e_00_failure_robustness_intervention_correction.md",
    "CJS-5.20": "cjs_05e_00_failure_robustness_intervention_correction.md",
    "CJS-5.21": "cjs_05e_00_failure_robustness_intervention_correction.md",
    "CJS-5.22": "cjs_05e_00_failure_robustness_intervention_correction.md",
    "CJS-5.23": "cjs_05e_00_failure_robustness_intervention_correction.md",
}

NEW_FILES: dict[str, dict] = {
    "cjs_05o_oversight_operations.md": {
        "family_title": "Oversight leg (CJS-5.2–CJS-5.6)",
        "preamble": (
            "This family operationalizes the **Oversight** leg of the [Constitutional Triad]"
            "(../core_00_preamble.md#constitutional-triad): watching, auditing, assuring, "
            "and verifying that implementation claims remain reviewable across **CJS**, **CS**, "
            "**CI**, and **CF**. Clusters here must be read together — a strong control in one "
            "link cannot cure a material failure in another."
        ),
        "clusters": ["CJS-5.2", "CJS-5.3", "CJS-5.4", "CJS-5.5", "CJS-5.6"],
    },
    "cjs_05p_participation_operations.md": {
        "family_title": "Participation leg (CJS-5.7–CJS-5.10)",
        "preamble": (
            "This family operationalizes the **Participation** leg of the [Constitutional Triad]"
            "(../core_00_preamble.md#constitutional-triad): quorum, comprehension, salience, "
            "and disclosure pathways that let materially affected sentients understand, contest, "
            "and shape outcomes. Primary constitutional aim: [Flourishing]"
            "(../core_01_a_values_principles.md#flourishing)."
        ),
        "clusters": ["CJS-5.7", "CJS-5.8", "CJS-5.9", "CJS-5.10"],
    },
    "cjs_05a_accountability_operations.md": {
        "family_title": "Accountability leg (CJS-5.11–CJS-5.15)",
        "preamble": (
            "This family operationalizes the **Accountability** leg of the [Constitutional Triad]"
            "(../core_00_preamble.md#constitutional-triad): authority distribution, justification "
            "burdens, procedural integrity, intervention authorization, and structural review. "
            "Accountability clusters scale with [material stake](../core_00_preamble.md#material-stake) "
            "and must remain contestable in practice."
        ),
        "clusters": ["CJS-5.11", "CJS-5.12", "CJS-5.13", "CJS-5.14", "CJS-5.15"],
    },
    "cjs_05c_continuity_operations.md": {
        "family_title": "Continuity aim operations (CJS-5.16–CJS-5.21)",
        "preamble": (
            "This family operationalizes the constitutional [Continuity aim]"
            "(../core_01_a_values_principles.md#continuity): preserving lawful function under "
            "dependency, lifecycle change, stress, and adversarial conditions. "
            "**Continuity disambiguation:** constitutional **Continuity aim** (Chapter One §1) "
            "is distinct from operational or protocol continuity elsewhere in the corpus."
        ),
        "clusters": ["CJS-5.16", "CJS-5.17", "CJS-5.18", "CJS-5.19", "CJS-5.20", "CJS-5.21"],
    },
    "cjs_05i_integrative_operations.md": {
        "family_title": "Integrative cross-leg operations (CJS-5.22–CJS-5.23)",
        "preamble": (
            "This family holds clusters that require simultaneous satisfaction across Triad legs "
            "and cannot be owned cleanly by one leg alone: constrained secrecy (Oversight + "
            "Accountability) and technical intervention integrity (Accountability + Continuity, "
            "complementing **CJS-5.14** governance authorization)."
        ),
        "clusters": ["CJS-5.22", "CJS-5.23"],
    },
}

OLD_TO_NEW = {old: new for old, new in CLUSTER_RENUMBER.items()}
NEW_TO_OLD = {v: k for k, v in CLUSTER_RENUMBER.items()}

# For unchanged IDs, map to self
for n in range(16, 20):
    cid = f"CJS-5.{n}"
    OLD_TO_NEW.setdefault(cid, cid)
    NEW_TO_OLD.setdefault(cid, cid)

SECTION_SPLIT = re.compile(r"(?=^## CJS-5\.\d+)", re.MULTILINE)
SECTION_HEADING = re.compile(r"^## (CJS-5\.\d+)\s+(.+)$", re.MULTILINE)

DEPRECATED_ALIAS_TABLE = """
| Deprecated ID | Current ID | Title |
|---|---|---|
| **CJS-5.2** | **CJS-5.11** | distributed and proportional authority terms |
| **CJS-5.3** | **CJS-5.14** | intervention governance and override-authorization terms |
| **CJS-5.4** | **CJS-5.2** | reflexive transparency and accountability terms |
| **CJS-5.5** | **CJS-5.12** | burden-of-justification and constraint terms |
| **CJS-5.6** | **CJS-5.22** | constrained-secrecy and protected-investigation terms |
| **CJS-5.7** | **CJS-5.13** | procedural integrity and adjudication terms |
| **CJS-5.8** | **CJS-5.6** | integrity assurance and resilience operations |
| **CJS-5.9** | **CJS-5.3** | auditability and reconstructability terms |
| **CJS-5.10** | **CJS-5.4** | tiered transparency and audit-access terms |
| **CJS-5.11** | **CJS-5.5** | independent verification and claim-integrity terms |
| **CJS-5.12** | **CJS-5.7** | quorum and participatory legitimacy terms |
| **CJS-5.13** | **CJS-5.8** | comprehensibility and cognitive accessibility terms |
| **CJS-5.14** | **CJS-5.9** | salience integrity and attention-allocation terms |
| **CJS-5.15** | **CJS-5.10** | disclosure sufficiency and observability terms |
| **CJS-5.20** | **CJS-5.23** | intervention and override integrity terms |
| **CJS-5.21** | **CJS-5.20** | reversibility and containment terms |
| **CJS-5.22** | **CJS-5.21** | adversarial robustness and abuse-resistance terms |
| **CJS-5.23** | **CJS-5.15** | structural review, correction urgency, and disclosure terms |
"""


def renumber_text(text: str) -> str:
    """Renumber cluster IDs using temp tokens; longest suffixes first to avoid prefix collisions."""
    ordered = sorted(
        CLUSTER_RENUMBER.items(),
        key=lambda kv: len(kv[0]),
        reverse=True,
    )
    temps: dict[str, str] = {}
    for idx, (old, new) in enumerate(ordered):
        if old == new:
            continue
        token = f"__CJS5REN{idx:02d}__"
        temps[token] = new
        text = text.replace(old, token)
    for token, new in temps.items():
        text = text.replace(token, new)
    return text


def principle_basis(new_id: str) -> str:
    old_id = NEW_TO_OLD.get(new_id, new_id)
    sections = OLD_PRINCIPLE_MAP.get(old_id, [])
    if not sections:
        return ""
    formatted = ", ".join(f"§{s}" for s in sections)
    return f"- Chapter One basis: {formatted} (see [CJS-5.1](#cjs-51-constitutional-compass-and-cluster-map) map)."


def constitutional_frame(new_id: str) -> list[str]:
    meta = CLUSTER_META.get(new_id, {})
    if not meta:
        return []
    lines = [
        f"- Constitutional frame: **{meta['leg']}** leg; **{meta['aim']}** aim (primary); "
        "scales with [material stake](../core_00_preamble.md#material-stake) via "
        "[Materiality Determination](../core_05defs_oversight.md#materiality-determination)."
    ]
    if meta.get("cross"):
        lines.append(f"- Cross-leg note: {meta['cross']}.")
    if meta.get("continuity_note"):
        lines.append(f"- Continuity disambiguation: {meta['continuity_note']}")
    basis = principle_basis(new_id)
    if basis:
        lines.append(basis)
    return lines


def extract_sections(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    parts = SECTION_SPLIT.split(text)
    for part in parts:
        m = SECTION_HEADING.match(part)
        if m:
            sections[m.group(1)] = part
    return sections


def inject_constitutional_frame(section: str, new_id: str) -> str:
    frame_lines = constitutional_frame(new_id)
    if not frame_lines:
        return section
    block = "\n" + "\n".join(frame_lines)
    pattern = (
        r"(<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>"
        r".*?)(\n</details>\s*\n\s*<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Definitions)"
    )
    return re.sub(pattern, r"\1" + block + r"\2", section, count=1, flags=re.DOTALL)


def update_section_header(section: str, new_id: str) -> str:
    meta = CLUSTER_META[new_id]
    title = meta["title"]
    # Replace heading
    section = SECTION_HEADING.sub(f"## {new_id} {title}", section, count=1)
    return section


def build_family_file(filename: str, spec: dict, all_sections: dict[str, str]) -> str:
    clusters = spec["clusters"]
    parts = [
        f"## {spec['family_title']}",
        "<details>",
        '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>',
        "",
        "- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.",
        f"- Downstream: this section's local operational requirements for **{spec['family_title']}**.",
        "- Read with: [CJS-5.1](cjs_05_cross_implementation_operational_terms.md#cjs-51-constitutional-compass-and-cluster-map) constitutional compass.",
        "",
        "</details>",
        "",
        "<br>",
        "",
        "",
        spec["preamble"],
        "",
        "| Cluster | Section |",
        "|---|---|",
    ]
    for cid in clusters:
        parts.append(f"| **{cid}** | {CLUSTER_META[cid]['title']} |")
    parts.extend(["", "---", ""])

    for new_id in clusters:
        old_id = NEW_TO_OLD[new_id]
        section = all_sections.get(old_id, "")
        if not section:
            raise RuntimeError(f"Missing section {old_id} for {new_id}")
        section = renumber_text(section)
        section = update_section_header(section, new_id)
        section = inject_constitutional_frame(section, new_id)
        parts.append(section.rstrip())
        parts.append("")
        parts.append("---")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def build_compass_section() -> str:
    rows = []
    for new_id in sorted(CLUSTER_META.keys(), key=lambda x: float(x.split(".")[1])):
        m = CLUSTER_META[new_id]
        old_id = NEW_TO_OLD.get(new_id, new_id)
        old_changed = "—" if old_id == new_id else f"was **{old_id}**"
        sections = OLD_PRINCIPLE_MAP.get(old_id, OLD_PRINCIPLE_MAP.get(new_id, []))
        ch1 = ", ".join(f"§{s}" for s in sections) if sections else "—"
        cont = m.get("continuity_note", "") or "—"
        cross = m.get("cross", "") or "—"
        rows.append(
            f"| **{new_id}** | {m['title']} | {m['leg']} | {m['aim']} | {ch1} | {cross} | {cont} | {old_changed} |"
        )

    return f"""## CJS-5.1 Constitutional compass and cluster map
<a id="cjs-51-constitutional-compass-and-cluster-map"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [Chapter One](../core_01_b_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) principles — [Constitutional Triad](../core_00_preamble.md#constitutional-triad), [Two Constitutional Aims](../core_01_a_values_principles.md#two-constitutional-aims), and [material stake](../core_00_preamble.md#material-stake).
- Downstream: constitutional orientation for all **CJS-5.2–CJS-5.23** operational clusters.
- Read with: [CJS-5.0](cjs_05_cross_implementation_operational_terms.md#cjs-50-role-definition-preface-and-standing-competency-gate-interface) role preface when role authority is in play; **CJS-2.1** topic router when a cross-layer topic is triggered.

</details>

<br>

Use this compass before applying any **CJS-5** operational cluster. **CJS-5** operationalizes Chapter Five definitions and owner-file rules across **CJS**, **CS**, **CI**, and **CF**; it does not replace the [Constitutional Triad](../core_00_preamble.md#constitutional-triad), [Two Constitutional Aims](../core_01_a_values_principles.md#two-constitutional-aims), or [material stake](../core_00_preamble.md#material-stake) scaling required by [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract).

**Reading order**

1. This compass and the constitutional bands below.
2. The constitutional band file for the relevant Triad leg, **Continuity** band, or **Integrative** band.
3. **CJS-2.1** mandatory read-with when a topic-router row applies.
4. Individual cluster OP terms (pinned cluster floor first, then sub-rules).

**Constitutional bands**

| Band | File | Clusters |
|---|---|---|
| **Oversight leg** | [cjs_05o_oversight_operations.md](cjs_05o_oversight_operations.md) | **CJS-5.2–CJS-5.6** |
| **Participation leg** | [cjs_05p_participation_operations.md](cjs_05p_participation_operations.md) | **CJS-5.7–CJS-5.10** |
| **Accountability leg** | [cjs_05a_accountability_operations.md](cjs_05a_accountability_operations.md) | **CJS-5.11–CJS-5.15** |
| **Continuity aim** | [cjs_05c_continuity_operations.md](cjs_05c_continuity_operations.md) | **CJS-5.16–CJS-5.21** |
| **Integrative cross-leg** | [cjs_05i_integrative_operations.md](cjs_05i_integrative_operations.md) | **CJS-5.22–CJS-5.23** |

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): full cluster map</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this section or in other corpus files. Per-cluster constitutional framing lives in each cluster's Trace block; use this map for cross-cluster lookup, audits, and migration reference.

**Cluster map**

| ID | Title | Triad leg / band | Primary aim | Chapter One § basis | Cross-leg note | Continuity disambiguation | Prior ID |
|---|---|---|---|---|---|---|---|
{chr(10).join(rows)}

</details>
"""


def build_redirect_stub(old_file: str, new_file: str, note: str) -> str:
    return f"""# Redirect — retired family file

This file is **retired** after the CJS-5 constitutional reorganization. {note}

**Read instead:** [{new_file}]({new_file})

See [CJS5_DEPRECATED_CLUSTER_ID_ALIASES_2026-06-18.md](../../archive/corpus_joint_structure_retired/CJS5_DEPRECATED_CLUSTER_ID_ALIASES_2026-06-18.md) for the deprecated-ID alias table.
"""


REDIRECT_MAP = {
    "cjs_05a_00_authority_constraint_secrecy_procedure.md": (
        "cjs_05a_accountability_operations.md",
        "Authority, constraint, secrecy, and procedure clusters are now split across Accountability, Integrative, and Oversight bands.",
    ),
    "cjs_05b_00_evidence_audit_claim_integrity.md": (
        "cjs_05o_oversight_operations.md",
        "Evidence, audit, and claim-integrity clusters are now in the Oversight leg band.",
    ),
    "cjs_05c_00_participation_comprehension_disclosure.md": (
        "cjs_05p_participation_operations.md",
        "Participation, comprehension, and disclosure clusters are now in the Participation leg band.",
    ),
    "cjs_05d_00_dependency_exit_lifecycle_integrity.md": (
        "cjs_05c_continuity_operations.md",
        "Dependency, exit, and lifecycle clusters are now in the Continuity aim band.",
    ),
    "cjs_05e_00_failure_robustness_intervention_correction.md": (
        "cjs_05c_continuity_operations.md",
        "Failure and robustness clusters are in the Continuity band; intervention integrity is in the Integrative band.",
    ),
}


def iter_corpus_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == "cjs5_constitutional_migration.py":
            continue
        yield path


def update_cross_file(cross_path: Path, dry_run: bool) -> None:
    text = renumber_text(cross_path.read_text(encoding="utf-8"))
    compass = build_compass_section()
    text = re.sub(
        r"## CJS-5\.1 Cluster family index.*",
        compass + "\n\n---\n\n**Previous file:**",
        text,
        flags=re.DOTALL,
    )
    text = text.replace(
        "**Next file:** [cjs_05a_00_authority_constraint_secrecy_procedure.md](cjs_05a_00_authority_constraint_secrecy_procedure.md)",
        "**Next file:** [cjs_05o_oversight_operations.md](cjs_05o_oversight_operations.md)",
    )
    if not dry_run:
        cross_path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # Collect all sections from old files
    all_sections: dict[str, str] = {}
    for fname in set(OLD_SOURCE.values()):
        all_sections.update(extract_sections(CJS_DIR / fname))

    # Build new family files
    for filename, spec in NEW_FILES.items():
        content = build_family_file(filename, spec, all_sections)
        path = CJS_DIR / filename
        if args.dry_run:
            print(f"Would write {path} ({len(content)} bytes)")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"Wrote {path}")

    # Redirect stubs
    for old_file, (new_file, note) in REDIRECT_MAP.items():
        stub = build_redirect_stub(old_file, new_file, note)
        path = CJS_DIR / old_file
        if args.dry_run:
            print(f"Would stub {path}")
        else:
            path.write_text(stub, encoding="utf-8")
            print(f"Stubbed {path}")

    # Corpus-wide renumber (excluding new family files and cross file — compass written after)
    skip_names = set(NEW_FILES) | {"cjs_05_cross_implementation_operational_terms.md"}
    changed = 0
    for path in iter_corpus_files(ROOT):
        if path.parent == CJS_DIR and path.name in skip_names:
            continue
        original = path.read_text(encoding="utf-8")
        updated = renumber_text(original)
        if updated != original:
            changed += 1
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")
    print(f"{'Would update' if args.dry_run else 'Updated'} {changed} corpus files with renumbered IDs")

    # Write compass after corpus renumber so IDs are not double-transformed
    update_cross_file(CJS_DIR / "cjs_05_cross_implementation_operational_terms.md", args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
