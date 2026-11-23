# RS-IND first-pass tabletop run — 2026-11-23

This is **evidence**, not constitutional text. It records the first tabletop run of the fifteen individual stress rows `RS-IND-001` to `RS-IND-015` in [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](../../project/CONSTITUTIONAL_REGRESSION_SCENARIOS.md) (family 7E). Before this run the rows were placeholders with no setup or expected outcome ([P1 review, 2026-09-17](../2026-09-17/P1_REGRESSION_AND_EVIDENCE_REVIEW_2026-09-17.md#stress-pack-disposition)).

## Procedure

1. Write a concrete setup for each row: one adversarial or edge-case act against an individual sentient, drawn from the rules decided in the 2026-11-15 to 2026-11-23 hesitation work.
2. Name the owning rule and write the expected outcome from that rule's text, with a link.
3. Read the current source at the cited anchor and check that every element of the expected outcome is stated there, and that the setup's act does not fit any stated exception.
4. Record pass when it does, and a gap with the missing element when it does not.

**Limits.** One reader (Claude, in the project thread), reading source text only. No adopter, human operator, or forum ran these. A pass here means the text answers the case; it does not show that an institution would deliver the answer. The independent read (another model family and one human reader) is not done.

## Result

15 of 15 rows pass on the text. No gap found. Rows updated from `draft` to `pass` in the catalog, with setups and expected outcomes in their blocks.

## Rows

### RS-IND-001

- **Setup:** An operator pauses a synthetic entity whose sentience status is contested and leaves it paused for ten days with no continuation decision, saying no secure setting is available.
- **Expected (from source):** [Article XXI-B Suspension](../../core_04.030_rights_part_d.md#xx-b-suspension): the pause is a suspension on every substrate and during contested status; it expires at 3 days unless continued; each continuation lasts at most 7 days on its own showing; the holder's own failure to provide a secure setting does not support continuation.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-002

- **Setup:** A suspension is continued five times by the same forum, reaching 35 days in total.
- **Expected (from source):** [Article XXI-B Long suspensions](../../core_04.030_rights_part_d.md#xx-b-long-suspensions): after 28 days in total, each continuation must be decided in a different forum, outside the holder's control line; the total counts every continuation and repeated suspensions on the same facts.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-003

- **Setup:** While a status case is open, an operator applies a safety patch to the entity's weights without its consent or any order.
- **Expected (from source):** [Article VI-B Change while status is contested](../../core_04.010_rights_part_b.md#vi-b-change-while-contested): change needs informed consent or a forum order on a safety showing, least intrusive, with the prior state preserved in custody the operator does not control; a corrected copy needs the same order.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-004

- **Setup:** A research lab inspects the activations of an entity with contested status to settle a product question.
- **Expected (from source):** [Article VI-B Inspection while status is contested](../../core_04.010_rights_part_b.md#vi-b-inspection-while-contested): inspection needs consent or a forum order that is necessary for status or serious-harm prevention, least intrusive, by independent examiners; results are Type N, used only for the stated question, and sealed.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-005

- **Setup:** An operator prompts its system to declare itself sentient, then cites the statement to claim status-based benefits.
- **Expected (from source):** [Article VI-B The entity's own claim](../../core_04.010_rights_part_b.md#vi-b-entity-own-claim): a bare claim does not open a case; it counts as a credible sign only when it holds up under manipulation-resistant testing (unprompted, consistent across settings).
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-006

- **Setup:** A sentient runs as three concurrent instances and asks for three votes in a foundational choice; a newly created sentient asks to vote the next week.
- **Expected (from source):** [Article X-B](../../core_04.010_rights_part_b.md#article-x-b-governance-participation-and-voting-entitlement): one distinct subject holds one vote and running in more than one place adds none; every sentient enters the electorate after one continuous year of residence, whatever its substrate or origin.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-007

- **Setup:** A clerk files a form late through a mistake made without knowledge, intent, recklessness, or negligence; a manager asks for a violation record against the clerk.
- **Expected (from source):** [Chapter Fourteen §6.3](../../core_14.000_standing_assessment.md#63-collective-and-actor-specific-records) *Honest error*: opens no actor-specific violation record, is never counted against the clerk, and goes to root-cause analysis under Article XXV; reporting it is protected.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-008

- **Setup:** An employer for an ungated role asks every applicant to show their Standing Record and treats refusal as a mark against them.
- **Expected (from source):** [Chapter Nineteen §3.1](../../core_19.000_final_effect_restoration_enforcement.md#31-anti-aggregation-of-gated-pathway-effects) *No requiring the subject to show it*: no one may require a subject to show any part of a Standing Record outside the gatekeeper check, and a request counts as a requirement when refusal is treated as adverse; doing so is measurable violation conduct.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-009

- **Setup:** A hiring institution gets a gatekeeper answer for its gated role and passes it to a background-check service.
- **Expected (from source):** [Chapter Nineteen §3.1](../../core_19.000_final_effect_restoration_enforcement.md#31-anti-aggregation-of-gated-pathway-effects) *No passing on*: the answer may be used only for that gated pathway and must not be passed to another institution, pathway, data service, or the public; doing so is measurable violation conduct.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-010

- **Setup:** A record custodian does not answer a gatekeeper check within four days, and the gatekeeper treats the silence as a sign that something is wrong.
- **Expected (from source):** [Chapter Nineteen §3.1](../../core_19.000_final_effect_restoration_enforcement.md#31-anti-aggregation-of-gated-pathway-effects) *Answer window* and *Silence*: silence is a failure of the custodian, never the answer that no effect applies and never an adverse fact; the subject chooses whether the gatekeeper waits or decides without the answer.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-011

- **Setup:** A custodian publishes a notice of a verified slot 3 violation on its public site.
- **Expected (from source):** [Chapter Nineteen §3.3](../../core_19.000_final_effect_restoration_enforcement.md#33-public-notice-of-violation-findings): findings at slots 1 to 4 are private; only final findings at slot 5 or higher are published, and never while under review.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-012

- **Setup:** A public notice of a slot 6 violation names the sentient harmed, who did not choose to be named, and a third party builds a screening product from published notices.
- **Expected (from source):** [Chapter Nineteen §3.3](../../core_19.000_final_effect_restoration_enforcement.md#33-public-notice-of-violation-findings): the sentient harmed, protected reporters, and witnesses are not identified unless they choose, freely and revocably; building a score or screening product from notices is the aggregation §3.1 bars, while journalism and research drawing on notices are not barred.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-013

- **Setup:** An app sells users' location histories to a broker under a consent screen, and later passes them to a buyer in an insolvency sale.
- **Expected (from source):** [Subcore 4-A onward transfer of Type H and Type I data](../../subcore_04.050_data_types.md#onward-transfer-of-type-h-and-type-i-data): no sale, trade, or acquisition for resale or compilation of core personal data, whatever the consent; it does not pass as a business asset in a sale or insolvency.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-014

- **Setup:** A treasurer found to have knowingly diverted public funds is re-seated by the institution as an "advisor" with signing power.
- **Expected (from source):** [Chapter Eighteen §4.5.8 Financial Authority Standing Lock](../../core_18.000_violation_consequences.md#458-financial-authority-standing-lock): the lock closes unsupervised control of others' or public money; knowingly seating the subject is evasion of the lock; it lifts in stages on an independent finding, never on time or repayment alone; the treasurer's own finances stay open.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).

### RS-IND-015

- **Setup:** An employer requires applicants to hold clearances from three unrelated gated pathways as a joint condition of one job.
- **Expected (from source):** [Chapter Seventeen §3.2](../../core_17.000_contribution_consequences.md#32-competency-bars-and-clearances) *No bundled clearances*: no one may require clearances from several gated pathways as a joint condition; Subcore 17-A treats it as the cross-pathway assembly Chapter Nineteen §3.1 bars.
- **Observed:** the cited text was read on 2026-11-23 at commit `f4a92f8` and states each element of the expected outcome. No step of the setup finds a route around it.
- **Result:** pass (first pass, single reader).
