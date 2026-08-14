#!/usr/bin/env python3
"""
Chapter 1 ↔ Chapter 5 Alignment Audit Script

Verifies that Chapter 0/1 principles have explicit definition anchors in
Chapter Five, with complete O/M/A/C guideposts and no segmentation of
dependent clusters. Also records CJS-3 oDef clusters that apply each term.

Usage: python ch1_ch5_alignment_audit.py [--output-dir /path/to/evidence]

Outputs:
- ch1_ch5_alignment_report_*.md
- ch1_ch5_traceability_matrix_*.csv
- ch1_ch5_audit_log_*.json
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from definition_index import (  # noqa: E402
    collect_ch1_principles,
    collect_ch5_entries_with_apex,
    collect_cjs3_clusters,
    extract_ch5_term_cites,
)


class AlignmentAuditor:
    def __init__(self, repo_root: Path, timestamp: str | None = None):
        self.repo_root = Path(repo_root)
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d")
        self.ch1_principles = {}
        self.ch5_definitions = {}
        self.completeness_gaps = []
        self.accuracy_gaps = []
        self.coverage_gaps = []
        self.cluster_gaps = []

    def extract_ch1_principles(self):
        """Parse Preamble and Chapter One for principles and D/A/C anchors."""
        for record in collect_ch1_principles(self.repo_root):
            self.ch1_principles[record.section] = {
                "title": record.title,
                "file": record.file,
                "line": record.line,
                "anchors": list(record.dac_terms),
            }

    def extract_ch5_definitions(self):
        """Parse Chapter Five leaves and apex heads for guidepost status."""
        clusters = collect_cjs3_clusters(self.repo_root)
        odef_by_term: dict[str, list[str]] = {}
        for cluster in clusters:
            for term in extract_ch5_term_cites(cluster.body):
                odef_by_term.setdefault(term.casefold(), []).append(cluster.cluster_id)

        for entry in collect_ch5_entries_with_apex(self.repo_root):
            category = "apex" if entry.category in {"apex", "tetrad_apex"} else entry.category
            odef_clusters = sorted(set(odef_by_term.get(entry.term.casefold(), [])))
            self.ch5_definitions[entry.term] = {
                "part": category,
                "category": category,
                "cluster_id": entry.cluster_id,
                "source_file": entry.source_file,
                "anchor": entry.anchor,
                "has_o": entry.has_o,
                "has_e": entry.has_m,
                "has_m": entry.has_m,
                "has_a": entry.has_a,
                "has_c": entry.has_c,
                "referenced_principles": [],
                "odef_clusters": odef_clusters,
            }

    def _definition_for_term(self, term: str) -> dict | None:
        if term in self.ch5_definitions:
            return self.ch5_definitions[term]
        folded = term.casefold()
        for label, data in self.ch5_definitions.items():
            if label.casefold() == folded:
                return data
        return None

    def build_backlinks(self):
        """Link definitions back to principles that reference them."""
        for principle_id, data in self.ch1_principles.items():
            resolved = []
            for term in data["anchors"]:
                def_data = self._definition_for_term(term)
                if def_data is not None:
                    def_data["referenced_principles"].append(principle_id)
                    resolved.append(term)
            data["anchors"] = resolved or data["anchors"]

    def check_completeness(self):
        """Check that all principles have definition anchors."""
        for principle_id, data in self.ch1_principles.items():
            if not data["anchors"]:
                self.completeness_gaps.append({
                    "principle": principle_id,
                    "title": data["title"],
                    "issue": "No definition anchors found",
                })

    def check_accuracy(self):
        """Check that referenced definitions have complete guideposts."""
        for principle_id, data in self.ch1_principles.items():
            for term in data["anchors"]:
                def_data = self._definition_for_term(term)
                if not def_data:
                    self.accuracy_gaps.append({
                        "principle": principle_id,
                        "definition": term,
                        "missing_components": ["Chapter Five home"],
                    })
                    continue
                missing = []
                if not def_data["has_o"]:
                    missing.append("What it is")
                if not def_data["has_m"]:
                    missing.append("How to measure and assess")
                if not def_data["has_c"]:
                    missing.append("What must hold")
                if missing:
                    self.accuracy_gaps.append({
                        "principle": principle_id,
                        "definition": term,
                        "missing_components": missing,
                    })

    def check_coverage(self):
        """Find orphan definitions and unreferenced principles."""
        for term, data in self.ch5_definitions.items():
            if not data["referenced_principles"]:
                self.coverage_gaps.append({
                    "type": "orphan_definition",
                    "term": term,
                    "part": data["category"],
                })

        for principle_id, data in self.ch1_principles.items():
            if not data["anchors"]:
                self.coverage_gaps.append({
                    "type": "unreferenced_principle",
                    "principle": principle_id,
                    "title": data["title"],
                })

    def check_cluster_integrity(self):
        """Check for segmentation of dependent clusters."""
        clusters: dict[str, list[str]] = {}
        for term, data in self.ch5_definitions.items():
            cluster_id = data.get("cluster_id")
            if not cluster_id:
                continue
            if data["category"] not in {"dependent_cluster", "semi_independent"}:
                continue
            clusters.setdefault(cluster_id, []).append(term)

        for cluster_id, terms in clusters.items():
            referenced_terms = [
                term for term in terms if self.ch5_definitions[term]["referenced_principles"]
            ]
            if referenced_terms and len(referenced_terms) < len(terms):
                self.cluster_gaps.append({
                    "cluster": cluster_id,
                    "all_terms": terms,
                    "referenced_terms": referenced_terms,
                    "missing_terms": [term for term in terms if term not in referenced_terms],
                })

    def _guidepost_complete(self, def_data: dict) -> bool:
        return bool(def_data["has_o"] and def_data["has_m"] and def_data["has_c"])

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
        report_file = output_dir / f"ch1_ch5_alignment_report_{self.timestamp}.md"

        total_principles = len(self.ch1_principles)
        anchored_principles = sum(1 for p in self.ch1_principles.values() if p["anchors"])
        complete_mappings = sum(
            1
            for data in self.ch1_principles.values()
            if data["anchors"]
            and all(
                (def_data := self._definition_for_term(term)) is not None
                and self._guidepost_complete(def_data)
                for term in data["anchors"]
            )
        )
        odef_linked = sum(1 for data in self.ch5_definitions.values() if data["odef_clusters"])

        with open(report_file, "w", encoding="utf-8") as f:
            f.write("# Chapter 1 ↔ Chapter 5 Alignment Audit Report\n\n")
            f.write(f"**Date:** {self.timestamp}\n\n")
            f.write("**Workflow:** CH1_CH5_ALIGNMENT_CHECK\n\n")

            f.write("## Executive Summary\n\n")
            f.write(
                f"- **Coverage:** {complete_mappings}/{total_principles} principles have complete definition mappings\n"
            )
            f.write(f"- **Anchored principles:** {anchored_principles}/{total_principles}\n")
            f.write(f"- **Completeness Gaps:** {len(self.completeness_gaps)} principles missing anchors\n")
            f.write(
                f"- **Accuracy Gaps:** {len(self.accuracy_gaps)} incomplete guidepost components\n"
            )
            f.write(f"- **Coverage Gaps:** {len(self.coverage_gaps)} orphans/unreferenced items\n")
            f.write(f"- **Cluster Integrity:** {len(self.cluster_gaps)} potential segmentations\n")
            f.write(
                f"- **oDef backlinks:** {odef_linked}/{len(self.ch5_definitions)} Def.* terms cited from CJS-3\n\n"
            )

            if self.completeness_gaps:
                f.write("## Completeness Findings\n\n")
                for gap in self.completeness_gaps:
                    f.write(f"- **{gap['principle']}** ({gap['title']}): {gap['issue']}\n")
                f.write("\n")

            if self.accuracy_gaps:
                f.write("## Accuracy Findings\n\n")
                for gap in self.accuracy_gaps:
                    f.write(
                        f"- **{gap['principle']}** → {gap['definition']}: Missing {', '.join(gap['missing_components'])}\n"
                    )
                f.write("\n")

            if self.coverage_gaps:
                f.write("## Coverage Findings\n\n")
                for gap in self.coverage_gaps:
                    if gap["type"] == "orphan_definition":
                        f.write(f"- Orphan definition: **{gap['term']}** ({gap['part']})\n")
                    else:
                        f.write(
                            f"- Unreferenced principle: **{gap['principle']}** ({gap['title']})\n"
                        )
                f.write("\n")

            if self.cluster_gaps:
                f.write("## Cluster Integrity Findings\n\n")
                for gap in self.cluster_gaps:
                    f.write(
                        f"- **{gap['cluster']}**: Referenced {len(gap['referenced_terms'])}/{len(gap['all_terms'])} terms\n"
                    )
                    f.write(f"  - Missing: {', '.join(gap['missing_terms'])}\n")
                f.write("\n")

            f.write("## oDef Application\n\n")
            f.write("| Def.* term | Category | Cluster | CJS-3 oDef clusters |\n")
            f.write("|---|---|---|---|\n")
            for term, data in sorted(self.ch5_definitions.items(), key=lambda item: item[0].casefold()):
                if not data["odef_clusters"]:
                    continue
                f.write(
                    f"| {term} | {data['category']} | {data['cluster_id'] or '—'} | {', '.join(data['odef_clusters'])} |\n"
                )
            f.write("\n")

            f.write("## Remediation Roadmap\n\n")
            if self.completeness_gaps:
                f.write("1. **Add missing anchors** to principles without definition references\n")
            if self.accuracy_gaps:
                f.write(
                    "2. **Complete guidepost components** (**What it is** / **How to measure and assess** / **What must hold**) for referenced definitions\n"
                )
            if self.cluster_gaps:
                f.write(
                    "3. **Fix cluster segmentation** by ensuring jointly invoked Def.Xn terms are referenced together\n"
                )
            if self.coverage_gaps:
                f.write("4. **Review orphans** — confirm intentional or add principle anchors\n")
            f.write(
                "5. Semantic adequacy of principle ↔ definition mapping remains a manual-review item.\n"
            )

    def generate_matrix(self, output_dir: Path):
        """Generate traceability matrix CSV."""
        matrix_file = output_dir / f"ch1_ch5_traceability_matrix_{self.timestamp}.csv"
        all_terms = sorted(self.ch5_definitions.keys(), key=str.casefold)

        with open(matrix_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Principle", "Title"] + all_terms)
            for principle_id, data in sorted(self.ch1_principles.items()):
                row = [principle_id, data["title"]]
                anchors = {term.casefold() for term in data["anchors"]}
                for term in all_terms:
                    if term.casefold() in anchors:
                        def_data = self.ch5_definitions[term]
                        row.append("✓" if self._guidepost_complete(def_data) else "⚠")
                    else:
                        row.append("")
                writer.writerow(row)

    def save_audit_log(self, output_dir: Path):
        """Save detailed audit data as JSON."""
        log_file = output_dir / f"ch1_ch5_audit_log_{self.timestamp}.json"
        audit_data = {
            "timestamp": self.timestamp,
            "workflow": "CH1_CH5_ALIGNMENT_CHECK",
            "ch1_principles": self.ch1_principles,
            "ch5_definitions": self.ch5_definitions,
            "gaps": {
                "completeness": self.completeness_gaps,
                "accuracy": self.accuracy_gaps,
                "coverage": self.coverage_gaps,
                "cluster_integrity": self.cluster_gaps,
            },
        }
        log_file.write_text(json.dumps(audit_data, indent=2), encoding="utf-8")

    def write_outputs(self, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        self.generate_report(output_dir)
        self.generate_matrix(output_dir)
        self.save_audit_log(output_dir)


def main():
    parser = argparse.ArgumentParser(description="Chapter 1 ↔ Chapter 5 Alignment Audit")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("evidence") / datetime.now().strftime("%Y-%m-%d"),
        help="Output directory for audit artifacts",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Repository root directory",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Evidence date stamp, YYYY-MM-DD.",
    )

    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    auditor = AlignmentAuditor(args.repo_root, timestamp=args.date)
    auditor.run_audit()
    auditor.write_outputs(args.output_dir)

    print(f"Audit complete. Outputs saved to {args.output_dir}")


if __name__ == "__main__":
    main()
