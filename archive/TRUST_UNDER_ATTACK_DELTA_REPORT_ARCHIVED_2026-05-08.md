# Trust Under Attack Delta Report

Date: 2026-04-08  
Scope: Constitutional readiness under coordinated adversarial pressure using existing regression scenarios and recorded run notes.

## Method

- Baseline signal: prior constitutional ticket completion plus pre-Protocol-R/Protocol-D control **assumptions** inferred from earlier scenario packs and definitions.
- Validation signal: tabletop and evidence-backed runs recorded in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md`.
- Scale: residual risk score from 1 (low) to 5 (high).

## Residual Risk Scoring (Before vs After)

1. Coordinated multi-system compromise  
   - Before R/D: 5  
   - After R validation: 3  
   - Evidence hooks: `RS-CAPR-*`, `RS-SUBV-001`, run notes `v2026-04-08-tabletop-03`, `v2026-04-08-operational-05`, `v2026-04-08-tabletop-05`

2. Partition exploitation and governance fork drift  
   - Before R/D: 4  
   - After D validation: 2  
   - Evidence hooks: `RS-DECP-*`, run notes `v2026-04-08-tabletop-04`, `v2026-04-08-operational-07` through `-10`

3. Epistemic capture during crisis  
   - Before R/D: 4  
   - Current (post existing CAP/R runs): 3  
   - Evidence hooks: `RS-CAP-005`, `RS-CAP-007`, `RS-CAPR-007`, run notes `v2026-04-08-operational-02`, `-03`, `-06`

4. Steward and credential-plane capture  
   - Before R/D: 4  
   - Current (post R/D codification + tabletop): 3  
   - Evidence hooks: `RS-SUBV-002`, Protocol R section 3/4, Protocol D section 5, run note `v2026-04-08-tabletop-05`

5. Cross-jurisdiction and supply-chain evasion under active attack  
   - Before R/D: 4  
   - Current (post codification + tabletop): 3  
   - Evidence hooks: `RS-CAPR-006`, `RS-SUBV-003`, Protocol R section 5, Protocol C cross-jurisdiction controls, run note `v2026-04-08-tabletop-05`

## Net Delta

- Highest-risk class moved from 5 to 3 with Protocol R activation and reconstitution controls.
- Partition-resilience class moved from 4 to 2 with Protocol D continuity and reconciliation controls.
- Remaining major residuals are operational, not definitional: evidence-backed execution depth for newly added `RS-SUBV-*` drills.

## Open Gaps

- Complete and record planned drills:
  - `v2026-04-08-operational-11` (`RS-SUBV-001`)
  - `v2026-04-08-operational-12` (`RS-SUBV-002`)
  - `v2026-04-08-operational-13` (`RS-SUBV-003`)
- Add one explicit reversible-decision red-team drill under high uncertainty/disinformation pressure.
