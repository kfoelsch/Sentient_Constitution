<!-- AI-assisted translation draft; unreviewed. Source lines 443–513; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

### 7. ผลการรับรอง

<details>
<summary><strong><span style="color: #2563eb;">ร่องรอย</span></strong></summary>

- ต้นทาง:
  - [§6](#6-forum-process) (*กระบวนการของเวทีและการโต้แย้งที่น่าเชื่อถือ*);
  - [ส่วน A §2 การประเมินประเภทระบบ](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) ถึง
  - [§5 การประเมินพื้นสิทธิและโดเมน](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*การจัดประเภทผิด ความไม่สอดคล้อง และข้อบกพร่องที่พบในการประเมิน*);
  - [เป้าหมายตามรัฐธรรมนูญสองประการ](core_00.000_preamble.md#two-constitutional-aims);
  - [บทที่สาม §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) และ
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*ความครบถ้วนของบทนิยามและการหลบเลี่ยง*);
  - [บทที่สาม §2.1 รูปแบบการหลบเลี่ยงทั่วไป](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*การหลบเลี่ยงขอบเขตและแนวแบ่งเขต*);
  - [กฎบัตรระบบ](core_05.040_band_continuity.md#system-charter) (*ความไม่ตรงกันระหว่างกฎบัตรระบบกับพฤติกรรม และการทบทวนที่เลยกำหนด*).
- ปลายทาง:
  - [ส่วน C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*ระบุผลลัพธ์ไว้ในบันทึก*);
  - [ส่วน C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*เปิดช่องทางโต้แย้งพร้อมผลลัพธ์*);
  - [ส่วน C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*การรับรองซ้ำและการเปิดใหม่*);
  - [ส่วน C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*ประตูข้อมูลเข้าที่ผ่านการตรวจยืนยัน เมื่อข้อเท็จจริงสนับสนุนข้อค้นพบที่เป็นผลเสีย*);
  - [บทที่สิบสาม](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*การกำกับดูแลของเวที*);
  - [บทที่สิบ](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- อ่านร่วมกับ: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*การจัดประเภทใหม่และการกำกับดูแลวงจรชีวิต*) สำหรับการประเมินชนิดข้อมูลซ้ำตามกำหนด และ **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*ข้อกำหนดการจัดประเภทใหม่*) สำหรับตัวกระตุ้นการประเมินประเภทระบบซ้ำและการตรวจยืนยัน SAC.
- หัวข้อย่อย:
  - [§7.1](#71-go-live-gate) (*ประตูก่อนเริ่มใช้งานจริง* ซึ่งประกอบด้วย
  - [§7.1.1 ระบบที่ดำเนินงานอยู่แล้ว](#711-systems-already-operating) และ
  - [§7.1.2 โครงการนำร่อง](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*ข้อบกพร่องของการรับรองและการแก้ไข*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*ความพร้อมในการแก้ไข: ความเต็มใจและความสามารถในการแก้ไข* ซึ่งประกอบด้วย
  - [§7.3.1 ความเต็มใจ](#731-willingness),
  - [§7.3.2 ความสามารถ](#732-capacity),
  - [§7.3.3 ขั้นตอนพิสูจน์](#733-proof-step),
  - [§7.3.4 ข้อค้นพบ](#734-findings), และ
  - [§7.3.5 เงื่อนไขเดียวกันสำหรับผู้ดำเนินระบบทุกราย](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*การปฏิเสธและการเพิกถอน* ซึ่งประกอบด้วย
  - [§7.4.1 การปฏิเสธและการเพิกถอนคืออะไร](#741-what-denial-and-revocation-are),
  - [§7.4.2 เมื่อใดต้องปฏิเสธหรือเพิกถอน](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 คุ้มครองก่อน](#743-protection-first),
  - [§7.4.4 กระบวนการ](#744-process),
  - [§7.4.5 ผล](#745-effect), และ
  - [§7.4.6 ไม่ใช่การห้ามถาวร](#746-not-a-permanent-bar)).

</details>

<br>

*กล่าวอย่างง่าย: การทบทวนการรับรองทุกครั้งสิ้นสุดด้วยผลลัพธ์ที่ระบุชัด โดยมีหลักฐานและข้อกังวลที่ยกขึ้นระหว่างกระบวนการรองรับ ไม่มีสิ่งใดเริ่มใช้งานจริงจนกว่าจะได้รับการรับรอง ผู้มีสภาวะรับรู้ที่ได้รับผลกระทบมีโอกาสจริงในการโต้แย้งผลลัพธ์ที่เผยแพร่ และมีการตรวจสอบมาตรการคุ้มครองที่ต้องทำก่อนเริ่มใช้งานจริงแล้ว*

ส่วนนี้คือ **ระยะ IV ตัดสินใจ** ซึ่งตามหลัง [§6 กระบวนการของเวที](#6-forum-process) (**ระยะ III ทบทวน**) โดยครอบคลุมผลลัพธ์ที่เวทีตัดสิน [§7.1 ประตูใช้งานจริง](#71-go-live-gate) ระบุประตูดังกล่าว ส่วน [§7.2 ข้อบกพร่องและการแก้ไขการรับรอง](#72-certification-defects-and-correction) ระบุสิ่งที่เกิดขึ้นเมื่อพบข้อบกพร่อง

ตาม [ส่วน C §8.1 เนื้อหาบันทึกขั้นต่ำ](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) ต้องระบุคำตัดสินการรับรองและข้อกังวลที่ยกขึ้นระหว่างการได้คำตัดสินไว้ในบันทึก ผลลัพธ์อย่างหนึ่งอย่างใดคือ:

- การรับรองชั่วคราว;
- การรับรองเต็มรูปแบบ;
- การรับรองแบบมีเงื่อนไข;
- การรับรองที่เลื่อนออกไป;
- ไม่ได้รับการรับรอง;
- การถอน;
- การหมดอายุ; หรือ
- การปลดเงื่อนไข

ระบบที่ไม่มีทั้งการรับรองชั่วคราวและเต็มรูปแบบคือ **ไม่ได้รับการรับรอง** ซึ่งเป็นกรณีเมื่อการรับรอง:

- ถูกเลื่อน;
- ถูกปฏิเสธ;
- ถูกถอน; หรือ
- หมดอายุ

การรับรองชั่วคราวและเต็มรูปแบบคือ **สถานะ** สองแบบของการรับรอง [ส่วน C §9.2 การรับรองชั่วคราวและเต็มรูปแบบ](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) อธิบายว่าระบบจะได้รับ รักษา และสูญเสียแต่ละสถานะอย่างไร เงื่อนไขของการรับรองแบบมีเงื่อนไขอาจผูกกับสถานะใดสถานะหนึ่งก็ได้

<a id="71-go-live-gate"></a>
