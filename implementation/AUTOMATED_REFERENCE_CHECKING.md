# Automated Reference Checking

This repository now includes an automated reference-integrity gate intended to run when TODO closure work is completed.

## Plan -> Act -> Verify flow

### Plan
- Canonical article map source: merged `### Article …:` headings from `core_10-10_rights_part_*.md` (see `tools/reference_audit.py`).
- Scan scope (default for `make reference-audit`):
  - `core_*.md` (Sentient Constitution chapters), `corpus_*.md`, companion subfiles such as `corpus_joint_structure/*.md`, `doc_architecture.md`
  - Optional / suspended: `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` when that file is present again

### Act
- Run a validation-only check:
  - `make reference-audit`
- Run and write an evidence artifact:
  - `make reference-audit-evidence`
  - Output: `evidence/<YYYY-MM-DD>/REFERENCE_INTEGRITY_AUDIT_<YYYY-MM-DD>.md`

### Prose continuity (corpus formatting regression)

The `tools/prose_continuity_audit.py` gate catches recurring editorial defects: stray leading-space lines (broken Markdown continuations) and a small set of known stranded continuation fragments (for example lines that begin with “Failure to do so” after a paragraph break).

- Validation: `make prose-continuity-audit` (also runs as part of `make regression`).
- Evidence artifact: `make prose-continuity-audit-evidence` → `evidence/<YYYY-MM-DD>/PROSE_CONTINUITY_AUDIT_<YYYY-MM-DD>.md`.
- Scope defaults to the Sentient Constitution `core_*.md` files, `corpus_joint_structure.md` plus `corpus_joint_structure/*.md`, `corpus_systems.md`, and `corpus_institutions.md`. Use `--no-orphan-lines` to only enforce the indent rule.

### Chapter Five trace-block metadata placement

The `tools/ch5_trace_crosslink_audit.py` gate protects the Chapter Five authoring rule that navigation metadata such as `Read with:` must remain inside the local `Trace` / `<details>` block and must not appear as standalone operative prose.
It does not prohibit selective same-file cross-definition links in the operative O / E / C body.

- Validation: `make ch5-trace-crosslink-audit` (also runs as part of `make regression`).
- Current scope: `core_05-05_definitions_a_independent.md`.
- Failure mode: any `Read with:` line found outside a local `<details>` block is treated as a regression.

### Chapter Ten subarticle trace coverage

The `tools/ch9_trace_audit.py` gate protects the Chapter Ten authoring rule that operative rights traces belong at the `#### Article …` subarticle level, not only at parent-article openings. It also requires a minimum navigation payload in each subarticle trace block: `Principles:` plus linked `Definitions:`.

- Validation: `make ch9-trace-audit` (also runs as part of `make regression`).
- Current scope: `core_10-10_rights_part_a.md` through `core_10-10_rights_part_d.md`.
- Failure mode: any Chapter Ten subarticle heading without a local `<details>` trace block, without a `Principles:` line, or without linked definition targets in `Definitions:` is treated as a regression.

### Verify
- Ensure the command exits successfully.
- Confirm evidence artifact is present for the run date.
- Link the artifact in any TODO closure note where relevant.

## Optional commit-time gate

A hook script is provided at `.githooks/pre-commit`.

It runs `make regression` when staged changes touch authoritative corpus files, regression scenarios, audit tooling, or the `Makefile`, and runs `make todo-close-check` when `TODO.md` is staged.

To enable it in a git repo:

1. `chmod +x .githooks/pre-commit`
2. `git config core.hooksPath .githooks`

If this workspace is not currently a git repo, the script is inert.
