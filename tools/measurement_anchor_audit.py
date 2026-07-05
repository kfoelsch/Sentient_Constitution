#!/usr/bin/env python3
"""Audit Chapter Zero measurement anchor hygiene across the operative corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from corpus_paths import source_markdown_files

CH00_FILE = "core_00_preamble.md"

# Legacy aliases retained in Chapter Zero only during transition.
LEGACY_MEASUREMENT_ANCHORS: frozenset[str] = frozenset(
    {
        "material-family-orientation",
        "measuring-flourishing-and-sentient-condition",
        "measuring-hidden-costs-dependencies-and-resource-flows",
        "measuring-participation-and-fair-access",
        "measuring-fair-access-agency-and-trust",
        "measuring-oversight-truth-and-trust",
        "measuring-accountability-incentives-and-timeliness",
        "measuring-governance-fidelity",
        "measuring-timely-resolution",
    }
)

CANONICAL_MEASUREMENT_ANCHORS: frozenset[str] = frozenset(
    {
        "2-the-measurements",
        "measurements-overview",
        "major-measurement-aspects",
        "what-measurement-is-for",
        "from-measurement-to-evidence-and-remedy",
        "measuring-threshold-and-scaling",
        "measuring-flourishing",
        "measuring-continuity",
        "measuring-participation",
        "measuring-oversight",
        "measuring-accountability",
        "measuring-timeliness",
        "measuring-constitutional-performance",
    }
)

MARKDOWN_LINK_RE = re.compile(
    r"\[[^\]]*\]\(([^)\s#]+(?:\.md)?)(#[^)\s]+)?(?:\s+\"[^\"]*\")?\)"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write dated report under evidence/<date>/.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Evidence date stamp (YYYY-MM-DD).",
    )
    return parser.parse_args()


def scan_file(path: Path, root: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    findings: list[Finding] = []
    allow_legacy = rel == CH00_FILE
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            anchor = match.group(2)
            if not anchor:
                continue
            anchor_id = anchor.lstrip("#")
            if anchor_id not in LEGACY_MEASUREMENT_ANCHORS:
                continue
            if allow_legacy:
                continue
            findings.append(
                Finding(
                    file=rel,
                    line=line_no,
                    kind="legacy_measurement_anchor",
                    detail=f"Outbound link uses legacy alias #{anchor_id}; prefer canonical Chapter Zero §3 anchor",
                )
            )
    return findings


def write_evidence(root: Path, date: str, findings: list[Finding]) -> Path:
    out_dir = root / "evidence" / date
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "measurement_anchor_audit_report.md"
    status = "PASS" if not findings else "FAIL"
    lines = [
        "# Measurement Anchor Audit Report",
        "",
        f"**Date:** {date}",
        f"**Status:** {status}",
        "",
        f"Legacy aliases allowed only in `{CH00_FILE}`. Canonical anchors: "
        + ", ".join(f"`#{a}`" for a in sorted(CANONICAL_MEASUREMENT_ANCHORS)),
        "",
    ]
    if not findings:
        lines.append("No stale outbound legacy measurement anchors found outside Chapter Zero.")
    else:
        lines.append("| File | Line | Detail |")
        lines.append("|---|---:|---|")
        for f in findings:
            lines.append(f"| `{f.file}` | {f.line} | {f.detail} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings: list[Finding] = []
    for path in source_markdown_files(root):
        findings.extend(scan_file(path, root))

    if args.write_evidence:
        report = write_evidence(root, args.date, findings)
        print(f"Wrote {report}")

    if findings:
        print(f"measurement-anchor-audit: FAIL ({len(findings)} finding(s))", file=sys.stderr)
        for f in findings[:50]:
            print(f"  {f.file}:{f.line} — {f.detail}", file=sys.stderr)
        if len(findings) > 50:
            print(f"  ... and {len(findings) - 50} more", file=sys.stderr)
        return 1

    print("measurement-anchor-audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
