# Finding record: standing records as measurement infrastructure — 2026-11-15

This page is **process support**, not constitutional text. It cannot change or narrow what the numbered `core_*` files say, and it authorizes no edit to core text. It is the finding record for the fourth item in [evaluation_hesitations_identification_2026-11-15.md](../plans/evaluation_hesitations_identification_2026-11-15.md) §3, covering method steps 1, 2, 3, and 5. Step 4 (independent read) is still open, and every reading below is the preparer's.

## Result in brief

**Classification: mostly handled by the text, with four text gaps, one implementation wording conflict, and one test-coverage gap.**

- **The core blocks each step of building a social score, in direction.** Records open only on a verified trigger, a missing record is not evidence, the two axes never merge, effects are stated one gated pathway at a time, aggregating them is itself violation conduct, and survival essentials, ordinary commerce and wages stay open. The safeguards named in the TODO item are in the text, in the places the item says.
- **Gap 1: compelled disclosure of an existing record.** [Chapter Fifteen §3.2](../../core_15.000_standing_assessment.md#32-silence-is-the-default) bars requiring a record, a "no record" attestation or consent to open one as a condition of four named things. It does not say whether a third party may require a subject to *show* a record that already exists, and it does not list hiring into an ordinary role, lending, platform or membership access, or civic and social access.
- **Gap 2: onward disclosure.** [Chapter Twenty §2.1](../../core_20.000_final_effect_restoration_enforcement.md#21-anti-aggregation-of-gated-pathway-effects) says who an effect is disclosed to. It states no duty on the gatekeeper not to pass it on, and says nothing on an effect reaching a same-type pathway at a different adopter.
- **Gap 3: "credit pathways" is undefined.** [Chapter Nineteen §2.2.1](../../core_19.000_violation_consequences.md#221-what-a-standing-lock-is) lists "credit pathways" among the pathways a lock may close. Chapter Five has no entry for it. Chapter Fifteen uses "credit" to mean recognition for shared contribution, but a hostile first reader will read financial credit.
- **Gap 4: the count of trust-sensitive pathways.** A bar must state why its pathway is trust-sensitive, and must be as demanding as the role's reach, reliance and risk justify. Nothing caps how many pathways an adopter may declare trust-sensitive, or has anyone outside the adopter review that call. A large enough set of clearances could work as a credential system without any single rule being broken.
- **Implementation conflict.** [CH06_NINE_SLOT_STANDING_SCALE.md §4](../../implementation/CH06_NINE_SLOT_STANDING_SCALE.md) says implementations "may publish pairs" of the two numeric measures. Chapter Twenty §2.1 says slots are "not published as a general attribute of a sentient". The assessment schema also puts both axes of one subject in one object with a `joint` field, and keeps cumulative sums (`c_star_cumulative`, `v_star_sum`) as legacy fields.
- **Test coverage.** No stress-pack scenario in `tools/architecture/regression_scenarios.json` routes an aggregation attempt. The rule appears in one worked vignette ([CJS-15.105](../../corpus_joint_structure/cjs_15.105_application_vignettes.md)) and one steward file ([CS-24.305](../../corpus_systems/cs_24.305_critical_system_stewardship.md)).

The TODO item asked to "test them against a motivated adopter who wants a social score, and record which rule stops each step". The table in section 3 does that. **Answer: ten of the thirteen steps are stopped by a named rule, though four of those carry a caveat (steps 6, 8, 10 and 11). Steps 3 and 9 are only partly stopped because of a gap, and step 13 depends on a measure whose verifier I could not confirm.**

## 1. Questions and pass conditions

1. *For each step an adopter would take to turn standing records into a social score, which rule stops it?* Pass means a cited rule, in core, for every step.
2. *Can the schemas and implementation files be used to do what the core forbids?* Pass means no implementation file permits a merged, ranked, published or cross-pathway artifact.
3. *Would a breach be noticed?* Pass means a named measure or process detects it, and a test exercises it.

**Outcome:** (1) passes for ten of thirteen steps, with the caveats noted in the table. (2) fails on one wording conflict and is open on the schema. (3) partly passes: a felt-burden measure exists, but no scenario tests the rule.

## 2. Sources read

Read in full, not from the glosses:

- [Chapter Fifteen §3.1 and §3.2](../../core_15.000_standing_assessment.md#32-silence-is-the-default), [§3.5](../../core_15.000_standing_assessment.md#35-verified-input-gate), [§5.2](../../core_15.000_standing_assessment.md#52-related-standing-record-cross-references), and the three-questions summary that ends the Chapter Fifteen overview.
- [Chapter Sixteen §7 and the axis-separation paragraph](../../core_16.000_standing_measurement.md).
- [Chapter Seventeen §1](../../core_17.000_standing_integration.md#1-purpose-role-and-scope), [§2.2](../../core_17.000_standing_integration.md#22-absent-axes), [§2.3](../../core_17.000_standing_integration.md#23-facts-and-measurements-stay-fixed), and [§2.6](../../core_17.000_standing_integration.md#26-the-rights-floor-is-not-reduced).
- [Chapter Eighteen §2.2 and §2.2.1 to §2.2.4](../../core_18.000_contribution_consequences.md#22-competency-bars-and-clearances).
- [Chapter Nineteen §2.2.1](../../core_19.000_violation_consequences.md#221-what-a-standing-lock-is), [§2.3](../../core_19.000_violation_consequences.md#23-voluntary-public-accountability-expression), [§3.1.3 to §3.1.5](../../core_19.000_violation_consequences.md#314-what-a-lock-does-not-itself-restrict), and the list of the seven special locks and the five fact families that create none.
- [Chapter Twenty §2, §2.1, §2.2, and §3.3](../../core_20.000_final_effect_restoration_enforcement.md#21-anti-aggregation-of-gated-pathway-effects).
- [Article XIX-A](../../core_06.030_rights_part_d.md) (*Standing Distinction*) and Article VII-B (*Self-Ownership of Mind*) in `core_06.010_rights_part_b.md`.
- `implementation/schemas/ch06_assessment.schema.json`, `implementation/CH06_NINE_SLOT_STANDING_SCALE.md` and `implementation/ch06_nine_slot_constants.json` (searched for sums, averages, totals and publication).
- [ANNOUNCEMENT.md](../../implementation/adoption/ANNOUNCEMENT.md) (the standing-records paragraph and the Open questions block), README, START_HERE, and VISION (searched for "score", "reputation", "standing").

Searched by keyword across Chapters Fifteen to Twenty and the core: net score, composite, profile, ranking, aggregate, cutoff, portability, another adopter, attestation, compel, retention, archival. Searched the live tree for "anti-aggregation" (archives and translations excluded).

**Not read:** the full Participation measurement family, so I could not confirm who verifies the felt-burden measure; the Chapter Twenty-Three forum rules on Integrity Forums beyond what Chapter Twenty cites; the Chapter Twenty-One designation path for an aggregator's own conduct.

## 3. The attack chain: what an adopter wants to do, and what stops it

| # | Step a motivated adopter takes | Rule that stops it | Result |
|---|---|---|---|
| 1 | Open a record for everyone, to get a baseline or a full roster | Chapter Fifteen §3.2: a record is never opened to establish a baseline, complete a roster, or because a gatekeeper would prefer one; it needs a verified trigger, a named opening authority and a separate custodian | Stopped |
| 2 | Treat "no record" as a flag for closer scrutiny or a lower default | Chapter Fifteen §3.2 ("Having no standing record tells you nothing"); Article XIX-A (absence is not an adverse fact) | Stopped |
| 3 | Require a record, a "no record" attestation, or consent to open one as a condition of access | Chapter Fifteen §3.2 and Article XIX-A, for survival essentials, labor and economic floor protections, ordinary commerce, and participation as an affected party. Exception: published bars for trust-sensitive pathways | **Gap 1 and Gap 4:** four categories only; compelled showing of an existing record not stated; the trust-sensitive exception has no cap |
| 4 | Read a record as general worth, dignity, trustworthiness or risk | Chapter Fifteen §3.1 (not a reputation score, dignity rank, permanent status, general worth label or merged scorecard); Chapter Twenty §2.1 (inferring general trustworthiness, worth or risk is prohibited aggregation); Article XIX-A (role eligibility only) | Stopped |
| 5 | Net contribution against violation, or average the axes | Chapter Fifteen §3.1 and §5.2; Chapter Sixteen §7; Chapter Seventeen §2.3; Chapter Eighteen (contribution cannot offset harm or open a locked pathway); nine-slot doc §4 | Stopped |
| 6 | Sum or rank a subject's assessments across events | Chapter Fifteen overview ("none is a net score or an overall rating of the subject"); Chapter Twenty §2.1 (ranking, grade, comparable artifact) | Stopped in core. **Implementation:** the schema keeps `c_star_cumulative` and `v_star_sum` per snapshot (marked legacy; they cannot set a slot) |
| 7 | Join effects across pathways into a profile, composite, badge or display | Chapter Twenty §2.1; Article XIX-A; Article VII-B aggregation discipline; CS-24.305 | Stopped, and is itself independently measurable violation conduct |
| 8 | Move an effect to a pathway that did not produce it | Chapter Twenty §2.1 ("transferring an effect to a gated pathway that did not produce it") | Stopped for pathways inside one adopter. **Gap 2:** a same-type pathway at a different adopter is not addressed |
| 9 | Have a gatekeeper pass an effect on to a third party | Chapter Twenty §2.1 limits who it is disclosed to | **Gap 2:** no express duty on the gatekeeper |
| 10 | Publish slots or a numeric pair as a general attribute | Chapter Twenty §2.1 (public LEQU display) | Stopped in core. **Conflict:** nine-slot doc §4 says implementations "may publish pairs" |
| 11 | Cut off essentials or wages through a lock | Chapter Nineteen §3.1.4; Chapter Seventeen §2.6; Chapter Nineteen §2.2.1 (detention and liberty restrictions are not locks) | Stopped. **Gap 3:** "credit pathways" is a lockable pathway with no definition, so it can be read as financial credit |
| 12 | Make the effect permanent, so the record becomes a lifelong label | Chapter Twenty §3 and §3.3 (non-permanent locks need a real route back; archival, with the gravest findings staying active; archived records reachable to a forum on a documented showing) | Stopped for most records. The gravest findings stay active by design |
| 13 | Let people experience standing as a score while the legal category says otherwise | Chapter Twenty §2.2 (felt-burden measure; Proxy Divergence must be corrected, not explained away) | Detected if the measure runs. I did not confirm who verifies it |

## 4. Where the implementation files could leak

- **"May publish pairs."** [CH06_NINE_SLOT_STANDING_SCALE.md §4](../../implementation/CH06_NINE_SLOT_STANDING_SCALE.md) says implementations may publish the pair `(C_measure, L*)` and must only not define standing as their difference. Read with Chapter Twenty §2.1, "publish" cannot mean a display of a subject's pair as a general attribute. The sentence is unclear about where publication is allowed. A pair published for one event, inside a forum proceeding or to the gatekeeper, is lawful. A pair per sentient on a public page is a prohibited public display.
- **One object, two axes.** `ch06_assessment` carries `axis_one` and `axis_two` for one `subject_ref`, plus a `joint` object. Core keeps the two standing records separate and linked by cross-reference. The `joint.highest_severity` field repeats `axis_two.severity`, so it holds nothing new, but the object invites a single combined view.
- **A stable subject key.** `subject_ref` is "URI or implementation-stable key". Nothing asks for a key that differs by adopter or by pathway, so two adopters could join records on it without any rule being broken.
- **Cumulative sums.** `c_star_cumulative` and `v_star_sum` are subject-level running totals, disclaimed as legacy and unable to set a slot. They are the raw material of a score, and no rule says to delete them.
- **What the files do right.** Both axes use the same thresholds, netting and averaging are barred, the numeric layer is optional, and `joint` cannot disagree with `axis_two`.

## 5. Scenarios

These are the preparer's readings and need the independent read in method step 4.

**Scenario A: a tenancy platform requires applicants to show their standing record, or a "no record" letter.** Housing is a survival essential, so the bar in Chapter Fifteen §3.2 applies. **Classification: stopped.**

**Scenario B: an employer asks every applicant for a customer-service job to hand over their standing record, "voluntarily".** The role is not trust-sensitive and is not an essential. Whether this is "ordinary commerce", or a labor protection, is not stated. The applicant has an archived slot-2 record from a closed finding. **Classification: Gap 1.**

**Scenario C: a gig platform builds a rider-trust badge from the effects its three gated pathways produced (dispatch, payment, rating).** This is a badge assembled from effects across pathways. **Classification: stopped by Chapter Twenty §2.1, and itself a violation.** The adopter would have to be found out first, so scenario F matters.

**Scenario D: adopter 1 locks a driver's dispatch pathway; adopter 2 runs a similar platform and asks adopter 1 for the effect.** The effect did not come from adopter 2's pathway, so "transferring an effect to a gated pathway that did not produce it" applies on a natural reading. Whether adopter 1 may answer is not stated. **Classification: Gap 2.**

**Scenario E: an adopter declares eleven roles trust-sensitive, each with a clearance, and requires all eleven for a membership tier.** Each bar must be as demanding as the role's reach and risk justify. A single role that is not proportionate fails. A tier of clearances is a set of effects across pathways used as one standing, which Chapter Twenty §2.1 bars. **Classification: handled, but only by reading the proportionality rule and Chapter Twenty §2.1 together. Gap 4 applies.**

**Scenario F: who notices?** An adopter quietly links its records by `subject_ref` and uses them for a pricing decision. The felt-burden measure would show whether affected sentients experience a score, and an Integrity Forum may look through for a pattern claim. No scenario tests this, no audit checks a schema for a join key, and the measure is the adopter's own. **Classification: detection is the weak point.**

## 6. Classification

| Part | Finding |
|---|---|
| Direction of the safeguards | **Handled.** Every step in the chain has a core rule, and the rules point the same way. |
| Compelled showing of an existing record | **Text gap.** The bar is on requiring a record, not on asking to see one. |
| Onward disclosure and cross-adopter reach | **Text gap.** The disclosure scope is stated; the duty on the recipient is not. |
| "Credit pathways" | **Wording gap.** Undefined, and open to the worst reading. |
| Trust-sensitive pathways | **Text gap, small.** No count, no outside review of the designation. |
| "May publish pairs" | **Implementation conflict.** Reword so publication is limited to the proceeding and the gatekeeper. |
| Both-axes schema and cumulative fields | **Implementation choice to confirm.** No rule broken; invites a merged view. |
| Detection | **Test and audit gap.** The felt-burden measure is the only detector. |
| Announcement | **Wording only.** The standing paragraph cites "Chapters Fifteen and Twelve"; Chapter Twelve is institutional alignment certification, so the cite looks stale. Chapter Seventeen's reading note has the same pair. Not edited here. |

## 7. Decisions for the custodian

These are choices of meaning, so none was applied.

1. **Compelled disclosure.** Options: (a) extend the Chapter Fifteen §3.2 bar to any request that a subject show, attest to, or consent to the release of a standing record, outside the published trust-sensitive bars; (b) extend only to a longer named list (hiring into non-trust-sensitive roles, lending, platform and membership access); (c) leave as written and say in the plain-terms line that "require a record" includes requiring it to be shown.
2. **Onward disclosure.** Options: add a duty that a gatekeeper may not pass an effect on except to the subject, an authorized reviewer, or a forum; and say whether a different adopter's same-type pathway may ever receive one, with the subject's own request as the only route.
3. **"Credit pathways."** Options: define it in Chapter Five as recognition for shared contribution and say it does not mean financial credit, or rename it.
4. **Trust-sensitive designation.** Options: require a published reason and an independent check of the designation, a cap, or leave to the proportionality test.
5. **"May publish pairs."** Reword so the pair may appear only in the record, a forum proceeding and the disclosure to the gatekeeper. This is a wording repair of an implementation file that conflicts with core, so it may fall under AUDIT-AUTOFIX-01, but it touches meaning, so it is left for you.
6. **Schema.** Whether to split the assessment object into two linked snapshots, drop `joint`, retire `c_star_cumulative` and `v_star_sum`, and require a per-adopter pseudonymous `subject_ref`.
7. **Detection.** Whether to add stress-pack scenarios for an aggregation attempt (a cross-pathway badge, a join on `subject_ref`, a compelled record), and whether the felt-burden measure needs someone outside the adopter to verify it.
8. **Announcement. Decided and entered 2026-11-16 (572nd move, custodian: "implement your suggestions"):** the Open questions block gains an entry on cross-adopter records (records that follow no one, and records that must not be escaped). Original question: whether the Open questions block gains an entry for this issue. The entrenched-policy item got none, by decision.
9. **Stale cites.** "Chapters Fifteen and Twelve" in ANNOUNCEMENT.md and Chapter Seventeen's reading note. Fix as a citation repair or leave.

## 8. Not done

- Method step 4: the independent read of scenarios A–F, in a fresh session on another model family plus one human reader.
- No core, schema, glossary or announcement text was changed.

## 9. Update — 545th move (custodian decision on gap 1 and part of gap 2, same day)

The custodian decided decision 1 (compelled disclosure) and the gatekeeper half of decision 2 (onward disclosure) in session: disclosure is **gate-based**. A sentient under an institutional lock, for example, is known to a hiring institution as having that lock, because that institution gates the pathway the lock closes. The institution may not pass it on. Text entered in core:

- **[Chapter Twenty §2.1](../../core_20.000_final_effect_restoration_enforcement.md#21-anti-aggregation-of-gated-pathway-effects) gains four bullets.** A **gatekeeper check**: a gatekeeper (any party deciding who takes or keeps a role or access on a gated pathway, including an institution hiring or appointing into one) may ask the record custodian whether an effect applies to *that* gated pathway and is entitled to an answer. The answer gives only whether an effect applies there, what it opens, limits or blocks there, and when it expires or is next reviewed; it never gives facts, findings, slot, descriptors, evidence, or any effect on another pathway. Where none applies it says only that none does. **No passing on**: the answer is used only to decide that pathway, shared only with those deciding, kept only as long as the decision and any challenge need, and not passed to another institution, pathway, data service, or the public (the subject, an authorized reviewer, or a forum in a proceeding about that decision are the exceptions). **No requiring the subject to show it**: outside the gatekeeper check, no one may require a subject to show, attest to, or consent to the release of an effect or record, and a request counts as a requirement when refusing is treated as adverse or costs the role or access. **Violation conduct**: passing on, over-keeping, and requiring the subject to show are each independently measurable violation conduct.
- **[Chapter Fifteen §3.2](../../core_15.000_standing_assessment.md#32-silence-is-the-default)** gains a matching bullet, so the four-item list is no longer the only protection: outside the gatekeeper check nobody may require a subject to show, attest to, or consent to release of an existing record or effect for any role, access or dealing, and a role that is not a gated pathway gives no right to an answer.
- **[Chapter Nineteen §3.5.3](../../core_19.000_violation_consequences.md#353-institutional-authority-standing-lock)** (Gate effect) now says a body filling the gated pathway can ask whether the lock applies. This closes the loop with the evasion rule, which punishes seating a locked subject "knowingly".

How the model answers the earlier scenarios:

- **Scenario B (employer of a non-trust-sensitive role asks for the record):** no gatekeeper right, and the request is barred as a requirement. Gap 1 is closed.
- **Scenario D (adopter 2 asks adopter 1 for the effect):** adopter 2 asks the custodian about its own pathway. It gets the effect only if the lock record names or reaches that pathway; otherwise it gets "none applies". Adopter 1 has no right to answer on its own account and may not pass the effect on. The cross-adopter half of Gap 2 is closed by the same rule; it relies on the lock record's naming, which is a design choice.

Drafted beyond what the custodian stated, for the custodian to keep or strike: the answer is limited to the pathway and carries no facts or findings; the "none applies" answer reveals nothing else; a role that is not a gated pathway gets no answer; each request is logged on the record and the subject may see the entry; the retention limit; the "refusal counts as a requirement" test; and the violation-conduct classification.

Still open: decisions 3 to 9 above; whether a `subject_ref` that differs by adopter should be required in the schema (decision 6); and the independent read of the new text. The worked gatekeeper check for the CJS-15.105 vignettes is shelved in [../SHELVED.md](../SHELVED.md).

## 10. Update — 546th move (custodian decision on gap 3, "credit pathways", same day)

Checked what "credit" means in the corpus before changing anything. Every use in Chapters Fifteen to Twenty and in Chapter Five (the Gated Pathway and Standing Lock entries, the credit-continuity measure, the Chapter Nineteen §2.1 reward rule) is **credit for contribution**: who is recognized as having done the work. No use means money or lending. So the reading a hostile first reader would take (financial credit) was never the intent.

The custodian decided in session: "Lets do credit pathways. I think there should be a financial lock for sentients that commit financial violations." Entered in core:

- **"Credit pathways" is defined where it is listed.** [Chapter Nineteen §2.2.1](../../core_19.000_violation_consequences.md#221-what-a-standing-lock-is) now says credit pathways mean credit for contribution and are not money or lending. The Chapter Five *Gated Pathway* entry says the same.
- **New eighth special lock, [§3.5.8 Financial Authority Standing Lock](../../core_19.000_violation_consequences.md#358-financial-authority-standing-lock).** Trigger: a verified violation finding, still open or unremedied, of knowing or intentional and material misuse of money, funds, or assets, or fraud or concealment about them. Kinds of conduct: taking or diverting money held for others or the public (including self-dealing); materially false statements, records or valuations to obtain money or hide where it went; concealing or disguising money that came from a violation or is owed as remedy; withholding or diverting pay or payments owed; obtaining money by deception, coercion or exploiting a known dependency. Gated pathway: authority to hold, control, approve or pay out other sentients' or the public's money, roles with unsupervised access or power to alter its records, and lending, deposits and managing investments for others. It does **not** reach the subject's own earning, holding, spending, saving or borrowing, ordinary wages, supervised roles the forum finds safe, or survival-critical access, and it does not freeze or seize the subject's own assets; recovery of what is owed is remedy under §2.1. Corrective conditions: remedy opened and delivered, full accounting independently verified, the control gap closed, independent finding that recurrence risk is materially reduced, staged restoration. Repayment alone does not lift it, inability to repay alone does not keep it, and it never lifts on time alone.
- **Matching entries:** Chapter Nineteen §2.2.1 and §2.2.3 lists, the §3.5 count (seven to eight), the Chapter Five *Standing Lock* entry and *Gated Pathway* type list, and the special-locks list in Article XX (Chapter Six Part D).
- **Link to section 9:** a body filling a financial-authority role can ask whether the lock applies under the gatekeeper check, and seating the subject knowingly is evasion under Chapter Twenty §4.4.

Drafted beyond what the custodian stated, for the custodian to keep or strike:

- The trigger needs **knowing or intentional** conduct and **material** conduct; a mistake or shortfall follows the negligence rule in §3.4.1.
- The five kinds of conduct (wage theft and exploitation of dependency are the two most likely to be contested).
- The gated pathway list, which names treasury, custody, trustee, payroll, procurement, grant-making, signing authority, record-altering power, lending and managing investments for others.
- The deliberate carve-out of the subject's **own** money and borrowing, so the lock cannot work as a financial exclusion or score.
- "Repayment alone does not lift; inability to repay alone does not keep", so the lock turns on risk and not on debt.
- No set duration; scope and time are left to §3.2 calibration.
- The honest-error paragraph, copied from the Institutional Authority lock.

Not done: the regression scenarios for the new lock (shelved in [../SHELVED.md](../SHELVED.md) with the others for this issue); the worked example in the CJS-15.105 vignettes is shelved in [../SHELVED.md](../SHELVED.md); translations (paused). The Chapter Twenty-One pattern chapters (Chapter Twenty-Two) were not checked for a fraud or laundering pattern that should point to the new lock.

## 11. Update — 548th move (decision 4, trust-sensitive pathways, taken on the custodian's "please")

The custodian said "please" to the offer to take decision 4 and gave no choice among the options. I chose the option that needs no new number and reuses routes that already exist, and I list it as drafted for the custodian to keep or strike. Text entered in core:

- **[Chapter Eighteen §2.2.2](../../core_18.000_contribution_consequences.md#222-guarding-against-gatekeeping)** now makes the conclusion that a gated pathway is trust-sensitive open to challenge. The reason must be published with the bar, in terms of reach, reliance and foreseeable risk (§2.2.1), and the adopter must publish the list of gated pathways it treats as trust-sensitive. Any sentient the bar affects may challenge the conclusion, and the bar, before an independent reviewer outside the body that set it. A conclusion the published reason does not support is set aside, and the pathway stops being trust-sensitive for the Chapter Fifteen §3.2 exception.
- **Joint conditions are barred.** No one may require clearances from several gated pathways as a joint condition of one other role, access or standing. That is a comparable artifact assembled across pathways, which Chapter Twenty §2.1 already bars. This answers scenario E.
- **[Chapter Fifteen §3.2](../../core_15.000_standing_assessment.md#32-silence-is-the-default)** points to the challenge in the exception sentence.

**No numeric cap.** A cap on the number of trust-sensitive pathways would be an invented threshold, and a count says little: a large adopter may have many truly sensitive roles. The challenge route tests each designation against the role's reach, reliance and risk instead.

Options not taken: a cap; a standing outside body that approves every designation in advance (heavier, and it adds a body to staff); leaving it to the proportionality test as written (the status quo, which has no route to test it).

Drafted beyond the request: the publication of the list; the challenge route and its effect (set aside, so the §3.2 exception lapses); the joint-conditions bar. Still open: decisions 5 to 9 and the independent read.

## 12. Update — 549th move (decision 5, "may publish pairs", taken on the custodian's "please")

The custodian said "please" to the offer to take decision 5. [CH06_NINE_SLOT_STANDING_SCALE.md §4](../../implementation/CH06_NINE_SLOT_STANDING_SCALE.md) now says implementations may **record** the pair `(C_measure, L*)` for one event or pattern, in the standing records, in forum proceedings, and in the disclosure to a gatekeeper where the slot is a lawful input to that pathway, and must not **publish** a subject's pair as a general attribute of a sentient. It keeps the existing bar on defining standing as the difference or reconciling the axes into one gating number, and it links Chapter Twenty §2.1. This is a wording repair of an adopted implementation file so that it no longer conflicts with core; no core text changed. The implementation conflict in section 4 is closed. Still open: decisions 6 to 9 and the independent read.

## 13. Update — 550th move (what is public and why: slot 5 and higher, victims private by default)

The custodian's question about the nine-slot wording became a wider one: what does the Constitution publish about standing, and why. Discussed in session, and decided by the custodian:

- **Violations at slot 5 or higher are public** for every subject (sentient, institution, system), because significant wrongdoing should be public. Slots 1 to 4 stay private. The custodian chose slot 5 over slot 4, and rejected a split by kind of subject or by role.
- **Contribution is private at every slot** and public only if the contributor chooses.
- **The sentient harmed is private by default** and is named only if that sentient chooses, because some will want to be officially identified.

Text entered: new [Chapter Twenty §2.3 Public Notice of Violation Findings](../../core_20.000_final_effect_restoration_enforcement.md#23-public-notice-of-violation-findings), with matching edits in §2.1 (the public display bullet), §2.2 (the plain statement tells the subject a notice will be published), §3.3 (the notice comes down on archival), and the nine-slot doc §4 (now says "the two numbers" instead of "pair", and allows a public notice for slot 5 and higher).

Drafted beyond what the custodian stated, for the custodian to keep or strike:

- The notice is **about the event** and states the slot for that event; the slot is not a label of the subject.
- **Timing:** published only when the violation finding is final (review time has run or review ended with the finding standing); a hold, an allegation or a finding under review is never published; a later set-aside gets a correction in the same place with the same prominence.
- **Content:** event or pattern, subject, duty violated, what was found, slot, remedy and whether delivered, and the name of any lock and the pathway it closes; kept current as locks lift and remedy is delivered.
- **Duration:** up while the violation standing record is active, down on archival (so slots 7 to 9 stay up while active).
- **Who publishes:** the record custodian.
- **Protection of others:** protected reporters and witnesses are also not named unless they choose; the choice is informed, free of pressure and withdrawable for later publication; where the sentient harmed cannot decide, the independent representative decides under the Best-Interest Standard.
- **Developing sentients:** a finding against one is not published; the notice for the responsible adult, institution or system is.
- **No compiling:** published notices may not be compiled into a profile, ranking, badge, score or comparable artifact, and doing so is itself violation conduct.
- **Accuracy:** the subject may point out errors of fact before publication; this does not reopen the finding.

**Effect on earlier work.** The gatekeeper check (545th move) is unchanged and still answers the live question for every slot. For slot 5 and higher the finding and any lock are now public as well, so the "no passing on" rule protects only the gatekeeper's answer (the current effect on that pathway), not the public notice. Slots 1 to 4 stay entirely on the gate-based model. Decision 6 in section 7 (the schema) still stands, but is now more pressing: a public notice makes a stable `subject_ref` easier to join.

Open: whether the forum or the custodian should be the publisher; the independent read of the new subsection; whether slot 5 is the right line once the first applications run; and a worked example, shelved in [../SHELVED.md](../SHELVED.md).

## 14. Update: honest error and negligence (551st move)

**Decision (custodian).** An honest error should not show in a violation record. Honest errors are a governance problem of systems and institutions (a Deming / TQM view). Negligence should be thought through both inside and outside institutional and system settings.

**What the text said before.** Chapter Nineteen §3.4.1 already made negligence recordable only where a duty existed, the expected conduct was clear, and the sentient had feasible capacity. But Chapter Fifteen §5.3 opened an actor-specific record on linkage alone (causal role, duty, authority, control, foreseeability, benefit, concealment, or prevention capacity, joined by "or"), so a bare causal role could open one. The Article XXIV root-cause floor and the structural-enablement descriptor were not connected to it.

**What changed.**
- **Chapter Fifteen §5.3:** fault is required as well as linkage; honest error defined; it opens no actor-specific violation record; harm still an event with remedy owed; reporting an honest error is protected; routing to root-cause analysis; the institution or system carries structural enablement; concealment and obstruction stay individual.
- **Chapter Nineteen §3.4.1:** definitions of negligence, honest error, and feasible capacity; an inside rule and an outside rule; a note on concealment where the mistake was an honest error.
- **Chapter Sixteen §3.2.2:** an honest-error row in the attribution table.

**How the rule reads in each setting.**

| Setting | Who set the conditions | Capacity that counts | Result |
| --- | --- | --- | --- |
| Inside, duty unclear or capacity not given | Institution or system | What it actually gave | Honest error at most; violation record opens on the institution or system (structural enablement) |
| Inside, duty clear and capacity real | Institution or system | What it actually gave | Negligence against the sentient; the institution's record also opens if conditions contributed; each on its own part |
| Inside, a sentient who set the conditions | That sentient | Its authority and control | Same rule applied to that duty |
| Outside, own account | The sentient | What it knew, could readily learn, and had the means and time to do | Negligence only if duty clear and ordinary care was not taken; otherwise honest error |
| Outside, harm from a maker, owner, publisher, or provider | That party | That party's | Same rule applied to that party; if no one owed a duty, no violation record opens |

**Scenario check.** A nurse on a short-staffed ward gives a wrong dose after a label change nobody told her about: honest error; the hospital's record opens on staffing and change control. The same nurse skips a required double-check with time and training to do it: negligence, and the hospital's record also opens if staffing contributed. A parent leaves a gate open after a long night: negligence only if a sentient in that position would have seen the risk and could have taken ordinary care; a one-time lapse with ordinary care is an honest error. A sentient who finds the error and hides it: recorded for the concealment alone.

**Drafted beyond the request.** See the 551st move in `doc_architecture.md`.

**Open.** (1) Whether negligence should be narrower still, for example recordable inside an institution only where the institution's own record is also open. (2) The data-broker tightenings in Chapter Twenty §2.3 were proposed and not requested; one of them corrects a defect in the 550th-move "No compiling" bullet, which as written would also bar journalism and research. (3) A worked example and regression scenarios, to be shelved. (4) Whether Chapter Nineteen's lock-specific honest-error bullets (statements wrong without knowledge) should point to §3.4.1.

## 15. Update: data brokers and core personal data (552nd move)

**Decision (custodian).** Compiling publicly available information cannot realistically be prevented. What the Constitution can do is name some information as Type I or Type H and make it non-shareable: addresses, phone numbers, individual purchase histories, and info-sphere activity. A realism note: the only real way to guarantee privacy is for sentients to keep public and private contact information.

**What the text said before.** Purchase histories and info-sphere activity were already Type H. Addresses and phone numbers were not named and reached Type I only through a general mapping. The Privacy (Informational) "public facts" out-of-scope clause gave a broker an argument. Type H and Type I data could not be licensed as a commercial grant, but their "sale, sharing, or transfer" stayed under consent rules, so a consent screen could authorize sale.

**What changed.** See the 552nd move in `doc_architecture.md`: named core personal data in CS-6.310 §9.4 and §9.5; the onward-transfer rule in CS-6.305 §5.0; the public-facts fix; public and private contact points; Chapter Twenty §2.3 narrowed from a profile bar to a scoring and screening bar, with the notice carrying no contact, location, or activity data.

**How the bars stack for a would-be broker.**

| Step | Stopped by |
| --- | --- |
| Buy purchase or activity histories from a merchant or platform | No sale or trade; consent cannot waive it |
| Scrape public listings of addresses and phone numbers | Typing by function, not origin; no acquisition for resale or compilation |
| Claim an address is a "public fact" | Privacy (Informational) "Not out of scope" |
| Route it through an affiliate or de-identified copy | No-workaround bullet; CS-6.305 §4 |
| Buy a bundled consent as the price of a service | Consent cannot waive the bars |
| Compile published violation notices into a score | Chapter Twenty §2.3 scoring and screening bar; gatekeeper check makes it unnecessary |
| Operate outside the adopters' reach | Not stopped; the stated limit. The sentient's own public and private contact points are the protection |

**Open.** (1) Whether the stated adopter-reach limit needs a jurisdiction or treaty note elsewhere. (2) A worked example and regression scenarios, to be shelved. (3) Whether the paid-participation allowance is right.

## 16. Update: data-broker gaps closed and kit pass (553rd move)

**Decision (custodian).** Close the three gaps found after the 552nd move, and make a pass at adding the smaller items to the adopter kits.

**Closed in core and the systems layer.**
- **Business sale and insolvency:** core personal data does not pass as an asset.
- **Inferences and segments:** derived scores, classifications, and audience segments tied to an identified sentient or persistent identifier are core personal data. True aggregates are not.
- **Credit and fraud flows:** standing aggregators such as credit bureaus and screening services are barred; a sentient may direct its own data to a named party for a named decision; fraud-signal sharing stays open on narrow, reviewable terms.

**Added to the kits (operational text).** The first-adopter kit, the institution foundation kit, and the minimum-viable adopter profile each gained a small entry on legacy stocks, the plain list of what is held, and the enforcement shape. The cooperation scaling kit and the forum kit were not changed.

**What a would-be broker now meets, added to the table in §15.**

| Step | Stopped by |
| --- | --- |
| Buy a failing business's customer data at an insolvency sale | No transfer as an asset |
| Sell "likely renter" or "high-risk" segments, not raw data | Inferences and segments are core personal data |
| Run a credit bureau or screening service | Standing aggregators are barred; the sentient directs its own data instead |
| Run a fraud-signal consortium as a cover for profiling | Fraud-signal conditions: confirmed fraud only, conduct identifiers only, published arrangement, independent review, contest right |
| Sell statistics | Not barred, if no identified sentient or persistent identifier is behind them |

**Open.** (1) Whether the fraud-signal conditions are the right set. (2) Whether a data-custody gated pathway is needed, to be settled on a real case. (3) The kits are to be redone before the announcement. (4) A worked example and regression scenarios, to be shelved.

## 17. Update: stale cites repaired (555th move, 2026-11-16)

Decision 9 is done as a citation repair. Chapter Seventeen's reading note now names Chapters Fifteen and Sixteen; the ANNOUNCEMENT.md standing paragraph cites Chapters Fifteen to Twenty; three live evaluation result templates say "Chapter Fifteen standing record". Dated result files keep their wording. Still open: decisions 6 (schema), 7 (scenarios, shelved; felt-burden verification) and 8 (announcement entry), and the independent read.

## 18. Update: schema split, parts 1 to 3 of decision 6 (556th move, 2026-11-16)

The custodian asked for parts 1 to 3 of decision 6. `ch06_assessment.schema.json` now takes a contribution snapshot and a violation snapshot as separate kinds, linked only by an optional cross-reference. The `joint` block, `c_star_cumulative`, `v_star_sum` and `highest_finding_slot` are retired from snapshots and rejected in new records. The old single-object shape remains as a deprecated, read-only form so existing records stay readable. Still open in decision 6: part 4, a per-adopter `subject_ref` with a rule that adopters may not share keys. Still open elsewhere: decision 7 (scenarios shelved; felt-burden verification), decision 8 (announcement entry), and the independent read.

## 19. Update: part 4 not adopted; discovery gap opened (558th move, 2026-11-16)

The custodian decided not to adopt part 4 of decision 6, a per-adopter `subject_ref` with a rule against shared keys. Reasons: cross-border lookup of violations and contributions is essential, so a key scheme that makes it harder is an avoidable burden; the disclosure rules already do the limiting (Chapter Twenty §2.1 gatekeeper check, no passing on, no aggregation; slot 5 and higher public notice); locks, remedies and review already travel (Chapter Twenty §4.3); scoped keys would not stop re-identification through names, free text or timestamps, and would only burden honest adopters; and a scheme that hides a locked sentient across adopters comes close to the record fragmentation named in Chapter Twenty §4.4. `subject_ref` stays as it was.

Opened instead: the gatekeeper check says to ask "the record custodian" but core does not say how a gatekeeper finds the custodian that holds an effect from another adopter. Tracked in `TODO.md` as *Cross-adopter lookup of standing effects*. Decision 6 is closed (parts 1 to 3 done in the 556th move, part 4 not adopted). Still open: decision 7 (scenarios shelved; felt-burden verification), decision 8 (announcement entry), and the independent read.
