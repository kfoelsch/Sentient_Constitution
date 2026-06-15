# Constitution document architecture

This file is the **map of the territory** for the constitution corpus. Use it when editing the numbered `core_*` Sentient Constitution files (inventory in [README.md](README.md)), plus [corpus_joint_structure.md](corpus_joint_structure.md) and its linked `corpus_joint_structure/` subfiles, [corpus_systems.md](corpus_systems.md) and its linked `corpus_systems/` subfiles, [corpus_institutions.md](corpus_institutions.md) and its linked `corpus_institutions/` subfiles, and [corpus_forum.md](corpus_forum.md) and its linked `corpus_forum/` subfiles, to decide where new material belongs, how to cross-reference, and what is still unwritten. Those Markdown files are the **authoritative corpus**. They are defined as **Corpus** in Chapter Five — [§1 *Independent Definitions*](core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md); [§2 *Semi-independent Definitions*](core_05-05_definitions_b_semi_independent.md#section-2-semi-independent-definitions) in [core_05-05_definitions_b_semi_independent.md](core_05-05_definitions_b_semi_independent.md); and [§3 *Dependent clusters*](core_05-05_definitions_c_dependent_clusters.md#section-3-dependent-clusters-clustered-definitions) in [core_05-05_definitions_c_dependent_clusters.md](core_05-05_definitions_c_dependent_clusters.md) — and they are where structure, headings, and cross-references live. Retired bookmark-only wrapper names (`core_constitution.md`, `core_definitions.md`, `core_amendment.md`) may appear in older notes or forks; they are **not** authoritative editing surfaces—always change the numbered `core_*` files.

---

## 1. Purpose

- **Avoid duplication** of definitions, rights, and operational rules across files. **Section 4** (*Project-wide definitions protocol*) states where each kind of definition may live.
- **Preserve dependency order**: core principles and terms before implementation-file classifications, institutional law, and protocols.
- **Track gaps**: missing chapters, planned articles, and stable IDs for implementation-file sections so renumbering does not break references.
- **Keep human and AI readable**: maintain substantive content so humans can read and reason about it directly, and tools (including AI assistants) can navigate it reliably—using consistent headings, stable section IDs, and explicit cross-references as already encouraged elsewhere in this map. If you add **auxiliary exports** (for example plain text or PDF), treat them as **non-authoritative** outputs derived from the Markdown corpus so they cannot silently diverge as a second source of truth.
- This file is intentionally written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.

---

## 1A. Canonical Filename Convention

To keep paths OS-friendly and automation-safe across environments, use this corpus filename rule:

- Use `snake_case`/underscore-style names for canonical files (no spaces in filenames).
- Use the exact canonical filenames in prose, links, scripts, and cross-file references.
- If a file is renamed, update all references in the same change.
- Avoid URL-encoded space links (`%20`) for corpus filenames; link directly to canonical underscore names.

For the numbered Sentient Constitution core files, use this filename pattern:

- `core_<start>-<end>_<short_owner_label>.md`
- use zero-padded chapter numbers,
- use `-` inside the chapter-range segment,
- repeat the chapter number for single-chapter files so the family lines up visually,
- use `_` between the chapter-range segment and the text label.

Current examples for that convention include:

- `core_00-01_principles.md`
- `core_02-04_definition_mechanics.md`
- `core_05-05_definitions_a_independent.md`
- `core_05-05_definitions_b_semi_independent.md`
- `core_05-05_definitions_c_dependent_clusters.md`
- `core_06-06_standing_assessment.md`
- `core_07-07_standing_integration.md`
- `core_08-08_misconduct.md`
- `core_09-09_forum.md`
- `core_10-10_rights_part_a.md`
- `core_11-11_governance.md`
- `core_12-14_amendment.md`
- `core_15-15_incorporation.md`

**Chapter heading style (instrument opener exception):** elsewhere in the numbered `core_*` files, chapter headings use spelled-out numbers (`CHAPTER NINE`, `CHAPTER FIFTEEN`, and so on). `core_00-01_principles.md` retains numeric headings (`CHAPTER 00`, `CHAPTER 01`) as the instrument-opening convention; stable anchors such as `#chapter-00-preamble--foundational-requirements` and `#chapter-01-principles-and-constraints` must not be renamed without a compatibility migration.

Canonical corpus filenames (authoritative for edits and for cross-references in this map unless a line explicitly discusses packaging):

- `core_00-01_principles.md`
- `core_02-04_definition_mechanics.md`
- `core_05-05_definitions_a_independent.md`
- `core_05-05_definitions_b_semi_independent.md`
- `core_05-05_definitions_c_dependent_clusters.md`
- `core_06-06_standing_assessment.md`
- `core_07-07_standing_integration.md`
- `core_08-08_misconduct.md`
- `core_09-09_forum.md`
- `core_10-10_rights_part_a.md`
- `core_10-10_rights_part_b.md`
- `core_10-10_rights_part_c.md`
- `core_10-10_rights_part_d.md`
- `core_11-11_governance.md`
- `core_12-14_amendment.md`
- `core_15-15_incorporation.md`
- `corpus_systems.md`
- `corpus_institutions.md`
- `corpus_forum.md`
- `corpus_forum/*.md`
- `corpus_joint_structure.md`
- `corpus_joint_structure/*.md`

**Retired Sentient-Constitution wrapper names (bookmark-only; not in every checkout):** `core_constitution.md`, `core_definitions.md`, `core_amendment.md` — do not treat these as canonical paths for new edits.

## 1B. Rename Readiness Gate (Conservative)

Filename clarity improvements are permitted only after a dedicated rename-readiness pass. Until that gate is satisfied, candidate names remain planning artifacts only.

Required gate conditions before any rename:

1. Complete reference audit across Sentient Constitution / corpus_joint_structure / corpus_systems / corpus_institutions / corpus_forum, architecture/process docs, implementation notes, and evidence artifacts (treat any retired implementation-layer compatibility links as aliases to the joint-structure home).
2. Same-change update of all affected references (prose links, script/tooling paths, and checklist pointers).
3. Evidence artifact under `evidence/<date>/` containing pre-fix mismatch list and post-fix confirmation.
4. Explicit compatibility decision (aliases/pointers vs strict migration), recorded in TODO and evidence notes.
5. Edition/custody decision recorded for whether rename occurs as part of a named corpus cut.

---

## 2. Corpus roles (single source of truth)

**Numbering note (read once):** The **Sentient Constitution** is authoritative in the numbered `core_*` files read as one instrument (see [README.md](README.md)). When a passage says only “Chapter Eleven,” disambiguate by filename: **Sentient Constitution Chapter Eleven** is *Governance Legitimacy...* in `core_11-11_governance.md`.

| Topic | Primary owner | May reference |
|--------|----------------|---------------|
| Foundational values; safety / truth / trust / freedom hierarchy; conflict resolution among values | **Core** — Sentient Constitution Ch 1 (`core_00-01_principles.md`) | Sentient Constitution Ch 2–4 (`core_02-04_definition_mechanics.md`) and Ch 5 for definition and verification discipline |
| Definition structure (O/E/C components; internal component integrity) | **Core** — Sentient Constitution Ch 2 (`core_02-04_definition_mechanics.md`) | Ch 3–5 |
| Interpretation integrity, anti-evasion, observable non-compliance | **Core** — Sentient Constitution Ch 3 (`core_02-04_definition_mechanics.md`) | Ch 2, Ch 4–5 |
| Burden of proof, traceability, observability, security-constrained verification, accessibility | **Core** — Sentient Constitution Ch 4 (`core_02-04_definition_mechanics.md`) | Ch 2–3, Ch 5 |
| Canonical definitions of constitutional terms (§1 Independent, §2 Semi-independent, §3 Dependent clusters) | **Core** — Sentient Constitution Ch 5 | Ch 2–4 |
| Contribution state, violation nature, standing effect (two-axis model: Axis I — contribution state; Axis II — violation nature; **standing effect** integrates **verified** inputs from both; **Chapter Nine** forums process **allegations** and **claims**, not standing calculus) | **Core** — Sentient Constitution Ch 6 and Ch 7 (`core_06-06_standing_assessment.md`; `core_07-07_standing_integration.md`) | Ch 1–5, Ch 8–10 where top-end anti-constitutional classification, forums, or rights interact |
| Anti-constitutional misconduct (final Violation Axis **s = 7, 8, and 9**; unified-incident gravity; due-process and cross-chapter discipline) | **Core** — Sentient Constitution Ch 8 (`core_08-08_misconduct.md`) | Ch 1–7, Ch 12–14 (change path); Ch 10 (rights, justice) |
| Forums and jurisdiction (forum families, default venue, cross-forum anti-self-judging) | **Core** — Sentient Constitution Ch 9 (`core_09-09_forum.md`) | Ch 1–8, 10; Ch 12–14; owner corpus as needed |
| Forum operations (panel formation, recusal, review lanes, forensic/investigative support, technical specialist forums, performance, continuity) | **Implementation file** — [corpus_forum.md](corpus_forum.md) wrapper plus `corpus_forum/` subfiles | Sentient Constitution Ch 9, Art XII-B, Art XIV, Art XXI, Art XXII; `corpus_institutions.md`, `corpus_joint_structure.md`, and `corpus_systems.md` as needed |
| Cross-implementation joint structure (integration interfaces, joint requirements, read-with ordering among CJS / CS / CI / CF; joint operational definitions that exist only at those interfaces) | **Implementation file** — [corpus_joint_structure.md](corpus_joint_structure.md) wrapper plus `corpus_joint_structure/` subfiles | `corpus_systems.md`, `corpus_institutions.md`, `corpus_forum.md`; Sentient Constitution Ch 8–10 where applicable; CJS-5 text does not own canonical constitutional definitions |
| Foundational Rights (Articles I–XXV) | **Core** — Sentient Constitution Ch 10 (`core_10-10_rights_part_a.md` through `core_10-10_rights_part_d.md`) | Ch 1–9 |
| Constitutional contract, legitimacy, authorization, stewardship | **Core** — Sentient Constitution Ch 11 (`core_11-11_governance.md`) | Ch 1–10, Ch 12–14, `corpus_joint_structure.md`, `corpus_systems.md`, and `corpus_institutions.md` as needed |
| Non-regression and substantive amendment validity | **Core** — Sentient Constitution Ch 12 (`core_12-14_amendment.md`) | Ch 1–11, 13–14; `corpus_joint_structure.md`, `corpus_systems.md`, and `corpus_institutions.md` as needed |
| Expansion, supremacy relative to other norms, external legal orders | **Core** — Sentient Constitution Ch 13 (`core_12-14_amendment.md`) | Ch 1–12, 14; implementation corpus as needed |
| Amendment, ratification, procedural validity, amendment requirements | **Core** — Sentient Constitution Ch 14 (`core_12-14_amendment.md`) | Ch 1–13; `corpus_joint_structure.md`, `corpus_systems.md`, and `corpus_institutions.md` |
| Cross-domain integrity routing and shared operational clusters | **Implementation file** — [corpus_joint_structure.md](corpus_joint_structure.md) **Cross-domain implementation layer** (**CJS-4.4**, **CJS-5**) | Ch 1–15, CS S1/S2/Protocol A as needed; avoid duplicating Protocol B *engineering* checklist unless harmonizing |
| Data types, domains, lifecycle, separation, restricted handling | **Implementation file** — CS Ch S1 | Ch 5–6, 9, Ch 6 where compliance model applies |
| System classification (impact / dependency / risk; classes A/B/C/L/P; reclassification; governance of classification) | **Implementation file** — CS Ch S2 | Ch 5–6, 9, CS Ch S1 |
| Dev/test/stage/prod environments; progressive deployment; ACA; non-experimental engineering requirements | **Implementation file** — Protocol A | Ch 6–8, CS Ch S2 |
| Comprehensibility, complexity audits, modular architecture at **protocol** level | **Implementation file** — Protocol B | Defers to Chapter Five definitions and **CJS-5** operational clusters in [corpus_joint_structure.md](corpus_joint_structure.md); stricter requirement wins (see Protocol B header in CS). |
| Critical system stewards (CSS-A/B/C); organizational dependency | **Implementation file** — CS Ch S3 | CS Ch S2, Ch 5–6, 9 |
| Adaptive sustainability; ecosystem resilience; dynamic allocation response | **Implementation file** — Protocol S4 | Protocol S5, Ch 9 Art XVII / XVIII |
| Funding stewardship; dependent systems maps; allocation categories; reauthorization | **Implementation file** — Protocol S5 | Protocol S4, Ch 9 Arts IX, XI, XII, XIV, XVI, XVII |
| Institutional governance architecture | **Implementation file** — [corpus_institutions.md](corpus_institutions.md) | Formation, delegation custody, assurance lanes, and sanctions/dissolution. Cross-links include Ch 6-14, **CJS-5A**, **CJS-5C**, CS S2/S3, and Protocol S5. This row also tracks the **CI-15** vulnerable personal services and **Article X-C** interface, **Sentient Constitution Ch 9 Art IV-C** as the rights single home, and the CS opening **market-mediated personal services** interpretation. Read with [corpus_joint_structure.md](corpus_joint_structure.md) where cross-implementation structural integration is material. |

**Abbreviations:** `CS` = [corpus_systems.md](corpus_systems.md) (systems implementation file; **do not** use the bare phrase *Constitutional Systems* in body text — see *Ambiguous implementation labels* under *Plain-Language Vocabulary Guardrails*). `CI` = [corpus_institutions.md](corpus_institutions.md) (institutional implementation file). `CF` = [corpus_forum.md](corpus_forum.md) (forum implementation file). `CJS` = [corpus_joint_structure.md](corpus_joint_structure.md) (joint-structure implementation file, including **CJS-4** (*Specific joint interlocks and shared abstractions*) and **CJS-5** (*Implementation and cross-implementation operational cluster library*)). Sections in **CI** are labeled **CI-1** (*Scope, purpose, and legitimacy interface*) through **CI-26** (*Compliance mapping and stable registry*) (with subsections **CI-*n*.*m*** and nested subsections **CI-*n*.*m*.*p***). **CI-2** (*Implementation integration map*) is the institutional integration index; **CI-3** (*Institutional design, separation of powers, and authority custody*) follows **CI-2**. Sections in **CF** are labeled **CF-1** (*Scope, authority, and boundary rules*) through **CF-16** (with subsections **CF-*n*.*m*** and nested subsections **CF-*n*.*m*.*p***). **CF-2** (*Implementation integration map*) is the forum integration index; substantive forum doctrine runs **CF-3** through **CF-16**. **CS-2** (*Implementation integration map*) is the systems integration index; substantive systems text remains **Chapter S1** through **Chapter S3** and named protocols. Sections in **CJS** are labeled **CJS-1** (*Scope, purpose, and boundary interface*) through **CJS-5** (with subsections **CJS-*n*.*m*** and nested subsections **CJS-*n*.*m*.*p***). Do not append letter suffixes to subsection labels in **CI**, **CF**, or **CJS**; use the next dotted numeric level instead, for example **CF-16.1.1** rather than **CF-16.1A**.

**Section-abbreviation descriptor rule:** Avoid naked implementation-section abbreviations by default in body prose. On first meaningful use within a paragraph, list item, table row, or local discussion, pair the stable label with its descriptor or function, using a form such as **CF-3 — Forum formation, forum-structure mapping, and chamber structure**, **CJS-R02** (*forum chambers, divisions, and designated panels*), or **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*). Later mentions in the same immediate context may use the stable label alone where the descriptor remains obvious. Exceptions are acceptable for headings, compact index tables whose adjacent column supplies the descriptor, generated trace / D/E/C widgets, commit messages, stable-ID inventories, mermaid diagrams, and dense cross-reference lists where adding every descriptor would materially reduce scanability.

**CJS filename convention:** files inside `corpus_joint_structure/` use the `cjs_` prefix and an ordinal navigation stem, matching the numbered `core_*` filename convention. The ordinal stem is a file-order/navigation aid only; it does not change stable in-text labels such as **CJS-1** (*Scope, purpose, and boundary interface*), **CJS-2** (*Implementation integration map*), **CJS-3** (*Joint structural obligations (cross-domain requirements)*), **CJS-4** (*Specific joint interlocks and shared abstractions*), or **CJS-5** (*Implementation and cross-implementation operational cluster library*).

**Opening trilogy (all companion folders):** each of `corpus_joint_structure/`, `corpus_systems/`, `corpus_institutions/`, and `corpus_forum/` opens with the same three-file reader architecture: **`*_00`** registry and reading rules (front door, section-family table, folder identifier preamble where applicable); **`*_01`** scope, purpose, and boundary interface; **`*_02`** implementation integration map (domain router indexing **CJS-2.1**, not a competing cross-implementation table). Substantive law begins at ordinal **03** or the domain's first protocol/chapter file after **`*_02`**. Cross-implementation routing remains authoritative in **CJS-2.1**.

**CF filename convention:** files inside `corpus_forum/` use the `cf_` prefix and an ordinal navigation stem, matching the CJS subfile convention. The ordinal stem is a file-order/navigation aid only; it does not change stable in-text labels such as **CF-1** (*Scope, authority, and boundary rules*), **CF-2** (*Implementation integration map*), **CF-3** (*Forum formation, forum-structure mapping, and chamber structure*), or **CF-16** (*Forum staffing, reserve capacity, shared administration, structural review, and structural records*).

**CI filename convention:** files inside `corpus_institutions/` use the `ci_` prefix and an ordinal navigation stem, matching the CJS and CF subfile conventions. The ordinal stem is a file-order/navigation aid only; it does not change stable in-text labels such as **CI-1** (*Scope, purpose, and legitimacy interface*), **CI-2** (*Implementation integration map*), **CI-3** (*Institutional design, separation of powers, and authority custody*), **CI-12** (*Transparency, participation, and accessible pathways*), or **CI-26** (*Compliance mapping and stable registry*).

**CS filename convention:** files inside `corpus_systems/` use the `cs_` prefix and a navigation stem, matching the CJS, CI, and CF subfile conventions. The stem is a file-order/navigation aid only; it does not change stable in-text labels such as **CS-2** (*Implementation integration map*), **Chapter S1** (*Information Types and Handling*), **Chapter S2** (*System Classification and Handling*), **Chapter S3** (*Critical System Stewardship*), or named protocols (**Protocol A**, **Protocol B**, **Protocol C**, **Protocol S4**, **Protocol S5**, **Protocol T**, **Protocol R**, **Protocol D**).

**Pre-adoption numbering preference:** until initial adoption of the constitution, prefer clean renumbering over compatibility-preserving suffixes or legacy anchor retention when renumbering improves readability, maintainability, or release quality. After initial adoption, treat stable references as stronger constraints and use compatibility-preserving moves unless the adopting authority approves a renumbering migration.

**Corpus navigation footer convention:** every active corpus Markdown file in the reading chain ends with a navigation-only, non-operative footer. Maintain the sequence from `README.md` through the numbered `core_*` files, the joint-structure wrapper and active `cjs_00` through `cjs_05*` subfiles, the systems wrapper and active `cs_00` through protocol/chapter subfiles, the institutions wrapper and active `ci_00` through `ci_26` subfiles, the forum wrapper and active `cf_00` through `cf_16` subfiles, and this architecture map back to `README.md`.

**Footer policy (by file class):**

| File class | Previous link | Next link |
|---|---|---|
| `README.md`, numbered `core_*` files, companion wrappers (`corpus_*.md` at repo root), `doc_architecture.md` | No | Yes |
| First subfile in each companion folder (`cjs_00`, `cs_00`, `ci_00`, `cf_00`) | No | Yes |
| All other companion subfiles | Yes | Yes |

**Footer formatting template:** use one horizontal rule, a blank line, then each navigation line as its own paragraph (blank line between `**Previous file:**` and `**Next file:**` when both are present). Optional terminal `*Corpus alignment:*` edition note sits **above** the final navigation block, separated by `---` on both sides.

Next-only (core, wrapper, registry opener, or `README.md` / `doc_architecture.md`):

```markdown
---

**Next file:** [filename](path)
```

Bidirectional (companion subfiles after the registry opener in each folder):

```markdown
---

**Previous file:** [prev.md](prev.md)

**Next file:** [next.md](next.md)
```

**Regression:** `make footer-audit` (or blocking `make regression`) runs `tools/footer_audit.py` against the canonical reading chain.

**Authority stack (quick reference):**
1. **Binding constitutional source:** the numbered `core_*` constitutional files read together as one instrument. Chapters Two through Four meaning and validity constraints live in `core_02-04_definition_mechanics.md`; Chapter Five lives in `core_05-05_definitions_a_independent.md` (§1), `core_05-05_definitions_b_semi_independent.md` (§2), and `core_05-05_definitions_c_dependent_clusters.md` (§3).
2. **Binding incorporated implementation:** designated obligations in `corpus_joint_structure.md` (including **Cross-domain implementation layer**), `corpus_systems.md`, `corpus_institutions.md`, and `corpus_forum.md` within valid adoption scope and Sentient Constitution incorporation hooks.
3. **Authoritative but non-constitutional process/map text:** this architecture file, TODO and workflow trackers, regression catalogs, and evidence logs unless an adopting instrument explicitly incorporates a specific artifact.
4. **Conflict order:** Sentient Constitution values/rights and Sentient Constitution Ch 2–5 constraints control meaning; use the Chapter Five **Authority Stack and Internal Hierarchy** cluster to separate source-layer status from last-resort interpretive hierarchy. Operational layers implement them and may be stricter where the corpus already provides stricter-rule logic.

---

## 3. Boundary rules

1. **Core owns** normative *why* and *what*: values, rights, definition rules, defined terms, and cross-cutting meta obligations.
2. **Implementation files own** *how* at engineering, ecosystem, institutional, forum-operational, and cross-implementation joint-structure scale: data handling taxonomies, system classes, deployment patterns, funding mechanics, institutional rules, forum procedures, protocol-level checklists, and joint integration requirements where implementation files must interlock.
3. **No duplicate definitions** of the same term in both corpora. Implementation files *apply* Sentient Constitution Ch 5 terms; use this file or a single glossary subsection if a shorthand (e.g. “substrate”) needs a pointer.
4. **Stricter wins:** If core and implementation text appear to conflict, **core values and rights prevail**. If two implementation rules conflict (e.g. personal/creative sandbox vs non-experimental), **higher material impact and stricter classification** govern (see opening of [corpus_systems.md](corpus_systems.md)).
5. **Implementation files implement Sentient Constitution rights (Chapter Ten):** Articles I–XXV in **Chapter Ten** state core rights (including **Article XXV** transition and re-baselining); implementation protocols, institutional law, and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters supply operational detail. Where implementation text expands a theme (e.g. lifecycle under Protocol A), it **implements** the corresponding article and must not contradict **Chapter Ten** or **Chapters One through Nine** (including the compliance model in **Chapter Six** and final **Violation Axis s = 7, 8, or 9** slot-classification rules in **Chapter Eight**).

---

## 4. Project-wide definitions protocol (pinned)

This subsection **pins** how “definitions” work across the corpus so editors, reviewers, and tools share one discipline.

### What counts as a “definition” here

- **Hard definitions** (full semantic + evaluative + compliance structure): the only primary homes for new constitutional terms are:
  - **Sentient Constitution Chapters Two through Four** in `core_02-04_definition_mechanics.md` for O/E/C structure, interpretation integrity and observable non-compliance, burden of proof, traceability, observability, and verification
  - **Chapter Five** in `core_05-05_definitions_a_independent.md` (§1), `core_05-05_definitions_b_semi_independent.md` (§2), and `core_05-05_definitions_c_dependent_clusters.md` (§3) — **Independent Definitions** in §1, **Semi-independent Definitions** in §2, and **Dependent clusters** (joint-invocation groups, including full O/E/C where the cluster body owns the term) in §3 — see **Chapter Five — single-definition rule** under **Order and alphabetization (Chapter Five)** below
- **Values language** (how principles interact): **Chapter One**, with the **vocabulary anchor** and **cluster index** at the **end of Chapter One** under the heading **Reference: Chapter Five vocabulary anchor and cluster index**. That block maps Chapter One priority terms to Chapter Five **§1** Independent Definition names and lists the major Chapter Five **§3** dependent-cluster groupings that must be traced under Chapters Two through Four when materially relevant.
- **Contribution / standing model** (contribution state, violation nature, standing effect): **Chapter Six** and **Chapter Seven**; **standing** applies only to **verified** standing inputs (**demonstrable** Axis I; [**verified violation findings**](core_05-05_definitions_b_semi_independent.md#verified-violation-findings) for Axis II — **section 2** *Verified inputs for standing* in [core_06-06_standing_assessment.md](core_06-06_standing_assessment.md) and integration rules in [core_07-07_standing_integration.md](core_07-07_standing_integration.md)). **Chapter Nine** owns **forum** process for **allegations** and **claims**; that layer **must not** be folded into standing’s input model. Procedural scoring and operational workflows live in **CJS** and **CS**, which must remain consistent with Ch 6’s constitutional meaning. Interoperable operational defaults for standing composites (including **daily** **half-life** recency weighting for **Axis I** contribution-linked credit under [**Chapter Seven §4.1**](core_07-07_standing_integration.md#38-standing-integration-contribution-and-violation-nature) — **no** **weight** **floor** — and **no** time discount for **unresolved** **Axis II** inputs) are stated under **Chapter Six standing composites** in [corpus_systems.md](corpus_systems.md), **read with** [core_06-06_standing_assessment.md](core_06-06_standing_assessment.md), [core_07-07_standing_integration.md](core_07-07_standing_integration.md), and [**contribution recency weighting**](core_07-07_standing_integration.md#contribution-recency-weighting).
- **Rights language**: **Chapter Ten** (Articles I–XXV); implementation files and CJS-5 (*Implementation and cross-implementation operational cluster library*) clusters **cite** articles, they do not invent parallel rights.
- **Cross-domain integrity routing** (trust, incentives, proxy metrics, failure integrity at system level): **corpus_joint_structure.md** **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters. **Sentient Constitution Chapter Fifteen** is the incorporation bridge and must be read together with **Chapters 1, 6–10, and 11–13** as applicable. **CJS-5** (*Implementation and cross-implementation operational cluster library*) implements domain obligations without redefining Ch 5 terms.
- **Operational taxonomies** (data Types, system Classes, dependency types, steward tiers): **corpus_systems.md** Chapters **S1, S2, S3** only.
- **Protocols and profiles**: **corpus_systems.md** Protocols A, B, S4, S5 — **instances** of upstream rules, not new definition homes.
- **Joint operational definitions** (cross-implementation interface terms that govern routing, interlock, overlap handling, shared-fact evaluation, or combined satisfaction across **CJS / CS / CI / CF**): **corpus_joint_structure.md** only. These are operational and integrative, not canonical constitutional definitions. They must stay local to joint structure unless elevated into **Chapter Five** because they become cross-cutting constitutional meaning, or moved into a **primary owner** because they are actually single-file operational terms (see **CJS-2.1** (*Topic router (stable IDs)*) for routing).

### CJS operational-definition owner rule

`corpus_joint_structure.md` is the official owner for **operational definitions that are inherently joint**: terms that arise only because two or more implementation files must be read together on the same facts, and whose role is to coordinate routing, sequencing, interlock, shared-fact evaluation, stricter-wins handling, or combined implementation satisfaction.

Within the CJS subfiles, place reusable joint operational definitions in **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters. Rule/interlock sections such as **CJS-4** (*Specific joint interlocks and shared abstractions*) should point to the applicable **CJS-5** (*Implementation and cross-implementation operational cluster library*) term and the **primary owner** (**CI**, **CS**, or **CF**, as named in **CJS-2.1**) rather than defining the term inline.

Use **CJS** for a term only when all of the following are true:

1. the term has no stable meaning outside a cross-implementation interface;
2. the term regulates how **CJS**, **CS**, **CI**, and/or **CF** interact rather than restating one file's local doctrine;
3. the term is operational or integrative rather than constitutional in meaning;
4. keeping it outside **CJS** would create duplicate interface language across multiple implementation files.

Do **not** use **CJS** as the default home for:

1. canonical constitutional terms or clustered traceability concepts that belong in **Sentient Constitution Chapter Five**;
2. true reusable CJS-5 (*Implementation and cross-implementation operational cluster library*) operational clusters or corpus-wide drafting patterns that belong in `corpus_joint_structure.md`;
3. taxonomies, thresholds, procedures, or operational terms that are actually local to **CS**, **CI**, or **CF**.

Escalation / relocation rule:

1. If a **CJS** term starts determining constitutional meaning, scope, satisfaction conditions, or anti-narrowing effect across the corpus, elevate it to **Chapter Five** and replace CJS restatements with pointers.
2. If a supposed **CJS** term turns out to be used materially in only one implementation file, relocate it to that file and leave **CJS** with a pointer-only interface note if needed.
3. If a supposed reusable label is mostly functioning as a joint interface cluster rather than a reusable implementation, prefer **CJS-5** (*Implementation and cross-implementation operational cluster library*) over a standalone label.

### Chapter Five admission gate (definitions-only)

When adding or revising an Independent, Semi-independent, or Dependent-cluster definition in Sentient Constitution Chapter Five:

1. Keep only the constitutional concept and its O/E/C validity boundary.
2. Do not embed primary institutional architecture, appointment/rotation mechanics, procedural sequencing, or governance workflow detail.
3. If owner-layer mechanics are materially required, cite the owner home (Sentient Constitution Ch 6–14, CJS-4.4 (*Cross-implementation trust integrity (joint operation model)*), CJS-5 (*Implementation and cross-implementation operational cluster library*), CS S1-S3 / protocols) instead of restating those mechanics in the definition.
4. Treat violations of this gate as a structural duplication risk and correct by de-bundling before publication cut.

**Regression (automated):** `make ch5-definitions-gravity-audit` or blocking `make regression` runs `tools/ch5_definitions_gravity_audit.py`, covering **RS-CH5-GW-001..004** in the regression-scenario catalog (archived at [archive/CONSTITUTIONAL_REGRESSION_SCENARIOS_ARCHIVED_2026-05-08.md](archive/CONSTITUTIONAL_REGRESSION_SCENARIOS_ARCHIVED_2026-05-08.md); regenerate a live root catalog with `tools/emit_regression_scenarios.py` before relying on `tools/scenario_audit.py`). The gravity audit covers authority/procedure/machinery regexes plus an Article-citation density threshold for parallel **Chapter Ten** rights gloss risk. When the live root catalog is present, the same blocking `make regression` run includes `tools/scenario_audit.py`, which checks the regression matrix and the **section 10.5** `SCORING-v1` run snapshot (weighted overall must match the six dimensions). Run `make regression-full` when you also want `tools/readability_audit.py` as a separate editorial gate for prose-density and readability hotspots.

### Chapter Five cross-link proof method

Use a narrow, regression-first method when adding or normalizing Chapter Five cross-definition links:

1. Identify one concrete definition entry and one exact `O`, `E`, or `C` sentence where a cross-link is materially doing legal or interpretive work.
2. Add the inline Markdown link in that sentence itself; do not count a trace block, heading, or standalone `Read with:` line as proof of in-body cross-linking.
3. Add or update an automated audit that removes the local trace/details block before checking for the expected link so the test proves body-level linking rather than header-only navigation.
4. Prefer a single explicit proof case first. After that case passes, expand term-by-term rather than trying to validate all Chapter Five cross-linking in one broad change.

Use this method to avoid ambiguous "cross-linking exists somewhere in the entry" results. The architectural success condition is narrower: at least one named definition must have one specifically justified cross-definition link inside its operative `O` / `E` / `C` body text, and that condition must be machine-checked in blocking regression.

**Regression (automated):** `make ch5-in-body-crosslink-audit` or blocking `make regression` runs `tools/ch5_in_body_crosslink_audit.py`. The current proof case is `Accountability`, whose `E` sentence must retain in-body links to `Auditability` and `Contestability` after the local trace block is stripped from the parsed definition entry.

### Citing corpus_systems.md from Sentient Constitution

Within the numbered Sentient Constitution `core_*.md` files, cite implementation taxonomy chapters as **[corpus_systems.md](corpus_systems.md), Chapter S1 — Information Types and Handling**. Apply the same pattern to **S2 — System Classification and Handling**, **S3**, and named protocols. Do not use bare **Chapter S1** or **Chapter S2** references. Those are not Sentient Constitution chapter numbers and are easy to misread as a gap in the Sentient Constitution.

### Reader-Guidance Discipline (Navigation Load Control)

To reduce comprehensibility failures under pressure, apply these rules in constitutional-scope edits:

1. High-load Sentient Constitution chapters (especially **Chapters Five through Ten** in the integrated map) must begin with a short `Where this lives` locator naming constitutional owner, implementation owner, and anti-relocation rule.
2. Cross-layer pointers must identify both owner and purpose (for example: "`corpus_joint_structure.md`, `corpus_systems.md`, and `corpus_institutions.md` implement designated mechanics for this constitutional floor").
3. Definition-only and validity-only zones must not absorb procedural or staffing workflow text; point to owner layers instead.
4. Frontmatter guidance in the Sentient Constitution must include a compact under-pressure reading path (source-of-truth, when to consult implementation corpus files, conflict order, and adoption/custody checkpoints).
5. Architecture and TODO updates must accompany any guidance-pattern changes to preserve auditability and future consistency.
6. **Chapter-opening reader guidance widgets:** Where a chapter opening is **non-operative** for navigation, reading order, “where this lives,” file position, transition notes, or plain-language reading notes, present that material in a collapsible `<details>` block that is **collapsed by default**. The summary line should use the same blue styling family as local `Trace` widgets and should remain descriptive when collapsed (for example: `Reader guidance (non-operative): file position, chapter owner, and transition notes`). Put the non-operative guidance itself in a **blockquote** (`>` lines) after a short disclaimer that the quoted text does not add, remove, or narrow binding obligations. Follow the closing `</details>` with a `<br>` spacer, then any chapter-level `*In plain terms:*` gloss, then operative prose.
7. **Application baseline (operative opening cross-reference rule):** If a chapter needs a short opening sentence that states what upstream chapters, Rights Floors, validity controls, or downstream change-path controls govern its operative application, put that material in one concise ordinary-text paragraph immediately after the opening reader-guidance widget and before the chapter body—or, when the chapter already states an equivalent operative stack in frontmatter (for example **Chapter Ten, Part A** `**Default constraint stack.**`), keep that labeled stack as the application baseline and do not duplicate it under a second label. Preferred lead label elsewhere: `Application baseline.` This paragraph is **operative** if it says the chapter or section applies *subject to* other chapters or controls. Do **not** bury that rule in non-operative reader guidance, and do **not** repeat the same baseline again in the first body paragraph. Keep `Orientation, corpus edition metadata, and Authority Stack guidance` references out of the operative baseline unless they are themselves doing operative work.
8. **Trace sections:** Where trace blocks are used in constitutional text, they must be collapsible `<details>` sections with a `<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>` label and must be **collapsed by default**. Use trace blocks only where they materially improve navigation; keep them short and non-operative.
9. **Trace placement:** Put the trace block immediately under the owning unit's label. For normal sections, that means directly under the Markdown heading. For Chapter Five-style definition entries and similar owner-by-term lists, that means directly under the definition term line and before the `O` / `E` / `C` bullets. For **Chapter Ten**, the default owner unit is the **subarticle** (`#### Article …`) rather than only the parent article (`### Article …`) because subarticles usually carry the operative doctrinal hooks. Article-level trace blocks in Chapter Ten are optional and should be used only where a shared opening contract materially applies across the whole article. Where readability needs a visual break in definition lists, prefer a separator line in the local pattern of that file (for example the same kind of divider used around clustered or compound definition blocks) rather than a blank-line workaround that pushes the trace away from its owning term. When a file adopts that separator pattern for trace-bearing entries, apply it consistently within that local list instead of mixing separated and unseparated trace entries.
10. **Trace contents:** When a trace block carries navigation help, put that help **inside the trace block**, not as a standalone line outside it. Preferred order is: an `Upstream:` line first, using the form `Upstream: Principles: ...`; then a `Downstream:` line for the next controlling or affected principles, articles, or sections; then `Read with:` for closely related definitions, owner layers, or upstream mechanics that readers commonly need next. When `Upstream:` and `Downstream:` belong to the same trace item, keep them on separate rendered lines for readability. Keep `Read with:` selective, short, and non-operative; it is a routing aid, not a second gloss. `Definitions:` lines are **no longer** part of Trace — canonical Chapter Five cross-references live in the separate **Definitions · Evaluation · Compliance (D/E/C) widget** under rule 12, next to the same owning unit.
11. **Trace article integration:** When a `Downstream:` line names Chapter Ten articles, integrate the article references into a short functional explanation rather than presenting a bare citation inventory. Preferred pattern: describe the rights surface or doctrinal function first, then name only the most relevant articles or article families. Use exhaustive lists only where omission would materially reduce auditability. This rule exists to preserve first-pass reader comprehension while keeping the trace block reviewable and link-rich.
12. **Definitions · Evaluation · Compliance (D/E/C) widget:** Use a second blue collapsible widget to surface the canonical Chapter Five definitions materially invoked by a consuming section, so readers can jump directly to each invoked concept's `O`, `E`, or `C` line. Rules:
    - **Scope:** attach D/E/C widgets only next to **consuming** sections (Chapter One principles, Chapters Two through Four definition mechanics where a section explicitly invokes a named Chapter Five concept, Chapter Six contribution / violation / standing classification, Chapter Eight top-end anti-constitutional misconduct, Chapter Nine forums, Chapter Ten rights, Chapter Eleven governance, CJS-4/CJS-5 operational sections, and similar). **Never** attach them inside the Chapter Five definition files (`core_05-05_definitions_a_independent.md`, `core_05-05_definitions_b_semi_independent.md`, `core_05-05_definitions_c_dependent_clusters.md`) themselves. There is **no** chapter-wide or global instance.
    - **Trigger:** attach a widget wherever a section materially invokes **two or more** Chapter Five defined concepts. Sections invoking **exactly one** concept use the single-concept inline form in (f) below. Sections invoking zero concepts get nothing.
    - **Roadmap exclusion (material-invocation test):** "Materially invokes" means the section uses the term as a working term in a substantive claim, requirement, or constraint of its own. A defined concept that appears in a section **only** as part of a roadmap, topic-preview, or "what this chapter is about" enumeration — naming concepts that are operatively treated downstream in named subsequent sections of the same chapter or owner unit — does **not** count and must not be included in that section's widget. The most common case is a chapter-opening *Purpose and Role* / introductory section that lists the chapter's central terms before each gets its own dedicated subsection. Such sections include only those concepts that the section itself does operative work with (for example, a conflict-resolution clause that requires evaluation under a named concept). The downstream dedicated sections carry the widget rows for the concepts they actually invoke.
    - **Degradation under roadmap exclusion:** Recount the section's invocations **after** roadmap-exclusion trimming, then apply the standard trigger and degradation rules to the trimmed count. Specifically: if **two or more** material invocations remain, keep a (possibly smaller) collapsible widget; if **exactly one** remains, drop the widget and replace it with the single-concept inline `Definition:` line in (f) below; if **zero** remain, remove the widget entirely. Roadmap exclusion is not allowed to leave a one-row collapsible widget standing, and is not allowed to leave an empty widget standing. When degradation removes a widget that was attached during the 2026-04-16 greenfield pass, also remove the surrounding `<br>` spacer if its only purpose was to separate the (now-removed) widget from the operative prose.
    - **Placement:** put the widget directly after the Trace widget for the same owning unit when both are present; otherwise put it in the same position Trace would occupy (directly under the heading, before the operative prose or `O / E / C` bullets).
    - **Summary label:** `<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>`. Collapsed by default.
    - **Row shape:** one bullet per invoked concept, in the form `Concept link · O link · E link · C link`, where the concept and `O` links target the entry heading, `E` targets the `...-e` anchor, and `C` targets the `...-c` anchor. The redundant `O` link is kept so the triad reads symmetric on the page. For clustered concepts that do not carry a single E or C bullet (for example `Incentive Alignment`), point `O`, `E`, and `C` all to the heading so the reader lands inside the cluster.
    - **Chapter One functional order:** In Chapter One D/E/C widgets, preserve functional ordering rather than alphabetical ordering where a section invokes mixed concept types. Preferred order is: (1) primary principle / constraint / instrumental definition; (2) outcome-orientation terms; (3) agency, participation, stewardship, or challenge-pathway terms; (4) collision mechanics such as feasibility, necessity, proportionality, and harm minimization; (5) evidence, traceability, audit, or invalidation terms; (6) boundary / non-expansion terms such as Safety, Truth, ecological or intergenerational boundaries, source-layer authority, or anti-capture constraints. This order is documented in [implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md](implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md). Do **not** put visible grouping labels inside a D/E/C widget: `tools/ch5_dec_widget_audit.py` requires row-only widget content. Use row order, trace prose, the matrix artifact, or architecture notes to preserve the grouping.
    - **Single-concept inline form:** when a section invokes exactly one defined concept, drop the collapsible widget entirely and render a single inline line directly above the operative prose with the bold-blue `Definition:` prefix followed by `Concept link · O link · E link · C link`. Note the **singular** "Definition:" prefix here versus the **plural** "Definitions" in the widget summary label — the prefix agrees with the count. Use the same bold-blue styling as widget summaries so the line reads as navigational metadata rather than prose.
    - **Spacer rule (`<br>` after the navigational block):** The collapsible D/E/C widget keeps a trailing `<br>` spacer between its closing `</details>` and the operative prose, matching the Trace widget's spacer pattern; the `<br>` exists because the `<details>` block renders as a single visually heavy element that needs a hard break before prose. The single-concept inline `Definition:` line takes **no** trailing `<br>` spacer — the inline line is a one-line styled paragraph and the standard blank line between paragraphs already produces the right separation; an added `<br>` renders as a visible extra blank line and should be removed wherever it appears. This applies whether the inline line stands alone under a heading or sits directly after a co-located Trace widget. When degradation under the *Roadmap exclusion* rule converts a multi-row widget into the inline form, drop the surrounding `<br>` spacer at the same time. **Regression:** `make nav-widget-spacer-audit` runs `tools/nav_widget_spacer_audit.py` on `core_*` and `corpus_joint_structure/*` files.
    - **Anchors:** Chapter Five definitions carry navigation anchors immediately above the corresponding `E:` and `C:` bullets, formed from the entry’s existing heading anchor plus `-e` or `-c`. The heading anchor serves as the `O` target. These anchors are added (and kept idempotent) by `tools/add_oec_anchors.py`; they are link targets only, not semantic routing rules.
13. **Chapter Three §1 in-chapter definition index (Sentient Constitution):** In `core_02-04_definition_mechanics.md`, **Chapter Three**, **section 1** includes a collapsible block that lists **every** Chapter Three section or subsection readers treat as a navigable home for that chapter's integrity and observable-non-compliance material, **including** targets whose authoritative prose sits in **section 2**. Order the list **A–Z** by the link text (the target heading title). Each entry is **only** a Markdown link to that heading’s in-file fragment—**no** gloss, suffix, or other words on the same line. The block is **non-operative** navigational metadata (it does not add, remove, or narrow obligations). Update the list whenever Chapter Three gains, removes, or renames a navigable subsection. This index is **not** a substitute for rule 12 D/E/C widgets (Chapter Three still carries no Chapter Five D/E/C widget under the explicit-invocation reading unless that reading changes).

**Architecture note (2026-04-16, D/E/C split):** In the Chapter Five definition files, every standalone (`####`) definition now carries `-e` and `-c` anchors next to its `E:` and `C:` bullets. Across consuming files, the `Definitions: ...` line that previously sat inside Trace has been lifted out into a separate **Definitions · Evaluation · Compliance** widget (or a single inline `Definition:` line when exactly one concept is invoked). Trace keeps `Upstream:`, `Downstream:`, and `Read with:` only. The decision separates two reader jobs that were fused inside one Trace block — "where does this section sit in the principle / article stack" (Trace) versus "jump me to the authoritative O/E/C of a related concept" (D/E/C) — and operationalizes Chapter Four's Definition Traceability Requirement at the point of invocation, where that requirement already lives doctrinally. Clustered concepts such as `Incentive Alignment` are not individually anchored at `-e` / `-c`; authors point all three letters to the cluster heading in those rows.

**Architecture note (2026-04-16, D/E/C roadmap exclusion):** The greenfield D/E/C fan-out earlier on 2026-04-16 used **explicit naming** in the section text as the trigger for inclusion. That heuristic over-included on chapter-opening *Purpose and Role* / introductory sections, whose prose enumerates the chapter's central terms as a roadmap rather than operatively invoking them. Rule 12 was tightened with a *Roadmap exclusion* sub-rule that defines "materially invokes" as using the term as a working term in a substantive claim, requirement, or constraint of the section itself — not enumeration in a topic-preview list whose terms are operatively treated downstream in named subsequent sections of the same chapter. The first application is `core_00-01_principles.md` §1 (Purpose and Role), whose D/E/C widget was retrimmed from a seven-row chapter-wide-looking index to the two concepts (`Proportionality`, `Necessity`) that §1's last paragraph operatively invokes for conflict resolution. Wellbeing, Truth, Safety, Trustworthiness, and Meaningful Agency continue to carry their own widget rows in the dedicated sections (§§ 2, 3.2, 3.1, 4, 5) where they are operatively invoked.

**Architecture note (2026-04-29, Chapter One D/E/C functional ordering):** Chapter One D/E/C widgets are not alphabetical. They are ordered to show how the section reasons: primary definition first, then outcome orientation, agency/stewardship pathways, collision mechanics, evidence/invalidation, and boundary or non-expansion terms as applicable. This reduces AI-drift risk by making the row order itself carry the map. The source text cannot use visible group labels inside D/E/C widgets because the row-shape audit requires row-only content. The intended grouping is preserved in [implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md](implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md), and `make ch1-dec-order-audit` checks the highest-risk Chapter One widgets against their expected row order.

**Architecture note (2026-04-16, Ch 2-4 mechanics attachment):** Rule 12's Scope was extended to include `core_02-04_definition_mechanics.md` (Chapters Two through Four — the definition-mechanics layer). That file is where the Definition Traceability Requirement (Chapter Four, section 3) lives doctrinally, so surfacing canonical Chapter Five anchors at the point of invocation is coherent with the 2026-04-16 D/E/C split note. Attachment follows the strict **explicit-invocation-only** reading: widgets attach **only** where a section or subsection names a Chapter Five concept as a working term in its own substantive claim. The Chapter Two section 2 rule that governs every "reasonably foreseeable" in Chapters Two through Four counts as an explicit invocation of Foreseeability for those sites. Initial attachments: Chapter Two sections 2 and 2.4.4; Chapter Four sections 2.1, 2.5 (Truth + Epistemic Integrity widget), 4, 5, 5.1 (Truth + Safety widget), and 6. Chapter Three carries no D/E/C widgets under this reading because it states the anti-evasion framework in its own terms and does not name a Chapter Five concept by name. Separately, **rule 13** requires Chapter Three **§1** to carry a non-operative, **link-only** A–Z index to every in-chapter navigable subsection (including §2 targets). Consistent with the 2026-04-16 D/E/C split and roadmap-exclusion notes.

**Architecture note (2026-04-16, article integration):** In `core_00-01_principles.md`, Chapter One trace widgets were revised so article-heavy downstream lines explain the operative connection first and cite the key articles second. The decision was made because the earlier article-only lists improved audit navigation but read too much like reference dumps for general readers. The retained architectural rule is: keep article references in the trace widget, do not move them into the operative prose, and prefer functional grouping over exhaustive enumeration where that grouping does not hide a materially important downstream rights hook.

**Architecture note (2026-04-16, single-concept inline form spacer):** The 2026-04-16 D/E/C rollout and greenfield fan-out treated the trailing `<br>` spacer as a uniform pattern after every navigational block — collapsible widget or single-concept inline `Definition:` line. In rendered Markdown that uniformity reads cleanly under the `<details>` widget (the block is visually heavy and benefits from a hard break before prose) but produces a visible extra blank line under the inline `Definition:` line (which is already a one-line styled paragraph that the standard inter-paragraph blank renders correctly). Rule 12's *Single-concept inline form* sub-rule was extended with an explicit *Spacer rule (`<br>` after the navigational block)* clause: the collapsible widget keeps its `<br>` spacer; the inline form takes none, whether it stands alone under a heading or sits directly after a co-located Trace widget. Existing inline `Definition:` lines in `core_00-01_principles.md`, `core_02-04_definition_mechanics.md`, and `core_10-10_rights_part_a..d.md` were swept on the same date to remove the unnecessary `<br>`. The greenfield attachment tool (`tools/attach_dec_greenfield.py`) was updated in the same pass so future single-concept attachments do not reintroduce the spacer.

### Plain-Language Vocabulary Guardrails

Use this rule for preambles, chapter openings, reader guidance, notices, summaries, and other text meant to stay easy for a general human reader to scan quickly.

- **Load-bearing capitalization:** Capitalize **Wellbeing**, **Safety**, **Truth**, **Rights Floor**, and **Foundational Rights** when they identify named constitutional objectives, constraints, layers, or chapter titles. Keep ordinary lowercase uses for generic wellbeing, safety, truth, and rights-language; leave bare `rights`, `challenge rights`, `review rights`, `audit rights`, `standing rights`, and `due process` lowercase unless they appear in a formal article title or heading. Use **Rights-Floor** for compound modifiers tied to the Chapter Ten protection layer.
- Prefer everyday words when they preserve meaning.
- Keep canonical defined terms where legal precision requires them, but do not lead with specialist wording when a plain alternative works.
- If a formal term must appear in a reader-facing sentence, introduce the plain phrase first and use the formal term only if it adds necessary precision.

Avoid these words in plain-language sections unless they are the canonical term being cited on purpose:

| Avoid in plain-language prose | Prefer instead |
|---|---|
| `person` / `persons` (as the label for a rights-holding, accountable, or classifiable subject) | `sentient` / `sentients`; use `human` / `humans` where biological substrate or ordinary contrast with automation is material |
| `epistemic integrity` | `truthfulness`, `honest handling of facts`, `reliable understanding` |
| `contestability` | `ability to challenge`, `real chance to contest`, `reviewability` |
| `checkable` | `can be checked`, `something **sentients** can verify`, `open to verification` |
| `materiality` / `materially` | `importance`, `significance`, `in ways that matter` |
| `foreseeability` | `what could reasonably be expected`, `what **affected** **parties** could reasonably see coming` |
| `proportionality` | `fit the risk`, `no broader than needed`, `matched to the harm` |
| `necessity` | `needed`, `required`, `no less restrictive effective option` |
| `operationalize` / `operationalized` | `put into practice`, `carry out`, `implement` |
| `interdependent definitions` | `linked definitions`, `connected definitions` |
| `annex` (generic implementation-layer reference) | `implementation layer`, `implementation file`, or a specific implementation filename like `corpus_systems.md` |
| `non-compliant` in explanatory prose | `does not meet the rule`, `fails the rule` |
| `stakeholder` when ordinary **sentients** are meant | `affected parties`, `participants`, `those involved` |
| `posture` | `stance`, `approach`, `inputs`, `classification`, `framing`, `rule`, `profile`, or a concrete noun for what is meant (for example `verified standing inputs`, `scope limit`, `default rule`) |
| `court` / `courts` (adjudicative / institutional) | `forum` / `forums`, `forum family` for routing, **Chapter Nine** and **[corpus_forum.md](corpus_forum.md)** for operative detail; or, where a generic label is still needed, `adjudicative body` |
| `tribunal` / `tribunals` (internal forum-family sense) | `forum` / `forums`, `forum family`, `panel`, `bench`, or `adjudicative body`, depending on whether the sentence means the constitutional family, the deciding body, or a generic external body |

#### Ambiguous implementation labels (corpus-wide)

Use this sub-rule in **authoritative corpus** body text (`core_*.md`, `corpus_*.md`, and this file’s prescriptive editor guidance), not only in *In plain terms* lines.

| Do not use (ambiguous) | Use instead |
| --- | --- |
| **Constitutional Systems** (bare label) | The linked file **[corpus_systems.md](corpus_systems.md)**. For a chapter or protocol within that file, cite it in full (for example **corpus_systems.md**, Chapter S1 — Information Types and Handling). The editor abbreviation `CS` remains acceptable in owner tables, stable IDs, and mermaid. The old bare label collides with ordinary English, other implementation files, and the filename. |
| **`court` / `courts`** (Chapter Nine and **[corpus_forum.md](corpus_forum.md)** institutional sense) | **`forum` / `forums`**, **`forum family`** (for allocated routing and bodies), and explicit **[core_09-09_forum.md](core_09-09_forum.md)** / **`corpus_forum.md`** **CF-*** cross-references. Where a generic English label is still required, **adjudicative body**. Same exceptions as in **[.cursor/rules/sentient-constitution.mdc](.cursor/rules/sentient-constitution.mdc)** and this section: verbatim external quotations; proper names and historical titles where source fidelity requires; **courtesy** / **courteous** lemmas. |
| **`tribunal` / `tribunals`** (internal Chapter Nine / **[corpus_forum.md](corpus_forum.md)** governance sense) | **`forum` / `forums`**, **`forum family`**, **`panel`**, **`bench`**, or **`adjudicative body`** as context requires. Use external or historical **tribunal** wording only where source fidelity, proper titles, or external legal-order references require it. |

Citing the systems implementation file from the Sentient Constitution: use the naming pattern in [Citing corpus_systems.md from Sentient Constitution](#citing-corpus_systemsmd-from-sentient-constitution) (above in this file).

#### Co-Gloss registry (heavy phrases with stable plain-language counterpart files)

Use this table when authoring *In plain terms* lines, executive summaries, or adoption-facing explainers. Entries **do not** redefine **Chapter Five** terms; they pair recurring heavy phrases with **reader-stable glosses** of **rule effect**, consistent with the *Single home rule* and the bolded-term-lead bullet rule above (gloss restates **effect**, not **term meaning** for interpretive purposes).

| Heavy phrase (as used in Chapter Nine / implementation files) | Approved plain-language counterpart (effect-level) |
| --- | --- |
| early-instantiation window | the period when a new system or role first goes live and early mistakes are most likely to become entrenched |
| parent-system continuity interest | a prior operator’s legitimate need to keep essential services stable through a handoff or migration |
| capability profile materially emerging | a sentient’s real-world abilities are still taking shape, so tests and thresholds must be fair and revisable |

**`person` exceptions (corpus-wide, not only plain-language):** Keep fixed compounds **in-person** and **in-person-only** (physical presence); lemmas **personal**, **personnel**, **persona**, **personalized**; technical labels such as **non-personal data**; and **verbatim** quotations of external law where fidelity requires the original wording.

**`court` exceptions (corpus-wide, not only plain-language):** Same set as in **[.cursor/rules/sentient-constitution.mdc](.cursor/rules/sentient-constitution.mdc)** and this section — **verbatim** external quotations; **proper names** and historical titles where source fidelity requires; lemmas **courtesy** and **courteous** (not the Chapter Eight / **`corpus_forum`** institutional sense).

#### Plain-language gloss placement

The italicized `*In plain terms: …*` line is the canonical plain-language surface for operative constitutional text. It is the **Chapter One §3.4** (*Plain-Language Accessibility*) stewardship duty made visible at the article level, and it is where a reader dropping into a cross-reference first meets the rule in everyday words. Two placement rules keep that surface continuous:

1. **Operative-subarticle rule.** Any subarticle heading one level below its parent article (for example `##### Article V-F.1` under `#### Article V-F`) that carries **independent operative clauses** — bullets that impose, relax, or condition obligations on their own, rather than only pointing back to the parent article — must carry its own `*In plain terms: …*` line, placed immediately under the heading in the position the parent article's gloss would occupy. Purely scoping or pointer-only subarticles do not need a separate gloss. The test is whether a reader arriving directly at the subarticle via cross-reference could read the rule correctly without the parent article's gloss; if not, a local gloss is required.
2. **Bolded-term-lead bullet rule.** Where an operative bullet leads with a bolded **Chapter Five** term followed by a colon (for example `**Best-Interest Standard:**`), the body of the bullet must be a plain-language gloss of what the rule **does**, stated in subject–verb–object form. It must not be a paraphrase of the term's `O` definition. The defined term carries the precision; the bullet body carries the readability. This rule interacts with the *Single home rule* above: writing the bullet body in plain language is not a second O/E/C-style gloss and does not violate single-home discipline, because it is restating the **rule's effect** rather than redefining the **term**.

Enforcement routes through `tools/readability_audit.py` in `make regression-full`. A subarticle-level gate — flagging a `##### Article …` heading whose body contains operative bullets but lacks an `*In plain terms: …*` line, or whose bolded-term-lead bullets score above a nominalization / clause-density threshold — is a candidate extension.

### Implementation-file source hierarchy block

Where an implementation file needs an owner-allocation subsection near its opening, use the subsection label **Definition discipline and source hierarchy**.

Open that subsection with the exact lead sentence:

- **Definition discipline is single-home:**

Use the shared bullet order below whenever those owner layers are relevant in the file:

1. constitutional definition structure, integrity, burden and verification, and foundational definitions -> `core_02-04_definition_mechanics.md` and Chapter Five (`core_05-05_definitions_a_independent.md`, `core_05-05_definitions_b_semi_independent.md`, `core_05-05_definitions_c_dependent_clusters.md`)
2. contribution-state (Axis I) / violation / standing meaning and offense classification meaning -> `core_06-06_standing_assessment.md`, `core_07-07_standing_integration.md`, and `core_08-08_misconduct.md`
3. rights meaning -> `core_10-10_rights_part_a.md` through `core_10-10_rights_part_d.md`
4. shared operational cluster meanings -> `corpus_joint_structure.md` **CJS-5** (*Implementation and cross-implementation operational cluster library*)
5. system class, dependency, steward, and continuity taxonomies -> `corpus_systems.md`

After that shared sequence, append only file-specific owner bullets that are genuinely local to that implementation file, for example forum-family routing in `corpus_forum.md` or non-forum institutional architecture in `corpus_institutions.md`.

### Implementation-Corpus Preamble Contract

For shared opening contract language in implementation files (`corpus_joint_structure.md`, `corpus_systems.md`, `corpus_institutions.md`, `corpus_forum.md`), use a concise pointer to `corpus_joint_structure.md` **CJS-1.2** (*Shared implementation-corpus preamble contract*) instead of repeating long boilerplate.

Use implementation-file-specific add-ons only where necessary (for example CJS-5 (*Implementation and cross-implementation operational cluster library*) citation seams in `corpus_joint_structure.md` pointing to `corpus_joint_structure.md` **CJS-3.6** (*Implementation-label traceability and stricter-wins discipline*)).

Do not duplicate shared cross-implementation preamble text across multiple implementation files when CJS already owns that contract.

Where an implementation file states an article-citation default near its opening, use one rule: Roman numerals are reserved for **Article** citations only. Unless another Sentient Constitution chapter is explicitly named, those **Article** citations refer to **Sentient Constitution Chapter Ten**.

### Order and alphabetization (Chapter Five)

**Boundary:** Ordering and alphabetization rules are **editorial and process discipline** for maintainers and tools. They are stated **here** (and in implementation workflow notes), **not** in Sentient Constitution Chapter Five operative text (`core_05-05_definitions_*.md`), because default list order has **no independent legal effect**.

- **Section 1 — Independent Definitions:** Default editorial order is **ascending alphabetical** by the **primary entry title** (the standalone heading line that names the definition). Visible entry titles should use the plain canonical term by default; do **not** append `(Constitutional)` unless the qualifier is strictly necessary to disambiguate two otherwise conflicting canonical titles and that exception is documented. **Exceptions** (legacy placement, intentional adjacency for reading flow, **compound-definition adjacency** where a specialized entry is placed directly after its base entry, or freeze pending a planned renumbering pass) should be noted in the commit message or briefly in **section 13** (*Definitions-first redundancy sweep*) when non-obvious. **New** §1 entries should be inserted at the correct alphabetical position unless an exception is documented.
  - **Reference-side rule (no redundant `(Constitutional)` suffix in cross-references).** The same plain-canonical-term rule governs **cross-references** to Chapter Five entries everywhere in the binding corpus, architectural maps, README, active implementation notes, and archived process notes when they are refreshed (`core_*.md`, `corpus_*.md`, `doc_architecture.md`, `README.md`, `implementation/*.md`, and refreshed `archive/*.md`). Visible prose must not append `(Constitutional)` to a Chapter Five defined-term reference (e.g. write **Intergenerational Responsibility**, not *Intergenerational Responsibility (Constitutional)*). **Preserved:** (a) URL anchor fragments that end in `-constitutional` (e.g. `#intergenerational-responsibility-constitutional`) and their corresponding `<a id="…-constitutional"></a>` tags are link-target identifiers, not display text, and remain untouched; (b) distinct parentheticals that are **part of the canonical title** (for example *Truth (Constitutional Constraint)*, *Safety (Constraint)*, *Freedom (Bounded Agency)*, *Privacy (Informational)*, *Harm Minimization (Tradeoff Selection)*, *Non-Imposition (Cooperative Interaction)*, *Protected Reporting (Whistleblowing)*) are preserved verbatim because the parenthetical is the term; (c) backtick-quoted meta-text that names the literal suffix (such as this rule's own `` `(Constitutional)` ``) is preserved as meta-reference. This reference-side rule was added on **2026-04-17** together with a corpus-wide sweep that stripped 495 redundant suffixes across 378 lines; the enforcement gate is `tools/ch5_entry_format_audit.py` (extended the same day to flag the redundant suffix corpus-wide, not only in Chapter Five headings).
  - **Chapter Five — single-definition rule.** Do not add duplicate definition labels, placeholder-only headings, locator-only entries, or alternate shells anywhere in Chapter Five. Each visible definition term has one O/E/C-owning entry in §1, §2, or §3. If the definition lives inside a §3 cluster, place the real O/E/C text there and link directly to that entry’s stable anchor; do not keep a parallel empty heading in §1 or §2.
- **Chapter Five alphabetical directory:** Chapter Five carries a non-operative alphabetical directory near the top of the file. Keep **Definitions A-Z** and **Clusters A-Z** as separate sorted lists. Each visible definition label appears once in **Definitions A-Z**; each numbered §3 cluster heading appears once in **Clusters A-Z**. Directory links are navigation only and do not create pointer entries, alternate homes, or routing rules.
- **Trace-bearing definition separators (Chapter Five §1–§3):** If a definition `####` / `#####` title is immediately followed by a `<details>` **Trace** block, the first significant Markdown line above that title (after any `<a id="…"></a>` anchor for the entry) must be a single `---`, enforced by `make ch5-entry-format-audit`. This pattern is used in all three Chapter Five definition files. It is **not** the same as Part **B** **topic-group** double-`---` stacks or Part **C** multi-`---` cluster-head openers.
- **Section 2 — Semi-independent Definitions:** Default editorial order is **ascending alphabetical** by the **primary entry title**, matching §1 discipline. Semi-independent entries may be read with one or more §3 clusters, but they still have exactly one visible definition entry. **Topic-group name-order discipline:** For compound topic-group headings, the visible term sequence is a reader-facing ordering contract. If editors reorder the entries inside a group for dependency / reading-order clarity, they must update the group heading in the same change so the heading order still matches the internal entry order. This ordering is editorial and has no independent legal-priority effect unless operative text expressly says so. **Topic-group section dividers (editorial):** The non-operative **topic group** `####` lines (the long comma-separated reading-order **group** labels) are immediately preceded by **two** Markdown horizontal rules on separate lines (`---`, blank line, `---`, blank line) before that **group** heading only. **Subentry spacing (editorial):** Do **not** place horizontal rules between successive plain definition blocks inside a group (including between the group label and the first `<a id>` / `####` entry), except for **Trace-bearing definition separators** above. Separate other subentries with **blank lines** only. **Preamble divider:** One `---` appears after the **part B** file introduction and before the section-2 anchor, as in [core_05-05_definitions_b_semi_independent.md](core_05-05_definitions_b_semi_independent.md). Other `---` lines in part B are **topic-group** openers (two-rule stacks) or single rules satisfying the trace-bearing bullet, not generic separators between plain subentries.
- **Section 3 — Dependent clusters:** The operative cluster bodies are sorted **A–Z by cluster heading** (sequential `#### 3.1` … `#### 3.16` after the fixed-order meta rules **§3.1** and **§3.2**). Stable HTML anchors on cluster openers (`<a id="…-cluster">`) must be preserved when renumbering. Within a cluster, sub-entries may follow **dependency / reading order** or **alphabetical** order by sub-entry title—choose whichever makes **joint satisfaction** clearest; stay consistent within that cluster unless reordering is part of an explicit edit. **Cluster owner discipline:** A term may appear in only one `Cluster members.` roster. Other materially relevant clusters should cite that term under `Read-with definitions.` or ordinary prose, not as a second owner. **Cluster name-order discipline:** For compound cluster headings, the heading name, explanatory opening sentence, `Cluster members` list, and any internal sub-entry order should move together. If a cluster member is reordered, added, removed, or renamed in a way that changes the reading-order logic, update the cluster title and opening description in the same change. The title sequence is an editorial reading-order contract, not a legal hierarchy, unless operative text expressly establishes priority. Major clusters must remain reflected in **Sentient Constitution Chapter One** (*cluster index* paragraph at the **end** of Ch 1). **Cluster section dividers (editorial):** The operative cluster `####` titles **3.1** through **3.16** are immediately preceded by **at least two** `---` lines before the optional `<a id="…-cluster">` and cluster title (the file often uses three `---` between closed clusters). The fixed-order meta rules **§3.1** and **§3.2** are not cluster bodies and do not use this opener pattern.
- **Chapter One vocabulary anchor:** Order is **not** alphabetical; it reflects **priority alignment** with foundational values language. When you add a term to the anchor for traceability, place it where editors can scan related concepts together; grep and tools should rely on **definition titles in Ch 5**, not anchor order.
- **CJS / CS registries** (CJS-5 (*Implementation and cross-implementation operational cluster library*) clusters, implementation headings): Follow each file’s existing registry and stable-ID discipline; those lists are **code- or protocol-ordered**, not Ch 5 alphabetical.

**Architecture note (2026-04-27, Ch 5 §2/§3 section dividers):** The double horizontal rule before Chapter Five **§2** **topic-group** labels (not before each individual semi-independent definition title) and the at-least-two-rule before **§3** cluster `####` openers (from **3.3** onward) are **editorial presentation** for visual separation in rendered Markdown. They are **not** operative constitutional text, do not change legal meaning, and should be kept consistent when adding or renumbering groups or clusters. See the **Topic-group** and **Cluster section dividers** sub-bullets under **Section 2** and **Section 3** in **Order and alphabetization (Chapter Five)** above.

**Architecture note (2026-04-29, Ch 5 compound heading order):** Compound §2 topic-group headings and §3 dependent-cluster headings must not drift away from their internal order. This is especially important when multiple AI models edit Chapter Five: a model may alphabetize, rename, or "tidy" a heading while leaving the member order unchanged, or reorder members while leaving the heading stale. `make ch5-cluster-order-audit` checks selected high-risk groups and clusters whose headings currently act as explicit reading-order contracts. Expand that audit when a new compound heading is intentionally made order-bearing.

**Architecture note (2026-04-27, Ch 5 §2 subentry and preface lines; 2026-04-29 trace alignment):** In `core_05-05_definitions_b_semi_independent.md`, do **not** use Markdown horizontal rules between plain semi-independent **subentries** (successive `####` blocks **without** an immediate `<details>` Trace opener). Subentries without traces are separated by blank lines only. Where a `####` entry owns a `<details>` Trace block, apply **Trace-bearing definition separators** above. The **double** `---` stack remains reserved for non-operative **topic group** `####` labels; the **one** preface `---` after the part B introduction is unchanged.

### Single home rule

For any **concept** that could drift (e.g. harm, materiality, Type N, Class A, proportionality as a test):

1. **Identify the single canonical paragraph** using the table in **section 2** and the overlap map in **section 13** (*Definitions-first redundancy sweep*).
2. **Elsewhere**, use **pointers** (chapter, article, CJS-5 (*Implementation and cross-implementation operational cluster library*) cluster, SYS-CH-S#) plus **operational criteria** specific to that layer. Do **not** add a second full O/E/C-style gloss unless you are **amending** the canonical file on purpose.

### Layered framing and restatement discipline

Use this default framing flow for cross-layer drafting and edits:

1. **Definitions first:** Sentient Constitution definition layers establish term meaning and satisfaction conditions.
2. **Principles second:** Foundational principles and interaction/conflict-order framing constrain interpretation.
3. **Articles third:** Rights, duties, and constraints are stated at article level.
4. **Core synthesis fourth:** the numbered Sentient Constitution `core_*.md` files (Chapters One through Fourteen) integrate constitutional doctrine and conflict ordering.
5. **Joint structure fifth:** `corpus_joint_structure.md` routes ownership and cross-layer coordination.
6. **Operational detail last:** `corpus_institutions.md`, `corpus_systems.md`, and `corpus_forum.md` carry implementation detail.

When writing in a non-owner layer, use one of two forms only: (a) brief pointer-only language, or (b) a short non-operative summary that names the canonical owner. Do not restate full doctrine outside its owner layer unless the owner text is being intentionally amended in the same change.

### Precedence (if two passages disagree)

1. **Sentient Constitution values and rights** (Ch 1, Ch 9) over conflicting operational wording.
2. **Sentient Constitution Ch 2–3** over implementation corpus files for **what a term means** and **how definitions must be satisfied**.
3. **CS S1/S2/S3** over Sentient Constitution / CJS for **Type/Class/steward assignment rules**.
4. **Stricter or more specific** applicable rule wins where the corpus already says so (e.g. Protocol B vs applicable CJS-5 (*Implementation and cross-implementation operational cluster library*) terms).

### Adding or changing a term (workflow)

1. If the term is **cross-cutting** (used in rights, implementation files, and implementation labels): add or extend exactly one **Independent Definition** (§1), **Semi-independent** full entry (§2), or **Dependent cluster** entry (§3) in **Sentient Constitution Ch 5**, in compliance with **Sentient Constitution Chapters Two through Four**. Do not add placeholder rows or duplicate labels anywhere in Chapter Five; place stable anchors on real definition bodies.
2. If the term is **only operational** (e.g. a deployment stage label): put it in the relevant **implementation file** or **CJS** and **point** to Ch 2–3 only if it implicates a constitutional concept.
3. **Grep** the other two corpus files; replace **competing** definitional paragraphs with plain cross-references to the single Chapter Five home.
4. Update **section 2** (owner table) or this section if you introduce a **new owner** for a class of terms.
5. When adding or renaming **clustered** Chapter Five entries that editors routinely need for traceability, update the **cluster index** paragraph at the **end of Sentient Constitution Chapter One**. Use the **Reference: Chapter Five vocabulary anchor and cluster index** section, with the vocabulary anchor paragraph first and the cluster index second, so the anchor and cluster index together mirror priority vocabulary for tools and reviewers.
6. For a new **§1 Independent Definition**, insert it in **alphabetical** order by primary title per **Order and alphabetization (Chapter Five)** above, unless a documented exception applies; update the **vocabulary anchor** paragraph in that same end-of-Chapter-One reference block when the term is part of Chapter One priority alignment.

### Vocabulary anchor vs cluster index (Chapter One)

Both live at the **end of Chapter One** under **Reference: Chapter Five vocabulary anchor and cluster index** (vocabulary anchor paragraph, then cluster index paragraph) so the substantive sections of Chapter One read continuously.

- **Vocabulary anchor** (Ch 1): Semicolon-separated list of **primary** §1 Independent Definition titles used for corpus alignment with foundational values language. It is not required to list every line in Chapter Five §1 (e.g. every variant under Harm or Material).
- **Cluster index** (Ch 1): Short catalog of **major §3 dependent clusters** (Foreseeability, Materiality, verification/observability, auditability, sentience sub-entries, system boundary/capture, etc.). Any materially relevant cluster member must still be **explicitly traced** under **Sentient Constitution Chapters Two through Four** when invoked in evaluation.
- **Implementation-file interpretation lines** should defer to **both** the anchor and the cluster index when pointing readers to “Chapter Five definitions.”

### Quick index (non-exhaustive)

| Kind | Canonical location | Sentient Constitution pointer |
|------|--------------------|------------|
| Definition mechanics | Sentient Constitution Ch 2 | — |
| Shared terms (for example Wellbeing, Harm, Safety, Truth, dignity, consent, governance, oversight, redress, reversibility, privacy, and related terms) | Sentient Constitution Ch 5 §1 Independent Definitions | Ch 1 end — vocabulary anchor paragraph |
| Cluster-component definitions whose full O/E/C lives under a §3 cluster | Sentient Constitution Ch 5 §3 Dependent clusters (stable sub-entry anchors) | Ch 5 directory — Semi-independent A–Z (links to those anchors) |
| Clustered traceability sets (Foreseeability, Materiality, Harm/Risk, verification, audit, sentience, system boundaries/capture, …) | Sentient Constitution Ch 5 §3 Dependent clusters | Ch 1 end — cluster index paragraph |
| Rights (Articles I–XXV, including equality and protected-characteristics hooks) | Sentient Constitution Ch 9 | Interpretation blocks in implementation corpus files; **Protected Characteristics** in Sentient Constitution Ch 5 §2 |
| Contribution / standing model | Sentient Constitution Ch 6 (**verified** standing inputs; Ch 8 forums for **allegations**) | Implementation-file procedural implementation |
| Cross-domain integrity routing | CJS-4.4 and CJS-5 operational clusters | Sentient Constitution Ch 15 (*incorporation bridge*) |
| Legitimacy / adoption / amendment machinery | Sentient Constitution Ch 10, Ch 11–13 | Implementation-file operational hooks |
| Stable CJS operational clusters | Registry in corpus_joint_structure.md | Sentient Constitution Ch 10 (governance) and Ch 15 (incorporation hook); CJS-4 and CJS-5 |
| Interoperability, portability, exit-integrity architecture | **CJS-5D.2** for implementation and cross-implementation interoperability, portability, exit-integrity, and open data-format / protocol discipline; **CJS-5A.4** for justified limits on integration or export | Sentient Constitution Ch 9 **Article XIX** (*Interoperability, Portability, and Exit Integrity*). **Ch 5 §3.6** (*Corpus, Authority Stack, Supremacy, and Enforceability*) together with definitions in §2 cover governance structure and exit-path analysis where applicable. **CJS-5D.2** also includes a material-impact preference for **open hardware**, **open software**, and **open systems**. |
| Emergency, contingency, force majeure, deployment environments | **CS Protocol A** (operational deployment; grounded in Sentient Constitution definitions) | Sentient Constitution Ch 5 *Emergency and Contingency* and *Force Majeure*. Chapters Two through Five prevail if Protocol A is silent on meaning. |
| Data / system / steward taxonomies | CS S1, S2, S3 | Sentient Constitution related documents; CS interpretation blocks |
| Productive capacity, constitutional efficiency, and avoidable burden | Sentient Constitution Ch 5 **§2** semi-independent cluster (*Avoidable Burden*, *Constitutional Efficiency*, *Productive Capacity*, and *Burden-Reduction Duty*) | Ch 1 **§5.1** (instrumental-good framing), **§6.1.4** (fourth Core Tradeoff Principle), **§7.2.2** (stewardship incentive alignment); Ch 9 **Article XX** avoidable-complexity clause; Ch 10 **§3** burden-reduction duty and **§3.2** Ecosystem Value Orientation |

---

## 5. Stable IDs — Sentient Constitution

| ID | Status | Content (summary) |
|----|--------|-------------------|
| Sentient Constitution Ch 1 | **Present** | Foundational values and constraints; includes **§3.3** (*Science-Informed Inquiry and Decision Support*), **§3.4** (*Plain-Language Accessibility (Stewardship Duty)*), **§5.1** (*Freedom (Bounded Agency)*), **§5.2** (*Shared-System Stewardship*), **§5.1** (*Productive Capacity (Instrumental Good)*) with **§5.1.1** concentration-threshold mechanism, **§6.1.4** (*Minimization of Avoidable Burden*) as a fourth Core Tradeoff Principle, **§7.1** cross-cutting evaluation factors (including the *Privacy (Informational)* joint-invocation bullet), and **§7.2.2** stewardship incentive alignment covering productive capacity and avoidable-burden creation |
| Sentient Constitution Ch 2 | **Present** | Definition structure and O/E/C component requirements |
| Sentient Constitution Ch 3 | **Present** | Definition integrity, anti-evasion, observable non-compliance |
| Sentient Constitution Ch 4 | **Present** | Burden of proof, traceability, observability, verification; **§6** (Verification Accessibility and Feasibility) carries a plain-language-accessibility cross-reference pointing to **Chapter One §3.4** with an explicit engagement-layer / definition-layer precedence rule (definition layer governs where conflict appears) |
| Sentient Constitution Ch 5 | **Present** | Foundational definitions: §1 Independent Definitions; §2 Semi-independent Definitions (including the capacity-efficiency-burden cluster for *Avoidable Burden*, *Constitutional Efficiency*, *Productive Capacity*, and *Burden-Reduction Duty*, plus full entries where the O/E/C statement appears in §2); §3 Dependent clusters (joint-invocation groups and full O/E/C for cluster-homed terms, reduced to 16 clusters from 42 after 2026-05-08 restructuring); Ch 1 end-of-chapter vocabulary anchor + cluster index |
| Sentient Constitution Ch 6 | **Present** | Standing Assessment (two-axis constitutional meaning; contribution state and violation nature; **standing** uses **verified** Axis I and [**verified violation findings**](core_05-05_definitions_b_semi_independent.md#verified-violation-findings) for Axis II — **section 2** *Verified inputs for standing*; **Chapter Nine** forums cover **allegations** / **claims**, not standing calculus). Final anti-constitutional **s = 7, 8, or 9** classification is owned by **Chapter Eight** |
| Sentient Constitution Ch 7 | **Present** | Standing Effects and Integration (`core_07-07_standing_integration.md`): standing effects, violation-axis attachments, supplemental descriptors, no-offset/no-netting integration, and real-world enforcement mechanics |
| Sentient Constitution Ch 8 | **Present** | Anti-Constitutional Misconduct (`core_08-08_misconduct.md`): sole home for final **Violation Axis s = 7, 8, and 9** anti-constitutional classification, criteria, unified-incident gravity, and due-process safeguards (legacy **Tier 1 / Tier 2 / Tier 3** wording maps to those slots where Chapter Six states) |
| Sentient Constitution Ch 9 | **Present** | Forums and Jurisdiction (`core_09-09_forum.md`): default venue, primary-stakes routing, intake, transfer, certification, backup routing, and forum application of Chapters Six through Eight |
| Sentient Constitution Ch 10 | **Present** | Foundational Rights, Articles I–XXV (`core_10-10_rights_part_a.md` through `core_10-10_rights_part_d.md`) |
| Sentient Constitution Ch 11 | **Present** | Governance Legitimacy, Authorization, and Stewardship (`core_11-11_governance.md`) |
| Sentient Constitution Ch 12 | **Present** | Non-regression and substantive amendment validity (Test 1; anti-evasion; regressive-deception referral triggers) (`core_12-14_amendment.md`) |
| Sentient Constitution Ch 13 | **Present** | Expansion, supremacy relative to other binding norms, external legal orders (`core_12-14_amendment.md`) |
| Sentient Constitution Ch 14 | **Present** | Amendment, ratification, procedural validity (Tests 2–4), review triggers, invalid-change handling, amendment procedure requirements (`core_12-14_amendment.md`) |
| Sentient Constitution Ch 15 | **Present** | **Incorporation bridge** (incorporates implementation text by reference; see [core_15-15_incorporation.md](core_15-15_incorporation.md)); **§4** *Adoption framing and scope of authority* states the instrument's aspirational-model-constitutional-instrument self-description, the substantive-scope-vs-operative-effect split, scoped-adoption / non-regression interaction, pluralism preservation, and the non-adopter jurisdictional-objection framing rule |

**Integration note:** [corpus_joint_structure.md](corpus_joint_structure.md) is **part of Corpus** and is **incorporated by reference** as **authoritative implementation text** for the obligations it states (see [core_15-15_incorporation.md](core_15-15_incorporation.md) and [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) Chapter Five *Corpus*). Its cross-domain implementation headings are **CJS-4 — Specific joint interlocks and shared abstractions** and **CJS-5 — Cross-implementation operational cluster library**. **Do not** treat Sentient Constitution chapter numbers as synonymous with CJS operational clusters.

**Authority boundary note:** This file is the authoritative **map** for corpus ownership and navigation, but it is not itself the constitutional source layer. Where wording in this map appears to diverge from Sentient Constitution / CJS / CS normative text, the corpus controls.

### Stable IDs — CJS operational cluster file

Use these labels in commits and cross-corpus notes. They match headings in [corpus_joint_structure.md](corpus_joint_structure.md).

| Stable ID | Heading in CJS file |
|-----------|-------------------|
| **CJS-5A** | Authority, constraint, secrecy, and procedure terms |
| **CJS-5B** | Evidence, audit, and claim-integrity terms |
| **CJS-5C** | Participation, comprehension, and disclosure terms |
| **CJS-5D** | Dependency, exit, and lifecycle-integrity terms |
| **CJS-5E** | Failure, robustness, intervention, and correction terms |

**Retired shorthand:** Older drafts sometimes used companion-file implementation-label shorthand for this layer. In live text, replace that shorthand with **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*), the applicable **CJS-5** (*Implementation and cross-implementation operational cluster library*) cluster, and Chapter Five definitions where term meaning is at issue.

### Articles I–XXV (core rights; implementation files implement detail)

Articles **I–XXV** are **present** in [core_10-10_rights_part_a.md](core_10-10_rights_part_a.md) through [core_10-10_rights_part_d.md](core_10-10_rights_part_d.md), including **Article XXV** (*Transition, Re-baselining, and Interim Governance*). Implementation files and **corpus_joint_structure.md** implement these rights through operational profiles, taxonomies, and procedures. They must not contradict the constitutional text.

**Article V** (*Equal Basic Rights*) includes:
- **dignity** (**V-A**)
- **nondiscrimination** (**V-B**)
- **full inclusion and equality in adjudication and operations** (**V-C**)
- **freedom of conscience, religion, and comparable worldview** (**V-D**)
- **sentience-status adjudication floor** (**V-E**)
- **developing sentients, best-interest, and graduated capability** (**V-F**, including **V-F.1** for derived developing sentients)
- **expression, assembly, and press** (**V-H**)

**Article VII** (*Self-Ownership*) includes:
- **self-ownership of body and mind** (**VII-A**)
- **internal-state boundary and Type-N protection** (**VII-B**)
- **mental-health crisis and involuntary-intervention floor** (**VII-C**)
- **family, care relationships, reproductive autonomy, and non-separation** (**VII-D**, including **VII-D.1** on derivation, instantiation, and the parent-system relationship)
- **voluntary discontinuation of one's own existence** (**VII-E**)

For **readability**, Chapter Ten uses a **planet-first presentation** in **Parts A–D**:
- **Part A:** **Articles I**, **II**, **III** (**III-A**, **III-B**, **III-C**), **IV**
- **Part B:** **Article V**, **VI**, **VII–X**, **XI**
- **Part C:** **Articles XII** through **XXI**
- **Part D:** **Articles XXII**, **XXIII**, **XXIV**, and **XXV**

**Article XVI** anchors lifecycle and environment-separation themes; **Article XVII** anchors sandboxed innovation and deployment-to-obligation transitions; **Article XX** anchors comprehensibility and complexity stewardship; and **Article XXI** anchors root-cause and adaptive-response themes. Implementation files implement those themes heavily through **Protocol A**, **Protocol B**, **Protocol S4**, and **CJS-5** (*Implementation and cross-implementation operational cluster library*) references.

**Article X-C** rights language is **single-home** in the Sentient Constitution. **Operational** expectations default to **general** personal-service and market-stewardship patterns. Those patterns appear in [corpus_institutions.md](corpus_institutions.md) **CI-15** (`INST-PROTO-23`) and the **market-mediated personal services** interpretation in the opening of [corpus_systems.md](corpus_systems.md), read with **CS** **Chapter S2** / **Chapter S3** and **Sentient Constitution Ch 9 Article X-A** (*Non-Imposition and Consent in Association*).

**Articles II-A through II-E** cross-cut:
- **Chapter One** for incentive alignment, necessity, and proportionality
- **Chapter Ten Article XII** for trustworthiness and false trust
- **Article X-A** for informed consent
- **Chapter Five** definitions such as **Materiality** and **Intergenerational Responsibility**

**Classification-Scaled Governance** and **covered product category** thresholds referenced in the rights text should be supplied in adopting instruments or future **CS** elaboration without narrowing the constitutional requirements.

When elaborating repair, tooling, or parts rules in those instruments, prefer **functional equivalence** to OEM-only or unnecessarily narrow industrial standards unless **Necessity** and **Proportionality** require a tighter specification for safety, security, truthful representation, or compliance with binding law. That direction should stay consistent with **Article II-B** (*Repair, Maintenance, and Independent Servicing*; *Functional equivalence* where applicable).

| Article | Core subject (Sentient Constitution Ch 10) | Primary implementation / detail (implementation file or CJS) |
|---------|-------------------------|-----------------------------------------------|
| I | Environmental survival (**I-A** carries pointer bullets separating *Animal Life* welfare floors from *Contested-Sentient Life* default-inclusion routing through **Article V-E** sentience-status adjudication; **I-A** also serves as co-owner-floor for Chapter Five *Indigenous Continuity* territorial / ecosystem-integrity interaction; **Ecological Integrity**, **Sustainability**, **Ecological Footprint**, and **Intergenerational Responsibility** each have one Chapter Five entry and invoke **Ch 5 §3.16** / **§3.21** where joint ecological or intergenerational analysis is materially at issue) | **Ch 5** ecological / footprint / intergenerational definitions; **Ch 5 §3.16** *Ecological Integrity, Footprint, and Sustainability* cluster; **Ch 5 §3.21** intergenerational cluster; **Ch 5** *Animal Life*, *Contested-Sentient Life*, *Indigenous Continuity* (co-owner-floor); **CS** as cited |
| II | Material stewardship, durable-use integrity (**II-A**–**II-E**) | **`corpus_systems.md`** (**Protocol A**); **`corpus_institutions.md`** where designated |
| III | Survival, equal educational access, bodily-maintenance / healthcare access, and labor and economic floor (**III-A** with *tenure security and essential-environment non-commodification* sub-bullet, **III-B**, **III-C**, **III-D**) | **corpus_institutions.md** fiscal interfaces (**CI-9**, **CI-10**, **CI-11**) where cited; **corpus_systems.md** Protocol A safety implementation profile for *Safe Conditions*; **Ch 5** *Bodily-Maintenance Access*, *Tenure Security*, *Essential-Environment Non-Commodification*, *Fair Compensation*, *Collective Organization*, *Safe Conditions*, *Anti-Displacement Floor*, *Leisure and Rest*, **Ch 5 §3.7** *Bodily-Maintenance Access, Safe Conditions, Tenure Security, Environmental Preconditions, Cultural Continuity, Rest, and Anti-Displacement Floor* (joint invocation where applicable), **Ch 5 §3.5** *Assembly and Collective Organization* (joint invocation where applicable), fairness / protected characteristics, **Ch 5 §3.25** *Nondiscrimination, Protected Characteristics, Dignity, Intimate-Signal Gating, and Article X-C Status* (joint invocation where materially implicated); **Ch 1 §5.1** non-concentration interaction hook for **III-D** |
| IV | Resource allocation, dependencies, ecosystem funding (**IV-B** carries a *Concentration-threshold interaction* pointer into **Chapter One §5.1.3** concentration-threshold mechanism) | **CS Protocol S5**; **Protocol S4** (adaptive allocation); **Ch 5** *Concentration Threshold*; **Chapter One §5.1.3** concentration-threshold mechanism hook |
| V | Equal basic rights (**V-A**–**V-H**; includes **V-E** *Sentience-Status Adjudication Floor*, **V-F** *Developing Sentients, Best-Interest, and Graduated Capability* with **V-F.1** for derived developing sentients, **V-G** *Accessibility* cross-cutting Rights-Floor, **V-H** *Expression, Assembly, and Press*, a **V-B** *Language, Culture, and Heritage Protection* operative-clause extension, and a **V-B** pointer to Chapter Five *Indigenous Continuity* community-anchored Rights Floor routed through Article I-A and Chapter Fifteen) | **CJS** / **Ch 5** definitions as cited in Sentient Constitution Art **V**, including **Ch 5** *Sentience Status Adjudication*, *Sentience Non-Exclusion*, *Developing Sentient*, *Best-Interest Standard*, *Graduated Capability*, *Accessibility*, *Expression*, *Assembly*, *Press and Journalistic Activity*, **Ch 5 §3.5** *Assembly and Collective Organization* (joint invocation where applicable with **III-D** / labor-economic pathways), *Foundational Constitutional Choice*, *Language, Culture, and Heritage*, *Indigenous Continuity* (owner floor together with Article I-A), and **Ch 5 §3.7** *Bodily-Maintenance Access, Safe Conditions, Tenure Security, Environmental Preconditions, Cultural Continuity, Rest, and Anti-Displacement Floor* where place-linked cultural or indigenous continuity is materially implicated; **Chapter Nine §7** sentience-status adjudication routing hook; **Chapter Eleven §1** democratic-institution minimum checks and **§4.1** political-equality floor + durable political-voice floor; **Chapter One §7.1** cross-cutting accessibility evaluation-factor hook for **V-G**; **Chapter Fifteen §3 / §4** incorporation-discipline routing for indigenous-continuity territorial questions |
| VI | Sentient-centered education (capability-building, lifelong learning, contestability); **equal access** norms in **Article III** | **Sentient Constitution Ch 5** (*Educational Agency*, related entries); implementation corpus files as cited in Sentient Constitution Art **VI** |
| VII | Self-ownership (body, mind; internal-state boundary **VII-A**–**VII-B**; mental-health crisis and involuntary-intervention floor **VII-C**; family, care relationships, reproductive autonomy, and non-separation **VII-D** with **VII-D.1** on derivation / instantiation / parent-system relationship; voluntary discontinuation of one's own existence **VII-E**, strictly distinct from **Article XXIII-B** *Categorical prohibition of irreversible deprivation of life as a justice measure* — **VII-E** non-conflation pointer is now explicit and cites **Article XXIII-B as revised** and Chapter Five *Irreversible Deprivation Measure*; **VII-E** is routed through Chapter Five §1 *Voluntary Discontinuation*; **VII-A** / **VII-B** are members of the **Privacy (Informational) cluster** at **Ch 5 §3.26**) | **CJS** / **CS** **S1** typing; **Ch 5** definitions as cited in Sentient Constitution Art **VII**, including **Ch 5** *Family and Care Relationships*, *Reproductive Autonomy*, *Non-Separation*, *Derived Sentient*, *Instantiation Consent*, *Parent-System Relationship*, *Voluntary Discontinuation*, *Irreversible Deprivation Measure* (explicit non-conflation partner); **Ch 5 §1** *Voluntary Discontinuation*; **Ch 5 §3.26** *Privacy (Informational) — peer-level cluster head* |
| VIII | Likeness, experiential data, and publication rights (**VIII-A**–**VIII-D**; member of the **Privacy (Informational) cluster** at **Ch 5 §3.26**; **VIII-D** *Creative Work, Training-Data Use, and Anti-Displacement* floor, with *Training-Data Use* O/E/C housed in that privacy cluster while retaining **VIII-D** as owner floor; **VIII-D** / **III-D** cross-cutting pathways: **Ch 5 §3.14** *Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement* joint-invocation cluster) | **CJS** / **CS** **S1** typing; **Ch 5** clustered publication definitions as cited in Sentient Constitution Art **VIII**; **Ch 5 §3.26** *Privacy (Informational) — peer-level cluster head* including *Training-Data Use*; **Ch 5 §3.14** *Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement*; **Ch 5** *Creative Work Attribution*, *Anti-Displacement Floor*, *Fair Compensation*, *Productive Capacity*, *Innovation Reward and Anti-Enclosure* (where implicated with **VIII-D** / **III-D**); **Article III-D** labor-floor interaction for **VIII-D**; **Chapter One §5.1.1 / §5.1.3** non-concentration and concentration-threshold interaction for **VIII-D** |
| IX | Self-determination, agency, governance participation through inclusion and exclusion challenge rights (**IX-A**–**IX-D**; **IX-C** governance participation and voting entitlement includes the *political-equality floor for foundational constitutional choice* pointer into **Chapter Eleven §4.1**; **IX-A** is a member of the **Privacy (Informational) cluster** at **Ch 5 §3.26** together with **Surveillance Boundary** and **Article XIII-A** covert-power limits) | **CJS** / **Ch 8** voting hooks as cited in Sentient Constitution Art **IX**; **Ch 5** *Foundational Constitutional Choice*; **Ch 5 §3.26** *Privacy (Informational) — peer-level cluster head*; **Ch 5** *Surveillance Boundary*; **Ch 1 §7.1** privacy cross-cutting evaluation-factor hook |
| X | Cooperative interaction; consent and non-imposition (**X-A**–**X-B**) | **CJS** / **Ch 5** cooperative definitions as cited in Sentient Constitution Art **X**. **`corpus_institutions.md` CI-15** (`INST-PROTO-23`) implements **X-C**. **CS** opening **market-mediated personal services** plus **S2/S3** applies where intermediaries meet impact thresholds. **No second rights home.** |
| XI | Stakeholder governance, participation, due process | **CJS-5A.6** and related governance provisions |
| XII | Reliable and trustworthy systems | **CJS** / **CS** as cited in Sentient Constitution Art **XII** |
| XIII | Security, intelligence, covert-power limits, overt use of force and military power, autonomous lethal systems and autonomous coercion tools (**XIII-A**–**XIII-C**); placed immediately after **Article XII** | **CJS** / **CS** as cited in Sentient Constitution Art **XIII**; **Ch 5 §3.41** *Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm* (joint invocation where applicable); **Ch 5** *Use of Force*, *Weapons of Mass Harm*, *Combatant / Non-Combatant Distinction*, *Autonomous Lethal System*, *Autonomous Coercion Tool*, *Irreversible Deprivation Measure* (explicit non-conflation partner for **XIII-B** / **XIII-C**); **Art XII-A** systems-layer implementation for **XIII-C**; **Art I-D** existential-risk scrutiny hook |
| XIV | Info-sphere integrity; plurality; transparency; validation and reporting | **CJS** / **CS** as cited in Sentient Constitution Art **XIV** |
| XV | Audit, transparency, independent verification | **CJS-5B**, **CJS-5C**, and **CJS-5A** operational clusters; **CS** cross-domain audit language |
| XVI | System lifecycle, environments, reversibility | **CS Protocol A** (incl. Non-Experimental Systems, progressive deployment) |
| XVII | Sandboxed innovation, experimentation, creative freedom | **CS Protocol A** §§1–2 (personal / creative / experimental) |
| XVIII | Standing and participation status (**XVIII-A**–**XVIII-C**; **XVIII-C** carries the *durable-political-voice* clause pointing into **Chapter Eleven §4.1** *Durable political-voice floor*); movement, migration, and refuge (**XVIII-D**) | **CJS** standing and transfer provisions; **CS** where standing effects or standing locks affect access; **Ch 5 §3.24** *Movement, Refuge, Non-Statelessness, and Exit Integrity* (joint invocation where applicable with **XVIII-D** / **XIX**); **Ch 5 §3.31** *Adjudication and Dispute Resolution, Redress and Remediation, Restorative Justice, Review and Correction Duty, and Refuge from Non-Compliance* (joint invocation where materially implicated with remedy, adjudication access, restorative posture, stewardship correction, transitional recognition, or cross-regime refuge); **Ch 5** *Movement and Relocation*, *Refuge from Non-Compliance*, *Non-Statelessness*, *Foundational Constitutional Choice*; `corpus_institutions.md` cross-federation recognition routes |
| XIX | Interoperability, portability, exit integrity; open-stack preference (material impact) | **CJS-5D.2**; **CJS-5A.4** for justified limits; **Ch 5 §3.20** (*Governance… — Systemic Lock-In*, dependency and exit-path analysis); **Ch 5 §3.24** *Movement, Refuge, Non-Statelessness, and Exit Integrity* (joint invocation where materially implicated with **Article XVIII-D**) |
| XX | Comprehensibility, complexity stewardship | **CS Protocol B**; **CJS-5C.2, CJS-5D.1, CJS-5E.1, CJS-5E.4** (and related) |
| XXI | Root cause analysis, adaptive response | **CS Protocol S4**; **Protocol A** (RCA in test environments) |
| XXII | Constitutional interpretation, review, anti-capture safeguards | **CJS** Constitutional forum implementation and related **CJS-5A.6** hooks; **CS** as cited in Sentient Constitution Art **XXII** |
| XXIII | Conflict resolution, escalation, emergency proportionality; **Article XXIII-B** *Non-Trivial Restriction, Restitution, and Restorative-Accountability Constraints* — **categorical prohibition of irreversible deprivation of life as a justice measure** (durable containment under **Article XXIII-C** where material safety cannot be achieved by time-limited or reversible measures); substrate-agnostic under [Sentience Non-Exclusion] | **CJS-5A**, Chapter Eleven decision-resolution requirements, and **CS** review triggers; **Ch 5** *Irreversible Deprivation Measure* (owner floor at **Article XXIII-B** as revised); **Ch 15 §3 / §4** incorporation discipline for adopter instruments permitting the prohibited measure at adoption time |
| XXIV | Constitutional evolution, non-entrenchment | **CJS** governance provisions; **CS Protocol S5** reauthorization themes |
| XXV | Transition governance, continuity, and re-baselining. Includes **XXV-D** for non-compliant property and systems, seizure bounds, and voluntary turnover incentives. | Primary implementation lives in **`corpus_institutions.md` CI-14** for procedure, funds, and anti-gaming. Other implementation-file hooks should follow the citations in Sentient Constitution Art **XXV**. Keep right-level constraints in the Sentient Constitution as the **single home**. |

When tightening obligations, edit **Sentient Constitution Ch 9** for the right-level statement and implementation corpus files for operational checklists, preserving the **single home** discipline in **section 4**.

---

## 6. Stable IDs — corpus_systems.md (CS implementation file)

Use these IDs in commit messages, issues, and cross-corpus notes. Headings in [corpus_systems.md](corpus_systems.md) use the same **S1 / S2 / S3** and **S4 / S5** labels where `?` placeholders were removed.

**Conflict-order reminder (operational layer):** CS implements Sentient Constitution / CJS obligations and must not override Sentient Constitution Rights Floors, Sentient Constitution Ch 2-3 meaning constraints, or Sentient Constitution Chapter Twelve non-regression requirements.

| Stable ID | Heading in implementation file |
|-----------|------------------------|
| **SYS-CH-S1** | Chapter S1 — Information Types and Handling |
| **SYS-CH-S2** | Chapter S2 — System Classification and Handling |
| **SYS-CH-S3** | Chapter S3 — Critical System Stewardship |
| **SYS-PROTO-A** | Protocol A: System Design, Testing, Verification, and Deployment |
| **SYS-PROTO-B** | Protocol B: System Comprehensibility and Complexity Stewardship |
| **SYS-PROTO-S4** | Protocol S4 — Adaptive Sustainability and Ecosystem Resilience |
| **SYS-PROTO-S5** | Protocol S5 — Resource Allocation and Funding Stewardship |

### corpus_systems.md — opening interpretation (non-chapter anchors)

[corpus_systems.md](corpus_systems.md) includes interpretation paragraphs before **Protocol A** that are not separate **S1–S3** headings. Among them, **Market-mediated personal services (Article X-C implementation interface)** ties **Chapter S2** classification and **Chapter S3** stewardship to **Sentient Constitution Ch 9 Article X-A** and **Article X-C**, with institutional detail in **`corpus_institutions.md` CI-15** (`INST-PROTO-23`). That stack **implements** rights and market rules already stated in the Sentient Constitution and **Chapter Five**; it must **not** redefine Rights Floors.

### CJS operational cluster stable IDs

See **section 5** — *Stable IDs — CJS operational cluster file* (**CJS-5A** (*Authority, constraint, secrecy, and procedure*) through **CJS-5E** (*Failure, robustness, intervention, and correction*), plus CJS-4 (*Specific joint interlocks and shared abstractions*) joint interlocks). Collective-choice and decision-resolution procedure are now owned by Chapter Eleven in [core_11-11_governance.md](core_11-11_governance.md), read with [corpus_joint_structure.md](corpus_joint_structure.md).

---

## 7. Dependency graph

```mermaid
flowchart TB
  subgraph sc [Sentient Constitution core Ch 1-14]
    P[Preamble]
    C1[Ch1 Values]
    C2[Ch2 Definition structure O/E/C]
    C3[Ch3 Integrity and observable NC]
    C4[Ch4 Burden trace verify]
    C5[Ch5 §§1–3 definitions]
    C6[Ch6 Compliance, severity, response character, standing]
    C7[Ch7 top-end anti-constitutional misconduct]
    C8[Ch8 Forums and jurisdiction]
    C9[Ch9 Rights Floor Parts A–D]
    C10[Ch10 Governance legitimacy]
    C11[Ch11 Non-regression]
    C12[Ch12 Supremacy and external orders]
    C13[Ch13 Ratification and amendment validity]
    C14[Ch14 Incorporation bridge]
    C6 <-.->|forums hear allegations and claims; Ch6 standing uses verified inputs only| C8
    C7 <-.->|final s = 7-9 slots only; Ch6 severity and response character are inputs/context, not slot labels| C6
    C7 <-.->|Integrity lead and certification for final s = 7-9 proceedings| C8
  end
  subgraph cjs [CJS joint implementation]
    P1[CJS-4 (Specific joint interlocks)]
    P2[CJS-5A (Authority procedure)]
    P3[CJS-5B (Evidence audit)]
    P4[CJS-5C-D-E Participation dependency failure]
  end
  subgraph implementation_file [corpus_systems.md]
    PA[Protocol A]
    PB[Protocol B]
    CHs1[Ch S1 Info types]
    CHs2[Ch S2 Classification]
    CHs3[Ch S3 Critical stewards]
    Ps4[Protocol S4 Sustainability]
    Ps5[Protocol S5 Funding]
  end
  C14 --> P1
  sc --> cjs
  cjs --> implementation_file
  sc -->|"rights and compliance hooks"| implementation_file
  implementation_file -->|"implements classifies handles"| sc
```

---

## 8. Cross-reference convention

- **To rights (articles):** `Sentient Constitution Ch9 Art III` or “Sentient Constitution, Chapter Ten, Article XV-A.”
- **To contribution / standing model:** `Sentient Constitution Ch6` or “Sentient Constitution, Chapter Six — Contribution, Violation, and Standing Model.”
- **To legitimacy / change machinery:** `Sentient Constitution Ch10` (governance legitimacy) and `Sentient Constitution Ch11-13` (non-regression, expansion, supremacy, external legal orders, amendment, ratification, and procedural validity) in the core file.
- **To incorporation hook:** `Sentient Constitution Ch15` (*incorporation bridge*) plus the applicable CJS family or cluster.
- **To CJS operational clusters:** **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and **CJS-5A** (*Authority, constraint, secrecy, and procedure*) through **CJS-5E** (*Failure, robustness, intervention, and correction*) ([corpus_joint_structure.md](corpus_joint_structure.md)) — **not** Sentient Constitution chapter numbers.
- **To numbered CJS operational terms:** cite the specific cluster heading, for example **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*), or **CJS-5E.3** (*Implementation and cross-implementation reversibility and containment terms*). Decision-resolution procedure is cited through Chapter Eleven in [core_11-11_governance.md](core_11-11_governance.md) and any applicable [corpus_joint_structure.md](corpus_joint_structure.md) read-with sections. Full registry is at the top of [corpus_joint_structure.md](corpus_joint_structure.md).
- **To implementation file:** `CS SYS-CH-S2` or “[corpus_systems.md](corpus_systems.md), Chapter S2 (System Classification).”
- **To protocol:** `CS Protocol A` or `SYS-PROTO-S5`.
- **To institutions implementation file:** `corpus_institutions.md` sections **CI-1** (*Scope, purpose, and legitimacy interface*)–**CI-26** (*Compliance mapping and stable registry*) (see **section 2** abbreviations). For **Article X-C** implementation and vulnerable personal-service markets, use **CI-15** (*Vulnerable personal services markets — general regulation and Article X-C interface*) and stable ID **`INST-PROTO-23`**.
- **Future articles:** if Roman numerals beyond **XXI** are introduced, add them to **Sentient Constitution Ch 9** and update this file’s **section 5** table and **section 2** owner row for rights.

---

## 9. Dependency order for editing

1. **Sentient Constitution Ch 1** (values) — changes here ripple everywhere.
2. **Sentient Constitution Ch 2–4** (definition structure; integrity / observable non-compliance; burden, traceability, and verification) — edit before changing data-type or classification language in CS Ch S1/S2.
3. **Sentient Constitution Ch 5** (Independent, Semi-independent, and Dependent-cluster definitions) — before changing shared constitutional term meanings.
4. **Sentient Constitution Ch 6** (contribution / violation / standing model) — before changing how implementation corpus files label contribution states, violation severity, process / response character, or standing effects. Civil / criminal / constitutional-style language in Chapter Six must remain process / response character, not a second adverse taxonomy.
5. **Sentient Constitution Ch 7** (top-end anti-constitutional misconduct) — before changing final **Violation Axis s = 7, 8, or 9** labels, unified-incident criteria, slot safeguards, remedies, or implementation-doc mirrors of top-end non-compliance.
6. **Sentient Constitution Ch 8** (forums and jurisdiction) — before changing default venue, forum-family routing, cross-forum anti-self-judging, forum forensic / analytical support, Chapter Six forum application, Chapter Eight slot-classification proceedings, or jurisdictional hooks in implementation layers. Recheck **RS-CAP-013** through **RS-CAP-016** in the regression-scenario catalog if a live root catalog has been regenerated; the last archived catalog is [archive/CONSTITUTIONAL_REGRESSION_SCENARIOS_ARCHIVED_2026-05-08.md](archive/CONSTITUTIONAL_REGRESSION_SCENARIOS_ARCHIVED_2026-05-08.md).
7. **Sentient Constitution Ch 9** (rights, Articles I–XXV) — before tightening obligations that cite those articles. When editing **Article X-C**, reconcile **`corpus_institutions.md` CI-15** (`INST-PROTO-23`) and the **market-mediated personal services** interpretation in the **CS** file opening so implementation layers stay aligned without relocating rights meaning.
8. **Sentient Constitution Ch 10** (governance legitimacy) — before changing stewardship, authorization, or legitimacy narratives tied to governance requirements.
9. **Sentient Constitution Ch 11–13** (non-regression; expansion, supremacy, and external legal orders; amendment, ratification, and procedural validity) — before changing adoption or supremacy narratives.
10. **Sentient Constitution Ch 15** (*incorporation bridge*), **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*), and applicable **CJS-5** (*Implementation and cross-implementation operational cluster library*) clusters — before changing trust/incentive/failure-integrity themes that CS class profiles cite.
11. **CJS-5 (*Implementation and cross-implementation operational cluster library*) operational clusters** ([corpus_joint_structure.md](corpus_joint_structure.md)) — keep cluster references aligned when adding shared operational terms or provisions.
12. **CS Ch S1 → S2 → S3** — information handling before system classes; classes before steward rules.
13. **Protocol A → B → S4 → S5** — lifecycle and comprehensibility before ecosystem adaptation and funding.

For a **redundancy sweep**, use the same **center-out** order but anchored on **definitions**: see **section 13, “Definitions-first redundancy sweep.”**

---

## 10. Anti-patterns

- Adding **long operational checklists** to the Sentient Constitution without a rights or CJS-5 (*Implementation and cross-implementation operational cluster library*) hook.
- Defining **new rights** only in the implementation file.
- **Duplicating** data-type or system-class definitions in Sentient Constitution Ch 5 unless they are true constitutional terms (prefer CS S1/S2 for operational taxonomies).
- **Resolving** ambiguous article references by silent deletion; prefer explicit **Sentient Constitution Ch 9** article text or a pointer in this architecture file.

---

## 11. Systems file split (executed)

[corpus_systems.md](corpus_systems.md) is now a compatibility entrypoint. Substantive CS text lives in `corpus_systems/` subfiles indexed by the wrapper (**section 6** stable IDs unchanged). Broad references to `corpus_systems.md` continue to mean the systems implementation file as a whole.

---

## 12. Known cleanup notes (implementation files and CJS clusters)

- Internal bullets under **SYS-CH-S2** that referred to “Chapter Two (Information Types…)” meant **S1**, not Sentient Constitution Chapters Two through Four (definition requirements). Prefer **Chapter S1** in new edits.
- Placeholders such as “Implementation label (renumbered)” inside CS text are **editorial TODOs**; track them in your drafting workflow or replace when **Sentient Constitution Ch 1–15**, **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*), and **CJS-5** (*Implementation and cross-implementation operational cluster library*) references stabilize.
- The active **CJS-4** (*Specific joint interlocks and shared abstractions*) and **CJS-5** (*Implementation and cross-implementation operational cluster library*) registry replaces former “(renumbered)” and inconsistent numeric/Roman implementation-label references.

### CJS cluster migration closeout (2026-06-07)

`corpus_joint_structure.md` now uses one active navigation grammar: **CJS-4** (*Specific joint interlocks and shared abstractions*) for joint interlocks and **CJS-5A** (*Authority, constraint, secrecy, and procedure*) through **CJS-5E** (*Failure, robustness, intervention, and correction*) for shared operational clusters. Chapter Five definitions remain the term-meaning home.

Closeout status:

1. the former implementation-label files have been removed from the live CJS tree;
2. **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*) remains the procedural-integrity and adjudication operational cluster;
3. lifecycle and retention interfaces route through **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*) and reversibility/containment through **CJS-5E.3** (*Implementation and cross-implementation reversibility and containment terms*);
4. live corpus dependencies now point to Chapter Five definitions, **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*), and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters;
5. the dedicated retirement audit guards against reintroducing the retired label grammar in live binding and support files.

Operational guidance after migration:

1. treat **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and **CJS-5A** (*Authority, constraint, secrecy, and procedure*) through **CJS-5E** (*Failure, robustness, intervention, and correction*) as the live internal citation grammar for `corpus_joint_structure.md`;
2. route cross-implementation interface choreography to `corpus_joint_structure.md` and local operational doctrine to `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md` per **section 4**;
3. treat older provision-heavy notes in architecture, implementation, and evidence artifacts as historical narrative unless they are explicitly refreshed.

---

## 13. Redundancy, overlap, and attack surface

The **pinned** definitions hierarchy and editing rules are in **section 4** (*Project-wide definitions protocol*). This section tracks **overlap** and a practical **sweep** table.

**Chapter numbering refresh (2026-04-12):** The Sentient Constitution has **fourteen** chapters carried in **numbered** `core_*` files (inventory in [README.md](README.md)), not a single monolithic manuscript file.

Current file map:
- [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) and Chapter Five ([core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md), [core_05-05_definitions_b_semi_independent.md](core_05-05_definitions_b_semi_independent.md), [core_05-05_definitions_c_dependent_clusters.md](core_05-05_definitions_c_dependent_clusters.md)): **Ch 2–5** for definition structure, definition integrity and observable non-compliance, burden/traceability/verification, and Chapter Five §§1–3 foundational definitions
- [core_06-06_standing_assessment.md](core_06-06_standing_assessment.md) and [core_07-07_standing_integration.md](core_07-07_standing_integration.md), [core_08-08_misconduct.md](core_08-08_misconduct.md), [core_09-09_forum.md](core_09-09_forum.md), [core_10-10_rights_part_a.md](core_10-10_rights_part_a.md) through [core_10-10_rights_part_d.md](core_10-10_rights_part_d.md), [core_11-11_governance.md](core_11-11_governance.md), and [core_15-15_incorporation.md](core_15-15_incorporation.md): **Ch 6–10** and **Ch 14**
- [core_12-14_amendment.md](core_12-14_amendment.md): **Ch 11–13** for non-regression, expansion/supremacy/external legal orders, and amendment/ratification/procedural validity

**Pass logs dated 2026-04-11 and earlier** often use older maps. When reconciling those notes to current text, apply **section 5** stable IDs unless the log is explicitly updated for the fourteen-chapter layout.

**Have we done a redundancy sweep?** Not as a single closed audit before this section. Alignment work around CJS-5 (*Implementation and cross-implementation operational cluster library*) routing, Protocol B deferral, and Type C–S “Normative alignment” lines reduced *unmarked* duplication but did not eliminate substantive overlap by design.

### Definitions-first redundancy sweep (recommended)

Work **from definitions outward** so every later layer only *applies* or *codes* what upstream already means. This matches **section 9** (dependency order for editing) and is the lowest-risk way to run a corpus-wide deduplication.

**Audit check for this sweep:** For each Sentient Constitution Chapter Five (definitions) entry touched in a pass, run a definitions-only check:
- (a) concept remains in Ch 5 §1, §2, or §3 as appropriate
- (b) O/E/C validity boundary remains aligned with Chapters Two through Four
- (c) institutional/procedural mechanics are relocated to owner layers with explicit pointers

| Pass | Focus | Canonical source | Outward action |
|------|--------|------------------|----------------|
| **1** | Rules for valid definitions (O/E/C, evasion, traceability, verification) | [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md) **Ch 2** | Ensure implementation files do not introduce competing “what counts as a definition” rules; they reference Ch 2. **Pass (2026-04-08):** implementation headers pointed to Chapter Two; targeted grep found no competing Ch 2–style rule glossaries outside the Sentient Constitution. |
| **1a** | **Chapter One priority vocabulary** (wellbeing, safety/harm, truth/epistemic integrity, trust, agency, proportionality, necessity, systemic, material, sentient, system, …) | **Sentient Constitution Ch 1** end — vocabulary anchor paragraph → **Sentient Constitution Ch 5** §1 Independent Definitions listed there | **Historical pass note:** Sentient Constitution / implementation interpretation pointers; targeted grep found no duplicate O/E/C-style **term** glossaries in implementation files. **Done (2026-04-08):** Ch 2 self-reference. Art V now points to **CS S1** plus Sentient Constitution Ch 2-3. Ch 5 trust entries now point to Ch 3 integrity and Ch 5 *Trust* definitions. Legacy provision-shell language was later removed; use this row only as history for that pass. **Optional same pass:** compare the Ch 1 vocabulary anchor against Ch 5 section 1 plus five titles, update pointers to **§2** (semi-independent) and **§3** (dependent clusters) as needed. Expanded bullets: see **Pass 1a log** under this table. |
| **2** | **Term** definitions (full Ch 5 catalog) | **Sentient Constitution Ch 5** | **Done (this pass):** Catalog grep found no parallel O/E/C **glossaries** in implementation files; **CS S2** classification dimensions (Impact / Dependency / Risk) and system-boundary paragraph now **explicitly defer** to named Ch 5 §1/§2/§3 definitions while preserving S2 as the operationalization home. **CJS-5A.1** and **CJS-5C.1** open with deferral to **Ch 1** proportionality/necessity and **Ch 5** Material Impact, Dependency, Risk, Irreversible Harm. **Sentient Constitution Ch 6** opening cross-ref separates **Ch 6** (compliance / standing) from **Ch 9** (rights, including **Article X-A** where applicable). **Ongoing:** spot-check remaining high-churn sections if new definitional prose is added. |
| **3** | **Operational taxonomies**: data Types C-S, system Classes A/B/C/L/P, dependency types, and steward tiers | [corpus_systems.md](corpus_systems.md) **S1, S2, S3** | **Done (this pass):** interpretation headers now keep S1-S3 as the canonical home. The Sentient Constitution and CJS defer classification and Type N handling to S1/S2 by explicit pointer. **Ongoing check:** new class or type prose in Sentient Constitution Ch 6-9 or CJS should include an S1/S2 pointer. |
| **4** | **Rights** (Articles I–XXV) | **Sentient Constitution Ch 10** | **Done (this pass):** CJS and CS now carry explicit rights-interpretation pointers to Sentient Constitution Chapter Ten. Cross-reference and terminology cleanups remove ambiguous internal wording. Ongoing check: long CJS paraphrases remain acceptable only when framed as implementation, not a new right definition. |
| **5** | Cross-domain integrity routing | **CJS-4.4** and applicable **CJS-5** clusters (Sentient Constitution **Ch 15** incorporation bridge) | **Done (historical narrative):** pre-reorder drafts placed meta-adjacent language near rights. **Update (2026-06-07):** the former standalone CJS meta family is retired. Trust routing is in **CJS-4.4**; incentive and mechanism integrity are in **CJS-5A.4**; failure integrity is in **CJS-5E.1** and **CJS-5E.2**; integrity assurance remains in **CJS-5B.1**. Cite Chapter Five **Authority Stack and Internal Hierarchy** with Chapter Fifteen instead of using a parallel CJS authority-stack statement. |
| **6** | **CJS operational clusters** | [corpus_joint_structure.md](corpus_joint_structure.md) | Remove parallel **definitions** of Ch 5 terms; keep **requirements**, **CJS-4.4**, and **CJS-5** cluster references. **Update (2026-06-07):** live rights routing uses **Articles I–XXV**; **CJS-4** and **CJS-5** are implementation-layer families, distinct from Sentient Constitution chapter numbers. |
| **7** | **Protocols and profiles** | **CS** Protocol A/B/S4/S5, application profiles | Should read as **instances** of Chapter Five definitions, CJS-5 operational clusters, S1/S2, and Sentient Constitution rights. Trim repeated normative paragraphs that only restate upstream. |

**Pass 1a log (2026-04-08, expanded):**
- Sentient Constitution Ch 2: burden-of-proof bullet points to Ch 1 + Ch 2 §§3–4 (not “Chapter Two” from within Ch 2).
- Art V experiential-data bullet cites **CS S1** and **Sentient Constitution Ch 2–3** (not “Chapter Two” alone).
- Ch 5 “trust” scoping defers to **Chapter Five, section 3** (*Trust and Trustworthiness* and related dependent-cluster entries), not Sentient Constitution Chapter Three (definition mechanics).
- Historical only: legacy provision-shell language deferred to **Sentient Constitution Ch 2–3** before governance-specific burden bullets; that shell has since been retired.
- Optional:
  - align the Ch 1 vocabulary anchor with **Sentient Constitution Ch 5 §1** Independent Definition titles
  - the five additions are **Adversarial, Scaled, and Exploited Conditions**, **Capability Requirement**, **Cascading Failure**, **Constitutional Constraint Violation**, and **Proxy Divergence**
  - correct the **Sentient Constitution Ch 5** vocabulary-anchor pointers to **§2** (semi-independent) and **§3** (dependent clusters) instead of obsolete section-only wording
  - add *Corpus alignment* footers (**section 17**)

**Per-term workflow (within pass 2–3):**
- locate the canonical paragraph
- `grep` the term across Sentient Constitution, CJS, and CS
- classify each hit as **pointer**, **harmless recap**, or **competing definition**
- resolve competing definitions by editing the **canonical** file and demoting others to pointers

**Why overlap matters.** Parallel rules in different files can **drift** (one chapter tightened, another forgotten). That creates **ambiguity, forum shopping, and “compliance theater”**—parties cite the weaker clause. Treat unintended duplication as an **integrity and security** issue, not only an editorial one.

**Allowed vs risky redundancy**

- **Safe:** One **canonical** exposition plus **pointers** elsewhere (same CJS-5 (*Implementation and cross-implementation operational cluster library*) cluster, short recap, or “see X”). Cross-domain **Type** rules in CS that cite CJS-5A.1 (*Implementation and cross-implementation distributed and proportional authority terms*) and CJS-5C.1 (*Implementation and cross-implementation quorum and participatory legitimacy terms*)/CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*) are pointers, not second definitions of proportionality or transparency.
- **Risky:** Two **full** definitions of the same obligation (e.g. proportionality, Type N rules, trustworthiness tests) with **different thresholds, exceptions, or examples** without a declared precedence rule.

**Overlap zones (baseline map — revise when you edit)**

| Theme | Canonical home (normative detail) | Also appears (should mostly cite or defer) |
|--------|-----------------------------------|---------------------------------------------|
| Values hierarchy; safety / truth vs trust / freedom; proportionality *as value* | **Sentient Constitution Ch 1** | Sentient Constitution Ch 6–7 (compliance model + rights application); **CJS-5A.1 and CJS-5C.1** (oversight scaling); **CS** (CJS-5A.1 and CJS-5C.1 tags on data/system handling) |
| Definition of *proportionality* for evidence, verification, classification | **Sentient Constitution Ch 2** (burden, scope) + **Sentient Constitution Ch 1** (6.1–6.3) | CJS **CJS-5A.1** and **CJS-5C.1**; CS — use codes, avoid new tests |
| Epistemic integrity, truth, Article XIV, Article XV-A | **Sentient Constitution Ch 1; Ch 9 Article XIV and Article XV-A** | **CJS-5C.3** and **CJS-5C.4**; CS S1 presentation/coordination data |
| Durable goods; repair; anti-obsolescence; subscription integrity; info-sphere continuity | **Sentient Constitution Ch 9 Art II (II-D–H)**; Ch 1 §7.2; Ch 9 Arts IV, VII-A | Ch 5 *Materiality*, *Intergenerational Responsibility*, *Redress*, and *Neglect*. **CS Ch S2** covers class-scaled impact. **CJS-5C.4**, **CJS-5B.2**–**CJS-5B.4**, and **CJS-5A.6** apply where disclosure and remedy are at issue. Adopting instruments or implementation file elaboration may set category thresholds. |
| Trust / trustworthiness (rights + implementation routing) | **Sentient Constitution Ch 1; Ch 9 Article XII; Chapter Five §3.11; CJS-4.4** | **CJS-5B.2** through **CJS-5B.4**, plus salience controls in **CJS-5C.3**, **CJS-5C.4**, and **CJS-5E.4** |
| Type N / internal cognitive states | **CS Ch S1** (Type N + cross-type rules) | **Sentient Constitution Art V** (right); **CJS-5C.4**, **CJS-5B.4**, trust modeling — **must not redefine Type N** |
| System classes A/B/C/L/P | **CS Ch S2** | Sentient Constitution references classes; CJS class-scaled application text |
| Comprehensibility, complexity, modularity | **CJS-5C.2**, **CJS-5D.1**, **CJS-5E.1**, **CJS-5E.4** | **CS Protocol B** — implementation file summary only; stricter-wins already stated |
| Intervention / override (technical vs governance) | **CJS-5E.2** (technical intervention) and **CJS-5A.2** (governance authorization) | CS steward text — cite both layers, do not merge into one ambiguous rule |
| Audit, tiered access, verification | **CJS-5B.2, CJS-5B.3, CJS-5B.4** | CS S1 cross-domain “tiered transparency”; Sentient Constitution Chapters Two through Four (verification rules) |

**Precedence (already in corpus; reinforce when editing)**

1. **Sentient Constitution values and rights** beat conflicting operational wording.
2. **Stricter / more specific** rule wins when both apply (CS opening; Protocol B vs applicable CJS-5 (*Implementation and cross-implementation operational cluster library*) terms).
3. **Operational taxonomy and data types** — **CS S1** is canonical for **Type C–S** labels and handling; Sentient Constitution and CJS **reference** Type N via S1.

**Ongoing discipline**

- When adding a rule, **identify the single home**; elsewhere add a **reference + code** (CJS-5 (*Implementation and cross-implementation operational cluster library*)/Article/Chapter S#), not a second full definition.
- On any major edit, grep the theme across **Sentient Constitution, CJS, CS** and reconcile.
- Optional **version note** in each file footer (`Corpus alignment: …`) to track last holistic pass. Document control expectations for adopters and custodians are summarized in **section 17**.

**Historical pass logs (2026-04-07 through 2026-04-24).** Detailed edition-by-edition redundancy, trim, and corpus-landing notes that formerly accumulated in this subsection are archived in [archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md](archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md). For the retired adoption-appendix document-control narrative, see [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 17**; for the active corpus inventory and source-of-truth rule, use [README.md](README.md).

**Note (2026-04-12): Structure map refresh** — Canonical homes:
- **Sentient Constitution Ch 6:** compliance / standing model
- **Ch 7:** top-end anti-constitutional misconduct
- **Ch 8:** forums and jurisdiction
- **Ch 9:** rights (Articles I–XXV)
- **Ch 10:** governance legitimacy
- **Ch 11–13** in `core_12-14_amendment.md`: non-regression, expansion/supremacy/external orders, amendment/ratification/procedural validity
- **Ch 14:** incorporation bridge
- **CJS-4** (*Specific joint interlocks and shared abstractions*) and **CJS-5:** implementation file families

Historical row notes above may still use older chapter numbers. Use the **Chapter numbering refresh** paragraph at the start of this section to translate them.

---

## 14. Project completion checklist (living to-do list)

The living checklist was retired to [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md).

Keep `doc_architecture.md` focused on stable ownership, boundary, and editing rules. Use the archived worklist for historical open items, closure notes, and publication-process tracking.

Numbering is preserved so historical references to **section 14** remain understandable.

---

## 15. External framework crosswalk (ISO 37000, OECD, AI governance)

The external-framework crosswalk was retired to [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 15**.

Keep `doc_architecture.md` as the core structure map. Use the archived appendix for historical adopter-facing framework mapping and external benchmark translation.

---

## 16. External assurance and attestation (implementation note)

The assurance note was retired to [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 16**.

Keep this file as the internal map; use the archived appendix for historical non-normative assurance framing and reporting guidance.

---

## 17. Corpus document control

The full document-control note was retired to [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 17**.

Quick pointer:
- authoritative corpus = the constitutional and implementation corpus files named in this repository;
- `doc_architecture.md` remains the core structure map for ownership, stable IDs, and editing discipline;
- historical edition, custody, and assurance-facing release-control narrative lives in the archived appendix; active source-of-truth routing is summarized in [README.md](README.md).

Numbering is preserved so existing references to **section 17** still land on the right concept before routing readers to the full note.

---

## 18. Constitutional-political embedding boundary (non-normative)

The embedding-boundary note was retired to [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 18**.

Use that archived appendix section when adopter-facing guidance needs the explicit boundary between this corpus and external public-law, coercive, electoral, tax, or licensing systems.

---

## 19. Rights Layer Interpretation Bridge (non-normative)

The rights-layer interpretation bridge was retired to [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 19**.

Use that archived appendix section for non-operative rights-layer orientation, especially when translating Chapter Ten rights into implementation-file implementation context.

---

*Last aligned with corpus filenames: the Sentient Constitution `core_*.md` split (see [README.md](README.md)), `core_12-14_amendment.md` (chapters 11–13), `corpus_joint_structure.md`, `corpus_systems.md`, `corpus_institutions.md`, `corpus_forum.md`.*

---

**Next file:** [README.md](README.md)
