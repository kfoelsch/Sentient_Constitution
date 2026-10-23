#!/usr/bin/env python3
"""Generate a reader-facing Chapter One to Chapter Five map from the latest trace matrix."""
from __future__ import annotations
import argparse, csv, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from definition_index import collect_ch5_entries_with_apex

FILES=('core_01.000_values_principles.md','core_01.005_interaction_interpretation.md','core_01.010_stewardship_capacity_principles.md')
def slug(text: str) -> str:
    text=text.lower().replace('&','and')
    text=re.sub(r'[^a-z0-9]+','-',text).strip('-')
    return text

def anchors(root: Path) -> dict[str,str]:
    out={}
    for name in FILES:
        pending=''
        for line in (root/name).read_text(encoding='utf-8').splitlines():
            a=re.match(r'^<a id="([^"]+)"',line.strip())
            if a: pending=a.group(1)
            m=re.match(r'^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s+',line)
            if m:
                out[m.group(1)]=pending or slug(m.group(1)+' '+re.match(r'^#{2,6}\s+\d+(?:\.\d+)*\.?\s+(.*)$',line).group(1))
                pending=''
    return out

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output',default='project/plain_language/PRINCIPLE_TO_DEFINITIONS_MAP.md'); args=ap.parse_args()
    root=Path(args.root); files=sorted((root/'evidence').glob('*/ch1_ch5_traceability_matrix_*.csv'),reverse=True)
    if not files: raise SystemExit('No Chapter One–Five traceability matrix found; run make ch1-ch5-alignment-audit first.')
    source=files[0]; rows=list(csv.DictReader(source.open(encoding='utf-8-sig',newline=''))); defs=[x for x in rows[0].keys() if x not in ('Principle','Title')]
    amap=anchors(root); sections={}
    for name in FILES:
        pending=''
        for line in (root/name).read_text(encoding='utf-8').splitlines():
            a=re.match(r'^<a id="([^"]+)"',line.strip())
            if a: pending=a.group(1)
            m=re.match(r'^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s+(.*)$',line)
            if m:
                sections[m.group(1)]=(name,m.group(2).strip())
                pending=''
    definitions={e.term.casefold():e for e in collect_ch5_entries_with_apex(root)}
    out=['# Chapter One principles → Chapter Five definitions','',f'Generated from [`{source.relative_to(root)}`](../../{source.relative_to(root)}). This is a navigation aid generated from the Chapter One–Five traceability matrix; it does not add duties or replace source text.','', '| Principle | Definitions linked by the matrix |','|---|---|']
    for row in rows:
        n=row['Principle'].strip(); title=row['Title'].strip(); linkdata=sections.get(n)
        if linkdata:
            f,t=linkdata; p=f'[{n} {title}](../../{f}#{amap.get(n, slug(n+" "+title))})'
        else: p=f'{n} {title}'
        names=[d for d in defs if row.get(d,'').strip() in ('✓','⚠')]
        if names:
            # Definition targets are resolved from canonical Chapter Five headings/anchors.
            links=[]
            for d in names:
                term=re.sub(r'^Def\.[A-Z0-9]+\s+','',d).casefold()
                e=definitions.get(term)
                mark='⚠ ' if row.get(d,'').strip()=='⚠' else ''
                if e: links.append(f'{mark}[{d}](../../{e.source_file}#{e.anchor.lstrip("#")})')
                else: links.append(f'{mark}{d}')
            out.append(f"| {p} | {'; '.join(links)} |")
        else: out.append(f'| {p} | — |')
    dest=root/args.output; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(f'Wrote {dest} from {source}')
if __name__=='__main__': main()
