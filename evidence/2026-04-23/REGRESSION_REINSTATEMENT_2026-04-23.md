# Regression suite reinstatement (2026-04-23)

**Run ID:** `reinstate-2026-04-23-01`

## What changed

- Restored root-level `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` (matrix **section 4** + **SCORING-v1** snapshot **section 10.5**).
- Added `tools/emit_regression_scenarios.py` to regenerate the catalog in-repo.
- Resumed dated evidence tree under `evidence/2026-04-23/`.
- `tools/scenario_audit.py` now fails closed if the scenarios file is missing.

## Verification

- `python3 tools/scenario_audit.py` — **PASS** (matrix + section 10.5).

## Linked coverage

- Implementation packet seeds: `RS-AC-*` (anti-corruption / integrity routing), `RS-VOICE-*` (political-voice restitution drills), `RS-XXV-*` (transition-phase controls), `RS-SL-*` (service-level minima placeholder).
