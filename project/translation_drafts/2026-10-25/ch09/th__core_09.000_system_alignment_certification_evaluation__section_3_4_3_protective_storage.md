<!-- AI-assisted translation draft; unreviewed. §3.4.3 protective storage and key custody, source lines 684–691; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.3 protective storage and key custody (th)

## English source (lines 684–691)

##### 3.4.3 Protective Storage and Key Custody

For data in the restricted-by-default and non-accessible bands, certification must verify that the system meets the protective storage and key-custody minimum in [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). The record must show:
- where restricted data and its keys actually sit, including backups, caches, logs, and swap;
- that plaintext is confined to the processes that need it; and
- that audit, export, and lawful-override paths still work.

A claim of encryption without that evidence does not satisfy this check.

## Translation draft

##### 3.4.3 การจัดเก็บเชิงป้องกันและการดูแลกุญแจ

สำหรับข้อมูลในแถบที่จำกัดการเข้าถึงเป็นค่าเริ่มต้นและแถบที่ไม่สามารถเข้าถึงได้ การรับรองต้องตรวจสอบว่าระบบปฏิบัติตามขั้นต่ำด้านการจัดเก็บเชิงป้องกันและการดูแลกุญแจใน [CS-6.305 ส่วน A §5.0 แถบท่าทีการเข้าถึง](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands) บันทึกต้องแสดงว่า:

- ข้อมูลที่ถูกจำกัดและกุญแจของข้อมูลนั้นอยู่ที่ใดจริง รวมถึงข้อมูลสำรอง แคช บันทึก และพื้นที่สว็อป;
- ข้อความธรรมดาถูกจำกัดไว้เฉพาะกระบวนการที่จำเป็นต้องใช้; และ
- ช่องทางการตรวจสอบ การส่งออก และการสั่งทับโดยชอบด้วยกฎหมายยังทำงานได้

การกล่าวว่าเข้ารหัสแล้วโดยไม่มีหลักฐานดังกล่าวไม่ผ่านการตรวจสอบนี้
