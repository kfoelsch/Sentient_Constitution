# User-facing software coverage audit

**Date:** 2026-09-10  
**Status:** Process / evidence support. This file does **not** bind. Indexes point; source binds.  
**Companion spreadsheet:** [cs_user_facing_software_matrix.csv](cs_user_facing_software_matrix.csv)  
**Twin (bodies, not software):** [MINIMUM_VIABLE_ADOPTER.md](../../implementation/adoption/MINIMUM_VIABLE_ADOPTER.md)  
**Method twin (data kinds, not surfaces):** [cs2_data_types_coverage_audit.md](../2026-08-31/cs2_data_types_coverage_audit.md)

## What this is

A coverage matrix, not a product catalog and not a new CS family. The 2026-08-31 CS-2 audit asked: for every named data kind, can we point at a type letter? This pass asks: for every **user-reachable act** the corpus already requires, can we point at a **capability surface** — who can do or inspect it, through what kind of interface, at what obligation strength — and does the **source** already say so?

Rows name **capabilities**, not apps. [CS-5](../../corpus_systems/cs_05_design_testing_verification_deployment.md) already states the rule this audit must not break: the Constitution defines required capabilities and outcomes; specific technical implementations may evolve.

**Out of the 2026-09-10 inventory pass:** corpus edits, a CS-13 family, software builds, and `make regression`. Findings stayed findings until the later home landed (this file, below).

## Scope

| Included | Excluded |
|---|---|
| Numbered `core_*` files where they name a do/inspect act | `archive/` |
| Incorporated companions (CS, CJS, CF, CI) where they name a reachable surface | Backend-only processing with no inspect or act |
| Chapter Five named records as **surfaces** (publish / inspect / challenge), not as data types | Invented products, portals, or a mandatory standing dashboard |
| `implementation/` schemas, dashboards, and templates as **nice-to-have** instantiations | Treating analog-sufficient functions as “must be digital” |

A **user-reachable act** is something an ordinary sentient, party, steward, auditor, forum participant, or the public must be able to **do or inspect** through a durable interface. Audiences other than “end user” still count. Digital is the usual form; analog (paper, hearing, published notice, manual continuity) remains lawful unless the source already requires a digital channel.

**Do not invent a standing portal for everyone.** [Chapter Eight §2.1](../../core_08_standing_assessment.md#21-silence-is-the-default) — silence is the default; most sentients never have a standing record. Tools under [§3.5](../../core_08_standing_assessment.md#35-implementation-tools) are optional and must not bury fields in a score.

## Two layers

| Layer | Question | CSV value |
|---|---|---|
| **Constitutional operating** | What must an adopter stand so the instrument can run? | `const-op` |
| **In-scope system** | What must any governed system expose to affected sentients? | `in-scope` |
| **Both** | Same act is both an operating surface and a duty on governed systems | `both` |
| **Process support** | `implementation/` only; cannot narrow core | `process-support` |

## Obligation and analog bands (auditor labels, not new duties)

| Obligation | Meaning |
|---|---|
| **must** | Source requires the capability for in-scope adopters |
| **class-scaled-must** | Required at a named CS-3 class, CS-4 steward tier, or Class A/B/C Type O baseline |
| **should** | Source uses “may” / “should” / “where used” |
| **nice-to-have** | Process support only |

| analog_ok | Meaning |
|---|---|
| **yes** | Paper, hearing, notice, or manual process can satisfy |
| **mixed** | Analog can satisfy unless digital publication or the same channel is already in use (Type O online-availability test; class-scaled logs) |
| **no** | Source requires a digital or machine-usable channel for that act |

The only binding **no** rows in this inventory are [CJS-3.17](../../corpus_joint_structure/cjs_03c_continuity_operations.md#digital-self-service-pathway-integrity) same-channel self-service and charge-exit **when entry was digital**, and [CS-12.5](../../corpus_systems/cs_12_decentralized_continuity_partition_resilience.md#cs-12-5-offline-audit-integrity-and-reconciliation) tamper-evident offline chains. Schema validators are `no` because they are machines, not duties.

## Assignment statuses

| Status | Meaning |
|---|---|
| **Explicit** | Source names a reachable surface (publish, inspect, file, contest, export, revoke, vote, …) |
| **Inferred** | Function is required and a surface is the practical satisfaction, but the home does not name the interface |
| **Process-support** | `implementation/` only |
| **Gap** | Named required act with no defensible surface under existing text |

## Counts

| Bucket | Count |
|---|---:|
| Named capability rows in the matrix | **108** |
| Explicit | 98 |
| Inferred | 3 |
| Process-support | 7 |
| Gap (no defensible surface) | **0** |
| Layer: constitutional operating | 49 |
| Layer: in-scope system | 46 |
| Layer: both | 6 |
| Layer: process support | 7 |
| Obligation: must | 72 |
| Obligation: class-scaled-must | 25 |
| Obligation: should | 4 |
| Obligation: nice-to-have | 7 |
| analog_ok: yes | 70 |
| analog_ok: mixed | 32 |
| analog_ok: no | 6 |

Every inventoried **required** act has at least one Explicit or Inferred surface. There is **no taxonomy hole** analogous to a missing CS-2 type letter. The remaining work is **integrator mapping** (who owns the surface) and a later CS pointer home — not a new product family.

---

## Constitutional operating surfaces

What an adopter must stand so the instrument can run. Full cites are in the CSV. Grouped here.

### Named records and Type O

| Capability | Audience | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|---|
| Publish / inspect Charter | public, steward, auditor | class-scaled-must | mixed | Explicit | [Charter](../../core_05_band_continuity.md#charter); [CI-3.6](../../corpus_institutions/ci_03_institutional_design_separation_of_powers.md#ci-36-charter-contents-review-and-formation-template) |
| Type O package (Charter, classification, data-types, certification public views) | public | class-scaled-must | mixed | Explicit | [Public Oversight Baseline Disclosure](../../core_05_band_oversight.md#public-oversight-baseline-disclosure); [CS-2 §7](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) |
| Inspect / challenge System Classification, Data Types, and Certification Records | public, party, auditor, forum | class-scaled-must | mixed | Explicit | CS-3 §7; CS-2 §8; [Ch.7 Part B §11–12](../../core_07_b_system_alignment_certification_record_process.md#11-certification-record) |
| Name record-opening authority and custodian on the Charter | steward, party, auditor | must | yes | Explicit | [Ch.8 §3.7](../../core_08_standing_assessment.md#37-record-custody-and-opening-authority); CI-3.6 field 11 |

Paywall of the Type O floor, where lawful online publication exists, is already a failure on the Chapter Five home. Analog-only posting does not satisfy that online-availability test; analog remains usable where digital publish is not the channel.

### Standing pipeline

| Capability | Audience | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|---|
| Notice when a standing record opens | subject | must | yes | Explicit | [Ch.8 §2.1](../../core_08_standing_assessment.md#21-silence-is-the-default) |
| Inspect own records; see the challenge path | subject, party, auditor, forum | must | mixed | Explicit | [Ch.8 §3.1](../../core_08_standing_assessment.md#31-minimum-record-contents) |
| Challenge, correct, version | subject, party, forum | must | yes | Explicit | [Ch.8 §3.4 / §3.6](../../core_08_standing_assessment.md#36-forum-boundary); [Ch.11 §2.3](../../core_11_forum.md#23-forum-records-standing-records-and-contests) |
| Integration record; remedy owed; lock terms; contest lock | party, subject, public | must | yes | Explicit | [Ch.9 §2](../../core_09_standing_integration.md#2-integration-record-and-decision-order), [§4.1](../../core_09_standing_integration.md#41-remedy-and-correction), [§5.3](../../core_09_standing_integration.md#53-record-visibility-and-escalation) |
| Plain-language statement of effect and burden | subject | must | yes | Explicit | [Ch.9 §7.2](../../core_09_standing_integration.md#72-plain-statement-of-effect-and-burden) |
| Lock-to-remedy performance figures | public, auditor | must | yes | Explicit | Ch.9 §4.4; [CI-27.2](../../corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md#ci-272-durability-backlog-and-publication); CF-11 |
| Competency bar / clearance (where a named pathway uses one) | ordinary sentient, steward | class-scaled-must | yes | Explicit | [Ch.9 §6.2](../../core_09_standing_integration.md#62-competency-bars-and-clearances) |
| Manual continuity during outage | steward, party, forum | must | yes | Explicit | [Ch.9 §2](../../core_09_standing_integration.md#2-integration-record-and-decision-order) |
| Optional standing tools / dashboards | steward | should | yes | Explicit | [Ch.8 §3.5](../../core_08_standing_assessment.md#35-implementation-tools) — may build; must not bury §3.1 fields |

A filed case is not standing by itself. Dashboards are optional. Do not treat “unrated” as a reason to open a record.

### Forum family

| Capability | Audience | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|---|
| File; published intake classes; contest routing | ordinary sentient, party | must | yes | Explicit | [Ch.11 §2](../../core_11_forum.md#2-default-venue-and-primary-stakes); CF-5.1/5.2 |
| Inspect forum case record; interim protection | party, forum, auditor | must | yes | Explicit | [Ch.11 §2.3](../../core_11_forum.md#23-forum-records-standing-records-and-contests); [interim protection](../../core_11_forum.md#interim-protection) |
| Reach each required distinct forum family; published structure map | filer, public | must | yes | Explicit | [CF-3.1](../../corpus_forum/cf_03_forum_formation_chamber_structure.md#cf-31-core-structural-rule); [CF-3.2](../../corpus_forum/cf_03_forum_formation_chamber_structure.md#cf-32-family-to-forum-structure-translation-map) |
| CF-15.1 standard record set (21 templates + status-adjudication format) | party, clerk, auditor | must | yes | Explicit | [CF-15.1](../../corpus_forum/cf_15_standard_records_forms_evidence_artifacts.md#cf-151-minimum-record-set) |
| Access-class tagging (party / public / audit / restricted) | party, public, auditor | must | mixed | Explicit | [CF-15.3](../../corpus_forum/cf_15_standard_records_forms_evidence_artifacts.md#cf-153-access-classes) |
| Performance / backlog / accessibility metrics; matter status | public, party | must | mixed | Explicit | [CF-11](../../corpus_forum/cf_11_performance_backlog_publication_accessibility.md) |
| Capacity-failure filing outside the starved body | party, reporter | must | yes | Explicit | [CF-5.4](../../corpus_forum/cf_05_routing_operations_transfer_certification_representative_treatment.md#cf-54-capacity-failure-routing) |
| Continuity-mode filing and status communications | party | must | yes | Explicit | [CF-12.4](../../corpus_forum/cf_12_forum_continuity.md#cf-124-continuity-minimum-functions); [CF-12.6](../../corpus_forum/cf_12_forum_continuity.md#cf-126-communication-duties) |
| Sentience-status file / inspect / independent representative | ordinary sentient, party, forum | must | yes | Explicit | [Article V-E](../../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor); [CF protocol](../../corpus_forum/cf_sentience_status_record.md) |
| Protected reporting | ordinary sentient, steward | must | yes | Explicit | [Protected Reporting](../../core_05_band_accountability.md#protected-reporting-whistleblowing); [Article XII-B](../../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) |

Twenty-one CF-15.1 templates are **one capability** (standard forms), not twenty-one products. Combining forms must not hide actor, authority, facts, review path, or family.

### Governance, voting, seats, remedy offices

| Capability | Audience | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|---|
| Published legitimacy mechanism; vote / verify outcomes; recall-class transfer | ordinary sentient, public, auditor | must | mixed | Explicit | [Ch.12 §1.1](../../core_12_governance.md#11-mechanism-families-auditability-and-pluralism); [§4](../../core_12_governance.md#4-voting-and-binding-collective-choice-protocols); [§1.3](../../core_12_governance.md#13-recall-class-pathways-and-mid-cycle-transfer-guardrails) |
| Role definitions; seat catalog; lane map | steward, public, auditor | must | mixed | Explicit | [Ch.12 §5](../../core_12_governance.md#5-authorized-roles-competency-development-and-contribution); [CI-4.6](../../corpus_institutions/ci_04_appointment_competency_rotation_removal.md#ci-46-seat-catalog); [CI-3.2](../../corpus_institutions/ci_03_institutional_design_separation_of_powers.md#ci-32-functional-separation-lanes) |
| Stakeholder notice, participation windows, weighting publication | party, public | must | yes | Explicit | [CI-8.1](../../corpus_institutions/ci_08_transparency_participation_accessible_pathways.md#ci-81-stakeholder-oversight-notification-and-binding-governance-pathway-integrity); [CI-8.2](../../corpus_institutions/ci_08_transparency_participation_accessible_pathways.md#ci-82-anti-concentration-and-participation-legitimacy-safeguards); [Article XI](../../core_06_rights_part_b.md#article-xi-a-stakeholder-system-participation-and-representation) |
| Remedy intake; contest under-capacity | party | must | yes | Explicit | [CI-27](../../corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md); [Ch.9 §9](../../core_09_standing_integration.md#92-remedy-system-durability) |
| Contest-integrity monitor outputs; control-failure notices; external-assurance triggers | public, auditor, party | class-scaled-must | mixed | Explicit | [CI-7.1–7.3](../../corpus_institutions/ci_07_oversight_assurance_controls_evidence.md) |
| Refuse unlawful instruction; document; escalate | steward | must | mixed | Explicit | [Ch.9 §5.4](../../core_09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions); [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) |

---

## In-scope system surfaces

What any governed system must expose to affected sentients. Class scaling is already in CS-3 / CS-4.

### Identity, consent, portability, self-service

| Capability | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|
| Revoke, rotate, correct identity and attribution credentials | must | yes | Explicit | [CS-2 §1.1](../../corpus_systems/cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability); [Article VII-A](../../core_06_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind) |
| Export / migrate continuity-critical data on disclosed paths | class-scaled-must | mixed | Explicit | [CS-2 §1.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#12-continuity-critical-collection-and-exportability); [Article XIX-A](../../core_06_rights_part_c.md#article-xix-a-portability-rights); [CJS-3.17](../../corpus_joint_structure/cjs_03c_continuity_operations.md#collection-time-exportability-and-continuity-critical-data-integrity) |
| Digital self-service enroll / manage / exit (same channel class) | must (if entry is digital) | **no** | Explicit | [CJS-3.17](../../corpus_joint_structure/cjs_03c_continuity_operations.md#digital-self-service-pathway-integrity); [CI-8.3](../../corpus_institutions/ci_08_transparency_participation_accessible_pathways.md#ci-83-digital-self-service-pathway-integrity) |
| Stop charges through a published path | must (if digital entry / recurring charges) | **no** | Explicit | [CJS-3.17 charge-exit](../../corpus_joint_structure/cjs_03c_continuity_operations.md#commitment-renewal-and-charge-exit-integrity) |
| Exit-feasibility and dependency disclosure | must | yes | Explicit | [CJS-3.17](../../corpus_joint_structure/cjs_03c_continuity_operations.md#exit-feasibility-disclosure-and-dependency-transparency); [Article XIX-C](../../core_06_rights_part_c.md#article-xix-c-anti-lock-in-rule) |
| Grant / refuse / revoke consent | must | yes | Explicit | [Consent](../../core_05_band_participation.md#consent-constitutional) |
| Control own experiential / derived data | must | mixed | Explicit | [Article VIII-B](../../core_06_rights_part_b.md#article-viii-b-experiential-and-derived-data-rights) |
| Training-data consent and revocation | must | mixed | Explicit | [Article VIII-D](../../core_06_rights_part_b.md#article-viii-d-creative-work-training-data-use-and-anti-displacement) |
| Likeness / reputation consent and contest | must | yes | Explicit | [Article VIII-A](../../core_06_rights_part_b.md#article-viii-a-self-ownership-of-likeness-and-reputation) |
| Chokepoint appeal, human review, export | class-scaled-must | mixed | Explicit | [CS-4.14](../../corpus_systems/cs_04_critical_system_stewardship.md#cs-4-14-private-chokepoints-sentients-depend-on-access-continuity-and-non-capture) |

If a system has **no** digital entry, CJS-3.17 does not force a digital channel. It forbids making exit harder than the entry channel that was actually used.

### Oversight, audit, comprehensibility, challenge

| Capability | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|
| Challenge, review, redress entry | must | yes | Explicit | [Article XII-B](../../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) |
| Reconstruct what the system did; qualified audit access | class-scaled-must | mixed | Explicit | [Article XV-A](../../core_06_rights_part_c.md#article-xv-a-auditability-and-observable-evidence); [CJS-3.3](../../corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-how-we-audit); [CS-2 §5.3](../../corpus_systems/cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) |
| Plural independent oversight; challenge verification barriers | must | yes | Explicit | [Article XV-B](../../core_06_rights_part_c.md#article-xv-b-distributed-oversight-and-anti-monopoly-review); [XV-C](../../core_06_rights_part_c.md#article-xv-c-verification-accessibility) |
| Compare alternative interpretations; contest rankings | must | mixed | Explicit | [Article XIV-B](../../core_06_rights_part_c.md#article-xiv-b-transparency-auditability-and-contestability) |
| Proportional comprehensibility; summaries plus drill-down | must / class-scaled-must | mixed | Explicit | [Article XX-A](../../core_06_rights_part_c.md#article-xx-a-proportional-comprehensibility-right); [CS-6](../../corpus_systems/cs_06_comprehensibility_complexity_stewardship.md); [CJS-3.8](../../corpus_joint_structure/cjs_03p_participation_operations.md#high-impact-drill-down-and-assisted-evaluation) |
| Inspectable attributable-action log (five-element set) | class-scaled-must | mixed | Explicit | [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) — role-scoped; **not** an ordinary-person surveillance dashboard |
| Risk disclosure; crisis communications; root-cause register | class-scaled-must | yes / mixed | Explicit | Risk Disclosure home; [CS-5 §8](../../corpus_systems/cs_05_design_testing_verification_deployment.md#cs-5-8-governance-continuity-crisis-communications-and-exercises-high-impact-systems); [CS-5 §9](../../corpus_systems/cs_05_design_testing_verification_deployment.md#cs-5-9-self-healing-and-recovery-path-integrity) |

### Continuity, restriction, funding, repair

| Capability | Obligation | analog_ok | Status | Owner stack |
|---|---|---|---|---|
| Restriction-validation record; scheduled review | must | yes | Explicit | [CS-7.3](../../corpus_systems/cs_07_justice_safeguards_restitution_rehabilitation.md#cs-7-3-mandatory-validation-record) |
| Dependent-systems map; funding inspect and challenge | class-scaled-must | mixed | Explicit | [CS-9](../../corpus_systems/cs_09_resource_allocation_funding_stewardship.md#cs-9-4-dependent-systems-map) |
| Transition phase publication and gate challenge | must | yes | Explicit | [CS-10](../../corpus_systems/cs_10_transition_constitution_migration_governance.md#cs-10-2-phased-transition-structure) |
| Subversion declaration inspect; exclusion challenge | must | yes | Explicit | [CS-11](../../corpus_systems/cs_11_subversion_response_replacement_reconstitution.md) |
| Continuity modes; partition-local contestability | class-scaled-must | mixed | Explicit | [CS-12.2](../../corpus_systems/cs_12_decentralized_continuity_partition_resilience.md#cs-12-2-continuity-modes-and-rights-floor-invariants) |
| Tamper-evident offline audit chains | class-scaled-must | **no** | Explicit | [CS-12.5](../../corpus_systems/cs_12_decentralized_continuity_partition_resilience.md#cs-12-5-offline-audit-integrity-and-reconciliation) |
| Ecological-footprint reporting | must | mixed | Explicit | [Article I-B](../../core_06_rights_part_a.md#article-i-b-ecological-footprint-and-transparency) |
| Repair docs / tools / parts / diagnostics | must | mixed | Explicit | [Article II-B](../../core_06_rights_part_a.md#article-ii-b-repair-maintenance-and-independent-servicing) |
| Occupancy / eviction contest with notice | must | yes | Explicit | [Occupancy Continuity](../../core_05_band_continuity.md#occupancy-continuity-constitutional) |
| Experiment opt-in, sandbox disclosure, rollback | must | yes | Explicit | [Article XVII-B](../../core_06_rights_part_c.md#article-xvii-b-containment-disclosure-and-opt-in) |
| Restore notice and challenge after emergency | must | yes | Explicit | [Article XXIII-D](../../core_06_rights_part_d.md#xxiii-d-restore-challenge-clocks) |

---

## Process-support instantiations (not duties)

| Artifact | What it is | Binding home if any |
|---|---|---|
| [cs4_inspectable_action_log.schema.json](../../implementation/schemas/cs4_inspectable_action_log.schema.json) | Machine-checkable form of the five-element set | [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) |
| [sentience_status_adjudication_record.schema.json](../../implementation/schemas/sentience_status_adjudication_record.schema.json) | Machine-checkable form | [Article V-E](../../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor); [CF protocol](../../corpus_forum/cf_sentience_status_record.md) |
| [ch06_assessment.schema.json](../../implementation/schemas/ch06_assessment.schema.json) | Logical Chapter Eight snapshot | Optional under [Ch.8 §3.5](../../core_08_standing_assessment.md#35-implementation-tools) |
| [STEWARD_ENTRY_DOORS.md](../../implementation/STEWARD_ENTRY_DOORS.md) + owner/clock index | Pointer index | Core boxed operative statements |
| [CONTINUITY_RESILIENCE_DASHBOARD.md](../../implementation/CONTINUITY_RESILIENCE_DASHBOARD.md) | Drill-list stub | Not a CS-12 duty |
| [SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md](../../implementation/SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md) | System/model cards, incident packets | Packaging aid for artifacts already required in substance |
| [MINIMUM_VIABLE_ADOPTER.md](../../implementation/adoption/MINIMUM_VIABLE_ADOPTER.md) | Body / staff / funding inventory | Not software |

None of these may be cited as if they were the duty.

---

## Owner-split register

Same surface, more than one layer describing it. Not a hole; later CS text should **point**, not restate.

| Surface | Split |
|---|---|
| Type O public baseline + qualified audit access | CS-2 types/posture; CJS-3.3 process; CJS-3.4 output-tier; CS-3 §7.2 class-record disclosure |
| Digital self-service (enroll / manage / exit) | CJS-3.17 shared floor; CI-8.3 institutional supervision |
| Continuity export / portability | CS-2 §1.2 collection-time; CJS-3.17 formats; CS-4.14 chokepoint export; Article XIX-A floor |
| Inspectable attributable action | CS-4 §10 logging contract; CI-4.6 seat named in “who authorized”; schema is process-support |
| Standing-record custody / contest | Ch.8 §3.7; CI-3.6 Charter field 11; CI-3.2 lane-map fallback; CI-4.6 contest seat |
| Lock-to-remedy / backlog publication | Ch.9 §4.4 floor; CI-27.2 institution; CF-11 forum metrics; CF-5.4 capacity-failure routing |
| Summaries + drill-down | CJS-3.8 joint floor; CS-6 systems profile; CI-8 pathway usability |
| Crisis / continuity communications | CS-5 §8 system channels; CF-12.6 forum-specific status |
| Charter ↔ Type O ↔ classification | CI-3.6 Charter; CS-2 §7 Type O mapped from Charter+class+behavior; CS-3 System Classification Record |
| Challenge entry | Article XII-B floor; CF intake; CS-7 invariant challenge/remediation |

---

## Gap register

**Taxonomy gaps (no defensible surface for a required act): none.** Every required row received Explicit or Inferred.

**Inferred rows (function required; home does not name the interface):**

| Capability | Suggested later move |
|---|---|
| Contest post-sale access / subscription cutoffs ([Article II-D](../../core_06_rights_part_a.md#article-ii-d-post-sale-access-and-subscription-integrity)) | Point at Article XII-B plus CJS-3.17 / CI-8.3 when the cutoff is digital self-service. Do not invent a second challenge home. |
| Accessibility accommodations in participation domains ([Article V-G](../../core_06_rights_part_b.md#article-v-g-accessibility)) | Parity on whatever channel the domain already uses (CF-11 / CJS-3.8). Not a separate product. |
| Unified “everything held about me” subject-access surface | Integrator convenience only. Pieces already exist (identity control, standing inspect-if-open, Article VIII-B). **Must not** defeat Chapter Eight silence default. |

**Other finding kinds (not missing duties):**

| Kind | Finding |
|---|---|
| **Surface without duty** | Continuity dashboard stub; steward-door pointer index; JSON schemas; system/model-card templates. Operators may build them. They are not required products. |
| **Owner split** | Table above. Later CS text points; it does not restate CF-15 or CJS-3.17. |
| **Product-shaped** | None in binding source. CS-5 already forbids locking a technical implementation. Chapter Eight §3.5 names “dashboards” only as optional tools with an anti-score rule. |
| **No analog fallback** | Digital self-service / charge-exit **when entry was digital**; CS-12.5 offline integrity proofs. Type O’s free-online test is mixed, not a blanket digital mandate. |
| **Schema-only** | No schema lacks a corpus owner. The three validating schemas instantiate CS-4 §10, the sentience-status record, and optional Chapter Eight snapshots. |
| **Discovery catalog** | Each Class A/B/C system must publish its own Type O floor. Source does **not** require a federated directory of all in-scope systems. Usability of a *known* system’s floor is Explicit; browsing all systems is nice-to-have, not a duty. |

---

## Later CS placement (landed 2026-09-10)

The inventory is **two clusters of similar size**, not one engineering family. **Do not mint CS-13.**

**In-scope system surfaces** now live in [`cs_05_a_user_facing_capabilities.md`](../../corpus_systems/cs_05_a_user_facing_capabilities.md) (**CS-5, Part A**): pointer catalog, analog vs digital channel class, and the silence-default / no-unified-subject-access negatives. Lifecycle engineering stays in [`cs_05_design_testing_verification_deployment.md`](../../corpus_systems/cs_05_design_testing_verification_deployment.md).

**Constitutional-operating surfaces** stay with Chapters Seven–Twelve, **CF**, and **CI**. Integrator routing is **CS-D12** on [CS-0](../../corpus_systems/cs_00_registry_and_reading_rules.md#domain-topic-owner-map-cs-d). This matrix remains process support; it cannot narrow.

That split is the software analog of the data-types result: no new type letter; assign on the home that already owns the kind.

---

## Method notes

1. Seeded from the 2026-08-31 Chapter Five artifact table and [CF-15.1](../../corpus_forum/cf_15_standard_records_forms_evidence_artifacts.md#cf-151-minimum-record-set), then asked whether each record has a **reachable surface**.
2. Walked Rights Floor user-reachable acts (Articles VII, VIII, XI, XII-B, XIV, XV, XVI, XVII, XIX, XX, XXIII-D); Chapters Seven–Twelve pipelines; CS-2–CS-12; CI-3, CI-4, CI-7, CI-8, CI-27; CF-3, CF-5, CF-11, CF-12, CF-15; CJS-3.3, CJS-3.8, CJS-3.17.
3. Added `implementation/` schemas, the continuity dashboard stub, system/model-card templates, steward doors, and the minimum-viable adopter page as **nice-to-have** only.
4. Grouped the twenty-one CF-15.1 templates as one capability. Did not list every Rights Floor as its own app.
5. Hydrated [Public Oversight Baseline Disclosure](../../core_05_band_oversight.md#public-oversight-baseline-disclosure) from source via `tools/corpus_lookup.py hydrate`. Other cites are file plus anchor on the owning home. If this audit and a source file disagree, the source wins.
6. Did not open `ai_corpus/indexes/id_resolver.json` for meaning.
7. Did not invent “must be digital.” analog_ok stays **yes** unless the source already requires a digital or machine-usable channel.

---

**Previous evidence twin:** [CS-2 data types coverage audit](../2026-08-31/cs2_data_types_coverage_audit.md)
