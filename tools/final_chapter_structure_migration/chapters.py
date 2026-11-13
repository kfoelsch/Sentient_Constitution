#!/usr/bin/env python3
"""One-off restructure engine for the final chapter structure (492nd move). usage: chapters.py ROOT [--apply]
Promotes Parts of Ch 9,10,13,14 to chapters, shifts chapters to 0-28, restarts sections, inserts
Purpose and Role stubs, rewrites headings/anchors/links/cites/reader numbers/filenames, registry, corpus homes."""
import os,re,sys,json,collections
root=sys.argv[1]; APPLY='--apply' in sys.argv
os.chdir(root)
WORDS=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Twenty-One','Twenty-Two','Twenty-Three','Twenty-Four','Twenty-Five','Twenty-Six','Twenty-Seven','Twenty-Eight']
W2N={w:i for i,w in enumerate(WORDS)}
SRCW=[w for w in WORDS[:21]]
CW='|'.join(sorted(SRCW,key=len,reverse=True))
STATS=collections.Counter()
# ------------------------------------------------------------------ plan
files={f for f in os.listdir('.') if re.match(r'core_\d\d\.\d{3}_',f)}
def find(prefix):
    m=[f for f in files if f.startswith(prefix)]
    assert len(m)==1,(prefix,m); return m[0]
OLD={}   # key -> filename
for k,p in {'9A':'core_09.000','9B':'core_09.005','9C':'core_09.010','10':'core_10.000','11':'core_11.000','12':'core_12.000','13A':'core_13.000','13B':'core_13.005','13C':'core_13.010','13D':'core_13.015','14A':'core_14.000','14B':'core_14.005','15':'core_15.000','16':'core_16.000','17':'core_17.000','18':'core_18.000','19':'core_19.000','20':'core_20.000','3':'core_03.000','4':'core_04.000','7':'core_07.000'}.items(): OLD[k]=find(p)
OLDCH={f:int(f[5:7]) for f in OLD.values()}
SRCFILES=set(OLD.values())
def smap(c,n):
    """old chapter c, old top-level section n -> (new chapter, new section)"""
    if c==9: return (9,n) if n<=5 else ((10,n-4) if n<=7 else (11,n-6))
    if c==10: return (12,n) if n<=5 else ((13,n-4) if n<=7 else (14,n-6))
    if c==13: return (17,n) if n<=4 else ((18,n-3) if n==5 else ((19,n-4) if n<=7 else (20,n-6)))
    if c==14: return (21,n) if n<=5 else (22,n-4)
    if c in (3,4,7): return (c,n+1)
    if c==11: return (15,n+1)
    if c==12: return (16,n+1)
    if c==15: return (23,n)
    if c==16: return (24,n+1)
    if c in (17,18,19): return (c+8,n+1)
    if c==20: return (28,n)
    return (c,n)
FIRST={9:9,10:12,11:15,12:16,13:17,14:21,15:23,16:24,17:25,18:26,19:27,20:28}
LAST ={9:11,10:14,11:15,12:16,13:20,14:22,15:23,16:24,17:25,18:26,19:27,20:28}
PARTMAP={(9,'A'):9,(9,'B'):10,(9,'C'):11,(13,'A'):17,(13,'B'):18,(13,'C'):19,(13,'D'):20,(14,'A'):21,(14,'B'):22}
PROMOTED={9,10,13,14}
def newch_first(c): return FIRST.get(c,c)
TITLES={9:'SYSTEM ALIGNMENT CERTIFICATION — EVALUATION',10:'SYSTEM ALIGNMENT CERTIFICATION — FORUM PROCESS AND OUTCOMES',
 11:'SYSTEM ALIGNMENT CERTIFICATION — RECORDS, RECERTIFICATION, CHALLENGE, AND STANDING',
 12:'INSTITUTIONAL ALIGNMENT CERTIFICATION — EVALUATION',13:'INSTITUTIONAL ALIGNMENT CERTIFICATION — FORUM PROCESS AND OUTCOMES',
 14:'INSTITUTIONAL ALIGNMENT CERTIFICATION — RECORDS, RECERTIFICATION, CHALLENGE, AND STANDING',
 17:'STANDING INTEGRATION — QUESTION 3, WHAT FOLLOWS?',18:'CONTRIBUTION CONSEQUENCES',19:'VIOLATION CONSEQUENCES — REMEDY, CORRECTION, AND LOCKS',
 20:'FINAL STANDING EFFECT, RESTORATION, AND ENFORCEMENT',21:'ANTI-CONSTITUTIONAL MISCONDUCT DESIGNATION',
 22:'ANTI-CONSTITUTIONAL MISCONDUCT — PATTERN APPLICATIONS AND CRITERIA ROUTING'}
STEM={9:'system_alignment_certification_evaluation',10:'system_alignment_certification_forum_process_outcomes',11:'system_alignment_certification_records_recertification',
 12:'institutional_alignment_certification_evaluation',13:'institutional_alignment_certification_forum_process_outcomes',14:'institutional_alignment_certification_records_recertification',
 17:'standing_integration',18:'contribution_consequences',19:'violation_consequences',20:'final_effect_restoration_enforcement',21:'misconduct_designation',22:'misconduct_pattern_applications'}
def newname(oldfile,newch):
    m=re.match(r'core_\d\d\.\d{3}_(.*)$',oldfile); stem=STEM.get(newch,m.group(1)[:-3])
    return f"core_{newch:02d}.000_{stem}.md" if newch in STEM else f"core_{newch:02d}.000_{m.group(1)}"
STUB=['### 1. Purpose and Role','','*Draft pending steward review.* This section states what the chapter is for, what it produces, and where it sits in the reading order. It restates existing rules and adds none.','']
STUBCH={3,4,7,10,11,13,14,15,16,18,19,20,22,25,26,27}
# ------------------------------------------------------------------ parse
def slug(t):
    t=re.sub(r'<[^>]+>','',t); t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t).strip().lower()
    t=re.sub(r'[^\w\- ]','',t,flags=re.U); return t.replace(' ','-')
SEC=re.compile(r'^### (\d+)\. '); ANCH=re.compile(r'^<a id="[^"]+"></a>\s*$'); HEAD=re.compile(r'^(#{1,6}) (.*)')
def parse(path):
    L=open(path,encoding='utf-8').read().split('\n')
    fi=next((i for i,l in enumerate(L) if l.startswith('**Previous file:**')),len(L)); j=fi
    while j>0 and L[j-1].strip() in ('','---'): j-=1
    footer=L[j:]; body=L[:j]; starts=[]
    for i,l in enumerate(body):
        m=SEC.match(l)
        if m:
            s=i
            while s>0 and (body[s-1].strip()=='' or ANCH.match(body[s-1])): s-=1
            starts.append((int(m.group(1)),s))
    header=body[:starts[0][1]]; blocks={}
    for k,(n,s) in enumerate(starts):
        e=starts[k+1][1] if k+1<len(starts) else len(body); blocks[n]=body[s:e]
    return header,blocks,footer
def heads_with_slugs(lines,seen):
    """yield (index, level, text, slug) for headings outside fences, dup-counted via seen"""
    out=[];fence=False
    for i,l in enumerate(lines):
        if l.startswith('```'): fence=not fence
        if fence: continue
        m=HEAD.match(l)
        if m:
            s=slug(m.group(2)); n=seen[s]; seen[s]+=1; out.append((i,len(m.group(1)),m.group(2),s if n==0 else f"{s}-{n}"))
    return out
HNUM=re.compile(r'^(#{2,6}) (\d+)((?:\.\d+)*)(\.?)(\s)')
def renum_heading(l,oldch):
    m=HNUM.match(l)
    if not m: return l
    nc,nn=smap(oldch,int(m.group(2)))
    return f"{m.group(1)} {nn}{m.group(3)}{m.group(4)}{m.group(5)}"+l[m.end():]
# ------------------------------------------------------------------ build destinations
dest={}      # newfile -> dict(lines=[], tags=[], ch=, src=)
AMAP={}      # (oldfile, oldfrag) -> (newfile, newfrag)  filled after slugs
FIRSTDEST={} # oldfile -> newfile (first dest)
EXPL={}
OLDNUM={}      # (oldfile, explicit id) -> newfile
recs=collections.defaultdict(list)   # newfile -> [(oldfile, old_slug or None)]
WORKED_TAKE={}
for key,of in OLD.items():
    oc=OLDCH[of]
    header,blocks,footer=parse(of)
    seen=collections.Counter()
    # old slugs for header then blocks in order
    hs_header=heads_with_slugs(header,seen)
    hs_blocks={n:heads_with_slugs(b,seen) for n,b in sorted(blocks.items())}
    # worked-examples tail lines (single-file Ch10) -> move to first dest
    lastn=max(blocks); worked=[]
    while blocks[lastn] and (blocks[lastn][-1].strip() in ('','---') or blocks[lastn][-1].startswith('*Worked examples')):
        x=blocks[lastn].pop()
        if x.startswith('*Worked examples'): worked.append(x)
    chs=[]
    for n in sorted(blocks):
        nc,nn=smap(oc,n)
        if nc not in chs: chs.append(nc)
    firstch=chs[0]
    def D(nc):
        nf=newname(of,nc)
        if nf not in dest: dest[nf]={'lines':[],'tags':[],'ch':nc,'src':of,'footer':None,'header_done':False}
        return nf,dest[nf]
    FIRSTDEST[of]=D(firstch)[0]
    # header goes to first dest
    nf,dd=D(firstch)
    h=list(header)
    # first-H1 and ids above it
    k=next(i for i,l in enumerate(h) if l.startswith('# '))
    old_h1=h[k][2:]; top_ids=[]
    j=k
    while j>0 and ANCH.match(h[j-1]): top_ids.append(re.match(r'<a id="([^"]+)"',h[j-1]).group(1)); j-=1
    t=TITLES.get(firstch)
    m1=re.match(r'CHAPTER ([A-Z0-9 \-]+?)(?:, PART [A-D])?: (.*)$',old_h1) or re.match(r'CHAPTER ([A-Z0-9 \-]+)',old_h1)
    title=t if t else (m1.group(2) if m1 and m1.lastindex and m1.lastindex>=2 else old_h1.split(': ',1)[-1])
    new_h1=f"CHAPTER {WORDS[firstch].upper()}: {title}" if not old_h1.startswith('CHAPTER 0') and not old_h1.startswith('PREAMBLE') else old_h1
    H1CHANGED=(new_h1!=old_h1)
    h=h[:j]+h[k:] if H1CHANGED else h
    kk=next(i for i,l in enumerate(h) if l.startswith('# ')); 
    if H1CHANGED: h[kk]='# '+new_h1
    # tag header lines
    hq=iter(hs_header); cur=next(hq,None)
    fence=False; emitted=[]
    # compute mapping from header line index (original header) to heading slug: replicate by scanning h with its own indices
    hs2=[]; seen2=None
    # simpler: tag by scanning original header heads in order, aligning with h by text
    olds=[(x[2],x[3]) for x in hs_header]; oi=0
    fence=False
    for l in h:
        tag=None
        if l.startswith('```'): fence=not fence
        mm=HEAD.match(l) if not fence else None
        if mm:
            # match to next old heading in order; if H1 changed, first heading is H1
            if oi<len(olds): tag=(of,olds[oi][1]); oi+=1
        dd['lines'].append(l); dd['tags'].append(tag)
    if H1CHANGED:
        AMAP[(of,slug(old_h1))]=None  # resolved later to new H1 slug
        for i_ in top_ids: AMAP[(of,i_)]=None
        dd['h1new']=new_h1; dd['h1old']=(of,slug(old_h1),top_ids)
    if firstch in STUBCH and key not in ('16',):
        for l in STUB: dd['lines'].append(l); dd['tags'].append('GEN')
    # blocks
    for n in sorted(blocks):
        nc,nn=smap(oc,n); nf2,d2=D(nc)
        if nc!=firstch and not d2['lines']:
            # generated skeleton header for a chapter carved from the middle of a single file
            secs=[x for x in sorted(blocks) if smap(oc,x)[0]==nc]
            h1=f"CHAPTER {WORDS[nc].upper()}: {TITLES[nc]}"
            DESC={13:'forum process and outcomes of institutional alignment certification',14:'Institutional Certification Records, recertification, challenge, and standing consequences of institutional alignment certification'}
            hdr=['# '+h1,'<details>','<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>','',
              f"> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one text. It contains **Chapter {WORDS[nc]}** — the {DESC[nc]}.",'','</details>','',
              '<details>','<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>','','- Upstream: the previous chapter;','- Downstream: the next chapter.','','</details>','','<br>','',
              f"Chapter {WORDS[nc]} is the constitutional owner of **{DESC[nc]}**.",'']
            for l in hdr: d2['lines'].append(l); d2['tags'].append('GEN')
            d2['skel']=True
            if nc in STUBCH:
                for l in STUB: d2['lines'].append(l); d2['tags'].append('GEN')
        # lines of block with tags
        hmap={x[0]:x[3] for x in hs_blocks[n]}
        fence=False
        for i,l in enumerate(blocks[n]):
            if l.startswith('```'): fence=not fence
            tag=(of,hmap[i]) if i in hmap else None
            if tag:
                mo=re.match(r'#{2,6} (\d+(?:\.\d+)*)',l)
                if mo: OLDNUM[tag]=mo.group(1).replace('.','')
                l=renum_heading(l,oc)
            d2['lines'].append(l); d2['tags'].append(tag)
        for x in hs_blocks[n]: pass
        # explicit ids in block
        for l in blocks[n]:
            for a in re.findall(r'<a id="([^"]+)"',l): EXPL[(of,a)]=nf2
    for a in re.findall(r'<a id="([^"]+)"',"\n".join(header)): EXPL.setdefault((of,a),FIRSTDEST[of])
    if worked:
        dest[FIRSTDEST[of]].setdefault('worked',[]).extend(worked)
    dest[FIRSTDEST[of]].setdefault('footer_src',footer)
    for nc in chs:
        nf3,d3=D(nc); d3.setdefault('footer_src',footer if nc==firstch else None)
print('destinations:',len(dest))
json.dump({'FIRSTDEST':FIRSTDEST,'dest':{k:{'ch':v['ch'],'src':v['src']} for k,v in dest.items()}},open('/tmp/chapters_plan.json','w'))

# ====================================================================== part 2: global rewriting
# ---- filename maps
CH6={'core_06.005':'core_06.010','core_06.010':'core_06.020','core_06.015':'core_06.030','core_06.020':'core_06.040'}
FNMAP={}   # old full filename -> new full filename (first dest)
for f in os.listdir('.'):
    m=re.match(r'(core_06\.\d{3})(_.*)$',f)
    if m and m.group(1) in CH6: FNMAP[f]=CH6[m.group(1)]+m.group(2)
for of,nf in FIRSTDEST.items(): FNMAP[of]=nf
THREE10=sorted([nf for nf,d in dest.items() if d['src']==OLD['10']],key=lambda x:dest[x]['ch'])
NEWCH_OF={nf:d['ch'] for nf,d in dest.items()}
for f in os.listdir('.'):
    m=re.match(r'core_(\d\d)\.',f)
    if m and f not in SRCFILES: NEWCH_OF.setdefault(FNMAP.get(f,f),int(m.group(1)))
OLDCH_ANY=dict(OLDCH)
for f in os.listdir('.'):
    m=re.match(r'core_(\d\d)\.',f)
    if m: OLDCH_ANY.setdefault(f,int(m.group(1)))
FNRE=re.compile(r'(?<![\w/.-])(?:\.\./|(?:[\w-]+/)*)?core_\d\d\.\d{3}_[a-z0-9_]+\.md')
BASE=re.compile(r'core_\d\d\.\d{3}_[a-z0-9_]+\.md')
def map_fn(name): return FNMAP.get(name,name)
# ---- corpus id re-homing
CORP={('CF',15):23,('CF',16):24,('CF',20):28,('CF',17):25,('CF',18):26,('CF',19):27,('CF',11):None}
HOME=json.load(open('tools/architecture/chapter_numbers.json'))
# discover the corpus files whose chapter prefix must change (layer file chapter prefix == old core chapter home)
CORPUS_RE=re.compile(r'\b(cjs|ci|cs|cf)_(\d\d)\.(\d+)_')
CORPUS_MAP={}   # (layer lower, '15') -> new ch, overrides by (layer,oldch,num)
OVER={('ci','13','205'):'20',('ci','13','210'):'19',('ci','13','215'):'19'}
LAYCH={('cjs','11'):'15',('ci','13'):'17',('ci','15'):'23',('ci','16'):'24',('cf','15'):'23',('cjs','20'):'28',('cs','11'):'15',('cs','13'):'17',('cs','15'):'23',('cs','16'):'24',('cs','20'):'28',
       ('cf','11'):'15',('cf','13'):'17',('cf','16'):'24',('cf','20'):'28',('ci','11'):'15',('ci','20'):'28',('cjs','13'):'17',('cjs','15'):'23',('cjs','16'):'24',('cjs','12'):'16',('cjs','14'):'21',
       ('cs','12'):'16',('cs','14'):'21',('ci','12'):'16',('ci','14'):'21',('cf','12'):'16',('cf','14'):'21',
       ('cjs','17'):'25',('cjs','18'):'26',('cjs','19'):'27',('cs','17'):'25',('cs','18'):'26',('cs','19'):'27',('ci','17'):'25',('ci','18'):'26',('ci','19'):'27',('cf','17'):'25',('cf','18'):'26',('cf','19'):'27'}
# only layer/chapter combos that actually have files
corp_files=[]
for r_,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in ('.git','archive','node_modules','_pages_site','translations')]
    for f in fs:
        m=re.match(r'(cjs|ci|cs|cf)_(\d\d)\.(\d+)_',f)
        if m: corp_files.append(os.path.join(r_,f)[2:])
used=collections.Counter((re.match(r'.*/(cjs|ci|cs|cf)_(\d\d)\.',p).group(1),re.match(r'.*/(cjs|ci|cs|cf)_(\d\d)\.',p).group(2)) for p in corp_files)
def corp_new(layer,ch,num):
    k=OVER.get((layer,ch,num))
    if k: return k
    if (layer,ch) in used and (layer,ch) in LAYCH: return LAYCH[(layer,ch)]
    return ch
# precise id renames from the plan's home table only
PLAN_HOMES={('cf','15'),('ci','15'),('ci','16'),('cjs','11'),('ci','13'),('cjs','20'),('cf','16'),('cf','20'),('cs','15'),('cs','16'),('cs','20'),('ci','20')}
def corp_new2(layer,ch,num):
    k=OVER.get((layer,ch,num))
    if k: return k
    if (layer,ch) in PLAN_HOMES and (layer,ch) in used: return LAYCH[(layer,ch)]
    return ch
CORPREN={}
for p in corp_files:
    d,f=os.path.split(p); m=re.match(r'(cjs|ci|cs|cf)_(\d\d)\.(\d+)_(.*)$',f)
    l,c,n,rest=m.groups(); nc=corp_new2(l,c,n)
    if nc!=c: CORPREN[p]=os.path.join(d,f"{l}_{nc}.{n}_{rest}")
IDRE=re.compile(r'\b(CJS|CI|CS|CF)-(\d+)\.(\d+)\b')
FILEIDRE=re.compile(r'\b(cjs|ci|cs|cf)_(\d\d)\.(\d+)_')
def corp_id_sub(t,c=None):
    def a(m):
        l=m.group(1).lower(); ch=m.group(2); n=m.group(3); nc=corp_new2(l,ch.zfill(2),n)
        if nc==ch.zfill(2): return m.group(0)
        if c is not None: c['cid']+=1
        return f"{m.group(1)}-{int(nc)}.{n}"
    def b(m):
        nc=corp_new2(m.group(1),m.group(2),m.group(3))
        if nc==m.group(2): return m.group(0)
        if c is not None: c['cfile']+=1
        return f"{m.group(1)}_{nc}.{m.group(3)}_"
    return FILEIDRE.sub(b,IDRE.sub(a,t))
# ---- cite engine
ATOM=re.compile(r'''
 (?P<foreign>\b(?:CJS|CI|CS|CF)-\d+(?:\.\d+)?|\bArticle\s+[IVX]+|\bDef\.\w+|\bAppendix\s+\w)
|(?P<ch>\b(?P<chw>Chapters?)\s+(?P<cw>'''+CW+r'''|\d{1,2}(?![\d.]))(?P<partpart>,?\s*(?:\*\*)?(?P<plist>Parts?\s+[A-D](?:\s*(?:–|-|—|,|,?\s+and)\s*[A-D]\b)*)\b)?)
|(?P<part>\b(?P<plist2>Parts?\s+[A-D](?:\s*(?:–|-|—|,|,?\s+and)\s*[A-D]\b)*)\b)
|(?P<rd>\((?P<rdc>\d{1,2})\.(?P<rds>\d{3})(?=\s*§|\)))
|(?P<sec>(?:§§?|\b[Ss]ections?\s)\s*(?P<sn>\d+)(?P<sub>(?:\.\d+)*))
''',re.X)
CLAUSE_BREAK=re.compile(r'[.;:!?]\s|\n|\)\s*\(')
TAIL=re.compile(r'\s*(?:–|-|—|and|through|to)\s*(%s|\d{1,2})\b'%CW)
SLOTCH={(9,'000'):9,(9,'005'):10,(9,'010'):11,(10,'000'):12,(13,'000'):17,(13,'005'):18,(13,'010'):19,(13,'015'):20,(14,'000'):21,(14,'005'):22}
RD6={'005':'010','010':'020','015':'030','020':'040'}
def plet(s):
    body=re.sub(r'^Parts?\s+','',s); toks=re.findall(r'[A-D]|–|-|—',body); out=[]; i=0
    while i<len(toks):
        if toks[i] in 'ABCD' and toks[i] not in '–-—':
            out.append(toks[i])
            if i+2<len(toks) and toks[i+1] in ('–','-','—') and toks[i+2] in 'ABCD':
                for o in range(ord(toks[i])+1,ord(toks[i+2])+1): out.append(chr(o))
                i+=2
        i+=1
    return out
def chap_text(chs):
    ws=[WORDS[c] for c in chs]
    if len(chs)==1: return 'Chapter '+ws[0]
    if len(chs)==2: return f'Chapters {ws[0]} and {ws[1]}'
    if chs==list(range(chs[0],chs[0]+len(chs))): return f'Chapters {ws[0]}–{ws[-1]}'
    return 'Chapters '+', '.join(ws[:-1])+', and '+ws[-1]
def w2n(w):
    if w.isdigit(): return int(w)
    for k,v in W2N.items():
        if k.lower()==w.lower(): return v
    raise KeyError(w)
REV=collections.Counter(); REVLIST=[]
def cite_rewrite(text,ctx,ctx_new,force_q=None,where=''):
    edits=[]; quals=[]; cur=None
    def gap_ok(a,b):
        g=text[a:b]; return len(g)<=90 and not CLAUSE_BREAK.search(g)
    def fin(q):
        if q is None or q.get('foreign'): return
        oc=q['oc']; toks=q['toks']; kind=q['kind']
        # new chapter per token
        tn=[(smap(oc,t['n']) if oc<=20 else (oc,t['n'])) for t in toks]
        if kind=='bare':
            Q=ctx_new
        elif toks:
            Q=tn[0][0]
        elif force_q is not None: Q=force_q
        elif kind=='rd':
            Q=SLOTCH.get((oc,q['slot']), None)
            if Q is None: Q=FIRST.get(oc,oc) if oc not in (6,1) else oc
        elif q.get('part') and (oc,q['part']) in PARTMAP:
            pcs=[]
            for L_ in plet(q['plist']):
                c_=PARTMAP.get((oc,L_))
                if c_ is not None and c_ not in pcs: pcs.append(c_)
            q['pchs']=pcs; Q=pcs[0]
        else:
            Q=FIRST.get(oc,oc)
            if oc in (9,10,13,14) and not q.get('part'):
                REV['bare_multi_dest']+=1; REVLIST.append((where,text[q['m'].start():q['m'].end()+20]))
        m=q['m']
        drop=bool(q.get('plist')) and oc in PROMOTED
        if kind=='ch' and drop and not toks and len(q.get('pchs') or [])>1:
            edits.append((m.start(),m.end(),chap_text(q['pchs']))); REV['qual_rewritten']+=1
        elif kind=='ch':
            if oc<=20:
                plural=m.group('chw')=='Chapters'
                if plural:
                    tl=TAIL.match(text,m.end())
                    if tl and w2n(tl.group(1))<=20:
                        b=w2n(tl.group(1)); nb=LAST.get(b,b)
                        if nb!=b: edits.append((tl.start(1),tl.end(1),str(nb) if tl.group(1).isdigit() else WORDS[nb])); REV['range_end']+=1
                        Q=FIRST.get(oc,oc)
                nm=str(Q) if m.group('cw').isdigit() else WORDS[Q]
                if drop: edits.append((m.start(),m.end(),('Chapters ' if plural else 'Chapter ')+nm)); REV['qual_rewritten']+=1
                elif Q!=oc: edits.append((m.start('cw'),m.end('cw'),nm)); REV['qual_rewritten']+=1
        elif kind=='part':
            pcs=q.get('pchs') or [Q]
            edits.append((m.start(),m.end(),chap_text(pcs) if not toks else f"Chapter {WORDS[Q]}")); REV['part_to_chapter']+=1
        elif kind=='rd':
            if oc==6 and q['slot'] in RD6 and not toks:
                edits.append((m.start(),m.end(),f"(6.{RD6[q['slot']]}"))
            elif oc not in (0,1,2,5,6,8):
                edits.append((m.start(),m.end(),f"({Q}.000")); REV['reader']+=1
            elif oc==6 and q['slot'] in RD6:
                edits.append((m.start(),m.end(),f"(6.{RD6[q['slot']]}"))
        for t,(nc,nn) in zip(toks,tn):
            rep=f"{nn}{t['sub']}" if True else ''
            if nn!=t['n']: edits.append((t['s'],t['e'],str(nn))); REV['sec_renumbered']+=1
            if nc!=Q and kind!='rd':
                edits.append((t['ms'],t['ms'],f"Chapter {WORDS[nc]} ")); REV['chapter_inserted']+=1
            elif nc!=Q and kind=='rd':
                edits.append((t['ms'],t['ms'],f"Chapter {WORDS[nc]} ")); REV['chapter_inserted']+=1
    for m in ATOM.finditer(text):
        if m.group('foreign'):
            fin(cur); cur={'foreign':True,'end':m.end()}; continue
        if m.group('ch'):
            fin(cur); w=m.group('cw'); oc=int(w) if w.isdigit() else w2n(w)
            if oc>20: cur={'foreign':True,'end':m.end()}; continue
            cur={'kind':'ch','oc':oc,'part':(plet(m.group('plist'))[0] if m.group('plist') else None),'plist':m.group('plist'),'m':m,'end':m.end(),'toks':[]}; continue
        if m.group('part'):
            if ctx in PROMOTED:
                fin(cur); cur={'kind':'part','oc':ctx,'part':plet(m.group('plist2'))[0],'plist':m.group('plist2'),'m':m,'end':m.end(),'toks':[]}
            continue
        if m.group('rd'):
            fin(cur); cur={'kind':'rd','oc':int(m.group('rdc')),'slot':m.group('rds'),'m':m,'end':m.end(),'toks':[]}; continue
        if m.group('sec'):
            if cur and not cur.get('foreign') and gap_ok(cur['end'],m.start()): q=cur
            elif cur and cur.get('foreign') and gap_ok(cur['end'],m.start()): continue
            elif ctx is not None:
                fin(cur); cur={'kind':'bare','oc':ctx,'m':None,'end':m.end(),'toks':[]}; q=cur
            else: continue
            q['toks'].append({'n':int(m.group('sn')),'sub':m.group('sub'),'s':m.start('sn'),'e':m.end('sn'),'ms':m.start('sec')}); q['end']=m.end()
            # continuation numbers after §§ / Sections ranges: "§§3–5", "§6 and §7" handled by ATOM; bare "3–5" only after §§
            mk=m.group('sec')
            if mk.startswith('§§') or mk.lower().startswith('sections'):
                pos=m.end()
                while True:
                    c=re.compile(r'\s*(?:–|-|—|,|and|through|to)\s*(\d+)((?:\.\d+)*)(?![\d.]*\s*(?:%|\w{4}))').match(text,pos)
                    if not c: break
                    q['toks'].append({'n':int(c.group(1)),'sub':c.group(2),'s':c.start(1),'e':c.end(1),'ms':c.start(1)}); pos=c.end(); q['end']=pos
    fin(cur)
    if not edits: return text
    # drop inserts that collide with replaced spans; apply right-to-left
    edits.sort(key=lambda e:(e[0],e[1]),reverse=True)
    out=text; last=len(text)+1
    for s,e,r in edits:
        if e>last: continue
        out=out[:s]+r+out[e:]; last=s
    return out
# ---- links
LINKRE=re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]*)((?:\s+"[^"]*")?)\)')
UNRES=[]
FRAGCORP=re.compile(r'\b(cjs|ci|cs|cf)-(\d\d)(\d{3})\b')
FRAGCORP2=re.compile(r'(?<=#)(cjs|ci|cs|cf)-(\d\d)(\d{3})(?![\d])')
def frag_corp(fr):
    def a(m):
        nc=corp_new2(m.group(1),m.group(2),m.group(3))
        return m.group(0) if nc==m.group(2) else f"{m.group(1)}-{nc}{m.group(3)}"
    return FRAGCORP.sub(a,fr)
def resolve(target,curold,curnew):
    """returns new target string"""
    if target.startswith(('http://','https://','mailto:')): return target,None
    path,_,frag=target.partition('#'); pref,_,base=path.rpartition('/'); pref=pref+'/' if pref else ''
    if base=='' and frag: base=curold; samefile=True
    else: samefile=False
    # corpus file renames
    full=(pref+base)
    nb=base
    if base in SRCFILES or base in FNMAP:
        tf=base
        if frag and (base,frag) in AMAP and AMAP[(base,frag)] is not None:
            nf,ns=AMAP[(base,frag)]; frag=ns
        else:
            nf=FNMAP.get(base,base)
            if frag and (base,frag) in EXPL: nf=EXPL[(base,frag)]
            elif frag and base in SRCFILES and (base,frag) not in AMAP: UNRES.append((curold,target)); nf=FIRSTDEST.get(base,nf)
        nb=nf; ctx_old=OLDCH_ANY.get(tf); ctx_new=NEWCH_OF.get(nf)
        if samefile and nb==curnew: return ('#'+frag if frag else ''),(ctx_old,ctx_new)
        return pref+nb+('#'+frag if frag else ''),(ctx_old,ctx_new)
    # other core file (unchanged filename) – keep
    m=re.match(r'core_(\d\d)\.',base)
    ctx=(int(m.group(1)),int(m.group(1))) if m else None
    # corpus file rename
    key=(pref+base)
    for p,np_ in CORPREN.items():
        pass
    return None,ctx
CORPREN_BY_BASE={os.path.basename(p):os.path.basename(n) for p,n in CORPREN.items()}
def link_target_final(target,curold,curnew):
    mu=re.match(r'^(https://github\.com/[^/]+/[^/]+/(?:blob|tree)/[^/]+/)(.*)$',target)
    if mu:
        nt_,ctx_=link_target_final(mu.group(2),curold,curnew); GST['url_links']+=1 if nt_!=mu.group(2) else 0; return mu.group(1)+nt_,ctx_
    nt,ctx=resolve(target,curold,curnew)
    if nt is None:
        path,_,frag=target.partition('#'); pref,_,base=path.rpartition('/'); pref=pref+'/' if pref else ''
        base=CORPREN_BY_BASE.get(base,base)
        nt=pref+base+('#'+frag if frag else '')
    path,_,frag=nt.partition('#')
    if frag: nt=path+'#'+frag_corp(frag)
    return nt,ctx
def process_line(line,mode,ctx,ctx_new,curold,curnew,where=''):
    """mode: 'live' (all), 'dated' (links only), 'tool' not used here"""
    out=[];pos=0
    for m in LINKRE.finditer(line):
        seg=line[pos:m.start()]
        out.append(seg_fix(seg,mode,ctx,ctx_new,where))
        label,target,title=m.group(1),m.group(2),m.group(3)
        nt,tctx=link_target_final(target,curold,curnew)
        if mode=='live':
            if tctx and tctx[0] is not None:
                if '#' in target and re.fullmatch(r'\d+(?:\.\d+)*(?:\s*[–-]\s*\d+(?:\.\d+)*)?',label.strip()):
                    label=re.sub(r'\d+(?:\.\d+)*',lambda mm:(lambda p:str(smap(tctx[0],int(p[0]))[1])+''.join('.'+x for x in p[1:]))(mm.group(0).split('.')),label); REV['numeric_label']+=1
                else:
                    label=cite_rewrite(label,tctx[0],tctx[1],force_q=tctx[1],where=where)
            else:
                label=cite_rewrite(label,None,None,where=where)
            label=corp_id_sub(label)
            label=BASE.sub(lambda mm: map_fn(mm.group(0)),label)
        out.append(f"[{label}]({nt}{title})"); pos=m.end()
    out.append(seg_fix(line[pos:],mode,ctx,ctx_new,where)); return ''.join(out)
def seg_fix(seg,mode,ctx,ctx_new,where=''):
    if mode!='live' or not seg: return seg
    seg=cite_rewrite(seg,ctx,ctx_new,where=where)
    seg=corp_id_sub(seg)
    seg=FRAGCORP.sub(lambda m:(lambda nc:m.group(0) if nc==m.group(2) else f'{m.group(1)}-{nc}{m.group(3)}')(corp_new2(m.group(1),m.group(2),m.group(3))),seg)
    return BASE.sub(lambda mm: map_fn(mm.group(0)),seg)
# new heading slugs per dest (computed from FINAL heading text) and fill AMAP
for nf,dd in dest.items():
    seen=collections.Counter(); fence=False
    src_=dd['src']; oc_=OLDCH[src_]
    for idx,(l,tag) in enumerate(zip(dd['lines'],dd['tags'])):
        if l.startswith('```'): fence=not fence
        if fence: continue
        mm=HEAD.match(l)
        if mm:
            hl=l if tag=='GEN' else corp_id_sub(cite_rewrite(l,oc_,dd['ch'],where=nf))
            mm2=HEAD.match(hl)
            s=slug(mm2.group(2)); n=seen[s]; seen[s]+=1; ns=s if n==0 else f"{s}-{n}"
            if tag and tag!='GEN': AMAP[tag]=(nf,ns)
            if l.startswith('# '): dd['h1slug']=ns
    # explicit <a id> lines that equal the old slug of the following heading -> new slug
    for i,l in enumerate(dd['lines']):
        m=re.match(r'^<a id="([^"]+)"></a>\s*$',l)
        if not m: continue
        j=i+1
        while j<len(dd['lines']) and (dd['lines'][j].strip()=='' or re.match(r'^<a id="[^"]+"></a>\s*$',dd['lines'][j])): j+=1
        if j<len(dd['lines']) and dd['tags'][j] not in (None,'GEN'):
            of_,os_=dd['tags'][j]
            if m.group(1)==os_ and AMAP.get(dd['tags'][j]):
                dd['lines'][i]=f'<a id="{AMAP[dd["tags"][j]][1]}"></a>'; STATS['anchor_ids_renamed']+=1
            else:
                od=OLDNUM.get(dd['tags'][j]); mh=re.match(r'#{2,6} (\d+(?:\.\d+)*)',dd['lines'][j])
                if od and mh and m.group(1).startswith(od+'-'):
                    nd=mh.group(1).replace('.','')
                    if nd!=od:
                        nid=f'{nd}-{m.group(1)[len(od)+1:]}'; dd['lines'][i]=f'<a id="{nid}"></a>'; STATS['anchor_ids_renumbered']+=1; AMAP[(dd['src'],m.group(1))]=(nf,nid)
def inline_anchor_pass():
    for nf,dd in dest.items():
        oc_=OLDCH[dd['src']]; L=dd['lines']; T=dd['tags']; heads=[]
        for i,l in enumerate(L):
            m=re.match(r'^### (\d+)\. ',l)
            if m and T[i]!='GEN':
                nn=int(m.group(1)); on=next((n for n in range(0,40) if smap(oc_,n)==(dd['ch'],nn)),None)
                s=i
                while s>0 and (L[s-1].strip()=='' or ANCH.match(L[s-1])): s-=1
                heads.append((s,on))
        for k,(s,on) in enumerate(heads):
            e=heads[k+1][0] if k+1<len(heads) else len(L)
            if on is None: continue
            newn=smap(oc_,on)[1]
            for i in range(s,e):
                if T[i]=='GEN' or '<a id="' not in L[i]: continue
                def r(m):
                    id_=m.group(1)
                    if (dd['src'],id_) in AMAP and AMAP[(dd['src'],id_)] is not None: return m.group(0)
                    mm=re.match(r'^(\d+)-',id_)
                    if not mm: return m.group(0)
                    dg=mm.group(1)
                    if not dg.startswith(str(on)) or newn==on: return m.group(0)
                    nid=str(newn)+dg[len(str(on)):]+id_[len(dg):]
                    AMAP[(dd['src'],id_)]=(nf,nid); STATS['inline_anchor_renumbered']+=1
                    return f'<a id="{nid}"'
                L[i]=re.sub(r'<a id="([^"]+)"',r,L[i])
inline_anchor_pass()
for nf,dd in dest.items():
    if 'h1old' in dd:
        of,s1,ids=dd['h1old']; AMAP[(of,s1)]=(nf,dd['h1slug'])
        for i_ in ids: AMAP[(of,i_)]=(nf,dd['h1slug'])
# ====================================================================== assemble destination files
CHAINOLD=re.search(r'CORE_CHAIN = \((.*?)\n\)',open('tools/footer_audit.py').read(),re.S).group(1)
CHAINOLD=re.findall(r'"([^"]+)"',CHAINOLD)
chain_new=[]
for e in CHAINOLD:
    b=e.split('#')[0]
    if b in SRCFILES:
        ds=sorted([nf for nf,d in dest.items() if d['src']==b],key=lambda x:dest[x]['ch']); chain_new+=ds
    else: chain_new.append(FNMAP.get(b,b))
# the chain must be unique, ordered
seen=set(); chain_new=[x for x in chain_new if not (x in seen or seen.add(x))]
print('chain len',len(chain_new))
NEIGH={f:(chain_new[i-1] if i>0 else None,chain_new[i+1] if i+1<len(chain_new) else None) for i,f in enumerate(chain_new)}
PREV=re.compile(r'^\*\*Previous file:\*\* \[[^\]]+\]\([^)]+\)\s*$'); NEXT=re.compile(r'^\*\*Next file:\*\* \[[^\]]+\]\([^)]+\)\s*$')
newtexts={}
def foot_lines(nf,extras,orig_prev,orig_next,oc,ch,src):
    ft=['','---','']
    for e in extras: ft+=[e,'']
    p,n_=NEIGH.get(nf,(None,None))
    if p: ft+=[f"**Previous file:** [{p}]({p})",'']
    elif orig_prev: ft+=[orig_prev,'']
    if n_: ft+=[f"**Next file:** [{n_}]({n_})"]
    elif orig_next: ft+=[orig_next]
    return ft
for nf,dd in dest.items():
    src=dd['src']; oc=OLDCH[src]
    lines=[]
    for l,tag in zip(dd['lines'],dd['tags']):
        lines.append(l if tag=='GEN' else process_line(l,'live',oc,dd['ch'],src,nf,where=nf))
    while lines and lines[-1].strip() in ('','---','<br>'): lines.pop()
    worked=[process_line(w,'live',oc,dd['ch'],src,nf,where=nf) for w in dd.get('worked',[])]
    # trailing Continue-to / Worked-examples lines left in the body (single-file Part A chapters)
    cont=[]
    while lines and (lines[-1].strip()=='' or lines[-1].startswith('*Continue to') or lines[-1].startswith('*Worked examples') or lines[-1].strip()=='<br>'):
        x=lines.pop()
        if x.startswith('*Worked examples'): worked.insert(0,x)
        elif x.startswith('*Continue to'): cont.append(x); REV['continue_lines_dropped']+=1
    footer=dd.get('footer_src') or parse(src)[2]
    extras=[];op=on=None
    for l in footer:
        if PREV.match(l): op=process_line(l,'live',oc,dd['ch'],src,nf,where=nf)
        elif NEXT.match(l): on=process_line(l,'live',oc,dd['ch'],src,nf,where=nf)
        elif l.strip() and l.strip()!='---': extras.append(process_line(l,'live',oc,dd['ch'],src,nf,where=nf))
    extras+=worked
    newtexts[nf]='\n'.join(lines)+'\n'+'\n'.join(foot_lines(nf,extras,op,on,oc,dd['ch'],src))+'\n'

# ====================================================================== global pass
LBL=re.compile(r'("label":\s*")([^"]*)("\s*,\s*"href":\s*")([^"]*)(")')
PAIR=re.compile(r'(?<![\w/.-])((?:[\w.-]+/)*)(core_\d\d\.\d{3}_[a-z0-9_]+\.md)(#[A-Za-z0-9_\-]+)')
def data_links(nt,p):
    def a(m):
        nh,ctx=link_target_final(m.group(4),p,p); lab=m.group(2)
        if ctx and ctx[0] is not None:
            esc='\\u00a7' in lab
            raw=json.loads('"'+lab+'"') if esc else lab
            new=cite_rewrite(raw,ctx[0],ctx[1],force_q=ctx[1])
            lab=json.dumps(new,ensure_ascii=True)[1:-1] if esc else new
            REV['data_label']+=1
        return m.group(1)+lab+m.group(3)+m.group(4)+m.group(5)
    nt=LBL.sub(a,nt)
    def b(m):
        nh,_=link_target_final(m.group(1)+m.group(2)+m.group(3),p,p); return nh
    return PAIR.sub(b,nt)
COREHOME=re.compile(r'^(Core home: )(\d+)(\s*)$')

SKIPD={'.git','archive','translations','_pages_site','node_modules','__pycache__','_to_delete','translation_drafts'}
DATED=('evidence/','evaluation/results/','project/MEMLOG','project/translation_drafts/','project/trials/')
HISTT=('tools/ch1_integration','tools/ch1_reading_arc','tools/ch1_part_b_consecutive','tools/ch1_market_structure','tools/ch8_','tools/core_filename_normalize','tools/ch06_','tools/renumber_','tools/chapter_insertion','tools/chapter_numbering_inverse','tools/chapters.py')
WLT=('tools/corpus_paths.py','tools/architecture/audit_scope_registry.json','tools/ch5_nested_list_candidate_audit.py')
OLD10=OLD['10']
GST=collections.Counter(); changed=[]
SKIPFILES={'tools/architecture/chapter_numbers.json'}
H1MAP={}
for nf_,dd_ in dest.items():
    if 'h1old' in dd_: H1MAP[dd_['h1old'][1]]=dd_['h1slug']
todo=[]
for r_,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in SKIPD]
    for f in fs:
        p=os.path.join(r_,f)[2:]
        if p in SKIPFILES: continue
        if not (f.endswith(('.md','.json','.py','.txt','.yml','.yaml','.toml','.html','.mmd','.csv','.mdc')) or f=='Makefile'): continue
        if p in SRCFILES: continue
        todo.append(p)
for p in todo:
    try: t=open(p,encoding='utf-8').read()
    except Exception: continue
    dated=p.startswith(DATED) or p=='doc_architecture.md'
    if p.startswith(HISTT): GST['hist_skipped']+=1; continue
    if p.endswith('.md'):
        ctx=None;ctx_new=None
        mm=re.match(r'core_(\d\d)\.',p)
        if mm and '/' not in p: ctx=int(mm.group(1)); ctx_new=NEWCH_OF.get(FNMAP.get(p,p),ctx)
        mode='dated' if dated else 'live'
        curnew=FNMAP.get(p,p)
        nt='\n'.join(process_line(l,mode,ctx,ctx_new,p,curnew,where=p) if l.strip() else l for l in t.split('\n'))
        if p.startswith('corpus_') and mode=='live':
            def ch_(l):
                m=COREHOME.match(l)
                if not m: return l
                n=int(m.group(2)); mp=re.match(r'.*/(?:cjs|ci|cs|cf)_(\d\d)\.',p); newp=CORPREN.get(p); 
                if newp and mp and n==int(mp.group(1)): nv=int(re.match(r'.*/(?:cjs|ci|cs|cf)_(\d\d)\.',newp).group(1))
                else: nv=FIRST.get(n,n)
                GST['core_home']+= (nv!=n)
                return f"{m.group(1)}{nv:02d}{m.group(3)}" if len(m.group(2))==2 else f"{m.group(1)}{nv}{m.group(3)}"
            nt='\n'.join(ch_(l) for l in nt.split('\n'))
        if ctx is not None and curnew in NEIGH:
            pv,nx=NEIGH[curnew]; o=[]
            for l in nt.split('\n'):
                if PREV.match(l) and pv: l=f"**Previous file:** [{pv}]({pv})"
                elif NEXT.match(l) and nx: l=f"**Next file:** [{nx}]({nx})"
                o.append(l)
            nt='\n'.join(o)
        if mode=='dated': pass
        else: pass
    else:
        if dated: continue
        nt=t
        if p in WLT:
            L=nt.split('\n'); o=[]
            for l in L:
                m=re.match(r'^(\s*)(["\'])'+re.escape(OLD10)+r'\2(,?)\s*$',l)
                if m:
                    for k,f_ in enumerate(THREE10): o.append(f"{m.group(1)}{m.group(2)}{f_}{m.group(2)}"+(',' if (m.group(3) or k<2) else ''))
                else: o.append(l)
            nt='\n'.join(o)
        nt=data_links(nt,p)
        if p.endswith('.json'):
            esc=('\\u00a7' in nt) and ('§' not in nt)
            tmp=nt.replace('\\u00a7','§') if esc else nt
            tmp=cite_rewrite(tmp,None,None,where=p)
            nt=tmp.replace('§','\\u00a7') if esc else tmp
            GST['json_cites']+=1
        nt=FRAGCORP.sub(lambda m:(lambda nc:m.group(0) if nc==m.group(2) else f'{m.group(1)}-{nc}{m.group(3)}')(corp_new2(m.group(1),m.group(2),m.group(3))),nt)
        nt=BASE.sub(lambda mm: map_fn(mm.group(0)),nt)
        nt=corp_id_sub(nt,GST)
        nt=FRAGCORP2.sub(lambda m:(lambda nc:m.group(0) if nc==m.group(2) else f'{m.group(1)}-{nc}{m.group(3)}')(corp_new2(m.group(1),m.group(2),m.group(3))),nt)
        for o_,n_ in H1MAP.items():
            if o_ in nt: nt=re.sub(r'(?<![a-z0-9-])'+re.escape(o_)+r'(?![a-z0-9-])',n_,nt); GST['h1slug_in_data']+=1
    if nt!=t:
        changed.append(p); GST['files_changed']+=1
        if APPLY: open(p,'w',encoding='utf-8').write(nt)
# dated files: corpus file/ids in link targets already handled in link_target_final; also core names in bare dated text untouched
# ---- write destination files
if APPLY:
    for of in SRCFILES: os.remove(of)
    for nf,txt in newtexts.items(): open(nf,'w',encoding='utf-8').write(txt)
    for f,nf in FNMAP.items():
        if f not in SRCFILES and os.path.exists(f): os.rename(f,nf)
    for p,n in CORPREN.items(): os.rename(p,n)
# ---- registry
REGP='tools/architecture/chapter_numbers.json'
reg=json.load(open(REGP)); rows=reg['chapters']; newrows=[]; handled=set()
for r in rows:
    df=r['destination_file']
    if r['layer']=='CORE':
        base=df
        if base in SRCFILES:
            ds=sorted([nf for nf,d in dest.items() if d['src']==base],key=lambda x:dest[x]['ch'])
            for nf in ds:
                c=dest[nf]['ch']; x=dict(r); x.update(destination_file=nf,display_id=f"{c}.000",machine_id=f"{c:02d}000",machine_number=f"{c:02d}000",core_home=f"{c:02d}",title=str(c),ordinal_name=str(c))
                newrows.append(x)
        elif base in FNMAP:
            m=re.match(r'core_(06)\.(\d{3})',FNMAP[base]); x=dict(r); x.update(destination_file=FNMAP[base],display_id=f"6.{m.group(2)}",machine_id=f"06{m.group(2)}",machine_number=f"06{m.group(2)}"); newrows.append(x)
        else: newrows.append(r)
    else:
        x=dict(r); p=None
        d0=r.get('destination_file','')
        for k,v in r.items():
            if isinstance(v,str) and not k.startswith('legacy') and k not in ('old_id','original_file'):
                nv=corp_id_sub(v)
                if nv!=v: x[k]=nv
        mfn=re.search(r'(cjs|ci|cs|cf)_(\d\d)\.(\d+)_',d0)
        if mfn:
            nc=corp_new2(mfn.group(1),mfn.group(2),mfn.group(3))
            if nc!=mfn.group(2):
                x['core_home']=nc
                for k in ('machine_id','machine_number'):
                    if k in x and isinstance(x[k],str) and x[k][:2]==mfn.group(2): x[k]=nc+x[k][2:]
        newrows.append(x)
reg['chapters']=newrows
if APPLY: json.dump(reg,open(REGP,'w'),indent=2,ensure_ascii=False); open(REGP,'a').write('\n')
# ---- CORE_CHAIN
if APPLY:
    p='tools/footer_audit.py'; t=open(p).read()
    new='CORE_CHAIN = (\n'+''.join(f'    "{e}",\n' for e in chain_new)+')'
    open(p,'w').write(re.sub(r'CORE_CHAIN = \(.*?\n\)',lambda m:new,t,count=1,flags=re.S))
print('global:',dict(GST),'files changed:',len(changed))
print('REV:',dict(REV)); print('UNRESOLVED frag links:',len(UNRES))
json.dump({'unres':UNRES[:300],'review':REVLIST[:500],'chain':chain_new,'corpren':CORPREN},open('/tmp/chapters_report.json','w'),indent=1)
