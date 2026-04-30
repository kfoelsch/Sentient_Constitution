# Core File Migration Map

Purpose: map the current three-file Sentient Constitution core into the planned numbered-file architecture.

This memo is not operative constitutional text. It is a migration planning aid.

## Target file family

- `core_index.md`
- `core_00-01_principles.md`
- `core_02-04_definition_mechanics.md`
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

## Current-to-target chapter map

| Current file | Current content | Target file | Migration note |
|---|---|---|---|
| `core_constitution.md` | Preamble | `core_00-01_principles.md` | Treat the preamble as Chapter `00` in the new visible file family. |
| `core_constitution.md` | Chapter `01` | `core_00-01_principles.md` | Move with the preamble as the unified principles block. |
| `core_definitions.md` | Chapters `02`-`04` | `core_02-04_definition_mechanics.md` | Keep the mechanics pipeline grouped while Chapter Five moves out as its own owner file. |
| `core_definitions.md` | Chapter `05` | `core_05-05_definitions_a_independent.md` | Split out the foundational definitions owner file for traceability and retrieval clarity. |
| `core_constitution.md` | Chapter `06` | `core_06-06_standing.md` | Standalone compliance file. |
| `core_constitution.md` | Chapter `07` | `core_07-07_misconduct.md` | Standalone tiering file. |
| `core_constitution.md` | Chapter `08` | `core_08-08_courts.md` | Standalone courts/jurisdiction file. |
| `core_constitution.md` | Chapter `09`, Part A, Articles `I`-`IV` | `core_09-09_rights_part_a.md` | Preserve current Part A order. |
| `core_constitution.md` | Chapter `09`, Part B, Articles `V`-`XI` | `core_09-09_rights_part_b.md` | Preserve current Part B order. |
| `core_constitution.md` | Chapter `09`, Part C, Articles `XII`-`XXI` | `core_09-09_rights_part_c.md` | Preserve current Part C order. |
| `core_constitution.md` | Chapter `09`, Part D, Articles `XXII`-`XXIV` | `core_09-09_rights_part_d.md` | Preserve current Part D order. |
| `core_constitution.md` | Chapter `10` | `core_10-10_governance.md` | Standalone governance file. |
| `core_amendment.md` | Chapters `11`-`13` | `core_11-13_amendment.md` | Mostly rename rather than doctrinal split. |
| `core_constitution.md` | Chapter `14` | `core_14-14_incorporation.md` | Standalone incorporation bridge file. |

## Current wrapper disposition

Recommended transition handling:

| Legacy file | Transition role |
|---|---|
| `core_constitution.md` | compatibility index pointing to `core_00-01_*`, `core_06-06_*`, `core_07-07_*`, `core_08-08_*`, `core_09-09_*`, `core_10-10_*`, and `core_14-14_*` |
| `core_definitions.md` | compatibility pointer to `core_02-04_definition_mechanics.md` and `core_05-05_definitions_a_independent.md` |
| `core_amendment.md` | compatibility pointer to `core_11-13_amendment.md` |

## Migration order

### Phase 1: navigation scaffolding

Create or stabilize:
- `core_index.md`
- target filename convention in `doc_architecture.md`
- this migration map

No doctrinal movement yet.

### Phase 2: highest-value file splits

Recommended order:

1. `core_00-01_principles.md`
2. `core_09-09_rights_part_a.md`
3. `core_09-09_rights_part_b.md`
4. `core_09-09_rights_part_c.md`
5. `core_09-09_rights_part_d.md`
6. `core_10-10_governance.md`
7. `core_14-14_incorporation.md`

Reason:
- this captures the biggest readability gains first,
- it isolates the best trace-block candidates early,
- it keeps the `02-04` mechanics block coherent while isolating Chapter Five as the expanding canonical term owner,
- it still leaves the `11-13` amendment block for a simpler rename-style pass.

### Phase 3: rename-style moves

Recommended order:

1. `core_definitions.md` -> `core_02-04_definition_mechanics.md` plus `core_05-05_definitions_a_independent.md`
2. `core_amendment.md` -> `core_11-13_amendment.md`
3. `core_constitution.md` -> compatibility wrapper only

### Phase 4: audit and stabilization

Required:
- same-change link updates,
- reference audit,
- README refresh,
- architecture map refresh,
- edition/custody decision for the publication cut.

## File-specific notes

### `core_00-01_principles.md`

Recommended contents:
- current preamble text,
- Chapter One text,
- optional lightweight trace blocks under selected major sections,
- short opening contract that points back to `core_index.md`.

### `core_09-09_rights_part_*.md`

Recommended shared opening:
- one short paragraph stating that all four files are Chapter Nine read together,
- one short line saying Part order remains binding reading order,
- no repeated long boilerplate.

### `core_02-04_definition_mechanics.md`

Recommended handling:
- preserve chapter numbering exactly,
- keep the mechanics pipeline together as one owner block,
- avoid trace-block clutter because the whole file already is the tracing/definition layer.

### `core_05-05_definitions_a_independent.md`

Recommended handling:
- preserve Chapter Five numbering exactly,
- treat this as the canonical term-owner file,
- watch growth here first during future traceability expansion.

### `core_11-13_amendment.md`

Recommended handling:
- preserve the grouped block unless amendment review work later justifies a split,
- keep Chapter Eleven, Twelve, and Thirteen tightly adjacent for validity logic.

## Success conditions

The migration is successful if:
- the file tree itself reveals constitutional order,
- AI can retrieve one chapter or one rights part without hauling unrelated core chapters,
- ownership stays single-home,
- links and chapter citations remain stable,
- legacy filenames can be retired or reduced to thin wrappers without ambiguity.
