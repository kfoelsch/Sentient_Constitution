# Independent draft review: ta, te, th, tr, ur, vi, zh

**Review scope:** Chapters 0 and 1 drafts against the pinned English source and each locale's `translations/<locale>/README.md` glossary. This is an AI-assisted structural and source comparison, not a fluent-speaker certification. Drafts remain drafts; no files under `translations/` were changed.

## Pair status

| Locale | Ch 0 | Ch 1 | Status |
| --- | --- | --- | --- |
| ta | Reviewed structurally; current Tetrad chart present | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| te | Reviewed structurally; current Tetrad chart present | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| th | Reviewed structurally; current Tetrad chart added | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| tr | Reviewed structurally; current Tetrad chart added | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| ur | Reviewed structurally; current Tetrad chart added | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| vi | Reviewed structurally; current Tetrad chart added | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |
| zh | Reviewed structurally; current Tetrad chart added | Reviewed structurally; §§7.1 and 8.1 charts replaced from current source | Needs fluent review; stale/ambiguous cross-file links remain |

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

Compared each locale's section content and owner entries with the pinned current English. The same substantive coverage blockers appear in all seven drafts:

- **§5 omits one of the five current process paths:** the explicit Functional Independence and Separation of Duties path, including the requirement to separate initiating, verify-or-authorize, record, and challenge-review seats before a materially binding act moves. Draft §5 has four path entries (system certification, Standing Records, correction/remedy, forum review). The topic appears elsewhere in §7, but that does not supply the missing §5 path entry.
- **§8.2 retains the previous sequence and chapter references.** The current source chain names Chapter Six, Chapter Five, Subcores 8-B/9-B/10-B/10-D/10-F, Chapters Fourteen/Sixteen/Seventeen/Nineteen/Twenty, and the related current outputs. Draft §8.2 follows the older Chapters Seven through Fifteen sequence and older ownership descriptions. The new §8.1 diagram itself was separately checked against the pinned source graph.
- **§9 is a major omission.** The source contains ten owner/output entries (system certification, institutional certification, three standing stages, anti-constitutional designation, two forum chapters, enforcement, and special enforcement), as well as an introduction. Each draft's §9 contains only a short Chapter Seven charter-output entry. This leaves nearly all of the current owner register absent.
- **§10 has five old owner headings and lacks the current Assemblies entry.** The source lists Chapter Eighteen Assemblies and Chapters Twenty-One through Twenty-Five for governance, non-regression, amendment, supremacy, and incorporation. Draft §10 instead lists old chapter numbers (20, 17, 18, 19, 20), uses previous chapter ranges in its opening paragraphs, and omits Assemblies.
- **§11 omits the final subcore paragraph.** The source explains subcore scope, binding force, amendment path, and how Chapter/Subcore citations identify layers. The drafts include the four corpus bullets and a summary, but not this explanation. Their incorporation reference also retains the old Chapter Twenty number; the current source is Chapter Twenty-Five.

These are source-coverage and remapping issues, not small terminology fixes. I made no prose additions because restoring the omitted owner register and remapped chain requires substantial translation and meaning review in each language. No high-confidence text correction was made in §§5–11 during this pass. The unresolved link/anchor counts and mapping caveats above still apply.
