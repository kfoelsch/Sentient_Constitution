# Translation resynchronization plan

**Status:** Plan only. Translation work remains paused under the standing decision in [MEMLOG](../MEMLOG.md) and [CONTRIBUTING.md](../../CONTRIBUTING.md#lane-f--translations). This plan does not authorize drafting or synchronization. The custodian has identified Chapters 0 and 1 as ready for a scoped pilot; drafting begins only after the custodian identifies the source snapshot and authorizes that pilot.

## Goal

Bring existing translations into alignment with the reorganized English corpus without losing translated material, carrying forward obsolete structure, or changing meaning. Use Chapters 0 and 1 as the pilot to validate the mapping, drafting, and review process before planning the remaining chapters.

## Scope and source identity

The pilot covers the current English [Chapter 0, the Preamble](../../core_00.000_preamble.md) and [Chapter 1, the Constitutional Map](../../core_01.000_constitutional_map.md), across the 19 supported locales: `ar`, `bn`, `es`, `fa`, `fr`, `hi`, `id`, `ja`, `ko`, `mr`, `pt`, `ru`, `ta`, `te`, `th`, `tr`, `ur`, `vi`, and `zh`. This is 38 locale/source pairs. Chapter 1 means the current Constitutional Map; the old Chapter 1 values and principles material now belongs to Chapter 2 and is outside this pilot.

At pilot start, the custodian pins one immutable English source commit or edition. Record its commit, edition, and SHA-256 hashes for both source files in the pilot inventory. If either source changes during drafting or review, pause that pair and rebase it against a newly pinned snapshot before proceeding. Use `tools/architecture/chapter_numbers.json` and the canonical source files to resolve numbering and destinations; do not infer destinations from filename digits, stale translation filenames, indexes, or glosses.

## Current-state inventory

1. For each locale, list the published translation files corresponding to old Chapter 0/1 material, their present file names, headings, section coverage, edition pins, and review status.
2. Inventory relevant material in `project/translation_drafts/`, including the pre-reorganization Chapter 0–4 and Chapter 1 refresh drafts. Record provenance and source revision where available; treat these as raw material, not as current translations or authority.
3. Map old source files, sections, and anchors to current English files and sections using the chapter registry and actual source headings. Record splits, merges, newly introduced material, removed material, and unresolved matches explicitly.
4. Flag the current Chapter 1 Constitutional Map as new translation work if no equivalent translated source exists. Do not relabel old Chapter 1 values/principles translations as Chapter 1; map them to current Chapter 2 for the later rollout.

The inventory is a planning and traceability aid. It does not claim any translation is reviewed, complete, or fit to publish.

## Pilot workflow

1. **Prepare the source map.** Build one reviewed source-section crosswalk per pilot chapter, with old source location, current English section and anchor, locale material available, and disposition (`retain`, `revise`, `translate`, `retire`, or `decision needed`). Resolve any substantive ambiguity with the custodian before drafting.
2. **Draft all locale pairs.** After explicit authorization, prepare each of the 38 pairs against the pinned English files. Draft in `project/translation_drafts/` only. Existing translated wording may be reused when it still matches, but compare every retained passage with the current English; do not use changed-line extracts as substitutes for a full-file fidelity pass.
3. **Preserve structure and links.** Keep the English HTML `id`s and add or retain English heading-slug `id`s so links work. Preserve the non-binding reader-guidance widget and edition pin. Translate chart labels and reader-facing prose while preserving Mermaid syntax and destinations. Use the locale glossary and name the language variety in the locale note.
4. **Track provenance.** Each draft records locale, language variety, English source commit/edition, both source-file hashes, source-to-translation crosswalk, drafting method, model name if AI-assisted, and `unreviewed` status. Keep source-specific terminology choices visible for fluent review.
5. **Run fidelity and structure checks.** Compare every section against the English source for coverage, omissions, additions, negation, actors, duties, conditions, exceptions, scope, thresholds, clocks, rights, and cross-references. Check Markdown, Mermaid, IDs, anchors, local links, file size, and the exact source pin. Automated checks support this review; they do not certify translation quality.
6. **Independent fluent review.** A fluent reader who did not write the draft checks it against the pinned English, resolves terminology against the locale glossary, and records findings and status. Any meaning uncertainty returns to the custodian; do not settle it by smoothing the translation.
7. **Pilot assessment.** Review the 38-pair results for mapping accuracy, repeated failure types, review effort, glossary gaps, and tooling needs. Record the outcome and any proposed workflow changes. Do not start other chapters until the custodian accepts the pilot process and separately authorizes the next scope.

## Synchronization gate

Only after the custodian separately authorizes synchronization may reviewed drafts replace or add files under `translations/<locale>/`. Before that move:

- all passages in the pair have independent fluent-reader review against the pinned English source;
- source-specific glossary decisions and language variety are recorded;
- `translations/<locale>/README.md` file lists and glossaries are updated, and `translations/README.md` inventory is reconciled;
- review status and source edition/hash metadata are updated consistently;
- touched-file links resolve (`make local-markdown-fragment-audit`) and the lane's regression gate reports no new failures;
- `make preflight` is run after each edit, generated files are refreshed where needed, and `make audit-report` is run before completion.

Until this gate is met, the work stays in `project/translation_drafts/` and is labeled unreviewed. Translation files remain untouched by this plan.

## Later rollout

After the pilot is accepted, make a second inventory for the full reorganized corpus. Group work by current source chapter and use the same immutable-source, crosswalk, all-19-locale, glossary, provenance, independent-review, and synchronization gates. Prioritize chapters whose English text the custodian has identified as settled. Keep old numbering only as traceability metadata; use current chapter numbers and filenames for destinations. Do not translate stale copies of material that has moved; map each passage to its current owner and retire duplicates only after its disposition is verified.

## Completion criteria for the pilot

- The pinned snapshot and source hashes are recorded.
- All 38 locale/source pairs have a source crosswalk and a draft or an explicit documented gap; all remain clearly unreviewed until independent review is complete.
- No draft is copied into `translations/` before its independent review and synchronization authorization.
- Chapter 0 and Chapter 1 destinations, IDs, links, glossary terms, and edition metadata agree with the pinned English sources.
- Pilot findings and any unresolved choices are presented to the custodian before wider resynchronization begins.
