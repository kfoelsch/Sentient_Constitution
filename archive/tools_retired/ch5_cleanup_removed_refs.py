#!/usr/bin/env python3
"""Clean up _REMOVED markers and handle removed cluster references.

For references to removed clusters, we have options:
1. Remove the "Cluster component:" line entirely
2. Replace with a note that the cluster was migrated

This script handles cleanup after the migration.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def clean_removed_markers(file_path: Path, dry_run: bool = False, verbose: bool = False) -> dict:
    """Clean up _REMOVED markers in a file."""

    text = file_path.read_text(encoding='utf-8')
    original_text = text
    changes = []

    # Fix 1: Clean up §3.X_REMOVED patterns -> restore to original §3.X for now
    # We'll handle removed clusters separately
    pattern1 = r'§(3\.\d+)_REMOVED'

    def clean_section_ref(match):
        old_num = match.group(1)
        changes.append(f"Cleaned: §{old_num}_REMOVED -> §{old_num}")
        return f"§{old_num}"

    text = re.sub(pattern1, clean_section_ref, text)

    # Fix 2: Clean up *cluster*REMOVED* patterns in markdown
    pattern2 = r'\*([^*]+)_REMOVED\*'

    def clean_cluster_title(match):
        title = match.group(1)
        changes.append(f"Cleaned cluster title: *{title}_REMOVED* -> *{title}*")
        return f"*{title}*"

    text = re.sub(pattern2, clean_cluster_title, text)

    # Fix 3: Fix specific case: "§3.3_REMOVED" in cluster description
    if "clusters begin at **§3.3**" in text:
        text = text.replace("clusters begin at **§3.3**", "clusters begin at **§3.1**")
        changes.append("Fixed: clusters begin at §3.3 -> §3.1")

    # Fix 4: Remove the "and are ordered alphabetically" if present with the old pattern
    text = re.sub(
        r'individual clusters begin at \*\*§3\.\d+\*\* and are ordered alphabetically',
        'individual clusters are ordered alphabetically',
        text
    )

    num_changes = len(changes)

    if not dry_run and text != original_text:
        file_path.write_text(text, encoding='utf-8')
        if verbose:
            print(f"Updated {file_path}")

    return {
        'file': str(file_path),
        'changes': changes,
        'num_changes': num_changes,
        'modified': text != original_text
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--files", nargs="+", required=True, help="Files to process")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen")
    p.add_argument("--verbose", "-v", action="store_true")
    args = p.parse_args()

    all_results = []

    for file_path_str in args.files:
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"Warning: File not found: {file_path}", file=sys.stderr)
            continue

        result = clean_removed_markers(file_path, dry_run=args.dry_run, verbose=args.verbose)
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
    print(f"Total cleanups: {total_changes}")

    if args.dry_run:
        print("(DRY RUN - no changes made)")


if __name__ == "__main__":
    main()
