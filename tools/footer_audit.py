#!/usr/bin/env python3
"""Audit corpus navigation footers for chain integrity and human-readable formatting."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_CHAIN = (
    "core_00.000_preamble.md",
    "core_01.005_values_principles.md",
    "core_01.010_interaction_interpretation.md",
    "core_01.015_stewardship_capacity_principles.md",
    "core_02.000_definition_structure.md",
    "core_03.000_definition_integrity.md",
    "core_04.000_burden_traceability_verification.md",
    "core_05.000_definitions_home.md",
    "core_05.005_apex_accountability_leg.md",
    "core_05.010_apex_continuity_aim.md",
    "core_05.015_apex_flourishing_aim.md",
    "core_05.020_apex_oversight_leg.md",
    "core_05.025_apex_participation_leg.md",
    "core_05.030_apex_timeliness_leg.md",
    "core_05.035_band_accountability.md",
    "core_05.040_band_continuity.md",
    "core_05.045_band_integrative.md",
    "core_05.050_band_oversight.md",
    "core_05.055_band_participation.md",
    "core_05.060_band_performance.md",
    "core_07.000_charters.md",
    "core_08.000_functional_independence_separation_of_duties.md",
    "core_09.005_system_alignment_certification_evaluation.md#chapter-nine-part-a-certification-evaluation",
    "core_09.010_system_alignment_certification_record_process.md#chapter-nine-part-b-certification-record-and-process",
    "core_09.015_system_alignment_certification_illustrations.md#chapter-nine-part-c-certification-illustrations",
    "core_09.020_institutional_alignment_certification.md#chapter-nine-part-d-institutional-alignment-certification",
    "core_10.000_standing_assessment.md",
    "core_11.000_standing_integration.md",
    "core_12.005_misconduct_designation.md",
    "core_12.010_misconduct_pattern_applications.md",
    "core_13.000_forum.md",
    "core_10.005_application_vignettes.md",
    "core_06.005_rights_part_a.md",
    "core_06.010_rights_part_b.md",
    "core_06.015_rights_part_c.md",
    "core_06.020_rights_part_d.md",
    "core_06.025_rights_part_e.md",
    "core_14.000_governance.md",
    "core_15.000_non_regression.md",
    "core_16.000_expansion_supremacy.md",
    "core_17.000_amendment_ratification.md",
    "core_18.000_incorporation.md",
)

CJS_CHAIN = (
    "corpus_joint_structure/cjs_reader_guide.md",
    "corpus_joint_structure/cjs_00.110_scope_purpose_boundary_interface.md",
    "corpus_joint_structure/cjs_18.105_drafting_contracts.md",
    "corpus_joint_structure/cjs_05.140_odef_parse_mechanics.md",
    "corpus_joint_structure/cjs_18.110_specific_joint_interlocks.md",
    "corpus_joint_structure/cjs_08.105_support_hosting_classification.md",
    "corpus_joint_structure/cjs_05.105_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_05.115_audit_process.md",
    "corpus_joint_structure/cjs_05.110_oversight_operations.md",
    "corpus_joint_structure/cjs_05.120_participation_operations.md",
    "corpus_joint_structure/cjs_05.125_accountability_operations.md",
    "corpus_joint_structure/cjs_05.130_continuity_operations.md",
    "corpus_joint_structure/cjs_05.135_integrative_operations.md",
)

# Side-path registry annexes: not in the default wrapper → *-1 reading order.
CJS_REGISTRY_ANNEX = "corpus_joint_structure/cjs_00.105_registry_and_reading_rules.md"

CS_CHAIN = tuple(
    f"corpus_systems/{name}"
    for name in (
        "cs_00.310_scope_purpose_identifier_rules.md",
        "cs_06.305_information_types_and_handling.md",
        "cs_06.310_data_classifications.md",
        "cs_09.305_system_classification_machinery.md",
        "cs_09.310_system_impact_classifications.md",
        "cs_14.305_critical_system_stewardship.md",
        "cs_06.345_design_testing_verification_deployment.md",
        "cs_06.340_system_requirements.md",
        "cs_06.315_comprehensibility_complexity_stewardship.md",
        "cs_06.320_justice_safeguards_restitution_rehabilitation.md",
        "cs_06.325_adaptive_sustainability_ecosystem_resilience.md",
        "cs_06.335_resource_allocation_funding_stewardship.md",
        "cs_06.350_transition_constitution_migration_governance.md",
        "cs_06.355_subversion_response_replacement_reconstitution.md",
        "cs_06.330_decentralized_continuity_partition_resilience.md",
    )
)

CS_REGISTRY_ANNEX = "corpus_systems/cs_00.305_registry_and_reading_rules.md"

CI_CHAIN = tuple(
    f"corpus_institutions/{name}"
    for name in (
        "ci_00.210_scope_purpose_legitimacy_interface.md",
        "ci_08.205_institutional_design_separation_of_powers.md",
        "ci_14.205_appointment_competency_rotation_removal.md",
        "ci_08.210_conflict_integrity_anti_capture_anti_corruption.md",
        "ci_13.205_procedure_integrity_contestability_secondary_review.md",
        "ci_08.215_oversight_assurance_controls_evidence.md",
        "ci_06.205_transparency_participation_accessible_pathways.md",
        "ci_09.210_classification_linked_institutional_obligations.md",
        "ci_06.210_public_revenue_fees_recurring_charges_billing_integrity.md",
        "ci_06.215_resource_stewardship_incentive_integrity.md",
        "ci_13.210_cross_institution_coordination_escalation.md",
        "ci_11.210_institutional_failure_dissolution.md",
        "ci_11.215_institutional_accountability_sanctions.md",
        "ci_06.275_transitional_governance_institutional_evolution.md",
        "ci_06.220_neurodiversity_disability_justice_trauma_informed_participation.md",
        "ci_06.225_care_labor_dependent_support_respite_care_economy_fairness.md",
        "ci_06.230_end_of_life_continuity_memorial_dignity_posthumous_data.md",
        "ci_06.235_collective_public_health_epidemic_response_addiction_informed_care.md",
        "ci_06.240_vulnerable_personal_services_markets_article_viie_interface.md",
        "ci_06.245_relational_coercive_control_intimate_power_anti_domination.md",
        "ci_06.250_community_life_voluntary_association_non_instrumental_time.md",
        "ci_06.255_commons_cooperatives_mutual_aid_non_market_governance.md",
        "ci_06.260_place_based_stewardship_indigenous_continuity_consultation.md",
        "ci_06.265_innovation_reward_disclosure_anti_enclosure.md",
        "ci_06.270_scientific_publication_peer_review_replication_evidence_stewardship.md",
        "ci_00.215_compliance_mapping_stable_registry.md",
        "ci_11.205_remedy_systems_institutional_redress_capacity.md",
    )
)

CI_REGISTRY_ANNEX = "corpus_institutions/ci_00.205_registry_and_reading_rules.md"

CF_CHAIN = tuple(
    f"corpus_forum/{name}"
    for name in (
        "cf_00.410_scope_authority_boundary_rules.md",
        "cf_13.405_forum_formation_chamber_structure.md",
        "cf_13.410_panel_formation_disclosure_recusal_bench_constitution.md",
        "cf_13.415_routing_operations_transfer_certification_representative_treatment.md",
        "cf_13.420_appeal_secondary_review_exhaustion_pathways.md",
        "cf_13.425_integrity_safeguards_anti_capture_anti_self_judging.md",
        "cf_13.430_forum_forensic_analytical_support.md",
        "cf_13.435_independent_investigative_service_prosecution_interface.md",
        "cf_13.440_technical_specialist_forums_specialist_chambers.md",
        "cf_13.445_performance_backlog_publication_accessibility.md",
        "cf_13.450_forum_continuity.md",
        "cf_13.455_fallback_operation.md",
        "cf_13.460_emergency_adjudication.md",
        "cf_13.465_standard_records_forms_evidence_artifacts.md",
        "cf_13.470_staffing_reserve_capacity_structural_records.md",
    )
)

CF_REGISTRY_ANNEX = "corpus_forum/cf_00.405_registry_and_reading_rules.md"

REGISTRY_ANNEXES: tuple[tuple[str, str, str], ...] = (
    (CJS_REGISTRY_ANNEX, "corpus_joint_structure.md", CJS_CHAIN[0]),
    (CS_REGISTRY_ANNEX, "corpus_systems.md", CS_CHAIN[0]),
    (CI_REGISTRY_ANNEX, "corpus_institutions.md", CI_CHAIN[0]),
    (CF_REGISTRY_ANNEX, "corpus_forum.md", CF_CHAIN[0]),
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
}

WRAPPER_ROOTS = {
    "corpus_joint_structure.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
}

TERMINAL_ALIGNMENT_FILES = {
    "corpus_joint_structure/cjs_05.135_integrative_operations.md",
    "corpus_systems/cs_06.330_decentralized_continuity_partition_resilience.md",
    "corpus_institutions/ci_00.215_compliance_mapping_stable_registry.md",
}

CORPUS_ALIGNMENT_RE = re.compile(r"\*Corpus alignment:\* edition")
PREV_RE = re.compile(r"^\*\*Previous file:\*\* \[([^\]]+)\]\(([^)]+)\)\s*$")
NEXT_RE = re.compile(r"^\*\*Next file:\*\* \[([^\]]+)\]\(([^)]+)\)\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--repair",
        action="store_true",
        help="Rewrite footers to the canonical template (adopted-implementation subfiles only).",
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
    if "/" in current:
        # A repository-root file linked from a subfolder needs the parent hop.
        return "../" * current.count("/") + nxt
    return nxt


def expected_prev_link(current: str, prev: str) -> str:
    if "/" in current and prev in WRAPPER_ROOTS:
        return f"../{prev}"
    if "/" in current and "/" in prev:
        return basename(prev)
    if "/" not in current and "/" in prev:
        folder = prev.split("/")[0]
        return f"{folder}/{basename(prev)}"
    return basename(prev) if "/" in prev else prev


NAV_FOOTER_PATTERNS = (
    r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n",
    r"\n\*\*Previous file:\*\*[^\n]*\n\n\*\*Next file:\*\*[^\n]*\n",
    r"\n---\n\n\*\*Previous file:\*\*[^\n]*\n",
    r"\n---\n\n\*\*Next file:\*\*[^\n]*\n",
    r"\n\*\*Previous file:\*\*[^\n]*\n",
    r"\n\*\*Next file:\*\*[^\n]*\n",
)


def strip_existing_footer(text: str) -> str:
    """Remove navigation footer blocks anywhere in the file (including stale mid-file footers)."""
    text = text.rstrip() + "\n"
    changed = True
    while changed:
        changed = False
        for pattern in NAV_FOOTER_PATTERNS:
            new_text = re.sub(pattern, "\n", text)
            if new_text != text:
                text = new_text
                changed = True
    # Strip terminal corpus-alignment blocks (re-applied only on terminal repair targets).
    while True:
        new_text = text
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
                "*Corpus alignment:* edition `SC-Corpus-2026.04.33`, effective **2026-04-24**; "
                "edition and custody in [README.md](../README.md) and "
                "[Chapter Five *Corpus*](../core_05.045_band_integrative.md#corpus).",
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


def navigation_footer_line_numbers(text: str) -> tuple[list[int], list[int]]:
    prev_lines: list[int] = []
    next_lines: list[int] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        if PREV_RE.match(line):
            prev_lines.append(idx)
        if NEXT_RE.match(line):
            next_lines.append(idx)
    return prev_lines, next_lines


def audit_file(
    root: Path,
    rel: str,
    prev: str | None,
    nxt: str,
    errors: list[str],
) -> None:
    path = root / rel.split("#", 1)[0]
    if not path.exists():
        errors.append(f"{rel}: missing file in reading chain")
        return
    # Fragment-addressed chain nodes (section deep-links) are validated via
    # neighbor Previous/Next hrefs; the host file need not carry end footers.
    if "#" in rel:
        return
    text = path.read_text(encoding="utf-8")
    info = parse_footer(text)
    prev_lines, next_lines = navigation_footer_line_numbers(text)

    if len(next_lines) > 1:
        errors.append(
            f"{rel}: multiple **Next file:** footers at lines {next_lines}"
        )
    if len(prev_lines) > 1:
        errors.append(
            f"{rel}: multiple **Previous file:** footers at lines {prev_lines}"
        )
    if len(next_lines) == 1 and info["next_idx"] is not None:
        last_content_line = len(text.splitlines())
        if info["next_idx"] < last_content_line - 5:
            errors.append(
                f"{rel}: **Next file:** at line {info['next_idx']} is not at file end "
                f"(stale mid-file navigation footer)"
            )

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
            elif repair_file(root, rel, prev, nxt):
                repaired += 1
        audit_file(root, rel, prev, nxt, errors)

    # Registry annexes: side path from wrapper → annex → *-1 (not default reading order).
    for annex_rel, annex_prev, annex_nxt in REGISTRY_ANNEXES:
        if args.repair:
            if repair_file(root, annex_rel, annex_prev, annex_nxt):
                repaired += 1
        audit_file(root, annex_rel, annex_prev, annex_nxt, errors)

    if args.repair and repaired:
        print(f"Repaired {repaired} file(s). Re-auditing...")
        errors.clear()
        for i, rel in enumerate(chain):
            prev = chain[i - 1] if i > 0 else None
            nxt = chain[i + 1] if i + 1 < len(chain) else "README.md"
            audit_file(root, rel, prev, nxt, errors)
        for annex_rel, annex_prev, annex_nxt in REGISTRY_ANNEXES:
            audit_file(root, annex_rel, annex_prev, annex_nxt, errors)

    if errors:
        print("Footer audit failures:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"Footer audit OK ({len(chain)} files in reading chain"
        f" + {len(REGISTRY_ANNEXES)} registry annexes)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
