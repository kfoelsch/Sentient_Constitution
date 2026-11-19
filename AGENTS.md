# Agent instructions (Sentient Constitution)

This file is a **pointer**. It is not the Constitution. It cannot narrow numbered `core_*` files.

- **Edition:** `SC-Corpus-2026.10.21` (effective 2026-10-21). **Pre-release.** Not adoption.
- **Public door:** [README.md](README.md). Adopters and operators: [START_HERE.md](START_HERE.md).
- **Indexes point. Source binds.** Do not open `ai_corpus/indexes/id_resolver.json` for meaning. Do not treat a locator, gloss, or steward card as a duty.

**Before you report done** (each item is a standing rule, listed here so none is missed):

1. Run `make preflight` after each edit (about a minute; read-only; failures only), and `make audit-report` before you report completion (**PREFLIGHT-01**, **AUDIT-AUTOFIX-01**). CI refreshes the generated indexes silently, so a green CI does not mean they are committed.
2. Add the numbered entry to the move log in [doc_architecture.md](doc_architecture.md) without being asked, and tell the person its number in the final reply (**MOVE-LOG-AUTO-01**). Take the number from the one shared log, `doc_architecture.md` on `origin/work`; if your push is refused because another session pushed first, rebase and renumber before pushing again (**MOVE-NUMBER-01**).
3. Regenerate and commit the generated files your change touched (`python3 tools/validate_ai_manifests.py --root . --refresh` for the AI indexes; the `-check` targets in `make audit-report` name any other stale file).
4. Git: all work in progress goes on the one shared branch `work`. Commit after each move and push `work` right away; merge `work` into `main` only when asked (**GIT-PUSH-CL-01**; `work` is the exception in **GIT-BRANCH-NAME-01**).
5. **One central folder (GIT-LOCAL-SYNC-01).** The custodian reads the work in VS Code in the checkout on their computer, and that checkout always sits on `work`. For every move: in your own clone `git fetch origin`, `git switch -C work origin/work` (`origin/main` if `origin/work` does not exist yet), make the move, commit, `git push origin work` (if refused: `git pull --rebase origin work`, keep both move-log entries and renumber yours, regenerate generated files, rerun `make preflight`, push again; never force-push). Then run `make sync-local` on the computer and check that `git rev-parse --short HEAD` there shows your commit. Do not report a move as done until it does. `make sync-local` switches the checkout to `work` and fast-forwards it; when the device shell cannot reach GitHub (it has had a proxy 403), copy a bundle of `origin/main` and `origin/work` to `<checkout>/_sync/origin.bundle` first (GIT-LOCAL-SYNC-01 point 6). Never copy repository files into the checkout one at a time, never leave `sync-<n>` folders, and never write drafts straight into the checkout: commit them to `work`. Updating files there needs `device_request_delete_permission`, so ask once per session. If the computer cannot be reached, say so in every reply that changes files and sync it as soon as it is back.

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

Checking your work: `make preflight` is the fast read-only pass to run after each edit; `make audit-report` is the full check. `make audit-report` runs the `make regression` targets quietly and prints one line per category, expanding only failures (about half a minute); `make audit-report-all` adds the audits outside the gate; `python3 tools/audit_report.py --root . --list` shows the categories. Prefer it to reading raw `make regression` output (**AUDIT-REGISTRY-01** in [doc_architecture.md](doc_architecture.md#audit-registry-and-report-audit-registry-01)).

**Automatic audit repairs (AUDIT-AUTOFIX-01):** Formatting, lexical, and citation findings are auto-fixable: fix them without requesting individual sign-off, rerun the affected audits, and run `make audit-report` before reporting completion. This authorization includes numbered core files when the repair preserves meaning. Use canonical source wording and targets; regenerate affected generated files. Do not weaken an audit, add an exemption, or change duties, authority, thresholds, clocks, or scope merely to pass. If a finding requires choosing meaning or has no unambiguous source-backed repair, fix the independent items and present that specific decision. Translation edits remain governed by the translation standing decision below. This is a standing agent workflow, not a claim that every audit has a software `--fix` option. See [Automatic audit repairs](doc_architecture.md#automatic-audit-repairs-audit-autofix-01).

**Audit scope (AUDIT-SCOPE-01):** Every audit, structural audits included, runs against the entire corpus at a minimum. Do not add a file list to a rule (teach it the legitimate uses and reword the real ones), do not use `--changed-only` in a gate recipe, and give a new audit an entry in `tools/architecture/audit_scope_registry.json`. Older findings go in a shrink-only baseline, never a hand-grown exemption. `make audit-scope-check` is the gate and `make audit-scope-probe` measures what each audit reads. The blanket exemption is `doc_architecture.md`. See [doc_architecture.md](doc_architecture.md#audit-scope-audit-scope-01).
**Automatic move log (MOVE-LOG-AUTO-01):** When a session changes corpus text, a rule, an audit, or generated structure, add its entry to the numbered move log in [doc_architecture.md](doc_architecture.md) in the same sitting, without being asked. One entry per decision, in the style of the latest entries: the next number in words, a short title and the date, who decided (for example "custodian, asked in session"), what changed and why, and "uncommitted" until committed. State any effect on a rule plainly (a new must or should, a wider or narrower scope, a new audit rule) and name the matching edits elsewhere. Wording-only or layout-only changes may share one entry per sitting, marked as such. Then regenerate the affected generated files and run `make audit-report` before reporting completion, and tell the person the entry number in the final reply. The entry is the record of the decision and its reasoning: do not also write a separate implementation or evaluation doc for the same move under the Claude project (`claude/`). Write a project doc only when the custodian asks for a plan, report or evaluation, or when the material is too long for a log entry.

**Edit the document live (EDIT-LIVE-01):** Until the announcement, when the custodian asks you to rewrite, reword, clarify, insert, or fix text in the corpus, make the edit in the file in that same reply and show what changed. Do not offer a draft and wait for a second "please insert". A question about what text means is answered without editing. Where the change would choose meaning (a duty, authority, threshold, clock, or scope), present that choice instead of making it. Translations stay under the translation standing decision below. The edit is uncommitted until the custodian asks for a commit; log it under **MOVE-LOG-AUTO-01**. This rule ends at the announcement, when the `CONTRIBUTING.md` lanes apply. See [Edit the document live](doc_architecture.md#edit-the-document-live-edit-live-01).

Spine pack (generated pointers, not duties): `doc_architecture/generated/spine_pack.md`.

Patterns: `ai_corpus/AI_NAVIGATION_GUIDE.md`.

Working files stay out of the repo root: plain-language companions go in `project/plain_language/`, drafts and WIP under `project/`, and `*.bundle` patch-transfer files are deleted once pushed. No file may exceed 1 MB (**FILE-SIZE-01**; `make file-size-audit`): split it, compact it, or keep it out of the repo. `make root-layout-audit` enforces this (**ROOT-LAYOUT-01**); `python3 tools/root_layout_audit.py --fix` moves plain-language files.

Front doors (README, START_HERE, ANNOUNCEMENT, `llms.txt`, `docs/index.md`): when you change something they count or quote (edition, chapter or Article numbers, translations, the Two Fundamental Questions, a `make` target, the fit list), update them in the same commit and run `make front-door-audit` (**FRONT-DOOR-01** in [doc_architecture.md](doc_architecture.md)). The edition label is the current date until the announcement: move it with `make edition-bump` (dry run: `python3 tools/bump_edition.py --root .`), not by hand. Section labels in their links are checked by `make section-label-anchor-audit` (**FRONT-DOOR-LABEL-01**).

Translations: Anthropic models (Claude) are not currently related to the translation work (steward note, 2026-10-20). Do not assume that files under `translations/`, translation work, or `project/translation_drafts/` come from a Claude session, and do not edit, sync, or commit them as part of English edits. Translations are paused (see `project/MEMLOG.md`, Standing Decisions). When translation work is authorized, draft each document in all 19 supported languages unless the custodian scopes the work otherwise. Keep drafts in `project/translation_drafts/` until separately authorized for synchronization.

Renumbering or renaming Articles: also update the Mermaid charts that list them (**VIS-CHART-SYNC-03** in [doc_architecture.md](doc_architecture.md#chart-sync-on-renumbering-vis-chart-sync-03)).

Files named like another file plus ` 2` before the extension (`core_07_charters 2.md`) are copy artifacts, not corpus, and may be deleted freely when the original exists and git does not track the copy (run `make install-hooks` once per checkout and the pre-commit hook deletes them before each commit, or run `make copy-suffix-clean`; **FILE-COPY-SUFFIX-01** in [doc_architecture.md](doc_architecture.md#copy-suffixed-duplicate-files-file-copy-suffix-01)).

New session: check that the git branch name matches the work, and rename it when it does not (**GIT-BRANCH-NAME-01** in [doc_architecture.md](doc_architecture.md#branch-naming-git-branch-name-01)).

New session and before each move: `git fetch origin` in your own clone and start from `origin/work` (or `origin/main` when there is no `work`), as in item 5 (**GIT-LOCAL-SYNC-01** in [doc_architecture.md](doc_architecture.md#keeping-your-local-copy-current-git-local-sync-01)). Regenerate generated files instead of resolving them by hand.

The custodian's checkout always sits on `work`; `make sync-local` keeps it there (**GIT-LOCAL-SYNC-01**). After every commit a Claude Code session pushes `work`; a session that cannot push gives the exact command, `git push origin work`. Merging waits for the custodian (**GIT-PUSH-CL-01** in [doc_architecture.md](doc_architecture.md#reporting-a-commit-git-push-cl-01)).

Pushing and merging from a Claude Code session: the shell on the custodian's computer (`device_bash`) has no GitHub credentials and no `gh`, and has had no network route to GitHub at all (proxy 403). So a Claude Code session does its git work in its own clone:

1. Attach the repo with `add_repo` (owner `kfoelsch`, repo `Sentient_Constitution`, access `push`) and make one shallow clone. Work on `work` as in item 5 above: fetch, `git switch -C work origin/work`, commit each move, `git -c push.negotiate=true push origin work`. Pushing `work` needs no ask.
2. **Sync the computer after each push:** `make sync-local` on the device, with a fresh `_sync/origin.bundle` when it cannot fetch (GIT-LOCAL-SYNC-01 point 6), and check the commit hash there.
3. **Work that began on the computer** (the custodian's edits or a Codex session) is committed on `work` there. When the computer cannot push it, run `git bundle create _sync/outgoing.bundle origin/work..work` on the device (`origin/main..work` if `origin/work` does not exist), copy it across with `device_stage_files`, and in the clone run `git bundle verify <file>`, `git fetch <file> work:refs/remotes/computer/work`, rebase onto `origin/work` if needed, and push. Do not replay with `git format-patch` and `git am`.
4. `gh pr create` fails in Claude Code sessions because GraphQL is blocked. When the custodian says "merge", open the pull request from `work` with `gh api repos/kfoelsch/Sentient_Constitution/pulls -X POST -f title=... -f head=work -f base=main -F body=@<file>` and write an accurate body that lists the moves on it. Merge with `gh api repos/kfoelsch/Sentient_Constitution/pulls/<n>/merge -X PUT -f merge_method=merge`; the repo uses merge commits titled `Merge pull request #<n> from ...`. GitHub then deletes `work`, and the next move recreates it from `main`.
5. Wait for the `regression` job and compare its failing audits with the last run on `main` (`gh api repos/kfoelsch/Sentient_Constitution/actions/runs`, then `.../actions/jobs/<id>/logs`). Read the `Result: FAIL (n gate targets failing)` line and the names of the failing targets, not every `FAIL` line: unit tests print `FAIL` messages on purpose and still pass (the time-window tests print TIME-LOCK-01 lines). Merge only when the pull request adds no failing target that `main` lacks. Run `make corpus-markdown-audit` after the last edit and before pushing: it requires a bold list intro to end in a colon (MD-LIST-INTRO-01), and that rule failed CI once.
6. Afterward, run `make sync-local` on the device (it fast-forwards `main` and keeps the checkout on `work`, which now matches `main`). Then delete the session's bundles and patch files in the project files.

Git commands run on the device leave `.git/*.lock` files, because deleting is blocked there. Move a stale lock aside (`mv .git/HEAD.lock .git/stale-HEAD-lock-<date>`), and never touch one that a running git may hold.

Pull requests: the Claude Code UI auto-generates PR bodies and can mislabel them (wrong lane, "no change of meaning", wrong model). After a PR is created, correct the body so it says what changed and which files were touched.

**Lanes are not enforced before the announcement (custodian decision, 2026-10-07).** The repo is pre-release, so the `CONTRIBUTING.md` lane gates (Proposal issue, obligation snapshot/diff, evidence folder, Substantive Test 1 self-check) do not block merging. Keep `make regression` green and the PR body accurate. The lanes apply after the announcement.

Chapter numbering: use `tools/architecture/chapter_numbers.json` as the source; never derive chapter numbers by splitting filename digits. After an intentional renumbering, update every front door and Mermaid chart that lists the changed chapters, regenerate indexes, run `make chapter-number-audit`, `make chapter-number-audit-test`, and `make audit-report`. Preserve translation files and translation work.
