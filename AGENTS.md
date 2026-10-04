# Agent instructions (Sentient Constitution)

This file is a **pointer**. It is not the Constitution. It cannot narrow numbered `core_*` files.

- **Edition:** `SC-Corpus-2026.08.09` (effective 2026-08-09). **Pre-release.** Not adoption.
- **Public door:** [README.md](README.md). Adopters and operators: [START_HERE.md](START_HERE.md).
- **Indexes point. Source binds.** Do not open `ai_corpus/indexes/id_resolver.json` for meaning. Do not treat a locator, gloss, or steward card as a duty.

Lookup (from repo root):

```bash
python3 tools/corpus_lookup.py edition
python3 tools/corpus_lookup.py resolve QUERY
python3 tools/corpus_lookup.py hydrate QUERY
python3 tools/corpus_lookup.py topic-route QUERY
python3 tools/corpus_lookup.py door CASE_ID
python3 tools/corpus_lookup.py route "QUESTION OR FACT PATTERN"
python3 tools/corpus_lookup.py apply-pack "QUESTION OR FACT PATTERN"
python3 tools/corpus_lookup.py cite --file FILE --anchor '#fragment'
python3 tools/corpus_lookup.py classes
python3 tools/corpus_lookup.py retrieve "QUESTION OR KEYWORDS"
python3 tools/corpus_lookup.py serve   # optional local HTTP at /v1/{command}
```

`retrieve` is token overlap over boundary-chunk locators, then `hydrate`. Vector embeddings are postponed indefinitely ([doc_architecture.md](doc_architecture.md#retrieval-locators-no-vector-embeddings)).

Spine pack (generated pointers, not duties): `doc_architecture/generated/spine_pack.md`.

Patterns: `ai_corpus/AI_NAVIGATION_GUIDE.md`.

Renumbering or renaming Articles: also update the Mermaid charts that list them (**VIS-CHART-SYNC-03** in [doc_architecture.md](doc_architecture.md#chart-sync-on-renumbering-vis-chart-sync-03)).

New session: check that the git branch name matches the work, and rename it when it does not (**GIT-BRANCH-NAME-01** in [doc_architecture.md](doc_architecture.md#branch-naming-git-branch-name-01)).
