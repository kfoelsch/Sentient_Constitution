#### 3.3 ข้อจำกัดด้านความสอดคล้องตามเวลา

การรับรองต้องไม่ถือว่าสิ่งต่อไปนี้เพียงพอ หากยังไม่ได้จัดการการละเมิดที่คาดการณ์ได้ในระยะกลางหรือระยะยาว:

- ตัวชี้วัดระยะใกล้;
- การปฏิบัติตามข้อกำหนดเฉพาะที่; หรือ
- ประสิทธิภาพในกรอบเวลาสั้น

การไล่ตามผลลัพธ์ระยะสั้นเป็นสิ่งที่ยอมรับไม่ได้ หากคาดหมายได้อย่างสมเหตุสมผลว่าอาจทำให้สิ่งต่อไปนี้เสื่อมถอยในภายหน้า แม้ความเสียหายจะค่อย ๆ สะสม ปรากฏขึ้นล่าช้า หรือแพร่กระจายข้ามระบบต่าง ๆ:

- **ความปลอดภัย**;
- **ความจริง**; หรือ
- **ความเป็นอยู่ที่ดี**

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 การประเมินประเภทและการจัดการข้อมูล

<details>
<summary><strong><span style="color: #2563eb;">ร่องรอย</span></strong></summary>

- ต้นทาง:
  - [§3](#3-whole-system-certification-evaluation) (*ปัจจัยการประเมินทั้งระบบ*);
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*ตัวอย่างการประยุกต์ใช้ทั้งระบบแยกตามชั้นระบบ*);
  - [ส่วน C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*เนื้อหาของบันทึก*);
  - [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ครอบครัวการวัดการกำกับดูแล (*ความจริงและความครบถ้วนทางญาณวิทยาในฐานะการวัดทางรัฐธรรมนูญ*);
  - [ข้อ XV: ความครบถ้วนของพื้นที่สารสนเทศ](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [ข้อ XVI: การตรวจสอบ ความโปร่งใส และการยืนยันอย่างเป็นอิสระ](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [ข้อ VII: การเป็นเจ้าของตนเอง](core_06.005_rights_part_b.md#article-vii-self-ownership)
- ปลายทาง:
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*ตัวอย่างการประยุกต์ใช้การจัดการข้อมูลแยกตามชั้นระบบ*);
  - [§5.1](#51-ecological-footprint-evaluation) และ
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class) (*ตัวอย่างการประยุกต์ใช้การประเมินรอยเท้าทางนิเวศแยกตามชั้นระบบ*);
  - [ส่วน C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*ความครบถ้วนของบันทึก*);
  - [ส่วน C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*ประตูตรวจสอบข้อมูลนำเข้า*);
  - [ส่วน B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*การจัดชั้นใหม่และการจัดการความไม่สอดคล้อง*)
- อ่านประกอบกับ:
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*ประเภทและการจัดการสารสนเทศ*) และ [CS-6.310 — การจัดชั้นข้อมูล](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (รวมถึง **
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*การจัดชั้นใหม่และธรรมาภิบาลวงจรชีวิต*) และ **
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*ธรรมาภิบาลบันทึกประเภทข้อมูลระบบ*));
  - [บันทึกประเภทข้อมูลระบบ](core_05.040_band_continuity.md#system-data-types-record);
  - [การเปิดเผยข้อมูลพื้นฐานด้านการกำกับดูแลสาธารณะ](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - **CJS-5.130 §18** (*เงื่อนไขการเก็บรักษาข้อมูลและความครบถ้วนของวงจรชีวิต*),
  - **CJS-5.130 §21** (*เงื่อนไขความทนทานต่อปฏิปักษ์และการต้านทานการใช้ในทางที่ผิด*), และ
  - **CJS-5.130 §17** (*เงื่อนไขการทำงานร่วมกัน การเคลื่อนย้ายได้ และความครบถ้วนของสิทธิในการออก*) เมื่อมีสาระเกี่ยวข้อง;
  - [§4.1 การเรียกใช้ร่วมกันด้านความเป็นส่วนตัว (ข้อมูล)](#41-privacy-informational-joint-invocation) เมื่อมีจุดที่เกี่ยวกับความเป็นส่วนตัว
- หัวข้อย่อย:
  - [§3.4.1](#341-type-o-baseline-disclosure) (*การเปิดเผยข้อมูลพื้นฐานประเภท O*);
  - [§3.4.2](#342-privacy-discipline) (*วินัยด้านความเป็นส่วนตัว*);
  - [§3.4.3](#343-protective-storage-and-key-custody) (*การจัดเก็บเพื่อคุ้มครองและการดูแลกุญแจ*);
  - [§3.4.4](#344-scheduled-data-type-re-evaluation) (*การประเมินประเภทข้อมูลซ้ำตามกำหนดเวลา*);
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*การยืนยันโครงสร้างพื้นฐานตามชั้นระบบ*);
  - [§3.4.6](#346-infrastructure-robustness-for-data) (*ความทนทานของโครงสร้างพื้นฐานสำหรับข้อมูล*);
  - [§3.4.7](#347-defects-and-misalignment) (*ข้อบกพร่องและการไม่สอดคล้องกัน*);
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*ตัวอย่างการประยุกต์ใช้การจัดการข้อมูลแยกตามชั้นระบบ*)

</details>

<br>

*พูดแบบตรง ๆ: การรับรองยังต้องพิจารณาด้วยว่าระบบแตะต้องข้อมูลประเภทใด และจัดการข้อมูลเหล่านั้นอย่างเหมาะสมหรือไม่ — รวมถึงประเภทข้อมูลยังถูกต้องในการทบทวนรอบปัจจุบันหรือไม่ และโครงสร้างพื้นฐานที่รองรับแข็งแกร่งพอสำหรับข้อมูลประเภทนั้นและชั้นระบบนั้นหรือไม่ กฎเกี่ยวกับประเภทข้อมูลและบันทึกประเภทข้อมูลระบบอยู่ในคลังระบบ ส่วนการรับรองตรวจสอบว่ามีการใช้กฎจริงและบันทึกนั้นตรงไปตรงมาหรือไม่*

การรับรองความสอดคล้องของระบบต้องประเมิน **ประเภทและการจัดการข้อมูล** เป็นส่วนหนึ่งของบันทึกการรับรองระบบทุกรายการที่มีผลกระทบเป็นสาระสำคัญ ส่วนนี้ระบุสิ่งที่การรับรองต้องตรวจสอบ อนุกรมวิธานประเภทข้อมูลและกลไกการจัดการอยู่ใน **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*ประเภทและการจัดการสารสนเทศ*) และ [CS-6.310 — การจัดชั้นข้อมูล](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** พร้อมกับ:

- นิยามประเภทสารสนเทศที่เป็นหลักเกณฑ์มาตรฐาน;
- กฎการจัดการและข้อกำหนดการแยกข้อมูล;
- รายละเอียดวงจรชีวิต; และ
- [บันทึกประเภทข้อมูลระบบ](core_05.040_band_continuity.md#system-data-types-record) ที่คงทนถาวร

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องพิจารณาว่าระบบ:

- ระบุประเภทข้อมูลที่อยู่ในขอบเขตอย่างเป็นสาระสำคัญ; และ
- จัดการข้อมูลเหล่านั้นตามการจัดชั้นที่ **เข้มงวดที่สุดที่ใช้บังคับ** รวมถึงระหว่างการแปลง การรวม การมอบหมาย การจัดเก็บ การเก็บรักษา และการเชื่อมโยงข้ามโดเมน

การประเมินต้องสะท้อนผลในทางปฏิบัติ ไม่ใช่พิจารณาเพียงป้ายกำกับ รูปแบบ หรือขั้นตอนในสายงาน

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 การเปิดเผยข้อมูลพื้นฐานประเภท O

เมื่อใช้ **[พื้นฐานประเภท O ตาม CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)** การรับรองต้องตรวจสอบด้วยว่า [การเปิดเผยข้อมูลพื้นฐานด้านการกำกับดูแลสาธารณะ](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) (**ประเภท O**) ที่เผยแพร่ครอบคลุม **ขอบเขตที่ได้รับการรับรอง** ซึ่งกำหนดจาก:

- [กฎบัตรของระบบ](core_05.040_band_continuity.md#system-charter) ที่ใช้กำกับ;
- ชั้นระบบที่กำหนด; และ
- [ขอบเขตของระบบ](core_05.040_band_continuity.md#system-boundaries) ที่สังเกตได้

ความครอบคลุมนั้นต้องรวมข้อค้นพบด้านธรรมาภิบาล แรงจูงใจ และความสามารถในการโต้แย้ง รวมทั้งบทบาทที่ได้รับมอบหมายตาม [§3.1 วินัยด้านธรรมาภิบาล แรงจูงใจ และความสามารถในการโต้แย้ง](#31-governance-incentive-and-contestability-discipline)

สำหรับระบบทุกชั้น รวมถึงชั้น L และชั้น P การรับรองต้องตรวจสอบด้วยว่ามีการเผยแพร่บันทึกการรับรองระบบเป็นข้อมูลการรับรอง **ประเภท O** ตาม [CS-6.310 ส่วน B §9.3 ประเภท O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data) การเผยแพร่ไม่จำเป็นต้องจัดทำการเปิดเผยข้อมูลพื้นฐานด้านการกำกับดูแลสาธารณะฉบับเต็มสำหรับระบบนอกชั้น A, B และ C

การเปิดเผยความเสี่ยงที่ประเมินแล้วอาจนับเป็นส่วนหนึ่งของพื้นฐานนี้ได้ด้วย เมื่อมีความเสี่ยงเชิงระบบ สิทธิพื้นฐานของสาธารณชนนี้กว้างกว่าการรับรอง และไม่ได้กำหนดให้จัดทำบันทึกแยกต่างหากควบคู่กับ [บันทึกการจัดชั้นระบบ](core_05.040_band_continuity.md#system-classification-record) หรือ [บันทึกประเภทข้อมูลระบบ](core_05.040_band_continuity.md#system-data-types-record)

การระงับการเปิดเผยแต่ละกรณีที่มีเหตุผลรองรับต้องมีข้อมูลทดแทนสาธารณะที่เข้มแข็งที่สุดเท่าที่ทำได้อย่างสมเหตุสมผล ([§3.4.5 การยืนยันโครงสร้างพื้นฐานตามชั้นระบบ](#345-system-class-scaled-infrastructure-assurance) ให้ตัวอย่าง) บทที่ห้าเป็นผู้กำหนดความหมายของคำนี้ ส่วน CS-6.305 (*ประเภทและการจัดการสารสนเทศ*) และ CS-6.310 (*การจัดชั้นข้อมูล*) เป็นผู้กำหนดเนื้อหาพื้นฐานและกลไกการเผยแพร่

<a id="342-privacy-discipline"></a>
