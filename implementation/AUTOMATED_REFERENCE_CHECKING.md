# Automated Reference Checking

Single catalog for corpus integrity audits. Rule IDs map to [tools/architecture/rule_registry.json](../tools/architecture/rule_registry.json). Operational commands also appear in [tools/README.md](../tools/README.md) under *Maintenance*.

## Blocking bundle (`make regression`)

| Make target | Tool | Rule ID(s) | Notes |
|-------------|------|------------|-------|
| `reference-audit` | `tools/reference_audit.py` | REF-ARTICLES | Chapter Six article map from part-file headings |
| `measurement-anchor-audit` | `tools/measurement_anchor_audit.py` | MEAS-ANCHOR | Fails on links to removed Preamble `#measuring-*` category anchors |
| `ch5-measurement-tier-audit` | `tools/ch5_measurement_tier_audit.py` | MEAS-DEF-01 | Enforces `*Measurements:*` and tier-aligned E/C for approved seeds |
| `ch5-measurement-coverage-audit` | `tools/ch5_measurement_coverage_audit.py` | MEAS-COVERAGE | Seed ↔ hierarchy sync and bidirectional Ch00 §3 owner links |
| `doc-architecture-section-audit` | `tools/architecture/doc_architecture_section_audit.py` | — | No letter-suffixed `##` sections in doc_architecture |
| `support-doc-pointer-audit` | `tools/support_doc_pointer_audit.py` | SUPPORT-DOC-POINTER-01 | Binding corpus must not cite `doc_architecture` for meaning/routing (non-binding classifications and reading-chain footers allowed) |
| `primitive-retirement-audit` | `tools/primitive_retirement_audit.py` | — | Retired primitive label grammar |
| `section-abbreviation-descriptor-audit` | `tools/section_abbreviation_descriptor_audit.py` | — | `--changed-only` in regression |
| `scenario-audit` | `tools/scenario_audit.py` | — | When live regression catalog present |
| `corpus-markdown-audit` | `tools/corpus_markdown_audit.py` | — | Markdown structure |
| `footer-audit` | `tools/footer_audit.py` | — | Corpus navigation footer chain |
| `nav-widget-spacer-audit` | `tools/nav_widget_spacer_audit.py` | NAV-DAC-12-SPACER | D/A/C vs inline Definition spacer |
| `trace-dac-widget-order-audit` | `tools/trace_dac_widget_order_audit.py` | NAV-DAC-12-ORDER | D/A/C widget or inline Definition immediately after Trace |
| `widget-top-placement-audit` | `tools/widget_top_placement_audit.py` | NAV-WIDGET-TOP-01, NAV-READER-06 | File-top / section-opening widget stack before operative prose |
| `file-top-placement-audit` | `tools/file_top_placement_audit.py` | NAV-PLACEMENT-01 | File-top Corpus placement widget |
| `trace-routing-prose-audit` | `tools/trace_routing_prose_audit.py` | NAV-TRACE-10 | Read with inside Trace; flags disguised read-with routing in operative prose |
| `in-paragraph-link-audit` | `tools/in_paragraph_link_audit.py` | LINK-IN-PARA-14 | Proof registry + See anti-patterns |
| `ch5-definitions-gravity-audit` | `tools/ch5_definitions_gravity_audit.py` | CH5-GRAVITY | Admission gate / de-bundling |
| `ch5-trace-crosslink-audit` | `tools/ch5_trace_crosslink_audit.py` | NAV-TRACE-10 | Ch5 Read with placement |
| `ch5-entry-format-audit` | `tools/ch5_entry_format_audit.py` | CH5-FORMAT | Separators, suffix discipline |
| `ch5-alphabetical-directory-audit` | `tools/ch5_alphabetical_directory_audit.py` | CH5-ORDER-01 | Directory order |
| `ch5-single-definition-audit` | `tools/ch5_single_definition_audit.py` | CH5-SINGLE-DEF | One label per term |
| `ch5-dac-widget-audit` | `tools/ch5_dac_widget_audit.py` | NAV-DAC-12 | Widget row shape |
| `ch5-cluster-order-audit` | `tools/ch5_cluster_order_audit.py` | CH5-ORDER-01 | Compound heading order |
| `ch1-dac-order-audit` | `tools/ch1_dac_order_audit.py` | NAV-DAC-CH1-ORDER | Config: `ch1_dac_order.json` |
| `ch9-trace-audit` | `tools/ch9_trace_audit.py` | NAV-TRACE-08–10 | Chapter Six subarticle traces |
| `prose-continuity-audit` | `tools/prose_continuity_audit.py` | — | Stray indent / orphan lines |
| `lexical-vocabulary-audit` | `tools/lexical_vocabulary_audit.py` | LEX-GUARDRAILS | Config: `lexical_guardrails.json` |
| `cjs-operational-cluster-audit` | `tools/cjs_operational_cluster_audit.py` | — | CJS-3 placement |
| `router-bidirectional-audit` | `tools/router_bidirectional_audit.py` | ROUTER-CJS01 | CJS-0.1 router |

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
| `doc-architecture-section-audit` | `tools/architecture/doc_architecture_section_audit.py` | Numeric `##` sections only (no `1A`/`1B` letter suffixes) |

## Evidence workflow

1. Run the validation target (or `make regression`).
2. For dated artifacts: `make reference-audit-evidence`, `make prose-continuity-audit-evidence`, `make lexical-vocabulary-audit-evidence`, or `make architecture-inventory`.
3. Link evidence in closure notes when closing TODO items.

## Optional commit-time gate

`.githooks/pre-commit` runs `make regression` when binding corpus, audit tooling, or the `Makefile` change; runs `make todo-close-check` when `TODO.md` is staged.

Enable:

1. `chmod +x .githooks/pre-commit`
2. `git config core.hooksPath .githooks`

## Manual / editorial (no automated gate yet)

- **NAV-READER-06**, **NAV-INDEX-13**: reader-guidance widgets; Chapter Three §1 index
- **Single-home overlap sweep**: grep discipline in [doc_architecture.md](../doc_architecture.md) **section 12**; overlap theme table archived under `archive/doc_architecture_decision_log/`

Historical navigation decisions: [archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md](../archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md).
