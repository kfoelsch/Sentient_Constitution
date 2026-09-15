#!/usr/bin/env python3
"""Audit doc_architecture.md section heading discipline.

Fails on:
- letter-suffixed top-level sections (e.g. ``## 1A.`` — use ``###`` under a numeric section)
- duplicate ``##`` section titles
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "doc_architecture.md"

LETTER_SECTION_RE = re.compile(r"^##\s+\d+[A-Za-z]\.", re.M)
SECTION_RE = re.compile(r"^##\s+(.+)$", re.M)


def audit(text: str) -> list[str]:
    findings: list[str] = []
    for match in LETTER_SECTION_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        findings.append(
            f"doc_architecture.md:{line}: top-level section uses letter suffix; "
            f"use a numeric ## section and ### subsections instead: {match.group(0).strip()}"
        )
    titles: list[tuple[int, str]] = []
    for match in SECTION_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        titles.append((line, match.group(1).strip()))
    seen: dict[str, int] = {}
    for line, title in titles:
        if title in seen:
            findings.append(
                f"doc_architecture.md:{line}: duplicate section heading (first at {seen[title]}): ## {title}"
            )
        else:
            seen[title] = line
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    path = args.root / "doc_architecture.md"
    if not path.exists():
        print(f"Missing {path}", file=sys.stderr)
        return 1
    findings = audit(path.read_text(encoding="utf-8"))
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("PASS: doc_architecture section headings use numeric ## sections only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
