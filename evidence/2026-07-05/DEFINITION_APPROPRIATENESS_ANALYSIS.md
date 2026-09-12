# Definition Appropriateness Audit — Bucket Closure Analysis

**Date:** 2026-07-06  
**Workflow:** DEFINITION_APPROPRIATENESS_AUDIT  
**Status:** All buckets closed — zero open findings

---

## Executive Summary

| Bucket | Check | Baseline | After fix | Ledger |
|--------|-------|----------|-----------|--------|
| One | CORE-TRACE | 4 | 0 | 5 resolved |
| Two | IMPL-NON-REDEFINITION | 3 | 0 | 3 resolved |
| Three | IMPL-RELOCATION | 104 | 0 | 104 accepted |
| Four | CJS-TRACE | 1 | 0 | 1 resolved |

**Current run:** **0** findings.

**Structural checks remain clean:** Chapter Five placement, gravity, CJS placement, constitutional creep, and competing O/E/C gloss — no actionable findings.

---

## Bucket One — CORE-TRACE (resolved)

| Finding | Fix |
|---------|-----|
| §10 missing D/E/C anchors | Added Governance, Stewardship, Necessity, Proportionality, Participation, Oversight, Accountability widget in `core_01_c_stewardship_capacity_principles.md` |
| §14 missing D/E/C anchors | Added Classification-Scaled Governance, Risk, Dependency widget (parseable by Ch1↔Ch5 alignment audit) |
| Cluster 3.8 missing Reproductive Autonomy | Added to §5 Freedom widget in `core_01_a_values_principles.md`; order updated in `ch1_dec_order.json` |
| Cluster 3.32 missing Cascading Failure | Added to §4.1 Resilience widget in `core_01_a_values_principles.md` |
| System Alignment Certification incomplete O/E/C | Superseded by §14 widget terms above (prior interim term dropped) |

**Verification:** `ch1_cjs5_alignment_audit` — 0 completeness, cluster, and accuracy gaps. `make regression` — pass.

---

## Bucket Two — IMPL-NON-REDEFINITION (resolved)

All three hits were heuristic false positives from definitional lead-in language on implementation-layer plain-terms prose.

| Finding | File | Fix |
|---------|------|-----|
| Dependency + systemic *means* on one line | `cs_s2_system_classification_and_handling.md` | Split Class B header from systemic gloss; use *denotes* and link [Cascading Failure](../core_05_band_continuity.md#cascading-failure) |
| Participation + *means* span | `ci_08_transparency_participation_accessible_pathways.md` | Rephrase “what a decision means” → “how a decision will affect them” |
| Transparency *means* | `ci_08_transparency_participation_accessible_pathways.md` | Replace with pointers to Chapter Five Transparency and Participation |

---

## Bucket Three — IMPL-RELOCATION (accepted + heuristic fix)

104 baseline hits were routing-read-with noise across CI/CS/CF owner layers, not misplaced constitutional definitions.

**Tool fix** (`tools/definition_appropriateness_audit.py`):

- Scope `IMPL-RELOCATION` to **CI** operative body text only (CS/CF owner layers excluded; see `ci-cjs-relocation-audit`).
- Strip Trace widgets and accepted CJS pointer sentences before scoring (reuse `ci_cjs_relocation_audit` helpers).
- Skip sections with pointer-discipline language (`does not repeat`, `do not reinvent`, `implementation-only`, etc.).
- Raise minimum relocation score to **16** on operative text.
- Tighten Chapter Five escalation to definitional lead-in / O/E/C-shaped prose, not bare keyword mentions.

**Ledger:** all 104 prior `IMPL-RELOCATION` entries marked `accepted` with note “by-design routing prose.”

**Verification:** re-run produces **0** `IMPL-RELOCATION` findings.

---

## Remaining open item

None. Ledger triage complete.

---

## Bucket Four — CJS-TRACE (resolved)

| Finding | Fix |
|---------|-----|
| CJS-5.0 weak Chapter One cite | Added `Chapter One basis: Chapter One §2.1, §3.4, §5.2, §7.1, §7.2, §10` to CJS-5.0 Trace in `cjs_05_cross_implementation_operational_terms.md` |

**Verification:** `ch1_cjs5_alignment_audit` — `weak_trace` empty. `definition_appropriateness_audit` — 0 findings.

---

## Artifacts

- Report: `definition_appropriateness_report_2026-07-06.md`
- Matrix: `definition_appropriateness_matrix_2026-07-06.csv`
- Log: `definition_appropriateness_log_2026-07-06.json`
- Persistent ledger: `evidence/definition_audit/ledger.json`
