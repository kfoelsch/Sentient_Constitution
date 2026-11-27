#!/usr/bin/env python3
"""Plan or apply a mapped section migration; default is a read-only dry run.

The JSON spec names the chapter files, a per-top-section mapping, and optional
physical moves. Links are resolved against their original file and rewritten
only when their target is an inventoried section. Ambiguous prose and anchors
are listed for human review. This tool does not certify unchanged meaning.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from local_markdown_fragment_audit import github_slug

HEAD = re.compile(r'^(#{3,6}) (\d+(?:\.\d+)*)(\.?) (.+?)\s*$')
ANCHOR = re.compile(r'^<a id="([^"]+)"></a>\s*$')
LINK = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')
SKIP = ('translations/', 'project/translation_drafts/', 'archive/', 'evidence/',
        'evaluation/results/', 'ai_corpus/indexes/', 'doc_architecture/generated/',
        '_pages_site/', '_local_backup/')


def make_plan(root: Path, spec: dict) -> tuple[dict[str, str], dict]:
    files = spec['chapter_files']
    mapping = spec['sections']
    moves = spec.get('moves', [])
    original = {f: (root / f).read_text(encoding='utf-8') for f in files}
    line_dest: dict[tuple[str, int], str] = {}
    bounds = []
    for move in moves:
        src, dst = move['source'], move['destination']
        lines = original[src].splitlines(keepends=True)
        starts = [i for i, line in enumerate(lines) if line.rstrip('\r\n') == move['start']]
        ends = [i for i, line in enumerate(lines) if line.rstrip('\r\n') == move['end'] and i > (starts[0] if starts else len(lines))]
        if len(starts) != 1 or len(ends) != 1:
            raise ValueError(f"move markers must uniquely delimit a block: {src}")
        a, b = starts[0], ends[0]
        for i in range(a, b):
            if (src, i) in line_dest:
                raise ValueError('overlapping moves')
            line_dest[src, i] = dst
        bounds.append((move, a, b))

    # Key by source file and fragment: section numbers are not globally unique.
    targets = {}
    headings = {}
    for file, text in original.items():
        lines = text.splitlines(keepends=True)
        fence = False
        for i, line in enumerate(lines):
            if line.lstrip().startswith('```'):
                fence = not fence
            if fence:
                continue
            h = HEAD.match(line.rstrip('\r\n'))
            if not h:
                continue
            level, num, dot, title = h.groups()
            top, *suffix = num.split('.')
            rule = mapping.get(top, {})
            newnum = '.'.join([str(rule.get('number', top)), *suffix])
            newfile = line_dest.get((file, i), file)
            if rule.get('file') and newfile != rule['file']:
                raise ValueError(f'heading {file}:{i+1} does not reach mapped file {rule["file"]}')
            oldslug = github_slug(f'{num}{dot} {title}')
            newslug = github_slug(f'{newnum}{dot} {title}')
            entry = (newfile, newslug, num, newnum)
            key = (file, oldslug)
            if key in targets:
                raise ValueError(f'duplicate heading anchor {key}')
            targets[key] = entry
            headings[file, i] = f'{level} {newnum}{dot} {title}' + ('\n' if line.endswith('\n') else '')
            j = i - 1
            while j >= 0 and ANCHOR.match(lines[j].rstrip('\r\n')):
                aid = ANCHOR.match(lines[j].rstrip('\r\n')).group(1)
                # Explicit aliases need an unambiguous numeric prefix or a spec override.
                alias = spec.get('aliases', {}).get(f'{file}#{aid}')
                if alias:
                    newaid = alias
                elif aid == oldslug:
                    newaid = newslug
                else:
                    oldprefix = num.replace('.', '')
                    newprefix = newnum.replace('.', '')
                    newaid = newprefix + aid[len(oldprefix):] if aid.startswith(oldprefix + '-') else aid
                targets[file, aid] = (newfile, newaid, num, newnum)
                j -= 1

    tracked = subprocess.check_output(['git', 'ls-files', '-z', '--', '*.md'], cwd=root).decode().split('\0')
    tracked = [p for p in tracked if p and not p.startswith(SKIP)]
    outputs = {}
    review = []
    counts = {'links': 0, 'headings': 0, 'anchors': 0}
    for file in tracked:
        text = original.get(file)
        if text is None:
            text = (root / file).read_text(encoding='utf-8')
        lines = text.splitlines(keepends=True)
        out = []
        for i, line in enumerate(lines):
            destfile = line_dest.get((file, i), file)
            if (file, i) in headings:
                line = headings[file, i]
                counts['headings'] += 1
            else:
                a = ANCHOR.match(line.rstrip('\r\n'))
                if a and (file, a.group(1)) in targets:
                    new = targets[file, a.group(1)][1]
                    if new != a.group(1):
                        line = line.replace(f'id="{a.group(1)}"', f'id="{new}"')
                        counts['anchors'] += 1
            def change(m):
                label, target, title = m.groups()
                if '://' in target or target.startswith(('mailto:', '<')) or '#' not in target:
                    return m.group(0)
                path, frag = target.split('#', 1)
                source = os.path.normpath(os.path.join(os.path.dirname(file), path)) if path else file
                entry = targets.get((source, frag))
                if not entry:
                    if file != destfile and not path:
                        review.append({'kind': 'unmapped local link in moved block', 'file': file, 'line': i+1, 'text': m.group(0)})
                    return m.group(0)
                newfile, newfrag, oldnum, newnum = entry
                newpath = '' if newfile == destfile else os.path.relpath(newfile, os.path.dirname(destfile) or '.')
                newtarget = newpath + '#' + newfrag
                # Change a citation label only when its number names this target or an ancestor.
                def relabel(n):
                    val = n.group(2)
                    if val == oldnum or oldnum.startswith(val + '.'):
                        oldtop, *tail = val.split('.')
                        newtop = newnum.split('.')[0]
                        return n.group(1) + '.'.join([newtop, *tail])
                    return n.group(0)
                label = re.sub(r'(§\s*)(\d+(?:\.\d+)*)', relabel, label)
                if newtarget != target or label != m.group(1):
                    counts['links'] += 1
                return f'[{label}]({newtarget}{title})'
            line = LINK.sub(change, line)
            stripped = LINK.sub('', line)
            if re.search(r'§§?\s*\d', stripped) and (file in files or re.search(spec.get('review_pattern', r'Chapter\s+Two'), stripped, re.I)):
                review.append({'kind': 'unlinked citation or range', 'file': file, 'line': i+1, 'text': stripped.strip()[:250]})
            out.append(line)
        new = ''.join(out)
        if new != text or file in files:
            outputs[file] = new

    # Relocate already rewritten lines. Descending indices preserve original boundaries.
    pieces = []
    for move, a, b in sorted(bounds, key=lambda x: (x[0]['source'], x[1]), reverse=True):
        src = move['source']
        lines = outputs[src].splitlines(keepends=True)
        pieces.append((move, ''.join(lines[a:b])))
        outputs[src] = ''.join(lines[:a] + lines[b:])
    for move, block in pieces:
        dst = move['destination']
        marker = move['before']
        marker_anchor = ANCHOR.match(marker)
        if marker_anchor and (dst, marker_anchor.group(1)) in targets:
            mapped_anchor = targets[dst, marker_anchor.group(1)][1]
            marker = f'<a id="{mapped_anchor}"></a>'
        lines = outputs[dst].splitlines(keepends=True)
        matches = [i for i, line in enumerate(lines) if line.rstrip('\r\n') == marker]
        if len(matches) != 1:
            raise ValueError(f'destination marker must be unique: {dst}: {marker}')
        pos = matches[0]
        outputs[dst] = ''.join(lines[:pos]) + block + ''.join(lines[pos:])
    outputs = {p: s for p, s in outputs.items() if s != (root / p).read_text(encoding='utf-8')}
    return outputs, {'counts': counts, 'files_changed': sorted(outputs), 'review': review,
                     'anchor_map': {f'{f}#{a}': f'{v[0]}#{v[1]}' for (f, a), v in targets.items() if (f, a) != (v[0], v[1])}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--spec', required=True, type=Path)
    parser.add_argument('--report', type=Path, help='write JSON report to this path')
    parser.add_argument('--write', action='store_true', help='apply plan; default is dry run')
    args = parser.parse_args()
    root = args.root.resolve()
    spec = json.loads(args.spec.read_text(encoding='utf-8'))
    outputs, report = make_plan(root, spec)
    print(json.dumps({'mode': 'write' if args.write else 'dry-run', 'counts': report['counts'],
                      'files_changed': len(outputs), 'review_items': len(report['review'])}, indent=2))
    if args.report:
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if args.write:
        if subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=root).strip():
            raise SystemExit('refusing to write: tracked files have uncommitted changes')
        for path, content in outputs.items():
            (root / path).write_text(content, encoding='utf-8')

if __name__ == '__main__':
    main()
