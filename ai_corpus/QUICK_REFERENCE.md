# AI Navigation Cheatsheet

## ⚡ Instant Lookup

| Need | File | Key |
|------|------|-----|
| Section location | `ai_corpus/indexes/section_manifest_sample.json` | `{"file": "...", "lines": [start, end]}` |
| Definition location | `ai_corpus/definitions/` | `{"term": "...", "file": "...", "range": [n, m]}` |
| Cross-references | `ai_corpus/indexes/crossref_matrix.json` | `{"source": "...", "targets": [...]}` |
| Architecture rules | `doc_architecture.md` | Section 2: Corpus roles |

## 📖 Reading Patterns

### Definition Lookup
```
Query: section_manifest_sample.json → find line range
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
| After `---` | Inside O/E/C components |
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
| Core Ch 1 | core_00-01_principles.md | ~1,400 |
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
