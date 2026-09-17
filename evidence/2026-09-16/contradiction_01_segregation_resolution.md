# Contradiction 1: verification and record entry

**Date:** 2026-09-16. **Edition:** SC-Corpus-2026.08.09, pre-release. **Status:** working-tree correction; not adoption or publication.

This resolves finding 1 of the [conceptual-overview alignment review](conceptual_overview_corpus_alignment_review.md). The review and its source snapshot describe the earlier state.

The controlling rule remains [Chapter One §10.2, Segregation of Duties](../../core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties): verification cannot be combined with record entry or review of the same act. The overview already reflects that rule.

The correction makes the record lifecycle consistent:

1. The record-opening authority verifies the facts and authorizes opening or changing the record.
2. A separate record custodian enters the authorized version and holds it.
3. A challenge goes to the independent contest seat or competent review forum.

Small communities retain the existing disinterested-relying-body route. One relying body may host separate verification and custody offices under its published lane map and independence safeguards. The same office or sentient cannot perform both duties on the same record. Formal institutional status is still not the qualification test, and informal work still requires no standing record merely because it could be recorded.

## Changes

- [Chapter Eight §§3.1 and 3.7](../../core_08_standing_assessment.md#37-segregation-of-duties): distinguish authorization from entry, remove the small-scope exception, and correct the watershed example and explanatory wording.
- [CI-3.6](../../corpus_institutions/ci_03_institutional_design_separation_of_powers.md): give the charter's verification and custody fields the same division of duties.
- [CI-22](../../corpus_institutions/ci_22_commons_cooperatives_mutual_aid_non_market_governance.md): remove the permission for the custodian to verify the same record.
- [CJS-3.11](../../corpus_joint_structure/cjs_03a_accountability_operations.md#constitutional-lane-and-functional-separation): make the failure test reject prohibited pairings even when a merged-hosting safeguard is published.

No change was made to Chapter One's substantive prohibition or the overview. Generated AI-corpus indexes were refreshed through the repository generator; their regeneration also reflects other changes already present in the working tree.

## Verification

The affected provisions were read together against Chapter One, CI-3.2, and CI-4.6. A search of the current English source and implementation material found no remaining instances of the removed permission or the identified wording that made the verifier also enter the record. Historical evidence and translations were excluded from that search; this correction does not certify translation alignment.

Full regression was run before and after the substantive change. Eleven targets failed before the change; ten still failed after index regeneration. Manifest freshness was repaired. Two citation-title diagnostics surfaced on edited lines and were corrected; rerunning that audit returned exactly its three pre-existing findings in other files.

The remaining failing targets are section-label-anchor-audit, section-label-anchor-audit-test, section-cite-name-audit, fossil-anchor-audit, fossil-anchor-audit-test, corpus-markdown-audit, nav-widget-spacer-audit, ch5-entry-format-audit, lexical-vocabulary-audit, and id-resolver-test. This is not a claim that the repository's full regression suite passes.

The next review item is the incorrect substantive chapter and article references. That item requires checking the current source again because other work is present in this shared working tree.
