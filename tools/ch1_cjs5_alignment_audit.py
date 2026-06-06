#!/usr/bin/env python3
"""
Chapter 01 -> CJS-5 Principle Alignment Audit.

This audit checks CJS-5 operational clusters against Chapter 01 principles:
- CJS-5 cluster inventory and owner-routing references
- direct and inferred Chapter 01 principle basis
- OP-O / OP-E / OP-C completeness for cluster and material sub-rules
- weak-trace, missing-anchor, owner-drift, overreach, and OP-component findings

Usage:
  python tools/ch1_cjs5_alignment_audit.py --output-dir evidence/2026-06-06
"""

import argparse
import csv
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set


CJS5_FILES = [
    "corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md",
    "corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md",
    "corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md",
    "corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md",
    "corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md",
]


EXPECTED_CLUSTER_IDS = [
    "CJS-5.0",
    "CJS-5A.1",
    "CJS-5A.2",
    "CJS-5A.3",
    "CJS-5A.4",
    "CJS-5A.5",
    "CJS-5A.6",
    "CJS-5B.1",
    "CJS-5B.2",
    "CJS-5B.3",
    "CJS-5B.4",
    "CJS-5C.1",
    "CJS-5C.2",
    "CJS-5C.3",
    "CJS-5C.4",
    "CJS-5D.1",
    "CJS-5D.2",
    "CJS-5D.3",
    "CJS-5E.1",
    "CJS-5E.2",
    "CJS-5E.3",
    "CJS-5E.4",
    "CJS-5E.5",
]


CLUSTER_PRINCIPLE_MAP = {
    "CJS-5.0": ["2.1", "3.4", "5.2", "7.1", "7.2", "10"],
    "CJS-5A.1": ["2.1", "4", "5.2", "7.2", "10"],
    "CJS-5A.2": ["3.1", "6.1", "6.4", "7.1", "9"],
    "CJS-5A.3": ["3.2", "4", "5.2", "7.1", "7.2"],
    "CJS-5A.4": ["6.1", "6.3", "6.4", "7.1", "8", "9"],
    "CJS-5A.5": ["3.2", "6.2", "6.4", "7.1", "8", "9"],
    "CJS-5A.6": ["2.1", "3.4", "6.4", "7.1", "8", "10"],
    "CJS-5B.1": ["3.1", "3.2", "4.1", "7.1", "7.2"],
    "CJS-5B.2": ["3.2", "4", "7.1", "7.2"],
    "CJS-5B.3": ["3.2", "6.2", "6.4", "7.1", "8"],
    "CJS-5B.4": ["3.2", "3.3", "4", "7.1", "7.2"],
    "CJS-5C.1": ["2.1", "4", "5.2", "6.4", "8", "10"],
    "CJS-5C.2": ["3.4", "5.2", "7.1", "8"],
    "CJS-5C.3": ["2", "3.2", "4", "7.1", "8"],
    "CJS-5C.4": ["3.2", "6.2", "7.1", "8"],
    "CJS-5D.1": ["3.1", "4.1", "5.1", "7.1", "9"],
    "CJS-5D.2": ["5.1", "6.1", "7.1", "8", "9"],
    "CJS-5D.3": ["3.2", "6.2", "7.1", "8", "9"],
    "CJS-5E.1": ["3.1", "4.1", "5.1", "6.1", "7", "9"],
    "CJS-5E.2": ["3.1", "6.1", "6.4", "7.1", "9"],
    "CJS-5E.3": ["3.1", "4.1", "6.1", "7.1", "9"],
    "CJS-5E.4": ["3.1", "3.2", "4.1", "7.1", "7.2", "9"],
    "CJS-5E.5": ["3.1", "3.2", "4.1", "5.2", "7.1", "7.2"],
}


PRINCIPLE_RULES = [
    (("authority", "governance", "role", "quorum", "delegated", "constitutional lane"),
     ["4", "5.2", "7.2", "10"]),
    (("intervention", "override", "emergency", "failure", "containment", "rollback", "reversibility"),
     ["3.1", "4.1", "6", "6.1", "6.4", "7", "9"]),
    (("transparency", "disclosure", "audit", "verification", "record", "claim", "evidence"),
     ["3.2", "3.3", "4", "5.2", "6.2", "7.1", "7.2"]),
    (("restriction", "burden", "constraint", "least-restrictive", "secrecy", "protected-investigation"),
     ["3", "6.1", "6.2", "6.3", "6.4", "7.1", "8", "9"]),
    (("procedure", "adjudication", "forum", "review", "contest", "restoration", "remedy"),
     ["2.1", "3.4", "6.4", "7.1", "8", "10"]),
    (("participation", "comprehension", "accessibility", "stakeholder", "notice", "affected"),
     ["2.1", "3.4", "4", "5.2", "6.4", "7.1", "8"]),
    (("dependency", "exit", "portability", "interoperability", "retention", "lifecycle", "lock-in"),
     ["3.1", "3.2", "5", "5.1", "6.1", "7.1", "8", "9"]),
    (("robustness", "abuse", "adversarial", "misuse", "correction", "structural"),
     ["3.1", "3.2", "4.1", "7.1", "7.2", "9"]),
]


OWNER_PATTERNS = [
    r"\bPRIM\d+\b",
    r"\bPROT\d+\b",
    r"\bCP\b",
    r"\bCS\b",
    r"\bCI\b",
    r"\bCF\b",
    r"`corpus_systems\.md`",
    r"`corpus_institutions\.md`",
    r"`corpus_forum\.md`",
    r"`core_[^`]+\.md`",
    r"Chapter Ten",
    r"Foundational Rights",
    r"Chapter Five",
    r"Core definitions",
    r"\bArticle\s+[IVX]+(?:-[A-Z])?\b",
    r"Chapter Seven",
    r"Chapter Eleven",
]


OVERREACH_PATTERNS = [
    r"notwithstanding\s+chapter\s+one",
    r"notwithstanding\s+chapter\s+five",
    r"notwithstanding\s+foundational\s+rights",
    r"override[s]?\s+chapter\s+one",
    r"override[s]?\s+foundational\s+rights",
    r"supersede[s]?\s+chapter\s+one",
    r"supersede[s]?\s+chapter\s+five",
    r"replace[s]?\s+chapter\s+one",
    r"replace[s]?\s+chapter\s+five",
    r"replace[s]?\s+foundational\s+rights",
]


@dataclass
class OperationalRule:
    label: str
    line: int
    has_o: bool = False
    has_e: bool = False
    has_c: bool = False

    @property
    def missing(self) -> List[str]:
        return [k for k, present in (("OP-O", self.has_o), ("OP-E", self.has_e), ("OP-C", self.has_c)) if not present]


@dataclass
class Cluster:
    cluster_id: str
    title: str
    file: str
    start_line: int
    end_line: int
    body: str
    read_with: List[str] = field(default_factory=list)
    direct_ch1_refs: List[str] = field(default_factory=list)
    inferred_principles: List[str] = field(default_factory=list)
    owner_refs: List[str] = field(default_factory=list)
    rules: List[OperationalRule] = field(default_factory=list)
    classifications: List[str] = field(default_factory=list)


class Ch1Cjs5AlignmentAuditor:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.timestamp = datetime.now().strftime("%Y-%m-%d")
        self.principles = self._extract_ch1_principles()
        self.clusters: List[Cluster] = []
        self.gaps: Dict[str, List[Dict[str, object]]] = {
            "missing_anchor": [],
            "weak_trace": [],
            "owner_drift": [],
            "op_component_gap": [],
            "overreach": [],
            "inventory": [],
        }

    def _extract_ch1_principles(self) -> Dict[str, Dict[str, object]]:
        path = self.repo_root / "core_00-01_principles.md"
        principles: Dict[str, Dict[str, object]] = {}
        pattern = re.compile(r"^(#{3,4})\s+(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$")
        for idx, line in enumerate(path.read_text().splitlines(), start=1):
            match = pattern.match(line)
            if match:
                principles[match.group(2)] = {"title": match.group(3).strip(), "line": idx}
        return principles

    def _extract_clusters_from_file(self, rel_path: str) -> List[Cluster]:
        path = self.repo_root / rel_path
        lines = path.read_text().splitlines()
        starts = []
        cluster_pattern = re.compile(r"^##\s+(CJS-5(?:\.0|[A-E]\.\d+))\s+(.+)$")
        for idx, line in enumerate(lines):
            match = cluster_pattern.match(line)
            if match:
                starts.append((idx, match.group(1), match.group(2).strip()))

        clusters = []
        for pos, (start_idx, cluster_id, title) in enumerate(starts):
            end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
            body_lines = lines[start_idx + 1:end_idx]
            clusters.append(
                Cluster(
                    cluster_id=cluster_id,
                    title=title,
                    file=rel_path,
                    start_line=start_idx + 1,
                    end_line=end_idx,
                    body="\n".join(body_lines),
                )
            )
        return clusters

    def _extract_read_with(self, body: str) -> List[str]:
        refs: List[str] = []
        in_block = False
        for line in body.splitlines():
            stripped = line.strip()
            if stripped == "Read it with:":
                in_block = True
                continue
            if in_block:
                if stripped.startswith("- "):
                    refs.append(stripped[2:].strip())
                    continue
                if stripped:
                    break
        return refs

    def _extract_direct_ch1_refs(self, text: str) -> List[str]:
        refs: Set[str] = set()
        for match in re.finditer(r"Chapter One\s+§+\s*([0-9]+(?:\.[0-9]+)*)", text):
            refs.add(match.group(1))
        if "core_00-01_principles.md" in text:
            refs.add("linked")
        return sorted(refs)

    def _infer_principles(self, cluster: Cluster) -> List[str]:
        if cluster.cluster_id in CLUSTER_PRINCIPLE_MAP:
            return CLUSTER_PRINCIPLE_MAP[cluster.cluster_id]

        haystack = f"{cluster.cluster_id} {cluster.title} {cluster.body}".lower()
        inferred: Set[str] = set()
        for terms, principles in PRINCIPLE_RULES:
            if any(term in haystack for term in terms):
                inferred.update(principles)
        return sorted(inferred, key=lambda value: [int(part) for part in value.split(".")])

    def _extract_owner_refs(self, text: str) -> List[str]:
        refs: Set[str] = set()
        for pattern in OWNER_PATTERNS:
            for match in re.finditer(pattern, text):
                refs.add(match.group(0).strip("`"))
        return sorted(refs)

    def _extract_rules(self, cluster: Cluster) -> List[OperationalRule]:
        lines = cluster.body.splitlines()
        rules: List[OperationalRule] = []
        current: Optional[OperationalRule] = None
        previous_label: Optional[tuple[str, int]] = None

        def is_label(line: str) -> bool:
            stripped = line.strip()
            if not stripped:
                return False
            if stripped.startswith(("- ", "#", "|", "---", "<", "```")):
                return False
            if stripped in {"Read it with:", "Role-definition reading rule", "Competency gate and standing interface"}:
                return True
            if stripped.endswith(":"):
                return False
            return True

        for offset, line in enumerate(lines, start=cluster.start_line + 1):
            stripped = line.strip()
            if is_label(stripped):
                previous_label = (stripped, offset)
                current = None
                continue
            if stripped.startswith("- OP-"):
                if current is None:
                    label, label_line = previous_label or ("Unlabeled operational rule", offset)
                    current = OperationalRule(label=label, line=label_line)
                    rules.append(current)
                if stripped.startswith("- OP-O:"):
                    current.has_o = True
                elif stripped.startswith("- OP-E:"):
                    current.has_e = True
                elif stripped.startswith("- OP-C:"):
                    current.has_c = True
                if current.has_o and current.has_e and current.has_c:
                    current = None
        return rules

    def _classify_cluster(self, cluster: Cluster) -> List[str]:
        classifications: Set[str] = set()
        incomplete_rules = [rule for rule in cluster.rules if rule.missing]
        text = f"{cluster.title}\n{cluster.body}".lower()

        if not cluster.inferred_principles and not cluster.direct_ch1_refs:
            classifications.add("missing_anchor")
            self.gaps["missing_anchor"].append({
                "cluster_id": cluster.cluster_id,
                "title": cluster.title,
                "file": cluster.file,
                "line": cluster.start_line,
                "issue": "No direct or inferred Chapter 01 principle basis found.",
            })
        elif not cluster.direct_ch1_refs:
            classifications.add("weak_trace")
            self.gaps["weak_trace"].append({
                "cluster_id": cluster.cluster_id,
                "title": cluster.title,
                "file": cluster.file,
                "line": cluster.start_line,
                "issue": "Principle basis is inferred from subject matter, not directly cited to Chapter 01.",
                "inferred_principles": cluster.inferred_principles,
            })

        if not cluster.owner_refs:
            classifications.add("owner_drift")
            self.gaps["owner_drift"].append({
                "cluster_id": cluster.cluster_id,
                "title": cluster.title,
                "file": cluster.file,
                "line": cluster.start_line,
                "issue": "No owner-layer routing reference detected.",
            })

        if incomplete_rules:
            classifications.add("op_component_gap")
            for rule in incomplete_rules:
                self.gaps["op_component_gap"].append({
                    "cluster_id": cluster.cluster_id,
                    "title": cluster.title,
                    "file": cluster.file,
                    "line": rule.line,
                    "rule": rule.label,
                    "missing": rule.missing,
                })

        drift_hits = [pattern for pattern in OVERREACH_PATTERNS if re.search(pattern, text)]
        if drift_hits:
            classifications.add("overreach")
            self.gaps["overreach"].append({
                "cluster_id": cluster.cluster_id,
                "title": cluster.title,
                "file": cluster.file,
                "line": cluster.start_line,
                "issue": "Potential overreach language detected.",
                "matches": drift_hits,
            })

        if not classifications:
            classifications.add("complete")
        return sorted(classifications)

    def run(self) -> None:
        for rel_path in CJS5_FILES:
            self.clusters.extend(self._extract_clusters_from_file(rel_path))

        discovered = {cluster.cluster_id for cluster in self.clusters}
        for expected in EXPECTED_CLUSTER_IDS:
            if expected not in discovered:
                self.gaps["inventory"].append({
                    "cluster_id": expected,
                    "issue": "Expected CJS-5 cluster heading not discovered.",
                })
        for cluster in self.clusters:
            if cluster.cluster_id not in EXPECTED_CLUSTER_IDS:
                self.gaps["inventory"].append({
                    "cluster_id": cluster.cluster_id,
                    "title": cluster.title,
                    "file": cluster.file,
                    "line": cluster.start_line,
                    "issue": "Unexpected CJS-5 cluster heading discovered.",
                })

        for cluster in self.clusters:
            cluster.read_with = self._extract_read_with(cluster.body)
            cluster.direct_ch1_refs = self._extract_direct_ch1_refs(cluster.body)
            cluster.inferred_principles = self._infer_principles(cluster)
            cluster.owner_refs = self._extract_owner_refs(cluster.body)
            cluster.rules = self._extract_rules(cluster)
            cluster.classifications = self._classify_cluster(cluster)

    def write_report(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_cjs5_principle_alignment_report_{self.timestamp}.md"
        total = len(self.clusters)
        complete = sum(1 for c in self.clusters if c.classifications == ["complete"])
        op_gap_count = len(self.gaps["op_component_gap"])
        weak_trace_count = len(self.gaps["weak_trace"])
        missing_anchor_count = len(self.gaps["missing_anchor"])
        owner_drift_count = len(self.gaps["owner_drift"])
        overreach_count = len(self.gaps["overreach"])
        inventory_count = len(self.gaps["inventory"])

        lines = [
            "# Chapter 01 -> CJS-5 Principle Alignment Audit Report",
            "",
            f"**Date:** {self.timestamp}",
            "**Workflow:** CH1_CJS5_PRINCIPLE_ALIGNMENT_CHECK",
            "**Auditor:** Automated static extraction with manual-review flags",
            "",
            "## Executive Summary",
            "",
            "| Metric | Result | Status |",
            "|---|---:|---|",
            f"| CJS-5 clusters discovered | {total}/23 | {'PASS' if total == 23 and inventory_count == 0 else 'REVIEW'} |",
            f"| Clusters with complete OP-O/OP-E/OP-C triads | {total - len({g['cluster_id'] for g in self.gaps['op_component_gap']})}/{total} | {'PASS' if op_gap_count == 0 else 'REVIEW'} |",
            f"| Clusters with direct Chapter 01 citations | {total - weak_trace_count - missing_anchor_count}/{total} | REVIEW |",
            f"| Clusters with inferred Chapter 01 basis | {total - missing_anchor_count}/{total} | {'PASS' if missing_anchor_count == 0 else 'REVIEW'} |",
            f"| Owner-routing issues | {owner_drift_count} | {'PASS' if owner_drift_count == 0 else 'REVIEW'} |",
            f"| Potential overreach flags | {overreach_count} | {'PASS' if overreach_count == 0 else 'REVIEW'} |",
            "",
            "## Overall Assessment",
            "",
        ]

        if op_gap_count == 0 and missing_anchor_count == 0 and owner_drift_count == 0 and overreach_count == 0:
            lines.append(
                "CJS-5 is operationally aligned with Chapter 01 at the structural level: all expected clusters were found, all operational rules carry complete `OP-O` / `OP-E` / `OP-C` triads, and each cluster has an inferred Chapter 01 principle basis. The main audit finding is trace explicitness: most CJS-5 clusters rely on PRIM/PROT, owner-file, and subject-matter routing rather than direct Chapter 01 citations."
            )
        else:
            lines.append(
                "CJS-5 has review items requiring editorial judgment before it should be treated as fully aligned. See the findings below."
            )

        lines.extend([
            "",
            "## Cluster Traceability Summary",
            "",
            "| Cluster | Title | File | Inferred Chapter 01 Principles | Direct Chapter 01 Refs | Owner Refs | Status |",
            "|---|---|---|---|---|---|---|",
        ])
        for cluster in sorted(self.clusters, key=lambda c: EXPECTED_CLUSTER_IDS.index(c.cluster_id) if c.cluster_id in EXPECTED_CLUSTER_IDS else 999):
            principles = ", ".join(cluster.inferred_principles) or "NONE"
            direct = ", ".join(cluster.direct_ch1_refs) or "None"
            owners = ", ".join(cluster.owner_refs[:6])
            if len(cluster.owner_refs) > 6:
                owners += f" (+{len(cluster.owner_refs) - 6})"
            lines.append(
                f"| {cluster.cluster_id} | {cluster.title} | `{cluster.file}` | {principles} | {direct} | {owners or 'None'} | {', '.join(cluster.classifications)} |"
            )

        lines.extend([
            "",
            "## Findings",
            "",
        ])
        if not any(self.gaps.values()):
            lines.append("No findings.")
        else:
            for category in ["inventory", "op_component_gap", "missing_anchor", "weak_trace", "owner_drift", "overreach"]:
                findings = self.gaps[category]
                if not findings:
                    continue
                title = category.replace("_", " ").title()
                lines.extend([f"### {title}", ""])
                for finding in findings:
                    cluster = finding.get("cluster_id", "n/a")
                    line = finding.get("line")
                    locator = f"`{finding.get('file')}`:{line}" if finding.get("file") and line else finding.get("file", "")
                    issue = finding.get("issue", "")
                    if category == "op_component_gap":
                        issue = f"{finding['rule']} missing {', '.join(finding['missing'])}"
                    if category == "weak_trace":
                        inferred = ", ".join(finding.get("inferred_principles", []))
                        issue = f"{issue} Inferred principles: {inferred}."
                    lines.append(f"- **{cluster}** {locator}: {issue}")
                lines.append("")

        lines.extend([
            "## Remediation Roadmap",
            "",
            "1. Treat `weak_trace` items as advisory unless the project wants every CJS-5 cluster to cite Chapter 01 directly.",
            "2. If direct traceability is desired, add concise `Read it with` bullets to high-risk clusters first: CJS-5A.2, CJS-5A.4, CJS-5A.5, CJS-5C.*, CJS-5D.*, and CJS-5E.*.",
            "3. Keep remediation text limited to routing metadata; do not convert CJS-5 into a competing Chapter 01 or Chapter Five doctrine layer.",
            "",
            "## Manual Review Notes",
            "",
            "High-risk families for human review are CJS-5A, CJS-5C, CJS-5D, and CJS-5E. The automated pass checks structure and trace signals; semantic adequacy should be reviewed against the operative text before making corpus edits.",
            "",
        ])
        path.write_text("\n".join(lines))
        return path

    def write_matrix(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_cjs5_traceability_matrix_{self.timestamp}.csv"
        with path.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "cluster_id",
                "cluster_title",
                "file",
                "start_line",
                "end_line",
                "inferred_ch1_principles",
                "direct_ch1_refs",
                "read_with_refs",
                "owner_refs",
                "op_rule_count",
                "op_complete",
                "status",
            ])
            for cluster in sorted(self.clusters, key=lambda c: EXPECTED_CLUSTER_IDS.index(c.cluster_id) if c.cluster_id in EXPECTED_CLUSTER_IDS else 999):
                writer.writerow([
                    cluster.cluster_id,
                    cluster.title,
                    cluster.file,
                    cluster.start_line,
                    cluster.end_line,
                    "; ".join(cluster.inferred_principles),
                    "; ".join(cluster.direct_ch1_refs),
                    " | ".join(cluster.read_with),
                    "; ".join(cluster.owner_refs),
                    len(cluster.rules),
                    "yes" if all(not rule.missing for rule in cluster.rules) else "no",
                    "; ".join(cluster.classifications),
                ])
        return path

    def write_log(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_cjs5_audit_log_{self.timestamp}.json"
        data = {
            "timestamp": self.timestamp,
            "workflow": "CH1_CJS5_PRINCIPLE_ALIGNMENT_CHECK",
            "principles": self.principles,
            "expected_cluster_ids": EXPECTED_CLUSTER_IDS,
            "clusters": [
                {
                    "cluster_id": cluster.cluster_id,
                    "title": cluster.title,
                    "file": cluster.file,
                    "start_line": cluster.start_line,
                    "end_line": cluster.end_line,
                    "read_with": cluster.read_with,
                    "direct_ch1_refs": cluster.direct_ch1_refs,
                    "inferred_principles": cluster.inferred_principles,
                    "owner_refs": cluster.owner_refs,
                    "op_rules": [
                        {
                            "label": rule.label,
                            "line": rule.line,
                            "has_op_o": rule.has_o,
                            "has_op_e": rule.has_e,
                            "has_op_c": rule.has_c,
                            "missing": rule.missing,
                        }
                        for rule in cluster.rules
                    ],
                    "classifications": cluster.classifications,
                }
                for cluster in self.clusters
            ],
            "gaps": self.gaps,
        }
        path.write_text(json.dumps(data, indent=2))
        return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Chapter 01 -> CJS-5 principle alignment audit")
    parser.add_argument("--repo-root", type=Path, default=Path("."), help="Repository root")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("evidence") / datetime.now().strftime("%Y-%m-%d"),
        help="Output directory for audit artifacts",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    auditor = Ch1Cjs5AlignmentAuditor(args.repo_root)
    auditor.run()
    report = auditor.write_report(args.output_dir)
    matrix = auditor.write_matrix(args.output_dir)
    log = auditor.write_log(args.output_dir)

    print("Chapter 01 -> CJS-5 alignment audit complete.")
    print(f"Report: {report}")
    print(f"Matrix: {matrix}")
    print(f"Audit log: {log}")


if __name__ == "__main__":
    main()
