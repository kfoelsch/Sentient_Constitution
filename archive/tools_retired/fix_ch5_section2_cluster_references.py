#!/usr/bin/env python3
"""Fix incorrect Section 3 cluster references in Section 2.

Section 2 contains "Cluster context" blocks that reference old cluster numbers
(3.3, 3.5, 3.15, etc.) that no longer exist after restructuring.

This script updates those references to reflect the current Section 3 structure
or removes them if the clusters were migrated to Section 2.
"""

import re
import sys
from pathlib import Path

# Mapping of OLD cluster numbers (referenced in Section 2) to disposition
# None = cluster no longer exists in Section 3 (was migrated or removed)
# "3.X" = new cluster number if remapped
OLD_CLUSTER_DISPOSITION = {
    # These clusters were migrated to Section 2 topic groups - remove Section 3 references
    '3.3': None,   # Accountability... - definitions are in Section 2
    '3.5': None,   # Assembly... - definitions are in Section 2
    '3.7': None,   # Bodily-Maintenance... - definitions are in Section 2
    '3.10': None,  # Consent... - definitions are in Section 2
    '3.15': None,  # Derived... - definitions are in Section 2
    '3.16': None,  # Ecological... - definitions are in Section 2
    '3.17': None,  # Emergency... - definitions are in Section 2
    '3.18': None,  # Family... - definitions are in Section 2
    '3.20': None,  # Governance... - definitions are in Section 2
    '3.21': None,  # Indigenous... - definitions are in Section 2
    '3.23': None,  # Materiality... - definitions are in Section 2
    '3.24': None,  # Movement... - definitions are in Section 2
    '3.25': None,  # Nondiscrimination... - definitions are in Section 2
    '3.27': None,  # Proportionality... - definitions are in Section 2
    '3.29': None,  # Protected Reporting... - definitions are in Section 2
    '3.30': None,  # Proxy Integrity... - definitions are in Section 2
    '3.31': None,  # Adjudication... - definitions are in Section 2
    '3.32': None,  # Capture... - definitions are in Section 2
    '3.36': None,  # Stakeholder Status... - definitions are in Section 2
    '3.37': None,  # Substantive Fairness... - definitions are in Section 2
}

# Current actual Section 3 clusters (for validation)
CURRENT_SECTION3_CLUSTERS = {
    '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', 
    '3.10', '3.11', '3.12', '3.13', '3.14'
}


def fix_section2_cluster_references(filepath: Path) -> tuple[str, list[dict]]:
    """Fix cluster references in Section 2 file.
    
    Returns (new_content, list_of_changes)
    """
    content = filepath.read_text()
    changes = []
    
    # Pattern to match Cluster context blocks referencing Section 3
    # Matches: **Cluster context:** This semi-independent topic group corresponds to [Chapter Five §3.XX *Title*](link)
    pattern = r'\*\*Cluster context:\*\* This semi-independent topic group corresponds to \[Chapter Five §(3\.\d+) \*([^*]+)\*\]\([^)]+\)[^\n]*\n'
    
    def replace_cluster_ref(match):
        old_num = match.group(1)
        old_title = match.group(2).strip()
        full_match = match.group(0)
        
        if old_num in OLD_CLUSTER_DISPOSITION:
            if OLD_CLUSTER_DISPOSITION[old_num] is None:
                # Cluster was migrated to Section 2 - update the language
                changes.append({
                    'old': f'§{old_num}',
                    'old_title': old_title,
                    'action': 'update_to_semi_independent',
                    'new_text': None  # Will be replaced with updated language
                })
                # Replace with language indicating this is now a semi-independent topic group
                # that corresponds to joint invocation requirements without referencing non-existent cluster
                new_text = f'**Cluster context:** This semi-independent topic group provides the canonical O/E/C home for these definitions. Joint invocation discipline applies where indicated in individual entry traces.\n'
                return new_text
            else:
                # Remapped to new cluster number
                new_num = OLD_CLUSTER_DISPOSITION[old_num]
                changes.append({
                    'old': f'§{old_num}',
                    'new': f'§{new_num}',
                    'action': 'remap'
                })
                return full_match.replace(f'§{old_num}', f'§{new_num}')
        elif old_num in CURRENT_SECTION3_CLUSTERS:
            # Valid reference - keep it
            return full_match
        else:
            # Unknown cluster number
            changes.append({
                'old': f'§{old_num}',
                'action': 'unknown',
                'warning': f'Cluster {old_num} not found in disposition mapping'
            })
            return full_match
    
    new_content = re.sub(pattern, replace_cluster_ref, content)
    
    # Also handle secondary references within the same paragraph
    # Pattern for "Chapter Five §3.XX" without the full link
    secondary_pattern = r'Chapter Five §(3\.\d+)'
    
    def replace_secondary_ref(match):
        old_num = match.group(1)
        if old_num in OLD_CLUSTER_DISPOSITION and OLD_CLUSTER_DISPOSITION[old_num] is None:
            # Remove the reference to non-existent cluster
            return 'the dependent cluster'
        return match.group(0)
    
    new_content = re.sub(secondary_pattern, replace_secondary_ref, new_content)
    
    return new_content, changes


def main():
    section2_file = Path('core_05-05_definitions_b_semi_independent.md')
    
    if not section2_file.exists():
        print(f"ERROR: {section2_file} not found")
        sys.exit(1)
    
    print("=" * 70)
    print("FIXING SECTION 2 CLUSTER REFERENCES")
    print("=" * 70)
    print()
    
    new_content, changes = fix_section2_cluster_references(section2_file)
    
    print(f"Proposed changes: {len(changes)}")
    print()
    
    for change in changes:
        if change['action'] == 'update_to_semi_independent':
            print(f"  • Remove reference to {change['old']} '{change['old_title'][:50]}...'")
            print(f"    -> Update to indicate semi-independent status (no Section 3 cluster)")
        elif change['action'] == 'remap':
            print(f"  • Remap {change['old']} -> {change['new']}")
        elif change['action'] == 'unknown':
            print(f"  ⚠ {change['warning']}")
    
    print()
    
    if changes:
        response = input("Apply these changes? (yes/no): ")
        if response.lower() in ('yes', 'y'):
            backup_file = section2_file.with_suffix('.md.backup')
            section2_file.rename(backup_file)
            section2_file.write_text(new_content)
            print(f"✓ Changes applied. Backup saved to {backup_file.name}")
        else:
            print("Changes cancelled.")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
