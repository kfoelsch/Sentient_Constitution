#!/usr/bin/env python3
"""Phase A1: Preamble §3.2 and §4-§9 become the Constitutional Map (temporary file core_00.500, final core_01.000).

Placeholder ⟦MAP⟧ stands for the Map's chapter name until the renumbering pass resolves it.
"""
import re, sys
from common import anchors_in, rewrite_all
P = 'core_00.000_preamble.md'; M = 'core_00.500_constitutional_map.md'
lines = open(P, encoding='utf-8').read().split('\n')
def idx(s): return next(i for i, l in enumerate(lines) if l.strip() == s)
i32 = idx('<a id="32-key-governance-processes"></a>')
i33 = idx('<a id="33-governance-layers"></a>')
i4 = idx('<a id="4-principles-definitions-and-rights"></a>')
ifoot = max(i for i, l in enumerate(lines) if l.strip() == '---')
pre_head = lines[:i32]; sec32 = lines[i32:i33]; sec33 = lines[i33:i4]; moved = lines[i4:ifoot]
moved_text = '\n'.join(sec32 + moved)
MOVED = anchors_in(moved_text)
AMAP = {a: a for a in MOVED}; AMAP['32-key-governance-processes'] = '3-key-governance-processes'
# §3.2 becomes the Map's §3
sec32 = [l.replace('<a id="32-key-governance-processes"></a>', '<a id="3-key-governance-processes"></a>')
          .replace('#### 3.2 Key Governance Processes', '### 3. Key Governance Processes') for l in sec32]
sec33 = [l.replace('<a id="33-governance-layers"></a>', '<a id="32-governance-layers"></a>')
          .replace('#### 3.3 Governance Layers', '#### 3.2 Governance Layers') for l in sec33]
def localize_moved(t):
    # relative links in moved text to anchors left in the Preamble become cross-file links
    def f(m):
        a = m.group(1)
        if a in MOVED: return '](#' + AMAP[a] + ')'
        if a == '33-governance-layers': a = '32-governance-layers'
        return '](' + P + '#' + a + ')'
    return re.sub(r'\]\(#([^)\s]+)\)', f, t)
def localize_pre(t):
    def f(m):
        a = m.group(1)
        if a in MOVED: return '](' + M + '#' + AMAP[a] + ')'
        if a == '33-governance-layers': return '](#32-governance-layers)'
        return m.group(0)
    return re.sub(r'\]\(#([^)\s]+)\)', f, t)
body32 = localize_moved('\n'.join(sec32)); body_moved = localize_moved('\n'.join(moved))
head = '\n'.join(pre_head); tail33 = '\n'.join(sec33)
new_pre = localize_pre(head + '\n' + tail33) + '\n---\n\n**Previous file:** [README.md](README.md)\n\n**Next file:** [' + M + '](' + M + ')\n'
open(P, 'w', encoding='utf-8').write(new_pre)
open('/tmp/a1_sec3.md', 'w').write(body32); open('/tmp/a1_moved.md', 'w').write(body_moved)
# corpus-wide link and cite rewrites
LINK = re.compile(re.escape(P) + r'#([A-Za-z0-9_-]+)')
def fix(path, t):
    if path in (P, M): return t
    def l(m):
        a = m.group(1)
        if a in MOVED: return M + '#' + AMAP[a]
        if a == '33-governance-layers': return P + '#32-governance-layers'
        return m.group(0)
    t = LINK.sub(l, t)
    t = re.sub(r'Preamble §3\.2(?![\d])', '⟦MAP⟧ §3', t)
    t = re.sub(r'Preamble §3\.3(?![\d])', 'Preamble §3.2', t)
    t = re.sub(r'Preamble,? (§§?)([4-9])', r'⟦MAP⟧ \1\2', t)
    t = re.sub(r'Preamble sections ([4-9])', r'⟦MAP⟧ sections \1', t)
    t = t.replace('Preamble — constitutional owner register', '⟦MAP⟧ — constitutional owner register')
    t = t.replace('Preamble constitutional owner register', '⟦MAP⟧ constitutional owner register')
    t = t.replace('Preamble owner register', '⟦MAP⟧ owner register')
    t = t.replace('Preamble register', '⟦MAP⟧ register')
    return t
ch = rewrite_all(fix)
print('moved anchors', len(MOVED), 'files changed', len(ch))
