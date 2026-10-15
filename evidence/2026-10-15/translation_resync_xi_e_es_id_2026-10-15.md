# AI-assisted translation check: Article XI-E (five locales)

**Date:** 2026-10-15  
**Status:** AI-drafted; unreviewed; non-binding.  
**English snapshot:** current working-tree `core_06_rights_part_b.md`, SHA-256 `49469d3e73d366f9290c1c632b8818c181d2af8ce77a01a29e30f3cc9bbaf3da`.  
**Locales/files covered:** ar (`ar`), `translations/ar/core_06_rights_part_b.md`, SHA-256 `7a8c94c83777e34bffdec6480775b05ef40edc23a1c42528a9db419c9401e25c`; es (`es`), `translations/es/core_06_rights_part_b.md`, SHA-256 `7a5e2247e71ee3546a6ea4ebb2ab1b571016858ffc3b5b9cc55714132124c5f6`; fr (`fr`), `translations/fr/core_06_rights_part_b.md`, SHA-256 `ce8b3b200c1159479acca2cad534171ef75d83e0b44b3080fa77313e775f2704`; hi (`hi`), `translations/hi/core_06_rights_part_b.md`, SHA-256 `e82a64cb3813a94c44fc26aa2a2b94178faa0bb383e4febad8b2283fdbf1d7b2`; id (`id`), `translations/id/core_06_rights_part_b.md`, SHA-256 `a0d10ac3eec7a0b43b930b5d75becb1776fd01196fbb4e553a2810eb05a06c38`.

## Coverage

Updated the XI-E plain-language summary in the five listed locales and translated the current source's missing material on authentic formation, evidence of intent, belief and affiliation safeguards, founders with no record, the no-clearance rule, both authority gates, the interim hold and its limits, and safeguards common to both gates. Retained existing translated material and the stable XI-E anchor.

Not covered in this pass: XI-E in the other 14 locales; other changed Chapter Six passages; the Chapter Five Domain-Specific Materiality / small-business addition, for which most target pages lack the parent section; and all other source-changed translation pairs.

## Checks performed

- Compared the new clauses in all five locale drafts against the current English XI-E for actors, scope, conditions, exceptions, burden, negation, and permission/constraint strength.
- Reviewed each locale draft for grammar and unintended mixed-language text. Named constitutional concepts and article names intentionally retain some English labels already used in this locale.
- Ran `python3 tools/translation_audit.py structure --locale {ar,es,fr,hi,id}`: each locale has no unbalanced details blocks or code fences; existing source-ID and marker-count review findings remain.
- Ran the full link audit for all five locales; it reports existing corpus-wide unresolved targets (ar 6,835; es 1,818; fr 6,198; hi 6,231; id 6,901). Checked links on the added lines against current files and fragments: 44 links checked, no new findings.
- Ran `git diff --check` on all edited translations and the check record: passed.

These are AI self-checks, not independent fluent review or semantic certification. No human review attestation or review-manifest entry was changed. English remains controlling.
