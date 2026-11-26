# Independent draft review: ta, te, th, tr, ur, vi, zh

**Review scope:** Chapters 0 and 1 drafts against the pinned English source and each locale's `translations/<locale>/README.md` glossary. This is an AI-assisted structural and source comparison, not a fluent-speaker certification. Drafts remain drafts; no files under `translations/` were changed.

## Pair status

| Locale | Ch 0 | Ch 1 | Status |
| --- | --- | --- | --- |
| ta | Reviewed structurally; current Tetrad chart present | §§8.2–11 replaced with current sequence, owner register, governance register, adopted corpus and subcore explanation | Needs fluent review; unresolved historical cross-file links remain |
| te | Reviewed structurally; current Tetrad chart present | §§8.2–11 replaced with current sequence, owner register, governance register, adopted corpus and subcore explanation | Needs fluent review; unresolved historical cross-file links remain |
| th | Reviewed structurally; current Tetrad chart added | §§8.2–11 replaced with current sequence, owner register, governance register, adopted corpus and subcore explanation | Needs fluent review; unresolved historical cross-file links remain |
| tr | Reviewed structurally; current Tetrad chart added | §§5–11 reconciled against current source owner register and process pipeline; charts retained | Needs independent fluent review; unresolved cross-file links remain |
| ur | Reviewed structurally; current Tetrad chart added | §§8.2–11 replaced with current sequence, owner register, governance register, adopted corpus and subcore explanation | Needs fluent review; unresolved historical cross-file links remain |
| vi | Reviewed structurally; current Tetrad chart added | §§5–11 reconciled against current source owner register and process pipeline; charts retained | Needs independent fluent review; unresolved cross-file links remain |
| zh | Reviewed structurally; current Tetrad chart added | §§5–11 reconciled against current process paths, owner register, pipeline and subcore explanation; charts retained | Needs independent fluent review; unresolved cross-file links remain |

## Changes and checks

- Corrected Chapter 1 §5 heading depth to match the English `###` in all seven drafts.
- Translated Chapter 1 §7, §7.1, and §8.1 headings in all seven drafts.
- Replaced Chapter 1 §7.1 and §8.1 Mermaid blocks with the graphs from the pinned English source, translating visible labels while retaining graph structure, IDs, edges, and styles.
- Added the pinned English Preamble Tetrad graph to `th`, `tr`, `ur`, `vi`, and `zh`. The `ta` and `te` graphs were already added by the coordinating work and were not edited in that pass.
- Compared the graph structures after removing labels: all three graph types match the pinned source for all seven locales.
- The draft filenames/metadata, section IDs, and chart structures were checked. No high-confidence prose correction to meaning-sensitive duties or rights was made: AI review cannot reliably certify fluency or nuanced meaning in these seven languages.

## Destination-aware link pass (2026-11-26)

Links in all fourteen drafts were resolved relative to the eventual `translations/<locale>/` location. I applied exact current destinations and locale targets where the README source mapping and file were verified, and used `chapter_numbers.json` for old-to-current aliases where the old numbering plus matching filename suffix identified the source. Chapter-pair links now target local `core_00_preamble.md` and `core_01_constitutional_map.md`. No hrefs use four or more parent-directory segments.

There are **29 unique unresolved target/anchor references per locale**. Where the current English destination is known, links now point to its canonical `../../<current-source-path>`; unresolved legacy fragments remain attached and need review. Other unresolved links still use older localized basenames because the current locale README does not map them to a current English source. These include `core_01_a_values_principles.md`, `core_07_charters.md`, `core_07_functional_independence_segregation_of_duties.md`, `core_10_institutional_alignment_certification.md`, and `core_11_forum.md`. The Chapter 7/8/9 references now have canonical current paths (`core_05.000_charters.md`, `core_06.000_functional_independence_separation_of_duties.md`, and `core_08.000_system_alignment_certification_evaluation.md`), but their legacy anchors do not match the current source and remain unresolved.

The 29-target count includes unresolved legacy local targets and fragments on known canonical targets; it does not certify that their referenced content is current. Chart labels and prose still need fluent review. No synchronization into `translations/` is authorized by this review note.

## Chapter 1 §§5–11 source-coverage pass (2026-11-26)

Compared each locale's section content and owner entries with the pinned current English. The original substantive coverage blockers applied to all seven drafts; the Chinese, Turkish, and Vietnamese drafts were reconciled on 2026-11-26; the other four still have these blockers:

- **§8.2 in ta, te, th, and ur retains the previous sequence and chapter references.** The current source chain names Chapter Six, Chapter Five, Subcores 8-B/9-B/10-B/10-D/10-F, Chapters Fourteen/Sixteen/Seventeen/Nineteen/Twenty, and the related current outputs. Draft §8.2 follows the older Chapters Seven through Fifteen sequence and older ownership descriptions. The new §8.1 diagram itself was separately checked against the pinned source graph.
- **§9 in ta, te, th, and ur is a major omission.** The source contains ten owner/output entries (system certification, institutional certification, three standing stages, anti-constitutional designation, two forum chapters, enforcement, and special enforcement), as well as an introduction. Each draft's §9 contains only a short Chapter Seven charter-output entry. This leaves nearly all of the current owner register absent.
- **§10 in ta, te, th, and ur has five old owner headings and lacks the current Assemblies entry.** The source lists Chapter Eighteen Assemblies and Chapters Twenty-One through Twenty-Five for governance, non-regression, amendment, supremacy, and incorporation. Draft §10 instead lists old chapter numbers (20, 17, 18, 19, 20), uses previous chapter ranges in its opening paragraphs, and omits Assemblies.
- **§11 in ta, te, th, and ur omits the final subcore paragraph.** The source explains subcore scope, binding force, amendment path, and how Chapter/Subcore citations identify layers. The drafts include the four corpus bullets and a summary, but not this explanation. Their incorporation reference also retains the old Chapter Twenty number; the current source is Chapter Twenty-Five.

These are source-coverage and remapping issues, not small terminology fixes. On 2026-11-26, I added the omitted Functional Independence and Separation of Duties path entry to §5 in all seven drafts, using localized wording and the current Chapter Six source link. I replaced the stale §8.2–11 content in the Chinese, Turkish, and Vietnamese drafts with source-aligned translations covering the current process chain, all ten process owners and outputs, all six governance/change/inclusion owners, the four adopted corpora, and the subcore binding/citation explanation. On 2026-11-26, Turkish and Vietnamese §8 were further reconciled with the source pipeline-bounds paragraph (Tetrad, Two Aims, Rights Floors) and the full seven-step chain, including the five materiality tiers and Integrity-family default routing, then named-party execution within its window and the shared special-enforcement floors/root-cause evaluation. These additions are AI-assisted and unreviewed. The stale §8.2 sequence, incomplete §9 register, outdated §10 register, and missing §11 subcore explanation previously identified in ta, te, th, and ur were reconciled on 2026-11-26. A later independent check identified the post-§8.1 constitutional-bounds paragraph as absent from all four; it has now been added. The unresolved link/anchor counts and mapping caveats above still apply.


### Independent verification and Chinese §8 repairs — 2026-11-26

Independent source-coverage verification found three remaining Chinese §8 gaps: the source's constitutional-bounds paragraph after the process diagram was absent; §8.2 omitted the A/B/C/L/P materiality tiers and Integrity-family default routing; and the sequence omitted the outcome-execution stage and its special-enforcement floors. The Chinese draft now includes all three. This closes the identified structural/source-coverage omissions for zh; it remains AI-assisted and unreviewed for fluency or semantic certification.

## Follow-up coverage repair — 2026-11-26

The previously documented Chapter 1 §§8.2–11 blockers are now repaired in `ta`, `te`, `th`, and `ur` against the pinned English:

- §8.2 replaces the obsolete chain with all seven current stages, including separate standing tracks, designation review, forum routing and timeliness, and enforcement/special enforcement.
- §9 replaces the single charter entry with all ten current process owners and concise statements of responsibility and output.
- §10 replaces old chapter numbers and headings with Assemblies (Chapter Eighteen) and Chapters Twenty-One through Twenty-Five for governance, non-regression, amendment, supremacy, and incorporation.
- §11 preserves all four adopted corpus descriptions and adds the current subcore binding-force, amendment, and citation-layer explanation.

The same coverage gaps remain in `tr` and `vi`. `zh` had already been reconciled. All four repaired pairs are still AI-assisted and need independent fluent review; the unresolved historical link/anchor mappings described above also remain. No files under `translations/` were changed.


### Follow-up: post-map bounds paragraph — 2026-11-26

Added the source paragraph after the §8.1 diagram to `ta`, `te`, `th`, and `ur`: it states that the Constitutional Tetrad requires participation, oversight, accountability, and timeliness at every stage; the Two Constitutional Aims require Flourishing and Continuity together; Rights Floors prohibit narrowing, bypassing, or hollowing out non-negotiable protections; and these bounds yield records and decisions that sentients can check, challenge, repair, and rely on in practice. Glossary forms were used for each locale. These remain AI-assisted, unreviewed drafts.

## zh follow-up reconciliation — 2026-11-26

Reconciled the remaining Chinese Chapter 1 text against the pinned English source:

- Replaced §§5–6 with the current process paths and the Chapter Two–Four owner register, including the Three-A/Three-B/Three-C definition subcores and Articles I–XXIX Rights Floor.
- Replaced §8’s obsolete Chapter Nine–Fifteen introduction and process narrative with the current Chapter Five/Six basis and the Chapter Eight/Nine certification, Chapter Ten standing, Chapter Fourteen designation, and Chapters Sixteen/Seventeen forum structure. The already source-aligned §8.1 graph was preserved.
- Confirmed §8.2 stage 7 includes the special-enforcement shared floors: protected minimum for seizure, surrender-pressure ladder, non-lethal-first force ladder, and root-cause evaluation.
- Corrected the §9 10-D and 10-F links to the actual `subcore_10.040_standing_measurement.md` and `subcore_10.060_standing_integration.md` source files.

The existing AI-assisted review status remains unreviewed; fluent review and the historical unresolved link/anchor set remain outstanding. No files under `translations/` were changed.


## Final coverage reconciliation — 2026-11-26

The previously identified §5, §6, §8.1–§8.2, and §9–§11 source-coverage gaps in all seven locales were repaired and recorded above. The later independent check also caught two residual structure issues: the Spanish §8.1 graph lacked the enforcement node and styles, and the Bengali §8.1 heading contained an Arabic word. The Spanish graph now matches the pinned source structure (13 nodes, 20 edges, 13 styles, two subgraphs), and the Bengali heading is localized. Current-source coverage checks found no other outstanding coverage omissions in these seven drafts. They remain AI-assisted and unreviewed for fluency; link mapping findings above are still open.
