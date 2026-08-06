# AI Corpus Access Optimization Plan

**Edition:** SC-Corpus-2026.04.33  
**Objective:** Maximize easy AI access, minimize token usage during edits, preserve human readability  
**Status:** Migration complete for the required AI navigation layer; optional validation and measurement work remains ongoing

---

## Executive Summary

The active corpus scope includes the numbered core constitutional files, companion root files, and companion subfiles discovered by `tools/corpus_paths.py`, totaling 15,000+ lines of interconnected legal-technical text. Current challenges include:

- **File sizes range from 400 to 2,500+ lines**, making full-file context expensive
- **Dense cross-references** create dependency chains requiring multiple file reads
- **No machine-readable index** of sections, definitions, or anchor points
- **Inconsistent chunk boundaries** can split semantic units

This plan established the token-efficient AI navigation layer while maintaining the corpus's human accessibility and architectural integrity. The live migration now consists of source-derived manifests, a Chapter Five definition registry, a cross-reference matrix, maintenance targets, validation tooling, and AI-facing navigation documentation.

### 2026-05-30 migration closeout

Required migration scope is complete:

- `ai_corpus/indexes/section_manifest.json` provides full-source section ranges for the active corpus scope.
- `ai_corpus/indexes/definition_registry.json` indexes all Chapter Five O/M/A/C-owning definitions.
- `ai_corpus/indexes/crossref_matrix.json` maps file-to-file Markdown references across the active corpus scope.
- `ai_corpus/visualization/dependency_map.mmd`, `ai_corpus/AI_NAVIGATION_GUIDE.md`, `ai_corpus/QUICK_REFERENCE.md`, and `ai_corpus/MAINTENANCE.md` document the workflow.
- `make ai-corpus-sync` regenerates the derived indexes.
- `make ai-manifest-validate` validates index shape and freshness against regenerated source-derived output.

The older per-definition JSON files under `ai_corpus/definitions/` are retained as pilot extracts, not the maintenance-critical index path. The generated definition registry is the authoritative AI lookup artifact for Chapter Five locations.

---

## 1. Current Corpus Architecture Analysis

### 1.1 File Inventory and Sizing

| File | Lines | Role | Primary Content |
|------|-------|------|-----------------|
| `core_00_preamble.md`, `core_01_a_values_principles.md`, and `core_01_b_stewardship_capacity_principles.md` | ~1,400 | Core | Preamble, Chapter 1 (values, constraints) |
| `core_02-03_definition_mechanics.md` | ~310 | Core | Chapters 2-3 (O/M/A/C structure, integrity) |
| `core_04-04_burden_traceability_verification.md` | ~340 | Core | Chapter 4 (burden, traceability, verification) |
| `core_05__definitions_home.md` | ~1,300 | Core | Chapter 5 §1 (independent definitions A-Z) |
| `core_05-05_definitions_b_semi_independent.md` | ~1,900 | Core | Chapter 5 §2 (semi-independent definitions) |
| `core_05-05_definitions_c_dependent_clusters.md` | ~1,800 | Core | Chapter 5 §3 (dependent clusters) |
| `core_08-08_standing_assessment.md` | ~880 | Core | Chapter 6 Part A (two-axis model) |
| `core_09-09_standing_integration.md` | ~780 | Core | Chapter 6 Part B (integration, effects) |
| `core_10_a_misconduct_designation.md` | ~420 | Core | Chapter 7 (anti-constitutional misconduct) |
| `core_11-11_forum.md` | ~380 | Core | Chapter 8 (forums, jurisdiction) |
| `core_06-06_rights_part_a.md` | ~630 | Core | Chapter 9 Part A (Articles I-IV) |
| `core_06-06_rights_part_b.md` | ~1,380 | Core | Chapter 9 Part B (Articles V-XI) |
| `core_06-06_rights_part_c.md` | ~1,600 | Core | Chapter 9 Part C (Articles XII-XXII) |
| `core_06-06_rights_part_d.md` | ~560 | Core | Chapter 9 Part D (Articles XXIII-XXV) |
| `core_12-12_governance.md` | ~330 | Core | Chapter 10 (constitutional contract) |
| `core_13-15_amendment.md` | ~640 | Core | Chapters 11-13 (non-regression, amendment) |
| `core_16-16_incorporation.md` | ~160 | Core | Chapter 14 (incorporation bridge) |
| `corpus_systems.md` | ~2,170 | Companion | Systems companion (CS-2–CS-4, Protocols A, B, S4, S5) |
| `corpus_institutions.md` | ~940 | Companion | Institutional governance (CI-1 to CI-26) |
| `corpus_forum.md` | ~1,150 | Companion | Forum operations |
| `corpus_joint_structure.md` | ~1,730 | Companion | Cross-domain implementation layer |

### 1.2 Cross-Reference Density Analysis

High-traffic cross-reference patterns:
- Chapter 5 definitions → referenced from all other chapters
- Chapter 2-4 mechanics → referenced from all definition-dependent content
- Chapter 9 Rights → referenced from corpus_systems.md and corpus_institutions.md
- corpus_systems.md Protocol A → referenced from Chapter 9 Article XVI-XVII

---

## 2. Token Optimization Strategies

### 2.1 Smart File Reading Patterns

**Pattern A: Definition-First Reading**
```
When editing content that uses defined terms:
1. Read the specific definition entry (O/M/A/C components) from Chapter 5
2. Read the referencing section from the target file
3. Only read surrounding context if ambiguity remains
```

**Pattern B: Hub-and-Spoke Navigation**
```
For Chapter 9 rights editing:
1. Read the specific Article from core_06-06_rights_part_*.md
2. Read doc_architecture.md section 2 for corpus role mapping
3. Read relevant implementation companion sections only if operational detail needed
```

**Pattern C: Minimal Viable Context**
```
For edits confined to a single semantic unit:
1. Read only the section header and content (not entire file)
2. Use indentation-mode reading to capture complete semantic blocks
3. Cross-reference only when semantic dependencies exist
```

### 2.2 Chunking Strategy

**Optimal chunk boundaries:**
- At `---` horizontal rules (major section breaks)
- Before `### ` or `#### ` headers (subsection starts)
- After definition entry completions (after C component)
- At `<details>` block boundaries

**Avoid splitting:**
- O/M/A/C component triplets within definitions
- Trace/DEFINITION/COMPLIANCE blocks
- Cross-reference lists mid-entry
- Table rows

### 2.3 Definition Entry Structure for AI Parsing

Each definition in Chapter 5 follows this pattern:
```markdown
#### Definition Name

[Trace block in <details>]

[DEFINITION block in <details> with O/M/A/C]

[COMPLIANCE block in <details>]

---
```

**AI reading optimization:** Read only the `#### ` header + `</details>` blocks for a definition, skipping prose interludes.

---

## 3. Implemented Artifacts for AI Navigation

### 3.1 Section-Level Manifest (`ai_corpus/indexes/section_manifest.json`)

Machine-readable index of every section with:
- File path
- Header hierarchy (H2, H3, H4)
- Line range (start, end)
- Nearby explicit anchor ID, where present

**Benefit:** AI can target specific line ranges without full file reads.

### 3.2 Definition Registry (`ai_corpus/indexes/definition_registry.json`)

Index of all Chapter 5 definitions with:
- Term name
- Canonical file location
- Line range
- Cluster membership (for dependent clusters)

**Benefit:** Instant location of any term's authoritative definition.

### 3.3 Cross-Reference Matrix (`ai_corpus/indexes/crossref_matrix.json`)

Directed graph of file-to-file Markdown references:
```json
{
  "source": "core_06-06_rights_part_c.md",
  "targets": [
    {"file": "core_05__definitions_home.md", "count": 15, "anchors": [...]},
    {"file": "corpus_systems.md", "count": 8, "anchors": [...]}
  ]
}
```

**Benefit:** Predict dependency depth before edits.

### 3.4 Dependency Map Visualization (`ai_corpus/visualization/dependency_map.mmd`)

Mermaid diagram showing:
- Core constitutional files as primary nodes
- Companion files as secondary nodes
- Cross-reference edges with thickness indicating density
- Color-coding for dependency direction

**Benefit:** Visual understanding of edit impact radius.

---

## 4. Token-Efficient Edit Patterns

### 4.1 Single-Definition Edit Workflow

```
Scenario: Update "Proportionality" definition

Current (expensive):
1. Read entire core_05__definitions_home.md (~1,300 lines)
2. Edit definition
3. Search all files for references to update

Optimized:
1. Query `ai_corpus/indexes/definition_registry.json` for "Proportionality" location
2. Read lines 1100-1150 (definition entry only, ~50 lines)
3. Query `ai_corpus/indexes/crossref_matrix.json` for files referencing "Proportionality"
4. Read only referencing sections, not full files
5. Apply edits using targeted diff
```

### 4.2 Cross-File Consistency Edit Workflow

```
Scenario: Rename term across corpus

Current (expensive):
1. Search all files for term occurrences
2. Read each file containing term
3. Edit each occurrence

Optimized:
1. Query `ai_corpus/indexes/crossref_matrix.json` for all occurrences
2. Group edits by file
3. Use batch diff operations
4. Run `make ai-corpus-sync` so the generated indexes reflect the rename
```

### 4.3 New Definition Addition Workflow

```
Scenario: Add new definition to Chapter 5

Optimized pattern:
1. Read only the alphabetical insertion point (adjacent definitions)
2. Add definition following O/M/A/C template
3. Run `make ai-corpus-sync` to regenerate `ai_corpus/indexes/definition_registry.json`
4. Flag for cross-reference audit (async)
```

---

## 5. Human Readability Preservation

### 5.1 Non-Negotiable Constraints

- **Plain language mandate** (stated in multiple files) must be preserved
- **Alphabetical directory** in Chapter 5 Part A aids human scanning
- **Trace blocks** provide essential context for readers
- **Horizontal rules** (`---`) create visual breathing room

### 5.2 AI-Friendly Enhancements That Preserve Human Readability

| Enhancement | Human Benefit | AI Benefit |
|-------------|---------------|------------|
| Stable anchor IDs | Deep linking in discussions | Precise targeting |
| Consistent header depth | Clear hierarchy | Predictable parsing |
| Machine-readable manifests | Faster contributor onboarding | Instant navigation |
| Definition entry templates | Consistent reading experience | Structured extraction |

---

## 6. Implementation Roadmap

### Phase 1: Manifest Generation (Complete)
- [x] Generate `ai_corpus/indexes/section_manifest.json` from the active corpus scope
- [x] Generate `ai_corpus/indexes/definition_registry.json` from Chapter Five files
- [x] Generate `ai_corpus/indexes/crossref_matrix.json` from source Markdown references
- [x] Create Mermaid dependency map

### Phase 2: Documentation (Complete)
- [x] Create `ai_corpus/AI_NAVIGATION_GUIDE.md` for assistant prompts
- [x] Document optimal reading patterns for common edit types
- [x] Create `ai_corpus/QUICK_REFERENCE.md`
- [x] Add maintenance and authority rules in `ai_corpus/README.md` and `ai_corpus/MAINTENANCE.md`
- [ ] Optional: update `doc_architecture.md` only if future owner rules change

### Phase 3: Tool Integration (Complete for local workflow)
- [x] Add manifest generation to Makefile
- [x] Create validation script for manifest shape and freshness
- [x] Add JSON schemas for generated index artifacts
- [ ] Optional: integrate manifests with existing audit tools where it reduces duplicate parsing
- [ ] Optional: add CI check for manifest updates on core file changes

### Phase 4: Optimization Validation (Ongoing)
- [ ] Measure token usage before/after manifest adoption
- [ ] Track edit efficiency improvements
- [ ] Gather feedback from AI assistants
- [ ] Iterate on manifest structure

### Phase 5: Future Corpus Split Migration Guardrail (Required for New Splits)
- [ ] For any future split of a root corpus document into subfiles, scan the migrated source for stale self-references: `this file`, `in this file`, `same file`, `one place`, and the retired monolithic filename.
- [ ] Reword stale references so folder-level obligations say "these files", "the [layer] folder", "the implementation-group files", or direct section IDs as appropriate.
- [ ] Keep subsection-local references only when they still point to the current subsection or shard.
- [ ] Avoid same-folder backticked folder references that audit tooling may parse as nonexistent nested paths.
- [ ] Run `make reference-audit` and a targeted `rg` sweep before closing the migration.

---

## 7. Quick Reference: File Access Patterns

### High-Frequency Access Patterns

| Task | Files to Read (Current) | Files to Read (Optimized) |
|------|------------------------|---------------------------|
| Edit Chapter 1 principle | `core_00_preamble.md`, `core_01_a_values_principles.md`, `core_01_b_stewardship_capacity_principles.md` + cross-refs | Section manifest → read section only |
| Edit Chapter 5 definition | Full Part file (~1,500 lines) | Definition registry → entry only (~50 lines) |
| Add Chapter 9 right | Full Part file + cross-refs | Target article + related definitions only |
| Cross-file reference audit | All files | Crossref matrix → specific files |
| Corpus-wide term rename | Search all files | Crossref matrix → targeted files |

---

## 8. Success Metrics

- **Token reduction:** Target 60-80% reduction for targeted edits
- **Navigation speed:** Sub-5 second section location time
- **Accuracy:** Zero cross-reference breaks due to AI navigation
- **Human compatibility:** No degradation in human readability scores
- **Maintenance overhead:** <5 minutes per editing session for manifest updates

---

## Appendix A: Current vs Optimized Reading Example

### Scenario: Edit "Proportionality" definition

**Current approach (~1,400 tokens):**
```
Read core_05__definitions_home.md (full file)
Search for "Proportionality" references across all files
Read each referencing file section
```

**Optimized approach (~150 tokens):**
```
Query: `ai_corpus/indexes/definition_registry.json` for "Proportionality"
Result: {file: "core_05__definitions_home.md", lines: [1100-1150]}
Read lines 1100-1150 only (~50 lines)
Query: `ai_corpus/indexes/crossref_matrix.json` references to "Proportionality"
Result: [3 files, 5 sections]
Read only those 5 sections (~100 lines total)
```

**Token savings: ~90%**

---

## Appendix B: Manifest Schema Specifications

See `ai_corpus/schemas/` for formal schema definitions for the generated section manifest, definition registry, and cross-reference matrix.

---

*This plan maintains compatibility with existing corpus architecture and does not require restructuring of authoritative files. All optimizations are additive (manifests, documentation) or procedural (reading patterns).*
