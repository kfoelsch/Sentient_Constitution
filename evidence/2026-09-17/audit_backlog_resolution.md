# Audit backlog resolution

**Date:** 2026-09-17. **Edition:** SC-Corpus-2026.08.09, pre-release. **Status:** working-tree repair; not adoption or publication.

This note closes the seven repository audit targets that remained open in the [follow-up quality check](alignment_followup_quality_check.md). It does not close the separate design/lived-experience validation, source-coverage, translation-coverage, or deferred P1 reinstatement decisions.

## Repairs

1. Removed the ten obsolete FAQ fragment aliases from [implementation/FAQ.md](../../implementation/FAQ.md). The generated resolver now contains only current anchors for those questions.
2. Added the missing post-Trace spacer in [core_06_rights_part_b.md](../../core_06_rights_part_b.md), and changed the nine flagged bold list-intro periods to colons in [core_06_rights_part_a.md](../../core_06_rights_part_a.md).
3. Added explicit Chapter Five O/M/A/C entry headings while preserving the canonical `-constitutional` anchors in the five apex files. Updated the registry generator to disambiguate the principle-layer `Flourishing` label, then synchronized the directory, resolver, cross-reference, and section manifests.
4. Replaced the seventeen flagged standalone `person`/`people` terms in the scoped normative prose with `sentient`, `individual`, or role-based wording, as appropriate.

## Validation

The following gates pass against the repaired working tree:

- `make regression` — pass.
- `make ai-manifest-validate` — pass; generated manifests are fresh.
- `make fossil-anchor-audit-test` — 2 tests pass.
- `make id-resolver-test` — 9 tests pass.
- `make corpus-markdown-audit-test` — 14 tests pass.
- `make section-label-anchor-audit-test` — 10 tests pass.
- `make section-cite-name-audit-test` — 14 tests pass.
- Fossil-anchor, corpus-Markdown, navigation-spacer, Chapter Five entry-format, lexical-vocabulary, reference, citation-name, section-label, and `git diff --check` gates pass.

The full regression run includes the repository's static scenario gate; it is not evidence of live institutional performance. The remaining practical validation and coverage tasks stay open in [TODO.md](../../project/TODO.md).
