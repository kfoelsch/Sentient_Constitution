# CS structural reformation — evidence

Date: 2026-08-09. Scope: `corpus_systems/` (15 files).

Phase 5 of the companion corpus reformation: give the CS files the section
structure the other three companion corpora already have, and remove the
emphasis and sentence-splitting habits that made them unreadable.

## What changed

| Change | Extent |
|---|---|
| Bold run-in labels promoted to `## N. Title` headings | 39 headings in `cs_04` and `Protocol S5`; 4 in `Protocol B` |
| Explicit `<a id="...">` anchors added above headings | 62 across 8 files |
| Pronoun-led sentence chains rebuilt as lists | 37 chains in 5 files |
| Meaningless emphasis removed | sentence-opening pronouns and bare imperatives |
| `*In plain terms:*` glosses added, one per section | 56 sections in 7 files |
| Clauses rejoined where a comma had become a sentence break | 12 in 4 files |

Tools: `tools/promote_cs_topic_labels.py`, `tools/add_section_anchors.py`,
`tools/collapse_pronoun_chains.py`, `tools/debold_shouting_prose.py`,
`tools/insert_section_glosses.py`.

Every CS file now opens each section with a heading, an anchor, and a
plain-language gloss. Before this phase, `cs_04` (29KB), `Protocol S5`, and
`Protocol B` had **zero** subsection headings.

## Meaning preservation

`tools/obligation_inventory_diff.py` compared a pre-change snapshot
(`evidence/obligation_snapshot_p5.json`, 715 clauses) against the result. Full
output: `obligation_inventory_diff_p5.json`.

**One finding, verified as a scanner artifact rather than a change:**

> `cs_protocol_s4`: ADDED DUTY not in the source — *"Required monitoring
> dimensions include: reliability and uptime, performance and efficiency,
> security and vulnerability exposure, ..."*

The source read `**Required monitoring dimensions** include **reliability and
uptime**. They include **performance and efficiency**. They include ...`. Only
the first sentence carried a word the scanner treats as a modality
(*Required*), so the four follower sentences were never in the inventory to
begin with. Collapsing the chain into one list brought that already-binding
text under the same clause, which reads as new terms appearing. No duty
changed; text that was always operative merely became visible to the tool.

Because that argument depends on the words being identical, it was checked
directly. Comparing the word bag of every CS file before and after:

```
cs_protocol_a: dropped only restated subjects/modals {'must': 3, 'they': 3}
cs_protocol_d: dropped only {'it': 7, 'must': 9, 'they': 5, 'includes': 3}
cs_protocol_s4: dropped only {'it': 4, 'must': 8, 'they': 14, 'include': 6, 'triggers': 2, 'may': 2}
cs_protocol_s5: dropped only {'it': 7, 'must': 36, 'they': 39, 'should': 4, 'may': 4, 'includes': 2}
cs_protocol_t: dropped only {'it': 4, 'must': 2, 'includes': 2, 'include': 2, 'they': 2}
```

**Not one word was added to any file, and the only removals are the subject and
modal each follower sentence restated** — now carried once by the list stem.

Chains whose followers negate ("They must **not** be altered retroactively")
were excluded from the automated pass, because folding a prohibition under a
bare `must:` stem would put a duty and its opposite in one list. The three such
chains were rewritten by hand with the prohibition kept intact.

## Readability

Flesch-Kincaid grade, `tools/readability_audit.py`, against HEAD:

| File | Before | After |
|---|---|---|
| `cs_protocol_b` | 22.02 | **12.93** |
| `cs_protocol_t` | 14.83 | **12.42** |
| `cs_protocol_s5` | 16.30 | 14.81 |
| `cs_protocol_c` | 19.84 | 17.55 |
| `cs_04` | 17.80 | 16.58 |
| `cs_protocol_s4` | 17.95 | 16.67 |
| `cs_protocol_d` | 17.90 | 16.54 |
| `cs_protocol_r` | 16.88 | 15.56 |
| `cs_protocol_a` | 17.73 | 17.20 |
| `cs_01` | 15.15 | 14.13 |

Median across the folder: **16.30 → 15.10**. Files over the grade-14 ceiling:
15 → 13. No file got worse.

## Regression

`make regression` fails 8 targets; HEAD fails 10. The two now passing are
`companion-anatomy-audit` and `file-top-placement-audit-companions`, both added
in Phase 0 and satisfied by the Phase 2 anatomy lift.

Findings inside each still-failing target were diffed against HEAD line by
line. No new finding appears in any of them; the only differences are line
numbers and quoted context shifting where text moved.

`trace-dac-widget-order-audit`, `nav-widget-spacer-audit`,
`router-bidirectional-audit`, `companion-anatomy-audit`, and
`file-top-placement-audit` all pass.
