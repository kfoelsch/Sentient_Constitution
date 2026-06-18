#!/usr/bin/env python3
"""Audit CJS placement and section-heading conventions for operational clusters.

Fails when:
- CJS-3 sections define reusable OP-O / OP-E / OP-C operational cluster terms
  (those belong in CJS-5 per doc_architecture.md).
- CJS-5 cluster section headings use letter suffixes (CJS-5A.1, CJS-5B, etc.).
- CJS-5.1 constitutional compass map is incomplete or cluster Trace blocks lack
  Constitutional frame / Chapter One basis metadata.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import binding_corpus_scope

CJS3_FILE = "corpus_joint_structure/cjs_03_joint_structural_obligations.md"
CJS5_GLOB = "corpus_joint_structure/cjs_05*.md"
CJS5_COMPASS_FILE = "corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md"
CJS5_BAND_FILES = [
    "corpus_joint_structure/cjs_05o_oversight_operations.md",
    "corpus_joint_structure/cjs_05p_participation_operations.md",
    "corpus_joint_structure/cjs_05a_accountability_operations.md",
    "corpus_joint_structure/cjs_05c_continuity_operations.md",
    "corpus_joint_structure/cjs_05i_integrative_operations.md",
]
EXPECTED_OPERATIONAL_CLUSTER_IDS = [f"CJS-5.{n}" for n in range(2, 24)]

SECTION_HEADING_RE = re.compile(r"^##\s+(CJS-5[A-E](?:\.\d+)?(?::|\s))", re.MULTILINE)
CLUSTER_HEADING_RE = re.compile(r"^##\s+(CJS-5\.\d+)\s+", re.MULTILINE)
TRACE_BLOCK_RE = re.compile(
    r"<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\s*\n(.*?)\n</details>",
    re.DOTALL,
)
LETTER_CLUSTER_ID_RE = re.compile(r"\bCJS-5[A-E](?:\.\d+)?\b")
LETTER_ANCHOR_RE = re.compile(r"#cjs-5[a-e]\d*", re.IGNORECASE)

OP_CLUSTER_BLOCK_RE = re.compile(
    r"^([A-Z][^\n]{2,120})\n"
    r"(- OP-O:.*\n"
    r"- OP-E:.*\n"
    r"- OP-C:.*)",
    re.MULTILINE,
)

# CJS-3 may cite CJS-5 clusters; exclude pointer-only lines.
POINTER_LINE_RE = re.compile(
    r"^(Apply|Read with|See|Follow|Use)\b|^- Topic routing \(|^- (Upstream|Downstream|Read with):",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def slice_cjs3_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    sections: list[tuple[str, str]] = []
    current_id = ""
    current_lines: list[str] = []
    for line in lines:
        if line.startswith("### CJS-3."):
            if current_id:
                sections.append((current_id, "\n".join(current_lines)))
            current_id = line.removeprefix("### ").strip()
            current_lines = []
            continue
        if current_id:
            current_lines.append(line)
    if current_id:
        sections.append((current_id, "\n".join(current_lines)))
    return sections


def find_cjs3_inline_op_clusters(section_id: str, body: str) -> list[str]:
    findings: list[str] = []
    for match in OP_CLUSTER_BLOCK_RE.finditer(body):
        title = match.group(1).strip()
        block = match.group(2)
        if "OP-O:" not in block or "OP-E:" not in block or "OP-C:" not in block:
            continue
        # Ignore if this is inside a collapsible definitions widget (rare).
        if title.startswith("[") or title.startswith("<"):
            continue
        findings.append(
            f"{CJS3_FILE}: {section_id} defines operational cluster {title!r}; "
            "move to CJS-5 and leave a pointer in CJS-3."
        )
    return findings


def audit_cjs3_op_clusters(root: Path) -> list[str]:
    path = root / CJS3_FILE
    if not path.is_file():
        return [f"Missing required file: {CJS3_FILE}"]
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    for section_id, body in slice_cjs3_sections(text):
        findings.extend(find_cjs3_inline_op_clusters(section_id, body))
    return findings


def audit_cjs5_letter_headings(root: Path) -> list[str]:
    findings: list[str] = []
    for path in sorted((root / "corpus_joint_structure").glob("cjs_05*.md")):
        text = path.read_text(encoding="utf-8")
        for match in SECTION_HEADING_RE.finditer(text):
            findings.append(
                f"{path.relative_to(root)}: section heading uses letter suffix {match.group(1).strip()!r}; "
                "use numeric CJS-5.n IDs only."
            )
    return findings


def audit_cjs5_compass_and_frames(root: Path) -> list[str]:
    """Validate CJS-5.1 compass map completeness and constitutional Trace metadata."""
    findings: list[str] = []
    compass_path = root / CJS5_COMPASS_FILE
    if not compass_path.is_file():
        return [f"Missing required file: {CJS5_COMPASS_FILE}"]

    compass_text = compass_path.read_text(encoding="utf-8")
    map_start = compass_text.find("**Cluster map**")
    map_end = compass_text.find("</details>", map_start)
    map_section = compass_text[map_start:map_end] if map_start != -1 and map_end != -1 else ""
    map_ids = re.findall(r"\*\*(CJS-5\.\d+)\*\*", map_section)
    map_ids = [cluster_id for cluster_id in map_ids if cluster_id in EXPECTED_OPERATIONAL_CLUSTER_IDS]
    if len(set(map_ids)) != 22:
        findings.append(
            f"{CJS5_COMPASS_FILE}: constitutional cluster map has {len(set(map_ids))} unique cluster rows; expected 22."
        )

    discovered: dict[str, str] = {}
    for rel in CJS5_BAND_FILES:
        path = root / rel
        if not path.is_file():
            findings.append(f"Missing required file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        parts = re.split(r"(?=^## CJS-5\.\d+ )", text, flags=re.MULTILINE)
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
    """Flag letter-suffixed CJS-5 cluster IDs in binding corpus (not evidence snapshots)."""
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
                    "use numeric CJS-5.5–CJS-5.53 IDs."
                )
            anchor = LETTER_ANCHOR_RE.search(line)
            if anchor:
                findings.append(
                    f"{rel}:{line_no}: legacy letter cluster anchor {anchor.group()}; "
                    "use numeric slug (for example #cjs-52-… for CJS-5.5)."
                )
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings: list[str] = []
    findings.extend(audit_cjs3_op_clusters(root))
    findings.extend(audit_cjs5_letter_headings(root))
    findings.extend(audit_cjs5_compass_and_frames(root))
    findings.extend(audit_letter_cluster_citations(root))

    if findings:
        print("CJS operational cluster audit failed:\n", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("CJS operational cluster audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
