# Archived TODO — structural checklist + governance backlog (snapshot)

**Archived:** 2026-04-08 (maintenance hygiene)  
**Live corpus at archive time:** `SC-Corpus-2026.04.5` (effective **2026-04-08**)  
**Authoritative law:** [core_constitution.md](../core_constitution.md), [corpus_primitives.md](../corpus_primitives.md), [corpus_systems.md](../corpus_systems.md). This file is **process history only**. **2026-04-10:** Sentient Constitution core chapters were expanded to **1–10**; task text that cites **Chapter Six** for voting/roles or **Chapter Four** for compliance reflects **pre-split** numbering—see [doc_architecture.md](../doc_architecture.md) section **5** and **13** for the current map.

---

## A) Open backlog (corpus / governance) — all closed by 2026-04-08

- [x] Add **no age limit** to steward qualifications (where steward eligibility is defined—e.g. Chapter Six / stewardship character, [corpus_systems.md](../corpus_systems.md) steward tiers, or related primitives). *(Done **2026-04-08**, edition **`SC-Corpus-2026.04.2`**: **core_constitution.md** Chapter Six §1 *Eligibility without maximum age*; **corpus_systems.md** Chapter S3 competency block; **Article I** governance participation uses the same no–age-alone rule for franchise; regression **RS-VI-001**.)*
- [x] Add **voting protocols** (scope, thresholds, eligibility, recordkeeping, and alignment with contestability / legitimacy layers as appropriate). *(Done **2026-04-08**, edition **`SC-Corpus-2026.04.3`**: **core_constitution.md** Chapter Six §4 *Voting and Binding Collective Choice Protocols*; **Article I** pointer; **corpus_primitives.md** **PROT6** cross-link; **corpus_systems.md** interpretation block; regression **RS-CH64-001**.)*
- [x] Add **science and scientific method** as key references for decision-making (epistemic / evidence norms consistent with Truth and Chapter Two verification discipline). *(Done **2026-04-08**, edition **`SC-Corpus-2026.04.4`**: **core_constitution.md** Chapter One §3.2 *Science-informed decision support*; Chapter Two §4 *Science-informed evidence alignment*; **Epistemic Integrity** evaluative bullet; regression **RS-EPI-001**.)*
- [x] **Verify / consolidate encryption policy** (high level): reconcile scattered requirements (e.g. observability, security-constrained verification, disclosure limits) into one coherent story without duplicating operational crypto standards across files. *(Done **2026-04-08**, edition **`SC-Corpus-2026.04.4`**: **core_constitution.md** Chapter Two **§7.1** *Cryptographic protection, credentials, and verification*; §8 pointer; **corpus_primitives.md** and **corpus_systems.md** interpretation cross-links; same **RS-EPI-001**.)*
- [x] **Authorized roles for competency and contribution:** For system stewards especially (and systems generally), define or strengthen **authorized roles** that support **caretaker competency**, **cross-functional training**, and **low-friction paths** into meaningful responsibility—aligned with **incentive structures that reward good performance** (Chapter One, section 7.2 — *Incentive Alignment and System Capture*) and **meaningful agency**, without substituting symbolic participation for real influence. Likely touchpoints: Chapter Six / stewardship character, [corpus_systems.md](../corpus_systems.md) steward tiers and competency blocks, governance primitives, and any employment or participation articles where roles and advancement are specified. *(Done **2026-04-08**, edition **`SC-Corpus-2026.04.5`**: **core_constitution.md** Chapter Six, section **5** — *Authorized Roles, Competency Development, and Contribution*; Chapter One, section **7.2** — *Incentive Alignment and System Capture* stewardship/operator incentives; **Article XXIII** *Internal Roles and Material Responsibility*; **corpus_primitives.md** **PROT1** bullet; **corpus_systems.md** **Chapter S3** + interpretation; regression **RS-ROLES-001**.)*

---

## B) Structural synchronization — P0 through P3 sub-items (all checked as of 2026-04-08)

*Original heading context: external review — constitution-shaped; assessment paragraph lived in [TODO.md](../TODO.md) and referred to [doc_architecture.md](../doc_architecture.md) section 13.*

### P0 — Lock the structure map to the corpus

- [x] **Refresh [doc_architecture.md](../doc_architecture.md) end-to-end** for the current Sentient Constitution chapter layout:
  - **Ch 4** — Compliance, Violation, and Standing Model (not rights).
  - **Ch 7** — Foundational rights, Articles V–XIX, and XXI–XXII (update article lists and every owner row that still says “Sentient Constitution Ch 4” for rights). *(Chapter numbering note corrected 2026-04-10.)*
  - **Ch 6** — Legitimacy, Authorization, and Stewardship Character.
  - **Ch 7** — Constitutional change, non-regression, ratification, supremacy, amendment minima, external-law disputes.
  - **Ch 8** — Meta primitives (**treat explicitly** as incorporation bridge / pointer chapter per item below, not as duplicate full text of CP).
- [x] **Disambiguate numbering in the architecture file** between (a) **Sentient Constitution** main-document chapters 1–8 and (b) **corpus_primitives.md** internal “Primitive Chapter One … Four” (and any legacy “Sentient Constitution Ch 6–9 = CP” wording). After Sentient Constitution gained real Ch 6–8, readers must not infer that “Sentient Constitution Ch 6” means only a CP satellite without reading the table.
- [x] **Update dependent rows** in section 2 (corpus roles), section 3 (boundary rules, especially “Annex implements … rights”), section 4 (definitions protocol, precedence bullets, quick index), section 5 (stable IDs + articles table + integration note), section 13 / redundancy tables, and any edition-control language that assumes the old four/five split. *(Section 13 historical pass notes may still mention legacy “Ch 4” for rights; superseded by **2026-04-08** structure note in section 13 and **section 17**.)*

### P0 — Heading hygiene in the main constitution

- [x] In [core_constitution.md](../core_constitution.md), promote **CHAPTER SIX**, **CHAPTER SEVEN**, and **CHAPTER EIGHT** (formerly plain text) to the same heading level as Chapters One–Five (`## CHAPTER …`) so document outline, search, and cross-file navigation match the normative structure.

### P1 — Cross-reference and corpus-wide consistency pass

- [x] **Grep the three canonical corpus files** ([core_constitution.md](../core_constitution.md), [corpus_primitives.md](../corpus_primitives.md), [corpus_systems.md](../corpus_systems.md)) plus [doc_architecture.md](../doc_architecture.md), [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](../CONSTITUTIONAL_REGRESSION_SCENARIOS.md), and [TODO.md](../TODO.md) for stale patterns: “rights in Chapter Four,” “Sentient Constitution Ch 4” meaning rights, “Chapter Four (Articles …)” for the rights layer, “meta … Sentient Constitution Ch 5” where Sentient Constitution Ch 5 is now rights, etc. **Fix or explicitly grandfather** each hit so no binding map implies the pre-reorder layout. *(Regression scenarios correctly use **Chapter Four** for compliance / enforcement realism; architecture **section 13** rows retain historical wording flagged by **2026-04-08** note.)*
- [x] **Reconcile closing / primitive-layer prose** at the end of Sentient Constitution (e.g. “Primitive Chapters One through Four”) with the architecture doc’s single story for **authoritative implementation text** vs **optional merge** (see next subsection).

### P1 — One clear rule: primitives file status + Chapter Ten role

- [x] **Authoritative status rule (one place in Sentient Constitution, one in architecture):** State whether [corpus_primitives.md](../corpus_primitives.md) is (i) **incorporated by reference** as the authoritative implementation layer for named obligation families, with Sentient Constitution Ch 8 (and any Ch 6–7 pointers) as the constitutional hook, or (ii) a **temporary companion** until merge. Remove ambiguous “until or unless merged” vs “authoritative there” tension in favor of one explicit rule. *(Done: Sentient Constitution preamble + Ch 8; CP header; architecture **section 5** integration note.)*
- [x] **Chapter Ten characterization:** If Ch 8 is an **incorporation bridge** (pointer + supremacy glue, not a second full copy of primitives), say so consistently in Sentient Constitution, [doc_architecture.md](../doc_architecture.md), and CP/CS interpretation lines so it is not treated as a full duplicate constitutional chapter in tooling or assurance.

### P2 — Edition and assurance claims

- [x] **Align “edition-stable through Chapter Ten”** ([core_constitution.md](../core_constitution.md) status line) with actual structural lock: either **soften** the claim (e.g. substance-stable for review; map/headings pending) or **defer** the label until P0–P1 items above are complete and verified. *(Status line now ties assurance review to edition id and requires map/cross-refs in lockstep.)*

### P3 — After structure is locked (sub-items only; parent tracked in live [TODO.md](../TODO.md))

- [x] **Pass 1 (partial, 2026-04-08):** CP/CS **Interpretation — Definitions requirements (Chapter Two)** — defers O/E/C, burden, traceability, observability, verification, and anti-evasion discipline to **Sentient Constitution Chapter Two**; CS Protocol C forum-shopping bullet uses full **Sentient Constitution Chapter Two** (disambiguates annex numbering). *(Architecture **section 13**.)*
- [x] **Pass 1a (partial, 2026-04-08):** Chapter One **vocabulary anchor** + CP/CS *Interpretation — Chapter One vocabulary* — added **Contestability**, **Educational Agency (Constitutional)**, **Constitutional Review Body (Constitutional)**, **Collective Accountability Failure (Constitutional)** (plus short-form **corpus** / **accountability** phrasing in CP/CS) to align anchor with Chapter Three entries heavily used by Ch 4–5; CS *Foundational rights* and inline corpus refs updated to **Articles V–XIX, and XXI–XXII** (current Ch 7). *(Logged in architecture **section 13**.)*
- [x] **Pass 2 (partial, 2026-04-08):** CP/CS **Interpretation — Foundational definitions (Chapter Three)** — Ch 3 Interdependent / Clustered Definitions as canonical **term** layer; **core_constitution.md** Ch 6 opening fixes cross-ref so **Article XXIII** sits under **Chapter Five**, not **Chapter Four**. *(Architecture **section 13**.)*
- [x] **Pass 3 (partial, 2026-04-08):** Taxonomy pointer sweep — **Sentient Constitution** Art II **Class** capitalization + **S2**; **CP** PRIM7 **Type I/H** + **S1**; **CP** PROT6 §13 **Type N** + **S1**; **CS** S1 tiered-transparency line ties types to **this Chapter**. *(Architecture **section 13**.)*
- [x] **Pass 4 (partial, 2026-04-08):** CP/CS *Interpretation — Foundational rights* — default **Article …** → **Sentient Constitution Chapter Five** (vs Provisions / PRIM/PROT / other chapters); **CS** Protocol C traceability spells **Sentient Constitution Chapter Four** for compliance model. *(Architecture **section 13**.)*
- [x] **Passes 5–7 (partial, 2026-04-08):** **Pass 5/6:** CP/CS *Interpretation — Meta primitives* — **CP-PCH1** / **CP-PCH2–PCH4** stable IDs. **Pass 7:** **CS** Protocol A → PRIM/PROT home; **Protocol C** §8/§9 order fixed (cross-jurisdiction before class templates); cross-refs disambiguate **Protocol C**, subsection **8**. *(Architecture **section 13**.)*
- [x] **Mini-audit (2026-04-08):** Overlap-zone spot check — **Type N** (Sentient Constitution / CP → **CS S1** only; no drift); **proportionality** in **CS** — two **Protocol A G** / **Protocol B** lines now cite **PROT1** + Sentient Constitution Ch **1–3** where proportionality was bare. Logged in architecture **section 13** (*Mini-audit* paragraph).
- [x] **Mini-audit (2026-04-08, cont.):** **Trust / trustworthiness** — grep + new CP/CS *Interpretation — Trust and trustworthiness* (Ch 1 / Ch 3 / Art IV / PCH1+Ch 8 / PRIM3·4·9–11 / S1); **PRIM8 vs PROT2** — new CP/CS *Interpretation — Intervention and override*. Logged in architecture **section 13** (second *Mini-audit* paragraph).
- [x] **Optional editorial trim (2026-04-08, cont. 1):** **CP Provision V** — Article V restatement compressed (architecture §13 + `evidence/2026-04-08/OPTIONAL_CORPUS_ALIGNMENT_PASS.md`).
- [x] **Optional editorial trim (2026-04-08, cont.):** **CP Provision III** — redress/audit/restorative pointers tightened toward **Art X** / **XIII** / **VII** + **Ch 3**; two governance bullets replace three (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 2):** **CP PRIM4** + **Provision IV** — Article VIII / Ch 3 / Ch 1 §6 deferrals and merged redundant bullets (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 3):** **CP PRIM3** — salience primitive consolidated with Article VIII / Ch 3 / Ch 8 deferral (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 4):** **CP PRIM1** — status/risk/scope representation consolidated with Article VIII / Ch 3 / Ch 2 deferral (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 5):** **CP PRIM2** + **PROT6** opening — comprehensibility vs disclosure + Protocol B; adjudication deferral to Art XIII / Ch 3 (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 6):** **CP PRIM5** + **PRIM6** — dependency + graceful degradation consolidated (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 7):** **CP PRIM7** + **Article XVII** cross-ref fix; architecture **section 5** article table resync; **Transition Framework** + **CS Protocol D** traceability (same evidence log).
- [x] **Optional editorial trim (2026-04-08, cont. 8):** **CP PRIM8** labeled subsections + **PROT2** governance-only layer (defers technical intervention to **PRIM8**); architecture **section 13** + `evidence/2026-04-08/OPTIONAL_CORPUS_ALIGNMENT_PASS.md`.
- [x] **Optional editorial trim (2026-04-08, cont. 9):** **CP PROT3** reflexivity consolidation + duplicate-stack merge; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 10):** **CP PROT4** consolidation + **Provision I** PROT cross-refs; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 11):** **CP PROT5** constrained-secrecy consolidation; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 12):** **CP PROT6** §§1–7 compression (subsection **13** / Type N anchor unchanged); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 13):** **CP PROT6** §§8–12 (CUL / systemic / structural transparency); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 14):** **CP PRIM9–PRIM11** integrity cluster; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 15):** **CP PRIM12–PRIM13** reversibility and retention lifecycle; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 16):** **CP PRIM14** adversarial robustness; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 17):** **CP PRIM15** + **Provision VI**/**PROT6** coupling; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 18):** **CP Provision VI** main-body compression (**Article XX** block + ladder/cross-border); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 19):** **CP PROT-DRP** + **Provision II** quorum; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 20):** **CP PCH1** intro + **Provision II** §**1** (*Distribution of Power*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 21):** **CP Provision I** + **PCH1** *Meta Primitive: Trust and Trustworthiness*; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 22):** **CP PCH1** *Supremacy* + *Trust Modeling* (incl. proxy/metric) + *Incentive Alignment* Meta Primitives; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 23):** **CP PCH1** *Meta Primitive: Failure Integrity*; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 24):** **CP Provision V** remainder (standing/resources/challenge/monitoring/scope); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 25):** **CP Provision IV** tradeoffs / temporal / pluralism / timeouts-bans; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 26):** **CP PROT6** §**13** (*Stakeholder Scope and Disclosure Targeting*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 27):** **CP Provision 1** (*Good Standing*) + **Provision 2** (*Resource Transfer*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 28):** **CP Provision 3** (*Transitional Stewardship*) + **Provision 4** (*External Systems*); architecture **section 13** + same evidence log.
- [x] **Optional editorial — CP batch closure log (2026-04-08, cont. 29):** architecture §13 *CP editorial batch closure* + `OPTIONAL_CORPUS_ALIGNMENT_PASS.md` **Batch closure** section + **Structural sync** *Still optional* line refresh; P3 parent note updated (**holistic** three-file sweep still open).
- [x] **Optional editorial trim (2026-04-08, cont. 30):** **CS Protocol A** §§**1–2**; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 31):** **CS Protocol A** §§**3–5**; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 32):** **CS Protocol A** subsection **F** (*Non-Experimental Systems*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 33):** **CS Protocol A** subsection **G** (*Governance Continuity…*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 34):** **CS Protocol B** opening block (post-header through **Periodic simplification**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 35):** **CS Protocol C** §§**2–9**; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 36):** **CS Chapter S1** *Introductory provisions*; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 37):** **CS Chapter S1** roman **III–V** (through cross-domain subsection **8**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 38):** **CS Chapter S1** roman **VI** (subsections **1–4**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 39):** **CS Chapter S1** roman **VII** (*Data Classifications*, **Types C/G/H/I/N/S**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 40):** **CS Chapter S2** preamble (through **Resilience and continuity requirements**, before **Class A**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 41):** **CS Chapter S2** **Class A** through **Class P**; architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 42):** **CS Chapter S2** *System Classification Governance…* through item **8** (*Integrated Risk Governance*); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 43):** **CS Chapter S3** (*Critical System Stewardship*, full chapter through closing dependency paragraph); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 44):** **CS Protocol S4** (*Adaptive Sustainability and Ecosystem Resilience*, sections **A–H**); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 45):** **CS Protocol S5** (*Resource Allocation and Funding Stewardship*, full protocol body); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 46):** **CS Protocols T, R, D** (transition; subversion response; decentralized continuity / partition resilience); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 47):** **CS** — **Protocol A**, **Protocol C**, **Chapter S1**/**S2** subsection headings unified to bold-labeled lines (no remaining **`###`** in [corpus_systems.md](../corpus_systems.md)); architecture **section 13** + same evidence log.
- [x] **Optional editorial trim (2026-04-08, cont. 48):** **CS Chapter S1** roman sections **I–VII** → bold-labeled; architecture **section 13** + same evidence log.

---

## C) P3 parent item (tracked in live [TODO.md](../TODO.md))

The **parent** checkbox for holistic grep-per-theme dedup across all three corpus files is **not** closed in this archive. After **2026-04-08** maintenance, it remains the only open structural-sync item in active [TODO.md](../TODO.md); close it only after an explicit custodian decision or a new edition cut.
