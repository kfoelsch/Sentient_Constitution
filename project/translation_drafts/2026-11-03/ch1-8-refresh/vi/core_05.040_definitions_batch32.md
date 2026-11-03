# Chapter Five definition batch 32 — Tier Window (vi)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Tier Window; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### Khung thời gian theo cấp

<details>
<summary><strong>Truy vết</strong></summary>

- Chủ thể chuẩn tắc: Chương Chín C §9.3.4 Khung thời gian theo cấp; đọc cùng Chương Mười Bốn §6 Giải quyết đúng hạn, cấp trọng yếu và kỷ luật chống trì hoãn. Đọc với Vòng chứng nhận và Bảo vệ tạm thời.

</details>

*Nói đơn giản: thời hạn ở một giai đoạn của vụ chứng nhận, được đặt theo cấp trọng yếu của vụ việc. Cấp thường khớp với lớp; mục tiêu tiếp nhận tương ứng là mục tiêu của cấp đó.*

- **What it is**
  - **In scope / out of scope / dependencies:** Phạm vi: thời gian và giới hạn ngoài của cấp trọng yếu được gán cho vụ chứng nhận. Cấp thường khớp với lớp Hệ thống/Thể chế; mục tiêu tiếp nhận của cấp là mục tiêu tương ứng. Không gồm thời hạn thông báo trước khi vận hành; chu kỳ tái chứng nhận; mục tiêu/giới hạn riêng Chương Mười Bốn. Phụ thuộc Vòng chứng nhận và Bảo vệ tạm thời. Cách dùng ở Chương Chín C §9.3.4; cấp/mục tiêu/giới hạn ở Chương Mười Bốn §6. Mục này chỉ nêu nghĩa Chương Năm.
<a id="tier-window-a"></a>
- **How to measure and assess**
  - Đánh giá theo họ đo lường liên tục: vụ việc được xếp vào cấp khớp lớp; việc quá hạn được xem xét theo yêu cầu Chương Mười Bốn hay không.
<a id="tier-window-c"></a>
- **What must hold**
  - **Primary failure:** Lỗi chính: tự động hóa/bộ lọc kéo dài khung thời gian hoặc mục tiêu tiếp nhận; không xem xét việc quá hạn theo quy định.
