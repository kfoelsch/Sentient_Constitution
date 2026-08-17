# AI Navigation Cheatsheet

Indexes **point**. Source text **binds**.

## Instant Lookup

| Need | File | Key |
|------|------|-----|
| ID / topic / term | `ai_corpus/indexes/id_resolver.json` | `ids["CF-10"]`, `topics[]`, `definitions[]` |
| Heading line range | `ai_corpus/indexes/section_manifest.json` | `{"file": "...", "line_start": n, "line_end": m}` |
| Definition location only | `ai_corpus/indexes/definition_registry.json` | `{"term": "...", "source_file": "...", "line_start": n}` |
| File-to-file citations | `ai_corpus/indexes/crossref_matrix.json` | `{"source": "...", "targets": [...]}` |
| Section-to-section citations | `ai_corpus/indexes/section_crossref.json` | `source_file` + `source_header` → `target_file#anchor` |
| Cross-file topic (JSON) | `doc_architecture/generated/topic_router.json` | `CJS-R##` → owner + read-with files |
| High-pressure next step | `implementation/STEWARD_ENTRY_DOORS.md` | five-field cards; machine index: `steward_owner_clock_index.json` |
| Architecture rules | `doc_architecture.md` | Corpus roles and edit order |

## Reading Patterns

```
Query: id_resolver.json → file + anchor + line
Read:  source file with offset/limit
Edit:  targeted diff
If locator and source disagree: source wins
```

```
Topic: id_resolver.json topics[] or topic_router.json
Read:  primary owner, then every mandatory read-with
Apply: Chapter One §8.4.4 combined satisfaction
```

## Safe Edit Boundaries

| Split Here | Never Split Here |
|------------|------------------|
| After `---` | Inside O/M/A/C components |
| Before `### ` | Inside `<details>` |
| After `</details>` | Mid-table |
| Between definitions | Mid-sentence |

## Pre-Edit Checklist

- [ ] Located the owner from `id_resolver.json` (not a retired filename)
- [ ] Read the complete semantic block
- [ ] Checked topic read-with and/or section_crossref
- [ ] Confirmed the heading's current fragment id (pre-release: no fossil aliases)

## Post-Edit Checklist

- [ ] Cross-references resolve
- [ ] `make ai-corpus-sync` if headings, IDs, or links moved
- [ ] No semantic units split
