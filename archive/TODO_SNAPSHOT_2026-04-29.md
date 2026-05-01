# TODO

**2026-04-26 archive:** A complete pre-slim copy of this file (closed items, long narratives, maintenance text, and structural-sync appendices) is in [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md). Historical closed subsections such as *External Framework and Embedding Gaps* and *Structural synchronization* (including patch-level edition notes) live there. **Working snapshot** of this file as of the same archive pass: [archive/TODO_SNAPSHOT_2026-04-26.md](archive/TODO_SNAPSHOT_2026-04-26.md).

## Editor Checklist (Pre-Review / Pre-Merge)

- [x] Filename convention check: use underscore-style canonical names, no spaces:
  - `core_00-01_principles.md` … `core_14-14_incorporation.md` (per [README.md](README.md) chapter list)
  - `corpus_joint_structure.md`
  - `corpus_systems.md`
  - `corpus_institutions.md`
  - `corpus_forum.md`
- [x] Corpus edits happen in those canonical Markdown files only (no parallel `.txt` layer).
- [x] Reference integrity check: update prose, links, and script references in the same change when filenames move.
- [x] Regression suite check: update and run `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` for any material constitutional change. **(Suspended 2026-04-17:** scenarios file removed for token-cost reduction; see *P1 — Reinstate regression scenarios and evidence tree* below. `tools/scenario_audit.py` reports `SUSPENDED` until reinstated.**)**
- [x] Single-home discipline check: new term definitions must follow `doc_architecture.md` section 4 owner rules.
- [x] Layered framing check: apply `doc_architecture.md` section 4 flow (`definitions -> principles -> articles -> core -> joint structure -> institutions/systems/forum`) and pointer-first restatement discipline.

## Sentient Constitution chapter map (2026-04-12)

**`core_definitions.md`:** **Ch 2**–**Ch 5** (definition structure through Interdependent and Clustered definitions).

**Numbered `core_*` (integrated instrument):** **Ch 1** `core_00-01_principles.md`; **Ch 6** `core_06-06_standing_classification.md` and `core_06-06_standing_integration.md`; **Ch 7** `core_07-07_misconduct.md`; **Ch 8** `core_08-08_forum.md` (forums and jurisdiction); **Ch 9** `core_09-09_rights_part_*.md` foundational rights (Articles **I–XXV**); **Ch 10** `core_10-10_governance.md`; **Ch 14** `core_14-14_incorporation.md` incorporation bridge. (Legacy `core_constitution.md` is a compatibility label only—use the chapter files as canonical.)

**`core_amendment.md`:** **Ch 11** non-regression and substantive amendment validity; **Ch 12** expansion, supremacy, and external legal orders; **Ch 13** amendment, ratification, and procedural validity.

Older closure notes may use earlier maps—translate using this list or [doc_architecture.md](doc_architecture.md) section **5**.

## Open backlog (corpus / governance)

**Status:** Edition closures, world-assessment follow-ups, D/E/C and productivity batches, and other **closed** work through 2026-04-25 remain in [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md). This file lists **open `[ ]` items** only.

### P1 — Regression and evidence (2026-04-17 suspension)

- [ ] **P1 — Reinstate regression scenarios and evidence tree (2026-04-17 suspension):** restore `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` (matrix + section 10.5 SCORING-v1 snapshot) and the `evidence/<YYYY-MM-DD>/` tree so that matrix integrity, snapshot validation, and dated artifact recording resume. Until then, the regression-scenario gate is paused per the user's 2026-04-17 token-reduction request.
  **Acceptance checks:**
  - (a) `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` present at the repository root with matrix (section **4**) and SCORING-v1 snapshot (section **10.5**) populated
  - (b) `make scenario-audit` switches off the `SUSPENDED` path in `tools/scenario_audit.py` and returns the live PASS / FAIL block (matrix counts + section 10.5 snapshot)
  - (c) `evidence/` directory restored with at least the next dated subdirectory used for any in-flight verification artifact
  - (d) `.cursor/rules/testing.mdc` *Regression suite suspended (2026-04-17)* section retired and the during-suspension reporting clause removed; baseline-verification bullets restored to their pre-suspension wording
  - (e) the `Editor Checklist` *Regression suite check* line and the dependent items below have their *(Suspended 2026-04-17)* annotations removed; any seed-worthy observations queued during the suspension are landed as `RS-*` rows

- [ ] **P1 — Humanity/Individual stress-pack regression integration (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`):** **[Blocked on regression-scenarios reinstatement (2026-04-17 suspension); see P1 — Reinstate regression scenarios and evidence tree above.]** complete first-pass validation cycle for the new 2026-04-10 stress scenarios added in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` section `7E` and align outcome tracking to current chapter-boundary guardrails.
  **Acceptance checks:**
  - (a) matrix entries for `RS-HUM-001..015`, `RS-IND-001..015`, and `RS-XD-001..005` are advanced from `draft` only after tabletop pass evidence exists
  - (b) boundary assertions are explicitly validated for **Chapters Eleven–Thirteen** vs Chapter **Six** classification authority (`RS-XD-001`) and rights-layer process-creep prevention (`RS-XD-002`)
  - (c) incorporation custody chain anti-drift safeguards are validated with edition/adoption traceability artifacts (`RS-XD-003`)
  - (d) emergency anti-normalization and evidence-gate controls are exercised (`RS-XD-004`, `RS-XD-005`)
  - (e) verification artifacts are published under `evidence/<YYYY-MM-DD>/` with run IDs linked in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` *(both paths currently absent under the 2026-04-17 suspension; reinstatement is a prerequisite)*

### P3 — Plain-language gloss and readability audit

- [x] **P3 — Plain-language gloss placement audit extension + Co-Gloss Registry follow-on:** **Closed (2026-04-26).** (b) **Co-Gloss registry** in [doc_architecture.md](doc_architecture.md) *Plain-Language Vocabulary Guardrails*; (b) **Chapter Five** *Plain-language reader companion* lines at **Graduated Capability**, **Instantiation Consent**, and **Parent-System Relationship** point to the registry. (a) **Subarticle plain-terms gate** — [tools/subarticle_gloss_audit.py](tools/subarticle_gloss_audit.py) and `make subarticle-gloss-audit` (not bundled into `make regression` / `regression-full` while P1 scenarios remain suspended; add to `regression-full` when reinstating if desired).
  **Residual:** optional merge of the same check into [tools/readability_audit.py](tools/readability_audit.py) as a convenience wrapper; the standalone tool is authoritative.

### Chapter Five — additional clustered definition candidates (2026-04-26)

**Context:** Evaluation pass on [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) — groups of interdependent entries already cross-wired in traces or O/E/C text that could become formal `§2` *Clustered Definitions* (numbered head, *Clustered Definitions A–Z* directory, `cluster component` lines on member stubs). The two **integration** items are partially authored but not fully wired like existing `2.3`–`2.20` clusters.

- [ ] **P2 — Emergency and contingency cluster:** *Emergency and Contingency*; *Constitutional Emergency and Contingency*; *Stakeholder Emergency and Contingency*; *Emergency Pre-Deliberation Action (Binding Collective Choice)*. **Partial 2026-04-27:** *Force Majeure* was instead added as a component of the Chapter Five §3.3 accountability cluster, where excuse claims must remain traceable, contestable, and auditable.

- [x] **P2 — Forum families and dispute-routing cluster:** *Forum Family, Constitutional*; *… Environment*; *… Institutional*; *… Integrity*; *… Sentient*; *… Technical*; read with *Adjudication and Dispute Resolution* and Chapter Eight owner layers. **Done 2026-04-27:** added Chapter Five §3.16 *Forum Families and Dispute Routing* and re-homed the six forum-family O/E/C entries there with existing anchors preserved.

- [ ] **P2 — Constitutional contract / authorization layer cluster:** *Foundational Constitutional Choice*; *Constitutional Contract Layer* (distinct from *Binding Stakeholder Choice* / ordinary stakeholder weighting).

- [ ] **P2 — Proportionality, necessity, feasibility, and burden / efficiency cluster:** *Proportionality*; *Necessity*; *Feasibility*; *Avoidable Burden*; *Burden-Reduction Duty*; *Constitutional Efficiency*; *Harm Minimization (Tradeoff Selection)*; *Productive Capacity*.

- [ ] **P2 — Nondiscrimination, protected status, and intimate-signal pathways cluster:** *Protected Characteristics*; *Protected Characteristic Proxying and Disparate Impact*; *Protected Intimate-Signal Gating*; *Protected Commercial Sexual Services Status and Article X-C Circumvention*; natural extensions: *Dignity and Equal Moral Standing*; *Anti-Displacement Floor*; *Tenure Security* with *Essential-Environment Non-Commodification*.

- [ ] **P2 — Redress, restoration, and refuge cluster:** *Adjudication and Dispute Resolution*; *Redress and Remediation*; *Restorative Justice*; *Review and Correction Duty*; *Refuge from Non-Compliance* (often *Irreversible Sanction* and *Procedural Fairness* in the same evaluation orbit).

- [ ] **P2 — Use of force, weapons, and combatant / targeting rules cluster:** *Use of Force*; *Autonomous Lethal System*; *Autonomous Coercion Tool*; *Weapons of Mass Harm*; *Combatant / Non-Combatant Distinction*.

- [ ] **P2 — Contingent claims, event-contract markets, and games of chance cluster:** *Contingent Claim*; *Event-Contract Market*; *Game of Chance* (complements *Capture, Resolution Integrity, and Anti-Capture* without duplicating the resolution-capture head).

- [ ] **P2 — Dependency, market structure, and exit cluster:** *Dependency*; *Systemic Lock-In*; *Concentration Threshold*; *Decentralization* (and *Incentive Alignment* where it functions as the hub).

- [ ] **P2 — Info-sphere, expression, and press cluster:** *Info-Sphere*; *Expression*; *Press and Journalistic Activity*; *Good Faith* where publication is in scope.

- [ ] **P2 — Resilience and catastrophic / systemic harm cluster:** *Safety (Constraint)*; *Reversibility*; *Self-Healing*; *Cascading Failure*; *Existential Risk*; *Environmental Preconditions*; *Wellbeing* (safety / continuity stack).

- [x] **P2 — Innovation, attribution, and anti-enclosure cluster:** *Innovation Reward and Anti-Enclosure*; *Creative Work Attribution*; *Anti-Displacement Floor*. **Closed 2026-04-27:** Landed as Chapter Five [§3.12 *Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement*](core_05-05_definitions_c_dependent_clusters.md#creative-work-training-data-attribution-compensation-and-anti-displacement-cluster) (joint invocation; members include *Training-Data Use*, *Creative Work Attribution*, *Anti-Displacement Floor*, *Fair Compensation*, *Productive Capacity*, and *Innovation Reward and Anti-Enclosure* where implicated). [doc_architecture.md](doc_architecture.md) Article **VIII** map row and Article **VIII-D** *Trace* in [core_09-09_rights_part_b.md](core_09-09_rights_part_b.md) point here.

- [ ] **P2 — Family, care, reproduction, and non-separation cluster:** *Family and Care Relationships*; *Reproductive Autonomy*; *Non-Separation*; *Parent-System Relationship*; *Instantiation Consent* (overlaps *Sentience Status, Subclasses, and Evaluation* for some members).

- [ ] **P2 — Indigenous, heritage, and natural standing cluster:** *Indigenous Continuity*; *Language, Culture, and Heritage*; *Natural Systems Standing*; *Intergenerational Responsibility*.

- [ ] **P2 — Systemic materiality and classification cluster:** *Material Impact*; *Materiality Determination*; *Classification-Scaled Governance*; *Oversight*; *Capability Requirement*.

- [ ] **P2 — Trust, trustworthiness, and misleading reliance (formal §2 integration):** *Trust*; *Trustworthiness*; *Trust Degradation and Misleading Reliance* — the last entry already uses internal "trust degradation cluster" sub-bullets and cites `§2` rules; add a numbered `§2` cluster head and directory / stub lines consistent with e.g. Truth / Epistemic.

- [ ] **P2 — Publication and high-impact communication (formal §2 integration):** the block titled *Publication and High-Impact Communication* at the tail of [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) (truthfulness, protected data, high-impact / systemic-harm publication, security-sensitive disclosure) — promote into numbered `§2`, *Clustered Definitions A–Z*, and interdependent directory as needed; today it reads as a joint-satisfaction head without full cluster wiring.

### Chapter Five definition audit (2026-04-26)

**Method:** Systematic pass over Chapter Five in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) (reader guidance, `####` / clustered / `#####` owner entries, and cross-corpus checks against [README.md](README.md) chapter map). Automated checks: `make ch5-definitions-gravity-audit` and `make ch5-trace-crosslink-audit` **PASS**; `make ch5-dec-widget-audit` **PASS**; `make ch5-entry-format-audit` **FAIL** (format items below). Full manual review of every definition line-by-line against the full corpus was not completed in one pass; the items below are **confirmed** misalignments or follow-ups.

- [ ] **P2 — Chapter Five unified definition index widget:** replace the current Chapter Five index / directory widget that is segregated by definition type with one unified A-Z list of terms. The user-facing goal is simple lookup: readers should be able to find any definition from one term list without first knowing whether it is independent, semi-independent, or cluster-dependent. Preserve canonical-home, cluster-component, and O/E/C routing metadata in the target entries or trace blocks rather than using the index buckets as the primary navigation model.
  **Acceptance checks:**
  - (a) [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) presents a single Chapter Five A-Z term list covering independent, semi-independent, and dependent-cluster terms
  - (b) each term links to its canonical O/E/C home or stable cluster/member anchor
  - (c) definition type remains available where needed as metadata, not as the top-level lookup structure
  - (d) any audit scripts or directory-generation scripts that assume separate independent / semi-independent / dependent lists are updated

- [ ] **P2 — Chapter Five stale-link and anchor repair after semi-independent rework:** repair stale Chapter One, Part A directory, and Part C cluster-member links created by the semi-independent definition rework. Known examples include [core_00-01_principles.md](core_00-01_principles.md) D/E/C rows for terms such as *Meaningful Agency*, Part A directory links to moved semi-independent terms, and Part C cluster-member links that currently point to missing anchors such as `#bodily-integrity-constitutional`, `#training-data-use-constitutional`, `#non-statelessness`, and `#educational-agency-constitutional`.
  **Acceptance checks:**
  - (a) all Chapter One D/E/C rows targeting Chapter Five resolve to live anchors
  - (b) the Chapter Five unified index resolves every listed term to a live canonical target
  - (c) Part C cluster-member links resolve either to Part B standalone entries or to local Part C member anchors
  - (d) `tools/ch5_structure_audit.py --check-cluster-member-anchors` passes for Part C, or an updated equivalent passes across the split files

- [ ] **P2 — Canonical-home decision pass for moved / cluster-only terms:** decide whether terms affected by the Chapter Five split have standalone Part B O/E/C homes, Part C member homes, or cluster-only routing. Terms needing explicit home confirmation include *Meaningful Agency*, *Expression*, *Educational Agency*, *Reproductive Autonomy*, *Privacy (Informational)*, *Protected Internal-State Boundary*, *Surveillance Boundary*, *Training-Data Use*, *Ecological Integrity*, *Sustainability*, *Intergenerational Responsibility*, *Substantive Fairness*, and *Procedural Fairness*.
  **Acceptance checks:**
  - (a) each affected term has exactly one canonical O/E/C home or is clearly marked as cluster-only
  - (b) Chapter One D/E/C widgets and Part A index links use that canonical home
  - (c) cluster heads state when standalone entries may operate alone and when joint satisfaction applies

- [ ] **P2 — Reciprocal Chapter One principle traces for high-load semi-independent definitions:** add explicit `Downstream: Principles` lines to semi-independent definitions that now carry principle-operationalizing work but lack reciprocal Chapter One backlinks. Priority terms: *Material*, *Material Impact*, *Material Risk*, *Materiality Determination*, *Stakeholder*, *Stakeholder Participation Weight*, *Environmental Preconditions*, *Ecological Footprint*, *Leisure and Rest*, *Tenure Security*, *Safe Conditions*, *Force Majeure*, *Emergency and Contingency*, *Constitutional Emergency and Contingency*, *Systemic Lock-In*, *Concentration Threshold*, and *Burden-Reduction Duty*.
  **Acceptance checks:**
  - (a) each priority entry includes a `Trace` block where absent
  - (b) principle backlinks target the specific Chapter One sections that invoke or operationally depend on the definition
  - (c) backlinks are reciprocal with Chapter One D/E/C widgets where those widgets already name the term

- [ ] **P2 — Normalize Chapter Five Trace block ordering:** standardize Chapter Five `Trace` blocks so readers and audit tools can scan the same metadata categories in the same order. Preferred order: `Upstream: Principles`, `Downstream: Principles`, `Owner floor`, `Cluster component`, `Read with`, and `Not narrowed here`.
  **Acceptance checks:**
  - (a) new and revised Chapter Five trace blocks follow the shared ordering
  - (b) existing materially important trace blocks are normalized during the stale-link and reciprocal-trace passes
  - (c) navigation metadata remains inside local `Trace` / `<details>` blocks rather than operative definition prose

- [ ] **P2 — Preserve cluster heads as integration maps, not substitutes for entry traces:** review Part C cluster heads and member entries to ensure cluster heads state admission scope, joint invocation, and anti-bypass rules, while individual definitions carry their own principle / owner / read-with trace where Chapter One or Chapter Nine directly invokes them.
  **Acceptance checks:**
  - (a) cluster heads answer when definitions must be satisfied together
  - (b) individual definitions answer which principles, rights floors, and companion definitions they operationalize
  - (c) direct Chapter One invocations do not rely solely on a cluster-head trace unless the term is expressly cluster-only

- [ ] **P2 — Cross-file Chapter Five anchor audit:** add or extend an audit that validates every Chapter One DEC / D/E/C link, every Chapter Five unified-index link, every Part C cluster-member link, and every in-body Chapter Five cross-link against actual anchors across Parts A, B, and C.
  **Acceptance checks:**
  - (a) audit covers `core_00-01_principles.md` plus all three Chapter Five files
  - (b) audit understands explicit `<a id="..."></a>` anchors and generated heading slugs used in the corpus
  - (c) audit is wired into the relevant `make` target or documented as the required verification command for Chapter Five link work

- [x] **P3 — Chapter Five reader guidance vs corpus chapter map:** **Closed (2026-04-26):** the non-operative blockquote in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) now points to **Chapter One** (values/direction), **Chapters Two through Four** (definition structure and verification mechanics), and **Chapter Nine** (foundational **rights** floor), with an explicit note that Chapters **Six** and **Seven** have separate reading paths and are not substitutes for the rights floor or for Ch2–4 mechanics.

- [x] **P3 — Adversarial, Scaled, and Exploited Conditions — fragment id mismatch:** **Closed (2026-04-26):** in-file `](#adversarial-scaled-and-exploited-conditions-constitutional)` targets were consolidated to `](#adversarial-scaled-and-exploited-conditions)` to match the `####` entry slug and existing `-e` / `-c` anchors; the redundant `…-constitutional` O-anchor experiment was reverted so `make ch5-dec-widget-audit` remains green.

- [x] **P3 — ch5-entry-format-audit outstanding (wiring, not definition substance):** **Closed (2026-04-26):** *Autonomous Coercion Tool* and *Autonomous Lethal System* use `##### In plain terms: *…*`; *Sentient (Composite)* uses an HTML comment separator before the `- O:` list; *Assembly* and *Review and Correction Duty* have `---` before trace-bearing `####` titles; reader guidance `</details>` is followed by a single `<br>`. `make ch5-entry-format-audit` is **PASS**.

- [x] **P3 — Article XVIII-D vs Article XIX-D (label alignment):** **Closed (2026-04-26).** Display text and implementation notes now use **Article XVIII-D** where the target anchor is `article-xviii-d-movement-migration-and-refuge` in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) (*Indigenous Continuity* interaction line; *Movement and Relocation*; *Non-Statelessness*; *Refuge from Non-Compliance*), [corpus_institutions.md](corpus_institutions.md) CI-22, and [implementation/DEC_INDIGENOUS_CONTINUITY_SCOPE_2026-04-17.md](implementation/DEC_INDIGENOUS_CONTINUITY_SCOPE_2026-04-17.md). **Article XIX** (portability / interoperability) remains a distinct family from movement / migration / refuge.

### Chapter 00 (preamble) hand-review — definitions and cross-uses (2026-04-26)

**Scope:** [core_00-01_principles.md](core_00-01_principles.md) `## CHAPTER 00: PREAMBLE / FOUNDATIONAL REQUIREMENTS` (lines 6–32), treated as a single chapter. **Method:** list every layer name, near-definition, and restated norm in the preamble; compare to [Chapter Five](core_05-05_definitions_a_independent.md) owner entries and [README.md](README.md) chapter map; check **internal** Chapter 00 uses (e.g. generic *participation* vs the named *Stakeholder System Participation* layer; CCL lead-in vs the canonical CCL *O* block).

**Implemented (2026-04-26):** [core_00-01_principles.md](core_00-01_principles.md) Chapter 00 — (1) CCL lead-in now includes **scope and** durable terms; (2) line 10 ties “participation” to governance/operation of those systems, adds a second sentence distinguishing the **general** triad from the two formal **layers**, and tightens the anti-bypass sentence to “stakeholder-level participation in already-authorized systems” plus a single link for duties under the SSP layer; (3) first-mention **Constitutional Contract Layer** and **Stakeholder System Participation** link to `#constitutional-contract-layer` and `#stakeholder-status-and-participation-weight-cluster`.

- [x] **P3 — Chapter 00 CCL one-line summary vs Chapter Five *Constitutional Contract Layer* O lead:** **Closed (2026-04-26):** “under what **scope and** durable terms” added in Chapter 00.

- [x] **P3 — Chapter 00 first paragraph “participation” vs Stakeholder System Participation layer (reader disambiguation):** **Closed (2026-04-26):** governance/operation framing + “general” triad vs formal “layers” bridge sentence + anti-bypass wording (“stakeholder-level participation in already-authorized systems” / duties under the SSP layer).

- [x] **P3 — Chapter 00 optional single-home / pointer links on first layer names:** **Closed (2026-04-26):** first-mention CCL and SSP link to `#constitutional-contract-layer` and `#stakeholder-status-and-participation-weight-cluster`.

**Verified aligned (no new TODO):** Reading-order list (Ch1 → Ch2–4 → Ch5 definitional, not rights floor → Ch6–8 classification / misconduct / forums → Ch9 rights → Ch10 CCL / authorization / stewardship) matches [README.md](README.md) fast locator; **Constitutional Contract Layer** and **Stakeholder System Participation** substance matches *Governance* layering and [architecture_primer.md](architecture_primer.md) section 1; Ch10 bullet correctly lists the CCL next to “legitimacy, authorization, and stewardship” per README; *Axes I and II* matches the standing model; *tiered* misconduct matches Chapter Seven framing; *productive capacity* in the preamble is consistent with the Chapter Five *Productive Capacity* / Chapter One §5.1 downstream arc (preamble is plain-language, not a duplicate definition); line 10 *truthfulness* vs line 14 *Truth* read as colloquial vs named constraint, not a clash; “ecological wellbeing of planet Earth” has no conflicting operative definition elsewhere in `core_*.md` (related rights/definitions: *Environmental Preconditions* / *Ecological Integrity* in Chapter Five and Article I-A, for optional future gloss only).

### Chapter One hand-review — definitions and cross-uses (2026-04-26)

**Scope:** [core_00-01_principles.md](core_00-01_principles.md) `## CHAPTER 01: PRINCIPLES AND CONSTRAINTS` (not Chapter 00 preamble), cross-checked against Chapter Nine rights text, [README.md](README.md) chapter map, and Chapter Five definition anchors where Chapter One D/E/C widgets or traces link to `core_05-05_definitions_a_independent.md`. **Method:** full read of the chapter’s outline and every trace / D/E/C block; `rg` on `core_00-01_principles.md` for `core_09-09`, `article-`, and duplicate Chapter Five link patterns; spot-verification of article headings in `core_09-09_rights_part_*.md`. **Not exhaustively re-verified:** all 200+ `core_05-05` pointer targets one-by-one (assumed valid where the dec-widget and prior edition passes hold); Chapter One’s inline Chapter Five O/E/C links use the same fragments as the Chapter Five D/E/C audit pattern.

- [x] **P0 — Chapter One rights-article display/anchor mis-pairs (broken or misleading links):** **Closed (2026-04-26)** in [core_00-01_principles.md](core_00-01_principles.md). Sub-items (formerly mis-pairs):
  - [x] **§2 Wellbeing** trace (line 114): display text is **Article XVIII-B**; link `#article-xviii-b-…` unchanged.
  - [x] **§3.3** trace and body (lines 307, 344, 359): [Article VI: Right to Sentient-Centered Education](core_09-09_rights_part_b.md#article-vi-right-to-sentient-centered-education); [Article XV: Audit, Transparency, and Independent Verification](core_09-09_rights_part_c.md#article-xv-audit-transparency-and-independent-verification) (both fragments and Part files corrected).
  - [x] **§8** trace (line 1220): display and links updated to **Article XIV-B**, **Article XVIII-B**, and **Article XXII-A** to match the existing fragment targets.

- [x] **P3 — Chapter One plain-language “people” (optional vocabulary pass):** **Closed (2026-04-26).** *In plain terms* lines at [core_00-01_principles.md](core_00-01_principles.md) (wellbeing, distributed understanding, §7.2.5 contingent claims) rephrased to **sentients** / **affected** **parties** / **participants** per the lexical gate.

- [ ] **P3 — Chapter One D/E/C → Chapter Five pointers (integrity spot-check):** Chapter One’s definition widgets generally mirror Chapter Five O/E/C anchors (*Proportionality*, *Necessity*, *Materiality* / `#materiality-determination`, *Harm*, *Foreseeability* as `#foreseeability-diligence`, *Trust* cluster, *Incentive Alignment* `#incentive-alignment`, etc.). **Follow-on:** if a project-wide `make reference-audit` or link-checker is added, include `core_00-01_principles.md` in the same gate as Chapter Five for internal `core_05-05` fragments.

**Verified aligned (no new TODO):** *Interpretive constraints* (Authority Stack pointer to Chapter Five; conflict procedure vs Chapter Fourteen §2); *§2.1 Fairness* Article XVIII-B link; *§6* and *§7* traces listing Article XII–XXIII where spot-checked; *§5.1* Article IV and ecological pointers; *Chapter One §7.2.5* downstream to Chapter Five *Contingent Claim* / *Event-Contract Market* (present in those definitions). **Out of hand-review scope for this pass:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) back-links into Chapter One §3.3 (not re-audited line by line).

### Chapter Two hand-review — definitions and cross-uses (2026-04-26)

**Scope:** `## CHAPTER TWO: DEFINITION STRUCTURE AND COMPONENT REQUIREMENTS` in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) through the line before `## CHAPTER THREE` (the mechanics file’s Chapters **Three and Four** are out of this Chapter Two–only pass). **Method:** Enumerate every explicit `core_05-05` link, every plain-language name-drop of a Chapter Five interdependent or clustered head, and every operative tie to the **reasonably foreseeable** / **Foreseeability** rule; for each, compare to the owning entry and anchors in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md). **Coverage of “every” Chapter Five definition:** Chapter Two contains **no** substantive uses of the vast majority of Chapter Five `####` entries; a negative scan (no informal competing gloss for e.g. *Harm*, *Proportionality*, *Truth*, *Stakeholder* in the Chapter Two block) is part of the pass.

- [x] **P3 — Chapter Two §2.2 “this chapter’s compliance pipeline” antecedent error:** **Closed (2026-04-26):** in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) Chapter Two, §2.2 (*Evaluative Components*), the sentence incorrectly referred to *this chapter’s* (Two’s) compliance pipeline while pointing at **Chapter Four, section 1**; it now reads that evaluation requirements in Chapters Two and Three are **enforced under Chapter Four, section 1** (with Ch4s2 for evidence), matching the correct chapter.

- [x] **P3 — Chapter Two §1 *Supremacy and Enforceability* name-only (optional link):** **Closed (2026-04-26):** *Purpose and Role* links [Supremacy and Enforceability](core_05-05_definitions_b_semi_independent.md#supremacy-and-enforceability) in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md).

- [x] **P3 — “Reasonably foreseeable” pointer precision vs `##### Reasonably Foreseeable` (optional):** **Closed (2026-04-26):** Chapter Two §2 and Chapter Four §2.1 *Read with* lines include [Reasonably Foreseeable](core_05-05_definitions_c_dependent_clusters.md#reasonably-foreseeable); Chapter Five adds explicit `<a id="reasonably-foreseeable"></a>` before that sub-head.

**Verified aligned (no new TODO):** `#chapter-five-foundational-definitions` targets `## CHAPTER FIVE: FOUNDATIONAL DEFINITIONS`; `#1-interdependent-definitions` matches `### 1. Independent Definitions`; **Foreseeability Diligence** D/E/C links `#foreseeability-diligence` (shared with the O line placement), `#foreseeability-diligence-e`, and `#foreseeability-diligence-c` resolve to the O/E/C lines under that head in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md). Foreseeability’s operative home is **Chapter Five, section 3 — Dependent clusters** (Truth and Epistemic Integrity; Foreseeability Diligence), read together with **§3.1** joint-invocation law. All other Chapter Five §§1–3 definition entries: **no** use in the Chapter Two block—no conflicting lay definitions detected.

**Note (existing backlog, not duplicate):** Chapter Five reader guidance “Chapters One and **Seven**” vs rights-floor / README map is already under *Chapter Five definition audit*; it does not appear in Chapter Two.

### Chapters Three and Four (definition mechanics) hand-review — definitions and cross-uses (2026-04-26)

**Scope:** `## CHAPTER THREE` and `## CHAPTER FOUR` in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) (through the end of Chapter Four, before the closing `---`). **Method:** same as the Chapter Two pass—every `core_05-05_definitions_a_independent.md` link, Chapter Five name-drop, and colloquial use of a defined term; negative scan for stray gloss of other Chapter Five entries. **Chapter Three** has **no** direct `core_05-05` pointer in traces (definition integrity and evasion are mechanics-local; the §1 *Read with* uses Chapter One §3.2 for the truth operationalization at the principles layer, which is consistent with Chapter Five *Truth* / *Epistemic* as the single-home **canonical** layer via the instrument read as a whole—no competing Chapter Five paraphrase in the Chapter Three block).

- [x] **P0 — Chapter Four §6 *Verification Accessibility* — Article XV fragment (Part C):** **Closed (2026-04-26):** the plain-language cross-reference at [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) *Verification Accessibility* uses the parent article fragment `#article-xv-audit-transparency-and-independent-verification`. The matching Chapter One P0 *Article XV* display/anchor alignment in [core_00-01_principles.md](core_00-01_principles.md) is **closed** under the Chapter One hand-review *P0 — rights-article display/anchor mis-pairs* item.

- [x] **P3 — Chapter Four §5.1 *Cryptographic protection* — optional inline links for Truth / Safety:** **Closed (2026-04-26):** narrative sentence links [Truth (Constitutional Constraint)] and [Safety (Constraint)] in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) §5.1.

- [x] **P3 — Chapter Five *Truth* / *Epistemic Integrity* D/E/C “O” targets (informational, cross-file):** **No change required (2026-04-26):** D/E/C widgets remain aligned to stub/cluster structure; *Science-informed* and §5.1 mechanics prose now link Truth/Safety by name in running text (see item above). **Re-verify:** if Chapter Five later adds a dedicated O anchor for cluster-body Truth, update widgets in a single follow-on pass.

**Verified aligned (no new TODO):** All **Foreseeability Diligence** traces and D/E/C repeats in Chapter Four (§2.1, §4, §5, §5 intro, §6) use `#foreseeability-diligence` / `-e` / `-c` consistently with Chapter Five. **Reasonably foreseeable** sub-bullets reference Chapter Five, section 3 — Dependent clusters (Truth and Epistemic Integrity cluster; Foreseeability Diligence) (Foreseeability) in line with Chapter Two. **Truth**, **Epistemic Integrity** (§2.5) and **Truth**, **Safety** (§5.1) **E**/**C** links (`#truth-constitutional-constraint-e` / `-c`, `#epistemic-integrity-e` / `-c`, `#safety-constraint` / `-e` / `-c`) resolve to the O/E/C material in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) (with stub/cluster architecture for Truth/Epistemic **O** as above). **Contestability** at `#contestability` in §6 is consistent with the `#### Contestability` §1 Independent Definition entry. **Proportionality**-adjacent phrasing in Chapter Four (e.g. “proportionality constraints” in §2.1) is not claimed as the capital-*P* [Proportionality](core_05-05_definitions_c_dependent_clusters.md#proportionality) definition—ordinary scaling language, not a mis-definition. All other Chapter Five `####` definitions: **no** substantive use in the Chapter Three or Chapter Four blocks beyond the list above; no spurious redefinitions detected.

**Note (existing backlog, not duplicate):** *Article XVIII-D / XIX-D* and Chapter Five *reader guidance* Ch1/Ch7 items are tracked elsewhere; they do not surface in the Chapter Three or Chapter Four mechanics text.

### Chapter Six hand-review — Chapter Five definitions and cross-uses (2026-04-26)

**Scope:** [core_06-06_standing_classification.md](core_06-06_standing_classification.md) and [core_06-06_standing_integration.md](core_06-06_standing_integration.md), cross-checked against every `####` / cluster owner entry and explicit fragment target in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md). **Method:** enumerate all `core_05-05` links and named-definition widgets in both Chapter Six files; spot-check operative prose for capitalized or definitional uses of Chapter Five terms (e.g. **contribution state**, **violation nature**, **verified violation findings**, **Harm**, **Materiality Determination**); verify section-number cross-references inside Chapter Six integration against the actual §5 taxonomy. **Coverage:** Chapter Six does **not** invoke the vast majority of Chapter Five interdependent heads; for those entries, **no use** in Chapter Six is expected and no competing informal gloss was found in the reviewed blocks.

- [x] **P3 — Integration §7.1 — standing-input bullets vs §5 section taxonomy:** **Closed (2026-04-26).** [core_06-06_standing_integration.md](core_06-06_standing_integration.md) **§7.1** now lists **section 5.5** (constitutional floor rule) separately from **sections 5.6 through 5.8** (collective accountability, duty-to-resist, negligence).

- [x] **P3 — Integration §9 — sanction ladder coupling; overlapping §5 spans:** **Closed (2026-04-26).** **§9** *Sanction Ladder Coupling* uses a single **sections 5.1 through 5.8** span with non-overlapping role labels (**5.1–5.4**, **5.5**, **5.6–5.8**).

- [x] **P3 — Chapter Six D/E/C widgets — *Epistemic Integrity* **O** target vs Chapter Five cluster architecture:** **Closed (2026-04-26).** [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) **§2.3** adds **`#epistemic-integrity-o`** and **`#truth-constitutional-constraint-o`** before the shared cluster **O** line; all **Epistemic Integrity** and **Truth (Constitutional Constraint)** widget **O** links in numbered `core_*.md` now target those anchors (same operative **O** text).

**Verified aligned (no new TODO):** **Contribution State**, **Verified Violation Findings**, **Violation Nature** (Chapter Six–owned phrasing with Chapter Five stubs), **Participant Standing** (`#participant-standing-constitutional`), **Materiality Determination**, **Harm**, **Proportionality**, **Necessity**, **Feasibility**, **Foreseeability Diligence**, **Dependency**, **Risk**, **System Capture**, **Supremacy and Enforceability**, **Constitutional Constraint Violation**, **Coercion and Manipulation**, **Accountability**, **Collective Accountability Failure**, **Redress and Remediation**, **Procedural Fairness**, **Wellbeing**, **Meaningful Agency**, **Dignity and Equal Moral Standing**, **Irreversible Harm**, **Existential Risk**, **Safety**, **Truth**, **Proxy Divergence**, **Ecological Integrity**, **Environmental Preconditions**, **Transparency**, and **Trustworthiness** (including `#trustworthiness-psychological-safety-and-substantive-agency-conditions-e`) are used or linked in ways consistent with the owning Chapter Five entries. Domain-lens and descriptor prose (**Info-Sphere**, **psychological safety**, **bodily integrity**, etc.) reads as reader vocabulary or stackable tags, not competing definitions. **§3.3.0** reference to **§§5.1–5.8** correctly covers the full Violation Axis attachment span.

### Chapter Seven hand-review — Chapter Five definitions and cross-uses (2026-04-26)

**Scope:** [core_07-07_misconduct.md](core_07-07_misconduct.md) (full chapter), cross-checked against every `core_05-05_definitions_a_independent.md` link target and against operative prose that invokes **Chapter Five**–owned concepts by name. **Method:** full read of traces, **Definitions · Evaluation · Compliance** widgets, **Definition:** blocks, *Read with* anchors, and inline `core_05-05` links; negative scan for informal re-gloss of Chapter Five terms not cited (e.g. **good faith**, **force** / **coercion**, **standing**, **constitutional harm**). **Coverage note:** Chapter Five has a large `####` surface; Chapter Seven is a narrow misconduct owner and materially invokes only a **subset** of those entries — absence of the rest is expected, not a defect.

**Verified aligned (no new TODO):** **Necessity** (including *Necessity*-bounded emergency carve-out read with Chapter One and Article XXIII-D); **Concentration Threshold** (`#concentration-threshold-constitutional`) vs Chapter One §5.1.1 routing in §6.1; **Auditability**, **Contestability**, **Necessity**, **Proportionality** in §6.2; **Contestability** and **Transparency** (§6.3 trace and operative text); **Contestability** and **Procedural Fairness** widgets (§6.3); **Info-Sphere**, **Epistemic Integrity**, **Truth (Constitutional Constraint)**, **Transparency** (§6.4 trace, widgets, and inline links); **Accountability**, **Auditability**, **Incentive Alignment**, **Oversight**, **Procedural Fairness**, **System Capture** (§6.5 widgets and bribery routing). **Productive capacity** / concentration substance in §6.1 stays under the Chapter One §5.1 / §5.1.1 layer referenced from **Concentration Threshold**, consistent with **Productive Capacity** in Chapter Five. Colloquial **good faith** (§4 safeguards; §6.3 / §6.4 exclusions) does not contradict the **Good Faith** entry. Criterion **5** language (**force**, **coercion**, **usurpation**) stays at operative constitutional-misconduct level without redefining **Use of Force** or **Coercion and Manipulation**. **Standing** in waiver / mobility bullets is consistent with **Participant Standing** / Chapter Six usage, not a competing Chapter Five gloss.

- [x] **P3 — Chapter Seven §6.5 — D/E/C widget vs *Read with* definition list:** **Closed (2026-04-26):** [core_07-07_misconduct.md](core_07-07_misconduct.md) §6.5 *Definitions · Evaluation · Compliance* now includes full rows for **Oversight** (`#oversight-constitutional` / `-e` / `-c`) and **Procedural Fairness** (`#procedural-fairness-constitutional` / `-e` / `-c`), matching the *Read with* trace. `make ch5-dec-widget-audit` **PASS**.

- [x] **P3 — Extend `ch5_dec_widget_audit` consumers to Chapter Seven:** **Closed (2026-04-26):** [tools/ch5_dec_widget_audit.py](tools/ch5_dec_widget_audit.py) `CONSUMERS` now includes [core_07-07_misconduct.md](core_07-07_misconduct.md). `make ch5-dec-widget-audit` **PASS** (Chapter Seven D/E/C rows resolve to live Chapter Five anchors).

### Chapter Eight hand-review — Chapter Five definitions and cross-uses (2026-04-26)

**Scope:** [core_08-08_forum.md](core_08-08_forum.md) (full chapter, including non-operative reader guidance and Traces), cross-checked against every `####` / cluster owner in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) where Chapter Eight’s routing text invokes the same ideas. **Method:** enumerate all `core_05-05_definitions_a_independent.md` link targets; read operative §§1–9 for **capitalized** or **definitional** uses of Chapter Five terms (forum families, contribution state, standing, **Corpus**, ecological terms, **Existential Risk**, **Sentience Status Adjudication**, **Truth** / **Safety** shorthand in certification, colloquial **good faith** / **trust** / **dependency** / **integrity** / **harm**); compare to the owning Ch5 O/E/C lines, especially the six *Forum Family, …* entries and the *Corpus* and *Sentience Status Adjudication* stubs. **Coverage note:** most Chapter Five `####` entries are **not** substantively used in Chapter Eight; absence in Ch8 is expected where routing does not implicate that term, and a negative scan did not find informal competing glosses for unused heads.

- [x] **P3 — Chapter Eight chapter-opening Trace *Upstream* missing Chapter Five (nav parity with §1 and corpus-wide baseline link):** **Closed (2026-04-26):** the first **Trace** block’s *Upstream* list in [core_08-08_forum.md](core_08-08_forum.md) now includes [Chapter Five](core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) (after [Chapters Two through Four](core_02-04_definition_mechanics.md)), matching **§1** and the established `#chapter-five-foundational-definitions` pattern used in other `core_*.md` upstream lines.

**Verified aligned (no new TODO):** Inline anchors `#chapter-five-foundational-definitions`, [`#corpus`](core_05-05_definitions_b_semi_independent.md#corpus), and [`#sentience-status-adjudication-constitutional`](core_05-05_definitions_c_dependent_clusters.md#sentience-status-adjudication-constitutional) resolve to the intended chapter head and stubs. **§4.2.4** parenthetical (*Ecological Integrity*, *Environmental Preconditions*) matches the corresponding Chapter Five entry substance and the *Forum Family, Environment* **O** line. **Default venue table** and **§4.2.1–§4.2.6** are consistent with the six *Forum Family, Sentient* through *Forum Family, Constitutional* **O** lines (including **Technical Forum Domains** / *Forum Family, Technical*). **Section 7** (*Existential Risk* handling, **Truth** / **Safety** in certified constitutional questions, *Sentience Status Adjudication* / Article V-E hook) is substantively consistent with the owning definitions; shorthand **Truth** / **Safety** in one certification bullet is the same long-horizon stack referenced elsewhere, not a competing gloss. **Colloquial** **standing**, **contribution state**, **dependency**, **good faith**, **public trust**, **integrity**, and route-level **harm** / **reversibility** language read as Chapter Six / ordinary instrument vocabulary or non-capital *good faith*, not redefinitions of *Participant Standing*, *Dependency*, *Good Faith*, *Trust*, etc. [tools/ch5_dec_widget_audit.py](tools/ch5_dec_widget_audit.py) has **no** Chapter Eight consumer (Chapter Eight does not host D/E/C definition widgets) — no tool change.

### Terminology and definitions consistency pass (2026-04-24)

- [x] **P3 — Sentient / people and breach-family vocabulary cleanup (regression-scoped `make regression` gate):** **Closed (2026-04-26)** for the files in `make lexical-vocabulary-audit` scope: plain-language and editor-guidance *people* / bare *charter* phrasing was aligned across the binding corpus, `doc_architecture.md` plain-language table, and related *In plain terms* lines in Chapters **Seven, Eight, Nine, Ten, Eleven, Fourteen**; [tools/prose_continuity_audit.py](tools/prose_continuity_audit.py) was updated so list continuations, top-level list continuations, and HTML lines are not misfired as *malformed-indent* (see *MEMLOG*). **`make regression`** and **`make lexical-vocabulary-audit`** **PASS**.
  **Optional follow-on:** re-scan for colloquial *people* in non-scoped or archived material; verify **breach**-family wording in Chapter Six if future edits reintroduce undefined uses outside the current gate.

- [x] **P3 — Article XVIII-D / XIX-D movement-refuge label decision:** **Closed (2026-04-26).** **Canonical label:** **Article XVIII-D** (*Movement, Migration, and Refuge*) at `#article-xviii-d-movement-migration-and-refuge`. Corpus and implementation text aligned; **Article XIX-*** remains interoperability / exit-integrity. Re-run `rg 'Article XIX-D' --glob '!archive/**'` after future edits to catch regressions.

### P3 — Holistic redundancy sweep (parent only)

- [ ] **Redundancy / definitions-first sweep** per [doc_architecture.md](doc_architecture.md) section 13. **Prerequisites met** as of **2026-04-08**. Partial passes and optional editorial batches are logged in **section 13** and archived under **[archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md)** section **B**. **Check this box** when you accept **holistic** closure across **all four** corpus files (full grep-per-theme dedup), or repurpose for the **next** edition's backlog.
  **Evaluation (2026-04-17, engineer note — not flipped):** This is an explicit user-acceptance gate ("**Check this box** when *you* accept holistic closure"), not an engineer-unilateral closure; accordingly the checkbox is left `[ ]` for the user's acceptance or repurposing. Engineer assessment of current state, for the user's evaluation: (i) the **four P3 D/E/C-widget follow-ups** (tool integration, greenfield over-inclusion, Article II opener, Mechanics/Read with) all closed on 2026-04-17 under the passes above, bringing every `core_*.md` D/E/C widget and every Chapter Five `####` definition entry under a blocking `make regression` gate (`ch5-dec-widget-audit`) that validates canonical anchor presence, widget row shape, and anchor resolution; (ii) the prior P3 per-file sub-items (passes 1–7, mini-audits, `cont. 1–48`) remain closed and are archived under [archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md) section B; (iii) the 2026-04-17 custody-hardening / dedup pass (edition `SC-Corpus-2026.04.28`) closed the P0 Chapters Eleven–Thirteen / Chapter Six de-duplication and the P1 boundary-watch guardrail for the three owners most at risk of cross-layer redundancy drift; (iv) the 2026-04-17 Chapter Nine boundary-watch zone (edition `SC-Corpus-2026.04.29`) added the converse-direction discipline under Chapter Nine. **Gaps for user consideration before acceptance:** a full grep-per-theme dedup across all four corpus files has not been run under the 2026-04-17 suspension (the regression-scenarios file and `evidence/` tree are both absent until `P1 — Reinstate regression scenarios and evidence tree` closes); if the user wants a genuine "holistic" acceptance, that sweep is the outstanding empirical step, and it is best run *after* regression-scenarios reinstatement so dedup findings can be seed-rowed in the matrix rather than queued. **Recommendation (not flipped):** either (a) leave this open as-is until after P1 regression-scenarios reinstatement, then run the grep-per-theme sweep and decide, or (b) repurpose the checkbox for the next edition's backlog as the existing prompt allows. No unilateral flip.

## TODO maintenance and archiving

**Authoritative normative state** is in the eight binding **Corpus (Constitutional)** files and chapter owners enumerated in [README.md](README.md) (numbered `core_*.md` plus `corpus_*.md` / `corpus_joint_structure.md` as there defined — *Corpus* defined in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) Chapter **Five**). This file and [doc_architecture.md](doc_architecture.md) track **process, checklists, and closure**; they are not substitutes for the corpus. Retired compatibility wrapper filenames (`core_constitution.md`, `core_definitions.md`, `core_amendment.md`) are not stand-alone law paths.

**Default:** Keep completed items here (`[x]` checkboxes and ticket narratives). No separate archive is required.

**Archive completed work** when one of these applies:

- **Corpus edition cut** — You tag or publish a named edition (edition id and effective date per architecture doc section **17**). Optionally append or snapshot "closed for this edition" notes so assurance readers see a frozen process summary.
- **Hygiene** — End of a quarter or sprint: if the file is hard to scan because most lists are complete, move **fully closed sections** to `archive/TODO_COMPLETED_<period>.md` (create `archive/` if needed) and replace them here with one line pointing to that file. Keep regression and drill IDs that remain operationally relevant, or link to the archive section that holds them.
- **Never treat the archive as law** — Archived TODO text is **history only**; if it disagrees with the current corpus commit, the corpus wins.

**Verification evidence** stays under [evidence/](evidence/); archiving TODO narratives does not replace drill records.

## Archived completed work

**2026-04-26 full-file snapshot (hygiene):** [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md) — open + closed items, long narratives, and structural-sync appendices as of the archive pass.

**2026-04-17 hygiene cut:** Track 7.1 *Capital-punishment policy* closure (Option (a) Categorical Abolition, edition `SC-Corpus-2026.04.26`); 2026-04-17 custody-hardening / dedup pass (Chapters Eleven–Thirteen / Chapter Six de-duplication; Chapters Eleven–Thirteen boundary-watch guardrail; Chapter Fourteen incorporation-custody hardening; edition `SC-Corpus-2026.04.28`); 2026-04-17 productivity / avoidable-burden verification (Chapter Ten governance integration; Article XX avoidable-complexity hook; `RS-CH1-PROD-CAP-*` / `RS-CH1-AVOID-BURDEN-*` regression scenarios); and the full 2026-04-16 constitutional content-gaps batch (26 items across Tiers 1 / 2 / 3 plus the planning-memo gate, landings spanning edition lineage `SC-Corpus-2026.04.14` through `SC-Corpus-2026.04.27`, including Q-10.2.B *Indigenous continuity scoping* on 2026-04-17):

- **[archive/TODO_COMPLETED_2026-04-17.md](archive/TODO_COMPLETED_2026-04-17.md)**

**2026-04-16 hygiene cut:** 2026-04-09 ChatGPT external-feedback batch closure, 2026-04-16 productivity-/-avoidable-burden §5.1 ecological-preconditions extension, 2026-04-16 §7.2.5 Chapter Five anchors promotion, 2026-04-16 D/E/C widget rollout follow-ups (spacer sweep, greenfield fan-out, Ch 4 §1.3 Trace, Ch 3 Trace gap closure, Ch 2-4 mechanics attachment, roadmap-exclusion sweep + refinement, `Internal Hierarchy` definition), 2026-04-16 §2.1 evasion prose cleanup, and 2026-04-16 self-healing systems doctrine (core plug-in + regression pack + Protocol profiles):

- **[archive/TODO_COMPLETED_2026-04-16.md](archive/TODO_COMPLETED_2026-04-16.md)**

**2026-Q2 hygiene cut:** Closed Protocol R/D checklists, Tickets 1–8 narratives, prioritization/sprint/insertion blocks, and Trust Under Active Attack audit material:

- **[archive/TODO_COMPLETED_2026-Q2.md](archive/TODO_COMPLETED_2026-Q2.md)**

**Edition closure (SC-Corpus-2026.04):** External framework / embedding gap batch (full done narratives):

- **[archive/TODO_COMPLETED_SC-Corpus-2026.04.md](archive/TODO_COMPLETED_SC-Corpus-2026.04.md)**

Regression scenario families and drill evidence are normally tracked in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` and `evidence/`. **Both are absent under the 2026-04-17 suspension** (see *P1 — Reinstate regression scenarios and evidence tree* above); the pointers will become live again on reinstatement.

**Structural sync + P3 sub-items (archived 2026-04-08):** Full P0–P3 checkbox bodies (structural map, cross-refs, optional editorial **cont. 1–48**) moved to **[archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md)** — section **B**. Evidence pointer: [evidence/2026-04-08/TODO_MAINTENANCE_ARCHIVE_2026-04-08.md](evidence/2026-04-08/TODO_MAINTENANCE_ARCHIVE_2026-04-08.md).

Historical *External Framework and Embedding Gaps* and *Structural synchronization* (patch-level history, gap-analysis narratives, and related pointers) are preserved in the **2026-04-26** full snapshot: [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md).
