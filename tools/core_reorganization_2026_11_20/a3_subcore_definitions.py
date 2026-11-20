#!/usr/bin/env python3
"""Phase A3: Chapters Two to Four become Subcore 3-A, 3-B and 3-C of the Definitions chapter (titles and slugs).

File renames and the word cites (Chapter Two -> Subcore 3-A, etc.) are done by the renumbering pass.
"""
from common import rewrite_all
SLUGS = {
 'chapter-two-definition-structure-and-component-requirements': 'subcore-3-a-definition-structure-and-component-requirements',
 'chapter-three-definition-integrity-evasion-and-non-compliance': 'subcore-3-b-definition-integrity-evasion-and-non-compliance',
 'chapter-four-burden-of-proof-traceability-and-verification': 'subcore-3-c-burden-of-proof-traceability-and-verification',
}
TITLES = {
 '# CHAPTER TWO: DEFINITION STRUCTURE AND COMPONENT REQUIREMENTS': '# SUBCORE 3-A: DEFINITION STRUCTURE AND COMPONENT REQUIREMENTS',
 '# CHAPTER THREE: DEFINITION INTEGRITY, EVASION, AND NON-COMPLIANCE': '# SUBCORE 3-B: DEFINITION INTEGRITY, EVASION, AND NON-COMPLIANCE',
 '# CHAPTER FOUR: BURDEN OF PROOF, TRACEABILITY, AND VERIFICATION': '# SUBCORE 3-C: BURDEN OF PROOF, TRACEABILITY, AND VERIFICATION',
}
PLACE = 'This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one text.'
NEWPLACE = 'This file is **part of the Sentient Constitution**: a [subcore](core_05.045_band_integrative.md#subcore) file attached to [Chapter Five](core_05.000_definitions_home.md#chapter-five-foundational-definitions), with the same force as that chapter, binding only together with the numbered `core_*` files and the rest of the subcore read as one text. Until 2026-11-20 it was a chapter of its own.'
FILES = ('core_02.000_definition_structure.md', 'core_03.000_definition_integrity.md', 'core_04.000_burden_traceability_verification.md')
def fix(path, t):
    for a, b in SLUGS.items(): t = t.replace(a, b)
    if path in FILES:
        for a, b in TITLES.items(): t = t.replace(a, b)
        t = t.replace(PLACE, NEWPLACE)
    return t
print(len(rewrite_all(fix)))
