# Definition Appropriateness Audit Report

**Date:** 2026-10-25
**Workflow:** DEFINITION_APPROPRIATENESS_AUDIT
**Auditor:** Automated unified definition placement and anti-redefinition pass

## Executive Summary

| Metric | Result |
|---|---:|
| Chapter Five terms indexed | 289 |
| CJS operational cluster clusters indexed | 22 |
| Findings this run | 13 |
| Ledger open findings | 13 |
| Ledger stale findings | 24 |
| Regressions (resolved → reopened) | 0 |

## Findings by Check

| Check | Count |
|---|---:|
| CORE-PLACEMENT | 2 |
| IMPL-NON-REDEFINITION | 5 |
| IMPL-RELOCATION | 6 |

## Top Findings

- **CORE-PLACEMENT** `CORE-PLACEMENT:925bd9e62ec6` — (Chapter Five structure) @ `tools/ch5_single_definition_audit.py:0`: FAIL: Chapter Five single-definition audit detected issues:
- **CORE-PLACEMENT** `CORE-PLACEMENT:61ba14caf203` — (Chapter Five structure) @ `core_05.000_definitions_home.md:141: Definitions A-Z row 'Combatant / Non-Combatant Distinction' should sort before 'Commercial Compliance':0`: core_05.000_definitions_home.md:141: Definitions A-Z row 'Combatant / Non-Combatant Distinction' should sort before 'Commercial Compliance'
- **IMPL-RELOCATION** `IMPL-RELOCATION:7586fc626554` — CI-6.205 @ `corpus_institutions/ci_06.205_transparency_participation_accessible_pathways.md:178`: Cross-layer relocation candidate (score=16; signals=routing-read-with, shared-procedure, dependency-failure, forum-system-touch): §3: Digital self-service pathway integrity
- **IMPL-RELOCATION** `IMPL-RELOCATION:31b4ee81ac37` — CI-11.205 @ `corpus_institutions/ci_11.205_remedy_systems_institutional_redress_capacity.md:127`: Cross-layer relocation candidate (score=16; signals=routing-read-with, dependency-failure, forum-system-touch): §5: Remedy parity and capacity-failure interface
- **IMPL-RELOCATION** `IMPL-RELOCATION:24daeea80cb8` — CI-11.215 @ `corpus_institutions/ci_11.215_institutional_accountability_sanctions.md:87`: Cross-layer relocation candidate (score=19; signals=joint-interface, routing-read-with, shared-procedure, dependency-failure, forum-system-touch): §2: Contraction order
- **IMPL-RELOCATION** `IMPL-RELOCATION:834cdf95ee79` — CI-14.205 @ `corpus_institutions/ci_14.205_appointment_competency_rotation_removal.md:181`: Cross-layer relocation candidate (score=21; signals=joint-interface, routing-read-with, shared-procedure, forum-system-touch): §5: Authorized roles and accountability chains
- **IMPL-RELOCATION** `IMPL-RELOCATION:e6ec399103db` — CI-14.205 @ `corpus_institutions/ci_14.205_appointment_competency_rotation_removal.md:226`: Cross-layer relocation candidate (score=25; signals=joint-interface, routing-read-with, shared-procedure, forum-system-touch): §6: Seat catalog — process-role archetypes and operational boundaries
- **IMPL-RELOCATION** `IMPL-RELOCATION:a47f46b1bcb1` — CI-14.205 @ `corpus_institutions/ci_14.205_appointment_competency_rotation_removal.md:361`: Cross-layer relocation candidate (score=24; signals=joint-interface, routing-read-with, shared-procedure, dependency-failure, forum-system-touch): §7: Practice licence, practice clearance, and joint professional practice
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:4f67c513e36c` — System @ `corpus_systems/cs_14.305_critical_system_stewardship.md:100`: Possible competing definition prose for canonical term: - **It stewards a Class A or Class B system:** to steward a system means to operate, govern, recover, or hold material authority over it.
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:36f80e229c9b` — Dependency @ `corpus_systems/cs_14.305_critical_system_stewardship.md:102`: Possible competing definition prose for canonical term: - **It stewards a Class C system or dependency and meets at least one relationship indicator below:** this is the "gated Class C" case. It usually means the org
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:5cc8647cc0be` — Sentient @ `corpus_institutions/ci_00.205_registry_and_reading_rules.md:68`: Possible competing definition prose for canonical term: Apply **CJS-0.110 §1** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this folder specifically, headings
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:9176e2a5d77e` — Independence @ `corpus_institutions/ci_08.210_conflict_integrity_anti_capture_anti_corruption.md:100`: Possible competing definition prose for canonical term: *In plain terms: each institution must write down who does what when honesty or independence is at stake — not leave it implied. That means a published map of a
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:8da526635067` — Sentient @ `corpus_forum/cf_00.405_registry_and_reading_rules.md:74`: Possible competing definition prose for canonical term: Apply **CJS-0.110 §1** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this file specifically, headings u

## Manual Review Notes

Review CJS-5.120 §7–5.10, 5.11–5.13, 5.16–5.18, and 5.19–5.21 cluster families for semantic adequacy.
Treat `weak_trace` and `IMPL-RELOCATION` hits as advisory unless escalation to Chapter Five is indicated.
`IMPL-RELOCATION` scopes to **CI** sections with relocation score >= 16 on operative body text (CS/CF owner layers excluded; see `ci-cjs-relocation-audit`).
Update `evidence/definition_audit/ledger.json` statuses (`accepted`, `deferred`, `resolved`) after triage.
