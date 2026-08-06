"""Shared corpus path discovery for audits and AI index generation."""

from __future__ import annotations

from pathlib import Path


CORE_FILES = (
    "core_00_preamble.md",
    "core_01_a_values_principles.md",
    "core_01_b_interaction_interpretation.md",
    "core_01_c_stewardship_capacity_principles.md",
    "core_02-03_definition_mechanics.md",
    "core_04-04_burden_traceability_verification.md",
    "core_05__definitions_home.md",
    "core_05_apex_accountability_leg.md",
    "core_05_apex_continuity_aim.md",
    "core_05_apex_flourishing_aim.md",
    "core_05_apex_oversight_leg.md",
    "core_05_apex_participation_leg.md",
    "core_05_apex_timeliness_leg.md",
    "core_05_band_accountability.md",
    "core_05_band_continuity.md",
    "core_05_band_integrative.md",
    "core_05_band_oversight.md",
    "core_05_band_participation.md",
    "core_05_band_performance.md",
    "core_07_a_system_alignment_certification_evaluation.md",
    "core_07_b_system_alignment_certification_record_process.md",
    "core_07-07_system_alignment_certification.md",
    "core_08-08_standing_assessment.md",
    "core_09-09_standing_integration.md",
    "core_10_a_misconduct_designation.md",
    "core_10_b_misconduct_pattern_applications.md",
    "core_11-11_forum.md",
    "core_08-11_application_vignettes.md",
    "core_06-06_rights_part_a.md",
    "core_06-06_rights_part_b.md",
    "core_06-06_rights_part_c.md",
    "core_06-06_rights_part_d.md",
    "core_12-12_governance.md",
    "core_13-15_amendment.md",
    "core_16-16_incorporation.md",
)

COMPANION_WRAPPERS = (
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
)

COMPANION_SUBDIRS = (
    "corpus_joint_structure",
    "corpus_systems",
    "corpus_institutions",
    "corpus_forum",
)

SUPPORT_DOCS = ("doc_architecture.md", "README.md")


def companion_subfiles(root: Path) -> list[str]:
    paths: list[str] = []
    for subdir in COMPANION_SUBDIRS:
        base = root / subdir
        if base.is_dir():
            paths.extend(
                path.relative_to(root).as_posix()
                for path in sorted(base.glob("*.md"))
                if path.is_file()
            )
    return paths


def binding_corpus_scope(root: Path, *, include_support_docs: bool = False) -> list[str]:
    scope = [*CORE_FILES, *COMPANION_WRAPPERS, *companion_subfiles(root)]
    if include_support_docs:
        scope.extend(SUPPORT_DOCS)
    return scope


def source_markdown_files(root: Path) -> list[Path]:
    return [root / rel for rel in binding_corpus_scope(root) if (root / rel).exists()]
