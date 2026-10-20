# Definition Appropriateness Audit Report

**Date:** 2026-10-19
**Workflow:** DEFINITION_APPROPRIATENESS_AUDIT
**Auditor:** Automated unified definition placement and anti-redefinition pass

## Executive Summary

| Metric | Result |
|---|---:|
| Chapter Five terms indexed | 283 |
| CJS-3 clusters indexed | 24 |
| Findings this run | 9 |
| Ledger open findings | 0 |
| Ledger stale findings | 24 |
| Regressions (resolved → reopened) | 0 |

## Findings by Check

| Check | Count |
|---|---:|
| IMPL-NON-REDEFINITION | 5 |
| IMPL-RELOCATION | 4 |

## Top Findings

- **IMPL-RELOCATION** `IMPL-RELOCATION:856eb46de805` — CI-4.5 @ `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:135`: Cross-layer relocation candidate (score=21; signals=joint-interface, routing-read-with, shared-procedure, forum-system-touch): Authorized roles and accountability chains
- **IMPL-RELOCATION** `IMPL-RELOCATION:a8ac8b7b6a14` — CI-4.6 @ `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:175`: Cross-layer relocation candidate (score=21; signals=joint-interface, routing-read-with, shared-procedure, forum-system-touch): Seat catalog — process-role archetypes and operational boundaries
- **IMPL-RELOCATION** `IMPL-RELOCATION:4e81a4eea369` — CI-4.7 @ `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:287`: Cross-layer relocation candidate (score=24; signals=joint-interface, routing-read-with, shared-procedure, dependency-failure, forum-system-touch): Practice licence, practice clearance, and joint professional practice
- **IMPL-RELOCATION** `IMPL-RELOCATION:9e1464a23078` — CI-27.5 @ `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:108`: Cross-layer relocation candidate (score=16; signals=routing-read-with, dependency-failure, forum-system-touch): Remedy parity and capacity-failure interface
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:d1c06a06dfe7` — System @ `corpus_systems/cs_04_critical_system_stewardship.md:71`: Possible competing definition prose for canonical term: - **It stewards a Class A or Class B system:** to steward a system means to operate, govern, recover, or hold material authority over it.
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:cfee7a889fb6` — Dependency @ `corpus_systems/cs_04_critical_system_stewardship.md:73`: Possible competing definition prose for canonical term: - **It stewards a Class C system or dependency and meets at least one relationship indicator below:** this is the "gated Class C" case. It usually means the org
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:80fade76411c` — Sentient @ `corpus_institutions/ci_00_registry_and_reading_rules.md:59`: Possible competing definition prose for canonical term: Apply **CJS-1.1** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this folder specifically, headings use 
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:258744362a1d` — Institution @ `corpus_institutions/ci_05_conflict_integrity_anti_capture_anti_corruption.md:76`: Possible competing definition prose for canonical term: *In plain terms: each institution must write down who does what when honesty or independence is at stake — not leave it implied. That means a published map of a
- **IMPL-NON-REDEFINITION** `IMPL-NON-REDEFINITION:1a3e05feceb7` — Sentient @ `corpus_forum/cf_00_registry_and_reading_rules.md:64`: Possible competing definition prose for canonical term: Apply **CJS-1.1** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this file specifically, headings use **

## Manual Review Notes

Review CJS-3.7–5.10, 5.11–5.13, 5.16–5.18, and 5.19–5.21 cluster families for semantic adequacy.
Treat `weak_trace` and `IMPL-RELOCATION` hits as advisory unless escalation to Chapter Five is indicated.
`IMPL-RELOCATION` scopes to **CI** sections with relocation score >= 16 on operative body text (CS/CF owner layers excluded; see `ci-cjs-relocation-audit`).
Update `evidence/definition_audit/ledger.json` statuses (`accepted`, `deferred`, `resolved`) after triage.
