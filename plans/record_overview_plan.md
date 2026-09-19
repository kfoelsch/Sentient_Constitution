# Record overview plan

**Status:** implemented with the companion overview.  
**Edition consulted:** `SC-Corpus-2026.08.09` (pre-release).  
**Scope:** reader-oriented process support; it does not create a record schema, a registry, a universal sequence, or any constitutional duty.

## Goal

Add a concise companion to `CONCEPTUAL_OVERVIEW.md` that helps a reader distinguish the Constitution's major record families, their relationships, and their limits.

## Plan

1. **Set the boundary.** State prominently that numbered `core_*` files bind; the overview is navigation support.  Define the reader question as “what does this record carry, and what can it not decide?” rather than prescribing an implementation.
2. **Map source-owned record families.** Use only source-grounded examples: attributable/materially binding acts; system context and certification; forum case records; Chapter Nine contribution and violation standing records; and Chapter Ten integration/effect records.
3. **Show relationships without a master pipeline.** Provide a Mermaid relationship map that uses cross-references rather than implied hand-offs.  Explain the important non-substitutions: evidence and logs are not records; case records do not create standing effects; integration records do not alter their sources; contribution and violation remain separate.
4. **Explain cross-cutting safeguards.** Cover the four seats, verification, custody, versioning, contestability, correction, audit trail, and continuity at a high level, linked to their primary sources.
5. **Integrate and validate.** Link the overview from the public and editor entry pages; run the repository's Markdown-link/reference checks relevant to changed files and manually inspect every link and diagram for unsupported claims.

## Acceptance criteria

- `RECORD_OVERVIEW.md` calls itself non-operative and states that it cannot narrow core text.
- Every substantive family and boundary is linked to a binding source anchor.
- The text never treats a process-support overview, log, or evidence item as a record with constitutional effect.
- The map does not imply every matter follows the same route or that every record has the same contents.
- `README.md` and `START_HERE.md` make the new overview discoverable.
