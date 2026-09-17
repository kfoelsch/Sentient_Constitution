# Source coverage record — 2026-09-17

**Status:** mechanical inventory and targeted audit pass complete; complete semantic source coverage is still open.

This record answers the open source-coverage item in [TODO.md](../../TODO.md). It separates source families so translation and implementation breadth is not mistaken for a completed human reading of the binding corpus.

## Inventory

| Source family | Inventory | Coverage status |
|---|---:|---|
| Numbered/core Markdown | 38 files at repository root | Structural and alignment checks run. The remaining numbered-chapter nested-list pass was reviewed and completed for the Preamble, Chapters One–Four, and Chapters Fourteen–Sixteen. This is not a semantic certification of every provision. |
| Companion wrappers | 4 files | Wrapper/cite checks passed. |
| Companion subfiles | 74 files: CJS 14, CS 16, CI 27, CF 17 | Anatomy and wrapper-cite checks passed. Full provision-by-provision human review remains open. |
| Translations | 19 locales, 531 translated core files | Counted separately. No claim of translation equivalence or complete translation review. |
| Implementation documentation | 59 Markdown files | Counted separately. No claim of complete operational or adopter-readiness review. |
| Evaluation documentation | 52 Markdown files | Counted separately. Existing AI evidence is present; human/live-fire evidence remains an open TODO. |

## Checks run

- `make alignment-audit` — completed; report index: [alignment_audit_index_2026-09-17.md](alignment_audit_index_2026-09-17.md). This is structural trace/completeness evidence, not semantic adequacy.
- `make corpus-markdown-audit` — PASS.
- `make companion-anatomy-audit` — PASS for 74 companion files.
- `make companion-cite-audit` — PASS; no wrapper-only family cites.
- `make owner-discipline-audit` — PASS.
- `make ch4-ch7-pointer-audit` — ADVISORY finding remains in `core_07_b_system_alignment_certification_record_process.md:38`.
- `make readability-audit` — FAIL as a whole-repository gate: 811 files scanned, overall estimated grade 12.56, 228 files over the grade-14 target. The output is dominated by translation and companion readability work and does not establish source semantic coverage.
- `make ai-manifest-validate` — initially detected stale derived manifests after current source edits; `make ai-corpus-sync` was run, and the follow-up freshness check passed.

## Final validation

After the prose and tooling edits, `make regression` passed. The readability result and the one advisory Chapter Four ↔ Chapter Seven pointer finding remain as recorded above; neither is being represented as complete source semantic coverage.

## Coverage boundary

The alignment and structural checks establish that the current source inventory is reachable and mechanically coherent in the audited dimensions. They do not establish that every core, definition, companion, translation, or implementation provision was read and checked by a human. The source-coverage TODO therefore remains open pending a tracked provision-by-provision review with separate translation and implementation dispositions.
