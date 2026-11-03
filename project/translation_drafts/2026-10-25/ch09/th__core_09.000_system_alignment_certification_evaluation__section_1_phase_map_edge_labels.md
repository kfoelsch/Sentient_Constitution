<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (th)

## English source

```mermaid
    Rec -.->|VIb, §10 —<br/>verified inputs only;<br/>current certification or facts<br/>arising during certification| S
    G --->|Yes: operate<br/>within the record| Ch
    G --->|Certified,<br/>prerequisites pending| Hold
    Ch -->|Material defect:<br/>protect and correct| Rm
    Ch -->|On schedule, or<br/>material change or<br/>credible challenge<br/>requires review| Re
    Ch -.->|VIb, §10 —<br/>verified inputs only;<br/>operation may supply facts<br/>for Contribution and<br/>Violation records| S2
    Rm -->|Correction evidence<br/>is checked in the<br/>next review pass| Re
    G -->|Not Certified| Rm
```

## Translation draft

```mermaid
    Rec -.->|VIb, §10 —<br/>ใช้เฉพาะข้อมูลนำเข้าที่ตรวจสอบแล้ว;<br/>การรับรองปัจจุบันหรือข้อเท็จจริง<br/>ที่เกิดระหว่างการรับรอง| S
    G --->|ใช่: ดำเนินงาน<br/>ภายในขอบเขตของบันทึก| Ch
    G --->|ได้รับการรับรองแล้ว,<br/>ข้อกำหนดก่อนเริ่มยังค้างอยู่| Hold
    Ch -->|ข้อบกพร่องสำคัญ:<br/>คุ้มครองและแก้ไข| Rm
    Ch -->|ตามกำหนด หรือเมื่อ<br/>การเปลี่ยนแปลงสำคัญ หรือ<br/>การท้าทายที่น่าเชื่อถือ<br/>ทำให้ต้องทบทวน| Re
    Ch -.->|VIb, §10 —<br/>ใช้เฉพาะข้อมูลนำเข้าที่ตรวจสอบแล้ว;<br/>การดำเนินงานอาจให้ข้อเท็จจริง<br/>แก่บันทึก Contribution<br/>และ Violation| S2
    Rm -->|ตรวจสอบหลักฐานการแก้ไข<br/>ในการทบทวนรอบ<br/>ถัดไป| Re
    G -->|ไม่ได้รับการรับรอง| Rm
```
