# Chapter Eight process-order reorder (2026-10-07)

Architectural rule: **CH8-PROCESS-ORDER-01** in [doc_architecture.md](../../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01).

## Decision

Before the pre-release announcement, Chapter Eight (System Alignment Certification) was renumbered so its sections follow the order the certification work is done. The reason for doing it now: after the announcement, outside readers cite sections, and NAV-PRE-RELEASE-FRAGMENT-01 forbids redirect anchors, so a later move could not be softened.

Only order, labels, and links changed. No obligation was added, dropped, or reworded.

## Five phases

| Phase | Sections | File |
|-------|----------|------|
| I. Frame | §2 System Class Evaluation; §3 Challenging a Certification | Part A |
| II. Evaluate | §4 (always §4.1–§4.4; when implicated §4.5–§4.7; when triggered §4.8) | Part A |
| III. Review | §5 Forum Process | Part B |
| IV. Record | §6 System Certification Record | Part B |
| V. Decide and keep current | §7 Outcomes, Recertification, and Reopening; §8 Relationship to Standing | Part B |

## Old to new numbers

| Old | New | Title |
|-----|-----|-------|
| A 1, 1.1, 1.2, 2, 2.1 | unchanged | |
| A 3 | A 4 | Whole-System Certification Evaluation |
| A 3.1 | A 4.1 | Systemic Scope and Risk Factors |
| A 3.5 | A 4.2 | Time-Consistency Constraint |
| A 3.6 | A 4.3 | Governance, Incentive, and Contestability Discipline |
| A 3.7 | A 4.4 | Data Types and Handling Evaluation |
| A 3.2 | A 4.5 | Privacy (Informational) Joint Invocation |
| A 3.3 | A 4.6 | Voluntary Discontinuation, Major Self-Modification, and Exit Rights |
| A 3.4 / 3.4.1 | A 4.7 / 4.7.1 | Assembly, Collective Organization, and Institutional Formation / Dissent and Peaceful Protest |
| A 3.8 and 3.8.k | A 4.8 and 4.8.k | Rights-Floor and Domain Evaluations and the six domain evaluations |
| B 4, 4.1, 4.2 | B 6, 6.1, 6.2 | System Certification Record; Minimum record contents; Record integrity |
| B 5, 5.1, 5.2 | unchanged | Forum Process; Forum supervision and component roles; Supervisory sequence |
| B 5.3 | **A 3** | Challenging a Certification (retitled from "Challenging a certification") |
| B 5.3.1 | **A 3.1** | Contestability paths |
| B 5.3.2 | B 5.3 | Contestability chain |
| B 5.3.3 | B 5.4 | Anti-bypass |
| B 6, 6.1, 6.2, 6.2.1, 6.3 | B 7, 7.1, 7.2, 7.2.1, 7.3 | Outcomes, Recertification, and Reopening and its subsections |
| B 7 | B 8 | Relationship to Standing |
| C 3.7.1 | C 4.4.1 | Illustrative data-handling application |
| C 3.8.k.1 | C 4.8.k.1 | Illustrative domain applications |

Anchors are the slug of "number title" (one current anchor per heading; no fossil anchors).

## Reading aids added (all non-operative)

- Part A §1.1: five-phase paragraph, redrawn chart (Phase I Frame through Phase V Decide and keep current), phase table.
- Part A §4: visible tier table (always, when implicated, when triggered) with a statement that it does not narrow any subsection.
- Hub (`core_08_system_alignment_certification.md`): phase table, run sheet, record checklist, recognition-status table.
- Part B §7.2: trigger list punctuation fixed (a dangling "; and" ended the first nested list).

## Verification

- Rewrite tool: `tools/ch8_process_order_reorder.py` (mapping-driven; links, anchors, bare cites; translations included; historical dirs untouched except anchor retargeting in `evaluation/external_audit_2026-08/`).
- `make -k regression`, before and after, on a clean copy of tracked files: the same five targets fail before and after (`ch5-measurement-coverage-audit`, `corpus-markdown-audit`, `prose-continuity-audit`, `lexical-vocabulary-audit`, `ai-manifest-validate`). Findings inside them differ only in line numbers.
- Passing after the change: `local-markdown-fragment-audit`, `section-label-anchor-audit`, `section-cite-name-audit`, `fossil-anchor-audit`, `anchor-heading-drift-audit`, `widget-top-placement-audit`, `reference-audit`.
- `tools/obligation_inventory_diff.py` over Parts A, B, and C: 295 clauses before, 294 after. The one missing clause is a reader-guidance sentence in §1.1 ("Part A covers what must be evaluated; Part B covers…") that was rewritten into the five-phase paragraph. All other differences are clauses that moved between files (the challenge-path section) or were retitled.
- Normalized diff of old Part B §5.3–§5.3.1 against new Part A §3–§3.1: identical except one added title in a cite ("defined in §3.1 Contestability paths") that SECTION-CITE-NAME-01 requires.
- Generated files regenerated: `doc_architecture/generated/plain_terms_edition.*`, `doc_architecture/generated/boundary_chunks.json`.
- Chart: rendered with mermaid-cli; VIS-CHART-READABILITY-01, THEME-02, ORIENT-04, CENTER-05, CROSSING-06, EXTERNAL-07, and SYMBOLS-08 checked by hand against the new chart.

## Open items

- `ai-manifest-validate` was already failing before this change (`ai_corpus/` is stale: run `make ai-corpus-sync`). Not run here, to keep this change reviewable.
- Stray untracked duplicates (for example `core_05_band_participation 2.md`) break `make regression` on the working folder with "Resource deadlock avoided". Delete them before the announcement.
- Translations were remapped mechanically so their links resolve. Their prose still describes the old structure until the translation restart (see MEMLOG, translations paused).
- The current git branch name no longer describes the work; if renamed, `restructure/ch08-process-order` fits GIT-BRANCH-NAME-01.
