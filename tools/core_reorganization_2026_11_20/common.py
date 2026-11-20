"""Shared helpers for the 2026-11-20 core reorganization (one-off record)."""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from local_markdown_fragment_audit import anchors_in, anchor_info, github_slug  # noqa: E402
anchor_info_slugs = anchor_info

SKIP_DIRS = {'.git', '_pages_site', 'archive', 'evidence', 'translations', 'results', 'node_modules',
             '__pycache__', '_local_backup', '_to_delete', 'translation_drafts', 'final_chapter_structure_migration',
             'one_off', 'enforcement_chapter_insertion', 'special_enforcement_chapter_insertion',
             'core_reorganization_2026_11_20'}
SKIP_PATHS = ('ai_corpus/indexes', 'doc_architecture/generated', 'docs/')
EXTS = {'.md', '.json', '.py', '.txt', '.yml', '.yaml', '.sh', '.html', '.js', '.toml', '.csv'}


def walk_text_files(root='.'):
    for r, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            p = os.path.normpath(os.path.join(r, f))
            if p.startswith(SKIP_PATHS):
                continue
            if os.path.splitext(f)[1] not in EXTS and f != 'Makefile':
                continue
            try:
                t = open(p, encoding='utf-8').read()
            except Exception:
                continue
            yield p, t


def rewrite_all(fn, apply=True, root='.'):
    changed = {}
    for p, t in walk_text_files(root):
        n = fn(p, t)
        if n != t:
            changed[p] = n
    if apply:
        for p, n in changed.items():
            open(p, 'w', encoding='utf-8').write(n)
    return changed
