import sys,importlib.util,collections
from pathlib import Path
orig=Path(sys.argv[1]); new=Path(sys.argv[2])
spec=importlib.util.spec_from_file_location('oid',str(orig)+'/tools/obligation_inventory_diff.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def tot(root):
    c=collections.Counter(); n=0; bysec=collections.Counter()
    for f in sorted(root.glob('core_*.md')):
        for it in m.inventory(f):
            n+=1; c[it.get('modality')]+=1
    return n,c
a=tot(orig); b=tot(new)
print('before',a[0],dict(a[1])); print('after ',b[0],dict(b[1])); print('equal counts:',a==b)
