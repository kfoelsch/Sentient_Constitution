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
import re
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

# Chapter One widgets shorten these Chapter Five labels; map display name → canonical term.
DAC_LABEL_ALIASES = {
    "materiality": "Materiality Determination",
    "foreseeability": "Foreseeability Diligence",
}
DETAILS_BLOCK_RE = re.compile(r"<details>[\s\S]*?</details>", re.IGNORECASE)
NON_OPERATIVE_SUMMARY_RE = re.compile(
    r"<summary>[\s\S]*?(?:non-operative|Reader guidance|Corpus placement)",
    re.IGNORECASE,
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
        self.expected_non_anchors: list[str] = []

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
        canon = self._canonical_term(term)
        return self.ch5_definitions.get(canon) if canon else None

    def build_backlinks(self):
        """Link definitions back to principles that reference them."""
        for principle_id, data in self.ch1_principles.items():
            resolved = []
            for term in data["anchors"]:
                canon = self._canonical_term(term)
                if canon is not None:
                    self.ch5_definitions[canon]["referenced_principles"].append(principle_id)
                    resolved.append(canon)
            data["anchors"] = resolved or data["anchors"]

    @staticmethod
    def _expects_dac_widget(principle_id: str) -> bool:
        """Preamble orients outward; §3 and §6 are roadmap preview parents.

        NAV-DAC-12: do not attach D/A/C widgets on Preamble (indexes to Chapter
        Five homes) or on Chapter One ### preview parents whose #### children
        already own the operative definitions. §3 and §6 name Safety and Truth
        as floors; §3.1–§3.4 and §6.1–§6.3 carry the working terms.
        """
        if principle_id.startswith("Preamble "):
            return False
        return principle_id not in {"3", "6"}

    def check_completeness(self):
        """Check that principles expected to invoke Def.* have D/A/C anchors."""
        for principle_id, data in self.ch1_principles.items():
            if not self._expects_dac_widget(principle_id):
                continue
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

    @staticmethod
    def _strip_non_operative_details(text: str) -> str:
        """Drop reader-guidance / corpus-placement widgets; keep Trace and D/A/C."""

        def keep_or_drop(match: re.Match[str]) -> str:
            block = match.group(0)
            return "" if NON_OPERATIVE_SUMMARY_RE.search(block) else block

        return DETAILS_BLOCK_RE.sub(keep_or_drop, text)

    def _operative_ch1_invocations(self) -> set[str]:
        """Chapter Five terms Chapter One actually uses at principle layer.

        Preamble and §3/§6 preview parents do not carry D/A/C widgets. Non-operative
        reader-guidance indexes are not invocations (NAV-DAC-12).
        """
        invoked: set[str] = set()
        for record in collect_ch1_principles(self.repo_root):
            if not self._expects_dac_widget(record.section):
                continue
            text = self._strip_non_operative_details(record.body)
            for term in [*extract_ch5_term_cites(text), *record.dac_terms]:
                canon = self._canonical_term(term)
                if canon:
                    invoked.add(canon)
        return invoked

    def check_coverage(self):
        """Flag unexpected orphans and unreferenced principles.

        Cluster heads, Preamble-only aims, and Chapter Five leaves that Chapter One
        never operatively invokes are expected non-anchors, not coverage gaps
        (NAV-DAC-12 roadmap exclusion).
        """
        invoked = self._operative_ch1_invocations()
        self.expected_non_anchors = []
        for term, data in self.ch5_definitions.items():
            if data["referenced_principles"]:
                continue
            if self._is_cluster_head(term) or term not in invoked:
                self.expected_non_anchors.append(term)
                continue
            self.coverage_gaps.append({
                "type": "orphan_definition",
                "term": term,
                "part": data["category"],
            })

        for principle_id, data in self.ch1_principles.items():
            if not self._expects_dac_widget(principle_id):
                continue
            if not data["anchors"]:
                self.coverage_gaps.append({
                    "type": "unreferenced_principle",
                    "principle": principle_id,
                    "title": data["title"],
                })

    @staticmethod
    def _is_cluster_head(term: str) -> bool:
        """Cluster-head titles are not Chapter One working terms (NAV-DAC-12)."""
        return bool(re.match(r"^Def\.[OPACI]\d+\s", term)) or "cluster head" in term.casefold()

    def _canonical_term(self, term: str) -> str | None:
        if term in self.ch5_definitions:
            return term
        folded = term.casefold()
        alias = DAC_LABEL_ALIASES.get(folded)
        if alias and alias in self.ch5_definitions:
            return alias
        for label in self.ch5_definitions:
            if label.casefold() == folded:
                return label
        return None

    def check_cluster_integrity(self):
        """Flag Def.Xn leaves invoked in a principle body but missing from its D/A/C widget.

        Cluster-head titles are excluded. Leaves that Chapter One never invokes remain
        coverage orphans, not segmentation findings (NAV-DAC-12 roadmap exclusion).
        """
        clusters: dict[str, list[str]] = {}
        for term, data in self.ch5_definitions.items():
            cluster_id = data.get("cluster_id")
            if not cluster_id or self._is_cluster_head(term):
                continue
            if data["category"] not in {"dependent_cluster", "semi_independent"}:
                continue
            clusters.setdefault(cluster_id, []).append(term)

        bodies = {
            record.section: self._strip_non_operative_details(record.body)
            for record in collect_ch1_principles(self.repo_root)
        }
        for principle_id, data in self.ch1_principles.items():
            dac = {
                canon
                for term in data["anchors"]
                if (canon := self._canonical_term(term)) is not None
            }
            body = {
                canon
                for term in extract_ch5_term_cites(bodies.get(principle_id, ""))
                if (canon := self._canonical_term(term)) is not None
            }
            for cluster_id, members in clusters.items():
                dac_in = [term for term in members if term in dac]
                if not dac_in:
                    continue
                missing = [term for term in members if term in body and term not in dac]
                if missing:
                    self.cluster_gaps.append({
                        "cluster": cluster_id,
                        "principle": principle_id,
                        "all_terms": members,
                        "referenced_terms": dac_in,
                        "missing_terms": missing,
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

        expected = {
            pid: data
            for pid, data in self.ch1_principles.items()
            if self._expects_dac_widget(pid)
        }
        total_principles = len(expected)
        indexed_principles = len(self.ch1_principles)
        anchored_principles = sum(1 for data in expected.values() if data["anchors"])
        complete_mappings = sum(
            1
            for data in expected.values()
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
                f"- **Coverage:** {complete_mappings}/{total_principles} principles that require D/A/C widgets have complete definition mappings\n"
            )
            f.write(
                f"- **Anchored principles:** {anchored_principles}/{total_principles} "
                f"({indexed_principles} indexed; Preamble and §3/§6 preview parents are excluded from completeness)\n"
            )
            f.write(f"- **Completeness Gaps:** {len(self.completeness_gaps)} principles missing anchors\n")
            f.write(
                f"- **Accuracy Gaps:** {len(self.accuracy_gaps)} incomplete guidepost components\n"
            )
            f.write(
                f"- **Coverage Gaps:** {len(self.coverage_gaps)} unexpected orphans/unreferenced items\n"
            )
            heads = sum(1 for term in self.expected_non_anchors if self._is_cluster_head(term))
            f.write(
                f"- **Expected non-anchors:** {len(self.expected_non_anchors)} "
                f"({heads} cluster heads; {len(self.expected_non_anchors) - heads} later-chapter or uninvoked leaves)\n"
            )
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
            elif self.expected_non_anchors:
                f.write("## Coverage Findings\n\n")
                f.write(
                    "No unexpected orphan definitions. Remaining Chapter Five terms without a "
                    "Chapter One D/A/C widget are expected non-anchors under NAV-DAC-12 "
                    "(cluster heads, Preamble-oriented aims, and later-chapter or uninvoked leaves).\n\n"
                )

            if self.cluster_gaps:
                f.write("## Cluster Integrity Findings\n\n")
                for gap in self.cluster_gaps:
                    principle = gap.get("principle", "")
                    loc = f"{gap['cluster']} on §{principle}" if principle else gap["cluster"]
                    f.write(
                        f"- **{loc}**: D/A/C cites {len(gap['referenced_terms'])} cluster leaves; "
                        f"body also invokes {', '.join(gap['missing_terms'])}\n"
                    )
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
                    "3. **Fix cluster segmentation** by adding D/A/C rows for Def.Xn leaves the same principle already invokes\n"
                )
            if self.coverage_gaps:
                f.write(
                    "4. **Review unexpected orphans** — add D/A/C rows where Chapter One operatively invokes the term\n"
                )
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
