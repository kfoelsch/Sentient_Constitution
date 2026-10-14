#!/usr/bin/env python3
"""Emit project/CONSTITUTIONAL_REGRESSION_SCENARIOS.md from tools/architecture/regression_scenarios.json.

Run from repo root:
  python3 tools/emit_regression_scenarios.py          # write the file
  python3 tools/emit_regression_scenarios.py --check  # exit 1 if the file differs from the catalog

The JSON catalog is the source of truth for the family index, the matrix rows, and the
scenario blocks. Edit the catalog, not the generated file. Link targets in the catalog
are written relative to project/, exactly as they appear in the generated file.
The emitter holds only the fixed prose (purpose, how to record a run, placeholders,
and the scoring snapshot).
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_OUT = _ROOT / "project" / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md"
_CATALOG = _ROOT / "tools" / "architecture" / "regression_scenarios.json"

RESULTS = ("pass", "draft", "fail")


def load_catalog(path: pathlib.Path = _CATALOG) -> dict:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    rows = catalog["rows"]
    blocks = catalog["blocks"]
    row_ids = [r[0] for r in rows]
    block_ids = [b["id"] for b in blocks]
    if len(set(row_ids)) != len(row_ids):
        raise ValueError("duplicate matrix row id in catalog")
    if len(set(block_ids)) != len(block_ids):
        raise ValueError("duplicate scenario block id in catalog")
    missing = [i for i in row_ids if i not in set(block_ids)]
    if missing:
        raise ValueError(f"matrix rows without a scenario block: {missing}")
    bad = [r for r in rows if r[2] not in RESULTS]
    if bad:
        raise ValueError(f"matrix rows with an unknown result: {bad}")
    return catalog


def _snapshot_block() -> str:
    # SCORING-v1: uniform 8.4 on six dimensions
    return """- Scoring model version: `SCORING-v1`
- Scenario-Weighted Score (0-10): `8.4`
- Rights Floor Integrity (0-10): `8.4`
- Contestability / Appeal Practicality (0-10): `8.4`
- Enforcement / Remedy Realism (0-10): `8.4`
- Boundary Discipline (0-10): `8.4`
- Epistemic Integrity (0-10): `8.4`
- Continuity / Recovery (0-10): `8.4`
- Delta vs prior comparable run: `Reinstated 2026-04-23 after 2026-04-17 token-reduction suspension; snapshot reset to single baseline.`
- Confidence: `medium`"""


def _block(b: dict) -> str:
    return (
        f"### Scenario ID: {b['id']}\n"
        f"- **Class:** {b['class']}\n"
        f"- **Summary:** {b['summary']}\n"
        f"- **Read with:** {b['read_with']}\n"
    )


def emit(catalog: dict | None = None) -> str:
    catalog = catalog or load_catalog()
    rows = catalog["rows"]
    counts = {r: sum(1 for row in rows if row[2] == r) for r in RESULTS}

    parts: list[str] = [
        "# CONSTITUTIONAL_REGRESSION_SCENARIOS",
        "",
        "Authoritative process artifact for the Sentient Constitution corpus. Matrix rows in **section 4** must each have a **Scenario ID** block somewhere in this file. **Section 10.5** records the latest **SCORING-v1** run snapshot; weighted overall must match the six dimension scores (`tools/scoring_v1.py`).",
        "",
        "## 1) Purpose and scope",
        "",
        "Regression seeds document adversarial and core paths against constitutional owner layers. They do **not** change constitutional meaning on their own.",
        "",
        "## 2) How to record a run",
        "",
        "1. Update the matrix row (section 4) for each exercised ID.",
        "2. Add or update evidence under `evidence/<YYYY-MM-DD>/` with run identifier.",
        "3. When publishing a new weighted snapshot, run `python3 tools/scoring_v1.py` with the six dimension scores and copy the block into **section 10.5**.",
        "",
        "## 3) Section index (families)",
        "",
        *catalog["families"],
        "",
        "## 4) Regression Recording Matrix",
        "",
        "| Scenario ID | Family | Result |",
        "| --- | --- | --- |",
    ]
    for sid, fam, res in rows:
        parts.append(f"| {sid} | {fam} | {res} |")
    parts.extend(
        [
            "",
            f"**Matrix row count:** {len(rows)} (pass={counts['pass']}, draft={counts['draft']}, fail={counts['fail']}).",
            "",
            "## 5) Full scenario seeds (one block per matrix ID)",
            "",
        ]
    )
    for b in catalog["blocks"]:
        parts.append(_block(b))
    parts.extend(
        [
            "",
            "## 6) Scoring and evaluation",
            "",
            "Weighted model **SCORING-v1** is defined in `tools/scoring_v1.py`. The audit does not recompute a tabletop score; it validates internal consistency of the **authored** snapshot.",
            "",
            "## 7) Optional section placeholders",
            "",
            "Historical subsection labels (*7A.1*, *7E*, etc.) refer to the families above. Detailed narratives may be expanded per drill without moving owner-layer law.",
            "",
            "### 7E) Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)",
            "",
            "Seeded in draft until tabletop pass evidence is filed under `evidence/<YYYY-MM-DD>/`. `RS-XD-001` checks **Chapters 13–14** vs **Chapter Ten** measurement authority; `RS-XD-002` rights-layer process-creep; `RS-XD-003` custody chain; `RS-XD-004` / `RS-XD-005` emergency and evidence-gate controls.",
            "",
            "## 8) (Reserved)",
            "",
            "## 9) (Reserved)",
            "",
            "## 10) Latest scoring snapshot (authoritative for audits)",
            "",
            "### 10.5 Run Scoring Snapshot (SCORING-v1)",
            "",
            _snapshot_block(),
            "",
        ]
    )
    return "\n".join(parts).rstrip("\n") + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if the generated file differs from the catalog")
    args = ap.parse_args(argv)
    try:
        text = emit()
    except ValueError as exc:
        print(f"emit_regression_scenarios: {exc}", file=sys.stderr)
        return 1
    if args.check:
        current = _OUT.read_text(encoding="utf-8") if _OUT.exists() else ""
        if current != text:
            print(f"emit_regression_scenarios: {_OUT} differs from the catalog; run tools/emit_regression_scenarios.py", file=sys.stderr)
            return 1
        print("emit_regression_scenarios: generated file matches the catalog")
        return 0
    _OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {_OUT} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
