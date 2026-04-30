# Filename Clarity Candidates and Execution Notes

Date: 2026-04-09  
Status: Executed for core corpus/architecture set; remaining candidates deferred

## Scope

This note records both the candidate analysis and the executed rename set for major top-level markdown files to reduce navigation burden and role ambiguity.

## Naming Policy (Proposed)

- Prefer short, role-signaling names over broad labels.
- Keep canonical corpus names stable unless there is a strong ambiguity reduction benefit.
- Keep uppercase underscore style for core constitutional artifacts to preserve existing corpus convention.
- Avoid overloaded terms like `FRAMEWORK`, `MAP`, or `REPORT` unless file role is explicitly process/evidence.
- Rename only when the new name improves "what this file is for" in one read.

## Candidate Matrix (Conservative)

| Current file | Candidate | Rationale | Decision posture |
|---|---|---|---|
| `Sentient_Constitution.md` | `core_constitution.md` | Shorter constitutional source name with role clarity. | Executed |
| `CONSTITUTIONAL_PRIMITIVES.md` | `corpus_primitives.md` | Reduces uppercase noise while preserving owner-layer meaning. | Executed |
| `CONSTITUTIONAL_SYSTEMS.md` | `corpus_systems.md` | Shorter operations-layer naming with corpus grouping. | Executed |
| `CONSTITUTION_DOCUMENT_ARCHITECTURE.md` | `doc_architecture.md` | Simplifies map/process filename while retaining role signal. | Executed |
| `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` | `CORPUS_REGRESSION_SCENARIOS.md` | Clarifies operational testing role versus constitutional doctrine. | Candidate only |
| `TRUST_UNDER_ATTACK_DELTA_REPORT.md` | `TRUST_UNDER_ATTACK_DELTA_EVIDENCE.md` | Aligns with evidence-layer vocabulary used elsewhere. | Candidate only |
| `TODO.md` | Keep | Universal workflow marker; lowest discovery cost. | Defer rename |
| `MEMLOG.md` | `SESSION_MEMLOG.md` | Optional role clarity for session memory vs governance TODO. | Candidate only |

## Rename Readiness Gate (Required Before Any Rename)

Gate conditions (applied to executed set):

1. Full reference audit across corpus, architecture/process docs, implementation notes, and evidence links.
2. Pre/post mismatch table is published under `evidence/<date>/`.
3. Script/tooling references are included in audit scope.
4. Backward-compatibility decision is explicitly recorded (current posture: conservative defer).
5. Planned edition/custody note identifies whether rename occurs pre-cut or as part of named corpus edition.

## Recommended Next Step

For remaining candidates, keep conservative defer posture. If execution is approved, perform a rename-only change set with same-change reference updates and an evidence artifact documenting zero stale links.
