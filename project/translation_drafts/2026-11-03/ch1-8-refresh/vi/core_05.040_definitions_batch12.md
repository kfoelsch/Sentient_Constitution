# Chapter Five definition batch 12 — Clean Recertification (vi)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Clean Recertification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### Tái chứng nhận sạch

<details>
<summary><strong>Truy vết</strong></summary>

- Chủ thể chuẩn tắc: Chương Chín Phần C §9.3.1 Hai trạng thái. Đọc cùng Tái chứng nhận, Chứng nhận tạm thời và đầy đủ. Thành phần cụm: không.

</details>

*Nói đơn giản, tái chứng nhận sạch khi không có sai lệch hiện hữu và không có chỉ báo giám sát báo hiệu sai lệch sắp xảy ra. Chỉ các lần tái chứng nhận sạch mới được tính vào chứng nhận đầy đủ.*

- **What it is**
  - **In scope / out of scope / dependencies:** Phạm vi: tái chứng nhận không phát hiện sai lệch hiện hữu hoặc chỉ báo sắp xảy ra. Số lần tái chứng nhận tạm thời sạch liên tiếp theo yêu cầu là một đầu vào của Chứng nhận đầy đủ. Không gồm lần tái chứng nhận thất bại phát hiện sai lệch hiện hữu và đặt lại số đếm về không; hoặc lần không có sai lệch hiện hữu nhưng có chỉ báo sắp xảy ra—không thất bại nhưng không sạch. Phụ thuộc Tái chứng nhận và chứng nhận tạm thời/đầy đủ. Số đếm và yêu cầu ở Chương Chín C §9.3.1; mục này chỉ nêu nghĩa Chương Năm.
<a id="clean-recertification-a"></a>
- **How to measure and assess**
  - Đánh giá theo họ đo lường liên tục: chỉ lần sạch mới tăng số đếm; lần thất bại đặt lại về không hay không.
<a id="clean-recertification-c"></a>
- **What must hold**
  - **Primary failure:** Lỗi chính: tính sạch khi còn sai lệch, lỗi, kiểm tra quá hạn hoặc thử hồi quy thất bại chưa xử lý; tăng số đếm dù có chỉ báo sai lệch sắp xảy ra.
