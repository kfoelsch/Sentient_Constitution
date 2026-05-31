# AI Corpus Maintenance Guide

## Overview

The `ai_corpus/` directory contains **derived indexes** that are automatically generated from the authoritative source files in the root directory. These indexes optimize AI token efficiency while preserving the human-readable source files.

## Single Source of Truth

**NEVER EDIT FILES IN THIS DIRECTORY DIRECTLY.**

- **Authoritative source:** Root directory `core_*.md` and `corpus_*.md` files
- **Derived indexes:** This `ai_corpus/` directory
- **On conflict:** Root directory files always prevail

## Directory Structure

```
ai_corpus/
├── README.md                      # Overview and usage
├── MAINTENANCE.md                 # This file
├── AI_NAVIGATION_GUIDE.md         # Detailed navigation patterns
├── QUICK_REFERENCE.md             # Quick lookup cheatsheet
├── definitions/                   # Retained pilot extracts
│   └── independent/              # Sample Chapter 5 §1 extracts
├── indexes/                       # Navigation indexes
│   ├── section_manifest.json
│   ├── definition_registry.json
│   ├── crossref_matrix.json
│   └── section_manifest_sample.json
├── visualization/                 # Visual aids
│   └── dependency_map.mmd        # Mermaid dependency diagram
└── schemas/                       # JSON schemas for generated indexes
    ├── section_manifest.schema.json
    ├── definition_registry.schema.json
    └── crossref_matrix.schema.json
```

## Update Procedure

### After Editing Source Files

When you modify any `core_*.md` or `corpus_*.md` file in the root directory:

```bash
# Step 1: Edit the authoritative source file
# (e.g., edit core_05-05_definitions_a_independent.md)

# Step 2: Regenerate all AI corpus indexes
make ai-corpus-sync

# Step 3: Review changes
git diff ai_corpus/

# Step 4: Commit both source and derived files together
git add core_05-05_definitions_a_independent.md ai_corpus/
git commit -m "Update Proportionality definition + regenerate AI indexes"
```

### After Splitting a Corpus File

When a corpus file is migrated into a folder of subfiles, add this migration-specific pass before closeout:

```bash
# Replace old_filename.md and stale "this file" language after the split
rg -n 'old_filename.md|this file|in this file|same file|one place' new_folder_or_files

# Confirm cross-references still resolve
make reference-audit
```

Rewrite any stale monolithic wording so folder-level duties refer to the new folder, layer, subfile family, or direct section IDs. Keep `this section` only when the reference remains local to the current shard. Avoid backticked same-folder directory references when prose wording is enough, because path-aware audits may treat them as links to nonexistent nested folders.

### Available Make Targets

```bash
# Generate all manifests (section, definition, crossref)
make ai-manifest-generate

# Validate manifests are up-to-date
make ai-manifest-validate

# Force regeneration (use with caution)
make ai-manifest-regenerate

# Sync ai_corpus with source (alias)
make ai-corpus-sync

# Show help
make ai-corpus-help
```

## Regeneration Triggers

| Change Type | Affected Indexes | Action |
|-------------|------------------|--------|
| Add/remove section | section_manifest.json | Regenerate |
| Rename section | section_manifest.json, crossref_matrix.json | Regenerate |
| Add/remove definition | definition_registry.json, section_manifest.json | Regenerate |
| Edit definition text | definition extract JSON files | Regenerate |
| Add cross-reference | crossref_matrix.json | Regenerate |
| Rename file | All indexes | Regenerate |
| Line shifts >10 lines | section_manifest.json | Regenerate |

## Human Readability Preservation

The AI corpus optimization **preserves** the corpus's human readability:

1. **Source files unchanged** - Plain language mandate intact
2. **No structural changes** to authoritative files
3. **Additive only** - Indexes are derived, not replacement
4. **Human-first design** - AI indexes are supplementary

## Token Efficiency Gains

| Operation | Before | After | Savings |
|-----------|--------|-------|---------|
| Definition lookup | 1,300 lines | 50 lines | 96% |
| Cross-reference audit | All files | Targeted sections | 80% |
| Section edit | Full chapter | Section only | 85% |

## Troubleshooting

### Manifests Out of Date

```bash
# Check if manifests need regeneration
make ai-manifest-validate

# If outdated, regenerate
make ai-corpus-sync
```

### Line Number Mismatch

If `section_manifest.json` line numbers don't match current files:

```bash
# Force regeneration
make ai-manifest-regenerate
```

### Cross-Reference Errors

If `crossref_matrix.json` shows broken references:

1. Check the source file for correct anchor IDs
2. Fix in source file (root directory)
3. Regenerate: `make ai-corpus-sync`

## Schema Evolution

JSON schemas in `ai_corpus/schemas/` define the structure of derived files. When adding new fields:

1. Update schema files first
2. Update generation tools
3. Regenerate all indexes
4. Update documentation

## Future Enhancements

Potential future additions to ai_corpus/:

- Semantic search index
- Definition dependency graph
- Automated consistency checker

## Contact

For questions about AI corpus optimization, refer to:
- `plans/ai_corpus_optimization_plan.md` - Strategic plan
- `AI_NAVIGATION_GUIDE.md` - Usage patterns
- `QUICK_REFERENCE.md` - Quick lookup
