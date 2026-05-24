#!/usr/bin/env python3
"""Deterministic article-reference integrity audit for the constitutional corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass


DEFAULT_SCOPE = [
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_assessment.md",
    "core_07-07_standing_integration.md",
    "core_08-08_misconduct.md",
    "core_09-09_forum.md",
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
    "core_11-11_governance.md",
    "core_12-14_amendment.md",
    "core_15-15_incorporation.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
    "doc_architecture.md",
]

DEFAULT_ARTICLE_SOURCES = [
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
]

ARTICLE_HEADING_RE = re.compile(r"^### Article ([IVXLCDM]+):\s*(.+?)\s*$")
ARTICLE_REF_RE = re.compile(r"\bArticle ([IVXLCDM]+)\b")

# These rules cover common stale-drifts tracked in prior audits.
SEMANTIC_RULES: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"\bstanding\b", re.IGNORECASE), "XII", "standing"),
    (re.compile(r"\bconflict resolution\b", re.IGNORECASE), "XIII", "conflict resolution"),
    (re.compile(r"\bequality\b", re.IGNORECASE), "XX", "equality"),
    (re.compile(r"\bcomprehensibility\b", re.IGNORECASE), "XVI", "comprehensibility"),
    (re.compile(r"\broot cause\b", re.IGNORECASE), "XIX", "root cause analysis"),
    (re.compile(r"\bresource allocation\b", re.IGNORECASE), "XVIII", "resource allocation"),
    (re.compile(r"\blifecycle\b", re.IGNORECASE), "IX", "lifecycle and reversibility"),
]


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str
    detail: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path. Defaults to current directory.",
    )
    parser.add_argument(
        "--source",
        default="core_10-10_rights_part_a.md",
        help="Primary file for article-heading discovery. If it has no headings, the audit merges ### Article … lines from the Chapter Ten part files.",
    )
    parser.add_argument(
        "--scope",
        nargs="+",
        default=DEFAULT_SCOPE,
        help="Files to scan for references.",
    )
    parser.add_argument(
        "--semantic-checks",
        action="store_true",
        help="Enable semantic drift checks (stricter, higher false-positive risk).",
    )
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write a dated audit artifact under evidence/<date>/.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date used in evidence path and report header (YYYY-MM-DD).",
    )
    return parser.parse_args()


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def canonical_map(source_text: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for line in source_text.splitlines():
        match = ARTICLE_HEADING_RE.match(line.strip())
        if match:
            mapping[match.group(1)] = match.group(2)
    if not mapping:
        raise SystemExit("No canonical Article headings found in source file.")
    return mapping


def canonical_map_from_paths(root: pathlib.Path, source: str) -> dict[str, str]:
    """Merge `### Article …` headings from the primary --source file and all Chapter Ten part files.

    Part A only contains top-level `### Article` rows for early articles; later Roman articles live in
    other `core_10-10_rights_part_*.md` files. A partial map from the first file alone is incorrect.
    """
    seen: set[str] = set()
    ordered_paths: list[str] = []
    if source and source not in seen:
        ordered_paths.append(source)
        seen.add(source)
    for rel_path in DEFAULT_ARTICLE_SOURCES:
        if rel_path not in seen:
            ordered_paths.append(rel_path)
            seen.add(rel_path)

    mapping: dict[str, str] = {}
    for rel_path in ordered_paths:
        part_path = root / rel_path
        if not part_path.is_file():
            continue
        text = part_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            match = ARTICLE_HEADING_RE.match(line.strip())
            if match:
                mapping[match.group(1)] = match.group(2)

    if not mapping:
        raise SystemExit("No canonical Article headings found in source file or Chapter Ten part files.")
    return mapping


def scan_file(
    rel_path: str,
    text: str,
    canonical: dict[str, str],
    semantic_checks: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    for idx, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        refs = ARTICLE_REF_RE.findall(raw_line)
        refs_set = set(refs)
        for numeral in refs:
            if numeral not in canonical:
                findings.append(
                    Finding(
                        file=rel_path,
                        line=idx,
                        kind="unknown-article",
                        detail=f"Reference to Article {numeral}, which is absent in canonical map",
                        text=raw_line.strip(),
                    )
                )

        if semantic_checks and refs_set:
            for pattern, expected, label in SEMANTIC_RULES:
                if pattern.search(raw_line) and expected not in refs_set:
                    findings.append(
                        Finding(
                            file=rel_path,
                            line=idx,
                            kind="semantic-mismatch",
                            detail=f"Line discusses {label} but does not cite expected Article {expected}",
                            text=raw_line.strip(),
                        )
                    )
    return findings


def report_markdown(
    run_date: str,
    scope: list[str],
    canonical: dict[str, str],
    findings: list[Finding],
) -> str:
    lines: list[str] = []
    lines.append(f"# Reference Integrity Audit - {run_date}")
    lines.append("")
    lines.append("## Scope")
    for file_path in scope:
        lines.append(f"- `{file_path}`")
    lines.append("")
    lines.append("## Canonical Chapter Five Map Snapshot")
    for numeral, title in sorted(canonical.items(), key=lambda item: roman_to_int(item[0])):
        lines.append(f"- `Article {numeral}` - {title}")
    lines.append("")
    lines.append("## Findings")

    if findings:
        lines.append("| File | Line | Type | Detail |")
        lines.append("|---|---:|---|---|")
        for item in findings:
            lines.append(
                f"| `{item.file}` | {item.line} | `{item.kind}` | {item.detail} |"
            )
        lines.append("")
        lines.append("## Manual Review Context")
        for item in findings:
            lines.append(
                f"- `{item.file}:{item.line}` - {item.text}"
            )
    else:
        lines.append("- No mismatches detected.")

    lines.append("")
    lines.append("## Result")
    lines.append("- `PASS`" if not findings else "- `FAIL`")
    lines.append("")
    return "\n".join(lines)


def roman_to_int(roman: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for char in reversed(roman):
        cur = values[char]
        if cur < prev:
            total -= cur
        else:
            total += cur
            prev = cur
    return total


def write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_file = evidence_dir / f"REFERENCE_INTEGRITY_AUDIT_{run_date}.md"
    evidence_file.write_text(report, encoding="utf-8")
    return evidence_file


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    canonical = canonical_map_from_paths(root, args.source)

    findings: list[Finding] = []
    for rel_path in args.scope:
        file_path = root / rel_path
        if not file_path.is_file():
            print(
                f"reference_audit: skipping missing scope file: {rel_path}",
                file=sys.stderr,
            )
            continue
        text = load_text(file_path)
        findings.extend(
            scan_file(
                rel_path=rel_path,
                text=text,
                canonical=canonical,
                semantic_checks=args.semantic_checks,
            )
        )

    report = report_markdown(args.date, args.scope, canonical, findings)
    if args.write_evidence:
        evidence_path = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {evidence_path}")
    else:
        print(report)

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
