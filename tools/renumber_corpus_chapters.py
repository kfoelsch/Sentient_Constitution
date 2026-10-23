#!/usr/bin/env python3
"""Registry-driven, reversible chapter renumbering operations.

`--report` and `--dry-run` are read-only. `--placeholder` creates reversible
markers and moves chapter files through temporary slots. `--finalize` resolves
the markers from the registry. A current section manifest is required so
fragment rewrites are based on real anchors rather than digit guessing.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from local_markdown_fragment_audit import ATX_HEADING_RE, HTML_ANCHOR_RE, anchor_info, content_lines, github_slug

TEXT_SUFFIXES={'.md','.json','.py','.yaml','.yml','.toml','.html','.js','.ts','.sh','.txt'}
SKIP_PARTS={'.git','_pages_site','archive','evidence','translations','results','node_modules','__pycache__'}
REG='tools/architecture/chapter_numbers.json'
MANIFEST='ai_corpus/indexes/section_manifest.json'

def load(root):
    reg=json.loads((root/REG).read_text()); man=json.loads((root/MANIFEST).read_text())['files']
    return reg,man

def rows_for(reg):
    return [r for r in reg['chapters'] if r['layer']!='CORE']

def source_bases(row):
    values=row.get('legacy_chapter_ids') or ([row['old_id']] if re.fullmatch(r'(?:CJS|CI|CS|CF)-\d+',row['old_id']) else [])
    return values

def id_map(reg):
    grouped={}
    for row in rows_for(reg):
        for base in source_bases(row): grouped.setdefault(base,set()).add(row['display_id'])
        for ident in row.get('legacy_section_ids',[]):
            m=re.match(r'((?:CJS|CI|CS|CF)-\d+)(?:\.(?P<suffix>\d+(?:\.\d+)*[A-Za-z]?))?$',ident)
            if not m or not m.group('suffix'): continue
            display=row['display_id']+f" §{m.group('suffix')}"
            grouped.setdefault(ident,set()).add(display)
    return ({k:next(iter(v)) for k,v in grouped.items() if len(v)==1},
            {k:sorted(v) for k,v in grouped.items() if len(v)>1})

def heading_slugs(text):
    bases=[]
    for lineno,line in content_lines(text):
        m=ATX_HEADING_RE.match(line)
        if m and m.group(2) is not None: bases.append((lineno,github_slug(m.group(2))))
    used=set(); counts={}; result={}
    for lineno,base in bases:
        slug=base; suffix=counts.get(base,1)
        while slug in used:
            slug=f"{base}-{suffix}"; suffix+=1
        used.add(slug); counts[base]=suffix; result[lineno]=slug
    return result

def anchor_maps(root,reg,manifest):
    maps={}
    for r in rows_for(reg):
        bases=source_bases(r)
        if not bases: continue
        source=root/r['original_file']
        if not source.is_file(): continue
        text=source.read_text(); lines=text.splitlines()
        old_info=anchor_info(text); old_real=old_info[0]; old_slugs=heading_slugs(text); old_custom=old_info[2]
        updated=list(lines); sections=manifest.get(r['original_file'],{}).get('sections',[])
        for sec in sections:
            line=sec.get('line_start',0)
            if line<1 or line>len(lines): continue
            header=sec.get('header','')
            match=None
            for base in bases:
                match=re.match(r'('+re.escape(base)+r')(?:\.(?P<suffix>\d+(?:\.\d+)*[A-Za-z]?))?(?P<rest>.*)$',header,re.I)
                if match: break
            if not match: continue
            suffix=match.group('suffix'); visible=r['display_id']+(f" §{suffix}" if suffix else '')+match.group('rest')
            line_match=re.match(r'^(\s{0,3}#{1,6}[ \t]+)(.*)$',lines[line-1])
            if line_match: updated[line-1]=line_match.group(1)+visible
        new_text='\n'.join(updated)+('\n' if text.endswith('\n') else '')
        new_info=anchor_info(new_text); new_slugs=heading_slugs(new_text); vals={}
        for sec in sections:
            line=sec.get('line_start',0); old_anchor=old_slugs.get(line); new_anchor=new_slugs.get(line)
            if old_anchor and new_anchor and old_anchor in old_real: vals[old_anchor]=new_anchor
        for ident,heading_slug in old_custom.items():
            if ident not in old_real: continue
            heading_line=next((ln for ln,slug in old_slugs.items() if slug==heading_slug),None)
            if heading_line in new_slugs: vals[ident]=new_slugs[heading_line]
        # Legacy aliases may be stacked immediately above a heading; map all of
        # them to that heading's actual slug, including aliases not directly adjacent.
        source_lines=text.splitlines()
        for line_no,line in enumerate(source_lines,1):
            for match in HTML_ANCHOR_RE.finditer(line):
                ident=next(group for group in match.groups() if group)
                probe=line_no
                while probe<len(source_lines):
                    candidate=source_lines[probe].strip()
                    if not candidate or re.fullmatch(r'<a\b[^>]*>\s*</a>',candidate,re.I): probe+=1; continue
                    break
                heading_line=probe+1
                if ident in old_real and heading_line in new_slugs: vals[ident]=new_slugs[heading_line]
        maps[r['original_file']]=vals
    return maps

def rewrite_headings(text,row,manifest):
    bases=source_bases(row)
    if not bases: return text
    lines=text.splitlines(keepends=True)
    for sec in manifest.get(row['original_file'],{}).get('sections',[]):
        line=sec.get('line_start',0)
        if line<1 or line>len(lines): continue
        header=sec.get('header',''); match=None
        for base in bases:
            match=re.match(r'('+re.escape(base)+r')(?:\.(?P<suffix>\d+(?:\.\d+)*[A-Za-z]?))?(?P<rest>.*)$',header,re.I)
            if match: break
        if not match or re.search(r'\b(?:CJS|CI|CS|CF)-\d+',match.group('rest'),re.I): continue
        line_match=re.match(r'^(\s{0,3}#{1,6}[ \t]+)(.*?)(\r?\n)?$',lines[line-1])
        if not line_match: continue
        suffix=match.group('suffix'); updated=row['display_id']+(f" §{suffix}" if suffix else '')+match.group('rest')
        lines[line-1]=line_match.group(1)+updated+(line_match.group(3) or '')
    return ''.join(lines)

def walk(root):
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES: continue
        rel=p.relative_to(root)
        if any(part in SKIP_PARTS for part in rel.parts): continue
        if str(rel) in {REG,MANIFEST,'tools/architecture/chapter_crosswalk.json'} or str(rel) in {'project/plans/corpus_chapter_numbering_migration_2026-10-20.md','project/plans/chapter_numbering_phase2_worklist_2026-10-21.txt'} or str(rel).startswith(('project/translation_drafts/','ai_corpus/indexes/','doc_architecture/generated/')): continue
        if str(rel) in {
            'tools/translation_preannouncement.py',
            'tools/renumber_corpus_chapters.py',
            'tools/chapter_number_audit.py',
            'tools/router_table_lib.py',
            'tools/router_bidirectional_sync.py',
            'tools/trace_widget_numbering.py',
            'tools/test_chapter_numbering_migration.py',
        }: continue
        yield p

def file_pairs(reg):
    return [(r['original_file'],r['destination_file'],i) for i,r in enumerate(reg['chapters'])]

def do_report(root,reg,manifest):
    unique,shared=id_map(reg); pairs=file_pairs(reg); anchors=anchor_maps(root,reg,manifest)
    files=list(walk(root)); total_refs=0; total_ids=0
    names={Path(a).name:b for a,b,_ in pairs}
    for p in files:
        t=p.read_text(errors='ignore')
        total_refs+=sum(t.count(a) for a,_,_ in pairs)
        total_ids+=sum(len(re.findall(r'(?<![A-Za-z0-9-])'+re.escape(k)+r'(?:\.\d+[A-Za-z]?)?(?![A-Za-z0-9-])',t)) for k in unique)
    print(f"registry: {len(reg['chapters'])} rows ({sum(r['layer']=='CORE' for r in reg['chapters'])} core, {sum(r['layer']!='CORE' for r in reg['chapters'])} corpus)")
    print(f"operative text files scanned: {len(files)}; legacy file-name occurrences: {total_refs}; uniquely mappable chapter-id occurrences: {total_ids}")
    ambiguous=shared
    print(f"shared legacy ids/sections requiring file-qualified resolution: {len(ambiguous)}; real source anchors indexed: {sum(len(v) for v in anchors.values())}")
    for old,displays in sorted(ambiguous.items()):
        print(f"  AMBIGUOUS {old}: {', '.join(displays)}")
    range_re=re.compile(r'\b(?:CJS|CI|CS|CF)-(?:\d{1,2})(?:\.\d+[A-Za-z]?)?\s*(?:to|through|–|—)\s*(?:CJS|CI|CS|CF)-(?:\d{1,2})(?:\.\d+[A-Za-z]?)?',re.I)
    slash_re=re.compile(r'\b(?:CJS|CI|CS|CF)-\d{1,2}\.\d+[A-Za-z]?(?:\s*/\s*\d+[A-Za-z]?)+',re.I)
    review=[]
    for p in files:
        try: lines=p.read_text(errors='ignore').splitlines()
        except OSError: continue
        for no,line in enumerate(lines,1):
            if range_re.search(line) or slash_re.search(line):
                review.append((p.relative_to(root).as_posix(),no,line.strip()))
    print(f"range/list expressions for manual review: {len(review)}")
    for file,no,line in review: print(f"  {file}:{no}: {line[:300]}")
    print('planned file renames:')
    for a,b,_ in pairs:
        if (root/a).exists(): print(f"  {a} -> {b}")

def replace_text(root, reg, manifest, mode):
    unique,shared=id_map(reg); shared_items=list(shared.items()); pairs=file_pairs(reg)
    if mode=='finalize':
        cross=json.loads((root/'tools/architecture/chapter_crosswalk.json').read_text())
        amap={x['source_file']:{a['old_anchor']:a['new_anchor'] for a in x['anchors']} for x in cross.get('anchor_maps',[])}
    else: amap=anchor_maps(root,reg,manifest)
    file_token={a:f'⟦CHFILE:{i}⟧' for a,_,i in pairs}
    final_path={f'⟦CHFILE:{i}⟧':b for a,b,i in pairs}
    base_token={Path(a).name:f'⟦CHBASE:{i}⟧' for a,_,i in pairs}
    final_base={f'⟦CHBASE:{i}⟧':Path(b).name for a,b,i in pairs}
    index_by_display={r['display_id']:i for i,r in enumerate(reg['chapters'])}
    id_token={k:f"⟦CHID:{index_by_display[v.split(' §',1)[0]]}⟧"+(f".{v.split(' §',1)[1]}" if ' §' in v else '') for k,v in unique.items()}
    id_pattern=re.compile(r'(?<![A-Za-z0-9-])(?:'+ '|'.join(re.escape(k) for k in sorted(id_token,key=len,reverse=True))+r')(?![A-Za-z0-9-])') if id_token else None
    ambiguous_pattern=re.compile(r'(?<![A-Za-z0-9-])(?:'+ '|'.join(re.escape(k) for k,_ in sorted(shared.items(),key=lambda x:-len(x[0])))+r')(?![A-Za-z0-9-])') if shared else None
    ambiguous_index={k:i for i,(k,_) in enumerate(shared_items)}
    row_by_name={Path(r['original_file']).name:r for r in rows_for(reg)}
    for p in list(walk(root)):
        try: text=p.read_text()
        except UnicodeDecodeError: continue
        original=text
        preserve_historical_ids=str(p.relative_to(root)) in {'doc_architecture.md','project/MEMLOG.md','TODO.md'}
        if mode=='placeholder':
            def map_link(m):
                label,target=m.group(1),m.group(2)
                target_file=Path(target.split('#',1)[0]).name
                row=row_by_name.get(target_file)
                if row and not re.search(r'(?:^|/)translations/[a-z]{2,3}/',target,re.I):
                    for old in source_bases(row):
                        label=re.sub(r'(?<![A-Za-z0-9-])'+re.escape(old)+r'(?P<suffix>(?:\.\d+[A-Za-z]?)+)?(?![A-Za-z0-9-])',lambda x:f"⟦CHID:{next(i for i,r in enumerate(reg['chapters']) if r is row)}⟧"+(x.group('suffix') or ''),label)
                return '['+label+']('+target+')'
            if not preserve_historical_ids: text=re.sub(r'\[([^]\n]*)\]\(([^)\n]*)\)',map_link,text)
        if mode == 'finalize' and not preserve_historical_ids:
            for tok,new in final_path.items(): text=text.replace(tok,new)
            for tok,new in final_base.items(): text=text.replace(tok,new)
            text=re.sub(r'⟦CHID:(\d+)⟧((?:\.\d+[A-Za-z]?)+)?',lambda m:reg['chapters'][int(m.group(1))]['display_id']+(f" §{m.group(2)[1:]}" if m.group(2) else ''),text)
            shared_items=list(id_map(reg)[1].items())
            def list_display(values): return values[0] if len(values)==1 else (', '.join(values[:-1])+', and '+values[-1] if len(values)>2 else ' and '.join(values))
            text=re.sub(r'⟦CHAMBIG:(\d+)⟧',lambda m:list_display(shared_items[int(m.group(1))][1]),text)
            # Restore mapped fragments from the source manifest.
            for source, vals in amap.items():
                index=next(i for a,b,i in pairs if source in (a,b))  # crosswalk uses dotted destination names
                for j,old_anchor in enumerate(vals):
                    token=f'⟦CHANCHOR:{index}:{j}⟧'; text=text.replace(token,'#'+list(vals.values())[j])
        elif mode == 'placeholder' and not preserve_historical_ids:
            if id_pattern:
                text=''.join(line if ATX_HEADING_RE.match(line.rstrip('\r\n')) else id_pattern.sub(lambda m:id_token[m.group(0)],line) for line in text.splitlines(keepends=True))
            if p.suffix.lower()=='.md' and ambiguous_pattern:
                text=''.join(line if ATX_HEADING_RE.match(line.rstrip('\r\n')) else ambiguous_pattern.sub(lambda m:f"⟦CHAMBIG:{ambiguous_index[m.group(0)]}⟧",line) for line in text.splitlines(keepends=True))
            row_for_file=row_by_name.get(p.name)
            if row_for_file: text=rewrite_headings(text,row_for_file,manifest)
            for old,tok in sorted(file_token.items(),key=lambda x:-len(x[0])):
                index=next(i for a,b,i in pairs if a==old)
                layer=reg['chapters'][index]['layer']
                if layer=='CORE':
                    text=re.sub(re.escape(old),lambda m:m.group(0) if re.search(r'translations/[a-z]{2,3}/$',text[max(0,m.start()-40):m.start()],re.I) else tok,text)
                else: text=text.replace(old,tok)
            for old,tok in sorted(base_token.items(),key=lambda x:-len(x[0])):
                index=next(i for a,b,i in pairs if Path(a).name==old)
                layer=reg['chapters'][index]['layer']
                if layer=='CORE':
                    text=re.sub(re.escape(old),lambda m:m.group(0) if re.search(r'translations/[a-z]{2,3}/$',text[max(0,m.start()-40):m.start()],re.I) else tok,text)
                else: text=text.replace(old,tok)
            # Rewrite only fragments verified from the manifest and only in links to their source file.
            for source, vals in amap.items():
                tok=file_token.get(source)
                if not tok: continue
                pattern=r'(\]\([^)]*⟦CH(?:FILE|BASE):'+str(next(i for a,b,i in pairs if a==source))+r'⟧)(?P<frag>#[^ )]+)?'
                def repl(m):
                    frag=m.group('frag')
                    anchor=frag[1:] if frag else ''
                    if frag and anchor in vals: frag='⟦CHANCHOR:'+str(next(i for a,b,i in pairs if a==source))+':'+str(list(vals).index(anchor))+'⟧'
                    return m.group(1)+(frag or '')
                text=re.sub(pattern,repl,text)
            if row_for_file:
                source=row_for_file['original_file']; vals=amap.get(source,{})
                index=next(i for a,b,i in pairs if source in (a,b))  # crosswalk uses dotted destination names
                for j,old_anchor in enumerate(vals):
                    text=text.replace(f'](#{old_anchor})',f'](⟦CHANCHOR:{index}:{j}⟧)')
                original_file=root/source
                if original_file.is_file():
                    custom={next(group for group in m.groups() if group) for line in original_file.read_text().splitlines() for m in HTML_ANCHOR_RE.finditer(line)}
                    for old_anchor in custom.intersection(vals):
                        text=re.sub(r'<a\b(?=[^>]*\bid=["\']'+re.escape(old_anchor)+r'["\'])[^>]*>\s*</a>', '', text, flags=re.I)
        if text!=original: p.write_text(text)

def rename_files(root, reg, direction):
    pairs=file_pairs(reg)
    if direction=='preflight':
        active=[(root/a,root/b,i) for a,b,i in pairs if (root/a).exists()]
        sources={src for src,_,_ in active}
        for src,dst,i in active:
            if dst.exists() and dst not in sources: raise RuntimeError(f'destination already exists: {dst}')
            tmp=src.with_name(f'.chapter-number-{i:03d}.tmp')
            if tmp.exists(): raise RuntimeError(f'temporary slot already exists: {tmp}')
        return
    active=[]
    for old,new,i in pairs:
        src,dst=(root/old,root/new) if direction=='forward' else (root/new,root/old)
        if src.exists(): active.append((src,dst,i))
    sources={src for src,_,_ in active}
    for src,dst,i in active:
        if dst.exists() and dst not in sources: raise RuntimeError(f'destination already exists: {dst}')
        tmp=src.with_name(f'.chapter-number-{i:03d}.tmp')
        if tmp.exists(): raise RuntimeError(f'temporary slot already exists: {tmp}')
    temps=[]
    for src,dst,i in active:
        tmp=src.with_name(f'.chapter-number-{i:03d}.tmp')
        if tmp.exists(): raise RuntimeError(f'temporary slot already exists: {tmp}')
        src.rename(tmp); temps.append((tmp,dst))
    for tmp,dst in temps:
        dst.parent.mkdir(parents=True,exist_ok=True)
        if dst.exists(): raise RuntimeError(f'destination already exists: {dst}')
        tmp.rename(dst)

def add_core_home_lines(root, reg):
    for row in rows_for(reg):
        path=root/row['destination_file']
        if not path.is_file(): continue
        text=path.read_text()
        declaration=f"Core home: {row['core_home']}"
        if declaration in text: continue
        lines=text.splitlines(keepends=True)
        if not lines: lines=["# " + row['title'] + "\n"]
        lines.insert(1, declaration + "\n")
        path.write_text(''.join(lines))

def verify_tree(root,reg):
    problems=[]
    for row in reg['chapters']:
        if not (root/row['destination_file']).is_file(): problems.append(f"missing destination: {row['destination_file']}")
    old_bases=sorted({base for row in rows_for(reg) for base in source_bases(row)},key=len,reverse=True)
    valid_display={row['display_id'] for row in rows_for(reg)}
    old_names=sorted({Path(row['original_file']).name for row in reg['chapters']},key=len,reverse=True)
    markers=re.compile(r'⟦CH(?:ID|FILE|BASE|ANCHOR|AMBIG):')
    for path in walk(root):
        rel=path.relative_to(root).as_posix()
        try:text=path.read_text(errors='ignore')
        except OSError:continue
        if markers.search(text): problems.append(f"unresolved placeholder: {rel}")
        # D7 preserves historical identifiers in the architecture move log,
        # MEMLOG, TODO and dated steward sign-off record. Link targets are checked
        # by link audits; operative citations remain subject to this verifier.
        historical = {'doc_architecture.md','project/MEMLOG.md','TODO.md',
                      'project/reviews/D04_emergency_signoff_2026-10-20.md'}
        if rel not in historical:
            for name in old_names:
                if name in text: problems.append(f"stale filename {name}: {rel}")
        if rel in historical: continue
        for base in old_bases:
            pattern=r'(?<![A-Za-z0-9-])'+re.escape(base)+r'(?:\.\d+(?:\.\d+)*[A-Za-z]?)?(?![A-Za-z0-9-])'
            for match in re.finditer(pattern,text,re.I):
                if match.group(0) not in valid_display:
                    problems.append(f"stale legacy id {match.group(0)}: {rel}")
    print(f"chapter migration verification: {len(problems)} findings")
    for problem in problems[:100]:print('  '+problem)
    return 1 if problems else 0

def main():
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--report',action='store_true'); mode.add_argument('--dry-run',action='store_true')
    mode.add_argument('--placeholder',action='store_true'); mode.add_argument('--finalize',action='store_true')
    mode.add_argument('--verify',action='store_true')
    ap.add_argument('--root',type=Path,default=Path.cwd())
    a=ap.parse_args(); root=a.root.resolve(); reg,man=load(root)
    if a.report or a.dry_run: do_report(root,reg,man); return 0
    if a.placeholder:
        rename_files(root,reg,'preflight')
        replace_text(root,reg,man,'placeholder'); rename_files(root,reg,'forward'); return 0
    if a.finalize:
        rename_files(root,reg,'forward'); replace_text(root,reg,man,'finalize'); add_core_home_lines(root,reg); return 0
    return verify_tree(root,reg)
if __name__=='__main__': raise SystemExit(main())
