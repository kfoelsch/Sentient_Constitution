# Companion corpus reformation — publication cut

Date: 2026-08-09. Edition: `SC-Corpus-2026.06.18` → `SC-Corpus-2026.08.09`.
Scope: the four implementation corpora — `corpus_joint_structure/`,
`corpus_systems/`, `corpus_institutions/`, `corpus_forum/` (70 files).

The companion files had drifted into two opposite failure modes, neither
resembling the `core_*` files they implement. CF, CI, and CJS were buried in
navigation scaffolding that mostly restated itself; CS had almost no
scaffolding but also no structure. This cut puts all four onto one anatomy.

## Reader-facing outcome

| | Before | After |
|---|---|---|
| Files opening with an `#` H1 title | 5 of 70 | **70 of 70** |
| Files with a one-line statement of what they govern | 0 | 61 |
| `*In plain terms:*` glosses, CF | 5 | **108** |
| `*In plain terms:*` glosses, all four layers | 212 | **453** |
| Sections with no gloss before their operative text | many | **0** |
| Lines inside collapsed widgets, CF | 56.7% | **32.1%** |
| Lines inside collapsed widgets, CI | 40.7% | 34.6% |

The scaffolding share fell less than the raw prune suggests, because Phase 2
added a file-top **Corpus placement** widget to every file. That trade is
deliberate: a reader gains a consistent orientation block and loses 251
self-referential `Downstream:` lines, 107 self-citing `Read with:` lines, and
266 `Upstream:` lines duplicated verbatim from the file-level Trace.

## Readability

Flesch-Kincaid grade via `tools/readability_audit.py`, measured against HEAD:

| Layer | Files | Median before | Median after | Over grade 14 | Worsened |
|---|---|---|---|---|---|
| `corpus_joint_structure` | 12 | 16.88 | **15.57** | 9 → 9 | 0 |
| `corpus_systems` | 15 | 16.30 | **15.10** | 15 → 13 | 0 |
| `corpus_institutions` | 27 | 16.97 | **15.57** | 27 → 26 | 0 |
| `corpus_forum` | 16 | 18.20 | **15.92** | 16 → 15 | 0 |

Not one file of the 70 got harder to read. The worst file in the corpus,
`cs_protocol_b` — the protocol on comprehensibility, at grade 22.02 — now
reads at **12.93**, under the repo ceiling.

Most files remain above grade 14. The remaining distance is in the operative
sentences themselves, which are dense because the obligations are; closing it
further means more of the Phase 4 rewrite work, gated the same way.

## Meaning preservation

Operative wording changed only in Phases 4 and 5, and each tranche was gated on
`tools/obligation_inventory_diff.py`, which extracts every normative clause
with its modality and content terms, then requires coverage in both directions:
nothing dropped or weakened, nothing invented.

Per-tranche artifacts in this directory:

- `obligation_inventory_diff.json` — Phase 4 tranche 1
- `obligation_inventory_diff_t2.json` — Phase 4 tranche 2
- `obligation_inventory_diff_p5.json` — Phase 5, with `cs_structure_phase5_2026-08-09.md` documenting the single residual flag and the word-level proof behind it

## Regression

`make regression-full` fails 11 targets; HEAD fails 13. The two now passing are
`companion-anatomy-audit` and `file-top-placement-audit-companions`, both added
in Phase 0 to enforce the new anatomy.

Every still-failing target was diffed finding-by-finding against HEAD. No new
finding appears in any of them; differences are line numbers and quoted context
shifting where text moved. All the failures predate this work.

Passing gates directly relevant to this change: `router-bidirectional-audit`,
`trace-dac-widget-order-audit`, `nav-widget-spacer-audit`,
`file-top-placement-audit`, `companion-anatomy-audit`,
`doc-architecture-section-audit`, `cjs-operational-cluster-audit`.

`make router-bidirectional-sync` and `make architecture-index` were re-run for
the cut; the stable-ID index, router reader index, definition hierarchy, and
measurement rollout status are regenerated.

## No renames

No file was renamed, moved, split, or merged. Heading promotions preserve
markdown slugs, which derive from heading text rather than depth, and the new
`<a id="...">` anchors reproduce the slug the renderer already generated. Every
inbound reference that resolved before this cut still resolves.

The anatomy is documented as **NAV-IMPL-SUBFILE-01** in
[`doc_architecture.md`](../../doc_architecture.md) so it is enforced rather than
merely present.
