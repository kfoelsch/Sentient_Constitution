#!/usr/bin/env python3
"""Check changed tracked files against the pre-chapter-numbering baseline.

Chapter-source prose has its dedicated proof. Planned policy, generated, and
tooling changes are listed separately; every other changed text file must
match the baseline after chapter references, links, anchors, Trace widgets,
and edition pins are normalized.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = "pre-chapter-numbering-2026-10-21"
PLANNED_EXACT = {
    "AGENTS.md", "CONTRIBUTING.md", "Makefile", "README.md", "START_HERE.md",
    "ANNOUNCEMENT.md", "llms.txt", "docs/index.md", "docs/corpus_index.md",
    "doc_architecture.md", "ai_corpus/AI_NAVIGATION_GUIDE.md",
    "ai_corpus/MAINTENANCE.md", "ai_corpus/README.md",
    "ai_corpus/visualization/dependency_map.mmd",
    "corpus_forum.md", "corpus_institutions.md", "corpus_joint_structure.md",
    "corpus_systems.md", "implementation/steward_owner_clock_index.json",
    "tools/architecture/chapter_numbers.json",
    "tools/architecture/chapter_crosswalk.json",
    "project/plans/corpus_chapter_numbering_migration_2026-10-20.md",
    "project/plans/chapter_numbering_phase2_worklist_2026-10-21.txt",
    "project/plans/ai_corpus_optimization_plan.md",
    "project/plans/announcement_readiness_2026-10-20.md",
    "project/reviews/announcement_interlocks_B04_2026-10-20.md",
    "implementation/adoption/MINIMUM_VIABLE_ADOPTER.md",
    "corpus_joint_structure/cjs_reader_guide.md",
    "implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md",
    "implementation/PRE_PUBLICATION_SPEC.md",
    "implementation/adoption/INSTITUTION_FOUNDATION_KIT.md",
    "project/plans/announcement_review_inventory_2026-10-20.md",
}
GENERATED_PREFIXES = (
    "ai_corpus/indexes/", "doc_architecture/generated/", "_pages_site/",
)


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True)


def intentional(path: str) -> str | None:
    if path in PLANNED_EXACT:
        return "policy, front door, wrapper, registry, or migration record"
    if path.startswith(GENERATED_PREFIXES):
        return "regenerated index, page output, or print artifact"
    if path.startswith("tools/"):
        return "migration support, audit, test, or resolver tooling"
    if path == "archive/renumber_ci_narrative.py":
        return "retired one-off renumber tool"
    return None


def load_baseline(root: Path, baseline: str, path: str) -> bytes | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"{baseline}:{path}"], cwd=root,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--baseline", default=DEFAULT_BASELINE)
    args = parser.parse_args()
    root = args.root.resolve()
    sys.path.insert(0, str(root / "tools"))
    import core_numbering_content_proof as source_proof
    import renumber_corpus_chapters as migration

    registry = json.loads(
        (root / "tools/architecture/chapter_numbers.json").read_text()
    )
    names = {row["destination_file"]: row["original_file"]
             for row in registry["chapters"]}
    _, shared = migration.id_map(registry)
    shared_lists = {
        (", ".join(destinations[:-1]) + ", and " + destinations[-1]
         if len(destinations) > 2 else " and ".join(destinations)): old
        for old, destinations in shared.items()
    }
    crosswalk = json.loads(
        (root / "tools/architecture/chapter_crosswalk.json").read_text()
    )
    section_map: dict[str, str] = {}
    for item in crosswalk.get("sections", []):
        legacy = item.get("legacy_section_id", "")
        if "." not in legacy:
            continue
        for current in (item.get("display_id", ""), item.get("machine_id", "")):
            if current:
                section_map[current] = legacy
    reverse_anchors: dict[str, set[str]] = defaultdict(set)
    for file_map in crosswalk.get("anchor_maps", []):
        for item in file_map.get("anchors", []):
            reverse_anchors[item["new_anchor"]].add(item["old_anchor"])
    unique_anchor_map = {
        new: next(iter(old)) for new, old in reverse_anchors.items()
        if len(old) == 1
    }

    def normalized(text: str) -> str:
        text = source_proof.normalized(text, names, shared_lists, section_map)
        text = re.sub(r"SC-Corpus-\d{4}\.\d{2}\.\d{2}",
                      "SC-Corpus-<EDITION>", text)
        text = re.sub(r"(SC-Corpus-<EDITION>[^\n]*?effective )\d{4}-\d{2}-\d{2}",
                      r"\1<DATE>", text)
        for new, old in sorted(unique_anchor_map.items(),
                               key=lambda item: -len(item[0])):
            text = text.replace(new, old)
        return text

    try:
        subprocess.run(["git", "rev-parse", "--verify", f"{args.baseline}^{{commit}}"],
                       cwd=root, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"baseline is not a local commit: {args.baseline}", file=sys.stderr)
        return 2

    changed = git(root, "diff", "--name-status", "--find-renames", args.baseline)
    planned: dict[str, list[str]] = defaultdict(list)
    mismatches: list[str] = []
    compared = 0
    skipped_binary = 0
    renames = 0
    for line in changed.splitlines():
        fields = line.split("\t")
        status = fields[0]
        if status.startswith("R"):
            old_path, current_path = fields[1], fields[2]
            renames += 1
        else:
            old_path = current_path = fields[1]

        if status == "D":
            # Chapter-file renames and the retired one-off are planned.
            chapter_old = {row["original_file"] for row in registry["chapters"]}
            if old_path in chapter_old or old_path == "tools/renumber_ci_narrative.py" or old_path in {
                "implementation/GOVERNANCE_DISCLOSURE_TEMPLATE_CI8_CI26.md",
                "implementation/ROLE_SEPARATION_MATRIX_CI3_CI12.md",
            }:
                planned["file rename or retired tool"].append(old_path)
            else:
                mismatches.append(f"unexpected deletion: {old_path}")
            continue

        reason = intentional(current_path)
        if reason:
            planned[reason].append(current_path)
            continue

        current = root / current_path
        baseline_bytes = load_baseline(root, args.baseline, old_path)
        if baseline_bytes is None or not current.is_file():
            mismatches.append(f"unclassified addition or rename: {current_path}")
            continue
        try:
            before = normalized(baseline_bytes.decode("utf-8"))
            after = normalized(current.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, OSError):
            skipped_binary += 1
            continue
        compared += 1
        if before != after:
            mismatches.append(f"content differs after inverse normalization: {current_path}")

    untracked = git(root, "ls-files", "--others", "--exclude-standard").splitlines()
    print(f"tracked changed paths: {len(changed.splitlines())}; renamed paths: {renames}")
    print(f"normalized content comparisons: {compared}; binary paths skipped: {skipped_binary}")
    for category, paths in sorted(planned.items()):
        print(f"planned {category}: {len(set(paths))} path(s)")
    print(f"untracked files outside baseline: {len(untracked)}")
    for path in untracked:
        if path.startswith(("core_", "corpus_")):
            continue
        print(f"  {path}")
    if mismatches:
        print(f"FAIL: {len(mismatches)} unclassified difference(s)")
        for item in mismatches:
            print(f"  {item}")
        return 1
    print("PASS: all tracked changes are planned or match after inverse normalization")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
