# Tools

Python utilities for this repository. Run from the repo root unless noted.

## Markdown conventions

Put a **blank line before** `---` when you mean a horizontal rule between sections. If `---` sits directly under a paragraph, CommonMark-style parsers may treat that paragraph as a Setext-style heading instead. `make corpus-markdown-audit` enforces this rule on corpus files.

## Maintenance (safe to use on the live corpus)

| Target | Command |
|--------|---------|
| Article reference integrity (Chapter Ten part files) | `make reference-audit` |
| Regression scenario matrix checks | `make scenario-audit` |
| Blocking regression bundle | `make regression` |
| Markdown / prose / definitions gravity | `make corpus-markdown-audit`, `make prose-continuity-audit`, `make ch5-definitions-gravity-audit`, `make ch5-trace-crosslink-audit` |
| Corpus navigation footer chain and formatting | `make footer-audit` |
| Trace / D/E/C / reader-guidance `<br>` spacer discipline | `make nav-widget-spacer-audit` |
| Trace → D/E/C widget order (definition carrier immediately after Trace) | `make trace-dec-widget-order-audit` |
| File-top Corpus placement widget | `make file-top-placement-audit` |
| CJS-2.1 topic-router bidirectional read-with links | `make router-bidirectional-audit` |
| Chapter Five compound heading/member order | `make ch5-cluster-order-audit` |
| Chapter Five single-definition and owner-roster rule | `make ch5-single-definition-audit` |
| Chapter Five alphabetical directory and section 1 order | `make ch5-alphabetical-directory-audit` |
| Chapter One D/E/C functional ordering | `make ch1-dec-order-audit` |
| Readability estimates | `make readability-audit` |
| Plain-language jargon scan | `make plain-language-audit` |
| Regression bundle plus readability gate | `make regression-full` |
| Institutional benchmark review | `make best-practices-check` |

`reference_audit.py` builds the **canonical Chapter Ten map** from merged `### Article …:` headings in `core_10-10_rights_part_*.md` (falling back across part files as needed). If a citation fails the audit, fix the citing file or the heading—not the audit script.

`ch5_trace_crosslink_audit.py` enforces the Chapter Five navigation-metadata rule: `Read with:` lines belong inside each entry's local `Trace` / `<details>` block, not in operative prose after the block closes. It does not ban selective same-file cross-definition links in O / E / C body text.

`trace_routing_prose_audit.py` enforces the binding-corpus rule that read-with routing stays inside Trace blocks. It also flags disguised navigation such as `Read them with …`, `Each … must be read with …`, `… also read **§…**`, and operative bullet labels such as `- *Read with.*` in operative prose.

`trace_dec_widget_order_audit.py` enforces Trace → D/E/C placement: when a `###`–`#####` unit's Trace block carries Chapter Five `· [O]` read-with links, the next block after Trace close must be a **Definitions · Evaluation · Compliance** widget or a single-concept inline **Definition:** line, with only blank lines between.

`ch5_single_definition_audit.py` enforces the Chapter Five directory cleanup rule: one visible definition label, one directory row, no placeholder-only definition shells, and no repeated `Cluster members.` owner roster membership. Anchor fragments remain navigation targets only.

`ch9_trace_audit.py` enforces the Chapter Ten trace-placement rule: each `#### Article …` subarticle in the rights split files must carry its own local `Trace` / `<details>` block, and each block must include both `Principles:` and linked `Definitions:` metadata.

`ch5_cluster_order_audit.py` guards selected Chapter Five compound §2 topic groups and §3 dependent clusters whose visible heading order is intended to mirror the internal entry/member order. Expand its expected set whenever a new compound heading is intentionally made order-bearing.

Machine-checkable editorial rules: [tools/architecture/rule_registry.json](tools/architecture/rule_registry.json). Full audit catalog: [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md).

`ch1_dec_order_audit.py` guards Chapter One D/E/C functional ordering using [tools/architecture/ch1_dec_order.json](tools/architecture/ch1_dec_order.json) (rule NAV-DEC-CH1-ORDER).

`readability_audit.py` excludes `MEMLOG.md` and `TODO.md` by default because those files are treated as AI-only working memory and project task tracking rather than reader-facing corpus prose.

`plain_language_audit.py` is an advisory checker for jargon-heavy reader notes and navigation prose. It flags exact phrases such as `extended narrative context` and `non-operative explanatory framing`, plus dense guidance sentences that stack abstract terms instead of plain words. Start by running it manually and tune the rule list before promoting it into a blocking bundle.

## Retired migration scripts

One-off structural rewrite and migration helpers (Chapter Five cluster inserts, Chapter Ten renumbering, corpus splits, D/E/C widget attachment, doc_architecture slim-down, etc.) were moved to [archive/tools_retired/](../archive/tools_retired/) on **2026-06-17**. **Do not run** them against the current tree unless you are deliberately replaying history from git; they can desync the corpus.

For **current** article numbers and titles, use `make reference-audit` or read Chapter Ten in `core_10-10_rights_part_*.md`.
