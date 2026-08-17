# AI-Optimized Corpus Mirror

**Status:** Derived locators. Not binding.
**Source of Truth:** The numbered `core_*.md` files and incorporated companion corpus files remain authoritative. The root `corpus_joint_structure.md` file is a compatibility wrapper whose substantive text is in `corpus_joint_structure/` subfiles.

## Purpose

This directory provides machine-readable **locators** so an assistant can open the right source slice without a corpus-wide grep:

1. **ID resolver** for family/section IDs, CJS-0.1 topics, and Chapter Five terms
2. **Section manifest** for heading line ranges
3. **Cross-reference graphs** (file-to-file and section-to-section)
4. **Definition registry** for Chapter Five locations

Indexes **point**. They do not restate duties. On conflict, root source files always prevail.

## Authority Stack

1. **Authoritative:** Numbered `core_*.md` files, companion root files, and companion subfiles
2. **Derived (this directory):** AI locators and indexes
3. **On conflict:** Root directory files always prevail

## Directory Structure

```
ai_corpus/
├── README.md                    # This file
├── AI_NAVIGATION_GUIDE.md       # Reading patterns
├── QUICK_REFERENCE.md           # Lookup cheatsheet
├── MAINTENANCE.md               # Regeneration
├── definitions/                 # Retired pilots (do not use)
├── indexes/                     # Navigation indexes
│   ├── id_resolver.json        # Compact locator (start here)
│   ├── section_manifest.json   # Heading line ranges
│   ├── definition_registry.json
│   ├── crossref_matrix.json    # File-to-file
│   └── section_crossref.json   # Section-to-section
├── visualization/
│   └── dependency_map.mmd      # Generated file inventory
└── schemas/
```

## Update Procedure

When source files change:

1. Edit authoritative source files (`core_*.md`, companion root files, or companion subfiles)
2. Run: `make ai-corpus-sync` (regenerates this directory)
3. Commit both source and derived files together
4. Never edit this directory directly — always regenerate from source

## Human Readability Note

The files in this directory are optimized for machine parsing. Humans should continue reading the plain-language source files in the root directory. The corpus-wide mandate for "plain language with low jargon" applies only to the authoritative source, not these derived indexes.
