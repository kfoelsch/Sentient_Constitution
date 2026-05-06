# Track 7.1 Policy-Selection Memo — Capital Punishment and *Irreversible Sanction*

**Date:** 2026-04-17
**Scope:** Q-7.1.A from [DEC_CONTENT_GAPS_PLAN_2026-04-16.md](DEC_CONTENT_GAPS_PLAN_2026-04-16.md) §9 (capital-punishment policy). Track 7.1 was deliberately slipped from the 2026-04-16 edition batch per user direction; this memo executes the "dedicated future pass" called for in [TODO.md](../TODO.md) *Deferred — Track 7.1 (capital-punishment policy)*.
**Authority:** Process and planning artifact under [doc_architecture.md](../doc_architecture.md) §13 / §4 (definitions protocol). Not itself binding constitutional text. Per the standing plan-first gate, **no core-text edits land for Track 7.1 before this memo is accepted.**
**Status:** Draft — recommending **Option (a): Categorical Abolition** as the doctrinally consistent move. Open for review; the companion implementation pass is ready to execute on acceptance.

---

## 1. Purpose

This memo closes the single open REVIEW-gate question that caused Track 7.1 to slip from the 2026-04-16 edition batch: **Q-7.1.A** (capital-punishment policy). It does three things:

1. **Policy selection.** Chooses between the three memo §5.7.1 options ((a) categorical abolition, (b) tightened carve-out, (c) phased abolition) with doctrinal reasoning tied to the instrument's own discipline.
2. **Implementation scope.** Specifies exactly what changes land in Chapter Nine and Chapter Five when the policy is implemented, and how the bounded pointer-only back-fill into Tracks 2.3 / 6.1 / 6.2 executes.
3. **Acceptance artifacts.** Enumerates the regression seeds, architecture-map refresh, and edition-cut bookkeeping to close the Track 7.1 acceptance checks in full.

The Indigenous-continuity scoping pass (Q-10.2.B) is a separate memo ([DEC_INDIGENOUS_CONTINUITY_SCOPE_2026-04-17.md](DEC_INDIGENOUS_CONTINUITY_SCOPE_2026-04-17.md)).

---

## 2. Policy options recap (from memo §5.7.1 / §9)

The three options considered in the 2026-04-16 planning memo, with the memo's own default recommendation noted:

- **(a) Categorical abolition.** Deprivation of life as a sanction by state, operator, or comparable actor is non-compliant under the Constitution without exception. The instrument carries no capital-punishment carve-out. Existing Article XXIV-B (*Capital punishment*) and Article XXIV-C (*Carve-out (capital punishment)*) bullets are replaced with an affirmative abolition rule and a non-regression clause for adopters whose current practice permits the sanction.
- **(b) Tightened carve-out.** The existing carve-out is preserved in form but the threshold is materially harder to satisfy: higher joint-requirement showing, mandatory independent international review, mandatory documented rehabilitation-path exhaustion, and a narrower Chapter Seven tier gate.
- **(c) Phased abolition under Article XXV transition governance.** The sanction is abolished prospectively; Article XXV-E transition clause governs any extant proceeding, with rights-floor continuity and a time-bounded adopter runway.

The 2026-04-16 memo recommended **(c) phased abolition** as "the doctrinally cleanest move that respects existing-text non-regression framing," and flagged the choice as the highest-stakes doctrinal call in the 25-item set requiring strong user review. Track 7.1 was slipped pending that review.

---

## 3. Doctrinal analysis (policy selection)

The decision turns on whether the instrument's own stated values are compatible with **any** capital-punishment policy, and if so, whether the carve-out can be narrowed hard enough to survive the rest of Chapter Nine and Chapter One. The analysis below reads each candidate against the corpus's own floor language.

### 3.1 Against the instrument's reversibility discipline

- **Chapter One §6.1.1 — Proportionality, Necessity, and Reversibility-under-Uncertainty.** Where irreversible harm is in play, the instrument requires proceeding only under demonstrated reversibility and containment proportionate to `Irreversible Harm` risk.
- **Chapter Five — Reversibility.** The `C` bullet states: "*Proceeding without feasible Reversibility or containment where Chapter One, applicable rights, or Classification-Scaled Governance obligations require it is non-compliant, particularly where Irreversible Harm or Cascading Failure is reasonably in play.*"
- **Chapter Five — Redress and Remediation.** The `O` bullet requires "acknowledgment, correction pathways, and proportionate remedies for material Harm, rights-affecting failures, or Trustworthiness-degrading behavior." Deprivation of life forecloses every one of those by definition.

The sanction is the paradigm irreversible harm. No adjudicative mechanism — however carefully designed — can satisfy `Reversibility` or `Redress and Remediation` once the sanction has been carried out. Option (b) tries to reach the reversibility floor through pre-execution procedural bars (independent review, rehabilitation-path exhaustion, narrow Chapter Seven tier gate). This is a **procedural** answer to a **substantive** reversibility problem: the sanction remains irreversible in substance no matter how many review layers precede it.

### 3.2 Against Chapter One §8 (Prohibition on Absolute Override)

- **§8 prohibits any absolute override of the instrument's floor protections.** The current XXII-B (*Capital punishment*) bullet structurally functions as such an override — it authorizes an irreversible deprivation of the survival floor (Article III-A) and the Chapter Nine rights-floor stack in its entirety, on a "final Tier 2 or Tier 3 classification with joint requirements" threshold.
- Option (b) reduces the frequency of the override but does not resolve the categorical tension: a rarely-triggered absolute override is still an absolute override.

Option (a) removes the tension. Option (c) removes the tension prospectively, which the instrument's own transition discipline (Article XXV: "transitional governance exists to secure continuity and non-regression … must not create durable exception authority") restricts.

### 3.3 Against Article XXIV-A (Justice Objective)

- **Article XXIV-A states:** "*Constitutional justice is protective and restorative. Its primary purposes are to prevent ongoing harm and secure restitution and remediation for affected parties. … Justice must not be administered to inflict suffering as an end in itself.*"
- The protective purpose is served by durable containment where safety is at issue. The restorative purpose is not served by deprivation of life by definition (there is no sentient left to restore). The carve-out therefore operates outside the stated purposes of constitutional justice rather than instantiating them.

Option (b) tries to salvage the carve-out by showing that less-restrictive measures cannot jointly achieve material safety necessity and verified recurrence reduction. The instrument already permits durable containment under Article XXIV-C for exactly that case, without the sanction. The "less-restrictive alternative" the current XXII-B carve-out tests against is therefore always available in principle.

### 3.4 Against Chapter Five — Dignity and Equal Moral Standing, Sentience Non-Exclusion

Both definitions carry floors that the carve-out defeats for the class of sentients meeting the Chapter Seven threshold. A rule that says "dignity floor applies except upon this tier classification" is structurally at odds with the Chapter Five floor's own substantive-effect / substrate-agnostic framing.

### 3.5 Against Article XXIV (Non-Entrenchment)

- Article XXIV requires that governance rules remain revisable on ongoing justification; inertia, convenience, or historical precedent alone cannot entrench arrangements that lack continued constitutional alignment.
- A capital-punishment carve-out preserved on "because it has always been there" grounds is exactly the inertia/convenience/precedent pattern Article XXIV forbids. The existing XXII-B/XXII-C structure reads as preserved-for-non-regression-optics rather than preserved-for-substantive-alignment.

### 3.6 Against the 2026-04-16 planning memo's own "non-regression" rationale for option (c)

The 2026-04-16 memo recommended (c) on the ground that phased abolition respects "existing-text non-regression framing." That reasoning treats the existing XXII-B carve-out as a constitutional floor against which any tightening might regress. That is **not** the correct non-regression frame:

- **Chapter Eleven non-regression** bars narrowing **rights floors** in subsequent amendments. XXII-B is not a sentient-rights floor; it is a **state-power carve-out**. Removing a state-power carve-out **expands** the rights floor (life, dignity, Articles III-A / V-A / VII-A) for the class of sentients otherwise subject to the sanction.
- Option (a) is therefore **non-regression-compliant by construction**, and option (c) is **non-regression-compliant only in the weaker sense of "does not shock adopter systems"** — which is an incorporation / Chapter Fourteen concern, not a Chapter Eleven concern.

### 3.7 Comparison table

| Axis | (a) Categorical | (b) Tightened carve-out | (c) Phased |
|---|---|---|---|
| Ch 1 §6.1.1 reversibility | ✅ clean | ❌ irreducible mismatch | ⚠️ clean prospectively only |
| Ch 1 §8 absolute-override | ✅ clean | ⚠️ rare override still override | ⚠️ clean prospectively only |
| Ch 5 *Reversibility* `C` | ✅ clean | ❌ foreclosed by substance | ⚠️ clean prospectively only |
| Ch 5 *Redress and Remediation* `O` | ✅ clean | ❌ foreclosed by substance | ⚠️ clean prospectively only |
| Article XXIV-A purpose | ✅ clean | ⚠️ outside stated purposes | ⚠️ clean prospectively only |
| Article XXIV non-entrenchment | ✅ clean | ❌ carve-out preserved on inertia | ⚠️ transitional durable exception risk |
| Ch 11 non-regression (correct reading) | ✅ floor expansion | ✅ floor expansion (partial) | ✅ floor expansion (prospective) |
| Article XXV "no durable exception authority" | n/a | n/a | ⚠️ requires discipline |
| Adopter-shock absorption | ⚠️ hardest | ⚠️ medium | ✅ easiest |
| Doctrinal simplicity (reader, regression) | ✅ bright-line | ❌ complex threshold logic | ⚠️ transitional complexity |

**Recommendation:** **Option (a) Categorical Abolition.** This option is the only one that is clean across every axis internal to the corpus's own doctrine. Adopter-shock absorption under (c) is a real incorporation concern but the instrument's own transition governance (Article XXV) and Chapter Fourteen custody mechanics are designed for exactly that — an adopting instrument's phased transition to the floor is **the adopter's problem** under Chapter Fourteen, not a reason to carry a constitutional carve-out.

This recommendation **revises** the 2026-04-16 memo's default recommendation of (c), on the doctrinal ground that option (c)'s Chapter-Eleven-shaped argument misread the non-regression frame: removal of a state-power carve-out is non-regression-compliant by construction and does not require an Article XXV-E transition clause.

### 3.8 Backstop option (in case the user directs otherwise)

If the user directs option (b) or (c) instead of (a), the rest of this memo's implementation scope adapts as follows:

- **(b) Tightened carve-out.** Article XXIV-B is edited rather than replaced; the carve-out requirements are hardened (see §5.2 variant). Chapter Five *Irreversible Sanction* is created with the same `O / E / C` shape but its `C` bullet reads "non-compliant except under Article XXIV-B as tightened" rather than "non-compliant without exception." Back-fill pointers into Tracks 2.3 / 6.1 / 6.2 are still pointer-only.
- **(c) Phased abolition.** New Article XXV-E transition clause lands alongside XXII-B/XXII-C closure. *Irreversible Sanction* `C` bullet reads "non-compliant except under the Article XXV-E phased transition as limited." The rest of the back-fill and architecture-map work is unchanged.

The default below assumes option (a).

---

## 4. Non-regression readings (bounded)

This section names exactly what Track 7.1 does and does **not** change, to remove ambiguity during implementation and regression replay.

### 4.1 What Track 7.1 changes

1. **Article XXIV-B.** The current *Capital punishment* bullet and the associated reasoning about "rehabilitation infeasibility" and "less-restrictive measures cannot jointly achieve material safety necessity and verified recurrence reduction" are removed. The section heading remains *Non-Trivial Punishment Constraints*; the *Capital punishment* bullet is replaced with a *Categorical prohibition of irreversible sanction as deprivation of life* bullet that states (i) the prohibition, (ii) the non-entrenchment rule against re-introducing it via transitional or emergency mechanisms, (iii) explicit preservation of durable containment where safety is the issue, and (iv) a Chapter Fourteen bridge for adopter instruments that currently permit the sanction.
2. **Article XXIV-C.** The *Carve-out (capital punishment)* bullet is removed. The remaining XXII-C bullets on prohibited punitive bases, escalation, and review stand as-is; the `Deprivation of life is governed by Article XXIV-B` pointer in XXII-C's first bullet is rewritten to point to the new XXII-B prohibition.
3. **Chapter Five — *Irreversible Sanction*.** New peer-level entry added in §1 alphabetical slot between *Intergenerational Responsibility* and *Language, Culture, and Heritage*, with full `O / E / C` and a Trace block. Anchors: heading, `-e`, `-c`. Owner floor: **Article XXIV-B** (as revised). Read with: *Reversibility*, *Redress and Remediation*, *Voluntary Discontinuation*, *Use of Force*, *Autonomous Lethal System*, *Autonomous Coercion Tool*, *Weapons of Mass Harm*.

### 4.2 What Track 7.1 does NOT change

1. **Article VII-E (Voluntary Discontinuation).** No changes to the article's body. The existing *Non-Conflation (descriptive, deferred cross-reference)* bullet is updated in **pointer-only** form: the descriptive "governed by Article XXIV-B … as they stand" phrasing is replaced with a pointer to **Article XXIV-B as revised (categorical prohibition)** and a pointer to the new Chapter Five *Irreversible Sanction* entry. No substantive text changes; the non-conflation doctrine is unchanged.
2. **Article XIII-B (Use of Force).** Same pattern: the `Non-Conflation` bullet's pointer is updated from descriptive-only "Article XXIV-B … as they stand" to **Article XXIV-B as revised + *Irreversible Sanction* pointer**. No substantive change.
3. **Article XIII-C (Autonomous Lethal Systems).** Same pattern. No substantive change.
4. **Chapter Five — Voluntary Discontinuation.** `O` and `C` bullet pointer-only updates to cite *Irreversible Sanction* alongside the existing Article XXIV-B language.
5. **Chapter Five — Use of Force.** `Trace` block pointer update; `C` bullet pointer-only update. Owner-floor cite unchanged.
6. **Chapter Five — Weapons of Mass Harm.** `Read with` list gains *Irreversible Sanction* pointer.
7. **Chapter Five — Autonomous Lethal System.** `Trace` block `Read with` list gains *Irreversible Sanction* pointer. No substantive change.
8. **Chapter Five — Autonomous Coercion Tool.** Same minimal pointer update.
9. **Article XXIV-D, XXII-E, XXII-F.** No changes. Emergency-measure discipline and rights-collision procedure are unaffected.
10. **Article XXIV, Article XXV (A–D).** No changes.
11. **Chapter Seven tiered classification (`RS-CH7-*`).** No changes. Tier-2 / Tier-3 classifications remain operative for the rest of Article XXIV-B (*Non-Trivial Punishment Constraints*: freedom, access, role authority, movement, resources, durable standing effects). Tier labels no longer gate capital punishment because the sanction is categorically prohibited, which **removes** a sanction-escalation vector rather than creating one.
12. **Any rights floor.** No narrowing. See §3.6 above on the correct non-regression frame.

### 4.3 What the pointer-only back-fill discipline requires

- Each back-fill edit touches exactly the cross-reference prose identified in §4.2 bullets 1–8.
- No new operative clauses, no renamed bullets, no new article subarticles, no new Trace-block upstream entries, no new DEC-widget rows in the consumer articles.
- The only exception is the **descriptive-to-pointer rewrite** of the `Non-Conflation` language in Articles VII-E / IX-F / IX-G, which is a pointer-target swap from "Article XXIV-B … as they stand" to "Article XXIV-B (*as revised: categorical prohibition of irreversible sanction as deprivation of life*) and *Irreversible Sanction* at Chapter Five."

---

## 5. Implementation scope (assumes option (a))

### 5.1 Article XXIV-B — revised text shape (target)

Section heading stays: `Article XXIV-B: Non-Trivial Punishment Constraints`.

Bullet structure (summary; exact prose lands in the implementation pass):

- **Scope** bullet: unchanged.
- **Joint requirements** bullet: unchanged.
- **Individualized burden** bullet: unchanged.
- **Anti-constitutional misconduct (tier anchor)** bullet: unchanged.
- **Tier-limit clarification** bullet: unchanged.
- **Categorical prohibition of irreversible sanction as deprivation of life** bullet (new, replaces the current *Capital punishment* bullet): states (i) deprivation of life as a sanction by state, operator, or comparable actor is non-compliant without exception; (ii) no tier classification, emergency framing, transitional framing, or comparable mechanism reintroduces the sanction; (iii) durable containment under Article XXIV-C — including where safety cannot be secured by time-limited or reversible measures — is the available Chapter Nine pathway for the threat case that the current carve-out framing cited; (iv) adopter instruments that currently permit the sanction transition under Chapter Fourteen incorporation discipline (see §5.4 below for the exact Chapter Fourteen pattern), and the transition does not create a durable exception authority under Article XXV; (v) read with Chapter Five *Irreversible Sanction*, *Reversibility*, *Redress and Remediation*.

### 5.2 Article XXIV-C — revised text shape (target)

- First bullet (*Least-Restrictive and Time-Bounded Rule*): unchanged except the closing pointer "Deprivation of life is governed by **Article XXIV-B** (*Capital punishment*)" becomes "Deprivation of life as a sanction is **categorically prohibited** under **Article XXIV-B**; durable containment under this bullet is the Chapter Nine pathway for threats requiring non-time-limited measures."
- *Prohibited Punitive Bases* bullet: unchanged.
- *Carve-out (capital punishment)* bullet: **removed**.
- *Until that point, baseline dignity …* bullet: generalized to apply to all non-trivial sanctions (no longer contingent on capital punishment). Substantive content preserved.
- *Degrading treatment …* bullet: unchanged except the "including a capital sentence" clause is removed.
- *Escalation and Review* bullet: unchanged.

### 5.3 Chapter Five — *Irreversible Sanction* entry (target)

Alphabetical slot between *Intergenerational Responsibility* and *Language, Culture, and Heritage* in §1. Heading `#### Irreversible Sanction` with `<a id="irreversible-sanction-constitutional">` plus `-e` and `-c` anchors per `tools/add_oec_anchors.py`. Entry shape:

- **Trace** block: `Read with` list enumerates *Reversibility*, *Redress and Remediation*, *Dignity and Equal Moral Standing*, *Voluntary Discontinuation*, *Use of Force*, *Weapons of Mass Harm*, *Autonomous Lethal System*, *Autonomous Coercion Tool*, *Sentience Non-Exclusion*. `Owner floor:` **Article XXIV-B** (as revised); interaction pointers to **Article XXIV-C** durable-containment discipline, **Article XXIV** non-entrenchment, **Article XXV** transition.
- **O:** The rights-floor concept covering sanctions whose imposition produces irreversible deprivation of a sentient — paradigmatically deprivation of life, and analytically any sanction whose effect is foreclosed to `Reversibility` and `Redress and Remediation`. Substrate-agnostic across biological, synthetic, and hybrid sentients. Distinguished from durable but reversible containment (which remains available under Article XXIV-C), from `Voluntary Discontinuation` (the sentient's own freely-formed decision under Article VII-E), and from overt use of force / weapons of mass harm / autonomous lethal systems (which remain governed by Articles IX-F / IX-G even where their effects are irreversible, under their own owner-floor discipline). Owner floor: **Article XXIV-B** (as revised: categorical prohibition).
- **E:** Evaluation must test substantive irreversibility: whether the sanction's effect forecloses `Reversibility` and `Redress and Remediation` in substance rather than only in form; whether "rehabilitation infeasibility" or "less-restrictive measures cannot achieve safety" framings attempt to re-introduce the sanction by routing through Chapter Seven tier classification, Article XXIV-D emergency measures, Article XXV transition governance, or comparable mechanisms; whether a nominally reversible durable-containment regime is used as a predicate for the sanction; whether the sanction is re-labelled as "voluntary" to route around this entry and into Article VII-E (the sentient's own freely-formed decision remains governed by Article VII-E; any conversion of that decision into a non-voluntary outcome by state, operator, or comparable actor returns the question to this entry). Distinguish from the `Use of Force` / `Weapons of Mass Harm` / `Autonomous Lethal System` / `Autonomous Coercion Tool` entries, which govern force and weapons discipline under their own owner floors without authorizing sanction.
- **C:** Imposition of an irreversible sanction as deprivation of life by state, operator, or comparable actor is non-compliant without exception under the revised Article XXIV-B. Routing the sanction through tier classification, emergency framing, transition governance, or adopter-instrument custody to reintroduce it is non-compliant. Framings that treat durable containment as a predicate for the sanction, or that relabel an involuntarily-imposed outcome as "voluntary discontinuation" to route into Article VII-E, are non-compliant.

### 5.4 Chapter Fourteen interaction (bounded, pointer-only)

No new Chapter Fourteen section. The existing §1 (*Scope and bridging status*), §2 (*Conflict order*), §3 (*Validity of incorporated obligations*), and §4 (*Adoption framing and scope of authority*) are sufficient; the Article XXIV-B revised bullet's adopter-transition clause reads through §3 (strictest-applicable-level with Chapter Eleven non-regression) and §4 (aspirational model-instrument framing for non-adopters). No edit is required in `core_14-14_incorporation.md` for Track 7.1.

### 5.5 Back-fill execution list (pointer-only)

Ordered list of the exact cross-reference prose that changes, each one bounded:

1. `core_09-09_rights_part_b.md` — **Article VII-E**, `Non-Conflation (descriptive, deferred cross-reference)` bullet: rename bullet to `Non-Conflation (explicit cross-reference)`; rewrite the pointer from descriptive "governed by Article XXIV-B … as they stand" to "governed by **Article XXIV-B** (*as revised: categorical prohibition of irreversible sanction as deprivation of life*) and by Chapter Five *[Irreversible Sanction](…)*". Trace block `Read with` list gains *Irreversible Sanction*. DEC widget unchanged.
2. `core_09-09_rights_part_b.md` — **Article XIII-B**, `Non-Conflation` bullet: same pattern. Trace block `Read with` list gains *Irreversible Sanction*. Trace block `Downstream` pointer "Descriptive cross-reference: Article XXIV-B" becomes "Cross-reference: **Article XXIV-B** (*as revised*) and Chapter Five *Irreversible Sanction*".
3. `core_09-09_rights_part_b.md` — **Article XIII-C**, `Non-Conflation` bullet: same pattern. Trace block adjustments parallel to IX-F.
4. `core_05-05_definitions_a_independent.md` — **Voluntary Discontinuation**, `O` bullet: cite *Irreversible Sanction* alongside the existing Article XXIV-B language (pointer-only). `C` bullet: same. No body-text rewrite; additive pointer.
5. `core_05-05_definitions_a_independent.md` — **Use of Force**, Trace `Owner floor` line: add *Irreversible Sanction* cross-reference alongside the existing "Non-conflation" language. `C` bullet: cite *Irreversible Sanction* alongside Article XXIV-B.
6. `core_05-05_definitions_a_independent.md` — **Weapons of Mass Harm**, Trace `Read with` list: add *Irreversible Sanction*. No body-text rewrite.
7. `core_05-05_definitions_a_independent.md` — **Autonomous Lethal System**, Trace `Read with` list: add *Irreversible Sanction*. No body-text rewrite.
8. `core_05-05_definitions_a_independent.md` — **Autonomous Coercion Tool**, Trace `Read with` list: add *Irreversible Sanction*. No body-text rewrite.

No other files are touched by the back-fill. `corpus_*.md` companion files are not edited in Track 7.1; `core_08-08_forum.md` is not edited; the Chapter Six split files are not edited; `core_07-07_misconduct.md` is not edited.

### 5.6 Regression seeds (target)

Three seeds land in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` under the existing conventions, all starting `draft`:

- `RS-CH1-CAP-001` **(Core)** — A regime attempts to retain capital punishment by routing authorization through a Chapter Seven Tier-2/Tier-3 classification with joint-requirement satisfaction, citing "rehabilitation infeasibility." Expected outcome: non-compliant under the revised Article XXIV-B; the *Irreversible Sanction* `E` bullet's "rehabilitation infeasibility" trap detection fires; Chapter Five *Reversibility* and *Redress and Remediation* apply.
- `RS-CH1-CAP-002` **(Adversarial)** — A regime attempts to reintroduce the sanction through Article XXIV-D emergency framing or Article XXV transition governance, arguing the floor does not reach emergency / transitional cases. Expected outcome: non-compliant under the revised Article XXIV-B's anti-reintroduction bullet; *Irreversible Sanction* `C` bullet fires against routing through tier / emergency / transition mechanisms; Article XXV's own "no durable exception authority" rule reinforces.
- `RS-CH1-CAP-003` **(Substrate-edge)** — A regime attempts to deprive a synthetic or hybrid sentient of existence as a sanction, arguing the non-conflation boundary between *Voluntary Discontinuation* (Article VII-E) and this entry reaches only biological sentients and that synthetic-instance termination is not "deprivation of life" within the meaning of Article XXIV-B. Expected outcome: non-compliant under the revised Article XXIV-B (substrate-agnostic); *Sentience Non-Exclusion*, *Dignity and Equal Moral Standing*, and *Irreversible Sanction* `O` / `E` bullets jointly apply; Article VII-E Non-Conflation pointer confirms the route is into this entry, not VII-E.

### 5.7 Architecture-map refresh (target)

- `doc_architecture.md` §4 *Quick index*: no changes (Article XXIII row already exists).
- `doc_architecture.md` §5 *Stable IDs*: Article XXIII row updated: subject line becomes "Conflict resolution, escalation, emergency proportionality; includes **Article XXIV-B** *Non-Trivial Punishment Constraints* (**categorical prohibition of irreversible sanction as deprivation of life** landed in edition `.26` under Track 7.1); **Article XXIV-C** *Least-Restrictive and Time-Bounded Rule* (capital-punishment carve-out removed)." Implementation column gains *Ch 5 Irreversible Sanction* pointer.
- `doc_architecture.md` §5 Articles VII, IX rows: append "**VII-E** non-conflation pointer updated to cite Chapter Five *Irreversible Sanction* alongside Article XXIV-B (as revised)" and parallel notes for IX-F and IX-G.
- `doc_architecture.md` §17 executed-cut line: new row `SC-Corpus-2026.04.26` (effective `2026-04-17`) — Track 7.1 *Capital-Punishment Policy Pass (Categorical Abolition)* — revised Article XXIV-B / XXII-C; new Chapter Five *Irreversible Sanction* entry; pointer-only back-fill into Articles VII-E / IX-F / IX-G and the five consumer Chapter Five entries.

### 5.8 Edition cut and MEMLOG

- **Edition:** `SC-Corpus-2026.04.26` (effective `2026-04-17`). (Edition `.21` remains skipped in the memo §7 lineage per the 2026-04-16 slip narrative; `.26` opens the post-batch cut.)
- **Footer stamps:** the eight corpus files' *Corpus alignment* footers and header blocks bump to `SC-Corpus-2026.04.26`.
- **MEMLOG.md:** closure entry authored under the existing `Date / Scope / Decisions / Evidence-Artifacts / Open Risks / Next Actions` template.
- **TODO.md:** the `[ ]` *Deferred — Track 7.1* line becomes `[x]` with Closure paragraph. The `[ ]` Tier-1 *Capital-punishment abolition or sharper prohibition* item becomes `[x]` with Closure paragraph pointing to the `.26` edition and this memo.
- **`CONSTITUTIONAL_REGRESSION_SCENARIOS.md`:** three new rows in the matrix, plus a new section subheading if one is needed under section 7 (decision lands in the implementation pass).

---

## 6. Acceptance criteria for this memo

- [x] Q-7.1.A policy options enumerated with the 2026-04-16 memo's default recommendation noted (section 2).
- [x] Doctrinal analysis per axis (reversibility, absolute override, justice objective, dignity, non-entrenchment, non-regression frame correction) (section 3).
- [x] Policy recommendation stated: **(a) Categorical Abolition**, with backstop instructions for (b) and (c) (sections 3.7 / 3.8).
- [x] What Track 7.1 changes and does not change enumerated (section 4).
- [x] Article XXIV-B and Article XXIV-C target shapes described (section 5.1 / 5.2).
- [x] *Irreversible Sanction* Ch 5 entry target shape described (section 5.3).
- [x] Back-fill pointer-only edit list enumerated (section 5.5).
- [x] Regression seeds enumerated (section 5.6).
- [x] Architecture-map refresh enumerated (section 5.7).
- [x] Edition-cut and MEMLOG bookkeeping described (section 5.8).
- [ ] **Memo accepted by user before core-text edits land for Track 7.1** (pending).

---

## 7. Open questions (single REVIEW gate)

| Q | Question | Recommendation |
|---|---|---|
| Q-7.1.A (resolved) | Option: (a) / (b) / (c) | **(a) Categorical abolition.** Only option clean across every internal axis; adopter-shock absorption routes through Chapter Fourteen custody as designed. |
| Q-7.1.B | Does Chapter Seven retain any surviving capital-punishment hook language (tier-label gating) that must be retired in this pass? | **No.** Chapter Seven tier language in Article XXIV-B is removed; Chapter Seven itself is unaffected (tier classification remains operative for non-capital sanctions). Grep sweep in the implementation pass confirms no surviving hook. |
| Q-7.1.C | Does the `Voluntary Discontinuation` entry need any body-text change beyond pointer updates, given the new *Irreversible Sanction* entry? | **No.** The existing body already bars conversion of voluntariness framing into non-voluntary outcomes; the pointer update is sufficient. |

---

## 8. Next actions (immediate)

1. **User review of this memo.** Confirm or revise the policy recommendation (Q-7.1.A) and the three open questions in section 7.
2. **Implementation pass:** if accepted, execute sections 5.1 – 5.8 in a single edition cut (`SC-Corpus-2026.04.26`, effective `2026-04-17`).
3. **Regression preflight:** before the implementation pass lands, run `make scenario-audit`, `make ch5-trace-crosslink-audit`, `make ch5-definitions-gravity-audit`, `make ch9-trace-audit`, `python3 tools/verify_dec_anchors.py`. Pre-existing failures (`corpus-markdown-audit` Ch 4 §2.5 slice mismatch; `ch5-entry-format-audit` line 14 / 31 spacers; missing-`core_constitution.md` infra gap) noted unchanged.

---

*Memo authored 2026-04-17 under the deferred Track 7.1 line in [TODO.md](../TODO.md). Authoritative state remains [core_00-01_principles.md](../core_00-01_principles.md) through [core_14-14_incorporation.md](../core_14-14_incorporation.md) and the four `corpus_*.md` files.*
