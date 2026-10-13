# Agent instructions (Sentient Constitution)

This file is a **pointer**. It is not the Constitution. It cannot narrow numbered `core_*` files.

- **Edition:** `SC-Corpus-2026.10.12` (effective 2026-10-12). **Pre-release.** Not adoption.
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

Working files stay out of the repo root: plain-language companions go in `project/plain_language/`, drafts and WIP under `project/`, and `*.bundle` patch-transfer files are deleted once pushed. No file may exceed 1 MB (**FILE-SIZE-01**; `make file-size-audit`): split it, compact it, or keep it out of the repo. `make root-layout-audit` enforces this (**ROOT-LAYOUT-01**); `python3 tools/root_layout_audit.py --fix` moves plain-language files.

Front doors (README, START_HERE, ANNOUNCEMENT, `llms.txt`, `docs/index.md`): when you change something they count or quote (edition, chapter or Article numbers, translations, the Two Fundamental Questions, a `make` target, the fit list), update them in the same commit and run `make front-door-audit` (**FRONT-DOOR-01** in [doc_architecture.md](doc_architecture.md)). The edition label is the current date until the announcement: move it with `make edition-bump` (dry run: `python3 tools/bump_edition.py --root .`), not by hand. Section labels in their links are checked by `make section-label-anchor-audit` (**FRONT-DOOR-LABEL-01**).

Renumbering or renaming Articles: also update the Mermaid charts that list them (**VIS-CHART-SYNC-03** in [doc_architecture.md](doc_architecture.md#chart-sync-on-renumbering-vis-chart-sync-03)).

New session: check that the git branch name matches the work, and rename it when it does not (**GIT-BRANCH-NAME-01** in [doc_architecture.md](doc_architecture.md#branch-naming-git-branch-name-01)).

New session and before a pull request: `git fetch origin` and check that the local copy is current with `origin/main` (**GIT-LOCAL-SYNC-01** in [doc_architecture.md](doc_architecture.md#keeping-your-local-copy-current-git-local-sync-01)). Fast-forward local `main`, merge `origin/main` into the work branch, and regenerate generated files instead of resolving them by hand.

Always leave the checkout on the current branch: a branch whose pull request has merged is finished, so start the next work from current `main` and stash or move any stale uncommitted work first (**GIT-LOCAL-SYNC-01**). After every commit, give the exact push command, `git push -u origin <branch>` for a first push and `git push` after, and do not push unless asked (**GIT-PUSH-CL-01** in [doc_architecture.md](doc_architecture.md#reporting-a-commit-git-push-cl-01)).

Pull requests: the Claude Code UI auto-generates PR bodies and can mislabel them (wrong lane, "no change of meaning", wrong model). After a PR is created, correct the body so it says what changed and which files were touched.

**Lanes are not enforced before the announcement (custodian decision, 2026-10-07).** The repo is pre-release, so the `CONTRIBUTING.md` lane gates (Proposal issue, obligation snapshot/diff, evidence folder, Test 1 self-check) do not block merging. Keep `make regression` green and the PR body accurate. The lanes apply after the announcement.
