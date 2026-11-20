#!/usr/bin/env python3
"""Phase D: retarget fragments the renumbering left dangling.
Reads tools/local_markdown_fragment_audit.py output. For each missing fragment:
- chapter-word slugs and corpus id fragments follow the chapter renumbering;
- Chapter Six (old Eight) §11 now lives in Chapter Seven §3; Preamble §4-§9 now live in Chapter One;
- otherwise a numbered fragment is retargeted to the one id in the target file with the same title slug.
usage: d_fix_fragments.py [--apply]
"""
import collections, os, re, subprocess, sys
APPLY = '--apply' in sys.argv
W = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
def word(n): return W[n] if n <= 20 else 'twenty-' + W[n - 20]
W2N = {word(n): n for n in range(0, 32)}
def newnum(n):
    if n == 0: return 0
    if n == 1: return 2
    if n in (2, 3, 4): return None
    if 5 <= n <= 8: return n - 2
    if 9 <= n <= 31: return n - 1
    return n
SLUG = re.compile(r'^chapter-(%s)(?=-)' % '|'.join(sorted(W2N, key=len, reverse=True)))
FRAG = re.compile(r'^(cjs|ci|cs|cf)-(\d{1,2})(\d{3})(?=-)')
IDS = re.compile(r'<a id="([^"]+)"')
HEAD = re.compile(r'^#{1,6}\s+(.*)$', re.M)
def gh(s):
    s = s.strip().lower(); s = re.sub(r'[^\w\- ]', '', s); return s.replace(' ', '-')
_cache = {}
def ids(path):
    if path not in _cache:
        t = open(path, encoding='utf-8').read()
        _cache[path] = set(IDS.findall(t)) | {gh(h) for h in HEAD.findall(t)}
    return _cache[path]
def tail(a): return re.sub(r'^\d+-', '', a)
out = subprocess.run([sys.executable, 'tools/local_markdown_fragment_audit.py', '--root', '.'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True).stdout
pat = re.compile(r'^\s+(\S+):(\d+) — missing-fragment: fragment #(\S+) is absent from (\S+) \((\S+)\)$')
edits = collections.defaultdict(list); unresolved = []
for line in out.splitlines():
    m = pat.match(line)
    if not m: continue
    src, ln, frag, tgt, href = m.groups()
    if src.startswith('doc_architecture/generated/'): continue
    newfile, newfrag = None, None
    if SLUG.match(frag):
        v = W2N[SLUG.match(frag).group(1)]; nv = newnum(v)
        if nv: newfrag = frag.replace(word(v), word(nv), 1)
    elif FRAG.match(frag):
        mm = FRAG.match(frag); nv = newnum(int(mm.group(2)))
        if nv: newfrag = '%s-%d%s' % (mm.group(1), nv, mm.group(3)) + frag[mm.end():]
    if tgt.startswith('core_06.000_functional') and re.match(r'^11\d*-', frag):
        newfile = 'core_07.000_independent_bodies.md'; newfrag = '3-what-makes-a-body-independent' if frag == '11-independent-bodies' else '3' + frag[2:]
    if tgt == 'core_00.000_preamble.md' and re.match(r'^[4-9]\d*-', frag):
        newfile = 'core_01.000_constitutional_map.md'; newfrag = frag
    if newfrag is None or newfrag not in ids(newfile or tgt):
        cand = [a for a in ids(newfile or tgt) if re.match(r'^\d', a) and tail(a) == tail(newfrag or frag)]
        if not cand: cand = [a for a in ids(newfile or tgt) if re.match(r'^\d', a) and tail(a).endswith('-' + tail(newfrag or frag))]
        if len(cand) == 1: newfrag = cand[0]
        elif newfrag is None or newfrag not in ids(newfile or tgt):
            unresolved.append(line.strip()); continue
    base = href.split('#')[0]
    nhref = (base.replace(os.path.basename(tgt), newfile) if newfile else base) + '#' + newfrag
    edits[src].append((int(ln), href, nhref))
for src, es in edits.items():
    lines = open(src, encoding='utf-8').read().split('\n')
    for ln, a, b in es:
        lines[ln - 1] = lines[ln - 1].replace('(' + a + ')', '(' + b + ')')
    if APPLY: open(src, 'w', encoding='utf-8').write('\n'.join(lines))
print('fixed', sum(len(v) for v in edits.values()), 'in', len(edits), 'files; unresolved', len(unresolved))
for u in unresolved: print(' ', u[:240])
