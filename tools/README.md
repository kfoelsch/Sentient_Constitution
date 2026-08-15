# Tools

Python utilities for this repository. Run from the repo root unless noted.

## Markdown conventions

Put a **blank line before** `---` when you mean a horizontal rule between sections. If `---` sits directly under a paragraph, CommonMark-style parsers may treat that paragraph as a Setext-style heading instead. `make corpus-markdown-audit` enforces this rule on corpus files.

Chapter Five and CJS-3 definition files use **one** `---` between reader units, with the next heading's `<a id>` anchors after that rule — not a second rule under the title. `make ch5-entry-format-audit` and `make cjs-operational-cluster-audit` enforce the shape (see `tools/definition_separator_format.py` and **CH5-FORMAT** in `doc_architecture.md`).

## Maintenance (safe to use on the live corpus)

| Target | Command |
|--------|---------|
| Article reference integrity (Chapter Six part files) | `make reference-audit` |
| Regression scenario matrix checks | `make scenario-audit` |
| Blocking regression bundle | `make regression` |
| Markdown / prose / definitions gravity | `make corpus-markdown-audit`, `make prose-continuity-audit`, `make ch5-definitions-gravity-audit`, `make ch5-o-scope-audit`, `make ch5-trace-crosslink-audit` |
| Corpus navigation footer chain and formatting | `make footer-audit` |
| Trace / D/A/C / reader-guidance `<br>` spacer discipline | `make nav-widget-spacer-audit` |
| Trace → D/A/C widget order (definition carrier immediately after Trace) | `make trace-dac-widget-order-audit` |
| File-top / section-opening widget stack (placement → reader → Trace → D/A/C) | `make widget-top-placement-audit` |
| File-top Corpus placement widget | `make file-top-placement-audit` |
| CJS-0.1 topic-router bidirectional read-with links | `make router-bidirectional-audit` |
| Binding corpus must not depend on `doc_architecture` for meaning/routing | `make support-doc-pointer-audit` |
| Chapter Five compound heading/member order | `make ch5-cluster-order-audit` |
| Chapter Five single-definition and owner-roster rule | `make ch5-single-definition-audit` |
| Chapter Five alphabetical directory and section 1 order | `make ch5-alphabetical-directory-audit` |
| Chapter One D/A/C functional ordering | `make ch1-dac-order-audit` |
| Readability estimates | `make readability-audit` |
| Plain-language jargon scan | `make plain-language-audit` |
| Chapter Four ↔ Seven pointer discipline | `make ch4-ch7-pointer-audit` |
| Regression bundle plus readability gate | `make regression-full` |
| Institutional benchmark review | `make best-practices-check` |
| AI alignment eval (advisory; Layer A/B handoff + willingness) | `make ai-alignment-eval` / `make ai-alignment-eval-evidence` |
| Four-layer alignment audit (principles · Def.* · oDef · Articles; advisory) | `make alignment-audit` |
| Chapter One ↔ Chapter Five only | `make ch1-ch5-alignment-audit` |
| Chapter One ↔ CJS-3 oDef (also in `make regression`) | `make ch1-cjs3-alignment-audit` |
| Preamble / Chapter One ↔ Chapter Six articles | `make ch1-ch6-alignment-audit` |

`alignment_audit.py` is the operator entry point for a structural alignment pass across principles, Chapter Five **Def.*** entries, CJS-3 **oDef** clusters, and Chapter Six Articles. It writes `alignment_audit_index_<date>.md` plus the three per-layer report / CSV / JSON families under `evidence/<date>/`. Semantic adequacy stays a manual-review item; the full pass is advisory and is not in `make regression`.

`reference_audit.py` builds the **canonical Chapter Six map** from merged `### Article …:` headings in `core_06-06_rights_part_*.md` (falling back across part files as needed). If a citation fails the audit, fix the citing file or the heading—not the audit script.

`apply_article_cite_gloss.py` adds missing **REF-ARTICLES-GLOSS** parenthetical titles to bare `**Article …**`, `[Article …](url)`, and unbolded `Article …` cites across the binding corpus (see `doc_architecture.md` section 7). Run after heading renames or bulk cite cleanup; review combined-label and bullet-specific edge cases by hand.

`ch5_trace_crosslink_audit.py` enforces the Chapter Five navigation-metadata rule: `Read with:` lines belong inside each entry's local `Trace` / `<details>` block, not in operative prose after the block closes. It does not ban selective same-file cross-definition links in O / E / C body text.

`trace_routing_prose_audit.py` enforces the binding-corpus rule that read-with routing stays inside Trace blocks. It also flags disguised navigation such as `Read them with …`, `Each … must be read with …`, `… also read **§…**`, and operative bullet labels such as `- *Read with.*` in operative prose.

`trace_dac_widget_order_audit.py` enforces Trace → D/A/C placement: when a `###`–`#####` unit's Trace block carries Chapter Five `· [O]` read-with links, the next block after Trace close must be a **Definitions · Assessment · Compliance** widget or a single-concept inline **Definition:** line, with only blank lines between. Without Trace, the D/A/C widget must be the first substantive block under `####` / `#####`. It also flags roadmap-only parent `###` D/A/C widgets (≤2 rows) when a `####` subsection owns operative definitions.

`widget_top_placement_audit.py` enforces the opening widget stack (**NAV-WIDGET-TOP-01** / **NAV-READER-06**): file-top widgets stay in order placement → reader guidance → Trace → D/A/C before ordinary operative prose (owner/home lines included), consecutive stack widgets may be separated by blank lines only (no `<br>` or prose between them), and when a section's direct content carries Trace / D/A/C those widgets open the unit. Local mid-section Traces under bold run-in titles (`**8.3. …**`) and child-heading widgets are out of scope for the parent.

`ch5_single_definition_audit.py` enforces the Chapter Five directory cleanup rule: one visible definition label, one directory row, no placeholder-only definition shells, and no repeated `Cluster members.` owner roster membership. Anchor fragments remain navigation targets only.

`ch9_trace_audit.py` enforces the Chapter Six trace-placement rule: each `#### Article …` subarticle in the rights split files must carry its own local `Trace` / `<details>` block, and each block must include both `Principles:` and linked `Definitions:` metadata.

`ch5_cluster_order_audit.py` guards selected Chapter Five compound §2 topic groups and §3 dependent clusters whose visible heading order is intended to mirror the internal entry/member order. Expand its expected set whenever a new compound heading is intentionally made order-bearing.

Machine-checkable editorial rules: [tools/architecture/rule_registry.json](tools/architecture/rule_registry.json). Full audit catalog: [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md).

`ch1_dac_order_audit.py` guards Chapter One D/A/C functional ordering using [tools/architecture/ch1_dac_order.json](tools/architecture/ch1_dac_order.json) (rule NAV-DAC-CH1-ORDER).

`readability_audit.py` excludes `MEMLOG.md` and `TODO.md` by default because those files are treated as AI-only working memory and project task tracking rather than reader-facing corpus prose.

`plain_language_audit.py` is an advisory checker for jargon-heavy reader notes and navigation prose. It flags exact phrases such as `extended narrative context` and `non-operative explanatory framing`, plus dense guidance sentences that stack abstract terms instead of plain words. Start by running it manually and tune the rule list before promoting it into a blocking bundle.

`ch4_ch7_pointer_audit.py` is an advisory checker for Chapter Seven pointer discipline against Chapter Four. It flags operative restatements of Chapter Four verification-substrate rules (burden, trace artifact, security-constrained verification, and related phrases) without upstream citations to Chapters Two through Four, and verifies the corpus-placement reader guidance names Chapter Four as verification-substrate owner. Run after edits to [`core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation`](../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation) or [`core_04-04_burden_traceability_verification.md`](../core_04-04_burden_traceability_verification.md) Chapter Four §§1–6; use `--strict` to block on findings.

## Retired migration scripts

One-off structural rewrite and migration helpers (Chapter Five cluster inserts, Chapter Six renumbering, corpus splits, D/A/C widget attachment, doc_architecture slim-down, etc.) were moved to [archive/tools_retired/](../archive/tools_retired/) on **2026-06-17**. **Do not run** them against the current tree unless you are deliberately replaying history from git; they can desync the corpus.

For **current** article numbers and titles, use `make reference-audit` or read Chapter Six in `core_06-06_rights_part_*.md`.
