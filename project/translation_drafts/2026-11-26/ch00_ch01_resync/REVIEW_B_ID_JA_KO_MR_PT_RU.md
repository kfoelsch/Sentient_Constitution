# Independent review: ID, JA, KO, MR, PT, RU

Date: 2026-11-26  
Review basis: pinned English sources and the locale glossaries in `translations/<locale>/README.md`.  
Scope: draft files only; no changes were made under `translations/`.

## Corrections made

- Added the current Preamble Tetrad Mermaid chart to all six Chapter 0 drafts after the Tetrad introduction. Node IDs, edges, styles, and chart layout follow the pinned source; display labels are localized.
- Added or replaced the two current Chapter 1 Mermaid charts in all six drafts. The four-seat chart and process chart preserve source node IDs, edges, subgraphs, directions, and styles; display labels are localized. Added the current `71-four-seat-separation-map` and `81-process-map` anchors where absent.
- Corrected Chapter 1 headings 5–11 in ID, MR, PT, and RU drafts, including top-level §5 and localized titles for §§6–11. Body prose was not changed by those heading-level corrections.
- Reconciled 773 cross-file links to the current source basename or to a localized file listed in that locale's README mapping. The README mapping and current chapter-number source table were used; unresolved links were left untouched rather than mapped by filename guess.
- Corrected the migrated §5 heading level in ID, MR, PT, and RU so §5 is top-level, matching the current English source.

## Pair status

| Locale | Ch0 | Ch1 | Status |
|---|---|---|---|
| ID | Tetrad chart added; existing prose retained | Sections 1–11 present; §5 body and §6 owner map are stale/incomplete against current source; other coverage remains open | Not ready to synchronize. AI coverage pass found source-mapping gaps. |
| JA | Tetrad chart added; existing prose retained | §§7, 9, and 10 are translated under current titles; §5 body and §6 owner map are stale/incomplete | Not ready to synchronize. AI coverage pass found source-mapping gaps. |
| KO | Tetrad chart added; existing prose retained | §§7, 9, and 10 are translated under current titles; §5 body and §6 owner map are stale/incomplete | Not ready to synchronize. AI coverage pass found source-mapping gaps. |
| MR | Tetrad chart added; existing prose retained | §§5–6 stale/incomplete; §7 coverage appears compressed; §9 contains only one owner summary; §8.2 added | Not ready to synchronize. Significant source coverage gaps remain. |
| PT | Tetrad chart added; existing prose retained | §§5–6 stale/incomplete; §7 coverage appears compressed; §9 contains only one owner summary; §8.2 added | Not ready to synchronize. Legacy §8 material remains ambiguous; significant source coverage gaps remain. |
| RU | Tetrad chart added; existing prose retained | §§5–6 stale/incomplete; §7 coverage appears compressed; §9 contains only one owner summary; §8.2 added | Not ready to synchronize. Significant source coverage gaps remain. |

## Unresolved concerns

- A small set of old targets has no unambiguous source-file mapping in `chapter_numbers.json` or the locale README mapping and remains unresolved. Current distinct targets include `core_09.000_system_alignment_certification_evaluation.md`, `core_10_a_misconduct_designation.md`, `core_11_forum.md`, and `core_11_standing_assessment.md`; MR/PT/RU also retain `core_07_functional_independence_segregation_of_duties.md`, while ID/JA/KO retain `core_15.000_forum.md`. Their anchors need a source-backed destination decision before synchronization.
- JA and KO were rechecked after translation updates. Their headings 5–10 follow the current English numbering and titles; §§7 and 9 match source bullet counts. Section 10 includes all six source chapter-owner entries, with one bullet-count variance whose grouping may reflect locale formatting. This was a structural and source-content coverage check, not fluent-language certification.
- PT retains legacy/dangling §8 material whose meaning and whether it is superseded could not be determined confidently; it was not removed.
- The diagram labels were localized using the available glossary and surrounding draft terminology. Fluency and nuanced terminology in these six languages were not independently certified; a fluent-language review remains necessary. In particular, the short labels used in several nodes may need the locale reviewer’s preferred established equivalents.
- The heading fixes for AR, BN, ES, FA, FR, and HI were separately requested for verification. Their §5 heading appears top-level in the current drafts and I found no duplicate stale §8 block in those six files at this check. This is a structural spot-check, not a full review of those locales.

No synchronization or commit was performed.

## Follow-up check — 2026-11-26

- Re-read JA and KO after the added translations. Current headings §§5–10 align with the source numbering/title sequence. §§7 and 9 match source bullet counts; §10 includes all six source owner entries. No untranslated/TODO placeholders remain in §§7, 9, or 10. This is a structure and coverage check, not a fluent-language certification.
- Rechecked §8.2 in MR/PT/RU: each has the current subsection anchor and all seven ordered stages from the English source. PT's ambiguous preexisting §8 content remains flagged above.
- Additional AI source-coverage pass across all six pairs found that §5 body text still contains superseded mappings and omits current safeguards; §6 in all six retains the old chapter-owner model instead of the current Chapters Two–Four register. In MR/PT/RU, §9 covers only the charter owner, omitting the other nine current owners; §7 appears substantially compressed. These are synchronization blockers. No translation was synthesized where a fluent-language choice would be required.
- Rebased paired chapter links to `core_00_preamble.md` / `core_01_constitutional_map.md` for final locale-folder context. Canonical English fallbacks use `../../<current English basename>`; no `../../../../` draft-relative links remain.
- Restored the second current Chapter 1 chart in JA/KO and checked that all six locale pairs have two complete fenced Mermaid blocks for Chapter 1 and one for Chapter 0. Diagram IDs, edges, subgraphs, directions, and styles match source; labels are localized.
- Ran `make preflight`: PASS (84/84).

## Additional AI source-coverage pass — 2026-11-26

Section numbering, list/owner coverage, and the current source mapping were compared against the pinned English files. This is AI review, not human fluent attestation. Chapter 0 section headings and principal list structures align in all six pairs; semantic fidelity and nuanced terminology remain unverified. Chapter 1 is not ready to synchronize: §5 prose and §6's owner register in all six still reflect superseded mappings; MR/PT/RU also omit most §9 owner summaries, and their §7 summaries are compressed relative to source. Exact stale references with uncertain destinations remain listed above. PT's legacy §8 material is unresolved.
