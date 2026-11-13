import os,re,sys,json
root,specp,stage=sys.argv[1],sys.argv[2],sys.argv[3]
os.chdir(root); spec=json.load(open(specp)); n=0
HIST=('tools/ch1_integration','tools/ch1_reading_arc','tools/ch1_part_b_consecutive','tools/ch1_market_structure','tools/ch8_','tools/core_filename_normalize','tools/ch06_','tools/renumber_','tools/chapter_insertion','tools/chapter_numbering_inverse')+('tools/test_',)
# 1 CORE_CHAIN
p='tools/footer_audit.py'; t=open(p).read()
new='CORE_CHAIN = (\n'+''.join(f'    "{e}",\n' for e in spec['chain_full'])+')'
t2=re.sub(r'CORE_CHAIN = \(.*?\n\)',lambda m:new,t,count=1,flags=re.S)
if t2!=t: open(p,'w').write(t2); n+=1; print('patched CORE_CHAIN')
def files():
    for d in ('tools','tools/architecture'):
        for f in sorted(os.listdir(d)):
            q=os.path.join(d,f)
            if os.path.isfile(q) and f.endswith(('.py','.json')) and not q.startswith(HIST) and f!='chapter_numbers.json': yield q
if stage=='ch10':
    A='core_10.000_institutional_alignment_certification.md'
    three=[p['file'] for p in list(spec['sources'].values())[0]['parts']]
    WL=('tools/corpus_paths.py','tools/architecture/audit_scope_registry.json','tools/ch5_nested_list_candidate_audit.py')
    for q in files():
        if q not in WL: continue
        t=open(q).read(); L=t.split('\n'); out=[]; ch=False
        for l in L:
            m=re.match(r'^(\s*)(["\'])'+re.escape(A)+r'\2(,?)\s*$',l)
            if m:
                for k,f in enumerate(three): out.append(f'{m.group(1)}{m.group(2)}{f}{m.group(2)}'+(',' if (m.group(3) or k<2) else '')); 
                ch=True
            else: out.append(l)
        t2='\n'.join(out)
        t2=t2.replace(f'("{A}",)','('+', '.join(f'"{f}"' for f in three)+',)')
        t2=t2.replace('core_10.000_*.md','core_10.*.md')
        if t2!=t: open(q,'w').write(t2); n+=1; print('patched',q)
else:
    six=[p['file'] for sp in spec['sources'].values() for p in sp['parts']]
    a,b,c='core_01.000_values_principles.md','core_01.020_interaction_interpretation.md','core_01.040_stewardship_capacity_principles.md'
    for q in files():
        if q=='tools/footer_audit.py': continue
        t=open(q).read(); L=t.split('\n'); out=[]; i=0; ch=False
        while i<len(L):
            if i+2<len(L) and a in L[i] and b in L[i+1] and c in L[i+2]:
                for f in six: out.append(L[i].replace(a,f))
                # fix trailing comma on last
                if not L[i+2].rstrip().endswith(','): out[-1]=out[-1].rstrip(',')
                i+=3; ch=True
            else: out.append(L[i]); i+=1
        t2='\n'.join(out)
        t2=re.sub(r'(["\'])'+re.escape(a)+r'\1(\s*,\s*)(["\'])'+re.escape(b)+r'\3\2(["\'])'+re.escape(c)+r'\4',lambda m:m.group(2).join(f'"{f}"' for f in six),t2)
        t2=t2.replace('core_01.000_*.md','core_01.*.md')
        if t2!=t: open(q,'w').write(t2); n+=1; print('patched',q)
print('tool files patched:',n)
