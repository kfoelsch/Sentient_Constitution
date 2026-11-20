#!/usr/bin/env python3
"""Phase C: renumber the core chapters (2026-11-20 core reorganization).

Old -> new: Preamble stays; the Constitutional Map (temporary core_00.500, placeholder ⟦MAP⟧) is Chapter One;
1 -> 2; Chapters Two, Three and Four become Subcore 3-A, 3-B and 3-C (subcore_03.010/.020/.030);
5 -> 3; 6 -> 4; 7 -> 5; 8 -> 6; Independent Bodies (temporary core_08.500, placeholder ⟦IB⟧) is Chapter Seven;
9..31 -> 8..30. Corpus files and ids homed under a chapter follow it.
usage: c_renumber.py [--apply]
"""
import collections, json, os, re, sys
from common import rewrite_all, walk_text_files
APPLY = '--apply' in sys.argv
def newnum(n):
    if n == 0: return 0
    if n == 1: return 2
    if n in (2, 3, 4): return None
    if 5 <= n <= 8: return n - 2
    if 9 <= n <= 31: return n - 1
    return n
SUB = {2: '3-A', 3: '3-B', 4: '3-C'}
UNITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
def word(n):
    if n < 10: return UNITS[n]
    if n < 20: return TEENS[n - 10]
    if n % 10 == 0: return {20: 'twenty', 30: 'thirty'}[n]
    return {2: 'twenty', 3: 'thirty'}[n // 10] + '-' + UNITS[n % 10]
W2N = {word(n): n for n in range(1, 32)}
WALT = '|'.join(sorted(W2N, key=len, reverse=True))
def style(tok, new):
    if tok.isupper(): return new.upper()
    if tok[0].isupper(): return '-'.join(p.capitalize() for p in new.split('-'))
    return new
STATS = collections.Counter(); CROSS = []
SKIP_FILES = {'tools/architecture/chapter_numbers.json', 'tools/architecture/chapter_crosswalk.json'}
# ---- prose chains
HEAD = re.compile(r'\b(Chapters?|CHAPTERS?|chapters?)(?:\*\*)?(?:[ \t]+|(?=\[))(?:\*\*)?')
TOK = re.compile(r'(?:\[\s*)?(?P<w>%s|\d{1,2})(?![\w-])(?:\s*\])?(?:\((?:[^)\s]*)\))?' % WALT, re.I)
SEC = re.compile(r'(?:’s|\'s)?,?\s*(?:§§?|sections?\s)\s*\d+(?:\.\d+)*(?:\s*(?:–|-|—|,|and|to)\s*§?\d+(?:\.\d+)*)*')
SEP = re.compile(r'(?:\s*,\s*(?:and\s+)?|\s+and\s+|\s+or\s+|\s*(?:–|—)\s*|-(?=\d)|\s+through\s+|\s+to\s+)(?:\*\*)?(?:Chapters?(?:\*\*)?[ \t]+(?:\*\*)?)?', re.I)
def tokval(w): return int(w) if w.isdigit() else W2N.get(w.lower())
def apply_edits(text, edits):
    out = text; last = len(text) + 1
    for s, e, r in sorted(set(edits), reverse=True):
        if e > last: continue
        out = out[:s] + r + out[e:]; last = s
    return out
RANGE_SEP = re.compile(r'^(?:\s*(?:–|—)\s*|-|\s+through\s+|\s+to\s+)(?:\*\*)?(?:Chapters?(?:\*\*)?[ \t]+(?:\*\*)?)?$', re.I)
def wordish(w, n): return str(n) if w.isdigit() else style(w, word(n))
def chain(text, path):
    edits = []
    for h in HEAD.finditer(text):
        if h.group(1)[0].islower(): continue
        pos = h.end(); toks = []; seps = []
        m = TOK.match(text, pos)
        while m:
            toks.append((m.start('w'), m.end('w'), m.group('w'))); pos = m.end()
            s = SEC.match(text, pos)
            if s: pos = s.end()
            sp = SEP.match(text, pos)
            if not sp: break
            m2 = TOK.match(text, sp.end())
            if not m2: break
            seps.append(text[pos:sp.end()]); m = m2
        if not toks: continue
        vals = [tokval(w) for _, _, w in toks]
        if None in vals: continue
        hs, he = h.start(1), h.end(1); plural = h.group(1).lower().endswith('s'); upper = h.group(1).isupper()
        is_range = len(toks) == 2 and RANGE_SEP.match(seps[0] or '')
        subs = [v for v in vals if v in SUB]
        if subs and all(v in SUB for v in vals):
            edits.append((hs, he, ('SUBCORES' if upper else 'Subcores') if plural else ('SUBCORE' if upper else 'Subcore')))
            for (s_, e_, w), v in zip(toks, vals): edits.append((s_, e_, SUB[v])); STATS['sub'] += 1
            if is_range: edits.append((toks[0][1], toks[1][0], ' to '))
            continue
        if is_range and (vals[0] in SUB or vals[0] == 1 or vals[1] in SUB):
            a, b = vals
            na = 1 if (a == 1 and b > 8) else (2 if a == 1 else 3)
            nb = 3 if b in SUB else newnum(b)
            w0 = toks[0][2]
            if na == nb:
                rep = ('Chapter ' if not upper else 'CHAPTER ') + wordish(w0, na) + ', including its subcore'
            elif nb == na + 1:
                rep = ('Chapters ' if not upper else 'CHAPTERS ') + wordish(w0, na) + ' and ' + wordish(toks[1][2], nb)
            else:
                rep = None
            if rep:
                edits.append((h.start(), toks[1][1], rep)); STATS['range_fix'] += 1; continue
            edits.append((toks[0][0], toks[0][1], wordish(w0, na)))
            edits.append((toks[1][0], toks[1][1], wordish(toks[1][2], nb))); STATS['range'] += 1; continue
        if subs:
            CROSS.append((path, text[h.start():toks[-1][1] + 30].replace('\n', ' '))); continue
        for (s_, e_, w), v in zip(toks, vals):
            nv = newnum(v)
            if nv is None or nv == v: continue
            edits.append((s_, e_, wordish(w, nv))); STATS['chain'] += 1
    return apply_edits(text, edits)
# ---- slugs: chapter-nine-..., chapter-01-part-e
SLUG = re.compile(r'(?<![\w-])chapters?-(%s)(?=-)' % WALT.replace(' ', '-'))
SLUGD = re.compile(r'(?<![\w-])chapter-(\d\d)-')
def slugs(text):
    def f(m):
        v = W2N[m.group(1)]; nv = newnum(v)
        if nv is None or nv == v: return m.group(0)
        STATS['slug'] += 1; return m.group(0).replace(m.group(1), word(nv))
    text = SLUG.sub(f, text)
    def g(m):
        v = int(m.group(1)); nv = newnum(v)
        if nv is None or nv == v: return m.group(0)
        STATS['slugd'] += 1; return 'chapter-%02d-' % nv
    return SLUGD.sub(g, text)
# ---- files and ids
SPECIAL = {'core_00.500_constitutional_map': 'core_01.000_constitutional_map',
           'core_08.500_independent_bodies': 'core_07.000_independent_bodies',
           'core_02.000_definition_structure': 'subcore_03.010_definition_structure',
           'core_03.000_definition_integrity': 'subcore_03.020_definition_integrity',
           'core_04.000_burden_traceability_verification': 'subcore_03.030_burden_traceability_verification'}
SPECIAL_RE = re.compile('|'.join(re.escape(k) for k in SPECIAL))
CORE_FN = re.compile(r'(?<![\w])core_(\d\d)\.(\d{3})_')
LAY_FN = re.compile(r'(?<![\w])(cjs|ci|cs|cf)_(\d\d)\.(\d{3})_')
LAY_ID = re.compile(r'(?<![\w-])(CJS|CI|CS|CF)-(\d{1,2})\.(\d{3})(?!\d)')
LAY_FRAG = re.compile(r'(?<![\w-])(cjs|ci|cs|cf)-(\d{1,2})(\d{3})(?=-)')
RD = re.compile(r'(?<![\d.$/_\w-])(\d{1,2})\.(\d{3})(?![\d\w.])')
def nums(text, path):
    text = SPECIAL_RE.sub(lambda m: (STATS.update(special=1), SPECIAL[m.group(0)])[1], text)
    def cf(m):
        v = int(m.group(1)); nv = newnum(v)
        if nv is None: CROSS.append((path, 'core file prefix ' + m.group(0))); return m.group(0)
        if nv == v: return m.group(0)
        STATS['core_fn'] += 1; return 'core_%02d.%s_' % (nv, m.group(2))
    text = CORE_FN.sub(cf, text)
    def lf(m):
        v = int(m.group(2)); nv = newnum(v)
        if nv is None or nv == v: return m.group(0)
        STATS['lay_fn'] += 1; return '%s_%02d.%s_' % (m.group(1), nv, m.group(3))
    text = LAY_FN.sub(lf, text)
    def li(m):
        v = int(m.group(2)); nv = newnum(v)
        if nv is None or nv == v: return m.group(0)
        STATS['lay_id'] += 1; return '%s-%d.%s' % (m.group(1), nv, m.group(3))
    text = LAY_ID.sub(li, text)
    def lg(m):
        v = int(m.group(2)); nv = newnum(v)
        if nv is None or nv == v: return m.group(0)
        STATS['lay_frag'] += 1; return '%s-%d%s' % (m.group(1), nv, m.group(3))
    text = LAY_FRAG.sub(lg, text)
    if path.endswith('.md'):
        def rd(m):
            v = int(m.group(1)); nv = newnum(v)
            if v > 31: return m.group(0)
            if nv is None:
                STATS['rd_sub'] += 1; return 'S' + SUB[v] + ('' if m.group(2) == '000' else '.' + m.group(2))
            if nv == v: return m.group(0)
            STATS['reader'] += 1; return '%d.%s' % (nv, m.group(2))
        text = RD.sub(rd, text)
    return text
PLACE = [('⟦MAP-UPPER⟧', 'ONE'), ('⟦IB-UPPER⟧', 'SEVEN'), ('⟦MAP⟧', 'Chapter One'), ('⟦IB⟧', 'Chapter Seven'),
         ('chapter-map-constitutional-map', 'chapter-one-constitutional-map'), ('chapter-ib-independent-bodies', 'chapter-seven-independent-bodies')]
def fix(path, text):
    if path in SKIP_FILES: return text
    if path.endswith('.py'):
        t = nums(text, path)
    else:
        t = chain(text, path); t = slugs(t); t = nums(t, path)
    for a, b in PLACE: t = t.replace(a, b)
    return t
changed = rewrite_all(fix, apply=APPLY)
print('files', len(changed), dict(STATS))
json.dump(CROSS, open('/tmp/c_cross.json', 'w'), indent=1)
print('cross', len(CROSS))
# ---- renames
ren = {}
for r, ds, fs in os.walk('.'):
    if any(x in r for x in ('.git', 'archive', 'evidence', 'translations', '_pages_site', 'node_modules', '_local_backup', 'ai_corpus/indexes', 'translation_drafts')): continue
    for f in fs:
        p = os.path.normpath(os.path.join(r, f)); stem = f[:-3] if f.endswith('.md') else None
        if stem in SPECIAL: ren[p] = os.path.join(r, SPECIAL[stem] + '.md'); continue
        m = re.match(r'core_(\d\d)\.(\d{3})_(.*)$', f); m2 = re.match(r'(cjs|ci|cs|cf)_(\d\d)\.(\d{3})_(.*)$', f)
        if m and newnum(int(m.group(1))) not in (None, int(m.group(1))):
            ren[p] = os.path.join(r, 'core_%02d.%s_%s' % (newnum(int(m.group(1))), m.group(2), m.group(3)))
        elif m2 and newnum(int(m2.group(2))) not in (None, int(m2.group(2))):
            ren[p] = os.path.join(r, '%s_%02d.%s_%s' % (m2.group(1), newnum(int(m2.group(2))), m2.group(3), m2.group(4)))
print('renames', len(ren))
if APPLY:
    tmp = {}
    for k, v in ren.items(): os.rename(k, k + '.renum_tmp'); tmp[k + '.renum_tmp'] = v
    for k, v in tmp.items():
        assert not os.path.exists(v), v
        os.rename(k, v)
    print('applied')
else:
    for k, v in sorted(ren.items()): print('  ', k, '->', v)
