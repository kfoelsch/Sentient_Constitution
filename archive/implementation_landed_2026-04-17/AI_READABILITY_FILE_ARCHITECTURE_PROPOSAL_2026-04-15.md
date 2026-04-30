# AI Readability File Architecture Proposal

Purpose: propose a smaller-file constitutional layout that preserves authority order, improves human scanning, and makes AI retrieval and editing more reliable.

This memo is not operative constitutional text. It is an architecture proposal for the corpus.

## Core judgment

Yes: ordered filename prefixes are likely one of the highest-value changes.

A naming pattern like `core_00-01_...`, `core_07-07_...`, or `core_02-05_...` gives three immediate benefits:
- readers can see constitutional order directly in the filesystem,
- AI tools can target the right file with less ambiguity,
- future splits can preserve sequence without renaming unrelated files.

The main requirement is to make the numbering scheme stable, explicit, and tied to owner boundaries rather than file size alone.

## Recommended design principles

1. Split by constitutional function, not by line count.
2. Preserve single-home ownership for meaning and doctrine.
3. Keep chapter order visible in filenames.
4. Keep top-level navigation separate from chapter substance.
5. Prefer filenames that remain stable even if chapter titles evolve.

## Recommended filename pattern

Use this default structure for core constitutional files:

`core_<start>-<end>_<short_owner_label>.md`

Examples:
- `core_00-01_principles.md`
- `core_02-02_definition_structure.md`
- `core_03-03_anti_evasion.md`
- `core_04-04_traceability_verification.md`
- `core_05-05_definitions_a_independent.md`
- `core_06-06_standing.md`
- `core_07-07_misconduct.md`
- `core_08-08_courts.md`
- `core_09-09_rights_part_a.md`
- `core_09-09_rights_part_b.md`
- `core_10-10_governance.md`
- `core_11-13_amendment.md`
- `core_14-14_incorporation.md`

Rules:
- use zero-padded chapter numbers,
- repeat the chapter number for single-chapter files so filenames line up visually with chapter ranges,
- use `-` inside the chapter-range segment,
- use `_` between the chapter-range segment and the text label,
- use chapter ranges only where the grouped chapters are a true unit,
- keep the text label short and functional,
- avoid embedding volatile drafting language in filenames.

## Why this pattern is better than the current three-file core

The current structure is doctrinally coherent, but it asks both humans and AI to carry a lot of internal map state:
- `core_constitution.md` contains several non-adjacent constitutional chapters,
- `core_definitions.md` contains a four-chapter block with a different logical role,
- `core_amendment.md` contains a three-chapter amendment block.

That is manageable once learned, but it is not self-revealing in the file tree.

The proposed numbered pattern makes the structure visible without opening any file.

## Recommended target structure

### Top-level navigation

Keep one top-level map file:

- `core_index.md`

Job:
- explain authority order,
- explain read order,
- link to all chapter files,
- explain which files are grouped and why,
- state that the full Sentient Constitution is the set of `core_*` files read together.

This file should be mostly navigational, not doctrinal.

### Core constitutional chapter files

Recommended first-pass target:

- `core_00-01_principles.md`
- `core_02-02_definition_structure.md`
- `core_03-03_anti_evasion.md`
- `core_04-04_traceability_verification.md`
- `core_05-05_definitions_a_independent.md`
- `core_06-06_standing.md`
- `core_07-07_misconduct.md`
- `core_08-08_courts.md`
- `core_09-09_rights_part_a.md`
- `core_09-09_rights_part_b.md`
- `core_09-09_rights_part_c.md`
- `core_09-09_rights_part_d.md`
- `core_10-10_governance.md`
- `core_11-13_amendment.md`
- `core_14-14_incorporation.md`

Why this is the strongest first pass:
- The preamble can be made explicit as Chapter `00`, letting the file capture the preamble plus Chapter One as one visible principles block.
- Chapters Two through Four form a tightly coupled pipeline, but traceability build-out is likely to make Chapter Five grow faster than the rest of the definitions layer.
- Splitting the definitions layer now reduces token overhead during the traceability build and prevents Chapter Five from becoming the next oversized owner file.
- `constitutional_definitions` is a clearer human-facing label than `canonical_definitions` while preserving the intended ownership meaning.
- Chapters Six through Eight are each distinct enough to stand alone.
- Chapter Nine is the biggest readability burden and already has clear internal Part structure.
- Chapter Ten stands well on its own.
- Chapters Eleven through Thirteen remain a valid grouped unit because they are all change-validity and amendment machinery.
- Chapter Fourteen is short, high-authority, and easy to retrieve when isolated.

## Optional second-pass structure

If Chapter Nine Part files are still too large, split them further by article family.

Possible pattern:
- `core_09-09_planetary_preconditions.md`
- `core_09-09_personhood_agency_governance.md`
- `core_09-09_trustworthy_systems_integrity.md`
- `core_09-09_justice_evolution_transition.md`

I do not recommend article-by-article files yet. That would likely oversplit the corpus and make sequential reading worse.

## Why the definitions layer should split early

Your instinct about names like `core_02-06` or `core_07-07` is strong because it exposes grouped spans and creates visual regularity.

That said, the grouping should correspond to a real doctrinal block. For the current corpus:
- `02-02`, `03-03`, `04-04`, and `05-05` are a better first-pass split than `02-05` as one file because traceability work is actively increasing the size and retrieval cost of the definitions layer.
- `05-05_constitutional_definitions.md` is especially likely to bloat as interdependent and clustered terms expand during traceability build-out.
- `11-13` still works because change validity, supremacy, and amendment procedure are one tightly coupled layer.
- `02-06` would still be too broad, because Chapter Six is not definitions anymore; it is compliance posture.

So I would use range names only where the range reflects one owner-layer job, and I would not preserve `02-05` as a grouped owner file if the near-term editing pattern is already pushing token use too high.

## Recommended naming rules

1. One chapter: `core_06-06_standing.md`
2. Definitions-first split when one owner block is expected to keep expanding: `core_02-02_definition_structure.md`, `core_03-03_anti_evasion.md`, `core_04-04_traceability_verification.md`, `core_05-05_definitions_a_independent.md`
3. Same chapter, split by major internal part: `core_09-09_rights_part_a.md`
4. Same chapter, split by numbered sub-block only if parts become unstable: `core_09-09_planetary_preconditions.md`
5. Preamble plus first chapter as one principles block: `core_00-01_principles.md`

Preferred default is the Part naming for Chapter Nine because the reader already understands that structure from the text.

## Trace-block implications

This redesign makes the trace idea much more viable.

Why:
- smaller files reduce visual overload from `<details>` blocks,
- trace blocks can be used only where they add value,
- chapter-local trace patterns can differ slightly without confusing the whole corpus,
- AI can ingest one chapter or one part at a time with less wasted context.

Best fit:
- `core_00-01_principles.md`
- the four `core_09-09_rights_part_*.md` files
- possibly `core_10-10_governance.md`

Lower need:
- `core_14-14_incorporation.md`, because it is short and structurally direct.

Special note:
- even after the definitions split, Chapter Five should be watched closely because new constitutional terms, interdependent definitions, and clustered definitions are likely to accumulate there first.

## Human readability benefits

- readers can infer constitutional order from filenames,
- long-scroll fatigue decreases,
- chapter-local tables of contents become useful,
- the rights chapter becomes much easier to navigate,
- links and citations become easier to check manually.

## AI readability benefits

- less irrelevant context per retrieval,
- cleaner file-level ownership boundaries,
- easier prompts like “review Chapter One only” or “trace Part C only,”
- lower risk of mixing rights text with governance or amendment doctrine,
- better chunking for audits, transformation passes, and reference checking.

## Risks

### 1. Cross-file citation drift

More files mean more links, more anchors, and more opportunities for stale references.

Mitigation:
- keep chapter numbers and heading wording stable where possible,
- maintain a strong reference-audit pass,
- treat same-change reference updates as mandatory.

### 2. Duplicate opening boilerplate

If each new file repeats too much source-of-truth language, the corpus will feel bloated again.

Mitigation:
- use a short shared opening contract,
- push most routing language into `core_index.md` and `doc_architecture.md`,
- keep chapter files focused on their doctrine.

### 3. Oversplitting

If files get too small, readers lose narrative continuity and AI loses adjacent context.

Mitigation:
- split only at natural chapter or Part boundaries,
- avoid article-by-article files unless there is a proven need.

## Migration strategy

### Phase 1: introduce the target map without moving text

Create:
- `core_index.md`
- a migration memo or map listing each future file and its chapters

Do not move doctrine yet.

### Phase 2: split the highest-value files first

Recommended order:
1. Definitions layer first:
   - `core_02-02_definition_structure.md`
   - `core_03-03_anti_evasion.md`
   - `core_04-04_traceability_verification.md`
   - `core_05-05_definitions_a_independent.md`
2. Preamble plus Chapter One into `core_00-01_principles.md`
3. Chapter Nine into `core_09-09_rights_part_a.md` through `core_09-09_rights_part_d.md`
4. Chapter Ten into `core_10-10_governance.md`
5. Chapter Fourteen into `core_14-14_incorporation.md`

This captures most readability benefit early.

### Phase 3: replace the old wrapper files

After references are stable:
- repurpose `core_constitution.md` into `core_index.md` or retire it cleanly,
- repurpose `core_definitions.md` into a brief compatibility index pointing to `core_02-02_definition_structure.md`, `core_03-03_anti_evasion.md`, `core_04-04_traceability_verification.md`, and `core_05-05_definitions_a_independent.md`,
- repurpose `core_amendment.md` to `core_11-13_amendment.md`.

If compatibility matters, keep temporary stub wrappers that point to the new names.

## Recommendation on compatibility wrappers

For one transition cycle, I recommend keeping the legacy filenames as short wrappers or redirects.

Example:
- `core_constitution.md` becomes a brief compatibility index pointing to `core_00-01_*`, `core_06-06_*`, `core_07-07_*`, `core_08-08_*`, `core_09-09_*`, `core_10-10_*`, and `core_14-14_*`.
- `core_definitions.md` becomes a brief compatibility index pointing to `core_02-02_definition_structure.md`, `core_03-03_anti_evasion.md`, `core_04-04_traceability_verification.md`, and `core_05-05_definitions_a_independent.md`.
- `core_amendment.md` points to `core_11-13_amendment.md`.

That lowers migration risk for tools, notes, and existing cross-references.

## Strong recommendation

If the redesign goes forward, use this file family as the likely target:

- `core_index.md`
- `core_00-01_principles.md`
- `core_02-02_definition_structure.md`
- `core_03-03_anti_evasion.md`
- `core_04-04_traceability_verification.md`
- `core_05-05_definitions_a_independent.md`
- `core_06-06_standing.md`
- `core_07-07_misconduct.md`
- `core_08-08_courts.md`
- `core_09-09_rights_part_a.md`
- `core_09-09_rights_part_b.md`
- `core_09-09_rights_part_c.md`
- `core_09-09_rights_part_d.md`
- `core_10-10_governance.md`
- `core_11-13_amendment.md`
- `core_14-14_incorporation.md`

This is the best balance I see right now between:
- visible constitutional order,
- manageable file size,
- doctrinal coherence,
- AI retrieval quality,
- migration realism.

## Bottom line

Yes: prefix-numbered filenames should be a core design feature of the redesign.

My main refinement is:
- use chapter-range prefixes only for true owner blocks,
- use duplicated chapter numbers for single-chapter files so the family aligns visually,
- treat the preamble as Chapter `00` and pair it with Chapter `01` in the principles file,
- use Part-based splits for the rights chapter,
- keep one top-level index file so the corpus still reads as one Constitution rather than a loose folder of fragments.
