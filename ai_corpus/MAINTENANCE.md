# AI Corpus Maintenance Guide

## Overview

The `ai_corpus/` directory contains **derived indexes** generated from the authoritative source files. These indexes optimize AI lookup while preserving the human-readable source files. They **point**; they do not bind.

## Single Source of Truth

**NEVER EDIT FILES IN THIS DIRECTORY DIRECTLY.**

- **Authoritative source:** Root directory `core_*.md` and `corpus_*.md` files
- **Derived indexes:** This `ai_corpus/` directory
- **On conflict:** Root directory files always prevail

## Directory Structure

```
ai_corpus/
├── README.md
├── MAINTENANCE.md
├── AI_NAVIGATION_GUIDE.md
├── QUICK_REFERENCE.md
├── definitions/                   # Retired pilots; not a lookup path
├── indexes/
│   ├── id_resolver.json
│   ├── section_manifest.json
│   ├── definition_registry.json
│   ├── crossref_matrix.json
│   ├── section_crossref.json
│   └── section_manifest_sample.json
├── visualization/
│   └── dependency_map.mmd
└── schemas/
```

## Update Procedure

### After Editing Source Files

```bash
make ai-corpus-sync
git diff ai_corpus/
```

Commit source and derived files together. `make regression` includes `make ai-manifest-validate` so stale locators fail closed.

### Available Make Targets

```bash
make ai-manifest-generate
make ai-manifest-validate
make ai-corpus-sync
make id-resolver-test
make architecture-index          # also writes topic_router.json
make ai-corpus-help
```

## Regeneration Triggers

| Change Type | Affected Indexes | Action |
|-------------|------------------|--------|
| Add/remove section or family ID | id_resolver.json, section_manifest.json | Regenerate |
| Rename section | id_resolver.json, section_manifest.json, both crossref indexes | Regenerate |
| Add/remove definition | definition_registry.json, id_resolver.json | Regenerate |
| Add cross-reference | crossref_matrix.json, section_crossref.json | Regenerate |
| Rename file | All indexes | Regenerate |
| Line shifts | section_manifest.json, id_resolver.json | Regenerate |

## Human Readability Preservation

1. **Source files unchanged** — plain language mandate intact
2. **No structural changes** to authoritative files
3. **Additive only** — indexes are derived, not replacement
4. **Locators, not restatements** — no O/M/A/C or `must` clauses in JSON

## Troubleshooting

```bash
make ai-manifest-validate
make ai-corpus-sync
```

If `id_resolver.json` is missing an ID, fix the heading or family map in source, then regenerate.

## Schema Evolution

JSON schemas in `ai_corpus/schemas/` define generated index shape. When adding fields: update schema, update generator, regenerate, update this file.

## Retired artifacts

- `ai_corpus/definitions/*.json` — pilot extracts; the definition registry and id_resolver are the lookup path
- Do not restore per-definition JSON extracts as an authority path

## Contact

- `AI_NAVIGATION_GUIDE.md` — usage patterns
- `QUICK_REFERENCE.md` — quick lookup
- `plans/ai_corpus_optimization_plan.md` — original (now superseded in parts by the locator layer)
