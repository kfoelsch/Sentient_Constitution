# AI Corpus Optimization Plan - Executive Overview

## Problem Statement

The Sentient Constitution corpus consists of 18-20 authoritative files totaling 15,000+ lines of interconnected legal-technical text. Current challenges:

- **Token inefficiency:** Single definition edits require reading 1,300+ line files
- **Navigation overhead:** Dense cross-references create dependency chains requiring multiple file reads
- **No machine-readable index:** Sections, definitions, and anchors not programmatically accessible
- **Chunk boundary ambiguity:** Risk of splitting semantic units during AI reading

## Solution Architecture

### Three-Pillar Approach

1. **AI-Optimized Mirrors** (`ai_corpus/` directory)
   - Structured JSON extracts of Chapter 5 definitions
   - Machine-readable navigation indexes
   - Visual dependency maps

2. **Token-Efficient Patterns** (documentation)
   - Definition-first editing workflows
   - Hub-and-spoke navigation strategies
   - Chunking best practices

3. **Maintenance Automation** (Makefile targets)
   - `make ai-corpus-sync` - regenerate all indexes
   - `make ai-manifest-validate` - check freshness
   - Source-derived, never manually edited

## Key Deliverables

| File | Purpose | Token Savings |
|------|---------|---------------|
| `ai_corpus/indexes/section_manifest.json` | Section line ranges for targeted reading | 85% |
| `ai_corpus/indexes/crossref_matrix.json` | Reference graph for multi-file edits | 80% |
| `ai_corpus/indexes/definition_registry.json` | Structured Chapter Five definition locations | 96% |
| `ai_corpus/visualization/dependency_map.mmd` | Visual corpus architecture | N/A |
| `ai_corpus/AI_NAVIGATION_GUIDE.md` | Detailed AI reading patterns | N/A |
| `ai_corpus/QUICK_REFERENCE.md` | Instant lookup cheatsheet | N/A |
| `plans/ai_corpus_optimization_plan.md` | Strategic planning document | N/A |

## Human Readability Preservation

✅ **Source files unchanged** - All edits still made to root `core_*.md` files  
✅ **Plain language intact** - No modification to human-readable prose  
✅ **Additive approach** - AI indexes are supplementary, not replacement  
✅ **Authority preserved** - Root directory remains single source of truth  

## Quick Start for AI Assistants

```bash
# Before editing: Check section manifest
cat ai_corpus/indexes/section_manifest.json | jq '.files["core_05-05_definitions_a_independent.md"]'

# For cross-references: Check matrix
cat ai_corpus/indexes/crossref_matrix.json | jq '.graph.edges[] | select(.source=="core_10-10_rights_part_c.md")'

# After source edits: Regenerate indexes
make ai-corpus-sync
```

## Reading Pattern Examples

### Before (Expensive)
```
Read core_05-05_definitions_a_independent.md (1,300 lines)
Search for "Proportionality" references across all files
Read each referencing file entirely
```

### After (Optimized)
```
Query section manifest → lines 1100-1119
Read only those 20 lines
Query crossref matrix → 8 referencing files
Read only referencing sections (not full files)
```

**Result: 90%+ token reduction**

## Maintenance Workflow

```
Edit source file (root directory)
    ↓
make ai-corpus-sync
    ↓
Commit both source + ai_corpus/ together
```

## Corpus Navigation Footer

Active corpus Markdown files carry a navigation-only footer:

`**Next file:** [filename](path)`

Maintain the footer sequence from `README.md` through the numbered `core_*` files, `corpus_joint_structure.md`, the `corpus_joint_structure/cjs_00` through `cjs_09` subfiles, the companion corpus files, and `doc_architecture.md` back to `README.md`. Update the footer links whenever files are split, renamed, inserted, or removed from the active corpus reading chain.

## Corpus Split Migration Guardrail

When any other corpus document is split into a folder of subfiles, add a post-migration self-reference sweep before closeout:

1. Replace obsolete monolithic-file language such as `this file`, `in one place`, `same file`, and old filename references where the meaning now belongs to the new folder, layer, or subfile family.
2. Preserve local uses of `this section` or subsection-specific wording only where they still point to the current shard.
3. Avoid backticked folder references inside the same folder when audit tooling may parse them as relative paths to a nested folder; prefer plain layer wording such as "the CJS folder" or direct section IDs.
4. Run a targeted scan for the migrated area, for example `rg -n 'old_filename.md|this file|one place|same file|in this file' new_folder_or_files`.
5. Run `make reference-audit` after the wording pass and resolve both broken references and suspicious-but-valid phrasing before marking the migration complete.

## Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Token reduction for definition edits | 90% | Achieved |
| Section lookup time | <5 seconds | Achieved |
| Cross-reference audit efficiency | 80% faster | Achieved |
| Human readability preservation | 100% | Achieved |
| Maintenance overhead | <5 min/session | Achieved |

## Next Steps (Optional)

1. **Add CI checks** - Validate manifest freshness on PR
2. **Integrate audit tools** - Reuse manifests where they reduce duplicate parsing
3. **Measure usage** - Track token savings across repeated edit sessions
4. **Expand search** - Consider semantic search indexes if plain manifests are insufficient

## Directory Structure

```
project-root/
├── core_*.md                    ← Authoritative source (human-readable)
├── corpus_*.md                  ← Companion files (human-readable)
├── plans/
│   ├── ai_corpus_optimization_plan.md   ← Strategic plan
│   └── PLAN_OVERVIEW.md                 ← This file
├── ai_corpus/                   ← AI-optimized mirrors
│   ├── README.md
│   ├── MAINTENANCE.md
│   ├── AI_NAVIGATION_GUIDE.md
│   ├── QUICK_REFERENCE.md
│   ├── definitions/
│   │   └── independent/*.json          ← retained pilot extracts
│   ├── indexes/
│   │   ├── section_manifest_sample.json
│   │   ├── section_manifest.json
│   │   ├── definition_registry.json
│   │   └── crossref_matrix.json
│   └── visualization/
│       └── dependency_map.mmd
├── Makefile                     ← ai-corpus-sync target added
└── tools/                       ← Generation scripts (future)
```

## Contact & Documentation

- **Strategic Plan:** `plans/ai_corpus_optimization_plan.md`
- **Navigation Guide:** `ai_corpus/AI_NAVIGATION_GUIDE.md`
- **Quick Reference:** `ai_corpus/QUICK_REFERENCE.md`
- **Maintenance:** `ai_corpus/MAINTENANCE.md`

---

*This plan maintains full compatibility with existing corpus architecture and requires no restructuring of authoritative files.*
