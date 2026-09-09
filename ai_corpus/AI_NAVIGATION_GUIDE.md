# AI Navigation Guide for Sentient Constitution Corpus

**Purpose:** Enable token-efficient AI access to the constitutional corpus while preserving human readability.

**Authority:** These indexes are **derived locators**. Numbered `core_*` files and incorporated companions bind. On conflict, source text wins. Indexes cannot narrow core meaning.

---

## Quick Start for AI Assistants

### Before You Read Any File

Use `python3 tools/corpus_lookup.py` (skill: `.cursor/skills/corpus-lookup/SKILL.md`). Do not open `id_resolver.json` for meaning — it embeds gloss. Locators point; source binds.

1. **High-pressure fact pattern** → `python3 tools/corpus_lookup.py door CASE_ID` or `door --high-pressure`
   - Open the returned `card_path`, then verify the boxed operative steward statement at `operative_box.href`
   - Do not treat card prose as a duty

2. **ID, topic, or term** → `python3 tools/corpus_lookup.py resolve QUERY`
   - `CF-10`, `CJS-3.13`, `CS-4`, `CI-12`, `Def.P1`
   - CJS-0.1 topic rows (`CJS-R09` and the topic string) via `topic-route`
   - Chapter Five terms (file + line range; hydrate the source block)
   - Current heading anchors only — `validity --file FILE --anchor '#fragment'`

3. **Authentic span** → `python3 tools/corpus_lookup.py hydrate QUERY`
   - Or `hydrate --file FILE --start N --end M` when the cap requires a smaller range

4. **Then cite the named source.** Do not treat a locator, gloss, or steward card as a duty.

---

## Optimal Reading Patterns

### Pattern 1: Locate, then read

```
Step 1: python3 tools/corpus_lookup.py resolve QUERY
        → file, anchor, line (and topic-route for mandatory read-with)

Step 2: python3 tools/corpus_lookup.py hydrate QUERY

Step 3: If the locator and the source disagree, the source wins
```

### Pattern 2: Definition lookup

```
Step 1: python3 tools/corpus_lookup.py resolve "Proportionality"
        → Get line range for the term

Step 2: python3 tools/corpus_lookup.py hydrate "Proportionality"
        (complete O/M/A/C block)

Step 3: Do not copy definition text into JSON or invent a parallel stack
```

### Pattern 3: Cross-file topic

```
Step 1: python3 tools/corpus_lookup.py topic-route CJS-R09
        → primary owner file(s) + mandatory read-with files

Step 2: Hydrate the owner, then each listed read-with

Step 3: Apply Chapter One §8.4.4 combined satisfaction; do not skip read-with
```

### Pattern 4: Citation / rename audit

```
python3 tools/corpus_lookup.py citator --file FILE [--anchor '#fragment']
python3 tools/corpus_lookup.py validity --file FILE --anchor '#fragment'
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

1. `python3 tools/corpus_lookup.py` — resolve / hydrate / topic-route / door / citator / validity
2. Generated indexes under `ai_corpus/indexes/` — machine input to that CLI, not a duty text
3. `implementation/STEWARD_ENTRY_DOORS.md` — high-pressure next step after `door` (process support)

### Tier 2: Architecture context

4. `README.md` — reading order and common lookups
5. `doc_architecture.md` — file ownership and boundaries
6. `doc_architecture/generated/topic_router_reader_index.md` — human topic map

### Tier 3: Binding source

7. Named `core_*` file or companion subfile from the locator
8. Mandatory read-with files from the topic row

---

## Current corpus shape (do not use retired filenames)

Chapter Five lives in **band and apex files** (`core_05_band_*.md`, `core_05_apex_*.md`), with Part A compass in `core_05__definitions_home.md`. Companions are **folders** (`corpus_systems/`, `corpus_institutions/`, `corpus_forum/`, `corpus_joint_structure/`) plus root wrappers. Rights Floor is **Chapter Six** (`core_06_rights_part_*.md`). Standing measurement is **Chapter Eight**; standing effects are **Chapter Nine**.

Inventory of current files: `ai_corpus/visualization/dependency_map.mmd` (generated file list, not a citation-weight graph). Citation edges: `crossref_matrix.json` and `section_crossref.json`.

Retired pilots under `ai_corpus/definitions/` are not a lookup path.

---

*This guide enables token-efficient navigation while maintaining the corpus's human-readable plain-language structure.*
