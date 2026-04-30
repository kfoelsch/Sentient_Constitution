#!/usr/bin/env python3
"""Regression check for CONSTITUTIONAL_REGRESSION_SCENARIOS.md: matrix + full SCORING-v1 snapshot.

1. Section **4) Regression Recording Matrix** — Pass/Fail/Draft counts and basic integrity.
2. Section **10.5** — latest **Run Scoring Snapshot**: six 0–10 dimensions, model `SCORING-v1`,
   delta, confidence, and **Scenario-Weighted Score** matching `tools/scoring_v1.py` weights.

Missing file is a hard failure (exit 1). Regenerate the catalog with `python3 tools/emit_regression_scenarios.py`
if the repository omits the scenarios file.

One command, one file: `make regression` runs this as `scenario-audit`.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

_TOOLS_DIR = pathlib.Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))
from scoring_v1 import overall  # noqa: E402


MATRIX_START_RE = re.compile(r"^##\s+4\)\s+Regression Recording Matrix\s*$")
NEXT_SECTION_RE = re.compile(r"^##\s+")
ROW_RE = re.compile(r"^\|(.+)\|\s*$")
SCENARIO_ID_RE = re.compile(r"^###\s+Scenario ID:\s*(RS-[A-Z0-9-]+)\s*$")

SECTION_105_HEADER = re.compile(r"^###\s+10\.5\b.*$")
SNAPSHOT_LINE_RES: list[tuple[str, re.Pattern[str]]] = [
    ("model", re.compile(r"^-\s*Scoring model version:\s*`([^`]+)`\s*$")),
    ("overall_stated", re.compile(r"^-\s*Scenario-Weighted Score \(0-10\):\s*`([0-9.]+)`\s*$")),
    ("rights", re.compile(r"^-\s*Rights Floor Integrity \(0-10\):\s*`([0-9.]+)`\s*$")),
    (
        "contestability",
        re.compile(r"^-\s*Contestability / Appeal Practicality \(0-10\):\s*`([0-9.]+)`\s*$"),
    ),
    ("enforcement", re.compile(r"^-\s*Enforcement / Remedy Realism \(0-10\):\s*`([0-9.]+)`\s*$")),
    ("boundary", re.compile(r"^-\s*Boundary Discipline \(0-10\):\s*`([0-9.]+)`\s*$")),
    ("epistemic", re.compile(r"^-\s*Epistemic Integrity \(0-10\):\s*`([0-9.]+)`\s*$")),
    ("continuity", re.compile(r"^-\s*Continuity / Recovery \(0-10\):\s*`([0-9.]+)`\s*$")),
    ("delta", re.compile(r"^-\s*Delta vs prior comparable run:\s*(.+?)\s*$")),
    ("confidence", re.compile(r"^-\s*Confidence:\s*`?(low|medium|high)`?\s*$", re.IGNORECASE)),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path. Defaults to current directory.",
    )
    parser.add_argument(
        "--file",
        default="CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
        help="Scenario specification file to audit.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on non-Pass matrix results (including draft and partial).",
    )
    return parser.parse_args()


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def extract_defined_ids(text: str) -> set[str]:
    defined: set[str] = set()
    for line in text.splitlines():
        match = SCENARIO_ID_RE.match(line.strip())
        if match:
            defined.add(match.group(1))
    return defined


def extract_matrix_rows(lines: list[str]) -> list[list[str]]:
    in_matrix = False
    rows: list[list[str]] = []
    for raw in lines:
        line = raw.rstrip()
        if not in_matrix:
            if MATRIX_START_RE.match(line):
                in_matrix = True
            continue

        if NEXT_SECTION_RE.match(line):
            break
        row_match = ROW_RE.match(line)
        if not row_match:
            continue

        cells = [cell.strip() for cell in row_match.group(1).split("|")]
        if not cells:
            continue
        if cells[0] == "Scenario ID" or cells[0].startswith("---"):
            continue
        rows.append(cells)
    return rows


def extract_section_105_lines(lines: list[str]) -> list[str] | None:
    start = None
    for i, line in enumerate(lines):
        if SECTION_105_HEADER.match(line.strip()):
            start = i + 1
            break
    if start is None:
        return None
    out: list[str] = []
    for j in range(start, len(lines)):
        if lines[j].startswith("## ") and not lines[j].startswith("###"):
            break
        out.append(lines[j])
    return out


def parse_run_snapshot(section_lines: list[str]) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    found: dict[str, str] = {}
    for key, pattern in SNAPSHOT_LINE_RES:
        m = None
        for line in section_lines:
            m = pattern.match(line.rstrip())
            if m:
                break
        if not m:
            errors.append(f"Missing or malformed snapshot field: {key}")
            continue
        if key == "delta":
            found[key] = m.group(1).strip()
        elif key == "confidence":
            found[key] = m.group(1).lower()
        else:
            found[key] = m.group(1)
    return found, errors


def validate_snapshot_scores(found: dict[str, str], errors: list[str]) -> None:
    if found.get("model") != "SCORING-v1":
        errors.append(
            f"Scoring model must be SCORING-v1, got {found.get('model', '')!r}"
        )

    dims = ("rights", "contestability", "enforcement", "boundary", "epistemic", "continuity")
    scores: dict[str, float] = {}
    for d in dims:
        raw = found.get(d)
        if raw is None:
            continue
        try:
            v = float(raw)
        except ValueError:
            errors.append(f"Non-numeric dimension {d}: {raw!r}")
            continue
        if not 0.0 <= v <= 10.0:
            errors.append(f"Dimension {d} out of range [0, 10]: {v}")
        scores[d] = v

    if len(scores) != 6:
        return

    computed = overall(scores)
    stated_raw = found.get("overall_stated")
    if stated_raw is None:
        return
    try:
        stated = float(stated_raw)
    except ValueError:
        errors.append(f"Non-numeric stated overall: {stated_raw!r}")
        return
    if round(computed, 1) != round(stated, 1):
        errors.append(
            f"Scenario-Weighted Score mismatch: stated {stated:.2f}, "
            f"computed from dimensions {computed:.2f} (SCORING-v1 weights)"
        )


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    path = root / args.file
    if not path.is_file():
        print(
            f"Missing required regression file: {path} "
            f"(create or regenerate: `python3 tools/emit_regression_scenarios.py`)",
            file=sys.stderr,
        )
        return 1
    text = load_text(path)
    lines = text.splitlines()

    exit_code = 0

    print("Regression scenarios:")
    print(f"- File: {args.file}")

    rows = extract_matrix_rows(lines)
    if not rows:
        print("- Matrix: FAIL (no rows in section '4) Regression Recording Matrix')")
        return 1

    defined_ids = extract_defined_ids(text)

    pass_count = 0
    partial_count = 0
    fail_count = 0
    draft_count = 0
    unknown_count = 0
    malformed_rows: list[str] = []
    missing_definitions: set[str] = set()

    for row in rows:
        if len(row) < 3:
            malformed_rows.append(" | ".join(row))
            continue
        scenario_id = row[0]
        result = row[2].strip().lower()

        if not scenario_id.startswith("RS-"):
            unknown_count += 1

        if result == "pass":
            pass_count += 1
        elif result == "partial":
            partial_count += 1
        elif result == "fail":
            fail_count += 1
        elif result == "draft":
            draft_count += 1
        else:
            unknown_count += 1

        if scenario_id.startswith("RS-") and scenario_id not in defined_ids:
            missing_definitions.add(scenario_id)

    matrix_issues: list[str] = []
    if malformed_rows:
        matrix_issues.append(f"Malformed matrix rows: {len(malformed_rows)}")
    if fail_count > 0:
        matrix_issues.append(f"Fail results present: {fail_count}")
    if pass_count == 0:
        matrix_issues.append("No Pass results present")

    if args.strict and (partial_count > 0 or draft_count > 0):
        matrix_issues.append(
            f"Strict mode rejects non-Pass rows: partial={partial_count}, draft={draft_count}"
        )
    if missing_definitions:
        matrix_issues.append(
            f"Matrix IDs without local seed blocks: {len(missing_definitions)}"
        )

    print("- Matrix:")
    print(f"  - Rows: {len(rows)}; pass={pass_count}, partial={partial_count}, fail={fail_count}, draft={draft_count}, unknown={unknown_count}")
    print(f"  - Defined Scenario IDs (seed blocks): {len(defined_ids)}")
    if matrix_issues:
        print("  - Result: FAIL")
        if missing_definitions:
            preview = ", ".join(sorted(missing_definitions)[:10])
            suffix = " ..." if len(missing_definitions) > 10 else ""
            print(
                f"    - Matrix IDs without local seed blocks ({len(missing_definitions)}): {preview}{suffix}"
            )
        for issue in matrix_issues:
            if issue.startswith("Matrix IDs without local seed blocks:"):
                continue
            print(f"    - {issue}")
        exit_code = 1
    else:
        print("  - Result: PASS")

    snap_issues: list[str] = []
    found: dict[str, str] = {}
    sec105 = extract_section_105_lines(lines)
    if not sec105:
        snap_issues.append("Missing ### 10.5 (latest Run Scoring Snapshot / SCORING-v1).")
    else:
        found, parse_errs = parse_run_snapshot(sec105)
        snap_issues.extend(parse_errs)
        validate_snapshot_scores(found, snap_issues)

    print("- Evaluation (SCORING-v1 snapshot, section 10.5):")
    if snap_issues:
        print("  - Result: FAIL")
        for issue in snap_issues:
            print(f"    - {issue}")
        exit_code = 1
    else:
        print("  - Result: PASS")
        # Regression validates the authored snapshot in the scenarios file; echo it so a
        # green run still surfaces the current scores (they are not computed here).
        ov = found.get("overall_stated", "?")
        print(f"  - Scenario-Weighted Score: {ov} (`{found.get('model', '?')}`)")
        print(
            "  - Dimensions: "
            f"rights {found.get('rights', '?')}, "
            f"contestability {found.get('contestability', '?')}, "
            f"enforcement {found.get('enforcement', '?')}, "
            f"boundary {found.get('boundary', '?')}, "
            f"epistemic {found.get('epistemic', '?')}, "
            f"continuity {found.get('continuity', '?')}"
        )
        print(
            f"  - Delta: {found.get('delta', '?')}; "
            f"confidence: {found.get('confidence', '?')}"
        )

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
