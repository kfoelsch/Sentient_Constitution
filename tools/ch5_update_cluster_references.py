#!/usr/bin/env python3
"""Update cross-references to Chapter 5 §3 clusters after renumbering.

This updates references in:
- definitions_c itself (cluster numbers in prose)
- definitions_b (cluster component references)
- Other core files that reference Chapter 5 §3 clusters
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Mapping of old cluster numbers to new ones
RENUMBER_MAP = {
    "3.1": "3.1",    # Meta rule - unchanged
    "3.2": "3.2",    # Meta rule - unchanged
    "3.3": None,     # Migrated/removed
    "3.4": "3.3",    # Animal Life
    "3.5": None,     # Migrated/removed
    "3.6": "3.4",    # Binding Stakeholder Choice
    "3.7": None,     # Migrated/removed
    "3.8": None,     # Migrated/removed
    "3.9": "3.5",    # Collective Harm Boundary
    "3.10": None,    # Migrated/removed
    "3.11": "3.6",   # Corpus/Authority
    "3.12": None,    # Migrated/removed
    "3.13": None,    # Migrated/removed
    "3.14": "3.7",   # Creative Work
    "3.15": None,    # Migrated/removed
    "3.16": None,    # Migrated/removed
    "3.17": None,    # Migrated/removed
    "3.18": None,    # Migrated/removed
    "3.19": "3.8",   # Forum Families
    "3.20": None,    # Migrated/removed
    "3.21": None,    # Migrated/removed
    "3.22": None,    # Migrated/removed
    "3.23": None,    # Migrated/removed
    "3.24": None,    # Migrated/removed
    "3.25": None,    # Migrated/removed
    "3.26": "3.9",   # Privacy
    "3.27": None,    # Migrated/removed
    "3.28": None,    # Migrated/removed
    "3.29": None,    # Migrated/removed
    "3.30": None,    # Migrated/removed
    "3.31": None,    # Migrated/removed
    "3.32": None,    # Migrated/removed
    "3.33": "3.10",  # Self-Determination
    "3.34": None,    # Migrated/removed
    "3.35": "3.11",  # Standing State
    "3.36": None,    # Migrated/removed
    "3.37": None,    # Migrated/removed
    "3.38": "3.12",  # Transparency
    "3.39": "3.13",  # Trust
    "3.40": "3.14",  # Truth
    "3.41": "3.15",  # Use of Force
    "3.42": "3.16",  # Voluntary Agency
}


def update_references_in_file(file_path: Path, dry_run: bool = False, verbose: bool = False) -> dict:
    """Update Chapter Five §3 cluster references in a file."""

    text = file_path.read_text(encoding='utf-8')
    original_text = text
    changes = []

    # Pattern 1: "Chapter Five §3.X" or "§3.X" references
    # Capture the section number
    pattern1 = r'(Chapter Five\s+)?§(3\.\d+)'

    def replace_section_ref(match):
        prefix = match.group(1) or ""
        old_num = match.group(2)

        if old_num in RENUMBER_MAP:
            new_num = RENUMBER_MAP[old_num]
            if new_num is None:
                # Cluster was removed - mark for review
                if verbose:
                    changes.append(f"REMOVED: {match.group(0)} -> [cluster removed]")
                return f"{prefix}§{old_num}_REMOVED"
            elif new_num != old_num:
                if verbose:
                    changes.append(f"{prefix}§{old_num} -> {prefix}§{new_num}")
                return f"{prefix}§{new_num}"
        return match.group(0)

    text = re.sub(pattern1, replace_section_ref, text)

    # Pattern 2: Cluster titles in markdown links that include section numbers
    # e.g., "[Chapter Five §3.33 *Self-Determination...*]"
    pattern2 = r'(Chapter Five\s+)?(§3\.\d+\s+\*[^*]+\*)'

    def replace_cluster_title_ref(match):
        prefix = match.group(1) or ""
        content = match.group(2)

        # Extract the section number
        num_match = re.match(r'§(3\.\d+)', content)
        if num_match:
            old_num = num_match.group(1)
            if old_num in RENUMBER_MAP:
                new_num = RENUMBER_MAP[old_num]
                if new_num is None:
                    if verbose:
                        changes.append(f"REMOVED cluster title: {old_num}")
                    return f"{prefix}§{old_num}_REMOVED*{content.split('*', 1)[1]}"
                elif new_num != old_num:
                    if verbose:
                        changes.append(f"Cluster title: §{old_num} -> §{new_num}")
                    return f"{prefix}§{new_num}{content[len(num_match.group(0)):]}"
        return match.group(0)

    text = re.sub(pattern2, replace_cluster_title_ref, text)

    # Pattern 3: "section 3" general references that mention starting cluster
    # Update "clusters begin at §3.3" to reflect new numbering
    if "clusters begin at **§3.3**" in text:
        text = text.replace("clusters begin at **§3.3**", "clusters begin at **§3.1**")
        changes.append("Updated: clusters begin at §3.3 -> §3.1")

    # Pattern 4: Update references that say "begin at 3.3 and are ordered alphabetically"
    # to remove the "begin at" part since we now have continuous numbering from 3.1
    text = re.sub(
        r'individual clusters begin at \*\*§3\.\d+\*\* and are ordered alphabetically',
        'individual clusters are ordered alphabetically',
        text
    )

    # Count changes
    num_changes = len(changes)

    if not dry_run and text != original_text:
        backup_path = file_path.with_suffix(file_path.suffix + '.backup_refs')
        file_path.rename(backup_path)
        file_path.write_text(text, encoding='utf-8')
        if verbose:
            print(f"Updated {file_path} (backup: {backup_path})")

    return {
        'file': str(file_path),
        'changes': changes,
        'num_changes': num_changes,
        'modified': text != original_text
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--files", nargs="+", default=[
        "core_05-05_definitions_c_dependent_clusters.md",
        "core_05-05_definitions_b_semi_independent.md"
    ], help="Files to process")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen")
    p.add_argument("--verbose", "-v", action="store_true")
    args = p.parse_args()

    all_results = []

    for file_path_str in args.files:
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"Warning: File not found: {file_path}", file=sys.stderr)
            continue

        result = update_references_in_file(file_path, dry_run=args.dry_run, verbose=args.verbose)
        all_results.append(result)

        if args.verbose and result['changes']:
            print(f"\n=== {file_path} ===")
            for change in result['changes']:
                print(f"  - {change}")

    # Summary
    total_changes = sum(r['num_changes'] for r in all_results)
    files_modified = sum(1 for r in all_results if r['modified'])

    print(f"\n=== SUMMARY ===")
    print(f"Files processed: {len(all_results)}")
    print(f"Files with changes: {files_modified}")
    print(f"Total reference updates: {total_changes}")

    if args.dry_run:
        print("(DRY RUN - no changes made)")


if __name__ == "__main__":
    main()
