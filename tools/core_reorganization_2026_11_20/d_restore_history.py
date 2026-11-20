#!/usr/bin/env python3
"""Phase D: restore historical records (project plans, reviews, analysis, trials, MEMLOG, SHELVED,
plain-language drafts) to their pre-reorganization prose. Only link targets move: file names,
corpus ids and corpus fragments follow the renumbering; section fragments are retargeted afterwards
by tools/fossil_anchor_audit.py --write. Prose chapter numbers stay as written at the time.
usage: d_restore_history.py BASE_SHA
"""
import re, subprocess, sys
BASE = sys.argv[1]
PREFIXES = ('project/plans/', 'project/reviews/', 'project/analysis/', 'project/trials/', 'project/plain_language/',
            'project/MEMLOG.md', 'project/SHELVED.md')
def newnum(n):
    if n == 0: return 0
    if n == 1: return 2
    if n in (2, 3, 4): return None
    if 5 <= n <= 8: return n - 2
    if 9 <= n <= 31: return n - 1
    return n
SPECIAL = {'core_00.500_constitutional_map': 'core_01.000_constitutional_map',
           'core_08.500_independent_bodies': 'core_07.000_independent_bodies',
           'core_02.000_definition_structure': 'subcore_03.010_definition_structure',
           'core_03.000_definition_integrity': 'subcore_03.020_definition_integrity',
           'core_04.000_burden_traceability_verification': 'subcore_03.030_burden_traceability_verification'}
SPECIAL_RE = re.compile('|'.join(re.escape(k) for k in SPECIAL))
CORE_FN = re.compile(r'(?<![\w])core_(\d\d)\.(\d{3})_')
LAY_FN = re.compile(r'(?<![\w])(cjs|ci|cs|cf)_(\d\d)\.(\d{3})_')
LINK = re.compile(r'\]\(([^)\s]+)\)')
def target(t):
    t = SPECIAL_RE.sub(lambda m: SPECIAL[m.group(0)], t)
    t = CORE_FN.sub(lambda m: m.group(0) if newnum(int(m.group(1))) in (None, int(m.group(1))) else 'core_%02d.%s_' % (newnum(int(m.group(1))), m.group(2)), t)
    return LAY_FN.sub(lambda m: m.group(0) if newnum(int(m.group(2))) in (None, int(m.group(2))) else '%s_%02d.%s_' % (m.group(1), newnum(int(m.group(2))), m.group(3)), t)
files = subprocess.run(['git', 'diff', '--name-only', BASE, 'HEAD', '--', *PREFIXES], capture_output=True, text=True).stdout.split()
for f in files:
    old = subprocess.run(['git', 'show', f'{BASE}:{f}'], capture_output=True, text=True).stdout
    if not f.endswith('.md'):
        continue  # data files keep the renumbered form (manifests and reports are regenerated)
    new = LINK.sub(lambda m: '](' + target(m.group(1)) + ')', old)
    open(f, 'w').write(new)
    print('restored', f)
