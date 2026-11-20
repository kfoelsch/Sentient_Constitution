#!/usr/bin/env python3
"""Phase A2: Chapter Eight §11 becomes its own chapter, Independent Bodies (temporary core_08.500, final core_07.000).

Placeholder ⟦IB⟧ stands for the new chapter's name until the renumbering pass.
"""
import re
from common import rewrite_all
C8 = 'core_08.000_functional_independence_separation_of_duties.md'; IB = 'core_08.500_independent_bodies.md'
NEWA = '3-what-makes-a-body-independent'
t = open(C8, encoding='utf-8').read()
s = t.index('<a id="11-independent-bodies"></a>'); e = t.rindex('\n---\n')
sec = t[s:e].rstrip('\n'); rest = t[:s].rstrip('\n') + '\n' + t[e:]
sec = sec.replace('<a id="11-independent-bodies"></a>', '<a id="' + NEWA + '"></a>').replace('### 11. Independent Bodies', '### 3. What Makes a Body Independent')
sec = re.sub(r'\[§(\d[^]]*)\]\(#([^)]+)\)', lambda m: '[Chapter Eight §' + m.group(1) + '](' + C8 + '#' + m.group(2) + ')', sec)
sec = re.sub(r'\]\(#([^)]+)\)', lambda m: '](' + C8 + '#' + m.group(1) + ')', sec)
# Chapter Eight loses §11
rest = rest.replace(' → §11 independent bodies.', '.')
rest = rest.replace('  - [§10](#10-relationship-to-later-processes);\n  - [§11](#11-independent-bodies).', '  - [§10](#10-relationship-to-later-processes).')
rest = rest.replace('[§3](#3-four-seat-constitutional-requirement) through [§11](#11-independent-bodies)', '[§3](#3-four-seat-constitutional-requirement) through [§10](#10-relationship-to-later-processes)')
rest = rest.replace('- the relationship to later processes (**section 10**); and\n- the standard independence requirements for a body that this Constitution or designated implementation text names as an Independent Body (**section 11**).',
                    '- the relationship to later processes (**section 10**).\n\nThe standard independence requirements for a body named as an Independent Body are in [⟦IB⟧](' + IB + '#chapter-ib-independent-bodies), *Independent Bodies*.')
rest = rest.replace('through [§11 Independent Bodies](#11-independent-bodies)', 'through [§10 Relationship to Later Processes](#10-relationship-to-later-processes)')
rest = rest.replace('**Next file:** [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md)', '**Next file:** [' + IB + '](' + IB + ')')
open(C8, 'w', encoding='utf-8').write(rest)
open('/tmp/a2_sec.md', 'w').write(sec)
def fix(path, x):
    if path in (C8, IB): return x
    x = x.replace(C8 + '#11-independent-bodies', IB + '#' + NEWA)
    x = re.sub(r'Chapter Eight,? §11(?![\d.])', '⟦IB⟧ §3', x)
    x = re.sub(r'Chapter Eight,? §11\.', '⟦IB⟧ §3.', x)
    return x
print(len(rewrite_all(fix)))
