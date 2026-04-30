# Best Practices Check Execution

This repository has two different review modes:

- `make regression` / `make regression-full`
  - automated integrity and editorial gates;
  - designed to catch corpus regressions and release blockers.
- `make best-practices-check`
  - benchmark-and-gap review against the institutional best-practices standard;
  - designed to compare the corpus against mapped governance, integrity, assurance, and AI-risk frameworks.

## Commands

- Run the benchmark review:
  - `make best-practices-check`
- Run and write a dated artifact:
  - `make best-practices-check-evidence`
  - Output: `evidence/<YYYY-MM-DD>/BEST_PRACTICES_CHECK_<YYYY-MM-DD>.md`

## Inputs used by the command

- `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`
- `implementation/INSTITUTIONAL_GOVERNANCE_GAP_MATRIX_2026-04-10.md`
- `implementation/AUTOMATED_REFERENCE_CHECKING.md`
- `doc_architecture.md` section `15. External framework crosswalk`
- dated drill artifacts under `evidence/2026-q2/drills/`

## Important distinction

The best-practices check is **not** a release gate. It is a structured review memo based on the local benchmark standard and current evidence.

Use it when the question is:
- "How does the corpus compare to known governance best practices?"
- "What are the major gap areas before assurance review?"
- "What should we prioritize next in institutional hardening?"

Use regression when the question is:
- "Did we break references, markdown, vocabulary, or other repository rules?"
- "Can this edition pass the current automated checks?"
