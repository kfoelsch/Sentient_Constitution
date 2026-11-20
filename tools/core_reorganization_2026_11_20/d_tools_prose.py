#!/usr/bin/env python3
"""Phase D: renumber chapter words and chapter slugs inside the live audit and generator tools.
Phase C changed only file names and ids in .py files; expected strings and messages that name chapters
("Chapter Five", "chapter-five-...") follow the renumbering here. Old Chapters Two to Four are reported for
manual review. Skips one-off and migration folders, which record history.
usage: d_tools_prose.py [--apply]
"""
import glob, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'c_renumber.py')).read()
src = src.split('changed = rewrite_all')[0]
sys.argv = [sys.argv[0]] + [a for a in sys.argv[1:] if a != '--apply'] + ([] if '--apply' not in sys.argv else [])
APPLY = '--apply' in sys.argv[1:] or os.environ.get('APPLY') == '1'
sys.path.insert(0, HERE)
ns = {'__name__': 'c_renumber_lib'}
exec(compile(src, 'c_renumber.py', 'exec'), ns)
SKIP = ('tools/one_off/', 'tools/final_chapter_structure_migration/', 'tools/core_reorganization_2026_11_20/')
n = 0
for f in sorted(glob.glob('tools/**/*.py', recursive=True)):
    if f.startswith(SKIP): continue
    t = open(f, encoding='utf-8').read()
    before = len(ns['CROSS'])
    t2 = ns['slugs'](ns['chain'](t, f))
    for c in ns['CROSS'][before:]: print('CROSS', c)
    if t2 != t:
        n += 1
        print('changed', f)
        if APPLY: open(f, 'w', encoding='utf-8').write(t2)
print('files', n)
