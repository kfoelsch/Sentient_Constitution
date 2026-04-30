# Primitives Reframe and Migration Matrix - 2026-04-14

**Status:** Historical. Operative **PRIM/PROT** implementation text and **PCH1–PCH4** structure now live in [`corpus_joint_structure.md`](../corpus_joint_structure.md) (*Constitutional primitives — implementation layer*). The [`corpus_primitives.md`](../corpus_primitives.md) path is **redirect-only**; do not use this memo as a live file map without cross-checking `corpus_joint_structure.md`.

Purpose: first-pass triage for the former `corpus_primitives.md` volume on a primitive-by-primitive basis so future edits could improve usability by changing ownership and framing, not just prose.

This memo is not doctrinal source text. It is a migration aid grounded in the owner rules in `doc_architecture.md` and the section structure that was migrated into `corpus_joint_structure.md`.

## Executive view

The current primitives file is difficult to use for three distinct reasons:

1. It mixes a clean active `PRIM`/`PROT` registry with a second legacy `Provision I-X` structure.
2. Some sections act like reusable primitives, while others act mainly as routing glue to `corpus_joint_structure.md` or local owner files.
3. Chapter Four reads like a partially completed migration: the legacy provisions no longer own much substance, but they still occupy navigation space and make the file feel internally contradictory.

## Recommended rule set

Use this decision rule for each section:

1. Keep in `corpus_primitives.md` if it states a reusable cross-domain primitive constraint.
2. Move to `corpus_joint_structure.md` if it mostly coordinates interfaces among `CP`, `CS`, `CI`, and `CC`.
3. Move to `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md` if it is really local operational doctrine.
4. Elevate to core only if it has become canonical constitutional meaning rather than implementation.
5. Delete or collapse to a one-line editor note if a section is only a redundant routing shell.

## Matrix

| Section | Current job | First-pass diagnosis | Recommendation | Destination / handling |
|---|---|---|---|---|
| Registry (`PRIM1`-`PRIM15`, `PROT1`-`PROT6`) | Canonical primitive code map | Necessary and useful | Keep | `corpus_primitives.md` frontmatter |
| Meta Primitive: Constitutional Supremacy, Enforceability, and Epistemic Grounding | Meta floor and routing anchor | Valid as a true meta primitive, but should stay short and non-duplicative | Keep, tighten | `corpus_primitives.md` PCH1 |
| Meta Primitive: Trust and Trustworthiness | Meta floor plus class/routing consequences | Mostly valid in CP; some routing language could be shortened | Keep, tighten | `corpus_primitives.md` PCH1 |
| Meta Primitive: Incentive Alignment and Mechanism Integrity | Meta floor with substantive reusable constraint | Strong fit for CP | Keep | `corpus_primitives.md` PCH1 |
| Meta Primitive: Failure Integrity | Meta floor with owner-layer routing | Strong fit for CP, but should resist absorbing continuity protocol detail | Keep, tighten | `corpus_primitives.md` PCH1 |
| PRIM1 | Reusable presentation constraint | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM2 | Reusable comprehensibility constraint | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM4 | Reusable transparency/disclosure constraint | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM5 | Reusable dependency and risk-integrity constraint | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM6 | Reusable degradation/failure-mode constraint | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM7 | Reusable anti-lock-in / portability primitive | Strong fit for CP; high value as single owner | Keep | `corpus_primitives.md` |
| PRIM8 | Technical intervention primitive | Strong fit for CP if kept distinct from governance authorization | Keep | `corpus_primitives.md` |
| PRIM9 | Reusable auditability primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM10 | Reusable tiered transparency primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM11 | Reusable independent-verification primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM12 core reversibility/containment rule | Reusable integrity primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM12 retention and lifecycle integrity block | Hybrid primitive plus heavy cross-companion implementation seam | Substantively important, but part of it behaves like a CJS/CS interface cluster | Split | Keep primitive floor in CP; move interface-heavy operational detail to `corpus_joint_structure.md` and `corpus_systems.md` |
| PRIM14 | Reusable adversarial robustness primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PRIM15 | Reusable evolution/non-entrenchment primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PROT1 | Governance-layer primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PROT2 | Governance-layer intervention authorization primitive | Strong fit for CP if separated from local emergency mechanics | Keep | `corpus_primitives.md` |
| PROT3 | Governance-layer reflexive accountability primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PROT4 | Governance-layer burden/constraint primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PROT5 | Governance-layer secrecy/investigation primitive | Strong fit for CP | Keep | `corpus_primitives.md` |
| PROT6 main section | Governance-layer procedural integrity primitive | Keep, but make it the only procedural anchor in Chapter Four | `corpus_primitives.md` |
| PROT6 subsections 1-13 | Mostly pointer stubs into CJS | They no longer carry independent doctrine and mostly duplicate the existence of CJS buckets | Collapse | Replace with short scoped index under PROT6 or move to editor memo |
| Provision I | Oversight/enforcement routing note | No longer owns doctrine | Delete from normative file after migration | Fold any needed note into Chapter Four intro |
| Provision II | Distribution-of-power legacy shell | Duplicates PROT1 and Chapter Ten routing | Delete from normative file after migration | If needed, one-line editor note only |
| Provision II.1 | Distribution of power routing note | Duplicate of PROT1 and owner map | Delete | No replacement needed beyond PROT1/CJS references |
| Provision II.2 | DRP routing note | Owner is already `core_constitution.md` Chapter Ten + CJS | Delete | No replacement needed |
| Provision II.3 | Quorum/legitimacy routing note | Owner is already Chapter Ten + CJS | Delete | No replacement needed |
| Provision III | Redress/restoration routing note | Duplicate owner pointer | Delete | No replacement needed |
| Provision IV | Conflict resolution routing note | Duplicate owner pointer | Delete | No replacement needed |
| Provision V | Dignity/equal standing routing note | Topic is too broad for CP and not actually owned here | Delete | No replacement needed |
| Provision VI | Adjudication/enforcement routing note | Fully superseded by `PROT6` plus courts/institutions/CJS owners | Delete | No replacement needed |
| Provision VII | Good standing/stewardship routing note | Topic is owned by core + institutions | Delete | No replacement needed |
| Provision VIII | Resource transfer/exchange routing note | Topic is owned by systems + related review owners | Delete | No replacement needed |
| Provision IX | Transitional stewardship/bootstrapping routing note | Topic is owned by systems | Delete | No replacement needed |
| Provision X | External systems/transitional interaction routing note | Topic is owned by systems | Delete | No replacement needed |

## Practical interpretation

The file is not unusable because every primitive is bad. The active primitive stack is mostly salvageable.

The file is unusable because it still contains two overlapping navigation grammars:

- the active grammar: `PRIM` / `PROT`
- the legacy grammar: `Provision I-X`

The second grammar now mostly contains owner-pointer residue rather than operative substance. That creates false density, obscures where doctrine really lives, and makes Chapter Four feel like both a live codebook and a decommissioned migration scaffold.

## Highest-value migration moves

1. Remove `Provision I-X` from `corpus_primitives.md` after confirming that each live owner pointer is already adequately represented in `doc_architecture.md` or the relevant owner file.
2. Collapse `PROT6` subsections `1-13` into a short scoped index unless they still carry unique doctrine not already present in `corpus_joint_structure.md`.
3. Split the retention/lifecycle block under `PRIM12` into:
   - primitive floor in `corpus_primitives.md`
   - cross-companion interface logic in `corpus_joint_structure.md`
   - class/data-type operational mechanics in `corpus_systems.md`
4. Keep Meta Primitive Chapter One, `PRIM1-PRIM15`, and `PROT1-PROT6` as the surviving canonical CP structure.
5. After structure is cleaned up, run a readability pass. Do not do the readability pass first.

## Suggested migration order

1. Chapter Four legacy provision deletion pass.
2. `PROT6` compression pass.
3. `PRIM12` split pass.
4. Readability cleanup on surviving sections only.
5. Reference audit and architecture note update if any citations or editing guidance change.

## Continued execution plan

The first three structural moves are now complete. The remaining work should stay narrow and should not reopen owner allocation unless a paragraph clearly fails the guardrails below.

### Phase 4 - readability cleanup

Goals:

1. Make each surviving section easier to scan without reintroducing a second navigation grammar.
2. Reduce repeated owner/routing prose that currently makes many sections feel longer than their actual doctrine.
3. Preserve the current allocation: CP keeps reusable primitive floors; CJS and owner files keep interface and local implementation detail.

Section-by-section method:

1. Keep one short anchor block where needed: constitutional anchor, canonical meaning, and any required read-with pointer.
2. Collapse repeated cross-companion formulas when they do not add section-specific substance.
3. Prefer short lead sentences that state the primitive floor before examples, lists, or owner notes.
4. Do not polish interface-heavy paragraphs in place if they mostly belong in `corpus_joint_structure.md`, `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md`.

Suggested pass order:

1. **PCH1** meta primitives: shorten routing-heavy explanation while preserving the meta-floor policy.
2. **PRIM1-PRIM15**: normalize repeated anchor and joint-interface language, keeping section-specific doctrine prominent.
3. **PROT1-PROT6**: preserve `PROT6` as the sole procedural anchor and keep Chapter Four clearly governance-primitive in character.

### Phase 5 - reference audit and closeout

Audit checklist:

1. Search `corpus_primitives.md` for stale `Provision` references and legacy primitive-number language.
2. Search the wider repo for CP references that still imply the deleted Chapter Four shell structure.
3. Verify that surviving `PRIM` / `PROT` citations, `CP-PCH1-PCH4` references, and `corpus_joint_structure.md` read-with pointers still point to live owner text.
4. Update `doc_architecture.md` and any evidence or execution note only if the readability pass changes migration guidance or exposes another relocation candidate.

Closeout condition:

The CP migration can be treated as complete for this cycle when `corpus_primitives.md` reads as a single active codebook built around **PCH1-PCH4** and **PRIM/PROT**, with no leftover reliance on the deleted legacy navigation layer.

### Execution note - 2026-04-14 readability continuation

This continuation pass advanced **Phase 4** without reopening owner allocation.

Completed in `corpus_primitives.md`:

1. Tightened **PCH1** opening and Meta Primitive anchor language so the chapter reads more like one active floor-setting layer and less like repeated routing boilerplate.
2. Clarified the surviving **PRIM8**, **PRIM12**, and **PROT6** bridge language so the CP/CJS split stays visible without reintroducing the deleted legacy shell.
3. Promoted the previously inline **Layer B — Integrity Implementation Primitives (PRIM9-PRIM15)** label into a visibly scoped lead-in.

Verification:

1. `make reference-audit` passed on **2026-04-14** after the readability edits.
2. Search of `corpus_primitives.md` found no live normative reliance on deleted **Provision I-X** navigation.

Remaining closeout work:

1. Broader repo cleanup only where historical notes or evidence artifacts still describe pre-migration CP structure.

### Execution note - 2026-04-14 readability completion continuation

This pass completed the remaining live **Phase 4** readability normalization inside `corpus_primitives.md` and updated the architecture note so plan status matches the file state.

Completed in `corpus_primitives.md`:

1. Tightened **PRIM14** so the section now states its integrity-layer role before the supporting cross-reference stack.
2. Tightened **PRIM15** so revalidation and non-entrenchment read as the main floor rather than as dispersed supporting clauses.
3. Clarified **PROT6** as the governance-layer home for due-process minima and binding-outcome safeguards without reopening old subsection scaffolding.

Completed in `doc_architecture.md`:

1. Updated the CP migration-plan status to mark the readability pass and same-pass reference-audit follow-through as complete.
2. Preserved older provision-heavy pass notes as historical narrative rather than live CP structure guidance.

Verification:

1. `make reference-audit` passed on **2026-04-14** after the completion pass.
2. `doc_architecture.md` now records the CP cleanup program as structurally complete for the live file, with only optional historical-note cleanup remaining outside `corpus_primitives.md`.

### Execution note - 2026-04-14 readability normalization continuation

This follow-on pass continued **Phase 4** and kept the owner map unchanged.

Completed in `corpus_primitives.md`:

1. Tightened **PRIM5-PRIM7** so each section now states its architecture-layer role before the supporting owner and read-with material.
2. Normalized **PRIM9-PRIM11** anchor language to surface the governing integrity floor more directly and reduce stacked boilerplate.
3. Clarified **PROT1-PROT5** as governance-layer homes for their respective domains, keeping the **PRIM/PROT** split visible without reviving legacy shell language.

Verification:

1. `make reference-audit` passed on **2026-04-14** after the normalization pass.
2. Search of `corpus_primitives.md` for `Provision [IVX]+` and `Primitive [0-9]+` returned no live matches.

### Execution note - 2026-04-14 closeout continuation

This pass advanced **Phase 5** closeout outside the live CP file without reopening any owner-allocation decision.

Completed in active project docs:

1. Recast `doc_architecture.md` from an in-progress CP migration plan to a CP migration closeout note so the architecture map now reflects completed status rather than a still-running cleanup program.
2. Updated live scenario hooks in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` to use surviving `PROT6` references instead of deleted `Provision VI` wording.
3. Updated `implementation/CORPUS_COURTS_FILE_PLAN_2026-04-12.md` so its retained courts-interface note treats `Provision VI` as legacy substance consolidated into `PROT6`.

Closeout result:

1. The remaining non-archive, non-evidence project guidance now describes CP using the surviving **CP-PCH1-PCH4** and **PRIM/PROT** structure more consistently.
2. Any older provision-heavy references left in architecture pass logs should be read as historical narrative unless separately refreshed.

## Default framing for the rebuilt file

If the file is revised after the migration, its effective mental model should be:

- Primitive Chapter One: cross-domain meta floors
- Primitive Chapters Two and Three: reusable presentation / architecture / integrity primitives
- Primitive Chapter Four: reusable governance primitives

Everything else should be somewhere else.
