#!/usr/bin/env python3
"""One-off record: Chapter Twenty-Three Part B becomes Chapter Twenty-Four (sections 6-9 become 2-5, new section 1).

usage: promote_ch23_part_b.py ROOT [--apply]
Rewrites file name, link fragments into the file, and "Chapter Twenty-Three §6-9" cites outside the skipped trees.
"""
import os,re,sys
ROOT=os.path.abspath(sys.argv[1]); APPLY='--apply' in sys.argv; os.chdir(ROOT)
OLD='core_23.005_forum_families_escalation_timeliness_support.md'
NEW='core_24.000_forum_families_escalation_timeliness_support.md'
AMAP={
 '6-forum-family-definitions--accountability-through-adjudication':'2-forum-family-definitions--accountability-through-adjudication',
 '61-sentient-forums':'21-sentient-forums','62-technical-forum-domains':'22-technical-forum-domains',
 '63-institutional-forums':'23-institutional-forums','64-environment-forums':'24-environment-forums',
 '65-integrity-forums':'25-integrity-forums','66-constitutional-forums':'26-constitutional-forums',
 '67-provisional-implementation-operational-law':'27-provisional-implementation-operational-law',
 '7-escalation-and-questions-for-ruling':'3-escalation-and-questions-for-ruling',
 '8-timely-resolution-materiality-tiers-and-anti-delay-discipline':'4-timely-resolution-materiality-tiers-and-anti-delay-discipline',
 '81-emergency-measures-and-continuation-burden':'41-emergency-measures-and-continuation-burden',
 '9-forum-support-before-during-and-after-review--oversight-architecture':'5-forum-support-before-during-and-after-review--oversight-architecture',
 'chapter-twenty-three-part-b-forum-families-escalation-timely-resolution-and-support':'chapter-twenty-four-forum-families-escalation-timely-resolution-and-support',
}
PARTA_OLD='chapter-twenty-three-part-a-standards-routing-and-forum-cases'
PARTA_NEW='chapter-twenty-three-standards-routing-and-forum-cases'
SKIP_DIRS={'.git','_pages_site','archive','evidence','translations','results','node_modules','__pycache__','_local_backup','_to_delete','translation_drafts','final_chapter_structure_migration','one_off','enforcement_chapter_insertion','special_enforcement_chapter_insertion'}
SKIP_PATHS=('ai_corpus/indexes','doc_architecture/generated')
EXTS={'.md','.json','.py','.txt','.yml','.yaml','.sh','.html','.js','.toml','.csv'}
LINK=re.compile(re.escape(OLD)+r'#([a-z0-9-]+)')
CITE=re.compile(r"(Chapters? )(Twenty-Three|23)((?:,? Part B)?(?:’s|'s)?,? )(§§?|sections? )([6-9])(?![\d])")
PARTB=re.compile(r"Chapter (Twenty-Three|23),? Part B\b")
PARTA=re.compile(r"Chapter (Twenty-Three|23),? Part A\b")
cnt={'link':0,'cite':0,'partb':0,'parta':0,'anchorA':0}
def fix(t):
    def l(m):
        a=m.group(1); cnt['link']+=1; return NEW+'#'+AMAP.get(a,a)
    t=LINK.sub(l,t); t=t.replace(OLD,NEW)
    def c(m):
        cnt['cite']+=1; ch='Twenty-Four' if m.group(2)=='Twenty-Three' else '24'
        mid=m.group(3).replace(', Part B','').replace(' Part B','') or ' '
        return m.group(1)+ch+mid+m.group(4)+str(int(m.group(5))-4)
    t=CITE.sub(c,t)
    t,n=PARTB.subn(lambda m:'Chapter '+('Twenty-Four' if m.group(1)=='Twenty-Three' else '24'),t); cnt['partb']+=n
    t,n=PARTA.subn(lambda m:'Chapter '+m.group(1),t); cnt['parta']+=n
    n=t.count(PARTA_OLD); t=t.replace(PARTA_OLD,PARTA_NEW); cnt['anchorA']+=n
    return t
changed={}
for r,ds,fs in os.walk('.'):
    ds[:]=[d for d in ds if d not in SKIP_DIRS]
    for f in fs:
        p=os.path.normpath(os.path.join(r,f))
        if p.startswith(SKIP_PATHS): continue
        if os.path.splitext(f)[1] not in EXTS: continue
        try: t=open(p,encoding='utf-8').read()
        except Exception: continue
        n=fix(t)
        if n!=t: changed[p]=n
print(len(changed),cnt)
if APPLY:
    for p,t in changed.items(): open(p,'w',encoding='utf-8').write(t)
    os.rename(OLD,NEW); print('applied')
