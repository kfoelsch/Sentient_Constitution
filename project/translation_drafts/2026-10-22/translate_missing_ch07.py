#!/usr/bin/env python3
"""Create unreviewed Chapter Seven drafts for missing locales.

Google Translate handles prose segments only. Markdown links, IDs, code,
formatting, HTML, and line structure stay verbatim.
"""
from __future__ import annotations
import json,re,sys,urllib.parse,urllib.request,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; SOURCE=ROOT/'core_07.000_charters.md'
TARGETS=[x for x in sys.argv[1:] if not x.startswith('--')] or ['ru','te','th','tr','ur','vi']; FORCE='--force' in sys.argv
FENCE=re.compile(r'^\s*```')
PREFIX=re.compile(r'^(\s*(?:(?:>\s*)+|(?:[-+*]\s+)|(?:\d+[.)]\s+)|(?:#{1,6}\s+)))')
LINK=re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
FIXED=re.compile(r'`[^`]*`|<[^>]+>|(?:https?://|\.\.?/)[^\s<>\])]+|\*\*|__|[*_`|]')

def translate_batch(items,lang):
 out=[]
 for start in range(0,len(items),24):
  batch=items[start:start+24]
  params=[('client','gtx'),('sl','en'),('tl',lang),('format','text')]+[('q',x) for x in batch]
  url='https://translate.googleapis.com/translate_a/t?'+urllib.parse.urlencode(params)
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  last=None
  for attempt in range(3):
   try:
    data=json.loads(urllib.request.urlopen(req,timeout=30).read().decode('utf-8'))
    if not isinstance(data,list) or len(data)!=len(batch):raise RuntimeError(f'expected {len(batch)} results, got {len(data) if isinstance(data,list) else type(data)}')
    out.extend(data);last=None;break
   except Exception as e:
    last=e;time.sleep(attempt+1)
  if last:raise last
 return out

def line_segments(line):
 prefix_match=PREFIX.match(line); prefix=prefix_match.group(1) if prefix_match else ''
 body=line[len(prefix):]
 parts=[('fixed',prefix)] if prefix else []
 pos=0
 # Links are handled specially: translate only their displayed label.
 for m in LINK.finditer(body):
  if m.start()>pos: parts.extend(split_inline(body[pos:m.start()]))
  parts.append(('fixed','['));parts.extend(split_inline(m.group(1)));parts.append(('fixed',']('+m.group(2)+')'))
  pos=m.end()
 if pos<len(body):parts.extend(split_inline(body[pos:]))
 return parts

def split_inline(s):
 parts=[];pos=0
 for m in FIXED.finditer(s):
  if m.start()>pos:parts.append(('text',s[pos:m.start()]))
  parts.append(('fixed',m.group(0)));pos=m.end()
 if pos<len(s):parts.append(('text',s[pos:]))
 return parts

def translate_document(src,lang):
 records=[];pending=[];fence=False
 for raw in src.splitlines(keepends=True):
  if FENCE.match(raw):
   records.append(('fixed',raw));fence=not fence;continue
  if fence or not raw.strip(): records.append(('fixed',raw));continue
  ending='\n' if raw.endswith('\n') else '';line=raw[:-1] if ending else raw
  parts=line_segments(line); records.extend(parts);records.append(('fixed',ending))
 # Batch all human-language text segments, preserving their positions exactly.
 indices=[];items=[]
 for i,(kind,value) in enumerate(records):
  if kind!='text' or not value.strip():continue
  lead=value[:len(value)-len(value.lstrip())];trail=value[len(value.rstrip()):]
  core=value.strip()
  records[i]=('textwrap',(lead,trail))
  indices.append(i);items.append(core)
 translations=translate_batch(items,lang)
 for i,out in zip(indices,translations):records[i]=('fixed',records[i][1][0]+out+records[i][1][1])
 return ''.join(value for _,value in records)

# Convert source-relative Markdown links to links from translations/<locale>/.
src=SOURCE.read_text(encoding='utf-8')
src=re.sub(r'\]\((?!https?://|#|\.\.?/)([^)]+)\)',r'](../../\1)',src)
def main():
 for lang in TARGETS:
  if not re.fullmatch(r'[a-z]{2,3}',lang):raise SystemExit(f'invalid locale {lang}')
  dest=ROOT/'translations'/lang/'core_07_charters.md'
  if dest.exists() and not FORCE:print(f'{lang}: already exists; skipped');continue
  translated=translate_document(src,lang)
  status=translate_batch(['AI-assisted translation draft — unreviewed; no independent fluent-reader review has been completed. This reader-language file is non-binding; the numbered English source remains controlling.'],lang)[0]
  dest.write_text(f'> **{status}**\n\n{translated}',encoding='utf-8')
  readme=ROOT/'translations'/lang/'README.md'
  if readme.exists():
   rs=readme.read_text(encoding='utf-8')
   row='| [core_07_charters.md](core_07_charters.md) | [core_07.000_charters.md](../../core_07.000_charters.md) |'
   if 'core_07_charters.md' not in rs:
    lines=rs.splitlines();idx=next((i for i,x in enumerate(lines) if x.startswith('| [core_07_')),None)
    if idx is None:idx=next((i for i,x in enumerate(lines) if x.startswith('| [core_06_')),len(lines)-1)+1
    lines.insert(idx,row);rs='\n'.join(lines)+'\n'
   note='**Chapter Seven status.** [Chapter Seven charters](core_07_charters.md) is an AI-assisted translation draft without independent fluent-reader review. It is non-binding; the numbered English source controls.\n\n'
   if 'Chapter Seven status.' not in rs:
    idx=rs.find('## ')
    if idx>=0:rs=rs[:idx]+note+rs[idx:]
   readme.write_text(rs,encoding='utf-8')
  print(f'{lang}: wrote {dest.relative_to(ROOT)} ({dest.stat().st_size} bytes)',flush=True)

if __name__ == "__main__":
 main()
