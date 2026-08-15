#!/usr/bin/env python3
"""Audit CJS placement and section-heading conventions for operational clusters.

Fails when:
- CJS-1 sections define reusable guidepost oDef operational cluster terms
  (those belong in CJS-3 per doc_architecture.md).
- CJS-3 band files still carry legacy ``- OP-O:`` / ``- OP-E:`` / ``- OP-C:`` lines.
- CJS-3 cluster section headings use letter suffixes (CJS-3A.1, CJS-3B, etc.).
- CJS-3.1 constitutional compass map is incomplete or cluster Trace blocks lack
  Constitutional frame / Chapter One basis metadata.
- CJS-3 band files stack ``---`` delimiters or place a rule between an entry's
  own ``<a id>`` anchors and its heading (CH5-FORMAT / CJS-1.14).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import binding_corpus_scope
from cjs_odef_format import LEGACY_OP_RE, titled_guidepost_entries
from definition_separator_format import audit_separator_lines

CJS1_FILES = (
    "corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md",
    "corpus_joint_structure/cjs_01_drafting_contracts.md",
    "corpus_joint_structure/cjs_01_odef_parse.md",
    "corpus_joint_structure/cjs_02_support_hosting_classification.md",
)
CJS1_FILE = CJS1_FILES[0]
CJS3_GLOB = "corpus_joint_structure/cjs_03*.md"
CJS3_COMPASS_FILE = "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md"
CJS3_BAND_FILES = [
    "corpus_joint_structure/cjs_03o_oversight_operations.md",
    "corpus_joint_structure/cjs_03p_participation_operations.md",
    "corpus_joint_structure/cjs_03a_accountability_operations.md",
    "corpus_joint_structure/cjs_03c_continuity_operations.md",
    "corpus_joint_structure/cjs_03i_integrative_operations.md",
]
EXPECTED_OPERATIONAL_CLUSTER_IDS = [f"CJS-3.{n}" for n in range(2, 24)]

SECTION_HEADING_RE = re.compile(r"^#{1,3}\s+(CJS-3[A-E](?:\.\d+)?(?::|\s))", re.MULTILINE)
CLUSTER_HEADING_RE = re.compile(r"^#{1,3}\s+(CJS-3\.\d+)\s+", re.MULTILINE)
CLUSTER_SPLIT_RE = re.compile(r"(?=^#{1,3} CJS-3\.\d+ )", re.MULTILINE)
CJS1_HEADING_RE = re.compile(r"^#{1,3}\s+(CJS-1\.\S*)")
TRACE_BLOCK_RE = re.compile(
    r"<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\s*\n(.*?)\n</details>",
    re.DOTALL,
)
LETTER_CLUSTER_ID_RE = re.compile(r"\bCJS-3[A-E](?:\.\d+)?\b")
LETTER_ANCHOR_RE = re.compile(r"#cjs-3[a-e]\d*", re.IGNORECASE)

# CJS-1 may cite CJS-3 clusters; exclude pointer-only lines.
POINTER_LINE_RE = re.compile(
    r"^(Apply|Read with|See|Follow|Use)\b|^- Topic routing \(|^- (Upstream|Downstream|Read with):",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def slice_cjs1_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    sections: list[tuple[str, str]] = []
    current_id = ""
    current_lines: list[str] = []
    for line in lines:
        heading = CJS1_HEADING_RE.match(line)
        if heading:
            if current_id:
                sections.append((current_id, "\n".join(current_lines)))
            current_id = line.lstrip("#").strip()
            current_lines = []
            continue
        if current_id:
            current_lines.append(line)
    if current_id:
        sections.append((current_id, "\n".join(current_lines)))
    return sections


def find_cjs1_inline_odef_clusters(section_id: str, body: str, rel: str = CJS1_FILE) -> list[str]:
    findings: list[str] = []
    # Skip parse-mechanics sections that describe the format itself.
    if section_id.startswith("CJS-1.13") or section_id.startswith("CJS-1.14"):
        return findings
    for title in titled_guidepost_entries(body):
        if title.startswith("[") or title.startswith("<"):
            continue
        if POINTER_LINE_RE.match(title):
            continue
        findings.append(
            f"{rel}: {section_id} defines operational cluster {title!r}; "
            "move to CJS-3 and leave a pointer in CJS-1."
        )
    return findings


def audit_cjs1_op_clusters(root: Path) -> list[str]:
    findings: list[str] = []
    for rel in CJS1_FILES:
        path = root / rel
        if not path.is_file():
            findings.append(f"Missing required file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for section_id, body in slice_cjs1_sections(text):
            findings.extend(find_cjs1_inline_odef_clusters(section_id, body, rel))
    return findings


def audit_cjs3_legacy_op_lines(root: Path) -> list[str]:
    findings: list[str] = []
    for rel in CJS3_BAND_FILES + [
        "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md"
    ]:
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            if LEGACY_OP_RE.match(line):
                findings.append(
                    f"{rel}:{line_no}: legacy {line[:8]!r} line; migrate to guidepost "
                    "**What it is** / **How to measure and assess** / **What must hold**."
                )
    return findings


def audit_cjs3_letter_headings(root: Path) -> list[str]:
    findings: list[str] = []
    for path in sorted((root / "corpus_joint_structure").glob("cjs_03*.md")):
        text = path.read_text(encoding="utf-8")
        for match in SECTION_HEADING_RE.finditer(text):
            findings.append(
                f"{path.relative_to(root)}: section heading uses letter suffix {match.group(1).strip()!r}; "
                "use numeric CJS-3.n IDs only."
            )
    return findings


def audit_cjs3_compass_and_frames(root: Path) -> list[str]:
    """Validate CJS-3.1 compass map completeness and constitutional Trace metadata."""
    findings: list[str] = []
    compass_path = root / CJS3_COMPASS_FILE
    if not compass_path.is_file():
        return [f"Missing required file: {CJS3_COMPASS_FILE}"]

    compass_text = compass_path.read_text(encoding="utf-8")
    map_start = compass_text.find("**Cluster map**")
    map_end = compass_text.find("</details>", map_start)
    map_section = compass_text[map_start:map_end] if map_start != -1 and map_end != -1 else ""
    map_ids = re.findall(r"\*\*(CJS-3\.\d+)\*\*", map_section)
    map_ids = [cluster_id for cluster_id in map_ids if cluster_id in EXPECTED_OPERATIONAL_CLUSTER_IDS]
    if len(set(map_ids)) != 22:
        findings.append(
            f"{CJS3_COMPASS_FILE}: constitutional cluster map has {len(set(map_ids))} unique cluster rows; expected 22."
        )

    discovered: dict[str, str] = {}
    for rel in CJS3_BAND_FILES:
        path = root / rel
        if not path.is_file():
            findings.append(f"Missing required file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        parts = CLUSTER_SPLIT_RE.split(text)
        for part in parts:
            heading = CLUSTER_HEADING_RE.match(part)
            if not heading:
                continue
            cluster_id = heading.group(1)
            trace_match = TRACE_BLOCK_RE.search(part)
            trace_body = trace_match.group(1) if trace_match else ""
            discovered[cluster_id] = rel
            if "- Constitutional frame:" not in trace_body:
                findings.append(
                    f"{rel}: {cluster_id} Trace block missing Constitutional frame metadata."
                )
            if "- Chapter One basis:" not in trace_body:
                findings.append(
                    f"{rel}: {cluster_id} Trace block missing Chapter One basis metadata."
                )

    for cluster_id in EXPECTED_OPERATIONAL_CLUSTER_IDS:
        if cluster_id not in discovered:
            findings.append(f"Expected operational cluster heading missing: {cluster_id}.")
    for cluster_id in discovered:
        if cluster_id not in EXPECTED_OPERATIONAL_CLUSTER_IDS:
            findings.append(
                f"{discovered[cluster_id]}: unexpected operational cluster heading {cluster_id}."
            )
    return findings


def audit_letter_cluster_citations(root: Path) -> list[str]:
    """Flag letter-suffixed CJS-3 cluster IDs in binding corpus (not evidence snapshots)."""
    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        if not rel.endswith(".md"):
            continue
        path = root / rel
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            match = LETTER_CLUSTER_ID_RE.search(line)
            if match:
                findings.append(
                    f"{rel}:{line_no}: legacy letter cluster ID {match.group()}; "
                    "use numeric CJS-3.5–CJS-3.53 IDs."
                )
            anchor = LETTER_ANCHOR_RE.search(line)
            if anchor:
                findings.append(
                    f"{rel}:{line_no}: legacy letter cluster anchor {anchor.group()}; "
                    "use numeric slug (for example #cjs-32-… for CJS-3.5)."
                )
    return findings


def audit_cjs3_separators(root: Path) -> list[str]:
    findings: list[str] = []
    for rel in [CJS3_COMPASS_FILE, *CJS3_BAND_FILES, "corpus_joint_structure/cjs_03_audit_process.md"]:
        path = root / rel
        if not path.exists():
            continue
        findings.extend(audit_separator_lines(path.read_text(encoding="utf-8").splitlines(), rel))
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings: list[str] = []
    findings.extend(audit_cjs1_op_clusters(root))
    findings.extend(audit_cjs3_legacy_op_lines(root))
    findings.extend(audit_cjs3_letter_headings(root))
    findings.extend(audit_cjs3_compass_and_frames(root))
    findings.extend(audit_letter_cluster_citations(root))
    findings.extend(audit_cjs3_separators(root))

    if findings:
        print("CJS operational cluster audit failed:\n", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("CJS operational cluster audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
