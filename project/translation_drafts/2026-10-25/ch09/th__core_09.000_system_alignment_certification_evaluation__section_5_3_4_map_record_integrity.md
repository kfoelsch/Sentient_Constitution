<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (th)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 ความครบถ้วนของแผนที่และบันทึก

ก่อนอาศัยแผนที่ความพึ่งพาและบันทึกกระแสทรัพยากร การรับรองต้องตรวจสอบว่าเอกสารเหล่านั้นเป็นไปตาม **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*) โดยต้อง:

- **ครบถ้วน:** ครอบคลุมความพึ่งพาต้นน้ำและปลายน้ำที่สำคัญ กระแสทรัพยากร และความสัมพันธ์ที่ซ่อนเร้นหรือไม่สมดุลเมื่อมีนัยสำคัญ
- **เป็นปัจจุบัน:** ปรับปรุงบ่อยพอตามความเร็วของการเปลี่ยนแปลงและความสำคัญของระบบ รวมถึงชั้นระบบตาม [§2 System Class Evaluation](#2-system-class-evaluation). แสดงระบบตามที่ดำเนินงานอยู่ในขณะนี้ ไม่ใช่ตามสภาพในการรับรองครั้งก่อน
- **ตรวจสอบได้:** เปิดให้ตรวจสอบตาม **Article XVI-A** (*Auditability and Observable Evidence*).

แผนที่หรือบันทึกที่ไม่ผ่านการทดสอบข้อใดข้อหนึ่งไม่อาจใช้สนับสนุนข้อสรุปว่าระบบส่งคืนการสนับสนุนเพียงพอ ต้องบันทึกช่องว่างและจัดการตามหัวข้อ *Defects and misalignment* ด้านล่าง
