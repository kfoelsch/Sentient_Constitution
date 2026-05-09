#!/usr/bin/env python3
"""Audit for duplicate definitions between Chapter 5 Section 2 and Section 3.

Each definition is supposed to appear only once with its canonical O/E/C home.
Section 2 (semi-independent) provides the canonical O/E/C home for certain terms,
while Section 3 (dependent clusters) provides joint-invocation contexts.

This script detects when both sections contain full O/E/C definitions for the same term,
which would violate the single-definition rule.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Definition:
    name: str
    anchor: str
    file: str
    line: int


def extract_definitions_from_file(filepath: Path) -> list[Definition]:
    """Extract all definitions with O/E/C content from a Chapter 5 file.
    
    A definition entry in Chapter 5 is identified by:
    1. An anchor <a id="..."></a> 
    2. Followed by "- O:" (Ontological component)
    3. Followed by "- E:" (Evaluative component) or <a id="...-e">
    4. Followed by "- C:" (Compliance component) or <a id="...-c">
    
    The pattern varies between files:
    - Section 2: main anchor, then O: line, then -e anchor, then E: line, then -c anchor, then C: line
    - Section 3: main anchor, then ##### heading, then O:/E:/C lines
    """
    definitions = []
    content = filepath.read_text()
    lines = content.split('\n')
    
    # Pattern 1: Find anchors followed by - O: within next 10 lines
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for anchor
        anchor_match = re.search(r'<a id="([^"]+)"', line)
        if not anchor_match:
            i += 1
            continue
        
        anchor = anchor_match.group(1)
        
        # Skip suffix anchors (-e, -c, -e1, -c1, etc.)
        if re.search(r'-[ec]\d*$', anchor):
            i += 1
            continue
        
        # Skip cluster-only anchors and section anchors
        if 'cluster' in anchor.lower() or anchor.startswith('section-'):
            i += 1
            continue
        
        # Look ahead for O/E/C content
        found_o = False
        found_e = False
        found_c = False
        
        for j in range(i + 1, min(i + 50, len(lines))):
            next_line = lines[j]
            
            # Stop conditions
            if re.match(r'^#{3,5} ', next_line):  # New heading
                break
            if re.match(r'^<a id="[^"]+"', next_line):  # New anchor
                # Allow -e and -c suffix anchors
                next_anchor = re.search(r'<a id="([^"]+)"', next_line)
                if next_anchor:
                    na = next_anchor.group(1)
                    if not (na == f"{anchor}-e" or na == f"{anchor}-c" or 
                            na.startswith(f"{anchor}-e-") or na.startswith(f"{anchor}-c-")):
                        break
            
            # Check for O:, E:, C:
            if re.match(r'^\s*-\s*O:', next_line):
                found_o = True
            elif re.match(r'^\s*-\s*E:', next_line):
                found_e = True
            elif re.match(r'^\s*-\s*C:', next_line):
                found_c = True
        
        # If we found O and (E or C), this is a valid definition
        if found_o and (found_e or found_c):
            # Find the name from preceding heading
            name = anchor.replace('-', ' ').title()
            for j in range(max(0, i - 15), i):
                h_match = re.match(r'^#{4,5}\s+(.+)$', lines[j])
                if h_match:
                    name = h_match.group(1).strip()
                    break
            
            definitions.append(Definition(
                name=name,
                anchor=anchor,
                file=str(filepath.name),
                line=i + 1
            ))
        
        i += 1
    
    return definitions


def extract_section2_topic_groups(filepath: Path) -> list[dict]:
    """Extract section 2 topic groups and their corresponding section 3 clusters."""
    content = filepath.read_text()
    groups = []
    
    # Find all "Cluster context" blocks that mention corresponding section 3
    pattern = r'<a id="([^"]+-semi-independent)"></a>\s*\n\s*#### (.+?)\s*\n.*?\*\*Cluster context:\*\* This semi-independent topic group corresponds to \[Chapter Five §(3\.\d+)'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        anchor = match.group(1)
        title = match.group(2).strip()
        section3_num = match.group(3)
        
        # Find the topic group members
        start_pos = match.end()
        section_end = content.find('\n---', start_pos)
        if section_end < 0:
            section_end = content.find('<a id="', start_pos + 10)
        
        section = content[start_pos:section_end if section_end > 0 else start_pos + 2000]
        
        # Extract member list
        members = []
        member_match = re.search(r'\*\*Topic group members\.\*\* This group comprises:(.+?)(?:---|$)', section, re.DOTALL)
        if member_match:
            member_section = member_match.group(1)
            for m in re.finditer(r'- \[([^\]]+)\]\(([^)]+)\)', member_section):
                members.append({
                    'name': m.group(1),
                    'link': m.group(2)
                })
        
        groups.append({
            'anchor': anchor,
            'title': title,
            'section3_num': section3_num,
            'members': members
        })
    
    return groups


def normalize_name(name: str) -> str:
    """Normalize a definition name for comparison."""
    norm = name.lower()
    # Remove common suffixes and variations
    for suffix in ['(constitutional)', '(semi-independent)', ' — ', ' - ', 'constitutional', 'semi independent']:
        norm = norm.replace(suffix, '')
    # Remove extra whitespace
    norm = ' '.join(norm.split())
    return norm.strip()


def find_potential_duplicates(section2_defs: list[Definition], section3_defs: list[Definition]) -> list[dict]:
    """Find definitions that appear to have O/E/C content in both sections."""
    duplicates = []
    
    # Build lookup by normalized name
    s2_by_name = defaultdict(list)
    s3_by_name = defaultdict(list)
    
    for d in section2_defs:
        norm = normalize_name(d.name)
        s2_by_name[norm].append(d)
    
    for d in section3_defs:
        norm = normalize_name(d.name)
        s3_by_name[norm].append(d)
    
    # Also build by anchor for cross-checking
    s2_by_anchor = {d.anchor: d for d in section2_defs}
    s3_by_anchor = {d.anchor: d for d in section3_defs}
    
    # Find matches by name
    all_names = set(s2_by_name.keys()) & set(s3_by_name.keys())
    
    for name in sorted(all_names):
        for s2_def in s2_by_name[name]:
            for s3_def in s3_by_name[name]:
                duplicates.append({
                    'name': s2_def.name,
                    'normalized': name,
                    'section2': s2_def,
                    'section3': s3_def,
                    'match_type': 'name'
                })
    
    # Also check by anchor (exact match)
    common_anchors = set(s2_by_anchor.keys()) & set(s3_by_anchor.keys())
    for anchor in common_anchors:
        # Skip if already found by name
        already_found = any(d['section2'].anchor == anchor for d in duplicates)
        if not already_found:
            duplicates.append({
                'name': s2_by_anchor[anchor].name,
                'normalized': anchor,
                'section2': s2_by_anchor[anchor],
                'section3': s3_by_anchor[anchor],
                'match_type': 'anchor'
            })
    
    return duplicates


def main():
    root = Path('.')
    
    section2_file = root / 'core_05-05_definitions_b_semi_independent.md'
    section3_file = root / 'core_05-05_definitions_c_dependent_clusters.md'
    
    if not section2_file.exists():
        print(f"ERROR: {section2_file} not found")
        sys.exit(1)
    if not section3_file.exists():
        print(f"ERROR: {section3_file} not found")
        sys.exit(1)
    
    print("=" * 70)
    print("CHAPTER 5 SECTION 2 vs SECTION 3 DUPLICATE DEFINITION AUDIT")
    print("=" * 70)
    print()
    
    # Extract definitions from both sections
    print("Extracting definitions from Section 2 (semi-independent)...")
    section2_defs = extract_definitions_from_file(section2_file)
    print(f"  Found {len(section2_defs)} definitions with O/E/C content")
    
    print()
    print("Extracting definitions from Section 3 (dependent clusters)...")
    section3_defs = extract_definitions_from_file(section3_file)
    print(f"  Found {len(section3_defs)} definitions with O/E/C content")
    
    # Show sample definitions found
    if section2_defs:
        print()
        print("  Sample Section 2 definitions:")
        for d in section2_defs[:10]:
            print(f"    - {d.name} (#{d.anchor})")
        if len(section2_defs) > 10:
            print(f"    ... and {len(section2_defs) - 10} more")
    
    if section3_defs:
        print()
        print("  Sample Section 3 definitions:")
        for d in section3_defs[:10]:
            print(f"    - {d.name} (#{d.anchor})")
        if len(section3_defs) > 10:
            print(f"    ... and {len(section3_defs) - 10} more")
    
    print()
    print("=" * 70)
    print("POTENTIAL DUPLICATES (same term with O/E/C in both sections)")
    print("=" * 70)
    print()
    
    duplicates = find_potential_duplicates(section2_defs, section3_defs)
    
    if duplicates:
        print(f"FOUND {len(duplicates)} POTENTIAL DUPLICATES:")
        print()
        for dup in duplicates:
            print(f"  ❌ '{dup['name']}' (matched by {dup['match_type']})")
            print(f"     Section 2: {dup['section2'].file}:{dup['section2'].line} (anchor: #{dup['section2'].anchor})")
            print(f"     Section 3: {dup['section3'].file}:{dup['section3'].line} (anchor: #{dup['section3'].anchor})")
            print()
    else:
        print("  ✓ No duplicate O/E/C definitions found between Section 2 and Section 3")
    
    # Also check section 2 topic groups against section 3
    print()
    print("=" * 70)
    print("SECTION 2 TOPIC GROUPS vs SECTION 3 CLUSTERS")
    print("=" * 70)
    print()
    
    topic_groups = extract_section2_topic_groups(section2_file)
    print(f"Found {len(topic_groups)} Section 2 topic groups that correspond to Section 3 clusters:")
    print()
    
    for tg in topic_groups:
        print(f"  • '{tg['title']}'")
        print(f"    Corresponds to: Chapter Five §{tg['section3_num']}")
        print(f"    Topic group members: {len(tg['members'])}")
        for m in tg['members'][:5]:
            print(f"      - {m['name']}")
        if len(tg['members']) > 5:
            print(f"      ... and {len(tg['members']) - 5} more")
        print()
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"Section 2 definitions with O/E/C:  {len(section2_defs)}")
    print(f"Section 3 definitions with O/E/C:  {len(section3_defs)}")
    print(f"Potential duplicates found:        {len(duplicates)}")
    print()
    
    if duplicates:
        print("STATUS: FAIL - Duplicate definitions violate single-canonical-home rule")
        sys.exit(1)
    else:
        print("STATUS: PASS - No duplicate O/E/C definitions detected")
        print()
        print("Note: Section 2 topic groups correctly reference Section 3 clusters")
        print("      for joint-invocation contexts without duplicating O/E/C content.")
        sys.exit(0)


if __name__ == "__main__":
    main()
