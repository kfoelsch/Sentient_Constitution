#!/usr/bin/env python3
"""Audit alphabetical order of CJS-3 OP cluster sub-terms within each subsection.

Fails when sortable sub-terms (excluding cluster intro lines and CJS-3.0 pinned
preface rules) are not in case-insensitive alphabetical order.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CJS3_GLOB = "corpus_joint_structure/cjs_03*.md"

SECTION_SPLIT_RE = re.compile(r"(?=^#{1,3} CJS-3)", re.MULTILINE)
SECTION_ID_RE = re.compile(r"^#{1,3} (CJS-3\S+)", re.MULTILINE)

CJS30_PINNED = {
    "Competency bar, clearance, and standing interface",
    "Role-definition reading rule",
}

OP_BLOCK_RE = re.compile(
    r"^([A-Z][^\n]{2,200})\n"
    r"(- OP-O:.*\n"
    r"- OP-E:.*\n"
    r"- OP-C:.*)",
    re.MULTILINE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def sortable_terms(section_id: str, body: str) -> list[str]:
    terms = [match.group(1).strip() for match in OP_BLOCK_RE.finditer(body)]
    filtered: list[str] = []
    for title in terms:
        if section_id.startswith("CJS-3.0") and title in CJS30_PINNED:
            continue
        filtered.append(title)
    return filtered


def audit_section(rel_path: str, section_text: str) -> list[str]:
    id_match = SECTION_ID_RE.search(section_text)
    if not id_match:
        return []
    section_id = id_match.group(1)
    terms = sortable_terms(section_id, section_text)
    if len(terms) < 2:
        return []

    findings: list[str] = []
    for i in range(1, len(terms)):
        prev, curr = terms[i - 1], terms[i]
        if curr.casefold() < prev.casefold():
            findings.append(
                f"{rel_path}: {section_id}: '{curr}' should come before '{prev}' "
                "in alphabetical order"
            )
            break
    return findings


def audit_file(root: Path, path: Path) -> list[str]:
    rel = str(path.relative_to(root))
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    for part in SECTION_SPLIT_RE.split(text):
        if part.startswith("## CJS-3"):
            findings.extend(audit_section(rel, part))
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings: list[str] = []
    for path in sorted((root / "corpus_joint_structure").glob("cjs_03*.md")):
        findings.extend(audit_file(root, path))

    if findings:
        print("FAIL: CJS-3 cluster term order audit detected issues:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("PASS: CJS-3 cluster sub-terms are alphabetically ordered within subsections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
