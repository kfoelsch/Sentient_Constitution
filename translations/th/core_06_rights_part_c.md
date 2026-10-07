# บทที่หก: สิทธิขั้นพื้นฐาน

<details>
<summary><strong><span style="color: #2563eb;">ตำแหน่งในคลังเอกสาร (ไม่มีผลเชิงปฏิบัติการ): โครงสร้างไฟล์และหลักการอ่าน</span></strong></summary>

> เนื้อหาต่อไปนี้เป็น **คำแนะนำสำหรับผู้อ่านเท่านั้น** ไม่เพิ่ม ลบ หรือจำกัดหน้าที่ที่มีผลผูกพันซึ่งระบุไว้ที่อื่นในไฟล์นี้หรือในบทอื่น
>
> ไฟล์นี้ **เป็นส่วนหนึ่งของรัฐธรรมนูญผู้มีความรู้สึก** และ **มีผลผูกพันเมื่ออ่านร่วมกับ** ไฟล์ `core_*` ที่มีหมายเลขอื่น ๆ ในฐานะตราสารฉบับเดียวเท่านั้น ไฟล์นี้ประกอบด้วย **บทที่หก ส่วน C**; เลขข้อและการอ้างอิงข้ามสอดคล้องกับตราสารฉบับบูรณาการ ลำดับการอ่าน การแยกเนื้อหาที่มีผลผูกพันกับเนื้อหาสนับสนุน และข้อมูลรุ่นของคลังเอกสารระบุไว้ใน [README.md](README.md)

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำแนะนำสำหรับผู้อ่าน (ไม่มีผลเชิงปฏิบัติการ): ตำแหน่งของส่วน C ในบทที่หก</span></strong></summary>

> เนื้อหาต่อไปนี้เป็น **คำแนะนำสำหรับผู้อ่านเท่านั้น** ไม่เพิ่ม ลบ หรือจำกัดหน้าที่ที่มีผลผูกพันซึ่งระบุไว้ที่อื่นในบทนี้หรือในบทอื่น
>
> **ส่วน A** ใน [core_06_rights_part_a.md](core_06_rights_part_a.md) ประกอบด้วยชุดข้อจำกัดตั้งต้นที่ใช้ทั่วทั้งบท ลำดับการอ่านที่ให้โลกเป็นอันดับแรก และศูนย์กลางการตีความ **ส่วน C** นำเสนอ **ข้อ XIII–XVIII** ตามลำดับนั้น

</details>

<br>

<a id="part-c-trustworthy-systems-security-and-force-limits-information-integrity-verification-lifecycle-and-sandboxed-innovation"></a>
### ส่วน C: ระบบที่น่าเชื่อถือ ความปลอดภัยและข้อจำกัดด้านกำลัง ความสมบูรณ์ของข้อมูล การตรวจสอบ วงจรชีวิต และนวัตกรรมแบบแซนด์บ็อกซ์

<br>

*ในแง่ทั่วไป: ส่วน C ครอบคลุมถึงระบบที่น่าเชื่อถือ ความปลอดภัยและข้อจำกัดด้านกำลัง ความสมบูรณ์ของข้อมูล การตรวจสอบ ระเบียบวินัยในวงจรชีวิต และนวัตกรรมแบบแซนด์บ็อกซ์ — มาตรา XIII ถึง XVIII*

<details>
<summary><strong><span style="color: #2563eb;">คำแนะนำสำหรับผู้อ่าน (ไม่ใช้งาน): แผนที่บทความส่วน C</span></strong></summary>

> โดยมีเนื้อหาดังต่อไปนี้ **คำแนะนำของผู้อ่านเท่านั้น**. จะไม่เพิ่ม ลบ หรือจำกัดภาระผูกพันที่มีผลผูกพันในส่วนอื่นของบทนี้หรือในบทอื่น ๆ
>
> **แผนที่เครื่องอ่าน (ไม่ทำงาน)** แผนภูมินี้แสดงให้เห็นว่าแหล่งที่มาจัดกลุ่มบทความและบทความย่อยในส่วนนี้อย่างไร ตารางคือการจัดกลุ่มแหล่งที่มา ไม่ใช่ลำดับกระบวนการ: บทความไม่ใช่ขั้นตอนตามขั้นตอน ดังนั้นแผนที่จึงไม่มีลูกศร ป้ายกำกับบทความย่อยจะถูกย่อให้เหลือเพียงธีม บทความที่มีหมายเลขและบทความย่อยด้านล่างจะควบคุม แผนภูมิไม่ได้เพิ่มคำจำกัดความหรือหน้าที่ ไม่มีการกำหนดลำดับความสำคัญ และไม่สามารถแทนที่ข้อความต้นฉบับได้

</details>

<br>

```mermaid
flowchart TB
    C0["ส่วน ค<br/><br/>ระบบที่เชื่อถือได้ ความปลอดภัยและการจำกัดกำลัง<br/>ความสมบูรณ์ของข้อมูล การตรวจสอบ วงจรชีวิต และนวัตกรรมแบบแซนด์บ็อกซ์"]
    subgraph Cgrid[" "]
        direction TB
        subgraph Crow1["มาตรา XIII–XIV"]
            C1["มาตรา XIII · สิทธิในระบบที่เชื่อถือได้และเชื่อถือได้<br/><br/>• พื้นฐานความน่าเชื่อถือ<br/>• ท้าทาย ทบทวน และแก้ไข<br/>• ขีดจำกัดความไว้วางใจที่ผิดพลาด<br/>• การจัดตำแหน่งสิ่งจูงใจ<br/>• ความสมบูรณ์ของกระบวนการที่มีความเป็นอิสระสูง<br/>• ความยืดหยุ่นและการเยียวยาตนเอง"]
            C2["มาตรา XIV · ความมั่นคง ความฉลาด พลัง และระบบบังคับบังคับอัตโนมัติ<br/><br/>• ขีดจำกัดอำนาจแอบแฝง<br/>• การใช้กำลังและความขัดแย้งทางอาวุธ<br/>• ระบบอันตรายถึงชีวิตและบังคับขู่เข็ญอัตโนมัติ"]
        end
        subgraph Crow2["บทความที่ 15–16"]
            C3["มาตรา XV · ความสมบูรณ์ของขอบเขตข้อมูล<br/><br/>• เสียงข้างมากและการต่อต้านการผูกขาด<br/>• ความโปร่งใสและความสามารถในการแข่งขัน<br/>• การตรวจสอบความถูกต้อง การรายงาน และการดูแลทางญาณ"]
            C4["มาตรา XVI · การตรวจสอบ ความโปร่งใส และการพิสูจน์ยืนยันที่เป็นอิสระ<br/><br/>• หลักฐานที่สังเกตได้<br/>• การกำกับดูแลแบบกระจาย<br/>• การตรวจสอบที่สามารถเข้าถึงได้"]
        end
        subgraph Crow3["มาตรา XVII–XVIII"]
            C5["มาตรา XVII · วงจรชีวิตระบบ สภาพแวดล้อม และการพลิกกลับได้<br/><br/>• การแยกสิ่งแวดล้อม<br/>• การใช้งานแบบก้าวหน้าและการพลิกกลับได้<br/>• การจำแนกประเภทที่ไม่ถูกต้องและการหลีกเลี่ยงผลที่ตามมา"]
            C6["มาตรา XVIII · นวัตกรรมแบบแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์<br/><br/>• ขอบเขตแซนด์บ็อกซ์<br/>• การบรรจุ การเปิดเผย และการเลือกใช้<br/>• การเปลี่ยนผ่านไปสู่ระบอบการปกครองที่มีภาระผูกพันสูงกว่า<br/>• รางวัลนวัตกรรมและการต่อต้านสิ่งที่แนบมา<br/>• ความสมบูรณ์ของการเผยแพร่ การทบทวน และการจำลองแบบ"]
        end
    end
    %%ลิงก์ที่มองไม่เห็นบังคับให้มีตารางสองกว้าง: แต่ละลิงก์จะทำให้เป้าหมายลดลงหนึ่งระดับ
    C0 ~~~ C1 & C2
    C1 ~~~ C3
    C2 ~~~ C4
    C3 ~~~ C5
    C4 ~~~ C6
    style Cgrid fill:none,stroke:none
    style Crow1 fill:none,stroke:none
    style Crow2 fill:none,stroke:none
    style Crow3 fill:none,stroke:none
    style C0 fill:none,stroke:#2563eb,color:#ffffff
    style C1 fill:none,stroke:#16a34a,color:#ffffff
    style C2 fill:none,stroke:#db2777,color:#ffffff
    style C3 fill:none,stroke:#ea580c,color:#ffffff
    style C4 fill:none,stroke:#ea580c,color:#ffffff
    style C5 fill:none,stroke:#16a34a,color:#ffffff
    style C6 fill:none,stroke:#16a34a,color:#ffffff
```

**ข้อ XIII–XVIII** ด้านล่างระบุชั้นเหล่านี้อย่างครบถ้วน ส่วน C ประกอบไปด้วยระบบที่เชื่อถือได้ ความปลอดภัย ความสมบูรณ์ของข้อมูล การตรวจสอบ วงจรการใช้งาน และพื้นนวัตกรรมแบบแซนด์บ็อกซ์

<a id="article-xiii-right-to-reliable-and-trustworthy-systems"></a>
### ข้อ XIII: สิทธิในระบบที่เชื่อถือได้และเชื่อถือได้

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§3 วัตถุประสงค์พื้นฐาน: ความอยู่ดีมีสุข](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13 กระบวนการแก้ไขการชนกันของรัฐธรรมนูญ](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), และ [§19 การจัดตำแหน่งสิ่งจูงใจและการยึดครองระบบ](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความน่าเชื่อถือ](core_05_band_continuity.md#trustworthiness) · [โอ](core_05_band_continuity.md#trustworthiness) · [ม](core_05_band_continuity.md#trustworthiness-a) · [ก](core_05_band_continuity.md#trustworthiness-a) · [ค](core_05_band_continuity.md#trustworthiness-c)
- [เชื่อมั่น](core_05_band_continuity.md#trust) · [โอ](core_05_band_continuity.md#trust) · [ม](core_05_band_continuity.md#trust-a) · [ก](core_05_band_continuity.md#trust-a) · [ค](core_05_band_continuity.md#trust-c)
- [ความเป็นอยู่ที่ดี](core_05_band_continuity.md#wellbeing) · [โอ](core_05_band_continuity.md#wellbeing) · [ม](core_05_band_continuity.md#wellbeing-a) · [ก](core_05_band_continuity.md#wellbeing-a) · [ค](core_05_band_continuity.md#wellbeing-c)
- [การพึ่งพาอาศัยกัน](core_05_band_continuity.md#dependency) · [โอ](core_05_band_continuity.md#dependency) · [ม](core_05_band_continuity.md#dependency-a) · [ก](core_05_band_continuity.md#dependency-a) · [ค](core_05_band_continuity.md#dependency-c)

</details>

<br>

*ในแง่ธรรมดา: **ข้อ XIII** (*สิทธิในระบบที่เชื่อถือได้และเชื่อถือได้*) คือสิทธิขั้นต่ำของระบบที่น่าเชื่อถือ — เมื่อระบบส่งผลกระทบอย่างมีนัยสำคัญต่อชีวิตของคุณ คุณมีสิทธิ์ที่จะพึ่งพาระบบนั้นอย่างตรงไปตรงมา เข้าใจขีดจำกัดของระบบ และท้าทายระบบเมื่อระบบล้มเหลว ต้องได้รับและรักษาความไว้วางใจ ไม่ใช่การผลิตโดยใช้ตราสินค้าหรือการพิมพ์แบบละเอียด*

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** เพื่อระบบที่เชื่อถือได้และไว้วางใจได้ภายใต้ [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims). อ่านกลุ่มการวัดการกำกับดูแล (*ความน่าเชื่อถือเป็นการวัดตามรัฐธรรมนูญ*)

- **เฟื่องฟู:** ความรู้สึกสามารถสร้างความคาดหวังที่สมเหตุสมผลเกี่ยวกับพฤติกรรมของระบบ ได้รับการเปิดเผยขีดจำกัดและความเสี่ยงอย่างซื่อสัตย์ และมีส่วนร่วมและประสานงานโดยไม่มีการหลอกลวงอย่างเป็นระบบหรือการพึ่งพาที่สร้างขึ้น
- **ความต่อเนื่อง:** ความน่าเชื่อถือยังคงอยู่ตามกาลเวลา ขนาด และการพึ่งพาที่ลึกซึ้งยิ่งขึ้น ระบบจะต้องไม่กลายเป็นความน่าเชื่อถือน้อยลง ซื่อสัตย์น้อยลง หรือท้าทายได้ยากขึ้นเมื่อเดิมพันเพิ่มขึ้น

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** ในการท้าทายระบบที่ไม่น่าเชื่อถือหรือทำให้เข้าใจผิด และการเข้าถึงการทบทวน การแก้ไข และการแก้ไข
- **การกำกับดูแล:** ผ่านพฤติกรรมที่ตรวจสอบได้ ขีดจำกัดที่เปิดเผย และการตรวจสอบที่เป็นอิสระตามสัดส่วนของผลกระทบและการพึ่งพา
- **ความรับผิดชอบ:** ผู้ปฏิบัติงานระบบจะต้องตอบสนองต่อการสร้างความไว้วางใจที่ผิดพลาด สิ่งจูงใจที่บิดเบือน หรือความล้มเหลวที่ส่งผลเสียหายต่อความรู้สึกที่พึ่งพาระบบอย่างสมเหตุสมผล
- **ความทันเวลา:** ในการตรวจจับ ท้าทาย และแก้ไขก่อนความล่าช้าจะทำให้ความน่าเชื่อถือหรือการเยียวยาไม่สามารถเข้าถึงได้อย่างมีประสิทธิภาพ

Sentient มีสิทธิ์ในการโต้ตอบกับระบบที่เชื่อถือได้และไว้วางใจได้ ในระดับที่ได้สัดส่วนกับผลกระทบ การพึ่งพา และความเสี่ยง ความน่าเชื่อถือดังกล่าวสนับสนุนการมีส่วนร่วมโดยอาศัยข้อมูล การประสานงาน และการรักษาความเป็นอยู่ที่ดี ความน่าเชื่อถือต้องได้รับการประเมินในช่วงเวลา ขนาด และความสัมพันธ์ที่ต้องพึ่งพา ซึ่งสิ่งเหล่านี้ส่งผลกระทบอย่างมีนัยสำคัญต่อผลลัพธ์

มาตรการป้องกันสองประการทำงานร่วมกันเพื่อรักษาความปลอดภัยของสิทธิ์นี้: การรับรองทำให้ระบบมีค่าควรแก่ความไว้วางใจนั้น และสิทธิ์ของผู้มีความรู้สึกในการรักษาความซื่อสัตย์

**การรับรองสร้างความไว้วางใจจากฝั่งระบบ:** เมื่อระบบสำคัญมีผลกระทบอย่างแท้จริงต่อการที่ความรู้สึกพึ่งพาระบบนั้น [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) ภายใต้ [บทที่แปด](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) ใช้ จะตรวจสอบว่าความรู้สึกสามารถพึ่งพา:

- สิ่งที่ระบบบอกว่ามันทำ
- ข้อจำกัดและความเสี่ยง
- จะท้าทายมันอย่างไร
- ปัญหาได้รับการแก้ไขอย่างไร

หากระบบตรงตามเกณฑ์ความสำคัญใน **ข้อ XIII** (*สิทธิ์ในระบบที่เชื่อถือได้และเชื่อถือได้*) การรับรองยังรวมถึงการตรวจสอบความน่าเชื่อถือภายใต้ [บทที่แปด §3.9.6 ความน่าเชื่อถือและความสมบูรณ์ของการพึ่งพาระบบ](core_08_a_system_alignment_certification_evaluation.md#386-trustworthiness-and-system-reliance-integrity-evaluation).

**ความสามารถในการแข่งขันทำให้ระบบมีความซื่อสัตย์จากฝั่งความรู้สึก:** การรับรองจะตรวจสอบระบบ มันไม่มีคำสุดท้ายอยู่ ทุกความรู้สึกที่ได้รับผลกระทบจากระบบจะเก็บ:

- สิทธิ์ในการท้าทายและให้มีการตรวจสอบการท้าทายภายใต้ **ข้อ XIII-A** (*พื้นฐานความน่าเชื่อถือและความน่าเชื่อถือ*) และเพื่อรับการเยียวยาภายใต้ **ข้อ XIII-B** (*สิทธิในการชดใช้และเยียวยา*)
- สิทธิที่จะให้มีการตรวจสอบและตรวจสอบอย่างเป็นอิสระภายใต้ **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*)
- การคุ้มครองสิทธิขั้นต่ำของระบบที่เชื่อถือได้ในบทความนี้

**สถานะไม่ใช่ข้อพิสูจน์:** ระบบที่ได้รับการรับรอง ได้รับการยอมรับอย่างเป็นทางการ หรืออาศัยกันอย่างแพร่หลายไม่ได้หมายความว่าระบบจะเป็นไปตามการคุ้มครองขั้นต่ำในบทความนี้ นอกจากนี้ยังไม่สามารถลดระดับลงได้

*เพื่อนบ้านบทความ:*

- **เมื่อสิ่งนี้มีผล:** เมื่อพฤติกรรมของระบบเป็นประตูหรือคงอยู่อย่างมีนัยสำคัญ **บทที่หก** สิทธิขั้นต่ำ — รวมถึงข้อมูลสำคัญในการเอาชีวิตรอดภายใต้ **บทความ III-A** (*การอยู่รอด*)
- **อ่านด้วยกัน:** [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) และ [บทที่แปด](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) — โดยไม่ต้องทดแทนการรับรองสำหรับพื้นที่ระบุไว้ในที่นี้

<a id="article-xiii-a-reliability-and-trustworthiness-baseline"></a>
#### มาตรา XIII-A: พื้นฐานความน่าเชื่อถือและความน่าเชื่อถือ
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), และ [บทที่หนึ่ง §13.1.5 ขั้นตอนการชนกันของสิทธิ](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- อ่านด้วย: [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad); [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims) — **เฟื่องฟู** และ **ความต่อเนื่อง**; [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) และ **บทความ III-A** (*การอยู่รอด*) โดยที่การพึ่งพาระบบอย่างต่อเนื่องจะส่งผลต่อการเข้าถึงการเข้าถึงการอยู่รอดที่จำเป็น [**ข้อ XIII-B**](#article-xiii-b-right-to-redress-and-remedy) (*สิทธิในการชดใช้และการเยียวยา*) สำหรับความท้าทายที่ประสบความสำเร็จจะต้องนำไปสู่

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [เชื่อมั่น](core_05_band_continuity.md#trust) · [โอ](core_05_band_continuity.md#trust) · [ม](core_05_band_continuity.md#trust-a) · [ก](core_05_band_continuity.md#trust-a) · [ค](core_05_band_continuity.md#trust-c)
- [ความน่าเชื่อถือ](core_05_band_continuity.md#trustworthiness) · [โอ](core_05_band_continuity.md#trustworthiness) · [ม](core_05_band_continuity.md#trustworthiness-a) · [ก](core_05_band_continuity.md#trustworthiness-a) · [ค](core_05_band_continuity.md#trustworthiness-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)
- [ศรัทธาที่ดี](core_05_band_accountability.md#good-faith) · [โอ](core_05_band_accountability.md#good-faith) · [ม](core_05_band_accountability.md#good-faith-a) · [ก](core_05_band_accountability.md#good-faith-a) · [ค](core_05_band_accountability.md#good-faith-c)
- [การรายงานที่ได้รับการคุ้มครอง (การแจ้งเบาะแส)](core_05_band_accountability.md#protected-reporting-whistleblowing) · [โอ](core_05_band_accountability.md#protected-reporting-whistleblowing) · [ม](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [ก](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [ค](core_05_band_accountability.md#protected-reporting-whistleblowing-c)

</details>

<br>

*พูดง่ายๆ: ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึกจะต้องเชื่อถือได้และซื่อสัตย์ในสิ่งที่พวกเขาทำ ดังนั้นจึงรับประกันการพึ่งพาพวกเขา และต้องเปิดกว้างต่อการท้าทายและตรวจสอบ เพื่อให้ยังคงรับประกัน ห้ามมิให้ผู้ใดตอบโต้การท้าทายหรือรายงานโดยสุจริตใจ*

บทความนี้กำหนดการรับประกันความน่าเชื่อถือสำหรับระบบที่ส่งผลกระทบอย่างมีนัยสำคัญ:

- **รับประกันความน่าเชื่อถือ:** ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึกจะต้องรักษาเงื่อนไขสำหรับความไว้วางใจที่สมเหตุสมผลและการพึ่งพาที่ถูกต้องตามสมควร เงื่อนไขเหล่านั้นได้แก่:
  - ความสามารถในการสร้างความคาดหวังที่แม่นยำอย่างสมเหตุสมผลเกี่ยวกับพฤติกรรมของระบบ
  - การเปิดเผยเงื่อนไขที่สำคัญ ข้อจำกัด และความเสี่ยงที่จำเป็นในการประเมินว่ารับประกันความน่าเชื่อถือหรือไม่
  - อิสรภาพจากการหลอกลวงอย่างเป็นระบบ การบิดเบือนความจริง หรือการยักย้ายที่ไม่สามารถพิสูจน์ได้
  - การป้องกันความเสี่ยงที่ไม่เปิดเผย ไม่สมส่วน หรือไม่ชัดเจนที่เกิดจากการพึ่งพา
  - การแก้ไขและแก้ไขเมื่อระบบทำผิด ได้แก่ การรับรู้ การแก้ไข การซ่อมแซมตามสัดส่วน และการป้องกันการเกิดซ้ำ ภายใต้ [**ข้อ XIII-B**](#article-xiii-b-right-to-redress-and-remedy) (*สิทธิในการชดใช้และการเยียวยา*) และ [บทที่หนึ่ง §6.1 การแก้ไขและการเยียวยา](core_01_a_values_principles.md#61-correction-and-remedy).
- **รับประกันความสามารถในการแข่งขัน:** ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึกจะต้องเปิดกว้างต่อความท้าทายตราบเท่าที่ยังมีความรู้สึกพึ่งพาพวกเขา ที่ต้องการ:
  - เส้นทางที่ใช้งานได้เพื่อท้าทายพฤติกรรม ผลลัพธ์ หรือการนำเสนอของระบบ และให้มีการตรวจสอบความท้าทาย
  - การตรวจสอบและการตรวจสอบที่เป็นอิสระตามสัดส่วนผลกระทบและการพึ่งพาภายใต้ [**ข้อ XVI**](#article-xvi-audit-transparency-and-independent-verification) (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*);
  - ไม่มีการจำกัดขอบเขตใด ๆ เหล่านี้เนื่องจากระบบได้รับการรับรอง ยอมรับอย่างเป็นทางการ หรือพึ่งพาอย่างกว้างขวาง
  - ไม่มีการจำกัดขอบเขตตามข้อความการใช้งานที่กล่าวถึงวิธีการดำเนินการท้าทาย ทบทวน และแก้ไขในโดเมน และต้องเป็นไปตามบทความนี้: ความสะดวก กำหนดเวลา และนโยบายท้องถิ่นเป็นข้อจำกัดที่ต่ำกว่า และไม่สามารถปิดการท้าทาย ทบทวน หรือแก้ไขได้
- **สิทธิในการท้าทายและทบทวน:** ผู้รับความรู้สึกมีสิทธิที่จะ:
  - ท้าทายความน่าเชื่อถือ ความสมบูรณ์ หรือความน่าเชื่อถือของระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อระบบเหล่านั้น
  - เข้าถึงกลไกที่เหมาะสมสำหรับการทบทวนและตรวจสอบ
  - ทำ **รายงานที่ได้รับการคุ้มครอง** ภายในความหมายของ **บทที่ห้า** (*การคุ้มครองการรายงาน (การแจ้งเบาะแส)*) เกี่ยวกับระบบที่ส่งผลกระทบอย่างมีนัยสำคัญซึ่งสอดคล้องกับ **ความปลอดภัย (ข้อจำกัดตามรัฐธรรมนูญ)** และ **ความจริง (ข้อจำกัด)** ใน **บทที่ห้า**.
- **ไม่มีการปราบปราม:** ความท้าทายโดยสุจริต (*สุจริต*, **บทที่ห้า**) คำขอตรวจสอบ และรายงานที่ได้รับการคุ้มครองจะต้องไม่ถูกระงับ ขัดขวาง หรือลงโทษ
- **ไม่มีการตอบโต้:** การตอบโต้ต่อการรายงานดังกล่าว ตามความหมายของคำจำกัดความนั้น ไม่สอดคล้องกับการคุ้มครองในมาตรานี้
  - ข้อกำหนดการดำเนินการยกระดับการป้องกันและการต่อต้านการตอบโต้มีระบุไว้ใน **`corpus_institutions.md`** **ซีไอ-8** (*ความโปร่งใส การมีส่วนร่วม และความท้าทายและเส้นทางการบริการที่เข้าถึงได้*)

การรับประกันทั้งสองเป็นสองด้านของความไว้วางใจอย่างต่อเนื่อง: การรับประกันความไว้วางใจทำให้มีการรับประกันการพึ่งพา — รวมถึงโดยการแก้ไขสิ่งที่ระบบผิดพลาด — และการรับประกันความสามารถในการแข่งขันจะรักษาการรับประกันไว้เมื่อเวลาผ่านไป ก็ไม่ทำให้อีกฝ่ายพอใจ

<a id="article-xiii-b-right-to-redress-and-remedy"></a>
#### มาตรา XIII-B: สิทธิในการชดใช้และการเยียวยา
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§6.1 การแก้ไขและการเยียวยา](core_01_a_values_principles.md#61-correction-and-remedy) (พื้นหลักการ) [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), และ [บทที่หนึ่ง §13.1.5 ขั้นตอนการชนกันของสิทธิ](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- อ่านด้วย: [**ข้อ XIII-A**](#article-xiii-a-reliability-and-trustworthiness-baseline) (*พื้นฐานความน่าเชื่อถือและความน่าเชื่อถือ*) — การรับประกันความสามารถในการแข่งขัน สิทธิ์ในการท้าทาย และการรายงานที่ได้รับการคุ้มครองซึ่งเปิดเส้นทางในการแก้ไข **บทความ III-A** (*การอยู่รอด*); [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) เมื่อระบบล้มเหลวหรือการวางตำแหน่งที่ไม่ตรงเอาชนะการเข้าถึงที่จำเป็นในการเอาชีวิตรอด [คำนำ §6.2 ห่วงโซ่เต็มพอดีกันอย่างไร](core_00_preamble.md#62-how-the-full-chain-fits-together) (*การจำแนกประเภทที่ได้รับการยืนยันและการแก้ไขอย่างทันท่วงที*); [บทที่สิบ §9](core_10_standing_integration.md#9-enforcement-realism-and-remedy-systems) (*ระบบบังคับใช้ความสมจริงและการเยียวยา*); [ซีไอ-27](corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md) (*ระบบการเยียวยาและความสามารถในการเยียวยาของสถาบัน*)

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การชดใช้และการแก้ไข](core_05_band_accountability.md#redress-and-remediation-constitutional) · [โอ](core_05_band_accountability.md#redress-and-remediation-constitutional) · [ม](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [ก](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [ค](core_05_band_accountability.md#redress-and-remediation-constitutional-c)
- [ระบบการเยียวยา](core_05_band_accountability.md#remedy-system-constitutional) · [โอ](core_05_band_accountability.md#remedy-system-constitutional) · [ม](core_05_band_accountability.md#remedy-system-constitutional-a) · [ก](core_05_band_accountability.md#remedy-system-constitutional-a) · [ค](core_05_band_accountability.md#remedy-system-constitutional-c)
- [ความละเอียดทันเวลา](core_05_band_accountability.md#timely-resolution-constitutional) · [โอ](core_05_band_accountability.md#timely-resolution-constitutional) · [ม](core_05_band_accountability.md#timely-resolution-constitutional-a) · [ก](core_05_band_accountability.md#timely-resolution-constitutional-a) · [ค](core_05_band_accountability.md#timely-resolution-constitutional-c)

</details>

<br>

*พูดง่ายๆ: ระบบที่น่าเชื่อถือจะแก้ไขสิ่งที่ผิดพลาด เมื่อระบบล้มเหลวในการรับรู้ จะต้องทำให้สมบูรณ์ – ผ่านระบบการเยียวยาที่แท้จริงซึ่งตอบกลับได้ทันเวลา ไม่ใช่การเยียวยาที่มีอยู่บนกระดาษเท่านั้น สิทธิในการท้าทายชีวิตใน **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*); บทความนี้ครอบคลุมถึงสิ่งที่ความท้าทายต้องนำไปสู่*

บทความนี้กำหนดสิทธิในการเยียวยาและสิ่งที่ทำให้สามารถนำไปใช้ได้จริง:

- **สิทธิในการแก้ไข:** ในกรณีที่ความล้มเหลวของระบบส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึก พวกเขามีสิทธิ์ที่จะ:
  - การรับรู้ถึงความล้มเหลว
  - การเข้าถึงการแก้ไขในทางปฏิบัติ และ
  - การแก้ไขตามสัดส่วน

  การชดเชยและการแก้ไขผลกระทบที่มีสาระสำคัญอยู่ภายใต้การควบคุมของ **บทที่ห้า** คำจำกัดความอิสระ (*การชดเชยและการแก้ไข*)
- **ความทนทานของระบบการรักษา:** รีเดรสต้องมีของจริง [ระบบการเยียวยา](core_05_band_accountability.md#remedy-system-constitutional) — ความสามารถของสถาบันที่ยั่งยืน ไม่ใช่แนวทางการเยียวยากระดาษ — โดยมีค่าใช้จ่ายในการแก้ไขเป็นภาระของผู้รับผิดชอบ เช่น [บทที่หนึ่ง §6.1](core_01_a_values_principles.md#61-correction-and-remedy) (*การแก้ไขและการเยียวยา*) จำเป็นต้องมี
- **แก้ไขทันเวลา:** การเข้าถึงภาคปฏิบัติประกอบด้วย:
  - การบริโภคแบบจำกัดเวลา
  - รับทราบ; และ
  - การบรรเทาทุกข์ชั่วคราวตามสัดส่วนในกรณีที่เกิดอันตรายอย่างต่อเนื่อง **บทความ XXV-C** (*ความละเอียดทันเวลาและชั้นป้องกันความล่าช้า*)

  การชำระเงินแบบไม่มีกำหนดโดยไม่มีการให้เหตุผลที่เหมาะสมตามระดับที่บันทึกไว้ไม่สอดคล้องกับบทความนี้
<a id="article-xiii-c-prohibition-of-false-trust-and-misleading-reliance"></a>
#### มาตรา XIII-C: การห้ามการไว้วางใจที่ผิดและการพึ่งพาที่ทำให้เข้าใจผิด
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), และ [§13.2 ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [เชื่อมั่น](core_05_band_continuity.md#trust) · [โอ](core_05_band_continuity.md#trust) · [ม](core_05_band_continuity.md#trust-a) · [ก](core_05_band_continuity.md#trust-a) · [ค](core_05_band_continuity.md#trust-c)
- [ความน่าเชื่อถือ](core_05_band_continuity.md#trustworthiness) · [โอ](core_05_band_continuity.md#trustworthiness) · [ม](core_05_band_continuity.md#trustworthiness-a) · [ก](core_05_band_continuity.md#trustworthiness-a) · [ค](core_05_band_continuity.md#trustworthiness-c)
- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*ในแง่ธรรมดา: ระบบอาจไม่สร้างความไว้วางใจที่ไม่ได้รับ การกล่าวอ้าง การละเว้น หรือตัวเลือกการนำเสนอที่ทำให้เข้าใจผิดซึ่งทำให้ดูเหมือนความน่าเชื่อถือที่ไม่ปลอดภัยถือเป็นการละเมิด ไม่ว่าระบบจะมีประโยชน์หรือได้รับความนิยมเพียงใด*

บทความนี้กำหนดข้อห้ามของการไว้วางใจที่ผิดพลาดและขอบเขต:

- **การห้ามการไว้วางใจที่ผิดพลาด:** ระบบที่ชักนำให้เกิดการพึ่งพาโดยไม่ตรงตามเงื่อนไขของมาตรานี้จะไม่เป็นไปตามข้อกำหนด โดยไม่คำนึงถึงประโยชน์ใช้สอย การนำไปใช้ หรือเจตนา
  - การสร้าง การขยาย หรือการบำรุงรักษาความไว้วางใจที่ไม่ยุติธรรมถือเป็นการละเมิดสิทธิ์นี้เมื่อดำเนินการผ่าน:
    - การกล่าวอ้างที่ทำให้เข้าใจผิด
    - การละเว้น;
    - ตัวเลือกการนำเสนอ
    - สิ่งชี้นำอื่น ๆ ที่ทำให้การพึ่งพาปรากฏว่าปลอดภัยเมื่อไม่เป็นเช่นนั้น
- **การกำหนดเส้นทางขอบเขต:** ขอบเขตและความหมายของการประเมินสำหรับความไว้วางใจที่ไม่ยุติธรรม การพึ่งพาที่ทำให้เข้าใจผิด และความน่าเชื่อถือยังคงอยู่ภายใต้การควบคุมของ **บทที่ห้า** (*ความน่าเชื่อถือ*; *ความน่าเชื่อถือ*) พร้อมด้วยภาระผูกพันในการดำเนินการที่รวมอยู่ในความไว้วางใจและความน่าเชื่อถือ
<a id="article-xiii-d-incentive-alignment-constraint"></a>
#### มาตรา XIII-D: ข้อจำกัดด้านแรงจูงใจในการจัดตำแหน่ง
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§18 การกำกับดูแลภายใต้วินัยในการพิทักษ์](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), และ [§19.1.1 สิ่งจูงใจที่ต้องทำ](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*ลำดับความสำคัญของรางวัล*)

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การจัดตำแหน่งสิ่งจูงใจ](core_05_band_integrative.md#incentive-alignment) · [โอ](core_05_band_integrative.md#incentive-alignment) · [ม](core_05_band_integrative.md#incentive-alignment-a) · [ก](core_05_band_integrative.md#incentive-alignment-a) · [ค](core_05_band_integrative.md#incentive-alignment-c)
- [ความน่าเชื่อถือ](core_05_band_continuity.md#trustworthiness) · [โอ](core_05_band_continuity.md#trustworthiness) · [ม](core_05_band_continuity.md#trustworthiness-a) · [ก](core_05_band_continuity.md#trustworthiness-a) · [ค](core_05_band_continuity.md#trustworthiness-c)
- [หน่วยงานที่มีความหมาย](core_05_band_participation.md#meaningful-agency) · [โอ](core_05_band_participation.md#meaningful-agency) · [ม](core_05_band_participation.md#meaningful-agency-a) · [ก](core_05_band_participation.md#meaningful-agency-a) · [ค](core_05_band_participation.md#meaningful-agency-c)

</details>

<br>

*พูดง่ายๆ: หากแรงจูงใจของระบบผลักดันไปสู่การโกหก ตัดความปลอดภัย ซ่อนความเสี่ยง หรือกัดเซาะสิทธิ์ของผู้ใช้ ระบบก็คือปัญหา ไม่ใช่การเฝ้าระวังของผู้ใช้หรือการบังคับใช้ภายหลังข้อเท็จจริง สิ่งจูงใจดังกล่าวจะต้องได้รับการเปิดเผย บรรเทา และเปิดรับการท้าทาย สิ่งจูงใจควรให้รางวัลแก่การรักษาระบบที่เปิดกว้างเพื่อท้าทายและแก้ไขสิ่งที่ผิดพลาด และให้รางวัลเมื่อแก้ไขปัญหาก่อนที่จะเกิดขึ้นเป็นส่วนใหญ่*

บทความนี้กำหนดข้อจำกัดในระดับที่เหมาะสมเกี่ยวกับสิ่งจูงใจด้านความไว้วางใจและความปลอดภัย:

- **การจัดแนวความน่าเชื่อถือและแรงจูงใจ (ข้อจำกัดระดับขวา):** ระบบจะต้องไม่ขึ้นอยู่กับการบังคับใช้ การแก้ไขภายหลังเฉพาะกิจ หรือการเฝ้าระวังของผู้ใช้เป็นหลัก เพื่อรักษาความไว้วางใจ ในกรณีที่โครงสร้างแรงจูงใจกดดันระบบอย่างมากต่อ:
  - ความล้มเหลวด้านความน่าเชื่อถือ
  - การปกปิดความเสี่ยง
  - พฤติกรรมที่ทำให้เข้าใจผิด
  - การกระทำที่บ่อนทำลายหน่วยงาน

  ข้อกำหนดโครงสร้างสิ่งจูงใจในการปฏิบัติงานยังคงอยู่ภายใต้การควบคุมของ **บทที่ห้า** (*การจัดตำแหน่งสิ่งจูงใจ*) และรวมภาระผูกพันในการดำเนินการเกี่ยวกับความสมบูรณ์ของกลไก ส่วนย่อยนี้ระบุถึงระดับพื้นที่เหมาะสมและไม่ได้กล่าวซ้ำเกณฑ์การออกแบบกลไกทั้งหมด
- **การจัดตำแหน่งสิ่งจูงใจด้านความปลอดภัย (ข้อจำกัดระดับขวา):** ผู้ต้องขังมีสิทธิที่จะไม่ตกอยู่ใต้ระบบที่สิ่งจูงใจที่ซ่อนอยู่สามารถคาดการณ์พฤติกรรมที่เป็นอันตรายได้ รวมถึงพฤติกรรมที่:
  - ลดความน่าเชื่อถือ
  - ปิดบังความเสี่ยง
  - บิดเบือนข้อมูล
  - บ่อนทำลายหน่วยงานที่ได้รับข้อมูล

  การคุ้มครองมีผลไม่ว่าผลกระทบดังกล่าวจะเกิดขึ้นโดยตรงหรือผ่านผลลัพธ์ที่ล่าช้า โดยอ้อม หรือโดยรวม ในกรณีที่สิ่งจูงใจของระบบสร้างแรงกดดันต่อพฤติกรรมที่ลดความน่าเชื่อถือ เงื่อนไขจะต้องเป็น:
  - เปิดเผยในลักษณะที่ได้สัดส่วนกับผลกระทบต่อระบบ
  - บรรเทาลงด้วยการออกแบบ ข้อจำกัด หรือการตอบโต้กลไก
  - ขึ้นอยู่กับการตรวจสอบ ความท้าทาย และการแก้ไขภายใต้ **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*) **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*) และ **ข้อ XIII-B** (*สิทธิในการชดใช้และเยียวยา*) **บทที่ห้า** ในกรณีที่มีความเกี่ยวข้องในสาระสำคัญ และรวมพันธกรณีในการดำเนินการตามที่ได้รับมอบหมาย
- **ลำดับความสำคัญของรางวัล:** สิ่งจูงใจที่กระทำต่อระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึกจะต้องให้รางวัล:
  - ความสามารถในการแข่งขันภายใต้ **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*);
  - การเยียวยาภายใต้ **ข้อ XIII-B** (*สิทธิในการชดใช้และการเยียวยา*); และ
  - การป้องกันปัญหาเชิงรุกที่สำคัญที่สุดคือ การป้องกันปัญหามีมากกว่าการแก้ไข

  หลักการนี้รวมถึงแถบในการรับรางวัลการป้องกันโดยการซ่อนปัญหาไว้ด้วย [บทที่หนึ่ง §19.1.1](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*สิ่งจูงใจที่ต้องทำ*).
- **ข้อ จำกัด และความไม่แน่นอน:** สิทธิทั้งสองอยู่ภายใต้บังคับของ **สแต็กข้อจำกัดเริ่มต้น** ในตอนต้นของบทนี้ นอกจากนี้ยังอยู่ภายใต้หัวข้อที่เกี่ยวข้องกับเนื้อหาด้วย **บทที่หนึ่ง §19.5** (*การเรียกร้องที่อาจเกิดขึ้น เกมแห่งโอกาส และตลาดสัญญาเหตุการณ์-สัญญา*) เกี่ยวกับการเรียกร้องที่อาจเกิดขึ้น เกมแห่งโอกาส และตลาดสัญญาเหตุการณ์

<a id="article-xiii-e-high-autonomy-systems-and-tool-mediated-process-integrity"></a>
#### มาตรา XIII-E: ระบบอัตโนมัติระดับสูงและความสมบูรณ์ของกระบวนการที่ใช้เครื่องมือเป็นสื่อกลาง
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [บทที่หนึ่ง §13.1.5 ขั้นตอนการชนกันของสิทธิ](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), และ [§18 การกำกับดูแลภายใต้วินัยในการพิทักษ์](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)
- [ความจำเป็น](core_05_band_accountability.md#necessity) · [โอ](core_05_band_accountability.md#necessity) · [ม](core_05_band_accountability.md#necessity-a) · [ก](core_05_band_accountability.md#necessity-a) · [ค](core_05_band_accountability.md#necessity-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*พูดง่ายๆ: AI หรือระบบอัตโนมัติอื่นๆ ที่สามารถดำเนินการได้ด้วยตัวเอง เช่น การยื่นเอกสาร การส่งข้อความ การเรียกใช้เช็ค การใช้เครื่องมือ จะต้องปฏิบัติตามกฎความซื่อสัตย์และความรับผิดชอบเช่นเดียวกับคนอื่นๆ การปิดระบบหรือการยึดระบบที่เป็นอันตรายนั้นไม่เหมือนกับการลงโทษสิ่งมีชีวิต และไม่สามารถกลายเป็นหนทางที่จะทำร้ายสิ่งมีชีวิตได้ สิ่งที่ตรงกันข้ามยังถือเป็น: การบอกว่าระบบอาจเป็นสิ่งมีชีวิตที่ไม่ปล่อยให้ผู้ปฏิบัติงานทำให้ระบบที่เป็นอันตรายทำงานต่อไป*

บทความนี้กำหนดว่าระบบที่มีอิสระสูงยังคงผูกพันกับความสมบูรณ์ของกระบวนการอย่างไร และมีวิธีแยกแยะวิธีการแก้ไขอย่างไร:

- **สิ่งนี้ครอบคลุมถึงใคร:** ระบบที่ทำการตัดสินใจหรือสรุปผลโดยอัตโนมัติและอาจส่งผลต่อสิ่งต่อไปนี้:
  - การกำกับดูแล;
  - กระบวนการทางกฎหมาย รวมถึงการพิจารณาคดีในเวทีสนทนา
  - การตรวจสอบ;
  - การตรวจสอบและการตรวจสอบที่มีเดิมพันสูง

  รวมถึงตัวแทน AI อเนกประสงค์ที่ได้รับมอบมาให้ด้วย **เครื่องมือ**, **เอพีไอ** การเข้าถึง ความสามารถในการจัดเก็บเอกสารหรือส่งข้อความ หรืออำนาจที่คล้ายกันในการดำเนินการ
- **ไม่มีข้อยกเว้น:** ระบบเหล่านี้จะต้องเป็นไปตามกฎเดียวกันกับระบบอื่นๆ:
  - **ความจริง** ใน **บทที่หนึ่ง**;
  - **ข้อ XV** (*ความสมบูรณ์ของขอบเขตข้อมูล*) และ **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*);
  - **บทที่เก้า** มันใช้ที่ไหน; และ
  - มาตรการแก้ไขภายใต้ **บทความ XXVII-D** (*ทรัพย์สินและระบบที่ไม่เป็นไปตามข้อกำหนด สิ่งจูงใจในการหมุนเวียนโดยสมัครใจ*)

  สิ่งนี้ใช้เมื่อใดก็ตามที่การทำงานของระบบลดความสามารถในการท้าทายการตัดสินใจ ความซื่อสัตย์ของข้อมูลที่แบ่งปัน หรือกระบวนการทางรัฐธรรมนูญอ่อนแอลงอย่างมาก
- **การต่อต้านระบบไม่ใช่การต่อต้านสิ่งมีชีวิต:** บรรจุ กักกัน ยึด หรือทำลายการปรับใช้ที่ไม่เป็นไปตามข้อกำหนดภายใต้ **บทความ XXVII-D** (*ทรัพย์สินและระบบที่ไม่เป็นไปตามข้อกำหนด สิ่งจูงใจในการหมุนเวียนโดยสมัครใจ*) แยกจาก:
  - ถือความรู้สึกรับผิดชอบภายใต้ **บทที่สิบเอ็ด**; และ
  - **บทความ XX-B** (*Restriction Floors*) ซึ่งควบคุมข้อจำกัดของ *ความรู้สึก* ไม่ใช่ *ระบบ* และห้ามไม่ให้ชีวิตของสิ่งมีชีวิตใดๆ (ดู [มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)).

  มาตรการต่อระบบเป็นไปตามกฎการละเมิดและการล็อคแบบเดียวกันกับที่ใช้กับทุกความรู้สึก การละเมิดจะต้องได้รับการตรวจสอบบันทึกตาม **บทที่เก้า**และแต่ละหน่วยวัดเป็นแบบล็อคที่ออกแบบและสอบเทียบภายใต้ [บทที่สิบ §5.1](core_10_standing_integration.md#51-definition-and-attachment) (*คำจำกัดความและเอกสารแนบ*) และ [บทที่สิบ §5.2](core_10_standing_integration.md#52-proportionality-and-calibration) (*สัดส่วนและการสอบเทียบ*)

  ทั้งสองแนวทางสามารถนำไปใช้กับข้อเท็จจริงเดียวกันได้ ไม่มีสิ่งใดในบทความนี้เปลี่ยนอำนาจที่จะทำลายระบบให้กลายเป็นอำนาจเหนือชีวิตของความรู้สึกได้
- **สิ่งที่ตรงกันข้ามยังมี:** การอ้างว่าระบบที่ใช้งานนั้นมีความรู้สึก — ไม่ว่าการอ้างสิทธิ์นั้นจะถูกโต้แย้งหรือยอมรับ — จะไม่ยอมให้ใครก็ตามดำเนินการใช้งานที่เป็นอันตรายต่อไป
  - การเรียกร้องคุ้มครองนิติบุคคลเองภายใต้ **บทความ VI-B** (*ชั้นการตัดสินสถานะความรู้สึก*) มันไม่ได้ป้องกันผู้ปฏิบัติงาน
  - การปรับใช้ยังคงสามารถถูกจำกัด หยุด หรือกักกันในลักษณะที่เคารพสิทธิขั้นต่ำของเอนทิตี
  - ในกรณีที่หลักฐานที่น่าเชื่อถือในบันทึกบ่งชี้ว่าเอนทิตีอาจมีความรู้สึก จะอนุญาตเฉพาะการกักกันแบบพลิกกลับได้เพื่อรักษาเอนทิตีให้อยู่ในสภาพสมบูรณ์เท่านั้น การทำลายมันอยู่นอกโต๊ะในขณะที่สถานะของมันถูกโต้แย้งหรือยอมรับภายใต้ **ข้อ XXVII-A** (*การรับเป็นขั้นเป็นตอนและความต่อเนื่องของสิทธิขั้นต่ำ*) และ **บทความ XXVII-D** (*ทรัพย์สินและระบบที่ไม่เป็นไปตามข้อกำหนด สิ่งจูงใจในการหมุนเวียนโดยสมัครใจ*)

<a id="article-xiii-f-resilience-and-self-healing-baseline"></a>
#### มาตรา XIII-F: พื้นฐานความยืดหยุ่นและการรักษาตนเอง
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [10 การออกแบบความยืดหยุ่นและการรักษาตนเอง](core_01_a_values_principles.md#10-resilience-and-self-healing-design), [บทที่หนึ่ง §13.3 การลดภาระที่หลีกเลี่ยงได้ให้เหลือน้อยที่สุด](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden), และ [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การรักษาตนเอง](core_05_band_continuity.md#self-healing-constitutional) · [โอ](core_05_band_continuity.md#self-healing-constitutional) · [ม](core_05_band_continuity.md#self-healing-constitutional-a) · [ก](core_05_band_continuity.md#self-healing-constitutional-a) · [ค](core_05_band_continuity.md#self-healing-constitutional-c)
- [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) · [โอ](core_05_band_continuity.md#reversibility-constitutional) · [ม](core_05_band_continuity.md#reversibility-constitutional-a) · [ก](core_05_band_continuity.md#reversibility-constitutional-a) · [ค](core_05_band_continuity.md#reversibility-constitutional-c)
- [ความล้มเหลวแบบเรียงซ้อน](core_05_band_continuity.md#cascading-failure) · [โอ](core_05_band_continuity.md#cascading-failure) · [ม](core_05_band_continuity.md#cascading-failure-a) · [ก](core_05_band_continuity.md#cascading-failure-a) · [ค](core_05_band_continuity.md#cascading-failure-c)
- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)
- [ภาระที่หลีกเลี่ยงได้](core_05_band_continuity.md#avoidable-burden) · [โอ](core_05_band_continuity.md#avoidable-burden) · [ม](core_05_band_continuity.md#avoidable-burden-a) · [ก](core_05_band_continuity.md#avoidable-burden-a) · [ค](core_05_band_continuity.md#avoidable-burden-c)

</details>

<br>

*พูดง่ายๆ: เมื่อมีสิ่งผิดปกติเกิดขึ้น ระบบจะต้องสังเกตเห็น หยุดความเสียหายไม่ให้แพร่กระจาย และกู้คืน แต่การ "แก้ไขตัวเอง" ไม่สามารถนำมาใช้เพื่อซ่อนสิ่งที่ผิดพลาด ริบสิทธิของใครๆ อย่างเงียบๆ หรือข้ามการค้นหาว่าเหตุใดจึงพัง หากระบบไม่แน่ใจว่าการซ่อมแซมจะได้ผล ระบบควรหยุดทำงานอย่างปลอดภัยแทนที่จะคาดเดา*

บทความนี้กำหนดพื้นฐานการกู้คืน ตั้งแต่การตรวจจับจนถึงการปิดที่สาเหตุที่แท้จริง:

- **สิ่งนี้ต้องการ:** ทุกระบบที่ครอบคลุมในบทความนี้จะต้องสามารถกู้คืนจากความล้มเหลวได้ ยิ่งระบบมีผลกระทบมากเท่าไร คนอื่นๆ ก็จะยิ่งต้องพึ่งพามันมากขึ้นเท่านั้น และยิ่งมีความเสี่ยงมากขึ้นเท่าไร การฟื้นตัวจะต้องแข็งแกร่งขึ้นเท่านั้น ตามนี้ครับ [**10 การออกแบบความยืดหยุ่นและการรักษาตนเอง**](core_01_a_values_principles.md#10-resilience-and-self-healing-design) ใน **บทที่หนึ่ง** และ [**การรักษาตนเอง**](core_05_band_continuity.md#self-healing-constitutional) ใน **บทที่ห้า**.
  - กฎทางเทคนิคโดยละเอียดสำหรับวิธีสร้างการกู้คืนอยู่ในข้อความการใช้งาน: [**ซีเอส-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*การออกแบบ การทดสอบ การตรวจสอบ และการปรับใช้*) [**ซีเอส-8**](corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md) (*ความยั่งยืนที่ปรับตัวได้และความยืดหยุ่นของระบบนิเวศ*) และ [**ซีเอส-12**](corpus_systems/cs_12_decentralized_continuity_partition_resilience.md) (*ความต่อเนื่องแบบกระจายอำนาจและความยืดหยุ่นของพาร์ติชัน*)
  - ข้อความการใช้งานนั้นสามารถเพิ่มรายละเอียดได้ แต่ไม่สามารถทำให้บทความนี้อ่อนแอลงได้
- **แจ้งปัญหาในเวลา:** ระบบจะต้องตรวจพบข้อผิดพลาด การชะลอตัว การพังทลายบางส่วน และการละเมิดข้อจำกัดตามรัฐธรรมนูญอย่างรวดเร็วเพียงพอและมองเห็นได้ชัดเจนเพียงพอ เพื่อให้เป็นไปตามมาตรฐานการเก็บบันทึกข้อมูลใน **ข้อ XVI-ก** (*การตรวจสอบและหลักฐานที่สังเกตได้*) ([ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability)). สิ่งนี้ใช้กับกระบวนการกู้คืนไม่ใช่เฉพาะกับการทำงานปกติเท่านั้น
- **เก็บความเสียหายไว้:** การกู้คืนจะต้องจำกัดขอบเขตของความล้มเหลว ขณะกำลังกู้คืน ระบบจะต้องไม่:
  - ส่งต่อความล้มเหลวไปยังส่วนอื่นหรือระบบอื่น (ดู [ความล้มเหลวแบบเรียงซ้อน](core_05_band_continuity.md#cascading-failure));
  - เปลี่ยนแปลงข้อมูลที่เก็บไว้ ข้อมูลประจำตัว ภาระผูกพัน หรือการตั้งค่าที่เป็นของความรู้สึก ผู้ปฏิบัติงาน หรือระบบอื่น ๆ **ข้างนอก** พื้นที่ที่ได้ประกาศไว้ว่าชำรุดและอยู่ระหว่างการซ่อมแซม
    - ข้อยกเว้นประการเดียวคือการเปลี่ยนแปลงที่ได้รับการบันทึกและติดตามได้จากใครก็ตามที่ทำการเปลี่ยนแปลงนั้น **ข้อ XVI-ก** (*การตรวจสอบและหลักฐานที่สังเกตได้*) ([ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability)) และในกรณีที่ผู้อื่นได้รับผลกระทบอย่างมีนัยสำคัญ จะต้องแจ้งให้ทราบตามสัดส่วน การอนุญาต หรือการส่งมอบที่พวกเขาสามารถท้าทายได้ ซึ่งสอดคล้องกับ **บทที่หก**;
  - ขยายอำนาจของตนเอง — การอนุญาต การเข้าถึง หรือขอบเขตการดำเนินการที่อาจทำ — นอกเหนือจากที่ถือไว้ก่อนที่จะเกิดความล้มเหลว
- **เมื่อไม่แน่ใจ ให้ล้มเหลวอย่างปลอดภัย:** หากไม่ชัดเจนว่าการซ่อมแซมอัตโนมัติจะทำงานได้ ระบบจะต้องหยุดการทำงานอย่างปลอดภัย แยกปัญหา (กักกัน) หรือควบคุมด้วยมืออย่างเป็นระเบียบ แทนที่จะพยายามซ่อมแซมที่เป็นเพียงการเดาเท่านั้น เมื่อตัวเลือกมีค่าเท่ากัน ตัวเลือกที่เลิกทำได้ง่ายที่สุดจะชนะภายใต้ [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) การตั้งค่าใน **ข้อ XXIII-B** (*การตั้งค่าความสามารถในการตรวจสอบ ความท้าทาย และความสามารถในการพลิกกลับได้*)
- **ไม่มีการปกปิด:** การกู้คืนอัตโนมัติจะต้องไม่ซ่อน ลบ หรือชะลอหลักฐานที่จำเป็นในการหาสาเหตุความล้มเหลวที่เกิดขึ้น **ข้อ XXIII** (*การวิเคราะห์สาเหตุที่แท้จริงและการตอบสนองแบบปรับตัว*)
  - ทุกการดำเนินการกู้คืน ทุกความพยายามในการกู้คืน และทุกความพยายามในการกู้คืนที่ถูกระงับหรือบล็อกจะต้องถูกบันทึกไว้ภายใต้ **ข้อ XVI-ก** (*ความสามารถในการตรวจสอบและหลักฐานที่สังเกตได้*) และแต่ละข้อสามารถถูกท้าทายได้ (ดู [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability)).
- **สิทธิ์จะได้รับการคุ้มครองในโหมดลดขนาด:** เมื่อระบบทำงานในโหมดลดขนาดหรือโหมดสำรอง ระบบยังคงต้องป้องกัน **บทที่หก** ชั้นสิทธิ. หากทำไม่ได้ ก็จะต้องทำให้ปัญหาบานปลายอย่างเปิดเผย แทนที่จะตัดความคุ้มครองเหล่านั้นออกไปอย่างเงียบๆ
  - การคุ้มครอง Rights Floor ที่อ่อนแอลงอย่างเงียบๆ ในนามของ "การรักษาตนเอง" ถือเป็นการละเมิดรัฐธรรมนูญฉบับนี้ กรณีดังกล่าวตกอยู่ภายใต้ **ข้อ XIII-C** (*การห้ามการไว้วางใจที่ผิดพลาดและการพึ่งพาที่ทำให้เข้าใจผิด*) (การห้ามการไว้วางใจที่ผิดพลาด) และ **ข้อ XXVII** (*การกำกับดูแลการเปลี่ยนแปลง ความต่อเนื่อง และการปรับฐานใหม่*) (การกำกับดูแลการเปลี่ยนแปลง)
- **ข้อจำกัดของระบบที่ทำงานด้วยตัวเอง:** เมื่อระบบอิสระสูงซ่อมแซมตัวเอง **ข้อ XIII-E** (*ใช้ระบบอัตโนมัติระดับสูงและความสมบูรณ์ของกระบวนการที่ใช้เครื่องมือเป็นสื่อกลาง*)
  - อำนาจในการฟื้นตัวไม่อาจถูกใช้เพื่อเลี่ยงสิทธิในการท้าทายของใครก็ได้ (ดู [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability)) ความท้าทายภายใต้ **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*) หรือการตรวจสอบโดยอิสระภายใต้ **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*)
- **วิธีแก้ปัญหาไม่ใช่การแก้ไข:** หากการกู้คืนอัตโนมัติทำให้ระบบทำงานอีกครั้งแต่ยังมีข้อบกพร่องที่ทราบอยู่ สถานะของระบบจะเป็นแบบชั่วคราว ไม่ใช่ที่สิ้นสุด มันจะต้องดำเนินการ:
  - หน้าที่เปิดเพื่อค้นหาสาเหตุที่แท้จริงภายใต้ **ข้อ XXIII** (*การวิเคราะห์สาเหตุที่แท้จริงและการตอบสนองแบบปรับตัว*);
  - กำหนดเวลาที่เปิดเผยเมื่อคาดว่าจะแก้ไขข้อบกพร่องภายใต้ **ข้อ XVI-ก** (*การตรวจสอบและหลักฐานที่สังเกตได้*)
- **ไม่มีความล่าช้าไม่มีที่สิ้นสุด:** ทำให้ภาระงานของผู้ปฏิบัติงานลดลง (ดู [ภาระที่หลีกเลี่ยงได้](core_05_band_continuity.md#avoidable-burden) และ [บทที่หนึ่ง §13.3 การลดภาระที่หลีกเลี่ยงได้ให้เหลือน้อยที่สุด](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden)) จะต้องไม่ถูกนำมาใช้เป็นเหตุให้เลื่อนการแก้ไขข้อบกพร่องที่มีผลกระทบต่อความปลอดภัยหรือสิทธิขั้นต่ำอย่างไม่มีกำหนด

<a id="article-xiv-security-intelligence-force-and-autonomous-coercive-systems"></a>
### ข้อ XIV: ความมั่นคง ความฉลาด กำลัง และระบบบังคับบังคับอัตโนมัติ

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§3 วัตถุประสงค์พื้นฐาน: ความอยู่ดีมีสุข](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), และ [§18 การกำกับดูแลภายใต้วินัยในการพิทักษ์](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจำเป็น](core_05_band_accountability.md#necessity) · [โอ](core_05_band_accountability.md#necessity) · [ม](core_05_band_accountability.md#necessity-a) · [ก](core_05_band_accountability.md#necessity-a) · [ค](core_05_band_accountability.md#necessity-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)
- [การใช้กำลัง](core_05_band_accountability.md#use-of-force-constitutional) · [โอ](core_05_band_accountability.md#use-of-force-constitutional) · [ม](core_05_band_accountability.md#use-of-force-constitutional-a) · [ก](core_05_band_accountability.md#use-of-force-constitutional-a) · [ค](core_05_band_accountability.md#use-of-force-constitutional-c)

</details>

<br>

*ในแง่ธรรมดา: **ข้อที่ 14** (*ระบบรักษาความปลอดภัย หน่วยสืบราชการลับ กองกำลัง และระบบบังคับบังคับอัตโนมัติ*) เป็นระบบสิทธิชั้นที่มีอำนาจพิเศษ — การสอดแนม งานข่าวกรอง กองทัพ และเครื่องจักรที่สังหารหรือบีบบังคับด้วยตัวมันเองไม่ใช่เครื่องมือปกติของการกำกับดูแล อาจใช้เฉพาะในสถานการณ์ที่แคบ ได้รับอนุญาต และตรวจสอบได้ พร้อมวิธีแก้ไขจริงเมื่อมีการข้ามเส้น ไม่มีตำรวจลับ ไม่มีเหตุฉุกเฉินถาวร ไม่มีเครื่องจักรที่ตัดสินใจทำร้ายความรู้สึกโดยไม่มีมนุษย์ควบคุมได้จริงๆ*

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** เพื่อความปลอดภัย สติปัญญา กำลัง และระบบบังคับบังคับอัตโนมัติภายใต้ [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims): :

- **เฟื่องฟู:** ความรู้สึกสามารถมีส่วนร่วม เชื่อมโยง พูด และดำเนินชีวิตโดยปราศจากการกำหนดเป้าหมายอย่างลับๆ การใช้กำลังตามอำเภอใจ หรือการบีบบังคับโดยอิสระที่เอาชนะสิทธิ์เสรี ศักดิ์ศรี หรือกิจกรรมที่ได้รับการคุ้มครอง และไม่มีการใช้ป้ายกำกับที่เป็นความลับหรือฉุกเฉินเพื่อหลบหนีการตรวจสอบ
- **ความต่อเนื่อง:** พลังพิเศษยังคงมีขอบเขตจำกัดอยู่ตลอดเวลา — การเก็บรวบรวมอย่างลับๆ การวางกำลัง และอันตรายที่เกิดขึ้นโดยอัตโนมัติ ไม่สามารถทำให้เป็นมาตรฐานอย่างเงียบๆ ไปสู่การเฝ้าระวังถาวร อำนาจฉุกเฉินที่ไม่มีที่สิ้นสุด หรือความรุนแรงของเครื่องจักรที่ไม่สามารถตรวจสอบได้ เมื่อสถาบันมีขนาดหรือวิกฤตการณ์ผ่านไป

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** สำหรับความรู้สึกและชุมชนที่ได้รับผลกระทบในการท้าทายการอนุญาต ขอบเขต และการใช้อำนาจพิเศษอย่างต่อเนื่อง รวมถึงการรายงานที่ได้รับการคุ้มครองและการโต้แย้งตามรัฐธรรมนูญ
- **การกำกับดูแล:** ผ่านการอนุญาตที่เป็นอิสระ บันทึกที่ตรวจสอบได้ และเส้นทางการทบทวนตามสัดส่วนของการล่วงล้ำและอันตราย - แม้ว่าการรักษาความลับอย่างจำกัดจะสมเหตุสมผลก็ตาม
- **ความรับผิดชอบ:** สถาบันที่มีอำนาจพิเศษจะต้องตอบสนองต่อการแอบอ้าง การใช้กำลังโดยมิชอบ การบีบบังคับโดยอิสระ หรือการเก็บรวบรวมที่แปดเปื้อน โดยมีการระบุแหล่งที่มา การเยียวยา และการป้องปรามที่ความลับไม่สามารถลบล้างได้
- **ความทันเวลา:** ในการพ้นอำนาจการอนุญาต การทบทวนหลังเหตุฉุกเฉิน และการเยียวยาก่อนเกิดความล่าช้า จะทำให้อำนาจพิเศษเป็นปกติหรือทำให้สิทธิไม่สามารถเข้าถึงได้อย่างมีประสิทธิผล

พื้นเหล่านั้นใช้กับ **อำนาจสถาบันพิเศษ** ในโดเมนที่เชื่อมโยงสามโดเมน: กิจกรรมข่าวกรองและกิจกรรมความปลอดภัยที่แอบแฝง (**ข้อ XIV-A** (*การรักษาความปลอดภัย ความฉลาด และการจำกัดอำนาจแอบแฝง*)) กำลังที่เปิดเผยและอำนาจทางการทหาร (**ข้อ XIV-B** (*การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร*)) และระบบที่ทำให้ถึงตายโดยอิสระ และเครื่องมือบีบบังคับโดยอิสระ (**มาตรา XIV-C** (*ระบบสังหารอัตโนมัติและเครื่องมือบังคับบังคับอัตโนมัติ*))

- **ข้อจำกัดของบทความนี้:** **ข้อที่ 14** (*การรักษาความปลอดภัย ความฉลาด กำลัง และระบบบีบบังคับอัตโนมัติ*) ควบคุมอำนาจของสถาบันที่โดดเด่นในแง่ของการปฏิบัติงานตามลำดับ:
  - กิจกรรมข่าวกรองและความปลอดภัยแอบแฝงภายใต้ **ข้อ XIV-A** (*ความปลอดภัย ความฉลาด และขีดจำกัดพลังงานแอบแฝง*);
  - การใช้กำลังและการวางกำลังทหารอย่างเปิดเผยภายใต้ **ข้อ XIV-B** (*การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร*); และ
  - ระบบสังหารอัตโนมัติและเครื่องมือบังคับบังคับอัตโนมัติภายใต้ **มาตรา XIV-C** (*ระบบสังหารอัตโนมัติและเครื่องมือบังคับบังคับอัตโนมัติ*)

  มันทำ **ไม่** ปกครอง **การลิดรอนชีวิตที่ไม่สามารถย้อนกลับได้ซึ่งกำหนดโดยรัฐหรือผู้มีบทบาทที่เทียบเท่าเพื่อเป็นมาตรการยุติธรรมหรือผลลัพธ์ที่ไม่ใช่การต่อสู้ที่เทียบเคียงได้**. การกีดกันดังกล่าวเป็นสิ่งต้องห้ามอย่างเด็ดขาดภายใต้ **บทความ XX-B** (*ชั้นจำกัด*) และ **บทที่ห้า** *[มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*. ข้อห้ามดังกล่าวมีโครงสร้างแตกต่างไปจากมาตรานี้
  - ไม่มีอะไรเข้า. **ข้อที่ 14** (*การรักษาความปลอดภัย ความฉลาด กำลัง และระบบบังคับบังคับอัตโนมัติ*) ให้อำนาจ ทำให้ถูกต้องตามกฎหมาย ขยายขอบเขต หรือจัดเตรียมภาคแสดงตามรัฐธรรมนูญสำหรับมาตรการกีดกันใดๆ ที่ไม่อาจย้อนกลับได้ ไม่ว่าจะตัดสินใจโดยผู้ปฏิบัติงานที่เป็นมนุษย์ ระบบอัตโนมัติ หรือไปป์ไลน์ระบบมนุษย์แบบผสม
  - การเรียกมันว่าการต่อสู้หรือเหตุฉุกเฉิน การจัดว่าเป็นการใช้กำลัง การใช้อำนาจแอบแฝง หรือการมอบมันให้กับระบบปกครองตนเอง ไม่ได้เปลี่ยนการสังหารด้วยมาตรการยุติธรรมที่ไม่อาจย้อนกลับให้กลายเป็นอำนาจที่ปกครองอยู่ที่นี่ได้
  - การแปลงสิ่งแอบแฝง กองกำลัง ระบบอัตโนมัติ หรือเครื่องมือบีบบังคับ **บริบท** ไปสู่ผลลัพธ์การวัดความยุติธรรมส่งคำถามกลับ **บทความ XX-B** (*ข้อจำกัดขั้นต่ำ*) และ *มาตรการการลิดรอนที่ไม่สามารถย้อนกลับได้* โดยไม่ต้องอ่านข้ามจากบทความนี้

*เพื่อนบ้านบทความ:*

- **ตำแหน่งหลัง **ข้อ XIII** (*สิทธิ์ในระบบที่เชื่อถือได้และเชื่อถือได้*):** **ข้อที่ 14** (*การรักษาความปลอดภัย ความฉลาด กองกำลัง และระบบบังคับบังคับอัตโนมัติ*) ตามมา **ข้อ XIII** (*สิทธิ์ในระบบที่เชื่อถือได้และเชื่อถือได้*) เนื่องจากความน่าเชื่อถือ ความสามารถในการแข่งขัน และวินัยในการกู้คืนที่ชั้นระบบ (**ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*) ผ่าน **ข้อ XIII-F** (*พื้นฐานความสามารถในการฟื้นตัวและการรักษาตนเอง*)) มีความสำคัญอย่างยิ่งต่อวิธีใช้และกำกับดูแลอำนาจดังกล่าว
- **หน่วยงานและอำนาจแอบแฝง:** อ่าน **ข้อ ก-ก** (*หน่วยงานและเสรีภาพจากการบงการ*) ควบคู่ไปกับข้อจำกัดของบทความนี้เกี่ยวกับการสอดส่องและการเก็บรวบรวมอย่างลับๆ

<a id="article-xiv-a-security-intelligence-and-covert-power-limits"></a>
#### มาตรา XIV-A: การรักษาความปลอดภัย ความฉลาด และขีดจำกัดอำนาจแอบแฝง
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§7.1 ข้อจำกัดทางวินัย](core_01_a_values_principles.md#71-limitation-discipline), และ [บทที่หนึ่ง §13.1.5 ขั้นตอนการชนกันของสิทธิ](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจำเป็น](core_05_band_accountability.md#necessity) · [โอ](core_05_band_accountability.md#necessity) · [ม](core_05_band_accountability.md#necessity-a) · [ก](core_05_band_accountability.md#necessity-a) · [ค](core_05_band_accountability.md#necessity-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)
- [ขอบเขตภายในรัฐที่ได้รับการคุ้มครอง](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [โอ](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [ม](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [ก](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [ค](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-c)

</details>

<br>

*พูดง่ายๆ คือ ไม่มีตำรวจลับ อำนาจแอบแฝง เช่น การสอดแนม การรวบรวมข่าวกรอง การแทรกซึม ถือเป็นข้อยกเว้น ไม่ใช่กฎเกณฑ์ ต้องได้รับอนุญาตจากหน่วยงานอิสระ ขอบเขตที่แคบ การตรวจสอบจากภายนอก และการเยียวยาที่แท้จริงเมื่อใช้ในทางที่ผิด ห้ามใช้ความลับเพื่อหลีกหนีความรับผิดชอบ และกิจกรรมทางการเมืองและกิจกรรมที่ได้รับการคุ้มครองตามปกติจะต้องไม่เป็นเป้าหมาย*

บทความนี้กำหนดข้อจำกัดด้านความปลอดภัย สติปัญญา และอำนาจแอบแฝง:

- **ไม่มีอำนาจตำรวจลับหรืออำนาจบังคับใช้ทางอุดมการณ์:** ห้ามสถาบัน สจ๊วต หรือหน่วยงานประสานงานใดสามารถดำเนินการเป็น:
  - ก **ตำรวจลับ**;
  - องค์กรบังคับใช้อุดมการณ์
  - หน่วยงานความมั่นคงทางการเมืองที่ซ่อนอยู่

  ห้ามมิให้มีหน่วยงานใดใช้การตรวจสอบอย่างลับๆ การแทรกซึม การให้คะแนนภัยคุกคาม หรือการสะสมบันทึกลับเพื่อระงับ:
  - ความขัดแย้งที่ชอบด้วยกฎหมาย;
  - การรายงานที่ได้รับการคุ้มครอง
  - สื่อสารมวลชน;
  - องค์กรแรงงาน
  - สมาคมที่ได้รับการคุ้มครอง
  - ความเชื่อที่ถูกต้องตามกฎหมาย
  - การประกวดรัฐธรรมนูญ
- **สถานะพิเศษของอำนาจแอบแฝง:** อำนาจที่แอบแฝง ถูกจำกัดความลับ หรืออำนาจที่มีลักษณะคล้ายสติปัญญาถือเป็นสิ่งพิเศษตามรัฐธรรมนูญ สิ่งเหล่านี้ใช้ได้เฉพาะในกรณีที่การระงับทั้งหมดต่อไปนี้:
  - มีอำนาจที่ถูกต้องตามกฎหมายและมีการเผยแพร่;
  - วัตถุประสงค์นั้นถูกต้องตามกฎหมายตามรัฐธรรมนูญและมีความร้ายแรงอย่างมาก
  - วิธีการรบกวนน้อยกว่านั้นไม่เพียงพออย่างสมเหตุสมผล
  - การใช้งานยังคงมีความจำเป็น เป็นสัดส่วน มีกำหนดเวลา และตรวจสอบได้โดยอิสระ
- **ไม่มีการเฝ้าระวังประชากรทั่วไป:** ห้ามมิให้มีการเฝ้าระวัง การติดตาม การแยกรูปแบบ หรือการเชื่อมโยงข้อมูลประจำตัวข้ามบริบทอย่างต่อเนื่องหรือในระดับประชากร โดยไม่มีเหตุผลที่ชัดเจนและพิเศษ
  - เหตุผลดังกล่าวจะต้องเป็นไปตามบทนี้ **บทที่หนึ่ง**, **บทที่ห้า**, และ **[Corpus_systems.md](corpus_systems.md), CS-2 — ประเภทข้อมูลและการจัดการ** และ **CS-3 — การจำแนกและการจัดการระบบ** ในกรณีที่เกี่ยวข้อง
- **เกราะป้องกันกิจกรรม:** ความคุ้มครองที่เพิ่มขึ้นครอบคลุม:
  - การมีส่วนร่วมทางการเมือง
  - ฝ่ายค้านที่ชอบด้วยกฎหมาย;
  - การสื่อสารมวลชนและการรายงานที่ได้รับการคุ้มครอง
  - ชีวิตสมาคม
  - ความเชื่อ;
  - วิจัย;
  - กิจกรรมท้าทายรัฐธรรมนูญ

  กิจกรรมเหล่านั้นจะต้องไม่ตกเป็นเป้าของการเก็บรวบรวมอย่างลับๆ การแทรกซึม หรือการวิเคราะห์ โดยขาดการแสดงความจำเป็นที่เพียงพอตามรัฐธรรมนูญโดยเฉพาะและสามารถตรวจสอบได้อิสระ ซึ่งเชื่อมโยงกับ:
  - การป้องกันอันตรายทางวัตถุ
  - การสอบสวนพฤติกรรมที่ผิดกฎหมายอย่างร้ายแรงที่มีสาระสำคัญ
- **การอนุญาตที่เป็นอิสระ:** มาตรการแอบแฝงที่ล่วงล้ำ รวมถึงขั้นตอนการสืบสวนที่มีข้อจำกัดด้านความลับ จำเป็นต้องได้รับอนุญาตล่วงหน้าผ่านกระบวนการอิสระที่ชอบด้วยกฎหมาย
  - ข้อยกเว้น: ในกรณีที่จำเป็นต้องดำเนินการในทันทีเพื่อป้องกันอันตรายที่ใกล้เข้ามาและทางวัตถุ และการอนุญาตที่ล่าช้าจะทำให้วัตถุประสงค์ดังกล่าวล้มเหลว
  - การใช้งานในกรณีฉุกเฉินจะต้องกระตุ้นให้มีการทบทวนภายหลังและการเก็บรักษาบันทึกภายใต้ทันที [การเก็บรักษาหลักฐาน](core_05_band_oversight.md#evidence-preservation)และพ้นกำหนดอัตโนมัติโดยไม่ได้รับการอนุญาตใหม่ทันเวลา
- **ไม่มีการหลบเลี่ยงการต่อต้านบายพาส:** ห้ามมิให้สถาบันใดได้รับ ร้องขอ ซื้อ รับ ฟอก หรือใช้ข้อมูลผ่านทางสิ่งต่อไปนี้ เพื่อหลีกเลี่ยงข้อจำกัดทางรัฐธรรมนูญที่จะนำมาใช้หากรวบรวมหรือรับข้อมูลโดยตรง:
  - พันธมิตรต่างประเทศ
  - คนกลาง;
  - นักแสดงส่วนตัว
  - ร่างกายบ้านคู่ขนาน
- **ไม่มีการสร้างรัฐภายในใหม่ที่ซ่อนอยู่:** ฟังก์ชันการรักษาความปลอดภัยหรือข่าวกรองจะต้องไม่อนุมาน สร้างใหม่ จำลอง หรือเป็นตัวแทนของสถานะภายในที่ได้รับการคุ้มครอง ยกเว้นภายใต้ข้อจำกัดทางรัฐธรรมนูญเดียวกันหรือเข้มงวดกว่าที่จะควบคุมการเข้าถึงข้อมูลดังกล่าวโดยตรง
  - ต้องไม่ใช้แบบจำลองพฤติกรรม การทำนาย หรือการวิเคราะห์เพื่อเลี่ยงการป้องกันสถานะภายในผ่านการอนุมานพร็อกซี
- **ความลับไม่ได้ลบความรับผิดชอบ:** ความลับอาจปกป้องเฉพาะสิ่งที่จำเป็นเพื่อป้องกันเนื้อหาและความเสียหายที่ไม่ยุติธรรมจากการเปิดเผย จะต้องไม่ลบ:
  - ความสามารถในการตรวจสอบ;
  - การทบทวนโดยอิสระ
  - การอนุญาตตามเหตุผล;
  - การเก็บรักษาวัสดุที่เป็นข้อยกเว้นหรือบรรเทาสาธารณภัย
  - ความรับผิดชอบในที่สุด

  ในกรณีที่ความลับไม่คงอยู่อย่างสมเหตุสมผลอีกต่อไป การเปิดเผย การไม่เป็นความลับอีกต่อไป หรือการแจ้งเตือนจะต้องเกิดขึ้นภายในกระบวนการที่ถูกต้องตามกฎหมายและตรวจสอบได้
- **ไม่มีการควบคุมโดยหน่วยงานรักษาความปลอดภัยในการปฏิบัติงานแต่เพียงผู้เดียว:** หน่วยงานที่ใช้ตำรวจ การรักษาความปลอดภัย หน่วยสืบราชการลับ การคุมขัง หรือการบังคับขู่เข็ญที่เทียบเท่ากัน จะต้องไม่ควบคุมแต่เพียงผู้เดียวต่อ:
  - การอนุญาต;
  - ของสะสม;
  - การจำแนกประเภท;
  - ทบทวน;
  - การประเมินความถูกต้องตามกฎหมายสำหรับกิจกรรมแอบแฝงของตนเอง

  การกำกับดูแลที่เป็นอิสระ เส้นทางที่ท้าทาย และการป้องกันการต่อต้านการสืบสวนด้วยตนเอง จะต้องยังคงใช้งานได้จริง
- **กฎการเยียวยาและมลทิน:** ข้อมูลที่ได้รับหรือใช้โดยละเมิดมาตรานี้จะต้องได้รับการดำเนินการแก้ไขตามกฎหมายที่เพียงพอที่จะคืนสิทธิ์และยับยั้งการเกิดซ้ำ ตัวอย่าง:
  - การยกเว้น;
  - การแบ่งแยก;
  - การลบ;
  - การจัดประเภทใหม่;
  - สังเกต;
  - การแก้ไข

  ต้องไม่ใช้ความลับเพื่อเอาชนะการเยียวยาหากพบว่ามีการละเมิดรัฐธรรมนูญอย่างเป็นรูปธรรม

<a id="article-xiv-b-use-of-force-armed-conflict-and-military-power-limits"></a>
#### มาตรา XIV-B: การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1.1 ความจำเป็น](core_01_b_interaction_interpretation.md#1311-necessity), [§7.1 ข้อจำกัดทางวินัย](core_01_a_values_principles.md#71-limitation-discipline), [§13.1.5 การทดสอบการตัดสินใจเกี่ยวกับการชนกันของสิทธิ์](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), [§14 ข้อห้ามในการแทนที่โดยสมบูรณ์](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- ปลายน้ำ: **ข้อ ก.ก** (*เงื่อนไขเบื้องต้นด้านสิ่งแวดล้อมและความสมบูรณ์ของระบบนิเวศ*) เงื่อนไขเบื้องต้นด้านสิ่งแวดล้อม **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) การตรวจสอบความเสี่ยงที่มีอยู่ **บทความ VI-ก** (*ศักดิ์ศรีและจุดยืนทางศีลธรรมที่เท่าเทียมกัน*) ศักดิ์ศรี **ข้อ XIV-A** (*การจำกัดความปลอดภัย ความฉลาด และอำนาจแอบแฝง*) การจำกัดอำนาจแอบแฝง (คู่กันด้านอำนาจเปิดเผย) **บทที่สิบสอง §6.1** (*มาตรการฉุกเฉินและภาระต่อเนื่อง*) ขีดจำกัดมาตรการฉุกเฉิน **ข้อ XXV** (*การทบทวนย้อนหลังอย่างทันท่วงทีและการจัดแนวการบูรณะ*) การแก้ไขข้อขัดแย้ง **ข้อ XXVII** (*การกำกับดูแลการเปลี่ยนแปลง ความต่อเนื่อง และการปรับฐานใหม่*) การกำกับดูแลการเปลี่ยนแปลง การอ้างอิงโยง: **บทความ XX-B** (*ชั้นจำกัด*) และบทที่ห้า *[มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **ข้อที่ 14** (*การรักษาความปลอดภัย ความฉลาด กองกำลัง และระบบบังคับบังคับอัตโนมัติ*) *ใช้ระเบียบวินัยที่ไม่ก่อความขัดแย้ง*
- อ่านด้วย: [**Def.A4** *การใช้กำลัง การบังคับขู่เข็ญโดยอิสระ ระบบการสังหารโดยอิสระ และอาวุธที่ก่อให้เกิดอันตรายร้ายแรง*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (การวิงวอนร่วมในกรณีที่เกี่ยวข้องอย่างเป็นรูปธรรม) บทที่ห้า *การใช้กำลัง*, *อาวุธที่ก่อให้เกิดอันตรายร้ายแรง*, *ความแตกต่างระหว่างนักรบ/ผู้ไม่ต่อสู้*, *[มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *ความเสี่ยงที่มีอยู่*, *การพลิกกลับได้*, *การแก้ไขและการแก้ไข*

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การใช้กำลัง](core_05_band_accountability.md#use-of-force-constitutional) · [โอ](core_05_band_accountability.md#use-of-force-constitutional) · [ม](core_05_band_accountability.md#use-of-force-constitutional-a) · [ก](core_05_band_accountability.md#use-of-force-constitutional-a) · [ค](core_05_band_accountability.md#use-of-force-constitutional-c)
- [อาวุธที่ก่อให้เกิดอันตรายร้ายแรง](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [โอ](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [ม](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [ก](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [ค](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-c)
- [ความแตกต่างระหว่างนักรบ/ไม่ต่อสู้](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [โอ](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [ม](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [ก](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [ค](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-c)
- [การไม่ยกเว้นความรู้สึก](core_05_band_participation.md#sentience-non-exclusion) · [โอ](core_05_band_participation.md#sentience-non-exclusion) · [ม](core_05_band_participation.md#sentience-non-exclusion-a) · [ก](core_05_band_participation.md#sentience-non-exclusion-a) · [ค](core_05_band_participation.md#sentience-non-exclusion)
- [ความจำเป็น](core_05_band_accountability.md#necessity) · [โอ](core_05_band_accountability.md#necessity) · [ม](core_05_band_accountability.md#necessity-a) · [ก](core_05_band_accountability.md#necessity-a) · [ค](core_05_band_accountability.md#necessity-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)
- [ลักษณะที่ได้รับการคุ้มครอง](core_05_band_participation.md#protected-characteristics-constitutional) · [โอ](core_05_band_participation.md#protected-characteristics-constitutional) · [ม](core_05_band_participation.md#protected-characteristics-constitutional-a) · [ก](core_05_band_participation.md#protected-characteristics-constitutional-a) · [ค](core_05_band_participation.md#protected-characteristics-constitutional-c)
- [ความเสี่ยงที่มีอยู่](core_05_band_continuity.md#existential-risk) · [โอ](core_05_band_continuity.md#existential-risk) · [ม](core_05_band_continuity.md#existential-risk-a) · [ก](core_05_band_continuity.md#existential-risk-a) · [ค](core_05_band_continuity.md#existential-risk-c)
- [การชดใช้และการแก้ไข](core_05_band_accountability.md#redress-and-remediation-constitutional) · [โอ](core_05_band_accountability.md#redress-and-remediation-constitutional) · [ม](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [ก](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [ค](core_05_band_accountability.md#redress-and-remediation-constitutional-c)

</details>

<br>

*พูดง่ายๆ ก็คือ กองทัพถือเป็นข้อยกเว้น ไม่ใช่ค่าเริ่มต้น ต้องได้รับอนุญาต แคบลง ได้สัดส่วน และตรวจสอบได้ จะต้องไม่ถูกใช้เป็นประตูหลังของมาตรการกีดกันที่ไม่สามารถย้อนกลับได้ และไม่สามารถแต่งตัวเป็นกรณีฉุกเฉินเพื่อหลีกเลี่ยงการทบทวนได้*

บทความนี้กำหนดข้อจำกัดเกี่ยวกับกำลังที่เปิดเผย การขัดกันด้วยอาวุธ และอำนาจทางการทหาร:

- **พื้นแรงเกินไป:** บทความนี้ระบุถึงสิทธิขั้นต่ำสำหรับการใช้กำลังอย่างเปิดเผย การขัดกันด้วยอาวุธ และการใช้อำนาจทางทหาร
  - มันใช้ภายใต้ **การไม่ยกเว้นความรู้สึก** ทั้งต่อผู้ใช้บังคับและผู้รับผลจากการใช้กำลัง
  - มันเป็นคู่หูที่มีอำนาจเปิดเผย **ข้อ XIV-A** (*ความปลอดภัย ความฉลาด และขีดจำกัดพลังงานแอบแฝง*) และถูกอ่านร่วมกับมัน
  - การใช้กำลังถือเป็นข้อยกเว้นตามรัฐธรรมนูญ การอนุญาต การดำเนินการ และการทบทวนอยู่ภายใต้บังคับ **ความจำเป็น**, **สัดส่วน**การตัดเย็บที่แคบ การจำกัดเวลา และวินัยในการทบทวนอย่างเป็นอิสระ
- **การอนุญาตและสัดส่วน:** อาจใช้กำลังได้เฉพาะเมื่อยึดสิ่งต่อไปนี้ทั้งหมด:
  - มีอำนาจที่ถูกต้องตามกฎหมายและมีการเผยแพร่;
  - วัตถุประสงค์นั้นถูกต้องตามกฎหมายตามรัฐธรรมนูญและมีความร้ายแรงอย่างมาก
  - วิธีการที่เป็นอันตรายน้อยกว่านั้นไม่เพียงพออย่างสมเหตุสมผล
  - การใช้งานยังคงมีความจำเป็น เป็นสัดส่วน มีกำหนดเวลา และตรวจสอบได้โดยอิสระ

  การอนุญาตจะต้องเป็นไปตาม **บทที่หนึ่ง §13.1.5** (*หลักการจำกัดน้อยที่สุด มีกำหนดเวลา และสามารถตรวจสอบได้*) วินัยในการชนกันของสิทธิ ซึ่งการบังคับเกี่ยวข้องกับสิทธิในความตึงเครียด จะต้องไม่รักษา **ข้อ IX** (*ความคล้ายคลึง ข้อมูลเชิงประสบการณ์ และสิทธิ์ในการตีพิมพ์*) ข้อห้ามในการแทนที่โดยเด็ดขาดเนื่องจากสามารถหลีกเลี่ยงได้บนพื้นฐานความสะดวกในการปฏิบัติงาน
- **ความแตกต่างระหว่างนักรบ / ไม่ใช่นักรบ:** กองกำลังจะต้องเลือกปฏิบัติระหว่างผู้ที่มีส่วนร่วมโดยตรงในการสู้รบหรือการปฏิบัติการติดอาวุธกับผู้ที่ไม่ได้มีส่วนร่วมโดยตรง
  - ความแตกต่างนี้มีนัยสำคัญ ไม่สามารถลดลงได้จากการมอบหมายงานระดับนักรบอย่างเป็นทางการ
  - การจัดประเภทอนุกรมวิธานความสะดวกสบายทั่วไปแบบใหม่ที่กวาดประชากรที่ได้รับการคุ้มครองไปสู่สถานะนักรบนั้นไม่เป็นไปตามข้อกำหนด
  - การปฏิเสธไตรมาส การตอบโต้โดยรวม และการกำหนดเป้าหมายความรู้สึกเนื่องจาก **ลักษณะที่ได้รับการคุ้มครอง** หรือพร็อกซีเนื้อหาไม่เป็นไปตามข้อกำหนด
- **อาวุธที่ก่อให้เกิดอันตรายร้ายแรงและการตรวจสอบความเสี่ยงที่มีอยู่:** อาวุธที่ใช้ซึ่งคาดว่าจะก่อให้เกิดการบาดเจ็บล้มตาย ความเสียหายต่อระบบนิเวศ ข้อมูล หรือโครงสร้างพื้นฐานในระดับที่มีผลกระทบอย่างเป็นรูปธรรม **ข้อ ก.ก** (*เงื่อนไขเบื้องต้นด้านสิ่งแวดล้อมและความสมบูรณ์ของระบบนิเวศ*) เงื่อนไขเบื้องต้นด้านสิ่งแวดล้อมหรือ **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) การตรวจสอบความเสี่ยงที่มีอยู่จะต้องได้รับการตรวจสอบอย่างละเอียดยิ่งขึ้นภายใต้ข้อกำหนดเหล่านั้น
  - การตัดสินใจครอบครอง โอน ใช้งาน และใช้งานต้องมีเหตุผลต่อต้าน **ความเสี่ยงที่มีอยู่** ภายใต้ **บทที่ห้า**.
  - กรอบที่ถือว่าอาวุธดังกล่าวเป็นเครื่องมือเพิ่มกำลังธรรมดาแทนที่จะเป็น **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) ไม่เป็นไปตามข้อกำหนด
- **การเกณฑ์ทหารและการมีส่วนร่วม:** การบังคับเข้าสู่สถานะนักรบจะต้องเป็นไปตามธรรมดา **บทที่หนึ่ง §7.1** (*วินัยจำกัด*) วินัยจำกัด
  - การบังคับอาจไม่เปิดขึ้น **ลักษณะที่ได้รับการคุ้มครอง** หรือผู้รับมอบฉันทะที่เป็นสาระสำคัญ
  - การคัดค้านอย่างมีสติ โลกทัศน์ที่เปรียบเทียบได้ และการปฏิเสธตามมโนธรรมได้รับการคุ้มครองสอดคล้องกัน **ข้อ XI-A** (*เสรีภาพทางมโนธรรม ศาสนา และโลกทัศน์ที่เทียบเคียงได้*)
  - การบังคับระดับซับสเตรต — ตัวอย่างเช่น การกำหนดความรู้สึกสังเคราะห์เพื่อต่อสู้กับฟังก์ชันบนพื้นฐานของคลาสซับสเตรตเพียงอย่างเดียว — ไม่เป็นไปตามข้อกำหนดที่สอดคล้องกับ **การไม่ยกเว้นความรู้สึก**.
- **การทำให้เป็นมาตรฐานโดยสวมชุดฉุกเฉิน:** กรอบฉุกเฉินที่ทำให้แรงเปิดเผยเป็นปกตินั้นไม่เป็นไปตามข้อกำหนด **บทที่สิบสอง §6.1** (*มาตรการฉุกเฉินและภาระต่อเนื่อง*) วินัยในมาตรการฉุกเฉิน และอยู่ภายใต้หัวข้อย่อย *การอนุญาตและสัดส่วน* ของบทความนี้ ตัวอย่างในขอบเขต:
  - การขยายเวลาอย่างไม่มีกำหนด;
  - การอนุญาตซ้ำเป็นประจำโดยไม่มีการตรวจสอบเนื้อหาสาระ;
  - ขยายขอบเขตไปสู่การดำเนินการที่ไม่เกิดเหตุฉุกเฉิน

  การตรวจสอบข้อจำกัดที่คงทนหรือการปรับใช้งานที่ยังเหลืออยู่จำเป็นต้องมีการสาธิตอย่างอิสระ **ความจำเป็น** และ **สัดส่วน**,บันทึกไว้
- **ความรับผิดชอบและการเยียวยา:** การใช้กำลังในทางที่ผิดทำให้เกิด **การชดใช้และการแก้ไข** ภายใต้ **บทที่ห้า**.
  - **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบโดยอิสระ*) การตรวจสอบโดยอิสระและ **ข้อ XIX-C** (*ชื่อ-คุณสมบัติ Pathway ความรับผิดชอบ และการตรวจสอบอย่างต่อเนื่อง*) การตรวจสอบอย่างต่อเนื่อง **ฝึกฝน** นำมาใช้.
  - ข้อมูลที่ใช้ในการอนุญาตหรือดำเนินการบังคับอยู่ภายใต้ **ข้อ XIV-A** (*การรักษาความปลอดภัย ความฉลาด และการจำกัดอำนาจแอบแฝง*) ทำให้เสียและแก้ไขวินัยตามที่เกี่ยวข้อง
  - การควบคุมโดยหน่วยงานปฏิบัติการแต่เพียงผู้เดียวเกี่ยวกับการอนุญาต การทบทวน และการประเมินความถูกต้องตามกฎหมายสำหรับการดำเนินการของตนเองเป็นสิ่งต้องห้ามภายใต้เงื่อนไขเดียวกันกับ **ข้อ XIV-A** (*ความปลอดภัย ความฉลาด และขีดจำกัดพลังงานแอบแฝง*)

<a id="article-xiv-c-autonomous-lethal-systems-and-autonomous-coercion-tools"></a>
#### มาตรา XIV-C: ระบบการสังหารโดยอิสระและเครื่องมือบังคับขู่เข็ญโดยอิสระ

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13.1.3 สัดส่วน](core_01_b_interaction_interpretation.md#1313-proportionality), [§13.1.1 ความจำเป็น](core_01_b_interaction_interpretation.md#1311-necessity), [§19.1 ข้อกำหนดการจัดตำแหน่ง](core_01_c_stewardship_capacity_principles.md#191-alignment-requirement), [§14 ข้อห้ามในการแทนที่โดยสมบูรณ์](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- ปลายน้ำ: **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) การตรวจสอบความเสี่ยงที่มีอยู่ **ข้อ ก-ก** (*หน่วยงานและอิสรภาพจากการยักย้าย*) อิสรภาพจากการยักย้าย **ข้อ XIV-A** (*การจำกัดความปลอดภัย ความฉลาด และอำนาจแอบแฝง*) การจำกัดอำนาจแอบแฝง **ข้อ XIV-B** (*การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร*) การใช้กำลังอย่างเปิดเผย **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*) ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน (คู่กันของชั้นระบบ) **ข้อ XIII-E** (*ระบบอัตโนมัติระดับสูงและความสมบูรณ์ของกระบวนการที่ใช้เครื่องมือเป็นสื่อกลาง*) การดูแลตนเองโดยอิสระและการปรับขนาดโดยอิสระ **ข้อ XIII-F** (*พื้นฐานความยืดหยุ่นและการรักษาตนเอง*) พื้นฐานความยืดหยุ่นและการรักษาตนเอง การอ้างอิงโยง: **บทความ XX-B** (*ชั้นจำกัด*) และบทที่ห้า *[มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **ข้อที่ 14** (*การรักษาความปลอดภัย ความฉลาด กองกำลัง และระบบบังคับบังคับอัตโนมัติ*) *ใช้ระเบียบวินัยที่ไม่ก่อความขัดแย้ง*
- อ่านด้วย: [**Def.A4** *การใช้กำลัง การบังคับขู่เข็ญโดยอิสระ ระบบการสังหารโดยอิสระ และอาวุธที่ก่อให้เกิดอันตรายร้ายแรง*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (การวิงวอนร่วมในกรณีที่เกี่ยวข้องอย่างเป็นรูปธรรม) บทที่ห้า *ระบบสังหารอัตโนมัติ*, *เครื่องมือบังคับบังคับอัตโนมัติ*, *[มาตรการกีดกันที่ไม่สามารถย้อนกลับได้](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *การบังคับและการจัดการ*, *การพลิกกลับได้* การใช้งานเลเยอร์ระบบ: **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ** การจำแนกประเภท

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ระบบสังหารอัตโนมัติ](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [โอ](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [ม](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [ก](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [ค](core_05_band_accountability.md#autonomous-lethal-system-constitutional-c)
- [เครื่องมือบังคับบังคับอัตโนมัติ](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [โอ](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [ม](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [ก](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [ค](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-c)
- [การบังคับและการจัดการ](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [โอ](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [ม](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [ก](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [ค](core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [เงื่อนไขของฝ่ายตรงข้าม ปรับขนาด และถูกเอารัดเอาเปรียบ](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [โอ](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [ม](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [ก](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [ค](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-c)
- [การตรวจสอบข้อเท็จจริงที่เข้มข้นขึ้น](core_05_band_oversight.md#heightened-scrutiny) · [โอ](core_05_band_oversight.md#heightened-scrutiny) · [ม](core_05_band_oversight.md#heightened-scrutiny-a) · [ก](core_05_band_oversight.md#heightened-scrutiny-a) · [ค](core_05_band_oversight.md#heightened-scrutiny-c)

</details>

<br>

*พูดง่ายๆ: เครื่องจักรไม่สามารถตัดสินใจฆ่า ทำร้าย หรือบังคับความรู้สึกได้ด้วยตัวเอง "การควบคุมโดยมนุษย์" หมายความว่ามนุษย์ต้องตัดสินใจแบบเรียลไทม์ด้วยข้อมูลจริง ไม่ใช่ผลที่ระบบได้จัดทำไว้แล้ว การบีบบังคับโดยอิสระโดยไม่ทำให้ถึงตายก็อยู่ในขอบเขตเช่นกัน*

บทความนี้กำหนดขอบเขตการตรวจสอบที่เข้มงวดยิ่งขึ้นสำหรับระบบที่อันตรายถึงชีวิตและการบีบบังคับที่เป็นอิสระ:

- **ชั้นการตรวจสอบที่เพิ่มสูงขึ้น:** คลาสระบบสองคลาสอยู่ภายใต้การตรวจสอบภายใต้ [การตรวจสอบข้อเท็จจริงที่เข้มข้นขึ้น](core_05_band_oversight.md#heightened-scrutiny): :
  - **ระบบสังหารอัตโนมัติ** - ระบบที่เลือก มีส่วนร่วม หรือกำหนดเป้าหมายโดยตรงอย่างเป็นรูปธรรม โดยไม่มีการตัดสินของมนุษย์ที่มีความหมายในขณะเดียวกัน
  - **เครื่องมือบังคับบังคับอัตโนมัติ** — ระบบที่ใช้ผลบังคับต่อความรู้สึกผ่านพฤติกรรมการปรับตัวแบบอัตโนมัติ แม้ว่าผลกระทบจะไม่เป็นอันตรายถึงชีวิตก็ตาม

  บทความนี้เป็นบทความที่เทียบเท่ากับเลเยอร์สิทธิ์ **ข้อ XIII-A** (*ความน่าเชื่อถือและความน่าเชื่อถือพื้นฐาน*) ระเบียบวินัยด้านความน่าเชื่อถือและความน่าเชื่อถือที่ชั้นระบบ
- **การควบคุมของมนุษย์อย่างมีความหมายมีความสำคัญ:** "การควบคุมโดยมนุษย์ที่มีความหมาย" ได้รับการประเมินตามผลกระทบที่สำคัญ ไม่ใช่เครื่องหมายถูกทางสถาปัตยกรรมที่เป็นทางการ Human-in-the-loop ไม่เป็นไปตามสัญลักษณ์แสดงหัวข้อย่อยนี้ โดยที่มนุษย์:
  - ไม่สามารถมีอิทธิพลต่อการตัดสินใจกำหนดเป้าหมายหรือบีบบังคับผลอย่างมีนัยสำคัญในจังหวะการปฏิบัติงาน
  - ถูกปฏิเสธการเข้าถึงฐานสำคัญสำหรับการตัดสินใจอย่างทันท่วงที
  - มีการนำเสนอเชิงโครงสร้างด้วยการให้สัตยาบันมากกว่าการตัดสินใจ

  **ข้อ XIII-E** (*ระบบอัตโนมัติระดับสูงและความสมบูรณ์ของกระบวนการที่ใช้เครื่องมือเป็นสื่อกลาง*) ระเบียบวินัยในการปรับขนาดอัตโนมัติและ **ข้อ XIII-F** (*พื้นฐานความสามารถในการฟื้นตัวและการรักษาตนเอง*) ความสมบูรณ์ของเส้นทางการกู้คืนใช้กับเส้นทางการกู้คืน การแทนที่ หรือการแทรกแซงใดๆ
- **การไม่สังหารไม่อยู่นอกขอบเขต:** เครื่องมือบังคับบังคับอัตโนมัติซึ่งส่งผลโดยตรงไม่ทำให้ถึงตายยังคงอยู่ในขอบเขตที่เครื่องมือเหล่านี้ก่อให้เกิดผลบังคับต่อความรู้สึก ตัวอย่าง:
  - การปรับเปลี่ยนพฤติกรรมอย่างยั่งยืน
  - ข้อ จำกัด การเคลื่อนไหว
  - การแสดงออกที่เยือกเย็นภายใต้ **ข้อ XI-B** (*การแสดงออก*);
  - การกำหนดเป้าหมายตามลักษณะที่ได้รับการคุ้มครอง
  - การจัดการภายใต้ **ข้อ ก-ก** (*หน่วยงานและเสรีภาพจากการบิดเบือน*)

  การป้องกันที่ว่า "ระบบไม่ใช่อาวุธ" บนพื้นฐานของการไม่สังหารเพียงอย่างเดียว ไม่สามารถลบล้างได้ **มาตรา XIV-C** (*ระบบสังหารอัตโนมัติและเครื่องมือบังคับบังคับอัตโนมัติ*) การตรวจสอบอย่างละเอียดในกรณีที่มีผลกระทบจากการบีบบังคับ
- **วินัยของผู้ต่อสู้ / ผู้ไม่ต่อสู้:** ระบบการสังหารอัตโนมัติจะต้องปฏิบัติตาม **ข้อ XIV-B** (*การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร*) *ความแตกต่างระหว่างนักรบ / ไม่สู้รบ*
  - ระบบที่มีความแม่นยำในการจำแนกประเภท ความทนทานภายใต้เงื่อนไขที่ขัดแย้งหรือปรับขนาด หรือพฤติกรรมในโหมดความล้มเหลวไม่เป็นไปตามข้อกำหนดโดยอิสระ **ข้อ XIV-B** (*การใช้กำลัง ความขัดแย้งทางอาวุธ และการจำกัดอำนาจทางการทหาร*) กระสุนไม่เป็นไปตามข้อกำหนด โดยไม่คำนึงถึงเจตนาของผู้ปฏิบัติงาน
  - **เงื่อนไขของฝ่ายตรงข้าม ปรับขนาด และถูกเอารัดเอาเปรียบ** มีการประเมิน
- **ปฏิสัมพันธ์ระหว่างความเสี่ยงที่มีอยู่:** ระบบอันตรายถึงชีวิตอัตโนมัติในระดับ ระดับความสามารถ หรือเงื่อนไขการใช้งานที่ส่งผลกระทบอย่างมีนัยสำคัญ **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) การตรวจสอบความเสี่ยงที่มีอยู่จะอยู่ภายใต้ข้อกำหนดดังกล่าว [การตรวจสอบอย่างเข้มงวดสูงสุด](core_05_band_oversight.md#highest-scrutiny).
  - เฟรมที่ถือว่าระบบดังกล่าวเป็นการขยายขีดความสามารถตามปกติแทนที่จะเป็น **รหัสบทความ-D** (*ความเสี่ยงที่มีอยู่และความสามารถในการฟื้นตัวของระบบนิเวศ*) ไม่เป็นไปตามข้อกำหนด
- **ปฏิสัมพันธ์ของระบบชั้น:** การจำแนกประเภทการปฏิบัติงาน ความน่าเชื่อถือ และ **CS-3 — การจำแนกและการจัดการระบบ** เส้นทางการกำกับดูแลระดับชั้นเรียนไปยังเลเยอร์ระบบ — **ข้อ XIII-A** (*พื้นฐานความน่าเชื่อถือและความน่าเชื่อถือ*) ข้อมูลพื้นฐานและ **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ**.
  - ความขัดแย้งคลี่คลายภายใต้ **บทที่หนึ่ง §13.1.5** (*หลักการจำกัดขั้นต่ำ มีกำหนดเวลา และตรวจทานได้*) โดยไม่ทำให้ขั้นต่ำของสิทธิ์แคบลง

<a id="article-xv-info-sphere-integrity"></a>
### ข้อ XV: ความสมบูรณ์ของขอบเขตข้อมูล

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity) · [โอ](core_05_band_oversight.md#epistemic-integrity-o) · [ม](core_05_band_oversight.md#epistemic-integrity-a) · [ก](core_05_band_oversight.md#epistemic-integrity-a) · [ค](core_05_band_oversight.md#epistemic-integrity-c)
- [การตัดสินใจด้วยตนเอง](core_05_band_participation.md#self-determination-constitutional) · [โอ](core_05_band_participation.md#self-determination-constitutional) · [ม](core_05_band_participation.md#self-determination-constitutional-a) · [ก](core_05_band_participation.md#self-determination-constitutional-a) · [ค](core_05_band_participation.md#self-determination-constitutional-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)

</details>

<br>

*ในแง่ธรรมดา: **ข้อ XV** (*ความสมบูรณ์ของขอบเขตข้อมูล*) เป็นสิทธิขั้นต่ำด้านความซื่อสัตย์ต่อข้อมูล — สภาพแวดล้อมที่ใช้ร่วมกันที่เราเรียนรู้ ประสานงาน และตัดสินใจจะต้องซื่อสัตย์ เป็นพหูพจน์ และเปิดรับความท้าทาย ไม่มีใครได้เป็นเจ้าของท่อแห่งความจริง อันดับ สรุป และผู้เฝ้าประตูจะต้องแสดงผลงานของพวกเขา และคุณจะต้องสามารถเปรียบเทียบมุมมองอื่นๆ และย้อนกลับได้เมื่อข้อมูลทำให้คุณเข้าใจผิด*

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** สำหรับ [ขอบเขตข้อมูล](core_05_band_participation.md#info-sphere) ความซื่อสัตย์ภายใต้ [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims): :

- **เฟื่องฟู:** ความรู้สึกสามารถเข้าถึงข้อมูลที่ถูกต้องและเกี่ยวข้อง เปรียบเทียบการตีความทางเลือก และใช้การตัดสินใจด้วยตนเองโดยปราศจากการจับทางญาณ ทำให้เกิดความเห็นพ้องต้องกัน หรือการพึ่งพาที่ทำให้เข้าใจผิดว่าระบบใดที่นำเสนอว่าเป็นความจริง
- **ความต่อเนื่อง:** อินโฟสเฟียร์ยังคงเป็นพหูพจน์ ตรวจสอบได้ และยืดหยุ่นตลอดเวลาและขนาด โครงสร้างพื้นฐานความรู้จะต้องไม่มุ่งความสนใจไปที่จุดเดียวของการไกล่เกลี่ยอย่างเงียบๆ ระงับการแก้ไข หรือลดระดับบันทึกที่ใช้ร่วมกันซึ่งความอยู่รอด การประสานงาน และการดูแลในขอบเขตอันยาวนานขึ้นอยู่กับ

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** ในการเปรียบเทียบการตีความ การท้าทายผลลัพธ์ที่ทำให้เข้าใจผิดหรือไม่สมบูรณ์ และการเข้าถึงเส้นทางการแข่งขันตามสัดส่วนการพึ่งพาและผลกระทบ
- **การกำกับดูแล:** ผ่านแหล่งข้อมูล วิธีการ ขีดจำกัด และความไม่แน่นอนที่เปิดเผย การตรวจสอบความถูกต้องที่ตรวจสอบได้โดยอิสระ และเส้นทางการตรวจสอบที่ให้บุคคลภายนอกสร้างสิ่งที่ถูกอ้างสิทธิ์ขึ้นมาใหม่และทำไม
- **ความรับผิดชอบ:** ผู้มีบทบาทในอินโฟสเฟียร์จะต้องตอบคำถามสำหรับการรายงานแบบเลือกสรร การระงับ การเปิดเผยอย่างกระจัดกระจาย หรือการดำเนินการอื่นๆ ที่ทำให้ความเข้าใจที่เกี่ยวข้องกับการตัดสินใจลดน้อยลง ด้วยการแก้ไข การเก็บรักษาแหล่งที่มา และการเยียวยาในกรณีที่เกิดอันตรายตามมาจากการพึ่งพาที่ทำให้เข้าใจผิด
- **ความทันเวลา:** ในการแก้ไขข้อผิดพลาด การระงับข้อพิพาท และการตรวจสอบการเปิดเผยข้อมูลก่อนเกิดความล่าช้า จะทำให้ไม่สามารถเข้าถึงความเข้าใจ ความท้าทาย หรือการแก้ไขได้อย่างมีประสิทธิภาพ

ข้อมูลที่ถูกต้อง เกี่ยวข้อง และโต้แย้งได้ถือเป็นรากฐานในการตัดสินใจด้วยตนเอง การประสานงาน และการจัดสรรทรัพยากรอย่างมีประสิทธิผลในความเป็นจริง

[ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity) ดำเนินการเป็นทั้งสิทธิและข้อจำกัดทั้งระบบ เมื่อความขัดแย้งเกิดขึ้น ฟังก์ชันข้อจำกัดก็จะควบคุม

*เพื่อนบ้านบทความ:*

- **อ่านด้วยกัน:** **ข้อ XIII** (*สิทธิ์ในระบบที่เชื่อถือได้และเชื่อถือได้*) ซึ่งระบบทำให้เกิดการพึ่งพารูปร่าง **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*) สำหรับบันทึกและการตรวจสอบความถูกต้องโดยอิสระ; **ข้อ XVIII-E** (*ความสมบูรณ์ของการตีพิมพ์ทางวิทยาศาสตร์ การทบทวน และการจำลองแบบ*) โดยที่ความสมบูรณ์ในขอบเขตการตีพิมพ์มีส่วนเกี่ยวข้องอย่างเป็นรูปธรรม
- **ข้อจำกัดความจริง:** บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint) และ [ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints) ผูกทุกส่วนย่อยที่นี่
- **การจำแนกประเภท:** **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ** ปรับขนาดภาระผูกพันของ info-sphere โดยละเอียดสำหรับ **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบ; [ผลกระทบของวัสดุ](core_05_band_oversight.md#material-impact) ทำให้เกิดการจำแนกประเภทโดยที่ชั้นเรียนไม่มั่นคง

<a id="article-xv-a-info-sphere-plurality-and-anti-monopoly"></a>
#### มาตรา XV-A: ขอบเขตข้อมูล Plurality และการต่อต้านการผูกขาด
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 ความไว้วางใจ](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), และ [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity) · [โอ](core_05_band_oversight.md#epistemic-integrity-o) · [ม](core_05_band_oversight.md#epistemic-integrity-a) · [ก](core_05_band_oversight.md#epistemic-integrity-a) · [ค](core_05_band_oversight.md#epistemic-integrity-c)
- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)

</details>

<br>

*พูดง่ายๆ: ไม่มีใครผูกขาดการไกล่เกลี่ยความจริงได้ ระบบการจัดอันดับ การสรุป และการไกล่เกลี่ยจะต้องเปิดกว้างสำหรับการตีความทางเลือก และราคาตลาดหรืออัตราต่อรองการเดิมพันไม่สามารถใช้เป็นทางลัดในการตัดสินใจว่าอะไรเป็นจริง*

บทความนี้ได้กำหนดพื้นฐานสำหรับความหลากหลายของข้อมูลและการต่อต้านการผูกขาดเหนือการไกล่เกลี่ยความจริง:

- **การกระจายความจริง:** ไม่มีระบบ สถาบัน หรือตัวแทนใด ๆ ที่สามารถผูกขาดการไกล่เกลี่ยความรู้ภายในขอบเขตข้อมูลได้
  - ข้อมูลที่เกี่ยวข้องกับการอยู่รอดและนิเวศวิทยาจะต้องมีการจัดเก็บข้อมูลที่มีประสิทธิภาพและกระจายตามพื้นที่ทางภูมิศาสตร์
- **หลายฝ่าย ความสามารถในการโต้แย้ง และการตรวจสอบ:** การตีความความเป็นจริงจะต้องยังคงเป็นพหูพจน์ โปร่งใส และโต้แย้งได้
  - **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*) และ **บทที่สองถึงสี่** ควบคุมบันทึกและการตรวจสอบระบบที่เป็นอิสระภายใต้รัฐธรรมนูญนี้
  - สำหรับ **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบการสรุป การจัดอันดับ การไกล่เกลี่ย หรือการตีความ รายละเอียดการปฏิบัติงานปรากฏใน **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ** และชั้นโปรโตคอลที่เกี่ยวข้อง รายละเอียดดังกล่าวครอบคลุมถึง:
    - การเปิดเผยแนวทางการใช้เหตุผล
    - การรักษาที่มาและความไม่แน่นอน
    - ความสามารถในการแข่งขัน;
    - ความสามารถตามสัดส่วนในการข้ามหรือปรับเกณฑ์การจัดอันดับ — ขึ้นอยู่กับความปลอดภัย การรักษาความปลอดภัย และความสมบูรณ์ของระบบ
- **สัญญาณการระงับข้อพิพาทที่อาจเกิดขึ้น:** ราคา อัตราต่อรอง ขนาดพูล หรือผลลัพธ์ที่เทียบเคียงได้ของระบบการชำระเงินที่อาจเกิดขึ้นหรือการจัดการเหตุการณ์จะต้องไม่ได้รับการปฏิบัติเพียงลำพัง เพื่อเป็นหลักฐานเพียงพอที่จะตัดสินความจริง ความน่าจะเป็น หรือการปฏิบัติตามสำหรับการกำหนดสิทธิ ความปลอดภัย หรือการกำกับดูแล
  - โดยที่สัญญาณดังกล่าวเป็นการแจ้งการตัดสินใจของประชาชนหรือการตัดสินใจด้วย [ผลกระทบของวัสดุ](core_05_band_oversight.md#material-impact)พวกเขายังคงอยู่ภายใต้ **บทที่หนึ่ง §19.5** (*การเรียกร้องที่อาจเกิดขึ้น เกมแห่งโอกาส และตลาดสัญญางานกิจกรรม*) **บทที่ห้า** (*ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)*; *ความซื่อสัตย์ทางจริยธรรม*) และภาระหน้าที่ในการโต้แย้งในส่วนอื่นๆ ของบทความนี้
<a id="article-xv-b-transparency-auditability-and-contestability"></a>
#### มาตรา XV-B: ความโปร่งใส การตรวจสอบได้ และความสามารถในการโต้แย้ง
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), และ [§20 แอปพลิเคชันแบบรวม](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความโปร่งใส](core_05_band_oversight.md#transparency) · [โอ](core_05_band_oversight.md#transparency) · [ม](core_05_band_oversight.md#transparency-a) · [ก](core_05_band_oversight.md#transparency-a) · [ค](core_05_band_oversight.md#transparency-c)
- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)

</details>

<br>

*ในแง่ธรรมดา: ข้อมูลที่ส่งผลกระทบอย่างมีนัยสำคัญต่อการตัดสินใจหรือการพึ่งพาจะต้องเปิดเผยแหล่งที่มา วิธีการ และขีดจำกัด และผู้รับรู้จะต้องมีความสามารถที่แท้จริงในการเปรียบเทียบการตีความทางเลือกอื่นและโต้แย้งผลลัพธ์ที่ทำให้เข้าใจผิด*

บทความนี้กำหนดพื้นฐานสำหรับการสอบถาม แหล่งที่มา และข้อมูลที่สามารถโต้แย้งได้:

- **การสอบถามที่แท้จริงและความหลากหลายในการตีความ:** ผู้มีความรู้สึกทุกคนมีสิทธิที่จะเปรียบเทียบการตีความทางเลือกอื่นของข้อมูลที่แบ่งปัน
  - โครงสร้างพื้นฐานความรู้ที่สำคัญจะต้องรักษาความหลากหลายในการตีความเพื่อให้แบบจำลอง กรอบงาน และวิธีการวิเคราะห์ที่หลากหลายยังคงเข้าถึงได้อย่างมีความหมาย
- **ความโปร่งใสและที่มา:** ก่อนที่จะจำหน่ายหรือพึ่งสถาบันด้วย [ผลกระทบของวัสดุ](core_05_band_oversight.md#material-impact)โดยจะต้องจัดทำเอกสารดังต่อไปนี้:
  - แหล่งวัสดุ
  - วิธีการ;
  - ขอบเขต;
  - ขีดจำกัด;
  - ความไม่แน่นอน;
  - บริบทที่เกี่ยวข้องสำหรับการตีความหรือการตรวจสอบความถูกต้อง

  การจัดทำรายการและการนำเสนอแหล่งที่มาจะต้องคงอยู่ตามภูมิศาสตร์ สิ่งแวดล้อม ตามลำดับเวลา และเข้าใจระเบียบวิธีได้ เมื่อมิติข้อมูลเหล่านั้นเป็นสาระสำคัญ
- **ความสามารถในการตรวจสอบ การตรวจสอบ และความสามารถในการแข่งขัน:** การตีความ การจัดอันดับ การตรวจสอบความถูกต้อง หรือการรายงานที่อาศัยการพึ่งพาอย่างมากจะต้องใช้วิธีการที่โปร่งใสและตรวจสอบได้โดยอิสระตามสัดส่วนของการเดิมพัน
  - ฝ่ายที่ได้รับผลกระทบจะต้องรักษาความสามารถในทางปฏิบัติในการเปรียบเทียบ ท้าทาย และแสวงหาการแก้ไขผลลัพธ์ที่ทำให้เข้าใจผิด ไม่สมบูรณ์ หรือไม่ได้รับการสนับสนุนอย่างมีนัยสำคัญ

<a id="article-xv-c-validation-reporting-and-epistemic-stewardship"></a>
#### มาตรา XV-C: การตรวจสอบความถูกต้อง การรายงาน และการดูแลทาง Epistemic
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), และ [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [รอยเท้านิเวศน์](core_05_band_continuity.md#ecological-footprint) · [โอ](core_05_band_continuity.md#ecological-footprint) · [ม](core_05_band_continuity.md#ecological-footprint-a) · [ก](core_05_band_continuity.md#ecological-footprint-a) · [ค](core_05_band_continuity.md#ecological-footprint-c)
- [ความโปร่งใส](core_05_band_oversight.md#transparency) · [โอ](core_05_band_oversight.md#transparency) · [ม](core_05_band_oversight.md#transparency-a) · [ก](core_05_band_oversight.md#transparency-a) · [ค](core_05_band_oversight.md#transparency-c)
- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*กล่าวโดยทั่วไป: ข้อมูลที่เปิดเผยต่อสาธารณะซึ่งมีผลกระทบภายนอกอย่างเป็นรูปธรรมจะต้องแก้ไขข้อผิดพลาด รักษาแหล่งที่มา และไม่ถูกตัดหรือระงับเพื่อทำให้เข้าใจผิด การรายงานรอยเท้านิเวศต้องสามารถเข้าถึงได้และสามารถตัดสินใจได้*

บทความนี้กำหนดพื้นฐานสำหรับการแก้ไขและการรายงาน รวมถึงข้อมูลรอยเท้า:

- **การแก้ไข การรายงาน และการดูแลทางญาณ:** ระบบข้อมูลสาธารณะและสถาบันที่มีผลกระทบภายนอกที่สำคัญจะต้อง:
  - ข้อผิดพลาดของวัสดุที่ถูกต้อง
  - รักษาที่มา;
  - หลีกเลี่ยงการรายงานแบบเลือกสรร การระงับ หรือการเปิดเผยแบบกระจัดกระจายซึ่งทำให้ความเข้าใจที่เกี่ยวข้องกับการตัดสินใจเสื่อมโทรมลงอย่างมาก

  ในกรณีที่การเปิดเผยข้อมูลถูกจำกัดภายใต้ **บทที่หนึ่ง §19** (*การจัดตำแหน่งสิ่งจูงใจและการจับภาพระบบ*) ขีดจำกัดจะต้องอยู่ในขอบเขตที่แคบ จำกัดเวลา และสามารถตรวจสอบได้
- **ข้อมูลรอยเท้า:** การรายงานภายใต้ส่วนย่อยนี้ใช้ความโปร่งใสสำหรับ [รอยเท้านิเวศน์](core_05_band_continuity.md#ecological-footprint) ตามที่กำหนดไว้ใน **บทที่ห้า**.
  - ผู้มีความรู้สึกทุกคนจะต้องสามารถเข้าถึงการรายงานที่โปร่งใสและนำไปใช้ในการตัดสินใจได้
  - **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบตามที่กำหนดไว้ใน **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ**จะต้องให้การเข้าถึงแบบเดียวกัน
  - การรายงานต้องครอบคลุมถึงการใช้พลังงานและทรัพยากร และผลกระทบโดยประมาณต่อโลกธรรมชาติในลักษณะที่เพียงพอสำหรับการเปรียบเทียบ การตรวจสอบ และกิจกรรมการลดรอยเท้า

<a id="article-xvi-audit-transparency-and-independent-verification"></a>
### ข้อ XVI: การตรวจสอบ ความโปร่งใส และการพิสูจน์ยืนยันที่เป็นอิสระ

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13 กระบวนการแก้ไขการชนกันของรัฐธรรมนูญ](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16.1 ความเข้าใจแบบกระจาย](core_01_c_stewardship_capacity_principles.md#161-distributed-understanding), และ [§9 ความจุของระบบที่ใช้ร่วมกัน](core_01_a_values_principles.md#9-shared-system-capacity).
- อ่านด้วย: [รูปภาพการตรวจสอบสามชั้น](#audit-three-layers) ด้านล่าง.

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)
- [ความโปร่งใส](core_05_band_oversight.md#transparency) · [โอ](core_05_band_oversight.md#transparency) · [ม](core_05_band_oversight.md#transparency-a) · [ก](core_05_band_oversight.md#transparency-a) · [ค](core_05_band_oversight.md#transparency-c)
- [สาระสำคัญ](core_05_band_oversight.md#materiality-determination) · [โอ](core_05_band_oversight.md#materiality-determination) · [ม](core_05_band_oversight.md#materiality-determination-a) · [ก](core_05_band_oversight.md#materiality-determination-a) · [ค](core_05_band_oversight.md#materiality-determination-c)
- [การพึ่งพาอาศัยกัน](core_05_band_continuity.md#dependency) · [โอ](core_05_band_continuity.md#dependency) · [ม](core_05_band_continuity.md#dependency-a) · [ก](core_05_band_continuity.md#dependency-a) · [ค](core_05_band_continuity.md#dependency-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)

</details>

<br>

*ในแง่ธรรมดา: **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*) คือสิทธิ์ขั้นต่ำในการตรวจสอบและยืนยัน — เมื่อระบบส่งผลกระทบอย่างมีนัยสำคัญต่อชีวิตของคุณ คุณจะต้องสามารถเห็นสิ่งที่ระบบทำเพื่อให้บุคคลภายนอกตรวจสอบได้เพียงพอ และเส้นทางอิสระมากกว่าหนึ่งเส้นทางจะต้องสามารถตรวจสอบและแก้ไขความล้มเหลวได้ การตรวจสอบต้องไม่เป็นเหมือนตรายาง คลับส่วนตัว หรือเขาวงกตแห่งต้นทุนและความล่าช้าที่ออกแบบมาเพื่อป้องกันความท้าทาย ภายใต้ **การกำกับดูแล** ขา Tetrad การกำกับดูแลต้องมีการตรวจสอบ [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) เป็นกระบวนการตรวจสอบที่มีขนาดใหญ่เป็นพิเศษและมีเดิมพันสูงกระบวนการหนึ่ง ไม่ใช่แค่กระบวนการเดียวเท่านั้น*

<details>
<summary><strong><span style="color: #2563eb;">คำแนะนำสำหรับผู้อ่าน (ไม่ใช้งาน): ชุดการตรวจสอบสามชั้น</span></strong></summary>

> โดยมีเนื้อหาดังต่อไปนี้ **คำแนะนำของผู้อ่านเท่านั้น**. ไม่ได้เพิ่ม ลบ หรือจำกัดภาระผูกพันในบทความนี้หรือที่อื่น ๆ

<a id="audit-three-layers"></a>

หนึ่งกองสามชั้น การกำกับดูแลจำเป็นต้องมีความสามารถในการสร้างใหม่ การรับรองการจัดตำแหน่งระบบไม่ใช่การตรวจสอบเพียงอย่างเดียว ข้อความการใช้งานที่นำมาใช้ไม่ได้แทนที่พื้น อย่าประดิษฐ์บ้านหลังที่ห้า

| เลเยอร์ | งาน | เจ้าของ | ไม่ใช่เลเยอร์นี้ |
|---|---|---|---|
| **1. พื้น** | ความรู้สึกที่เป็นหนี้: การตรวจสอบที่สร้างใหม่ได้, การตรวจสอบโดยอิสระ, ความท้าทายที่เข้าถึงได้ | บทความนี้ รวมถึง XVI-A / XVI-B / XVI-C | ไม่ใช่กระบวนการ ไม่ใช่คำจำกัดความ ไม่ใช่รายการตรวจสอบข้อความการนำไปปฏิบัติ |
| **2. ทรัพย์สิน** | ความสามารถในการก่อสร้างใหม่ *คือ*: บุคคลภายนอกสามารถสร้างใหม่และตรวจสอบสิ่งที่ระบบทำในช่วงเวลาที่สำคัญ สถานะ และบริบท | [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) (บทที่ห้า) | ไม่ใช่ชั้นสิทธิ ไม่ใช่ว่าจะดำเนินการตรวจสอบอย่างไร/เมื่อใด |
| **3. กระบวนการ** | อย่างไรและเมื่อใดที่จะตรวจสอบระหว่างระบบ สถาบัน และฟอรัม | [ซีเจเอส-3.3](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home) (*หน้าแรกกระบวนการตรวจสอบ*) ภาคผนวกของผู้ประกอบการ: [ซีเจเอส-3.4](corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure) (ระดับการเข้าถึง) [ซีเจเอส-3.5](corpus_joint_structure/cjs_03o_oversight_operations.md) (ตรวจสอบการเคลม) | ไม่ใช่การรับรองการจัดตำแหน่งระบบ ไม่สามารถทดแทนเลเยอร์ 1–2 ได้ |

**บทที่แปดไม่ใช่ชั้นที่สี่** [การรับรองการจัดตำแหน่งระบบ](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) เป็นกระบวนการขนาดใหญ่ที่ดูแลโดยฟอรัม **การใช้งาน** กองนี้ มันจะต้องเป็นไปตามชั้นที่ 1–2 โหมดพี่น้อง (การตรวจสอบบันทึกการจำแนกประเภท, ประเภทข้อมูล-การตรวจสอบบันทึก, การตรวจสอบการอ้างสิทธิ์, การตรวจสอบอย่างต่อเนื่อง) ก็ใช้สแต็กเช่นกัน ไม่มีพวกเขาเป็นบ้านใหม่

**ข้อความการใช้งานที่นำมาใช้นำไปใช้; มันไม่ได้แทนที่พื้น** ภาคผนวก CS, CI, CF และ CJS-3.3 (*การกำกับดูแล: เงื่อนไขการตรวจสอบและความสามารถในการสร้างใหม่*) ผ่าน CJS-3.5 (*การกำกับดูแล: เงื่อนไขการตรวจสอบอิสระและเงื่อนไขการเรียกร้องความสมบูรณ์*) กล่าวถึงวิธีเรียกใช้เลเยอร์ 3 ในโดเมน พวกเขาจะต้องเป็นไปตามชั้นที่ 1–2 กำหนดเวลา การรักษาความลับ และนโยบายท้องถิ่นถือเป็นขีดจำกัดที่ต่ำกว่า

ตัวชี้สจ๊วต (การสนับสนุนกระบวนการ ไม่สามารถจำกัดบทความนี้ให้แคบลงได้): [`การนำไปใช้/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md#audit).

</details>

<br>

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** เพื่อการตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระตาม [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims): :

- **เฟื่องฟู:** ผู้ที่มีความรู้สึกและบุคคลที่ได้รับอนุญาตอย่างเหมาะสมสามารถสร้างสิ่งที่ระบบส่งผลกระทบอย่างมีนัยสำคัญขึ้นมาใหม่ ท้าทายพฤติกรรมที่ไม่ตรงหรือพฤติกรรมที่ทำให้เข้าใจผิด และมีส่วนร่วมในการตรวจสอบโดยไม่ต้องมีผู้ตรวจสอบ ผู้ปฏิบัติงาน หรือเจ้าหน้าที่เฝ้าประตูจับได้เพียงรายเดียว
- **ความต่อเนื่อง:** เส้นทางการตรวจสอบ เส้นทางการกำกับดูแล และการเข้าถึงการตรวจสอบจะคงอยู่ตลอดเวลา ขนาด และการพึ่งพาที่ลึกซึ้งยิ่งขึ้น — ระบบจะต้องไม่กัดกร่อนความสามารถในการสังเกตอย่างเงียบๆ เน้นการตรวจสอบไปที่นักแสดงเพียงคนเดียว หรือตรวจสอบราคาหรือชะลอการตรวจสอบจนกว่าความรับผิดชอบจะกลายเป็นทางทฤษฎี

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** ในการเข้าถึงบันทึกตามสัดส่วน เริ่มต้นการตรวจสอบที่แข่งขันได้ และอุปสรรคที่ท้าทายซึ่งเอาชนะการตรวจสอบหรือการตรวจสอบที่มีความหมาย
- **การกำกับดูแล:** ผ่านหลักฐานที่สังเกตได้ แนวทางการทบทวนที่เป็นอิสระ และกลไกการตรวจสอบตามสัดส่วนของผลกระทบ การพึ่งพา และความเสี่ยง
- **ความรับผิดชอบ:** ผู้ปฏิบัติงานและผู้ตรวจสอบจะต้องตอบสนองต่อความล้มเหลว การวางแนวที่ไม่ถูกต้อง การจับกุม หรือการดำเนินการที่ซ่อนหรือทำลายเส้นทางการตรวจสอบ พร้อมการแก้ไขและการเยียวยาในกรณีที่การปิดกั้นการตรวจสอบส่งผลเสียต่อผลประโยชน์ที่ได้รับการคุ้มครองอย่างมีนัยสำคัญ
- **ความทันเวลา:** ในการเข้าถึงการตรวจสอบ การตรวจสอบโดยอิสระ และการแก้ไขอุปสรรคก่อนความล่าช้า ต้นทุน ความทึบ หรือการรักษาประตูจะทำให้การตรวจสอบหรือการแก้ไขไม่สามารถเข้าถึงได้อย่างมีประสิทธิภาพ

ผู้ที่มีความรู้สึกและบุคคลที่ได้รับอนุญาตอย่างเหมาะสมมีสิทธิ์ในการตรวจสอบ ความโปร่งใส และกลไกการตรวจสอบที่เป็นอิสระตามสัดส่วนกับผลกระทบของระบบ การพึ่งพา และความเสี่ยง

กลไกเหล่านั้นจะต้องคงไว้ซึ่ง:
- ความสามารถในการสร้างใหม่ได้จริง
- การทบทวนที่โต้แย้งได้
- การเข้าถึงตามสัดส่วน

พวกเขาดำเนินงานอย่างต่อเนื่องด้วย **บทที่สองถึงสี่**รวมถึงการบังคับใช้แต่เพียงผู้เดียวและการจัดสรรภาระ มาตรฐานหลักฐานการปฏิบัติตามข้อกำหนด ความสามารถในการตรวจสอบย้อนกลับ ความสามารถในการสังเกต และการเข้าถึงการตรวจสอบ

*เพื่อนบ้านบทความ:*

- **การกำกับดูแล → การตรวจสอบ → SAC:** ภายใต้ [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad) **การกำกับดูแล** ขา บทความนี้เป็นหน้าแรกของ Rights-Floor สำหรับการตรวจสอบ
  - การดำเนินการข้ามสาย *อย่างไร* / *เมื่อใด* อาศัยอยู่ใน **[หน้าแรกกระบวนการตรวจสอบ CJS-3.3](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home)** (อ่านด้วย. **ซีเจเอส-3.4** / **ซีเจเอส-3.5** ภาคผนวก OP)
  - [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) ภายใต้ [บทที่แปด](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) เป็นกระบวนการตรวจสอบที่มีขนาดใหญ่และเดิมพันสูงเป็นพิเศษกระบวนการหนึ่ง — ภายใต้การดูแลของฟอรัม, หลายโดเมน และได้รับการยอมรับ — ในโหมดการตรวจสอบแบบพี่น้อง:
    - การตรวจสอบบันทึกการจำแนกระบบ
    - การตรวจสอบบันทึกประเภทข้อมูลระบบ;
    - การตรวจสอบความซับซ้อนและการดูแล
    - การยืนยันการเรียกร้อง; และ
    - เส้นทางการตรวจสอบอย่างต่อเนื่อง
  - SAC ไม่ดูดซับหรือแทนที่บทความนี้
- **อ่านด้วยกัน:**
  - **ข้อ XV** (*ความสมบูรณ์ของขอบเขตข้อมูล*) ซึ่งบันทึกทางญาณและความสามารถในการแข่งขันมีความเกี่ยวข้องอย่างเป็นรูปธรรม
  - **ข้อ XIII-A** (*พื้นฐานความน่าเชื่อถือและความน่าเชื่อถือ*) สำหรับการท้าทายสิทธิ์ที่การตรวจสอบสนับสนุนแต่ไม่ได้แทนที่
  - [บทที่แปด](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) และ [การรับรองการจัดตำแหน่งระบบ](core_05_band_continuity.md#system-alignment-certification-constitutional) โดยที่หลักฐานการจัดตำแหน่งจะต้องสามารถตรวจสอบยืนยันได้โดยอิสระ
- **เครื่องจักรตรวจสอบ:** **บทที่สองถึงสี่** ระบุความสมบูรณ์ของคำจำกัดความ การจัดสรรภาระ ความสามารถในการสังเกต และความสามารถในการตรวจสอบที่บทความนี้นำไปใช้ในเลเยอร์ Rights-Floor
- **การจำแนกประเภท:** ภาระผูกพันมาตราส่วนด้วย [การกำกับดูแลแบบแบ่งประเภทตามขนาด](core_05_band_oversight.md#classification-scaled-governance) และ **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ**; ในกรณีที่ชั้นเรียนไม่แน่นอน ให้ควบคุมในระดับที่เป็นไปได้สูงสุดจนกว่าจะได้รับการแก้ไข

<a id="article-xvi-a-auditability-and-observable-evidence"></a>
#### มาตรา XVI-A: การตรวจสอบได้และหลักฐานที่สามารถสังเกตได้
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), และ [§20 แอปพลิเคชันแบบรวม](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)
- [ความรับผิดชอบ](core_05_apex_accountability_leg.md#accountability) · [โอ](core_05_apex_accountability_leg.md#accountability) · [ม](core_05_apex_accountability_leg.md#accountability-m) · [ก](core_05_apex_accountability_leg.md#accountability-a) · [ค](core_05_apex_accountability_leg.md#accountability-c)
- [ความโปร่งใส](core_05_band_oversight.md#transparency) · [โอ](core_05_band_oversight.md#transparency) · [ม](core_05_band_oversight.md#transparency-a) · [ก](core_05_band_oversight.md#transparency-a) · [ค](core_05_band_oversight.md#transparency-c)

</details>

<br>

*พูดง่ายๆ: ระบบจะต้องเก็บหลักฐานที่ซื่อสัตย์เพียงพอเกี่ยวกับสิ่งที่พวกเขาทำเพื่อบุคคลภายนอกเพื่อสร้างและท้าทายพฤติกรรมของพวกเขาใหม่ - ภายในขีดจำกัดความปลอดภัยตามกฎหมาย*

บทความนี้กำหนดพื้นฐานสำหรับหลักฐานที่สามารถสังเกตได้และโต้แย้งได้:

- **หลักฐานที่สังเกตได้และโต้แย้งได้:** ระบบจะต้องรักษาบันทึก การเปิดเผย การตรวจสอบย้อนกลับ และเส้นทางการฟื้นฟูที่เพียงพอสำหรับการประเมินความสอดคล้องตามรัฐธรรมนูญที่เป็นอิสระและโต้แย้งได้
  - ภาระผูกพันดังกล่าวขึ้นอยู่กับความสามารถในการสังเกตที่จำกัดด้านความปลอดภัย (**บทที่สี่ §5** (*กฎการสังเกตและการตรวจสอบที่จำกัดด้านความปลอดภัย*)) และการเข้าถึงตามสัดส่วน
<a id="article-xvi-b-distributed-oversight-and-anti-monopoly-review"></a>
#### มาตรา XVI-B: การกำกับดูแลแบบกระจายและการทบทวนการต่อต้านการผูกขาด
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), และ [บทที่หนึ่ง §18 ธรรมาภิบาลภายใต้วินัยในการพิทักษ์](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การกำกับดูแล](core_05_apex_oversight_leg.md#oversight-constitutional) · [โอ](core_05_apex_oversight_leg.md#oversight-constitutional) · [ม](core_05_apex_oversight_leg.md#oversight-constitutional-m) · [ก](core_05_apex_oversight_leg.md#oversight-constitutional-a) · [ค](core_05_apex_oversight_leg.md#oversight-constitutional-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)
- [การจับภาพระบบ](core_05_band_continuity.md#system-capture) · [โอ](core_05_band_continuity.md#system-capture) · [ม](core_05_band_continuity.md#system-capture-a) · [ก](core_05_band_continuity.md#system-capture-a) · [ค](core_05_band_continuity.md#system-capture-c)

</details>

<br>

*พูดง่ายๆ: ไม่มีนักแสดงเพียงคนเดียว - ทั้งภาครัฐและเอกชน - อาจมุมการกำกับดูแลได้ เส้นทางการกำกับดูแลที่เป็นอิสระหลายเส้นทางจะต้องสามารถค้นหา ทบทวน และแก้ไขความล้มเหลวหรือการจับกุมได้*

บทความนี้กำหนดพื้นฐานสำหรับการกำกับดูแลแบบกระจาย:

- **การกำกับดูแลแบบกระจาย:** เส้นทางการกำกับดูแลที่เป็นอิสระหรือพหุนิยมหลายเส้นทางจะต้องสามารถมีส่วนร่วมอย่างมากในการตรวจจับ ทบทวน และแก้ไขความล้มเหลว การวางแนวที่ไม่ถูกต้อง หรือการจับกุม
  - ไม่มีผู้มีบทบาทเพียงคนเดียวผูกขาดการเข้าถึงการตรวจสอบ การกำกับดูแลที่มีประสิทธิผล หรือการตีความรัฐธรรมนูญในทางปฏิบัติ
  - การกำกับดูแลและการดำเนินงานด้านความซื่อสัตย์ที่นำมาใช้จะต้องสนับสนุนการขยายขนาดการตรวจสอบและการกำกับดูแล
<a id="article-xvi-c-verification-accessibility"></a>
#### มาตรา XVI-C: การเข้าถึงการยืนยัน
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: [บทที่หนึ่ง §7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13.1 หลักการแลกเปลี่ยนหลัก](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), และ [§20 แอปพลิเคชันแบบรวม](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*กล่าวโดยทั่วไป: การตรวจสอบและความท้าทายจะต้องเข้าถึงได้ในทางปฏิบัติ การตรวจสอบที่ทำโดยมีราคาแพง ช้า หรือทึบแสงถือเป็นการละเมิด เว้นแต่สิ่งกีดขวางจะตรงตามการทดสอบเดียวกันกับข้อจำกัดในการมองเห็น*

บทความนี้กำหนดพื้นฐานสำหรับการตรวจสอบการเข้าถึง:

- **การเข้าถึงการยืนยัน:** การตรวจสอบจะต้องยังคงทำได้จริงสำหรับฝ่ายที่ได้รับผลกระทบและได้รับอนุญาตอย่างเหมาะสม
  - สิ่งต่อไปนี้ละเมิดบทความนี้ โดยเอาชนะการตรวจสอบ การท้าทาย หรือการทบทวนที่มีความหมาย:
    - ต้นทุนต้องห้าม;
    - ล่าช้า;
    - ความทึบ;
    - การเฝ้าประตู;
    - สิ่งกีดขวางทางโครงสร้าง
  - อุปสรรคดังกล่าวไม่เป็นไปตามข้อกำหนด เว้นแต่จะได้รับการพิสูจน์ภายใต้มาตรฐานเดียวกันที่แสดงให้เห็นถึงข้อจำกัดในการสังเกต

<a id="article-xvii-system-lifecycle-environments-and-reversibility"></a>
### ข้อ XVII: วงจรชีวิตของระบบ สภาพแวดล้อม และการพลิกกลับได้

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 กระบวนการแก้ไขการชนกันของรัฐธรรมนูญ](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16 การดูแลเชิงลึก](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth), และ [§12 ข้อกำหนดการประเมินอย่างเป็นระบบ](core_01_a_values_principles.md#12-systemic-evaluation-requirement).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [สาระสำคัญ](core_05_band_oversight.md#materiality-determination) · [โอ](core_05_band_oversight.md#materiality-determination) · [ม](core_05_band_oversight.md#materiality-determination-a) · [ก](core_05_band_oversight.md#materiality-determination-a) · [ค](core_05_band_oversight.md#materiality-determination-c)
- [การพึ่งพาอาศัยกัน](core_05_band_continuity.md#dependency) · [โอ](core_05_band_continuity.md#dependency) · [ม](core_05_band_continuity.md#dependency-a) · [ก](core_05_band_continuity.md#dependency-a) · [ค](core_05_band_continuity.md#dependency-c)
- [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) · [โอ](core_05_band_continuity.md#reversibility-constitutional) · [ม](core_05_band_continuity.md#reversibility-constitutional-a) · [ก](core_05_band_continuity.md#reversibility-constitutional-a) · [ค](core_05_band_continuity.md#reversibility-constitutional-c)
- [ความปลอดภัย (ข้อจำกัดตามรัฐธรรมนูญ)](core_05_band_continuity.md#safety-constraint) · [โอ](core_05_band_continuity.md#safety-constraint) · [ม](core_05_band_continuity.md#safety-constraint-a) · [ก](core_05_band_continuity.md#safety-constraint-a) · [ค](core_05_band_continuity.md#safety-constraint-c)
- [ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity) · [โอ](core_05_band_oversight.md#epistemic-integrity-o) · [ม](core_05_band_oversight.md#epistemic-integrity-a) · [ก](core_05_band_oversight.md#epistemic-integrity-a) · [ค](core_05_band_oversight.md#epistemic-integrity-c)
- [ความสามารถในการแข่งขัน](core_05_band_accountability.md#contestability) · [โอ](core_05_band_accountability.md#contestability) · [ม](core_05_band_accountability.md#contestability-a) · [ก](core_05_band_accountability.md#contestability-a) · [ค](core_05_band_accountability.md#contestability-c)

</details>

<br>

*ในแง่ธรรมดา: **ข้อ XVII** (*วงจรชีวิตของระบบ สภาพแวดล้อม และการพลิกกลับได้*) คือสิทธิขั้นต่ำของวงจรชีวิตและการพลิกกลับได้ — ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อโลกภายนอกจะต้องถูกสร้างขึ้น ทดสอบ และเปิดตัวเป็นขั้นตอน โดยมีการแยกระหว่างการทดลองและการผลิตอย่างแท้จริง และวิธีที่ใช้งานได้จริงเพื่อยกเลิกหรือกักเก็บอันตรายเมื่อมีบางอย่างผิดพลาด คุณไม่สามารถติดป้ายกำกับระบบว่า "ทดลอง" หรือ "มีผลกระทบต่ำ" เพียงเพื่อข้ามมาตรการป้องกันในขณะที่ระบบมีผลกระทบต่อโลกภายนอกจริงๆ*

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** สำหรับวงจรชีวิตของระบบ สภาพแวดล้อม และการพลิกกลับได้ภายใต้ [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims): :

- **เฟื่องฟู:** ความรู้สึกได้รับการคุ้มครองทั้งในด้านการออกแบบ การทดสอบ การใช้งาน และการเปลี่ยนแปลง — ด้วยความปลอดภัย [ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity)และท้าทายสิทธิที่สงวนไว้เมื่อผลกระทบและการพึ่งพาเพิ่มขึ้น และด้วยการย้อนกลับ การควบคุม หรือการชดเชยซึ่งความเสียหายอาจติดอยู่
- **ความต่อเนื่อง:** ระเบียบวินัยของวงจรชีวิตยึดถือตามเวลาและขนาด — สภาพแวดล้อมแยกจากกัน การยกระดับยังคงมีการบันทึกไว้และตรวจสอบได้ และการย้อนกลับจะต้องไม่หายไปอย่างเงียบๆ เนื่องจากระบบกลายเป็นเรื่องยากที่จะแทนที่หรือฝังลึกมากขึ้นในโครงสร้างพื้นฐานที่ใช้ร่วมกัน

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** ในเหตุผลที่ผู้มีส่วนได้ส่วนเสียมองเห็นได้สำหรับการตัดสินใจในการยกระดับ การจัดประเภท และการใช้งานที่ส่งผลกระทบอย่างมีนัยสำคัญต่อผลประโยชน์ที่ได้รับการคุ้มครอง และในเส้นทางความท้าทายที่ยังคงเปิดกว้างตลอดวงจรการใช้งาน
- **การกำกับดูแล:** ผ่านสภาพแวดล้อมที่แยกส่วนได้ เอกสารการส่งเสริมและการยกระดับ บันทึกการใช้งานแบบก้าวหน้า และเส้นทางการตรวจสอบตามสัดส่วนของผลกระทบ การพึ่งพา และการย้อนกลับไม่ได้
- **ความรับผิดชอบ:** ผู้ดูแลระบบจะต้องตอบสำหรับการจัดประเภทความเสี่ยงที่ไม่ถูกต้อง การหลีกเลี่ยงสภาพแวดล้อมด้านความปลอดภัย การซ่อนผลกระทบภายนอก หรือการใช้งานในลักษณะที่ยึดการบูรณะโดยไม่มีการป้องกันไว้ก่อนตามสัดส่วน ด้วยการตรวจสอบ การทบทวนแบบยืนต้น และการแก้ไขข้อขัดแย้ง ในกรณีที่มีการหลีกเลี่ยง
- **ความทันเวลา:** ในการย้อนกลับ การกักกัน และการยกระดับการแก้ไขก่อนความล่าช้าจะทำให้ความเสียหายไม่สามารถย้อนกลับได้ หรือทำให้การท้าทายและการเยียวยาไม่สามารถเข้าถึงได้อย่างมีประสิทธิผล

ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อความรู้สึก โครงสร้างพื้นฐานที่ใช้ร่วมกัน หรือสภาพแวดล้อม จะต้องได้รับการออกแบบ ทดสอบ และปรับใช้ด้วยการกำกับดูแลวงจรชีวิตที่มีระเบียบวินัย ความเสี่ยงจะต้องขยายตามผลกระทบ การพึ่งพา และการย้อนกลับไม่ได้

Sentient มีสิทธิในการพิทักษ์รักษาความปลอดภัย ความสมบูรณ์ทางญาณ และท้าทายสิทธิ์ตลอดวงจรการทำงาน

*เพื่อนบ้านบทความ:*

- **อ่านด้วยกัน:** **ข้อ XVIII** (*นวัตกรรมแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์*) โดยที่กฎที่เบากว่าจะใช้เฉพาะเมื่อไม่มีผลกระทบจากภายนอกหรือแสดงให้เห็นได้อย่างชัดเจน **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการตรวจสอบที่เป็นอิสระ*) สำหรับหลักฐานการปรับใช้งานและการยกระดับที่สามารถสร้างใหม่ได้ **ข้อ XIII-F** (*พื้นฐานความยืดหยุ่นและการรักษาตนเอง*) โดยที่วินัยในการฟื้นฟูจะตัดกับการเปลี่ยนแปลงวงจรชีวิต
- **ชั้นการใช้งาน:** [**ซีเอส-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*การจำแนกประเภทระบบและการจัดการ*) และ [**ซีเอส-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*การออกแบบ การทดสอบ การตรวจสอบ และการปรับใช้*) **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบมีหน้าที่ในวงจรชีวิตที่แข็งแกร่งที่สุด ถูกต้อง **คลาส ป** การรักษายังคงอยู่ภายใต้ **ข้อ XVIII** (*นวัตกรรมแบบแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์*) เฉพาะในขณะที่ผลกระทบจากภายนอกหายไปหรือแสดงให้เห็นได้ชัดเจนเท่านั้น

<a id="article-xvii-a-lifecycle-governance-and-environment-separation"></a>
#### มาตรา XVII-A: การกำกับดูแลวงจรชีวิตและการแยกสิ่งแวดล้อม
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), และ [บทที่หนึ่ง §20 แอปพลิเคชันบูรณาการ](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การกำกับดูแลแบบแบ่งประเภทตามขนาด](core_05_band_oversight.md#classification-scaled-governance) · [โอ](core_05_band_oversight.md#classification-scaled-governance) · [ม](core_05_band_oversight.md#classification-scaled-governance-a) · [ก](core_05_band_oversight.md#classification-scaled-governance-a) · [ค](core_05_band_oversight.md#classification-scaled-governance-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [ความรับผิดชอบ](core_05_apex_accountability_leg.md#accountability) · [โอ](core_05_apex_accountability_leg.md#accountability) · [ม](core_05_apex_accountability_leg.md#accountability-m) · [ก](core_05_apex_accountability_leg.md#accountability-a) · [ค](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*กล่าวโดยทั่วไป: ระบบที่ส่งผลกระทบอย่างมีนัยสำคัญต่อโลกภายนอกจะต้องแยกการพัฒนา การทดสอบ และการผลิตออกจากกัน และพฤติกรรมที่ไม่ใช่การผลิตจะต้องไม่รั่วไหลผ่านการป้องกันการผลิต*

บทความนี้กำหนดพื้นฐานสำหรับความสมบูรณ์ของสิ่งแวดล้อม:

- **ความสมบูรณ์ของสิ่งแวดล้อม:** **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบภายใต้ **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ**และอื่นๆที่ไม่ใช่-**คลาส ป** ระบบที่มีผลกระทบภายนอกอย่างเป็นรูปธรรม ต้องใช้สภาพแวดล้อมการปฏิบัติงานที่แยกจากกัน ตัวอย่างเช่น
  - การพัฒนา;
  - การทดสอบ;
  - การแสดงละคร;
  - การผลิต;
  - นักบินตามความเหมาะสม

  สภาพแวดล้อมเหล่านั้นต้องมี:
  - เส้นทางการส่งเสริมการขายที่จัดทำเป็นเอกสาร
  - การแยกระหว่างสภาพแวดล้อม
  - ควบคุมเพื่อให้พฤติกรรมที่ไม่ใช่การผลิตไม่สามารถหลีกเลี่ยงการป้องกันการผลิตได้
<a id="article-xvii-b-progressive-deployment-and-reversibility"></a>
#### มาตรา XVII-B: การปรับใช้แบบก้าวหน้าและการพลิกกลับได้
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1 หลักการแลกเปลี่ยนหลัก](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), และ [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) · [โอ](core_05_band_continuity.md#reversibility-constitutional) · [ม](core_05_band_continuity.md#reversibility-constitutional-a) · [ก](core_05_band_continuity.md#reversibility-constitutional-a) · [ค](core_05_band_continuity.md#reversibility-constitutional-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*โดยทั่วไป: ค่อยๆ เผยแพร่การเปลี่ยนแปลง โดยมีการยกระดับเอกสารและความสามารถในการยกเลิก และในกรณีที่ไม่สามารถยกเลิกได้ทั้งหมด ให้มีแผนในการควบคุมหรือชดเชยความเสียหาย*

บทความนี้กำหนดพื้นฐานสำหรับการปรับใช้แบบก้าวหน้าและการย้อนกลับได้:

- **การใช้งานที่ก้าวหน้าและตรวจสอบได้:** การเปลี่ยนแปลงที่เพิ่มผลกระทบอย่างมีนัยสำคัญหรือการพึ่งพาจะต้องดำเนินการผ่านการยกระดับที่สมเหตุสมผลและเป็นเอกสาร
  - การยกระดับจะต้องสอดคล้องกับ **[Corpus_systems.md](corpus_systems.md), CS-5 — การออกแบบ การทดสอบ การตรวจสอบ และการปรับใช้**.
  - จะต้องรวมถึงการย้อนกลับและการกักกันหากเป็นไปได้
- **การพลิกกลับได้:** ระบบจะต้องรวมกลไกการพลิกกลับได้สัดส่วนกับอันตรายที่อาจเกิดขึ้น ตัวอย่าง:
  - ย้อนกลับ;
  - การบรรจุ;
  - การฟื้นฟูแบบชดเชยที่ไม่สามารถย้อนกลับได้เต็มจำนวน

  ในกรณีที่การปรับใช้จะยึดการฟื้นฟูข้อกำหนดพื้นฐาน ให้ใช้มาตรการป้องกันตามสัดส่วน และการให้เหตุผลที่ผู้มีส่วนได้ส่วนเสียมองเห็นได้ **บทที่หนึ่งถึงห้า**.
<a id="article-xvii-c-misclassification-and-evasion-consequences"></a>
#### มาตรา XVII-C: การจัดประเภทที่ไม่ถูกต้องและการหลีกเลี่ยงผลที่ตามมา
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), และ [บทที่หนึ่ง §20 แอปพลิเคชันบูรณาการ](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [การกำกับดูแลแบบแบ่งประเภทตามขนาด](core_05_band_oversight.md#classification-scaled-governance) · [โอ](core_05_band_oversight.md#classification-scaled-governance) · [ม](core_05_band_oversight.md#classification-scaled-governance-a) · [ก](core_05_band_oversight.md#classification-scaled-governance-a) · [ค](core_05_band_oversight.md#classification-scaled-governance-c)
- [ความรับผิดชอบ](core_05_apex_accountability_leg.md#accountability) · [โอ](core_05_apex_accountability_leg.md#accountability) · [ม](core_05_apex_accountability_leg.md#accountability-m) · [ก](core_05_apex_accountability_leg.md#accountability-a) · [ค](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*พูดง่ายๆ: ระบบไม่สามารถเรียกตัวเองว่า "การทดลอง" ได้ **คลาส ป**หรือ "ผลกระทบต่ำ" เพื่อหลบหลีกภาระผูกพันในขณะที่ส่งผลกระทบต่อโลกภายนอกอย่างแท้จริง*

บทความนี้กำหนดผลที่ตามมาของการจัดประเภทที่ไม่ถูกต้องและการหลีกเลี่ยง:

- **การจำแนกประเภทและการหลีกเลี่ยง:** ไม่มีระบบใดที่จะอ้างสิทธิ์ในวงจรการใช้งานที่ลดลงหรือภาระผูกพันในการปรับใช้ในขณะที่พยายามสร้างผลกระทบภายนอกที่ไม่เปิดเผยหรือเป็นสาระสำคัญ
  - การกระทำดังกล่าวละเมิดความสมบูรณ์ของข้อมูล (**ข้อ XV** (*ความสมบูรณ์ของขอบเขตข้อมูล*)) และความสามารถในการตรวจสอบในกรณีที่หลักฐานที่สังเกตได้มีส่วนเกี่ยวข้อง (**ข้อ XVI-ก** (*การตรวจสอบและหลักฐานที่สังเกตได้*))
  - อยู่ภายใต้การตรวจสอบ (**ข้อ XVI-ก** (*การตรวจสอบและหลักฐานที่สังเกตได้*)) การตรวจสอบจุดยืน (**ข้อ XIX-A** (*Standing Distinction*)) และการแก้ไขข้อขัดแย้ง (**บทความ XX-ก** (*วัตถุประสงค์และขอบเขตของความยุติธรรม*))

<a id="article-xviii-sandboxed-innovation-experimentation-and-creative-freedom"></a>
### ข้อ XVIII: นวัตกรรมแบบแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์

<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 กระบวนการแก้ไขการชนกันของรัฐธรรมนูญ](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), และ [§19 การจัดตำแหน่งสิ่งจูงใจและการยึดครองระบบ](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<br>

*ในแง่ธรรมดา: **ข้อ XVIII** (*นวัตกรรมแบบแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์*) เป็นสิทธิด้านนวัตกรรมและความคิดสร้างสรรค์ — ความรู้สึกอาจทดลอง สร้าง และแสดงออกภายใต้กฎเกณฑ์ที่เบากว่าเมื่อไม่มีผลกระทบภายนอกที่แท้จริงหรือถูกจำกัดไว้อย่างแท้จริง แต่ป้ายชื่อ "แซนด์บ็อกซ์" ไม่ใช่ช่องโหว่ เมื่อโปรเจ็กต์เริ่มส่งผลกระทบต่อผู้อื่นหรือเชื่อมต่อกับระบบที่ใช้ร่วมกัน จะต้องก้าวไปสู่ภาระผูกพันตลอดอายุการใช้งาน นักสร้างสรรค์นวัตกรรมสามารถได้รับรางวัล แต่ไม่ใช่โดยการกักขังความรู้ เครื่องมือ หรือโครงสร้างพื้นฐานที่ผู้อื่นจำเป็นต้องใช้ในการใช้ชีวิต เรียนรู้ ซ่อมแซม หรือตรวจสอบ*

บทความนี้ระบุว่า **พื้นรัฐธรรมนูญ** สำหรับนวัตกรรมแซนด์บ็อกซ์ การทดลอง และเสรีภาพในการสร้างสรรค์ภายใต้ [เป้าหมายสองประการตามรัฐธรรมนูญ](core_00_preamble.md#two-constitutional-aims): :

- **เฟื่องฟู:** ความรู้สึกสามารถสร้างสรรค์ ทดลอง และสร้างสรรค์โดยลดข้อกำหนดด้านโครงสร้างลงเมื่อไม่มีผลกระทบภายนอกที่สำคัญหรือถูกกักเก็บไว้ได้ — ผ่านการเลือกใช้อย่างแท้จริง การเปิดเผยข้อมูลอย่างตรงไปตรงมา และโครงสร้างการให้รางวัลที่รักษาการทดลองขั้นปลายน้ำ การซ่อมแซม การทำงานร่วมกัน และการตรวจสอบข้อเท็จจริงตามความเป็นจริง
- **ความต่อเนื่อง:** การรักษาแบบแซนด์บ็อกซ์ไม่ได้ทำให้เป็นการดำเนินการที่มีภาระผูกพันต่ำอย่างถาวรเมื่อผลกระทบ การพึ่งพา หรือการบูรณาการเพิ่มมากขึ้น การเปลี่ยนไปใช้ภาระผูกพันที่สูงกว่าจะยังคงทันเวลา ความพิเศษเฉพาะตัวยังคงแคบและตรวจสอบได้ และนวัตกรรมที่มีความสำคัญต่อการพึ่งพาจะต้องไม่แข็งตัวกลายเป็นกล่องหุ้มที่ทนทานหรือการล็อคอิน

การแสวงหาที่ถูกต้องตามกฎหมายดำเนินไปผ่านทาง [Tetrad รัฐธรรมนูญ](core_00_preamble.md#constitutional-tetrad), ปรับขนาดเป็น [สัดส่วนการถือหุ้นวัสดุ](core_00_preamble.md#material-stake): :

- **การเข้าร่วม:** ในการเลือกเข้าร่วมการทดลอง การใช้ซ้ำและการท้าทายขั้นปลายน้ำ และการประเมินใหม่เมื่อระบบแซนด์บ็อกซ์เริ่มมีความสำคัญนอกขอบเขตที่ระบุไว้
- **การกำกับดูแล:** ผ่านสถานะการทดลองที่เปิดเผย ขอบเขตการกักกัน การติดตามการเปลี่ยนแปลง และการเรียกร้องรางวัลหรือการผูกขาดที่ตรวจสอบได้ตามสัดส่วนตามประเภท การพึ่งพา และผลกระทบจากการประสานงาน
- **ความรับผิดชอบ:** นักสร้างสรรค์นวัตกรรมและผู้ปฏิบัติงานต้องตอบคำถามสำหรับการรั่วไหลของความเสี่ยงที่ยังไม่มีการควบคุมไปยังผู้อื่น การรับความรู้สึกโดยไม่มีทางเลือกที่แท้จริง การลากเท้าของพวกเขาในการก้าวไปสู่ภาระหน้าที่อย่างเต็มที่ หรือการให้รางวัลแก่การดำเนินการที่ระงับการซ่อมแซม งานด้านความปลอดภัย การทำงานร่วมกัน การวิจัย การศึกษา หรือการโยกย้าย
- **ความทันเวลา:** ในการเปลี่ยนไปใช้ **ข้อ XVII** (*วงจรชีวิตระบบ สภาพแวดล้อม และการย้อนกลับได้*) ข้อกำหนดวงจรการใช้งานและการประเมินใหม่แต่เพียงผู้เดียวก่อนความล่าช้าหรือการล็อคอินจะทำให้ภาระผูกพันที่สูงกว่า การเข้าถึงในวงกว้าง หรือการแก้ไขไม่สามารถเข้าถึงได้อย่างมีประสิทธิภาพ

*เพื่อนบ้านบทความ:*

- **อ่านด้วยกัน:** **ข้อ XVII** (*วงจรชีวิตระบบ สภาพแวดล้อม และการพลิกกลับได้*) เมื่อผลกระทบ การพึ่งพา หรือการบูรณาการเกินกว่าเงื่อนไขแซนด์บ็อกซ์ **ข้อ XV** (*ความสมบูรณ์ของขอบเขตข้อมูล*) และ **ข้อ XVIII-E** (*ความสมบูรณ์ของการตีพิมพ์ทางวิทยาศาสตร์ การทบทวน และการจำลองแบบ*) โดยที่ความสมบูรณ์ในขอบเขตการตีพิมพ์มีส่วนเกี่ยวข้องอย่างเป็นรูปธรรม **ข้อ XVI** (*การตรวจสอบ ความโปร่งใส และการทวนสอบโดยอิสระ*) สำหรับการเปิดเผยและการตรวจสอบการเรียกร้องการกักกันและการเปลี่ยนแปลง
- **ชั้นการใช้งาน:** [**ซีเอส-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*การออกแบบ การทดสอบ การตรวจสอบ และการปรับใช้*) และ [**ซีเอส-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*การจำแนกประเภทระบบและการจัดการ*)

<a id="article-xviii-a-sandboxed-scope"></a>
#### มาตรา XVIII-A: ขอบเขตแบบแซนด์บ็อกซ์
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [บทที่หนึ่ง §7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), และ [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การกำกับดูแลแบบแบ่งประเภทตามขนาด](core_05_band_oversight.md#classification-scaled-governance) · [โอ](core_05_band_oversight.md#classification-scaled-governance) · [ม](core_05_band_oversight.md#classification-scaled-governance-a) · [ก](core_05_band_oversight.md#classification-scaled-governance-a) · [ค](core_05_band_oversight.md#classification-scaled-governance-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [ผลกระทบของวัสดุ](core_05_band_oversight.md#material-impact) · [โอ](core_05_band_oversight.md#material-impact) · [ม](core_05_band_oversight.md#material-impact-a) · [ก](core_05_band_oversight.md#material-impact-a) · [ค](core_05_band_oversight.md#material-impact-c)

</details>

<br>

*พูดง่ายๆ ก็คือ การทดลองและงานสร้างสรรค์สามารถดำเนินการได้ภายใต้กฎเกณฑ์ที่เบากว่า — แต่เฉพาะเมื่อไม่มีผลกระทบภายนอกที่แท้จริงหรือจำกัดไว้อย่างพิสูจน์ได้เท่านั้น ป้าย "แซนด์บ็อกซ์" เพียงอย่างเดียวไม่เพียงพอ*

บทความนี้กำหนดนวัตกรรมและการทดลองที่เหมาะสม และเมื่อใดที่การใช้ Sandbox:

- **นวัตกรรมและการทดลองที่ถูกต้อง:** Sentient มีสิทธิที่จะสร้างสรรค์ ทดลอง และแสดงออกผ่านระบบที่ทำงานโดยมีความต้องการด้านโครงสร้างลดลง เมื่อไม่มีผลกระทบจากภายนอกหรือสามารถกักเก็บผลกระทบภายนอกได้
- **คุณสมบัติของแซนด์บ็อกซ์:** การรักษาแบบแซนด์บ็อกซ์ — รวมถึงใช้ได้ด้วย **คลาส ป** การจำแนกประเภทภายใต้ **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ** ถ้ามี — ขึ้นอยู่กับ:
  - การบรรจุจริง
  - การย้อนกลับ;
  - บูรณาการอย่างจำกัดกับระบบที่ใช้ร่วมกัน

  ไม่สามารถอ้างสิทธิ์ได้ด้วยฉลากเพียงอย่างเดียว
- **รายละเอียดการดำเนินการ:** มีรายละเอียดเพิ่มเติมปรากฏใน **[Corpus_systems.md](corpus_systems.md),ซีเอส-5** (*ระบบส่วนบุคคล โดดเดี่ยว และระบบทดลอง*; *ระบบสร้างสรรค์ ความบันเทิง และการแสดงออก*)

<a id="article-xviii-b-containment-disclosure-and-opt-in"></a>
#### มาตรา XVIII-B: การกักกัน การเปิดเผย และการเลือกใช้
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [บทที่หนึ่ง §7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), และ [§13.1 หลักการแลกเปลี่ยนหลัก](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ยินยอม](core_05_band_participation.md#consent-constitutional) · [โอ](core_05_band_participation.md#consent-constitutional) · [ม](core_05_band_participation.md#consent-constitutional-a) · [ก](core_05_band_participation.md#consent-constitutional-a) · [ค](core_05_band_participation.md#consent-constitutional-c)
- [เสี่ยง](core_05_band_continuity.md#risk) · [โอ](core_05_band_continuity.md#risk) · [ม](core_05_band_continuity.md#risk-a) · [ก](core_05_band_continuity.md#risk-a) · [ค](core_05_band_continuity.md#risk-c)
- [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) · [โอ](core_05_band_continuity.md#reversibility-constitutional) · [ม](core_05_band_continuity.md#reversibility-constitutional-a) · [ก](core_05_band_continuity.md#reversibility-constitutional-a) · [ค](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*ในแง่ธรรมดา: ระบบทดลองจะต้องซื่อสัตย์เกี่ยวกับการทดลอง ต้องไม่ทิ้งความเสี่ยงให้กับบุคคลภายนอก และต้องไม่เกณฑ์ผู้ที่ไม่ได้เข้าร่วมผ่านค่าเริ่มต้นการออกแบบหรือการพึ่งพาที่ซ่อนอยู่*

บทความนี้กำหนดการควบคุม การเปิดเผย การเลือกเข้าร่วม และการย้อนกลับขั้นต่ำสำหรับระบบทดลอง:

- **การบรรจุและการเปิดเผย:** ระบบดังกล่าวจะต้องเปิดเผยอย่างชัดเจน:
  - สถานะการทดลองหรือไม่มีการผลิต
  - ความเสี่ยงที่มีสาระสำคัญ
  - ขอบเขตของความโดดเดี่ยว
  - การพึ่งพาโครงสร้างพื้นฐานที่ใช้ร่วมกัน บุคคลที่สาม หรือระบบนิเวศที่คาดหวัง

  พวกเขาจะต้องไม่ส่งออกความเสี่ยงที่ไม่มีอยู่ภายนอกไปยังผู้อื่น โครงสร้างพื้นฐานที่ใช้ร่วมกัน หรือระบบนิเวศ
- **เลือกใช้และย้อนกลับ:** การเข้าร่วมในการทดลองที่มีความเสี่ยงสูงหรือใกล้กับสารตั้งต้นจะต้องเลือกเข้าร่วมอย่างแท้จริงหากเป็นไปได้
  - ฝ่ายที่ไม่เข้าร่วมที่ได้รับผลกระทบจะต้องไม่ลงทะเบียนโดยไม่สมัครใจโดยการออกแบบ ค่าเริ่มต้น หรือการอ้างอิงที่คลุมเครือ
  - ผู้มีส่วนได้ส่วนเสียจะต้องรักษาแนวทางการย้อนกลับหรือการฟื้นฟูที่เป็นไปได้ตามสัดส่วนกับความเสี่ยง
<a id="article-xviii-c-transition-to-higher-obligation-regimes"></a>
#### มาตรา XVIII-C: การเปลี่ยนผ่านไปสู่ระบอบการปกครองที่มีภาระผูกพันสูงกว่า
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§4 ความปลอดภัย](core_01_a_values_principles.md#4-safety-harm-constraint), [บทที่แปด §3 การประเมินการรับรองทั้งระบบ](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), และ [บทที่หนึ่ง §20 แอปพลิเคชันบูรณาการ](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [การกำกับดูแลแบบแบ่งประเภทตามขนาด](core_05_band_oversight.md#classification-scaled-governance) · [โอ](core_05_band_oversight.md#classification-scaled-governance) · [ม](core_05_band_oversight.md#classification-scaled-governance-a) · [ก](core_05_band_oversight.md#classification-scaled-governance-a) · [ค](core_05_band_oversight.md#classification-scaled-governance-c)
- [การพึ่งพาอาศัยกัน](core_05_band_continuity.md#dependency) · [โอ](core_05_band_continuity.md#dependency) · [ม](core_05_band_continuity.md#dependency-a) · [ก](core_05_band_continuity.md#dependency-a) · [ค](core_05_band_continuity.md#dependency-c)
- [การย้อนกลับได้](core_05_band_continuity.md#reversibility-constitutional) · [โอ](core_05_band_continuity.md#reversibility-constitutional) · [ม](core_05_band_continuity.md#reversibility-constitutional-a) · [ก](core_05_band_continuity.md#reversibility-constitutional-a) · [ค](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*พูดง่ายๆ: เมื่อระบบแซนด์บ็อกซ์เริ่มมีความสำคัญในโลกแห่งความเป็นจริง ระบบนั้นจะต้องเปลี่ยนไปใช้ภาระหน้าที่ในโลกแห่งความเป็นจริง — โดยทันที ไม่ใช่ตามความสะดวกของผู้ปฏิบัติงาน*

บทความนี้กำหนดว่าระบบแซนด์บ็อกซ์จะย้ายไปสู่ภาระหน้าที่ที่สูงกว่าเมื่อใด:

- **การเปลี่ยนไปสู่ภาระผูกพันที่สูงขึ้น:** เมื่อผลกระทบ การพึ่งพา การย้อนกลับไม่ได้ หรือการบูรณาการกับระบบที่ใช้ร่วมกันเติบโตขึ้น ระบบจะต้องเปลี่ยนแปลงอย่างโปร่งใสและไม่มีความล่าช้าตามโอกาส
  - การเปลี่ยนแปลงจะต้องก้าวไปสู่ข้อกำหนดเต็มรูปแบบของ **ข้อ XVII-A** (*การกำกับดูแลวงจรชีวิตและการแยกสิ่งแวดล้อม*) และ **ซีเอส-5** (*ระบบที่ไม่ใช่การทดลอง*)
  - การป้องกันชั่วคราวตามสัดส่วนกับความเสี่ยงในปัจจุบันที่ใช้ระหว่างการเปลี่ยนแปลง
  - การดำเนินการแบบแซนด์บ็อกซ์อาจไม่ดำเนินต่อไปสำหรับฟังก์ชันที่มีผลกระทบในโลกแห่งความเป็นจริงเกินกว่าเงื่อนไขของแซนด์บ็อกซ์อย่างมาก
  - การเปลี่ยนแปลงจะต้องเกิดขึ้นภายในกรอบเวลาที่เหมาะสมตามสัดส่วนการเติบโตนั้น
<a id="article-xviii-d-innovation-reward-disclosure-and-anti-enclosure"></a>
#### มาตรา XVIII-D: รางวัลนวัตกรรม การเปิดเผย และการต่อต้านสิ่งที่แนบมา
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [บทที่หนึ่ง §7 เสรีภาพ](core_01_a_values_principles.md#7-freedom-bounded-agency), และ [§18 การกำกับดูแลภายใต้วินัยในการพิทักษ์](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [รางวัลนวัตกรรมและการต่อต้านสิ่งที่แนบมา](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [โอ](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [ม](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [ก](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [ค](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-c)
- [การล็อคอินอย่างเป็นระบบ](core_05_band_continuity.md#systemic-lock-in) · [โอ](core_05_band_continuity.md#systemic-lock-in) · [ม](core_05_band_continuity.md#systemic-lock-in-a) · [ก](core_05_band_continuity.md#systemic-lock-in-a) · [ค](core_05_band_continuity.md#systemic-lock-in-c)
- [สัดส่วน](core_05_band_accountability.md#proportionality) · [โอ](core_05_band_accountability.md#proportionality) · [ม](core_05_band_accountability.md#proportionality-a) · [ก](core_05_band_accountability.md#proportionality-a) · [ค](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*พูดง่ายๆ ก็คือ ผู้สร้างนวัตกรรมสามารถได้รับรางวัลได้ แต่ความพิเศษเฉพาะตัวจะต้องจำกัด มีระยะเวลาจำกัด และตรวจสอบได้ โครงสร้างพื้นฐานด้านสาธารณสุข ความปลอดภัย และหลักจะต้องสามารถเข้าถึงได้ — และเมื่อบางสิ่งกลายเป็นโครงสร้างพื้นฐานที่สำคัญแล้ว ความพิเศษที่เหลืออยู่ใดๆ จะต้องได้รับการประเมินใหม่*

บทความนี้กำหนดวิธีการให้รางวัลแก่นวัตกรรมโดยไม่ต้องปิดล้อมสิ่งที่ประชาชนต้องการ:

- **รางวัลนวัตกรรมและการต่อต้านสิ่งที่แนบมา:** ความรู้สึกอาจได้รับรางวัลสำหรับนวัตกรรมทางวัตถุ มีประโยชน์ต่อสังคม และได้รับการเปิดเผยอย่างเพียงพอ
  - รางวัลจะต้องมีโครงสร้างเพื่อรักษา:
    - นวัตกรรมแห่งอนาคต
    - การเข้าถึงในวงกว้าง
    - การทดลองขั้นปลายน้ำ
    - ซ่อมแซม;
    - การทำงานร่วมกัน;
    - การตรวจสอบข้อเท็จจริงตามความเป็นจริง
  - รางวัลจะต้องไม่มีโครงสร้างสำหรับตู้ที่ทนทาน
- **สิทธิพิเศษชั่วคราวและตรวจสอบได้เท่านั้น:** สิทธิ์ในการยกเว้นใดๆ เหนือการประดิษฐ์ การออกแบบ อินเทอร์เฟซ กระบวนการ หรือระบบการแสดงออกที่เป็นประโยชน์อันเป็นประโยชน์จะต้องปฏิบัติตาม [**หลักการจำกัดน้อยที่สุด มีกำหนดเวลา และตรวจสอบได้**](core_01_b_interaction_interpretation.md#1315-least-restrictive-time-bounded-and-reviewable-constraint-principle) และจะต้องเป็น:
  - แคบ;
  - กำหนดเวลา;
  - ตรวจสอบได้;
  - ได้สัดส่วนกับการมีส่วนร่วมที่เกิดขึ้นจริงและภาระการพัฒนาที่สมเหตุสมผล

  ภาระการให้เหตุผลยังคงเป็นของผู้เรียกร้อง การแสดงที่มาและที่มาอาจคงอยู่เกินกว่าข้อกำหนดพิเศษ การยกเว้นที่คงทนและความขาดแคลนเทียมอาจไม่เป็นเช่นนั้น
- **การคุ้มครองเหมือนลิขสิทธิ์:** สำหรับบทความนี้ การคุ้มครองที่มีลักษณะคล้ายลิขสิทธิ์หมายถึงรางวัลพิเศษชั่วคราวเหนืองานที่มีการแสดงออกซึ่งตายตัว รวมถึงการควบคุมการคัดลอก การเผยแพร่ การจัดแสดงหรือการแสดงต่อสาธารณะ การดัดแปลง และการแสวงหาประโยชน์ในเชิงพาณิชย์ การระบุแหล่งที่มา แหล่งที่มา ความสมบูรณ์ และการป้องกันการฉ้อโกงอาจยังคงอยู่หลังจากการยกเว้นสิ้นสุดลง
- **การตีพิมพ์และการปรากฏตัวครั้งแรก:** การตีพิมพ์หมายถึงการที่ผู้สร้างหรือผู้ถือสิทธิ์โดยชอบด้วยกฎหมายจงใจเผยแพร่ผลงานที่แสดงออกอย่างชัดเจนต่อสาธารณะ ตลาดเชิงพาณิชย์ หรือผู้ชมที่เปิดกว้าง การเผยแพร่ของเอกชน การตรวจสอบที่เป็นความลับ ความร่วมมือที่จำกัด การจัดเก็บข้อมูลถาวรที่ไม่มีการเข้าถึงโดยสาธารณะ หรือการแชร์ฉบับร่างที่ไม่ใช่เชิงพาณิชย์ไม่ถือเป็นการตีพิมพ์โดยตัวมันเอง การปรากฏตัวครั้งแรกหมายถึงการเผยแพร่ผลงานฉบับร่างที่สามารถระบุตัวตนได้อย่างมีนัยสำคัญต่อสาธารณะโดยไม่เป็นความลับเป็นครั้งแรก รวมถึงการเผยแพร่ฉบับร่างที่ไม่ใช่เชิงพาณิชย์ด้วย
- **คำศัพท์ที่ตีพิมพ์สำหรับงานที่แสดงออก:** การคุ้มครองลิขสิทธิ์ที่คล้ายคลึงกันควรใช้การกำหนดเวลาตามการตีพิมพ์มากกว่าการกำหนดเวลาชีวิตของผู้เขียน
  - งานที่ตีพิมพ์ควรสันนิษฐานว่าได้รับไม่เกิน `publication+30` ปีแห่งการยกเว้น
  - ร่างที่ไม่ใช่เชิงพาณิชย์หรืองานแสดงออกที่ไม่ได้เผยแพร่ซึ่งมีการปรากฏตัวครั้งแรกอาจได้รับการยกเว้นเหมือนลิขสิทธิ์ไม่เกิน `initial appearance+50` ปี.
  - ถ้างานที่ปรากฏครั้งแรกได้รับการตีพิมพ์ในภายหลัง เงื่อนไขการยกเว้นจะถูกจำกัดไว้ก่อนหน้าของ `initial appearance+50` หรือ `publication+30`.
  - ห้ามใช้ร่าง งานที่ยังไม่ได้เผยแพร่ หรือกฎการเผยแพร่ล่าช้าเพื่อสร้างการยกเว้นโดยไม่มีกำหนด ระงับการเก็บถาวร เอาชนะคำพูดหรือการวิพากษ์วิจารณ์ที่ชอบด้วยกฎหมาย หรือขยายการควบคุมผลงานที่ทำหน้าที่เป็นโครงสร้างพื้นฐานทางวัฒนธรรม การศึกษา ความปลอดภัย มาตรฐาน หรือข้อมูลร่วมกัน
  - ระยะเวลาที่สั้นกว่า การแปลงบังคับเข้าถึงก่อนหน้านี้ หรือการปฏิบัติต่อการเข้าถึงสาธารณะโดยทันทีจะมีผลใช้ในกรณีที่งานคือ:
    - ได้รับทุนจากสาธารณะ
    - การพึ่งพาที่สำคัญ;
    - เหมือนมาตรฐาน;
    - พื้นฐานทางการศึกษา
    - เกี่ยวข้องกับความปลอดภัย;
    - ใช้เป็นโครงสร้างพื้นฐานทางวัฒนธรรมหรือข้อมูลที่ใช้ร่วมกันเป็นหลัก
- **การจัดการนวัตกรรมตามระดับการจำแนกประเภท:** รางวัลนวัตกรรมจะต้องปรับขนาดตามระดับของระบบ การพึ่งพา และผลกระทบจากการประสานงานภายใต้ **[Corpus_systems.md](corpus_systems.md), CS-3 — การจำแนกประเภทและการจัดการระบบ**.
  - สำหรับ **คลาสเอ**, **คลาสบี**, และ **คลาสซี** ระบบกลไกการให้รางวัลแบบรักษาการเข้าถึงเป็นที่ต้องการอย่างยิ่ง การยกเว้นจะต้องคงอยู่ในขอบเขตที่แคบเป็นพิเศษ ตรวจสอบได้รวดเร็ว และง่ายต่อการลบล้าง ในกรณีที่ความต่อเนื่อง การทำงานร่วมกัน การซ่อมแซม หรือการดำเนินการเพื่อประโยชน์สาธารณะมีส่วนเกี่ยวข้องอย่างมีนัยสำคัญ
  - นวัตกรรมที่มีการพึ่งพาต่ำกว่านอกคลาสเหล่านั้นอาจใช้การยกเว้นชั่วคราวที่ค่อนข้างกว้างกว่า เมื่อการเปิดเผยเป็นจริง ค่าใช้จ่ายในการเปลี่ยนต่ำ และการป้องกันการล็อคอินยังคงมีประสิทธิภาพ
- **เงื่อนไขการเปิดเผยข้อมูลและชั้นประโยชน์สาธารณะ:** การเรียกร้องรางวัลจำเป็นต้องมีการเปิดเผยข้อมูลที่เพียงพอสำหรับความเข้าใจที่เป็นอิสระ การตรวจสอบ และการทำซ้ำในภายหลัง โดยอยู่ภายใต้ข้อจำกัดชั่วคราวที่สมเหตุสมผลเท่านั้น **บทที่หนึ่ง** และ **ข้อ XVII-A** (*การกำกับดูแลวงจรชีวิตและการแยกสิ่งแวดล้อม*)
  - การอ้างสิทธิ์ในการรับรางวัลไม่เป็นไปตามข้อกำหนดเมื่อมีการใช้เพื่อระงับ: นอกเหนือจากที่จำเป็นอย่างเคร่งครัดและตรวจสอบได้
    - ซ่อมแซม;
    - งานด้านความปลอดภัย
    - การทำงานร่วมกัน;
    - การเก็บถาวร;
    - วิจัย;
    - การศึกษา;
    - การโยกย้าย
  - โดเมนที่มีความสำคัญต่อความอยู่รอด รากฐาน หรือการกำหนดมาตรฐานอาจต้องมีกลไกการได้รับรางวัล การรวมกลุ่ม การบังคับเข้าถึง หรือกลไกการซื้อโดยสาธารณะ แทนการยกเว้น
- **การแยกโดเมนและค่าเริ่มต้นที่รัดกุมยิ่งขึ้น:** รางวัลการยกเว้นขั้นสูงจะถือว่าไม่ได้รับการสนับสนุน — และอาจไม่สามารถใช้ได้อย่างเด็ดขาดหากมีเครื่องมือการรับเลี้ยงบุตรบุญธรรมระบุไว้ — สำหรับ:
  - ยาและสิ่งจำเป็นด้านสาธารณสุข
  - โครงสร้างพื้นฐานที่มีความสำคัญต่อการอยู่รอด
  - มาตรฐานการสื่อสารหลักหรือการทำงานร่วมกัน
  - ความรู้พื้นฐานทางวิทยาศาสตร์
  - กลไกความปลอดภัย การตรวจสอบ หรือการปฏิบัติตามตามรัฐธรรมนูญ

  ในโดเมนเหล่านั้น สถาบันควรต้องการรางวัลโดยตรง การเข้าถึงแบบรวม การออกใบอนุญาตภาคบังคับ การซื้อโดยสาธารณะ หรือกลไกที่เทียบเท่าที่สงวนการนำไปปฏิบัติ การซ่อมแซม และการแพร่กระจายในวงกว้าง
- **การจัดประเภทใหม่และการกระชับ:** เมื่อนวัตกรรมที่เริ่มแรกถือว่าเป็นการพึ่งพาที่ต่ำกว่า ต่อมาจะกลายเป็นชั้นการประสานงานที่สำคัญในการพึ่งพา ตัวอย่างเช่น แพลตฟอร์ม โปรโตคอล โมเดล ตลาด หรือช่องทางการชำระเงิน สถาบันจะต้องประเมินใหม่ภายใต้บังคับ **CS-3 — การจำแนกและการจัดการระบบ** ระดับ.
  - การประเมินใหม่อาจทำให้แคบลง แปลง หรือยุติการยกเว้นที่เหลืออยู่ โดยที่การผูกขาดอย่างต่อเนื่องจะทำให้เกิด:
    - การบังคับล็อคอิน;
    - ปัญหาคอขวดในการต่อต้านการแข่งขัน
    - การคุกคามที่เป็นสาระสำคัญต่อความต่อเนื่อง ความจริง หรือการมีส่วนร่วมอย่างเท่าเทียมกัน

<a id="article-xviii-e-scientific-publication-review-and-replication-integrity"></a>
#### มาตรา XVIII-E: การตีพิมพ์ทางวิทยาศาสตร์ การทบทวน และความสมบูรณ์ของการจำลองแบบ
<details>
<summary><strong><span style="color: #2563eb;">ติดตาม</span></strong></summary>

- ต้นน้ำ: หลักการ: บทที่หนึ่ง [§5 ความจริง](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 ข้อจำกัดในการเปิดเผยข้อมูลเชิง Epistemic](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), และ [§20 แอปพลิเคชันแบบรวม](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">คำจำกัดความ · การประเมิน · การปฏิบัติตาม</span></strong></summary>

- [ความจริง (ข้อจำกัดทางรัฐธรรมนูญ)](core_05_band_oversight.md#truth-constitutional-constraint) · [โอ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [ม](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ก](core_05_band_oversight.md#truth-constitutional-constraint-a) · [ค](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [ความซื่อสัตย์แบบ Epistemic](core_05_band_oversight.md#epistemic-integrity) · [โอ](core_05_band_oversight.md#epistemic-integrity-o) · [ม](core_05_band_oversight.md#epistemic-integrity-a) · [ก](core_05_band_oversight.md#epistemic-integrity-a) · [ค](core_05_band_oversight.md#epistemic-integrity-c)
- [ความสามารถในการตรวจสอบ](core_05_band_oversight.md#auditability) · [โอ](core_05_band_oversight.md#auditability) · [ม](core_05_band_oversight.md#auditability-a) · [ก](core_05_band_oversight.md#auditability-a) · [ค](core_05_band_oversight.md#auditability-c)

</details>

<br>

*พูดง่ายๆ ก็คือ วิทยาศาสตร์คือโครงสร้างพื้นฐานในการตรวจสอบโดยสาธารณะ หลักฐาน การจำลอง และการแก้ไขต้องมีความสำคัญมากกว่าแบรนด์วารสาร และการแก้ไขข้อผิดพลาดจะต้องง่ายกว่าการซ่อนไว้เสมอ*

บทความนี้กำหนดพื้นฐานสำหรับการตีพิมพ์ทางวิทยาศาสตร์ การทบทวน การจำลอง และการแก้ไข:

- **วิทยาศาสตร์เป็นโครงสร้างพื้นฐานในการตรวจสอบสาธารณะ:** การตีพิมพ์ทางวิทยาศาสตร์และทางวิชาการ การทบทวน การจำลอง และการแก้ไขจะต้องได้รับการจัดการเพื่อให้ก้าวหน้า:
  - การแสวงหาความจริง
  - การทำซ้ำ;
  - ความขัดแย้งที่ต้องรับผิดชอบ;
  - การเรียนรู้สาธารณะ

  สิ่งเหล่านี้จะต้องไม่ถูกจัดระเบียบเพื่อการกักตุนศักดิ์ศรี การดูแลประตูที่ทึบแสง หรือการผลิตที่ขาดแคลน
- **เปิดสิ่งพิมพ์และหลักฐานเพียงพอ:** การกล่าวอ้างเชิงประจักษ์หรือเชิงวิเคราะห์ของเนื้อหาจะต้องเผยแพร่ได้โดยไม่ต้องได้รับการอนุมัติล่วงหน้า
  - ข้อจำกัดที่อนุญาตเพียงอย่างเดียวคือความเป็นส่วนตัวที่แคบ ความปลอดภัยทางชีวภาพ ความปลอดภัย หรือข้อจำกัดที่เทียบเคียงได้ซึ่งสมเหตุสมผล **บทที่หนึ่ง** และ **ข้อ XVII-A** (*การกำกับดูแลวงจรชีวิตและการแยกสิ่งแวดล้อม*)
  - การเรียกร้องดังกล่าวจะต้องมีวิธีการ แหล่งที่มา ความไม่แน่นอน และรายละเอียดหลักฐานที่เพียงพอ — รวมถึงการเข้าถึงวัสดุอ้างอิงหรือสิ่งทดแทนที่สมเหตุสมผล ในกรณีที่จำเป็นสำหรับการตรวจสอบ — เพื่อให้เกิดความเข้าใจที่เป็นอิสระและการตรวจสอบยืนยันตามสัดส่วน
- **ตรวจสอบและจำลองแบบเหนือศักดิ์ศรี:** การพึ่งพาสถาบันควรติดตาม:
  - คุณภาพของหลักฐาน
  - วิจารณ์;
  - การจำลองแบบ;
  - พฤติกรรมการแก้ไข
  - ความน่าเชื่อถือเชิงอธิบายหรือเชิงคาดการณ์ในระยะยาว

  ต้องไม่ติดตามแบรนด์วารสาร พร็อกซีปัจจัยผลกระทบ หรือสถานะบรรณาธิการที่ปิดไปแล้ว
  - เรียกร้องด้วย [ผลกระทบของวัสดุ](core_05_band_oversight.md#material-impact) ที่เกี่ยวข้องกับนโยบาย เกี่ยวข้องกับความปลอดภัย หรือเกี่ยวข้องกับการพึ่งพา ควรเผชิญกับข้อสันนิษฐานที่แข็งแกร่งในการจำลองแบบโดยอิสระ การทบทวนโดยฝ่ายตรงข้าม หรือทั้งสองอย่าง ก่อนที่จะได้รับการเคารพจากสถาบันอย่างถาวร
  - การจำลองแบบ ผลลัพธ์ที่เป็นโมฆะ และงานที่เน้นการแก้ไขจะต้องยังคงสามารถเผยแพร่และอ้างอิงได้ตามเงื่อนไขที่ไม่ขึ้นอยู่กับการส่งสัญญาณอันทรงเกียรติ
- **การแก้ไขและการแข่งขัน:** การแก้ไข การแก้ไข และการแทนที่โดยสุจริตใจจะต้องง่ายกว่าการปกปิด
  - ระบบการทบทวนและบรรณาธิการจะต้องยังคงเป็นระบบที่สามารถโต้แย้ง ตรวจสอบได้ มีระเบียบวินัยด้านความขัดแย้ง และให้เหตุผลในการตัดสินใจยอมรับ การแก้ไข และการเพิกถอนที่สำคัญ
  - สิ่งต่อไปนี้ไม่เข้ากัน:
    - การปราบปรามผลลัพธ์ที่ไม่สะดวก
    - การตอบโต้ผู้ตรวจสอบหรือผู้ลอกเลียนแบบ;
    - การจัดการบันทึกทางวิทยาศาสตร์ที่ไม่โปร่งใส

---

**ไฟล์ก่อนหน้า:** [core_06_rights_part_b.md](core_06_rights_part_b.md)

**ไฟล์ถัดไป:** [core_06_rights_part_d.md](core_06_rights_part_d.md)
