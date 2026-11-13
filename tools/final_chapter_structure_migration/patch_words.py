import re,sys
EXTRA=['Twenty-One','Twenty-Two','Twenty-Three','Twenty-Four','Twenty-Five','Twenty-Six','Twenty-Seven','Twenty-Eight']
n=0
for p in ['chapter_number_audit','heading_echo_topic_audit','part_cite_chapter_audit','section_cite_name_audit','section_label_anchor_audit','trace_widget_numbering']:
    q=f'tools/{p}.py'; t=open(q).read(); o=t
    t=t.replace('Nineteen|Twenty|','Nineteen|'+'|'.join(EXTRA)+'|Twenty|')
    if p=='part_cite_chapter_audit': t=t.replace('"Twenty",','"Twenty", '+', '.join(f'"{w}"' for w in EXTRA)+',',1)
    if t!=o: open(q,'w').write(t); n+=1
q='tools/owner_line_audit.py'; t=open(q).read(); o=t
t=t.replace('20: "Twenty",','20: "Twenty", '+', '.join(f'{21+i}: "{w}"' for i,w in enumerate(EXTRA))+',',1)
if t!=o: open(q,'w').write(t); n+=1
q='tools/front_door_audit.py'; t=open(q).read(); o=t
t=t.replace('"twenty": 20,','"twenty": 20, '+', '.join(f'"{w.lower()}": {21+i}' for i,w in enumerate(EXTRA))+',',1)
if t!=o: open(q,'w').write(t); n+=1
q='tools/lift_adopted_implementation_anatomy.py'; t=open(q).read(); o=t
t=t.replace('[Chapter Twenty](../core_28.000','[Chapter Twenty-Eight](../core_28.000')
if t!=o: open(q,'w').write(t); n+=1
print('word patches',n)
