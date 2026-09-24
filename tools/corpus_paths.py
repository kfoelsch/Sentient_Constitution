"""Shared corpus path discovery for audits and AI index generation."""

from __future__ import annotations

import os
import re
from pathlib import Path


CORE_FILES = (
    "core_00_preamble.md",
    "core_01_a_values_principles.md",
    "core_01_b_interaction_interpretation.md",
    "core_01_c_stewardship_capacity_principles.md",
    "core_02_definition_structure.md",
    "core_03_definition_integrity.md",
    "core_04_burden_traceability_verification.md",
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
    "core_07_functional_independence_segregation_of_duties.md",
    "core_08_a_system_alignment_certification_evaluation.md",
    "core_08_b_system_alignment_certification_record_process.md",
    "core_08_system_alignment_certification.md",
    "core_09_standing_assessment.md",
    "core_10_standing_integration.md",
    "core_11_a_misconduct_designation.md",
    "core_11_b_misconduct_pattern_applications.md",
    "core_12_forum.md",
    "core_09-12_application_vignettes.md",
    "core_06_rights_part_a.md",
    "core_06_rights_part_b.md",
    "core_06_rights_part_c.md",
    "core_06_rights_part_d.md",
    "core_13_governance.md",
    "core_14_non_regression.md",
    "core_15_expansion_supremacy.md",
    "core_16_amendment_ratification.md",
    "core_17_incorporation.md",
)

ADOPTED_IMPLEMENTATION_WRAPPERS = (
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
)

ADOPTED_IMPLEMENTATION_SUBDIRS = (
    "corpus_joint_structure",
    "corpus_systems",
    "corpus_institutions",
    "corpus_forum",
)

SUPPORT_DOCS = ("doc_architecture.md", "README.md")


def adopted_implementation_subfiles(root: Path) -> list[str]:
    paths: list[str] = []
    for subdir in ADOPTED_IMPLEMENTATION_SUBDIRS:
        base = root / subdir
        if base.is_dir():
            paths.extend(
                path.relative_to(root).as_posix()
                for path in sorted(base.glob("*.md"))
                if path.is_file()
            )
    return paths


def binding_corpus_scope(root: Path, *, include_support_docs: bool = False) -> list[str]:
    scope = [*CORE_FILES, *ADOPTED_IMPLEMENTATION_WRAPPERS, *adopted_implementation_subfiles(root)]
    if include_support_docs:
        scope.extend(SUPPORT_DOCS)
    return scope


def source_markdown_files(root: Path) -> list[Path]:
    return [root / rel for rel in binding_corpus_scope(root) if (root / rel).exists()]


_REL_LINK_RE = re.compile(r"\]\((?!https?:|mailto:|#|/)([^)\s]+)\)")


def rebase_relative_links(text: str, src_dir: Path, out_dir: Path) -> str:
    """Rewrite relative Markdown link targets in text copied out of ``src_dir``.

    Generators lift cells verbatim from corpus files into
    doc_architecture/generated/, which sits at a different depth. A target
    that is correct beside its source resolves to the wrong path in the
    output, so each relative target is re-expressed against ``out_dir``.
    """

    def fix(match: "re.Match[str]") -> str:
        target = match.group(1)
        path, sep, fragment = target.partition("#")
        if not path:
            return match.group(0)
        rebased = os.path.relpath((src_dir / path).resolve(), out_dir)
        return f"]({rebased}{sep}{fragment})"

    return _REL_LINK_RE.sub(fix, text)
