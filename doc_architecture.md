# Constitution document architecture

This file is the **editor map** for the Sentient Constitution corpus. **Binding text** lives in the numbered `core_*` files (inventory in [README.md](README.md)), [corpus_joint_structure.md](corpus_joint_structure.md), [corpus_systems.md](corpus_systems.md), [corpus_institutions.md](corpus_institutions.md), and [corpus_forum.md](corpus_forum.md). **Corpus** is defined in [Chapter Five Chapter One §8.16 *Corpus, Authority Stack, Supremacy, and Enforceability*](core_05a_accountability_definitions.md#corpus-authority-stack-supremacy-and-enforceability-cluster). Edition labels and custody metadata: [README.md](README.md).

Retired architecture sections **14–19** (worklist, adoption appendix, document control) → [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) and [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md).

---

## 1. Purpose

- **Avoid duplication** — owner routing in **section 2**; definitions protocol in **section 4**.
- **Preserve dependency order** — edit order in **section 9**.
- **Track gaps** — stable IDs via `make architecture-index` ([generated index](doc_architecture/generated/stable_id_index.md)).
- **Keep human and AI readable** — consistent headings, stable anchors, explicit cross-references. Auxiliary exports (PDF, plain text) are **non-authoritative** derivatives.

### Canonical filename convention

- `snake_case` canonical filenames (no spaces; no `%20` links).
- Core pattern: `core_<start>-<end>_<short_owner_label>.md` (zero-padded chapters).
- Full inventory: [README.md](README.md). Chapter One spans **Chapter 00** (`core_00_preamble.md`) and **Chapter One, Parts A–B** (`core_01_a_values_principles.md`, `core_01_b_stewardship_capacity_principles.md`); numeric headings (`CHAPTER 00`, `CHAPTER 01`) remain the instrument-opening exception.

### Rename readiness gate

Filename renames require: reference audit, same-change link updates, dated evidence under `evidence/<date>/`, compatibility decision, and edition/custody record. Until the gate passes, candidate names stay planning-only.

---

## 2. Corpus roles (single source of truth)

**Numbering note:** When a passage says only “Chapter Twelve,” disambiguate by filename — see [README.md](README.md).

**Constitutional owner layers:** canonical positive register — [Chapter Five — Constitutional Owner Layers](core_05i_integrative_definitions.md#constitutional-owner-layers). The table below is the editorial mirror; substantive owner discipline and non-relocation rules live in that Chapter Five entry.

| Layer | Primary home | Routing |
|--------|--------------|---------|
| Values, definition mechanics, definitions | Sentient Constitution `core_*` Ch 1–5 | [README.md](README.md) reading order |
| Rights (Articles I–XXV) | Ch 6 | `core_06-06_rights_part_*.md`; titles via `make reference-audit` |
| System alignment certification | Ch 7 | `core_07-07_system_alignment_certification.md` |
| Standing pipeline | Ch 8–10 | `core_08-08_standing_assessment.md` through `core_10-10_misconduct.md`; comprehension layer: [Chapters Eight–Eleven compass](core_08-08_standing_assessment.md#chapters-eight-eleven-constitutional-compass) |
| Forums (constitutional) | Ch 11 | `core_11-11_forum.md` (same compass) |
| Governance / amendment / incorporation | Ch 12–16 | `core_12-12_governance.md`, `core_13-15_amendment.md`, `core_16-16_incorporation.md` |
| Cross-implementation joint structure | CJS | [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-2.1** (*Topic router*) |
| Systems, institutions, forum operations | CS / CI / CF | Companion wrappers + subfiles |

**Footer policy:** `make footer-audit`. Optional `*Corpus alignment:*` cites [README.md](README.md) edition metadata and [Chapter Five *Corpus*](core_05i_integrative_definitions.md#corpus).

**Authority stack:** (1) numbered `core_*` constitutional source; (2) incorporated implementation within adoption scope; (3) this map and process docs unless explicitly adopted; (4) Sentient Constitution meaning controls operational layers — see [Authority Stack and Internal Hierarchy](core_05i_integrative_definitions.md#authority-stack).

---

## 3. Boundary rules

1. **Core owns** normative *why* and *what* (values, rights, definitions, meta obligations).
2. **Implementation files own** *how* (taxonomies, protocols, institutions, forums, joint interlocks).
3. **No duplicate definitions** across layers — implementation files *apply* Chapter Five terms.
4. **Stricter wins** where the corpus already says so; core values and rights prevail over conflicting operational wording.
5. **Chapter Six implements detail** for Articles I–XXV; do not invent parallel rights in implementation files.

---

## 4. Project-wide definitions protocol (pinned)

Machine-checkable rules: [tools/architecture/rule_registry.json](tools/architecture/rule_registry.json). Audit catalog: [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md). Lexical guardrails: [tools/architecture/lexical_guardrails.json](tools/architecture/lexical_guardrails.json).

### What counts as a definition

- **Hard definitions:** Ch 2–4 (`core_02-04_definition_mechanics.md`); Chapter Five §1–§3 (single-home rule below).
- **Values language:** Chapter 00 §1 — [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad), [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims) (**Flourishing** / **Continuity**), and [material stake](core_00_preamble.md#material-stake) at principle layer; Chapter Five O/E/C for Tetrad legs ([Participation](core_05p_participation_definitions.md#participation-constitutional), [Oversight](core_05o_oversight_definitions.md#oversight-constitutional), [Accountability](core_05a_accountability_definitions.md#accountability), [Timeliness](core_05a_accountability_definitions.md#timeliness-constitutional)) and aims ([Flourishing](core_05p_participation_definitions.md#flourishing-constitutional), [Continuity (Constitutional Aim)](core_05c_continuity_definitions.md#continuity-aim-constitutional)); Chapter One develops those aims into operative principles; vocabulary anchor + cluster index at end of Chapter One, Part A (§§1–8). **Reading arc:** Part A (values, bounded agency, tradeoffs, override prohibition, interpretation) → Part B (§§9–13 stewardship through systemic evaluation) → **§14 Integrated Application** capstone in Part B. Use **Continuity aim** when linking to Chapter One §11; reserve bare *continuity* for operational uses elsewhere.
- **Standing:** Ch 8–9 (**verified** inputs); Ch 11 forums for **allegations**, not standing-record classification inputs.
- **Rights:** Chapter Six; implementation files **cite** articles.
- **Joint operational terms:** `corpus_joint_structure.md` only — route via **CJS-2.1**.
- **Operational taxonomies:** **CS-3**, **CS-4**, **CS-5** and named protocols.

### CJS owner rule

Use **CJS** only for cross-implementation interface terms with no stable single-file home. Reusable joint terms → **CJS-5** clusters; **CJS-4** interlocks point to **CJS-5** and the primary owner named in **CJS-2.1**. Escalate to Chapter Five when constitutional meaning is at stake.

### Chapter Five admission gate

Keep constitutional concept + O/E/C boundary only; cite owner homes for institutional machinery. **`make ch5-definitions-gravity-audit`** (blocking).

**Band layout (June 2026):** Part A ([`core_05-05_definitions_a_independent.md`](core_05-05_definitions_a_independent.md)) holds the compass, alphabetical directory, and §3.0 joint-invocation meta rules. Definition bodies live in five constitutional band files — **Oversight** [`core_05o_oversight_definitions.md`](core_05o_oversight_definitions.md) (Chapter One §8.2–§3.3), **Participation** [`core_05p_participation_definitions.md`](core_05p_participation_definitions.md) (§3.5–§3.7), **Accountability** [`core_05a_accountability_definitions.md`](core_05a_accountability_definitions.md) (§3.8–Chapter One §8.11), **Continuity** [`core_05c_continuity_definitions.md`](core_05c_continuity_definitions.md) (Chapter One §8.12–Chapter One §8.15), **Integrative** [`core_05i_integrative_definitions.md`](core_05i_integrative_definitions.md) (Chapter One §8.16). Each band file contains §1 Independent, §2 Semi-independent, and §3 Dependent cluster entries assigned to that leg or aim. Retired Part B/C paths live under [`archive/core_ch5_retired/`](archive/core_ch5_retired/README.md) only.

### Editorial rule registry

| Rule ID | Summary | Gate |
|---------|---------|------|
| NAV-TRACE-08–10 | Trace placement and contents | `make ch9-trace-audit`, `make trace-routing-prose-audit` |
| NAV-READER-06 | Reader-guidance widget placement | Manual |
| NAV-DEC-12 | D/E/C widget discipline | `make ch5-dec-widget-audit`, `make nav-widget-spacer-audit` |
| NAV-DEC-12-ORDER | Trace → D/E/C placement | `make trace-dec-widget-order-audit` |
| NAV-DEC-12-SPACER | `<br>` after collapsible D/E/C only | `make nav-widget-spacer-audit` |
| NAV-DEC-CH1-ORDER | Chapter One D/E/C row order | `make ch1-dec-order-audit` |
| NAV-PLACEMENT-01 | File-top Corpus placement widget | `make file-top-placement-audit` |
| LINK-IN-PARA-14 | Load-bearing in-paragraph links | `make in-paragraph-link-audit` |
| CH5-GRAVITY | Chapter Five admission / de-bundling | `make ch5-definitions-gravity-audit` |
| CH5-ORDER-01 | Chapter Five editorial order | `make ch5-cluster-order-audit`, `make ch5-entry-format-audit`, `make ch5-constitutional-cluster-audit` |
| CH5-SINGLE-DEF | One visible definition per term | `make ch5-single-definition-audit` |
| LEX-GUARDRAILS | Vocabulary and capitalization | `make lexical-vocabulary-audit` |
| GLOSS-SUBARTICLE | Chapter Six `*In plain terms:*` on subarticles | `make subarticle-gloss-audit` |
| OWNER-SINGLE-HOME | Competing O/E/C gloss heuristics | `make owner-discipline-audit` |
| REF-ARTICLES | Article titles and Roman numerals; prose cite gloss per **section 7** | `make reference-audit` |
| ROUTER-CJS21 | Cross-implementation routing | `make router-bidirectional-audit` |

Historical D/E/C rollout: [archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md](archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md).

### Reader-guidance placement (NAV-READER-06)

Collapsed **Reader guidance (non-operative)** widgets give readers orientation without creating, narrowing, or relocating binding obligations.

**Placement rule:**

- **Chapter-level or part-level orientation** belongs at the chapter or part opening: after the file-top **Corpus placement** widget and chapter/part heading, and before the first operative purpose, rule, article, or numbered section.
- In split-chapter files, a part-position widget belongs immediately after that file's chapter/part heading and before the part's first operative section.
- **Local reader guidance** may appear later only when it explains a specific nearby table, directory, crosswalk, routing index, example set, or other local navigation aid. It should stay adjacent to the material it explains.
- Do not leave general reading order, layer routing, architecture maps, or anti-relocation orientation in the middle of operative prose. Move those into opening reader-guidance widgets.
- Reader-guidance widgets use the standard blue collapsed `<details>` styling and must state that the content is reader guidance only and does not add, remove, or narrow binding obligations.

### D/E/C widget template (NAV-DEC-12)

Collapsed **Definitions · Evaluation · Compliance** widget (same blue `<details>` styling as Trace). Trace carries routing only (`Upstream:`, `Downstream:`, `Read with:`); D/E/C carries Chapter Five O/E/C jump links at the point of invocation.

**When to attach**

- Attach where a section **materially invokes** Chapter Five concepts as working terms in its own substantive claims — not roadmap enumeration of terms treated downstream in named sections (*roadmap exclusion*; see archived decision log).
- **Two or more** invoked concepts → collapsible D/E/C widget.
- **Exactly one** invoked concept → single-line inline **`Definition:`** (no collapsible widget).

**Placement under the owning `###`–`#####` unit (NAV-DEC-12-ORDER)**

1. **With Trace** — D/E/C widget or inline `Definition:` immediately follows Trace `</details>`; only blank lines may intervene. Enforced by `make trace-dec-widget-order-audit` when Trace carries Chapter Five `· [O]` read-with links.
2. **Without Trace** — D/E/C widget is the **first substantive block under the heading**, before `*In plain terms:*` and operative prose. Legacy `<a id="…"></a>` anchors may follow the widget block (after its closing `</details>` and spacer). Example: Chapter One `#### 5.2 Voluntary Discontinuation and Exit Rights`.

**Spacer (NAV-DEC-12-SPACER)**

- Collapsible D/E/C widget: `<br>` after `</details>` before operative prose.
- Inline `Definition:` line: **no** `<br>` (standard paragraph break only).

**Inside the widget**

- **Row shape (enforced by `make ch5-dec-widget-audit`):** each row is  
  `- [Name](core_05…#slug) · [O](…) · [E](…) · [C](…)`.
- **Annotation prose (optional, non-row):** italic-label lines such as `*Scope.*`, `*Definition home.*`, or `*Cluster-head home.*` may appear as plain paragraphs inside the widget before the row list. They are **not** list bullets and must not mimic row shape.
- **Chapter One row order:** functional reasoning order, not alphabetical — config in [tools/architecture/ch1_dec_order.json](tools/architecture/ch1_dec_order.json); `make ch1-dec-order-audit`.

**Do not** put `Definitions:` lines inside Trace (2026-04-16 D/E/C split). **Do not** use visible group labels as fake list rows inside D/E/C widgets.

### File-top placement template (NAV-PLACEMENT-01)

One collapsed **Corpus placement** widget per audited file top. Summary label: **`Corpus placement (non-operative): file structure and reading rules`** (same blue `<details>` styling as Trace and Reader guidance).

**Visible before the first `##` heading (or first operative registry section):**

- `#` title.
- On implementation `*_00_registry_and_reading_rules.md` files only: one-line `*In plain terms:*` front-door gloss.
- The placement widget, then `<br>` when operative prose or `---` follows.

**Inside the placement widget (non-operative):**

- `core_*` — binding-together notice, which chapter/part/band the file holds, README reading-order pointer, and file-sequence navigation (**Next**, **Upstream**, **Previous**) when present.
- `*_00_registry` — edition and effective date, core vs implementation status, four-layer map (**CJS** / **CS** / **CI** / **CF**), navigation wrapper link, **CJS-1.2** pointer, and routing-anchor indexes previously split across multiple reader-guidance widgets.

**Do not keep visible at file top:** **Application baseline**, upstream inheritance boilerplate, or pipeline routing that duplicates the Corpus placement widget, chapter reader-guidance widgets, or [README.md](README.md). Chapter-specific scope boundaries and anti-substitution notes belong in the Corpus placement widget (file-level) or in chapter reader-guidance widgets (chapter-level within multi-chapter files).

**Single sources:** global edition and reading order in [README.md](README.md); implementation shared contract in **CJS-1.2**; section-family registries remain in `*_00` files below the file-top block.

### Plain-language guardrails (summary)

Capitalize **Constitutional Tetrad**, **Two Constitutional Aims**, **Flourishing**, **Continuity** (constitutional aim sense), **material stake**, **Wellbeing**, **Safety**, **Truth**, **Rights Floor**, and **Foundational Rights** when they name constitutional layers. Full tables: [tools/architecture/lexical_guardrails.json](tools/architecture/lexical_guardrails.json). Forum vocabulary: [.cursor/rules/sentient-constitution.mdc](.cursor/rules/sentient-constitution.mdc).

### Order and single-home discipline

Chapter Five editorial order: `make ch5-entry-format-audit`, `make ch5-alphabetical-directory-audit`, `make ch5-cluster-order-audit`, `make ch5-constitutional-cluster-audit`. For drift-prone concepts: one canonical paragraph (**section 2**; **CJS-2.1**); elsewhere pointers only.

**Precedence:** (1) Sentient Constitution values/rights; (2) Ch 2–3 for term meaning; (3) CS-3/4/5 for Type/Class/steward assignment; (4) stricter applicable rule where declared.

---

## 5. Stable IDs and routing indexes

Do not maintain hand-edited article or implementation maps here.

- **Sentient Constitution chapters:** [README.md](README.md) inventory.
- **Article titles / Roman numerals:** `make reference-audit` / Chapter Six part files.
- **Cross-implementation routing:** [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-2.1**; `make router-bidirectional-audit`.
- **Generated stable-ID index:** [doc_architecture/generated/stable_id_index.md](doc_architecture/generated/stable_id_index.md) via `make architecture-index`.
- **Topic router reader index (generated, human view):** [doc_architecture/generated/topic_router_reader_index.md](doc_architecture/generated/topic_router_reader_index.md) — plain-language grouped index derived from **CJS-2.1**; reading guidance in **CJS-0.1** ([cjs_00_registry_and_reading_rules.md](corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing)). Authoritative mandatory read-with lists remain in the integrator table.
- **CI-primary router slice (generated, integrator view):** [doc_architecture/generated/ci_primary_router_index.md](doc_architecture/generated/ci_primary_router_index.md) — filter of **CJS-2.1** rows whose primary owner is **CI**; do not duplicate in `corpus_institutions/` operative text.
- **CJS cluster bands:** Oversight **CJS-5.2–5.6**, Participation **CJS-5.7–5.10**, Accountability **CJS-5.11–5.15**, Continuity **CJS-5.16–5.21**, Integrative **CJS-5.22–5.23** — see [CJS-5.1 compass](corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md#cjs-51-constitutional-compass-and-cluster-map) and [corpus_joint_structure.md](corpus_joint_structure.md).
- **CS stable IDs:** [corpus_systems/cs_00_registry_and_reading_rules.md](corpus_systems/cs_00_registry_and_reading_rules.md).

---

## 6. Dependency graph

```mermaid
flowchart TB
  subgraph sc [Sentient Constitution core Ch 1-15]
    C1[Ch1 Values]
    C5[Ch5 definitions]
    C6[Ch6-8 standing pipeline]
    C9[Ch9 forums]
    C10[Ch10 rights]
    C15[Ch15 incorporation]
  end
  subgraph cjs [CJS]
    R[CJS-2.1 router]
    P[CJS-4 / CJS-5]
  end
  subgraph impl [CS CI CF]
    OPS[protocols and operations]
  end
  sc --> cjs --> impl
  sc --> impl
```

---

## 7. Cross-reference convention

- **Rights:** `Sentient Constitution Ch 6 Art III` or spelled-out article cite.
- **Standing / forums:** Ch 8–9; Ch 11 for allegations.
- **CJS:** specific **CJS-5.*n*** heading; router **CJS-2.1**.
- **CS / CI / CF:** named chapter or section label in the companion file.

### Chapter Six article and subarticle cite gloss (REF-ARTICLES-GLOSS)

When a Chapter Six article or subarticle is cited in **body prose** — outside its own `###` / `####` heading line — follow the Roman label with the canonical short title in parentheses:

**Format:** `**Article {label}** (*{title}*)`

Examples: `**Article XV-C** (*Verification Accessibility*)`; `**Article XXIII-G** (*Timely Resolution and Anti-Delay Floor*)`.

**Rules**

- **{label}** — Roman numeral (`III`) or subarticle label (`XV-C`), consistent with `REF-ARTICLES` / `make reference-audit`.
- **{title}** — text after the first colon in the owning heading in `core_06-06_rights_part_*.md` (`### Article III: …` or `#### Article III-A: …`). Do not repeat the word *Article* inside the parentheses.
- **Combined labels** (`**Article VII-A / VII-B**`): gloss each part, separated by `/`: `(*Self-Ownership of Body and Mind* / *Internal-State Boundary and Type-N Protection*)`.
- **Markdown links:** put the gloss on the same mention, after the link: `[Article XII-B](core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*Right to Challenge, Review, and Redress*)`.
- **First mention in a section** (or in a collapsed Trace / D/E/C widget) should include the gloss when the cite is load-bearing. Later mentions in the same `###`–`#####` unit may use the bare label if the reader is already oriented.
- **Headings** (`### Article …`, `#### Article …-…`) already carry the title; do not duplicate the gloss there.
- **Dense routing lists** may omit the gloss only when every entry is a self-explanatory chapter name (for example **Chapter Seven**) or when the same block already states each title on the same line.

**Source of truth:** Chapter Six part-file headings; verified by `make reference-audit`.

---

## 8. Dependency order for editing

1. Ch 1 → Ch 2–4 → Ch 5 → Ch 6 → Ch 7 → Ch 8 → Ch 9 → Ch 10 → Ch 11 → Ch 12 → Ch 13–15 → Ch 16.
2. Then **CJS-4.3** / **CJS-5**, then **CS-3 → CS-4 → CS-5**, then **Protocol A → B → S4 → S5**.

Redundancy sweeps: center-out from Chapter Five definitions (**section 13**).

---

## 9. Anti-patterns

- Long operational checklists in the Sentient Constitution without a rights or **CJS-5** hook.
- New rights defined only in implementation files.
- Duplicate Type/Class definitions in Chapter Five (prefer CS-3/CS-4).
- Silent deletion of ambiguous article references.

---

## 10. Systems file split (executed)

[corpus_systems.md](corpus_systems.md) is a compatibility entrypoint; substantive CS text lives in `corpus_systems/` subfiles.

---

## 11. Known cleanup notes

- Prefer **CS-3** over legacy “Chapter Two (Information Types…)” wording inside CS text.
- **CJS-4** and **CJS-5** are the live citation grammar for `corpus_joint_structure.md`.
- Route cross-implementation choreography to CJS; local doctrine to CS / CI / CF per **section 4**.

---

## 12. Redundancy, overlap, and attack surface

Definitions hierarchy: **section 4**. Pass logs archived: [archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md](archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md). Overlap themes: [archive/doc_architecture_decision_log/OVERLAP_THEME_TABLE_ARCHIVED_2026-06-15.md](archive/doc_architecture_decision_log/OVERLAP_THEME_TABLE_ARCHIVED_2026-06-15.md).

**Safe redundancy:** one canonical exposition + pointers. **Risky:** two full definitions with different thresholds without declared precedence.

**Ongoing discipline:** grep by theme on major edits; optional `*Corpus alignment:*` footers per [README.md](README.md) and [Chapter Five *Corpus*](core_05i_integrative_definitions.md#corpus).

---

*Last aligned with corpus filenames: see [README.md](README.md).*

---

**Next file:** [README.md](README.md)
