# AI Navigation Cheatsheet

Indexes **point**. Source text **binds**. Do not open `id_resolver.json` for meaning.

## Instant Lookup

| Need | Command |
|------|---------|
| ID / topic / term | `python3 tools/corpus_lookup.py resolve QUERY` |
| Authentic source span | `python3 tools/corpus_lookup.py hydrate QUERY` |
| Cross-file topic | `python3 tools/corpus_lookup.py topic-route CJS-R09` |
| High-pressure next step | `python3 tools/corpus_lookup.py door CASE_ID` |
| Question or fact pattern | `python3 tools/corpus_lookup.py route "QUERY"` |
| Owner + read-with spans | `python3 tools/corpus_lookup.py apply-pack "QUERY"` |
| Citation block | `python3 tools/corpus_lookup.py cite --file FILE --anchor '#fragment'` |
| Public next-step classes | `python3 tools/corpus_lookup.py classes` |
| Boundary-chunk locators | `python3 tools/corpus_lookup.py retrieve "QUERY"` |
| Section citations | `python3 tools/corpus_lookup.py citator --file FILE [--anchor '#fragment']` |
| Current vs fossil fragment | `python3 tools/corpus_lookup.py validity --file FILE --anchor '#fragment'` |
| Edition pin | `python3 tools/corpus_lookup.py edition` |

Generated JSON under `ai_corpus/indexes/` is input to that CLI, not a duty text. Architecture rules: `doc_architecture.md`.

## Reading Patterns

```
Query: python3 tools/corpus_lookup.py route "QUERY"
Read:  python3 tools/corpus_lookup.py apply-pack "QUERY"
If locator and source disagree: source wins
```

```
Query: python3 tools/corpus_lookup.py retrieve "QUERY"
Then:  python3 tools/corpus_lookup.py hydrate --file FILE --start N --end M
Token overlap only (not embeddings; postponed indefinitely — doc_architecture.md#retrieval-no-vector-embeddings). Scores heading locators and source spans. Never gloss JSON. Source binds.
```

```
Query: python3 tools/corpus_lookup.py resolve QUERY
Read:  python3 tools/corpus_lookup.py hydrate QUERY
Edit:  targeted diff
If locator and source disagree: source wins
```

```
Topic: python3 tools/corpus_lookup.py topic-route CJS-R09
Read:  hydrate primary owner, then every mandatory read-with
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

- [ ] Located the owner via `corpus_lookup.py resolve` (not a retired filename)
- [ ] Hydrated the complete semantic block
- [ ] Checked topic read-with and/or `citator`
- [ ] Confirmed the heading's current fragment id (`validity`; pre-release: no fossil aliases)

## Post-Edit Checklist

- [ ] Cross-references resolve
- [ ] `make ai-corpus-sync` if headings, IDs, or links moved
- [ ] No semantic units split
