# Plan: identifying the whole-project evaluation hesitations — 2026-11-15

This page is **process support**, not constitutional text. It cannot change or narrow what the numbered `core_*` files say. It plans how to pin down the six hesitations listed in [TODO.md](../../TODO.md) under *Whole-project evaluation — open hesitations (Claude review, 2026-11-15)*. It does not resolve them and authorizes no edit to core text.

**Aim:** turn each hesitation from an impression into a precise finding: a confirmed gap, something the text already handles, or a design choice that needs the custodian's decision.

**Starting limit:** all six were raised from the README, START_HERE, VISION, the conceptual overview, the Rights Floor sheet, and the *In plain terms* glosses. The reviewer did not read the full core. Step 2 below exists to correct for that.

## 1. Method for every issue

1. **State it as a question with a pass condition.** Example: "Can a creator pause a derived system whose sentience is unresolved? Pass means a cited rule says yes, by whom, and for how long."
2. **Verify against the operative text.** Read the full sections and their implementation files, not the glosses.
3. **Attack it with fact patterns.** Write two or three scenarios per issue and route them through the text, as the existing stress packs do.
4. **Get an independent read.** Run the same scenarios in a fresh session without the preparer's analysis, ideally on a different model family, plus one human reader.
5. **Classify the result.** Each finding is one of: text gap, internal contradiction, deliberate choice to defend, or announcement wording only.

## 2. What to do per issue

| Issue | How to pin it down |
|---|---|
| **Instances and the foundational vote** | Search the whole corpus for how a "sentient" is individuated. Scenarios: one model with 10,000 instances at ratification; a fork the day before a vote; a merge after. |
| **Derived sentients and correction of AI systems** | Trace Articles VI-B, VII-B, VIII-C, XVII, and XX-B, plus the emergency rules in Chapter Twenty-Three §6.1. Scenarios: a misaligned derived system before adjudication; a system that falsely claims sentience. |
| **Contested policy entrenched as Rights Floor** | Inventory every number and specific policy choice in Chapter Six. Run one mock amendment (the 30-year creative term to 20) through Chapters Twenty-Six and Twenty-Seven and record who decides whether it is a weakening. |
| **Standing records as measurement infrastructure** | List the steps an adopter would take to build a social score: aggregate, rank, share across adopters, condition services. Find the rule that blocks each step, then check the implementation files for leaks. |
| **Scale against comprehensibility** | Give three cold readers the 15-minute path and five questions. Separately, compute the smallest set of sections needed to resolve the existing vignettes. |
| **Unproven under pressure** | Audit the announcement copy line by line and mark each claim as evidenced, designed, or aspirational. |

## 3. Order

1. Instances and the vote; correction of AI systems. Cheap to check, and the two most likely to be raised by a hostile first reader.
2. Entrenched policy; standing records.
3. Scale; unproven claims. These depend on the final text.

## 4. Output

Each issue ends with a short finding record (question, sources read, scenarios, independent read, classification) and an update to its `TODO.md` item.

## 5. Status

- **Instances and the vote:** steps 1, 2, 3, and 5 done on 2026-11-15. Classified as a text gap. Record: [hesitation_instances_foundational_vote_finding_2026-11-15.md](../reviews/hesitation_instances_foundational_vote_finding_2026-11-15.md). Step 4 (independent read) and the custodian's decisions are open. Draft text for the counting unit, branches, and merges: [distinct_subject_criteria_draft_2026-11-15.md](distinct_subject_criteria_draft_2026-11-15.md) (for review; not in core).
- **Derived sentients and correction of AI systems:** steps 1, 2, 3, and 5 done on 2026-11-15. Classified as mostly handled by the text, with one deliberate choice to defend and three text gaps in the contested period. Record: [hesitation_derived_sentients_ai_correction_finding_2026-11-15.md](../reviews/hesitation_derived_sentients_ai_correction_finding_2026-11-15.md). Step 4 (independent read) and the custodian's decisions are open.
- **Contested policy entrenched as Rights Floor:** steps 1, 2, 3, and 5 done on 2026-11-15. Classified as mostly a reading problem (the numbers are caps), with two text gaps (two-sided trade-offs; no named decider) and one deliberate choice to defend (Articles VII-D and VII-E). Record: [hesitation_entrenched_policy_rights_floor_finding_2026-11-15.md](../reviews/hesitation_entrenched_policy_rights_floor_finding_2026-11-15.md). Step 4 (independent read) and the custodian's decisions are open, except that gap 2 (who decides, and the hearing gate and 30-day window) was decided and entered on 2026-11-15 (539th move), and the trade-off default and outer-limit wording were entered in the 541st move. The Chapter Five *Minority* entry and the correction route were entered in the 542nd move; the independent reads are shelved in [../SHELVED.md](../SHELVED.md), so the item is closed.
- **Standing records as measurement infrastructure:** steps 1, 2, 3, and 5 done on 2026-11-15. Classified as mostly handled by the text, with four text gaps (compelled showing of an existing record; onward disclosure and cross-adopter reach; the undefined "credit pathways"; the count of trust-sensitive pathways), one implementation wording conflict ("may publish pairs"), and a test-coverage gap. Record: [hesitation_standing_records_measurement_infrastructure_finding_2026-11-15.md](../reviews/hesitation_standing_records_measurement_infrastructure_finding_2026-11-15.md). Step 4 (independent read) and the custodian's decisions are open, except that gaps 1 and 2 (compelled showing; onward disclosure) were decided as a gate-based gatekeeper check and entered on 2026-11-15 (545th move), and gap 3 ("credit pathways") was decided as a definition plus a new Financial Authority Standing Lock and entered the same day (546th move), and gap 4 (trust-sensitive pathways) was entered as a published, challengeable designation plus a joint-conditions bar (548th move). The question of what standing the Constitution publishes was decided on 2026-11-15 (550th move): violations at slot 5 and higher are public as a notice about the event, everything else is private unless the sentient chooses.
- **Unproven under pressure:** announcement claims audit done on 2026-11-16 (steps 1, 2 and 5; step 4 not done). Classified as mostly handled: 14 claims checked, none aspirational presented as fact, two wording points (the same-standard line is overstated while no adopter exists; the definition count is stale at "more than two hundred" against 310 in the registry). Record: [hesitation_unproven_under_pressure_announcement_claims_finding_2026-11-16.md](../reviews/hesitation_unproven_under_pressure_announcement_claims_finding_2026-11-16.md). Custodian decisions open.
- **Scale against comprehensibility:** not started. The audit above found that the core is now 544,568 words in 50 files, not the 300,000 the item assumed.
