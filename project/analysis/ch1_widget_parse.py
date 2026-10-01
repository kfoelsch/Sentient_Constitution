import re,json,collections
files=['core_01_a_values_principles.md','core_01_b_interaction_interpretation.md','core_01_c_stewardship_capacity_principles.md']
SUM='Definitions · Assessment · Compliance'
prin=[]
for f in files:
    L=open(f).read().split('\n')
    cur=None
    for i,l in enumerate(L):
        m=re.match(r'^(#{2,6})\s+(\d+(?:\.\d+)*)\.?\s+(.*)',l)
        if m:
            cur={'file':f,'line':i+1,'num':m.group(2),'title':m.group(3).strip(),'rows':[],'body_start':i}
            prin.append(cur); continue
        if cur is None: continue
        if SUM in l:
            j=i+1
            while j<len(L) and '</details>' not in L[j]:
                r=re.match(r'^\s*-\s+\[([^\]]+)\]\(([^)]*)\)',L[j])
                if r: cur['rows'].append((r.group(1),r.group(2)))
                j+=1
            cur['dac']=True
json.dump(prin,open('/tmp/an/prin.json','w'),indent=1)
w=[p for p in prin if p['rows']]
print(len(prin),len(w))
