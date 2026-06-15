# CI to CJS Relocation Candidate Audit

Generated: 2026-06-15

Scope: `corpus_institutions/*.md` compared against `corpus_joint_structure/*.md` and the CJS-2.2 topic router.

This is an editorial exposure audit. It identifies candidate passages for relocation, pointer replacement, or split ownership; it does not apply moves.

## Summary

- Candidate threshold: relocation score >= 5
- Candidates: 0
- Confidence: high 0, medium 0, low 0

## Classification rules

- `split-CI-and-CJS`: likely shared rule should move to CJS while CI keeps institution-specific application.
- `replace-with-pointer`: CI appears to restate existing or near-existing CJS text; replace local repetition with a short CJS pointer after review.
- `needs-human-review`: cross-layer signals exist, but ownership is ambiguous or mixed.

## Candidates

## Recommended next pass

1. Review high-confidence `split-CI-and-CJS` candidates first.
2. For each accepted move, relocate only the shared operational rule to CJS and leave CI with a one-line pointer plus institution-specific application.
3. Run `make reference-audit` after any actual relocation.
