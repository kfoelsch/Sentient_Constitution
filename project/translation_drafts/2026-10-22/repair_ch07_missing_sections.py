#!/usr/bin/env python3
"""Restore two incomplete Chapter Seven reader-language sections from source."""
import importlib.util,re
from pathlib import Path
p=Path(__file__).with_name('translate_missing_ch07.py')
spec=importlib.util.spec_from_file_location('translator',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
source=mod.SOURCE.read_text(encoding='utf-8')
source=re.sub(r'\]\((?!https?://|#|\.\.?/)([^)]+)\)',r'](../../\1)',source)
def span(text,anchor):
 marker=f'<a id="{anchor}"></a>';start=text.index(marker)
 m=re.search(r'<a\b[^>]*\bid=["\']([^"\']+)',text[start+len(marker):])
 end=start+len(marker)+m.start() if m else len(text)
 return start,end
for locale,anchor in [('bn','1-when-system-and-institutional-charters-are-required'),('hi','3-what-system-and-institutional-charters-must-state')]:
 s0,e0=span(source,anchor); chunk=source[s0:e0]
 target=mod.ROOT/'translations'/locale/'core_07_charters.md';text=target.read_text(encoding='utf-8')
 st,en=span(text,anchor);translated=mod.translate_document(chunk,locale)
 text=text[:st]+translated+text[en:];target.write_text(text,encoding='utf-8')
 print(locale,anchor,'restored',len(chunk),'source chars')
