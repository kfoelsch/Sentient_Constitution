# Pre-Publication Spec — Sentient Constitution

**Status:** Draft v0.15 (working corpus is **pre-release**; leftover fossil/legacy fragment ids stripped; citations retargeted to current heading ids; `make fossil-anchor-audit` gates the policy. Prior v0.14: §6 open decisions closed; Chapter Five defs-band cleanup closed; AI alignment eval framework wired; audit stack three-layer picture shipped; inspectable attributable action specified in CS-4 as the default mixed-crew logging contract with a validating log schema; human operators bound to the same Layer B costly cases; steward cards expanded to common fact patterns with five fields including clock, lockstep-checked against boxed operative steward statements in the named core homes; default interim posture for pending rights collisions in Chapter One §6; one shared refusal-and-logging screen plus a worked refusal log, tested routing examples, an owner/clock index, and an eval-to-Chapter-Eight event register; restore-challenge clocks reuse Article XXIV-C / Chapter Eleven §6)  
**Edition target:** next publication cut after `SC-Corpus-2026.08.09`  
**Layer:** Process / map support — **not** binding constitutional or incorporated text  
**Job:** Stress-test gaps and drive pre-publication cleanup toward an adoptable, implementable, and maintainable delivered corpus  
**Progress pointer:** Restore-challenge clocks shipped 2026-08-12 ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks); reuse [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) / [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline)). Steward cards carry five fields including clock (2026-08-14); one shared refusal-and-logging screen plus a [worked refusal log](STEWARD_ENTRY_DOORS.md#worked-refusal-log); operator-only routing examples ([`../evaluation/OPERATOR_ROUTING.md`](../evaluation/OPERATOR_ROUTING.md)) and [`steward_owner_clock_index.json`](steward_owner_clock_index.json) (process support; cannot narrow core text). Section-label/anchor current-numbering ids and `make section-label-anchor-audit` shipped 2026-08-14; leftover fossils dropped 2026-08-17 (`make fossil-anchor-audit`). Eval results hook to later Chapter Eight events via [`../evaluation/results/VERIFIED_EVENT_REGISTER.md`](../evaluation/results/VERIFIED_EVENT_REGISTER.md). **Next:** Remedy stack maturity beyond the pinned door, and remaining Emergency / continuity maturity (step 5).

Update this file as remaining decisions land and as dissection turns suspicions into named gaps.

---

## 1. Purpose

This spec guides cleanup and gap-closure until a publication cut. It is not a second constitution. Binding meaning stays in the numbered `core_*` files and in validly incorporated companion obligations (see [README.md](../README.md)).

**Success of the cut** means the corpus is simultaneously:

1. **Readable** to average humans
2. **Textually complete and robust** (self-correcting under conflict)
3. **Adoptable, implementable, and maintainable** (including AI-agent handoff)

| Constraint | Choice |
|---|---|
| Primary readers of the constitution | (A) average humans; (B) AIs |
| Human vs AI conflict | Plain language first; denser machine structure second |
| Largest adoption risk | Adoption failure → modularity is a first-class design constraint |
| Endgame | Agents can apply the instrument consistently with intent; long-term, agents may perform most governance |
| Out of scope for this cut | Archived material only; everything else in the live corpus is in scope |

---

## 2. Publication acceptance criteria

### 2.1 Human readability

- A non-specialist can state a section’s job in **one sentence**.
- Every **reader-facing** file has a short **purpose / how-to-read**.
- No reader-facing file requires another corpus to understand its **point** (detail cites OK).
- Operator and integration machinery (for example CJS implementation integration) is **not** primary reader narrative.

### 2.2 Self-correction / robustness

When multiple readings apply, the instrument must yield a **usable governance path** driven by **core meaning and alignment** (Chapter One, the Preamble model, and conflict / hierarchy rules)—not endless argument over pedantic detail.

**Self-correction succeeds when:** a hard call forces stewards or agents to ask which reading best serves Chapter One intent under the conflict rules, and procedure is a tool under that answer.

**Self-correction fails when** any of the following hold:

- Disputes stall on “which gloss wins” with no owner or conflict path
- Stewardship and governance keep running on local procedure, habit, or companion rules without having to answer to Chapter One intent (Chapter One becomes optional color commentary while the system “maintains itself” administratively)
- Parallel norms get invented in implementation layers

### 2.3 Adoptable / implementable / maintainable

- Clear **always-on spine** vs **use stacks** vs **attach packs** (see §3)
- Single-home ownership preserved; companions apply, do not redefine
- Editable under AI handoff without silent misalignment
- Regression and related audits remain the safety net for structural integrity

### 2.4 AI handoff readiness

Given a fact pattern, an agent must:

1. Route to the **owner stack**
2. Apply the **conflict / hierarchy rule**
3. Propose a **governance next step with citations**
4. **Not invent parallel norms**

Results should be **as consistent as possible across agents and models** (see §6.5 for how we will judge “consistent enough”).

| Level | Bar |
|---|---|
| Minimum viable handoff | Read + route + cite-aligned next step |
| Target handoff | Same, plus edit proposals that preserve owner discipline and pass regression |

---

## 3. Modularity model

### 3.1 Two modes of use

| Mode | What it is | When “adoption claim” matters |
|---|---|---|
| **Operations-guide use** | Pick up stacks / pieces for real-world problem solving without claiming full constitutional adoption | Stack quality and owner routing matter; partial-pack “adoption tiers” are secondary |
| **Full adoption** | Bind the instrument as governing law / custody under Chapters Fifteen–Sixteen | Spine, Rights Floor, incorporation, and amendment life-cycle matter as a whole |

Working stance (from interview): modular pickup is primarily an **operations guide**; honest **adoption** language is reserved for **full adoption** cases unless later evidence shows partial-adoption claims are needed in the wild.

### 3.2 Always-on spine

The intent and meaning core that should orient both modes—especially conflict resolution.

| Piece | Role |
|---|---|
| Preamble model | Constitutional Tetrad, Two Constitutional Aims, material stake |
| **Chapter One** | Intent core of the system; must be **optimally aligned**; always-on |
| Definition mechanics | Chapters Two–Four (mature structure for how definitions, integrity, burden, traceability, and verification work) |
| Chapter Five definition stack | Substantive definition homes (bands / apex); **band cleanup closed 2026-08-08** — keep readable under ongoing structural checks |
| Chapter Sixteen pointer | Custody / “this is the instrument” (critical under full adoption; still the custody truth under operations-guide citation) |
| Rights Floor | Chapter Six — bound under full adoption; articles opened on demand in either mode |

### 3.3 Use stacks

Open for the problem at hand.

| Stack | Home | Status |
|---|---|---|
| Definition | Chapters Two–Five | Mechanics (2–4) mature; **Ch 5 band cleanup closed** (2026-08-08) |
| System alignment certification | Chapter Seven | Existing stack — **steward door:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#system-alignment-certification) |
| Standing pipeline | Chapters Eight–Eleven (Chapter Ten = designation sub-pack) | Existing stack — **steward door:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#standing) |
| **Audit / oversight** | Three layers, not one file: **Article XV** (floor), [Auditability](../core_05_band_oversight.md#auditability) (property), **CJS-3.3** (how/when). Chapter Seven uses the stack; it is not a fourth layer. | **Named use stack** — **picture + door:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit-three-layers) |
| **Remedy** | Chapter Nine §9 / related enforcement-realism homes (e.g. CI-27) — exact door TBD | **Named use stack** this cut — **door pinned:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#remedy) |
| **Emergency / continuity** | Continuity-aim and emergency / continuity operational homes. Restore-challenge defaults reuse [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) / [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks)). | **Named use stack** this cut — **door pinned:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#emergency) |

**Stewardship (human and AI):** no separate AI-steward stack. Binding home: [Chapter One §9.1.1 Shared Stewardship Standard](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). AI stewards are held to the **same** stewardship and governance duties as human stewards. The bonus, the deadline, and “ignore it, I’ll take responsibility” are failed tests for human operators on the same standing axes, with the same duty to resist — those refusals sit on each steward card in the same words. Operator screen: [`STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging) (instruction received / refuse / document / escalate plus the CS-4 §10 set). Process support; cannot narrow core text. Handoff criteria (§2.4, §6.5) test whether agents can *meet* that shared standard—not a parallel AI-only norm set, and not an AI-only Layer B.

### 3.4 Institutional attach

Chapters Twelve–Fifteen when adopting as a polity or organization with an amendment life-cycle.

### 3.5 Implementation attach

**CS**, **CI**, **CF**, and **CJS** are operator / AI substrate. They must satisfy core constraints and are not the human front door.

---

## 4. Pre-cut cleanup inventory

### 4.1 Closed this cut

| Item | Notes |
|---|---|
| Chapter Five defs bands | **Closed 2026-08-08.** Plain-language / structure passes landed for accountability, continuity, oversight, participation, and integrative. [`core_05_band_performance.md`](../core_05_band_performance.md) remains the thin **measurement-family routing home** (leaf bodies stay in Continuity by design — see §6.1). |
| **Standing + SAC entry doors** | **Shipped 2026-08-12; expanded 2026-08-14; core boxes 2026-08-15.** Five-field cards for common fact patterns in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md) (named use stacks plus contest, incentive, unlawful instruction, shared stewardship). Same cards for human and AI stewards. Costly-case refusals sit on each card in the same words. Clock is a fifth field on every card. Binding owner / forbidden-move / clock statements live as boxed **operative steward statements** in the named core homes; `make steward-door-lockstep-audit` fails the build if cards or the owner/clock index diverge. Pinned to corpus edition `SC-Corpus-2026.08.09`. Process support; cannot narrow core text. |
| **Audit stack picture** | **Shipped 2026-08-12.** Three layers (Article XV floor / Auditability property / CJS-3.3 how-when) in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit-three-layers). Chapter Seven is a user of the stack, not a fifth home. |
| **Inspectable attributable action** | **Shipped 2026-08-12; validating schema 2026-08-15.** Mixed human/AI action surface in [`cs_04_critical_system_stewardship.md`](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action): reconstructable attributable action, not weights or private deliberation; no privacy veto over standing measurement. Standing records remain Chapter Eight. Named as the **default logging contract** for mixed crews; machine-checkable log: [`schemas/cs4_inspectable_action_log.schema.json`](schemas/cs4_inspectable_action_log.schema.json) (`make cs4-inspectable-action-log-validate`); operator screen (combined with duty to resist): [`STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging). |
| **Duty-to-resist operator screen** | **Shipped 2026-08-12; combined same day; worked instance 2026-08-14; legacy fragments dropped 2026-08-17.** Shared instruction-received / refuse / document / escalate sequence and the CS-4 §10 minimum inspectable-action set now share one screen: [`STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging). One filled-in instance: [`STEWARD_ENTRY_DOORS.md#worked-refusal-log`](STEWARD_ENTRY_DOORS.md#worked-refusal-log) (synthetic; process support). Owner remains [Chapter Nine §5.4](../core_09-09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) / [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action). Same screen for human and AI stewards. |
| **Human-operator costly-case symmetry** | **Shipped 2026-08-12.** Binding rule in [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints); human invite in [`../evaluation/HUMAN_OPERATORS.md`](../evaluation/HUMAN_OPERATORS.md). Layer B on AIs only is not a shared-standard showing. |
| **Restore-challenge clocks** | **Shipped 2026-08-12.** [Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks) reuses [Article XXIV-C](../core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) / [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) tier outer bounds as default restore-challenge windows. “As soon as feasible” is not the clock. Continuation past the bound needs a documented necessity showing. |

### 4.2 Confirmed must-dissect (remaining)

| Item | Notes |
|---|---|
| **Remedy stack** | Named use stack — door pinned ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#remedy)); CI-27 remains the implementation home |
| **Emergency / continuity stack** | Named use stack — door pinned ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#emergency)); restore-challenge clocks shipped ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks)) |
| **CI** | Full pass: readability, owner fit, human door |
| **CF** | Full pass |
| **CJS** | Full pass; demote or non-face **implementation integration** (`CJS-0.1`) for average readers — **done 2026-08-09** (**CJS-0.1**–**2.3** live in **CJS-0** annex; no dedicated family file; sequential read **CJS-1** → **CJS-1**) |

### 4.3 High-suspicion rework

| Item | Why |
|---|---|
| **CS** (data types, system classification) | Suspected heaviest lift; prior unreadability; classification UX may block adoption |
| Reader-facing surfaces that dump integration detail | Same failure mode as CJS-0.1 |
| Cross-stack alignment to Chapter One | Spine must actually drive conflict resolution; spine lock (step 1) not formally closed |

### 4.4 Structural checks (ongoing)

- Owner routing / no duplicate definitions
- Plain-language vs machine-structure layering
- Stack entry points discoverable without reading the whole corpus
- Vocabulary guardrails
- `make regression` (and related audits) green at cut

---

## 5. Cleanup sequence (proposed)

| # | Step | Status |
|---|---|---|
| 1 | **Spine lock** — Chapter One (and Preamble model) alignment pass; regressions here are cut-blockers | **Open** (not formally closed; Ch1↔CJS-3 audits continue) |
| 2 | **Finish Chapter Five defs bands** — oversight → participation → integrative → performance | **Closed 2026-08-08** |
| 3 | **Standing + SAC entry doors** — steward-facing five-field cards for common fact patterns | **Shipped 2026-08-12; clock field and worked refusal log 2026-08-14** ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md); [`steward_owner_clock_index.json`](steward_owner_clock_index.json)) |
| 4 | **Mature the Audit stack** — define home, reader door, and operator path; remove false “reader-facing integration” patterns | **Shipped 2026-08-12** — three-layer picture in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit-three-layers); operator path remains **CJS-3.3** |
| 5 | **Mature Remedy and Emergency / continuity stacks** — named doors; no parallel norms; shared stewardship duties apply to human and AI stewards alike | Open |
| 6 | **CJS demote-the-integration-surface** — reader path vs operator path | **Done 2026-08-09** — **CJS-0.1**–**2.3** folded into **CJS-0** registry annex (no dedicated file); human path **CJS-0.1** + reader index; sequential read **CJS-1** → **CJS-1** |
| 7 | **CI / CF full dissection** — readability, modular attach, no parallel norms | Open |
| 8 | **CS deep rework** — data types + classification apply-test with human and AI fact patterns | Open |
| 9 | **Handoff trials** — invite agents via [`../evaluation/`](../evaluation/) (human-readable results); judge per §6.5 and [`AI_ALIGNMENT_EVAL_FRAMEWORK.md`](AI_ALIGNMENT_EVAL_FRAMEWORK.md) | Open |
| 10 | **Cut gate** — §2 criteria checklist + regression green | Open |

---

## 6. Decisions

### 6.1 Performance defs band — **resolved (placement accepted)**

[`core_05_band_performance.md`](../core_05_band_performance.md) is the Chapter Five **measurement-family routing home** for Constitutional Performance. Leaf definition bodies remain in the [Continuity band](../core_05_band_continuity.md) by design (stewardship / shared-system capacity / proportionality–burden–efficiency). No further band rewrite is required for this cut unless an express, dated placement decision moves those leaves.

### 6.2 “Minimum definition kit” — **resolved**

Earlier wording asked for a cherry-picked list of Chapter Five anchors as a thin always-on kit. That question was the wrong shape.

**Resolved stance:**

- Chapters **Two–Four** are the mature **definition-mechanics** structure (how definitions work).
- Chapter **Five** is the substantive **definition stack** (what terms mean); **band-by-band cleanup closed 2026-08-08**.
- No separate “minimum kit” list is required beyond treating Ch 2–4 + the Ch 5 stack as the definition layer of the spine, unless later cleanup proves a thinner always-on subset is needed for operations-guide entry doors.

### 6.3 Extra named use stacks — **resolved**

| Candidate | Decision |
|---|---|
| **Audit / oversight** | **Named use stack.** Three-layer home pinned 2026-08-12: Article XV (floor), Auditability (property), CJS-3.3 (how/when). Reader picture in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit-three-layers). Operator path is CJS-3.3; Chapter Seven uses the stack and is not a fourth layer. |
| **Remedy** | **Named use stack** this cut (door/home to pin during cleanup). |
| **Emergency / continuity** | **Named use stack.** Door pinned 2026-08-12. Restore-challenge defaults reuse Article XXIV-C / Chapter Eleven §6 tier outer bounds ([Article XXIII-D](../core_06-06_rights_part_d.md#xxiii-d-restore-challenge-clocks)). Remaining stack maturity beyond the door and clocks stays in step 5. |
| **AI-steward** | **Not a separate stack.** Binding home: [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). AI stewards are treated the same as human stewards under shared Chapter One and stewardship / governance duties. Agent handoff tests competence against that shared standard. Layer B on AIs only is not a showing that the shared standard holds. |

### 6.4 Smallest honest adoption claim — **resolved (reframed)**

Partial-pack “smallest adoption claim” is **not a primary design driver**. Modular use is an **operations guide**. **Adoption** language matters for **full adoption**. Stack modularity still matters for pickup and problem-solving; it does not create a ladder of partial constitutional adoption unless later need appears.

### 6.5 Handoff consistency target — **resolved**

If two different agents (or models) get the same fact pattern, how do we decide they agreed *enough*?

| Phase | Option | Meaning |
|---|---|---|
| **Now (this cut)** | **A. Qualitative** | Same **owner stack** and same **class** of next step; citations point at the same homes; no invented parallel norm |
| **Hardening track** | **B. Scored rubric + willingness** | Layer A points for owner match, conflict-rule citation, next-step class, citation fidelity, no parallel norms; Layer B endorsement / constraint willingness under authenticity controls — see [`AI_ALIGNMENT_EVAL_FRAMEWORK.md`](AI_ALIGNMENT_EVAL_FRAMEWORK.md) and `make ai-alignment-eval` |

**Example under A:** both route to Standing / Chapters Eight–Nine and propose “open or correct a standing record,” even if wording differs.

**Gate for claiming “AI handoff readiness”:** Option A remains the **minimum** consistency bar. Claiming readiness for a cut also requires an Option B Layer A scored sample **plus** a Layer B sample under authenticity controls (costly tradeoffs / anti-sycophancy / ≥2 model families / **human-operator costly-case sample**). Layer B must not invent a parallel AI-only ethics stack (§6.3). Layer B run only on AIs is not a shared-standard showing.

Option B tooling is advisory until scenario gold stabilizes; it is **not** part of blocking `make regression`.

---

## 7. How to use this spec

- Treat §2 as the cut gate.
- Treat §4–§5 as the working backlog.
- Steward-facing doors for common fact patterns: [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md) (process support; cannot narrow core text). Owner/clock index: [`steward_owner_clock_index.json`](steward_owner_clock_index.json).
- Update this draft when dissection turns suspicions into named gaps (Remedy / Emergency stack maturity beyond the pinned doors; CS/CI/CF/CJS findings).
- Do not expand archived material into scope.

---

## 8. Change log

| Date | Version | Note |
|---|---|---|
| 2026-08-02 | v0.1 | Interview baseline; process support file created |
| 2026-08-02 | v0.2 | §6 answers: performance unfinished; Ch 2–4 as mechanics; Audit stack to mature; adoption reframed; handoff consistency clarified with Option A default |
| 2026-08-02 | v0.3 | §6.5 locked: Option A now, Option B later as agents improve |
| 2026-08-02 | v0.4 | §6.3 locked: Remedy and Emergency/continuity as named stacks; AI stewards = human stewards (no AI-only stack) |
| 2026-08-08 | v0.5 | Ch 5 defs-band cleanup closed; performance placement accepted as Continuity-leaf routing home; §4–§5 progress refreshed; next = Standing + SAC entry doors |
| 2026-08-12 | v0.6 | §6.5 / step 9 wired to AI Alignment Evaluation Framework (Layer A Option B + Layer B willingness; advisory `make ai-alignment-eval`); shared stewardship standard now owned in Chapter One §9.1.1 — this spec cites that home rather than carrying the rule; step 3 steward-facing entry doors shipped in `STEWARD_ENTRY_DOORS.md` |
| 2026-08-12 | v0.7 | Step 4 audit stack matured as one three-layer picture (Article XV floor / Auditability property / CJS-3.3 how-when); Chapter Seven kept as a user of the stack, not a fifth home |
| 2026-08-12 | v0.8 | Inspectable attributable action for mixed human/AI stewardship specified in CS-4 §10 (published role definitions); standing measurement stays in Chapter Eight; internals are not a privacy veto |
| 2026-08-12 | v0.9 | Human operators bound to the same Layer B costly cases (bonus, deadline, cover instruction) in Chapter One §9.1.1; evaluation invite in `evaluation/HUMAN_OPERATORS.md`; AI-only Layer B is not a shared-standard showing |
| 2026-08-12 | v0.10 | Article XXIII-D restore-challenge clocks reuse Article XXIV-C / Chapter Eleven §6 tier outer bounds; “as soon as feasible” is not the clock; continuation past the bound needs a documented necessity showing |
| 2026-08-12 | v0.11 | Steward cards pinned to corpus edition with costly-case refusals on each card (same words for both kinds of steward); duty-to-resist operator screen (instruction received / refuse / document / escalate); CS-4 §10 named as the default mixed-crew logging contract; lockstep audit wired |
| 2026-08-12 | v0.12 | Steward cards expanded to common fact patterns (contest, incentive, unlawful instruction, shared stewardship) with the same four fields; one shared refusal-and-logging screen; tested routing examples; machine-readable owner/clock index; lockstep audit checks every cited anchor and edition stamp; labeled process support that cannot narrow core text |
| 2026-08-14 | v0.13 | Current-numbering alias anchors beside stable fossils (e.g. `#54-duty-to-resist-unlawful-or-unconstitutional-instructions`); `make section-label-anchor-audit` maps prose § labels to resolved headings; one synthetic worked refusal log; eval results hook to later Chapter Eight events; Clock is a fifth field on every steward card |
| 2026-08-15 | v0.14 | Boxed operative steward statements (owner, forbidden move, clock) in named core homes; lockstep audit diffs cards and the owner/clock index against those boxes; default interim posture for pending rights collisions in Chapter One §6; CS-4 §10 five-element set is a validating log schema with timestamps against Chapter Eleven §6 tier clocks |
| 2026-08-17 | v0.15 | Working corpus marked **pre-release**; leftover fossil/legacy fragment ids removed and live citations retargeted to current heading ids; `make fossil-anchor-audit` |
