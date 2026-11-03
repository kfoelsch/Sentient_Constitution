# Chapter Five definition batch 22 — Pilot (vi)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Pilot; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### Thí điểm

<details>
<summary><strong>Truy vết</strong></summary>

- Chủ thể chuẩn tắc: Chương Chín A §2.3 Chứng nhận thí điểm; B §7.1 Cổng đưa vào vận hành. Tiếp nối: CS-6.345 Vòng đời Hệ thống. Đọc với đưa vào vận hành, chứng nhận tạm thời, hồ sơ Hệ thống, Phụ thuộc, Khóa chặt hệ thống và Khả năng đảo ngược.

</details>

*Nói đơn giản: triển khai thật nhưng cố ý giới hạn. Chúng sinh cảm nhận bị tác động thật hoặc bắt đầu dựa vào, nên không phải thử nghiệm sandbox; phạm vi, dân số, thời hạn được định trước. Vì là thật nên cần chứng nhận riêng trước khi bắt đầu và không được âm thầm vượt giới hạn.*

- **What it is**
  - **In scope / out of scope / dependencies:** Phạm vi: lần đưa vào vận hành thật trước triển khai đầy đủ, giới hạn trong phạm vi/dân số/thời hạn nêu trước ở hồ sơ Hệ thống riêng. Chứng nhận chỉ bao phủ các giới hạn đó; vận hành vượt là lần đưa vào vận hành riêng do mở rộng trọng yếu và cần chứng nhận riêng trước. Nhãn beta/thử nghiệm/xem trước không quyết định. Không gồm thử sandbox không có tác động thật hoặc giai đoạn chuyển đổi không đáp ứng định nghĩa. Phụ thuộc đưa vào vận hành và hồ sơ Hệ thống. Độ sâu đánh giá/lý do không thí điểm ở Chương Chín A §2.3. Mục này chỉ nêu nghĩa Chương Năm.
<a id="pilot-a"></a>
- **How to measure and assess**
  - Đánh giá theo họ đo lường liên tục: chứng nhận và giới hạn ghi trước khi bắt đầu; thí điểm ở trong giới hạn; phần vượt được chứng nhận riêng trước khi vận hành; vận hành thật tên khác được chứng nhận là thí điểm hay triển khai đầy đủ.
<a id="pilot-c"></a>
- **What must hold**
  - **Primary failure:** Lỗi chính: coi thí điểm là thử nghiệm không cần chứng nhận riêng; thí điểm không giới hạn/dân số/kết thúc nhưng thực chất triển khai đầy đủ; vượt giới hạn không chứng nhận mới; tạo phụ thuộc/khóa chặt khiến việc từ chối, đặt điều kiện hay thu hồi sau này gây tốn kém cho chúng sinh bị ảnh hưởng.
