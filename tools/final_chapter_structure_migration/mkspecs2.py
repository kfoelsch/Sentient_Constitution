import os,sys,json,re
root=sys.argv[1]; os.chdir(root)
src=open('tools/footer_audit.py').read()
blk=re.search(r'CORE_CHAIN = \((.*?)\n\)',src,re.S).group(1)
chain=re.findall(r'"([^"]+)"',blk)
def slug(t):
    t=re.sub(r'[^\w\- ]','',t.strip().lower(),flags=re.U); return t.replace(' ','-')
# ---- Ch10
A='core_10.000_institutional_alignment_certification.md'
B='core_10.010_institutional_alignment_certification_forum_process_outcomes.md'
C='core_10.020_institutional_alignment_certification_record_recertification.md'
ch10={'reader':'10.000','parts':[
 {'file':A,'reader':'10.000','sections':[1,2,3,4,5],'h1':'CHAPTER TEN, PART A: INSTITUTIONAL ALIGNMENT CERTIFICATION — EVALUATION','label':'Chapter Ten, Part A','desc':'**institutional evaluation** (the evaluation areas and the rights floor)'},
 {'file':B,'reader':'10.010','sections':[6,7],'h1':'CHAPTER TEN, PART B: INSTITUTIONAL ALIGNMENT CERTIFICATION — HOW THE FORUM DECIDES AND WHAT FOLLOWS','label':'Chapter Ten, Part B','desc':'the **forum process and outcomes** of institutional alignment certification'},
 {'file':C,'reader':'10.020','sections':[8,9,10,11],'h1':'CHAPTER TEN, PART C: INSTITUTIONAL ALIGNMENT CERTIFICATION — INSTITUTIONAL RECORDS, RECERTIFICATION, AND STANDING','label':'Chapter Ten, Part C','desc':'**Institutional Certification Records, recertification, and standing** consequences of institutional alignment certification'}]}
# ---- Ch1
S0='core_01.000_values_principles.md';S1='core_01.005_interaction_interpretation.md';S2='core_01.010_stewardship_capacity_principles.md'
def P(f,r,secs,h,l,d): return {'file':f,'reader':r,'sections':secs,'h1':h,'label':l,'desc':d}
ch1={
 S0:{'reader':'1.000','parts':[
  P('core_01.000_values_principles.md','1.000',list(range(1,8)),'CHAPTER 01, PART A: PURPOSE AND THE FLOURISHING AIM','Chapter One, Part A','the **purpose** of the Constitution and the **Flourishing Aim** (wellbeing, safety, truth, trust, freedom)'),
  P('core_01.010_values_principles_continuity_aim.md','1.010',list(range(8,13)),'CHAPTER 01, PART B: THE CONTINUITY AIM','Chapter One, Part B','the **Continuity Aim** (shared-system capacity, resilience, market structure, and the systemic evaluation requirement)')]},
 S1:{'reader':'1.005','parts':[
  P('core_01.020_interaction_interpretation.md','1.020',[13,14],'CHAPTER 01, PART C: COLLISION RESOLUTION AND THE OVERRIDE LIMIT','Chapter One, Part C','**constitutional collision resolution** and the **prohibition on absolute override**'),
  P('core_01.030_constitutional_interpretation.md','1.030',[15],'CHAPTER 01, PART D: CONSTITUTIONAL INTERPRETATION','Chapter One, Part D','**constitutional interpretation**')]},
 S2:{'reader':'1.010','parts':[
  P('core_01.040_stewardship_capacity_principles.md','1.040',[16,17],'CHAPTER 01, PART E: STEWARDSHIP AND THE STEWARD ROLE','Chapter One, Part E','**stewardship** and the **Steward role**'),
  P('core_01.050_governance_incentive_application.md','1.050',[18,19,20],'CHAPTER 01, PART F: GOVERNANCE, INCENTIVE ALIGNMENT, AND INTEGRATED APPLICATION','Chapter One, Part F','**governance under stewardship discipline**, **incentive alignment and system capture**, and **integrated application**')]}}
def entry(f,h1,frag): return f+('#'+slug(h1) if frag else '')
# stage-2 chain (Ch10 split)
def build(chain,replace):
    out=[]
    for e in chain:
        b=e.split('#')[0]
        out+= replace.get(b,[e])
    return out
c10=build(chain,{A:[entry(p['file'],p['h1'],True) for p in ch10['parts']]})
c1=build(chain,{S0:[entry(p['file'],p['h1'],False) for p in ch1[S0]['parts']],S1:[entry(p['file'],p['h1'],False) for p in ch1[S1]['parts']],S2:[entry(p['file'],p['h1'],False) for p in ch1[S2]['parts']]})
def spec(sources,ch): return {'sources':sources,'order':[e.split('#')[0] for e in ch],'chain':{e.split('#')[0]:e for e in ch if '#' in e},'chain_full':ch}

json.dump(spec(ch1,c1),open(sys.argv[2],'w'),indent=1)
print(len(chain),len(c10),len(c1))
