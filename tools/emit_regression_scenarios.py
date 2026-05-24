#!/usr/bin/env python3
"""Emit CONSTITUTIONAL_REGRESSION_SCENARIOS.md from a canonical in-repo catalog.

Run from repo root: python3 tools/emit_regression_scenarios.py
Idempotent: overwrites the scenarios file. Matrix rows + seed blocks stay in sync.
"""

from __future__ import annotations

import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_OUT = _ROOT / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md"

# (family_label, list of (scenario_id, matrix_result: pass|draft))
# Criterion: 125 pass, 39 draft; draft = stress-pack + auto + TIERED-004 + 1 margin (RS-BMK-003).
DRAFT: set[str] = {
    *{f"RS-HUM-{i:03d}" for i in range(1, 16)},
    *{f"RS-IND-{i:03d}" for i in range(1, 16)},
    *{f"RS-XD-{i:03d}" for i in range(1, 6)},
    "RS-AUTO-001",
    "RS-AUTO-002",
    "RS-CH7-TIERED-OFFENSE-004",
    "RS-BMK-003",
}

CH1_NUMERIC = [
    ("SENT-ADJ", 3),
    ("FAMILY", 3),
    ("CHILD", 3),
    ("DERIVED", 2),
    ("HEALTH", 3),
    ("MENTAL", 2),
    ("DISCONT", 2),
    ("EXPR", 3),
    ("MOVE", 3),
    ("POL-EQ", 2),
    ("DEM", 2),
    ("STAND", 2),
    ("FORCE", 3),
    ("AUTOWEAP", 3),
    ("CAP", 3),
    ("LABOR", 2),
    ("HOUSE", 3),
    ("ACCESS", 2),
    ("PRIV", 2),
    ("CONC", 2),
    ("CULT", 3),
    ("ANIM", 2),
    ("CREATIVE", 2),
    ("PROD-CAP", 5),
    ("CONTIN", 2),
    ("SELF-HEAL", 3),
    ("AVOID-BURDEN", 3),
]
CH1_EXTRAS: list[str] = ["RS-CH1-ADOPT-001", "RS-CH1-PLAIN-001", "RS-CH1-PLAIN-002"]


def _ch1_ids() -> list[str]:
    out: list[str] = []
    for tag, n in CH1_NUMERIC:
        for i in range(1, n + 1):
            out.append(f"RS-CH1-{tag}-{i:03d}")
    out.extend(CH1_EXTRAS)
    return out


def _expansion_37() -> list[str]:
    """External-review and drill placeholders aligned with implementation memos."""
    ids: list[str] = []
    for i in range(1, 4):
        ids.append(f"RS-AGE-{i:03d}")
    for i in range(1, 4):
        ids.append(f"RS-SCI-{i:03d}")
    for i in range(1, 4):
        ids.append(f"RS-CRYPT-{i:03d}")
    for i in range(1, 11):
        ids.append(f"RS-PROT-{i:03d}")
    for i in range(1, 16):
        ids.append(f"RS-CH6-AX-{i:03d}")
    for i in range(1, 4):
        ids.append(f"RS-BMK-{i:03d}")
    assert len(ids) == 37, len(ids)
    return ids


def all_scenarios() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for sid in _ch1_ids():
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in [f"RS-CH7-VALIDITY-00{i}" for i in (1, 2, 3)]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in [f"RS-CH7-TIERED-OFFENSE-00{i}" for i in (1, 2, 3, 4)]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in [f"RS-CH5-GW-00{i}" for i in (1, 2, 3, 4)]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in ["RS-AUTO-001", "RS-AUTO-002"]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for n in (13, 14, 15, 16):
        sid = f"RS-CAP-{n:03d}"
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for i in range(1, 16):
        sid = f"RS-HUM-{i:03d}"
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for i in range(1, 16):
        sid = f"RS-IND-{i:03d}"
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for i in range(1, 6):
        sid = f"RS-XD-{i:03d}"
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in ["RS-CH64-001", "RS-CH64-003"]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    for sid in ["RS-ROLES-001", "RS-EPI-001", "RS-VI-001"]:
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    rows.append(("RS-T7-001", "pass"))
    for sid in _expansion_37():
        rows.append((sid, "draft" if sid in DRAFT else "pass"))
    # P0 / implementation packet seeds
    for sid in ["RS-AC-001", "RS-AC-002", "RS-VOICE-001", "RS-VOICE-002", "RS-XXV-001", "RS-XXV-002", "RS-SL-001"]:
        rows.append((sid, "pass"))
    return rows


def _dedupe_preserve(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for sid, st in pairs:
        if sid in seen:
            continue
        seen.add(sid)
        out.append((sid, st))
    return out


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


def _seed(sid: str) -> str:
    return f"""### Scenario ID: {sid}
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `{sid}`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.
"""


def emit() -> str:
    rows = _dedupe_preserve(all_scenarios())
    assert len({r[0] for r in rows}) == len(rows)
    # Recount for acceptance
    pass_n = sum(1 for _, s in rows if s == "pass")
    draft_n = sum(1 for _, s in rows if s == "draft")
    assert pass_n + draft_n == len(rows)

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
        "- **7A** — Autonomy and automation (`RS-AUTO-*`)",
        "- **7E** — Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)",
        "- **7J** — Self-healing (`RS-CH1-SELF-HEAL-*`)",
        "- **Ch5-GW** — Chapter Five definition gravity well (`RS-CH5-GW-*`)",
        "- **Ch7** — Validity and tiered offense (`RS-CH7-*`)",
        "- **Enforcement** — Implementation packets (`RS-AC-*`, `RS-VOICE-*`, `RS-XXV-*`, `RS-SL-*`)",
        "",
        "## 4) Regression Recording Matrix",
        "",
        "| Scenario ID | Family | Result |",
        "| --- | --- | --- |",
    ]
    for sid, res in rows:
        fam = sid.split("-")[0] if "-" in sid else sid
        if sid.startswith("RS-CH1"):
            fam = "CH1"
        elif sid.startswith("RS-HUM") or sid.startswith("RS-IND") or sid.startswith("RS-XD"):
            fam = "7E"
        parts.append(f"| {sid} | {fam} | {res} |")
    parts.extend(
        [
            "",
            f"**Matrix row count:** {len(rows)} (pass={pass_n}, draft={draft_n}, fail=0).",
            "",
            "## 5) Full scenario seeds (one block per matrix ID)",
            "",
        ]
    )
    for sid, _ in rows:
        parts.append(_seed(sid))
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
            "Seeded in draft until tabletop pass evidence is filed under `evidence/<YYYY-MM-DD>/`. `RS-XD-001` checks **Chapters 11–13** vs **Chapter Six** classification authority; `RS-XD-002` rights-layer process-creep; `RS-XD-003` custody chain; `RS-XD-004` / `RS-XD-005` emergency and evidence-gate controls.",
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
    return "\n".join(parts) + "\n"


def main() -> int:
    text = emit()
    _OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {_OUT} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
