#!/usr/bin/env python3
"""Phase B2: write the reviewed section 2 text into twenty chapters, and Grounded in lists into seven."""
import re, sys
sys.path.insert(0, sys.argv[1])
from s2_specs import SPECS, LISTS
from common import github_slug
ch1 = {}; art = {}
for line in open(sys.argv[1] + '/anchors.txt'):
    k, rest = line.split(' ', 1); a, t, f = [x.strip() for x in rest.split('|')]
    (ch1 if k == 'CH1' else art)[a.replace('Article ', '')] = (t, f)
def c1(n):
    t, f = ch1[n]; return f"[§{n} {t}]({f}#{github_slug(n + ' ' + t)})"
def ar(n):
    t, f = art[n]; return f"[Article {n}]({f}#{github_slug('Article ' + n + ' ' + t)}) (*{t}*)"
def block(cs, As):
    out = ["**Grounded in:**", "", "- Chapter One principles:"]
    for i, n in enumerate(cs): out.append("  - " + c1(n) + (";" if (i < len(cs) - 1 or As) else "."))
    if As:
        out.append("- Chapter Six Articles:")
        for i, n in enumerate(As): out.append("  - " + ar(n) + (";" if i < len(As) - 1 else "."))
    return "\n".join(out)
def insert_before(lines, idx):
    j = idx
    while j > 0 and (lines[j - 1].startswith('<a id=') or not lines[j - 1].strip()): j -= 1
    while j < idx and not lines[j].strip(): j += 1
    return j
for word, f, h, pt, why, cs, As in SPECS:
    if word in ('Two', 'Three', 'Four'): continue
    lines = open(f, encoding='utf-8').read().split('\n')
    i3 = next(i for i, l in enumerate(lines) if l.startswith('### 3. '))
    j = insert_before(lines, i3)
    slug = github_slug('2. ' + h)
    new = [f'<a id="{slug}"></a>', f'### 2. {h}', '', f'*In plain terms: {pt}*', '', why, '', block(cs, As), '']
    lines[j:j] = new
    open(f, 'w', encoding='utf-8').write('\n'.join(lines))
for word, f, cs, As in LISTS:
    lines = open(f, encoding='utf-8').read().split('\n')
    i2 = next(i for i, l in enumerate(lines) if l.startswith('### 2. '))
    k = next(i for i in range(i2 + 1, len(lines)) if lines[i].startswith(('### ', '#### 2.')))
    j = insert_before(lines, k)
    lines[j:j] = [block(cs, As), '']
    open(f, 'w', encoding='utf-8').write('\n'.join(lines))
print('done')
