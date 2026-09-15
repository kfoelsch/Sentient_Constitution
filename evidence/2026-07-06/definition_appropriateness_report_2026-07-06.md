# Definition Appropriateness Audit Report

**Date:** 2026-07-06
**Workflow:** DEFINITION_APPROPRIATENESS_AUDIT
**Auditor:** Automated unified definition placement and anti-redefinition pass

## Executive Summary

| Metric | Result |
|---|---:|
| Chapter Five terms indexed | 221 |
| CJS-5 clusters indexed | 24 |
| Findings this run | 0 |
| Ledger open findings | 0 |
| Ledger stale findings | 1 |
| Regressions (resolved → reopened) | 0 |

## Findings by Check

| Check | Count |
|---|---:|

## Top Findings


## Manual Review Notes

Review CJS-5.7–5.10, 5.11–5.13, 5.16–5.18, and 5.19–5.21 cluster families for semantic adequacy.
Treat `weak_trace` and `IMPL-RELOCATION` hits as advisory unless escalation to Chapter Five is indicated.
`IMPL-RELOCATION` scopes to **CI** sections with relocation score >= 16 on operative body text (CS/CF owner layers excluded; see `ci-cjs-relocation-audit`).
Update `evidence/definition_audit/ledger.json` statuses (`accepted`, `deferred`, `resolved`) after triage.
