# CF-3 filename rename — reference audit

**Date:** 2026-08-15  
**Gate:** [doc_architecture.md](../../doc_architecture.md) rename readiness (reference audit, same-change link updates, dated evidence, compatibility decision, edition/custody record).

## Change

| | |
|---|---|
| **Old filename** | `corpus_forum/cf_03_forum_formation_tribunal_mapping_chamber_structure.md` |
| **New filename** | `corpus_forum/cf_03_forum_formation_chamber_structure.md` |
| **Stable family ID** | **CF-3** (unchanged) |
| **Section anchors** | unchanged |

Reason: the old filename used `tribunal` in the institutional/adjudicative sense forbidden by the corpus vocabulary guardrails. The public family title remains *Forum formation, forum-structure mapping, and chamber structure*.

## Compatibility decision

No redirect stub file. **CF-3** is the public ID; inbound cites use the family ID plus the new path. Historical mentions of the old filename remain only under `archive/`.

## Edition / custody

No publication-cut edition bump. Registry annexes (`*_00`) now inherit edition metadata from [README.md](../../README.md) rather than stamping a second edition.

## Same-change link updates

Live corpus, tools, generated indexes, and family map were updated in the same change. Regenerators: `make family-map-indexes`, `python3 tools/emit_architecture_index.py`.

## Reference audit

Post-rename grep of the working tree excluding `archive/` found **no** remaining live references to `cf_03_forum_formation_tribunal_mapping_chamber_structure.md`.
