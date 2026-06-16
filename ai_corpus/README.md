# AI-Optimized Corpus Mirror

**Status:** Derived from SC-Corpus-2026.04.33  
**Source of Truth:** The numbered `core_*.md` files and incorporated companion corpus files remain authoritative. The root `corpus_joint_structure.md` file is a compatibility wrapper whose substantive text is in `corpus_joint_structure/` subfiles. This directory contains AI-optimized mirrors for token-efficient access.

## Purpose

This directory provides:
1. **Structured definition registry** for Chapter 5 terms
2. **Machine-readable indexes** for instant navigation
3. **Cross-reference graphs** for dependency analysis
4. **Semantic chunk boundaries** for optimal token usage

## Authority Stack

1. **Authoritative:** Numbered `core_*.md` files in root directory, companion root files, and companion subfiles such as `corpus_joint_structure/*.md`
2. **Derived (this directory):** AI-optimized mirrors and indexes
3. **On conflict:** Root directory files always prevail

## Directory Structure

```
ai_corpus/
├── README.md                    # This file
├── definitions/                 # Retained pilot definition extracts
│   └── independent/            # Sample extracts from Chapter 5 §1
├── indexes/                     # Navigation indexes
│   ├── section_manifest.json   # All sections with line ranges
│   ├── definition_registry.json # Definition locations and metadata
│   └── crossref_matrix.json    # File-to-file reference graph
└── schemas/                     # JSON schemas for validation
    ├── section_manifest.schema.json
    ├── definition_registry.schema.json
    └── crossref_matrix.schema.json
```

## Update Procedure

When source files change:

1. Edit authoritative source files (`core_*.md`, companion root files, or companion subfiles)
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
