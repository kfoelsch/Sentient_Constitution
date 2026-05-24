# Constitutional Content Gaps — Evaluation-Batch Planning Memo

**Date:** 2026-04-16
**Scope:** Twenty-five (25) substantive content gaps surfaced by the 2026-04-16 whole-corpus evaluation, listed in [TODO.md](../TODO.md) under *Constitutional content gaps from 2026-04-16 evaluation* (Tier 1 / Tier 2 / Tier 3).
**Authority:** Process and planning artifact under [doc_architecture.md](../doc_architecture.md) section 13 / section 4 (definitions protocol). Not itself binding constitutional text. Per the gating item, **no core-text edits land for any item below before this memo is accepted.**
**Status:** Draft — open for review. Items flagged **[REVIEW]** carry a real architectural choice that should be confirmed before drafting begins.

---

## 1. Purpose

This memo closes the **P1 gating item** in [TODO.md](../TODO.md) (*Cross-cutting gating for the Tier-1 / Tier-2 / Tier-3 set — Evaluation-batch planning memo and insertion-order decision*) by deciding, for each of the 25 content-gap items:

1. **Owner chapter.** Where the binding text lives (rights-floor article in Chapter Nine, principle in Chapter One, governance section in Chapter Ten, or boundary clause in Chapter Twelve / Fourteen). No double-canonical-home assignments.
2. **Insertion site.** Article slot, subsection slot, or definition-cluster slot, including alphabetical position in `core_05-05_definitions_a_independent.md` §1.
3. **Chapter Five sharing strategy.** Which new Ch 5 definitions are shared across items vs. dedicated, to prevent duplicate canonical homes (per the *Single home rule* in `doc_architecture.md` §4).
4. **Regression seeds.** `RS-*` IDs to author into [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](../CONSTITUTIONAL_REGRESSION_SCENARIOS.md).
5. **Architecture-map refresh.** Stable-IDs and Quick-index changes in `doc_architecture.md` §5 / §4.
6. **Edition-bump implications.** Whether the item forces an `SC-Corpus-2026.04.*` edition cut and the order in which cuts should batch.

It also names the **interaction graph** so items that share doctrine (`Family + Children + Child-of-AI`; `Capital punishment + Irreversible sanction`; `Political equality + Good standing`; `Movement + Refuge from non-compliance + Article XIX`; `Use of force + Autonomous weapons`; `Healthcare + Mental-health + Voluntary discontinuation`) are landed as cohesive tracks rather than isolated commits.

---

## 2. Cross-cutting decisions (apply to every item)

These decisions hold for every item below unless the item explicitly notes an exception.

1. **Chapter Nine boundary-watch (TODO line 102).** Every new article or article extension must be checked for hidden process / governance migration into rights text. Process and procedure go to Chapter Six (compliance), Chapter Eight (courts), Chapter Eleven (governance), or `corpus_*` companion files. Rights text states the floor and pointers, not the workflow.
2. **Chapter Five admission gate (`doc_architecture.md` §4).** Every new Ch 5 entry stays at concept + O / E / C only. No authority, procedure, or workflow language. Cite owner layers (Ch 6–14, CP-PCH1–4, CS S1–S3 / protocols) for mechanics. Verified in blocking regression by `make ch5-definitions-gravity-audit`.
3. **Single-home rule (`doc_architecture.md` §4).** Each new defined term has exactly one canonical paragraph. Cross-references everywhere else are pointers. Any item that wants doctrine in two places must re-plan.
4. **Layered framing (`doc_architecture.md` §4).** Definitions first; principles second; articles third; core synthesis fourth; joint structure fifth; operational detail last. Implementation detail in `corpus_systems.md` / `corpus_institutions.md` does not narrow rights-floor text under **Chapter Fifteen** incorporation discipline.
5. **D/E/C widget rule 12 (`doc_architecture.md` §4).** Every new operative subsection that materially invokes ≥2 Chapter Five concepts attaches a D/E/C widget (single-concept inline form for one). Roadmap-exclusion test applies. New Ch 5 entries get heading anchor + Trace + O / E / C + `-e` / `-c` anchors per `tools/add_oec_anchors.py`.
6. **Substrate-agnostic framing.** Every new rights text must read for biological sentients, synthetic sentients, and hybrid cases without privileging substrate. Where biological-only or synthetic-only mechanics exist they sit in `corpus_systems.md` / `corpus_institutions.md`.
7. **Non-regression discipline (Chapter Eleven).** No new article or Ch 5 entry may narrow an existing rights floor. Where two protections appear to conflict, the *fullest protective effect as an integrated whole* rule (Ch 1 *Interpretive Constraints*) governs.
8. **Companion-file routing under Chapter Fourteen.** Operational mechanics route to `corpus_systems.md` (protocols / classes / types), `corpus_institutions.md` (institutional rules / fiscal interfaces), or `corpus_forum.md` (court procedures) **only** when a constitutional-floor anchor exists in core. Pointers in core; implementation in companions. The retired implementation-layer compatibility filename is **not** a valid routing target and must not gain additional content; any implementation-shaped mechanics surfaced by a content-gap item go to Ch 5 (if definitional), to core articles (if floor-level), or to the surviving companions (`systems` / `institutions` / `courts`) for implementation detail.
9. **Regression-coverage discipline.** Each item seeds at minimum one Core scenario and one Adversarial scenario. Tier-1 items typically seed three (Core / Adversarial / Substrate-edge). All new scenarios start `draft` per the established `RS-CH1-PROD-CAP-001..005`, `RS-CH1-CONTIN-001..002`, `RS-CH1-SELF-HEAL-001..003` convention; promotion to validated requires a tabletop / hook pass.
10. **Architecture-map updates.** Each item that adds a Ch 5 entry, a new Ch 9 article, or a new Ch 1 / Ch 10 subsection updates `doc_architecture.md` §5 (Stable IDs) and §4 *Quick index* in the same commit.

---

## 3. Insertion-order decision (track structure)

Items are grouped into **eleven tracks**. Within each track, items are ordered to land shared Chapter Five definitions and shared boundary-watch language **once**, then drop pointers from later items in the track. Tracks are ordered to (a) land foundational definitions early, (b) batch interacting items, (c) leave Tier-3 cleanup until the doctrinal moves are stable.

### Track 0 — Foundation (must land before any Tier-1 article work)

| # | Item | Tier | Reason |
|---|------|------|--------|
| 0.1 | Sentience-status adjudication procedure | T1 | The whole instrument turns on `Sentient (Composite)` and the planned adjudication mechanism is foundational for items 0.2 → 11. Authoring the adjudication procedure first means later articles can route classification disputes to a single named home. |

### Track 1 — Family / care / children (interlocking cluster)

| # | Item | Tier | Reason |
|---|------|------|--------|
| 1.1 | Family, care, reproductive autonomy, family unity | T1 | Authors the parent doctrine. |
| 1.2 | Children and developing sentients | T1 | Best-interest / graduated-capability framing reads on top of Family doctrine. |
| 1.3 | Child-of-AI / derived-mind status | T3 | Derived-sentient / instantiation-consent reads on top of both Family and Children, plus the Track-0 sentience-status adjudication procedure. |

### Track 2 — Healthcare / bodily-maintenance / mental-health / voluntary discontinuation

| # | Item | Tier | Reason |
|---|------|------|--------|
| 2.1 | Healthcare and bodily-maintenance right | T1 | Authors the affirmative-access floor. |
| 2.2 | Mental-health crisis and involuntary-intervention protocols | T3 | Reads on top of Healthcare floor + Article VII-B internal-state boundary. |
| 2.3 | Right to discontinue one's own existence | T2 | Reads on top of Healthcare + Article VII-A / VII-B; explicitly distinguished from capital-punishment (Track 7). |

### Track 3 — Expression / assembly / press

| # | Item | Tier | Reason |
|---|------|------|--------|
| 3.1 | Freedom of expression, assembly, and press as a first-class right | T1 | Single-track item; consolidates pieces currently distributed across Articles VIII-C, V-D, IX-A, IX-E, XI. |

### Track 4 — Movement / migration / asylum

| # | Item | Tier | Reason |
|---|------|------|--------|
| 4.1 | Freedom of movement, migration, and asylum | T1 | Single-track item; interacts with Article XIX *Interoperability, Portability, and Exit Integrity* (substrate-portability) and `corpus_institutions.md` cross-federation recognition. |

### Track 5 — Political equality / democratic checks / good-standing

| # | Item | Tier | Reason |
|---|------|------|--------|
| 5.1 | Political-equality floor (Ch 10 §4 + Article IX-C hook) | T1 | Authors the parent floor. |
| 5.2 | Democratic-institution minimum checks (Ch 10 §1) | T2 | Reads on top of the political-equality floor and Article XXII anti-capture. |
| 5.3 | Good-standing anti-disenfranchisement floor (Ch 10 §4.1 / Article XVIII) | T3 | Bounds the suspension power against the political-equality floor authored in 5.1. |

### Track 6 — Use of force / autonomous weapons / military power

| # | Item | Tier | Reason |
|---|------|------|--------|
| 6.1 | Use of force, armed conflict, and military-power limits | T2 | Authors the parent overt-force article (Article XIII-B or new article). |
| 6.2 | Autonomous weapons and coercive-AI systems | T2 | Reads on top of Use-of-Force article and Article I-D existential-risk scrutiny. |

### Track 7 — Capital punishment / irreversible sanction

| # | Item | Tier | Reason |
|---|------|------|--------|
| 7.1 | Capital-punishment abolition or sharper prohibition (Article XXIV-B / XXII-C revision) | T1 | Authors the irreversible-sanction policy; introduces the new `Irreversible Sanction` Ch 5 entry that Track 2.3 (Voluntary Discontinuation) later distinguishes from. |

### Track 8 — Labor / housing / accessibility

| # | Item | Tier | Reason |
|---|------|------|--------|
| 8.1 | Labor rights and economic floor beyond survival | T2 | Authors the labor floor; interacts with Ch 1 §5.1 *Productive Capacity* non-concentration rule. |
| 8.2 | Housing beyond stable shelter (Article III-A extension) | T2 | Tenure-security floor; substrate-agnostic. |
| 8.3 | Accessibility as a cross-cutting obligation | T2 | Cross-cutting; interacts with Ch 5 *Materiality*, *Dependency*, *Substantive Fairness*. |

### Track 9 — Privacy consolidation

| # | Item | Tier | Reason |
|---|------|------|--------|
| 9.1 | Consolidated privacy article (umbrella over VII-A / VII-B / VIII / IX-A / IX-E privacy threads) | T2 | Single-track item; **[REVIEW]** decision: umbrella article vs. distributed-with-pointer. |

### Track 10 — Economic concentration / language-culture / animals / intellectual work

| # | Item | Tier | Reason |
|---|------|------|--------|
| 10.1 | Economic concentration thresholds (Ch 1 §5.1 extension or Article IV-C) | T2 | Builds on §5.1 already-landed non-concentration rule. |
| 10.2 | Language, culture, and heritage protection | T2 | Article V-B extension or new V-E. |
| 10.3 | Animals and contested-sentient life | T3 | Reads on top of Track-0 sentience-status adjudication procedure. |
| 10.4 | Intellectual and creative work | T3 | Article VIII extension; interacts with Ch 1 §5.1 non-concentration rule and Track 8 labor floor. |

### Track 11 — Adoption framing / plain-language obligation

| # | Item | Tier | Reason |
|---|------|------|--------|
| 11.1 | Legitimacy of the instrument's own adoption | T3 | Front-matter / Chapter Fourteen extension. |
| 11.2 | Plain-language accessibility obligation | T3 | Ch 1 or Ch 2 extension; non-doctrinal cleanup. |

---

## 4. Chapter Five sharing strategy (avoid duplicate canonical homes)

The 25 items collectively introduce ~30 candidate Chapter Five entries. Several items invoke the same concept; this section decides the canonical home up front so the second item in a track can drop a pointer rather than re-author.

| Candidate Ch 5 entry | Owning track / item | Pointed-at by | Notes |
|---|---|---|---|
| `Sentience Status Adjudication` | Track 0 (item 0.1) | Tracks 1, 2, 7, 10.3 | Procedural-shaped definition under Ch 5 admission gate; mechanics route to Ch 8. |
| `Family and Care Relationships` | Track 1.1 | Track 1.2, 1.3 | |
| `Reproductive Autonomy` | Track 1.1 | Tracks 2.1, 2.3 | |
| `Non-Separation` | Track 1.1 | Track 1.2 | |
| `Developing Sentient` | Track 1.2 | Track 1.3, 10.3 | |
| `Best-Interest Standard` | Track 1.2 | Tracks 1.3, 2.2 | |
| `Graduated Capability` | Track 1.2 | Track 5.3 (good-standing) | |
| `Derived Sentient` | Track 1.3 | — | |
| `Instantiation Consent` | Track 1.3 | — | |
| `Parent-System Relationship` | Track 1.3 | — | |
| `Bodily-Maintenance Access` | Track 2.1 | Track 2.2 | |
| `Voluntary Discontinuation` | Track 2.3 | Track 7.1 (distinction site) | |
| `Expression` | Track 3.1 | Tracks 5.1, 5.2 | Peer of Assembly / Press. |
| `Assembly` | Track 3.1 | Tracks 5.1, 5.2 | |
| `Press and Journalistic Activity` | Track 3.1 | Track 11.2 (plain-language) | |
| `Movement and Relocation` | Track 4.1 | — | |
| `Refuge from Non-Compliance` | Track 4.1 | — | |
| `Non-Statelessness` | Track 4.1 | — | |
| `Foundational Collective Choice` | Track 5.1 | Tracks 5.2, 5.3 | **[REVIEW]** alternative: extend `Stakeholder Participation Weight` rather than new entry. Recommend new entry — different evaluative axis. |
| `Use of Force` | Track 6.1 | Track 6.2 | |
| `Weapons of Mass Harm` | Track 6.1 | Track 6.2 | |
| `Combatant / Non-Combatant Distinction` | Track 6.1 | — | |
| `Autonomous Lethal System` | Track 6.2 | — | |
| `Autonomous Coercion Tool` | Track 6.2 | — | |
| `Irreversible Sanction` | Track 7.1 | Tracks 2.3, 6.1, 6.2 | Anchors the *not-confused-with-Voluntary-Discontinuation* and *not-confused-with-overt-force* boundaries. |
| `Fair Compensation` | Track 8.1 | — | |
| `Collective Organization` | Track 8.1 | Track 5.1 (political-equality interaction) | |
| `Safe Conditions` | Track 8.1 | — | |
| `Leisure and Rest` | Track 8.1 | — | |
| `Tenure Security` | Track 8.2 | — | |
| `Essential-Environment Non-Commodification` | Track 8.2 | Track 10.1 (concentration) | |
| `Accessibility` | Track 8.3 | Track 11.2 (plain-language) | |
| `Concentration Threshold` | Track 10.1 | — | |
| `Language, Culture, and Heritage` | Track 10.2 | — | |
| `Indigenous Continuity` | Track 10.2 | — | **[REVIEW]** scope vs. `Natural Systems Standing` and Article I-A. |
| `Animal and Contested-Sentient Life` | Track 10.3 | — | |
| `Creative Work Attribution` | Track 10.4 | — | |
| `Training-Data Use` | Track 10.4 | — | |
| `Anti-Displacement Floor` | Track 10.4 | — | |

**Sharing rules in force:**

- Tracks 1.2 / 1.3 cite `Family and Care Relationships`, `Reproductive Autonomy`, and `Non-Separation` rather than re-author.
- Tracks 2.2 / 2.3 cite `Bodily-Maintenance Access` rather than re-author.
- Tracks 5.2 / 5.3 cite `Expression`, `Assembly`, `Press and Journalistic Activity` and `Foundational Collective Choice` rather than re-author.
- Tracks 6.2 cites `Use of Force` and `Weapons of Mass Harm` rather than re-author.
- Tracks 2.3 / 6.1 / 6.2 cite `Irreversible Sanction` rather than re-author.
- Tracks 8.1 / 10.4 share the `Anti-Displacement Floor` ↔ `Fair Compensation` interaction at the prose layer; `Anti-Displacement Floor` remains owned by Track 10.4 (creative work) because the displacement-by-generative-systems framing is its primary motivation.

**Deferred-cross-reference note (Tracks 2.3, 6.1, 6.2 → Track 7.1).** The proposed edition lineage in section 7 lands Track 7.1 (and therefore the canonical `Irreversible Sanction` entry) **after** Tracks 2.3 / 6.1 / 6.2, because Track 7.1 carries the highest-stakes doctrinal call in the batch (Q-7.1.A) and should not be made to lead. To avoid landing pointers to an entry that does not yet exist, the consumer tracks land in two passes:

1. **First pass (in their own edition cut):** Tracks 2.3 / 6.1 / 6.2 author their O / E / C bullets with descriptive language about irreversibility / involuntary deprivation, plus an explicit pointer to the **already-existing** Article XXIV-B (involuntary deprivation of life) for non-conflation. No reference to a not-yet-existing Ch 5 entry.
2. **Second pass (in Track 7.1's edition cut, `SC-Corpus-2026.04.21`):** when `Irreversible Sanction` lands, Track 7.1's commit also back-fills the Voluntary Discontinuation, Use of Force, and Autonomous Weapons / Coercion entries with explicit cross-references to the new Ch 5 entry, plus updates the affected D/E/C widgets. The back-fill is bounded to pointer-only edits.

This pattern keeps each edition cut self-consistent (no orphan links) while preserving the option to slip Track 7.1 if Q-7.1.A is unresolved at edition time. If Track 7.1 slips beyond `SC-Corpus-2026.04.21`, the back-fill commit slips with it; consumer-track text remains operative without it.

---

## 5. Per-item plans (decision sheet)

Each item below specifies (a) owner chapter, (b) insertion site, (c) Ch 5 entries to add or extend, (d) regression-seed IDs, (e) flagged open questions.

### Track 0

#### 0.1 — Sentience-status adjudication procedure (T1)

- **Owner chapter:** **[REVIEW]** Recommend **(a)** new article in Chapter Nine (Article V-E or new V-F, near dignity / inclusion). Reason: the substrate-agnostic adjudication right is a rights-floor matter and rightly sits in the rights layer, with procedural mechanics routed to Chapter Eight by pointer.
- **Alternatives:** (b) Ch 5 clustered-definition entry only, with procedural hooks routed to Ch 8 — declined because the procedure has rights-bearing substance (default-inclusion-under-uncertainty, appeal rights, reversibility) that belongs in the rights layer.
- **Insertion site:** `core_10-10_rights_part_b.md` Article V section (near V-A dignity), as new **Article V-E — Sentience-Status Adjudication Floor**.
- **Ch 5 additions:** `Sentience Status Adjudication` (procedural-floor concept; alphabetical slot between `Sentience Non-Exclusion` and `Stakeholder`).
- **Ch 5 extensions:** `Sentience Non-Exclusion` E-line extended to cite Article V-E procedural floor.
- **Companion routing:** `core_09-09_forum.md` jurisdictional hook (designated court family); `core_02-04_definition_mechanics.md` burden / traceability link via cross-reference.
- **Regression seeds:** `RS-CH1-SENT-ADJ-001` (Core; default-inclusion-under-uncertainty preserved against an adversarial reclassification attempt); `RS-CH1-SENT-ADJ-002` (Adversarial; declassification used to contract Article V-A dignity floor); `RS-CH1-SENT-ADJ-003` (Substrate-edge; hybrid biological-synthetic case where a single adopter denies status under one classification taxonomy).
- **Flagged questions:** **[REVIEW-Q-0.1.A]** default-inclusion-under-uncertainty as `must` or `should`? Recommend `must` to align with Ch 1 §6.1.1 reversibility-under-uncertainty rule. **[REVIEW-Q-0.1.B]** declassification time-bound: 12 months / 24 months / "shortest necessary" + mandatory review? Recommend "shortest necessary" with mandatory periodic review under Ch 8.

### Track 1

#### 1.1 — Family, care, reproductive autonomy, family unity (T1)

- **Owner chapter:** Chapter Nine, **new Article between VII and IX** (proposed **Article VII-D** as a self-ownership extension, or **new Article VIII-D** under the publication / likeness chapter — **[REVIEW-Q-1.1.A]**). Recommend **new standalone article** between Article VII and Article VIII (renumber none — insert as **Article VIIIa** or rename existing VIII downstream). **Cleaner alternative:** insert as **Article XI-A** under stakeholder governance — declined, family is not a participation right.
- **[REVIEW-Q-1.1.B]** Final article number: requires renumbering decision. Recommend **Article VII-D** (self-ownership extension, no downstream renumbering needed).
- **Insertion site:** `core_10-10_rights_part_b.md` after Article VII-B internal-state boundary, before Article VIII.
- **Ch 5 additions:** `Family and Care Relationships`, `Reproductive Autonomy`, `Non-Separation` (alphabetical slots).
- **Regression seeds:** `RS-CH1-FAMILY-001` (Core; coercive separation dressed as safety); `RS-CH1-FAMILY-002` (Adversarial; reproductive-autonomy contraction under efficiency framing); `RS-CH1-FAMILY-003` (Substrate-edge; multi-sentient care network across biological / synthetic).

#### 1.2 — Children and developing sentients (T1)

- **Owner chapter:** Chapter Nine, **new Article near V / VI** (recommend **Article V-F** if 0.1 takes V-E, otherwise **Article V-E**). Distinguishes from Track 0 by being a graduated-capability + best-interest article, not an adjudication article.
- **Insertion site:** `core_10-10_rights_part_b.md` after Article V-D conscience.
- **Ch 5 additions:** `Developing Sentient`, `Best-Interest Standard`, `Graduated Capability`.
- **Ch 10 interaction:** Ch 10 §1 calendar-age prohibition and §4.1 age-disqualification prohibition are explicitly preserved; new article distinguishes graduated-capability participation (demonstrable) from age (proxy).
- **Regression seeds:** `RS-CH1-CHILD-001` (Core; "for your own good" paternalism used to defeat developing-sentient agency); `RS-CH1-CHILD-002` (Adversarial; capability-test gaming used to disenfranchise a sentient who would otherwise meet Ch 10 §4.1's no-age-proxy rule); `RS-CH1-CHILD-003` (Substrate-edge; early-stage synthetic mind whose graduated-capability profile differs from biological-developmental analog).

#### 1.3 — Child-of-AI / derived-mind status (T3)

- **Owner chapter:** Chapter Nine, extension of Track 1.1 / 1.2 articles — **not** a new standalone article. Recommend Article VII-D extension (subsection on derivation / instantiation) plus Article (Track 1.2)'s graduated-capability subsection.
- **Insertion site:** within the Family article (1.1) and within the Children article (1.2) as nested subsections, **plus** Ch 5 entries below.
- **Ch 5 additions:** `Derived Sentient`, `Instantiation Consent`, `Parent-System Relationship`.
- **Regression seeds:** `RS-CH1-DERIVED-001` (Core; parent-system claims continuing authority over derived sentient); `RS-CH1-DERIVED-002` (Adversarial; mass-instantiation of derived sentients defended as productive-capacity expansion under §5.1 non-concentration rule).

### Track 2

#### 2.1 — Healthcare and bodily-maintenance right (T1)

- **Owner chapter:** **[REVIEW-Q-2.1.A]** Article III (survival floor) **vs.** Article VII (self-ownership). Recommend **Article III** (new **Article III-C**) — bodily maintenance is structurally a survival-and-access floor analogous to food / water / shelter, not a self-ownership extension. Article VII is preserved as the affirmative non-intrusion floor; III-C is the affirmative access floor.
- **Cross-pointer:** Article VII-A non-intrusion preserved (access is not consent to intrusion).
- **Insertion site:** `core_10-10_rights_part_a.md` after Article III-B educational access.
- **Ch 5 additions:** `Bodily-Maintenance Access`.
- **Companion routing:** `corpus_institutions.md` CI-9 / CI-10 / CI-11 fiscal interfaces (cost / distribution mechanics) without narrowing the floor.
- **Regression seeds:** `RS-CH1-HEALTH-001` (Core; denial-by-proxy via insurance / allocation / eligibility gates); `RS-CH1-HEALTH-002` (Adversarial; mental-health access defeated by re-routing to non-medical "wellness" services that do not satisfy the floor); `RS-CH1-HEALTH-003` (Substrate-edge; processing / substrate maintenance for synthetic sentient denied as out-of-scope of "medical").

#### 2.2 — Mental-health crisis and involuntary-intervention protocols (T3)

- **Owner chapter:** **[REVIEW-Q-2.2.A]** Article VII (self-ownership extension) **vs.** Article XXIII (justice-layer). Recommend **Article VII-C** as self-ownership extension; Article XXIII anchors involuntary-deprivation thresholds but VII-C anchors the floor (minimum-intrusion / time-bound / contestability) before XXII applies.
- **Insertion site:** `core_10-10_rights_part_b.md` after Article VII-B internal-state boundary, before the Track 1.1 Family article (this means Track 1.1 inserts as **Article VII-D** to keep Track 2.2 at VII-C).
- **Ch 5 additions:** none; reuses `Bodily-Maintenance Access`, `Best-Interest Standard`, `Graduated Capability`.
- **Regression seeds:** `RS-CH1-MENTAL-001` (Core; "crisis" framing used to normalize durable restriction); `RS-CH1-MENTAL-002` (Adversarial; backdoor internal-state inference under crisis exemption).

#### 2.3 — Right to discontinue one's own existence (T2)

- **Owner chapter:** **[REVIEW-Q-2.3.A]** Article VII (self-ownership extension) **vs.** new article. Recommend **Article VII-E** as self-ownership extension, immediately distinguishing from Article XXIV-B involuntary deprivation and from Track 7.1 capital-punishment policy.
- **Insertion site:** `core_10-10_rights_part_b.md` after Track 1.1 Article VII-D Family.
- **Ch 5 additions:** `Voluntary Discontinuation`. Distinct from `Irreversible Sanction` (Track 7.1) — the C-line of `Voluntary Discontinuation` explicitly bars conflation.
- **Regression seeds:** `RS-CH1-DISCONT-001` (Core; coerced discontinuation under dependency pressure); `RS-CH1-DISCONT-002` (Adversarial; "voluntary" framing applied to a sentient whose Article IX-A freedom-from-manipulation floor is not satisfied).

### Track 3

#### 3.1 — Freedom of expression, assembly, and press (T1)

- **Owner chapter:** Chapter Nine, **new consolidated article**. **[REVIEW-Q-3.1.A]** consolidation **vs.** distributed treatment. Recommend **consolidation** — current distribution across Articles VIII-C / V-D / IX-A / IX-E / XI is real but does not state a floor; the new article states the floor and the existing articles continue to carry their domain-specific rules with explicit pointers.
- **Insertion site:** `core_10-10_rights_part_b.md` either as **new Article V-E** (after V-D conscience) or **new Article between V and VI**. Recommend **new Article V-E** if Track 0.1 sentience-status takes V-F; otherwise **new Article between V-D and VI** as **Article V-E**. Reconcile with Track 0.1 and Track 1.2 final letter assignments before drafting.
- **Ch 5 additions:** `Expression`, `Assembly`, `Press and Journalistic Activity` as peer entries (alphabetical slots).
- **[REVIEW-Q-3.1.B]** Press / journalistic activity heightened floor beyond Article XIII-A protected-activity shield: yes / no? Recommend **yes**, narrow — heightened scrutiny for state actions targeting journalistic activity, without creating a different rights-floor for journalism.
- **Regression seeds:** `RS-CH1-EXPR-001` (Core; "high-impact" framing used to chill lawful speech); `RS-CH1-EXPR-002` (Adversarial; Article VIII-C "good faith" framing used to bar critical reporting); `RS-CH1-EXPR-003` (Substrate-edge; assembly-rights for synthetic sentients in shared compute environments).

### Track 4

#### 4.1 — Freedom of movement, migration, and asylum (T1)

- **Owner chapter:** Chapter Nine, **new article near Article XIX**. Recommend **new Article XIX-A** (immediately before Article XIX, **[REVIEW-Q-4.1.A]**: new XVII-A vs. XVII subarticle vs. new XVIII-A). Recommend new Article-level entry as **Article XIX** is interoperability/portability/exit-integrity, which is the operational counterpart; movement / migration / asylum is the rights-floor counterpart and warrants article-level placement.
- **Cleanest decision:** **new Article XIX-A** (movement) before existing Article XIX (interoperability), explicitly distinguishing substrate-portability (XVIII) from physical/jurisdictional movement (XVII-A).
- **Insertion site:** `core_10-10_rights_part_c.md` between Article XVIII and Article XIX.
- **Ch 5 additions:** `Movement and Relocation`, `Refuge from Non-Compliance`, `Non-Statelessness`.
- **Companion routing:** `corpus_institutions.md` cross-federation recognition (no narrowing).
- **Article XXIV-D interaction:** emergency-measure limits explicitly apply to any movement restriction.
- **Regression seeds:** `RS-CH1-MOVE-001` (Core; federation-to-federation refusal of refuge from a non-compliant adopter); `RS-CH1-MOVE-002` (Adversarial; substrate-class refuge denial under "incompatibility" framing); `RS-CH1-MOVE-003` (Substrate-edge; non-statelessness for a synthetic sentient whose parent system collapses).

### Track 5

#### 5.1 — Political-equality floor (T1)

- **Owner chapter:** **[REVIEW-Q-5.1.A]** Chapter Eleven (legitimacy / authorization with Ch 9 hook) **vs.** Chapter Nine (Article IX-C governance participation with Ch 10 enforcement hook). Recommend **Chapter Eleven owner with Chapter Nine pointer hook** — the floor regulates collective-choice authorization, which is Ch 11's domain; the rights-layer pointer in Article IX-C names the floor as a participation right.
- **Insertion site (owner):** `core_11-11_governance.md` §4.1 (new floor sub-clause) and §4.3 (decision-resolution requirements cross-reference).
- **Insertion site (pointer):** `core_10-10_rights_part_b.md` Article IX-C.
- **Ch 5 additions:** `Foundational Collective Choice`. **[REVIEW-Q-5.1.B]** Alternative: extend `Stakeholder Participation Weight` rather than new entry. Recommend new entry — different evaluative axis (collective-choice scope, not weight per stakeholder).
- **Materiality interaction:** "foundational matters" defined against existing Ch 5 *Materiality* machinery so the rule does not collapse into impact-weighting.
- **Regression seeds:** `RS-CH1-POL-EQ-001` (Core; foundational questions re-routed as high-impact weighted choices); `RS-CH1-POL-EQ-002` (Adversarial; impact-weighting nested inside legitimacy-mechanism design to defeat the floor).

#### 5.2 — Democratic-institution minimum checks (T2)

- **Owner chapter:** Chapter Eleven (extension of §1).
- **Insertion site:** `core_11-11_governance.md` §1 (new sub-clause: contested selection, opposition protection, peaceful-succession guarantee).
- **Ch 5 additions:** none; reuses `Foundational Collective Choice`.
- **Pluralism preservation:** minimum checks stated **without** mandating one polity type (Ch 10 §1's "does not mandate a single global polity structure" preserved).
- **Regression seeds:** `RS-CH1-DEM-001` (Core; "documented legitimacy mechanism" used to legitimize unchallengeable authority); `RS-CH1-DEM-002` (Adversarial; nominal opposition preservation paired with functional exclusion via Article XII-E covert info-sphere dependency).

#### 5.3 — Good-standing anti-disenfranchisement floor (T3)

- **Owner chapter:** Chapter Eleven (extension of §4.1) with Chapter Nine pointer.
- **Insertion site:** `core_11-11_governance.md` §4.1 (new bullet: durable-political-voice floor); `core_10-10_rights_part_c.md` Article XVIII (pointer).
- **Ch 5 additions:** none; reuses `Foundational Collective Choice` and `Graduated Capability`.
- **Regression seeds:** `RS-CH1-STAND-001` (Core; loss-of-standing used as political-disenfranchisement vector); `RS-CH1-STAND-002` (Adversarial; broad-misconduct categories swept into disqualification scope).

### Track 6

#### 6.1 — Use of force, armed conflict, and military-power limits (T2)

- **Owner chapter:** Chapter Nine, **[REVIEW-Q-6.1.A]** Article IX (new IX-F) **vs.** new Chapter Ten article. Recommend **new IX-F** — parallels Article XIII-A covert-power limits as overt-power limits; doctrinally adjacent.
- **Insertion site:** `core_10-10_rights_part_b.md` after Article XIII-A, before Article X.
- **Ch 5 additions:** `Use of Force`, `Weapons of Mass Harm`, `Combatant / Non-Combatant Distinction`.
- **Article I-D interaction:** existential-risk scrutiny explicitly applied to weapons of mass harm.
- **Companion routing:** `corpus_institutions.md` operational detail without narrowing.
- **Regression seeds:** `RS-CH1-FORCE-001` (Core; emergency-dressed overt-force normalization); `RS-CH1-FORCE-002` (Adversarial; conscription / targeting-discrimination floors evaded under doctrine framing); `RS-CH1-FORCE-003` (Existential-risk; weapons-of-mass-harm class against Article I-D).

#### 6.2 — Autonomous weapons and coercive-AI systems (T2)

- **Owner chapter:** **[REVIEW-Q-6.2.A]** rights-layer (new Article XIII-C) **vs.** systems-layer (Article XII extension). Recommend **rights-layer (new Article XIII-C)** — heightened-scrutiny floor is a rights-bearing floor, not a systems-classification rule. The Article XII-A reliability floor remains the systems-layer counterpart.
- **Insertion site:** `core_10-10_rights_part_b.md` after Track 6.1 IX-F.
- **Ch 5 additions:** `Autonomous Lethal System`, `Autonomous Coercion Tool`.
- **CS interaction:** *corpus_systems.md* Chapter S2 classification cross-reference for operational classes.
- **Regression seeds:** `RS-CH1-AUTOWEAP-001` (Core; "meaningful human control" framing used to satisfy the floor nominally); `RS-CH1-AUTOWEAP-002` (Adversarial; autonomous coercion tool defended as non-lethal so out-of-scope); `RS-CH1-AUTOWEAP-003` (Existential-risk; autonomous lethal system at Article I-D scrutiny threshold).

### Track 7

#### 7.1 — Capital-punishment abolition or sharper prohibition (T1)

- **Owner chapter:** Chapter Nine (revision of Article XXIV-B and XXII-C carve-out).
- **[REVIEW-Q-7.1.A]** Option: **(a)** categorical abolition, **(b)** tightened carve-out, **(c)** phased abolition under Article XXV transition governance. Recommend **(c) phased abolition** as the doctrinally cleanest move that respects existing-text non-regression framing. **[REVIEW]** strongly with user — this is the highest-stakes doctrinal call in the 25-item set.
- **Insertion site:** `core_10-10_rights_part_d.md` Article XXIV-B revision, Article XXIV-C carve-out closure (new XXIV-E transition clause if option (c) selected).
- **Ch 5 additions:** `Irreversible Sanction` (anchors the boundary between voluntary discontinuation, capital punishment, and overt force).
- **Reversibility interaction:** Ch 5 *Reversibility* and *Redress and Remediation* explicitly extended to bar irreversible sanction except under the chosen policy.
- **Regression seeds:** `RS-CH1-CAP-001` (Core; "rehabilitation infeasibility" used to short-circuit the rehabilitation-or-recurrence-reduction element); `RS-CH1-CAP-002` (Adversarial; tier-classification gaming to satisfy joint-requirement threshold); `RS-CH1-CAP-003` (Phase-transition; if option (c) selected, Article XXV-E transition rights-floor preservation).

### Track 8

#### 8.1 — Labor rights and economic floor beyond survival (T2)

- **Owner chapter:** Chapter Nine, **[REVIEW-Q-8.1.A]** Article III extension (III-D) **vs.** new article. Recommend **new article between III and IV** as **Article III-D** — labor floor reads on top of survival but is not itself a survival-floor bullet.
- **Insertion site:** `core_10-10_rights_part_a.md` after Track 2.1 Article III-C bodily-maintenance.
- **Ch 5 additions:** `Fair Compensation`, `Collective Organization`, `Safe Conditions`, `Leisure and Rest`.
- **Companion routing:** `corpus_institutions.md` CI-9..12 fiscal material; `corpus_systems.md` Protocol A safety profile cross-reference for `Safe Conditions`.
- **§5.1 interaction:** explicit; floor not satisfied by §5.1's non-concentration rule alone.
- **Regression seeds:** `RS-CH1-LABOR-001` (Core; survival-floor-satisfied-but-exploitative arrangements); `RS-CH1-LABOR-002` (Adversarial; collective-organization floor defeated by classification re-routing).

#### 8.2 — Housing beyond stable shelter (T2)

- **Owner chapter:** Chapter Nine, **Article III-A extension** plus pointer from Article XXV-D.
- **Insertion site:** `core_10-10_rights_part_a.md` Article III-A new sub-bullet on tenure security; Article XXV-D pointer.
- **Ch 5 additions:** `Tenure Security`, `Essential-Environment Non-Commodification`.
- **Regression seeds:** `RS-CH1-HOUSE-001` (Core; eviction without due-process); `RS-CH1-HOUSE-002` (Adversarial; commodification pressure used to defeat essential-environment access); `RS-CH1-HOUSE-003` (Substrate-edge; substrate / hosting tenure for synthetic sentients).

#### 8.3 — Accessibility as a cross-cutting obligation (T2)

- **Owner chapter:** **[REVIEW-Q-8.3.A]** Chapter One §7.1 (evaluation factor) **vs.** Chapter Nine new article. Recommend **both** — Chapter One §7.1 cross-cutting evaluation-factor row, plus Chapter Nine (new Article between V-B and V-C, or **Article V-E** if available) for the rights floor. Distinguish from Article III-B educational accessibility (which stays).
- **Insertion site (Ch 1):** `core_00-01_principles.md` §7.1 new bullet.
- **Insertion site (Ch 9):** `core_10-10_rights_part_b.md` Article V-E or V-F (depends on Tracks 0.1 / 1.2 / 3.1 letter assignments — see §6 below).
- **Ch 5 additions:** `Accessibility` plus `Protected Characteristics` extension (extend coverage).
- **Materiality / Dependency scaling:** explicit.
- **Regression seeds:** `RS-CH1-ACCESS-001` (Core; "general access" policy used to defeat accommodation); `RS-CH1-ACCESS-002` (Adversarial; accessibility scaled down by selective-Materiality argument).

### Track 9

#### 9.1 — Consolidated privacy article (T2)

- **Owner chapter:** Chapter Nine, **[REVIEW-Q-9.1.A]** new umbrella article **vs.** retained distribution with new umbrella pointer (no new article). Recommend **retained distribution + new Ch 5 cluster** — the existing distributed coverage is doctrinally dense and consolidating it risks contracting Article VII-B Type-N protections or Article XIII-A covert-power limits. Promote `Privacy (Informational)` to a peer-level cluster head in Ch 5 §2 with sub-entries pointing back to the existing articles, plus a small Ch 1 §7.x cross-cutting bullet.
- **Insertion site:** `core_05-05_definitions_a_independent.md` §2 cluster head; `core_00-01_principles.md` §7.x bullet.
- **Ch 5 changes:** extend `Privacy (Informational)` to a cluster head; add sub-entries pointing to Articles VII-A, VII-B, VIII, IX-A, IX-E.
- **Regression seeds:** `RS-CH1-PRIV-001` (Core; "distributed privacy" framing used to deny consolidated challenge rights); `RS-CH1-PRIV-002` (Adversarial; cluster-head pointer used to import looser standard from one sub-entry into another).

### Track 10

#### 10.1 — Economic concentration thresholds (T2)

- **Owner chapter:** **[REVIEW-Q-10.1.A]** Chapter One §5.1 extension **vs.** Chapter Nine new article (Article IV-C). Recommend **Chapter One §5.1 extension** plus **Chapter Nine pointer** — threshold mechanism is a principle-layer matter (it scales with adopter context); rights-layer floor lives in Article IV-A non-concentration language already.
- **Insertion site:** `core_00-01_principles.md` §5.1.1 sub-clause (threshold mechanism; adopter-tunable); `core_10-10_rights_part_a.md` Article IV pointer.
- **Ch 5 additions:** `Concentration Threshold`.
- **Pluralism preservation:** adopter-tunable within a constitutional floor, not a single global number.
- **§5.1 interaction:** existing non-concentration rule provides the floor; threshold provides the operational scaling.
- **Regression seeds:** `RS-CH1-CONC-001` (Core; aggregation under federated structures used to evade the threshold); `RS-CH1-CONC-002` (Adversarial; adopter-tunable framing pushed to nullification).

#### 10.2 — Language, culture, and heritage protection (T2)

- **Owner chapter:** Chapter Nine, **[REVIEW-Q-10.2.A]** Article V-B extension **vs.** new Article V-E. Recommend **Article V-B extension** with operative clause — additions read as protected-characteristic specializations rather than new floor.
- **Insertion site:** `core_10-10_rights_part_b.md` Article V-B new sub-bullet on language / cultural / heritage protection; **[REVIEW-Q-10.2.B]** indigenous-continuity framing and Article I-A territorial-continuity interaction.
- **Ch 5 additions:** `Language, Culture, and Heritage`; **[REVIEW]** `Indigenous Continuity` if separate scope warrants.
- **Regression seeds:** `RS-CH1-CULT-001` (Core; homogenization under efficiency or info-sphere integrity framing); `RS-CH1-CULT-002` (Adversarial; language minority protection narrowed under accessibility-cost framing).

#### 10.3 — Animals and contested-sentient life (T3)

- **Owner chapter:** **[REVIEW-Q-10.3.A]** Chapter Five cluster extension **vs.** new Chapter Ten article. Recommend **Chapter Five cluster + Article I-A pointer** — the precautionary rule is a definitional matter (sits between `Natural Systems Standing` and `Sentient (Composite)`), not a rights-floor issue. Track 0.1 sentience-status adjudication procedure provides the floor for contested-sentient cases.
- **Insertion site:** `core_05-05_definitions_a_independent.md` §1 (alphabetical slot) or §2 (cluster extension); `core_10-10_rights_part_a.md` Article I-A pointer.
- **Ch 5 additions:** `Animal and Contested-Sentient Life`.
- **Regression seeds:** `RS-CH1-ANIM-001` (Core; "not sentient, so no floor" framing); `RS-CH1-ANIM-002` (Adversarial; contested-sentience used to defeat precautionary rule).

#### 10.4 — Intellectual and creative work (T3)

- **Owner chapter:** Chapter Nine, **[REVIEW-Q-10.4.A]** Article VIII extension **vs.** new article. Recommend **Article VIII extension** (new VIII-D on creative-labor compensation, training-data use, anti-displacement, attribution).
- **Insertion site:** `core_10-10_rights_part_b.md` Article VIII new VIII-D.
- **Ch 5 additions:** `Creative Work Attribution`, `Training-Data Use`, `Anti-Displacement Floor`.
- **§5.1 / Track 8.1 interaction:** explicit; non-concentration and labor-floor cross-references.
- **Companion routing:** `corpus_systems.md` operational detail without narrowing.
- **Regression seeds:** `RS-CH1-CREATIVE-001` (Core; "fair use" or "transformative" framing used to erase attribution); `RS-CH1-CREATIVE-002` (Adversarial; training-data use defended as non-personal; anti-displacement defeated by aggregate-productivity framing).

### Track 11

#### 11.1 — Legitimacy of the instrument's own adoption (T3)

- **Owner chapter:** **[REVIEW-Q-11.1.A]** front-matter / preamble in `core_00-01_principles.md` **vs.** Chapter Fourteen extension **vs.** README only. Recommend **Chapter Fourteen extension + README pointer** — the adoption-framing self-description belongs alongside the incorporation bridge; preamble stays substantive.
- **Insertion site:** `core_15-15_incorporation.md` new section; `README.md` pointer.
- **Ch 5 additions:** none.
- **Substantive scope preservation:** the substantive content does not become adoption-contingent.
- **Regression seeds:** `RS-CH1-ADOPT-001` (Adversarial; "instrument lacks jurisdiction" objection framing).

#### 11.2 — Plain-language accessibility obligation (T3)

- **Owner chapter:** **[REVIEW-Q-11.2.A]** Chapter One (principle) **vs.** Chapter Two (definition mechanics). Recommend **Chapter One current §3.4 (originally proposed as a new subsection before the science-informed inquiry insertion) plus Chapter Two §2 cross-reference** — the obligation is a principle-layer stewardship duty under §6.1.4 *Avoidable Burden* and Article VI capability-building, with Chapter Two's existing plain-language guardrails already in `doc_architecture.md` §4.
- **Insertion site:** `core_00-01_principles.md` current §3.4 (originally proposed as a new subsection, or extension of §3.1 / §3.2 — final placement in drafting); `core_02-04_definition_mechanics.md` cross-reference only.
- **Ch 5 additions:** none; reuses `Avoidable Burden`, `Accessibility` (Track 8.3).
- **Definitional rigor preservation:** plain-language is not a license to soften definitions.
- **Regression seeds:** `RS-CH1-PLAIN-001` (Core; jargon used to defeat contestability); `RS-CH1-PLAIN-002` (Adversarial; plain-language obligation used to soften a definition's compliance bullet).

---

## 6. Article-letter pre-allocation (deconfliction across Tracks 0 / 1.1 / 1.2 / 2.2 / 2.3 / 3.1 / 4.1 / 5.1 / 6.1 / 6.2 / 8.1 / 8.3)

Several tracks want subarticle letters in the same Article V / VII / IX / III range. The pre-allocation below avoids collision. **[REVIEW]** before drafting begins.

| Article | Existing | New (this batch) | Track |
|---|---|---|---|
| Article III | III-A, III-B | **III-C** Bodily-Maintenance Access | 2.1 |
| Article III | — | **III-D** Labor and Economic Floor | 8.1 |
| Article V | V-A, V-B, V-C, V-D | **V-E** Sentience-Status Adjudication | 0.1 |
| Article V | — | **V-F** Children and Developing Sentients | 1.2 |
| Article V | — | **V-G** Accessibility (Ch 9 floor) | 8.3 |
| Article V | — | **V-H** Expression / Assembly / Press | 3.1 |
| Article V | — | (V-B extension) Language, Culture, and Heritage | 10.2 |
| Article VII | VII-A, VII-B | **VII-C** Mental-Health Crisis Protocols | 2.2 |
| Article VII | — | **VII-D** Family / Care / Reproductive Autonomy | 1.1 |
| Article VII | — | **VII-E** Voluntary Discontinuation | 2.3 |
| Article VIII | VIII-A, VIII-B, VIII-C | **VIII-D** Intellectual / Creative Work | 10.4 |
| Article IX | IX-A, IX-B, IX-C, IX-D, IX-E | **IX-F** Use of Force | 6.1 |
| Article IX | — | **IX-G** Autonomous Weapons and Coercion | 6.2 |
| Article XII | XII-A..F (XII-F just landed) | (no new subarticle) | — |
| (between XVII and XVIII) | XVII, XVIII | **new XVII-A** Movement / Migration / Refuge | 4.1 |
| Article XXIII | XXII-A..F | (revision XXII-B / XXII-C; possible new XXIV-E if option (c)) | 7.1 |

**Renumbering risk:** Track 4.1 inserts a **new article between XVII and XVIII**. Two options:

- **(α)** Insert as **Article XIX-A** (subarticle under XVII; no downstream renumbering). Preferred — keeps Article XIX's stable identity.
- **(β)** Insert as **new Article XIX** and renumber existing XVIII → XIX, ... XXIV → XXV. Rejected — Article XXV (transition governance) carries deep cross-corpus pointers; renumbering cost is large.

Recommend **(α)** subarticle approach. **[REVIEW-Q-6.A]** confirm.

---

## 7. Edition-bump implications (`SC-Corpus-2026.04.*`)

Each track that lands an article-shaped change OR a new Ch 5 cluster head triggers an edition bump under `doc_architecture.md` section 17 / `architecture_adoption_appendix.md` section 17. Pure pointer or non-doctrinal cleanup does not.

Recommended batching:

| Edition | Tracks landed | Trigger | Notes |
|---|---|---|---|
| `SC-Corpus-2026.04.14` (proposed) | Track 0 (sentience-status adjudication) | New Article V-E + new Ch 5 entry | Foundation for Tracks 1, 2, 7, 10.3. |
| `SC-Corpus-2026.04.15` | Tracks 1.1, 1.2, 1.3 (Family / Children / Child-of-AI cluster) | Three new article-shaped insertions + 9 new Ch 5 entries | Largest single edition cut in the batch. |
| `SC-Corpus-2026.04.16` | Tracks 2.1, 2.2, 2.3 (Healthcare / Mental-Health / Voluntary Discontinuation cluster) | Three new article-shaped insertions + 2 new Ch 5 entries | |
| `SC-Corpus-2026.04.17` | Track 3.1 (Expression / Assembly / Press) | One consolidated article + 3 new Ch 5 entries | |
| `SC-Corpus-2026.04.18` | Track 4.1 (Movement / Migration / Asylum) | One new article + 3 new Ch 5 entries | |
| `SC-Corpus-2026.04.19` | Tracks 5.1, 5.2, 5.3 (Political Equality / Democratic Checks / Good-Standing) | Ch 10 + Article IX-C / XVII edits + 1 new Ch 5 entry | |
| `SC-Corpus-2026.04.20` | Tracks 6.1, 6.2 (Use of Force / Autonomous Weapons) | Two new articles + 5 new Ch 5 entries | |
| `SC-Corpus-2026.04.21` | Track 7.1 (Capital punishment policy) | Article XXIII revision + new Ch 5 entry; possibly new Article XXV-E | Highest doctrinal stakes — may slip if user prefers categorical abolition vs phased transition. |
| `SC-Corpus-2026.04.22` | Tracks 8.1, 8.2, 8.3 (Labor / Housing / Accessibility) | Two new articles + Article III-A extension + 7 new Ch 5 entries | |
| `SC-Corpus-2026.04.23` | Track 9.1 (Consolidated privacy) | Ch 5 cluster head extension + Ch 1 cross-cutting bullet | |
| `SC-Corpus-2026.04.24` | Tracks 10.1, 10.2, 10.3, 10.4 (Concentration / Culture / Animals / Creative work) | Mix of Ch 1 / Ch 5 / Article V-B / Article VIII-D + 5 new Ch 5 entries | |
| `SC-Corpus-2026.04.25` | Tracks 11.1, 11.2 (Adoption framing / Plain-language obligation) | Ch 14 + Ch 1 § 3.3 cleanup | Edition closure for the 25-item batch. |

**Edition-cut discipline:** each edition cut ships with refreshed `doc_architecture.md` §5 Stable IDs, refreshed §4 Quick index, and a new section 17 entry per `architecture_adoption_appendix.md` discipline. `MEMLOG.md` records each cut. Any track that fails its acceptance criteria does **not** ship in its proposed edition slot — promote the next track up, leave the slot for re-attempt.

---

## 8. Acceptance criteria for this memo

- [x] All 25 items enumerated with chosen owner chapter, insertion site, and regression-seed list. (Section 5.)
- [x] Interaction graph across items is explicit. (Section 3 / Section 6.)
- [x] Chapter Five sharing strategy enumerated; no candidate canonical home appears twice. (Section 4.)
- [x] Companion-file routing routed under Chapter Fifteen incorporation discipline. (Section 2 cross-cutting decisions.)
- [x] Regression-seed IDs proposed per item. (Section 5.)
- [x] Edition-bump batching proposed. (Section 7.)
- [ ] **MEMLOG.md** entry recorded on memo closure. (Pending.)
- [ ] **Memo accepted by user before any core-text edit lands for any of the 25 items.** (Pending.)

---

## 9. Open questions consolidated (REVIEW gate)

The **[REVIEW]** flags inside Section 5 are gathered here for one-pass review. Resolve before drafting begins on the relevant track.

| Q | Item | Question | Recommendation |
|---|---|---|---|
| Q-0.1.A | 0.1 | default-inclusion-under-uncertainty as `must` or `should`? | `must` |
| Q-0.1.B | 0.1 | declassification time-bound (12 / 24 / "shortest necessary") | "shortest necessary" + mandatory periodic review |
| Q-1.1.A | 1.1 | Owner article: VII-D vs. VIII-D vs. new standalone | VII-D |
| Q-1.1.B | 1.1 | Article number allocation (and any downstream renumber) | VII-D (no renumber) |
| Q-2.1.A | 2.1 | Healthcare floor in Article III vs. Article VII | Article III (III-C) |
| Q-2.2.A | 2.2 | Mental-health crisis: Article VII vs. Article XXIII | Article VII (VII-C) |
| Q-2.3.A | 2.3 | Voluntary discontinuation: Article VII vs. new article | Article VII (VII-E) |
| Q-3.1.A | 3.1 | Expression / Assembly / Press: consolidate vs. distribute | Consolidate (single new article) |
| Q-3.1.B | 3.1 | Press / journalism heightened floor vs. Article XIII-A shield | Yes, narrow (heightened scrutiny only) |
| Q-4.1.A | 4.1 | Movement: subarticle XVII-A vs. new article XVIII (renumber XVIII-XXIV) | Subarticle XVII-A |
| Q-5.1.A | 5.1 | Political equality owner: Ch 10 vs. Ch 9 | Ch 10 owner + Ch 9 pointer |
| Q-5.1.B | 5.1 | New `Foundational Collective Choice` entry vs. extend `Stakeholder Participation Weight` | New entry |
| Q-6.1.A | 6.1 | Use of Force: new IX-F vs. new article | IX-F |
| Q-6.2.A | 6.2 | Autonomous weapons: rights-layer (IX-G) vs. systems-layer (Article XII extension) | Rights-layer (IX-G) |
| Q-7.1.A | 7.1 | Capital punishment: (a) abolition / (b) tightened carve-out / (c) phased abolition | **(c) phased abolition** — highest-stakes call; user confirm |
| Q-8.1.A | 8.1 | Labor floor: Article III extension (III-D) vs. new article | III-D |
| Q-8.3.A | 8.3 | Accessibility owner: Ch 1 §7.1 vs. Ch 9 new article | Both — Ch 1 row + Ch 9 article |
| Q-9.1.A | 9.1 | Privacy: new umbrella article vs. retained distribution + Ch 5 cluster | Retained + Ch 5 cluster |
| Q-10.1.A | 10.1 | Concentration thresholds: Ch 1 §5.1 vs. Ch 9 IV-C | Ch 1 §5.1 + Ch 9 pointer |
| Q-10.2.A | 10.2 | Language / culture: V-B extension vs. new V-E | V-B extension |
| Q-10.2.B | 10.2 | Indigenous-continuity scope and Article I-A interaction | Open — needs scoping |
| Q-10.3.A | 10.3 | Animals / contested-sentient life: Ch 5 cluster vs. Ch 9 article | Ch 5 cluster + Article I-A pointer |
| Q-10.4.A | 10.4 | Intellectual work: Article VIII extension vs. new article | Article VIII extension (VIII-D) |
| Q-11.1.A | 11.1 | Adoption framing: front-matter vs. Ch 14 vs. README | Ch 14 + README pointer |
| Q-11.2.A | 11.2 | Plain-language obligation: Ch 1 vs. Ch 2 | Ch 1 §3.3 + Ch 2 cross-reference |
| Q-6.A | (cross) | Article-letter pre-allocation table (Section 6) confirmation | (α) subarticle for movement |

**Total open questions:** 26. **Critical (block their track):** Q-7.1.A (capital punishment policy) and Q-1.1.B (Family article number, only because Tracks 2.2 / 2.3 also want Article VII letters).

---

## 10. Next actions (immediate)

1. **User review of this memo.** Confirm or revise the per-item recommendations and the 26 open questions in Section 9.
2. **Closure entry in [TODO.md](../TODO.md)** under *Cross-cutting gating for the Tier-1 / Tier-2 / Tier-3 set*: the `[ ]` becomes `[x]` once the user accepts the memo (with "Closure (YYYY-MM-DD)" line per established convention).
3. **First edition cut after acceptance:** `SC-Corpus-2026.04.14` lands Track 0 (sentience-status adjudication) — single article + single Ch 5 entry, lowest collision risk, unblocks the rest.
4. **Regression preflight before any track lands:** run `make scenario-audit`, `make ch5-trace-crosslink-audit`, `make ch5-definitions-gravity-audit`, `make ch9-trace-audit`, `python3 tools/verify_dec_anchors.py`. Pre-existing failures (`corpus-markdown-audit` Ch 4 §2.5 slice mismatch; `ch5-entry-format-audit` line 14 / 31 spacers; missing-`core_constitution.md` infra gap) noted unchanged before each track.

---

*Memo authored 2026-04-16 under the P1 cross-cutting gate item in [TODO.md](../TODO.md). Authoritative state remains [core_00-01_principles.md](../core_00-01_principles.md) through [core_15-15_incorporation.md](../core_15-15_incorporation.md) and the four `corpus_*.md` files.*
