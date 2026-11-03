<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (th)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*กล่าวอย่างง่ายคือ การรับรองต้องพิจารณาด้วยว่าระบบแตะข้อมูลประเภทใดและจัดการข้อมูลอย่างเหมาะสมหรือไม่ รวมถึงประเภทข้อมูลยังถูกต้องในรอบการทบทวนปัจจุบันหรือไม่ และโครงสร้างพื้นฐานเบื้องหลังแข็งแกร่งพอสำหรับข้อมูลนั้นในชั้นระบบดังกล่าวหรือไม่ กฎเรื่องประเภทข้อมูลและ[บันทึกประเภทข้อมูลระบบ](core_05.040_band_continuity.md#system-data-types-record)อยู่ในคลังระบบ การรับรองตรวจสอบว่ามีการใช้กฎจริงและบันทึกมีความถูกต้องซื่อตรง*

การรับรองความสอดคล้องของระบบต้องประเมิน **ประเภทข้อมูลและการจัดการข้อมูล** เป็นส่วนหนึ่งของบันทึกการรับรองทุกฉบับที่มีผลกระทบอย่างเป็นสาระสำคัญ ส่วนนี้ระบุสิ่งที่การรับรองต้องตรวจสอบ อนุกรมวิธานประเภทข้อมูลและกลไกการจัดการอยู่ใน **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*ประเภทข้อมูลและการจัดการข้อมูล*) และ [CS-6.310 — การจัดประเภทข้อมูล](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** พร้อมกับ:

- คำนิยามมาตรฐานของประเภทข้อมูล;
- กฎการจัดการและข้อกำหนดการแยกข้อมูล;
- รายละเอียดวงจรชีวิต; และ
- [บันทึกประเภทข้อมูลระบบ](core_05.040_band_continuity.md#system-data-types-record)ที่คงทน

**ข้อกำหนดการประเมิน** กระบวนการรับรองต้องกำหนดว่าระบบ:

- ระบุประเภทข้อมูลที่อยู่ในขอบเขตอย่างเป็นสาระสำคัญหรือไม่; และ
- จัดการข้อมูลตามการจัดประเภทที่ **เข้มงวดที่สุดเท่าที่ใช้บังคับ** หรือไม่ รวมถึงระหว่างการแปลง การรวม การมอบหมาย การจัดเก็บ การเก็บรักษา และการเชื่อมโยงข้ามโดเมน

การประเมินต้องสะท้อนผลเชิงหน้าที่ ไม่ใช่เพียงป้ายกำกับ รูปแบบ หรือขั้นตอนในไปป์ไลน์
