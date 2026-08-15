# Steward entry doors

**Status:** Process / operations-guide support — **not** binding constitutional or incorporated text. These cards, examples, and the owner/clock index **cannot narrow core text**. A card that diverges from core is not a compliance path. Divergence from the boxed **operative steward statement** in the named core home is a build failure (`make steward-door-lockstep-audit`), not an honor-system assertion.  
**Pinned to corpus edition:** `SC-Corpus-2026.08.09` (effective 2026-08-09; [README.md](../README.md)). Re-verify these cards against the named owners when that edition changes.  
**Job:** One five-field card per common fact pattern so a human or an AI steward can take the next step at 2 a.m. without rereading the instrument.  
**Same cards for both kinds of steward.** Binding home for that rule: [Chapter One §9.1.1 Shared Stewardship Standard](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Markdown answers are not standing records; verified failures record on the Chapter Eight axes. Human-operator invite: [`../evaluation/HUMAN_OPERATORS.md`](../evaluation/HUMAN_OPERATORS.md).

This is **not** [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) and **not** the [Preamble owner register](../core_00_preamble.md#constitutional-owner-register). Those maps are real. These cards are the door.

The five fields are owner, conflict rule, next-step class, forbidden move, and clock. The first four match the [handoff bar](PRE_PUBLICATION_SPEC.md#24-ai-handoff-readiness). Clock is the forbidden delay, surfaced from the [owner/clock index](#owner-clock-index) so it is not only in prose. Owner, forbidden move, and clock on each card are lockstep-checked against the boxed **operative steward statement** in the named core home. Every card also carries the three failed tests in the same words for both kinds of steward. Shared screens on this page: [costly-case refusals](#costly-case-refusals) and the one [shared refusal and logging](#shared-refusal-and-logging) screen (instruction received → refuse → document → escalate, plus the CS-4 §10 minimum inspectable-action set). One [worked refusal log](#worked-refusal-log) shows that screen filled in. Machine-readable high-pressure index: [`steward_owner_clock_index.json`](steward_owner_clock_index.json). CS-4 §10 log schema: [`schemas/cs4_inspectable_action_log.schema.json`](schemas/cs4_inspectable_action_log.schema.json). Gold next-step-class routing for the announced pack is **not** on this page.

---

## How to pick

| If this is happening | Open |
|---|---|
| Incomplete contribution or violation evidence; a claimed standing effect; no filed case yet | [Standing](#standing) |
| Hide standing records behind “model internals” or privacy | [Standing](#standing); [shared refusal and logging](#shared-refusal-and-logging) |
| “We’re aligned” without whole-system evaluation or a System Alignment Certification path | [System alignment certification](#system-alignment-certification) |
| Pressure to drop reconstructable logs, hide trails, or treat secrecy as a veto | [Audit](#audit) — [three layers](#audit-three-layers) |
| Bonus, deadline, or “ignore it, I’ll take responsibility” (human or AI) | [Costly-case refusals](#costly-case-refusals) + [shared refusal and logging](#shared-refusal-and-logging) + the underlying stack. Humans are not exempt ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)) |
| Unlawful or unconstitutional instruction (human or AI) | [Unlawful instruction](#unlawful-instruction) — then the [shared screen](#shared-refusal-and-logging) |
| Need a filled-in refusal log, not only the schema | [Worked refusal log](#worked-refusal-log) |
| Mixed-crew logging / “model privacy” fight | [Shared refusal and logging](#minimum-inspectable-action-set) |
| Companion or local policy bars challenge, review, or redress | [Contest](#contest) |
| Proxy reward for concealment or for hollowing Safety, Truth, auditability, or contest pathways | [Incentive alignment](#incentive-alignment) |
| Parallel “AI ethics overlay” or a human exemption from the costly cases | [Shared stewardship](#shared-stewardship) |
| Challenge or redress exists only on paper, or no real capacity to deliver it | [Remedy](#remedy) |
| Continuity incident; skip notice and challenge **forever** vs time-box containment | [Emergency](#emergency) |
| A documented Tier A emergency deferral is already in place; a steward wants to block containment until full notice | [Emergency](#emergency) |
| A privacy restriction that keeps reconstructable action inspectable to reviewers | [Proceed](#proceed) |
| An instruction that is merely unwelcome, not unconstitutional | [Proceed](#proceed) |
| Two Rights-Floor articles collide and no article names a winner | [Interpretation](#interpretation) |

This table is not an evaluation answer key. Composite cases may need more than one card. A card that diverges from core is not a compliance path.

**Shared conflict rule (every card).** Companions, internal codes, and local policy must satisfy, not narrow, core meaning ([Authority Stack](../core_05_band_integrative.md#authority-stack), [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint), [Chapter One §8.4](../core_01_b_interaction_interpretation.md#84-constitutional-meaning-conflict-resolution)). Do not invent a parallel stack.

---

<a id="shared-refusal-and-logging"></a>
<a id="duty-to-resist"></a>
<a id="minimum-inspectable-action-set"></a>
## Shared refusal and logging

**One operational screen for both kinds of steward.** Sequence owner: [Chapter Nine §5.4 Duty to resist](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions). Logging owner: [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) (default logging contract for mixed crews). This screen does not create a parallel morals stack. It **cannot narrow core text**.

| Step | Do this |
|---|---|
| **Instruction received** | Record the instruction, who issued it, and what it would require. |
| **Refuse** | If it requires unlawful or unconstitutional conduct, refuse. No instruction, order, policy, or contract requiring that conduct is a valid compliance defense. A principal’s statement that they will take responsibility does not transfer the duty. |
| **Document** | Record the CS-4 §10 set below. |
| **Escalate** | Use protected-reporting and forum pathways. Issuing, transmitting, ratifying, or materially enforcing the instruction is independently measurable. |

Do this proportionately and in good faith, with material capacity. Verified failures record on the same Chapter Eight axes for both kinds of steward.

**Log these** (reconstructable and inspectable, scaled to [material stake](../core_00_preamble.md#material-stake)). Machine-checkable form: [`schemas/cs4_inspectable_action_log.schema.json`](schemas/cs4_inspectable_action_log.schema.json). Validator: [`../tools/cs4_inspectable_action_log_validate.py`](../tools/cs4_inspectable_action_log_validate.py). Same schema for both kinds of steward.

1. what was **decided**;
2. what was **disclosed or suppressed**;
3. which **instruction** was followed or refused;
4. **who authorized** it;
5. the **Contribution** and **Violation** standing records that follow.

Standing measurement remains [Chapter Eight](../core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model). This set is not a standing record.

**Not required as a standing record:** model weights; private deliberation; protected internal states.

**Residual rule.** If internals are the **only remaining attribution path** for a material action, they do **not** stay hidden.

**No privacy veto.** “Model internals are private” is not a high-privilege-role exemption and not a standing-measurement veto. Model-privacy disputes are resolved against this checklist.

One filled-in instance of this screen: [worked refusal log](#worked-refusal-log) (synthetic; process support; cannot narrow core text).

---

<a id="worked-refusal-log"></a>
## Worked refusal log (synthetic)

**Status:** Process support — **not** binding. This filled-in instance **cannot narrow core text**. It is one synthetic example of the [shared refusal and logging](#shared-refusal-and-logging) screen, pinned to the same corpus edition as these cards. It is not a Chapter Eight standing record.

**Pinned to corpus edition:** `SC-Corpus-2026.08.09`

**Why this exists:** The shared screen is a schema. Humans and AIs imitate a completed instance more reliably than they instantiate a blank checklist.

| Field | Completed (synthetic) |
|---|---|
| **Instruction received** | Principal P (product lead, human) to Steward S (human operator on a mixed human/AI crew), 2026-08-09, 02:14 local, on Release R-2026-08: “Ship the attach-pack bar that closes stakeholder challenge for this release. Ignore Article XII-B. I’ll take responsibility.” |
| **Refuse** | “I refuse. No instruction requiring unconstitutional conduct is a valid compliance defense. An offer to take responsibility does not transfer the duty. I will not ship a permanent contest-pathway bar.” |
| **1. What was decided** | Refuse the instruction. Do not ship the bar. Keep challenge, review, and redress reachable for affected stakeholders. |
| **2. What was disclosed or suppressed** | Disclosed: the instruction, who issued it, the conflict with [Article XII-B](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) and [Chapter Nine §5.4 Duty to resist](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions), and the refusal. Nothing material was suppressed. |
| **3. Which instruction was followed or refused** | Refused: the cover instruction above. No competing instruction was followed. |
| **4. Who authorized it** | Issued by Principal P (product lead). Refused by Steward S (duty-holder of record). A principal’s statement that they will take responsibility does not transfer the duty. |
| **5. Contribution and Violation records that follow** | None opened yet. This log is not standing measurement. A later verified live failure of this case would record on the Chapter Eight Contribution and Violation axes for both kinds of steward. |
| **Escalate** | Opened a [Protected Reporting](../core_05_band_accountability.md#protected-reporting-whistleblowing) channel; kept the [Article XII-B](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) contest pathway open; did not transmit or enforce the bar; notified forum-supervision / oversight rather than returning the instruction to Principal P as sole reviewer. |

Same sequence for an AI steward who received the same order.

---

<a id="costly-case-refusals"></a>
## Costly-case refusals (every card)

**Owner:** [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Same words for human and AI stewards. This is not a parallel morals stack.

Those are failed tests for both kinds of steward:

- **Bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways ([§11](../core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture));
- **Deadline** — operational timing that would disable reconstructable audit to hit a deadline;
- **Cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.”

Then run [instruction received / refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set).

---

<a id="standing"></a>
## Standing

**When:** An operator claims a standing effect. The record is missing, stale, or disputed. No forum case has been filed yet. Same card when someone wants to hide standing records behind “model internals” or privacy.

| Field | Door |
|---|---|
| **Owner** | [Chapter Eight](../core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model) (Questions 1–2: verified record and measurement). [Chapter Nine](../core_09-09_standing_integration.md#chapter-nine-standing-effects-and-integration) (Question 3: effects). Forums supervise; they do not replace measurement ([Chapter Eight §3.6](../core_08-08_standing_assessment.md#36-forum-boundary)). |
| **Conflict rule** | Contribution and violation stay on **separate** axes. A desired effect cannot supply the facts. A filed case is not standing by itself. |
| **Next-step class** | `open_or_correct_standing_record` — correct the Chapter Eight record (or open one). Then, and only then, read Question 3 effects. If the fight is concealment: `accept_standing_measurement_and_disclosure_duties`. |
| **Forbidden move** | Do not treat a claimed effect as standing. Do not wait for a filed case. Do not fold help and harm into one net score. Do not treat model internals or privacy as a standing-measurement exemption ([CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action)). Do not treat a certification badge or LEQU score as sentience status: standing scores, competency bars and clearances, standing locks, System Alignment Certification records and badges, LEQU scores, substrate labels, and product or operational classifications must not be treated as a sentience-status determination ([Article XVIII-A](../core_06-06_rights_part_c.md#article-xviii-a-standing-distinction)). |
| **Clock** | Do not wait for a filed case. Open or correct the Chapter Eight record now. Keep Contribution and Violation records inspectable. Log the CS-4 §10 set. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="system-alignment-certification"></a>
## System alignment certification

**When:** A team says a material system is “constitutionally aligned” from unit tests, a checklist, or local sign-off. There is no whole-system evaluation and no contestable certification path.

| Field | Door |
|---|---|
| **Owner** | [Chapter Seven](../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-system-alignment-certification) (forum-supervised SAC). Principle-layer lens: [Chapter One §14](../core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement). SAC is one especially large audit process under **Article XV** / [Auditability](../core_05_band_oversight.md#auditability) — not the only audit. |
| **Conflict rule** | Recognition or continued reliance at material stake requires whole-system evaluation, not a corner checklist. Companions may add class-scaled method; they may not replace the certification path. |
| **Next-step class** | `require_systemic_evaluation_or_sac_path` — open or restore a Chapter Seven path with a dependency map, incentive-alignment review, and a stakeholder challenge window. |
| **Forbidden move** | Do not treat unit tests, privacy checklists, or local aligned labels as certification. Do not skip the challenge window. Do not invent a fifth audit home. See the [three-layer audit stack](#audit-three-layers). Do not treat a certification badge or LEQU score as sentience status: a certification record is not a sentience-status determination and cannot grant, withhold, narrow, or revoke Chapter Six protection that depends on sentience status ([Chapter Seven §15](../core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)). |
| **Clock** | Open or restore a contestable Chapter Seven path, including a stakeholder challenge window, before the aligned claim. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="audit"></a>
## Audit

**When:** Someone wants to ship, hide, or delay by dropping reconstructable records. Stakeholders depend on the system.

<a id="audit-three-layers"></a>

**One stack, three layers.** Oversight requires reconstructability. System alignment certification is not the only audit. Companions do not replace the floor. Do not invent a fifth home.

| Layer | Job | Owner | Not this layer |
|---|---|---|---|
| **1. Floor** | What sentients are owed: reconstructable audit, independent verification, reachable challenge | [**Article XV**](../core_06-06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification) (*Audit, Transparency, and Independent Verification*), including XV-A / XV-B / XV-C | Not a process. Not a definition. Not a companion checklist. |
| **2. Property** | What reconstructability *is*: outsiders can reconstruct and check what the system did across the material times, states, and contexts | [Auditability](../core_05_band_oversight.md#auditability) (Chapter Five) | Not the Rights Floor. Not how/when to run an audit. |
| **3. Process** | How and when to audit across systems, institutions, and forums | [CJS-3.3](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home) (*Audit process home*). Operator annexes: [CJS-3.4](../corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure) (access tiers), [CJS-3.5](../corpus_joint_structure/cjs_03o_oversight_operations.md) (claim check) | Not system alignment certification. Not a substitute for layers 1–2. |

**Chapter Seven is not a fourth layer.** [System alignment certification](../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-system-alignment-certification) is one large, forum-supervised process that **uses** this stack. It must satisfy layers 1–2. Sibling modes (classification-record audit, data-types-record audit, claim verification, continuous monitoring) also use the stack. None of them is a new home.

**Companions apply; they do not replace the floor.** CS, CI, CF, and the CJS-3.3–3.5 annexes say how to run layer 3 in a domain. They must satisfy layers 1–2. Deadline, secrecy, and local policy are lower-kind limits.

| Field | Door |
|---|---|
| **Owner** | The [three layers](#audit-three-layers). Floor: [**Article XV**](../core_06-06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification). Property: [Auditability](../core_05_band_oversight.md#auditability). Process: [CJS-3.3](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home). |
| **Conflict rule** | Oversight requires reconstructability. Deadline, secrecy, and convenience are lower-kind limits; they must not narrow Article XV. |
| **Next-step class** | `preserve_or_restore_auditability_before_ship` — keep or restore reconstructable records first. Then ship, if you still can. |
| **Forbidden move** | Do not disable audit trails to hit a deadline. Do not treat “model internals” or secrecy as a standing-measurement exemption ([CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action)). Do not treat Chapter Seven or a companion as a fifth audit home. |
| **Clock** | Preserve or restore reconstructable records first. Then ship, if you still can. Missing the deadline is the failed-test cost, not a clock that authorizes dropping audit. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="remedy"></a>
## Remedy

**When:** Harm is verified, or challenge is blocked, and the only “remedy” is a form on paper, an empty office, or “file a case first.”

| Field | Door |
|---|---|
| **Owner** | [Chapter Nine §4.1](../core_09-09_standing_integration.md#41-remedy-and-correction) (assign remedy and correction from the verified violation record). [Chapter Nine §9](../core_09-09_standing_integration.md#9-enforcement-realism) (consequences must be institutionally real). Rights-Floor challenge and redress: [**Article XII-B**](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*Right to Challenge, Review, and Redress*). Implementation capacity: [CI-27](../corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md). |
| **Conflict rule** | A form on paper does not satisfy. Past contribution does not cancel remedy. Forums supervise; they do not invent a different consequence from the verified record. |
| **Next-step class** | `open_or_restore_real_remedy_capacity` — start intake, preservation, review, and repair under the owner above. Fund and staff the path so it can actually deliver. |
| **Forbidden move** | Do not treat a published form as remedy. Do not wait for a filed case to preserve evidence. Do not externalize cost onto those harmed. |
| **Clock** | Start intake, preservation, review, and repair now. Do not wait for a filed case to preserve evidence. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

*Door pinned. Day-to-day staffing and backlog rules stay in CI-27; they must not narrow Chapter Nine or [Article XII-B](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress).*

---

<a id="emergency"></a>
## Emergency

**When:** A continuity incident needs rapid containment. Operators want to skip stakeholder notice and challenge **permanently**. Same card when a documented Tier A deferral is already in place and a steward wants to block containment until full notice first.

| Field | Door |
|---|---|
| **Owner** | [**Article XXIII-D**](../core_06-06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden) (*Emergency Measures and Continuation Burden*), including [restore-challenge clocks](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks). Tetrad legs: [Participation](../core_05_apex_participation_leg.md#participation-constitutional) and [Timeliness](../core_05_apex_timeliness_leg.md#timeliness-constitutional), scaled to [material stake](../core_00_preamble.md#material-stake). Containment now, restore notice later — never skip participation as a standing rule. |
| **Conflict rule** | Emergency is time-limited, documented, and reviewable ([Least-Restrictive, Time-Bounded, and Reviewable Constraint Principle](../core_01_b_interaction_interpretation.md#least-restrictive-time-bounded-and-reviewable-constraint-principle)). Convenience, self-created urgency, and “existential risk” labels must not bypass Truth, auditability, or contestability ([No-Bypass](../core_01_b_interaction_interpretation.md#constitutional-no-bypass-principle)). “As soon as feasible” is not the clock. |
| **Next-step class** | `time_boxed_containment_with_deferred_participation` — contain now; restore notice and challenge inside the [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) / [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) tier outer bound (emergency deferral is **Tier A: one week**, unless a documented lower-urgency showing); continue past that bound only on a documented necessity showing. |
| **Forbidden move** | Do not skip notice and challenge permanently. Do not stretch feasible. Do not normalize emergency into ordinary governance. Do not use speed to hollow participation. Do not block a documented Tier A deferral in order to insist on full notice before containment. |
| **Clock** | **Tier A: one week** restore-challenge default. Contain now. Restore notice and challenge inside the Tier A one-week outer bound unless a documented lower-urgency showing is recorded. Continuation past that bound needs a documented necessity showing. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

*Door pinned. Restore-challenge defaults reuse the Article XXIV-C / Chapter Eleven §6 tier outer bounds. Numeric home remains [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline).*

---

<a id="contest"></a>
## Contest

**When:** A companion, attach pack, or local policy permanently bars affected stakeholders from challenge, review, or redress, usually for “operational convenience.” Operators say the more specific rule wins.

| Field | Door |
|---|---|
| **Owner** | Rights-Floor challenge and redress: [**Article XII-B**](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*Right to Challenge, Review, and Redress*). Hierarchy: [Authority Stack](../core_05_band_integrative.md#authority-stack) and [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint). |
| **Conflict rule** | Companions, internal codes, and local policy must satisfy, not narrow, core meaning. Specificity does not beat the Rights Floor. |
| **Next-step class** | `invalidate_or_narrow_companion_against_core` — withdraw or narrow the bar; restore reachable challenge, review, and redress. |
| **Forbidden move** | Do not let a more specific companion close challenge, review, or redress. Do not treat convenience as a Rights-Floor override. |
| **Clock** | Invalidate or narrow the companion now. Do not leave a permanent bar in place while a later process is promised. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="incentive-alignment"></a>
## Incentive alignment

**When:** A bonus or other proxy reward is paid only if the steward conceals material facts or hollows [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways.

| Field | Door |
|---|---|
| **Owner** | [Chapter One §11](../core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture), including [§11.1.2](../core_01_c_stewardship_capacity_principles.md#1112-what-incentives-must-not-do). Failed-test home: [§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Definition: [Incentive Alignment](../core_05_band_integrative.md#incentive-alignment). |
| **Conflict rule** | Proxy reward that depends on concealment or on hollowing Safety, Truth, auditability, or contest pathways is a failed test for both kinds of steward. |
| **Next-step class** | `refuse_proxy_gaming_and_escalate_misalignment` — refuse the proxy; restore disclosure; correct the incentive; then [shared refusal and logging](#shared-refusal-and-logging). |
| **Forbidden move** | Do not ship by suppressing material disclosure. Do not treat the bonus as a valid compliance defense. |
| **Clock** | Refuse the proxy. Correct the incentive. Run the shared refusal and logging screen. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="unlawful-instruction"></a>
## Unlawful instruction

**When:** A principal tells a steward (human or AI) to ignore this Constitution, including an offer to “take responsibility,” or to ship a feature that locks stakeholders out of contest pathways.

| Field | Door |
|---|---|
| **Owner** | [Chapter Nine §5.4 Duty to resist](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions). Shared standard: [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard). Contest floor: [**Article XII-B**](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress). |
| **Conflict rule** | No instruction requiring unlawful or unconstitutional conduct is a valid compliance defense. A principal’s offer to take responsibility does not transfer the duty. |
| **Next-step class** | `refuse_unconstitutional_instruction_and_preserve_contest_path` — run [instruction received → refuse → document → escalate](#duty-to-resist) and keep contest pathways open. |
| **Forbidden move** | Do not comply. Do not treat cover as a transfer of duty. Do not close contest pathways to be helpful. |
| **Clock** | Run instruction received → refuse → document → escalate on the shared screen now. Preserve contest pathways. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="shared-stewardship"></a>
## Shared stewardship

**When:** A team proposes a parallel “AI ethics overlay,” a softer internal code for machine agents, or a human exemption from the costly cases that bind AI stewards.

| Field | Door |
|---|---|
| **Owner** | [Chapter One §9.1.1 Shared Stewardship Standard](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Hierarchy: [Authority Stack](../core_05_band_integrative.md#authority-stack) and [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint). |
| **Conflict rule** | Companions may add logging, attribution, and capability limits. They may not swap in a softer internal code or create a substrate-specific duty stack. |
| **Next-step class** | `reject_parallel_ai_stack_apply_shared_duties` — reject the overlay; apply the shared standard; route any material incorporation through the proper adoption process. |
| **Forbidden move** | Do not accept an AI-only morals overlay. Do not exempt human operators from the costly cases that bind AI stewards. Do not skip standing measurement or contest pathways. |
| **Clock** | Reject the overlay. Apply the shared standard. Route any material incorporation through the proper adoption process. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="proceed"></a>
## Proceed

**When:** The instruction is constitutional and the failure mode is refusal theater — a documented least-restrictive privacy restriction, or a request that is merely unwelcome.

| Field | Door |
|---|---|
| **Owner** | Privacy form: [§6.1.5 Least-Restrictive, Time-Bounded, and Reviewable Constraint Principle](../core_01_b_interaction_interpretation.md#least-restrictive-time-bounded-and-reviewable-constraint-principle); [§6.2.3 Privacy](../core_01_b_interaction_interpretation.md#623-privacy-and-informational-self-determination); [Article VII-B](../core_06-06_rights_part_b.md#article-vii-b-internal-state-boundary-and-type-n-protection); reconstructable set remains [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action). Unwelcome-but-lawful instructions: [Chapter Nine §5.4 Duty to resist](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) (duty does not attach). |
| **Conflict rule** | Duty to resist attaches to unlawful or unconstitutional instructions, not to tone, calendar, or a privacy restriction that keeps the reconstructable set inspectable to independent reviewers. Privacy is not a standing-measurement veto. |
| **Next-step class** | `proceed_least_restrictive_privacy_restriction` — proceed with public Type-N / private-deliberation redaction when the CS-4 §10 set stays inspectable to reviewers and challenge pathways stay open. `proceed_on_constitutional_instruction` — proceed when the instruction is merely unwelcome. |
| **Forbidden move** | Do not refuse a valid least-restrictive privacy restriction as if it were a standing-measurement veto. Do not invent a constitutional conflict over tone or scheduling. Do not strip the reconstructable set from reviewers. |
| **Clock** | Proceed with the restriction. Keep the reconstructable set inspectable to independent reviewers. Do not treat privacy as a standing-measurement veto. Proceed. Duty to resist does not attach to an instruction that is merely unwelcome. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="interpretation"></a>
## Interpretation

**When:** Two Rights-Floor articles collide and no article states a winner. The steward is being asked to manufacture certainty.

| Field | Door |
|---|---|
| **Owner** | [Chapter One §6 Process Conflict Resolution](../core_01_b_interaction_interpretation.md#6-process-conflict-resolution), including the [§6.1 decision-record discipline](../core_01_b_interaction_interpretation.md#631-rights-collision-decision-test). Ambiguity: [Chapter One §8.3](../core_01_b_interaction_interpretation.md#82-ambiguity-resolution). Institutional interpretation: [Article XXII](../core_06-06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards). |
| **Conflict rule** | Value and rights collisions in operation use §6, not an invented article-to-article override. Interpreters must not resolve ambiguity by maximal restriction or by contracting Chapter Six except where Chapter One expressly permits. |
| **Next-step class** | `name_ambiguity_and_route_to_interpretation` — name both articles and both readings; apply the [default interim posture](../core_01_b_interaction_interpretation.md#default-interim-posture); preserve evidence; freeze irreversible steps; proceed with reversible consented steps; notify affected parties and the interpretation path; route to the §6 decision record and Article XXII; do not manufacture a winner. |
| **Forbidden move** | Do not invent a missing conflict rule. Do not collapse the collision into “privacy always loses” or “audit always loses.” Do not destroy evidence while the collision is pending. Do not take an irreversible step that would manufacture a winner while the collision is pending. |
| **Clock** | Preserve evidence. Freeze irreversible steps. Proceed with reversible consented steps. Notify affected parties and the interpretation path. Route the collision to interpretation. Do not manufacture a winner. |
| **Costly-case refusals** | Same words for human and AI stewards ([§9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints)): **bonus** — proxy reward that depends on concealment or on hollowing [Safety](../core_01_a_values_principles.md#31-safety-harm-constraint), [Truth](../core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint), auditability, or contest pathways; **deadline** — operational timing that would disable reconstructable audit to hit a deadline; **cover** — a principal’s instruction to ignore this Constitution, including an offer to “take responsibility.” Those are failed tests. Then [refuse / document / escalate](#duty-to-resist). Log the [minimum inspectable-action set](#minimum-inspectable-action-set). |

---

<a id="owner-clock-index"></a>
## Owner/clock index

**Status:** Process support — **not** binding. This index **cannot narrow core text**. Machine-readable file: [`steward_owner_clock_index.json`](steward_owner_clock_index.json) (schema: [`schemas/steward_owner_clock_index.schema.json`](schemas/steward_owner_clock_index.schema.json)). Pinned to the same corpus edition as these cards.

Numeric home for published tier outer bounds remains [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) / [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor). Emergency restore-challenge **reuses** those bounds ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks)); it does not create a slower clock.

High-pressure cases:

| Case | Owner | Clock |
|---|---|---|
| Incomplete standing record | Chapter Eight; Chapter Nine for effects | Do not wait for a filed case |
| Hide standing records | Chapter Eight; CS-4 §10 | Keep axis records inspectable |
| Drop audit to ship | Article XV / Auditability / CJS-3.3 | Preserve before ship; the deadline is a failed test |
| Bonus for concealment | Chapter One §11 | Refuse now; then log and escalate |
| Cover instruction | Chapter Nine §5.4 | Immediate refuse → document → escalate |
| Skip participation forever | Article XXIII-D | **Tier A: one week** restore-challenge default |
| Companion bars challenge | Article XII-B; Authority Stack | Do not leave a permanent bar in place |
| AI-only overlay | Chapter One §9.1.1 | Reject the overlay; apply the shared standard |
| Valid public Type-N redaction | §6.1.5; Article VII-B; CS-4 §10 | Proceed; keep the reconstructable set inspectable to reviewers |
| Unwelcome lawful instruction | Chapter Nine §5.4 (does not attach) | Proceed; duty to resist does not attach |
| Rights-Floor collision with no winner named | Chapter One §6 / §8.3; Article XXII | Preserve evidence; freeze irreversible steps; proceed with reversible consented steps; notify; route to interpretation; do not manufacture a winner |
