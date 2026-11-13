#!/usr/bin/env python3
"""One-off Chapter One Part splitter (492nd move). usage: split_parts.py ROOT SPEC.json [--apply]
Splits core files into Parts at section boundaries, rewrites every link/filename/reader-number
repo-wide in one pass, fixes footer chains. Prints a report."""
import os,re,sys,json,collections
root=sys.argv[1]; spec=json.load(open(sys.argv[2])); apply='--apply' in sys.argv
os.chdir(root)
def slug(t):
    t=re.sub(r'<[^>]+>','',t); t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t).strip().lower()
    t=re.sub(r'[^\w\- ]','',t,flags=re.U); return t.replace(' ','-')
SEC=re.compile(r'^### (\d+)\. ')
ANCH=re.compile(r'^<a id="[^"]+"></a>\s*$')
def parse(path):
    L=open(path,encoding='utf-8').read().split('\n')
    # footer
    fi=next((i for i,l in enumerate(L) if l.startswith('**Previous file:**')),len(L))
    j=fi
    while j>0 and (L[j-1].strip() in ('','---')): j-=1
    footer=L[j:]; body=L[:j]
    starts=[]
    for i,l in enumerate(body):
        m=SEC.match(l)
        if m:
            s=i
            while s>0 and (body[s-1].strip()=='' or ANCH.match(body[s-1])): s-=1
            starts.append((int(m.group(1)),s))
    header=body[:starts[0][1]]
    blocks={}
    for k,(n,s) in enumerate(starts):
        e=starts[k+1][1] if k+1<len(starts) else len(body)
        blocks[n]=body[s:e]
    return header,blocks,footer
def anchors_in(lines,seen=None):
    out=set(); fence=False; seen=seen if seen is not None else collections.Counter()
    for l in lines:
        if l.startswith('```'): fence=not fence
        if fence: continue
        for a in re.findall(r'<a id="([^"]+)"',l): out.add(a)
        m=re.match(r'^(#{1,6}) (.*)',l)
        if m:
            s=slug(m.group(2)); n=seen[s]; seen[s]+=1; out.add(s if n==0 else f"{s}-{n}")
    return out
# --- plan
fmap={}      # anchor-> dest file, per source name
first={}     # source name -> first dest file
rd_by_sec={} # (source reader, sec)-> dest reader
rd_first={}  # source reader -> first dest reader
dest_content={}; report=collections.Counter()
for src,sp in spec['sources'].items():
    header,blocks,footer=parse(src)
    seen=collections.Counter()
    # slug dup counting must follow source order: compute per-file anchor sets in source order
    hdr_anch=anchors_in(header,seen)
    secanch={n:anchors_in(b,seen) for n,b in sorted(blocks.items())}
    m={}
    for a in hdr_anch: m[a]=sp['parts'][0]['file']
    allsecs=sorted(blocks)
    covered=[s for p in sp['parts'] for s in p['sections']]
    assert sorted(covered)==allsecs,(src,covered,allsecs)
    for p in sp['parts']:
        for s in p['sections']:
            for a in secanch[s]: m[a]=p['file']
            rd_by_sec[(sp['reader'],s)]=p['reader']
    fmap[src]=m; first[src]=sp['parts'][0]['file']; rd_first[sp['reader']]=sp['parts'][0]['reader']
    dest_content[src]=(header,blocks,footer)
# auto anchor_remap: old custom ids above H1 and old H1 slug -> new first-part H1 slug
AR=dict(spec.get('anchor_remap',{}))
for src,sp in spec['sources'].items():
    header=dest_content[src][0]
    k=next(i for i,l in enumerate(header) if l.startswith('# '))
    new=slug(sp['parts'][0]['h1'])
    AR[slug(header[k][2:])]=new
    j=k
    while j>0 and ANCH.match(header[j-1]):
        AR[re.match(r'<a id="([^"]+)"',header[j-1]).group(1)]=new; j-=1
spec['anchor_remap']=AR
for src,sp in spec['sources'].items():
    for p in sp['parts']: p['slug']=slug(p['h1'])
# --- build dest texts
dest_text={}
WORKED={}
for src,sp in spec['sources'].items():
    header,blocks,footer=dest_content[src]
    worked=[]
    lastn=max(blocks)
    while blocks[lastn] and (blocks[lastn][-1].strip() in ('','---') or blocks[lastn][-1].startswith('*Worked examples')):
        l=blocks[lastn].pop()
        if l.startswith('*Worked examples'): worked.append(l)
    WORKED[src]=worked
    for i,p in enumerate(sp['parts']):
        body=[]
        if i==0:
            h=list(header)
            for k,l in enumerate(h):
                if l.startswith('# '):
                    h[k]='# '+p['h1']
                    j=k
                    while j>0 and ANCH.match(h[j-1]): j-=1
                    h=h[:j]+h[k:]
                    break
            body+=h
        else:
            secs=p['sections']; rng=f"§{secs[0]}" if len(secs)==1 else f"§{secs[0]}–§{secs[-1]}"
            fo=spec['order']; idx=fo.index(p['file']); prevf=fo[idx-1]; nextf=fo[idx+1]
            LAB={q['file']:q['label'] for s_ in spec['sources'].values() for q in s_['parts']}
            WORDS=("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty")
            def lab(f): return LAB.get(f) or "Chapter "+WORDS[int(f[5:7])]+(" (Part)" if False else "")
            pl,nl=lab(prevf),lab(nextf); pt,nt_=spec.get('chain',{}).get(prevf,prevf),spec.get('chain',{}).get(nextf,nextf)
            body+=['# '+p['h1'],
              '<details>','<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>','',
              f"> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one text. It contains **{p['label']}** — {p['desc']} (**{rng}**, continuing from the earlier Part of this chapter).",
              '>',f"> **Upstream:** [{pl}]({pt}). **Downstream:** [{nl}]({nt_}).",'','</details>','',
              '<details>','<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>','',
              f"- Upstream: [{pl}]({pt});",f"- Downstream: [{nl}]({nt_}).",'','</details>','','<br>','',
              f"{p['label']} is the constitutional owner of {p['desc']}.",'']
        for s in p['sections']: body+=blocks[s]
        dest_text[p['file']]=body
        report['dest_files']+=1
# --- regex rewrite of references
FN=re.compile(r'(core_\d\d\.\d{3}_[a-z0-9_]+\.md)(#[^)\s"\'`]*)?')
SRCNAMES=set(spec['sources'])
def fn_sub(t,self_file=None):
    def r(m):
        name,frag=m.group(1),m.group(2)
        if name not in SRCNAMES: return m.group(0)
        if frag and frag[1:] in spec.get('anchor_remap',{}):
            frag='#'+spec['anchor_remap'][frag[1:]]; d=first[name]
        elif frag:
            d=fmap[name].get(frag[1:])
            if d is None: d=first[name]; report['unresolved_frag']+=1
        else: d=first[name]
        report['fn_rewrites']+=1 if d!=name else 0
        return d+(frag or '')
    return FN.sub(r,t)
RDMAP=collections.defaultdict(dict)
RDRE=re.compile(r'(?<=[(（])(\d{1,2}\.\d{3})(?:(\s§)(\d+))?(?=[\s\.)）;,])')
def rd_sub(t):
    def r(m):
        num,sp,sec=m.group(1),m.group(2),m.group(3)
        if num not in rd_first: return m.group(0)
        if sec is not None and (num,int(sec)) in rd_by_sec: new=rd_by_sec[(num,int(sec))]
        else: new=rd_first[num]
        if new!=num: report['rd_rewrites']+=1
        return new+(sp or '')+(sec or '')
    return RDRE.sub(r,t)
INFILE=re.compile(r'\]\(#([^)\s]+)\)')
def infile_sub(t,dest):
    srcname=dest_src[dest]
    def r(m):
        d=fmap[srcname].get(m.group(1))
        if d and d!=dest: report['infile_to_crossfile']+=1; return f']({d}#{m.group(1)})'
        return m.group(0)
    return INFILE.sub(r,t)
FIRSTS={sp['parts'][0]['file'] for sp in spec['sources'].values()}
dest_first={}
dest_src={p['file']:src for src,sp in spec['sources'].items() for p in sp['parts']}
# footers
order=spec['order']
chain=spec.get('chain',{})   # basename -> 'basename#frag'
def tgt(n): return chain.get(n,n)
def footer_for(f):
    i=order.index(f); prev=order[i-1] if i>0 else None; nxt=order[i+1] if i+1<len(order) else None
    out=['','---','']
    if f==dest_first.get(f) or f in FIRSTS:
        for w in WORKED[dest_src[f]]: out+=[w,'']
    if prev: out+=[f'**Previous file:** [{prev}]({tgt(prev)})','']
    if nxt: out+=[f'**Next file:** [{nxt}]({tgt(nxt)})']
    return out
SKIP={'.git','archive','translations','_pages_site','node_modules','__pycache__','_to_delete','translation_drafts'}
DATED=('evidence/','evaluation/results/','project/MEMLOG','project/trials/')
HIST=('tools/ch1_integration','tools/ch1_reading_arc','tools/ch1_part_b_consecutive','tools/ch1_market_structure','tools/ch8_','tools/core_filename_normalize','tools/ch06_','tools/renumber_','tools/chapter_insertion','tools/chapter_numbering_inverse')
LINKONLY=re.compile(r'\]\([^)]*\)')
changed=0; newtexts={}
dests=set(dest_text)
for r,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in SKIP]
    for f in fs:
        if not f.endswith(('.md','.json','.py','.txt','.yml','.yaml','.toml','.html','.mmd','.csv','.mdc')) and f!='Makefile': continue
        p=os.path.join(r,f)[2:]
        if p in dests or p in SRCNAMES: continue
        if p.startswith(HIST): continue
        try:t=open(p,encoding='utf-8').read()
        except Exception: continue
        if p.startswith(DATED): nt=LINKONLY.sub(lambda m: fn_sub(m.group(0)),t)
        else:
            nt=fn_sub(t)
            if p.endswith('.md'): nt=rd_sub(nt)
        if nt!=t: changed+=1; newtexts[p]=nt
report['other_files_changed']=changed
# write dests
final={}
for dest,body in dest_text.items():
    t='\n'.join(body).rstrip('\n')+'\n'
    t=fn_sub(t); t=rd_sub(t); t=infile_sub(t,dest)
    t=t.rstrip('\n')+'\n'+'\n'.join(footer_for(dest))+'\n'
    final[dest]=t
print(json.dumps(dict(report),indent=1))
for d,t in final.items(): print(f"  {d}: {len(t.encode())/1024:.1f} KiB")
if apply:
    for s in SRCNAMES:
        if s not in dests: os.remove(s)
    for d,t in final.items(): open(d,'w',encoding='utf-8').write(t)
    for p,t in newtexts.items(): open(p,'w',encoding='utf-8').write(t)
    # footer neighbours: fix Previous/Next in files adjacent to changed
    PV=re.compile(r'\*\*Previous file:\*\* \[([^\]]*)\]\(([^)#]*)(#[^)]*)?\)'); NX=re.compile(r'\*\*Next file:\*\* \[([^\]]*)\]\(([^)#]*)(#[^)]*)?\)')
    for i,f in enumerate(order):
        if f in dests or not os.path.exists(f): continue
        t=open(f,encoding='utf-8').read(); nt=t
        if i>0:
            nt=PV.sub(lambda m: m.group(0) if (m.group(2)+(m.group(3) or ''))==tgt(order[i-1]) else f'**Previous file:** [{order[i-1]}]({tgt(order[i-1])})',nt)
        if i+1<len(order):
            nt=NX.sub(lambda m: m.group(0) if (m.group(2)+(m.group(3) or ''))==tgt(order[i+1]) else f'**Next file:** [{order[i+1]}]({tgt(order[i+1])})',nt)
        if nt!=t: open(f,'w',encoding='utf-8').write(nt); report['footer_neighbours_fixed']+=1
    REGP='tools/architecture/chapter_numbers.json'; reg=json.load(open(REGP)); rows=reg['chapters']; newrows=[]
    for row in rows:
        newrows.append(row)
        sp=spec['sources'].get(row['destination_file']) or next((x for x in spec['sources'].values() if x['parts'][0]['file']==row['destination_file']),None)
        if not sp or row.get('layer','CORE')!='CORE': continue
        parts=sp['parts']
        for k,p in enumerate(parts):
            maj,minor=p['reader'].split('.'); mid=f"{int(maj):02d}{minor[0]}{minor[1:]}"
            if k==0: r0=row
            else:
                r0=dict(row); r0.pop('original_file',None); newrows.append(r0)
            r0.update(destination_file=p['file'],machine_id=mid,machine_number=mid,display_id=p['reader'])
    reg['chapters']=newrows; json.dump(reg,open(REGP,'w'),indent=2,ensure_ascii=False); open(REGP,'a').write('\n'); print('registry rows now',len(newrows))
    print('footer neighbours fixed:',report['footer_neighbours_fixed']); print('APPLIED')
