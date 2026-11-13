import re,sys,os,collections
root=sys.argv[1]; os.chdir(root)
rep=collections.defaultdict(list)
for l in open(sys.argv[2]):
    m=re.match(r'(\S+?):(\d+):(\d+): \[PART-CITE-CHAPTER-01:part-mismatch\] Part (\w).*?is Part (\w)(?:,| not|\b)',l)
    if m: 
        mm=re.search(r'is Part (\w)',l); rep[m.group(1)].append((int(m.group(2)),int(m.group(3)),m.group(4),mm.group(1)))
n=0
for f,items in rep.items():
    L=open(f,encoding='utf-8').read().split('\n')
    for ln,col,old,new in sorted(items,reverse=True):
        s=L[ln-1]; i=col-1
        if s[i:i+6]==f'Part {old}': L[ln-1]=s[:i]+f'Part {new}'+s[i+6:]; n+=1
        else: print('MISS',f,ln,col,s[i:i+12])
    open(f,'w',encoding='utf-8').write('\n'.join(L))
print('fixed',n)
