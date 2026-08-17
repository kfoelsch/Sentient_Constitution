# AI Navigation Guide for Sentient Constitution Corpus

**Purpose:** Enable token-efficient AI access to the constitutional corpus while preserving human readability.

**Authority:** These indexes are **derived locators**. Numbered `core_*` files and incorporated companions bind. On conflict, source text wins. Indexes cannot narrow core meaning.

---

## Quick Start for AI Assistants

### Before You Read Any File

1. **High-pressure fact pattern** → `implementation/STEWARD_ENTRY_DOORS.md` or `implementation/steward_owner_clock_index.json`
   - Owner, next-step class, forbidden move, clock
   - Verify the card against the boxed operative steward statement in the named core home

2. **ID, topic, or term** → `ai_corpus/indexes/id_resolver.json`
   - `CF-10`, `CJS-3.13`, `CS-4`, `CI-12`, `Def.P1`
   - CJS-0.1 topic rows (`CJS-R09` and the topic string)
   - Chapter Five terms (file + line range; no duty text in the index)
   - Current heading anchors only (pre-release: no fossil or legacy fragment aliases)

3. **Heading line range** → `ai_corpus/indexes/section_manifest.json`
   - Read only those lines from the source file

4. **Then open the named source.** Do not treat a locator, gloss, or steward card as a duty.

---

## Optimal Reading Patterns

### Pattern 1: Locate, then read

```
Step 1: Query ai_corpus/indexes/id_resolver.json
        → file, anchor, line (and mandatory read-with for topics)

Step 2: Read only those lines from the source file

Step 3: If the locator and the source disagree, the source wins
```

### Pattern 2: Definition lookup

```
Step 1: Query id_resolver.json definitions[] or definition_registry.json
        → Get line range for the term

Step 2: Read only those lines (complete O/M/A/C block)

Step 3: Do not copy definition text into JSON or invent a parallel stack
```

### Pattern 3: Cross-file topic

```
Step 1: Query id_resolver.json topics[] or doc_architecture/generated/topic_router.json
        → primary owner file(s) + mandatory read-with files

Step 2: Read the owner, then each listed read-with

Step 3: Apply Chapter One §8.4.4 combined satisfaction; do not skip read-with
```

### Pattern 4: Citation / rename audit

```
File-to-file:   ai_corpus/indexes/crossref_matrix.json
Section-to-section: ai_corpus/indexes/section_crossref.json
```

---

## Chunking Best Practices

### Safe Chunk Boundaries (Split Here)

- After `---` horizontal rules
- Before `### ` or `#### ` headers
- After `</details>` closing tags
- Between definition entries
- At empty lines between major sections

### Unsafe Chunk Boundaries (Never Split Here)

- Inside O/M/A/C component triplets
- Inside `<details>...</details>` blocks
- Inside cross-reference lists
- Inside tables
- Mid-sentence or mid-paragraph

---

## File Access Priority

### Tier 1: Locators (check first)

1. `ai_corpus/indexes/id_resolver.json` — IDs, topics, terms, current heading anchors, steward-door pointers
2. `ai_corpus/indexes/section_manifest.json` — heading line ranges
3. `implementation/STEWARD_ENTRY_DOORS.md` — high-pressure next step (process support)

### Tier 2: Architecture context

4. `README.md` — reading order and common lookups
5. `doc_architecture.md` — file ownership and boundaries
6. `doc_architecture/generated/topic_router_reader_index.md` — human topic map

### Tier 3: Binding source

7. Named `core_*` file or companion subfile from the locator
8. Mandatory read-with files from the topic row

---

## Current corpus shape (do not use retired filenames)

Chapter Five lives in **band and apex files** (`core_05_band_*.md`, `core_05_apex_*.md`), with Part A compass in `core_05__definitions_home.md`. Companions are **folders** (`corpus_systems/`, `corpus_institutions/`, `corpus_forum/`, `corpus_joint_structure/`) plus root wrappers. Rights Floor is **Chapter Six** (`core_06-06_rights_part_*.md`). Standing measurement is **Chapter Eight**; standing effects are **Chapter Nine**.

Inventory of current files: `ai_corpus/visualization/dependency_map.mmd` (generated file list, not a citation-weight graph). Citation edges: `crossref_matrix.json` and `section_crossref.json`.

Retired pilots under `ai_corpus/definitions/` are not a lookup path.

---

*This guide enables token-efficient navigation while maintaining the corpus's human-readable plain-language structure.*
