<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (th)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

ส่วนนี้ระบุสิ่งที่การรับรองต้องตรวจสอบ:

- **ข้อกำหนดการประเมิน:**
  - ชั้นระบบที่กำหนดสะท้อน **ผลกระทบ** **การพึ่งพา** และ **ความเสี่ยง** ที่สังเกตได้และคาดการณ์ได้อย่างสมเหตุสมผลตาม CS-9.305 (*กลไกการจัดชั้นระบบ*) และ CS-9.310 (*การจัดประเภทผลกระทบของระบบ*) หรือไม่ รวมถึง:
    - ผลรวม;
    - ผลจากปฏิสัมพันธ์;
    - ผลจากฝ่ายปฏิปักษ์;
    - ผลจากเกณฑ์ขีดจำกัด;
  - การจัดประเภทกำหนดจากพฤติกรรมและผลกระทบจริงของระบบ ไม่ใช่จาก:
    - เจตนาที่ประกาศไว้;
    - ขอบเขตตามชื่อ;
    - ข้อความใน [กฎบัตรระบบ](core_05.040_band_continuity.md#system-charter) เพียงอย่างเดียว; หรือ
    - คำอธิบายตนเองเพียงอย่างเดียว;
  - มีการตรวจชั้นระบบอีกครั้งตาม **[ข้อกำหนดการจัดประเภทใหม่ CS-9.305 §3.5](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** ทุกครั้งที่การเปลี่ยนแปลงสำคัญทำให้ต้องดำเนินการ; และ
  - [บันทึกการจัดประเภทระบบ](core_05.040_band_continuity.md#system-classification-record) แสดง **ชั้นระบบสูงสุดที่ใช้บังคับ** ภายใต้เงื่อนไขปัจจุบัน
- **การประกันและการทดสอบรีเกรสชัน:**
  - การประกันที่ปรับตามชั้นระบบ ความทนทานของโครงสร้างพื้นฐาน และความครอบคลุมของการทดสอบรีเกรสชันสอดคล้องกับชั้นระบบที่กำหนด ตาม:
    - CS-9.305 (*กลไกการจัดชั้นระบบ*) และ CS-9.310 (*การจัดประเภทผลกระทบของระบบ*); และ
    - CS-6.345 (*วงจรชีวิตระบบ*) เมื่ออ่านร่วมกับคำศัพท์ปฏิบัติการร่วมต่อไปนี้ในกรณีที่เกี่ยวข้องอย่างมีนัยสำคัญ:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*ความต่อเนื่อง: คำศัพท์ว่าด้วยการเสื่อมถอยอย่างค่อยเป็นค่อยไปและความสมบูรณ์ของรูปแบบความล้มเหลว*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*ความต่อเนื่อง: คำศัพท์ว่าด้วยการย้อนกลับได้และการควบคุมจำกัดผลกระทบ*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*ความต่อเนื่อง: คำศัพท์ว่าด้วยความทนทานต่อฝ่ายปฏิปักษ์และการต้านทานการใช้ในทางที่ผิด*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*การบูรณาการ: คำศัพท์ว่าด้วยการรักษาความลับแบบจำกัดและการสืบสวนที่ได้รับการคุ้มครอง*) เมื่อชั้นหรือหน้าที่ของระบบทำให้เกี่ยวข้องอย่างมีนัยสำคัญ; และ
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*การบูรณาการ: คำศัพท์ว่าด้วยความสมบูรณ์ของการแทรกแซงและการสั่งทับ*) เมื่อชั้นหรือหน้าที่ของระบบทำให้เกี่ยวข้องอย่างมีนัยสำคัญ; และ
  - มีการทดสอบรีเกรสชันในการรับรองซ้ำทุกครั้งตามที่ CS-6.345 (*วงจรชีวิตระบบ*) กำหนด และบันทึกผลไว้ตาม [§8.1 เนื้อหาขั้นต่ำของบันทึก](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).
