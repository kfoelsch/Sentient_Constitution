#!/usr/bin/env python3
"""
Chapter 1 ↔ Chapter 5 Alignment Audit Script

This script verifies that all Chapter 1 principles have explicit, complete definition anchors in Chapter 5,
with proper O/E/C components and no segmentation of dependent clusters.

Usage: python ch1_ch5_alignment_audit.py [--output-dir /path/to/evidence]

Outputs:
- alignment_report.md: Executive summary, gap findings, remediation roadmap
- traceability_matrix.csv: Bidirectional mapping table
- audit_log.json: Detailed gap data for automation
"""

import re
import json
import csv
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class AlignmentAuditor:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.ch1_files = [
            repo_root / "core_00_preamble.md",
            repo_root / "core_01_a_values_principles.md",
            repo_root / "core_01_b_interaction_interpretation.md",
            repo_root / "core_01_c_stewardship_capacity_principles.md",
        ]
        self.ch5_files = [repo_root / name for name in (
            "core_05-05_definitions_a_independent.md",
            "core_05o_oversight_definitions.md",
            "core_05p_participation_definitions.md",
            "core_05a_accountability_definitions.md",
            "core_05c_continuity_definitions.md",
            "core_05i_integrative_definitions.md",
        )]
        
        # Extracted data
        self.ch1_principles = {}  # principle_id -> {title, anchors: [term, ...]}
        self.ch5_definitions = {}  # term -> {part, cluster_id, has_o, has_e, has_c, referenced_principles: []}
        
        # Gap tracking
        self.completeness_gaps = []  # Principles missing anchors
        self.accuracy_gaps = []      # Incomplete O/E/C in referenced definitions
        self.coverage_gaps = []      # Orphan definitions + unreferenced principles
        self.cluster_gaps = []       # Segmented dependent clusters
        
    def extract_ch1_principles(self):
        """Parse Chapter 1 for principles and their definition anchors."""
        content = "\n".join(
            path.read_text() for path in self.ch1_files if path.is_file()
        )
        
        # Find all principle sections
        principle_pattern = r'^### (\d+(?:\.\d+)*)\. (.+)$'
        anchor_pattern = r'- \[([^\]]+)\]\([^)]+\) · \[O\]\([^)]+\) · \[E\]\([^)]+\) · \[C\]\([^)]+\)'
        
        current_principle = None
        for line in content.split('\n'):
            # New principle
            match = re.match(principle_pattern, line)
            if match:
                principle_id = match.group(1)
                title = match.group(2)
                current_principle = principle_id
                self.ch1_principles[principle_id] = {'title': title, 'anchors': []}
                continue
                
            # Anchors for current principle
            if current_principle and 'Definitions · Evaluation · Compliance' in line:
                # Look for anchors in following lines
                continue
            elif current_principle and line.strip().startswith('- ['):
                match = re.match(anchor_pattern, line.strip())
                if match:
                    term = match.group(1)
                    self.ch1_principles[current_principle]['anchors'].append(term)
    
    def extract_ch5_definitions(self):
        """Parse Chapter 5 files for definitions and O/E/C status."""
        for ch5_file in self.ch5_files:
            content = ch5_file.read_text()
            
            # Determine part
            if 'a_independent' in str(ch5_file):
                part = 'A'
            elif 'b_semi_independent' in str(ch5_file):
                part = 'B'
            else:
                part = 'C'
            
            # Find definition sections
            lines = content.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i]
                
                # Definition header
                if line.startswith('#### ') and not line.startswith('#### Reader-friendly'):
                    term = line[5:].strip()
                    if term and term[0].isupper():
                        # Extract cluster info from trace block
                        cluster_id = None
                        has_o = has_e = has_c = False
                        
                        # Look for trace block
                        j = i + 1
                        while j < len(lines) and not lines[j].startswith('#### '):
                            if 'Cluster component:' in lines[j]:
                                # Extract cluster ID
                                cluster_match = re.search(r'Chapter Five §(\d+\.\d+)', lines[j])
                                if cluster_match:
                                    cluster_id = cluster_match.group(1)
                            elif '- O:' in lines[j]:
                                has_o = True
                            elif '- E:' in lines[j]:
                                has_e = True
                            elif '- C:' in lines[j]:
                                has_c = True
                            j += 1
                        
                        self.ch5_definitions[term] = {
                            'part': part,
                            'cluster_id': cluster_id,
                            'has_o': has_o,
                            'has_e': has_e,
                            'has_c': has_c,
                            'referenced_principles': []
                        }
                        
                        i = j - 1  # Skip processed lines
                i += 1
    
    def build_backlinks(self):
        """Link definitions back to principles that reference them."""
        for principle_id, data in self.ch1_principles.items():
            for term in data['anchors']:
                if term in self.ch5_definitions:
                    self.ch5_definitions[term]['referenced_principles'].append(principle_id)
    
    def check_completeness(self):
        """Check that all principles have definition anchors."""
        for principle_id, data in self.ch1_principles.items():
            if not data['anchors']:
                self.completeness_gaps.append({
                    'principle': principle_id,
                    'title': data['title'],
                    'issue': 'No definition anchors found'
                })
    
    def check_accuracy(self):
        """Check that referenced definitions have complete O/E/C."""
        for principle_id, data in self.ch1_principles.items():
            for term in data['anchors']:
                if term in self.ch5_definitions:
                    def_data = self.ch5_definitions[term]
                    if not (def_data['has_o'] and def_data['has_e'] and def_data['has_c']):
                        missing = []
                        if not def_data['has_o']: missing.append('O')
                        if not def_data['has_e']: missing.append('E') 
                        if not def_data['has_c']: missing.append('C')
                        self.accuracy_gaps.append({
                            'principle': principle_id,
                            'definition': term,
                            'missing_components': missing
                        })
    
    def check_coverage(self):
        """Find orphan definitions and unreferenced principles."""
        # Orphan definitions
        for term, data in self.ch5_definitions.items():
            if not data['referenced_principles']:
                self.coverage_gaps.append({
                    'type': 'orphan_definition',
                    'term': term,
                    'part': data['part']
                })
        
        # Unreferenced principles (principles with no anchors)
        for principle_id, data in self.ch1_principles.items():
            if not data['anchors']:
                self.coverage_gaps.append({
                    'type': 'unreferenced_principle',
                    'principle': principle_id,
                    'title': data['title']
                })
    
    def check_cluster_integrity(self):
        """Check for segmentation of dependent clusters."""
        # Group definitions by cluster
        clusters = {}
        for term, data in self.ch5_definitions.items():
            if data['part'] == 'C' and data['cluster_id']:
                if data['cluster_id'] not in clusters:
                    clusters[data['cluster_id']] = []
                clusters[data['cluster_id']].append(term)
        
        # Check each cluster
        for cluster_id, terms in clusters.items():
            referenced_terms = [t for t in terms if self.ch5_definitions[t]['referenced_principles']]
            if referenced_terms and len(referenced_terms) < len(terms):
                # Partial reference - potential segmentation
                self.cluster_gaps.append({
                    'cluster': cluster_id,
                    'all_terms': terms,
                    'referenced_terms': referenced_terms,
                    'missing_terms': [t for t in terms if t not in referenced_terms]
                })
    
    def run_audit(self):
        """Run all checks."""
        self.extract_ch1_principles()
        self.extract_ch5_definitions()
        self.build_backlinks()
        
        self.check_completeness()
        self.check_accuracy()
        self.check_coverage()
        self.check_cluster_integrity()
    
    def generate_report(self, output_dir: Path):
        """Generate alignment report."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        report_file = output_dir / f"ch1_ch5_alignment_report_{timestamp}.md"
        
        # Calculate metrics
        total_principles = len(self.ch1_principles)
        anchored_principles = sum(1 for p in self.ch1_principles.values() if p['anchors'])
        complete_mappings = sum(1 for p in self.ch1_principles.values() 
                              if p['anchors'] and all(
                                  term in self.ch5_definitions and 
                                  self.ch5_definitions[term]['has_o'] and 
                                  self.ch5_definitions[term]['has_e'] and 
                                  self.ch5_definitions[term]['has_c'] 
                                  for term in p['anchors']))
        
        with open(report_file, 'w') as f:
            f.write("# Chapter 1 ↔ Chapter 5 Alignment Audit Report\n\n")
            f.write(f"**Date:** {timestamp}\n\n")
            
            f.write("## Executive Summary\n\n")
            f.write(f"- **Coverage:** {complete_mappings}/{total_principles} principles have complete definition mappings\n")
            f.write(f"- **Completeness Gaps:** {len(self.completeness_gaps)} principles missing anchors\n")
            f.write(f"- **Accuracy Gaps:** {len(self.accuracy_gaps)} incomplete O/E/C components\n")
            f.write(f"- **Coverage Gaps:** {len(self.coverage_gaps)} orphans/unreferenced items\n")
            f.write(f"- **Cluster Integrity:** {len(self.cluster_gaps)} potential segmentations\n\n")
            
            # Detail sections
            if self.completeness_gaps:
                f.write("## Completeness Findings\n\n")
                for gap in self.completeness_gaps:
                    f.write(f"- **{gap['principle']}** ({gap['title']}): {gap['issue']}\n")
                f.write("\n")
            
            if self.accuracy_gaps:
                f.write("## Accuracy Findings\n\n")
                for gap in self.accuracy_gaps:
                    f.write(f"- **{gap['principle']}** → {gap['definition']}: Missing {', '.join(gap['missing_components'])}\n")
                f.write("\n")
            
            if self.coverage_gaps:
                f.write("## Coverage Findings\n\n")
                for gap in self.coverage_gaps:
                    if gap['type'] == 'orphan_definition':
                        f.write(f"- Orphan definition: **{gap['term']}** (Part {gap['part']})\n")
                    else:
                        f.write(f"- Unreferenced principle: **{gap['principle']}** ({gap['title']})\n")
                f.write("\n")
            
            if self.cluster_gaps:
                f.write("## Cluster Integrity Findings\n\n")
                for gap in self.cluster_gaps:
                    f.write(f"- **Cluster {gap['cluster']}**: Referenced {len(gap['referenced_terms'])}/{len(gap['all_terms'])} terms\n")
                    f.write(f"  - Missing: {', '.join(gap['missing_terms'])}\n")
                f.write("\n")
            
            f.write("## Remediation Roadmap\n\n")
            # Add prioritized remediation steps based on gaps
            if self.completeness_gaps:
                f.write("1. **Add missing anchors** to principles without definition references\n")
            if self.accuracy_gaps:
                f.write("2. **Complete O/E/C components** for referenced definitions\n")
            if self.cluster_gaps:
                f.write("3. **Fix cluster segmentation** by ensuring joint-invocation terms are referenced together\n")
            if self.coverage_gaps:
                f.write("4. **Review orphans** - confirm intentional or add principle anchors\n")
    
    def generate_matrix(self, output_dir: Path):
        """Generate traceability matrix CSV."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        matrix_file = output_dir / f"ch1_ch5_traceability_matrix_{timestamp}.csv"
        
        # Collect all unique terms
        all_terms = sorted(self.ch5_definitions.keys())
        
        with open(matrix_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Header
            header = ['Principle', 'Title'] + all_terms
            writer.writerow(header)
            
            # Rows
            for principle_id, data in sorted(self.ch1_principles.items()):
                row = [principle_id, data['title']]
                for term in all_terms:
                    if term in data['anchors']:
                        def_data = self.ch5_definitions[term]
                        status = '✓' if def_data['has_o'] and def_data['has_e'] and def_data['has_c'] else '⚠'
                        row.append(status)
                    else:
                        row.append('')
                writer.writerow(row)
    
    def save_audit_log(self, output_dir: Path):
        """Save detailed audit data as JSON."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        log_file = output_dir / f"ch1_ch5_audit_log_{timestamp}.json"
        
        audit_data = {
            'timestamp': timestamp,
            'ch1_principles': self.ch1_principles,
            'ch5_definitions': self.ch5_definitions,
            'gaps': {
                'completeness': self.completeness_gaps,
                'accuracy': self.accuracy_gaps,
                'coverage': self.coverage_gaps,
                'cluster_integrity': self.cluster_gaps
            }
        }
        
        with open(log_file, 'w') as f:
            json.dump(audit_data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Chapter 1 ↔ Chapter 5 Alignment Audit")
    parser.add_argument('--output-dir', type=Path, default=Path('evidence') / datetime.now().strftime('%Y-%m-%d'),
                       help="Output directory for audit artifacts")
    parser.add_argument('--repo-root', type=Path, default=Path('.'),
                       help="Repository root directory")
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Run audit
    auditor = AlignmentAuditor(args.repo_root)
    auditor.run_audit()
    
    # Generate outputs
    auditor.generate_report(args.output_dir)
    auditor.generate_matrix(args.output_dir)
    auditor.save_audit_log(args.output_dir)
    
    print(f"Audit complete. Outputs saved to {args.output_dir}")

if __name__ == '__main__':
    main()
