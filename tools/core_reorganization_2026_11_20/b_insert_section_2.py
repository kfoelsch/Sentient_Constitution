#!/usr/bin/env python3
"""Phase B: insert the standard section 2 in twenty chapters and shift their later sections by one.

usage: b_insert_section_2.py [--apply]   (dry run prints counts and a sample)
Run before the chapter renumbering pass: it reads chapter cites in their pre-2026-11-20 numbering.
"""
import json, re, sys
from common import anchor_info_slugs, rewrite_all, github_slug, walk_text_files
APPLY = '--apply' in sys.argv
TARGET = {7: 'core_07.000_charters.md', 10: 'core_10.000_system_alignment_certification_forum_process_outcomes.md',
 11: 'core_11.000_system_alignment_certification_records_recertification.md',
 13: 'core_13.000_institutional_alignment_certification_forum_process_outcomes.md',
 14: 'core_14.000_institutional_alignment_certification_records_recertification.md',
 15: 'core_15.000_standing_assessment.md', 16: 'core_16.000_standing_measurement.md', 17: 'core_17.000_standing_integration.md',
 18: 'core_18.000_contribution_consequences.md', 19: 'core_19.000_violation_consequences.md',
 20: 'core_20.000_final_effect_restoration_enforcement.md', 21: 'core_21.000_misconduct_designation.md',
 22: 'core_22.000_misconduct_pattern_applications.md', 23: 'core_23.000_forum.md',
 24: 'core_25.000_forum_families_escalation_timeliness_support.md', 27: 'core_28.000_governance.md',
 28: 'core_29.000_non_regression.md', 29: 'core_30.000_amendment_ratification.md', 30: 'core_31.000_expansion_supremacy.md',
 31: 'core_25.000_incorporation.md'}
FILE2CH = {v: k for k, v in TARGET.items()}
UNITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
def word(n):
    if n < 10: return UNITS[n]
    if n < 20: return TEENS[n - 10]
    if n % 10 == 0: return {20: 'twenty', 30: 'thirty'}[n]
    return {2: 'twenty', 3: 'thirty'}[n // 10] + '-' + UNITS[n % 10]
W2N = {word(n): n for n in range(1, 32)}
WALT = '|'.join(sorted(W2N, key=len, reverse=True))
HEAD_RE = re.compile(r'^(#{3,6}) (\d+)((?:\.\d+)*)(\.?) (.*)$')

# ---- per-file heading and anchor maps
AMAP = {}
def build(f):
    lines = open(f, encoding='utf-8').read().split('\n')
    old_h = []; new_h = []
    for l in lines:
        m = HEAD_RE.match(l)
        if m and int(m.group(2)) >= 2:
            n = int(m.group(2)) + 1
            old_h.append(l); new_h.append(f'{m.group(1)} {n}{m.group(3)}{m.group(4)} {m.group(5)}')
    amap = {}
    for o, n in zip(old_h, new_h):
        so = github_slug(o.lstrip('#').strip()); sn = github_slug(n.lstrip('#').strip())
        if so != sn: amap[so] = sn
    return amap
for c, f in TARGET.items(): AMAP[f] = build(f)

def shift_heads(t):
    out = []
    for l in t.split('\n'):
        m = HEAD_RE.match(l)
        if m and int(m.group(2)) >= 2:
            l = f'{m.group(1)} {int(m.group(2)) + 1}{m.group(3)}{m.group(4)} {m.group(5)}'
        out.append(l)
    return '\n'.join(out)

# ---- prose section references
KW = r'(?P<kw>§§?\s?|\b[Ss]ections?\s+|\bsection\*\*\s+)'
NUM = r'\d+(?:\.\d+)*'
CONT = r'(?:\s*(?:,\s*and|,|–|—|-|\bto\b|\bthrough\b|\band\b|\bor\b)\s*(?:\*\*)?(?:§\s?|[Ss]ections?\s+)?(?:\*\*)?' + NUM + r'(?!\.\d)(?![\w-]))'
CHAIN = re.compile(KW + r'(?:\*\*)?(?P<first>' + NUM + r')(?P<rest>(?:' + CONT + r')*)')
QUAL_CH = re.compile(r'(?:\bChapter|\bCh\.?)\s*(?:\*\*)?\s*(?P<w>' + WALT + r'|\d{1,2})(?:\*\*)?(?:’s|\'s)?[,\s]*(?:\(\s*\d+\.\d{3}\s*\)\s*)?$', re.I)
QUAL_RD = re.compile(r'(?<![-\w.])(?P<n>\d{1,2})\.\d{3}\s*$')
QUAL_NO = re.compile(r'(?:\b(?:CJS|CI|CS|CF)-[\d.]+[A-Za-z]?|\bArticle [IVXL]+(?:-[A-Z])?|\bPreamble|\bPart [A-E]|\bannex|\bAnnex|\bArticles?|\bRS-[A-Z0-9-]+|\bsub-?article|\bguide|\bGuide|\.md|\bSchedule)(?:\*\*)?(?:’s|\'s)?[,\s]*$')
LINKTXT = re.compile(r'\[([^\[\]]*)\]\(([^)\s]*)\)')
STATS = {'shift': 0}
LOG = []
def chapter_from_word(w):
    return int(w) if w.isdigit() else W2N.get(w.lower())

def referent(text, pos, path, link_spans):
    # 1) inside a link text: use its target
    for s, e, target in link_spans:
        if s <= pos < e:
            before = text[s:pos]
            if QUAL_NO.search(before): return None
            if QUAL_CH.search(before) or QUAL_RD.search(before):
                break
            fpart = target.split('#')[0]
            if not fpart: return FILE2CH.get(path)
            base = fpart.split('/')[-1]
            return FILE2CH.get(base)
    before = text[max(0, pos - 90):pos]
    if QUAL_NO.search(before): return None
    m = QUAL_CH.search(before)
    if m: return chapter_from_word(m.group('w'))
    m = QUAL_RD.search(before)
    if m: return int(m.group('n'))
    return FILE2CH.get(path)

def shift_nums(seg, c):
    def one(m):
        parts = m.group(0).split('.')
        n = int(parts[0])
        if n >= 2:
            STATS['shift'] += 1
            parts[0] = str(n + 1)
        return '.'.join(parts)
    return re.sub(NUM, one, seg)

def prose(path, text):
    link_spans = [(m.start(1), m.end(1), m.group(2)) for m in LINKTXT.finditer(text)]
    edits = []
    for m in CHAIN.finditer(text):
        c = referent(text, m.start(), path, link_spans)
        if c not in TARGET: continue
        s = m.start('first'); e = m.end('rest') if m.group('rest') else m.end('first')
        new = shift_nums(text[s:e], c)
        if new != text[s:e]:
            LOG.append((path, c, text[max(0, m.start() - 70):m.start()].replace('\n', ' '), text[m.start():e], new))
        edits.append((s, e, new))
    for s, e, r in sorted(edits, reverse=True):
        text = text[:s] + r + text[e:]
    return text

def anchors(path, text):
    for f, amap in AMAP.items():
        if not amap: continue
        pat = re.compile(re.escape(f) + r'#([A-Za-z0-9_-]+)')
        text = pat.sub(lambda m: f + '#' + amap.get(m.group(1), m.group(1)), text)
    if path in AMAP:
        amap = AMAP[path]
        text = re.sub(r'\]\(#([A-Za-z0-9_-]+)\)', lambda m: '](#' + amap.get(m.group(1), m.group(1)) + ')', text)
        text = re.sub(r'<a id="([^"]+)"></a>', lambda m: '<a id="' + amap.get(m.group(1), m.group(1)) + '"></a>', text)
    return text

def fix(path, text):
    t = prose(path, text)
    t = anchors(path, t)
    if path in FILE2CH: t = shift_heads(t)
    return t

changed = rewrite_all(fix, apply=False)
print('files', len(changed), STATS)
open('/tmp/b_edits.tsv','w').write('\n'.join('\t'.join(map(str,r)) for r in LOG))
json.dump({f: a for f, a in AMAP.items()}, open('/tmp/b_anchor_map.json', 'w'), indent=1)
if APPLY:
    for p, n in changed.items(): open(p, 'w', encoding='utf-8').write(n)
    print('applied')
else:
    import difflib
    for p in sys.argv[2:] or ['core_19.000_violation_consequences.md']:
        a = open(p).read().split('\n'); b = changed.get(p, '\n'.join(a)).split('\n')
        d = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if l.startswith(('+', '-'))]
        print('==',p); print('\n'.join(x[:200] for x in d[:int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else 40]))
