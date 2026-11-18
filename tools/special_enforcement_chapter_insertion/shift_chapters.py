#!/usr/bin/env python3
"""One-off record: insert the new Chapter Twenty-Five (Special Enforcement) and shift old Chapters 25-29 to 26-30.

Adapted from tools/enforcement_chapter_insertion/shift_chapters.py (575th move).

usage: shift_chapters.py ROOT [--apply]    (default is a dry run that writes a report to /tmp)

Rewrites, outside archive/, evidence/, translations/, translation_drafts/, generated indexes and earlier one-off
tools: chapter cites in prose (words and digits, chains and ranges, upper/title/lower case), slug forms of those cites
in link fragments and anchors, reader numbers (NN.000), core filenames, corpus-layer homes (cjs/ci/cs/cf files and
CJS-/CI-/CS-/CF- ids with a 25-29 home) and the registry rows. Generated files are regenerated afterwards by make.
"""
import os,re,sys,json,collections
ROOT=os.path.abspath(sys.argv[1]); APPLY='--apply' in sys.argv
os.chdir(ROOT)
LO,HI=25,29
def sh(n): return n+1 if LO<=n<=HI else n
UNITS=['','one','two','three','four','five','six','seven','eight','nine']
TEENS=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
def word(n):
    if n<10: return UNITS[n]
    if n<20: return TEENS[n-10]
    if n==20: return 'twenty'
    if n==30: return 'thirty'
    return 'twenty-'+UNITS[n-20]
N2W={n:word(n) for n in range(1,31)}
W2N={w:n for n,w in N2W.items() if n<30}
WALT='|'.join(sorted(W2N,key=len,reverse=True))
def style(tok,new):
    if tok.isupper(): return new.upper()
    if tok[0].isupper(): return '-'.join(p.capitalize() for p in new.split('-'))
    return new
SKIP_DIRS={'.git','_pages_site','archive','evidence','translations','results','node_modules','__pycache__','_local_backup','_to_delete','translation_drafts','final_chapter_structure_migration','one_off','enforcement_chapter_insertion','special_enforcement_chapter_insertion'}
SKIP_PATHS={'ai_corpus/indexes','doc_architecture/generated','tools/chapter_insertion_diff.py'}
EXTS={'.md','.json','.py','.txt','.yml','.yaml','.sh','.html','.js','.toml','.csv'}
STATS=collections.Counter(); CROSS=[]; DIGITCH=collections.Counter()
# ---- chapter-cite chains (prose)
TOKW=r'(?:%s|\d{1,2})'%WALT
HEAD=re.compile(r'\bChapters?(?:\*\*)?(?:[ \t]+|(?=\[))(?:\*\*)?',re.I)
TOK=re.compile(r'(?:\[\s*)?(?P<w>%s)(?![\w-])(?:\s*\])?(?:\((?:[^)\s]*)\))?'%TOKW,re.I)
SEC=re.compile(r'\s*§§?\s*\d+(?:\.\d+)*(?:\s*(?:–|-|—|,|and)\s*§?\d+(?:\.\d+)*)*')
SEP=re.compile(r'(?:\s*,\s*(?:and\s+)?|\s+and\s+|\s*(?:–|—)\s*|\s+through\s+|\s+to\s+)(?:\*\*)?(?:Chapters?(?:\*\*)?[ \t]+(?:\*\*)?)?',re.I)
def tokval(w):
    return int(w) if w.isdigit() else W2N.get(w.lower())
def chain_rewrite(text,path):
    edits=[]; vals_by_chain=[]
    for h in HEAD.finditer(text):
        pos=h.end(); toks=[]
        m=TOK.match(text,pos)
        while m:
            toks.append((m.start('w'),m.end('w'),m.group('w'))); pos=m.end()
            s=SEC.match(text,pos)
            if s: pos=s.end()
            sp=SEP.match(text,pos)
            if not sp: break
            m2=TOK.match(text,sp.end())
            if not m2: break
            m=m2; pos=sp.end()
        vals=[tokval(w) for _,_,w in toks]
        if any(v is not None and v>=LO for v in vals) and any(v is not None and v<LO for v in vals):
            # crossing the insertion point; ranges only matter when joined by through/dash
            CROSS.append((path,text[h.start():toks[-1][1]+1][:120]))
        for (s_,e_,w),v in zip(toks,vals):
            if v is not None and LO<=v<=HI:
                new=str(v+1) if w.isdigit() else style(w,N2W[v+1])
                edits.append((s_,e_,new)); STATS['chain']+=1
                if w.isdigit(): DIGITCH[text[max(0,s_-20):e_+12].replace('\n',' ')]+=1
    return apply(text,edits)
def apply(text,edits):
    edits=sorted(set(edits),reverse=True); out=text; last=len(text)+1
    for s,e,r in edits:
        if e>last: continue
        out=out[:s]+r+out[e:]; last=s
    return out
# ---- slug forms of the same cites
SLUGHEAD=re.compile(r'chapters?-',re.I)
SLUGTOK=re.compile(r'(?P<w>%s)(?![\w])'%WALT.replace(' ','-'),re.I)
SLUGSEP=re.compile(r'-(?:through|and|to)-',re.I)
def slug_rewrite(text):
    edits=[]
    for h in SLUGHEAD.finditer(text):
        if h.start()>0 and (text[h.start()-1].isalpha()): continue
        pos=h.end(); m=SLUGTOK.match(text,pos)
        while m:
            v=tokval(m.group('w'))
            if v is not None and LO<=v<=HI: edits.append((m.start('w'),m.end('w'),N2W[v+1])); STATS['slug']+=1
            sp=SLUGSEP.match(text,m.end())
            if not sp: break
            m=SLUGTOK.match(text,sp.end())
    return apply(text,edits)
# ---- reader numbers, filenames, corpus ids
RD=re.compile(r'(?<![\d.$/_\w-])(2[5-9])\.000(?![\d\w])')
CORE_FN=re.compile(r'\bcore_(2[5-9])\.000_')
LAY_FN=re.compile(r'\b(cjs|ci|cs|cf)_(2[5-9])\.(\d{3})_')
LAY_ID=re.compile(r'\b(CJS|CI|CS|CF)-(2[5-9])\.(\d)')
LAY_FRAG=re.compile(r'(?<![\w])(cjs|ci|cs|cf)-(2[5-9])(\d{3})(?!\d)',re.I)
def num_rewrite(text):
    def a(m): STATS['reader']+=1; return f'{int(m.group(1))+1}.000'
    text=RD.sub(a,text)
    text=CORE_FN.sub(lambda m:(STATS.update(core_fn=1),f'core_{int(m.group(1))+1}.000_')[1],text)
    text=LAY_FN.sub(lambda m:(STATS.update(lay_fn=1),f'{m.group(1)}_{int(m.group(2))+1}.{m.group(3)}_')[1],text)
    text=LAY_ID.sub(lambda m:(STATS.update(lay_id=1),f'{m.group(1)}-{int(m.group(2))+1}.{m.group(3)}')[1],text)
    text=LAY_FRAG.sub(lambda m:(STATS.update(lay_frag=1),f'{m.group(1)}-{int(m.group(2))+1}{m.group(3)}')[1],text)
    return text
def transform(text,path):
    t=chain_rewrite(text,path); t=slug_rewrite(t); t=num_rewrite(t); return t
# ---- walk
changed={}; 
for r,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in SKIP_DIRS]
    rel=os.path.relpath(r,'.')
    for f in fs:
        p=os.path.normpath(os.path.join(rel,f))
        if any(p.startswith(s) for s in SKIP_PATHS): continue
        if os.path.splitext(f)[1] not in EXTS and f not in ('Makefile',): continue
        try: t=open(p,encoding='utf-8').read()
        except Exception: continue
        n=transform(t,p)
        if n!=t: changed[p]=n
print('files changed',len(changed),dict(STATS))
# ---- renames
ren={}
for r,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in SKIP_DIRS]
    for f in fs:
        m=CORE_FN.match(f) or None
        m2=re.match(r'(core)_(2[5-9])\.000_(.*)$',f); m3=re.match(r'(cjs|ci|cs|cf)_(2[5-9])\.(\d{3})_(.*)$',f)
        p=os.path.normpath(os.path.join(r,f))
        if m2: ren[p]=os.path.join(r,f"core_{int(m2.group(2))+1}.000_{m2.group(3)}")
        elif m3: ren[p]=os.path.join(r,f"{m3.group(1)}_{int(m3.group(2))+1}.{m3.group(3)}_{m3.group(4)}")
print('renames',len(ren))
for k,v in sorted(ren.items()): print('  ',k,'->',v)
json.dump({'changed':sorted(changed),'cross':CROSS,'digit':DIGITCH.most_common(40)},open('shift_report_special.json','w'),indent=1)
if not APPLY: sys.exit(0)
for p,t in changed.items(): open(p,'w',encoding='utf-8').write(t)
order=sorted(ren.items(),key=lambda kv:kv[0],reverse=True)
for k,v in order:
    k2=k if os.path.exists(k) else None
    os.rename(k,v)
print('applied')
