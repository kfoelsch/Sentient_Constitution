<!-- Read CONTRIBUTING.md first. One lane, one concern, one pull request. -->

## Lane

<!-- Keep one. -->
- [ ] A — Finding (defect fix, no change of meaning)
- [ ] B — Evaluation result (new results file only)
- [ ] C — Companion maturation (CS / CI / CF / CJS / Remedy / Emergency)
- [ ] D — Core text proposal (numbered `core_*` file) — linked Proposal issue: #
- [ ] E — Tooling and audits

## Layer touched

- [ ] Binding core (`core_*`)
- [ ] Binding incorporated implementation (`corpus_*` wrappers or subfiles)
- [ ] Process support (`implementation/`, `evaluation/`, `START_HERE.md`, `README.md`, `docs/`, `VISION.md`, `CONTRIBUTING.md`)
- [ ] Tooling (`tools/`, `Makefile`, `.github/`)
- [ ] Derived artifacts regenerated (`ai_corpus/`, `doc_architecture/generated/`, `implementation/steward_owner_clock_index.json`)

## What changed and why

<!-- Two to five sentences. Cite the section (file + heading) you changed and the owner home it answers to. -->

## Gate output

```text
make regression          → 
make readability-audit   →  (prose-heavy changes)
lane-specific targets    →  (steward-door-lockstep-audit, obligation-diff, alignment audits, tests)
```

## Checklist

- [ ] Core meaning not narrowed; no conflict resolved by bending a `core_*` file toward a companion
- [ ] No duplicate definition or restated obligation; pointers used instead
- [ ] Vocabulary guardrails followed (`doc_architecture.md` § Plain-Language Vocabulary Guardrails)
- [ ] Derived artifacts regenerated and committed with the source change, or none affected
- [ ] Edition label `SC-Corpus-2026.08.09` untouched; pre-release status untouched
- [ ] No fossil anchors; every inbound link to a renamed heading fixed
- [ ] Evidence (if any) under `evidence/<YYYY-MM-DD>/` and linked below
- [ ] Lane C / D only: `make obligation-snapshot` before and `make obligation-diff` after; diff linked below
- [ ] Lane D only: Test 1 non-regression self-check written below; Proposal issue linked above

## Evidence links

<!-- evidence/<YYYY-MM-DD>/... ; leave blank for Lane A and B. -->

## Lane D — Test 1 self-check

<!-- Delete this section unless Lane D. State what the change does NOT weaken: Chapter One constraints, Chapter Two–Four integrity, Chapter Six Rights Floor, Chapter Twelve legitimacy — including indirect narrowing through definitions, standing gates, evidence rules, or emergency labels. List downstream files that cite the changed section. -->

## Attribution

<!-- Required. Examples:
     human — <name or handle>
     AI agent (<model>) directed by human — <name or handle>; AI touched: <files>
-->
