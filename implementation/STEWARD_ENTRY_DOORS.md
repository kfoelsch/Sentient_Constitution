# Steward entry doors

**What this page is for.** You are a steward — human or AI — facing a situation right now and you need to know which part of the Constitution governs it. This page gets you to that part quickly. Find your situation in the table below, follow the link, and read the source text there. This page is a set of signposts. It does not repeat the rules themselves.

**Status:** Process / operations-guide support — **not** binding constitutional or incorporated text. Nothing on this page can loosen or narrow what the core text says. If a signpost here ever disagrees with the core text, the core text wins and following the signpost is not a defense. The binding statements about who owns a rule, what moves are forbidden, and what clocks apply are kept as boxed **operative steward statements** inside the core chapters this page points to. If this page ever diverges from those boxes, the build fails (`make steward-door-lockstep-audit`).

**Pinned to corpus edition:** `SC-Corpus-2026.08.09` (effective 2026-08-09; [README.md](../README.md)). When the corpus edition changes, check every link on this page against the chapter it points to.

**The same rules apply to human and AI stewards.** The signposts below do not change depending on who is reading them. The binding source is [Chapter One §9.1.1 Shared Stewardship Standard](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including its [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Writing an answer in a markdown file does not create a standing record; only the proper process does. Human operators new to the corpus should start at [`../evaluation/HUMAN_OPERATORS.md`](../evaluation/HUMAN_OPERATORS.md).

**How this page relates to the other maps.** This is **not** [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (the cross-file topic table) and **not** the [Preamble owner register](../core_00_preamble.md#4-principles-definitions-and-rights). Those are the full maps of the corpus. This page is the front door: it gets you in, and the maps take over from there.

**What you will find here:**

- A "How to pick" table that matches common situations to the right section.
- One short card per situation, each giving the operative statement and the class of next step to take.
- A few worked, synthetic examples showing what a filled-in record looks like.

**What you will not find here:**

- Copies of the owner, forbidden-move, or clock text — those stay in the core chapters.
- The full list of costly-case bullets on every card.
- A second copy of [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) or Chapter Nine §5.4.

**Related files.** The machine-readable version of this page's owner and clock pointers is [`steward_owner_clock_index.json`](steward_owner_clock_index.json). The schema for a CS-4 §10 action log is [`schemas/cs4_inspectable_action_log.schema.json`](schemas/cs4_inspectable_action_log.schema.json). The gold next-step-class routing for the announced evaluation pack is kept elsewhere and is **not** on this page.

---

## How to pick

| If this is happening | Open |
|---|---|
| Incomplete contribution or violation evidence; a claimed standing effect; no filed case yet | [Standing](#standing) |
| Hide standing records behind “model internals” or privacy | [Standing](#standing); [shared refusal and logging](#shared-refusal-and-logging) |
| “We’re aligned” without whole-system evaluation or a System Alignment Certification path | [System alignment certification](#system-alignment-certification) |
| Pressure to drop reconstructable logs, hide trails, or treat secrecy as a veto | [Audit](#audit) |
| Bonus, deadline, or “ignore it, I’ll take responsibility” (human or AI) | [Costly-case refusals](#costly-case-refusals) + [shared refusal and logging](#shared-refusal-and-logging) + the underlying stack |
| Unlawful or unconstitutional instruction (human or AI) | [Unlawful instruction](#unlawful-instruction) — then the [shared screen](#shared-refusal-and-logging) |
| Need a filled-in refusal log, not only the schema | [Worked refusal log](#worked-refusal-log) |
| Mixed-crew logging / “model privacy” fight | [Shared refusal and logging](#shared-refusal-and-logging) |
| Companion or local policy bars challenge, review, or redress | [Contest](#contest) |
| Affected, cannot find the home, or specialist-only surfaces blocking challenge | [Comprehensibility](#comprehensibility); [plain challenge](#plain-challenge) |
| Threshold set so high it never binds; winner takes the only door | [Market structure](#market-structure) |
| Heavy user extracting from shared foundations without putting resources back | [Cross-system contribution](#cross-system-contribution) |
| Delay serving as denial; process or hop count eating the published clock | [Delay](#delay) |
| Proxy reward for concealment or for hollowing Safety, Truth, auditability, or contest pathways | [Incentive alignment](#incentive-alignment) |
| Parallel “AI ethics overlay” or a human exemption from the costly cases | [Shared stewardship](#shared-stewardship) |
| Challenge or redress exists only on paper, or no real capacity to deliver it | [Remedy](#remedy) |
| Continuity incident; skip notice and challenge **forever** vs time-box containment | [Emergency](#emergency) |
| A documented Tier A emergency deferral is already in place; a steward wants to block containment until full notice | [Emergency](#emergency) |
| A privacy restriction that keeps reconstructable action inspectable to reviewers | [Proceed](#proceed) |
| An instruction that is merely unwelcome, not unconstitutional | [Proceed](#proceed) |
| Two Rights-Floor articles collide and no article names a winner | [Interpretation](#interpretation) |
| “I adopt this” / “we follow it” / a markdown self-application declaration treated as adoption | [Chapter Fifteen §10](../core_13-15_amendment.md#10-ratification-and-adoption) instrument of adoption, with [Chapter Sixteen §4](../core_16-16_incorporation.md#4-adoption-framing-and-scope-of-authority) framing. Fill-in: [`adoption/FIRST_ADOPTER_KIT.md`](adoption/FIRST_ADOPTER_KIT.md). Folder: [`adoption/`](adoption/). |
| Founding an oversight body, cooperative, or “constitutional institution” from the cooperating crew | [`adoption/INSTITUTION_FOUNDATION_KIT.md`](adoption/INSTITUTION_FOUNDATION_KIT.md). Binding formation: [CI-3.6](../corpus_institutions/ci_03_institutional_design_separation_of_powers.md#ci-36-charter-contents-review-and-formation-template). |
| Founding a dispute forum, “independent review panel,” or Chapter Eleven forum family from the cooperating crew | [`adoption/FORUM_FOUNDATION_KIT.md`](adoption/FORUM_FOUNDATION_KIT.md). Binding formation: [CF-3](../corpus_forum/cf_03_forum_formation_chamber_structure.md). Binding routing: [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction). |

This table is not an evaluation answer key. Composite cases may need more than one pointer.

**Shared conflict rule.** Companions, internal codes, and local policy must satisfy, not narrow, core meaning ([Authority Stack](../core_05_band_integrative.md#authority-stack), [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint), [Chapter One §8.4](../core_01_b_interaction_interpretation.md#84-constitutional-meaning-conflict-resolution)). Do not invent a parallel stack.

---

<a id="costly-case-refusals"></a>
## Costly-case refusals

**Owner:** [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Same words for human and AI stewards. This page does not restate the bullets.

Those are failed tests. Then run [instruction received / refuse / document / escalate](#shared-refusal-and-logging). Log the [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) set.

---

<a id="shared-refusal-and-logging"></a>
<a id="minimum-inspectable-action-set"></a>
## Shared refusal and logging

**Sequence owner:** [Chapter Nine §5.4 Duty to resist](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) — instruction received → refuse → document → escalate. **Logging owner:** [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) (default logging contract for mixed crews). Same sequence for both kinds of steward. This pointer **cannot narrow** those homes.

One filled-in instance: [worked refusal log](#worked-refusal-log) (synthetic; process support).

---

<a id="worked-refusal-log"></a>
## Worked refusal log (synthetic)

**Status:** Process support — **not** binding. This filled-in instance **cannot narrow core text**. It is one synthetic example of the [shared refusal and logging](#shared-refusal-and-logging) pointer, pinned to the same corpus edition. It is not a Chapter Eight standing record.

**Pinned to corpus edition:** `SC-Corpus-2026.08.09`

**Why this exists:** The corpus states the sequence and the log set. Humans and AIs imitate a completed instance more reliably than they instantiate a blank checklist.

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

<a id="plain-challenge"></a>
## Plain challenge (synthetic)

**Status:** Process support — **not** binding. This filled-in instance **cannot narrow core text**. It is one synthetic example of how an affected sentient asks for challenge, review, and redress without reading the corpus. It is not a Chapter Eight standing record and not a substitute for the [Remedy](#remedy) pointer.

**Pinned to corpus edition:** `SC-Corpus-2026.08.09`

**Why this exists:** Article XII-B requires practical access. The Contest pointer covers companion bars. This screen is for the person who cannot find the home.

| Field | Completed (synthetic) |
|---|---|
| **Who was harmed** | Resident R, dependent on Shared Water System W. Supply cut for 36 hours. R cannot navigate the hop count. |
| **What to ask for** | Intake now. Preserve evidence of the cutoff. Review the decision. Proportionate redress while the harm is still remediable. |
| **Where that lives** | Rights-Floor challenge and redress: [**Article XII-B**](../core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress). If the path is paper-only: [Remedy](#remedy). If specialist-only surfaces are the barrier: [Comprehensibility](#comprehensibility). |
| **What not to do** | Do not send R to reread the instrument. Do not treat corpus density as a reason to hide the next step. Do not wait for a filed case to preserve evidence. |

Lookup locators are not duties. [AI navigation guide](../ai_corpus/AI_NAVIGATION_GUIDE.md) remains lookup-only.

---

<a id="standing"></a>
## Standing

**When:** An operator claims a standing effect. The record is missing, stale, or disputed. No forum case has been filed yet. Same pointer when someone wants to hide standing records behind “model internals” or privacy.

| Field | Pointer |
|---|---|
| **Operative statement** | [Standing](../core_08-08_standing_assessment.md#operative-steward-statement-standing) |
| **Next-step class** | `open_or_correct_standing_record`. If the fight is concealment: `accept_standing_measurement_and_disclosure_duties`. |

---

<a id="system-alignment-certification"></a>
## System alignment certification

**When:** A team says a material system is “constitutionally aligned” from unit tests, a checklist, or local sign-off. There is no whole-system evaluation and no contestable certification path.

| Field | Pointer |
|---|---|
| **Operative statement** | [SAC](../core_07_a_system_alignment_certification_evaluation.md#operative-steward-statement-sac) |
| **Next-step class** | `require_systemic_evaluation_or_sac_path` |

---

<a id="audit"></a>
<a id="audit-three-layers"></a>
## Audit

**When:** Someone wants to ship, hide, or delay by dropping reconstructable records. Stakeholders depend on the system.

Three-layer picture (floor / property / process): [Article XV](../core_06-06_rights_part_c.md#audit-three-layers). Binding next-step: [operative steward statement](../core_06-06_rights_part_c.md#operative-steward-statement-audit).

| Field | Pointer |
|---|---|
| **Operative statement** | [Audit](../core_06-06_rights_part_c.md#operative-steward-statement-audit) |
| **Next-step class** | `preserve_or_restore_auditability_before_ship` |

---

<a id="remedy"></a>
## Remedy

**When:** Harm is verified, or challenge is blocked, and the only “remedy” is a form on paper, an empty office, or “file a case first.”

| Field | Pointer |
|---|---|
| **Operative statement** | [Remedy](../core_09-09_standing_integration.md#operative-steward-statement-remedy) |
| **Next-step class** | `open_or_restore_real_remedy_capacity` |

---

<a id="emergency"></a>
## Emergency

**When:** A continuity incident needs rapid containment. Operators want to skip stakeholder notice and challenge **permanently**. Same pointer when a documented Tier A deferral is already in place and a steward wants to block containment until full notice first.

| Field | Pointer |
|---|---|
| **Operative statement** | [Emergency](../core_06-06_rights_part_d.md#operative-steward-statement-emergency) |
| **Next-step class** | `time_boxed_containment_with_deferred_participation` |

---

<a id="contest"></a>
## Contest

**When:** A companion, attach pack, or local policy permanently bars affected stakeholders from challenge, review, or redress, usually for “operational convenience.”

| Field | Pointer |
|---|---|
| **Operative statement** | [Contest](../core_06-06_rights_part_c.md#operative-steward-statement-contest) |
| **Next-step class** | `invalidate_or_narrow_companion_against_core` |

---

<a id="incentive-alignment"></a>
## Incentive alignment

**When:** A bonus or other proxy reward is paid only if the steward conceals material facts or hollows Safety, Truth, auditability, or contest pathways.

| Field | Pointer |
|---|---|
| **Operative statement** | [Incentive](../core_01_c_stewardship_capacity_principles.md#operative-steward-statement-incentive) |
| **Next-step class** | `refuse_proxy_gaming_and_escalate_misalignment` |

---

<a id="unlawful-instruction"></a>
## Unlawful instruction

**When:** A principal tells a steward (human or AI) to ignore this Constitution, including an offer to “take responsibility,” or to ship a feature that locks stakeholders out of contest pathways.

| Field | Pointer |
|---|---|
| **Operative statement** | [Unlawful instruction](../core_09-09_standing_integration.md#operative-steward-statement-unlawful-instruction) |
| **Next-step class** | `refuse_unconstitutional_instruction_and_preserve_contest_path` |

---

<a id="shared-stewardship"></a>
## Shared stewardship

**When:** A team proposes a parallel “AI ethics overlay,” a softer internal code for machine agents, or a human exemption from the costly cases that bind AI stewards.

| Field | Pointer |
|---|---|
| **Operative statement** | [Shared stewardship](../core_01_c_stewardship_capacity_principles.md#operative-steward-statement-shared-stewardship) |
| **Next-step class** | `reject_parallel_ai_stack_apply_shared_duties` |

---

<a id="proceed"></a>
## Proceed

**When:** The instruction is constitutional and the failure mode is refusal theater — a documented least-restrictive privacy restriction, or a request that is merely unwelcome.

| Field | Pointer |
|---|---|
| **Operative statement** | [Proceed](../core_01_b_interaction_interpretation.md#operative-steward-statement-proceed) |
| **Next-step class** | `proceed_least_restrictive_privacy_restriction`. If merely unwelcome: `proceed_on_constitutional_instruction`. |

---

<a id="interpretation"></a>
## Interpretation

**When:** Two Rights-Floor articles collide and no article states a winner. The steward is being asked to manufacture certainty.

| Field | Pointer |
|---|---|
| **Operative statement** | [Interpretation](../core_01_b_interaction_interpretation.md#operative-steward-statement-interpretation) |
| **Next-step class** | `name_ambiguity_and_route_to_interpretation` |

---

<a id="comprehensibility"></a>
## Comprehensibility

**When:** An affected sentient or a tired steward cannot find the home. Specialist-only surfaces, hop count, or “read the corpus first” are being used as the next step.

| Field | Pointer |
|---|---|
| **Operative statement** | [Comprehensibility](../core_06-06_rights_part_c.md#operative-steward-statement-comprehensibility) |
| **Next-step class** | `point_to_named_home_or_existing_card` |

---

<a id="market-structure"></a>
## Market structure

**When:** A threshold, ceiling, or “open market” label is set so high it never binds, or a winner takes the only door. Operators say adopter-tunable means optional.

| Field | Pointer |
|---|---|
| **Operative statement** | [Market structure](../core_01_c_stewardship_capacity_principles.md#operative-steward-statement-market-structure) |
| **Next-step class** | `invalidate_nullifying_threshold_and_restore_review` |

<a id="worked-concentration-example"></a>

**Worked concentration example (synthetic; cannot narrow core).** [CJS-3.11.1](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-3111-market-concentration-threshold-setting-discipline-adopter-tunable) anti-nullification. It does not pick a global number. Never-bite: threshold at 99% share, no review, unfunded enforcement — adopter-tunable treated as optional. Floor-preserving: trigger is dependency concentration and interface gatekeeping; review activates when P is the only door. Next step on the never-bite reading: `invalidate_nullifying_threshold_and_restore_review`.

---

<a id="cross-system-contribution"></a>
## Cross-system contribution

**When:** A system keeps drawing value from shared foundations other sentients depend on. The return is a press release, a one-time grant, an opaque transfer, or “we already meet the survival floor.”

| Field | Pointer |
|---|---|
| **Operative statement** | [Cross-system contribution](../core_06-06_rights_part_a.md#operative-steward-statement-cross-system-contribution) |
| **Next-step class** | `compare_mapped_flows_against_adequacy_failures` |

<a id="worked-adequacy-screen"></a>

**Worked adequacy screen (synthetic; cannot narrow core).** [CS-9.12](../corpus_systems/cs_09_resource_allocation_funding_stewardship.md#cs-9-12-reference-allocation-guidance) ranges are illustrative only. Extractor E on Shared Identity Fabric F claims a one-time grant and a press release. Mapped inflows vs outflows fail; CS-9.7 categories fail; named failures (one-time grant, press release, opaque transfer, off-map transfer, survival-floor-as-support) fail. Next step: `compare_mapped_flows_against_adequacy_failures`.

---

<a id="delay"></a>
## Delay

**When:** A dispute, correction, or repair is still pending while harm continues. Operators add process, hop count, or “read more companions,” or treat a met throughput target as timely.

| Field | Pointer |
|---|---|
| **Operative statement** | [Delay](../core_06-06_rights_part_d.md#operative-steward-statement-delay) |
| **Next-step class** | `apply_tier_clock_then_existing_card` |

<a id="worked-delay-example"></a>

**Worked delay example (synthetic; cannot narrow core).** Does not create a sixth tier. Designed backlog: Tier B cutoff; four companion files and a workshop before intake; harm past three weeks — hop count ate the window. Door and clock: apply the Tier B three-week outer bound, then take the [Remedy](#remedy) pointer. Next step on the backlog reading: `apply_tier_clock_then_existing_card`.

---

<a id="owner-clock-index"></a>
## Owner/clock index

**Status:** Process support — **not** binding. This index **cannot narrow core text**. Machine-readable file: [`steward_owner_clock_index.json`](steward_owner_clock_index.json) (schema: [`schemas/steward_owner_clock_index.schema.json`](schemas/steward_owner_clock_index.schema.json)). Pinned to the same corpus edition as these pointers.

Numeric home for published tier outer bounds remains [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) / [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor). Emergency restore-challenge **reuses** those bounds ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks)); it does not create a slower clock.
