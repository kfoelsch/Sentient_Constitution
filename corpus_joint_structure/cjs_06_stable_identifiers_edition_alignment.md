## CJS-6: Stable section identifiers, edition alignment, and drafting notes

**Edition alignment:** The header **Corpus edition** and **Effective date** must track **Corpus** labels in adopting instruments and `doc_architecture.md` corpus-alignment notes.

**Drafting priority (suggested):**

1. Extend **CJS-2.2** with new rows only when `doc_architecture.md` section 2 ownership or cross-file overlap changes; keep row IDs **stable**—append new IDs, do not renumber.
2. When **CI**/**CF**/**CS** repeat the same joint interface paragraph, prefer a **one-line** pointer to the relevant CJS joint section (including **CJS-4.1** for hybrid composition shared by **CI-9.1B.2** and **CF-2.5.2**) and keep operative checklists in the domain owner.
3. When **Cross-domain implementation layer** files repeat the same joint interface paragraph, apply **CJS-4.3** the same way: **one-line** pointer to **CJS-4** (or **CJS-2.2**), and keep **PRIM/PROT** operative substance in that layer rather than duplicating it at length in **CJS-5** OP clusters.
4. Run `make reference-audit` after substantive cross-file moves.
5. Where a new high-level joint abstraction is added, verify it remains **Tier 1 only** (no owner-mechanics migration) and record the duplicate-taxonomy risk in the active review notes until the deferred regression path is reinstated.

`doc_architecture.md` remains the **editorial map** and **placement guide**. The CJS folder holds **binding joint structural** text within **Corpus** as designated in **Chapter Five** and incorporated through **Chapter Fifteen**.

*Corpus alignment:* edition `SC-Corpus-2026.04.30`, effective **2026-04-18**; canonical mapping in [doc_architecture.md](../doc_architecture.md) **section 17**.

---

**Next file:** [cjs_07_implementation_layer_overview.md](cjs_07_implementation_layer_overview.md)
