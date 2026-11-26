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

## Gap-closure pass — 2026-11-26

Replaced superseded content rather than layering a second summary over it:

- Rewrote Chapter 1 §5 in ID, JA, KO, MR, PT, and RU against the pinned English. It now covers the four separated functions, current Chapter Four / Subcore 8-B triggers, the paired certification and challenge safeguards, separate correction and remedy, ordinary challenge-path-first sequencing, and the current §8.2 stages.
- Rewrote Chapter 1 §6 in all six locales as the current constitutional owner register for Chapters Two through Four. It now covers the values and stewardship remit; the Chapter Three definition stack and Subcores 3-A through 3-C; and the Articles I–XXIX Rights Floor and its boundaries.
- Rebuilt Chapter 1 §7 in MR, PT, and RU to cover the current owners and outputs of Chapters Five (Charters), Six (Functional Independence), and Seven (Independent Bodies), replacing compressed/obsolete material.
- Rebuilt Chapter 1 §9 in MR, PT, and RU with all ten current process owners: Subcores 8-B, 9-B, 10-B, 10-D, 10-F and Chapters Fourteen, Sixteen, Seventeen, Nineteen, and Twenty. Each summary states the owner's responsibility and output at a concise level.
- PT's ambiguous legacy §8 text remains untouched; its disposition is still not source-clear. Historical cross-file links and fragment aliases listed above remain for separate source-backed link reconciliation.

These are AI-assisted translations and source-coverage repairs, not independent fluent review. The other sections were not re-certified by this pass. No synchronization into `translations/` was made.


## Follow-up coverage repair — 2026-11-26 (MR/PT/RU)

- Replaced the stale §8 opening summary and framing in MR, PT, and RU with the current Chapter Five charter and Chapter Six separation-of-functions basis and the current process chain.
- Added the source's post-chart bounds paragraph in all three locales: the Constitutional Tetrad, Two Constitutional Aims, and Rights Floors constrain the full process.
- Added the full current §11 subcore explanation in all three locales, covering its place between chapters and adopted corpora, chapter ownership and equal binding force, Chapter Twenty-Three amendment route, guarantee text versus full procedural detail, and citation-layer cues.
- PT's ambiguous legacy §8 material remains untouched and unresolved; no supersession or disposition was inferred.
- This follow-up addresses only the listed MR/PT/RU coverage points. It is AI-assisted translation and source-coverage repair, not fluency certification. The previously noted historical cross-file link mappings remain separate review items.


## Mermaid graph check — 2026-11-26 (MR/PT/RU)

Compared Chapter 1 §7.1 and §8.1 graphs with the pinned English graph structure and current chapter numbering. The four-seat §7.1 graph was absent in MR, PT, and RU, so it was restored with the source's four nodes, four directed edges, and styles; its same-act safeguards and labels are localized. Updated §8.1 displayed chapter labels to match the source (Chapters 5, 6, 8–10, 12–14, 16–17, and 19–20). Graph identifiers, edges, subgraphs, and styles were preserved for §8.1.

This is a structural and source-label check, not fluent-language certification.

## Follow-up process-pipeline repair — 2026-11-26 (ID/JA/KO)

- Replaced the stale §8 introduction in Indonesian, Japanese, and Korean with the current basis in Chapters Five and Six and the current process descriptions for certification, separate contribution/violation records and measurement, standing effects, misconduct review, and forum supervision.
- Moved the obsolete second Mermaid block out of §7.1 and replaced it with the current English §8.1 Process Map, preserving node IDs, all directed edges, and styles while localizing visible labels. The four-seat §7.1 map remains in place.
- Added explicit §8.1 and §8.2 anchors/headings and the current post-map constitutional-bounds paragraph covering the Constitutional Tetrad, Two Constitutional Aims, and Rights Floors.
- Replaced the obsolete ownership narrative with the current seven-stage §8.2 chain. It includes seat separation; system and institutional certification; separate verified-input records and measurement; separate-track effects; ACMD review; forum sequencing, Article XXVII-C timing, A/B/C/L/P materiality tiers, and Integrity-family default routing; and named-party execution within its window with the special-enforcement floors and root-cause evaluation.
- Compared the three §8.1 graphs with the pinned English source: node IDs, edge structure, and styles match (13 nodes, 20 edges, 13 style declarations in each graph).
- PT's legacy §8 material was not edited. AI-assisted structural/source coverage repair only; independent fluent review and historical cross-file link resolution remain outstanding.

## Follow-up subcore-layer repair — 2026-11-26 (ID/JA/KO)

- Added the current §11 explanation of the subcore layer in Indonesian, Japanese, and Korean: its position between chapters and adopted corpora, same binding force as its owning chapter, one-chapter ownership, amendment only under Chapter Twenty-Three, the chapter's plain-language guarantee versus the subcore's complete detail, equal force of Chapter/Subcore citation layers, and citation of Chapter Three definitions by defined term.
- Corrected the §11 incorporation cross-reference label to Chapter Twenty-Five in all three locales.
- AI-assisted source coverage repair only; independent fluent review and remaining historical link/anchor issues remain outstanding.


## Mermaid fence repair — 2026-11-26 (MR/PT/RU)

Moved the §8.1 Mermaid closing fence onto its own line in MR, PT, and RU. Confirmed both Chapter 1 Mermaid blocks in each of the six reviewed drafts now have one opening and one standalone closing fence.


## Destination-aware forum link reconciliation — 2026-11-26 (ID/JA/KO)

Mapped the obsolete `core_15.000_forum.md` destinations in the Chapter 0/1 drafts to current source chapters using the actual section topics and current anchors: forum purpose to Chapter Sixteen §1; dispute sequencing to Chapter Sixteen's explicit `dispute-sequencing` anchor; Technical Forum Domains to Chapter Seventeen §3.2; and shared standards/anti-displacement to Chapter Seventeen's explicit §6.2 anchor. The old file split across current Chapters Sixteen and Seventeen; no filename-only guess was used.


## PT §8.1 stale-splice cleanup — 2026-11-26

Removed the obsolete splice immediately after the §8.1 heading: it duplicated §6.2.3 and Rights Floor/Charter material with superseded Chapter Eleven/Nine/Seven–Fifteen references. Preserved the four-seat map disclaimer and relocated it under §7.1, where the pinned English source places it; corrected its reference from Chapter Eight to Chapter Six. The existing PT §8.2 legacy material remains separately flagged where its disposition is unclear.


## Stale §8.1 splice cleanup — 2026-11-26 (MR/RU)

Removed the same superseded §8.1 splice in Marathi and Russian that was removed in Portuguese: old verification/rights/Charter summaries with stale Chapter Nine/Eleven and Seven–Fifteen references. Preserved the four-seat map disclaimer, moved it under §7.1, and corrected its rule reference to Chapter Six, matching the pinned English layout. The current process map now follows the §8.1 heading directly.


## Exact stale anchor and destination repair — 2026-11-26 (six locales)

Updated only source-backed mappings in the Chapter 0/1 drafts: the moved incentive subsections now target current Chapter Two Part F (`core_02.050...#1911...` / `#1912...`); the anti-reward heading uses current `#327`; misconduct review uses current Chapter Fourteen; and obsolete governance chapter slugs now use current Chapters Twenty-One through Twenty-Four. The obsolete forum source in ID/JA/KO was already mapped to current Chapter Sixteen/Seventeen anchors above.


## Final link and splice disposition — 2026-11-26

The prior PT §8 ambiguity refers to the obsolete splice described above; its disposition is now source-backed and resolved. The stale verification/rights/charter block was removed from §8.1 in PT, MR, and RU, while the four-seat disclaimer was preserved under §7.1 with the current Chapter Six reference. Destination-aware checks now report no unresolved target files or anchors across all twelve drafts. Some stale historical sections without a unique current heading are linked to the verified current file at document level. The drafts remain AI-assisted and unreviewed for fluency.
