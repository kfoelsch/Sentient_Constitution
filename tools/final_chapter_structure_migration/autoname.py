import re,os,sys,subprocess,collections
def slug(t):
    t=re.sub(r'<[^>]+>','',t); t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t).strip().lower()
    t=re.sub(r'[^\w\- ]','',t,flags=re.U); return t.replace(' ','-')
def heads(path):
    seen=collections.Counter(); out={}; fence=False
    for l in open(path,encoding='utf-8').read().split('\n'):
        if l.startswith('```'): fence=not fence
        if fence: continue
        m=re.match(r'^(#{1,6}) (.*)',l)
        if m:
            s=slug(m.group(2)); n=seen[s]; seen[s]+=1; out[s if n==0 else f"{s}-{n}"]=m.group(2)
    return out
HC={}
tot=0; skipped=[]
for rnd in range(3):
    r=subprocess.run(['python3','tools/section_cite_name_audit.py'],capture_output=True,text=True).stdout
    items=re.findall(r'^\s*(\S+?):(\d+): SECTION-CITE-NAME-01: unnamed (.+?): section-number',r,re.M)
    if not items: break
    byfile=collections.defaultdict(list)
    for f,ln,c in items: byfile[f].append((int(ln),c))
    fixed=0
    for f,lst in byfile.items():
        L=open(f,encoding='utf-8').read().split('\n')
        for ln,c in lst:
            line=L[ln-1]; done=False
            for m in re.finditer(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]*)\)',line):
                lab=re.sub(r'[*_]','',m.group(1)).strip()
                if lab==c:
                    path,_,frag=m.group(2).partition('#'); tgt=os.path.join(os.path.dirname(f),path) if path else f
                    tgt=os.path.normpath(tgt)
                    if tgt not in HC and os.path.exists(tgt): HC[tgt]=heads(tgt)
                    h=HC.get(tgt,{}).get(frag)
                    if not h: continue
                    title=re.sub(r'^\d+(?:\.\d+)*\.?\s+','',h); title=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',title).replace('*','').strip().rstrip('.')
                    if not title: continue
                    new='['+m.group(1)+' '+title+']('+m.group(2)+')'
                    line=line[:m.start()]+new+line[m.end():]; done=True; fixed+=1; break
            if done: L[ln-1]=line
            else: skipped.append((f,ln,c))
        open(f,'w',encoding='utf-8').write('\n'.join(L))
    tot+=fixed
    if not fixed: break
print('autonamed',tot,'skipped',len(skipped))
for s in skipped[:20]: print('  skipped',s)
