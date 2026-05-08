#!/usr/bin/env python3
"""Migrate shell clusters from Section 3 to Section 2.

This script:
1. Removes specified clusters from definitions_c
2. Renumbers remaining clusters sequentially
3. Updates cross-references
4. Preserves backup
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Clusters to KEEP in Section 3 (exactly per restructuring plan - 12 clusters)
# Note: 3.31, 3.32, 3.34, 3.36, 3.37 are healthy but not in the plan's keep list
CLUSTERS_TO_KEEP = {
    "3.1", "3.2",    # Meta rules
    "3.4",           # Animal Life
    "3.6",           # Binding Stakeholder Choice
    "3.9",           # Collective Harm Boundary
    "3.11",          # Corpus/Authority (marginal but keeping)
    "3.14",          # Creative Work
    "3.19",          # Forum Families
    "3.26",          # Privacy (marginal - peer-level cluster head)
    "3.33",          # Self-Determination
    "3.35",          # Standing State (marginal - Chapter Six interface)
    "3.38",          # Transparency
    "3.39",          # Trust
    "3.40",          # Truth
    "3.41",          # Use of Force (keeping per plan)
    "3.42"           # Voluntary Agency
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--file", default="core_05-05_definitions_c_dependent_clusters.md",
                  help="Path to definitions_c file")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen")
    p.add_argument("--verbose", "-v", action="store_true")
    return p.parse_args()


def extract_cluster_boundaries(text: str) -> list[dict]:
    """Extract all cluster boundaries from the file."""
    clusters = []

    # Find all cluster headers #### 3.N
    pattern = r'^(#### (3\.\d+) (.+?))$\n'
    matches = list(re.finditer(pattern, text, re.MULTILINE))

    for i, match in enumerate(matches):
        cluster_num = match.group(2)
        cluster_title = match.group(3).strip()
        start_pos = match.start()

        # End is start of next cluster or end of file
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(text)

        clusters.append({
            'num': cluster_num,
            'title': cluster_title,
            'start': start_pos,
            'end': end_pos,
            'content': text[start_pos:end_pos]
        })

    return clusters


def create_renumbering_map(clusters: list[dict]) -> dict[str, str]:
    """Create a map of old cluster numbers to new numbers."""
    # Filter to clusters we're keeping
    kept_clusters = [c for c in clusters if c['num'] in CLUSTERS_TO_KEEP]

    # Sort by original number to maintain order
    kept_clusters.sort(key=lambda c: [int(x) for x in c['num'].split('.')])

    # Create renumbering map
    renumber_map = {}
    for new_idx, cluster in enumerate(kept_clusters, start=1):
        old_num = cluster['num']
        new_num = f"3.{new_idx}"
        renumber_map[old_num] = new_num

    return renumber_map


def remove_clusters_and_renumber(text: str, clusters: list[dict], renumber_map: dict,
                                  dry_run: bool = False, verbose: bool = False) -> str:
    """Remove migrated clusters and renumber remaining ones."""

    # Clusters to migrate = all clusters not in keep list
    cluster_nums = {c['num'] for c in clusters}
    clusters_to_migrate = cluster_nums - CLUSTERS_TO_KEEP

    if verbose:
        print("\n=== CLUSTER PROCESSING ===")
        print(f"Total clusters found: {len(clusters)}")
        print(f"Clusters to migrate (remove): {len(clusters_to_migrate)}")
        print(f"Clusters to keep: {len(CLUSTERS_TO_KEEP)}")
        print("\nRenumbering plan:")
        for old, new in sorted(renumber_map.items(), key=lambda x: x[0]):
            print(f"  {old} -> {new}")

    # Build new content
    # Keep everything before the first cluster
    first_cluster_start = min(c['start'] for c in clusters)
    new_text = text[:first_cluster_start]

    # Process clusters in order
    sorted_clusters = sorted(clusters, key=lambda c: c['start'])

    for cluster in sorted_clusters:
        old_num = cluster['num']

        if old_num in clusters_to_migrate:
            if verbose:
                print(f"\n[REMOVING] Cluster {old_num}: {cluster['title'][:50]}...")
            continue  # Skip this cluster (remove it)

        elif old_num in CLUSTERS_TO_KEEP:
            new_num = renumber_map.get(old_num, old_num)
            cluster_content = cluster['content']

            # Renumber the cluster header
            if old_num != new_num:
                if verbose:
                    print(f"\n[RENAMING] {old_num} -> {new_num}: {cluster['title'][:50]}...")

                # Replace the cluster number in the header
                old_header = f"#### {old_num} "
                new_header = f"#### {new_num} "
                cluster_content = cluster_content.replace(old_header, new_header, 1)

                # Also update anchor IDs if they reference the cluster number
                # Pattern: <a id="...-3-X-...">
                def replace_anchor_refs(match):
                    anchor = match.group(0)
                    # Replace old cluster number patterns in anchors
                    for old_n, new_n in renumber_map.items():
                        old_pattern = old_n.replace(".", "-")  # 3.4 -> 3-4
                        new_pattern = new_n.replace(".", "-")
                        anchor = anchor.replace(f'"{old_pattern}-', f'"{new_pattern}-')
                        anchor = anchor.replace(f'"{old_pattern}"', f'"{new_pattern}"')
                    return anchor

                cluster_content = re.sub(r'<a id="[^"]+"></a>', replace_anchor_refs, cluster_content)

            else:
                if verbose:
                    print(f"\n[KEEPING] {old_num}: {cluster['title'][:50]}...")

            new_text += cluster_content

        else:
            # Unknown cluster - keep it but warn
            if verbose:
                print(f"\n[WARNING] Unknown cluster {old_num} - keeping as-is")
            new_text += cluster['content']

    return new_text


def main():
    args = parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    text = file_path.read_text(encoding='utf-8')

    # Extract clusters
    clusters = extract_cluster_boundaries(text)

    if not clusters:
        print("No clusters found in file!")
        sys.exit(1)

    # Create renumbering map
    renumber_map = create_renumbering_map(clusters)

    # Process the file
    new_text = remove_clusters_and_renumber(
        text, clusters, renumber_map,
        dry_run=args.dry_run, verbose=args.verbose
    )

    if args.dry_run:
        print("\n=== DRY RUN - No changes made ===")
        print(f"Would remove {len(CLUSTERS_TO_MIGRATE)} clusters")
        print(f"Would keep {len([c for c in clusters if c['num'] in CLUSTERS_TO_KEEP])} clusters")
        print(f"Final cluster count would be: {len(renumber_map)}")
    else:
        # Write the modified file
        backup_path = file_path.with_suffix('.md.backup')
        file_path.rename(backup_path)
        file_path.write_text(new_text, encoding='utf-8')
        print(f"\n=== COMPLETE ===")
        print(f"Backup saved to: {backup_path}")
        print(f"Modified file: {file_path}")
        print(f"Removed {len(CLUSTERS_TO_MIGRATE)} clusters")
        print(f"Renumbered {len(renumber_map)} clusters (now 3.1 through 3.{len(renumber_map)})")


if __name__ == "__main__":
    main()
