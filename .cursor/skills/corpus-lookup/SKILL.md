---
name: corpus-lookup
description: Resolves Sentient Constitution IDs, Chapter Five terms, CJS-0.1 topics, and steward doors through tools/corpus_lookup.py, then hydrates authentic source spans. Use when looking up CF-10, Def.P1, CJS-R09, core_* citations, companion sections, steward entry doors, or when citing constitutional text.
---

# Corpus lookup

Indexes point. Source binds. Do not treat a locator, gloss, or steward card as a duty.

## Procedure

```bash
python3 tools/corpus_lookup.py edition
python3 tools/corpus_lookup.py resolve QUERY
python3 tools/corpus_lookup.py hydrate QUERY
python3 tools/corpus_lookup.py topic-route QUERY
python3 tools/corpus_lookup.py door CASE_ID
python3 tools/corpus_lookup.py route "QUESTION OR FACT PATTERN"
python3 tools/corpus_lookup.py apply-pack "QUESTION OR FACT PATTERN"
python3 tools/corpus_lookup.py citator --file FILE [--anchor '#fragment']
python3 tools/corpus_lookup.py validity --file FILE --anchor '#fragment'
python3 tools/corpus_lookup.py cite --file FILE --anchor '#fragment'
python3 tools/corpus_lookup.py classes
python3 tools/corpus_lookup.py retrieve "QUESTION OR KEYWORDS"
python3 tools/corpus_lookup.py serve
```

1. **High-pressure or plain-language fact pattern** → `route` (or `door CASE_ID`).
2. `hydrate` the ID or definition term, or `apply-pack` to hydrate owner plus each mandatory read-with.
3. Keyword locator ranking with no ID → `retrieve`, then `hydrate --file --start --end`. Token overlap over heading locators **and** source spans. Vector embeddings are postponed indefinitely (`doc_architecture.md#retrieval-no-vector-embeddings`). Never gloss JSON.
4. If the span exceeds the cap, hydrate a listed term or pass `--file --start --end`.
5. For topics, `hydrate` each `read_with` as well as each primary owner (`apply-pack` does this).
6. For doors, open the returned `card_path`, then verify the boxed operative statement at `operative_box.href`.
7. Cite `file` plus `anchor` plus edition. If the CLI and the source disagree, the source wins.

## Example

`Def.P1` → `resolve Def.P1` → `hydrate` a definition term in that cluster (or a capped range) → cite `core_05_band_participation.md#defp1`.

## Forbidden

- Answering from parametric memory or quoting locator `gloss`
- Treating steward cards as duties
- Opening `ai_corpus/indexes/id_resolver.json` for meaning
- Editing `ai_corpus/` by hand
- Writing a wiki of “what the provision means”
