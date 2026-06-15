#!/usr/bin/env python3
"""Audit bidirectional CJS-2.1 topic-router references."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from router_table_lib import (
    build_section_index,
    extract_section,
    load_router_rows,
    primary_attach_ids,
    section_has_primary_route,
    section_has_read_with_route,
)

SKIP_READ_WITH = set()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write markdown report to evidence/YYYY-MM-DD/.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    rows = load_router_rows(root)
    index = build_section_index(root)
    findings: list[str] = []

    for row in rows:
        for attach in row.primary_attach:
            path = index.get(attach)
            if not path:
                findings.append(f"MISSING_SECTION primary {row.row_id} -> {attach} (no heading found)")
                continue
            section_text = extract_section(path.read_text(encoding="utf-8"), attach)
            if not section_text:
                findings.append(f"MISSING_SECTION primary {row.row_id} -> {attach} (heading not extracted)")
                continue
            if not section_has_primary_route(section_text, row):
                findings.append(
                    f"PRIMARY_OWNER {row.row_id} ({attach}): missing router cite for primary owner"
                )

        primary_label = row.primary_attach[0] if len(row.primary_attach) == 1 else ", ".join(row.primary_attach)
        for attach in row.read_with_attach:
            if attach in row.primary_attach:
                continue
            path = index.get(attach)
            if not path:
                findings.append(f"MISSING_SECTION read-with {row.row_id} -> {attach} (no heading found)")
                continue
            section_text = extract_section(path.read_text(encoding="utf-8"), attach)
            if not section_text:
                findings.append(f"MISSING_SECTION read-with {row.row_id} -> {attach} (heading not extracted)")
                continue
            if not section_has_read_with_route(section_text, row):
                findings.append(
                    f"READ_WITH {row.row_id} ({attach}): missing router cite back to row and primary owner ({primary_label})"
                )

    today = dt.date.today().isoformat()
    lines = [
        f"# Router bidirectional audit - {today}",
        "",
        "## Scope",
        f"- Router: `corpus_joint_structure/cjs_02_implementation_integration_map.md` **CJS-2.1**",
        f"- Rows: {len(rows)}",
        "",
        "## Findings",
    ]
    if findings:
        lines.extend(f"- {item}" for item in findings)
        lines.extend(["", "## Result", "- `FAIL`"])
        result = 1
    else:
        lines.append("- No mismatches detected.")
        lines.extend(["", "## Result", "- `PASS`"])
        result = 0

    report = "\n".join(lines) + "\n"
    print(report)
    if args.write_evidence:
        out_dir = root / "evidence" / today
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "router_bidirectional_audit.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(root)}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
