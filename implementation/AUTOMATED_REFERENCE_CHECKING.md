# Automated Reference Checking

Single catalog for corpus integrity audits. Rule IDs map to [tools/architecture/rule_registry.json](../tools/architecture/rule_registry.json). Operational commands also appear in [tools/README.md](../tools/README.md) under *Maintenance*.

## Weight classes (what a second maintainer may relax)

Every blocking target below carries a **weight**. The weight says what a failure means and what a maintainer other than the original tool author may do when a gate is red and the fix is not obvious.

| Weight | Meaning of a failure | May it be relaxed? |
|---|---|---|
| **L — load-bearing** | A citation resolves to nothing or to the wrong place; a binding / non-binding boundary is crossed; a term has two homes; a derived index or pointer card has diverged from the source it points at; a schema contract is broken. Readers or AI lookups would be sent to the wrong text. | **No.** Fix the source or the citation. Never skip, soften, or delete the gate. If the tool itself is wrong, fix the tool and record why in the commit. |
| **S — structural** | A house structure that carries meaning by position is out of shape: Trace / D/A/C widget order, read-with routing leaking into operative prose, Chapter Five O-component scope bullets, companion anatomy, Markdown that would render a paragraph as a heading. The text still resolves, but the reading contract the corpus promises is broken. | **Temporarily**, by an operator decision recorded in the commit message, when a publication cut is blocked and the finding is confined to a non-core file. Restore before the next edition stamp. Never relax on `core_*` files. |
| **C — cosmetic** | Ordering, spacing, capitalization, vocabulary, abbreviation descriptors, spacer rows, duplicate legacy stubs. Nothing resolves differently; readers are not misrouted. | **Yes**, when the finding is a false positive or the rule is being revised: fix the config JSON (`lexical_guardrails.json`, `ch1_dac_order.json`, expected-set lists) rather than the corpus, or drop the target from `make regression` with a TODO row. Do not silently edit the tool to pass. |

Rules of thumb: (1) if the audit's *notes* column mentions **anchor, fragment, cite, pointer, lockstep, schema, single-definition, freshness, or binding**, treat it as L even if it looks fiddly; (2) `*-test` targets inherit the weight of the tool they test; (3) `make regression` should stay green at all three weights before a publication cut — the weight governs how a red gate may be *handled*, not whether it counts.

## Blocking bundle (`make regression`)

Order follows the Makefile `regression` list.

| Make target | Weight | Tool | Rule ID(s) | Notes |
|-------------|--------|------|------------|-------|
| `reference-audit` | **L** | `tools/reference_audit.py` | REF-ARTICLES | Chapter Six article map from part-file headings; every `Article …` cite must resolve |
| `measurement-anchor-audit` | **L** | `tools/measurement_anchor_audit.py` | MEAS-ANCHOR | Fails on links to removed Preamble `#measuring-*` category anchors |
| `ch5-measurement-tier-audit` | S | `tools/ch5_measurement_tier_audit.py` | MEAS-DEF-01 | Enforces `*Measurements:*` and tier-aligned E/C for approved seeds |
| `ch5-measurement-coverage-audit` | **L** | `tools/ch5_measurement_coverage_audit.py` | MEAS-COVERAGE | Seed ↔ hierarchy sync and bidirectional Ch00 §3 owner links |
| `doc-architecture-section-audit` | C | `tools/architecture/doc_architecture_section_audit.py` | — | No letter-suffixed `##` sections in doc_architecture |
| `support-doc-pointer-audit` | **L** | `tools/support_doc_pointer_audit.py` | SUPPORT-DOC-POINTER-01 | Binding corpus must not cite `doc_architecture` for meaning/routing (non-binding classifications and reading-chain footers allowed) |
| `steward-door-lockstep-audit` (+ `-test`) | **L** | `tools/steward_door_lockstep_audit.py` | — | `STEWARD_ENTRY_DOORS.md` cards and `steward_owner_clock_index.json` stay in lockstep with the boxed operative steward statements in core; a stale door misroutes a steward under pressure |
| `cs4-inspectable-action-log-validate` (+ `-test`) | **L** | `tools/cs4_inspectable_action_log_validate.py` | — | Schema self-check for the CS-4 §10 log contract (`implementation/schemas/`) |
| `sentience-status-adjudication-record-validate` (+ `-test`) | **L** | `tools/sentience_status_adjudication_record_validate.py` | — | Schema self-check for the Sentience-Status Adjudication Record |
| `section-label-anchor-audit` (+ `-test`) | **L** | `tools/section_label_anchor_audit.py` | SECTION-CITE-MATCH-01, SECTION-LABEL-ANCHOR-01, NAV-HEADING-SEQUENCE-01 | `§` / dotted-number link text must match the target heading and fragment; related cites need a current-numbering id; `core_*` numbered sibling headings must not duplicate or skip |
| `fossil-anchor-audit` (+ `-test`) | **L** | `tools/fossil_anchor_audit.py` | — | Pre-release fragment policy: one current id per heading, no fossil aliases that would let stale cites keep resolving |
| `primitive-retirement-audit` | C | `tools/primitive_retirement_audit.py` | — | Retired primitive label grammar |
| `section-abbreviation-descriptor-audit` | C | `tools/section_abbreviation_descriptor_audit.py` | — | `--changed-only` in regression |
| `scenario-audit` | **L** | `tools/scenario_audit.py` | — | Regression-scenario matrix integrity when the live catalog is present |
| `corpus-markdown-audit` | S | `tools/corpus_markdown_audit.py` | — | Markdown structure; a `---` directly under a paragraph turns it into a heading |
| `local-markdown-fragment-audit` (+ `-test`) | **L** | `tools/local_markdown_fragment_audit.py` | — | Inbound local `file.md#fragment` links to a selected source must resolve |
| `footer-audit` | S | `tools/footer_audit.py` | — | Corpus navigation footer chain (Previous / Next file) |
| `nav-widget-spacer-audit` | C | `tools/nav_widget_spacer_audit.py` | NAV-DAC-12-SPACER | D/A/C vs inline Definition spacer |
| `trace-dac-widget-order-audit` | S | `tools/trace_dac_widget_order_audit.py` | NAV-DAC-12-ORDER | D/A/C widget or inline Definition immediately after Trace |
| `widget-top-placement-audit` | S | `tools/widget_top_placement_audit.py` | NAV-WIDGET-TOP-01, NAV-READER-06 | File-top / section-opening widget stack before operative prose |
| `file-top-placement-audit` (+ `-companions`) | S | `tools/file_top_placement_audit.py` | NAV-PLACEMENT-01 | File-top Corpus placement widget (core; companions with `--include-companions`) |
| `family-map-audit` | S | `tools/generate_family_map_indexes.py --check` | — | Generated companion-wrapper family indexes match `family_map.json`; regenerate with `make family-map-indexes` |
| `companion-cite-audit` | S | `tools/companion_cite_audit.py` | — | Wrapper-only companion cites that should point at the owning subfile |
| `companion-anatomy-audit` | S | `tools/companion_anatomy_audit.py` | — | Reader-facing anatomy of companion subfiles |
| `companion-filename-audit` (+ `-test`) | S | `tools/companion_filename_audit.py` | NAV-IMPL-FILENAME-01 | Shared numeric prefix only for parts of one chapter |
| `trace-routing-prose-audit` | S | `tools/trace_routing_prose_audit.py` | NAV-TRACE-10 | Read with inside Trace; flags disguised read-with routing in operative prose |
| `in-paragraph-link-audit` | S | `tools/in_paragraph_link_audit.py` | LINK-IN-PARA-14 | Proof registry + See anti-patterns |
| `ch5-definitions-gravity-audit` | **L** | `tools/ch5_definitions_gravity_audit.py` | CH5-GRAVITY | Admission gate / de-bundling — machinery absorbed into a definition changes what the term binds |
| `ch5-o-scope-audit` | S | `tools/ch5_o_scope_audit.py` | — | Chapter Five O components carry In scope / Out of scope sub-bullets |
| `ch5-depends-on-audit` | C | `tools/ch5_depends_on_audit.py` | — | Optional `**Depends on:**` sub-bullet shape under O |
| `ch5-measurement-stub-audit` | C | `tools/ch5_measurement_stub_audit.py` | — | Redundant legacy measurement stubs |
| `ch5-trace-crosslink-audit` | S | `tools/ch5_trace_crosslink_audit.py` | NAV-TRACE-10 | Ch5 Read with placement |
| `ch5-entry-format-audit` | C | `tools/ch5_entry_format_audit.py` | CH5-FORMAT | One `---` above entry anchors; no stacks; suffix discipline |
| `ch5-alphabetical-directory-audit` | C | `tools/ch5_alphabetical_directory_audit.py` | CH5-ORDER-01 | Directory order |
| `ch5-single-definition-audit` | **L** | `tools/ch5_single_definition_audit.py` | CH5-SINGLE-DEF | One label per term — the single-home rule that makes `Def.*` cites unambiguous |
| `ch5-dac-widget-audit` | C | `tools/ch5_dac_widget_audit.py` | NAV-DAC-12 | Widget row shape |
| `ch5-cluster-order-audit` | C | `tools/ch5_cluster_order_audit.py` | CH5-ORDER-01 | Compound heading order |
| `ch5-constitutional-cluster-audit` | S | `tools/ch5_constitutional_cluster_audit.py` | — | Constitutional band placement and compass completeness |
| `ch1-dac-order-audit` | C | `tools/ch1_dac_order_audit.py` | NAV-DAC-CH1-ORDER | Config: `ch1_dac_order.json` |
| `ch9-trace-audit` | S | `tools/ch9_trace_audit.py` | NAV-TRACE-08–10 | Chapter Six subarticle traces present with Principles and linked Definitions |
| `prose-continuity-audit` | C | `tools/prose_continuity_audit.py` | — | Stray indent / orphan lines |
| `lexical-vocabulary-audit` | C | `tools/lexical_vocabulary_audit.py` | LEX-GUARDRAILS | Config: `lexical_guardrails.json`; vocabulary and load-bearing capitalization |
| `cjs-operational-cluster-audit` | S | `tools/cjs_operational_cluster_audit.py` | — | CJS-3 placement |
| `cjs3-cluster-term-order-audit` | C | `tools/cjs3_cluster_term_order_audit.py` | — | Alphabetical order of oDef sub-terms |
| `ch1-cjs3-alignment-audit` | S | `tools/ch1_cjs3_alignment_audit.py` | CJS-TRACE | Chapter One ↔ CJS-3 oDef cluster trace metadata |
| `router-bidirectional-audit` | **L** | `tools/router_bidirectional_audit.py` | ROUTER-CJS01 | CJS-0.1 topic router rows ↔ read-with links; a one-way row misroutes cross-file topics |
| `id-resolver-test`, `corpus-lookup-test` | **L** | `tools/test_generate_id_resolver.py`, `tools/test_corpus_lookup.py` | — | Tests for the AI lookup path (`corpus_lookup.py resolve / hydrate / door`) |
| `ai-manifest-validate` | **L** | `tools/validate_ai_manifests.py --check-freshness` | — | `ai_corpus/indexes/*` must be regenerated after source edits (`make ai-corpus-sync`); stale indexes point at text that no longer exists |

Load-bearing count: 17 targets (plus their tests). If only those pass, citations, homes, doors, schemas, and derived indexes are trustworthy; everything else is reading-contract shape or house style.

## Advisory / extended gates

| Make target | Tool | Rule ID(s) | Promotion path |
|-------------|------|------------|----------------|
| `plain-language-audit` | `tools/plain_language_audit.py` | PLAIN-JARGON | Phrase rules from `lexical_guardrails.json` |
| `subarticle-gloss-audit` | `tools/subarticle_gloss_audit.py` | GLOSS-SUBARTICLE | Chapter Six `*In plain terms:*` on `#### Article` |
| `readability-audit` | `tools/readability_audit.py` | — | `make regression-full`; optional `--with-subarticle-gloss` |
| `owner-discipline-audit` | `tools/owner_discipline_audit.py` | OWNER-SINGLE-HOME | Heuristic O/M/A/C outside Ch5; use `--strict` to block |
| `ch4-ch7-pointer-audit` | `tools/ch4_ch7_pointer_audit.py` | CH4-CH7-POINTER | Ch7 must cite Ch2–4 for verification substrate; use `--strict` to block |
| `ch5-cross-file-link-audit` | `tools/ch5_cross_file_link_audit.py` | — | Promote when clean |
| `ci-cjs-relocation-audit` | `tools/ci_cjs_relocation_audit.py` | — | Relocation drift evidence |
| `definition-appropriateness-audit` | `tools/definition_appropriateness_audit.py` | DEF-APPROPRIATENESS | Unified core vs CJS-3 placement; advisory by default; `--strict` to block |
| `alignment-audit` | `tools/alignment_audit.py` | — | Combined principles · Def.* · oDef · Articles index; writes dated evidence; not in `make regression` |
| `ch1-ch5-alignment-audit` | `tools/ch1_ch5_alignment_audit.py` | CORE-TRACE | Chapter One D/A/C widgets ↔ Chapter Five guideposts; oDef backlinks |
| `ch1-cjs3-alignment-audit` | `tools/ch1_cjs3_alignment_audit.py` | CJS-TRACE | Also in `make regression`; Chapter One ↔ CJS-3 oDef clusters |
| `ch1-ch6-alignment-audit` | `tools/ch1_ch6_alignment_audit.py` | — | Preamble / Chapter One ↔ Chapter Six articles, including Def.* and oDef cites |

### Definition appropriateness finding taxonomy (`definition-appropriateness-audit`)

| Check ID | Layer | Question |
|----------|-------|----------|
| `CORE-PLACEMENT` | Chapter Five | Correct band / §1–§3 home and structural invariants |
| `CORE-GRAVITY` | Chapter Five | Institutional or procedural machinery absorbed into definitions |
| `CORE-TRACE` | Chapter One ↔ Five | Principle anchors and complete O/M/A/C traceability |
| `CJS-PLACEMENT` | CJS-3 | Operational clusters only in CJS-3 (not CJS-1) |
| `CJS-TRACE` | Chapter One ↔ CJS-3 | Cluster trace metadata and guidepost triad completeness |
| `CJS-CONSTITUTIONAL-CREEP` | CJS-3 | OP rules matching Ch5 labels without Chapter Five pointers |
| `IMPL-COMPETING-GLOSS` | CS / CI / CF | O/M/A/C-shaped gloss outside Chapter Five |
| `IMPL-RELOCATION` | CI (operative body) | Cross-layer material that may belong in CJS-3 or Chapter Five; CS/CF owner layers use integration maps and `ci-cjs-relocation-audit` |
| `IMPL-NON-REDEFINITION` | CS / CI / CF | Definitional lead-ins for canonical Chapter Five terms |

Persistent ledger: `evidence/definition_audit/ledger.json`. Dated snapshots: `definition_appropriateness_report_*.md`, `definition_appropriateness_matrix_*.csv`, `definition_appropriateness_log_*.json`.

## Architecture maintenance

| Make target | Tool | Purpose |
|-------------|------|---------|
| `architecture-inventory` | `tools/architecture/inventory_doc_architecture.py` | Section sizes + external references → `evidence/<date>/` |
| `architecture-index` | `tools/emit_architecture_index.py` | `doc_architecture/generated/stable_id_index.md` |
| `plain-terms-edition` / `plain-terms-edition-check` | `tools/generate_plain_terms_edition.py` | Non-binding single-file gloss edition (`doc_architecture/generated/plain_terms_edition.md` + `.json`): heading + *In plain terms* gloss + one source link per core section; `--check` is an advisory freshness gate |
| `doc-architecture-section-audit` | `tools/architecture/doc_architecture_section_audit.py` | Numeric `##` sections only (no `1A`/`1B` letter suffixes) |

## Evidence workflow

1. Run the validation target (or `make regression`).
2. For dated artifacts: `make reference-audit-evidence`, `make prose-continuity-audit-evidence`, `make lexical-vocabulary-audit-evidence`, or `make architecture-inventory`.
3. Link evidence in closure notes when closing TODO items.

## Optional commit-time gate

`.githooks/pre-commit` runs `make regression` when binding corpus, audit tooling, or the `Makefile` change; runs `make todo-close-check` when `TODO.md` is staged.

**Status 2026-09-09:** the `.githooks/` directory is not present in this checkout; the gate is documented intent only. Until it is restored, run `make regression` by hand before a publication cut (the README checklist step).

Enable:

1. `chmod +x .githooks/pre-commit`
2. `git config core.hooksPath .githooks`

## Manual / editorial (no automated gate yet)

- **NAV-READER-06**, **NAV-INDEX-13**: reader-guidance widgets; Chapter Three §1 index
- **Single-home overlap sweep**: grep discipline in [doc_architecture.md](../doc_architecture.md) **section 12**; overlap theme table archived under `archive/doc_architecture_decision_log/`

Historical navigation decisions: [archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md](../archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md).
