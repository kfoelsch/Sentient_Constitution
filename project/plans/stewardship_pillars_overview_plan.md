# Stewardship pillars overview plan

**Status:** implemented in `CONCEPTUAL_OVERVIEW.md` (subsection *Stewardship: three pillars*). Open decisions 1 and 2 remain open.  
**Edition consulted:** `SC-Corpus-2026.08.09` (pre-release).  
**Scope:** reader-oriented conceptual support in `CONCEPTUAL_OVERVIEW.md`. It adds no definitions or duties, creates no pillar taxonomy of its own, and cannot narrow `core_01_c_stewardship_capacity_principles.md`.

## Assessment: does the pillar chart belong in the overview?

Yes. Four reasons, in order of weight:

1. **The overview names stewardship as a Chapter One guardrail but never shows it.** The guardrail list carries one bullet — *"**Stewardship** is shared by human and AI actors; neither gets a special exemption from the same duties."* That is §10.1 alone. The three-pillar architecture that organizes the whole of §9 does not appear anywhere in the overview.
2. **The reader meets governance without its frame.** The overview has a *Governance* section and a *Segregation of duties* section. Chapter One §11 is titled *Governance Under Stewardship Discipline*, and at principle layer stewardship discipline controls where the two conflict. A reader arrives at governance in the overview having never been shown the discipline it sits under.
3. **The chart's sink node is already in the overview.** The §9 chart terminates in the Constitutional Tetrad, which the overview establishes in *Two aims and the Constitutional Tetrad*. The pillar chart is the natural next step from that section: here are the four legs, and here is how stewardship carries three of them.
4. **It resolves a live ambiguity.** Every occurrence of "material stewardship" in the overview today is the Chapter Six Article II sense — durable goods, lifecycle honesty, repair. A reader of the overview alone would reasonably conclude that stewardship *is* product lifecycle integrity. A Chapter One stewardship subsection, with one distinguishing sentence, closes that gap.

**But not as a copy.** The §9 chart is written for a reader already inside Chapter One and should be adapted, not duplicated — see *Design decisions* below.

## Direction of reproduction

The corpus already has a convention for shared diagrams, and it runs in the opposite direction from what "copy it there" implies:

- `core_01_a_values_principles.md` reproduces the Tetrad chart and closes with *"Reproduced from the [Conceptual Overview](CONCEPTUAL_OVERVIEW.md#two-aims-and-the-constitutional-tetrad)."*
- `core_01_b_interaction_interpretation.md` uses the same pattern for the definitions chart.

Those are cross-cutting maps that span the instrument, so the overview is their natural canonical home. The pillar chart is different: it is Chapter One §9's own taxonomy, and §9 is its source. So this plan inverts the pointer and uses the overview's *own* native pattern instead — the Tetrad subsection already says *"Their source is the [Preamble's Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad)."*

**Decision:** the overview version carries a source pointer to §9. `core_01_c` is left unchanged. A reciprocal pointer in §9 is optional and listed under *Open decisions*.

## Design decisions

1. **Placement.** New `###` subsection between *Two aims and the Constitutional Tetrad* and *Rights Floor*, inside *Principles, articles, and definitions*. Anchor `<a id="stewardship-pillars"></a>`, heading `### Stewardship: three pillars`, preceded by the house `<hr>` rule. This keeps Chapter One material together before Chapter Six and places the chart immediately after the Tetrad it feeds.
2. **Drop chapter-local navigation from node labels.** The §9 chart puts "§10", "§9.1" and "§9.2" inside nodes. No diagram in the overview carries section numbers in a node — the overview uses concept names and Article numbers. Section links move to the prose beneath the chart.
3. **Parallel edges, not a chain.** The §9 chart wires `P1 --> P2 --> P3a --> TETRAD` with `P2 --> P3b --> TETRAD`, which reads as a causal sequence: Pillar 1 produces Pillar 2 produces Pillar 3. §9's own prose says the opposite — *"Together, all three pillars carry the Constitutional Tetrad participation, oversight, and timeliness legs."* The overview version runs all three pillars into the Tetrad in parallel. (This also suggests a possible correction in §9 itself; see *Open decisions*.)
4. **Respect the overview's colour vocabulary.** The overview binds colours to concepts: green `#16a34a` for the aims, teal `#0f766e` Participation, orange `#ea580c` Oversight, pink `#db2777` Accountability, purple `#9333ea` Timeliness, blue `#2563eb` structural. The §9 chart uses green for Pillar 1 and teal for Pillar 3, which would collide with that mapping. The overview version puts all three pillars on a neutral slate `#64748b` and the Tetrad sink on structural blue `#2563eb`.
5. **Two senses of "stewardship" distinguished.** One short paragraph separates Chapter One stewardship (who runs shared systems, and to what standard) from Article II Material Stewardship (how durable goods are made, described, and supported).

## Proposed content

Insert after the Tetrad subsection's closing prose and before `<a id="rights-floor"></a>`:

````markdown
<a id="stewardship-pillars"></a>
### Stewardship: three pillars

<hr style="border: 0; border-top: 1px solid currentColor;">

```mermaid
flowchart TB
    subgraph Pillars["Stewardship · three pillars"]
        direction LR
        P1["Sentient organization<br/><br/>• Hands-on operation, maintenance, oversight, and improvement<br/>• Records and review pathways others can verify and challenge<br/>• Not a sealed-off priesthood of specialists"]
        P2["Staying ahead of problems<br/><br/>• Notice trouble while it is still small<br/>• Escalate on a clock sized to the role's stakes<br/>• Close problems out, not merely flag them"]
        P3["Competence at scale<br/><br/>• Understanding and challenge workable for affected communities<br/>• Institutions that keep learning through feedback and correction"]
    end
    TETRAD["Constitutional Tetrad<br/><br/>• Participation, oversight, and timeliness legs<br/>• Scaled to material stake"]
    P1 --> TETRAD
    P2 --> TETRAD
    P3 --> TETRAD
    style Pillars fill:none,stroke:none
    style P1 fill:none,stroke:#64748b,color:#ffffff
    style P2 fill:none,stroke:#64748b,color:#ffffff
    style P3 fill:none,stroke:#64748b,color:#ffffff
    style TETRAD fill:none,stroke:#2563eb,color:#ffffff
```

The Tetrad says which duties keep a shared system legitimate. Stewardship is how those duties get carried by the people and institutions actually running it. All three pillars work together rather than in sequence, and each is bounded by Safety, Truth, Necessity, Proportionality, Avoidable Burden, and Epistemic Integrity — they operate within those constraints, not around them.

Their source is [§9 Stewardship In Depth](core_01_c_stewardship_capacity_principles.md#9-stewardship-in-depth). The steward role itself — the hands-on duties, the shared standard binding human and AI stewards alike, symmetric costly constraints, and role-scoped observability — lives at [§10 Consequential Stewardship: The Steward Role](core_01_c_stewardship_capacity_principles.md#10-consequential-stewardship). The community and institutional facets of the third pillar are [§9.1 Distributed Understanding](core_01_c_stewardship_capacity_principles.md#91-distributed-understanding) and [§9.2 Institutional Development](core_01_c_stewardship_capacity_principles.md#92-institutional-development).

This is a different sense of the word from [Article II: Material Stewardship and Durable-Use Integrity](core_06_rights_part_a.md#article-ii-material-stewardship-and-durable-use-integrity). Chapter One stewardship is about who operates shared systems and to what standard; Article II is a Rights Floor about how durable and network-dependent products are designed, described, and supported.
````

## Companion edits

- Link the existing guardrail bullet — *"**Stewardship** is shared by human and AI actors…"* — to the new `#stewardship-pillars` anchor, so the overview's opening list reaches the new subsection.
- No change to the seven-question list: question 2 already routes to *Principles, articles, and definitions*, which now contains this subsection.

## Acceptance criteria

- The subsection states no duty and introduces no pillar language absent from §9.
- Every pillar and both role sections resolve to a binding source anchor in `core_01_c`.
- The chart implies no sequence among the pillars and no precedence over the Tetrad.
- Chapter One stewardship and Article II Material Stewardship are distinguishable from the overview alone.
- Node colours preserve the overview's existing colour-to-concept mapping; no pillar borrows the Participation or aims colour.
- `core_01_c_stewardship_capacity_principles.md` is unchanged by this plan.

## Validation

No tool in `tools/` covers `CONCEPTUAL_OVERVIEW.md`, so there is no fixture to update — and no automated guard against drift, which is why the source pointer in the prose matters. Run against changed files:

```bash
make reference-audit
make corpus-markdown-audit
make local-markdown-fragment-audit
make in-paragraph-link-audit
make pages-site-check
```

Then confirm the Mermaid block renders and every link resolves.

## Open decisions

1. **Reciprocal pointer in §9.** Add *"Also shown in the [Conceptual Overview](CONCEPTUAL_OVERVIEW.md#stewardship-pillars)."* beneath the §9 chart? It aids navigation but creates a second place to maintain if the overview subsection is ever renamed.
2. **The §9 chain.** Should `P1 --> P2 --> P3a` in the §9 chart become parallel edges too, matching its own "together" prose? Handled as a separate change; this plan does not touch `core_01_c`.
3. **Pillar colours.** Neutral slate for all three is the conservative choice. The alternative is colouring each pillar with the Tetrad leg it most carries — participation teal, timeliness purple, oversight orange — which is more informative but asserts a one-to-one pillar-to-leg mapping that §9 does not make.
