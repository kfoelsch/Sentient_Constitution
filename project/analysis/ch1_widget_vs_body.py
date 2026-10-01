import re,json,collections
P=json.load(open('/tmp/an/prin.json'))
home=open('core_05__definitions_home.md').read()
lab={m.group(3):m.group(1) for m in re.finditer(r'\[([^\]]+)\]\((core_05[^)#]*)#([^)]+)\)',home)}
def canon(a):
    if a in lab: return lab[a]
    m=re.match(r'^(.*)-[acmoe]$',a)
    if m and m.group(1) in lab: return lab[m.group(1)]
    return None
by=collections.defaultdict(list)
for p in P: by[p['file']].append(p)
out={}
for f,ps in by.items():
    L=open(f).read().split('\n')
    for i,p in enumerate(ps):
        end=ps[i+1]['body_start'] if i+1<len(ps) else len(L)
        txt='\n'.join(L[p['body_start']:end])
        wid=re.search(r'<details>(?:(?!</details>).)*?Definitions · Assessment · Compliance.*?</details>',txt,flags=re.S)
        body=txt.replace(wid.group(0),'') if wid else txt
        bl=set();unk=set()
        for u in re.findall(r'\]\((core_05[^)]*)\)',body):
            a=u.split('#')[-1]; c=canon(a)
            (bl.add(c) if c else unk.add(a))
        wl=set()
        for n,u in p['rows']:
            c=canon(u.split('#')[-1]); wl.add(c or n)
        out[p['num']]=dict(title=p['title'],w=sorted(wl),b=sorted(bl),unk=sorted(unk),has=bool(p['rows']))
json.dump(out,open('/tmp/an/cmp.json','w'),indent=1)
