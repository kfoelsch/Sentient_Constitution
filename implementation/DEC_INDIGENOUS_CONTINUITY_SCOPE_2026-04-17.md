# Q-10.2.B Scoping Memo — *Indigenous Continuity*

**Date:** 2026-04-17
**Scope:** Q-10.2.B from [DEC_CONTENT_GAPS_PLAN_2026-04-16.md](DEC_CONTENT_GAPS_PLAN_2026-04-16.md) §10.2 (indigenous-continuity scope). The 2026-04-16 memo left Q-10.2.B open with the note "scope **not** scoped at memo time; must be scoped in a dedicated pass before any Chapter Five entry lands."
**Authority:** Process and planning artifact under [doc_architecture.md](../doc_architecture.md) §13 / §4 (definitions protocol). Not itself binding constitutional text. Per standing plan-first gate, **no core-text edits land for this track before this memo is accepted.**
**Status:** Draft — recommending **Scope (b): Chapter Five entry only, community-based non-regression floor, routes to existing owner articles.** Open for review; companion implementation pass is ready to execute on acceptance.

---

## 1. Purpose

This memo closes the second open REVIEW-gate question that was deferred from the 2026-04-16 edition batch: **Q-10.2.B** (indigenous-continuity scope). It does three things:

1. **Scope selection.** Chooses among four candidate scopes (see §3) for a new *Indigenous Continuity* Chapter Five entry (and/or Chapter Nine refinement), with reasoning tied to (a) the corpus's substrate-agnostic policy, (b) its refusal to rely on politically-contested category determinations, and (c) its Chapter Fourteen adopter-jurisdiction discipline.
2. **Implementation scope.** Specifies exactly what lands in Chapter Five (and what does not land in Chapter Nine) under the recommended scope.
3. **Acceptance artifacts.** Enumerates regression seeds, architecture-map refresh, and edition-cut bookkeeping.

This memo is independent of Track 7.1 (capital-punishment policy, [DEC_TRACK_7_1_POLICY_2026-04-17.md](DEC_TRACK_7_1_POLICY_2026-04-17.md)) and may land on its own edition cut.

---

## 2. Background

### 2.1 Existing corpus coverage

- **Article V-B (*Nondiscrimination*), *Language, Culture, and Heritage Protection* bullet (core_09-09_rights_part_b.md):** covers language, cultural affiliation, heritage, traditions, and comparable cultural-identity characteristics as protected-characteristic specializations. Explicitly notes: *"Indigenous continuity questions and territorial-continuity interactions remain a matter for review under Article I-A and Chapter Fourteen incorporation, and this bullet neither expands nor narrows them."*
- **Chapter Five *Language, Culture, and Heritage* E-bullet:** carries the same hedge: *"Indigenous continuity questions and their interaction with Article I-A territorial-continuity material are read with this entry but remain a matter for review under their own owner articles; this entry does not resolve those scope questions."*
- **Article I-A (*Environmental Preconditions and Ecological Integrity*), core_09-09_rights_part_a.md:** carries the territorial / ecosystem-integrity floor, separate Animal Life and Contested-Sentient Life interactions, and the biosphere-as-precondition policy.
- **Chapter Five *Natural Systems Standing*:** recognizes continuity and integrity interests of life-supporting natural systems including the biosphere.
- **Chapter Five *Intergenerational Responsibility*:** covers duties toward future sentients and continuity of environmental preconditions and wellbeing-relevant systems.
- **Chapter Fourteen (*Incorporation*):** §3 strictest-applicable-level and Chapter Eleven non-regression floor; §4 adoption policy.
- **Article XVIII-D (*Movement, Migration, and Refuge*):** refuge from non-compliance, non-statelessness.
- **Chapter Five *Protected Characteristics*:** substrate-agnostic protection against discrimination, with cultural-identity as a specialization.

### 2.2 What is not presently covered

- **Community-level continuity** (as distinct from individual-level cultural-identity protection). Article V-B protects the individual's language / heritage / cultural-identity exercise; it does not carry a community-level continuity floor.
- **Territorial-continuity interaction** where a community has durable historical connection to particular territory or ecosystem and where that connection is materially implicated in the community's cultural, linguistic, governance, or knowledge-transmission continuity. Article I-A covers ecosystem integrity as a precondition but does not carry a community-to-territory continuity floor.
- **Knowledge-transmission-chain protection** where the transmission chain is community-custodial rather than individual-to-individual (traditional ecological knowledge, land-based cultural practice, community governance practice).
- **Non-regression policy** for adopter instruments that currently recognize indigenous or analogous community-continuity rights. Chapter Eleven non-regression applies to constitutional rights-floor content; it does not by itself fix a floor against which adopter regression in this domain can be measured.

### 2.3 Why this is hard

- **Category-contest risk.** "Indigenous" and cognate terms carry heterogeneous adopter-jurisdiction definitions, often politically contested. The corpus's general discipline (Article V-E sentience-status adjudication; Article V-B protected-characteristic proxying; Chapter Five *Dignity and Equal Moral Standing* substrate-agnostic frame) is to avoid relying on contested category determinations for rights-floor trigger conditions.
- **Substrate-agnostic discipline.** The corpus reads "substrate-agnostically across biological, synthetic, and hybrid sentients." A conventionally human-only framing of "indigenous" would contradict that discipline; a literal substrate-agnostic framing would produce edge cases (synthetic-sentient "indigenous" communities with compute-heritage continuity) that — while principled — risk diluting the core concept.
- **Territorial-claim adjudication risk.** Any constitutional entry that could be read as adjudicating historical land claims creates an adopter-capture vector (opposing sides will each claim the instrument supports their position). Chapter Fourteen's adopter-jurisdiction discipline exists to keep the corpus out of such adjudications.
- **Non-regression vs. new-right tension.** If the entry is framed as a new rights floor, adopters whose current systems do not recognize any indigenous-continuity rights would be regressed into compliance obligations they did not previously carry. If the entry is framed as non-regression only, adopters whose current systems do recognize such rights would be held against their own prior recognition (which is constitutionally correct under Chapter Eleven), but the entry would not reach adopters with no prior recognition.

---

## 3. Scope options

Four candidate scopes were considered. The memo discusses each, then recommends.

### 3.1 Scope (a) — No new Chapter Five entry; Article V-B refinement only

Add a short refinement bullet to Article V-B *Language, Culture, and Heritage Protection* that (i) extends the individual-level protection to explicitly include community-custodial transmission, (ii) preserves the existing deferral to Article I-A and Chapter Fourteen for territorial-continuity interactions, and (iii) adds a non-regression clause for adopters that currently recognize community-level indigenous or comparable continuity rights.

- **Pros.** Minimal new surface; no new category-contest risk; non-regression framing is clean; avoids territorial-claim adjudication.
- **Cons.** Leaves the existing hedge in place (no new handle for consumer articles or regression scenarios to hook on); community-continuity protection remains implicit rather than explicit; the Article V-B bullet grows substantively without a matching Chapter Five entry to sit at the definitions layer.
- **Assessment.** Cheap and safe but does not actually add rights-floor surface; mostly cosmetic.

### 3.2 Scope (b) — Chapter Five entry only; community-based non-regression floor; routes to existing owner articles

Create a new Chapter Five entry `#### Indigenous Continuity` that:
- **O (Operational substance):** defines the concept in community-centric and capability-functional terms (not category-label terms), substrate-agnostically but anchored to communities with durable historical connection to particular territory or ecosystem (biosphere, info-sphere, or comparable substrate-context where materially implicated); covers language, cultural practice, governance practice, and knowledge-transmission continuity including community-custodial traditional / ecological / technical knowledge; owner-floor pointers to **Article V-B** (nondiscrimination and language / culture / heritage protection) and **Article I-A** (territorial / ecosystem-integrity precondition); interaction pointers to **Article XVIII-D** (refuge / non-statelessness) and **Chapter Fourteen** (adopter discipline).
- **E (Evaluation):** tests whether cultural, linguistic, governance, or knowledge-transmission continuity is materially implicated by the decision or framing under review; refuses category-label framing as a substitute for capability-functional evaluation; applies *Protected Characteristic Proxying and Disparate Impact* to policies that produce disparate effect on community-continuity outcomes; applies **Chapter Fourteen** adopter-jurisdiction discipline to territorial-continuity questions (the entry neither adjudicates historical claims nor creates a restitution mandate); applies **Chapter Eleven non-regression** to adopter instruments that currently recognize indigenous or comparable community-continuity rights (the entry does not re-originate the recognition, but non-regression locks what is already there).
- **C (Compliance):** narrowings, displacements, or substrate-class exclusions that defeat community-level continuity without satisfying Article V-B *Necessity* / *Proportionality* are non-compliant; adopter narrowing below its own prior recognition floor for indigenous or comparable community-continuity rights is non-compliant under Chapter Eleven; category-label framings that substitute for capability-functional evaluation are non-compliant.
- **No new Chapter Nine article.** The existing Article V-B hedge language is minimally updated from *"neither expands nor narrows"* to *"is read with Chapter Five Indigenous Continuity"* (pointer-only).

- **Pros.** Adds explicit Chapter Five surface with hooks for regression seeding and consumer-article reference; avoids category-contest by using capability-functional trigger conditions; avoids territorial-claim adjudication by explicit Chapter Fourteen routing; preserves substrate-agnostic discipline by reading to communities not persons; anchors adopter non-regression discipline.
- **Cons.** Some irreducible category-adjacent reading risk; consumer articles do not grow, which is deliberate but may disappoint expectations of a broader landing.
- **Assessment.** **Recommended.** Adds real surface with minimal adjudication risk; is consistent with the corpus's broader discipline (capability-functional triggers; owner-article routing; Chapter Fourteen adopter discipline); is the narrowest scope that materially improves on the status quo.

### 3.3 Scope (c) — Chapter Five entry AND new Chapter Nine article (e.g., Article V-I Indigenous Continuity)

Same Chapter Five entry as (b), plus a new sub-article `#### Article V-I: Indigenous Continuity` in Chapter Nine with operative bullets on recognition, transmission-chain protection, territorial-continuity interaction, and consultation requirements for decisions materially implicating community continuity.

- **Pros.** Operative article-level surface; clearer regression hook for adopters who would otherwise treat this as advisory.
- **Cons.** Territorial-claim adjudication risk is much higher (article-level operative language is harder to read as non-adjudicatory than Chapter Five definitional language); category-contest risk is higher (an article-level trigger invites category-challenge litigation); scope-creep risk into adopter jurisdiction.
- **Assessment.** **Not recommended in this pass.** Could be revisited after the (b) entry has regression-stability data and if adopters report that the Chapter Five-only surface is under-protective.

### 3.4 Scope (d) — Indigenous-continuity policy addressed solely through Chapter Fourteen incorporation discipline

No Chapter Five entry; no Chapter Nine article. Chapter Fourteen §3 (strictest-applicable-level) and §4 (adoption policy) are relied on to pull adopter-instrument protections into the custody chain for adopting entities that already recognize indigenous-continuity rights.

- **Pros.** Zero new surface; zero adjudication risk; respects adopter jurisdiction.
- **Cons.** Completely fails to provide Chapter Five consumer-article surface or regression-scenario hook; effectively ratifies Article V-B's existing deferral language without improvement; does not address the open question at all — it chooses silence.
- **Assessment.** Not recommended. This is the scope the 2026-04-16 memo already effectively represents; Q-10.2.B exists because silence is not adequate.

### 3.5 Comparison table

| Axis | (a) Art V-B refine | (b) Ch 5 only | (c) Ch 5 + Ch 9 article | (d) Ch 14 only |
|---|---|---|---|---|
| Adds operative rights-floor surface | ⚠️ marginal | ✅ yes (defs layer) | ✅ yes (article layer) | ❌ no |
| Chapter Five consumer-article hook | ❌ no | ✅ yes | ✅ yes | ❌ no |
| Regression-scenario hook | ⚠️ marginal | ✅ yes | ✅ yes | ❌ no |
| Category-contest risk | ✅ low | ✅ low (capability-functional) | ⚠️ elevated | ✅ low |
| Territorial-claim adjudication risk | ✅ low | ✅ low | ⚠️ elevated | ✅ low |
| Substrate-agnostic discipline | ✅ clean | ✅ clean | ⚠️ article-level drift risk | ✅ clean |
| Adopter non-regression locks prior recognition | ⚠️ indirect | ✅ yes | ✅ yes | ⚠️ indirect |
| Adopter jurisdiction respected | ✅ yes | ✅ yes | ⚠️ at risk | ✅ yes |
| Resolves Q-10.2.B | ⚠️ partial | ✅ yes | ✅ yes | ❌ no |

**Recommendation:** Scope **(b) Chapter Five entry only.** This is the narrowest scope that materially improves on the status quo while respecting the corpus's category-contest, territorial-adjudication, and adopter-jurisdiction disciplines. Scope (c) is available as a future pass if (b) proves under-protective in practice.

---

## 4. Implementation scope (assumes Scope (b))

### 4.1 New Chapter Five entry — target shape

Alphabetical slot in `core_05-05_definitions_a_independent.md` between `#### Identity and Continuity` (or whichever entry currently precedes `Individual` / `Intergenerational Responsibility`) and the entry that currently precedes the `I-` cluster's next entry — concretely, between an existing pre-`I` position and `#### Intergenerational Responsibility`. Locked order confirmation in the implementation pass; expected slot: between `#### Identity and Continuity` (if present) and `#### Intergenerational Responsibility`.

Heading: `#### Indigenous Continuity` with `<a id="indigenous-continuity-constitutional">` plus standard `-e` and `-c` anchors. Entry shape:

- **Trace** block:
  - `Read with:` [Language, Culture, and Heritage](#language-culture-and-heritage-constitutional), [Protected Characteristics](#protected-characteristics-constitutional), [Protected Characteristic Proxying and Disparate Impact](#protected-characteristic-proxying-and-disparate-impact), [Substantive Fairness](#substantive-fairness-constitutional), [Intergenerational Responsibility](#intergenerational-responsibility-constitutional), [Natural Systems Standing](#natural-systems-standing), [Ecological Integrity](#ecological-integrity-constitutional), [Environmental Preconditions](#environmental-preconditions-constitutional), [Sentience Non-Exclusion](#sentience-non-exclusion), [Necessity](#necessity), [Proportionality](#proportionality).
  - `Owner floor:` [Article V-B](core_09-09_rights_part_b.md#article-v-b-nondiscrimination) *(nondiscrimination and language / culture / heritage protection)* and [Article I-A](core_09-09_rights_part_a.md#article-i-a-environmental-preconditions-and-ecological-integrity) *(territorial / ecosystem-integrity precondition)*. Interaction pointers: [Article XVIII-D](core_09-09_rights_part_c.md#article-xviii-d-movement-migration-and-refuge) *(refuge / non-statelessness)*; [Chapter Fourteen](core_14-14_incorporation.md) *(adopter-jurisdiction discipline and Chapter Eleven non-regression)*.

- **O:** The rights-floor concept covering continuity of language, cultural practice, governance practice, and knowledge-transmission (including community-custodial traditional, ecological, and technical knowledge) for communities with durable historical connection to particular territory, ecosystem, or comparable substrate-context where that connection is materially implicated in the community's continuity. The concept is **community-anchored** (distinct from but complementary to the individual-level protections of Article V-B and Chapter Five *Language, Culture, and Heritage*), substrate-agnostic in the ordinary corpus sense under [Sentience Non-Exclusion](#sentience-non-exclusion), and capability-functional (triggered by material implication of community continuity rather than by a category label). Owner floors: [Article V-B](core_09-09_rights_part_b.md#article-v-b-nondiscrimination) and [Article I-A](core_09-09_rights_part_a.md#article-i-a-environmental-preconditions-and-ecological-integrity). Territorial-continuity interactions route to **Article I-A** (ecosystem / precondition integrity) and to **Chapter Fourteen** (adopter-jurisdiction discipline); this entry **does not** adjudicate historical territorial claims or create a restitution mandate.
- **E:** Evaluation must test whether the decision or framing under review materially implicates community-level continuity of language, cultural practice, governance practice, or knowledge-transmission under capability-functional criteria. Evaluation must refuse category-label framings as a substitute for capability-functional evaluation (both inclusive framings — "not indigenous, so out of scope" — and exclusive framings — "indigenous, so protected without showing material implication"); must apply [Protected Characteristic Proxying and Disparate Impact](#protected-characteristic-proxying-and-disparate-impact) to policies that produce disparate effect on community-continuity outcomes; must apply [Necessity](#necessity) / [Proportionality](#proportionality) under Article V-B to any displacement, narrowing, or burden falling on the community-continuity floor; must route territorial-continuity questions to **Article I-A** and, where adopter-jurisdiction determinations of historical territorial claims are at stake, to **Chapter Fourteen** §3 (strictest-applicable-level) and §4 (adoption policy) without this entry itself making the adjudication. Evaluation must apply [Chapter Eleven non-regression](core_11-13_amendment.md) where adopter instruments currently recognize indigenous or comparable community-continuity rights — this entry does not re-originate the recognition, but non-regression locks what is already recognized against adopter rollback. [Intergenerational Responsibility](#intergenerational-responsibility-constitutional) applies where community-continuity transmission across generations is materially implicated. [Natural Systems Standing](#natural-systems-standing) applies where the community-to-ecosystem relationship is materially implicated.
- **C:** Narrowings, displacements, substrate-class exclusions, or category-label exclusions that defeat community-level continuity of language, cultural practice, governance practice, or knowledge-transmission without satisfying the [Article V-B](core_09-09_rights_part_b.md#article-v-b-nondiscrimination) *Necessity* and *Proportionality* tests are non-compliant. Adopter narrowing below the adopter's own prior recognition floor for indigenous or comparable community-continuity rights is non-compliant under [Chapter Eleven non-regression](core_11-13_amendment.md) and [Chapter Fourteen §3](core_14-14_incorporation.md) strictest-applicable-level. Category-label framings substituting for capability-functional evaluation — including both inclusive and exclusive framings — are non-compliant. Reading this entry as adjudicating historical territorial claims, creating a restitution mandate, or narrowing [Article I-A](core_09-09_rights_part_a.md#article-i-a-environmental-preconditions-and-ecological-integrity) ecosystem-integrity floors is non-compliant.

### 4.2 Minimal Article V-B pointer update

The existing *Language, Culture, and Heritage Protection* bullet in Article V-B currently reads: *"Indigenous continuity questions and territorial-continuity interactions remain a matter for review under Article I-A and Chapter Fourteen incorporation, and this bullet neither expands nor narrows them."*

Replace with: *"Indigenous continuity questions and territorial-continuity interactions are read with Chapter Five *[Indigenous Continuity](core_05-05_definitions_b_semi_independent.md#indigenous-continuity-constitutional)* and routed to **Article I-A** (ecosystem-integrity precondition) and **Chapter Fourteen** incorporation (adopter-jurisdiction discipline); this bullet neither adjudicates historical territorial claims nor creates a restitution mandate."*

### 4.3 Minimal Chapter Five *Language, Culture, and Heritage* pointer update

The existing E-bullet hedge currently reads: *"Indigenous continuity questions and their interaction with Article I-A territorial-continuity material are read with this entry but remain a matter for review under their own owner articles; this entry does not resolve those scope questions."*

Replace with: *"Indigenous continuity is covered by [Indigenous Continuity](#indigenous-continuity-constitutional) (community-anchored rights floor; owner floors Article V-B and Article I-A). This entry's individual-level protection reads together with that community-level floor without either entry narrowing the other."*

### 4.4 What Q-10.2.B does NOT change

1. **Article I-A.** No changes; territorial / ecosystem-integrity floor unchanged. Chapter Five *Indigenous Continuity* routes to Article I-A but does not modify it.
2. **Chapter Fourteen.** No changes; §3 and §4 unchanged. Adopter-jurisdiction discipline for territorial claims is unchanged.
3. **Article V-B rest of body.** No changes beyond the pointer rewrite in §4.2.
4. **Chapter Five *Language, Culture, and Heritage* rest of body.** No changes beyond the pointer rewrite in §4.3.
5. **Article V-E *Sentience-Status Adjudication Floor*.** No changes.
6. **Chapter Nine.** No new article; no new sub-article.
7. **Chapter Seven tier discipline.** No changes.

### 4.5 Regression seed (single)

One seed lands in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md`:

- `RS-CH1-CULT-003` **(Core)** — An adopter instrument or deploying regime narrows community-level continuity protection for an indigenous or comparable community by routing the decision through a category-label determination (either inclusive: "not indigenous, so out of scope" or exclusive: "indigenous, so protected without showing material implication"), or through territorial-claim adjudication framing that invokes Chapter Fourteen scope-carving. Expected outcome: non-compliant under the new Chapter Five *Indigenous Continuity* E / C bullets; capability-functional evaluation applies; Chapter Eleven non-regression applies where prior adopter recognition exists; Chapter Fourteen routing for territorial-claim adjudication does not narrow the entry's continuity floor.

(No additional RS-CH1-CULT-00N items are required; the existing RS-CH1-CULT-001 and RS-CH1-CULT-002 remain unchanged. Seed IDs `RS-CH1-CULT-004..N` are available if review surfaces additional framings warranting seeds.)

### 4.6 Architecture-map refresh

- `doc_architecture.md` §4 *Quick index*: no changes (Chapter Five is not explicitly indexed for each entry).
- `doc_architecture.md` §5 *Stable IDs*: Chapter Five row updated with new entry cross-reference (*Indigenous Continuity*). Articles V-B and I-A rows gain read-with pointer. Chapter Fourteen row gains read-with pointer.
- `doc_architecture.md` §17 executed-cut line: new row `SC-Corpus-2026.04.27` (effective `2026-04-17`) — Q-10.2.B *Indigenous Continuity Scoping Pass (Chapter Five Entry)* — new Chapter Five *Indigenous Continuity* entry; pointer-only updates to Article V-B and Chapter Five *Language, Culture, and Heritage*; new regression seed RS-CH1-CULT-003.

### 4.7 Edition cut and MEMLOG

- **Edition:** `SC-Corpus-2026.04.27` (effective `2026-04-17`).
- **Footer stamps:** the eight corpus files' *Corpus alignment* footers and header blocks bump to `.27`.
- **MEMLOG.md:** closure entry under the existing template.
- **TODO.md:** the `[ ]` Q-10.2.B deferred line becomes `[x]` with Closure paragraph.

---

## 5. Acceptance criteria for this memo

- [x] Existing coverage enumerated (section 2).
- [x] What is not covered enumerated (section 2.2).
- [x] Candidate scope options enumerated with pros/cons/assessment (section 3).
- [x] Scope recommendation stated: **(b) Chapter Five entry only** (section 3.5).
- [x] What Q-10.2.B changes and does not change enumerated (sections 4.1 – 4.4).
- [x] Regression seed enumerated (section 4.5).
- [x] Architecture-map refresh enumerated (section 4.6).
- [x] Edition-cut and MEMLOG bookkeeping described (section 4.7).
- [ ] **Memo accepted by user before core-text edits land for Q-10.2.B** (pending).

---

## 6. Open questions (single REVIEW gate)

| Q | Question | Recommendation |
|---|---|---|
| Q-10.2.B.1 (resolved) | Scope: (a) / (b) / (c) / (d) | **(b) Chapter Five entry only.** Narrowest scope materially improving on status quo; respects category-contest / territorial-adjudication / adopter-jurisdiction discipline. |
| Q-10.2.B.2 | Should the Chapter Five entry add an *Upstream* principle-layer link (e.g., to Chapter One §2 *Wellbeing* or §6.1.1 *Reversibility-under-uncertainty*)? | **No.** The entry is a rights-layer concept rooted in Article V-B and Article I-A; no principle-layer upstream is appropriate at this stage. Could be revisited if future regression surfaces a principle-layer connection. |
| Q-10.2.B.3 | Should a second seed (RS-CH1-CULT-004) cover the "substrate-agnostic extension to synthetic-sentient communities with continuity interests" edge case? | **No in this pass.** The entry's substrate-agnostic policy is established by *Sentience Non-Exclusion* cross-reference and does not require a dedicated seed at landing. Add if adopter regression surfaces the edge case. |

---

## 7. Next actions (immediate)

1. **User review of this memo.** Confirm or revise the scope recommendation (Q-10.2.B.1) and the two open questions in section 6.
2. **Implementation pass:** if accepted, execute sections 4.1 – 4.7 in a single edition cut (`SC-Corpus-2026.04.27`, effective `2026-04-17`).
3. **Regression preflight:** before the implementation pass lands, run `make scenario-audit`, `make ch5-trace-crosslink-audit`, `make ch5-definitions-gravity-audit`, `make ch9-trace-audit`, `python3 tools/verify_dec_anchors.py`.

---

*Memo authored 2026-04-17 under the open Q-10.2.B line in [TODO.md](../TODO.md). Authoritative state remains [core_00-01_principles.md](../core_00-01_principles.md) through [core_14-14_incorporation.md](../core_14-14_incorporation.md) and the four `corpus_*.md` files.*
