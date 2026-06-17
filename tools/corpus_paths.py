"""Shared corpus path discovery for audits and AI index generation."""

from __future__ import annotations

from pathlib import Path


CORE_FILES = (
    "core_00_preamble.md",
    "core_01_a_values_principles.md",
    "core_01_b_stewardship_capacity_principles.md",
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
