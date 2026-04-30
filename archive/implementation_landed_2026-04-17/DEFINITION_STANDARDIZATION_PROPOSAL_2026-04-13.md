# Definition Standardization Proposal

## Purpose

This proposal addresses a recurring corpus problem: definition descriptions and non-core file rule statements are governed by the right general principle already, but they are not yet normalized into one reusable drafting pattern.

The current corpus already establishes most of the needed authority structure:
- `core_definitions.md` Chapters Two through Five are the single constitutional home for definition mechanics and canonical constitutional terms.
- `doc_architecture.md` section 4 already says definitions should have a single owner and that other files should use pointers plus layer-specific operational criteria.
- `corpus_primitives.md`, `corpus_systems.md`, and `corpus_institutions.md` already say they do not redefine constitutional terms, rights floors, or O/E/C mechanics.

The remaining gap is not mainly one of authority. It is one of drafting standardization:
- companion files still restate similar description logic in slightly different prose,
- local interpretation blocks vary in shape and density,
- some non-core sections still risk sounding like second-home definitions even when they intend only to operationalize the canonical term.

The recommended fix is:
1. place the binding drafting rule in the core constitutional layer,
2. place the reusable implementation pattern in the primitive layer,
3. require companion files to inherit by pointer unless they are defining a taxonomy or subsection-local operational construct that the architecture map expressly assigns to them.

## Recommended model

### 1. Core should define the corpus-wide rule

The most important rule is not merely editorial. It is interpretive and anti-drift in character, so it belongs in the core constitutional source.

Recommended content for the core rule:
- each constitutional term, definition description, and clustered traceability concept has one canonical home,
- other files may apply, scale, or operationalize that term but must not restate it as a parallel definition,
- when a companion file needs local terminology, it must label that terminology as local and non-redefinitional,
- if a passage outside the canonical home appears to broaden, narrow, or compete with the canonical definition, the canonical definition governs.

Best home:
- primary home: `core_definitions.md`, likely in Chapter Five near the Interdependent / Clustered framework or as a short concluding rule tied back to Chapters Two through Four,
- secondary cross-reference: `core_constitution.md` Chapter Fourteen, because incorporated companion text is where drift pressure shows up in practice.

### 2. Primitives should define the reusable drafting pattern

The primitive layer is a good place to standardize how implementation-layer text is supposed to speak when it is applying rather than redefining.

Recommended primitive-level function:
- define a reusable inheritance-and-application pattern for incorporated companion text,
- specify the approved forms of non-core drafting,
- make explicit what counts as permissible elaboration versus prohibited redefinition.

That primitive should say companion text may do only the following:
- identify the canonical source,
- state the operational purpose of the local section,
- add implementation conditions, thresholds, procedures, classifications, or controls that the owner table assigns to that file,
- define subsection-local shorthand only if it is explicitly labeled local in scope,
- state conflict and override behavior.

This is more a corpus-governance primitive than a rights primitive, so the best home is likely `corpus_primitives.md` in the governance or architecture layer rather than in a rights-facing core article.

### 3. Non-core files should use an explicit inheritance template

The companion files should stop inventing their own near-equivalent opening language and instead use one standard pattern.

Recommended standard section shape for non-core files:

1. `Canonical source`
   Identifies the controlling core or assigned owner file.

2. `Local function`
   States what this file does operationally that the canonical source does not do.

3. `No redefinition`
   States that constitutional meaning, rights floors, and O/E/C mechanics remain in the canonical home.

4. `Permitted local additions`
   States what this file may add: procedures, thresholds, taxonomies, stewardship tiers, controls, recordkeeping, review lanes, and similar implementation detail.

5. `Local terminology rule`
   States that any subsection-local term is local unless separately elevated into a canonical definition owner.

6. `Conflict rule`
   States that the canonical definition controls if local wording diverges.

This would replace the current pattern where each file says roughly the same thing in slightly different prose.

## Draft rule text

### A. Proposed core text

Suggested draft for insertion into `core_definitions.md`:

> Each constitutional definition, definition description, and clustered traceability concept must have one canonical home in this corpus. That canonical home governs meaning, scope, and satisfaction conditions. No incorporated or companion text may create a parallel definition, competing gloss, or narrowing restatement of a term whose canonical home is assigned by this Constitution or by the corpus architecture map adopted under it.
>
> Companion and incorporated text may operationalize canonical terms only by pointer plus layer-specific criteria, procedures, classifications, controls, or implementation conditions within their assigned scope. Any subsection-local terminology in such text must be expressly identified as local and non-redefinitional unless and until adopted into a canonical definition owner.
>
> Where wording outside the canonical home appears to broaden, narrow, substitute for, or compete with the canonical definition, the canonical definition governs. Such competing wording must be read, if possible, as implementation detail only; if that reading is not possible, the competing wording is inoperative to the extent of the conflict.

Why this belongs in core:
- it protects interpretive integrity,
- it reduces silent drift in incorporated files,
- it gives courts and editors a clean conflict rule,
- it turns current editorial best practice into an explicit constitutional instruction.

### B. Proposed primitive text

Suggested draft for insertion into `corpus_primitives.md`:

> Incorporated implementation text must inherit constitutional meaning from its canonical source. Its role is to realize, scale, or operationalize that meaning within the implementation domain assigned to it. Incorporated implementation text must not restate constitutional meaning as a second home.
>
> When a companion file uses a canonical constitutional term, the local section should identify the canonical source, state the operational function of the local section, and then add only the implementation detail necessary for that layer. Permitted additions include procedures, control patterns, thresholds, stewardship requirements, taxonomies, audit hooks, review lanes, and subsection-local shorthand clearly marked as local.
>
> Local shorthand or operational constructs do not become constitutional definitions by analogy, formatting, or repeated reuse. If a local construct becomes cross-cutting or interpretively necessary across layers, it must be elevated into the canonical owner file rather than duplicated across companion files.

Why this belongs in primitives:
- it gives drafters a repeatable implementation pattern,
- it applies directly to incorporated text,
- it can normalize file openings and subsection intros without overloading the core with drafting mechanics.

### C. Standard inheritance block for companion files

Suggested reusable template:

> **Definition inheritance and local scope**
>
> This file implements constitutional requirements within its assigned domain. Canonical meaning for constitutional terms, rights floors, and definition-satisfaction rules remains in the Sentient Constitution and any other file identified as the canonical owner in `doc_architecture.md`.
>
> This file may add only domain-specific implementation detail within its assigned scope, including procedures, taxonomies, thresholds, stewardship controls, review paths, and recordkeeping or audit requirements. It does not create a second home for constitutional meaning.
>
> Any subsection-local shorthand in this file is local to the hosting section unless another canonical owner later adopts it expressly. If local wording appears to conflict with or narrow the canonical definition, the canonical definition governs.

This block could replace the slightly different language now found in:
- `corpus_primitives.md`,
- `corpus_systems.md`,
- `corpus_institutions.md`,
- likely `corpus_courts.md` as well.

## Standardized schema for definition descriptions

The corpus should standardize the shape of definition descriptions before trying to force sentence-level uniformity.

Recommended schema for canonical definition entries:
- `Function`: what role the definition plays in the corpus,
- `Scope`: what it covers and what it excludes,
- `Satisfaction logic`: what must be true for application or satisfaction,
- `Traceability hooks`: what clustered definitions, burden rules, or articles must be read with it,
- `Boundary rule`: what this definition does not itself decide and where that work belongs.

This can be implemented lightly. It does not require every entry to use the same exact prose cadence. It only requires each entry to answer the same structural questions.

That approach preserves legitimate variation while preventing accidental omission and drift.

## Decision rule for what lives where

Use this sorting rule:

- Put it in core if it states meaning, scope, satisfaction, or anti-narrowing rules for a constitutional term or cross-cutting interpretive concept.
- Put it in primitives if it states a reusable implementation-layer drafting or governance pattern that multiple incorporated files should follow.
- Keep it in a companion file only if it is a taxonomy, procedure, threshold, stewardship rule, or subsection-local operational construct assigned to that file by `doc_architecture.md`.

Practical trigger for elevation:
- if a local term appears in more than one companion file,
- or if its wording changes legal meaning rather than mere implementation,
- or if editors need to ask repeatedly what the “real” description is,
- then it should be elevated to a canonical home.

## Suggested adoption sequence

1. Add the core anti-duplication / canonical-home rule.
2. Add the primitive inheritance-and-application rule.
3. Replace opening interpretation language in companion files with one standard inheritance block.
4. Sweep for repeated definition-description prose and convert repeats into pointers plus local criteria.
5. Reserve local O/E/C analogues like `OP-O` / `OP-E` / `OP-C` for clearly labeled companion-file operational constructs only.

## Bottom line

The corpus already has the right constitutional instinct: single home, pointers elsewhere, no silent narrowing. What it lacks is one explicit reusable standard for how definition descriptions and non-core elaborations must be written.

So my recommendation is:
- yes, define the canonical-home rule in the core,
- yes, define the implementation inheritance pattern in primitives,
- yes, standardize companion-file openings and local-definition disclaimers around one template,
- and no, do not rely on ad hoc file-by-file interpretation prose going forward.
