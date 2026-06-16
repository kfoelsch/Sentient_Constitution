#!/usr/bin/env python3
"""Audit corpus navigation footers for chain integrity and human-readable formatting."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_CHAIN = (
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_assessment.md",
    "core_07-07_standing_integration.md",
    "core_08-08_misconduct.md",
    "core_09-09_forum.md",
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
    "core_11-11_governance.md",
    "core_12-14_amendment.md",
    "core_15-15_incorporation.md",
)

CJS_CHAIN = (
    "corpus_joint_structure/cjs_00_registry_and_reading_rules.md",
    "corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md",
    "corpus_joint_structure/cjs_02_implementation_integration_map.md",
    "corpus_joint_structure/cjs_03_joint_structural_obligations.md",
    "corpus_joint_structure/cjs_04_specific_joint_interlocks.md",
    "corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md",
    "corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md",
    "corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md",
    "corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md",
)

CS_CHAIN = tuple(
    f"corpus_systems/{name}"
    for name in (
        "cs_00_registry_and_reading_rules.md",
        "cs_01_scope_purpose_identifier_rules.md",
        "cs_02_implementation_integration_map.md",
        "cs_protocol_a_system_design_testing_verification_deployment.md",
        "cs_protocol_b_system_comprehensibility_complexity_stewardship.md",
        "cs_protocol_c_justice_safeguards_restitution_rehabilitation.md",
        "cs_s1_information_types_and_handling.md",
        "cs_s2_system_classification_and_handling.md",
        "cs_s3_critical_system_stewardship.md",
        "cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md",
        "cs_protocol_s5_resource_allocation_funding_stewardship.md",
        "cs_protocol_t_transition_constitution_migration_governance.md",
        "cs_protocol_r_subversion_response_replacement_reconstitution.md",
        "cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md",
    )
)

CI_CHAIN = tuple(
    f"corpus_institutions/{name}"
    for name in (
        "ci_00_registry_and_reading_rules.md",
        "ci_01_scope_purpose_legitimacy_interface.md",
        "ci_02_implementation_integration_map.md",
        "ci_03_institutional_design_separation_of_powers.md",
        "ci_04_appointment_competency_rotation_removal.md",
        "ci_05_conflict_integrity_anti_capture_anti_corruption.md",
        "ci_06_procedure_integrity_contestability_secondary_review.md",
        "ci_07_oversight_assurance_controls_evidence.md",
        "ci_08_cross_institution_coordination_escalation.md",
        "ci_09_classification_linked_institutional_obligations.md",
        "ci_10_public_revenue_fees_recurring_charges_billing_integrity.md",
        "ci_11_resource_stewardship_incentive_integrity.md",
        "ci_12_transparency_participation_accessible_pathways.md",
        "ci_13_institutional_failure_sanctions_dissolution_accountability.md",
        "ci_14_transitional_governance_institutional_evolution.md",
        "ci_15_vulnerable_personal_services_markets_article_xc_interface.md",
        "ci_16_innovation_reward_disclosure_anti_enclosure.md",
        "ci_17_scientific_publication_peer_review_replication_evidence_stewardship.md",
        "ci_18_community_life_voluntary_association_non_instrumental_time.md",
        "ci_19_end_of_life_continuity_memorial_dignity_posthumous_data.md",
        "ci_20_care_labor_dependent_support_respite_care_economy_fairness.md",
        "ci_21_relational_coercive_control_intimate_power_anti_domination.md",
        "ci_22_commons_cooperatives_mutual_aid_non_market_governance.md",
        "ci_23_place_based_stewardship_indigenous_continuity_consultation.md",
        "ci_24_neurodiversity_disability_justice_trauma_informed_participation.md",
        "ci_25_collective_public_health_epidemic_response_addiction_informed_care.md",
        "ci_26_compliance_mapping_stable_registry.md",
    )
)

CF_CHAIN = tuple(
    f"corpus_forum/{name}"
    for name in (
        "cf_00_registry_and_reading_rules.md",
        "cf_01_scope_authority_boundary_rules.md",
        "cf_02_implementation_integration_map.md",
        "cf_03_forum_formation_tribunal_mapping_chamber_structure.md",
        "cf_04_panel_formation_disclosure_recusal_bench_constitution.md",
        "cf_05_routing_operations_transfer_certification_representative_treatment.md",
        "cf_06_appeal_secondary_review_exhaustion_pathways.md",
        "cf_07_integrity_safeguards_anti_capture_anti_self_judging.md",
        "cf_08_forum_forensic_analytical_support.md",
        "cf_09_independent_investigative_service_prosecution_interface.md",
        "cf_10_technical_specialist_forums_specialist_chambers.md",
        "cf_11_performance_backlog_publication_accessibility.md",
        "cf_12_forum_continuity.md",
        "cf_13_fallback_operation.md",
        "cf_14_emergency_adjudication.md",
        "cf_15_standard_records_forms_evidence_artifacts.md",
        "cf_16_staffing_reserve_capacity_structural_records.md",
    )
)

READING_CHAIN: tuple[str, ...] = (
    ("README.md",)
    + CORE_CHAIN
    + ("corpus_joint_structure.md",)
    + CJS_CHAIN
    + ("corpus_systems.md",)
    + CS_CHAIN
    + ("corpus_institutions.md",)
    + CI_CHAIN
    + ("corpus_forum.md",)
    + CF_CHAIN
    + ("doc_architecture.md",)
)

NEXT_ONLY = {
    "README.md",
    "doc_architecture.md",
    "corpus_joint_structure.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    *CORE_CHAIN,
    CJS_CHAIN[0],
    CS_CHAIN[0],
    CI_CHAIN[0],
    CF_CHAIN[0],
}

TERMINAL_ALIGNMENT_FILES = {
    "corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md",
    "corpus_systems/cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md",
    "corpus_institutions/ci_26_compliance_mapping_stable_registry.md",
}

CORPUS_ALIGNMENT_RE = re.compile(r"\*Corpus alignment:\* edition")
PREV_RE = re.compile(r"^\*\*Previous file:\*\* \[([^\]]+)\]\(([^)]+)\)\s*$")
NEXT_RE = re.compile(r"^\*\*Next file:\*\* \[([^\]]+)\]\(([^)]+)\)\s*$")

FIRST_SUBFILE = {
    CJS_CHAIN[0],
    CS_CHAIN[0],
    CI_CHAIN[0],
    CF_CHAIN[0],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--repair",
        action="store_true",
        help="Rewrite footers to the canonical template (companion subfiles only).",
    )
    return parser.parse_args()


def basename(path: str) -> str:
    return Path(path).name


def expected_next_link(current: str, nxt: str) -> str:
    """Return the link target string expected in the current file's Next footer."""
    if nxt.startswith("corpus_") and "/" not in nxt:
        if current.startswith("corpus_joint_structure/"):
            if nxt == "corpus_systems.md":
                return "../corpus_systems.md"
        if current.startswith("corpus_systems/"):
            if nxt == "corpus_institutions.md":
                return "../corpus_institutions.md"
        if current.startswith("corpus_institutions/"):
            if nxt == "corpus_forum.md":
                return "../corpus_forum.md"
        if current.startswith("corpus_forum/"):
            if nxt == "doc_architecture.md":
                return "../doc_architecture.md"
    if "/" in current and "/" in nxt:
        return basename(nxt)
    if "/" not in current and "/" in nxt:
        folder = nxt.split("/")[0]
        return f"{folder}/{basename(nxt)}"
    return basename(nxt) if "/" in nxt else nxt


def expected_prev_link(current: str, prev: str) -> str:
    if "/" in current and "/" in prev:
        return basename(prev)
    if "/" not in current and "/" in prev:
        folder = prev.split("/")[0]
        return f"{folder}/{basename(prev)}"
    return basename(prev) if "/" in prev else prev


def strip_existing_footer(text: str) -> str:
    """Remove trailing navigation footer blocks from file tail."""
    text = text.rstrip() + "\n"
    # Repeat until no trailing nav/alignment remains.
    while True:
        new_text = text
        new_text = re.sub(
            r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n?$",
            "\n",
            new_text,
            flags=re.DOTALL,
        )
        new_text = re.sub(
            r"\n---\n\n\*\*Next file:\*\*[^\n]*\n?$",
            "\n",
            new_text,
            flags=re.DOTALL,
        )
        new_text = re.sub(
            r"\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n?$",
            "\n",
            new_text,
            flags=re.DOTALL,
        )
        new_text = re.sub(
            r"\n\*\*Next file:\*\*[^\n]*\n?$",
            "\n",
            new_text,
        )
        new_text = re.sub(
            r"\n---\n\n\*Corpus alignment:\*[^\n]*\n\n---\n?",
            "\n",
            new_text,
        )
        new_text = re.sub(
            r"\n\*Corpus alignment:\*[^\n]*\n---\n?",
            "\n",
            new_text,
        )
        new_text = re.sub(
            r"\n\*Corpus alignment:\*[^\n]*\n?",
            "\n",
            new_text,
        )
        if new_text == text:
            break
        text = new_text
    text = re.sub(r"\n---\n---\n", "\n---\n", text)
    text = re.sub(r"\n---\s*$", "", text.rstrip())
    return text.rstrip() + "\n"


def build_footer(
    current: str,
    prev: str | None,
    nxt: str,
    *,
    with_alignment: bool = False,
) -> str:
    lines: list[str] = []
    if with_alignment:
        lines.extend(
            [
                "*Corpus alignment:* edition `SC-Corpus-2026.04.32`, effective **2026-04-24**; "
                "edition and custody in [README.md](../README.md) and "
                "[Chapter Five *Corpus*](../core_05-05_definitions_c_dependent_clusters.md#corpus).",
                "",
                "---",
                "",
            ]
        )
    if prev and current not in NEXT_ONLY:
        lines.append(
            f"**Previous file:** [{expected_prev_link(current, prev)}]"
            f"({expected_prev_link(current, prev)})"
        )
        lines.append("")
    next_target = expected_next_link(current, nxt)
    lines.append(
        f"**Next file:** [{basename(nxt) if '/' in nxt else nxt}]({next_target})"
    )
    lines.append("")
    return "\n\n---\n\n" + "\n".join(lines)


def parse_footer(text: str) -> dict:
    lines = text.splitlines()
    next_idx = None
    for i in range(len(lines) - 1, -1, -1):
        if NEXT_RE.match(lines[i]):
            next_idx = i
            break
    if next_idx is None:
        return {
            "prev_label": None,
            "prev_href": None,
            "next_label": None,
            "next_href": None,
            "has_alignment": False,
            "prev_next_adjacent": False,
            "prev_idx": None,
            "next_idx": None,
        }

    prev_label = prev_href = None
    prev_idx = None
    window_start = max(0, next_idx - 25)
    for i in range(window_start, next_idx):
        if m := PREV_RE.match(lines[i]):
            prev_label, prev_href = m.group(1), m.group(2)
            prev_idx = i

    next_m = NEXT_RE.match(lines[next_idx])
    footer_tail = "\n".join(lines[window_start : next_idx + 1])
    has_alignment = bool(CORPUS_ALIGNMENT_RE.search(footer_tail))
    prev_next_adjacent = (
        prev_idx is not None
        and next_idx == prev_idx + 1
    )
    return {
        "prev_label": prev_label,
        "prev_href": prev_href,
        "next_label": next_m.group(1) if next_m else None,
        "next_href": next_m.group(2) if next_m else None,
        "has_alignment": has_alignment,
        "prev_next_adjacent": prev_next_adjacent,
        "prev_idx": prev_idx,
        "next_idx": next_idx,
    }


def audit_file(
    root: Path,
    rel: str,
    prev: str | None,
    nxt: str,
    errors: list[str],
) -> None:
    path = root / rel
    if not path.exists():
        errors.append(f"{rel}: missing file in reading chain")
        return
    text = path.read_text(encoding="utf-8")
    info = parse_footer(text)

    if not info["next_href"]:
        errors.append(f"{rel}: missing **Next file:** footer")
        return

    exp_next = expected_next_link(rel, nxt)
    if info["next_href"] != exp_next and info["next_href"] != nxt:
        errors.append(
            f"{rel}: Next points to {info['next_href']!r}, expected {exp_next!r}"
        )

    needs_prev = rel not in NEXT_ONLY
    if needs_prev and not info["prev_href"]:
        errors.append(f"{rel}: missing **Previous file:** footer")
    if not needs_prev and info["prev_href"]:
        errors.append(f"{rel}: unexpected **Previous file:** (next-only class)")

    if needs_prev and prev and info["prev_href"]:
        exp_prev = expected_prev_link(rel, prev)
        if info["prev_href"] != exp_prev and info["prev_href"] != prev:
            errors.append(
                f"{rel}: Previous points to {info['prev_href']!r}, expected {exp_prev!r}"
            )

    if info["prev_next_adjacent"]:
        errors.append(f"{rel}: Previous and Next lack blank line between them")

    if info["prev_idx"] is not None and info["next_idx"] is not None:
        if info["prev_idx"] > info["next_idx"]:
            errors.append(f"{rel}: Previous appears after Next")

    if info["has_alignment"] != (rel in TERMINAL_ALIGNMENT_FILES):
        if rel in TERMINAL_ALIGNMENT_FILES and not info["has_alignment"]:
            errors.append(f"{rel}: missing terminal *Corpus alignment:* block")
        elif rel not in TERMINAL_ALIGNMENT_FILES and info["has_alignment"]:
            errors.append(f"{rel}: unexpected *Corpus alignment:* block")

    tail = text.rstrip()
    if re.search(r"\n---\n\n---\n\n\*\*(Previous|Next) file:", tail):
        errors.append(f"{rel}: duplicate --- before navigation footer")


def repair_file(root: Path, rel: str, prev: str | None, nxt: str) -> bool:
    path = root / rel
    if rel in NEXT_ONLY and rel not in TERMINAL_ALIGNMENT_FILES:
        return False
    if rel in NEXT_ONLY and rel in FIRST_SUBFILE:
        # first subfile: next only, no repair unless malformed
        pass
    text = path.read_text(encoding="utf-8")
    body = strip_existing_footer(text)
    footer = build_footer(
        rel,
        prev,
        nxt,
        with_alignment=rel in TERMINAL_ALIGNMENT_FILES,
    )
    new_text = body.rstrip() + footer
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def repair_next_only(root: Path, rel: str, nxt: str) -> bool:
    path = root / rel
    text = path.read_text(encoding="utf-8")
    body = strip_existing_footer(text)
    next_target = expected_next_link(rel, nxt)
    label = basename(nxt) if "/" in nxt else nxt
    footer = f"\n\n---\n\n**Next file:** [{label}]({next_target})\n"
    new_text = body.rstrip() + footer
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    repaired = 0

    chain = READING_CHAIN
    for i, rel in enumerate(chain):
        prev = chain[i - 1] if i > 0 else None
        nxt = chain[i + 1] if i + 1 < len(chain) else "README.md"
        if args.repair:
            if rel in NEXT_ONLY:
                if repair_next_only(root, rel, nxt):
                    repaired += 1
            else:
                if repair_file(root, rel, prev, nxt):
                    repaired += 1
        audit_file(root, rel, prev, nxt, errors)

    if args.repair and repaired:
        print(f"Repaired {repaired} file(s). Re-auditing...")
        errors.clear()
        for i, rel in enumerate(chain):
            prev = chain[i - 1] if i > 0 else None
            nxt = chain[i + 1] if i + 1 < len(chain) else "README.md"
            audit_file(root, rel, prev, nxt, errors)

    if errors:
        print("Footer audit failures:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"Footer audit OK ({len(chain)} files in reading chain).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
