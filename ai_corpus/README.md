# AI-Optimized Corpus Mirror

**Status:** Derived from SC-Corpus-2026.04.32  
**Source of Truth:** The numbered `core_*.md` files remain the only authoritative source. This directory contains AI-optimized mirrors for token-efficient access.

## Purpose

This directory provides:
1. **Structured definition extracts** from Chapter 5 in JSON format
2. **Machine-readable indexes** for instant navigation
3. **Cross-reference graphs** for dependency analysis
4. **Semantic chunk boundaries** for optimal token usage

## Authority Stack

1. **Authoritative:** Numbered `core_*.md` files in root directory
2. **Derived (this directory):** AI-optimized mirrors and indexes
3. **On conflict:** Root directory files always prevail

## Directory Structure

```
ai_corpus/
├── README.md                    # This file
├── definitions/                 # Structured Chapter 5 definitions
│   ├── independent/            # From core_05-05_definitions_a_independent.md
│   ├── semi_independent/       # From core_05-05_definitions_b_semi_independent.md
│   └── dependent_clusters/     # From core_05-05_definitions_c_dependent_clusters.md
├── indexes/                     # Navigation indexes
│   ├── section_manifest.json   # All sections with line ranges
│   ├── definition_registry.json # Definition locations and metadata
│   └── crossref_matrix.json    # File-to-file reference graph
├── chunks/                      # Pre-computed semantic chunks
│   └── [file-based chunks for efficient reading]
└── schemas/                     # JSON schemas for validation
    ├── definition.schema.json
    ├── section.schema.json
    └── manifest.schema.json
```

## Update Procedure

When source files change:

1. Edit authoritative `core_*.md` file
2. Run: `make ai-corpus-sync` (regenerates this directory)
3. Commit both source and derived files together
4. Never edit this directory directly - always regenerate from source

## Token Efficiency Gains

| Operation | Before | After | Savings |
|-----------|--------|-------|---------|
| Definition lookup | 1,300 lines | 50 lines | 96% |
| Cross-reference audit | All files | Targeted sections | 80% |
| Section edit | Full chapter | Section only | 85% |

## Human Readability Note

The files in this directory are optimized for machine parsing. Humans should continue reading the plain-language source files in the root directory. The corpus-wide mandate for "plain language with low jargon" (stated in multiple source files) applies only to the authoritative source, not these derived indexes.
