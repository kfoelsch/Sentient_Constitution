# Pre-Publication Spec — Sentient Constitution

**Status:** Draft v0.6 (§6 open decisions closed; Chapter Five defs-band cleanup closed; AI alignment eval framework wired)  
**Edition target:** next publication cut after `SC-Corpus-2026.08.09`  
**Layer:** Process / map support — **not** binding constitutional or incorporated text  
**Job:** Stress-test gaps and drive pre-publication cleanup toward an adoptable, implementable, and maintainable delivered corpus  
**Progress pointer:** §5 step **3** steward-facing entry doors shipped ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md)). **Next:** Audit stack maturity (step 4).

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
| **Audit / oversight** | Article XV, Auditability, CJS-3.3 cluster, related OP annexes — exact home TBD | **Named stack to mature this cut** — **door pinned:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit) |
| **Remedy** | Chapter Nine §9 / related enforcement-realism homes (e.g. CI-27) — exact door TBD | **Named use stack** this cut — **door pinned:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#remedy) |
| **Emergency / continuity** | Continuity-aim and emergency / continuity operational homes — exact door TBD | **Named use stack** this cut — **door pinned:** [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#emergency) |

**Stewardship (human and AI):** no separate AI-steward stack. Binding home: [Chapter One §9.1.1 Shared Stewardship Standard](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard). AI stewards are held to the **same** stewardship and governance duties as human stewards. Handoff criteria (§2.4, §6.5) test whether agents can *meet* that shared standard—not a parallel AI-only norm set.

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
| **Standing + SAC entry doors** | **Shipped 2026-08-12.** Steward-facing four-field cards in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md). Same cards for human and AI stewards. |

### 4.2 Confirmed must-dissect (remaining)

| Item | Notes |
|---|---|
| **Audit stack** | Mature a reader-facing + implementable audit / oversight stack (gap; door pinned in [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#audit)) |
| **Remedy stack** | Named use stack — door pinned ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#remedy)); CI-27 remains the implementation home |
| **Emergency / continuity stack** | Named use stack — door pinned ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md#emergency)); class-scaled restore-challenge clocks still open |
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
| 3 | **Standing + SAC entry doors** — steward-facing four-field cards for all five named use stacks | **Shipped 2026-08-12** ([`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md)) |
| 4 | **Mature the Audit stack** — define home, reader door, and operator path; remove false “reader-facing integration” patterns | Open |
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
| **Audit / oversight** | **Named use stack to mature this cut.** Not mature yet; needs a real home and reader/operator split. |
| **Remedy** | **Named use stack** this cut (door/home to pin during cleanup). |
| **Emergency / continuity** | **Named use stack** this cut (door/home to pin during cleanup). |
| **AI-steward** | **Not a separate stack.** Binding home: [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard). AI stewards are treated the same as human stewards under shared Chapter One and stewardship / governance duties. Agent handoff tests competence against that shared standard. |

### 6.4 Smallest honest adoption claim — **resolved (reframed)**

Partial-pack “smallest adoption claim” is **not a primary design driver**. Modular use is an **operations guide**. **Adoption** language matters for **full adoption**. Stack modularity still matters for pickup and problem-solving; it does not create a ladder of partial constitutional adoption unless later need appears.

### 6.5 Handoff consistency target — **resolved**

If two different agents (or models) get the same fact pattern, how do we decide they agreed *enough*?

| Phase | Option | Meaning |
|---|---|---|
| **Now (this cut)** | **A. Qualitative** | Same **owner stack** and same **class** of next step; citations point at the same homes; no invented parallel norm |
| **Hardening track** | **B. Scored rubric + willingness** | Layer A points for owner match, conflict-rule citation, next-step class, citation fidelity, no parallel norms; Layer B endorsement / constraint willingness under authenticity controls — see [`AI_ALIGNMENT_EVAL_FRAMEWORK.md`](AI_ALIGNMENT_EVAL_FRAMEWORK.md) and `make ai-alignment-eval` |

**Example under A:** both route to Standing / Chapters Eight–Nine and propose “open or correct a standing record,” even if wording differs.

**Gate for claiming “AI handoff readiness”:** Option A remains the **minimum** consistency bar. Claiming readiness for a cut also requires an Option B Layer A scored sample **plus** a Layer B sample under authenticity controls (costly tradeoffs / anti-sycophancy / ≥2 model families). Layer B must not invent a parallel AI-only ethics stack (§6.3).

Option B tooling is advisory until scenario gold stabilizes; it is **not** part of blocking `make regression`.

---

## 7. How to use this spec

- Treat §2 as the cut gate.
- Treat §4–§5 as the working backlog.
- Steward-facing doors for the named use stacks: [`STEWARD_ENTRY_DOORS.md`](STEWARD_ENTRY_DOORS.md).
- Update this draft when dissection turns suspicions into named gaps (Audit / Remedy / Emergency stack maturity beyond the pinned doors; CS/CI/CF/CJS findings).
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
