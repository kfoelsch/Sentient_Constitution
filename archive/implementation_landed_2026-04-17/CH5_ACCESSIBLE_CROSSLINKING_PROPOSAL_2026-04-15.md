# Chapter Five Accessible Cross-Linking Proposal

Purpose: propose a readable, low-noise, accessible way to cross-link definitions inside `core_05-05_definitions_a_independent.md` without turning the chapter into a wall of inline links.

This memo is not operative constitutional text. It is an implementation proposal for the constitutional definitions chapter.

## Core judgment

The best solution is:

1. promote each Chapter Five definition term to a real Markdown heading,
2. give each definition one consistent, optional cross-link block directly under the heading,
3. keep most links out of the O / E / C bullets unless the reference is legally necessary in the sentence itself,
4. use explicit link text that names the destination and the relationship, rather than dense parenthetical link clusters.

That approach improves four things at once:

- anchor reliability for human readers and tooling,
- heading navigation for screen-reader users,
- readability under pressure because the main O / E / C text stays cleaner,
- editability because every definition gets the same link location and syntax.

## Problem in the current chapter

The current file already has useful navigation aids, but they are uneven:

- some terms have collapsible `Trace` blocks,
- some terms rely mostly on inline "Read with" prose,
- many definitions are introduced by plain text labels rather than headings,
- related-definition references are often embedded inside dense evaluation sentences.

That creates three accessibility problems:

1. Links are harder to scan because they are mixed into doctrinal prose.
2. Term-level anchors are weaker because plain labels do not form a robust heading structure.
3. Screen-reader navigation is less effective because users cannot jump definition-by-definition through the chapter's term list as headings.

## Recommended pattern

### 1. Make every definition a heading

Use a consistent heading level for each term, for example:

```md
#### Accountability
```

or, if the surrounding chapter hierarchy requires it:

```md
##### Accountability
```

Requirements:

- one heading per canonical definition term,
- the visible heading text should be exactly the canonical term,
- avoid decorative punctuation in the heading unless the canonical term requires it,
- keep the heading stable so anchor links do not churn.

Why this matters:

- Markdown viewers generate stable in-page anchors from headings,
- screen readers can navigate by heading,
- cross-links can target a definition directly instead of landing nearby,
- future tools can audit links more reliably.

### 2. Replace ad hoc local link prose with one standard block

Directly under the term heading, use a collapsed block for navigation only:

```md
<details>
<summary><strong>Related Definitions and Sources</strong></summary>

- Read with: [Auditability](#auditability), [Contestability](#contestability)
- Principles: [3.2 Truth](core_00-01_principles.md#32-truth-epistemic-integrity-constraint)
- Owner layers: [Article XVII-A](core_constitution.md#article-xvii-a)

</details>
```

This should replace the current mixture of:

- standalone "Read with:" lines,
- inconsistent trace blocks,
- reference-heavy lead-ins before the O / E / C content.

Recommended labels inside the block:

- `Read with:` for closely related Chapter Five definitions,
- `Principles:` for Chapter One or principles-file anchors,
- `Owner layers:` for other constitutional chapters or designated companion owners,
- `See also:` only when neither of the above labels fits cleanly.

Hard rule:

- a Chapter Five `Read with:` line belongs inside that entry's local `Trace` / `<details>` block,
- if no trace block is present, do not add a standalone `Read with:` line in operative prose,
- anything outside the `Trace` block should be treated as operative definition text and therefore should not carry duplicate navigation-only metadata.
- this rule does **not** prohibit selective same-file cross-definition links in the O / E / C body where they improve legal precision or reader navigation.

If a definition has no useful navigation payload, omit the block entirely rather than forcing empty boilerplate.

### 3. Keep O / E / C bullets readable

Use cross-links in the O / E / C bullets only when they are doing real legal work in the sentence.

Good use:

- a direct pointer to a controlling article,
- a reference needed to define admission scope,
- a cross-link whose absence would make the sentence ambiguous.

Avoid:

- linking every capitalized term,
- linking repeated occurrences of the same term inside one definition,
- stacking multiple parenthetical links inside already dense evaluation prose.

Rule of thumb:

- the first necessary mention may be linked,
- later mentions in the same definition should usually remain plain text,
- the cross-link block should carry the navigation burden for `Read with:` / principles / owner-layer metadata,
- the operative body may still include selective same-file cross-definition links where the sentence itself is doing doctrinal work.

### 4. Prefer explicit relationship text over bare links

Accessibility improves when the link context is spoken clearly.

Prefer:

- `Read with: [Transparency](#transparency)`
- `Principles: [4. System Stability Enabler: Trust](core_00-01_principles.md#4-system-stability-enabler-trust-coordination-integrity)`

Avoid:

- a naked list of linked terms with no relationship label,
- generic labels like `here`,
- color-dependent cues such as "blue trace items" or "highlighted links."

### 5. Add a lightweight term navigator near the chapter start

Add a short, non-operative navigation section near the start of Chapter Five:

```md
### Definition navigator (non-operative)

- Accountability
- Adjudication and Dispute Resolution (Constitutional)
- Authority Stack (Constitutional)
- ...
```

Each item should link to the term heading.

This is optional for every term in the final chapter, but strongly recommended because the file is long and users may need to jump directly to a term without searching the page.

If the list becomes too long, split it by local clusters such as:

- governance and review,
- agency and participation,
- environment and planetary conditions,
- information, trust, and verification.

That is usually more readable than one giant alphabetical block.

## Recommended standard template

Use this pattern for Chapter Five entries that need cross-links:

```md
#### Epistemic Integrity

<details>
<summary><strong>Related Definitions and Sources</strong></summary>

- Principles: [3.2 Truth](core_00-01_principles.md#32-truth-epistemic-integrity-constraint), [4. System Stability Enabler: Trust](core_00-01_principles.md#4-system-stability-enabler-trust-coordination-integrity)
- Read with: [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Transparency](#transparency), [Auditability](#auditability), [Verifiability](#verifiability)
- Owner layers: [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)

</details>

- O: ...
- E: ...
- C: ...
```

Benefits of this template:

- the heading creates the anchor,
- the summary text tells screen-reader and keyboard users what the block is for,
- the relationship labels explain why each destination matters,
- the O / E / C content remains visually and cognitively distinct from navigation help.

## Why this is better than the current `Trace` label by itself

The existing collapsed `Trace` pattern is directionally good, but `Trace` alone is not very descriptive for many readers and assistive technologies.

`Related Definitions and Sources` is better because it tells the user:

- this is navigation help,
- it links both related definitions and upstream authorities,
- opening it is optional and not part of the binding O / E / C text.

If maintaining the shorter `Trace` label is important for corpus consistency, a middle path is:

```md
<summary><strong>Trace: Related Definitions and Sources</strong></summary>
```

That preserves continuity while making the label self-explanatory.

## Accessibility-specific guidance

### Do

- use real headings for terms,
- use descriptive summary text for collapsed blocks,
- keep link text meaningful out of context,
- place the navigation block before O / E / C bullets,
- keep link order predictable across entries.

### Do not

- rely on color alone to signal cross-reference value,
- bury all related-definition links deep inside long paragraphs,
- use symbol-only backlink markers like `^`, `<<`, or `↩`,
- create huge repeated link lists for every term,
- mix operative and non-operative material in the same unlabeled block.
- place a duplicate `Read with:` line below the closing `</details>` tag.

## Rollout recommendation

Use a three-step rollout.

### Phase 1: structural accessibility pass

- convert all Chapter Five term labels to headings,
- keep existing text unchanged where possible,
- preserve existing `<details>` content but move it under the new heading,
- upgrade summary text from `Trace` to `Trace: Related Definitions and Sources` or directly to `Related Definitions and Sources`.

This phase yields the biggest accessibility gain with the least doctrinal churn.

### Phase 2: normalize high-value cross-links

- identify the most reused definition relationships,
- move repeated "Read with" guidance out of O / E / C prose and into the standard block,
- reduce duplicated inline link clusters.
- enforce the placement rule with a machine check so `Read with:` lines cannot silently escape the `Trace` block.

### Phase 3: add chapter navigator

- add a short linked term navigator near the chapter opening,
- group entries by reader task if the list is too long.

## Practical decision rule

Use the standard block only where it earns its keep.

Add the block when:

- the term is frequently cross-read with other Chapter Five definitions,
- the term depends on upstream principles or owner layers that readers repeatedly need,
- the O / E / C bullets are already dense enough that extra inline links would hurt readability.

Skip the block when:

- the definition is self-contained,
- there are no especially important cross-links beyond one necessary inline citation.

## Bottom line

For readable and accessible cross-linking between definitions, the chapter should stop treating term names as plain labels and start treating them as navigable headings.

Then each term should get one small, consistent, collapsed navigation block for related definitions and sources, leaving the substantive O / E / C text clearer and easier to read.

That is the highest-value, lowest-risk improvement for Chapter Five cross-linking.
