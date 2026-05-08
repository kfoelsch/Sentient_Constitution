#!/usr/bin/env python3
"""Audit Chapter 5 §3 clusters to detect 'shell clusters' without local O/E/C member definitions.

A 'shell cluster' is a dependent cluster that:
1. Lists cluster members that all point to OTHER files (not local to the cluster)
2. Has no O/E/C (Ontological/Evaluative/Compliance) definition content for those members

Definition clusters should house their member definitions with full O/E/C content.
This script identifies clusters that violate this architectural principle.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Workspace root")
    p.add_argument("--file", default="core_05-05_definitions_c_dependent_clusters.md",
                  help="Path to the dependent clusters file")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    return p.parse_args()


def extract_clusters(text: str) -> list[dict]:
    """Extract all §3 clusters with their content."""
    clusters = []

    # Find section 3 start
    m3 = re.search(r"^### 3\.\s+Dependent", text, re.M)
    if not m3:
        return clusters

    sec3 = text[m3.start():]

    # Split into cluster blocks (starting with #### 3.N)
    # Pattern matches #### 3. followed by digits and space
    parts = re.split(r"(?=^#### 3\.\d+ )", sec3, flags=re.M)

    pat_heading = re.compile(r"^#### (3\.\d+)\s+(.+)$", re.M)

    for part in parts:
        hm = pat_heading.match(part)
        if not hm:
            continue

        cluster_num = hm.group(1)
        cluster_title = hm.group(2).strip()

        clusters.append({
            'num': cluster_num,
            'title': cluster_title,
            'content': part
        })

    return clusters


def extract_cluster_members(cluster_content: str) -> list[dict]:
    """Extract cluster member definitions from the cluster content.

    Returns list of dicts with 'name', 'slug', 'is_local' (bool), 'file'.
    """
    members = []

    # Find Cluster members section
    idx = cluster_content.find("**Cluster members.**")
    if idx < 0:
        return members

    rest = cluster_content[idx + len("**Cluster members.**"):]

    # Find end of cluster members (Read-with definitions or next major section)
    end_m = re.search(r"\n\*\*Read-with definitions\.\*\*|\n\*\*Joint invocation", rest)
    list_region = rest[:end_m.start()] if end_m else rest

    # Parse member entries: - [Name](#slug) or - [Name](file.md#slug)
    for line in list_region.splitlines():
        line = line.strip()
        if not line.startswith("- ["):
            continue

        # Extract link info
        # Match patterns like: [Name](#slug) or [Name](file.md#slug)
        match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
        if not match:
            continue

        name = match.group(1)
        link = match.group(2)

        if "#" in link:
            if ".md" in link:
                # External file reference: file.md#slug
                parts = link.split("#", 1)
                file_ref = parts[0]
                slug = parts[1] if len(parts) > 1 else ""
                is_local = False
            else:
                # Local anchor: #slug
                slug = link[1:]  # Remove leading #
                file_ref = ""
                is_local = True
        else:
            # Just a file reference without anchor
            file_ref = link
            slug = ""
            is_local = False

        members.append({
            'name': name,
            'slug': slug,
            'file': file_ref,
            'is_local': is_local,
            'raw_link': link
        })

    return members


def has_local_oec_definitions(cluster_content: str, member_slug: str) -> bool:
    """Check if a member has O/E/C definitions locally in the cluster content.

    Looks for patterns like:
    - <a id="slug"></a> followed by O:/E:/C: content
    - ##### Member Name with O/E/C subsections
    """+ member_slug
    """Check if a member has O/E/C definitions locally in the cluster content."""
    # Normalize slug for searching
    slug_base = member_slug.split('-')[0] if '-' in member_slug else member_slug

    # Look for anchor with this slug
    anchor_pattern = rf'<a id="{re.escape(member_slug)}"></a>'
    has_anchor = bool(re.search(anchor_pattern, cluster_content))

    if not has_anchor:
        # Also check for partial matches (e.g., slug-e, slug-c suffixes)
        anchor_pattern_alt = rf'<a id="{re.escape(member_slug)}-[a-z0-9\-]+?"></a>'
        has_anchor = bool(re.search(anchor_pattern_alt, cluster_content))

    if not has_anchor:
        return False

    # Find the content after this anchor
    anchor_match = re.search(rf'<a id="{re.escape(member_slug)}(?:-[a-z0-9\-]+?)?"></a>', cluster_content)
    if not anchor_match:
        return False

    # Get content from anchor to next major heading or end
    content_after = cluster_content[anchor_match.end():]

    # Check for O:, E:, or C: markers in the next ~500 chars (rough heuristic)
    # Look for patterns like "- O:", "- E:", "- C:" at start of lines
    oec_pattern = r'\n-\s*[OEC]:'
    next_section = content_after[:1500]

    return bool(re.search(oec_pattern, next_section))


def analyze_cluster(cluster: dict, full_text: str) -> dict:
    """Analyze a single cluster and determine if it's a 'shell' cluster."""
    content = cluster['content']
    members = extract_cluster_members(content)

    if not members:
        return {
            'cluster': cluster,
            'members': [],
            'is_shell': False,  # No members to evaluate
            'shell_reason': 'no_members',
            'external_count': 0,
            'local_count': 0,
            'local_with_oec': 0
        }

    external_members = []
    local_members = []
    local_with_oec = []

    for member in members:
        if member['is_local']:
            local_members.append(member)
            # Check if this local member has O/E/C content
            if has_local_oec_definitions(content, member['slug']):
                local_with_oec.append(member)
        else:
            external_members.append(member)

    # Determine if this is a shell cluster
    # A shell cluster has all members pointing externally (no local O/E/C)
    is_shell = len(local_members) == 0 and len(external_members) > 0

    # Also flag if it has local anchors but no O/E/C content
    has_local_anchors_but_no_oec = len(local_members) > 0 and len(local_with_oec) == 0

    return {
        'cluster': cluster,
        'members': members,
        'is_shell': is_shell,
        'has_local_anchors_but_no_oec': has_local_anchors_but_no_oec,
        'external_members': external_members,
        'local_members': local_members,
        'local_with_oec': local_with_oec,
        'shell_reason': 'all_external' if is_shell else ('local_no_oec' if has_local_anchors_but_no_oec else 'none')
    }


def main() -> int:
    args = parse_args()
    path = Path(args.root) / args.file

    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    clusters = extract_clusters(text)

    print(f"=" * 70)
    print(f"CHAPTER 5 §3 CLUSTER CONTENT AUDIT")
    print(f"File: {args.file}")
    print(f"Total clusters found: {len(clusters)}")
    print(f"=" * 70)

    shell_clusters = []
    problematic_clusters = []

    for cluster in clusters:
        analysis = analyze_cluster(cluster, text)

        if analysis['is_shell']:
            shell_clusters.append(analysis)
        elif analysis.get('has_local_anchors_but_no_oec'):
            problematic_clusters.append(analysis)

    # Report shell clusters (all members external)
    print(f"\n{'=' * 70}")
    print(f"SHELL CLUSTERS: {len(shell_clusters)} clusters with NO local member definitions")
    print(f"{'=' * 70}")

    if shell_clusters:
        for analysis in shell_clusters:
            cluster = analysis['cluster']
            print(f"\n  §{cluster['num']} {cluster['title']}")
            print(f"  {'-' * 60}")
            print(f"  Cluster members (ALL point externally):")
            for member in analysis['members']:
                print(f"    - {member['name']} → {member['raw_link']}")
    else:
        print("  None found")

    # Report problematic clusters (local anchors but no O/E/C)
    print(f"\n{'=' * 70}")
    print(f"PROBLEMATIC CLUSTERS: {len(problematic_clusters)} clusters with local anchors but no O/E/C content")
    print(f"{'=' * 70}")

    if problematic_clusters:
        for analysis in problematic_clusters:
            cluster = analysis['cluster']
            print(f"\n  §{cluster['num']} {cluster['title']}")
            print(f"  {'-' * 60}")
            print(f"  Local members without O/E/C definitions:")
            for member in analysis['local_members']:
                print(f"    - {member['name']} (#{member['slug']})")
    else:
        print("  None found")

    # Summary statistics
    total_members = sum(len(analysis['members']) for analysis in
                       [analyze_cluster(c, text) for c in clusters])

    print(f"\n{'=' * 70}")
    print(f"SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total clusters analyzed: {len(clusters)}")
    print(f"Shell clusters (all external): {len(shell_clusters)}")
    print(f"Problematic clusters (no O/E/C): {len(problematic_clusters)}")
    print(f"Healthy clusters (local + O/E/C): {len(clusters) - len(shell_clusters) - len(problematic_clusters)}")

    if shell_clusters or problematic_clusters:
        print(f"\nRECOMMENDATION:")
        print(f"  Consider migrating member definitions from external files into these")
        print(f"  clusters, or restructuring to clarify the cluster architecture.")
        return 1

    print("\nPASS: All clusters have appropriate local member definitions with O/E/C content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
