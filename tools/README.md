# Tools

Python utilities for this repository. Run from the repo root unless noted.

## Maintenance (safe to use on the live corpus)

| Target | Command |
|--------|---------|
| Article reference integrity (Chapter Ten part files) | `make reference-audit` |
| Regression scenario matrix checks | `make scenario-audit` |
| Blocking regression bundle | `make regression` |
| Markdown / prose / definitions gravity | `make corpus-markdown-audit`, `make prose-continuity-audit`, `make ch5-definitions-gravity-audit`, `make ch5-trace-crosslink-audit` |
| Corpus navigation footer chain and formatting | `make footer-audit` |
| Trace / D/E/C / reader-guidance `<br>` spacer discipline | `make nav-widget-spacer-audit` |
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

`ch5_single_definition_audit.py` enforces the Chapter Five directory cleanup rule: one visible definition label, one directory row, no placeholder-only definition shells, and no repeated `Cluster members.` owner roster membership. Anchor fragments remain navigation targets only.

`ch9_trace_audit.py` enforces the Chapter Ten trace-placement rule: each `#### Article …` subarticle in the rights split files must carry its own local `Trace` / `<details>` block, and each block must include both `Principles:` and linked `Definitions:` metadata.

`ch5_cluster_order_audit.py` guards selected Chapter Five compound §2 topic groups and §3 dependent clusters whose visible heading order is intended to mirror the internal entry/member order. Expand its expected set whenever a new compound heading is intentionally made order-bearing.

`ch1_dec_order_audit.py` guards against AI drift in Chapter One D/E/C widgets by checking the highest-risk principle sections against the functional order documented in `doc_architecture.md` and `implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md`. It is intentionally narrow and blocking in `make regression`.

`readability_audit.py` excludes `MEMLOG.md` and `TODO.md` by default because those files are treated as AI-only working memory and project task tracking rather than reader-facing corpus prose.

`plain_language_audit.py` is an advisory checker for jargon-heavy reader notes and navigation prose. It flags exact phrases such as `extended narrative context` and `non-operative explanatory framing`, plus dense guidance sentences that stack abstract terms instead of plain words. Start by running it manually and tune the rule list before promoting it into a blocking bundle.

## Legacy Chapter Ten migration scripts

The following were used during **one-off structural rewrites** (readability order, planet-first Parts A–D, material-article insertion, likeness **Article VIII** split, **IX–XXIV** renumbering). They are **not** part of normal editing workflow.

**Do not run** them against the current tree unless you are deliberately replaying history; they can desync the corpus.

| Script | Notes |
|--------|--------|
| `ch7_map_iii_material_to_iv.py` | Old string-replacement map (material / agency article IDs); superseded by the current Chapter Ten part files. |
| `ch7_reorder_readability_iv_ix.py` | Historical heading reorder pass. |
| `ch7_article_renumber.py`, `ch7_bump_articles_iv_to_xxii.py`, `ch7_execute_planet_first_renumber.py`, `ch7_increment_from_info.py`, `ch7_fix_headings_post_cite.py` | Renumbering / heading fix helpers from migration windows. |
| `ch7_constraint_stack_ab_regression.py` | A/B regression over Chapter One §7 constraint stack; legacy harness that expected a monolithic `core_constitution.md` (file not present in the split-corpus tree; see `Makefile`). |
| `reletter_article_i.py` | Early Roman reletter experiment. |

For **current** article numbers and titles, use `make reference-audit` or read Chapter Ten in `core_10-10_rights_part_*.md`.
