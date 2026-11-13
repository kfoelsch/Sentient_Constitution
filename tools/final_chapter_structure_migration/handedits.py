"""Hand-edit stand-ins for the dry run: tool constants and front-door/working docs. Each is a worklist item."""
import re,os,json,sys
def sub(path,a,b,count=1):
    t=open(path,encoding='utf-8').read()
    if a not in t: print('  MISSING',path,a[:60]); return
    open(path,'w',encoding='utf-8').write(t.replace(a,b,count)); print('  edited',path)
# --- tool constants
sub('tools/owner_line_audit.py','''                part = (
                    original_match.group(2)
                    if original_match and int(original_match.group(1)) == int(m.group(1))
                    else None
                )''','''                part = (
                    original_match.group(2)
                    if original_match and int(original_match.group(1)) == int(m.group(1))
                    else None
                )
                if part and sum(1 for r in rows if r.get("core_home") == m.group(1) and r.get("layer") == "CORE") <= 1:
                    part = None  # Parts only where the chapter still has several files (Chapters 1 and 6)''')
sub('tools/corpus_markdown_audit.py','"### 2. Definition Traceability Requirement",\n        "### 3. Observability of Traceability Requirement",','"### 3. Definition Traceability Requirement",\n        "### 4. Observability of Traceability Requirement",')
sub('tools/corpus_markdown_audit.py','"#### 2.1 Common Evasion Patterns",\n        "#### 2.2 Reductive Evasion",','"#### 3.1 Common Evasion Patterns",\n        "#### 3.2 Reductive Evasion",')
# --- README
t=open('README.md',encoding='utf-8').read()
t=t.replace('the Preamble and Chapters 1–20','the Preamble and Chapters 1–28').replace('a Preamble and twenty chapters','a Preamble and twenty-eight chapters')
def row(old_file_marker,newrow_first):
    global t
    L=t.split('\n')
    for i,l in enumerate(L):
        if l.startswith('| ') and old_file_marker in l.split(' | ')[0]:
            rest=l.split(' | ',1)[1]; L[i]='| '+newrow_first+' | '+rest; t='\n'.join(L); return
    print('  README row missing',old_file_marker)
def lk(n,label=None):
    f=[x for x in os.listdir('.') if x.startswith(f'core_{n:02d}.000_')][0]; return f"[{label or n}]({f})"
row('core_01.000','**Chapter 1**: '+' · '.join(f"[Part {c}](core_01.0{k}0_{n}.md)" for k,(c,n) in enumerate(zip('ABCDEF',['values_principles','values_principles_continuity_aim','interaction_interpretation','constitutional_interpretation','stewardship_capacity_principles','governance_incentive_application']))))
row('core_02.000','**Chapters 2–4**: '+' · '.join(lk(n) for n in (2,3,4)))
row('core_09.000','**Chapters 9–11**: '+' · '.join(lk(n) for n in (9,10,11))+' · [worked illustrations, CS-9.320](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md)')
row('core_12.000','**Chapters 12–14**: '+' · '.join(lk(n) for n in (12,13,14)))
row('core_15.000','**Chapter 15**: [Standing records]'+re.search(r'\((core_15[^)]*)\)',t).group(0))
row('core_16.000','**Chapter 16**: [Standing measurement]'+re.search(r'\((core_16[^)]*)\)',t).group(0))
row('core_17.000','**Chapters 17–20**: '+' · '.join(lk(n) for n in (17,18,19,20)))
row('core_21.000','**Chapters 21–22**: '+' · '.join(lk(n) for n in (21,22)))
for n,lab in ((23,'Forums'),(24,'Governance'),(25,'Non-regression'),(26,'Supremacy and other laws'),(27,'Amendment and adoption'),(28,'Incorporation')):
    f=[x for x in os.listdir('.') if x.startswith(f'core_{n:02d}.000_')][0]
    row(f'core_{n}.000',f'**Chapter {n}**: [{lab}]({f})')
t=re.sub(r'Worked examples for Chapters? [^\]]*\]\(corpus_joint_structure/cjs_15','Worked examples for Chapters 15–22](corpus_joint_structure/cjs_15',t)
open('README.md','w',encoding='utf-8').write(t); print('  edited README.md')
# --- TODO.md chapter map
L=open('TODO.md',encoding='utf-8').read().split('\n')
i=next(k for k,l in enumerate(L) if l.startswith('## Current Chapter Map')); j=i+1
while j<len(L) and (L[j].strip()=='' or L[j].startswith('- **')): j+=1
core=sorted(f for f in os.listdir('.') if re.match(r'core_\d\d\.\d{3}_',f))
bych={}
for f in core: bych.setdefault(int(f[5:7]),[]).append(f)
new=['']
for c in range(0,29):
    fs=bych.get(c,[]); 
    if not fs: continue
    lab='Preamble' if c==0 else f'Ch {c}'
    new.append(f"- **{lab}:** "+', '.join(f"[{f}]({f})" for f in fs))
new.append('')
L[i+1:j]=new; open('TODO.md','w',encoding='utf-8').write('\n'.join(L)); print('  edited TODO.md chapter map')
# --- steward_box_review.md: abbreviations
t=open('steward_box_review.md',encoding='utf-8').read()
t=t.replace('Ch9 Part A §3 and Part B §5–§6.2','Ch9 §3 and Ch10 §2').replace('Ch9 Part A §3','Ch9 §3').replace('Ch9 Part A and Ch6 Part B','Ch9 and Ch6 Part B').replace('Note: Chapters Nine and Ten do not mention','Note: Chapters Nine to Eleven do not mention')
open('steward_box_review.md','w',encoding='utf-8').write(t); print('  edited steward_box_review.md')
# --- FINDINGS label
sub('evaluation/external_audit_2026-08/FINDINGS.md','[Chapter Eighteen §2.4]','[Chapter Nineteen §3.4.3]')

# --- more tool constants and fixtures
import glob
sub('tools/front_door_audit.py','words = "|".join(NUMBER_WORDS)','words = "|".join(sorted(NUMBER_WORDS, key=len, reverse=True))')
sub('tools/test_adopted_implementation_filename_audit.py','self.assertEqual(item.number, "20110")','self.assertEqual(item.number, "28110")')
sub('tools/test_owner_line_audit.py','body = "Chapter Nine is the constitutional owner of **X**.','body = "Chapter One is the constitutional owner of **X**.')
sub('tools/test_owner_line_audit.py','name = "core_09.000_system_alignment_certification_evaluation.md"\n        self.assertTrue(any("name \'Part A\'"','name = "core_01.000_values_principles.md"\n        self.assertTrue(any("name \'Part A\'"')
sub('tools/test_owner_line_audit.py','ok = "Chapter Nine, **Part A**, is the constitutional owner','ok = "Chapter One, **Part A**, is the constitutional owner')
sub('tools/test_owner_line_audit.py','body = "Chapter Nine, Part B, is the constitutional owner of these parts:','body = "Chapter Ten is the constitutional owner of these parts:')
for f in glob.glob('corpus_systems/cs_09.315_*.md'):
    sub(f,'**Chapter Nine** (Parts A, B, and C)','**Chapters Nine to Eleven**')
sub('tools/section_label_anchor_audit.py','''            if rel.startswith(("implementation/", "evaluation/")) and (
                rel not in front_door
            ):
                continue''','''            if rel == "doc_architecture.md" or (
                rel.startswith(("implementation/", "evaluation/")) and rel not in front_door
            ):
                continue  # dated move log and support files keep the numbering of their day''')
sub('tools/ch5_cluster_order_audit.py','"Chapter Sixteen §4.3 Decision-Resolution Requirements for Binding Stakeholder Choice"','"Chapter Twenty-Four §5.3 Decision-Resolution Requirements for Binding Stakeholder Choice"')
