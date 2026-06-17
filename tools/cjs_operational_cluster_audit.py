#!/usr/bin/env python3
"""Audit CJS placement and section-heading conventions for operational clusters.

Fails when:
- CJS-3 sections define reusable OP-O / OP-E / OP-C operational cluster terms
  (those belong in CJS-5 per doc_architecture.md).
- CJS-5 cluster section headings use letter suffixes (CJS-5A.1, CJS-5B, etc.).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import binding_corpus_scope

CJS3_FILE = "corpus_joint_structure/cjs_03_joint_structural_obligations.md"
CJS5_GLOB = "corpus_joint_structure/cjs_05*.md"

SECTION_HEADING_RE = re.compile(r"^##\s+(CJS-5[A-E](?:\.\d+)?(?::|\s))", re.MULTILINE)
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
                    "use numeric CJS-5.2–CJS-5.23 IDs."
                )
            anchor = LETTER_ANCHOR_RE.search(line)
            if anchor:
                findings.append(
                    f"{rel}:{line_no}: legacy letter cluster anchor {anchor.group()}; "
                    "use numeric slug (for example #cjs-52-… for CJS-5.2)."
                )
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings: list[str] = []
    findings.extend(audit_cjs3_op_clusters(root))
    findings.extend(audit_cjs5_letter_headings(root))
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
