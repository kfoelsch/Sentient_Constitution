"""Shared corpus path discovery for audits and AI index generation."""

from __future__ import annotations

import os
import re
from pathlib import Path


CORE_FILES = (
    "core_00.000_preamble.md",
    "core_01.000_constitutional_map.md",
    "core_02.000_values_principles.md",
    "core_02.010_values_principles_continuity_aim.md",
    "core_02.020_interaction_interpretation.md",
    "core_02.030_constitutional_interpretation.md",
    "core_02.040_stewardship_capacity_principles.md",
    "core_02.050_governance_incentive_application.md",
    "core_03.000_definitions_home.md",
    "core_05.000_charters.md",
    "core_06.000_functional_independence_separation_of_duties.md",
    "core_07.000_independent_bodies.md",
    "core_08.000_system_alignment_certification_evaluation.md",
    "core_09.000_system_alignment_certification_forum_process_outcomes.md",
    "core_10.000_system_alignment_certification_records_recertification.md",
    "core_11.000_institutional_alignment_certification_evaluation.md",
    "core_12.000_institutional_alignment_certification_forum_process_outcomes.md",
    "core_13.000_institutional_alignment_certification_records_recertification.md",
    "core_14.000_standing_assessment.md",
    "core_15.000_standing_measurement.md",
    "core_16.000_standing_integration.md",
    "core_17.000_contribution_consequences.md",
    "core_18.000_violation_consequences.md",
    "core_19.000_final_effect_restoration_enforcement.md",
    "core_20.000_misconduct_designation.md",
    "core_21.000_misconduct_pattern_applications.md",
    "core_22.000_forum.md",
    "core_23.000_forum_families_escalation_timeliness_support.md",
    "core_24.000_assemblies.md",
    "core_25.000_enforcement.md",
    "core_26.000_special_enforcement.md",
    "core_04.000_rights_part_a.md",
    "core_04.010_rights_part_b.md",
    "core_04.020_rights_part_c.md",
    "core_04.030_rights_part_d.md",
    "core_04.040_rights_part_e.md",
    "core_27.000_governance.md",
    "core_28.000_non_regression.md",
    "core_29.000_amendment_ratification.md",
    "core_30.000_expansion_supremacy.md",
    "core_31.000_incorporation.md",
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


SUBCORE_GLOB = "subcore_*.md"


def subcore_files(root: Path) -> list[str]:
    """Binding subcore files (TIER-PLACE-01): same force as the core, kept at the root."""
    return [path.name for path in sorted(root.glob(SUBCORE_GLOB)) if path.is_file()]


def binding_corpus_scope(root: Path, *, include_support_docs: bool = False) -> list[str]:
    scope = [
        *CORE_FILES,
        *subcore_files(root),
        *ADOPTED_IMPLEMENTATION_WRAPPERS,
        *adopted_implementation_subfiles(root),
    ]
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
