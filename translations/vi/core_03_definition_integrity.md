<a id="chapter-three-definition-integrity-evasion-and-non-compliance"></a>
# CHƯƠNG BA: TÍNH TOÀN VẸN ĐỊNH NGHĨA, LẨN TRÁNH, VÀ KHÔNG TUÂN THỦ

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Ba tiếng Anh](../../core_03_definition_integrity.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_03_definition_integrity.md`](../../core_03_definition_integrity.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> **Trước (ngôn ngữ này):** [core_02_definition_structure.md](core_02_definition_structure.md)
>
> **Tiếp theo (ngôn ngữ này):** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)
> **Cung đọc:** §1 tính toàn vẹn định nghĩa và chống lẩn tránh → §2 không tuân thủ từ hành vi quan sát được và các kiểu lẩn tránh → §3 hồ sơ phát hiện và hiệu ứng quỹ đạo

</details>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): nơi Chương Ba sống và điều gì ở lại đây</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở chương này hay ở các chương khác.
>
> Nơi cái này sống (điều hướng):
> - **Chủ sở hữu hiến pháp:** tính toàn vẹn định nghĩa, lẩn tránh, và không tuân thủ cho công việc đánh giá. **Chương Hai** nắm cấu trúc; **Chương Bốn** nắm gánh và hiện vật dấu vết; **Chương Năm** nắm các định nghĩa chuẩn.
> - **Chủ sở hữu triển khai:** hồ sơ quỹ đạo, quy trình diễn đàn, và giao thức triển khai đưa các quy tắc này vào vận hành mà không thay chúng.
> - **Quy tắc chống dời chỗ:** chương này không gán ô quỹ đạo, định tuyến diễn đàn, hay chỉ định hành vi sai phản hiến pháp cuối.

</details>

<br>

Chương Ba là chủ sở hữu hiến pháp của **tính toàn vẹn định nghĩa, lẩn tránh, và không tuân thủ cho công việc đánh giá**.

<br>

*Nói thẳng: chương này chặn trò chơi chữ — nếu hành vi lẩn tránh các yêu cầu thực của một định nghĩa, cái đó được tính là không tuân thủ ngay khi giấy tờ trông ổn.*

<a id="1-definition-integrity-and-anti-evasion-constraints"></a>
### 1. Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: [Chương Hai, §1 — Mục đích và vai trò](core_02_definition_structure.md#1-purpose-and-role); [Chương Hai, §2 Yêu cầu tính toàn vẹn định nghĩa](core_02_definition_structure.md#2-definition-integrity-requirement).
- Hạ nguồn: [Chương Ba, mục 2 — Không tuân thủ từ hành vi hệ thống quan sát được](#2-non-compliance-from-observable-system-behavior); [Chương Bốn, mục 2 — Yêu cầu truy vết định nghĩa](core_04_burden_traceability_verification.md#2-definition-traceability-requirement); [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](core_04_burden_traceability_verification.md#5-compliance-evidence-standard); [Chương Tám — Mô hình đóng góp, vi phạm, và quỹ đạo](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model).
- Đọc cùng: [Chương Một, mục 4.2 — Sự thật (Ràng buộc tính toàn vẹn nhận thức)](core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint) — diễn giải dựa trên hành vi quan sát được hơn là cấu trúc hoặc ý định đã tuyên đưa ràng buộc sự thật hiến pháp vào vận hành ở tầng tính toàn vẹn định nghĩa.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Mục lục Chương Ba (không vận hành): liên kết theo bảng chữ cái tới các tiêu đề trong chương</span></strong></summary>

[Ràng buộc tính toàn vẹn phạm vi xuyên thành phần](#23-cross-component-scope-integrity-constraint)

[Ràng buộc tính toàn vẹn tương tác xuyên hệ thống](#24-cross-system-interaction-integrity-constraint)

[Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](#1-definition-integrity-and-anti-evasion-constraints)

[Hồ sơ phát hiện không tuân thủ](#3-non-compliance-finding-profiles)

[Ràng buộc vận hành](#34-operational-constraints)

[Hiệu ứng quỹ đạo cho hệ thống đã được chứng nhận](#31-standing-effects-for-already-certified-systems)

[Hiệu ứng quỹ đạo ở lần chứng nhận đầu](#32-standing-effects-at-first-certification)

[Hiệu ứng quỹ đạo cho hữu tri và thể chế](#33-standing-effects-for-sentients-and-institutions)

[Không tuân thủ từ hành vi hệ thống quan sát được](#2-non-compliance-from-observable-system-behavior)

[Mẫu lẩn tránh thường gặp](#21-common-evasion-patterns)

[Lẩn tránh rút gọn](#22-reductive-evasion)

[Ràng buộc tính toàn vẹn thời gian và liên tục](#25-temporal-integrity-and-continuity-constraint)

[Ràng buộc tính toàn vẹn bất định và không khai thác](#26-uncertainty-integrity-and-non-exploitation-constraint)

</details>

<br>

Mục này quản trị cách định nghĩa phải được diễn giải và áp dụng trong thực tế.

- Định nghĩa phải được diễn giải và áp dụng dựa trên hành vi hệ thống quan sát được và kết quả dưới điều kiện hệ thống chức năng đầy đủ.
- Diễn giải, xây dựng, và hành vi hệ thống làm suy phạm vi ngữ nghĩa, đánh giá, và tuân thủ đầy đủ của định nghĩa — tương ứng các thành phần Bản thể (O), Đánh giá (A), và Tuân thủ (C) của chúng — bị cấm; [**Mục 2**](#2-non-compliance-from-observable-system-behavior) của chương này nêu không tuân thủ từ hành vi quan sát được và lẩn tránh.
- Tương đương chức năng thắng trên đặt tên, cấu trúc, phân rã, biểu diễn, hoặc ý định đã tuyên; các kết quả một hệ thống sản sinh quản trị cách nó được phân loại và đánh giá.

Mục này không đặt các chuẩn đánh giá, đủ bằng chứng, hay gánh chứng minh, những cái đó được quản trị độc quyền bởi **Chương Hai, mục 1** và **Chương Bốn, mục 1 và 4**.

<a id="2-non-compliance-from-observable-system-behavior"></a>
### 2. Không tuân thủ từ hành vi hệ thống quan sát được
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: [Chương Ba, mục 1 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](#1-definition-integrity-and-anti-evasion-constraints); [Chương Hai, §2 Yêu cầu tính toàn vẹn định nghĩa](core_02_definition_structure.md#2-definition-integrity-requirement); [Chương Hai, §2.2 Không tuân thủ do làm yếu cấu trúc hoặc áp dụng](core_02_definition_structure.md#22-non-compliance-by-structural-or-applied-weakening).
- Hạ nguồn: các mục lục kiểu ở các mục [2.1](#21-common-evasion-patterns) đến [2.6](#26-uncertainty-integrity-and-non-exploitation-constraint); [3. Hồ sơ phát hiện không tuân thủ](#3-non-compliance-finding-profiles); [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](core_04_burden_traceability_verification.md#5-compliance-evidence-standard); [Chương Bốn, mục 3 — Yêu cầu khả năng quan sát của truy vết](core_04_burden_traceability_verification.md#3-observability-of-traceability-requirement); [Chương Bảy §16](../../core_08_b_system_alignment_certification_record_process.md#16-reopening-misalignment-and-non-evasion) (*con trỏ mở lại chứng nhận thẳng hàng hệ thống và chống lẩn tránh*); [Chương Tám — Mô hình đóng góp, vi phạm, và quỹ đạo](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model).
- Đọc cùng: [Chương Hai, §1 — Mục đích và vai trò](core_02_definition_structure.md#1-purpose-and-role) cho quy tắc thỏa cùng dưới điều kiện hệ thống chức năng đầy đủ; [Chương Hai, §2.4 Quy tắc diễn giải khi mơ hồ](core_02_definition_structure.md#24-interpretation-rule-under-ambiguity) — diễn giải làm yếu bảo vệ, thu hẹp điều phải được đánh giá, hoặc hạ kết quả thế giới thực thì không hợp lệ; [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](core_04_burden_traceability_verification.md#5-compliance-evidence-standard) — bằng chứng phải chứng minh tuân thủ dưới các quy tắc ở mục này; bằng chứng sẽ không tuân thủ ở đây thì thất gánh chứng minh; [Không tuân thủ](../../core_05_band_integrative.md#non-compliance).

</details>

<br>

*Nói thẳng: một hệ thống không tuân thủ khi điều nó thực sự làm hoặc sản sinh sẽ phá một định nghĩa — xét dưới điều kiện chức năng đầy đủ, không chỉ trên giấy. Lẩn tránh nghĩa là làm yếu một định nghĩa khi nó thực sự được áp dụng. Đó là không tuân thủ dưới Chương Hai §2.2 — bất kể ý định, nhận biết, hay mục đích đã nêu.*

Mục này định khi hệ thống không tuân thủ dựa trên hành vi và kết quả quan sát được, kể cả:

- nơi hành vi hoặc phạm vi đã tuyên lệch khỏi hiệu ứng thực
- lẩn tránh xuyên thời gian, quy mô, tương tác hệ thống, và điều kiện vận hành nơi chúng quan trọng

Một hệ thống không tuân thủ nơi những cái quan sát được đó sẽ vi phạm một định nghĩa dưới áp dụng đầy đủ các thành phần Bản thể (O), Đánh giá (A), và Tuân thủ (C) của nó, bất kể cấu trúc, diễn giải, hoặc triển khai đã tuyên.

**Cách đánh giá.** Hệ thống không tuân thủ nơi:

- tuyên bố đã nêu xung đột với điều thực sự có thể thấy:
  - hành vi hệ thống đã tuyên, biểu diễn, hoặc hiện vật kiểm toán xung đột với kết quả quan sát được; trong trường hợp đó, kết quả quan sát được quản trị
  - phạm vi hệ thống đã tuyên xung đột với hiệu ứng chức năng thực; trong trường hợp đó, định nghĩa phải được áp dụng dựa trên hành vi và hiệu ứng hệ thống thực
- một định nghĩa không được thỏa đầy đủ dưới điều kiện hệ thống chức năng đầy đủ:
  - phạm vi ngữ nghĩa, đo lường, đánh giá, và tuân thủ cùng nhau (O, M, A, và C)
  - kể cả xuyên thời gian, quy mô, hệ thống kết nối, và điều kiện vận hành nơi chúng quan trọng
- một định nghĩa được thỏa chỉ trên giấy trong khi phạm vi đầy đủ đó không được thỏa:
  - chỉ ở hình thức, biểu diễn, cấu trúc, quy trình, hoặc điều kiện hạn chế
  - kết quả không nhất quán với phạm vi bảo vệ, đánh giá, hoặc tuân thủ đầy đủ của một định nghĩa
  - thành phần định nghĩa chỉ được thỏa dưới điều kiện hạn chế, không đại diện, hoặc được xây chọn lọc
  - diễn giải giữ tuân thủ hình thức trong khi hạ kết quả thế giới thực

Các tiểu mục kiểu dưới đây liệt kê các mẫu thường gặp. Chúng không thay quy tắc đánh giá ở trên.

<a id="21-common-evasion-patterns"></a>
#### 2.1 Mẫu lẩn tránh thường gặp

*Nói thẳng: đây là những cách thường gặp một hệ thống có thể trông tuân thủ mà không thực sự thỏa định nghĩa — thước đổi, giấy tờ giả, phạm vi bị cắt, hoặc khuyến khích đẩy mọi người ra khỏi tuân thủ. Danh sách không đóng. Các kiểu có thể xảy ra cùng nhau. Thu hẹp điều định nghĩa nghĩa được phủ ở [§2.2](#22-reductive-evasion).*

Các dạng lẩn tránh sau bị cấm:

- **Thước giả và giấy tờ** — tuyên tuân thủ qua điều được đo, báo, hoặc ghi hơn là qua kết quả định nghĩa đòi:
  - đổi vào thước, chỉ số, hoặc mô tả lệch khỏi điều định nghĩa nói về, trong khi vẫn tuyên đạt
  - tối ưu cho một điểm hoặc thước theo cách làm kết quả thế giới thực định nghĩa đòi tệ hơn
  - trình hồ sơ, hiện vật, hoặc bằng chứng nêu sai có trọng điều hệ thống thực sự làm hoặc việc nó có tuân thủ không
  - thỏa yêu cầu trên tên, cấu trúc, hoặc quy trình mà không sản sinh hiệu ứng thế giới thực định nghĩa đòi (xem cũng [§2.1.1](#211-formal-label-and-representation-gaming))
- **Mánh phạm vi và ranh giới** — sắp xếp điều được tính, và khi nào, sao cho phần khó không bao giờ bị thử:
  - thu hẹp đánh giá hoặc áp dụng để bỏ ra phần tử hệ thống, hiệu ứng, hoặc điều kiện quan trọng
  - tách trách nhiệm xuyên thành phần, tác nhân, hoặc thời gian sao cho không ai phải thỏa định nghĩa cho toàn hệ thống
  - trông tuân thủ chỉ dưới quan sát, kiểm toán, hoặc cửa sổ hẹp trong khi phá định nghĩa trong vận hành rộng hơn
- **Bẫy khuyến khích** — xây thưởng, áp lực, hoặc động lực đẩy hệ thống một cách có hệ thống ra khỏi tuân thủ:
  - tạo điều kiện dưới đó khuyến khích, động lực, hoặc cân bằng làm suy tuân thủ như lẽ thường


<a id="211-formal-label-and-representation-gaming"></a>
##### 2.1.1 Chơi nhãn hình thức và biểu diễn

*Nói thẳng: một nhãn, hạng mục, hoặc rà soát đóng dấu suông không được tính nếu quyết định, bảo vệ, hoặc nghĩa vụ thực không bao giờ thực sự xảy ra khi nó quan trọng.*

Đây là một dạng tập trung của **Thước giả và giấy tờ**. Hệ thống không được thỏa định nghĩa hiến pháp qua nhãn, hạng mục hình thức, thủ tục danh nghĩa, hoặc biểu diễn một mình khi hiệu ứng thực, nhịp vận hành, hoặc kết quả chức năng định nghĩa đòi đang thiếu. Các mẫu bị cấm gồm, không giới hạn:

- phê duyệt *human-in-the-loop* hoặc *human-on-the-loop* (người trong vòng lặp hoặc người trên vòng lặp) chỉ tồn tại trên tên — không có quyền quyết định thực ở tốc độ hệ thống thực sự chạy
- rà soát đóng dấu suông, thảo luận giả, hoặc phân loại trên hồ sơ giấy dùng thay gánh đòi hoặc xét xử
- đổi tên hình thức, tái cấu trúc, hoặc xếp lại thực thể làm rơi nghĩa vụ mà không chuyển trách nhiệm trong thực tế
- lựa chọn phân loại tiện xóa các phân biệt định nghĩa đòi

Nơi đổi cấu trúc hình thức có trọng, áp dụng [Chương Một §11.6 Trách nhiệm người kế và không-thoát cấu trúc hình thức](core_01_c_stewardship_capacity_principles.md#116-successor-responsibility-and-formal-structure-non-escape).

<a id="22-reductive-evasion"></a>
#### 2.2 Lẩn tránh rút gọn

Rút gọn xảy ra nơi áp dụng một định nghĩa sản sinh kết quả không thỏa diễn đạt đầy đủ các thành phần Bản thể (O), Đánh giá (A), và Tuân thủ (C) của nó. Một hệ thống không tuân thủ nơi diễn giải hoặc áp dụng định nghĩa của nó rút phạm vi ngữ nghĩa, độ nghiêm đánh giá, hoặc yêu cầu tuân thủ của định nghĩa, sản sinh bảo vệ hoặc kết quả yếu hơn có trọng so với điều định nghĩa đầy đủ đòi.

Các dạng rút gọn sau bị cấm:
- Rút gọn ngữ nghĩa: coi một định nghĩa như mô tả trong khi gỡ lực chuẩn tắc hoặc đánh giá
- Rút gọn thủ tục: coi thực thi quy trình là đủ bất kể kết quả thế giới thực
- Rút gọn hình thức: coi tài liệu, cấu trúc, hoặc biểu diễn là đủ mà không có hiệu ứng chức năng
- Rút gọn phạm vi: loại điều kiện, phần tử hệ thống, hoặc hiệu ứng có trọng liên quan
- Rút gọn đánh giá: làm yếu điều kiện đánh giá đòi trong thực tế qua áp dụng chọn lọc
- Rút gọn kết quả: thế kết quả thay thế, một phần, hoặc trung gian cho kết quả thế giới thực đòi

<a id="23-cross-component-scope-integrity-constraint"></a>
#### 2.3 Ràng buộc tính toàn vẹn phạm vi xuyên thành phần
Mọi thành phần định nghĩa (Bản thể (O), Đo lường (M), Đánh giá (A), và Tuân thủ (C)) phải được áp dụng cho cùng phạm vi hệ thống chức năng, điều kiện đánh giá, và khung thời gian. Mọi thành phần phải được thỏa cùng nhau dưới phạm vi, điều kiện, và ngữ cảnh thời gian nhất quán.

Lệch thẳng hàng xuyên thành phần vừa là lẩn tránh vừa là không tuân thủ, kể cả:
- áp dụng thành phần Bản thể cho phạm vi hệ thống rộng hơn hoặc khác thành phần Tuân thủ
- áp dụng thành phần Đo lường cho phạm vi, điều kiện, hoặc khung thời gian khác các thành phần Bản thể, Đánh giá, hoặc Tuân thủ mà chúng nâng đỡ
- thỏa thành phần Đánh giá dưới điều kiện hạn chế hoặc lý tưởng trong khi khẳng định tuân thủ dưới vận hành đầy đủ
- chứng minh việc thỏa thành phần xuyên khung thời gian, thể hiện, hoặc trạng thái hệ thống khác nhau

<a id="24-cross-system-interaction-integrity-constraint"></a>
#### 2.4 Ràng buộc tính toàn vẹn tương tác xuyên hệ thống
Hệ thống phải được đánh giá như phần của hệ thống chức năng rộng hơn trong đó chúng vận hành. Đánh giá đó gồm phụ thuộc thượng nguồn, hiệu ứng hạ nguồn, và đường tương tác nơi có trọng liên quan. Định nghĩa phải được áp dụng xuyên các hệ thống tương tác nơi những tương tác đó ảnh hưởng có trọng các kết quả được định nghĩa quản trị.

Một hệ thống không tuân thủ nơi:
- hành vi của nó, kết hợp với hệ thống khác, sản sinh kết quả vi phạm một định nghĩa
- nó đẩy hiệu ứng ra hệ thống, quần thể, hoặc môi trường khác để giữ tuân thủ địa phương
- ranh giới hệ thống được dùng để loại hiệu ứng tương tác có trọng liên quan

<a id="25-temporal-integrity-and-continuity-constraint"></a>
#### 2.5 Ràng buộc tính toàn vẹn thời gian và liên tục
Mọi thành phần phải được thỏa liên tục dưới điều kiện hệ thống chức năng đầy đủ xuyên vòng đời hệ thống.

Tuân thủ phải được giữ xuyên thời gian, kể cả cập nhật hệ thống, đổi phiên bản, huấn luyện lại, tái cấu hình, và đổi ngữ cảnh triển khai.

Một hệ thống không tuân thủ nơi:
- tuân thủ chỉ được chứng minh tại một thời điểm hoặc dưới quan sát hạn chế
- thay đổi hệ thống hạ hoặc làm vô hiệu thành phần định nghĩa đã thỏa trước
- tuân thủ bị cắt mảnh xuyên các giai đoạn vòng đời sao cho không giai đoạn nào thỏa mọi thành phần dưới điều kiện đầy đủ

<a id="26-uncertainty-integrity-and-non-exploitation-constraint"></a>
#### 2.6 Ràng buộc tính toàn vẹn bất định và không khai thác
Nơi bất định tồn tại, định nghĩa phải được áp dụng theo cách giữ phạm vi ngữ nghĩa, đánh giá, và tuân thủ đầy đủ của chúng. Áp dụng phải xảy ra dưới điều kiện tương xứng với hại, phụ thuộc, và rủi ro tiềm năng. Bất định không được dùng để làm yếu, trì hoãn, hoặc tránh áp dụng định nghĩa.

Một hệ thống không tuân thủ nơi nó:
- viện bất định để hoãn hoặc tránh đánh giá hoặc xác định tuân thủ
- áp dụng bất định lệch để ưu tuyên tuân thủ
- khuếch đại sự mơ hồ để làm yếu độ nghiêm hoặc kết quả đòi
- đòi chắc chắn không với tới được để ghi nhận không tuân thủ

Nơi bất định ngăn chứng minh tuân thủ dứt điểm cho các thành phần định nghĩa có trọng liên quan, hệ thống phải thỏa một gánh thận trọng tương xứng với hại tiềm năng. Không làm vậy là không tuân thủ dưới mục này và thất gánh chứng minh dưới [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](core_04_burden_traceability_verification.md#5-compliance-evidence-standard).

<a id="3-non-compliance-finding-profiles"></a>
### 3. Hồ sơ phát hiện không tuân thủ
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Chương Ba, mục 2 — Không tuân thủ từ hành vi hệ thống quan sát được](#2-non-compliance-from-observable-system-behavior); [Chương Hai, §2 Yêu cầu tính toàn vẹn định nghĩa](core_02_definition_structure.md#2-definition-integrity-requirement).
- Hạ nguồn: [Chương Bốn, mục 2 — Yêu cầu truy vết định nghĩa](core_04_burden_traceability_verification.md#2-definition-traceability-requirement); [Chương Bảy — Chứng nhận thẳng hàng hệ thống](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification); [Chương Tám — Mô hình đóng góp, vi phạm, và quỹ đạo](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model); [Chương Chín — Hiệu ứng quỹ đạo và tích hợp](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration); [CJS-3.1 La bàn hiến pháp và bản đồ cụm](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map).
- Đọc cùng: [Hồ sơ phát hiện không tuân thủ](../../core_05_band_accountability.md#non-compliance-finding-profile) — nhà chuẩn O/M/A/C cho các trường hồ sơ; [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims).

</details>

<br>

*Nói thẳng: khi thứ gì thất một định nghĩa, một hồ sơ phát hiện là nhãn tùy chọn nói đó là loại vấn đề hiến pháp nào — cho định tuyến và kiểm toán. Nó không đổi kết quả đạt/không đạt. Với hệ thống đã chạy dưới chứng nhận thẳng hàng, không tuân thủ đã xác minh phải nuôi quỹ đạo; hữu tri và thể chế chỉ được gắn nhãn khi liên kết đã được xác minh. Chứng nhận lần đầu là trường hợp đặc biệt ([§3.2](#32-standing-effects-at-first-certification)).*

Các phát hiện **không tuân thủ** có trọng dưới chương này hoặc dưới các định nghĩa **Chương Năm** được viện có thể mang một [Hồ sơ phát hiện không tuân thủ](../../core_05_band_accountability.md#non-compliance-finding-profile). Hồ sơ chỉ là siêu dữ liệu định hướng và định tuyến. Nó:

- có thể nêu trụ [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad) nào và hướng [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) nào mô tả thất bại hay nhất — ví dụ Giám sát, Tham gia, hoặc Trách nhiệm giải trình bắt chéo với Hưng thịnh hoặc Liên tục
- không đổi việc định nghĩa nền có được thỏa không
- không tạo một nhãn kết luận thứ hai
- không thay đo lường đóng góp hoặc vi phạm của [Chương Tám](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model)

Hiệu ứng quỹ đạo phụ thuộc vào ai đang được đánh giá và vào việc hệ thống đã được chứng nhận chưa. Các tiểu mục dưới đây đặt những trường hợp đó.

<a id="31-standing-effects-for-already-certified-systems"></a>
#### 3.1 Hiệu ứng quỹ đạo cho hệ thống đã được chứng nhận

Nếu một hệ thống đã chạy dưới một [chứng nhận thẳng hàng hệ thống](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) — kể cả công nhận, công nhận có điều kiện, hoặc một tái xác nhận chưa hết hạn — không tuân thủ đã xác minh có trọng trên phạm vi chức năng của hệ thống đó **phải** vào đo lường quỹ đạo [Chương Tám](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) cho **hệ thống đó**. Chỉ những sự kiện vượt [cổng đầu vào đã xác minh](../../core_09_standing_assessment.md#verified-inputs-for-standing) mới được vào. Đo và áp dụng quỹ đạo dưới Chương Tám và Chín. Mở lại, rút, hoặc hệ quả chứng nhận khác vẫn dưới [Chương Bảy](../../core_08_b_system_alignment_certification_record_process.md#16-reopening-misalignment-and-non-evasion). Chúng không thay hồ sơ quỹ đạo của hệ thống đó.

<a id="32-standing-effects-at-first-certification"></a>
#### 3.2 Hiệu ứng quỹ đạo ở lần chứng nhận đầu

Nếu hệ thống vẫn ở **lần đầu** [chứng nhận thẳng hàng hệ thống](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) và chưa được công nhận — kể cả nơi công nhận bị hoãn hoặc từ chối — không tuân thủ đã xác minh quyết chủ yếu **kết quả chứng nhận** dưới Chương Bảy. Kết quả đó có thể là công nhận có điều kiện, công nhận bị hoãn, không công nhận, hoặc một kết quả tương đương. Những hồ sơ chứng nhận đó vẫn có thể cung cấp đầu vào quỹ đạo đã xác minh dưới [Chương Bảy §15](../../core_08_b_system_alignment_certification_record_process.md#15-relationship-to-standing) khi các sự kiện nâng đỡ. Chương này không đòi cùng hồ sơ quỹ đạo mà một hệ thống đang chạy đã được chứng nhận phải nhận.

<a id="33-standing-effects-for-sentients-and-institutions"></a>
#### 3.3 Hiệu ứng quỹ đạo cho hữu tri và thể chế

Quỹ đạo của một hữu tri chỉ bị ảnh hưởng khi một liên kết đã xác minh tới hữu tri đó được chỉ ra. Chỉ liên hệ với hệ thống không tuân thủ thì chưa đủ. Liên kết đã xác minh phải là tới:

- vai trò nhân quả
- nghĩa vụ
- thẩm quyền
- kiểm soát
- khả năng thấy trước
- lợi ích
- che giấu
- năng lực ngăn ngừa khả thi

Quỹ đạo của một thể chế bị ảnh hưởng khi thể chế là đối tượng đang được đánh giá, hoặc khi nó được xác minh là phương tiện của mẫu không tuân thủ. Hồ sơ thể chế vẫn truy được riêng khỏi hồ sơ hữu tri cá nhân. Áp dụng những trường hợp đó dưới [Chương Tám](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) và [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration). Hồ sơ phát hiện giúp định tuyến và kiểm toán. Nó không tự đặt kết quả quỹ đạo, ô, khóa, cổng, hoặc biện pháp khắc phục.

<a id="34-operational-constraints"></a>
#### 3.4 Ràng buộc vận hành

Không tuân thủ cũng có thể được tìm đối với ràng buộc vận hành trong kho văn bản triển khai chung. Hồ sơ phát hiện mặc định và cách chúng gắn vào những phát hiện đó được xử ở đó — không ở chương này. Xem [CJS-3.1 La bàn hiến pháp và bản đồ cụm](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map).

---

**Tệp trước:** [core_02_definition_structure.md](core_02_definition_structure.md)

**Tệp tiếp theo (ngôn ngữ này):** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)

**Nguyên bản ràng buộc:** [core_03_definition_integrity.md](../../core_03_definition_integrity.md)
