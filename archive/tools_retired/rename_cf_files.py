#!/usr/bin/env python3
"""Rename corpus_forum cf_02…cf_15 files to cf_03…cf_16 using temp staging."""

from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "corpus_forum"

RENAMES = [
    ("cf_15_staffing_reserve_capacity_structural_records.md", "cf_16_staffing_reserve_capacity_structural_records.md"),
    ("cf_14_standard_records_forms_evidence_artifacts.md", "cf_15_standard_records_forms_evidence_artifacts.md"),
    ("cf_13_emergency_adjudication.md", "cf_14_emergency_adjudication.md"),
    ("cf_12_fallback_operation.md", "cf_13_fallback_operation.md"),
    ("cf_11_forum_continuity.md", "cf_12_forum_continuity.md"),
    ("cf_10_performance_backlog_publication_accessibility.md", "cf_11_performance_backlog_publication_accessibility.md"),
    ("cf_09_technical_specialist_forums_specialist_chambers.md", "cf_10_technical_specialist_forums_specialist_chambers.md"),
    ("cf_08_independent_investigative_service_prosecution_interface.md", "cf_09_independent_investigative_service_prosecution_interface.md"),
    ("cf_07_forum_forensic_analytical_support.md", "cf_08_forum_forensic_analytical_support.md"),
    ("cf_06_integrity_safeguards_anti_capture_anti_self_judging.md", "cf_07_integrity_safeguards_anti_capture_anti_self_judging.md"),
    ("cf_05_appeal_secondary_review_exhaustion_pathways.md", "cf_06_appeal_secondary_review_exhaustion_pathways.md"),
    ("cf_04_routing_operations_transfer_certification_representative_treatment.md", "cf_05_routing_operations_transfer_certification_representative_treatment.md"),
    ("cf_03_panel_formation_disclosure_recusal_bench_constitution.md", "cf_04_panel_formation_disclosure_recusal_bench_constitution.md"),
    ("cf_02_forum_formation_tribunal_mapping_chamber_structure.md", "cf_03_forum_formation_tribunal_mapping_chamber_structure.md"),
]

def main() -> int:
    temps: list[tuple[Path, Path]] = []
    for old, new in RENAMES:
        src = DIR / old
        tmp = DIR / f"__tmp__{new}"
        if not src.exists():
            raise SystemExit(f"Missing: {src}")
        src.rename(tmp)
        temps.append((tmp, DIR / new))
        print(f"staged {old}")
    for tmp, dest in temps:
        tmp.rename(dest)
        print(f"-> {dest.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
