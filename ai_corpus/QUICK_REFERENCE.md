# AI Navigation Cheatsheet

## ⚡ Instant Lookup

| Need | File | Key |
|------|------|-----|
| Section location | `ai_corpus/indexes/section_manifest.json` | `{"file": "...", "line_start": n, "line_end": m}` |
| Definition location | `ai_corpus/indexes/definition_registry.json` | `{"term": "...", "source_file": "...", "line_start": n, "line_end": m}` |
| Cross-references | `ai_corpus/indexes/crossref_matrix.json` | `{"source": "...", "targets": [...]}` |
| Architecture rules | `doc_architecture.md` | Section 2: Corpus roles |

## 📖 Reading Patterns

### Definition Lookup
```
Query: definition_registry.json or section_manifest.json → find line range
Read: read_file(file, offset=start, limit=count)
Edit: apply_diff with targeted change
```

### Cross-File Audit
```
Query: crossref_matrix.json → get referencing files
For each: Query section manifest → get sections
Read: Only those sections, not full files
```

## 🎯 Safe Edit Boundaries

| Split Here | Never Split Here |
|------------|------------------|
| After `---` | Inside O/M/A/C components |
| Before `### ` | Inside `<details>` |
| After `</details>` | Mid-table |
| Between definitions | Mid-sentence |

## 📊 Token Budgets

| Task | Tokens | Strategy |
|------|--------|----------|
| Definition edit | 500-1K | Manifest lookup + section read |
| Cross-file consistency | 1-2K | Matrix-guided targeted reads |
| New definition | 800-1.5K | Adjacent context only |

## 🗂️ File Sizes (Lines)

| Category | Files | Size |
|----------|-------|------|
| Core Ch 1 | `core_00_preamble.md`, `core_01_a_values_principles.md`, `core_01_b_interaction_interpretation.md`, `core_01_c_stewardship_capacity_principles.md` | ~272 / ~756 / ~646 / ~1,078 |
| Core Ch 5 (all) | definitions_a/b/c | ~1,300-1,900 |
| Core Ch 9 | rights a/b/c/d | ~560-1,600 |
| Companion | systems/institutions/forum/joint | ~940-2,170 |

## ✅ Pre-Edit Checklist

- [ ] Verified line numbers in manifest
- [ ] Read complete semantic block
- [ ] Checked crossref matrix for dependencies
- [ ] Confirmed anchor ID stability

## ✅ Post-Edit Checklist

- [ ] Cross-references resolve
- [ ] Manifests fresh (regenerate if needed)
- [ ] No semantic units split
