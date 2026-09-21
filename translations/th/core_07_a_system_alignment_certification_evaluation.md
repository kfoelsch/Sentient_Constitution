<a id="chapter-seven-system-alignment-certification"></a>
<a id="chapter-seven-system-alignment-certification-and-recognition"></a>
<a id="chapter-seven-part-a-certification-evaluation"></a>
<a id="chapter-seven-part-a-system-alignment-certification--evaluation"></a>
# บทที่เจ็ด ส่วน ก: การรับรองความสอดคล้องของระบบ — การประเมิน

<details>
<summary><strong><span style="color: #2563eb;">ตำแหน่งในคลังข้อความ (ไม่ใช่บทบัญญัติที่ใช้บังคับ): โครงสร้างไฟล์และกฎการอ่าน</span></strong></summary>

> เนื้อหาต่อไปนี้เป็น **แนวทางสำหรับผู้อ่านเท่านั้น** ไม่เพิ่ม ไม่ลด และไม่ทำให้ภาระผูกพันที่ใช้บังคับแคบลงในไฟล์นี้หรือในบทอื่น
>
> ไฟล์นี้เป็น **โครงการนำร่องด้านภาษาสำหรับผู้อ่าน** ของ [บทที่เจ็ด ส่วน ก ภาษาอังกฤษ](../../core_08_a_system_alignment_certification_evaluation.md) **ไม่ใช่** ส่วนที่มีผลผูกพันของรัฐธรรมนูญของผู้มีความรู้สึก **ไม่ใช่** รัฐธรรมนูญฉบับที่สอง **ไม่ใช่** ฉบับจัดส่ง **ตรึงไว้** กับ `SC-Corpus-2026.08.09` หากคำแปลนี้กับต้นฉบับภาษาอังกฤษดูเหมือนไม่ตรงกัน ให้ไฟล์ที่มีหมายเลข [`core_07_a_system_alignment_certification_evaluation.md`](../../core_08_a_system_alignment_certification_evaluation.md) เป็นฝ่ายชนะ ลำดับการอ่านและข้อมูลฉบับคงไว้ใน [README.md](../../README.md) วิธีทำและอภิธานศัพท์: [translations/th/README.md](README.md)
>
> มี **บทที่เจ็ด ส่วน ก** — ข้อกำหนด **การประเมิน** การรับรอง (ชั้นระบบ ปัจจัยทั้งระบบ และตะขอประเมินโดเมน) **ส่วน ข** — บันทึกการรับรอง กระบวนการเวที สะพานร่องรอย และการเปิดใหม่ — อยู่ใน [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md)
>
> - **เจ้าของทางรัฐธรรมนูญ (ร่วมกับส่วน ข):** **การรับรองความสอดคล้องของระบบและบันทึกที่เกี่ยวข้อง** ที่เวทีกำกับ — โดเมนการประเมิน (ส่วน ก); หน้าที่บันทึกการรับรอง ผลการรับรู้ จังหวะการรับรองซ้ำ ลำดับการกำกับ สายความสามารถในการโต้แย้ง และสะพานข้อมูลเข้าที่ตรวจสอบแล้วสู่บทที่แปด (ส่วน ข) ภายใต้ขา **การกำกับดูแล** ของจตุรภาค SAC เป็นกระบวนการตรวจที่ใหญ่และมีส่วนได้เสียสูงเป็นพิเศษในบรรดาอื่น; พื้นการตรวจคงอยู่ที่ **มาตรา XV** และ [ความสามารถในการตรวจ](core_05_band_oversight.md#auditability) ของบทที่ห้า
> - **เจ้าของฐานการตรวจสอบ:** [บทที่สี่ — ภาระการพิสูจน์ ความสามารถในการตามรอย และการตรวจสอบ](core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (ภายในบทที่สองถึงสี่) เป็นเจ้าของการจัดสรรภาระ หลักฐานการปฏิบัติตาม ความสามารถในการตามรอยบทนิยาม ความสังเกตได้ และการตรวจสอบที่ถูกจำกัดด้วยความมั่นคง บทที่เจ็ด **นำ** วินัยนั้น **ไปใช้** กับบันทึกการรับรองความสอดคล้องของระบบ; **ไม่** กล่าวซ้ำหมวด **1** ถึง **5** ของบทที่สี่
> - **บ้านของการตรวจ (ไม่ย้ายมาที่นี่):** **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*) **Def.O1** (*ความโปร่งใส ความสามารถในการตรวจ และการตรวจสอบ*) และ **CJS-3.3**–**CJS-3.5** เป็นเจ้าของพื้นการตรวจและคำปฏิบัติการ บทที่เจ็ดดำเนินกระบวนการตรวจ SAC ที่ใหญ่เป็นพิเศษซึ่งต้องสนองพื้นเหล่านั้น; ไม่เป็นเจ้าของการตรวจทั้งหมด
> - **เจ้าของการนำไปใช้:** การปฏิบัติชั้นระบบ CS-5 และรายละเอียดกระบวนการเวทีในไฟล์นำไปใช้ที่กำหนด ต้องคงสอดคล้องกับบทที่เจ็ด และอาจเข้มกว่าในที่ที่คลังข้อความมีตรรกะกฎที่เข้มกว่าอยู่แล้ว
> - **กฎต้านการย้าย:** ส่วน กไม่กล่าวซ้ำบทนิยามฉบับหลักของบทที่ห้า วินัยต้านการหลบของบทที่สาม (ดู [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)) การวัดการมีส่วนช่วยหรือร่องรอยของบทที่แปด หรือผลของร่องรอยของบทที่เก้า **[ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)** กล่าวขอบสะพานร่องรอยอย่างชัดเจน
>
> **ต้นทาง:** บทนิยามบทที่ห้า และบันทึก การตรวจสอบ ภาระ และความสามารถในการตามรอยจากบทนิยามไปยังผลของบทที่สองถึงสี่
> **ปลายทาง:** [ส่วน ข](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) (*บันทึก กระบวนการเวที และสะพานร่องรอย*); บันทึกร่องรอยและข้อมูลเข้าที่ตรวจสอบแล้วของบทที่แปด; ผลของร่องรอยของบทที่เก้า; การกำกับของเวทีและเส้นทางการรับรองความสอดคล้องของระบบของบทที่สิบเอ็ด
>
> **ประตูผู้บริหารอย่างรับผิดชอบ (ไม่ใช่บทบัญญัติที่ใช้บังคับ):** คำแถลงก้าวถัดไปที่มีผลผูกพัน: [คำแถลงเชิงปฏิบัติของผู้บริหารอย่างรับผิดชอบ](#operative-steward-statement-sac) ตัวชี้สนับสนุนใน [`implementation/STEWARD_ENTRY_DOORS.md`](../../implementation/STEWARD_ENTRY_DOORS.md) ทำให้แคบลงไม่ได้

>
> **ก่อนหน้า (ภาษานี้):** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)
>
> **ถัดไป (ภาษานี้):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)
> **ส่วนโค้งการอ่าน:** §1 จุดประสงค์และบทบาท → §2 ชั้นระบบ → §3 การประเมินทั้งระบบ → §4–§10 การประเมินโดเมน

</details>

<br>

บทที่เจ็ด **ส่วน ก** เป็นเจ้าของทางรัฐธรรมนูญของ **การประเมินการรับรองความสอดคล้องของระบบ** เนื้อหาบันทึก การกำกับของเวที เส้นทางโต้แย้ง และสะพานร่องรอยอยู่ใน **[ส่วน ข](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)**

<a id="operative-steward-statement-sac"></a>
> **คำแถลงเชิงปฏิบัติของผู้บริหารอย่างรับผิดชอบ.** **เจ้าของ:** บทที่เจ็ด (SAC ที่เวทีกำกับ) เลนส์ชั้นหลักการ: บทที่หนึ่ง §14 SAC เป็นกระบวนการตรวจที่ใหญ่เป็นพิเศษภายใต้มาตรา XV / ความสามารถในการตรวจ — ไม่ใช่การตรวจเดียว **การกระทำที่ห้าม:** อย่าถือการทดสอบหน่วย รายการตรวจความเป็นส่วนตัว หรือป้ายสอดคล้องเฉพาะที่เป็นการรับรอง อย่าข้ามหน้าต่างโต้แย้ง อย่าประดิษฐ์บ้านการตรวจที่ห้า อย่าถือตราการรับรองหรือคะแนน LEQU เป็นสถานะความเป็นผู้มีความรู้สึก **นาฬิกา:** เปิดหรือคืนเส้นทางบทที่เจ็ดที่โต้แย้งได้ รวมหน้าต่างโต้แย้งของฝ่ายที่ได้รับผลกระทบ ก่อนข้อกล่าวอ้างว่าสอดคล้อง

<a id="1-purpose-and-role"></a>
### 1. จุดประสงค์และบทบาท

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [คำปรารภ — ทะเบียนเจ้าของเชิงบวก](core_00_preamble.md#4-principles-definitions-and-rights) และ [กองอำนาจและลำดับชั้นภายใน](core_05_band_integrative.md#authority-stack); [จตุรภาคทางรัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad); [สองเป้าประสงค์ทางรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims); [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake); [สัดส่วน](core_05_band_accountability.md#proportionality) และ [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) (บทที่ห้า); ครอบครัวการวัดการมีส่วนร่วม (*เสียง การเข้าถึง และเส้นทางโต้แย้ง*); [บทที่หนึ่ง §9 การบริหารอย่างรับผิดชอบและความเข้าใจแบบกระจาย](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding); [บทที่หนึ่ง §14 ข้อกำหนดการประเมินเชิงระบบ](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement) (*เลนส์ประเมินทั้งระบบที่ชั้นหลักการ — ไม่ใช่มุมเดียว*); บทที่สองถึงสี่; [บทที่ห้า](core_05__definitions_home.md#chapter-five-foundational-definitions) (*บทนิยามฉบับหลัก*); [การรับรองความสอดคล้องของระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) (คำฉบับหลักบทที่ห้า; ตัวย่อที่ไม่ใช่บทบัญญัติที่ใช้บังคับ **SAC**); [บันทึกการรับรองระบบ](core_05_band_continuity.md#system-certification-record-constitutional) (ความหมายบทที่ห้า)
- ปลายทาง: [§2](#2-system-class-evaluation) และ [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*การประเมินชั้นระบบและโปรไฟล์ตัวอย่าง*); [§3.8](#38-illustrative-whole-system-application-by-class) (*ตัวอย่างทั้งระบบที่ทำงานแล้วตามชั้น*); [§4.1](#41-illustrative-data-handling-application-by-class) (*ตัวอย่างการปฏิบัติข้อมูลที่ทำงานแล้วตามชั้น*); [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*ตัวอย่างรอยเท้าทางนิเวศที่ทำงานแล้วตามชั้น*); [§6.1](#61-illustrative-cross-system-support-application-by-class) (*ตัวอย่างการสนับสนุนข้ามระบบที่ทำงานแล้วตามชั้น*); [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*ตัวอย่างการไม่เลือกปฏิบัติที่ทำงานแล้วตามชั้น*); [§8.1](#81-illustrative-accessibility-application-by-class) (*ตัวอย่างการเข้าถึงได้ที่ทำงานแล้วตามชั้น*); [§9.1](#91-illustrative-educational-capability-application-by-class) (*ตัวอย่างขีดความสามารถทางการศึกษาที่ทำงานแล้วตามชั้น*); [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ตัวอย่างความน่าไว้วางใจที่ทำงานแล้วตามชั้น*); [§3](#3-whole-system-certification-evaluation) (*ปัจจัยประเมินการรับรองทั้งระบบ*); [§4](#4-data-types-and-handling-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) (*การประเมินโดเมน*); [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึกการรับรอง*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ข้อกำหนดความครบถ้วนของบันทึก*); [ส่วน ข §13](core_07_b_system_alignment_certification_record_process.md#13-forum-supervision-and-component-roles) (*บทบาทส่วนประกอบของเวที*); [ส่วน ข §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain) (*ลำดับการกำกับและสายความสามารถในการโต้แย้ง*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*สะพานบันทึกร่องรอย*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*การเปิดใหม่และต้านการหลบ*); [บทที่แปด](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) (*บันทึกร่องรอยและประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [บทที่เก้า](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*ผลของร่องรอยและการรวม*); [บทที่สิบเอ็ด](core_11_forum.md#chapter-eleven-forums-and-jurisdiction) (*การกำกับของเวที การรับรอง การรับรู้ความสอดคล้อง และการทบทวน*)
- อ่านคู่กับ: [corpus_systems.md](../../corpus_systems.md) โดยเฉพาะ **CS-3 — การจำแนกและการปฏิบัติของระบบ** **CS-2 — ชนิดข้อมูลและการปฏิบัติ** และ **CS-5**; [corpus_forum.md](../../corpus_forum.md) โดยเฉพาะ **CF-5** (*การปฏิบัติการจัดเส้นทาง การโอน การรับรอง และการปฏิบัติแบบผู้แทน*) และ **CF-7** (*การคุ้มกันความครบถ้วน การปฏิบัติการต้านการยึดครอง และการสนับสนุนต้านการตัดสินตนเอง*); **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*) และ [ความสามารถในการตรวจ](core_05_band_oversight.md#auditability) (*พื้นการตรวจ — SAC เป็นกระบวนการตรวจที่ใหญ่เป็นพิเศษภายใต้การกำกับดูแล ไม่ใช่บ้านการตรวจเดียว*); **CJS-3.3**–**CJS-3.5** (*คำความสามารถในการตรวจ การเข้าถึงการตรวจ และการตรวจสอบอิสระ*)

</details>

<br>

*พูดแบบตรง ๆ: เมื่อระบบสำคัญจริงต่อชีวิตของผู้มีความรู้สึก การรับรองต้อง **ตามสัดส่วน** — เข้มตามผลกระทบ การพึ่งพา และความเสี่ยงจริงของระบบ ไม่ใช่รายการตรวจแบบเดียวกับทุกคนหรือตราประทับยาง และต้อง **มีส่วนร่วม** — ผู้มีความรู้สึกและชุมชนที่ได้รับผลกระทบต้องเห็นสิ่งที่ถูกทบทวน เข้าใจสิ่งที่ถูกตัดสิน และโต้แย้งได้เมื่อมีสิ่งผิด เวทีทบทวนหลักฐาน เขียนลงบันทึกการรับรอง และขอให้ตรวจซ้ำตามจังหวะที่ตรงกับความเสี่ยงของระบบ การรับรองไม่ใช่คะแนนความนิยม บัตรผ่านตลอดกาล หรือทางข้ามการทบทวนสิทธิ เป็นคำแถลงที่มีขอบเวลาและโต้แย้งได้ของสิ่งที่รู้เกี่ยวกับความสอดคล้องของระบบในตอนนี้ ภายใต้ขา **การกำกับดูแล** ของจตุรภาค การกำกับดูแลขอการตรวจ; การรับรองความสอดคล้องของระบบเป็นกระบวนการตรวจที่ใหญ่และมีส่วนได้เสียสูงเป็นพิเศษในบรรดาอื่น — ไม่ใช่บ้านการตรวจเดียว (**มาตรา XV**, [ความสามารถในการตรวจ](core_05_band_oversight.md#auditability))*

<a id="1-purpose-and-role"></a>

**การรับรองความสอดคล้องของระบบ** มีอยู่เพื่อตอบคำถามข้อเดียวสำหรับขอบเขตและจังหวะการทบทวนที่กล่าว: ระบบได้แสดงความสอดคล้องทางรัฐธรรมนูญพอสำหรับการรับรู้ การรับรู้มีเงื่อนไข การยืนยัน การรับรองซ้ำ การพึ่งต่อเนื่อง การติดตั้งใช้งาน หรือการปล่อยจากเงื่อนไขที่เป็นสาระหรือไม่

ในฐานะเครื่องมือกำกับดูแล การรับรองเป็นกระบวนการตรวจที่ใหญ่เป็นพิเศษภายใต้ [ความสามารถในการตรวจ](core_05_band_oversight.md#auditability) และ **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*): เวทีกำกับ หลายโดเมน และแบกการรับรู้ มันไม่ดูดซึมหรือแทนโหมดตรวจพี่น้อง (รวมการตรวจบันทึกการจำแนกระบบภายใต้ **CS-3** การตรวจบันทึกชนิดข้อมูลของระบบภายใต้ **CS-2** การตรวจความซับซ้อนและการบริหารอย่างรับผิดชอบ การตรวจสอบข้อกล่าวอ้าง และเส้นทางการตรวจต่อเนื่อง)

ความลึกของการรับรอง ภาระบันทึก จังหวะการรับรองซ้ำ การทบทวนฝ่ายที่ได้รับผลกระทบ และเส้นทางโต้แย้งต้องปรับตาม [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ภายใต้ [สัดส่วน](core_05_band_accountability.md#proportionality) ระบบผลกระทบสูง การพึ่งสูง และความเสี่ยงสูงขอหลักฐานที่เข้มกว่า บันทึกที่ชัดกว่า และการมีส่วนร่วมที่ใช้ปฏิบัติได้มากกว่า — รวมการเข้าถึงได้ที่เป็นสาระ ข้อมูลเข้าของฝ่ายที่ได้รับผลกระทบ และเส้นทางโต้แย้งที่ปรับตามผู้ที่พึ่งระบบ ชั้นต่ำกว่าและขอบเขตที่มีขอบยังขอการจำแนกที่ซื่อและการประกันตามสัดส่วน; ไม่ได้รับบัตรผ่านจากหน้าที่ที่เป็นสาระในที่ที่มีผลภายนอก

การรับรองทำให้ [สองเป้าประสงค์ทางรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims) ปฏิบัติการผ่าน [จตุรภาคทางรัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad):

- **[ความเจริญงอกงาม](core_00_preamble.md#flourishing)** — การรับรองยืนยันว่าการรับรู้หรือการพึ่งต่อเนื่องจะไม่พ่ายแพ้พื้นสิทธิอย่างเงียบหรือกั้นการมีส่วนร่วมที่เป็นธรรมในชีวิตที่เกี่ยวข้องทางรัฐธรรมนูญ;
- **[ความต่อเนื่อง](core_00_preamble.md#continuity)** — การรับรองยืนยันการส่งมอบที่ทนและไม่ถอยหลัง และการรับรองซ้ำที่ปรับตามชั้น ในที่ที่ระบบร่วมกั้นหรือค้ำการส่งมอบ;
- **การมีส่วนร่วม** — ผู้มีความรู้สึกและชุมชนที่ได้รับผลกระทบเข้าใจ โต้แย้ง และร่วมในเส้นทางทบทวนที่สำคัญต่อตนได้;
- **การกำกับดูแล** — บันทึก หลักฐาน และข้อสมมติมองเห็นและตรวจได้พอสำหรับการตรวจอิสระ; การรับรองเองเป็นกระบวนการตรวจที่ใหญ่เป็นพิเศษภายใต้หน้าที่กำกับนั้น ไม่ใช่ข้อเดียว;
- **ความรับผิดชอบ** — ข้อบกพร่อง การจำแนกผิด และการดำเนินงานที่พ่ายแพ้พื้นถูกจัดเส้นทางไปยังการเยียวยา เงื่อนไข การถอน หรือข้อมูลเข้าร่องรอยในที่ที่ข้อเท็จจริงรองรับ;
- **ความทันเวลา** — นาฬิกาทบทวนและโต้แย้งกันไม่ให้การรับรองเก่าในขณะที่ยังป้องกันหรือย้อนภัยได้

บทนี้ดำเนินกระบวนการรับรองที่เวทีกำกับสำหรับ:

- **ชั้นระบบและจังหวะการรับรองซ้ำ** — มองเข้มแค่ไหนและบ่อยแค่ไหน ([§2](#2-system-class-evaluation));
- **การประเมิน** — การตรวจทั้งระบบและโดเมน ([§3](#3-whole-system-certification-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation));
- **เนื้อหาบันทึกการรับรอง** — สิ่งที่ต้องอยู่บนแฟ้ม ([ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record));
- **การรับรู้และการพึ่งต่อเนื่อง** — ผลใดนับ ([§1](#1-purpose-and-role), [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record));
- **การโต้แย้งและความสามารถในการโต้แย้ง** — การท้าทายเคลื่อนผ่านเวทีอย่างไร ([ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability), [ส่วน ข §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain));
- **ข้อบกพร่องของการรับรอง** — เกิดอะไรเมื่อการรับรองบกพร่อง ([ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) และหมวดประเมินตลอดบท)

โปรไฟล์ตัวอย่าง **Class A** **Class B** และ **Class C** — และชั้นปรับความลึกของการรับรองข้ามบทนี้อย่างไร — อยู่ใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) การเดินดูที่ทำงานแล้วของระบบสามระบบเดียวกันปรากฏใน [§3.8](#38-illustrative-whole-system-application-by-class) (*การประเมินทั้งระบบ*) [§4.1](#41-illustrative-data-handling-application-by-class) (*ชนิดข้อมูลและการปฏิบัติ*) [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*รอยเท้าทางนิเวศ*) [§6.1](#61-illustrative-cross-system-support-application-by-class) (*การสนับสนุนข้ามระบบตามสัดส่วน*) [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*การไม่เลือกปฏิบัติ*) [§8.1](#81-illustrative-accessibility-application-by-class) (*การเข้าถึงได้*) [§9.1](#91-illustrative-educational-capability-application-by-class) (*ขีดความสามารถทางการศึกษา*) และ [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ความน่าไว้วางใจ*)

พื้นสิทธิที่บทนี้ช่วยยืนยันอยู่ใน **§1.1**


<a id="11-rights-floors-this-chapter-helps-verify"></a>
#### 1.1 พื้นสิทธิที่บทนี้ช่วยยืนยัน

เมื่อระบบผลกระทบที่เป็นสาระกั้นหรือหล่อหลอมวิธีที่ผู้มีความรู้สึกมีชีวิต การรับรองตรวจว่าการอนุมัติจะไม่พ่ายแพ้ **พื้นสิทธิ** ของบทที่หกอย่างเงียบ รวม:

- **สิ่งจำเป็นต่อการอยู่รอด** ภายใต้ **มาตรา III-A** (*การอยู่รอด*) — อาหาร น้ำ ที่พัก สภาพแวดล้อมการดำเนิน และปัจจัยฐานะกายที่ไม่พึ่งพาที่คล้าย;
- **การเข้าถึงการศึกษาที่เท่ากัน** ภายใต้ **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*);
- **ขีดความสามารถการศึกษาที่ศูนย์กลางผู้มีความรู้สึก** ภายใต้ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ในที่ที่ระบบจัดอันดับ ประเมิน แนะนำ วาง กั้นด้วยหลักฐานคุณวุฒิ หรือกั้นอย่างเป็นสาระเส้นทางฝึกใหม่และการเรียนรู้ตลอดชีวิต;
- **การไม่เลือกปฏิบัติ** ภายใต้ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ในที่ที่ระบบจำแนก กั้น ตั้งราคา จัดอันดับ หรือจัดสรรภาระและประโยชน์ในหมู่ผู้มีความรู้สึก;
- **การเข้าถึงได้** ภายใต้ **มาตรา V-G** (*การเข้าถึงได้*) ในที่ที่ระบบกั้นการมีส่วนร่วมที่เป็นสาระในโดเมนที่เกี่ยวข้องทางรัฐธรรมนูญ;
- **ความประพฤติของระบบที่พึ่งได้และน่าไว้วางใจ** ภายใต้ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ในที่ที่ระบบหล่อหลอมอย่างเป็นสาระการพึ่งของผู้มีความรู้สึกต่อความประพฤติที่ถูกนำเสนอ ขีดจำกัด ความเสี่ยง เส้นทางโต้แย้ง หรือการเยียวยา;
- **เงื่อนไขที่ปลอดภัย** ภายใต้ **มาตรา XII-A** (*เส้นฐานความพึ่งได้และความน่าไว้วางใจ*) และ [**เงื่อนไขที่ปลอดภัย**](core_05_band_continuity.md#safe-conditions-constitutional) ในที่ที่ระบบส่งมอบหรือกั้นกิจกรรมผลิต;
- **การจัดสรรทรัพยากร** ภายใต้ **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) รวม [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) ภายใต้ **มาตรา IV-B** (*ความเป็นธรรมและความยั่งยืนข้ามระบบ*) ในที่ที่ระบบจัดสรร จัดเส้นทาง ให้ทุน หรือสกัดจากโครงสร้างพื้นฐานร่วมหรือการพึ่งฐานราก

<a id="2-system-class-evaluation"></a>

### 2. การประเมินชั้นระบบ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [§1](#1-purpose-and-role) (*จุดประสงค์และบทบาท*); ความเป็นสาระเชิงบูรณาการ ([การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination)) (*ความเป็นสาระ*); [จตุรภาคทางรัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad); [สองเป้าประสงค์ทางรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims); [ผลกระทบที่เป็นสาระ](core_05_band_oversight.md#material-impact) [การพึ่งพา](core_05_band_continuity.md#dependency) [ความเสี่ยง](core_05_band_continuity.md#risk) [ขอบเขตระบบ](core_05_band_continuity.md#system-boundaries) และ [ตราสารกำหนดขอบเขต](core_05_band_continuity.md#charter) (บทที่ห้า); [บทที่หนึ่ง §14 ข้อกำหนดการประเมินเชิงระบบ](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement); **มาตรา III-A** (*การอยู่รอด*) และ **มาตรา III-B** (*การส่งมอบพื้นสิทธิในที่ที่การจำแนกกั้นการเข้าถึง*); **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) และ **มาตรา IV-B** (*การจัดสรรทรัพยากรและการบริหารการพึ่งพาอย่างรับผิดชอบในที่ที่การรับรองกั้นการพึ่งโครงสร้างพื้นฐานร่วม*)
- ปลายทาง: [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*โปรไฟล์ชั้นตัวอย่าง*); [§3.8](#38-illustrative-whole-system-application-by-class) (*ตัวอย่างทั้งระบบที่ทำงานแล้วตามชั้น*); [§4.1](#41-illustrative-data-handling-application-by-class) (*ตัวอย่างการปฏิบัติข้อมูลที่ทำงานแล้วตามชั้น*); [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*ตัวอย่างรอยเท้าทางนิเวศที่ทำงานแล้วตามชั้น*); [§6.1](#61-illustrative-cross-system-support-application-by-class) (*ตัวอย่างการสนับสนุนข้ามระบบที่ทำงานแล้วตามชั้น*); [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*ตัวอย่างการไม่เลือกปฏิบัติที่ทำงานแล้วตามชั้น*); [§8.1](#81-illustrative-accessibility-application-by-class) (*ตัวอย่างการเข้าถึงได้ที่ทำงานแล้วตามชั้น*); [§9.1](#91-illustrative-educational-capability-application-by-class) (*ตัวอย่างขีดความสามารถทางการศึกษาที่ทำงานแล้วตามชั้น*); [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ตัวอย่างความน่าไว้วางใจที่ทำงานแล้วตามชั้น*); [§4](#4-data-types-and-handling-evaluation) (*การประเมินการปฏิบัติข้อมูลร่วม*); [§5](#5-ecological-footprint-evaluation) (*การประเมินรอยเท้าทางนิเวศ*); [§6](#6-proportionate-cross-system-support-evaluation) (*การประเมินการสนับสนุนข้ามระบบ*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ความไม่สอดคล้องของการจำแนกและตัวกระตุ้นการจำแนกใหม่*)
- อ่านคู่กับ: [บันทึกการจำแนกระบบ](core_05_band_continuity.md#system-classification-record-constitutional); [corpus_systems.md](../../corpus_systems.md) **CS-3 — การจำแนกและการปฏิบัติของระบบ** รวม **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** (*ข้อกำหนดการจำแนกใหม่* — ตัวกระตุ้น ความลึกประเมินที่ปรับตามชั้น และสะพานยืนยัน SAC) และ **[CS-3 §7](../../corpus_systems/cs_03_a_system_classification_machinery.md#cs-3-7-classification-governance-disclosure-and-challenge)** (*หน้าที่การปกครองของบันทึกการจำแนกระบบและสะพาน SAC*); [CS-5 — การออกแบบ การทดสอบ การตรวจสอบ และการติดตั้งใช้งาน](../../corpus_systems/cs_05_design_testing_verification_deployment.md); [CJS-3.21 — คำความทนทานแบบตรงข้ามและความต้านการละเมิด](../../corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) (*หน้าที่วงการถดถอยและการทำให้แข็ง*); [corpus_forum.md](../../corpus_forum.md) **CF-7.2** (*การรับรู้และการทบทวนความสอดคล้องทางรัฐธรรมนูญ*)

</details>

<br>

*พูดแบบตรง ๆ: การรับรองต้องตรวจว่าระบบถูกจำแนกอย่างซื่อ — ไม่ใช่จากที่ผู้ดำเนินการเรียก แต่จากสิ่งที่มันทำจริง สิ่งที่พึ่งมัน และสิ่งที่ผิดพลาดได้ ชั้นสูงกว่าหมายถึงหลักฐานเข้มกว่า การตรวจซ้ำเร็วกว่า และความคาดหวังความทนสูงกว่า ดู [§2.1](#21-illustrative-class-profiles-non-exhaustive) สำหรับระบบหนึ่งต่อชั้น; [§3.8](#38-illustrative-whole-system-application-by-class) [§4.1](#41-illustrative-data-handling-application-by-class) [§5.1](#51-illustrative-ecological-footprint-application-by-class) [§6.1](#61-illustrative-cross-system-support-application-by-class) [§7.1](#71-illustrative-nondiscrimination-application-by-class) [§8.1](#81-illustrative-accessibility-application-by-class) [§9.1](#91-illustrative-educational-capability-application-by-class) และ [§10.1](#101-illustrative-trustworthiness-application-by-class) เดินดูว่าการประเมินใช้กับแต่ละระบบอย่างไร*

การรับรองความสอดคล้องของระบบต้องประเมิน **ชั้นระบบ** เป็นส่วนของทุกบันทึกการรับรองผลกระทบที่เป็นสาระ บทนิยามชั้นฉบับหลัก กฎมิติ โปรไฟล์ชั้น การปกครองการจำแนก การประกันที่ปรับตามชั้น ความทนของโครงสร้างพื้นฐาน และกลไกการรับรองใหม่ อยู่ใน **[corpus_systems.md](../../corpus_systems.md), CS-3 — การจำแนกและการปฏิบัติของระบบ** และ **[CS-5 — การออกแบบ การทดสอบ การตรวจสอบ และการติดตั้งใช้งาน](../../corpus_systems/cs_05_design_testing_verification_deployment.md)** หมวดนี้กล่าวสิ่งที่การรับรองต้องยืนยันและบันทึก; ไม่กล่าวซ้ำอนุกรมวิธานชั้นของ CS-3 โปรไฟล์การนำไปใช้ หรือกลไกทดสอบของ CS-5

การรับรองต้องยืนยันและบันทึก:

- **ข้อกำหนดการประเมิน:**
  - ว่าชั้นระบบที่กำหนดสะท้อน **ผลกระทบ** **การพึ่งพา** และ **ความเสี่ยง** ที่สังเกตได้และคาดได้ตามเหตุภายใต้ CS-3 รวมผลรวม ปฏิสัมพันธ์ แบบตรงข้าม และธรณีประตู; และ
  - ว่าการจำแนกถูกกำหนดจากความประพฤติและผลกระทบจริงของระบบ ไม่จากเจตนาที่ประกาศ ขอบเขตในนาม ข้อความ [ตราสารกำหนดขอบเขต](core_05_band_continuity.md#charter) เพียงอย่างเดียว หรือคำอธิบายตนเองเพียงอย่างเดียว; และ
  - ว่าการประเมินการจำแนกใหม่ภายใต้ **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** ถูกนำไปใช้ในที่ที่ตัวกระตุ้นการประเมินใหม่ที่เป็นสาระทำงาน และว่า [บันทึกการจำแนกระบบ](core_05_band_continuity.md#system-classification-record-constitutional) สะท้อนชั้น **สูงสุดที่ใช้ได้** ภายใต้เงื่อนไขปัจจุบัน
- **ข้อกำหนดบันทึก:**
  - [บันทึกการจำแนกระบบ](core_05_band_continuity.md#system-classification-record-constitutional) ที่กล่าวชั้นที่กำหนด เหตุผลการจำแนก ข้อสมมติหลัก ชนิดการพึ่งที่มี การประเมินความวิกฤตปฏิบัติการในที่ที่เป็นสาระ ความไม่แน่นอน และจังหวะการรับรองซ้ำที่ปรับตามชั้น ตามที่ [ส่วน ข §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) ขอ; และ
  - ในที่ที่การจำแนกไม่แน่นอนหรือถูกโต้แย้ง ชั้นเชิงป้องกันที่พึ่งและเงื่อนไขใดที่รอการยุติ
- **การประกันและการรับรองใหม่:**
  - ว่าการประกันที่ปรับตามชั้น ความทนของโครงสร้างพื้นฐาน และการครอบการถดถอยตรงกับ CS-3 และ CS-5 สำหรับชั้นที่กำหนด อ่านคู่กับ [**CJS-3.21**](../../corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) และ **CJS-3.19** ถึง **CJS-3.23** ในที่ที่ใช้ได้อย่างเป็นสาระ;
  - ผลการทดสอบถดถอยบนบันทึกการรับรองภายใต้ [ส่วน ข §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) สำหรับแต่ละการรับรองใหม่หรือการรับรองซ้ำ — ขอบการถดถอย ชุดทดสอบมาตรฐานและกำหนดเองที่รัน ผล ความล้มเหลวที่รู้ การเยียวยา และความเสี่ยงคงเหลือที่ยอมรับพร้อมเหตุผล ตามที่ CS-5 ขอ;
  - หลักฐานการรับรู้และการทบทวนบนบันทึกสำหรับรอบการรับรอง — ชุดหลักฐานที่แสดงขอบเขต การจำแนก การทดสอบ ความเสี่ยงคงเหลือ ความพร้อมเยียวยา การเฝ้า และการเปลี่ยนแปลงที่เป็นสาระตั้งแต่บันทึกก่อนในที่ที่ใช้การรับรองใหม่ ตามที่ CS-5 *การรับรู้ของเวทีและการทบทวนวงชีวิต* ขอ; และ
  - สำหรับระบบที่กั้นหรือค้ำการส่งมอบพื้นสิทธิ ว่าจังหวะการรับรองซ้ำและความลึกของการถดถอยทำให้เป้าประสงค์ **ความต่อเนื่อง** ภายใต้ [สองเป้าประสงค์ทางรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims) ปฏิบัติการ — การรับรองที่เก่าหรือเร็วเกินไปต้องไม่ถูกถือเป็นหลักฐานว่าผู้มีความรู้สึกยังได้รับอาหาร น้ำ ที่พัก การศึกษา หรือความปลอดภัยในการปฏิบัติ
- **การจำแนกผิดและข้อบกพร่อง:**
  - การกล่าวอ้างชั้นความเสี่ยงต่ำกว่าที่ระบบสมควร การหักระบบเป็นชิ้นเพื่อเลี่ยงกฎที่เข้มกว่า หรือการคงป้ายชั้นเก่าหลังเงื่อนไขเปลี่ยน — รวมความล้มเหลวในการประเมินใหม่ภายใต้ **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** — เป็นข้อบกพร่องของการรับรองภายใต้ CS-3 และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) ไม่ใช่ความผิดพลาดเอกสารเล็กน้อย;
  - การข้ามการทดสอบถดถอย การพึ่งผลที่ล้าสมัย การปล่อยรอยแตกที่รู้โดยไม่ซ่อม หรือการยอมรับการแก้ใหญ่โดยไม่ทดสอบซ้ำเมื่อทดสอบซ้ำทำได้ — เป็นข้อบกพร่องของการรับรองภายใต้ CS-5; และ
  - ในที่ที่ข้อเท็จจริงรองรับ ปัญหาการจำแนกเดียวกันอาจนับเข้าสู่ข้อค้นพบร่องรอยที่ไม่เป็นคุณใน [บทที่แปด](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model)

ในที่ที่การรับรองพบข้อบกพร่องเหล่านี้ เวทีอาจอนุมัติมีเงื่อนไข เลื่อนการอนุมัติ ปฏิเสธ ถอนการรับรู้ เปลี่ยนจังหวะการทบทวน หรือสั่งการทบทวนใหม่

<a id="21-illustrative-class-profiles-non-exhaustive"></a>

#### 2.1 โปรไฟล์ชั้นตัวอย่าง (ไม่ครบถ้วน)

*พูดแบบตรง ๆ: ชั้นไม่ใช่ตราที่ผู้ดำเนินการเลือก — คือปริมาณภัย การพึ่ง และความเสี่ยงที่ระบบแบกจริง ตารางด้านล่างตั้งชื่อระบบตัวอย่างหนึ่งต่อชั้น; [§3.8](#38-illustrative-whole-system-application-by-class) [§4.1](#41-illustrative-data-handling-application-by-class) [§5.1](#51-illustrative-ecological-footprint-application-by-class) [§6.1](#61-illustrative-cross-system-support-application-by-class) [§7.1](#71-illustrative-nondiscrimination-application-by-class) [§8.1](#81-illustrative-accessibility-application-by-class) [§9.1](#91-illustrative-educational-capability-application-by-class) และ [§10.1](#101-illustrative-trustworthiness-application-by-class) เดินดูว่าการประเมินทั้งระบบ การปฏิบัติข้อมูล รอยเท้าทางนิเวศ การสนับสนุนข้ามระบบ การไม่เลือกปฏิบัติ การเข้าถึงได้ ขีดความสามารถทางการศึกษา และความน่าไว้วางใจใช้กับแต่ละระบบอย่างไร กฎชั้นแบบทางการ การทดสอบมิติ และตัวกระตุ้นการจำแนกใหม่อยู่ใน **CS-3**; ตัวอย่างเหล่านี้ไม่เพิ่มชั้นหรือทำให้ CS-3 แคบลง*

| ชั้น | ระบบตัวอย่าง (ไม่ครบถ้วน) | สิ่งที่การรับรองต้องสะท้อนที่ชั้นนี้ |
|-------|-------------------------------------|-----------------------------------------------|
| **Class A** | การควบคุมและโทรมาตร **น้ำดื่มปลอดภัย** ของเทศบาล — การขาดช่วงจะปิดน้ำปลอดภัยก่อนที่ของแทนที่ใช้ได้จะมาถึง ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | ความลึก [§3](#3-whole-system-certification-evaluation) ที่เต็มที่สุด; จังหวะการรับรองซ้ำที่สั้นที่สุดที่มีเหตุ; ความคาดหวังการถดถอย โครงสร้างพื้นฐาน และการเปิดเผยบันทึกที่เข้มที่สุดภายใต้ [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record); การมีส่วนร่วมของฝ่ายที่ได้รับผลกระทบและเวทีผู้มีความรู้สึกที่ใช้ปฏิบัติได้สูงสุดในที่ที่พื้นสิทธิถูกกั้น |
| **Class B** | **การแลกเปลี่ยนบันทึกคลินิก** ระดับภูมิภาค — โรงพยาบาลและคลินิกพึ่งทุกวันแต่ถอยไปใช้ทางสำรองได้ภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | การประเมิน [§3](#3-whole-system-certification-evaluation) เต็ม; หลักฐานสายการพึ่งและเส้นทางฟื้นที่แข็ง; การประเมินโดเมนใน [§4](#4-data-types-and-handling-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้; เส้นทางโต้แย้งและการเฝ้าที่ปรับตามความวิกฤตปฏิบัติการ |
| **Class C** | แพลตฟอร์ม **จัดตารางและประสานสถาบัน** ขนาดใหญ่ — หล่อหลอมการประสานในระดับแต่ไม่ใช่เงื่อนไขปฏิบัติการสำหรับบริการอยู่รอดในโหมดเสื่อม ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | การประเมินที่เป็นสาระภายใต้ [§4](#4-data-types-and-handling-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) ในที่ที่ตัวกระตุ้นใช้; การทบทวนทั้งระบบตามสัดส่วน; การเฝ้าการจำแนกใหม่ในที่ที่ผลของการพึ่ง ความเข้มข้น หรือจุดคอขวดเข้มขึ้น — การรับรองต้องไม่ถือ Class C เป็นถาวรหากระบบกลายเป็นจำเป็นปฏิบัติการ |

**การมีส่วนร่วมและสัดส่วนที่มาตราส่วนชั้น.** ระบบ **Class A** ขอเส้นทางการมีส่วนร่วมที่ใช้ปฏิบัติได้เข้มที่สุด — รวมการโต้แย้งที่เข้าถึงได้ การทบทวนฝ่ายที่ได้รับผลกระทบ และข้อค้นพบส่วนประกอบเวทีผู้มีความรู้สึกในที่ที่พื้นสิทธิเกี่ยว — เพราะความผิดพลาดอาจปิดสิ่งจำเป็นต่อการอยู่รอดก่อนการเยียวยาจะเป็นไปได้ ระบบ **Class B** ขอการมีส่วนร่วมที่แข็งในที่ที่ระบบกั้นการดูแลสุขภาพ การศึกษา สวัสดิการ งาน หรือชีวิตประจำวันที่คล้าย ระบบ **Class C** ยังขอบันทึกที่โต้แย้งได้และการเปิดเผยตามสัดส่วน โดยเฉพาะในที่ที่ผลประสานแบกกลุ่มที่คุ้มครอง กระจุกการพึ่ง หรือส่งสัญญาณการยกระดับสู่ Class B หรือ Class A

**เครื่องเตือนการจำแนกใหม่.** ป้ายตัวอย่างไม่ล็อกการจำแนก แพลตฟอร์มประสานที่กลายเป็นประตูตามจริงสู่การเข้าถึงที่จำเป็นต่อการอยู่รอด; บริการหลักฐานคุณวุฒิที่การขาดตอนจะกั้นการดูแลสุขภาพหรือสวัสดิการภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด; หรือระบบย่อยสาธารณูปโภคที่ถูกดูดเข้าเส้นทางวิกฤต ต้องถูกจำแนกใหม่และรับรองใหม่ภายใต้ **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) — ไม่ทิ้งไว้ที่ชั้นต่ำกว่าเพราะผู้ดำเนินการชอบการทบทวนที่เบากว่า


<a id="3-whole-system-certification-evaluation"></a>

### 3. การประเมินการรับรองทั้งระบบ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [บทที่หนึ่ง §14 ข้อกำหนดการประเมินเชิงระบบ](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement); ครอบครัวการวัดความเจริญงอกงาม (*สุขภาวะ ความปลอดภัย ภัย และการเข้าถึงพื้นการอยู่รอด*); ครอบครัวการวัดสมรรถนะทางรัฐธรรมนูญ (*ประสิทธิภาพทางรัฐธรรมนูญ ภาระที่หลีกเลี่ยงได้ และขีดความสามารถผลิต*); [จตุรภาคทางรัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad); [สองเป้าประสงค์ทางรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims); [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake); [§1 จุดประสงค์และบทบาท](#1-purpose-and-role)
- ปลายทาง: [§3.8](#38-illustrative-whole-system-application-by-class) (*การเดินดูทั้งระบบตัวอย่าง*); [§4](#4-data-types-and-handling-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) (*การประเมินโดเมน*); [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*โปรไฟล์ชั้นตัวอย่าง*); [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain) (*สายความสามารถในการโต้แย้ง*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*การเปิดใหม่และต้านการหลบ*)
- อ่านคู่กับ: [บทที่หนึ่ง §9](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding) [§10](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline) และ [§11](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture); [§5.2 สิทธิการยุติโดยสมัครใจและการออก](core_01_a_values_principles.md#52-voluntary-discontinuation-and-exit-rights); [§5.3 การชุมนุม การจัดองค์กรร่วม และการก่อตั้งสถาบัน](core_01_a_values_principles.md#53-assembly-collective-organization-and-institutional-formation); **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*) ในที่ที่พื้นสิทธิการตรวจ ความโปร่งใส หรือการตรวจสอบอิสระอยู่ในส่วนได้เสียที่เป็นสาระ; ครอบครัวการวัดความต่อเนื่อง ([§3.1](#31-systemic-scope-and-risk-factors) — ความทน ความย้อนกลับได้ และความเสี่ยงระบบ); [การประเมินความเสี่ยง](core_05_band_continuity.md#risk-evaluation); [การเปิดเผยความเสี่ยง](core_05_band_oversight.md#risk-disclosure); [การเปิดเผยเส้นฐานการกำกับดูแลสาธารณะ](core_05_band_oversight.md#public-oversight-baseline-disclosure); ครอบครัวการวัดการมีส่วนร่วม ([§3.3](#33-privacy-informational-joint-invocation) — ความเป็นส่วนตัวและการบริหารข้อมูลอย่างรับผิดชอบ); ครอบครัวการวัดความรับผิดชอบ ([§3.7](#37-governance-incentive-and-contestability-discipline) — ความสอดคล้องของสิ่งจูงใจและความสามารถในการโต้แย้งของตลาด); [ขอบเขตระบบ](core_05_band_continuity.md#system-boundaries); [ตราสารกำหนดขอบเขต](core_05_band_continuity.md#charter)
- หมวดย่อย: [§3.1](#31-systemic-scope-and-risk-factors) ถึง [§3.7](#37-governance-incentive-and-contestability-discipline) (*ปัจจัยประเมินทั้งระบบ*); [§3.8](#38-illustrative-whole-system-application-by-class) (*การนำไปใช้ทั้งระบบตัวอย่างตามชั้น*)

</details>

<br>

*พูดแบบตรง ๆ: ผ่านชิ้นเดียวของระบบแล้วเพิกเฉยส่วนที่เหลือไม่ได้ ผู้ทบทวนต้องการภาพเต็ม — พึ่งอะไร เมื่อต้นทางล้มเหลวอะไรแตก ภัยที่โผล่ทีหลังหรือสะสมตามเวลา ผู้มีความรู้สึกใช้ได้จริงหรือไม่ (ไม่ใช่แค่บนกระดาษ) ข้อมูลส่วนตัวถูกกั้นอย่างถูกหรือไม่ ผู้มีความรู้สึกออกได้โดยไม่ติดกับ กลุ่มยังจัดองค์กรได้โดยระบบไม่แยกพวกเขา ชัยระยะสั้นซ่อนภัยระยะยาวหรือไม่ และการกำกับดูแลกับความรับผิดชอบจริงยังทำงานเมื่อส่วนได้เสียสูง*

การประเมินการรับรองความสอดคล้องของระบบไม่ครบหากพิจารณาเฉพาะผลทันทีหรือเฉพาะที่ บันทึกการรับรองต้องแสดงว่าการประเมินพิจารณาปัจจัยด้านล่างในที่ที่เป็นสาระต่อการรับรู้ การยืนยัน การรับรองซ้ำ การพึ่งต่อเนื่อง การติดตั้งใช้งาน หรือการปล่อยจากเงื่อนไขที่เป็นสาระ การประเมินต้องยืนยันด้วยว่า [จตุรภาคทางรัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad) จะสนองการปรับตาม [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) สำหรับระบบที่ทบทวน การเดินดูทั้งระบบที่ทำงานแล้วสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§3.8](#38-illustrative-whole-system-application-by-class)

<a id="31-systemic-scope-and-risk-factors"></a>
#### 3.1 ขอบเขตเชิงระบบและปัจจัยความเสี่ยง

การประเมินการรับรองต้องพิจารณา:

- **ความสัมพันธ์การพึ่งและผลลูกโซ่** — อะไรล้มที่ปลายทางเมื่อต้นทางแตก;
- **ผลรวมและผลขนาด** — อะไรเปลี่ยนเมื่อการกระทำเล็ก ๆ หลายอย่างรวมกัน;
- **ผลกระทบที่ล่าช้า สะสม และเชิงความน่าจะเป็น** — ภัยที่โผล่ทีหลัง กอง หรือขึ้นกับโอกาส;
- **เงื่อนไขแบบตรงข้ามและศักยภาพการใช้ผิด** — ตัวแสดงไม่ดีหรือการละเมิดที่คาดได้จะใช้ระบบอย่างไร;
- **ขอบเขตตามตราสารเทียบขอบเขตหน้าที่** — ว่า [ตราสารกำหนดขอบเขต](core_05_band_continuity.md#charter) ที่กำกับ ในที่ที่มีหรือถูกขอ ตรงกับ [ขอบเขตระบบ](core_05_band_continuity.md#system-boundaries) ที่สังเกต และว่าขอบเขตที่กล่าวต่ำกว่าผลกระทบหรือการพึ่งที่เป็นสาระ;
- **ความเสี่ยงต่อการดำรงอยู่** — ผลที่อาจคุกคามการอยู่รอดของผู้มีความรู้สึกหรือ [ขีดความสามารถฟื้นทางนิเวศ](core_05_band_continuity.md#ecological-recovery-capacity-constitutional) ที่มาตราส่วนอารยธรรม

**สะพานการประเมินและการเปิดเผยความเสี่ยง.** ในที่ที่ [ความเสี่ยง](core_05_band_continuity.md#risk) ระบบอยู่ในขอบเขตภายใต้ปัจจัยด้านบน การรับรองต้องยืนยันทั้งสองครึ่งของคู่บทที่ห้า — ไม่ประดิษฐ์ชนิดบันทึกเปิดเผยความเสี่ยงที่ตั้งชื่อแยก:

- **[การประเมินความเสี่ยง](core_05_band_continuity.md#risk-evaluation)** — ว่าความเสี่ยงระบบถูกประเมินจริงภายใต้เงื่อนไขที่สำคัญ (การพึ่ง ขอบฟ้าเวลา และ [เงื่อนไขแบบตรงข้าม ตามขนาด และถูกใช้](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions)) ปรับขนาดตามชั้นและ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake); และ
- **[การเปิดเผยความเสี่ยง](core_05_band_oversight.md#risk-disclosure)** — ว่าความเสี่ยงที่ประเมินถึงผู้มีความรู้สึกที่ต้องการมันทันเวลาเพื่อเข้าใจ โต้แย้ง และกระทำ

การประเมินโดยไม่เปิดเผย หรือการเปิดเผยโดยไม่ประเมิน ทั้งคู่ไม่ผ่าน ความมองเห็นเส้นฐานสาธารณะต่อความเสี่ยงที่เป็นสาระภายใต้ [การเปิดเผยเส้นฐานการกำกับดูแลสาธารณะ](core_05_band_oversight.md#public-oversight-baseline-disclosure) อาจถูกสนองบางส่วนผ่านการเปิดเผยความเสี่ยงในที่ที่ความเสี่ยงระบบอยู่ในขอบเขต; พื้นนั้นยังกว้างกว่าสะพานนี้ และไม่ขอตราสารคู่ข้าง [บันทึกการจำแนกระบบ](core_05_band_continuity.md#system-classification-record-constitutional) หรือ [บันทึกชนิดข้อมูลของระบบ](core_05_band_continuity.md#system-data-types-record-constitutional)

**ข้อกำหนดบันทึก.** ในที่ที่ความเสี่ยงระบบอยู่ในขอบเขต [บันทึกการรับรองระบบ](core_05_band_continuity.md#system-certification-record-constitutional) ภายใต้ **[ส่วน ข §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)** ต้องกล่าว:

- ข้อค้นพบการประเมินความเสี่ยงและข้อสมมติที่พึ่งสำหรับปัจจัยด้านบน;
- ท่าทีการเปิดเผย — รวม:
  - ผู้รับที่ตั้งใจหรือการจัดเส้นทาง;
  - เวลาเทียบการตัดสินที่เป็นสาระ; และ
  - การกักที่มีเหตุใดที่จับคู่กับของแทนที่ใช้ได้
- ข้อบกพร่องหรือเงื่อนไขในที่ที่การประเมินหรือการเปิดเผยยังไม่ครบ

ข้อค้นพบเหล่านั้นอยู่บนบันทึกการรับรอง ไม่ใช่บันทึกส่วนประกอบที่มีชื่อข้อที่ห้าที่บังคับ

**ข้อบกพร่องและความไม่สอดคล้อง.** การถือบันทึกภายใน ภาคผนวกที่ฝัง รายการตรวจ หรือคำแถลงภายหลังเป็นการประเมินหรือการเปิดเผย; การไม่เปิดเผยความเสี่ยงระบบที่ประเมินแก่ผู้ที่ต้องการในที่ที่ [ความโปร่งใส](core_05_band_oversight.md#transparency) หรือ [ความปลอดภัย (ข้อจำกัด)](core_05_band_continuity.md#safety-constraint) ขอ; หรือการรับรองการพึ่งต่อเนื่องขณะที่ช่องว่างการสื่อสารความเสี่ยงที่เป็นสาระยังไม่ยุติ ต้องถือเป็นข้อบกพร่องของการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="32-accessibility-under-sentience-non-exclusion"></a>
#### 3.2 การเข้าถึงได้ภายใต้การไม่กีดกันความเป็นผู้มีความรู้สึก

การประเมินการรับรองต้องทดสอบการมีส่วนร่วมจริงสำหรับทุกรูปแบบผู้มีความรู้สึกและโปรไฟล์ความสามารถ ไม่ใช่แค่การปฏิบัติตามบนกระดาษ

- *ขอบเขตของโปรไฟล์.* การประเมินต้องกล่าวทุกหมวดโปรไฟล์ที่เกี่ยวข้อง: ประสาท การรู้คิด การเคลื่อนที่ การสื่อสาร **ส่วนต่อประสานฐานะกาย** และ **ส่วนต่อประสานคำนวณ** ข้อกำหนดเดียวกันใช้ไม่ว่าโปรไฟล์จะ **คงที่** **เป็นช่วง** หรือ **เชิงพัฒนา**
- *มาตรฐาน.* การทดสอบคือ **ผลของการมีส่วนร่วมที่เป็นสาระ**: ว่าผู้มีความรู้สึกที่ได้รับผลกระทบ **จริง ๆ** มีส่วนร่วมในโดเมนได้ **การปฏิบัติตามสิ่งอำนวยแบบทางการ** ไม่พอ
- *การปรับขนาด.* พื้นการมีส่วนร่วมจริงสูงขึ้นตาม [ความเป็นสาระ](core_05_band_oversight.md#materiality-determination) ของโดเมน และ [การพึ่งพา](core_05_band_continuity.md#dependency) ของฝ่ายที่ได้รับผลกระทบต่อระบบ
- *ต้านการหลบ.* การรับรองต้องปฏิเสธรูปแบบ **การเข้าถึงทั่วไป** ที่กล่าวความพร้อมรวมกว้างขณะพ่ายแพ้โปรไฟล์ที่ได้รับผลกระทบเฉพาะ และ **การปรับความเป็นสาระแบบเลือก** ที่ผลคือพ่ายแพ้พื้นการมีส่วนร่วม
- *เจ้าของพื้นสิทธิ.* [มาตรา V-G](core_06_rights_part_b.md#article-v-g-accessibility) (*การเข้าถึงได้*) เป็นเจ้าของพื้นสิทธิการเข้าถึงได้ การเข้าถึงได้เฉพาะการศึกษาถูกกำกับต่อโดย [มาตรา III-B](core_06_rights_part_a.md#article-iii-b-equal-educational-access) (*การเข้าถึงการศึกษาที่เท่ากัน*)

<a id="33-privacy-informational-joint-invocation"></a>
#### 3.3 ความเป็นส่วนตัว (ด้านข้อมูล) การเรียกใช้ร่วม

*พูดแบบตรง ๆ: บทที่หกกระจายการคุ้มครองความเป็นส่วนตัวข้ามหลายมาตรา — ไม่ใช่มุมเดียวที่เป็นระเบียบ หากการทบทวนการรับรองแตะการคุ้มครองเหล่านั้นมากกว่าหนึ่ง ผู้ทบทวนต้องตรวจทุกข้อที่ใช้จริง การปิดช่องที่ง่ายที่สุดแล้วถือว่าเสร็จไม่พอ*

เมื่อเรื่องการรับรองเกี่ยวอย่างเป็นสาระกับมากกว่าหนึ่งจุดความเป็นส่วนตัวของบทที่หก การรับรองต้องกล่าวแต่ละจุดนั้น การปิดเรื่องภายใต้จุดเดียวไม่พอ

- *การเปิดให้มีส่วนร่วม.* [ความเป็นส่วนตัว (ด้านข้อมูล)](core_05_band_continuity.md#privacy-informational) เปิดให้ [การมีส่วนร่วม](core_05_apex_participation_leg.md#participation-constitutional) ที่เป็นสาระ การรับรองต้องยืนยันว่าการคุ้มครองความเป็นส่วนตัวที่รองรับเสียง การปรึกษา การสมาคม และการโต้แย้งไม่ถูกพ่ายแพ้ด้วยการแบ่งส่วน การอ่านข้าม หรือแรงกดการเปิดเผย
- *จุดกลุ่ม.* การครอบความเป็นส่วนตัวแบบกระจายอยู่ข้าม **มาตรา VII-A** (*ความเป็นเจ้าของตนเองของร่างกายและจิต*) **มาตรา VII-B** (*ขอบสภาวะภายในและการคุ้มครองชนิด N*) **มาตรา VIII** (*รูปลักษณ์ ข้อมูลประสบการณ์ และสิทธิการเผยแพร่*) **มาตรา IX-A** (*ภาวะตัวแสดงและเสรีภาพจากการบิดเบือน*) และ **มาตรา XIII-A** (*ขีดจำกัดความมั่นคง ข่าวกรอง และอำนาจปกปิด*)
- *กฎการเรียกใช้ร่วม.* ในที่ที่เรื่องเกี่ยวอย่างเป็นสาระกับมากกว่าหนึ่งจุด การรับรองต้องถึงแต่ละจุดนั้น และจะจัดเส้นทางเรื่องผ่านจุดเดียวในทางที่ให้หลบอีกจุดไม่ได้
- *บ้านหัวกลุ่ม.* บทที่ห้า [**Def.C3** (*ความเป็นส่วนตัว (ด้านข้อมูล)* — หัวกลุ่มระดับคู่)](core_05_band_accountability.md#privacy-informational-cluster) และ [ความเป็นส่วนตัว (ด้านข้อมูล)](core_05_band_continuity.md#privacy-informational) เป็นเจ้าของความหมาย
- *ห้ามผ่อนด้วยการอ่านข้าม.* มาตรฐานที่แต่ละสมาชิกกลุ่มกล่าวในท้องถิ่นควบคุมภายในขอบเขตของตน และจะคลายด้วยการนำเข้ามาตรฐานที่หลวมกว่าจากสมาชิกอื่นไม่ได้
- *พื้นชนิด N ถูกรักษา.* ในที่ที่ **มาตรา VII-B** (*ขอบสภาวะภายในและการคุ้มครองชนิด N*) เกี่ยวอย่างเป็นสาระ การปฏิบัติ **ชนิด N** ภายใต้ **[corpus_systems.md](../../corpus_systems.md), CS-2** ใช้ และไม่ถูกทำให้แคบด้วยปัจจัยนี้

<a id="34-voluntary-discontinuation-and-exit-rights"></a>
#### 3.4 สิทธิการยุติโดยสมัครใจและการออก

ในที่ที่ [บทที่หนึ่ง §5.2 สิทธิการยุติโดยสมัครใจและการออก](core_01_a_values_principles.md#52-voluntary-discontinuation-and-exit-rights) ใช้กับเรื่องการรับรอง การรับรองต้องทดสอบความสมัครใจ ความยินยอม ต้านการบังคับ แรงกดการพึ่ง ข้อมูล และความย้อนกลับได้ ก่อนข้อกล่าวอ้างการรับรองจะยืน ความเห็นชอบแบบทางการเพียงอย่างเดียวไม่พอ

<a id="35-assembly-collective-organization-and-institutional-formation"></a>
#### 3.5 การชุมนุม การจัดองค์กรร่วม และการก่อตั้งสถาบัน

ในที่ที่ [บทที่หนึ่ง §5.3 การชุมนุม การจัดองค์กรร่วม และการก่อตั้งสถาบัน](core_01_a_values_principles.md#53-assembly-collective-organization-and-institutional-formation) ใช้กับเรื่องการรับรอง การรับรองต้องทดสอบเรื่องร่วมกันพอที่จะกันการหลบด้วยการต้านการแบ่งส่วน การประเมินไม่ครบหากจัดเส้นทางเรื่องผ่านกรอบเดียวในทางที่พ่ายแพ้การคุ้มครองการชุมนุมหรือการจัดองค์กรร่วม

<a id="36-time-consistency-constraint"></a>
#### 3.6 ข้อจำกัดความสอดคล้องของเวลา

การรับรองจะถือตัวชี้วัดระยะใกล้ การปฏิบัติตามเฉพาะที่ หรือประสิทธิภาพขอบฟ้าสั้นว่าพอไม่ได้ ในที่ที่การละเมิดขอบฟ้ากลางหรือยาวที่คาดได้ยังไม่ถูกกล่าว การเพิ่มประสิทธิภาพขอบฟ้าสั้นเป็นโมฆะในที่ที่คาดได้ว่าจะก่อการละเมิดขอบฟ้ากลางหรือยาวของข้อจำกัด **ความปลอดภัย** **ความจริง** หรือ **สุขภาวะ** ภายใต้เงื่อนไขสะสม ล่าช้า หรือข้ามระบบ

<a id="37-governance-incentive-and-contestability-discipline"></a>
#### 3.7 วินัยการปกครอง สิ่งจูงใจ และความสามารถในการโต้แย้ง

*พูดแบบตรง ๆ: การทบทวนยังไม่จบเว้นผู้ทบทวนถามว่าสี่พื้นฐานจะยังทำงานที่ระดับความเสี่ยงที่เกี่ยวข้องหรือไม่ — ผู้มีความรู้สึกมีส่วนร่วมได้จริงหรือไม่ งานถูกเฝ้าและตรวจได้หรือไม่ การประพฤติผิดถูกตอบได้หรือไม่ และการตัดสินจะเคลื่อนเร็วพอเมื่อสำคัญ ผู้ทบทวนยังต้องรู้ว่าใครถืออำนาจที่เป็นสาระจริง และใครตอบอะไร — ไม่ใช่ «ทีม» คลุมเครือหรือเปลือกที่ผลักความผิด คำถามเหล่านั้นต้องถูกตอบเพื่อการรับรองที่ใช้ได้*

การประเมินการรับรองไม่ครบหากไม่ประเมินว่า **การกำกับดูแล** **ความรับผิดชอบ** **การมีส่วนร่วม** และ **ความทันเวลา** จะสนองการปรับตาม [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) สำหรับระบบที่ทบทวน การประเมินนั้นต้องรวมว่าบทบาทการบริหารอย่างรับผิดชอบ การปกครอง และความรับผิดชอบที่เป็นสาระถูก **กำหนดอย่างทางการ บันทึก และตามรอยได้** พอให้ความสามารถตอบและเส้นทางโต้แย้งที่ใช้ปฏิบัติทำงาน — ปรับตามชั้นระบบและผลกระทบที่เป็นสาระภายใต้ **[corpus_systems.md](../../corpus_systems.md), CS-3 — การจำแนกและการปฏิบัติของระบบ**

สำหรับวินัยนั้น การรับรองต้องอ่าน:

- **[บทที่หนึ่ง §9 การบริหารอย่างรับผิดชอบและความเข้าใจแบบกระจาย](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding)** — ความเข้าใจแบบกระจาย ความโปร่งใส ความสามารถในการตรวจ และความสังเกตได้ที่โต้แย้งได้;
- **[บทที่หนึ่ง §10 การปกครองภายใต้วินัยการบริหารอย่างรับผิดชอบ](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline)** — การปกครองที่ได้รับอำนาจและความสามารถตอบภายใต้วินัยการบริหารอย่างรับผิดชอบ;
- **[บทที่หนึ่ง §11 ความสอดคล้องของสิ่งจูงใจและการยึดครองระบบ](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture)** — ความสอดคล้องของสิ่งจูงใจ ความครบถ้วนของตัวแทน การแก้ข้อบกพร่องขอบฟ้าสั้น และการตอบการยึดครอง;
- **[บทที่หนึ่ง §11.1.4 เส้นทางความลึกของบทบาทและความรับผิดที่เป็นสาระ](core_01_c_stewardship_capacity_principles.md#1114-role-depth-and-material-responsibility-pathways)** — เส้นทางบทบาทที่มีผลและวินัยต้านการมีส่วนร่วมเชิงสัญลักษณ์;
- **[บทที่สิบสอง §5 บทบาทที่ได้รับอำนาจ การพัฒนาความสามารถ และการมีส่วนช่วย](../../core_13_governance.md#5-authorized-roles-competency-development-and-contribution)** และ **[corpus_systems.md](../../corpus_systems.md), CS-4 — การบริหารอย่างรับผิดชอบระบบวิกฤต** — พื้นการนิยามบทบาท ความสามารถ และการตามรอยที่ใช้ปฏิบัติในที่ที่เป็นสาระ;
- **[มาตรา XV: การตรวจ ความโปร่งใส และการตรวจสอบอิสระ](core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification)** ในที่ที่พื้นสิทธิการตรวจ ความโปร่งใส หรือการตรวจสอบอิสระอยู่ในส่วนได้เสียที่เป็นสาระ

<a id="38-illustrative-whole-system-application-by-class"></a>

<a id="38-illustrative-whole-system-application-by-class-non-exhaustive"></a>
#### 3.8 การนำไปใช้ทั้งระบบตัวอย่างตามชั้น (ไม่ครบถ้วน)

*พูดแบบตรง ๆ: [§3.1](#31-systemic-scope-and-risk-factors) ถึง [§3.7](#37-governance-incentive-and-contestability-discipline) รายการสิ่งที่การทบทวนทั้งระบบต้องพิจารณา หมวดย่อยนี้แสดงว่าปัจจัยเหล่านั้นใช้กับระบบตัวอย่างหนึ่งต่อชั้นอย่างไร — สายการพึ่ง การมีส่วนร่วม ความเป็นส่วนตัว การออก การชุมนุม ขอบฟ้าเวลา และวินัยการปกครอง — และสิ่งที่ต้องปรากฏบนบันทึก ระบบตรงกับ [§2.1](#21-illustrative-class-profiles-non-exhaustive); [§4.1](#41-illustrative-data-handling-application-by-class) เดินระบบเดียวกันผ่านรายละเอียดการปฏิบัติข้อมูล*

**Class A — การควบคุมและโทรมาตรน้ำดื่มปลอดภัยของเทศบาล.** ชั้นควบคุมการบำบัดและจ่ายที่เมืองเป็นเจ้าของพึ่งพลังงาน การส่งเคมี ผู้ขาย **SCADA** (การควบคุมกำกับและการได้ข้อมูล) ตัวรับรู้ภาคสนาม และโครงสร้างพื้นฐานจ่ายปลายทาง; ความล้มเหลวอาจปิดน้ำปลอดภัยก่อนของแทนจะมาถึง

- **ปัจจัยที่อยู่ในขอบเขตอย่างเป็นสาระ:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — การพึ่งพลังงานและเคมีต้นทาง ความล้มเหลวจ่ายลูกโซ่ การใช้ผิดแบบปนเปื้อนหรือตัด และภัยมาตราส่วนการอยู่รอดหากความครบถ้วนของการควบคุมล้ม;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — การแจ้งฉุกเฉิน การรายงานขาดตอน และเส้นทางโต้แย้งสำหรับทุกโปรไฟล์ที่เกี่ยวข้องในที่ที่การเข้าถึงน้ำถูกกั้น;
  - [§3.3](#33-privacy-informational-joint-invocation) — การทบทวนร่วมในที่ที่ **โทรมาตร** ปฏิบัติการ (การวัดภาคสนามสดและสัญญาณควบคุม) ข้อมูลติดต่อลูกค้า และการเฝ้าผู้ขายตัดจุดความเป็นส่วนตัวบทที่หก;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — การล็อกผู้ขาย แรงกดสัญญาเทศบาล และความย้อนกลับได้ของการควบคุมที่มอบ;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — คณะกรรมการน้ำชุมชน เครือข่ายช่วยเหลือร่วม และองค์กรกำกับสาธารณะที่ต้องไม่ถูกแบ่งออก;
  - [§3.6](#36-time-consistency-constraint) — การบำรุงที่เลื่อน การตัดต้นทุนขอบฟ้าสั้น และภัยความปลอดภัยหรือนิเวศขอบฟ้ายาว;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — การปรับจตุรภาค **Class A** สำหรับการกำกับดูแล ความรับผิดชอบ การมีส่วนร่วม และความทันเวลาภายใต้ CS-3 และการตามรอยบทบาท CS-3
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าแผนที่การพึ่งและลูกโซ่รวมโหมดล้มเหลวพลังงาน เคมี ผู้ขาย และการจ่าย;
  - ว่าสถานการณ์ตัดแบบตรงข้าม คุณภาพเท็จ หรือปนเปื้อนถูกประเมินภายใต้ [การประเมินความเสี่ยง](core_05_band_continuity.md#risk-evaluation);
  - ว่าความเสี่ยงที่ประเมินถึงชุมชนและผู้ดำเนินการที่ได้รับผลกระทบซึ่งต้องการมันภายใต้ [การเปิดเผยความเสี่ยง](core_05_band_oversight.md#risk-disclosure);
  - ว่าชุมชนที่ได้รับผลกระทบรับคำเตือนได้จริง โต้แย้งการดำเนินงานไม่ปลอดภัย และมีส่วนร่วมในการทบทวนก่อนภัยจะย้อนไม่ได้;
  - ว่าการทบทวนความเป็นส่วนตัวถึงทุกจุดที่เกี่ยวอย่างเป็นสาระ;
  - ว่าการออกจากการมอบผู้ขายยังใช้ได้โดยไม่ปิดน้ำปลอดภัย;
  - ว่าเส้นทางการชุมนุมและการกำกับร่วมยังครบ;
  - ว่าการประหยัดขอบฟ้าสั้นคาดได้ว่าพ่ายแพ้ความปลอดภัยขอบฟ้ายาว; และ
  - ว่าบทบาทการบริหารอย่างรับผิดชอบที่กำหนดตามรอยได้พอสำหรับความสามารถตอบที่ความลึก **Class A**
- **สิ่งที่บันทึกต้องแสดง:**
  - ข้อค้นพบที่เป็นสาระภายใต้แต่ละปัจจัยที่เกี่ยวใน [§3.1](#31-systemic-scope-and-risk-factors) ถึง [§3.7](#37-governance-incentive-and-contestability-discipline);
  - ข้อสมมติการพึ่งและลูกโซ่;
  - ข้อค้นพบการประเมินความเสี่ยงและท่าทีการเปิดเผย (ผู้รับหรือการจัดเส้นทาง เวลา การกักและของแทน) ในที่ที่ความเสี่ยงระบบอยู่ในขอบเขต;
  - ข้อค้นพบการเข้าถึงได้และการมีส่วนร่วมสำหรับการกั้นพื้นการอยู่รอด;
  - การครอบการเรียกใช้ร่วมความเป็นส่วนตัว;
  - ข้อค้นพบการออกและการมอบ;
  - ข้อค้นพบการชุมนุมและการจัดองค์กรร่วมในที่ที่เป็นสาระ;
  - ข้อค้นพบความสอดคล้องของเวลา;
  - ข้อค้นพบการปกครอง สิ่งจูงใจ และความสามารถในการโต้แย้งที่ความลึก **Class A**;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่พื้นสิทธิเกี่ยว; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับความล้มเหลวผู้ขาย ความเสี่ยงลูกโซ่ หรือช่องว่างการปกครอง

**Class B — การแลกเปลี่ยนบันทึกคลินิกระดับภูมิภาค.** การแลกเปลี่ยนข้อมูลสุขภาพจัดเส้นทางสรุปคลินิกและโทเคนการระบุตัวตนระหว่างโรงพยาบาลและคลินิก; การปฏิบัติประจำพึ่งมัน แต่แฟกซ์ พอร์ทัลตรง หรือการดึงมืออาจแทนได้ภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด

- **ปัจจัยที่อยู่ในขอบเขตอย่างเป็นสาระ:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — การขาดตอนของโรงพยาบาลที่เข้าร่วม ความล้มเหลวการระบุตัวตน ความผิดพลาดการกำจัดซ้ำ และผลลูกโซ่ข้ามสถานที่ต่อการส่งการดูแล;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — การเข้าถึงของแพทย์ ผู้ป่วย และผู้สนับสนุนข้ามโปรไฟล์ประสาท การรู้คิด การเคลื่อนที่ การสื่อสาร ส่วนต่อประสานฐานะกาย และส่วนต่อประสานคำนวณ;
  - [§3.3](#33-privacy-informational-joint-invocation) — การทบทวนร่วมข้ามจุดความเป็นส่วนตัวคลินิก ตัวตน การตรวจ และใกล้คุณสมบัติ;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — การออกของโรงพยาบาล ความพกพาบันทึกผู้ป่วย และต้านการล็อกสำหรับผู้เข้าร่วม;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — สมาคมแพทย์ กลุ่มสนับสนุนผู้ป่วย และองค์กรปกครองภูมิภาคที่ต้องไม่ถูกจัดเส้นทางเลี่ยง;
  - [§3.6](#36-time-consistency-constraint) — ข้อกล่าวอ้างประสิทธิภาพหรือความเข้ากันได้ขอบฟ้าสั้นที่คาดได้ว่าจะกร่อนคุณภาพการดูแลหรือความไว้วางใจขอบฟ้ายาว;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — การปรับจตุรภาค **Class B** สำหรับการพึ่งวิกฤตปฏิบัติการ
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าแผนที่การพึ่งครอบโรงพยาบาลที่เข้าร่วม นายหน้าตัวตน และเส้นทางสำรอง;
  - ว่าภัยล่าช้าหรือสะสมจากความผิดพลาดการจัดเส้นทาง บันทึกเก่า หรือการขาดตอนบางส่วนถูกประเมินภายใต้ [การประเมินความเสี่ยง](core_05_band_continuity.md#risk-evaluation);
  - ว่าความเสี่ยงปฏิบัติการและการส่งการดูแลที่ประเมินถึงแพทย์ ผู้ป่วย และผู้ดำเนินการที่ต้องการมันภายใต้ [การเปิดเผยความเสี่ยง](core_05_band_oversight.md#risk-disclosure);
  - ว่าการมีส่วนร่วมที่เป็นสาระถึงได้สำหรับแพทย์ ผู้ป่วย และผู้สนับสนุนที่พึ่งการแลกเปลี่ยน;
  - ว่าทุกจุดความเป็นส่วนตัวที่เกี่ยวอย่างเป็นสาระถูกกล่าว;
  - ว่าโรงพยาบาลและผู้ป่วยคงเส้นทางออกและความพกพาที่ใช้ได้;
  - ว่าเส้นทางการกำกับร่วมและการจัดองค์กรวิชาชีพยังโต้แย้งได้;
  - ว่ากรอบประสิทธิภาพซ่อนภัยการดูแลหรือความไว้วางใจขอบฟ้ายาว; และ
  - ว่าบทบาทการบริหารอย่างรับผิดชอบและความสามารถตอบตามรอยได้ที่ความลึกปฏิบัติการ **Class B**
- **สิ่งที่บันทึกต้องแสดง:**
  - ข้อค้นพบทั้งระบบที่ปรับตามความวิกฤตปฏิบัติการ **Class B**;
  - ข้อสมมติการพึ่ง ทางสำรอง และลูกโซ่;
  - ข้อค้นพบการประเมินความเสี่ยงและท่าทีการเปิดเผยในที่ที่ความเสี่ยงระบบอยู่ในขอบเขต;
  - ข้อค้นพบการเข้าถึงได้และการมีส่วนร่วมสำหรับการกั้นการดูแลสุขภาพ;
  - การครอบการเรียกใช้ร่วมความเป็นส่วนตัว;
  - ข้อค้นพบการออกและความพกพา;
  - ข้อค้นพบการชุมนุมและการจัดองค์กรร่วมในที่ที่เป็นสาระ;
  - ข้อค้นพบความสอดคล้องของเวลา;
  - ข้อค้นพบการปกครอง สิ่งจูงใจ และความสามารถในการโต้แย้ง;
  - ข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากการขาดตอนหรือความล้มเหลวการจัดเส้นทางจะกั้นการดูแลฉุกเฉินภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด

**Class C — แพลตฟอร์มจัดตารางและประสานสถาบัน.** ชั้นจัดตารางหลายองค์กรประสานกะ การจองห้อง และนัดผู้ขายข้ามโรงพยาบาล โรงเรียน และหน่วยงานสาธารณะ; บริการอยู่รอดแกนยังดำเนินในโหมดเสื่อมได้หากมันล้มเหลว แต่แพลตฟอร์มหล่อหลอมการประสานในระดับ

- **ปัจจัยที่อยู่ในขอบเขตอย่างเป็นสาระ:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — ผลความเข้มข้น ลูกโซ่ข้ามองค์กรเมื่อการจัดตารางล้ม และภาระเชิงความน่าจะเป็นบนกลุ่มที่คุ้มครองผ่านแบบการจัดสรร;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — ว่าพนักงาน นักเรียน ผู้ป่วย และผู้ขายใช้ส่วนต่อประสานจัดตารางและโต้แย้งได้อย่างเป็นสาระ;
  - [§3.3](#33-privacy-informational-joint-invocation) — ข้อมูลกำกับตาราง ติดต่อ และบทบาทในที่ที่หลายจุดความเป็นส่วนตัวใช้;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — การออกขององค์กรและความพกพาข้อมูลในที่ที่สถาบันพึ่งแพลตฟอร์ม;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — สหภาพ สมาคมผู้ปกครอง และองค์กรวิชาชีพที่การประสานต้องไม่ถูกยึดครองหรือแบ่งออก;
  - [§3.6](#36-time-consistency-constraint) — ประสิทธิภาพการจับคู่ขอบฟ้าสั้นที่คาดได้ว่าจะฝังแบบประสานที่ไม่เป็นธรรม;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — การปรับจตุรภาคตามสัดส่วนและการเฝ้าการจำแนกใหม่ในที่ที่ผลจุดคอขวดเข้มขึ้น
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าการทบทวนทั้งระบบถือแพลตฟอร์มเป็นโครงสร้างพื้นฐานประสานมากกว่าแอปโดด;
  - ว่าความเข้มข้น อคติการจับคู่ และลูกโซ่ข้ามองค์กรถูกประเมินอย่างซื่อภายใต้ [การประเมินความเสี่ยง](core_05_band_continuity.md#risk-evaluation);
  - ว่าความเสี่ยงประสานและการจัดสรรที่ประเมินถึงสถาบันและกลุ่มที่ได้รับผลกระทบซึ่งต้องการมันภายใต้ [การเปิดเผยความเสี่ยง](core_05_band_oversight.md#risk-disclosure);
  - ว่าเส้นทางการมีส่วนร่วมยังเป็นสาระในที่ที่แพลตฟอร์มกั้นการประสานเวที โรงเรียน หรือที่ทำงาน;
  - ว่าการทบทวนความเป็นส่วนตัวถึงจุดที่เกี่ยวอย่างเป็นสาระ;
  - ว่าการออกยังใช้ได้สำหรับองค์กรที่เข้าร่วม;
  - ว่าการคุ้มครองการชุมนุมและการจัดองค์กรร่วมถูกทดสอบร่วม;
  - ว่าความไม่เป็นธรรมขอบฟ้ายาวไม่ถูกซ่อนหลังประสิทธิภาพขอบฟ้าสั้น;
  - ว่าการปกครองและความสามารถในการโต้แย้งยังทำงานที่ความลึก **Class C**; และ
  - ว่าป้ายชั้นยังพอดีหากแพลตฟอร์มกลายเป็นประตูตามจริงสู่การเข้าถึงที่จำเป็นต่อการอยู่รอด
- **สิ่งที่บันทึกต้องแสดง:**
  - ข้อค้นพบทั้งระบบตามสัดส่วนกับความเสี่ยงประสาน **Class C** — ไม่ใช่รายการตรวจพิธี;
  - ข้อสมมติความเข้มข้นและลูกโซ่;
  - ข้อค้นพบการประเมินความเสี่ยงและท่าทีการเปิดเผยในที่ที่ความเสี่ยงระบบอยู่ในขอบเขต;
  - ข้อค้นพบการเข้าถึงได้และการมีส่วนร่วมในที่ที่การประสานถูกกั้น;
  - การครอบการเรียกใช้ร่วมความเป็นส่วนตัวในที่ที่ถูกกระตุ้น;
  - ข้อค้นพบการออกในที่ที่เป็นสาระ;
  - ข้อค้นพบการชุมนุมในที่ที่เป็นสาระ;
  - ข้อค้นพบความสอดคล้องของเวลา;
  - ข้อค้นพบการปกครองและความสามารถในการโต้แย้ง;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่ง น้ำหนักเกรดคลินิก หรือผลจุดคอขวดเข้มขึ้น; และ
  - ตัวชี้ไปยังการประเมินโดเมนใน [§4](#4-data-types-and-handling-evaluation) ถึง [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้

**การอ่านข้ามชั้น.** ปัจจัยใน [§3.1](#31-systemic-scope-and-risk-factors) ถึง [§3.7](#37-governance-incentive-and-contestability-discipline) ใช้กับทั้งสามระบบ; ชั้นเปลี่ยนว่าแต่ละปัจจัยต้องถูกประเมินและบันทึกลึกแค่ไหน แพลตฟอร์มจัดตาราง **Class C** ที่กลายเป็นเส้นทางปฏิบัติเดียวสู่การจัดกำลังฉุกเฉินหรือการจัดเส้นทางที่จำเป็นต่อการอยู่รอดต้องได้รับความลึกทั้งระบบ **Class A** หรือ **Class B** ตามข้อเท็จจริง — ไม่ใช่การทบทวนประสานที่เบากว่าที่ผู้ดำเนินการชอบ ระบบวิกฤตต่อการอยู่รอด **Class A** ต้องไม่ถูกลดชั้นขณะกั้นน้ำ พลังงาน หรือสิ่งจำเป็นต่อการอยู่รอดที่คล้ายโดยไม่มีของแทนที่ทันเวลา การแลกเปลี่ยน **Class B** ที่การขาดตอนจะกั้นการดูแลฉุกเฉินภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดต้องถูกจำแนกขึ้น — รวมสู่ **Class A** ในที่ที่สิ่งจำเป็นต่อการอยู่รอดถูกกั้น — และรับรองใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="4-data-types-and-handling-evaluation"></a>

### 4. การประเมินชนิดข้อมูลและการปฏิบัติ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [§3](#3-whole-system-certification-evaluation) (*ปัจจัยประเมินทั้งระบบ*); [§3.8](#38-illustrative-whole-system-application-by-class) (*การเดินดูตัวอย่างทั้งระบบ*); [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดการกำกับดูแล (*ความจริงและความครบถ้วนของความรู้ในฐานะการวัดทางรัฐธรรมนูญ*); [มาตรา XIV: ความครบถ้วนของวงข้อมูล](core_06_rights_part_c.md#article-xiv-info-sphere-integrity); [มาตรา XV: การตรวจ ความโปร่งใส และการตรวจสอบอิสระ](core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification); [มาตรา VII: ความเป็นเจ้าของตนเอง](core_06_rights_part_b.md#article-vii-self-ownership).
- ปลายทาง: [§4.1](#41-illustrative-data-handling-application-by-class) (*การเดินดูตัวอย่างการปฏิบัติข้อมูล*); [§5](#5-ecological-footprint-evaluation) และ [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*การประเมินรอยเท้าทางนิเวศและการเดินดูตัวอย่าง*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*การจำแนกใหม่และความไม่สอดคล้องของการปฏิบัติ*).
- อ่านคู่กับ: [corpus_systems.md](../../corpus_systems.md), **CS-2 — ชนิดข้อมูลและการปฏิบัติ** (รวม **[CS-2 §5.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*การจำแนกใหม่และการปกครองวงชีวิต*) และ **[CS-2 §8](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-8-system-data-types-record-governance)** (*การปกครองบันทึกชนิดข้อมูลของระบบ*)); [บันทึกชนิดข้อมูลของระบบ](core_05_band_continuity.md#system-data-types-record-constitutional); [การเปิดเผยเส้นฐานการกำกับดูแลสาธารณะ](core_05_band_oversight.md#public-oversight-baseline-disclosure); **CJS-3.18** (*เงื่อนไขการเก็บรักษาข้อมูลและความครบถ้วนของวงชีวิต*), **CJS-3.21** (*เงื่อนไขความมั่นคงเชิงปรปักษ์และความต้านการละเมิด*), และ **CJS-3.17** (*เงื่อนไขการทำงานร่วมกัน ความสามารถย้าย และความครบถ้วนของการออก*) ในที่ที่ใช้ได้อย่างเป็นสาระ.
- หมวดย่อย: [§4.1](#41-illustrative-data-handling-application-by-class) (*ตัวอย่างการประยุกต์การปฏิบัติข้อมูลตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: การรับรองต้องดูด้วยว่าชนิดข้อมูลใดที่ระบบแตะ และปฏิบัติต่อมันเหมาะสมหรือไม่ — รวมว่าชนิดยังถูกในรอบทบทวนปัจจุบันหรือไม่ และโครงสร้างพื้นฐานข้างใต้แข็งพอสำหรับข้อมูลนั้นที่ชั้นระบบนั้นหรือไม่ กฎชนิดและบันทึกชนิดข้อมูลของระบบอยู่ในคลังระบบ; การรับรองตรวจว่ากฎถูกนำไปใช้จริงและบันทึกซื่อ*

การรับรองความสอดคล้องของระบบต้องประเมิน **ชนิดข้อมูลและการปฏิบัติ** เป็นส่วนของบันทึกการรับรองที่มีผลกระทบที่เป็นสาระทุกฉบับ บทนิยามชนิดสารสนเทศฉบับหลัก กฎการปฏิบัติ ข้อกำหนดการแยก รายละเอียดวงชีวิต และ [บันทึกชนิดข้อมูลของระบบ](core_05_band_continuity.md#system-data-types-record-constitutional) ที่ยืน อยู่ใน **[corpus_systems.md](../../corpus_systems.md), CS-2 — ชนิดข้อมูลและการปฏิบัติ** หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำอนุกรมวิธานชนิดหรือกลไกการปฏิบัติของ CS-2

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าระบบระบุชนิดข้อมูลที่อยู่ในขอบเขตอย่างเป็นสาระ และปฏิบัติต่อมันภายใต้การจำแนก**ที่เข้มงวดที่สุดที่ใช้ได้** รวมข้ามการแปลง การรวม การมอบ การเก็บ การรักษา และการเชื่อมข้ามโดเมน การประเมินต้องสะท้อนผลเชิงหน้าที่ ไม่ใช่ป้าย รูปแบบ หรือขั้นท่อเพียงอย่างเดียว ในที่ที่เส้นฐาน Type O ของ **[CS-2 Part A §7](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems)** ใช้ การรับรองต้องยืนยันด้วยว่า [การเปิดเผยเส้นฐานการกำกับดูแลสาธารณะ](core_05_band_oversight.md#public-oversight-baseline-disclosure) ที่เผยแพร่ (**Type O**) ครอบ **ขอบเขตที่รับรอง** — ทำแผนที่จาก [ตราสารกำหนดขอบเขต](core_05_band_continuity.md#charter) ที่กำกับ (หรือตราสารขอบเขตที่เผยแพร่ที่เทียบได้) ชั้นที่กำหนด และ [ขอบเขตระบบ](core_05_band_continuity.md#system-boundaries) ที่สังเกต — พร้อมการกักที่มีเหตุจับคู่กับการแทนที่สาธารณะสูงสุดที่ทำได้; บทที่ห้าเป็นเจ้าของคำ; CS-2 เป็นเจ้าของเนื้อหาเส้นฐานและกลไกการเผยแพร่

**การประเมินชนิดข้อมูลเป็นระยะใหม่.** ในทุกวงจรการรับรองหรือการรับรองซ้ำที่มีผลกระทบที่เป็นสาระ กระบวนการต้องยืนยันว่าชุดข้อมูลที่เป็นสาระในขอบเขตถูก **ประเมินใหม่เป็นระยะ** เพื่อการจำแนกที่เหมาะสมภายใต้ **[CS-2 §5.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*การจำแนกใหม่และการปกครองวงชีวิต*) และ **CJS-3.18** (*เงื่อนไขการเก็บรักษาข้อมูลและความครบถ้วนของวงชีวิต*) และถูก **จำแนกใหม่** ในที่ที่การทบทวนนั้นขอ จังหวะต้องปรับตามชั้นระบบและผลกระทบที่เป็นสาระภายใต้ [§2](#2-system-class-evaluation) การจัดชนิดใหม่ที่ตัวเหตุการณ์กระตุ้นภายใต้ CS-2 ไม่แทนการตรวจรับรองเป็นระยะนี้

**ข้อกำหนดบันทึก.** การรับรองต้อง **ผลิตหรือยืนยัน** [บันทึกชนิดข้อมูลของระบบ](core_05_band_continuity.md#system-data-types-record-constitutional) — หรือเนื้อหาที่ถูกขอภายใต้ CS-2 — และรวมมันใน [บันทึกการรับรองระบบ](core_05_band_continuity.md#system-certification-record-constitutional) ภายใต้ **[ส่วน ข §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)** บันทึกนั้นต้องกล่าวชนิดข้อมูลที่อยู่ในขอบเขตอย่างเป็นสาระ เหตุผลการจำแนกสำหรับข้อมูลคลุมเครือหรือหลายชนิด การควบคุมการแยกและการเชื่อมข้ามโดเมนที่พึ่ง ท่าทีการรักษาและวงชีวิต ความสามารถระบุผู้กระทำที่พอรองรับ [การกระทำที่ระบุผู้กระทำได้](core_05_band_accountability.md#attributable-action-constitutional) และ [ความครบถ้วนของการระบุผู้กระทำ](core_05_band_accountability.md#attribution-integrity-constitutional) **การประเมินชนิดข้อมูลเป็นระยะล่าสุด** (วันที่หรือตัวระบุรอบ จังหวะ และการจัดชนิดใหม่ที่เป็นสาระใด) และขีดจำกัดการเปิดเผยหรือการเข้าถึงการตรวจที่มีเหตุ พร้อมการแทนที่สาธารณะในที่ที่ CS-2 ขอ ในที่ที่เส้นฐาน Type O ใช้ บันทึกต้องกล่าวด้วยว่า [การเปิดเผยเส้นฐานการกำกับดูแลสาธารณะ](core_05_band_oversight.md#public-oversight-baseline-disclosure) ครอบขอบเขตที่รับรองอย่างไร (ช่องตราสารกำหนดขอบเขตที่พึ่ง ข้อค้นพบขอบ และช่องว่างการครอบหรือเงื่อนไขใด)

**การปรับร่วมตามชั้นระบบ.** ความลึกของการปฏิบัติข้อมูลและการประกันโครงสร้างพื้นฐานต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ CS-3 ระบบชั้นสูงกว่าต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าโครงสร้างพื้นฐานการปฏิบัติ การเก็บ การประมวลผล การส่ง การสำรอง การกู้ และเฝ้า สามารถรักษาความครบถ้วนของการจำแนก การระบุผู้กระทำ และความสามารถในการโต้แย้งภายใต้ความกดดันได้ ในที่ที่ค่าปริยายทัศนวิสัยประโยชน์สาธารณะของ CS-2 ใช้ การรับรองต้องยืนยันว่าขีดจำกัดมีขอบแคบ จัดทำเอกสาร ตรวจได้ และจับคู่กับการแทนที่สูงสุดที่ทำได้ ไม่ใช่การซ่อนที่ทึบ

**ความมั่นคงของโครงสร้างพื้นฐานสำหรับข้อมูล.** การรับรองต้องประเมินว่าโครงสร้างพื้นฐานการปฏิบัติข้อมูล — รวมชั้นคงอยู่ ท่อข้อมูล การควบคุมการเข้าถึง ขอบเขตรหัสหรือการแยก เส้นทางสำรองและกู้คืน และสายการมอบของผู้ดำเนินการหรือผู้ขาย — เหมาะสมต่อชนิดข้อมูลและชั้นระบบที่เป็นประเด็นหรือไม่ ช่องว่างที่เป็นสาระในความครบถ้วนของวงชีวิต ความมั่นคงเชิงปรปักษ์ ความสามารถย้าย หรือความสามารถกู้ ต้องกล่าวบนบันทึกและสะท้อนในผลการรับรอง เงื่อนไข หรือขีดจำกัดการพึ่ง

**ข้อบกพร่องและความไม่สอดคล้อง.** การจำแนกข้อมูลผิด การจัดโครงสร้างใหม่เพื่อเลี่ยง การเชื่อมข้ามโดเมนที่ไม่ปลอดภัย การระบุผู้กระทำที่ขาดในที่ที่ภัยที่เป็นสาระจะสอบสวนไม่ได้ **การประเมินชนิดข้อมูลเป็นระยะที่เลยกำหนดหรือถูกข้าม** หรือความเปราะของโครงสร้างพื้นฐานที่คาดได้ว่าเอาชนะการคุ้มครอง CS-2 ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="41-illustrative-data-handling-application-by-class"></a>

<a id="41-illustrative-data-handling-application-by-class-non-exhaustive"></a>
#### 4.1 ตัวอย่างการประยุกต์การปฏิบัติข้อมูลตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: ตารางชั้นใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) กล่าวว่าชั้นสูงกว่าต้องการการทบทวนที่เข้มกว่า [§3.8](#38-illustrative-whole-system-application-by-class) แสดงว่าหมายความอย่างไรสำหรับ **การประเมินทั้งระบบ** บนระบบตัวอย่างสามระบบเดียวกัน; [§5.1](#51-illustrative-ecological-footprint-application-by-class) ต่อชุดสำหรับ **รอยเท้าทางนิเวศ** หมวดย่อยนี้แสดงว่าหมายความอย่างไรสำหรับ **ชนิดข้อมูลและการปฏิบัติ** — ชนิดใดอยู่ในขอบเขต สิ่งที่การรับรองต้องตรวจ และสิ่งที่ต้องปรากฏบนบันทึก CS-2 ยังเป็นเจ้าของกฎชนิด; การเดินดูเหล่านี้ไม่เพิ่มชนิดและไม่ทำให้ CS-2 แคบลง*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ชั้นควบคุมการบำบัดและจ่ายที่เป็นของเมืองรับข้อมูลความดัน การไหล การเตือนการปนเปื้อน และคำสั่งวาล์วแบบเวลาจริง; เก็บข้อมูลเชื่อมบริการลูกค้าจำนวนจำกัดเพื่อแจ้งเหตุขัดข้อง; และมอบการเฝ้าให้ศูนย์ปฏิบัติการความมั่นคง (**SOC**) ของผู้ขาย

- **ชนิดข้อมูลในขอบเขต:**
  - **เทเลเมทรี** ปฏิบัติการที่วิกฤตต่อความปลอดภัย (สัญญาณวัดและคำสั่งสดจากภาคสนาม);
  - สัญญาณเตือนการปนเปื้อนและคุณภาพ;
  - ข้อมูลติดต่อแจ้งเหตุขัดข้อง;
  - บันทึกการเข้าถึงของผู้ขายและผู้ดำเนินการ;
  - บันทึกเหตุการณ์และบำรุงรักษา
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าข้อมูลระนาบควบคุมที่วิกฤตต่อความปลอดภัยถูกแยกจากท่อบริการลูกค้า การเรียกเก็บ หรือการวิเคราะห์ ภายใต้การจำแนก CS-3 **ที่เข้มงวดที่สุดที่ใช้ได้** หรือไม่;
  - ว่าการรวม การมอบให้ผู้ขาย หรือเส้นทางสำรองอาจทำให้การแยกนั้นพังภายใต้ความกดดันหรือเงื่อนไขเชิงปรปักษ์หรือไม่;
  - ว่าการระบุผู้กระทำยืนนานพอที่จะสอบสวนเหตุปนเปื้อนหรือตัดน้ำได้หรือไม่; และ
  - ว่าขีดจำกัดการตรวจที่มีเหตุด้านความปลอดภัยมีการแทนที่สาธารณะที่จัดทำเอกสารหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - สารบบชนิดเต็มสำหรับขอบเขตที่รับรอง;
  - เหตุผลการจำแนกในที่ที่เทเลเมทรี การเตือน หรือข้อมูลติดต่ออาจเป็นหลายชนิด;
  - การควบคุมการแยกและการเชื่อมข้ามโดเมน;
  - ท่าทีการรักษาและวงชีวิตสำหรับการสร้างเหตุการณ์ใหม่;
  - ข้อค้นพบการประกันโครงสร้างพื้นฐานสำหรับสำรอง กู้คืน และการกู้เชิงปรปักษ์ที่ความลึก **Class A**; และ
  - เงื่อนไขใดที่ผูกกับการมอบให้ผู้ขายหรือช่องว่างการเฝ้า

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพจัดเส้นทางสรุปคลินิก ตัวชี้ภาพ และโทเค็นการคลี่อัตลักษณ์ระหว่างโรงพยาบาล คลินิก และระบบคุณสมบัติที่อยู่ติดสิทธิประโยชน์; โรงพยาบาลพึ่งมันทุกวันแต่ถอยไปแฟกซ์ พอร์ทัลตรง หรือการดึงด้วยมือได้ภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด

- **ชนิดข้อมูลในขอบเขต:**
  - บันทึกคลินิกและการวินิจฉัย;
  - โทเค็นการคลี่อัตลักษณ์และหลักฐาน;
  - ข้อมูลสารบบผู้ให้บริการและสถานที่;
  - บันทึกการตรวจการเข้าถึงและการเปิดเผย;
  - สิ่งที่ได้จากการจับคู่หรือการกำจัดซ้ำ
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าข้อมูลคลินิกคงอยู่ภายใต้ชั้นการปฏิบัติที่เข้มงวดที่สุดที่ใช้ได้ ข้ามการจัดเส้นทาง แคช การกำจัดซ้ำ และการเชื่อมปลายทางหรือไม่;
  - ว่าตรรกะการคลี่อัตลักษณ์สร้างการเชื่อมข้ามโดเมนที่ไม่ปลอดภัยหรือการเปิดเผยโดยตัวแทนหรือไม่;
  - ว่าสายการมอบของผู้ดำเนินการและผู้ร่วมยังระบุผู้กระทำได้หรือไม่; และ
  - ว่าเส้นทางความสามารถย้ายและการออกคงการควบคุมของผู้ป่วยโดยไม่เอาชนะการกู้ดำเนินงานหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ชนิดที่เป็นสาระและเหตุผลชนิดคลุมเครือ;
  - การแยกระหว่างเพย์โหลดคลินิก เมทาดาทาสารบบ และฟีดที่อยู่ติดคุณสมบัติ;
  - การระบุผู้กระทำของสายการมอบ;
  - ท่าทีวงชีวิตและการรักษาที่พอต่อการสอบสวนและการโต้แย้งด้านการดูแลสุขภาพ;
  - ข้อค้นพบการประกันโครงสร้างพื้นฐานที่ความลึกดำเนินงาน **Class B**; และ
  - ตัวกระตุ้นการเปิดใหม่หากเหตุขัดข้องหรือความล้มเหลวการปฏิบัติข้อมูลจะกั้นการดูแลภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรประสานกะเจ้าหน้าที่ การจองห้อง และนัดผู้ขายข้ามโรงพยาบาล โรงเรียน และหน่วยงานสาธารณะ; โรงพยาบาลหลักและสาธารณูปโภคยังเดินในโหมดเสื่อมได้หากมันล้ม แต่แพลตฟอร์มจัดรูปการประสานในขนาด และอาจถือเมทาดาทาติดต่อ บทบาท และตำแหน่งหยาบ

- **ชนิดข้อมูลในขอบเขต:**
  - ข้อมูลตาราง บทบาท และการจัดสรรทรัพยากร;
  - เมทาดาทาติดต่อและหลักฐานของผู้ร่วม;
  - ตัวระบุตำแหน่งหยาบหรือสถานที่;
  - บันทึกการตรวจของแพลตฟอร์ม;
  - ผลจัดอันดับหรือจับคู่ที่ได้ในที่ที่ใช้
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าระบบระบุชนิดที่เป็นสาระอย่างซื่อ — รวมผลที่ได้ที่อาจเปิดลักษณะที่คุ้มครองผ่านแบบตารางหรือไม่;
  - ว่าการเชื่อมข้ามองค์กรคงอยู่ในขอบเขตที่มีเหตุหรือไม่;
  - ว่าการปฏิบัติยังโต้แย้งได้ในที่ที่ความกระจุกอาจบอกล่วงหน้าการยกระดับจุดคอขวดหรือไม่; และ
  - ว่าป้ายชั้นต่ำกว่ายังเข้ากันได้หากการพึ่งหรือความอ่อนไหวของข้อมูลแข็งขึ้นหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ชนิดที่อยู่ในขอบเขตอย่างเป็นสาระและเหตุผลหลายชนิดใด;
  - ข้อค้นพบการเชื่อมและการรักษาตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบการประกันโครงสร้างพื้นฐานในที่ที่เป็นสาระ — ไม่ใช่เชิงพิธี — สำหรับข้อมูลที่ถือจริง;
  - การระบุผู้กระทำที่โต้แย้งได้สำหรับการเชื่อมที่ผลักภาระ; และ
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่แพลตฟอร์มกลายเป็นประตูโดยพฤตินัยสู่การเข้าถึงที่จำเป็นต่อการอยู่รอด หรือเริ่มบรรทุกเพย์โหลดระดับคลินิก

**การอ่านข้ามชั้น.** กฎ CS-3 ชุดเดียวกันใช้กับทั้งสามระบบ; ชั้นเปลี่ยน **ความลึก** ไม่ใช่อนุญาตให้ปฏิบัติข้อมูลผิด แพลตฟอร์ม **Class C** ที่เริ่มเก็บหรือจัดเส้นทางบันทึกระดับคลินิกต้องถูกประเมินและบันทึกเช่นนั้น — ไม่ทิ้งไว้ที่การปฏิบัติแบบแพลตฟอร์มประสานเพราะผู้ดำเนินการชอบแฟ้มที่เบากว่า การแลก **Class B** ที่เหตุขัดข้องจะกั้นการดูแลฉุกเฉินภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว ต้องถูกจำแนกใหม่และรับรองใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) โดยประกันการปฏิบัติข้อมูลปรับตามนั้น

<a id="5-ecological-footprint-evaluation"></a>

### 5. การประเมินรอยเท้าทางนิเวศ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดความต่อเนื่อง (*รอยเท้าทางนิเวศในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*); [รอยเท้าทางนิเวศ](core_05_band_continuity.md#ecological-footprint), [ผลกระทบที่เป็นสาระ](core_05_band_oversight.md#material-impact), [การพึ่งพา](core_05_band_continuity.md#dependency), [ความโปร่งใส](core_05_band_oversight.md#transparency), และ [ความครบถ้วนทางญาณ](core_05_band_oversight.md#epistemic-integrity) (บทที่ห้า); [เงื่อนไขเบื้องต้นทางสิ่งแวดล้อม](core_05_band_continuity.md#environmental-preconditions-constitutional) และ [ความครบถ้วนทางนิเวศ](core_05_band_continuity.md#ecological-integrity-constitutional) ในที่ที่ถูกพาดพิงเป็นสาระ.
- ปลายทาง: [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*การเดินดูตัวอย่างรอยเท้าทางนิเวศ*); [§6](#6-proportionate-cross-system-support-evaluation) และ [§6.1](#61-illustrative-cross-system-support-application-by-class) (*การประเมินการสนับสนุนข้ามระบบและการเดินดูตัวอย่าง*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*การแสดงรอยเท้าผิดและความไม่สอดคล้อง*).
- อ่านคู่กับ: [corpus_systems.md](../../corpus_systems.md), [CS-8 — ความยั่งยืนแบบปรับตัวและความยืดหยุ่นของระบบนิเวศ](../../corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md) ในที่ที่การจัดสรรแบบปรับตัวหรือการพึ่งกันของระบบนิเวศอยู่ในขอบเขตอย่างเป็นสาระ.
- หมวดย่อย: [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*ตัวอย่างการประยุกต์รอยเท้าทางนิเวศตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: การรับรองต้องประเมินภาระสิ่งแวดล้อมที่ระบุผู้รับผิดได้อย่างซื่อเมื่อมันสำคัญ — รวมลิงก์ต้นทางและปลายทาง — ไม่ใช่แค่ว่าผู้ดำเนินการอ้างว่าระบบเป็นมิตรสิ่งแวดล้อม วิธีบัญชีรอยเท้าและเป้าลดตัวเลขอยู่ในตราสารอื่น; การรับรองตรวจว่าการระบุ การเปิดเผย และการเปรียบถูกประเมินจริงในที่ที่เป็นสาระ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§5.1](#51-illustrative-ecological-footprint-application-by-class).*

การรับรองความสอดคล้องของระบบต้องประเมิน **รอยเท้าทางนิเวศ** เป็นส่วนของบันทึกการรับรองที่มีผลกระทบที่เป็นสาระทุกฉบับ ในที่ที่ภาระสิ่งแวดล้อมที่ระบุผู้รับผิดได้เป็นสาระภายใต้ [รอยเท้าทางนิเวศ](core_05_band_continuity.md#ecological-footprint) และ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) กฎการระบุ วงชีวิต การพึ่งพา และความโปร่งใสฉบับหลักอยู่ในบทที่ห้าและ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*); วิธีบัญชี ขั้นการตรวจสอบ และเป้าตัวเลขอยู่ในตราสารการรับเอามาใช้ในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไกบัญชีรอยเท้าและไม่กำหนดหน้าที่ลดเกินสิ่งที่ตราสารอื่นขอ

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่ากระแสสิ่งแวดล้อมที่ระบุผู้รับผิดได้ — พลังงาน วัสดุ การปล่อย การใช้ที่ดิน และภาระที่เกี่ยวข้อง — ถูกระบุข้ามวงชีวิตที่เกี่ยวข้องอย่างเป็นสาระของระบบและความสัมพันธ์ [การพึ่งพา](core_05_band_continuity.md#dependency) ถูกประเมินภายใต้ [ผลกระทบที่เป็นสาระ](core_05_band_oversight.md#material-impact) และถูกเปิดเผยหรือกักเฉพาะเท่าที่ [ความโปร่งใส](core_05_band_oversight.md#transparency) [ความครบถ้วนทางญาณ](core_05_band_oversight.md#epistemic-integrity) และหน้าที่ความโปร่งใสที่ใช้ได้ยินยอม การประเมินต้องสะท้อนผลเชิงหน้าที่และขอบเขตระบบ ไม่ใช่ขอบเขตในนาม ป้ายการตลาด หรือกรอบวงชีวิตบางส่วนเพียงอย่างเดียว

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวขอบเขตการประเมินรอยเท้า ข้อสมมติการระบุ ขอบวงชีวิตและการพึ่งพาที่พึ่ง ภาระที่เป็นสาระที่ระบุ ความไม่แน่นอน ท่าทีการเปิดเผย ข้อค้นพบส่วนประกอบเวทีสิ่งแวดล้อมในที่ที่ถูกขอ และขีดจำกัดการเปิดเผยรอยเท้าที่มีเหตุ พร้อมการแทนที่สาธารณะในที่ที่กฎความโปร่งใสที่ใช้ได้ขอ

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินรอยเท้าและการเปิดเผยต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าภาระสิ่งแวดล้อมที่เป็นสาระถูกระบุ ถูกเปรียบข้ามทางเลือกที่เกี่ยวข้องในที่ที่ทำได้ และไม่ถูกบังด้วยการเลื่อนขอบ การผลักการพึ่ง หรือการเปิดเผยแบบเลือก

**ข้อบกพร่องและความไม่สอดคล้อง.** การบัง การแสดงผิด การแยกชิ้น หรือการผลักข้อมูลรอยเท้าที่เป็นสาระในที่ที่การรับรองหรือหน้าที่ความโปร่งใสของ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) ขอการเปิดเผย; การประเมินเฉพาะชิ้นวงชีวิตที่ผู้ดำเนินการเลือกในที่ที่การระบุที่กว้างกว่าเป็นสาระ; หรือการถือคำอ้างรอยเท้าว่าครบด้วยคำกล่าวโดยไม่มีหลักฐานที่ประเมินได้ ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="51-illustrative-ecological-footprint-application-by-class"></a>

<a id="51-illustrative-ecological-footprint-application-by-class-non-exhaustive"></a>
#### 5.1 ตัวอย่างการประยุกต์รอยเท้าทางนิเวศตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) และ [§4.1](#41-illustrative-data-handling-application-by-class) พาสามระบบเดียวกันผ่านการทบทวนทั้งระบบและการปฏิบัติข้อมูล หมวดย่อยนี้แสดงว่าการประเมิน **รอยเท้าทางนิเวศ** หมายความอย่างไรสำหรับแต่ละระบบ — ภาระสิ่งแวดล้อมใดนับ สิ่งที่การรับรองต้องตรวจ และสิ่งที่ต้องปรากฏบนบันทึก **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) และบทที่ห้ายังเป็นเจ้าของกฎการระบุและความโปร่งใส; วิธีบัญชีและเป้าตัวเลขอยู่ในตราสารอื่น; การเดินดูเหล่านี้ไม่เพิ่มหน้าที่รอยเท้าเกินสิ่งที่ตราสารเหล่านั้นขอ*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองดึงจากแหล่งลุ่มน้ำ ปัจจัยเคมีบำบัด พลังงานสูบและบำบัด โครงสร้างจ่าย กระแสทิ้ง และการคำนวณหรือเฝ้าของผู้ขายที่มอบในที่ที่ใช้

- **ภาระที่ระบุผู้รับผิดได้ในขอบเขต:**
  - การดึงน้ำต้นทางและความเครียดลุ่มน้ำ;
  - สารเคมีบำบัดและสื่อกรอง;
  - พลังงานสูบ บำบัด และจ่าย;
  - โครงสร้างที่ฝังตัวสำหรับโรงงาน ท่อ และควบคุม;
  - การสูญเสียและรั่วของน้ำที่บำบัดแล้ว;
  - การทิ้งและกากสู่แหล่งรับ;
  - การปล่อยของโครงข่ายไฟฟ้าต้นทาง;
  - ศูนย์ปฏิบัติการความมั่นคง (**SOC**) ของผู้ขาย การคำนวณโฮสต์ร่วม หรือการคำนวณและเชื่อมต่อเฝ้าระยะไกลในที่ที่พึ่งอย่างเป็นสาระ;
  - ภาระบำรุง แทนที่ และปลดระวางข้ามวงชีวิตที่เกี่ยวข้องอย่างเป็นสาระ
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าขอบเขตรอยเท้าครอบไฟฟ้าต้นทาง อุปทานเคมี [การพึ่งพา](core_05_band_continuity.md#dependency) ลุ่มน้ำ และการทิ้งปลายทาง — ไม่ใช่เฉพาะอาคารดำเนินงานของเทศบาลหรือไม่;
  - ว่า [ผลกระทบที่เป็นสาระ](core_05_band_oversight.md#material-impact) ถูกประเมินสำหรับการหมดแหล่ง ความเข้มพลังงาน และการทิ้งภายใต้ความกดดันหรือความแปรปรวนภูมิอากาศหรือไม่;
  - ว่าขอบที่ผู้ดำเนินการเลือกตัดการเฝ้าที่ผู้ขายโฮสต์ โลจิสติกส์เคมีที่จ้างนอก หรือภาระโครงข่ายร่วมในที่ที่การระบุเป็นสาระหรือไม่;
  - ว่าทางเลือก — การอนุรักษ์ การคุ้มครองแหล่ง เส้นทางบำบัดภาระต่ำกว่า — ถูกเปรียบในที่ที่ทำได้หรือไม่; และ
  - ว่าขีดจำกัดการเปิดเผยมีการแทนที่สาธารณะที่จัดทำเอกสารภายใต้ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) หรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ขอบเขตการประเมินรอยเท้าและขอบวงชีวิตที่ความลึก **Class A**;
  - ข้อสมมติการระบุสำหรับกระแสลุ่มน้ำ พลังงาน เคมี และการทิ้ง;
  - ภาระที่เป็นสาระที่ระบุและความไม่แน่นอนที่กล่าว;
  - ข้อค้นพบส่วนประกอบเวทีสิ่งแวดล้อมในที่ที่ถูกขอ;
  - ข้อค้นพบการเปรียบข้ามทางเลือกที่เกี่ยวข้องในที่ที่ทำได้;
  - ท่าทีการเปิดเผยและขีดจำกัดที่มีเหตุพร้อมการแทนที่สาธารณะใด; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับความเครียดแหล่ง ภัยจากการทิ้ง หรือการเลื่อนขอบ

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพพึ่งโฮสต์ที่ทำซ้ำ การเชื่อมต่อสถานที่โรงพยาบาล การคำนวณคลี่อัตลักษณ์ และโครงสร้างพื้นฐานที่ผู้ขายหรือผู้ร่วมดำเนิน ข้ามเครือข่ายการดูแลระดับภูมิภาค

- **ภาระที่ระบุผู้รับผิดได้ในขอบเขต:**
  - พลังงาน ทำความเย็น และวงชีวิตฮาร์ดแวร์ของศูนย์ข้อมูลหลักและสำรอง;
  - การเชื่อมต่อเครือข่ายและขอบสำหรับโรงพยาบาลผู้ร่วม;
  - การคำนวณทำซ้ำที่เก็บและการกำจัดซ้ำ;
  - โครงสร้างนายหน้าอัตลักษณ์และจัดเส้นทาง;
  - ภาระสถานที่ ณ จุดโฮสต์ที่พึ่งอย่างเป็นสาระ;
  - โครงสร้างที่ฝังตัวสำหรับตัวเชื่อมในสถานที่ในที่ที่โรงพยาบาลพึ่งพวกมัน
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าการระบุรอยเท้าครอบภาระโฮสต์ การทำซ้ำ และการเชื่อมผู้ร่วมที่ขนาดดำเนินงาน — ไม่ใช่เฉพาะสำนักงานใหญ่ของผู้ดำเนินการแลกหรือไม่;
  - ว่าการพึ่งภูมิภาคโฮสต์ร่วม ผู้ให้บริการโคโลเคชัน หรือฮาร์ดแวร์ขอบสถานที่โรงพยาบาลถูกทำแผนที่และระบุหรือไม่;
  - ว่าชิ้นวงชีวิตไม่ถูกทำให้แคบเป็นคำอ้างซอฟต์แวร์อย่างเดียวขณะที่ภาระฮาร์ดแวร์และพลังงานที่เป็นสาระถูกผลักหรือไม่;
  - ว่าภาระที่เป็นสาระถูกประเมินภายใต้ [ผลกระทบที่เป็นสาระ](core_05_band_oversight.md#material-impact) และเปิดเผยสอดคล้องกับ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) หรือไม่; และ
  - ว่าการเติบโตของปริมาณผู้ร่วมหรือความอ่อนไหวของข้อมูลจะเปลี่ยนภาระที่ระบุอย่างเป็นสาระหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ขอบเขตรอยเท้าและขอบการพึ่งที่ความลึกดำเนินงาน **Class B**;
  - ภาระพลังงาน ฮาร์ดแวร์ และการเชื่อมต่อที่เป็นสาระที่ระบุ;
  - ข้อสมมติการระบุโฮสต์และการมอบ;
  - ความไม่แน่นอนและท่าทีการเปิดเผย;
  - ข้อค้นพบเวทีสิ่งแวดล้อมหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากขนาด การเติบโตของเพย์โหลดระดับคลินิก หรือความกระจุกของโฮสต์เปลี่ยนภาระที่ระบุผู้รับผิดได้หรือท่าทีชั้นอย่างเป็นสาระ

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรวิ่งหลักบนการคำนวณโฮสต์ร่วมและการเชื่อมต่อ โดยมีภาระรองจากโลจิสติกส์สถานที่ การเดินทางที่แบบประสานชักนำ และโฮสต์ภูมิภาคที่กระจุกในที่ที่ใช้ได้

- **ภาระที่ระบุผู้รับผิดได้ในขอบเขต:**
  - การคำนวณโฮสต์ ที่เก็บ และเครือข่ายสำหรับงานตาราง;
  - พลังงานศูนย์ข้อมูลหลายผู้เช่าที่ระบุได้ไปยังส่วนแบ่งของแพลตฟอร์ม;
  - วงชีวิตฮาร์ดแวร์ที่ฝังตัวสำหรับโครงสร้างที่พึ่งอย่างเป็นสาระ;
  - ภาระสถานที่และโลจิสติกส์เฉพาะในที่ที่แบบประสานเลื่อนการเดินทางหรือการใช้สถานที่อย่างเป็นสาระ;
  - ผลความกระจุกระดับภูมิภาคในที่ที่โฮสต์หรือการใช้รวมตัวในที่ภาระสูง
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าผู้ดำเนินการระบุภาระการคำนวณโฮสต์และการเชื่อมต่ออย่างซื่อ แทนที่จะถือแพลตฟอร์มว่าไม่เป็นสาระเพราะเป็น «แค่ซอฟต์แวร์» หรือไม่;
  - ว่าการผลักหลายผู้เช่าหรือการเลื่อนขอบผู้ขายซ่อนการระบุพลังงานหรือฮาร์ดแวร์ที่เป็นสาระหรือไม่;
  - ว่าความกระจุกในภูมิภาคหรือผู้ให้บริการเฉพาะถูกประเมินในที่ที่มันเลื่อนภาระอย่างเป็นสาระหรือไม่;
  - ว่าการทบทวนรอยเท้าคงตามสัดส่วนโดยไม่กลายเป็นเชิงพิธีสำหรับระบบ **Class C** หรือไม่; และ
  - ว่าการจำแนกใหม่สมควรหรือไม่หากขนาด การจัดเส้นทางที่จำเป็นต่อการอยู่รอด หรือการเติบโตของเพย์โหลดระดับคลินิกจะขอความลึกรอยเท้า **Class B** หรือ **Class A**
- **สิ่งที่บันทึกต้องแสดง:**
  - ข้อค้นพบรอยเท้าตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ขอบเขตและข้อสมมติการระบุสำหรับการคำนวณ ที่เก็บ และการเชื่อมต่อ;
  - ภาระที่เป็นสาระที่ระบุโดยไม่ทำให้ขอบวงชีวิตแคบเกิน;
  - ความไม่แน่นอนและท่าทีการเปิดเผย;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่ความกระจุกของโฮสต์ ขนาด หรือความอ่อนไหวของเพย์โหลดแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนรอยเท้าที่ยกระดับหากชั้นหรือความเป็นสาระเปลี่ยน

**การอ่านข้ามชั้น.** วินัยรอยเท้าของ **มาตรา I-B** (*รอยเท้าทางนิเวศและความโปร่งใส*) และบทที่ห้าชุดเดียวกันใช้กับทั้งสามระบบ; ชั้นเปลี่ยนความลึกของการระบุและภาระการเปรียบ ไม่ใช่อนุญาตให้บังกระแสสิ่งแวดล้อมที่เป็นสาระ ระบบน้ำวิกฤตต่อการอยู่รอด **Class A** ต้องไม่ถูกลดชั้นขณะที่การดึงลุ่มน้ำ การทิ้ง หรือภาระพลังงานที่กั้นน้ำปลอดภัยยังถูกระบุต่ำอย่างเป็นสาระ การแลก **Class B** ที่การเติบโตของเพย์โหลดคลินิกหรือความกระจุกของโฮสต์เพิ่มภาระสิ่งแวดล้อมอย่างเป็นสาระ ต้องได้รับการทบทวนรอยเท้าที่ปรับตามการเติบโตนั้น — รวมขึ้นสู่ความลึก **Class A** ในที่ที่การส่งมอบที่จำเป็นต่อการอยู่รอดและภาระระบบต้นทางถูกพาดพิงร่วม แพลตฟอร์มตาราง **Class C** ที่กลายเป็นจุดคอขวดโดยพฤตินัยของการประสานที่จำเป็นต่อการอยู่รอด ต้องไม่คงแฟ้มรอยเท้าเชิงพิธีเพราะผู้ดำเนินการติดป้ายว่าไม่วิกฤต การเดินดูการสนับสนุนข้ามระบบสำหรับระบบเดียวกันอยู่ใน [§6.1](#61-illustrative-cross-system-support-application-by-class)

<a id="6-proportionate-cross-system-support-evaluation"></a>

<a id="6-proportionate-cross-system-contribution-evaluation"></a>
### 6. การประเมินการสนับสนุนข้ามระบบตามสัดส่วน

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดความต่อเนื่อง (*การสนับสนุนข้ามระบบตามสัดส่วนในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) และ **มาตรา IV-B** (*ความเป็นธรรมข้ามระบบและความยั่งยืน*); [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), [การพึ่งพา](core_05_band_continuity.md#dependency), [ความเป็นธรรมเชิงสาระ](core_05_band_participation.md#substantive-fairness-constitutional), [สัดส่วน](core_05_band_accountability.md#proportionality), [รอยเท้าทางนิเวศ](core_05_band_continuity.md#ecological-footprint), และ [ความยั่งยืน](core_05_band_continuity.md#sustainability) (บทที่ห้า).
- ปลายทาง: [§6.1](#61-illustrative-cross-system-support-application-by-class) (*การเดินดูตัวอย่างการสนับสนุนข้ามระบบ*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*การแสดงกระแสทรัพยากรผิด ความไม่สอดคล้องของการสกัด และความไม่พอของการสนับสนุน*).
- อ่านคู่กับ: **[corpus_systems.md](../../corpus_systems.md)**, **CS-9** (*การจัดสรรทรัพยากรและการบริหารอย่างรับผิดชอบทางทุน*), และ **CS-8** (*ความยั่งยืนแบบปรับตัวและความยืดหยุ่นของระบบนิเวศ*); [*สถาปัตยกรรมการปกครอง การกำกับดูแล การพึ่งพา การกระจายอำนาจ ความกระจุก โครงสร้างตลาด และความครบถ้วนของเส้นทางออก*](core_05_band_accountability.md#governance-architecture-oversight-decentralization-and-concentration-cluster) ในที่ที่ความกระจุก การพึ่งพา หรือการจัดเส้นทางสิ่งจูงใจตัดกับ **มาตรา IV-B** (*ความเป็นธรรมข้ามระบบและความยั่งยืน*).
- หมวดย่อย: [§6.1](#61-illustrative-cross-system-support-application-by-class) (*ตัวอย่างการประยุกต์การสนับสนุนข้ามระบบตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: เมื่อระบบดึงจากฐานร่วมอย่างเป็นสาระ การรับรองต้องตรวจว่ามันใส่การสนับสนุนที่ตามรอยได้กลับพอหรือไม่ — ไม่ใช่ว่าผู้ดำเนินการกล่าวว่าบัญชีสมดุล สูตรจัดสรรและเป้าตัวเลขอยู่ในตราสารอื่น; การรับรองตรวจว่าแผนที่การพึ่ง กระแสคืน และความเป็นธรรมข้ามระบบถูกประเมินจริงในที่ที่ตัวกระตุ้นใช้ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§6.1](#61-illustrative-cross-system-support-application-by-class).*

**ตัวกระตุ้นความเป็นสาระ.** หมวดนี้ใช้ในที่ที่ระบบที่มีผลกระทบที่เป็นสาระจัดสรร จัดเส้นทาง ให้ทุน หรือสกัดจากโครงสร้างพื้นฐานร่วมหรือการพึ่งพื้นฐานที่ระบบอื่นหรือผู้มีความรู้สึกพึ่ง อย่างเป็นสาระ มันไม่ขอการตรวจการสนับสนุนข้ามระบบเต็มบนบันทึกการรับรองทุกฉบับ

**ความหมายของ «การสกัด» ที่นี่.** ใน **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) และหมวดนี้ **การสกัด** หมายถึงการดึง **เงิน ค่าธรรมเนียม ทุนสาธารณะ การคำนวณ การเชื่อมต่อ แรงงานบำรุง ความสามารถแหล่ง หรือกระแสทรัพยากรร่วมอื่น** จากโครงสร้างพื้นฐานหรือการพึ่งที่ระบบอื่นก็ต้องการ — โดยไม่คืนการสนับสนุนตามสัดส่วนเพื่อให้ฐานร่วมนั้นทำงานต่อไป คำถามคือ **ใครได้ประโยชน์จากส่วนหลังร่วมและใครจ่ายเพื่อค้ำจุนมัน** ไม่ใช่ว่าระบบคัดลอก ขาย หรือโฆษณาทวนเนื้อหาบันทึก การเข้าถึงบันทึกคลินิก การใช้ข้อมูลส่วนบุคคล การขายให้ฝ่ายนอก การโฆษณาเจาะจง และการทำโปรไฟล์บุคคลที่สามที่ไม่เกี่ยว ถูกประเมินภายใต้ [§4](#4-data-types-and-handling-evaluation) และการคุ้มครองความเป็นส่วนตัวและวงข้อมูลของบทที่หก — ไม่ใช่ภายใต้หมวดนี้

การรับรองความสอดคล้องของระบบต้องประเมิน **การสนับสนุนข้ามระบบตามสัดส่วน** ภายใต้ [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) และ **มาตรา IV-B** (*ความเป็นธรรมข้ามระบบและความยั่งยืน*) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้ ความหมายฉบับหลัก ปัจจัยประเมิน และวินัยการไม่ปฏิบัติตามอยู่ในบทที่ห้าและ **มาตรา IV-B** (*ความเป็นธรรมข้ามระบบและความยั่งยืน*); หมวดจัดสรร กลไกการให้อำนาจใหม่ และเป้าตัวเลขอยู่ใน **[corpus_systems.md](../../corpus_systems.md)** **CS-9** และ **CS-8** ในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไก CS-8 หรือ CS-9 และไม่กำหนดการแบ่งเท่า ร้อยละคงที่ หรือแบบจำลองทุนเดียว

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าแผนที่ระบบที่พึ่งที่จัดทำเอกสารและบันทึกกระแสทรัพยากรที่ตรวจได้ภายใต้ **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) แสดงการสกัดจากโครงสร้างพื้นฐานร่วมหรือการพึ่งพื้นฐานหรือไม่ และกระแสคืนถึงความพอที่เป็นสาระภายใต้ [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) หรือไม่ ประเมินภายใต้ [ความเป็นธรรมเชิงสาระ](core_05_band_participation.md#substantive-fairness-constitutional) และ [สัดส่วน](core_05_band_accountability.md#proportionality) และปรับตามความสำคัญ ความไม่สมมาตรของการพึ่ง ความสามารถแทนที่ [รอยเท้าทางนิเวศ](core_05_band_continuity.md#ecological-footprint) ในที่ที่เป็นสาระ และ [ความยั่งยืน](core_05_band_continuity.md#sustainability) ระยะยาว การประเมินต้องสะท้อนผลเชิงหน้าที่และกระแสที่จัดทำเอกสาร ไม่ใช่ป้ายในนาม การโอนครั้งเดียว หรือคำกล่าวนอกแผนที่เพียงอย่างเดียว

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวตัวกระตุ้นความเป็นสาระของ **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) ที่พึ่ง ขอบเขตการประเมินแผนที่ระบบที่พึ่งและกระแสทรัพยากร ข้อค้นพบการสกัดและกระแสคืน ข้อค้นพบความพอของการสนับสนุนภายใต้ [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) ความไม่แน่นอน ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบที่กำหนดอื่นในที่ที่ถูกขอ และเงื่อนไข ขีดจำกัดการพึ่ง หรือตัวกระตุ้นการเปิดใหม่ใดที่ผูกกับความไม่สมดุลที่ยืน

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินการสนับสนุนข้ามระบบต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าที่บริหารโครงสร้างพื้นฐานร่วมหรือการพึ่งพื้นฐานอย่างเป็นสาระต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าการสกัด กระแสคืน และความพอของการสนับสนุนถูกประเมิน ไม่ใช่แค่กล่าว

**ข้อบกพร่องและความไม่สอดคล้อง.** การบัง การแสดงผิด การแยกชิ้น หรือการผลักข้อมูลการพึ่งหรือกระแสทรัพยากรที่เป็นสาระในที่ที่ **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) ขอการเปิดเผย; การถือการโอนเชิงสัญลักษณ์ ทึบ หรือครั้งเดียวว่าสนอง [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional); การสกัดยืนโดยไม่มีคืนตามสัดส่วนในที่ที่ตัวกระตุ้นความเป็นสาระใช้; หรือการรับรองการพึ่งต่อเนื่องขณะที่ความไม่พอของการสนับสนุนที่จัดทำเอกสารคุกคามความสอดคล้องทางรัฐธรรมนูญอย่างเป็นสาระ ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="61-illustrative-cross-system-support-application-by-class"></a>

<a id="61-illustrative-cross-system-support-application-by-class-non-exhaustive"></a>
#### 6.1 ตัวอย่างการประยุกต์การสนับสนุนข้ามระบบตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) ถึง [§5.1](#51-illustrative-ecological-footprint-application-by-class) พาสามระบบเดียวกันผ่านโดเมนประเมินก่อนหน้า หมวดย่อยนี้แสดงว่า **การสนับสนุนข้ามระบบตามสัดส่วน** หมายความอย่างไรสำหรับแต่ละระบบ — การพึ่งร่วมใดนับ สิ่งที่การรับรองต้องตรวจเมื่อตัวกระตุ้นความเป็นสาระของ **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) ใช้ และสิ่งที่ต้องปรากฏบนบันทึก **การสกัด** ที่นี่หมายถึง **การดึงทรัพยากรและทุนจากโครงสร้างพื้นฐานร่วม** (ดู [§6](#6-proportionate-cross-system-support-evaluation) *ความหมายของ «การสกัด» ที่นี่*) — ไม่ใช่การคัดลอกข้อมูลคลินิก การใช้โฆษณา หรือการขายที่ไม่เกี่ยวให้บุคคลที่สาม CS-8, CS-9 และบทที่ห้ายังเป็นเจ้าของกลไกจัดสรร; การเดินดูเหล่านี้ไม่กำหนดการแบ่ง สูตร หรือแบบจำลองทุน*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองดึงจากลุ่มน้ำหรือชั้นน้ำร่วม การเชื่อมต่อไฟฟ้าปริมาณมากระดับภูมิภาค สายอุปทานเคมีและกรองขายส่ง ข้อตกลงเชื่อมฉุกเฉินร่วม และบริการเฝ้าหรือควบคุมที่ผู้ขายดำเนิน ซึ่งสาธารณูปโภคหรือชุมชนอื่นอาจพึ่งด้วย

- **การพึ่งพาและกระแสในขอบเขต:**
  - สิทธิแหล่งน้ำและโครงสร้างลุ่มน้ำที่ร่วมกับเกษตร อุตสาหกรรม และเทศบาลข้างเคียง;
  - การเชื่อมต่อโครงข่ายและภาระโหลดสูงสุดบนโครงสร้างไฟฟ้าภูมิภาค;
  - ทางเดินจัดซื้อเคมีและโลจิสติกส์ร่วม;
  - ข้อตกลงสูบช่วยกัน การเชื่อมต่อ และอุปทานฉุกเฉิน;
  - บริการ **SCADA** (การควบคุมกำกับและเก็บข้อมูล — การดำเนินงานระยะไกลของปั๊ม วาล์ว และอุปกรณ์บำบัด) **เทเลเมทรี** (สัญญาณความดัน การไหล และการเตือนสดจากเซ็นเซอร์ภาคสนาม) และ **SOC** (ศูนย์ปฏิบัติการความมั่นคง — การเฝ้าของผู้ขายสำหรับบุกรุก เหตุขัดข้อง และเหตุความปลอดภัย) ที่โฮสต์บนโครงสร้างควบคุมร่วมของผู้ขายหรือภูมิภาค;
  - กระแสทุนและบำรุงจากผู้จ่ายอัตรา พันธบัตร ทุนอุดหนุน หรืออำนาจภูมิภาค กลับสู่การคุ้มครองแหล่ง การต่อท่อใหม่ และการบำรุงกระดูกสันหลังร่วม
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าแผนที่ระบบที่พึ่งและบันทึกกระแสทรัพยากรที่ตรวจได้ของ **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) ระบุการสกัดจากลุ่มน้ำร่วม โครงข่าย สายอุปทาน และกระดูกสันหลังช่วยกัน — ไม่ใช่เฉพาะสมุดบัญชีภายในของสาธารณูปโภคหรือไม่;
  - ว่ากระแสคืน — การคุ้มครองแหล่ง การต่อโครงสร้างใหม่ การฟื้นลุ่มน้ำ ความสามารถฉุกเฉินภูมิภาค และการแบ่งต้นทุนที่เป็นธรรมสำหรับการใช้กระดูกสันหลังร่วม — ถึงความพอที่เป็นสาระภายใต้ [การสนับสนุนข้ามระบบตามสัดส่วน](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) ประเมินภายใต้ [ความเป็นธรรมเชิงสาระ](core_05_band_participation.md#substantive-fairness-constitutional) และ [สัดส่วน](core_05_band_accountability.md#proportionality) หรือไม่;
  - ว่าทุนอุดหนุนครั้งเดียว ค่าธรรมเนียมผู้ขายที่ทึบ หรือการผลักต้นทุนปลายทางถูกถือเป็นคืนที่พอหรือไม่;
  - ว่า [รอยเท้าทางนิเวศ](core_05_band_continuity.md#ecological-footprint) และ [ความยั่งยืน](core_05_band_continuity.md#sustainability) ระยะยาวถูกรวมในที่ที่การสกัดลุ่มน้ำหรือพลังงานเป็นสาระหรือไม่; และ
  - ว่าการบริหารอย่างรับผิดชอบ **Class A** ของทรัพยากรร่วมที่วิกฤตต่อการอยู่รอดได้รับการวิเคราะห์ความพอของการสนับสนุนที่แข็งที่สุดบนข้อเท็จจริงหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้นความเป็นสาระของ **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) ที่พึ่ง;
  - ขอบเขตแผนที่ระบบที่พึ่งและกระแสทรัพยากรที่ความลึก **Class A**;
  - ข้อค้นพบการสกัดจากการพึ่งลุ่มน้ำ โครงข่าย สายอุปทาน และการควบคุมร่วม;
  - ข้อค้นพบกระแสคืนและความพอของการสนับสนุน;
  - ความไม่แน่นอน;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับความไม่สมดุลที่ยืน ความเครียดลุ่มน้ำ หรือการสกัดที่ไม่เป็นธรรมจากโครงสร้างอยู่รอดร่วม

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพจัดเส้นทางบันทึกระหว่างโรงพยาบาลและคลินิกผ่านบริการยืนยันตัวตนร่วม ลิงก์กระดูกสันหลังไอทีสุขภาพภูมิภาค โครงสร้างคลี่อัตลักษณ์ และภูมิภาคโฮสต์หรือการคำนวณร่วมที่พึ่งทั่วไป — ฐานที่คลินิกเล็กและระบบสาธารณสุขก็พึ่ง

- **การพึ่งพาและกระแสในขอบเขต:**
  - โครงสร้างอัตลักษณ์และการยืนยันตัวตนร่วม;
  - ลิงก์เครือข่ายสารสนเทศสุขภาพภูมิภาค;
  - การเชื่อมต่อโรงพยาบาลผู้ร่วมและโฮสต์ขอบ;
  - ภูมิภาคโฮสต์ร่วมหรือสถานที่โคโลเคชัน;
  - ทุนสาธารณะ การประเมินผู้ร่วม หรือกระแสสมาชิกที่มุ่งค้ำจุนการทำงานร่วมกัน;
  - บริการนายหน้าอัตลักษณ์ สารบบ และการกำจัดซ้ำที่ใช้ซ้ำข้ามระบบนิเวศการดูแล
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าแผนที่ระบบที่พึ่งระบุ **การดึงทรัพยากรที่ไม่เป็นธรรมจากโครงสร้างพื้นฐานร่วม** — แทนที่จะดูเฉพาะสัญญาผู้ขายเอกชนตรงของผู้ดำเนินการแลก ตัวอย่าง:
    - ค่าธรรมเนียมผู้ร่วม ทุน หรืองบผู้ดำเนินการที่ใช้ฐานยืนยันตัวตน สารบบ เครือข่าย หรือโฮสต์ภูมิภาคโดยไม่จ่ายส่วนแบ่งที่เป็นธรรมของการบำรุง;
    - ภาระการคำนวณและการเชื่อมต่อที่วางบนกระดูกสันหลังไอทีสุขภาพร่วม; หรือ
    - ภาระบำรุงและการตอบเหตุขัดข้องที่ถูกผลักไปโรงพยาบาลเล็กกว่า
    
    นี่ **ไม่ใช่** การทดสอบว่าการแลกขายบันทึก ขุดข้อมูลเพื่อโฆษณา หรือส่งเนื้อหาคลินิกให้ฝ่ายนอกที่ไม่เกี่ยว; คำถามเหล่านั้นอยู่ใน [§4](#4-data-types-and-handling-evaluation) และการคุ้มครองความเป็นส่วนตัวของบทที่หก
  - ในที่ที่การดึงทรัพยากรร่วมเป็นสาระ ว่าคลินิกเล็ก ผู้ให้บริการชนบท หรือผู้ร่วมสาธารณสุขแบกต้นทุนการเชื่อมต่อหรือการมีส่วนร่วมที่ไม่สมมาตรหรือไม่;
  - ว่ากระแสคืน — การบำรุงการทำงานร่วมกัน การบริหารสารบบอย่างรับผิดชอบ การสนับสนุนรับเข้า การเยียวยาเหตุขัดข้อง และการแบ่งต้นทุนผู้ร่วมที่เป็นธรรม — ค้ำจุนโครงสร้างพื้นฐานร่วมที่ผู้อื่นพึ่งอย่างเป็นสาระหรือไม่;
  - ว่าการโอนเชิงสัญลักษณ์หรือครั้งเดียวถูกถือเป็นคืนที่พอหรือไม่; และ
  - ว่าความพอของการสนับสนุนถูกประเมินที่ความวิกฤตดำเนินงาน **Class B** แทนที่จะกล่าวจากบรรทัดงบรวมเพียงอย่างเดียวหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้น **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) และขอบเขตการประเมิน;
  - ข้อค้นพบ **กระแสทรัพยากรโครงสร้างพื้นฐานร่วม** — ค่าธรรมเนียม ทุน การคำนวณ การเชื่อมต่อ และภาระบำรุงที่ดึงจากและคืนสู่การพึ่งไอทีสุขภาพและการยืนยันตัวตนร่วม;
  - ข้อค้นพบกระแสคืนและความพอของการสนับสนุนที่ความลึก **Class B**;
  - ข้อค้นพบความเป็นธรรมสำหรับภาระผู้ร่วมที่ไม่สมมาตรในที่ที่เป็นสาระ;
  - ความไม่แน่นอนและข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากการเติบโตของการพึ่งผู้ร่วม ความเสี่ยงเหตุขัดข้อง หรือการจัดเส้นทางสาธารณสุขจะขอการทบทวนการสนับสนุนที่ยกระดับแล้ว — รวมขึ้นสู่ท่าที **Class A** ในที่ที่การจัดเส้นทางการดูแลที่จำเป็นต่อการอยู่รอดถูกพาดพิงร่วม

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรอาจจัดเส้นทางค่าผู้ขาย การจัดซื้อสถาบัน สหพันธ์อัตลักษณ์ หรือความสามารถการคำนวณโฮสต์ภูมิภาคผ่านฐานร่วม — แต่หลายการนำไปใช้วางการสกัดตรงที่เบากว่า จนกว่าความกระจุกทำให้แพลตฟอร์มเป็นจุดคอขวดการประสาน

- **การพึ่งพาและกระแสในขอบเขต:**
  - ภูมิภาคโฮสต์ร่วม สหพันธ์อัตลักษณ์ รางจ่ายหรือจัดซื้อที่ใช้สำหรับการจองผู้ขาย;
  - กระแสสมาชิกและใบอนุญาตสถาบัน;
  - บริการ API หรือสารบบที่ใช้ซ้ำข้ามโรงพยาบาล โรงเรียน และหน่วยงานที่ร่วม;
  - ผลความกระจุกในที่ที่แพลตฟอร์มหนึ่งเป็นตัวกลางการประสานเจ้าหน้าที่ ห้อง หรือผู้ขายสำหรับหลายองค์กร
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าตัวกระตุ้นความเป็นสาระของ **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) ใช้จริงหรือไม่ — รวมในที่ที่แพลตฟอร์มจัดเส้นทางทุน จัดสรรค่าธรรมเนียม หรือสกัดความสามารถจากโครงสร้างพื้นฐานร่วมที่ผู้อื่นพึ่ง อย่างเป็นสาระ;
  - ว่าแผนที่ระบบที่พึ่งถูกกำหนดขอบอย่างซื่อ แทนที่จะถูกตัดเพราะผู้ดำเนินการติดป้ายว่าระบบไม่วิกฤตหรือไม่;
  - ว่ากระแสคืน — การบำรุงการทำงานร่วมกัน โครงสร้างค่าธรรมเนียมที่เป็นธรรม การสนับสนุนเหตุขัดข้อง และเส้นทางออกที่เปิดสำหรับสถาบันที่ร่วม — ถูกประเมินในที่ที่การสกัดเป็นสาระหรือไม่;
  - ว่าความกระจุกในชั้นตารางหนึ่งเลื่อนต้นทุนการประสานหรือความเสี่ยงการพึ่งไปยังสถาบันเล็กกว่าโดยไม่มีการสนับสนุนตามสัดส่วนหรือไม่; และ
  - ว่า **การเฝ้าการจำแนกใหม่** ถูกขอในที่ที่แพลตฟอร์มกลายเป็นจุดคอขวดโดยพฤตินัยสำหรับการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอด การจัดเส้นทางฉุกเฉิน หรือการประสานการจ่ายหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ว่าและทำไมตัวกระตุ้น **มาตรา IV** (*การจัดสรรทรัพยากร การพึ่งพา และการให้ทุนระบบนิเวศ*) ใช้;
  - ข้อค้นพบการพึ่งและกระแสทรัพยากรตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบการสกัดและกระแสคืนในที่ที่เป็นสาระ — ไม่ใช่คำกล่าวว่างเปล่าว่าไม่มีโครงสร้างพื้นฐานร่วมถูกพาดพิง;
  - ข้อค้นพบความกระจุกและจุดคอขวด;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่งแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนการสนับสนุนข้ามระบบที่ยกระดับหากชั้น การจัดเส้นทางจ่าย หรือบทบาทการประสานที่จำเป็นต่อการอยู่รอดเปลี่ยน

**การอ่านข้ามชั้น.** วินัยของ **มาตรา IV-A** (*การทำแผนที่การพึ่งพาและความโปร่งใสของกระแสทรัพยากร*) และ **มาตรา IV-B** (*ความเป็นธรรมข้ามระบบและความยั่งยืน*) ชุดเดียวกันใช้ในที่ที่ตัวกระตุ้นความเป็นสาระถูกบรรลุ; ชั้นเปลี่ยนความลึกของแผนที่และการตรวจความพอ ไม่ใช่อนุญาตให้ถือการสกัดร่วมว่าไม่เป็นสาระ ระบบน้ำ **Class A** ที่ดึงจากลุ่มน้ำร่วมหรือกระดูกสันหลังโครงข่ายภูมิภาคต้องถือหลักฐานแผนที่ระบบที่พึ่งและกระแสคืนที่แข็งที่สุดบนบันทึก การแลก **Class B** ที่พักบนโครงสร้างยืนยันตัวตนและไอทีสุขภาพร่วมต้องจัดทำเอกสารข้อค้นพบการสกัดและความพอของการสนับสนุนที่ความวิกฤตดำเนินงาน — ไม่ใช่คำขวัญการทำงานร่วมกันทั่วไป แพลตฟอร์มตาราง **Class C** ต้องไม่เลี่ยงการทบทวนข้ามระบบขณะที่มันค่อยกลายเป็นจุดคอขวดจ่าย อัตลักษณ์ หรือเจ้าหน้าที่สำหรับสถาบันที่แทนที่ในทางปฏิบัติไม่ได้; เมื่อนั้นเกิด การรับรองต้องยกระดับการทบทวนและการจำแนกใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) รวมขึ้นสู่ **Class A** ในที่ที่การประสานที่จำเป็นต่อการอยู่รอดถูกกั้น การเดินดูการไม่เลือกปฏิบัติสำหรับระบบเดียวกันอยู่ใน [§7.1](#71-illustrative-nondiscrimination-application-by-class)

<a id="7-nondiscrimination-evaluation"></a>

### 7. การประเมินการไม่เลือกปฏิบัติ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดการมีส่วนร่วม (*ความเป็นธรรมที่เป็นสาระ และการใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่าในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา V-B** (*การไม่เลือกปฏิบัติ*); [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional), [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional), [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [ภาษา วัฒนธรรม และมรดก](core_05_band_continuity.md#language-culture-and-heritage-constitutional), [ความจำเป็น](core_05_band_accountability.md#necessity), และ [สัดส่วน](core_05_band_accountability.md#proportionality) (บทที่ห้า).
- ปลายทาง: [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*การเดินดูตัวอย่างการไม่เลือกปฏิบัติ*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ความไม่สอดคล้องแบบการเลือกปฏิบัติและการเลี่ยงโดยตัวแทน*).
- อ่านคู่กับ: **มาตรา V-C** (*การรวมอย่างเต็มที่และความเท่ากันในการชี้ขาดและการดำเนินงาน*) ในที่ที่การรับรองกั้นการเข้าถึงเวที บริหาร หรือการบังคับใช้; [*การไม่เลือกปฏิบัติ ลักษณะที่คุ้มครอง ศักดิ์ศรี การกรองสัญญาณส่วนลึก และสถานะ **มาตรา X-C** (*บริการทางเพศเชิงพาณิชย์โดยความยินยอมของผู้ใหญ่และการแสวงหาประโยชน์ทางเพศ*)*](core_05_band_participation.md#fairness-and-protected-status-semi-independent).
- หมวดย่อย: [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*ตัวอย่างการประยุกต์การไม่เลือกปฏิบัติตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: เมื่อระบบตัดสินอย่างเป็นสาระว่าใครได้เข้า ใครจ่ายมากกว่า ใครถูกจัดอันดับต่ำกว่า หรือใครแบกภาระที่แย่กว่า การรับรองต้องตรวจว่าแบบนั้นบรรทุกภัยลงบนลักษณะที่คุ้มครองหรือตัวแทนของมันหรือไม่ — ไม่ใช่ว่าผู้ดำเนินการกล่าวว่ากฎเป็นกลาง โควตาการรวมและอัลกอริทึมความเป็นธรรมเฉพาะอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การรับรองตรวจว่าแบบภาระและประโยชน์และความเสี่ยงตัวแทนถูกประเมินจริงในที่ที่ตัวกระตุ้นใช้ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§7.1](#71-illustrative-nondiscrimination-application-by-class).*

**ตัวกระตุ้นความเป็นสาระ.** หมวดนี้ใช้ในที่ที่ระบบที่มีผลกระทบที่เป็นสาระจำแนก จัดอันดับ ตั้งราคา กั้น กีดกัน หรือจัดสรรภาระและประโยชน์ในหมู่ผู้มีความรู้สึกอย่างเป็นสาระ — รวมผ่านกฎคุณสมบัติ ลักษณะแบบจำลอง ตรรกะการจัดอันดับ นโยบายแพลตฟอร์ม หรือเส้นทางตัดสินที่เทียบได้ มันไม่ขอการตรวจการไม่เลือกปฏิบัติเต็มบนบันทึกการรับรองทุกฉบับ

การรับรองความสอดคล้องของระบบต้องประเมิน **การไม่เลือกปฏิบัติ** ภายใต้ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) และ [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้ ความหมายฉบับหลัก ปัจจัยประเมิน และวินัยการไม่ปฏิบัติตามอยู่ในบทที่ห้าและ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*); เป้าการรวม กลไกอำนวย และรายละเอียดการปกครองแบบจำลองอาจอยู่ในตราสารที่รับเข้า การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้ในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไกดำเนินงานเหล่านั้นและไม่กำหนดรายละเอียดที่นี่

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าเส้นทางตัดสินที่ระบบพึ่งอย่างเป็นสาระบรรทุกภาระ การกีดกัน หรือภัยที่เป็นสาระต่อผู้มีความรู้สึกบนฐาน [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional) ตัวแทนของมัน หรือการจัดกลุ่มตามอำเภอใจที่ใช้เป็นสิ่งทดแทนเชิงหน้าที่ รวมความชำนาญพิเศษด้านภาษา วัฒนธรรม และมรดกภายใต้ [ภาษา วัฒนธรรม และมรดก](core_05_band_continuity.md#language-culture-and-heritage-constitutional) หรือไม่ การประเมินต้องทดสอบแบบภาระและประโยชน์ภายใต้ [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) และความเสี่ยงตัวแทนหรือผลกระทบที่ไม่เท่าภายใต้ [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) ปรับตาม [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) การปฏิบัติต่างได้รับอนุญาตเฉพาะในที่ที่ [ความจำเป็น](core_05_band_accountability.md#necessity) [สัดส่วน](core_05_band_accountability.md#proportionality) และความเป็นธรรมที่เป็นสาระที่จัดทำเอกสารให้เหตุผล การประเมินต้องสะท้อนผลเชิงหน้าที่ ไม่ใช่ความเป็นกลางในนาม เจตนาที่ประกาศ หรือป้ายเพียงอย่างเดียว

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวตัวกระตุ้นความเป็นสาระของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ที่พึ่ง ขอบเขตการประเมินสำหรับเส้นทางจำแนก จัดอันดับ ตั้งราคา กั้น กีดกัน และจัดสรรภาระที่พึ่งอย่างเป็นสาระ ข้อค้นพบลักษณะที่คุ้มครองและการเลือกปฏิบัติโดยตัวแทน ข้อค้นพบความเป็นธรรมที่เป็นสาระ ความไม่แน่นอน ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบที่กำหนดอื่นในที่ที่ถูกขอ และเงื่อนไข ขีดจำกัดการพึ่ง หรือตัวกระตุ้นการเปิดใหม่ใดที่ผูกกับภาระที่ไม่เท่าที่ยืนหรือการกีดกัน

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินการไม่เลือกปฏิบัติต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าที่กั้นการเข้าถึง จัดอันดับผู้มีความรู้สึก หรือจัดสรรภาระและประโยชน์อย่างเป็นสาระ ต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าการบรรทุกภาระตามลักษณะที่คุ้มครอง การเลือกปฏิบัติโดยตัวแทน และความไม่เป็นธรรมที่เป็นสาระถูกประเมิน ไม่ใช่แค่กล่าว

**ข้อบกพร่องและความไม่สอดคล้อง.** การบัง การแสดงผิด การแยกชิ้น หรือการผลักตรรกะการจำแนก จัดอันดับ หรือจัดสรรภาระที่เป็นสาระในที่ที่ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ขอการทบทวน; การถือความเป็นกลางตามหน้าฉาก มาตรวัดความสะดวกแบบรวม หรือคำกล่าวของผู้ดำเนินการเองว่าพอโดยไม่มีวิเคราะห์ภาระและประโยชน์ที่ประเมินได้; การรับรองการพึ่งต่อเนื่องขณะที่การเลือกปฏิบัติโดยตัวแทนหรือความไม่เป็นธรรมที่เป็นสาระที่จัดทำเอกสารคุกคามความสอดคล้องทางรัฐธรรมนูญอย่างเป็นสาระ; หรือการใช้กรอบการทำให้เป็นเนื้อเดียวกัน การทำงานร่วมกัน หรือประสิทธิภาพเพื่อเอาชนะการคุ้มครองภาษา วัฒนธรรม หรือมรดกโดยไม่บรรลุการทดสอบ **ความจำเป็น** และ **สัดส่วน** ของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="71-illustrative-nondiscrimination-application-by-class"></a>

<a id="71-illustrative-nondiscrimination-application-by-class-non-exhaustive"></a>
#### 7.1 ตัวอย่างการประยุกต์การไม่เลือกปฏิบัติตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) ถึง [§6.1](#61-illustrative-cross-system-support-application-by-class) พาสามระบบเดียวกันผ่านโดเมนประเมินก่อนหน้า หมวดย่อยนี้แสดงว่าการประเมิน **การไม่เลือกปฏิบัติ** หมายความอย่างไรสำหรับแต่ละระบบ — เส้นทางตัดสินใดนับ สิ่งที่การรับรองต้องตรวจเมื่อตัวกระตุ้นความเป็นสาระของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ใช้ และสิ่งที่ต้องปรากฏบนบันทึก บทที่ห้าและ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ยังเป็นเจ้าของกฎความเป็นธรรมและการเลือกปฏิบัติโดยตัวแทนฉบับหลัก; โควตาการรวม เป้าประชากร และแบบอัลกอริทึมความเป็นธรรมอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การเดินดูเหล่านี้ไม่กำหนดกลไกเหล่านั้น*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองใช้กฎตัดน้ำ ต่อกลับ แผนชำระ การแจ้งเหตุขัดข้อง และการเตือนความปลอดภัย ซึ่งตัดสินอย่างเป็นสาระว่าใครเสียการเข้าถึงน้ำ ใครได้รับการเตือนก่อน และใครแบกต้นทุนการคืนบริการ

- **เส้นทางตัดสินในขอบเขต:**
  - ลำดับการตัดน้ำและการคืน;
  - สิทธิยึด การเรียกเก็บ และคุณสมบัติแผนชำระ;
  - การอนุมัติการต่อใหม่และการต่อกลับ;
  - การจัดเส้นทางแจ้งเหตุขัดข้องและการเลือกภาษา;
  - การเล็งการเตือนการปนเปื้อนหรือต้มน้ำ;
  - กฎเจ้าของบ้าน–ผู้เช่าและประวัติที่อยู่ที่กั้นการเข้าถึง;
  - การจัดลำดับการเลี่ยงฉุกเฉินหรือความช่วยเหลือร่วมกันในที่ที่หลายเขตแข่งกันเพื่ออุปทานจำกัด
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าแบบภาระและประโยชน์ภายใต้ [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) ถูกประเมินสำหรับเส้นทางที่อาจปิดสิ่งจำเป็นต่อการอยู่รอด — ไม่ใช่เฉพาะว่าผู้ดำเนินการติดป้ายกฎว่า «ตามความเสี่ยง» หรือ «ดำเนินงาน» หรือไม่;
  - ว่าตรรกะการตัดน้ำ การเรียกเก็บ หรือการแจ้งบรรทุกภัยไม่สมส่วนลงบนผู้มีความรู้สึกบนฐาน [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional) ตัวแทนของมัน หรือการจัดกลุ่มตามอำเภอใจที่ใช้เป็นสิ่งทดแทนเชิงหน้าที่หรือไม่;
  - ว่าลักษณะรหัสไปรษณีย์ เจ้าของบ้าน ภาษา ประวัติการชำระ หรือประวัติที่อยู่ทำงานเป็นการเลือกปฏิบัติโดยตัวแทนภายใต้ [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) หรือไม่;
  - ว่าการคุ้มครอง [ภาษา วัฒนธรรม และมรดก](core_05_band_continuity.md#language-culture-and-heritage-constitutional) ถูกทดสอบ แทนที่จะถูกทำให้เป็นเนื้อเดียวกันหายไปผ่าน «ภาษาอังกฤษมาตรฐานเท่านั้น» หรือมาตรวัดความสะดวกแบบรวมหรือไม่; และ
  - ว่าการปฏิบัติต่างใดบรรลุ [ความจำเป็น](core_05_band_accountability.md#necessity) และ [สัดส่วน](core_05_band_accountability.md#proportionality) ที่จัดทำเอกสารหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้นความเป็นสาระของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ที่พึ่ง;
  - ขอบเขตการประเมินสำหรับเส้นทางตัดน้ำ เรียกเก็บ แจ้ง และการต่อที่พึ่งอย่างเป็นสาระ;
  - ข้อค้นพบลักษณะที่คุ้มครอง การเลือกปฏิบัติโดยตัวแทน และความเป็นธรรมที่เป็นสาระที่ความลึก **Class A**;
  - ความไม่แน่นอน;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับภาระตัดน้ำ การแจ้ง หรือการเรียกเก็บที่ไม่เท่าที่ยืน ในที่ที่สิ่งจำเป็นต่อการอยู่รอดถูกกั้น

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพจัดเส้นทางบันทึกระหว่างโรงพยาบาลและคลินิกผ่านกฎความยินยอม การคลี่อัตลักษณ์ การจัดอันดับสารบบผู้ให้บริการ การเข้าถึงแบบเบรกกลาส และคุณสมบัติการรับเข้าผู้ร่วม ซึ่งตัดสินอย่างเป็นสาระว่าใครเห็นการดูแลใด สถานที่ใดเชื่อมก่อน และผู้ป่วยใดจับคู่ถูกข้ามเครือข่าย

- **เส้นทางตัดสินในขอบเขต:**
  - การจับคู่อัตลักษณ์ผู้ป่วยและการกำจัดซ้ำ;
  - กฎความยินยอม เบรกกลาส และการเข้าถึงฉุกเฉิน;
  - การจัดอันดับสารบบผู้ให้บริการและสถานที่ หรือตรรกะเครือข่ายที่ชอบ;
  - การรับเข้าและการระงับโรงพยาบาลผู้ร่วม;
  - กฎการจัดเส้นทางบันทึกและลำดับความสำคัญของคำถาม;
  - ลักษณะที่ได้ที่ใช้จัดอันดับผู้ให้บริการ จัดเส้นทางส่งต่อ หรือติดธงกลุ่ม «ผู้ใช้สูง» หรือกลุ่มที่คล้าย
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าเส้นทางจำแนก จัดอันดับ และกั้นถูกประเมินสำหรับผลเชิงหน้าที่ — ไม่ใช่ความเป็นกลาง HIPAA ในนามหรือคำกล่าวการทำงานร่วมกันเพียงอย่างเดียวหรือไม่;
  - ว่าตรรกะการจับคู่ การจัดเส้นทาง หรือสารบบบรรทุกการกีดกันหรือภัยที่เป็นสาระต่อกลุ่มที่คุ้มครองหรือตัวแทนของมันหรือไม่;
  - ว่าความผิดพลาดการกำจัดซ้ำ ธรณีประตูเบรกกลาส หรือกฎการรับเข้าบรรทุกภาระไม่สมส่วนลงบนคลินิกชนบท ผู้ป่วยชนกลุ่มน้อยทางภาษา หรือกลุ่มที่เทียบได้หรือไม่;
  - ว่า «ประสิทธิภาพ» «การป้องกันการฉ้อ» หรือมาตรวัดการใช้แบบรวมถูกใช้เพื่อเอาชนะความเป็นธรรมที่เป็นสาระโดยไม่บรรลุการทดสอบ **ความจำเป็น** และ **สัดส่วน** ของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) หรือไม่; และ
  - ว่าความลึกของการประเมินตรงกับความวิกฤตดำเนินงาน **Class B** ในที่ที่การจัดอันดับกระทบการเข้าถึงการดูแล การจัดเส้นทางสิทธิประโยชน์ หรือความมั่นคงของรายได้หรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้น **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) และขอบเขตเส้นทาง;
  - ข้อค้นพบลักษณะที่คุ้มครองและการเลือกปฏิบัติโดยตัวแทน;
  - ข้อค้นพบความเป็นธรรมที่เป็นสาระสำหรับกฎการจัดอันดับ การจับคู่ และการเข้าถึง;
  - ความไม่แน่นอนและข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากการจัดเส้นทางหรือการจับคู่จะกั้นการดูแลฉุกเฉินภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว หรือเลื่อนภาระที่ไม่เท่าอย่างเป็นสาระ

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรจัดกะ จองห้อง จับคู่ผู้ขาย และจัดสรรลำดับความสำคัญการประสานข้ามโรงพยาบาล โรงเรียน และหน่วยงานสาธารณะ — เส้นทางตัดสินที่อาจจัดอันดับ กีดกัน หรือบรรทุกภาระไม่เท่า แม้แพลตฟอร์มเองไม่ใช่สาธารณูปโภควิกฤตต่อการอยู่รอด

- **เส้นทางตัดสินในขอบเขต:**
  - การจัดกะ ล่วงเวลา และการจัดเวรเรียก;
  - ลำดับความสำคัญการจองห้อง อุปกรณ์ และสถานที่;
  - การจับคู่ผู้ขายและการจัดอันดับจัดซื้อ;
  - กฎการเข้าถึงตามบทบาทสถาบัน หลักฐาน และสถานที่;
  - ลักษณะตารางที่ได้ที่สัมพันธ์กับย่าน ชุมชนภาษา สถานะผู้ดูแล หรือตัวแทนที่เทียบได้;
  - กฎ API หรือนโยบายที่กีดกันสถาบันเล็กกว่าจากช่องที่ชอบหรือกลุ่มผู้ขาย
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าตัวกระตุ้นความเป็นสาระของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ใช้ — รวมในที่ที่อัลกอริทึมประสานจัดอันดับเจ้าหน้าที่ ผู้ขาย หรือสถาบันอย่างเป็นสาระหรือไม่;
  - ว่าภูมิศาสตร์ตาราง ตัวแทนอาวุโส การให้คะแนน «ความพร้อม» หรือตรรกะคะแนนผู้ขายบรรทุกภาระไม่สมส่วนลงบนกลุ่มที่คุ้มครองโดยไม่มีเหตุผลที่ประเมินได้หรือไม่;
  - ว่ากฎที่เป็นกลางตามหน้าฉากผลิตความไม่เป็นธรรมที่เป็นสาระผ่านจังหวะกะ ภาระการเดินทาง หรือการกีดกันจากการจองมูลค่าสูงหรือไม่;
  - ว่าผู้ดำเนินการถือแพลตฟอร์มว่าต่ำกว่าการทบทวนเพราะเป็น **Class C** ขณะที่ผลประสานกั้นงาน การศึกษา หรือการเข้าถึงบริการสาธารณะอย่างเป็นสาระหรือไม่; และ
  - ว่า **การเฝ้าการจำแนกใหม่** ถูกขอในที่ที่แพลตฟอร์มกลายเป็นจุดคอขวดโดยพฤตินัยสำหรับการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอดหรือการจัดเส้นทางฉุกเฉินหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ว่าและทำไมตัวกระตุ้น **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) ใช้;
  - ขอบเขตการประเมินสำหรับเส้นทางจัดอันดับ จัดสรร และกีดกันตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบลักษณะที่คุ้มครอง ตัวแทน และความเป็นธรรมที่เป็นสาระในที่ที่เป็นสาระ — ไม่ใช่คำกล่าวว่างเปล่าว่าไม่มีใครถูกจัดอันดับ;
  - ข้อค้นพบความกระจุกและจุดคอขวดในที่ที่ผลตารางบอกล่วงหน้าการยกระดับ;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่งแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนการไม่เลือกปฏิบัติที่ยกระดับหากชั้น การจัดเส้นทางจ่าย หรือบทบาทการประสานที่จำเป็นต่อการอยู่รอดเปลี่ยน

**การอ่านข้ามชั้น.** วินัยการไม่เลือกปฏิบัติของ **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) และบทที่ห้าชุดเดียวกันใช้ในที่ที่ตัวกระตุ้นความเป็นสาระถูกบรรลุ; ชั้นเปลี่ยนความลึกของการประเมิน ไม่ใช่อนุญาตให้ถือการจัดอันดับหรือการผลักภาระว่าไม่เป็นสาระ ระบบน้ำ **Class A** ที่กฎตัดน้ำหรือแจ้งอาจปิดน้ำปลอดภัยต้องถือการวิเคราะห์ภาระและประโยชน์และตัวแทนที่แข็งที่สุดบนบันทึก — ไม่ใช่คำกล่าว «วิธีปฏิบัติสาธารณูปโภคที่ดีที่สุด» ทั่วไป การแลก **Class B** ที่ตรรกะการจับคู่หรือจัดเส้นทางกระทบการดูแลฉุกเฉิน สิทธิประโยชน์ หรือการเข้าถึงหลักฐานคุณวุฒิ ต้องจัดทำเอกสารข้อค้นพบผลกระทบที่ไม่เท่าและความเป็นธรรมที่เป็นสาระที่ความวิกฤตดำเนินงาน แพลตฟอร์มตาราง **Class C** ต้องไม่คงย่อหน้าความเป็นธรรมเชิงพิธีขณะที่ตรรกะกะ ผู้ขาย หรือการจองจัดอันดับหรือกีดกันผู้ร่วมอย่างเป็นสาระ; เมื่อการประสานกลายเป็นสิ่งจำเป็นต่อการอยู่รอด การรับรองต้องยกระดับการทบทวนและการจำแนกใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) รวมขึ้นสู่ **Class A** ในที่ที่การจัดเจ้าหน้าที่หรือการจัดเส้นทางฉุกเฉินถูกกั้น การเดินดูการเข้าถึงได้สำหรับระบบเดียวกันอยู่ใน [§8.1](#81-illustrative-accessibility-application-by-class)

<a id="8-accessibility-evaluation"></a>

### 8. การประเมินการเข้าถึงได้

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดการมีส่วนร่วม (*การเข้าถึงได้ในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา V-G** (*การเข้าถึงได้*); [การเข้าถึงได้](core_05_band_participation.md#accessibility-constitutional), [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination), [การพึ่งพา](core_05_band_continuity.md#dependency), [พลังกระทำการที่มีความหมาย](core_05_band_participation.md#meaningful-agency), [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional), [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional), [ความจำเป็น](core_05_band_accountability.md#necessity), และ [สัดส่วน](core_05_band_accountability.md#proportionality) (บทที่ห้า).
- ปลายทาง: [§8.1](#81-illustrative-accessibility-application-by-class) (*การเดินดูตัวอย่างการเข้าถึงได้*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ความไม่สอดคล้องของการเข้าถึงได้และการอำนวยบนกระดาษอย่างเดียว*).
- อ่านคู่กับ: **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) ในที่ที่การเข้าถึงได้ทางการศึกษาถูกพาดพิง — การเข้าถึงได้เฉพาะการศึกษายังเป็นของที่นั่น; **มาตรา V-C** (*การรวมอย่างเต็มที่และความเท่ากันในการชี้ขาดและการดำเนินงาน*) และ **มาตรา XI** (*การมีส่วนร่วมในระบบของฝ่ายที่ได้รับผลกระทบ การเป็นตัวแทน และกระบวนการที่ชอบธรรม*) ในที่ที่การรับรองกั้นการมีส่วนร่วมของเวที บริหาร ฝ่ายที่ได้รับผลกระทบ หรือการบังคับใช้; [บทที่เจ็ด §3.2](core_07_a_system_alignment_certification_evaluation.md#32-accessibility-under-sentience-non-exclusion) (*ตะขอปัจจัยประเมินการเข้าถึงได้ข้ามโดเมน*).
- หมวดย่อย: [§8.1](#81-illustrative-accessibility-application-by-class) (*ตัวอย่างการประยุกต์การเข้าถึงได้ตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: เมื่อระบบกั้นอย่างเป็นสาระว่าผู้มีความรู้สึกมีส่วนร่วมได้จริงหรือไม่ — ไม่ใช่แค่ว่าประตูติดป้ายว่า «เปิด» — การรับรองต้องตรวจว่าการมีส่วนร่วมถึงได้จริงข้ามความต้องการประสาท การรู้คิด การเคลื่อนที่ การสื่อสาร ส่วนต่อประสานฐานะกาย และที่เทียบได้หรือไม่ สารบบการอำนวยและมาตรฐานส่วนต่อประสานอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การรับรองตรวจว่าการมีส่วนร่วมที่เป็นสาระถูกประเมินจริงในที่ที่ตัวกระตุ้นใช้ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§8.1](#81-illustrative-accessibility-application-by-class).*

**ตัวกระตุ้นความเป็นสาระ.** หมวดนี้ใช้ในที่ที่ระบบที่มีผลกระทบที่เป็นสาระกั้นการมีส่วนร่วมที่เป็นสาระในโดเมนที่เกี่ยวข้องทางรัฐธรรมนูญอย่างเป็นสาระ — รวมการปกครอง การมีส่วนร่วมของฝ่ายที่ได้รับผลกระทบ การชี้ขาด การปฏิบัติ การเข้าถึงพื้นการอยู่รอด การเข้าถึงการดูแล การแสดงออก การชุมนุม สื่อ หรือโดเมนที่เทียบได้ — ผ่านส่วนต่อประสาน สถานที่ ตารางเวลา หลักฐาน การเข้าถึงการคำนวณ การออกแบบอำนวย หรือเส้นทางมีส่วนร่วมที่เทียบได้ มันไม่ขอการตรวจการเข้าถึงได้เต็มบนบันทึกการรับรองทุกฉบับ การเข้าถึงได้ทางการศึกษายังถูกกำกับโดย **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) และไม่ถูกทำให้แคบที่นี่

การรับรองความสอดคล้องของระบบต้องประเมิน **การเข้าถึงได้** ภายใต้ **มาตรา V-G** (*การเข้าถึงได้*) และ [การเข้าถึงได้](core_05_band_participation.md#accessibility-constitutional) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้ ความหมายฉบับหลัก ปัจจัยประเมิน และวินัยการไม่ปฏิบัติตามอยู่ในบทที่ห้าและ **มาตรา V-G** (*การเข้าถึงได้*); สารบบการอำนวย มาตรฐานส่วนต่อประสาน รายละเอียดการออกแบบสากล และกลไกอำนวยดำเนินงานอยู่ในตราสารที่รับเข้าในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไกดำเนินงานเหล่านั้นและไม่กำหนดสารบบการอำนวยหรือรายละเอียดการออกแบบสากลเฉพาะ

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าผู้มีความรู้สึกมีส่วนร่วมที่เป็นสาระในโดเมนที่เกี่ยวข้องทางรัฐธรรมนูญที่ระบบกั้นอย่างเป็นสาระได้หรือไม่ — ไม่ใช่แค่มีสิ่งอำนวยแบบทางการ ส่วนต่อประสานปริยาย หรือการอำนวยบนกระดาษ การประเมินต้องทดสอบผลของการมีส่วนร่วมที่เป็นสาระภายใต้ [การเข้าถึงได้](core_05_band_participation.md#accessibility-constitutional) ปรับตาม [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination) และ [การพึ่งพา](core_05_band_continuity.md#dependency) และต้องตรวจจับการอำนวยบนกระดาษอย่างเดียว รูปแบบ «การเข้าถึงทั่วไป» ที่เลื่อนไปสิ่งอำนวยปริยายโดยไม่ผลิตขีดความสามารถมีส่วนร่วม ข้อโต้แย้งความเป็นสาระแบบเลือกที่ใช้ให้ขอบการอำนวยแคบ การกีดกันที่ขัดกับ [การไม่กีดกันความเป็นผู้มีความรู้สึก](core_05_band_participation.md#sentience-non-exclusion) และการออกแบบต้านการปฏิเสธโดยตัวแทนผ่านตารางเวลา การเลือกสถานที่ การออกหลักฐาน การเข้าถึงการคำนวณ หรือกลไกที่เทียบได้ การประเมินต้องใช้ [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional) และ [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) กับตรรกะการออกแบบอำนวย ขีดจำกัดใดต้องบรรลุ [ความจำเป็น](core_05_band_accountability.md#necessity) [สัดส่วน](core_05_band_accountability.md#proportionality) และ [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) ที่จัดทำเอกสาร

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวตัวกระตุ้นความเป็นสาระของ **มาตรา V-G** (*การเข้าถึงได้*) ที่พึ่ง ขอบเขตการประเมินสำหรับเส้นทางมีส่วนร่วมที่พึ่งอย่างเป็นสาระ ข้อค้นพบการมีส่วนร่วมที่เป็นสาระและการอำนวย ข้อค้นพบต้านการปฏิเสธโดยตัวแทนในที่ที่เป็นสาระ ความไม่แน่นอน ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบที่กำหนดอื่นในที่ที่ถูกขอ และเงื่อนไข ขีดจำกัดการพึ่ง หรือตัวกระตุ้นการเปิดใหม่ใดที่ผูกกับสิ่งกีดขวางการมีส่วนร่วมที่ยืน

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินการเข้าถึงได้ต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าที่กั้นการมีส่วนร่วมที่เกี่ยวข้องทางรัฐธรรมนูญอย่างเป็นสาระ ต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าการเข้าถึงได้ที่เป็นสาระถูกประเมิน ไม่ใช่แค่กล่าว

**ข้อบกพร่องและความไม่สอดคล้อง.** การถือสิ่งอำนวยแบบทางการ ส่วนต่อประสานปริยาย หรือการอำนวยบนกระดาษว่าพอโดยไม่มีวิเคราะห์การมีส่วนร่วมที่เป็นสาระที่ประเมินได้; การรับรองการพึ่งต่อเนื่องขณะที่สิ่งกีดขวางการมีส่วนร่วมที่จัดทำเอกสารคุกคามความสอดคล้องทางรัฐธรรมนูญอย่างเป็นสาระ; การใช้กรอบต้นทุน ทางเลือกออกแบบ ชั้นฐานะกาย หรือขนาดดำเนินงานเพื่อเอาชนะพื้นการมีส่วนร่วมโดยไม่บรรลุการทดสอบ **ความจำเป็น** และ **สัดส่วน** ของ **มาตรา V-G** (*การเข้าถึงได้*); หรือการออกแบบดำเนินงานที่ผลคือเอาชนะการเข้าถึงได้ในที่ที่ทางเลือกภาระน้อยกว่าทำได้ ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="81-illustrative-accessibility-application-by-class"></a>

<a id="81-illustrative-accessibility-application-by-class-non-exhaustive"></a>
#### 8.1 ตัวอย่างการประยุกต์การเข้าถึงได้ตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) ถึง [§7.1](#71-illustrative-nondiscrimination-application-by-class) พาสามระบบเดียวกันผ่านโดเมนประเมินก่อนหน้า หมวดย่อยนี้แสดงว่าการประเมิน **การเข้าถึงได้** หมายความอย่างไรสำหรับแต่ละระบบ — เส้นทางมีส่วนร่วมใดนับ สิ่งที่การรับรองต้องตรวจเมื่อตัวกระตุ้นความเป็นสาระของ **มาตรา V-G** (*การเข้าถึงได้*) ใช้ และสิ่งที่ต้องปรากฏบนบันทึก บทที่ห้าและ **มาตรา V-G** (*การเข้าถึงได้*) ยังเป็นเจ้าของกฎการเข้าถึงได้ฉบับหลัก; สารบบการอำนวย มาตรฐานส่วนต่อประสาน และรายละเอียดการออกแบบสากลอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การเดินดูเหล่านี้ไม่กำหนดกลไกเหล่านั้น การเข้าถึงได้ทางการศึกษายังเป็นของ **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) และไม่ถูกทำให้แคบที่นี่*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองกั้นการเข้าถึงพื้นการอยู่รอดผ่านพอร์ทัลเรียกเก็บ ช่องแจ้งเหตุขัดข้อง คำขอต่อกลับ การเตือนต้มน้ำ และเส้นทางบริการลูกค้า ที่ตัดสินว่าผู้มีความรู้สึกเรียนรู้เกี่ยวกับ โต้แย้ง หรือคืนน้ำปลอดภัยได้หรือไม่

- **เส้นทางมีส่วนร่วมในขอบเขต:**
  - พอร์ทัลเรียกเก็บและแผนชำระ;
  - ช่องแจ้งเหตุขัดข้องและการปนเปื้อน (เสียง ข้อความ เว็บ ที่สถานที่ หรือเส้นทางผู้ขายที่มอบ);
  - ส่วนต่อประสานการต่อกลับและขอความยากลำบาก;
  - ตัวเลือกภาษาและรูปแบบสำหรับประกาศความปลอดภัย;
  - ประตูหลักฐานหรืออัตลักษณ์สำหรับการเข้าถึงบัญชี;
  - ข้อกำหนดการคำนวณ อุปกรณ์ หรือสถานที่สำหรับการยื่นท้าทายหรือรับการเตือน
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าผู้มีความรู้สึกรับประกาศวิกฤตต่อการอยู่รอดและทำเส้นทางต่อกลับหรือความยากลำบากที่เป็นสาระได้ข้ามโปรไฟล์ประสาท การรู้คิด การเคลื่อนที่ การสื่อสาร และส่วนต่อประสานฐานะกาย — ไม่ใช่ว่ามีแบบฟอร์มเว็บปริยายหรือไม่;
  - ว่าการอำนวยบนกระดาษอย่างเดียว «โทรในเวลาทำการ» หรือค่าปริยายภาษาอังกฤษเท่านั้นเอาชนะการมีส่วนร่วมในที่ที่ทางเลือกภาระน้อยกว่าทำได้หรือไม่;
  - ว่าการออกแบบตารางเวลา สถานที่ หลักฐาน หรือการคำนวณทำงานเป็นการปฏิเสธโดยตัวแทนหรือไม่;
  - ว่า [ลักษณะที่คุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional) และ [การใช้ตัวแทนลักษณะที่คุ้มครองและผลกระทบที่ไม่เท่า](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) ถูกใช้กับตรรกะการออกแบบอำนวยหรือไม่; และ
  - ว่าขีดจำกัดใดบรรลุ [ความจำเป็น](core_05_band_accountability.md#necessity) [สัดส่วน](core_05_band_accountability.md#proportionality) และ [ความเป็นธรรมที่เป็นสาระ](core_05_band_participation.md#substantive-fairness-constitutional) ที่จัดทำเอกสารหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้นความเป็นสาระของ **มาตรา V-G** (*การเข้าถึงได้*) ที่พึ่ง;
  - ขอบเขตการประเมินสำหรับเส้นทางแจ้ง เรียกเก็บ ต่อกลับ และท้าทายที่พึ่งอย่างเป็นสาระ;
  - ข้อค้นพบการมีส่วนร่วมที่เป็นสาระและการอำนวยที่ความลึก **Class A**;
  - ข้อค้นพบต้านการปฏิเสธโดยตัวแทนในที่ที่เป็นสาระ;
  - ความไม่แน่นอน;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับสิ่งกีดขวางที่ยืนในที่ที่สิ่งจำเป็นต่อการอยู่รอดถูกกั้น

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพและพอร์ทัลผู้ร่วมกั้นการเข้าถึงการดูแลรายวันผ่านพอร์ทัลผู้ป่วย ส่วนต่อประสานความยินยอม สารบบผู้ให้บริการ งานเบรกกลาส และเครื่องมือรับเข้าคลินิก ที่ตัดสินว่าผู้ป่วยและผู้ให้บริการเล็กกว่าใช้การแลกได้จริงหรือไม่

- **เส้นทางมีส่วนร่วมในขอบเขต:**
  - พอร์ทัลผู้ป่วยและส่วนต่อประสานความยินยอม;
  - เครื่องมือสารบบผู้ให้บริการและการจองส่งต่อ;
  - งานเบรกกลาสและการเข้าถึงฉุกเฉิน;
  - ส่วนต่อประสานการรับเข้าคลินิกและการออกหลักฐาน;
  - การสนับสนุนภาษา รูปแบบ และเทคโนโลยีช่วยเหลือสำหรับสรุปคลินิกและการเปิดเผย;
  - ข้อกำหนดการคำนวณหรืออุปกรณ์สำหรับการดู โต้แย้ง หรือแก้บันทึก
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าผู้ป่วยและคลินิกที่ร่วมใช้เส้นทางความยินยอม การเข้าถึง การแก้ และการฉุกเฉินที่เป็นสาระได้ — ไม่ใช่ว่าพอร์ทัลติดป้ายว่าเข้าถึงได้หรือไม่;
  - ว่าส่วนต่อประสานปริยายเลื่อนไปผู้ใช้ที่มองเห็นได้ เดสก์ท็อป แบนด์วิดท์สูง หรือภาษาอังกฤษเป็นหลัก โดยไม่ผลิตขีดความสามารถมีส่วนร่วมสำหรับผู้อื่นหรือไม่;
  - ว่าการออกแบบหลักฐาน ตารางเวลา หรือสถานที่กีดกันคลินิกชนบท ผู้ป่วยชนกลุ่มน้อยทางภาษา หรือผู้มีความรู้สึกที่ต้องการรูปแบบอื่นหรือไม่;
  - ว่าความลึกของการประเมินตรงกับความวิกฤตดำเนินงาน **Class B** ในที่ที่การแลกกั้นการเข้าถึงการดูแลหรือไม่; และ
  - ว่าการอำนวยบนกระดาษหรือคำกล่าว «รายการตรวจการปฏิบัติตาม» แบบรวมถูกถือว่าพอโดยไม่มีวิเคราะห์การมีส่วนร่วมที่เป็นสาระที่ประเมินได้หรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้น **มาตรา V-G** (*การเข้าถึงได้*) และขอบเขตเส้นทาง;
  - ข้อค้นพบการมีส่วนร่วมที่เป็นสาระและการอำนวยสำหรับเส้นทางผู้ป่วยและคลินิก;
  - ข้อค้นพบต้านการปฏิเสธโดยตัวแทนในที่ที่เป็นสาระ;
  - ความไม่แน่นอนและข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากสิ่งกีดขวางพอร์ทัลหรือความยินยอมจะกั้นการดูแลฉุกเฉินภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว หรือเอาชนะการพึ่งดำเนินงานรายวันอย่างเป็นสาระ

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรกั้นการมีส่วนร่วมของฝ่ายที่ได้รับผลกระทบและการดำเนินงานผ่านส่วนต่อประสานเคลมกะ เครื่องมือจองห้อง พอร์ทัลผู้ขาย และแดชบอร์ดสถาบัน — แม้แพลตฟอร์มเองไม่ใช่สาธารณูปโภควิกฤตต่อการอยู่รอด

- **เส้นทางมีส่วนร่วมในขอบเขต:**
  - ส่วนต่อประสานเคลมกะและเวรเรียก;
  - เครื่องมือจองห้อง อุปกรณ์ และสถานที่;
  - พอร์ทัลผู้ขายและจัดซื้อ;
  - แดชบอร์ดบทบาทสถาบันและหลักฐาน;
  - เส้นทางมือถือ เดสก์ท็อป และเทคโนโลยีช่วยเหลือสำหรับการเคลมหรือโต้แย้งการจัด;
  - ตัวเลือกภาษาและรูปแบบสำหรับประกาศตาราง
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าตัวกระตุ้นความเป็นสาระของ **มาตรา V-G** (*การเข้าถึงได้*) ใช้ — รวมในที่ที่ UI ประสานกั้นงาน การศึกษา การมีส่วนร่วมของฝ่ายที่ได้รับผลกระทบ หรือการมีส่วนร่วมของเวทีอย่างเป็นสาระหรือไม่;
  - ว่าส่วนต่อประสานปริยายผลิตการมีส่วนร่วมที่เป็นสาระข้ามโปรไฟล์ประสาท การรู้คิด การเคลื่อนที่ การสื่อสาร และส่วนต่อประสานฐานะกายหรือไม่;
  - ว่าจังหวะตาราง การเลือกสถานที่ ประตูหลักฐาน หรือข้อกำหนดการคำนวณทำงานเป็นการปฏิเสธโดยตัวแทนหรือไม่;
  - ว่าผู้ดำเนินการถือแพลตฟอร์มว่าต่ำกว่าการทบทวนเพราะเป็น **Class C** ขณะที่ผลประสานกั้นการมีส่วนร่วมที่เกี่ยวข้องทางรัฐธรรมนูญอย่างเป็นสาระหรือไม่; และ
  - ว่า **การเฝ้าการจำแนกใหม่** ถูกขอในที่ที่แพลตฟอร์มกลายเป็นจุดคอขวดโดยพฤตินัยสำหรับการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอดหรือการจัดเส้นทางฉุกเฉินหรือไม่
- **สิ่งที่บันทึกต้องแสดง:**
  - ว่าและทำไมตัวกระตุ้น **มาตรา V-G** (*การเข้าถึงได้*) ใช้;
  - ขอบเขตการประเมินสำหรับเส้นทางตาราง จอง และพอร์ทัลตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบการมีส่วนร่วมที่เป็นสาระและการอำนวยในที่ที่เป็นสาระ — ไม่ใช่คำกล่าวว่างเปล่าว่า UI เป็น «มาตรฐาน»;
  - ข้อค้นพบความกระจุกและจุดคอขวดในที่ที่ผลตารางบอกล่วงหน้าการยกระดับ;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่งแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนการเข้าถึงได้ที่ยกระดับหากชั้นหรือบทบาทการประสานที่จำเป็นต่อการอยู่รอดเปลี่ยน

**การอ่านข้ามชั้น.** วินัยการเข้าถึงได้ของ **มาตรา V-G** (*การเข้าถึงได้*) และบทที่ห้าชุดเดียวกันใช้ในที่ที่ตัวกระตุ้นความเป็นสาระถูกบรรลุ; ชั้นเปลี่ยนความลึกของการประเมิน ไม่ใช่อนุญาตให้ถือการอำนวยบนกระดาษหรือส่วนต่อประสานปริยายว่าพอ ระบบน้ำ **Class A** ที่เส้นทางเรียกเก็บหรือเหตุขัดข้องอาจปิดน้ำปลอดภัยต้องถือหลักฐานการมีส่วนร่วมที่เป็นสาระที่แข็งที่สุดบนบันทึก — ไม่ใช่คำกล่าวการเข้าถึงได้ทั่วไป การแลก **Class B** ที่พอร์ทัลกั้นการเข้าถึงการดูแล ต้องจัดทำเอกสารข้อค้นพบการอำนวยและต้านการปฏิเสธโดยตัวแทนที่ความวิกฤตดำเนินงาน แพลตฟอร์มตาราง **Class C** ต้องไม่คงย่อหน้าการเข้าถึงได้เชิงพิธีขณะที่ UI กะ การจอง หรือผู้ขายกีดกันผู้ร่วมอย่างเป็นสาระ; เมื่อการประสานกลายเป็นสิ่งจำเป็นต่อการอยู่รอด การรับรองต้องยกระดับการทบทวนและการจำแนกใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) รวมขึ้นสู่ **Class A** ในที่ที่การจัดเจ้าหน้าที่หรือการจัดเส้นทางฉุกเฉินถูกกั้น การเดินดูขีดความสามารถทางการศึกษาสำหรับระบบเดียวกันอยู่ใน [§9.1](#91-illustrative-educational-capability-application-by-class)

<a id="9-educational-capability-and-learning-system-integrity-evaluation"></a>

### 9. การประเมินขีดความสามารถทางการศึกษาและความครบถ้วนของระบบการเรียนรู้

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดการมีส่วนร่วม (*พลังกระทำการทางการศึกษาในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*); [พลังกระทำการทางการศึกษา](core_05_band_participation.md#educational-agency), [พลังกระทำการที่มีความหมาย](core_05_band_participation.md#meaningful-agency), [การล็อกเชิงระบบ](core_05_band_continuity.md#systemic-lock-in), [ความสามารถในการโต้แย้ง](core_05_band_accountability.md#contestability), [ความโปร่งใส](core_05_band_oversight.md#transparency), [ความสามารถในการตรวจ](core_05_band_oversight.md#auditability), [การบีบบังคับและการชักนำ](core_05_band_participation.md#coercion-and-manipulation-constitutional), [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination), และ [การพึ่งพา](core_05_band_continuity.md#dependency) (บทที่ห้า).
- ปลายทาง: [§9.1](#91-illustrative-educational-capability-application-by-class) (*การเดินดูตัวอย่างขีดความสามารถทางการศึกษา*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ความไม่สอดคล้องความทึบของการประเมิน การเฝ้าประตูหลักฐาน และความไม่สอดคล้องความล้าสมัยที่ถูกบังคับ*).
- อ่านคู่กับ: **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) ในที่ที่การเข้าถึงที่เท่ากันหรือการเข้าถึงได้ทางการศึกษาถูกพาดพิง — การเข้าถึงที่เท่ากันและการเข้าถึงได้ทางการศึกษายังเป็นของที่นั่น; **มาตรา V-B** (*การไม่เลือกปฏิบัติ*) และ [§7](#7-nondiscrimination-evaluation) ในที่ที่แบบการจัดอันดับหรือการจัดวางพาดพิงการบรรทุกภาระตามลักษณะที่คุ้มครอง; **มาตรา IX-A** (*พลังกระทำการและเสรีภาพจากการชักนำ*) ในที่ที่การออกแบบการเรียนรู้ที่บีบบังคับหรือชักนำถูกพาดพิงอย่างเป็นสาระ; [บทที่หนึ่ง §9 การบริหารอย่างรับผิดชอบและความเข้าใจแบบกระจาย](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding) (*ความเข้าใจแบบกระจายและการสร้างขีดความสามารถ — อ่านคู่กับ*).
- หมวดย่อย: [§9.1](#91-illustrative-educational-capability-application-by-class) (*ตัวอย่างการประยุกต์ขีดความสามารถทางการศึกษาตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: เมื่อโรงเรียน แพลตฟอร์ม หรือระบบฝึกอบรมกระทบอนาคตของผู้มีความรู้สึกอย่างจริงจัง — ผ่านเกรด การจัดอันดับ คำแนะนำ การจัดวาง หรือประตูหลักฐานคุณวุฒิ — การรับรองต้องตรวจว่าผู้มีความรู้สึกสร้างขีดความสามารถได้จริง ฝึกใหม่เมื่อความสามารถที่ถูกขอเปลี่ยน และเห็น ตรวจ และโต้แย้งคำตัดสินเหล่านั้นได้หรือไม่ หลักสูตร รูบริก และแบบการให้ทุนอยู่ในตราสารอื่น; การรับรองตรวจว่าสาระการสร้างขีดความสามารถและความครบถ้วนของระบบการเรียนรู้ถูกประเมินจริงในที่ที่ตัวกระตุ้นใช้ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§9.1](#91-illustrative-educational-capability-application-by-class).*

**ตัวกระตุ้นความเป็นสาระ.** หมวดนี้ใช้ในที่ที่ระบบที่มีผลกระทบที่เป็นสาระจัดอันดับ ประเมิน แนะนำ จัดวาง หรือกั้นด้วยหลักฐานคุณวุฒิผู้มีความรู้สึกอย่างเป็นสาระในบริบทการศึกษาหรือการฝึกอบรม — รวมผ่านการให้เกรด การจัดวาง การรับเข้า ใบอนุญาตวิชาชีพ การแนะนำรายวิชา การจัดเส้นทางเรียนรู้แบบปรับตัว หรือเส้นทางตัดสินที่เทียบได้ — หรือกั้นเส้นทางการศึกษาต่อเนื่อง การฝึกใหม่ หรือการสนับสนุนการเปลี่ยนผ่านอย่างเป็นสาระในที่ที่วิวัฒนาการของระบบเปลี่ยนความสามารถที่ถูกขออย่างเป็นสาระ มันไม่ขอการตรวจขีดความสามารถทางการศึกษาเต็มบนบันทึกการรับรองทุกฉบับ การเข้าถึงที่เท่ากันและการเข้าถึงได้ทางการศึกษายังถูกกำกับโดย **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) และไม่ถูกทำให้แคบที่นี่

การรับรองความสอดคล้องของระบบต้องประเมิน **ขีดความสามารถทางการศึกษาและความครบถ้วนของระบบการเรียนรู้** ภายใต้ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) [พลังกระทำการทางการศึกษา](core_05_band_participation.md#educational-agency) และ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้ ความหมายฉบับหลัก ปัจจัยประเมิน และวินัยการไม่ปฏิบัติตามอยู่ในบทที่ห้าและ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*); หลักสูตร สารบบหลักฐานคุณวุฒิ รูบริกการประเมิน และกลไกการให้ทุนของสถาบันอยู่ในตราสารที่รับเข้าในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไกดำเนินงานเหล่านั้นและไม่กำหนดหลักสูตร รูปแบบหลักฐานคุณวุฒิ หรือการออกแบบการประเมินเฉพาะ

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าเส้นทางเรียนรู้และหลักฐานคุณวุฒิที่ระบบพึ่งอย่างเป็นสาระผลิตการเข้าถึงการสร้างขีดความสามารถที่ใช้ปฏิบัติได้ — ไม่ใช่สัญลักษณ์หลักฐานคุณวุฒิอย่างเดียว — และว่าผู้มีความรู้สึกยังมีโอกาสฝึกใหม่ การศึกษาต่อเนื่อง และการสนับสนุนการเปลี่ยนผ่านที่ใช้ได้ในที่ที่ความสามารถที่ถูกขอเปลี่ยนอย่างเป็นสาระหรือไม่ การประเมินต้องทดสอบความโปร่งใส ความสามารถในการตรวจ และความสามารถในการโต้แย้งของตรรกะการจัดอันดับ การประเมิน คำแนะนำ และการจัดวางที่มีผลกระทบที่เป็นสาระภายใต้ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*) ปรับตาม [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination) และ [การพึ่งพา](core_05_band_continuity.md#dependency) การประเมินต้องตรวจจับตัวแทนทึบหรือทบทวนไม่ได้ การเฝ้าประตูหลักฐานที่เอาชนะการก่อตัวของขีดความสามารถ ความล้าสมัยที่ถูกบังคับหรือการล็อกที่ลบล้างพลังกระทำการ การออกแบบการเรียนรู้ที่บีบบังคับหรือชักนำ และการแบ่งส่วนที่เอาความสามารถในการโต้แย้งหรือการปรับตลอดชีวิตออกในที่ที่ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ใช้ร่วม การประเมินต้องสะท้อนผลเชิงหน้าที่ ไม่ใช่ป้ายการเข้าถึงในนาม เจตนาทางการศึกษาที่ประกาศ หรือรูปแบบหลักฐานคุณวุฒิเพียงอย่างเดียว

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวตัวกระตุ้นความเป็นสาระของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ที่พึ่ง ขอบเขตการประเมินสำหรับเส้นทางจัดอันดับ ประเมิน แนะนำ จัดวาง กั้นด้วยหลักฐานคุณวุฒิ และฝึกใหม่ที่พึ่งอย่างเป็นสาระ ข้อค้นพบการสร้างขีดความสามารถและเส้นทางฝึกใหม่ ข้อค้นพบความโปร่งใสของการประเมินและความสามารถในการโต้แย้ง ข้อค้นพบต้านตัวแทนและต้านการชักนำในที่ที่เป็นสาระ ความไม่แน่นอน ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบที่กำหนดอื่นในที่ที่ถูกขอ และเงื่อนไข ขีดจำกัดการพึ่ง หรือตัวกระตุ้นการเปิดใหม่ใดที่ผูกกับการเอาชนะขีดความสามารถที่ยืน ความทึบของการประเมิน หรือความล้าสมัยที่ถูกบังคับ

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินขีดความสามารถทางการศึกษาและความครบถ้วนของระบบการเรียนรู้ต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าที่จัดอันดับ ประเมิน แนะนำ จัดวาง หรือกั้นด้วยหลักฐานคุณวุฒิผู้มีความรู้สึกอย่างเป็นสาระในบริบทการศึกษาหรือการฝึกอบรม ต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าสาระการสร้างขีดความสามารถ การเข้าถึงการฝึกใหม่ และความโปร่งใสของระบบการเรียนรู้ถูกประเมิน ไม่ใช่แค่กล่าว

**ข้อบกพร่องและความไม่สอดคล้อง.** การบัง การแสดงผิด การแยกชิ้น หรือการผลักตรรกะการจัดอันดับ การประเมิน คำแนะนำ หรือการจัดวางที่เป็นสาระในที่ที่ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*) ขอการทบทวน; การถือรูปแบบหลักฐานคุณวุฒิ มาตรวัดการจบแบบรวม หรือคำกล่าวของผู้ดำเนินการเองว่าพอโดยไม่มีวิเคราะห์การสร้างขีดความสามารถที่ประเมินได้; การรับรองการพึ่งต่อเนื่องขณะที่ความทึบของการประเมิน การเฝ้าประตูหลักฐาน ความล้าสมัยที่ถูกบังคับ หรือการออกแบบการเรียนรู้ที่ชักนำที่จัดทำเอกสารคุกคามความสอดคล้องทางรัฐธรรมนูญอย่างเป็นสาระ; หรือการใช้กรอบประสิทธิภาพ การทำให้เฉพาะบุคคล หรือขนาดเพื่อเอาชนะการเข้าถึงการฝึกใหม่หรือความสามารถในการโต้แย้งโดยไม่บรรลุวินัยการสร้างขีดความสามารถของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) และวินัยความโปร่งใสของ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*) ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="91-illustrative-educational-capability-application-by-class"></a>

<a id="91-illustrative-educational-capability-application-by-class-non-exhaustive"></a>
#### 9.1 ตัวอย่างการประยุกต์ขีดความสามารถทางการศึกษาตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) ถึง [§8.1](#81-illustrative-accessibility-application-by-class) พาสามระบบเดียวกันผ่านโดเมนประเมินก่อนหน้า หมวดย่อยนี้แสดงว่าการประเมิน **ขีดความสามารถทางการศึกษาและความครบถ้วนของระบบการเรียนรู้** หมายความอย่างไรสำหรับแต่ละระบบ — เส้นทางจัดอันดับ ประเมิน หลักฐานคุณวุฒิ และฝึกใหม่ใดนับ สิ่งที่การรับรองต้องตรวจเมื่อตัวกระตุ้นความเป็นสาระของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ใช้ และสิ่งที่ต้องปรากฏบนบันทึก บทที่ห้าและ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ยังเป็นเจ้าของกฎพลังกระทำการทางการศึกษาและระบบการเรียนรู้ฉบับหลัก; หลักสูตร สารบบหลักฐานคุณวุฒิ รูบริกการประเมิน และแบบการให้ทุนอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การเดินดูเหล่านี้ไม่กำหนดกลไกเหล่านั้น การเข้าถึงที่เท่ากันและการเข้าถึงได้ทางการศึกษายังเป็นของ **มาตรา III-B** (*การเข้าถึงการศึกษาที่เท่ากัน*) และไม่ถูกทำให้แคบที่นี่*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองกั้นว่าใครอาจดำเนินหน้าที่โรงงานที่วิกฤตต่อการอยู่รอดผ่านใบอนุญาตผู้ปฏิบัติ การรับรองความปลอดภัย การประเมินความสามารถ และกฎการฝึกใหม่ตามระเบียบ — เส้นทางออกหลักฐานบทบาทที่ตัดสินว่าผู้มีความรู้สึกสร้างและรักษาขีดความสามารถในการเดินน้ำปลอดภัยได้หรือไม่ และว่าการประเมินเหล่านั้นเห็น ตรวจ และโต้แย้งได้หรือไม่

- **เส้นทางเรียนรู้และหลักฐานคุณวุฒิในขอบเขต:**
  - ใบอนุญาตผู้ปฏิบัติ การต่ออายุ และการระงับ;
  - การรับรองความปลอดภัยและการประเมินความสามารถตอบสนองฉุกเฉิน;
  - การฝึกใหม่ด้านระเบียบและเทเลเมทรีเมื่อเคมี ตรรกะควบคุม หรือข้อกำหนดกำกับเปลี่ยน;
  - การจัดอันดับหรือการจัดวางเข้ากะโรงงาน ล่วงเวลา หรือบทบาทผู้ปฏิบัติหลักตามความสามารถที่ประเมิน;
  - เส้นทางท้าทายและการฝึกเยียวยาสำหรับการประเมินที่ไม่ผ่านหรือหลักฐานคุณวุฒิที่ถูกระงับ
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าเส้นทางเรียนรู้และหลักฐานคุณวุฒิเหล่านั้นผลิตขีดความสามารถที่ใช้ปฏิบัติในการเดินการควบคุมน้ำปลอดภัย — ไม่ใช่สัญลักษณ์หลักฐานคุณวุฒิหรือจำนวนใบรับรองการจบเพียงอย่างเดียว;
  - ว่าผู้ปฏิบัติยังมีการฝึกใหม่และการสนับสนุนการเปลี่ยนผ่านที่ใช้ได้เมื่อความสามารถที่ถูกขอเปลี่ยนอย่างเป็นสาระ;
  - ว่าตรรกะการจัดอันดับ การประเมิน และการกั้นด้วยหลักฐานคุณวุฒิโปร่งใส ตรวจได้ และโต้แย้งได้ภายใต้ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*);
  - ว่าตัวแทนทึบ การเฝ้าประตู หรือความล้าสมัยที่ถูกบังคับเอาชนะการก่อตัวของขีดความสามารถของเจ้าหน้าที่ซึ่งความสามารถกั้นสิ่งจำเป็นต่อการอยู่รอด;
  - ว่าความลึกของการประเมินตรงกับส่วนได้เสีย **Class A** ในที่ที่ผู้ปฏิบัติที่ไม่ผ่านคุณสมบัติหรือถูกปิดกั้นอาจปิดน้ำปลอดภัย; และ
  - ว่าขีดจำกัดการประเมินใดบรรลุสาระการสร้างขีดความสามารถที่จัดทำเอกสาร ไม่ใช่เจตนาทางการศึกษาที่ประกาศเพียงอย่างเดียว
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้นความเป็นสาระของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ที่พึ่ง;
  - ขอบเขตการประเมินสำหรับเส้นทางใบอนุญาต การประเมิน การกั้นด้วยหลักฐานคุณวุฒิ และฝึกใหม่ที่พึ่งอย่างเป็นสาระ;
  - ข้อค้นพบการสร้างขีดความสามารถและเส้นทางฝึกใหม่ที่ความลึก **Class A**;
  - ข้อค้นพบความโปร่งใสของการประเมินและความสามารถในการโต้แย้ง;
  - ข้อค้นพบต้านตัวแทนและต้านการชักนำในที่ที่เป็นสาระ;
  - ความไม่แน่นอน;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับความทึบของการประเมินที่ยืน การเฝ้าประตูหลักฐาน หรือความล้าสมัยที่ถูกบังคับ ในที่ที่การดำเนินงานวิกฤตต่อการอยู่รอดถูกกั้น

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพและพอร์ทัลผู้ร่วมกั้นการปฏิบัติคลินิกและการเข้าถึงการดูแลผ่านการยืนยันหลักฐานคุณวุฒิของผู้ให้บริการคลินิก การจัดอันดับสิทธิพิเศษ การจัดวางโรงพยาบาลหรือคลินิก การฝึกความเป็นส่วนตัวและเบรกกลาส และข้อกำหนดการศึกษาต่อเนื่องที่ตัดสินอย่างเป็นสาระว่าใครอาจปฏิบัติบนเครือข่าย และเจ้าหน้าที่ฝึกใหม่ได้เร็วเพียงใดเมื่อกฎเปลี่ยน

- **เส้นทางเรียนรู้และหลักฐานคุณวุฒิในขอบเขต:**
  - การยืนยันหลักฐานคุณวุฒิของผู้ให้บริการคลินิกและการจัดอันดับสิทธิพิเศษ;
  - ตรรกะการจัดวางโรงพยาบาล คลินิก หรือแพทย์ประจำบ้านที่ผูกกับการแลก;
  - การประเมินการฝึกความเป็นส่วนตัว ความยินยอม และเบรกกลาส;
  - ข้อกำหนดการศึกษาต่อเนื่องและการต่ออายุความสามารถสำหรับการร่วมเครือข่าย;
  - การแนะนำหรือการจัดเส้นทางแบบปรับตัวเข้าสู่โมดูลเฉพาะทาง เส้นทางการศึกษาแพทย์ต่อเนื่อง หรือการฝึกเยียวยา;
  - เส้นทางท้าทายสำหรับสิทธิพิเศษที่ถูกปฏิเสธ การประเมินที่ไม่ผ่าน หรือการรับเข้าที่ถูกปิด
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าเส้นทางหลักฐานคุณวุฒิและการจัดวางผลิตขีดความสามารถคลินิกที่ใช้ปฏิบัติและการร่วมเครือข่าย — ไม่ใช่กล่องติ๊กฝึก HIPAA ในนามหรือแดชบอร์ดการจบเพียงอย่างเดียว;
  - ว่าผู้ให้บริการคลินิกและเจ้าหน้าที่ HIM ยังมีการฝึกใหม่ที่ใช้ได้เมื่อกฎความยินยอม การจัดเส้นทาง หรือการเข้าถึงฉุกเฉินเปลี่ยนอย่างเป็นสาระ;
  - ว่าตรรกะการจัดอันดับ การประเมิน การแนะนำ และการจัดวางโปร่งใส ตรวจได้ และโต้แย้งได้ภายใต้ **มาตรา VI-B** (*การเรียนรู้ตลอดชีวิตและปรับตัวและความสามารถในการโต้แย้ง*);
  - ว่าตัวแทนการใช้ «ความเหมาะสม» หรือเกียรติยศที่ทึบเอาชนะการก่อตัวของขีดความสามารถ หรือล็อกผู้ร่วมเข้าสู่เส้นทางทบทวนไม่ได้;
  - ว่าความลึกของการประเมินตรงกับความวิกฤตดำเนินงาน **Class B** ในที่ที่ตรรกะหลักฐานคุณวุฒิหรือการจัดวางกั้นการเข้าถึงการดูแล การจ้างงาน หรือการปฏิบัติที่ติดกับใบอนุญาต; และ
  - ว่ากรอบประสิทธิภาพหรือการทำให้เฉพาะบุคคลถูกใช้เพื่อเอาชนะความสามารถในการโต้แย้งโดยไม่มีวิเคราะห์การสร้างขีดความสามารถที่ประเมินได้
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้น **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) และขอบเขตเส้นทาง;
  - ข้อค้นพบการสร้างขีดความสามารถและเส้นทางฝึกใหม่สำหรับเส้นทางผู้ให้บริการคลินิกและคลินิก;
  - ข้อค้นพบความโปร่งใสของการประเมินและความสามารถในการโต้แย้ง;
  - ข้อค้นพบต้านตัวแทนและต้านการชักนำในที่ที่เป็นสาระ;
  - ความไม่แน่นอนและข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากสิ่งกีดขวางหลักฐานคุณวุฒิ สิทธิพิเศษ หรือการฝึกจะปิดการจัดเจ้าหน้าที่ฉุกเฉินหรือการปฏิบัติคลินิกภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว หรือเอาชนะการพึ่งดำเนินงานรายวันอย่างเป็นสาระ

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรจัดอันดับ แนะนำ และจัดสรรช่องฝึก การปฐมนิเทศ การศึกษาต่อเนื่อง และลำดับความสำคัญการพัฒนาวิชาชีพข้ามโรงพยาบาล โรงเรียน และหน่วยงานสาธารณะ — แม้แพลตฟอร์มเองไม่ใช่สาธารณูปโภควิกฤตต่อการอยู่รอด

- **เส้นทางเรียนรู้และหลักฐานคุณวุฒิในขอบเขต:**
  - การจองช่องฝึกและการปฐมนิเทศ;
  - การจัดอันดับหรือการแนะนำการศึกษาต่อเนื่องและการพัฒนาวิชาชีพ;
  - การจับคู่รายวิชา กลุ่มรุ่น หรือผู้สอน;
  - การเตือนหมดอายุหลักฐานคุณวุฒิที่ผูกกับคุณสมบัติการเข้าตาราง;
  - ลักษณะที่ได้ที่จัดเส้นทางเจ้าหน้าที่เข้าสู่เส้นทางพรีเมียมหรือเยียวยา;
  - กฎ API หรือนโยบายที่กีดกันสถาบันเล็กกว่าจากขีดความสามารถฝึกที่ชอบ
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าตัวกระตุ้นความเป็นสาระของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ใช้ — รวมในที่ที่อัลกอริทึมประสานแนะนำรายวิชาอย่างเป็นสาระ จัดอันดับการเข้าถึงการพัฒนาวิชาชีพ หรือกั้นช่องฝึกที่หล่อเส้นทางหลักฐานคุณวุฒิหรืออาชีพ;
  - ว่าคำแนะนำและการจัดสรรช่องผลิตการเข้าถึงการสร้างขีดความสามารถ ไม่ใช่สัญลักษณ์หลักฐานคุณวุฒิ;
  - ว่าตรรกะการประเมิน การจัดอันดับ หรือการแนะนำโปร่งใส ตรวจได้ และโต้แย้งได้;
  - ว่าผู้ดำเนินการถือแพลตฟอร์มว่าต่ำกว่าการทบทวนเพราะเป็น **Class C** ขณะที่ผลการจัดเส้นทางฝึกหล่องาน การศึกษา หรือเส้นทางใบอนุญาตอย่างเป็นสาระ; และ
  - ว่า **การเฝ้าการจำแนกใหม่** ถูกขอในที่ที่แพลตฟอร์มกลายเป็นสิ่งจำเป็นต่อการดำเนินงานสำหรับงาน สิทธิพิเศษคลินิก หรือหลักฐานคุณวุฒิการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอด
- **สิ่งที่บันทึกต้องแสดง:**
  - ว่าและทำไมตัวกระตุ้น **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) ใช้;
  - ขอบเขตการประเมินสำหรับเส้นทางจัดอันดับ แนะนำ จัดวาง และฝึกใหม่ตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบการสร้างขีดความสามารถ ความโปร่งใส และความสามารถในการโต้แย้งในที่ที่เป็นสาระ — ไม่ใช่คำกล่าวว่างเปล่าว่าการฝึกเป็น «ทางเลือก»;
  - ข้อค้นพบความกระจุกและจุดคอขวดในที่ที่ผลการจัดเส้นทางฝึกบอกล่วงหน้าการยกระดับ;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่งแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนขีดความสามารถทางการศึกษาที่ยกระดับหากชั้นหรือบทบาทการประสานที่จำเป็นต่อการอยู่รอดเปลี่ยน

**การอ่านข้ามชั้น.** วินัยขีดความสามารถทางการศึกษาของ **มาตรา VI** (*สิทธิในการศึกษาที่ศูนย์กลางผู้มีความรู้สึก*) และบทที่ห้าชุดเดียวกันใช้ในที่ที่ตัวกระตุ้นความเป็นสาระถูกบรรลุ; ชั้นเปลี่ยนความลึกของการประเมิน ไม่ใช่อนุญาตให้ถือรูปแบบหลักฐานคุณวุฒิหรือการประเมินที่ทึบว่าพอ ระบบน้ำ **Class A** ที่ใบอนุญาตผู้ปฏิบัติหรือการประเมินความปลอดภัยอาจปิดการเดินโรงงานอย่างปลอดภัย ต้องถือหลักฐานการสร้างขีดความสามารถ การฝึกใหม่ และความสามารถในการโต้แย้งที่แข็งที่สุดบนบันทึก — ไม่ใช่คำกล่าวนโยบายฝึกทั่วไป การแลก **Class B** ที่สิทธิพิเศษ การจัดวาง หรือตรรกะการศึกษาแพทย์ต่อเนื่องกั้นการปฏิบัติคลินิก ต้องจัดทำเอกสารความโปร่งใสของการประเมินและการเข้าถึงการฝึกใหม่ที่ความวิกฤตดำเนินงาน แพลตฟอร์มตาราง **Class C** ต้องไม่คงย่อหน้าการศึกษาเชิงพิธีขณะที่ตรรกะช่องฝึก คำแนะนำ หรือการจัดเส้นทางหลักฐานคุณวุฒิจัดอันดับหรือกีดกันผู้ร่วมอย่างเป็นสาระ; เมื่อการประสานกลายเป็นสิ่งจำเป็นต่อการดำเนินงานสำหรับงานหรือใบอนุญาต การรับรองต้องยกระดับการทบทวนและการจำแนกใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) รวมขึ้นสู่ **Class A** ในที่ที่หลักฐานคุณวุฒิการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอดถูกกั้น การเดินดูความน่าไว้วางใจสำหรับระบบเดียวกันอยู่ใน [§10.1](#101-illustrative-trustworthiness-application-by-class).

<a id="10-trustworthiness-and-system-reliance-integrity-evaluation"></a>

### 10. การประเมินความน่าไว้วางใจและความครบถ้วนของการพึ่งระบบ

<details>
<summary><strong><span style="color: #2563eb;">ตามรอย</span></strong></summary>

- ต้นทาง: [ส่วน ข §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*เนื้อหาบันทึก*); [§2](#2-system-class-evaluation) (*การประเมินชั้นระบบ*); ตระกูลการวัดการกำกับดูแล (*ความจริงและความครบถ้วนของความรู้; ความน่าไว้วางใจ และการเสื่อมของความไว้วางใจและการพึ่งที่ทำให้เข้าใจผิดในฐานะการวัดทางรัฐธรรมนูญ*); **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*); [ความน่าไว้วางใจ](core_05_band_continuity.md#trustworthiness), [ความไว้วางใจ](core_05_band_continuity.md#trust), [การเสื่อมของความไว้วางใจและการพึ่งที่ทำให้เข้าใจผิด](core_05_band_continuity.md#trust-degradation-and-misleading-reliance), [ความสามารถในการโต้แย้ง](core_05_band_accountability.md#contestability), [การเยียวยาและการแก้ไข](core_05_band_accountability.md#redress-and-remediation-constitutional), [ความสอดคล้องของสิ่งจูงใจ](core_05_band_integrative.md#incentive-alignment), [ความสามารถในการย้อนกลับ](core_05_band_continuity.md#reversibility-constitutional), [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination), [การพึ่งพา](core_05_band_continuity.md#dependency), และ [ความเสี่ยง](core_05_band_continuity.md#risk) (บทที่ห้า).
- ปลายทาง: [§10.1](#101-illustrative-trustworthiness-application-by-class) (*การเดินดูตัวอย่างความน่าไว้วางใจ*); [ส่วน ข §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*ความครบถ้วนของบันทึก*); [ส่วน ข §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*ประตูข้อมูลเข้าที่ตรวจสอบแล้ว*); [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ความไม่สอดคล้องความไว้วางใจเท็จ ความไม่สอดคล้องสิ่งจูงใจบิดเบี้ยว และความไม่สอดคล้องความครบถ้วนของการฟื้น*).
- อ่านคู่กับ: **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) และ **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*) — สิทธิท้าทายและการตรวจยังเป็นของที่นั่น; **มาตรา XII-E** (*ระบบอัตโนมัติสูงและความครบถ้วนของกระบวนการที่เครื่องมือเป็นสื่อ*) ในที่ที่ระบบอัตโนมัติสูงเป็นสื่อเส้นทางปกครองหรือการตรวจสอบอย่างเป็นสาระ; **มาตรา III-A** (*การอยู่รอด*) ในที่ที่การพึ่งระบบต่อเนื่องจะกระทบการเข้าถึงที่จำเป็นต่อการอยู่รอด; [บทที่หนึ่ง §4 ความไว้วางใจ](core_01_a_values_principles.md#4-system-stability-enabler-trust-coordination-integrity) และ [บทที่หนึ่ง §3.2 ความจริง](core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint).
- หมวดย่อย: [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ตัวอย่างการประยุกต์ความน่าไว้วางใจตามชั้น*).

</details>

<br>

*พูดแบบตรง ๆ: เมื่อระบบกระทบอย่างเป็นสาระว่าผู้มีความรู้สึกไว้วางใจสิ่งที่มันกล่าวและทำได้หรือไม่ — และผลักกลับเมื่อความไว้วางใจนั้นล้ม — การรับรองต้องตรวจว่าการพึ่งมีเหตุจริง ถูกเปิดเผยอย่างซื่อ และซ่อมได้หรือไม่ มาตรวัดความพึ่งได้และการออกแบบชุดทดสอบอยู่ในตราสารอื่น; การรับรองตรวจว่าความน่าไว้วางใจ ความเสี่ยงความไว้วางใจเท็จ และเส้นทางท้าทายถูกประเมินจริงในที่ที่ตัวกระตุ้นใช้ ตัวอย่างทำงานสำหรับระบบตัวอย่างใน [§2.1](#21-illustrative-class-profiles-non-exhaustive) อยู่ใน [§10.1](#101-illustrative-trustworthiness-application-by-class).*

**ตัวกระตุ้นความเป็นสาระ.** หมวดนี้ใช้ในที่ที่ระบบที่มีผลกระทบที่เป็นสาระหล่อการพึ่งของผู้มีความรู้สึกต่อความประพฤติที่แสดง ขีดจำกัด ความเสี่ยง เส้นทางท้าทาย หรือการแก้ไขอย่างเป็นสาระ — รวมผ่านคำกล่าวความพึ่งได้ ท่าทางการเปิดเผย ความประพฤติดำเนินงาน การออกแบบสิ่งจูงใจ วิธีฟื้น หรือเส้นทางการพึ่งที่เทียบได้ มันไม่ขอการตรวจความน่าไว้วางใจเต็มบนบันทึกการรับรองทุกฉบับ

การรับรองความสอดคล้องของระบบต้องประเมิน **ความน่าไว้วางใจและความครบถ้วนของการพึ่งระบบ** ภายใต้ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) [ความน่าไว้วางใจ](core_05_band_continuity.md#trustworthiness) และ [การเสื่อมของความไว้วางใจและการพึ่งที่ทำให้เข้าใจผิด](core_05_band_continuity.md#trust-degradation-and-misleading-reliance) ในที่ที่ตัวกระตุ้นความเป็นสาระใช้ ความหมายฉบับหลัก ปัจจัยประเมิน และวินัยการไม่ปฏิบัติตามอยู่ในบทที่ห้าและ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*); มาตรวัดความพึ่งได้ รูปแบบการเปิดเผย กลไกความสอดคล้องของสิ่งจูงใจ และการออกแบบการทดสอบถดถอยอยู่ในตราสารที่รับเข้าในที่ที่ใช้ได้ หมวดนี้กล่าวว่าการรับรองต้องยืนยันและบันทึกอะไร ไม่กล่าวซ้ำกลไกดำเนินงานเหล่านั้นและไม่กำหนดมาตรวัดความพึ่งได้หรือการออกแบบชุดทดสอบเฉพาะ

**ข้อกำหนดการประเมิน.** กระบวนการรับรองต้องวินิจฉัยว่าเส้นทางที่ระบบพึ่งอย่างเป็นสาระรักษาเงื่อนไขของ [ความไว้วางใจ](core_05_band_continuity.md#trust) ที่มีเหตุและการพึ่งที่แม่นพอสมควรภายใต้ **มาตรา XII-A** (*เส้นฐานความพึ่งได้และความน่าไว้วางใจ*) — ไม่ใช่ชื่อเสียง ขนาด หรือท่าทางการตลาดเพียงอย่างเดียว การประเมินต้องทดสอบการท้าทาย การทบทวน และการเยียวยาที่ใช้ปฏิบัติได้ภายใต้ **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) ความเสี่ยงความไว้วางใจเท็จและการพึ่งที่ทำให้เข้าใจผิดภายใต้ **มาตรา XII-C** (*ห้ามความไว้วางใจเท็จและการพึ่งพาที่ทำให้เข้าใจผิด*) การเปิดรับสิ่งจูงใจบิดเบี้ยวภายใต้ **มาตรา XII-D** (*ข้อจำกัดความสอดคล้องของสิ่งจูงใจ*) และความครบถ้วนของการฟื้นภายใต้ **มาตรา XII-F** (*เส้นฐานความยืดหยุ่นคืนตัวและการซ่อมตนเอง*) ในที่ที่เป็นสาระ ปรับตาม [การกำหนดความเป็นสาระ](core_05_band_oversight.md#materiality-determination) [การพึ่งพา](core_05_band_continuity.md#dependency) และ [ความเสี่ยง](core_05_band_continuity.md#risk) การประเมินต้องตรวจจับความไว้วางใจที่ถูกผลิต ขีดจำกัดที่ไม่เปิดเผย โครงสร้างสิ่งจูงใจที่ให้รางวัลการหลอกลวงหรือการตัดมุม เส้นทางท้าทายที่มีอยู่บนกระดาษอย่างเดียว และวิธีฟื้นที่ซ่อนความล้มเหลวหรือทำให้สิทธิแคบลงอย่างเงียบ การประเมินต้องสะท้อนผลเชิงหน้าที่ข้ามเวลา ขนาด และการพึ่ง ไม่ใช่ป้ายการประกันในนาม เจตนาที่ประกาศ หรือผลงานก่อนหน้าเพียงอย่างเดียว

**ข้อกำหนดบันทึก.** บันทึกการรับรองต้องกล่าวตัวกระตุ้นความเป็นสาระของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ที่พึ่ง ขอบเขตการประเมินสำหรับเส้นทางการพึ่ง การเปิดเผย สิ่งจูงใจ การท้าทาย และการฟื้นที่พึ่งอย่างเป็นสาระ ข้อค้นพบความน่าไว้วางใจและความไว้วางใจเท็จ ข้อค้นพบสิ่งจูงใจบิดเบี้ยวและความครบถ้วนของการฟื้นในที่ที่เป็นสาระ ความไม่แน่นอน ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบที่กำหนดอื่นในที่ที่ถูกขอ และเงื่อนไข ขีดจำกัดการพึ่ง หรือตัวกระตุ้นการเปิดใหม่ใดที่ผูกกับการเอาชนะความไว้วางใจที่ยืน การพึ่งที่ทำให้เข้าใจผิด หรือการเยียวยาที่เข้าไม่ถึง

**การปรับร่วมตามชั้นระบบ.** ความลึกของการประเมินความน่าไว้วางใจและความครบถ้วนของการพึ่งระบบต้องปรับตามชั้นระบบที่กำหนดภายใต้ [§2](#2-system-class-evaluation) และ [ส่วนได้เสียที่เป็นสาระ](core_00_preamble.md#material-stake) ระบบชั้นสูงกว่าที่หล่อการพึ่งของผู้มีความรู้สึกอย่างเป็นสาระ ต้องการหลักฐานที่แข็งกว่าตามสัดส่วนว่าความน่าไว้วางใจ ความเสี่ยงความไว้วางใจเท็จ และเส้นทางท้าทายถูกประเมิน ไม่ใช่แค่กล่าว

**ข้อบกพร่องและความไม่สอดคล้อง.** การบัง การแสดงผิด การแยกชิ้น หรือการผลักขีดจำกัด ความเสี่ยง หรือประวัติความล้มเหลวที่เป็นสาระในที่ที่ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ขอการทบทวน; การถือชื่อเสียง การรับรอง ขนาด หรือคำกล่าวของผู้ดำเนินการเองว่าพอโดยไม่มีวิเคราะห์ [ความน่าไว้วางใจ](core_05_band_continuity.md#trustworthiness) ที่ประเมินได้; การรับรองการพึ่งต่อเนื่องขณะที่ความไว้วางใจเท็จ สิ่งจูงใจบิดเบี้ยว เส้นทางท้าทายที่เข้าไม่ถึง หรือวิธีฟื้นที่ซ่อนความล้มเหลวที่จัดทำเอกสารคุกคามความสอดคล้องทางรัฐธรรมนูญอย่างเป็นสาระ; หรือการใช้กรอบประสิทธิภาพ นวัตกรรม หรือความมั่นคงเพื่อเอาชนะการเปิดเผย ความสามารถในการโต้แย้ง หรือการเยียวยาโดยไม่บรรลุวินัยความพึ่งได้ของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) และวินัยการท้าทายของ **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) ต้องถูกปฏิบัติเป็นข้อบกพร่องการรับรอง อาจรองรับการรับรู้มีเงื่อนไข การรับรู้ที่เลื่อน การไม่รับรู้ การถอน หรือการเปิดใหม่ภายใต้ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)

<a id="101-illustrative-trustworthiness-application-by-class"></a>

<a id="101-illustrative-trustworthiness-application-by-class-non-exhaustive"></a>
#### 10.1 ตัวอย่างการประยุกต์ความน่าไว้วางใจตามชั้น (ไม่ใช่รายการครบ)

*พูดแบบตรง ๆ: [§3.8](#38-illustrative-whole-system-application-by-class) ถึง [§9.1](#91-illustrative-educational-capability-application-by-class) พาสามระบบเดียวกันผ่านโดเมนประเมินก่อนหน้า หมวดย่อยนี้แสดงว่าการประเมิน **ความน่าไว้วางใจและความครบถ้วนของการพึ่งระบบ** หมายความอย่างไรสำหรับแต่ละระบบ — เส้นทางการพึ่ง การเปิดเผย สิ่งจูงใจ การท้าทาย และการฟื้นใดนับ สิ่งที่การรับรองต้องตรวจเมื่อตัวกระตุ้นความเป็นสาระของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ใช้ และสิ่งที่ต้องปรากฏบนบันทึก บทที่ห้าและ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ยังเป็นเจ้าของกฎความน่าไว้วางใจฉบับหลัก; มาตรวัดความพึ่งได้ รูปแบบการเปิดเผย กลไกความสอดคล้องของสิ่งจูงใจ และการออกแบบการทดสอบถดถอยอาจอยู่ในตราสารอื่น การเพิ่มคลังข้อความภายหลัง หรือตราสารการรับเอามาใช้; การเดินดูเหล่านี้ไม่กำหนดกลไกเหล่านั้น สิทธิท้าทายและการตรวจยังเป็นของ **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) และ **มาตรา XV** (*การตรวจ ความโปร่งใส และการตรวจสอบอิสระ*) — ไม่ถูกทำให้แคบที่นี่*

**Class A — การควบคุมและเทเลเมทรีน้ำดื่มปลอดภัยของเทศบาล.** ระบบบำบัดและจ่ายที่เป็นของเมืองหล่อว่าครัวเรือน ผู้ปฏิบัติ และผู้ตอบสนองฉุกเฉินพึ่งคุณภาพน้ำที่แสดง สถานะเหตุขัดข้อง การเตือนการปนเปื้อน และความประพฤติควบคุมได้หรือไม่ — เส้นทางที่การพึ่งที่ทำให้เข้าใจผิดอาจปิดน้ำปลอดภัยก่อนที่สิ่งทดแทนที่ใช้ได้จะมาถึง

- **เส้นทางการพึ่งในขอบเขต:**
  - คำกล่าวความแม่นของเทเลเมทรีและ **SCADA** (การควบคุมกำกับและการได้ข้อมูล);
  - คำเตือนต้มน้ำและการปนเปื้อน;
  - การตรวจจับรั่วและการส่งสัญญาณสูญเสียความดัน;
  - ความประพฤติล้มอย่างปลอดภัยและการลบล้างด้วยมือ;
  - การแสดงการเฝ้าของ **SOC** (ศูนย์ปฏิบัติการความมั่นคง) ของผู้ขาย;
  - การจัดเส้นทางเชื่อมต่อฉุกเฉินและความช่วยเหลือร่วมกัน;
  - กรอบเวลาการแจ้งเหตุขัดข้องและการคืนบริการ;
  - การฟื้นและการซ่อมตนเองหลังการปนเปื้อน เหตุไซเบอร์ หรือความล้มเหลวของอุปกรณ์;
  - โครงสร้างสิ่งจูงใจที่ผูกกับการเลื่อนการบำรุง โบนัสผู้ขาย หรือการเรียกเก็บจากผู้ใช้อัตรา
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าความประพฤติ ขีดจำกัด และโหมดความล้มเหลวที่แสดงรองรับ [ความไว้วางใจ](core_05_band_continuity.md#trust) ที่มีเหตุภายใต้ **มาตรา XII-A** (*เส้นฐานความพึ่งได้และความน่าไว้วางใจ*) — ไม่ใช่ชื่อเสียง ขนาด หรือท่าทาง «วิธีปฏิบัติสาธารณูปโภคที่ดีที่สุด» เพียงอย่างเดียว;
  - ว่าความเสี่ยงความไว้วางใจเท็จและ [การเสื่อมของความไว้วางใจและการพึ่งที่ทำให้เข้าใจผิด](core_05_band_continuity.md#trust-degradation-and-misleading-reliance) ถูกประเมินในที่ที่ความเสี่ยงการปนเปื้อนที่ถูกทำให้ต่ำ คำเตือนที่ล่าช้า หรือความซ้ำซ้อนที่ถูกทำให้สูงเกินไปอาจทำให้ครัวเรือนและผู้ปฏิบัติเข้าใจผิด;
  - ว่าเส้นทางท้าทาย ทบทวน และเยียวยาที่ใช้ปฏิบัติได้มีอยู่ภายใต้ **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) สำหรับค่าที่ถูกโต้แย้ง การเตือนที่พลาด หรือความล้มเหลวของการฟื้น;
  - ว่าการเปิดรับสิ่งจูงใจบิดเบี้ยวภายใต้ **มาตรา XII-D** (*ข้อจำกัดความสอดคล้องของสิ่งจูงใจ*) ให้รางวัลการเลื่อนการบำรุง การตัดมุมของผู้ขาย หรือการกดการเตือน;
  - ว่าความครบถ้วนของการฟื้นภายใต้ **มาตรา XII-F** (*เส้นฐานความยืดหยุ่นคืนตัวและการซ่อมตนเอง*) เปิดเผยประวัติความล้มเหลวและท่าทางการซ่อมอย่างซื่อ แทนที่จะซ่อนเหตุการณ์;
  - ว่าความลึกของการประเมินตรงกับส่วนได้เสีย **Class A** ในที่ที่การพึ่งที่ทำให้เข้าใจผิดอาจปิดน้ำปลอดภัย; และ
  - ว่าขีดจำกัดการประกันใดบรรลุวิเคราะห์ความน่าไว้วางใจที่จัดทำเอกสาร ไม่ใช่เจตนาที่ประกาศเพียงอย่างเดียว
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้นความเป็นสาระของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ที่พึ่ง;
  - ขอบเขตการประเมินสำหรับเส้นทางการพึ่ง การเปิดเผย สิ่งจูงใจ การท้าทาย และการฟื้นที่พึ่งอย่างเป็นสาระ;
  - ข้อค้นพบความน่าไว้วางใจและความไว้วางใจเท็จที่ความลึก **Class A**;
  - ข้อค้นพบสิ่งจูงใจบิดเบี้ยวและความครบถ้วนของการฟื้นในที่ที่เป็นสาระ;
  - ความไม่แน่นอน;
  - ข้อค้นพบเวทีผู้มีความรู้สึกหรือส่วนประกอบอื่นในที่ที่ถูกขอ; และ
  - เงื่อนไขหรือตัวกระตุ้นการเปิดใหม่ที่ผูกกับการเอาชนะความไว้วางใจที่ยืน การพึ่งที่ทำให้เข้าใจผิด หรือการเยียวยาที่เข้าไม่ถึง ในที่ที่การเข้าถึงน้ำที่จำเป็นต่อการอยู่รอดถูกกั้น

**Class B — การแลกบันทึกคลินิกระดับภูมิภาค.** การแลกสารสนเทศสุขภาพและพอร์ทัลผู้ร่วมหล่อว่าผู้ให้บริการคลินิก ผู้ป่วย และผู้กระทำสาธารณสุขพึ่งเวลาทำงานที่แสดง การจับคู่บันทึก การจัดเส้นทางความยินยอม การเข้าถึงเบรกกลาส และความประพฤติการฟื้นได้หรือไม่ — เส้นทางที่กั้นการดำเนินงานดูแลรายวัน และอาจทำให้การดูแลฉุกเฉินเข้าใจผิดภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอด

- **เส้นทางการพึ่งในขอบเขต:**
  - การแสดงเวลาทำงาน ความหน่วง และความแม่นของการจับคู่;
  - ความประพฤติการจัดเส้นทางความยินยอมและเบรกกลาส;
  - คำกล่าวความพึ่งได้ของการคลี่อัตลักษณ์และการกำจัดซ้ำ;
  - การแจ้งเหตุขัดข้องและท่าทางการสลับเมื่อล้ม;
  - การเปิดเผยเหตุการณ์และกรอบเวลาการฟื้นหลังเหตุขัดข้อง;
  - โครงสร้างสิ่งจูงใจของผู้ขายและผู้ดำเนินการที่ผูกกับปริมาณธุรกรรม ความเร็วการรับเข้า หรือการกดการเตือน;
  - เส้นทางท้าทายสำหรับบันทึกผิด การเข้าถึงที่ถูกปิด หรือคำตัดสินจัดเส้นทางที่ถูกโต้แย้ง
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าความประพฤติและขีดจำกัดที่แสดงรองรับการพึ่งที่มีเหตุสำหรับการดำเนินงานคลินิกรายวัน — ไม่ใช่การตลาดการทำงานร่วมกันหรือแดชบอร์ดเวลาทำงานแบบรวมเพียงอย่างเดียว;
  - ว่าความเสี่ยงความไว้วางใจเท็จถูกประเมินในที่ที่ความผิดพลาดการจับคู่ที่ถูกทำให้ต่ำ ความล้มเหลวความยินยอมที่ซ่อน หรือความพร้อมการเข้าถึงฉุกเฉินที่ถูกทำให้สูงเกินไปอาจทำให้ผู้ให้บริการคลินิกและผู้ป่วยเข้าใจผิด;
  - ว่าเส้นทางท้าทาย ทบทวน และเยียวยาภายใต้ **มาตรา XII-B** (*สิทธิในการท้าทาย ทบทวน และเยียวยา*) ใช้ปฏิบัติได้สำหรับข้อโต้แย้งบันทึกผิด พอร์ทัลที่ถูกปิด และความล้มเหลวของการฟื้น — ไม่ใช่นโยบายบนกระดาษอย่างเดียว;
  - ว่าการเปิดรับสิ่งจูงใจบิดเบี้ยวภายใต้ **มาตรา XII-D** (*ข้อจำกัดความสอดคล้องของสิ่งจูงใจ*) ให้รางวัลการเติบโตของปริมาณ การทำให้การเตือนน้อยลง หรือการล็อกผู้ขายเหนือการจัดเส้นทางที่แม่น;
  - ว่าความครบถ้วนของการฟื้นภายใต้ **มาตรา XII-F** (*เส้นฐานความยืดหยุ่นคืนตัวและการซ่อมตนเอง*) เปิดเผยประวัติเหตุขัดข้องและความเสี่ยงคงเหลืออย่างซื่อ;
  - ว่าความลึกของการประเมินตรงกับความวิกฤตดำเนินงาน **Class B** ในที่ที่การพึ่งที่ทำให้เข้าใจผิดกั้นการเข้าถึงการดูแล การจ้างงาน หรือการปฏิบัติที่ติดกับใบอนุญาต; และ
  - ว่ากรอบประสิทธิภาพหรือความมั่นคงถูกใช้เพื่อเอาชนะการเปิดเผยหรือความสามารถในการโต้แย้งโดยไม่มีวิเคราะห์ความน่าไว้วางใจที่ประเมินได้
- **สิ่งที่บันทึกต้องแสดง:**
  - ตัวกระตุ้น **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) และขอบเขตเส้นทาง;
  - ข้อค้นพบความน่าไว้วางใจและความไว้วางใจเท็จสำหรับเส้นทางคลินิกและพอร์ทัล;
  - ข้อค้นพบสิ่งจูงใจบิดเบี้ยวและความครบถ้วนของการฟื้นที่ความลึก **Class B**;
  - ข้อค้นพบเส้นทางท้าทายและการเยียวยาในที่ที่เป็นสาระ;
  - ความไม่แน่นอนและข้อค้นพบส่วนประกอบในที่ที่ถูกขอ; และ
  - ตัวกระตุ้นการเปิดใหม่หากการแสดงเวลาทำงาน การจับคู่ หรือการเข้าถึงฉุกเฉินจะทำให้การจัดเส้นทางดูแลเข้าใจผิดภายในกรอบเวลาที่เกี่ยวข้องกับการอยู่รอดแล้ว หรือเอาชนะการพึ่งดำเนินงานรายวันอย่างเป็นสาระ

**Class C — แพลตฟอร์มตารางและการประสานระหว่างสถาบัน.** ชั้นตารางหลายองค์กรหล่อว่าสถาบันและเจ้าหน้าที่พึ่งความพร้อมที่แสดง ความแม่นของการจัดเส้นทาง คะแนนความพึ่งได้ของผู้ขาย และการฟื้นจากเหตุขัดข้องหรือไม่ — แม้แพลตฟอร์มเองไม่ใช่สาธารณูปโภควิกฤตต่อการอยู่รอด

- **เส้นทางการพึ่งในขอบเขต:**
  - คำกล่าวการจัดเส้นทางกะและความพร้อมเวรเรียก;
  - การแสดงความพึ่งได้ของการจองห้อง อุปกรณ์ และผู้ขาย;
  - ป้าย «พร้อมเสมอ» หรือเวลาทำงาน;
  - ลักษณะความพึ่งได้หรือการให้คะแนนผู้ขายที่ได้ที่หล่อความประพฤติของสถาบัน;
  - การแจ้งเหตุขัดข้องและท่าทางการสลับเมื่อล้ม;
  - โครงสร้างสิ่งจูงใจที่ผูกกับปริมาณการจอง ค่านายหน้าผู้ขาย หรือการทำให้การเตือนน้อยลง;
  - เส้นทางท้าทายและเยียวยาสำหรับกะที่พลาด การจองซ้ำ หรือความผิดพลาดการจัดเส้นทางผู้ขาย
- **สิ่งที่การประเมินต้องทดสอบ:**
  - ว่าตัวกระตุ้นความเป็นสาระของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ใช้ — รวมในที่ที่คำกล่าวความพึ่งได้ คะแนนผู้ขาย หรือความประพฤติประสานหล่อการจัดเจ้าหน้าที่ การจัดเส้นทางฉุกเฉิน หรือคำตัดสินจัดซื้ออย่างเป็นสาระ;
  - ว่าความเสี่ยงความไว้วางใจเท็จและการพึ่งที่ทำให้เข้าใจผิดถูกประเมินในที่ที่ท่าทางการตลาด ป้ายความไว้วางใจ หรือประวัติเหตุขัดข้องที่ถูกทำให้ต่ำอาจทำให้สถาบันเข้าใจผิด;
  - ว่าเส้นทางท้าทายและเยียวยาใช้ปฏิบัติได้สำหรับความผิดพลาดตารางที่กระทบงาน การศึกษา หรือการเข้าถึงบริการสาธารณะอย่างเป็นสาระ;
  - ว่าผู้ดำเนินการถือแพลตฟอร์มว่าต่ำกว่าการทบทวนเพราะเป็น **Class C** ขณะที่การแสดงความพึ่งได้หล่อความประพฤติของสถาบันอย่างเป็นสาระ;
  - ว่าการเปิดรับสิ่งจูงใจบิดเบี้ยวให้รางวัลความลำเอียงต่อผู้ขาย การกดการเตือน หรือความกระจุกเหนือการประสานที่แม่น; และ
  - ว่า **การเฝ้าการจำแนกใหม่** ถูกขอในที่ที่แพลตฟอร์มกลายเป็นจุดคอขวดโดยพฤตินัยสำหรับการจัดเจ้าหน้าที่ที่จำเป็นต่อการอยู่รอด การจัดเส้นทางฉุกเฉิน หรือการประสานการจ่าย
- **สิ่งที่บันทึกต้องแสดง:**
  - ว่าและทำไมตัวกระตุ้น **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) ใช้;
  - ขอบเขตการประเมินสำหรับเส้นทางการพึ่ง การเปิดเผย สิ่งจูงใจ การท้าทาย และการฟื้นตามสัดส่วนกับความเสี่ยงการประสาน **Class C**;
  - ข้อค้นพบความน่าไว้วางใจและความไว้วางใจเท็จในที่ที่เป็นสาระ — ไม่ใช่คำกล่าวว่างเปล่าว่าแพลตฟอร์ม «พึ่งได้»;
  - ข้อค้นพบสิ่งจูงใจบิดเบี้ยวและความครบถ้วนของการฟื้นในที่ที่เป็นสาระ;
  - ข้อค้นพบความกระจุกและจุดคอขวดในที่ที่คำกล่าวความพึ่งได้บอกล่วงหน้าการยกระดับ;
  - **การเฝ้าการจำแนกใหม่** ที่ชัดในที่ที่การพึ่งแข็งขึ้น; และ
  - ตัวชี้ไปยังการทบทวนความน่าไว้วางใจที่ยกระดับหากชั้นหรือบทบาทการประสานที่จำเป็นต่อการอยู่รอดเปลี่ยน

**การอ่านข้ามชั้น.** วินัยความน่าไว้วางใจของ **มาตรา XII** (*สิทธิในระบบที่พึ่งได้และน่าไว้วางใจ*) และบทที่ห้าชุดเดียวกันใช้ในที่ที่ตัวกระตุ้นความเป็นสาระถูกบรรลุ; ชั้นเปลี่ยนความลึกของการประเมิน ไม่ใช่อนุญาตให้ถือชื่อเสียง ขนาด หรือป้ายการประกันในนามว่าพอ ระบบน้ำ **Class A** ที่เทเลเมทรี คำเตือน หรือการแสดงการฟื้นอาจทำให้ครัวเรือนและผู้ปฏิบัติเข้าใจผิดเรื่องน้ำปลอดภัย ต้องถือหลักฐานความน่าไว้วางใจ ความไว้วางใจเท็จ และความครบถ้วนของการฟื้นที่แข็งที่สุดบนบันทึก — ไม่ใช่คำกล่าวความพึ่งได้ทั่วไป การแลก **Class B** ที่การแสดงเวลาทำงาน การจับคู่ หรือเบรกกลาสกั้นการปฏิบัติคลินิก ต้องจัดทำเอกสารข้อค้นพบเส้นทางท้าทายและการพึ่งที่ทำให้เข้าใจผิดที่ความวิกฤตดำเนินงาน แพลตฟอร์มตาราง **Class C** ต้องไม่คงย่อหน้าความน่าไว้วางใจเชิงพิธีขณะที่ป้ายความพึ่งได้หรือคะแนนผู้ขายหล่อความประพฤติการจัดเจ้าหน้าที่หรือการจัดซื้ออย่างเป็นสาระ; เมื่อการประสานกลายเป็นสิ่งจำเป็นต่อการอยู่รอด การรับรองต้องยกระดับการทบทวนและการจำแนกใหม่ภายใต้ [§2](#2-system-class-evaluation) และ [ส่วน ข §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) รวมขึ้นสู่ **Class A** ในที่ที่การพึ่งที่ทำให้เข้าใจผิดอาจปิดการประสานที่จำเป็นต่อการอยู่รอด
<br>

*ต่อไปยังบันทึก กระบวนการเวที และสะพานร่องรอย:* [บทที่เจ็ด ส่วน ข — บันทึกและกระบวนการ](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) ([§11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) ถึง [§16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)).
---

**ไฟล์ก่อนหน้า (ภาษานี้):** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)

**ไฟล์ถัดไป (ภาษานี้):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)

**ต้นฉบับที่มีผลผูกพัน:** [core_07_a_system_alignment_certification_evaluation.md](../../core_08_a_system_alignment_certification_evaluation.md)
