#!/usr/bin/env python3
"""Translate reader-visible labels inside the Chapter Seven Mermaid diagram."""
import json,re,time,urllib.parse,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
LOCALES={'ru':'ru','te':'te','th':'th','tr':'tr','ur':'ur','vi':'vi'}
FENCE=re.compile(r'```mermaid\n(.*?)```',re.S)
QUOTED=re.compile(r'("[^"]*")')
BR=re.compile(r'(<br\s*/?>)',re.I)
def batch(items,lang):
 out=[]
 for start in range(0,len(items),20):
  group=items[start:start+20]
  params=[('client','gtx'),('sl','en'),('tl',lang)]+[('q',x) for x in group]
  url='https://translate.googleapis.com/translate_a/t?'+urllib.parse.urlencode(params)
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  for a in range(3):
   try:
    got=json.loads(urllib.request.urlopen(req,timeout=30).read().decode())
    if len(got)!=len(group):raise ValueError('translation result count mismatch')
    out.extend(got);break
   except Exception:
    if a==2:raise
    time.sleep(a+1)
 return out
for loc,lang in LOCALES.items():
 p=ROOT/'translations'/loc/'core_07_charters.md';s=p.read_text(encoding='utf-8')
 m=FENCE.search(s)
 if not m:raise SystemExit(f'{loc}: Mermaid diagram missing')
 block=m.group(1); quoted=list(QUOTED.finditer(block)); pieces=[]
 for q in quoted:
  content=q.group(1)[1:-1]
  pieces.append((q.start(),q.end(),content))
 # Translate visible portions, keeping every HTML line break and quote verbatim.
 work=[];records=[]
 for start,end,content in pieces:
  segs=BR.split(content);rec=[]
  for seg in segs:
   if BR.fullmatch(seg):rec.append(('fixed',seg))
   elif seg:rec.append(('text',seg));work.append(seg)
  records.append((start,end,rec))
 translated=iter(batch(work,lang));replacements=[]
 for start,end,rec in records:
  text=''.join(v if k=='fixed' else next(translated) for k,v in rec)
  replacements.append((start,end,'"'+text+'"'))
 new=block
 for start,end,value in reversed(replacements):
  # positions are against original block; apply replacements in reverse order
  new=new[:start]+value+new[end:]
 s=s[:m.start(1)]+new+s[m.end(1):]
 p.write_text(s,encoding='utf-8')
 print(loc,'Mermaid labels translated',len(quoted),flush=True)
