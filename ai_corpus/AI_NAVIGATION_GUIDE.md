# AI Navigation Guide for Sentient Constitution Corpus

**Purpose:** Enable token-efficient AI access to the constitutional corpus while preserving human readability.

---

## Quick Start for AI Assistants

### Before You Read Any File

1. **Check the Section Manifest First** → `ai_corpus/indexes/section_manifest_sample.json`
   - Find exact line ranges for any section
   - Avoid reading entire files when only a section is needed

2. **For Definition Lookups** → `ai_corpus/definitions/independent/*.json` (sample)
   - Locate any term's authoritative definition instantly
   - Get O/E/C component boundaries for precise reading

3. **For Cross-Reference Analysis** → `ai_corpus/indexes/crossref_matrix.json`
   - See which files reference which
   - Plan multi-file edits efficiently

---

## Optimal Reading Patterns

### Pattern 1: Definition-First Editing

**Use when:** Editing content that references defined terms

```
Step 1: Query ai_corpus/indexes/section_manifest_sample.json
        → Get line range for the definition
        
Step 2: Read only those lines using read_file with offset/limit
        → Capture O/E/C components completely
        
Step 3: Read your target section using manifest
        → Get exact line range
        
Step 4: Edit with confidence
```

**Example:**
```python
# Instead of reading entire file:
# read_file("core_05-05_definitions_a_independent.md")  # 1,300 lines!

# Query manifest for "Proportionality"
# Result: lines 1100-1119

# Read only definition entry:
read_file("core_05-05_definitions_a_independent.md", offset=1100, limit=20)
```

### Pattern 2: Cross-File Reference Audit

**Use when:** Renaming a term or checking consistency

```
Step 1: Query ai_corpus/indexes/crossref_matrix.json
        → Get list of files referencing the target
        
Step 2: For each referencing file, query section manifest
        → Get exact sections containing references
        
Step 3: Read only those sections
        → Not entire files
        
Step 4: Batch edit with apply_diff
```

### Pattern 3: Definition Entry Extraction

**Use when:** Adding or modifying definitions

```
Step 1: Read adjacent definitions using manifest
        → Understand alphabetical placement
        
Step 2: Follow template structure:
        #### Term Name
        <details> [Trace block] </details>
        <details> [DEFINITION: O/E/C] </details>
        <details> [COMPLIANCE] </details>
        ---
        
Step 3: Update ai_corpus index files
        → Add new entry with line range
```

---

## Chunking Best Practices

### Safe Chunk Boundaries (Split Here)

- ✅ After `---` horizontal rules
- ✅ Before `### ` or `#### ` headers
- ✅ After `</details>` closing tags
- ✅ Between definition entries
- ✅ At empty lines between major sections

### Unsafe Chunk Boundaries (Never Split Here)

- ❌ Inside O/E/C component triplets
- ❌ Inside `<details>...</details>` blocks
- ❌ Inside cross-reference lists
- ❌ Inside tables
- ❌ Mid-sentence or mid-paragraph

---

## Token Budget Guidelines

| Task Type | Recommended Budget | Optimization Strategy |
|-----------|-------------------|----------------------|
| Single definition edit | 500-1,000 tokens | Manifest-guided section read |
| Cross-file consistency | 1,000-2,000 tokens | Matrix-guided targeted reads |
| New definition addition | 800-1,500 tokens | Adjacent context only |
| Full article review | 2,000-3,000 tokens | Section-by-section manifest reads |
| Architecture decision | 3,000-5,000 tokens | Tier 1-3 context + manifests |

---

## File Access Priority

### Tier 1: AI Indexes (Check First)

1. `ai_corpus/indexes/section_manifest_sample.json` - Section locations
2. `ai_corpus/indexes/crossref_matrix.json` - Reference graph
3. `ai_corpus/definitions/` - Structured definition extracts

### Tier 2: Architecture Context

4. `doc_architecture.md` - File ownership and boundaries
5. `README.md` - Reading order and fast locator

### Tier 3: Implementation Details

6. `corpus_systems.md` - System classification
7. `corpus_institutions.md` - Institutional rules
8. `corpus_forum.md` - Forum procedures

---

## Quick Reference: Core File Inventory

| File | Lines | Primary Content |
|------|-------|-----------------|
| core_00-01_principles.md | ~1,400 | Values, constraints, hierarchy |
| core_02-04_definition_mechanics.md | ~530 | O/E/C structure, burden, traceability |
| core_05-05_definitions_a_independent.md | ~1,300 | Independent definitions A-Z |
| core_05-05_definitions_b_semi_independent.md | ~1,900 | Semi-independent definitions |
| core_05-05_definitions_c_dependent_clusters.md | ~1,800 | Dependent definition clusters |
| core_06-06_standing_classification.md | ~880 | Two-axis standing model |
| core_06-06_standing_integration.md | ~780 | Standing effects, integration |
| core_07-07_misconduct.md | ~420 | Anti-constitutional misconduct |
| core_08-08_forum.md | ~380 | Forums, jurisdiction |
| core_09-09_rights_part_a.md | ~630 | Articles I-IV |
| core_09-09_rights_part_b.md | ~1,380 | Articles V-XI |
| core_09-09_rights_part_c.md | ~1,600 | Articles XII-XXII |
| core_09-09_rights_part_d.md | ~560 | Articles XXIII-XXV |
| core_10-10_governance.md | ~330 | Constitutional contract |
| core_11-13_amendment.md | ~640 | Non-regression, amendment |
| core_14-14_incorporation.md | ~160 | Incorporation bridge |
| corpus_systems.md | ~2,170 | Systems protocols S1-S5 |
| corpus_institutions.md | ~940 | Institutional governance CI-1-24 |
| corpus_forum.md | ~1,150 | Forum operations |
| corpus_joint_structure.md | ~1,730 | Cross-domain implementation |

---

## Visual Dependency Map

See `ai_corpus/visualization/dependency_map.mmd` for a Mermaid diagram showing:
- Core constitutional files as primary nodes
- Companion files as secondary nodes
- Cross-reference edges with thickness indicating density

---

*This guide enables token-efficient navigation while maintaining the corpus's human-readable plain-language structure.*
