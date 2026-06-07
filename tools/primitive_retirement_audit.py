#!/usr/bin/env python3
"""Fail if retired primitive-layer references reappear in live corpus files."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from dataclasses import dataclass

from corpus_paths import binding_corpus_scope


RETIRED_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("retired PRIM code", re.compile(r"\bPRIM\d+\b")),
    ("retired PROT code", re.compile(r"\bPROT\d+\b")),
    ("retired PRIM shorthand", re.compile(r"\bPRIM\b")),
    ("retired PROT shorthand", re.compile(r"\bPROT\b")),
    ("retired CP-PCH label", re.compile(r"\bCP-PCH\d+\b")),
    ("retired primitive term", re.compile(r"\b[Pp]rimitives?\b")),
    ("retired corpus_primitives path", re.compile(r"\bcorpus_primitives\.md\b")),
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--include-support-docs",
        action="store_true",
        default=True,
        help="Scan README.md and doc_architecture.md in addition to binding corpus files.",
    )
    return parser.parse_args()


def scan_file(root: pathlib.Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []

    findings: list[Finding] = []
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for label, pattern in RETIRED_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(rel_path, idx, label, line.strip()))
    return findings


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    scope = binding_corpus_scope(root, include_support_docs=args.include_support_docs)

    findings: list[Finding] = []
    for rel_path in scope:
        findings.extend(scan_file(root, rel_path))

    if findings:
        print("Retired primitive-layer references found:", file=sys.stderr)
        for finding in findings:
            print(
                f"{finding.file}:{finding.line}: {finding.kind}: {finding.text}",
                file=sys.stderr,
            )
        return 1

    print("Primitive retirement audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
