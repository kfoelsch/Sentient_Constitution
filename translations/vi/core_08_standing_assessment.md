<a id="chapter-eight-compliance-violation-and-standing-model"></a>
<a id="chapter-eight-contribution-violation-and-standing-model--measurement"></a>
# CHƯƠNG TÁM: MÔ HÌNH ĐÓNG GÓP, VI PHẠM, VÀ QUỸ ĐẠO — ĐO LƯỜNG

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Tám tiếng Anh](../../core_09_standing_assessment.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_08_standing_assessment.md`](../../core_09_standing_assessment.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> Nó giới thiệu ba câu hỏi của chuỗi quỹ đạo, trả lời Câu hỏi 1 (*điều gì đã xảy ra?*), và trả lời Câu hỏi 2 (*tốt hay xấu đến mức nào?*). Câu hỏi 3 (*điều gì xảy ra vì thế?*) tiếp ở [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration), với rà soát chỉ-chỉ định ở [Chương Mười](../../core_11_a_misconduct_designation.md#chapter-eleven-anti-constitutional-misconduct) cho các phát hiện Trục Vi phạm đủ điều kiện `s` = 7–9.

>
> **Trước (ngôn ngữ này):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)
>
> **Tiếp theo (vẫn tiếng Anh):** [core_09_standing_integration.md](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration)
> **Cung đọc:** §1 ba câu hỏi → §2 hồ sơ → §3 xác minh → §4 đo lường → §5 ngữ pháp ô → §6 đầu vào hiến pháp → §7 thang LEQU
</details>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): nơi Chương Tám sống và điều gì ở lại đây</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở chương này hay ở các chương khác.
>
> | Câu hỏi | Chủ sở hữu và vai trò |
> | --- | --- |
> | **1. Điều gì đã xảy ra?** | Lập sự kiện đã xác minh trong một hồ sơ có giới hạn, tranh biện được. |
> | **2. Tốt hay xấu đến mức nào?** | Đo các sự kiện đã xác minh mà không gộp giúp và hại. |
> | **3. Điều gì xảy ra vì thế?** | Tiếp sang [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration). |
>
> Cáo buộc, độ nổi tiếng, và tường thuật tranh chấp không phải câu trả lời cho Câu hỏi 1. Một xếp hạng mong muốn không thể cung cấp sự kiện cho Câu hỏi 1, và một hệ quả mong muốn không thể cung cấp xếp hạng cho Câu hỏi 2.
>
> **Cửa quản trị có trách nhiệm (không vận hành):** Tuyên bố bước tiếp ràng buộc: [Tuyên bố quản trị có trách nhiệm mang tính vận hành](#operative-steward-statement-standing). Con trỏ hỗ trợ trong [`implementation/STEWARD_ENTRY_DOORS.md`](../../implementation/STEWARD_ENTRY_DOORS.md) không thể thu hẹp nó.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [Lời nói đầu §5 Các chuỗi quy trình thực tiễn then chốt](core_00_preamble.md#5-key-practical-process-pipelines) (*chuỗi Chương Bảy đến Mười Một*).
- Thượng nguồn: [Chương Một](core_01_c_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) (*Khả năng tiếp cận ngôn ngữ thường* — quản trị có trách nhiệm phản ánh ở chú giải cấp mục); [Chương Một §9 — Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding) (*nền tảng lớp nguyên tắc cho quỹ đạo truy vết được, gắn năng lực — tin cậy, vai trò, và ghi nhận*); [Chương Hai đến Bốn](core_02_definition_structure.md) (*toàn vẹn, hồ sơ, và xác minh*); [Chương Năm](core_05__definitions_home.md#chapter-five-foundational-definitions) (*định nghĩa và tối thượng đọc cùng Chương Hai đến Bốn*).
- Thượng nguồn: [Chương Bảy](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-system-alignment-certification) (*chứng nhận thẳng hàng hệ thống*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cầu quỹ đạo — chỉ đầu vào đã xác minh tiềm năng*).
- Chuỗi quỹ đạo: [README — Standing pipeline and forums](../../README.md#standing-pipeline-and-forums); [Chương Tám — Đo lường](core_08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model) (*khung ba câu hỏi, hồ sơ Câu hỏi 1, và đo lường Câu hỏi 2 — các mục **1–7***); [Chương Chín — Hiệu ứng quỹ đạo và tích hợp](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*hiệu ứng Câu hỏi 3 và tích hợp*); [Chương Mười](../../core_11_a_misconduct_designation.md#chapter-eleven-anti-constitutional-misconduct) (*chỉ định chỉ cho Trục Vi phạm đủ điều kiện s = 7–9*).
- Tiểu mục trong tệp này: [§1](#1-the-three-questions) (*khung ba câu hỏi và phạm vi*); [§2](#2-standing-records) (*Câu hỏi 1 — sự kiện đã xác minh và hồ sơ*); [§3](#3-standing-record-operational-requirements) (*yêu cầu xác minh và hồ sơ*); [§4](#4-standing-measurement-evaluation-dimensions) (*Câu hỏi 2 — chiều đo lường*); [§5](#5-slot-grammar-and-lequ-calibration) (*ngữ pháp ô và chia tỷ lệ chung*); [§6](#6-constitutional-inputs-to-axis-assignment) (*định tuyến nguồn hiến pháp*); [§7](#7-unified-proportional-lequ-scale) (*thang LEQU tỷ lệ thống nhất cho cả hai trục*).
- Hạ nguồn: [Chương Mười](../../core_11_a_misconduct_designation.md#chapter-eleven-anti-constitutional-misconduct) (*chỉ chỉ định — không mở lại đo lường Câu hỏi 2*); [Chương Mười Một](core_11_forum.md#chapter-eleven-forums-and-jurisdiction) (*giám sát diễn đàn và định tuyến*); [Điều XXIV-C](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) (*giải quyết kịp thời*); [Điều XXIII](core_06_rights_part_d.md#article-xxiii-a-justice-objective-and-scope) (*ràng buộc công lý*).
- Đọc cùng: [Chương Năm *Trạng thái quỹ đạo, đóng góp, và vi phạm*](core_05_band_accountability.md#standing-state-contribution-and-violation-cluster) (*định tuyến định nghĩa chuẩn*).
- Đọc cùng: [README.md](../../README.md) (*thứ tự đọc*); [doc_architecture.md](../../doc_architecture.md) (*bản đồ biên tập không ràng buộc trừ khi được tiếp nhận*).

</details>

<br>

*Nói thẳng: chương này ghi điều gì đã xảy ra và tốt hay hại đến mức nào — trên hai đường riêng, không bao giờ một điểm ròng. Nộp một vụ không phải quỹ đạo tự nó.*

<a id="chapter-eight-part-a-orientation"></a>
Chương Tám là chủ sở hữu của hồ sơ sự kiện đã xác minh cho Câu hỏi 1 và đo lường quỹ đạo cho Câu hỏi 2. Câu hỏi 3 tiếp ở Chương Chín.

<a id="operative-steward-statement-standing"></a>
> **Tuyên bố quản trị có trách nhiệm mang tính vận hành.** **Chủ trì:** Chương Tám (Câu hỏi 1–2: hồ sơ đã xác minh và đo lường). Chương Chín (Câu hỏi 3: hiệu ứng). Các diễn đàn giám sát; chúng không thế đo lường. **Động thái bị cấm:** Đừng coi một hiệu ứng tuyên là quỹ đạo. Đừng chờ một vụ đã nộp. Đừng gộp giúp và hại thành một điểm ròng. Đừng coi nội bộ mô hình hay quyền riêng tư là miễn đo lường quỹ đạo. Đừng coi huy hiệu chứng nhận hay điểm LEQU là trạng thái hữu tri. Đừng xác minh sự kiện hay nhập hồ sơ về thể chế của chính mình, tuyên của chính mình, hoặc tuyên từ đường kiểm soát của mình; định tuyến tới quyền mở hồ sơ đã đặt tên hoặc người xác minh độc lập dưới §3.7. **Đồng hồ:** Đừng chờ một vụ đã nộp. Mở hoặc sửa hồ sơ Chương Tám ngay, qua quyền mở hồ sơ đã đặt tên. Giữ hồ sơ Đóng góp và Vi phạm kiểm được. Ghi nhật ký bộ CS-4 §10.

<a id="1-the-three-questions"></a>

### 1. Ba câu hỏi

*Nói thẳng: quỹ đạo được làm ra bằng cách trả lời ba câu hỏi theo thứ tự. Đừng suy sự kiện từ một xếp hạng mong muốn, và đừng chọn xếp hạng để biện minh một hệ quả mong muốn.*

| Câu hỏi | Câu hỏi hỏi gì | Nơi được trả lời |
| --- | --- | --- |
| **1. Điều gì đã xảy ra?** | Sự kiện nào đã được xác minh, về ai hoặc cái gì, trong khoảng nào, và với trạng thái hồ sơ và tranh biện nào? | [Mục 2](#2-standing-records) |
| **2. Tốt hay xấu đến mức nào?** | Loại và độ lớn đóng góp hoặc vi phạm nào những sự kiện đó lập? | [Mục 4](#4-standing-measurement-evaluation-dimensions) |
| **3. Điều gì xảy ra vì thế?** | Ghi nhận, sẵn sàng, khắc phục, bảo vệ, hạn chế, hay hệ quả khác nào theo sau? | [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) |

Mỗi câu hỏi phụ thuộc câu trả lời trước nó:

- Câu hỏi 1 cung cấp sự kiện đã xác minh cho Câu hỏi 2.
- Câu hỏi 2 đo những sự kiện đó cho Câu hỏi 3.
- Câu hỏi 3 không được viết lại sự kiện hay xếp hạng để khớp một kết quả ưa thích.

Cùng nhau, câu trả lời cho cả ba câu hỏi tạo thành đánh giá quỹ đạo đầy đủ. Hồ sơ quỹ đạo giữ câu trả lời Câu hỏi 1 và 2; quyết định Câu hỏi 3 nêu điều theo sau chúng.

<a id="11-purpose-and-scope"></a>
#### 1.1 Mục đích và phạm vi

Chương này nêu khung hồ sơ và đo lường hiến pháp cho **hệ thống**, **hữu tri**, và **thể chế**, kể cả mọi hệ thống phân hạng dưới [**CS-3**](../../corpus_systems/cs_03_a_system_classification_machinery.md). Những khung này không đo tin đồn, độ nổi tiếng, danh tiếng mơ hồ, phẩm giá vốn có, hay giá trị chung; không cái nào là đối tượng được phép của đánh giá quỹ đạo.

Chuỗi quỹ đạo phải vẫn hiệu lực khi đóng góp đã xác minh trước trở nên quá cũ để hiện năng lực hay độ tin cậy hiện tại, vi phạm còn chưa giải, sửa chữa đắt, trách nhiệm vượt biên, hoặc một tác nhân dùng phân tầng tổ chức hay dán nhãn lại để cản trách nhiệm giải trình.

Thủ tục hàng ngày, bước leo thang, vận hành bồi hoàn và sửa chữa, biện pháp trách nhiệm giải trình phục hồi, và thiết kế khuyến khích thuộc văn bản triển khai đã tiếp nhận.

Đo lường Chương Tám **không**, tự nó, ủy quyền lực, giam giữ, hay hạn chế tự do khác. Mọi hệ quả loại đó phải độc lập thỏa Chương Sáu, **Điều XXIII**, kể cả yêu cầu tính tương xứng, hạn chế nhẹ nhất, có hạn thời gian, bồi hoàn, và trách nhiệm giải trình phục hồi.

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết · Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- Thượng nguồn: [Chương Một §9 — Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding); [Chương Hai đến Bốn](core_02_definition_structure.md); [Chương Năm](core_05__definitions_home.md#chapter-five-foundational-definitions).
- Hạ nguồn: [§2](#2-standing-records) (*Câu hỏi 1*); [§3](#3-standing-record-operational-requirements) (*yêu cầu xác minh và hồ sơ*); [§4](#4-standing-measurement-evaluation-dimensions) (*đo lường Câu hỏi 2*); [§5](#5-slot-grammar-and-lequ-calibration) (*ngữ pháp ô và chia tỷ lệ chung*); [§6](#6-constitutional-inputs-to-axis-assignment) (*định tuyến nguồn hiến pháp*); [§7](#7-unified-proportional-lequ-scale) (*thang LEQU tỷ lệ thống nhất cho cả hai trục*); [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*Câu hỏi 3*).
- [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) · [O](core_05_band_oversight.md#materiality-determination) · [M](core_05_band_oversight.md#materiality-determination-a) · [A](core_05_band_oversight.md#materiality-determination-a) · [C](core_05_band_oversight.md#materiality-determination-c)
- [Hại](core_05_band_accountability.md#harm) · [O](core_05_band_accountability.md#harm) · [M](core_05_band_accountability.md#harm-a) · [A](core_05_band_accountability.md#harm-a) · [C](core_05_band_accountability.md#harm-c)
- [Tính tương xứng](core_05_band_accountability.md#proportionality) · [O](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [A](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)

</details>

<a id="2-standing-records"></a>


<a id="2-question-1--what-happened"></a>
### 2. Câu hỏi 1 — điều gì đã xảy ra?

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§1](#1-the-three-questions) (*khung ba câu hỏi*); [Chương Hai đến Bốn](core_02_definition_structure.md) (*hồ sơ, xác minh, và truy vết định nghĩa tới kết quả*).
- Trụ Tứ diện: **tham gia**; **giám sát** (khả năng tranh biện và đường tranh biện). Mục tiêu sơ cấp: **Hưng thịnh** và **Liên tục** (hồ sơ truy vết được giữ phát hiện đóng góp và vi phạm riêng cho đo lường sau).
- Hạ nguồn: [§2.2](#22-linked-records-and-no-offset-bridge) (*cầu không-bù của hồ sơ liên kết*); [§2.3](#23-question-1-event-type-guide) (*hướng dẫn loại sự kiện*); [§3](#3-standing-record-operational-requirements) (*cổng đầu vào đã xác minh và ranh giới diễn đàn*); [§4](#4-standing-measurement-evaluation-dimensions) (*đo lường Câu hỏi 2*); [§5](#5-slot-grammar-and-lequ-calibration) (*ngữ pháp ô và chia tỷ lệ chung*); [§6](#6-constitutional-inputs-to-axis-assignment) (*định tuyến nguồn hiến pháp*); [§7](#7-unified-proportional-lequ-scale) (*thang LEQU tỷ lệ thống nhất cho cả hai trục*); [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*Câu hỏi 3*).

</details>

<br>

*Nói thẳng: Câu hỏi 1 lập một tường thuật có giới hạn, tranh biện được về điều đã xảy ra. Nó nhận diện đối tượng, sự kiện hoặc mẫu, khoảng thời gian, sự kiện đã xác minh, và trạng thái hồ sơ trước khi xét xếp hạng hay hệ quả nào. Giúp đã xác minh và vi phạm đã xác minh dùng hồ sơ riêng để cái này không xóa cái kia. Những hồ sơ này không phải điểm nổi tiếng hay nhãn mơ hồ.*

<a id="21-standing-records-as-the-unit-of-application"></a>

<a id="21-what-question-1-must-establish"></a>
#### 2.1 Điều Câu hỏi 1 phải lập

Một **hồ sơ quỹ đạo** là hồ sơ có giới hạn chương này dùng cho một đối tượng, phạm vi chức năng, cửa sổ thời gian, trạng thái rà soát, và ngữ cảnh quyết định cụ thể. Trước khi đo lường bắt đầu, nó phải lập:

- hồ sơ liên quan ai hoặc cái gì;
- liệu nó liên quan một sự kiện có giới hạn hay một mẫu đã định;
- khi nào và ở đâu hành vi và hiệu ứng liên quan xảy ra;
- sự kiện nào đã xác minh và sự kiện nào còn tranh;
- bằng chứng, gán, và đường tranh biện nào nâng những phát hiện đó; và
- trạng thái rà soát, sửa, và thay thế hiện tại của hồ sơ.

Câu hỏi 1 dùng một **hồ sơ quỹ đạo đóng góp** cho giúp đã xác minh và một **hồ sơ quỹ đạo vi phạm** cho phát hiện bất lợi đã xác minh. Một hồ sơ không gộp cả hai loại phát hiện.

- Một hồ sơ quỹ đạo có thể liên quan một hữu tri, thể chế, hệ thống, đánh giá, sự kiện có giới hạn, vai trò, tập thể, hồ sơ riêng-tác nhân, hoặc đơn vị hiến pháp liên quan khác. Nó không được sụp các đối tượng, vai trò, hệ thống, cộng đồng, cửa sổ thời gian, trạng thái rà soát, hoặc ngữ cảnh quyết định khác nhau thành một nhãn quỹ đạo không phân biệt.
- Một hồ sơ có thể phủ một **sự kiện có giới hạn** — một tập có đầu và cuối rõ — hoặc một **mẫu** hành vi lặp. Một mẫu đòi đối tượng, phạm vi, và kỳ rà soát đã định.
- Cùng một đối tượng có thể giữ nhiều hồ sơ quỹ đạo theo thời gian, kể cả hồ sơ quỹ đạo đóng góp và vi phạm liên kết. Hồ sơ liên quan phải **tham chiếu chéo** nhau dưới **mục 3.2** nơi chúng chia đối tượng, cửa sổ thời gian chồng, sự kiện có giới hạn, mẫu, hoặc ngữ cảnh quyết định.
- Một hồ sơ quỹ đạo không phải điểm danh tiếng độc lập, hạng phẩm giá, trạng thái vĩnh viễn, nhãn giá trị chung, hay bảng điểm đã gộp. Yêu cầu vận hành nằm ở **mục 3**.

<a id="21-silence-is-the-default"></a>
**Im lặng là mặc định.** Không có hồ sơ quỹ đạo là trạng thái thường của một hữu tri, thể chế, hoặc hệ thống, và là trạng thái hầu hết hữu tri sẽ ở lại.

- Một hồ sơ mở chỉ khi có cò đã xác minh dưới **mục 3**, được nhập bởi quyền mở hồ sơ đã đặt tên dưới **mục 3.7**; nó không bao giờ được mở:
  - để lập một đường cơ sở;
  - để hoàn tất một danh sách; hoặc
  - vì người gác cổng một đường dẫn được đặt tên muốn có một hồ sơ.
- Vắng hồ sơ không nâng suy nào. «Chưa xếp», «chưa xác minh», hoặc «không có hồ sơ» không phải bằng chứng rủi ro, đóng góp thấp, hay bất kỳ điều gì khác, và không được coi là lý do soi kỹ hơn, mặc định thấp hơn, hoặc trạng thái đường dẫn được đặt tên có điều kiện.
- Không thể chế hay hệ thống nào được đòi một hồ sơ quỹ đạo, một chứng nhận «không hồ sơ», hoặc đồng ý mở một hồ sơ như điều kiện của:
  - thiết yếu **Điều III** (*Sinh tồn và lối vào giáo dục bình đẳng*);
  - bảo vệ **Điều III-D** (*Sàn lao động và kinh tế*);
  - thương mại thường; hoặc
  - tham gia như bên bị ảnh hưởng.
  Thanh năng lực đã công bố cho các đường dẫn được đặt tên nhạy-tin cậy cụ thể dưới [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) là ngoại lệ, và chúng phải nêu vì sao đường dẫn được đặt tên đó nhạy-tin cậy.
- Khi một hồ sơ về một đối tượng được mở, đối tượng phải được thông báo dưới **mục 3** trừ khi một chứng minh [Bảo toàn bằng chứng](core_05_band_oversight.md#evidence-preservation) hoặc An toàn có hồ sơ biện minh một hoãn có hạn thời gian; một hồ sơ đối tượng không thể biết thì không tranh biện được.

Mọi hiệu ứng quỹ đạo sau thuộc Chương Chín và phải truy được về hồ sơ quỹ đạo liên quan mà không trở thành phần của chính hồ sơ.

<a id="22-linked-records-and-no-offset-bridge"></a>

#### 2.2 Hồ sơ liên kết và cầu không-bù

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§2.1](#21-standing-records-as-the-unit-of-application) (*hồ sơ đóng góp và vi phạm riêng*).
- Hạ nguồn: [§3.1](#31-minimum-record-contents) (*cổng đầu vào đã xác minh*); [§3.2](#32-related-record-cross-references) (*tham chiếu chéo*); [§3.6](#36-forum-boundary) (*ranh giới diễn đàn*); [§4](#4-standing-measurement-evaluation-dimensions) (*đo lường Câu hỏi 2*); [§5](#5-slot-grammar-and-lequ-calibration) (*ngữ pháp ô và chia tỷ lệ chung*); [§6](#6-constitutional-inputs-to-axis-assignment) (*định tuyến nguồn hiến pháp*); [§7](#7-unified-proportional-lequ-scale) (*thang LEQU tỷ lệ thống nhất cho cả hai trục*); [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*Câu hỏi 3*).
- Đọc cùng: [Chương Chín — Tích hợp quỹ đạo](../../core_10_standing_integration.md#2-automatic-integration-review-and-continuity) (*không-miễn và tích hợp hồ sơ liên kết*); [Chương Chín §6.2 — Thanh năng lực và giấy phép](../../core_10_standing_integration.md#62-competency-bars-and-clearances); [Chương Chín §4.2 — Khóa quỹ đạo](../../core_10_standing_integration.md#42-prevention--general-standing-locks).

</details>

<br>


**Quy tắc cốt:** **hồ sơ quỹ đạo đóng góp** đã xác minh và **hồ sơ quỹ đạo vi phạm** đã xác minh được giữ riêng dưới **mục 2.1**. Mỗi phát hiện đóng góp hoặc vi phạm phải tựa trên sự kiện riêng đã nâng trong hồ sơ riêng của nó. Phân tích và tư liệu nâng phải giữ hai đường hồ sơ truy vết riêng. Không một mục hay bộ liên kết nào là điểm ròng, điểm hòa, hay đánh đổi.

- **Hồ sơ quỹ đạo vi phạm và khóa quỹ đạo:**
  - Dưới Chương Chín, **khóa quỹ đạo** áp dụng rút từ hồ sơ quỹ đạo vi phạm có thể hạn quỹ đạo, hạn đủ điều kiện vai trò, hoặc ảnh hưởng lối vào khắc phục trong khi một vi phạm đã xác minh còn chưa giải.
  - Khóa quỹ đạo không được xóa đóng góp dương đã xác minh ghi trong hồ sơ quỹ đạo đóng góp.
  - Vi phạm đã xác minh chưa giải không bị chiết khấu thời gian chỉ vì thời gian trôi.
  - Vi phạm đã xác minh không được viết lại hồ sơ quỹ đạo đóng góp không liên quan thành một tệp danh tiếng âm giả.
- **Hồ sơ quỹ đạo đóng góp và giấy phép năng lực:**
  - Đóng góp đã xác minh có thể nâng **giấy phép năng lực** áp dụng đối với **thanh năng lực** đã công bố và nâng đủ điều kiện gắn tin cậy, vai trò, hoặc ghi nhận nơi còn hiện và liên quan vai trò.
  - Đóng góp đã xác minh không được bù, trung bình xuống, bào chữa, hay dán nhãn lại một phát hiện vi phạm đã xác minh.
  - Thỏa cổng không miễn khóa quỹ đạo áp dụng nào.

**Ngoại lệ duy nhất:** Nếu một phát hiện vi phạm tự bác một đóng góp đã tuyên — ví dụ, nếu bằng chứng cho thấy bạn không thực sự làm điều hồ sơ đóng góp tuyên — thì hồ sơ quỹ đạo đóng góp liên kết có thể được sửa hoặc gỡ qua quy trình bằng chứng và rà soát đúng, với tham chiếu chéo đòi dưới **mục 3.2**. Nhưng vi phạm không tự xóa việc tốt không liên quan ghi trong hồ sơ quỹ đạo đóng góp riêng.

<a id="23-question-1-event-type-guide"></a>

<a id="23-question-1-event-type-guide--what-kind-of-help-or-harm-occurred"></a>
#### 2.3 Hướng dẫn loại sự kiện Câu hỏi 1 — loại giúp hoặc hại nào đã xảy ra?

*Nói thẳng: dùng các bảng này để mô tả điều đã xảy ra sau khi sự kiện được xác minh. Chúng giúp nhận diện loại đóng góp hoặc vi phạm liên quan. Chúng không quyết tốt hay xấu đến mức nào, gán ô, hay xác định điều xảy ra vì thế.*

<a id="231-contribution-event-types"></a>

##### 2.3.1 Loại sự kiện đóng góp

**Quy tắc đủ điều kiện:** Một đóng góp tuyên chỉ được tính khi nó truy vết được, không bị ngoại hóa, và nhất quán với Hiến pháp vận hành như một toàn thể.

- Hại đã ngoại hóa, phụ thuộc cưỡng, thu hẹp Sàn Quyền, hoặc gánh che có thể loại hoặc hạn đóng góp đã tuyên.
- Một đóng góp tuyên không bù một phát hiện vi phạm riêng.

Mỗi hàng trong bảng dưới đặt tên một đường thường của giúp đã xác minh và liên quan hiến pháp của nó. Nhiều hơn một hàng có thể áp cho cùng hồ sơ.

| Loại đóng góp đã xác minh | Điều đã xảy ra | Trụ Tứ diện | Mục tiêu sơ cấp |
| --- | --- | --- | --- |
| Sinh tồn và duy trì thân thể | Ai đó nhận thức ăn, chỗ ở, chăm sóc y tế, hoặc an toàn | **Tham gia**, **Giám sát** | **Hưng thịnh** |
| Chăm sóc và dạy | Trẻ được nuôi, người già được chăm, hoặc người khác được giáo dục | **Tham gia**, **Giám sát** | **Hưng thịnh**, **Liên tục** |
| Giải chấn thương | Ai đó nhận giúp phục hồi khỏi hại tâm lý đã chặn phúc lợi | **Tham gia**, **Trách nhiệm giải trình** | **Hưng thịnh** |
| Gỡ gánh nặng | Nợ đè, điều kiện làm việc bóc lột, hoặc rào hệ thống được gỡ | **Tham gia**, **Giám sát** | **Hưng thịnh** |
| Khôi quyền năng | Ai đó có lựa chọn có nghĩa về đời mình | **Tham gia** | **Hưng thịnh** |
| Mở năng lực sản xuất | Công cụ, hạ tầng, hoặc cơ hội cho người khác hưng thịnh độc lập | **Tham gia**, **Giám sát** | **Hưng thịnh**, **Liên tục** |
| Cải hiệu thời gian | Chờ tránh được, ma sát hành chính, hoặc chi phí phối hợp được giảm, trả lại thời gian dùng được cho chăm sóc, nghỉ, quyền năng, học, hoặc việc khớp quyền | **Tham gia**, **Giám sát** | **Hưng thịnh** |
| Giảm rủi ro sinh thái hoặc hạ tầng | Sụp môi trường hoặc thất hệ thống then chốt được ngăn | **Giám sát**, **Trách nhiệm giải trình** | **Liên tục**, **Hưng thịnh** |
| Củng an toàn, sự thật, khả năng kiểm toán, hoặc năng lực tranh biện | Thể chế hoặc thực hành được xây hoặc sửa để bảo quyền và giữ quyền lực phải trả lời | **Tham gia**, **Giám sát**, **Trách nhiệm giải trình** | **Hưng thịnh**, **Liên tục** |

<a id="232-violation-event-types"></a>

##### 2.3.2 Loại sự kiện vi phạm

**Quy tắc đủ điều kiện:** Một loại sự kiện vi phạm đòi một phát hiện đã xác minh vẫn truy vết được, có giới hạn, kiểm toán được, và tranh biện được dưới **Chương Hai đến Bốn**.

- Cáo buộc, thẻ tạm, tường thuật diễn đàn, và nhãn tiếp nhận có thể nâng định tuyến hoặc phân loại, nhưng chúng không hoàn tất Câu hỏi 1.
- Đóng góp dương không bù, bào chữa, chữa, hay dán nhãn lại một vi phạm đã xác minh.

Mỗi hàng trong bảng dưới đặt tên một đường thường của mất, nguy, hoặc thất bổn phận đã xác minh và liên quan hiến pháp của nó. Nhiều hơn một hàng có thể áp cho cùng hồ sơ.

| Loại mất hoặc nguy đã xác minh | Điều đã xảy ra | Trụ Tứ diện | Mục tiêu sơ cấp |
| --- | --- | --- | --- |
| Tước sinh tồn hoặc duy trì thân thể | Chết tránh được, từ chối chăm sóc, điều kiện không an toàn, hoặc tước sinh tồn có trọng đã xảy ra | **Trách nhiệm giải trình**, **Tham gia** | **Hưng thịnh** |
| Gánh nặng tránh được nghiêm | Gánh đè, áp, hoặc chuyển hệ thống đã làm suy phúc lợi hoặc quyền năng có trọng | **Trách nhiệm giải trình**, **Tham gia** | **Hưng thịnh** |
| Mất quyền năng cưỡng | Cưỡng, thao túng, đe dọa đáng tin, giam, hoặc nguy tự do đã xảy ra | **Trách nhiệm giải trình**, **Tham gia** | **Hưng thịnh** |
| Đánh bại Sàn Quyền | Sàn hiến pháp không thương lượng, tối thượng, hoặc lối vào tranh biện-và-khắc phục bị vi phạm có trọng | **Trách nhiệm giải trình**, **Giám sát** | **Hưng thịnh**, **Liên tục** |
| Hại sinh thái hoặc hạ tầng | Điều kiện cần cho phúc lợi hiến pháp bị hại | **Trách nhiệm giải trình**, **Giám sát** | **Liên tục**, **Hưng thịnh** |
| Phá năng lực sản xuất | Công cụ, năng lực, quan hệ, hoặc tài nguyên cần để hưng thịnh độc lập bị đóng cửa | **Trách nhiệm giải trình** | **Hưng thịnh** |
| Suy An toàn, Sự thật, hoặc khả năng kiểm toán | Che giấu, thông tin sai, hồ sơ gãy, đường tranh biện không vào được, hoặc gộp không rà soát được đã xảy ra | **Giám sát**, **Trách nhiệm giải trình** | **Hưng thịnh**, **Liên tục** |
| Cản trở trách nhiệm giải trình | Can thiệp đã xác minh vào máy phải-trả-lời — toàn vẹn bằng chứng, xác minh, quy trình diễn đàn, hồ sơ quỹ đạo, đồng hồ khắc phục, hoặc đường tranh biện và khắc phục — đã xảy ra; nơi cản là một siêu-tấn công lên một hại nền riêng, mở một hồ sơ quỹ đạo vi phạm liên kết riêng | **Trách nhiệm giải trình**, **Giám sát**, **Kịp thời** | **Hưng thịnh**, **Liên tục** |
| Chiếm hệ thống hoặc lạm phụ thuộc | Mở đường cấu trúc, lạm bất đối xứng phụ thuộc, thiết kế chống lẩn tránh, hoặc chiếm các đường dẫn trách nhiệm giải trình đã xảy ra | **Trách nhiệm giải trình**, **Tham gia** | **Liên tục**, **Hưng thịnh** |

<a id="3-standing-record-operational-requirements"></a>

<a id="3-verification-and-record-requirements"></a>

### 3. Yêu cầu xác minh và hồ sơ

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§2](#2-standing-records) (*hồ sơ Câu hỏi 1 và hướng dẫn loại sự kiện*); [Chương Hai đến Bốn](core_02_definition_structure.md) (*hồ sơ, xác minh, và truy vết định nghĩa tới kết quả*).
- Hạ nguồn: [§3.1](#31-minimum-record-contents) (*nội dung tối thiểu và cổng đầu vào đã xác minh*); [§3.2](#32-related-record-cross-references) (*tham chiếu chéo*); [§3.6](#36-forum-boundary) (*ranh giới diễn đàn*); [§3.7](#37-record-custody-and-opening-authority) (*lưu giữ hồ sơ và quyền mở*); [§4](#4-standing-measurement-evaluation-dimensions) (*Câu hỏi 2*).

</details>

<br>

*Nói thẳng: Mục này nêu mỗi hồ sơ quỹ đạo phải chứa gì, ai được mở và giữ nó, và cách nó có thể bị tranh biện hoặc sửa. Đo lường Câu hỏi 2 chỉ được thêm sau khi cơ sở sự kiện đã xác minh được ghi.*

Chi tiết bằng chứng và hồ sơ đòi có thể tăng theo lợi hại vật chất và lớp hệ thống. Việc chia tỷ lệ này không loại hữu tri, thể chế, hoặc hệ thống nào được phủ khỏi chuỗi quỹ đạo.

<a id="31-minimum-record-contents"></a>

#### 3.1 Nội dung hồ sơ tối thiểu


Mọi hồ sơ quỹ đạo phải gồm, tối thiểu:

- loại hồ sơ — **hồ sơ quỹ đạo đóng góp** hoặc **hồ sơ quỹ đạo vi phạm**;
- ai hoặc cái gì đang được đánh giá và phạm vi đánh giá, kể cả ranh giới hệ thống liên quan, ranh giới vai trò, cộng đồng bị ảnh hưởng, và quan hệ phụ thuộc;
- hành vi hoặc phát hiện nào đang được đánh giá, kể cả hành động, bỏ sót, bổn phận, tác động, sự kiện có giới hạn, mẫu trong phạm vi, hồ sơ đóng góp, hoặc phát hiện vi phạm hồ sơ tựa vào;
- cửa sổ thời gian và trạng thái rà soát hiện tại — ví dụ, tạm, cuối cho một mục đích đã nêu, đang tranh biện, đã thay, hoặc đến hạn tái đánh giá theo lịch;
- mọi hồ sơ quỹ đạo liên quan được tham chiếu chéo như đòi dưới **mục 3.2**;
- hồ sơ, nhân chứng, đo lường, kiểm toán, quyết định diễn đàn, hoặc tư liệu xác minh khác làm hồ sơ quỹ đạo chứng minh được, rà soát được, và tranh biện được dưới Chương Hai đến Bốn;
- **quyền mở hồ sơ** đã xác minh cơ sở sự kiện và nhập hồ sơ, và **người lưu giữ hồ sơ** giữ nó, mỗi cái được đặt tên dưới **mục 3.7**;
- cách tranh biện hồ sơ, kể cả:
  - diễn đàn hoặc quyền nào rà soát nó;
  - giới hạn công bố nào; và
  - điều kiện cho:
    - sửa;
    - khôi;
    - hết hạn; hoặc
    - rà soát theo lịch;
- các trường đo lường Câu hỏi 2 riêng-trục đòi dưới đây, một khi đo lường xảy ra.

**Hành động gán kiểm được.** Với nhân sự/tác nhân thực hiện Quản trị có trách nhiệm Hệ thống Then chốt hoặc thẩm quyền vận hành có trọng, bằng chứng hành động-gán tái lập được được nêu ở **[CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action)** như hợp đồng nhật ký mặc định cho kíp hỗn. Bằng chứng đó có thể nuôi hồ sơ này. Nó không thế hồ sơ này. Trọng số mô hình và deliber nội bộ không phải nội dung hồ sơ quỹ đạo trừ khi chúng là đường gán còn lại duy nhất. Bảo vệ riêng tư và trạng thái nội bộ không tạo miễn đo lường quỹ đạo.

**Ranh giới giai đoạn.** Câu hỏi 1 ghi sự kiện đã xác minh; Câu hỏi 2 đo chúng. Một hồ sơ có thể mở một khi cơ sở sự kiện đã xác minh đầy dù đo lường Câu hỏi 2 còn treo. Cho đến khi đo lường xảy ra, các trường Câu hỏi 2 phải nói chúng đang treo chứ không hàm một ô hay hạng. Hồ sơ không được nêu hoặc áp một **hiệu ứng quỹ đạo** Câu hỏi 3.

<a id="verified-inputs-for-standing"></a>

**Cổng đầu vào đã xác minh.** Mọi quyết định ảnh hưởng quỹ đạo, tin cậy, vai trò, ghi nhận, hoặc đủ điều kiện ghi nhận chỉ được dùng đầu vào đã xác minh từ **hồ sơ quỹ đạo đóng góp** hoặc **hồ sơ quỹ đạo vi phạm** liên quan. Cáo buộc, tuyên chưa phân xử, thẻ định tuyến tạm, tường thuật chỉ-tiếp-nhận, và tư liệu giai đoạn-tranh khác không tự cung cấp bản chất đóng góp hay bản chất vi phạm cho quỹ đạo.

**Hồ sơ quỹ đạo đóng góp** cũng phải nêu:

- đo lường đóng góp Câu hỏi 2, kể cả:
  - dải sơ cấp;
  - ô `s` nơi được gán;
  - cơ sở bằng chứng;
  - lý do tính trọng yếu; và
  - mọi hiệu chỉnh LEQU hoặc tương đương đã tiếp nhận dùng cho nâng trong suốt;
- nơi đóng góp được chia, tín dụng được phân thế nào, kể cả xét:
  - thời gian;
  - nỗ lực;
  - phối hợp;
  - bảo trì;
  - đóng góp nhân quả; và
  - việc hỗ trợ ít thấy;
- cơ sở đo lường đóng góp mà mọi hiệu ứng quỹ đạo Chương Chín sau phải dùng.

**Hồ sơ quỹ đạo vi phạm** cũng phải nêu:

- đo lường vi phạm Câu hỏi 2, kể cả:
  - quyền phát hiện hoặc cơ sở hồ sơ;
  - tác động LEQU;
  - ô `s` nơi được gán;
  - tính chất quy trình / đáp nơi áp dụng; và
  - mọi trạng thái chỉ định Chương Mười;
- nơi vi phạm được chia hoặc phân tán, cơ sở đã xác minh cho mọi quỹ đạo bất lợi riêng-tác nhân, kể cả:
  - vai trò nhân quả;
  - bổn phận;
  - thẩm quyền;
  - kiểm soát;
  - khả năng thấy trước;
  - lợi;
  - che giấu; hoặc
  - năng lực ngăn khả thi;
- nơi phát hiện vi phạm liên quan bỏ sót công bố diễn đàn hoặc thất quy trình rút cố ý (đọc **§4.2** cho kỷ luật đo lường):
  - cơ sở đã xác minh cho bỏ sót hoặc thất;
  - bổn phận công bố hoặc rút chưa thỏa;
  - hiểu biết, liều, hoặc ý định của tác nhân nơi được tìm; và
  - liệu hành vi có ảnh hưởng có trọng:
    - tính hợp pháp của ban;
    - độc lập;
    - tranh biện rút;
    - toàn vẹn bằng chứng;
    - thời điểm khắc phục;
    - định tuyến dự phòng; hoặc
    - khả năng tranh biện thực tiễn;
- cơ sở đo lường vi phạm mà mọi hiệu ứng quỹ đạo Chương Chín sau phải dùng.

<a id="32-related-record-cross-references"></a>

#### 3.2 Tham chiếu chéo hồ sơ liên quan


Khi một hồ sơ quỹ đạo đóng góp và một hồ sơ quỹ đạo vi phạm liên quan cùng đối tượng, cửa sổ thời gian chồng, sự kiện có giới hạn, mẫu, hoặc ngữ cảnh quyết định, mỗi cái phải trỏ tới cái kia.

Mỗi tham chiếu chéo phải nhận diện, tối thiểu:

- hồ sơ liên quan và liệu nó là đóng góp hay vi phạm;
- đối tượng, sự kiện có giới hạn, mẫu, hoặc ngữ cảnh quyết định chung;
- cửa sổ thời gian hoặc phạm vi chồng thế nào; và
- vì sao hồ sơ được liên kết, kể cả nơi một phát hiện vi phạm bác, sửa, hoặc hạn một đóng góp tuyên dưới **mục 2.2**.

Tham chiếu chéo phải vẫn kiểm toán được và mở cho tranh biện. Chúng không được thế đo lường riêng, tạo điểm gộp, hoặc che phạm vi lệch giữa hồ sơ.

<a id="33-collective-and-actor-specific-records"></a>

#### 3.3 Hồ sơ tập thể và riêng-tác nhân


Khi nhiều hữu tri hoặc thực thể chia cùng lợi hoặc vi phạm, hệ thống có thể giữ cả hồ sơ quỹ đạo tập thể và hồ sơ riêng-tác nhân. Phát hiện đóng góp và vi phạm phải ở lại hồ sơ riêng dưới **mục 2.1**.

Với tín dụng chung, ghi nhận nên theo điều mỗi hữu tri thực sự đóng góp — vai trò, thời gian, nỗ lực, rủi ro, kỹ năng, phối hợp, bảo trì, và tác động nhân quả. Khi nhiều hữu tri giúp và phần cá nhân không tách sạch được, phân phối rộng được ưa.

Với vi phạm chung, trách không được gán chỉ vì thành viên nhóm. Quỹ đạo bất lợi riêng-tác nhân đòi liên kết đã xác minh tới vai trò nhân quả, bổn phận, thẩm quyền, kiểm soát, khả năng thấy trước, lợi, che giấu, hoặc năng lực ngăn khả thi.

<a id="34-versioning"></a>

#### 3.4 Phiên bản


Hồ sơ quỹ đạo phải được đánh phiên khi sự kiện, phát hiện, kết quả rà soát, trạng thái sửa, bằng chứng đóng góp, hiệu chỉnh triển khai, hoặc quy tắc hiến pháp quan trọng đổi. Một phiên sau có thể:

- cập nhật hồ sơ về phía trước;
- sửa nó hồi tố nơi nó sai;
- hết hạn nó cho một ngữ cảnh quyết định đã xong; hoặc
- thay nó cho một ngữ cảnh quyết định mới.

Phiên sau phải giữ dấu vết kiểm toán trước và giải thích điều đổi, ai đổi, dưới quyền mở hoặc lưu giữ nào dưới **mục 3.7**, trên tư liệu xác minh nào, và theo yêu cầu của ai.

<a id="35-implementation-tools"></a>

#### 3.5 Công cụ triển khai

Đội có thể xây công cụ thực tiễn cho hồ sơ quỹ đạo — trường dữ liệu, thẻ, ngưỡng, mẫu, bảng điều khiển, và bước rà soát, kể cả **thước đóng góp chuẩn** đã công bố cho việc lặp dưới **mục 5.1**. Những công cụ đó phải giữ các trường đòi bởi **mục 3.1** thấy riêng và tranh biện được. Chúng không được chôn những trường đó trong một điểm mờ hay nhãn ẩn.

<a id="36-forum-boundary"></a>

#### 3.6 Ranh giới diễn đàn


*Nói thẳng: diễn đàn là nơi tranh chấp được giám sát, tranh biện, và biến thành kết quả đã xác minh — nhưng nộp một vụ hoặc thắng một trận tường thuật không cập nhật quỹ đạo. Cổng đầu vào đã xác minh ở **mục 3.1** vẫn áp. Khi một diễn đàn xác minh sự kiện dưới Chương Hai đến Bốn, nó có thể **mở, cập nhật, hoặc sửa** một hồ sơ quỹ đạo — hoặc **gạt một hồ sơ xấu sang một bên khi tranh biện**. Diễn đàn không gộp tốt và xấu thành một điểm hay tự bịa hạng quỹ đạo.*

Họ diễn đàn dưới [Chương Mười Một](core_11_forum.md#chapter-eleven-forums-and-jurisdiction) **giám sát** cách tranh chấp cụ thể đi qua chuỗi quỹ đạo. Tệp giai đoạn-tranh một diễn đàn giữ cho giám sát đó là [**hồ sơ vụ diễn đàn**](core_05_band_accountability.md#forum-case-record) dưới [Chương Mười Một §2.3](core_11_forum.md#23-forum-records-standing-records-and-contests); nó **không** tự là hồ sơ quỹ đạo. Diễn đàn cung cấp tranh biện vào được, rà soát độc lập, hỗ trợ pháp y, trình tự sửa, và đồng hồ mặc định-bậc dưới [Chương Mười Một §6](core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) và [Điều XXIV-C](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) (*Sàn Giải quyết kịp thời và Chống trì hoãn*), và khi những phát hiện đó thỏa cổng đầu vào đã xác minh dưới Chương Hai đến Bốn chúng có thể **mở, cập nhật, hoặc sửa** hồ sơ quỹ đạo dưới **mục 3.1** — hoặc **gạt một hồ sơ xấu sang một bên khi tranh biện**.

Phát hiện sự kiện đã xác minh của một diễn đàn có thể cung cấp cơ sở sự kiện cho một hồ sơ quỹ đạo Câu hỏi 1. Chúng **không** xác định đo lường Câu hỏi 2 về đóng góp hoặc vi phạm đã xác minh tốt hay xấu đến mức nào. Theo đó:

- Thủ tục diễn đàn **không** được gộp tư liệu đóng góp và vi phạm thành một điểm ròng, câu trả lời công trạng hòa, hoặc nhãn quỹ đạo không phân biệt; hồ sơ liên kết vẫn riêng dưới **mục 2.1** và **2.2**.
- Đầu ra diễn đàn **không** được thế tường thuật tranh chấp, tiện định tuyến, hoặc ưa thích của ban cho đầu vào đã xác minh chứng minh được, đo lường riêng, hoặc cơ chế hiệu ứng quỹ đạo thuộc [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration).

Ranh giới này **không** giảm tranh biện, khắc phục, cứu trợ tạm, hoặc bảo vệ thủ tục đòi dưới [Điều XII-B](core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*Quyền tranh biện, rà soát, và khắc phục*), [Chương Mười Một §6](core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline), [Điều XXIV-C](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) (*Sàn Giải quyết kịp thời và Chống trì hoãn*), hoặc các điều công lý liên quan. Nó đòi phát hiện diễn đàn đã xác minh vào quỹ đạo qua cùng cổng như đầu vào đã xác minh khác — không vòng quanh nó.

<a id="37-record-custody-and-opening-authority"></a>

#### 3.7 Lưu giữ hồ sơ và quyền mở

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Chương Một §10.2 *Phân tách nhiệm vụ*](core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties) (*sàn lớp nguyên tắc mục này áp cho hồ sơ quỹ đạo; không được thu hẹp ở đây*); [Chương Một §11.3 *Phát hiện và rà soát số nhiều*](core_01_c_stewardship_capacity_principles.md#113-misalignment-detection); [§2.1](#21-silence-is-the-default) (*cò đã xác minh; thông báo đối tượng*); [§3.1](#31-minimum-record-contents) (*nội dung tối thiểu và cổng đầu vào đã xác minh*); [§3.4](#34-versioning) (*phiên bản*); [§3.6](#36-forum-boundary) (*diễn đàn có thể mở, cập nhật, sửa, hoặc gạt sang một bên*); [Chương Hai đến Bốn](core_02_definition_structure.md) (*hồ sơ, xác minh, và truy vết*); [Bảo toàn bằng chứng](core_05_band_oversight.md#evidence-preservation) (*chuỗi lưu giữ bằng chứng*).
- Trụ Tứ diện: **trách nhiệm giải trình** (một tác nhân đã đặt tên trả lời cho mọi mục); **giám sát** (không bên nào xác minh tuyên của chính mình). Mục tiêu sơ cấp: **Hưng thịnh** và **Liên tục**.
- Đọc cùng: [Chương Năm *Điều lệ*](core_05_band_continuity.md#charter) (*văn kiện phạm vi đã công bố đặt tên hoặc trỏ tới quyền mở hồ sơ và người lưu giữ cho một phạm vi đã điều lệ*); **CI-3.6** (*nội dung Điều lệ — trường lưu giữ hồ sơ quỹ đạo*); [**CJS-3.11** *Làn hiến pháp và tách chức năng*](../../corpus_joint_structure/cjs_03a_accountability_operations.md#constitutional-lane-and-functional-separation) (*năm làn nhiệm vụ hồ sơ được đặt vào; phân tách nhiệm vụ*); **CI-3.2** (*Làn tách chức năng — bản đồ làn đã công bố, dự phòng khi Điều lệ im*); **CI-3.3** (*chuỗi thẩm quyền và kiểm ủy*); **CI-4.6** (*Mục lục ghế — bốn ghế hồ sơ như loại ghế 1–4, với quy tắc ghế sai*); **CF-9.6** (*không tự điều tra*) và **CF-9.8** (*bàn giao phát hiện đã xác minh*); [Chương Mười Một §2.1](core_11_forum.md#21-lead-default-limits) (*dự phòng chống tự xét*); [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) (*ai ủy; nhật ký không phải hồ sơ*); [Chương Chín §5.4](../../core_10_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) (*dừng, từ chối, ghi, leo thang*); [Chương Bốn §5](core_04_burden_traceability_verification.md#5-compliance-evidence-standard) (*chuẩn bằng chứng ghế xác minh áp cho tuyên người ghi và bên*); [Thiện chí](core_05_band_accountability.md#good-faith) (*giả định thẳng thắn, không phải đúng*); [Khả năng tranh biện](core_05_band_accountability.md#contestability) và [Điều XII-B](core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*một tranh biện nêu trên hồ sơ được ghi và định tuyến trước mọi nộp*); [Chương Mười Một §2.3](core_11_forum.md#23-forum-records-standing-records-and-contests) (*tranh biện hồ sơ quỹ đạo một khi chúng tới diễn đàn*).
- Hạ nguồn: [§4](#4-standing-measurement-evaluation-dimensions) (*Câu hỏi 2 chỉ đo hồ sơ nhập dưới mục này*); [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*hiệu ứng Câu hỏi 3 truy về một hồ sơ đã gán*).

</details>

<br>

*Nói thẳng: bốn việc khác nhau chạm một hồ sơ quỹ đạo — xin đổi, xác minh sự kiện, viết và giữ hồ sơ, và nghe tranh biện — và không một văn phòng nào làm hai việc đó trên cùng hồ sơ. Mọi hồ sơ đặt tên văn phòng đã xác minh nó và văn phòng giữ nó. Không cái nào được là đối tượng của hồ sơ, bên tuyên giúp, bên cáo hại, hoặc ai những bên đó kiểm. Một người quản trị có trách nhiệm bên trong người vận hành có thể dừng hành động, ghi nhật ký, bảo toàn bằng chứng, và leo thang — nhưng không thể xác minh sự kiện và viết hồ sơ về thể chế của chính mình. Nếu Điều lệ quên nói ai xác minh, bản đồ làn đã công bố của thể chế đã trả lời: làn bảo đảm, không bao giờ văn phòng chạy hệ thống hoặc giữ kho. Hữu tri đã mở hồ sơ trước là nhân chứng về nó sau, không phải thẩm phán của nó — được tin là thẳng thắn, nhưng đúng hay sai được chứng bởi nhật ký, không bởi lời họ. Nếu người lưu giữ là người xung đột, hồ sơ đó chuyển sang người giữ thay; kho thì không. Một tranh chấp nêu trên hồ sơ được ghi và định tuyến ngày nó tới; nó không chờ một lần nộp. Mọi đổi đặt tên ai làm và dưới quyền nào. Không điều nào trong này là lý do để chờ.*

<a id="37-segregation-of-duties"></a>

**Phân tách nhiệm vụ.** Điều này áp [Chương Một §10.2 *Phân tách nhiệm vụ*](core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties) cho hồ sơ quỹ đạo. Bốn nhiệm vụ chạm mọi hồ sơ quỹ đạo, và mỗi cái là một ghế riêng trên cùng hồ sơ:

| Nhiệm vụ | Nó là gì | Làn dưới [CJS-3.11 *Làn hiến pháp và tách chức năng*](../../corpus_joint_structure/cjs_03a_accountability_operations.md#constitutional-lane-and-functional-separation) |
| --- | --- | --- |
| **Xin** | xin một hồ sơ được mở, sửa, hết hạn, hoặc thay, kể cả xin của chính đối tượng hoặc bên tuyên | thực thi (hoặc bên xin, người không giữ ghế) |
| **Xác minh** | lập cơ sở sự kiện dưới Chương Hai đến Bốn tới cổng **mục 3.1** — hành động của quyền mở hồ sơ | bảo đảm và kiểm toán |
| **Nhập và giữ** | viết phiên dưới **mục 3.4**, giữ hồ sơ, công bố đường tranh biện — hành động của người lưu giữ hồ sơ | công bố và bằng chứng |
| **Tranh biện** | nghe tranh biện hồ sơ và gạt sang một bên, sửa, hoặc xác nhận nó dưới **mục 3.6** | tranh biện và rà soát |

Không văn phòng nào giữ hai ghế này trên cùng hồ sơ trừ khi thể chế đã công bố một bảo vệ chủ-gộp cho cặp đó dưới **CJS-3.11** (*Trách nhiệm giải trình: thuật ngữ thẩm quyền phân tán và tỷ lệ*) và **CI-3.2** (*Làn tách chức năng*) kiểm toán được và tranh biện được, và **không văn phòng nào vừa xác minh vừa nhập** cùng hồ sơ, hoặc vừa xác minh vừa nghe tranh biện của nó. Văn phòng chạy hệ thống một hồ sơ liên quan giữ làn thực thi cho hệ thống đó và vì thế không bao giờ xác minh hồ sơ về nó. Chủ gộp dưới một bảo vệ đã công bố là ngoại lệ chia tỷ lệ theo lớp cho bên tiếp nhận nhỏ, không phải mặc định; nơi lợi hại vật chất hoặc lớp hệ thống cao, ghế là văn phòng riêng.

<a id="37-lane-map-fallback"></a>

**Dự phòng khi Điều lệ im.** Nơi một Điều lệ thất đặt tên quyền mở hồ sơ hoặc người lưu giữ cho một phạm vi, im lặng đó là khuyết Điều lệ dưới **CI-3.6** (*Nội dung, rà soát, và mẫu hình thành Điều lệ*) để ghi và sửa — và không phải lý do hồ sơ không thể chạy. Bản đồ làn đã công bố của thể chế dưới **CI-3.2** (*Làn tách chức năng*) quản trị trong lúc đó: quyền mở hồ sơ là văn phòng giữ làn bảo đảm và kiểm toán cho phạm vi đó, người lưu giữ là văn phòng giữ làn công bố và bằng chứng, và không cái nào được là văn phòng giữ làn thực thi cho hệ thống liên quan. Nơi cũng không có bản đồ làn, hồ sơ định tuyến tới xác minh độc lập dưới *Không tự lưu giữ* dưới đây — hoặc, với hồ sơ không chính thức và phạm vi nhỏ, tới thân dựa vào dưới *Hồ sơ không chính thức và phạm vi nhỏ* kế. Một người quản trị có trách nhiệm được xin ngồi một ghế bản đồ làn không cho họ từ chối ghế, ghi yêu cầu và khoảng trống, và định tuyến; họ không nhập hồ sơ vì họ có thể.

<a id="37-informal-and-small-scope-records"></a>

**Hồ sơ không chính thức và phạm vi nhỏ.** Phân tách nhiệm vụ chia tỷ lệ theo lợi hại vật chất, không theo tính hình thức ([Chương Một §10.2 Phân tách nhiệm vụ](core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties)). Với việc không lương, tổ chức đồng đẳng, tương trợ, chăm sóc, bảo trì, sửa, dạy, và quản trị có trách nhiệm cộng đồng — mà [Chương Chín §6 Hệ quả đóng góp thứ hai](../../core_10_standing_integration.md#6-contribution-consequences-second) đòi được ghi nhận trên chuẩn bình đẳng — ghế xác minh được thỏa bởi **mọi văn phòng vô tư có thẩm quyền đã công bố để dựa vào hồ sơ**, thường là thân sẽ dùng nó: hội đồng lưu vực, thân tài trợ hoặc liên tục, văn phòng ghi nhận hồ sơ **CI-22** (*Tài sản chung, hợp tác xã, tương trợ, và quản trị cộng đồng ngoài thị trường*), hoặc một diễn đàn. Nó không được thỏa bởi tính hình thức của thân xác minh. Trên hồ sơ đó:

- người tham gia là đối tượng và, nơi họ xin ghi nhận, bên tuyên; trong hồ sơ tập thể dưới **mục 3.3** mỗi đồng-tham-gia là bên tuyên, nên tuyên của một thành viên về phần của thành viên khác là đầu vào, không bao giờ xác minh;
- người thụ, hàng xóm, và người không-tham-gia khác cung cấp chứng nhận như tư liệu xác minh dưới **mục 3.1**; hữu tri giữ nhật ký của nhóm là người ghi và nhân chứng dưới *Tuyên người ghi là đầu vào* dưới đây;
- văn phòng hồ sơ của thân dựa vào giữ lưu giữ; với phạm vi nhỏ, xác minh và nhập-và-giữ có thể ngồi trong một văn phòng đó dưới một bảo vệ đã công bố, và nó không bao giờ ngồi với bên tuyên;
- một thanh hoặc quy trình đòi xác minh bởi một thể chế hình thức nhóm không chính thức không với tới được, nơi một thân dựa vào vô tư có sẵn, là mẫu gác-cổng tùy tiện [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances), không phải phân tách nhiệm vụ.

Không điều nào trong này đòi một hồ sơ tồn tại. **Mục 2.1** *Im lặng là mặc định* kiểm soát: việc không chính thức không được ghi vì nó có thể được ghi, và phân tách nhiệm vụ chỉ ràng một khi một hồ sơ được xin.

<a id="371-named-record-opening-authority"></a>

**Quyền mở hồ sơ đã đặt tên.** Mọi hồ sơ quỹ đạo được mở, sửa, hết hạn, hoặc thay bởi một **quyền mở hồ sơ**: một vai trò, văn phòng, diễn đàn, hoặc thân có thẩm quyền xác minh cơ sở sự kiện dưới Chương Hai đến Bốn và nhập hồ sơ được công bố trước khi nó hành. Nơi hồ sơ liên quan một hệ thống, thể chế, hoặc doanh nghiệp giữ một [Điều lệ](core_05_band_continuity.md#charter), Điều lệ đó đặt tên quyền mở hồ sơ và người lưu giữ hồ sơ cho hồ sơ liên quan phạm vi đã điều lệ của nó, hoặc trỏ tới văn kiện đã công bố đặt tên chúng (**CI-3.6** (*Nội dung, rà soát, và mẫu hình thành Điều lệ*)). Diễn đàn hành như quyền mở hồ sơ trên các điều khoản ở **mục 3.6**; một diễn đàn đã xác minh một hồ sơ không nghe tranh biện của hồ sơ đó, việc đó đi tới rà soát thứ cấp dưới [Chương Mười Một](core_11_forum.md#chapter-eleven-forums-and-jurisdiction) và **CF-6** (*Đường dẫn kháng, rà soát thứ cấp, và cạn*). Nơi không Điều lệ hay chỉ định diễn đàn nào với tới hồ sơ, *Dự phòng khi Điều lệ im* trên áp, và văn kiện tiếp nhận dưới [Chương Mười Lăm](../../core_16_amendment_ratification.md) hoặc quy tắc đã công bố của thân vận hành chuỗi quỹ đạo phải rồi đặt tên một quyền. Một mục làm không có quyền đã đặt tên được đánh **tạm**: nó giữ bằng chứng và thông báo dưới **mục 2.1**, nhưng nó không cung cấp đầu vào đã xác minh dưới **mục 3.1** và không hiệu ứng Chương Chín cho đến khi một quyền đã đặt tên xác nhận, sửa, hoặc gạt nó sang một bên.

<a id="372-record-custodian"></a>

**Người lưu giữ hồ sơ.** Mọi hồ sơ quỹ đạo có một **người lưu giữ hồ sơ** đã đặt tên giữ hồ sơ, kiểm phiên dưới **mục 3.4**, công bố đường tranh biện dưới **mục 3.1**, và trả lời cho liên tục của hồ sơ. Người lưu giữ là ghế riêng khỏi quyền mở hồ sơ dưới *Phân tách nhiệm vụ* trên: nó nhập điều quyền đã xác minh, và không xác minh. Lưu giữ không được đứt: khi một người lưu giữ bị giải, xung đột, hoặc thay, lưu giữ chuyển với đầy đủ dấu vết kiểm toán dưới [Bảo toàn bằng chứng](core_05_band_oversight.md#evidence-preservation) tới người kế Điều lệ hoặc chỉ định đặt tên, hoặc, nơi không ai được đặt tên, tới diễn đàn giám sát dưới **mục 3.6**.

<a id="373-no-self-custody"></a>

**Không tự lưu giữ.** Những cái sau không được hành như quyền mở hồ sơ hoặc người lưu giữ hồ sơ cho một hồ sơ: đối tượng của hồ sơ; bên tuyên đóng góp hoặc cáo vi phạm hồ sơ liên quan; và mọi văn phòng trên đường thẩm quyền kiểm có trọng, hoặc bị kiểm có trọng bởi, những bên đó. Một người quản trị có trách nhiệm bên trong đối tượng thực hiện Quản trị có trách nhiệm Hệ thống Then chốt hoặc thẩm quyền vận hành có trọng giữ mọi bổn phận dưới [Chương Chín §5.4](../../core_10_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) và [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) — dừng điều họ kiểm, ghi bộ tái lập được, bảo toàn bằng chứng họ giữ, thông báo, và leo thang — và không hành động nào trong đó là xác minh sự kiện hay nhập hồ sơ. Nơi quyền mở hồ sơ thường tự là đối tượng hoặc ngồi trên đường kiểm soát của nó, hồ sơ định tuyến tới xác minh độc lập: một diễn đàn dưới **mục 3.6**, dịch vụ điều tra độc lập dưới **CF-9.6** (*Không tự điều tra*), hoặc một thân dự phòng chỉ định trước có thẩm quyền đã công bố, cái nào Điều lệ hoặc chỉ định đặt tên trước. Vắng mọi đường đó là khoảng trống người quản trị có trách nhiệm phải đặt tên trong nhật ký, không phải lý do tự nhập hồ sơ. Quy tắc này loại bên theo lợi trong hồ sơ; *Phân tách nhiệm vụ* trên tách ghế theo chức năng. Cả hai áp, và câu trả lời hẹp hơn kiểm soát.

<a id="37-conflicted-custodian-on-a-single-record"></a>

**Người lưu giữ xung đột trên một hồ sơ.** Nơi người lưu giữ đã đặt tên bị loại dưới *Không tự lưu giữ* cho một hồ sơ nhưng không cho phạm vi — thường vì bên tuyên, đối tượng, hoặc người tranh ngồi trên đường báo cáo của người lưu giữ — việc loại là theo hồ sơ và kéo dài khi xung đột còn, và được trả lời bằng lưu giữ thay: không bằng người lưu giữ kiêng trong khi hồ sơ nằm, và không bằng chuyển cả kho. Người lưu giữ bị loại ghi yêu cầu và xung đột trên hồ sơ dưới *Mục đã gán* dưới đây, bảo toàn hồ sơ và bằng chứng không đổi dưới [Bảo toàn bằng chứng](core_05_band_oversight.md#evidence-preservation), giữ đường tranh biện đã công bố mở, và không nhập phiên. Lưu giữ hồ sơ đó chuyển, với đầy đủ dấu vết kiểm toán, tới người giữ thay Điều lệ hoặc bản đồ làn đặt tên cho phạm vi (**CI-3.6** (*Nội dung, rà soát, và mẫu hình thành Điều lệ*) trường 11; làn công bố-và-bằng-chứng **CI-3.2** (*Làn tách chức năng*) ngoài đường kiểm soát), hoặc, nơi không ai được đặt tên, tới diễn đàn giám sát dưới **mục 3.6**, thân giữ hồ sơ hoặc chỉ định người giữ. Người thay được đặt tên trên hồ sơ. Khi xung đột hết — bên có lợi rời đường kiểm soát, hoặc hồ sơ đóng cho ngữ cảnh quyết định của nó — lưu giữ có thể trở lại bằng một chuyển đã ghi dưới *Người lưu giữ hồ sơ* trên. Một người lưu giữ tiếp nhập phiên với quan điểm xung đột chỉ hình thức phạm thất *Không tự lưu giữ*; đó không phải phán tính tương xứng mở cho họ. Một thể chế có bản đồ làn để mọi người lưu giữ cho một hệ thống bên trong đường báo cáo của văn phòng chạy nó có khuyết **CI-3.2** phải sửa, và hồ sơ của nó định tuyến tới diễn đàn trong lúc đó.

<a id="374-recorder-statements-are-inputs"></a>

**Tuyên người ghi là đầu vào.** Một tuyên sau của hữu tri hoặc văn phòng đã mở, xác minh, hoặc trước đó giữ một hồ sơ — nâng hoặc bác một đóng góp tuyên, một bỏ sót cáo, hoặc một tranh biện — vào hồ sơ như tư liệu xác minh dưới **mục 3.1** và qua cùng cổng đầu vào đã xác minh như mọi đầu vào khác. Người ghi trước là nhân chứng về hồ sơ, không phải thẩm phán của nó. Nâng của họ không tự xác minh một đóng góp; bác của họ không tự bác một đóng góp; đồng ý của họ với đối tượng hoặc với người tranh không tự quyết gì. Có mặt hay vắng mặt của họ không đóng băng cũng không hoàn tất hồ sơ: nơi một người ghi trước không với tới được, hồ sơ nói vậy và tiến trên tư liệu đã xác minh còn lại.

Tuyên người ghi nặng đến mức nào là câu hỏi Chương Hai đến Bốn cho ghế xác minh, không phải câu hỏi lưu giữ. Người xác minh đọc nó như đưa ra trong [Thiện chí](core_05_band_accountability.md#good-faith) khi không có chỉ báo ngược, nhưng thiện chí đi tới thẳng thắn, không tới đúng; đúng được lập bởi xác nhận dưới [Chương Bốn §5](core_04_burden_traceability_verification.md#5-compliance-evidence-standard). Một tuyên khớp nhật ký đồng thời, phiên trước, kiểm toán, hoặc xác nhận độc lập mang trọng của những tư liệu đó. Một tuyên đứng một mình là chứng nhận và không tự mang gánh. Một tuyên từ bên tuyên, đối tượng, người tranh, hoặc văn phòng trên đường kiểm soát của họ là tự-chứng cho mục đích đó. Nơi tuyên giải thích *vì sao* hồ sơ được để như vậy — như khi một người ghi trước nói một mục bị bỏ vì chưa được xác minh — nó là bằng chứng về trạng thái hồ sơ lúc đó và về điều chưa xác minh khi đó; nó không quyết sự kiện bị bỏ từ đó đã được xác minh chưa, việc ghế xác minh trả lời trên tư liệu hiện tại.

<a id="375-attributed-entry"></a>

**Mục đã gán.** Mọi mở, sửa, sửa hồi tố, hết hạn, thay, hoặc chuyển lưu giữ đặt tên, trên chính hồ sơ, ai đổi, dưới thẩm quyền đã công bố nào, trên tư liệu xác minh nào, và theo yêu cầu của ai. Một yêu cầu từ bên có lợi — đối tượng, bên tuyên, người tranh, hoặc văn phòng trên đường kiểm soát của họ — được ghi như yêu cầu lúc nhận, dù có được hành hay không, và chỉ được hành qua xác minh riêng của quyền mở hồ sơ. Không người lưu giữ hay quyền nào được từ chối ghi một yêu cầu hoặc một từ chối hành.

<a id="37-challenge-received-on-the-record"></a>

**Tranh biện nhận trên hồ sơ.** [Khả năng tranh biện](core_05_band_accountability.md#contestability) không bắt đầu ở diễn đàn. Khi một bên bị ảnh hưởng tranh một hồ sơ, một phiên, hoặc một hiệu ứng tuyên từ nó — với người lưu giữ, với quyền mở hồ sơ, hoặc với mọi văn phòng của thể chế — người lưu giữ ghi tranh biện trên hồ sơ dưới *Mục đã gán* trên lúc nhận, đặt trạng thái rà soát dưới **mục 3.1** thành *đang tranh biện*, thông báo đối tượng và mọi bên tuyên, và định tuyến nó tới ghế tranh biện: văn phòng giữ làn tranh-biện-và-rà-soát dưới **CI-3.2** (*Làn tách chức năng*), hoặc một diễn đàn đủ năng lực dưới **mục 3.6** và [Chương Mười Một §2.3](core_11_forum.md#23-forum-records-standing-records-and-contests) (*Tranh biện hồ sơ quỹ đạo*), cái nào đường tranh biện đã công bố của hồ sơ đặt tên. Đường đã công bố đó là bước thường đầu tiên dưới [Trình tự tranh chấp](core_11_forum.md#dispute-sequencing); một diễn đàn đủ năng lực vẫn sẵn khi đường đó còn bị tranh, thiếu, bị chiếm, hoặc không thể cấp cứu trợ cần. Người lưu giữ và quyền không quyết tranh biện. *Đang tranh biện* là trạng thái, không phải đình: hồ sơ vẫn kiểm được, phiên trước vẫn tại chỗ, và dựa vào phiên bị tranh cho một hiệu ứng Chương Chín chỉ tạm dừng nơi ghế tranh biện hoặc một diễn đàn ra lệnh vậy. Một tranh biện không phải yêu cầu sửa và không đóng băng một yêu cầu sửa: tường thuật của người tranh, như của bên tuyên, là đầu vào xác minh dưới *Tuyên người ghi là đầu vào* và **mục 3.1**, không bao giờ xác minh, và không bên nào được coi tranh biện đang treo là lý do nhập, hoặc từ chối nhập, một phiên quyền mở hồ sơ đã xác minh cách khác. Đồng hồ bậc dưới [Chương Mười Một §6](core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) và [Điều XXIV-C](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) chạy từ lúc nhận. Một tranh biện không định tuyến được vì không ghế tranh biện nào được đặt tên là khuyết trường 11 **CI-3.6** ghi trên hồ sơ và định tuyến tới diễn đàn giám sát dưới **mục 3.6**; nó không bị đóng vì thiếu nơi, và đóng nó vì lý do đó là cản trở dưới [Điều XII-B](core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) và **mục 2.3.2** (*Cản trở trách nhiệm giải trình*).

<a id="376-custody-is-not-delay"></a>

**Lưu giữ không phải trì hoãn, và lưu giữ không phải sở hữu.** Một câu hỏi lưu giữ được trả lời bằng định tuyến tới quyền đã đặt tên hoặc độc lập, không bằng chờ. Không bên nào được dùng tranh chấp lưu giữ, người ghi trước không có mặt, hoặc quyền chưa đặt tên để giữ một hồ sơ mở, đóng, hoặc chưa sửa quá đồng hồ bậc dưới [Chương Mười Một §6](core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) và [Điều XXIV-C](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) (*Sàn Giải quyết kịp thời và Chống trì hoãn*). Giữ một hồ sơ không ban thẩm quyền về hiệu chỉnh đo lường Câu hỏi 2, về hiệu ứng quỹ đạo Chương Chín, hoặc về đối tượng; một người lưu giữ áp một hiệu ứng, giữ đường tranh biện, hoặc đặt điều kiện nhập vào hợp tác của đối tượng tự là đối tượng của một hồ sơ quỹ đạo vi phạm riêng dưới **mục 2.3.2** (*Cản trở trách nhiệm giải trình*).

<a id="4-standing-measurement-evaluation-dimensions"></a>
<a id="4-classification-evaluation-dimensions"></a>

<a id="4-question-2-how-good-or-bad-was-it"></a>

<a id="4-question-2--how-good-or-bad-was-it"></a>
### 4. Câu hỏi 2 — tốt hay xấu đến mức nào?
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§2](#2-standing-records) (*Câu hỏi 1 — hồ sơ quỹ đạo và sự kiện đã xác minh*); [§3](#3-standing-record-operational-requirements) (*cổng đầu vào đã xác minh và yêu cầu hồ sơ*); [§1](#1-the-three-questions) (*khung ba câu hỏi*).
- Hạ nguồn: [§5](#5-slot-grammar-and-lequ-calibration) (*ngữ pháp ô và chia tỷ lệ chung*); [§6](#6-constitutional-inputs-to-axis-assignment) (*định tuyến nguồn hiến pháp*); [§7](#7-unified-proportional-lequ-scale) (*gán Trục Đóng góp và Trục Vi phạm*); [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) (*Câu hỏi 3 đóng góp — ủy thác an toàn*); [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) (*khóa ngăn*); [Chương Chín §5](../../core_10_standing_integration.md#5-lock-design-and-enforcement) (*thiết kế và cưỡng khóa*).
- Đọc cùng: [§3.1](#31-minimum-record-contents) (*trường hồ sơ đã xác minh; không hiệu ứng quỹ đạo trong Chương Tám*).

</details>

<br>

*Nói thẳng: Câu hỏi 2 đo sự kiện đã xác minh từ Câu hỏi 1. Nó hỏi **đóng góp tốt đến mức nào?** hoặc **vi phạm xấu đến mức nào?** Đây là nơi chương lần đầu đưa hai trục đo lường hình thức: **Trục Đóng góp** cho giúp đã xác minh và **Trục Vi phạm** cho phát hiện bất lợi đã xác minh. Các trục vẫn riêng; chúng không phải hai mặt của một điểm ròng.*

<a id="lequ-baseline-constitutional-outcome"></a>
<a id="6-lequ-baseline-constitutional-outcome"></a>
<a id="46-lequ-baseline-constitutional-outcome"></a>

**Đường cơ sở LEQU.** Để quyết đóng góp hoặc vi phạm của ai thuộc ô nào, chương này đo tác động dùng một **Đơn vị tương đương tuổi thọ (LEQU)**. Một LEQU xấp xỉ bằng cứu hoặc phá cả đời phúc lợi của một hữu tri. Đây không phải đếm thân thể hay đô la; nó hỏi liệu một hành động có đổi có nghĩa phúc lợi của cộng đồng hiến pháp không. Cùng đơn vị làm việc với mọi hữu tri, người hay không.

Thang ô đo độ lớn và tính chất kết quả hiến pháp. Trên Trục Đóng góp, nó đo lợi hiến pháp đã xác minh, không phải sản lượng thô, uy tín, giàu, sử dụng, tốc độ, hay quy mô thể chế. Trên Trục Vi phạm, nó đo mất, hại, lãng, đóng cửa, hoặc nguy hiến pháp đã xác minh, không phải trạng thái không ưa, cáo buộc, hay ghét đạo đức một mình.

Một **lợi hiến pháp tương đương cả đời** nghĩa là lợi đã xác minh sánh với giữ, khôi, hoặc giải phóng một đời hữu tri đầy đủ của phúc lợi không tầm thường, khớp quyền. Một **mất hiến pháp tương đương cả đời** nghĩa là hại, lãng, phá, đóng cửa, tước, hoặc hiện rủi đã xác minh sánh với phá, tiêu sai, hoặc ngăn một lợi hiến pháp tương đương cả đời. Một **Đơn vị tương đương tuổi thọ** (**LEQU**) là đơn vị tắt cho lợi hoặc mất hiến pháp tương đương cả đời đó khi triển khai đã tiếp nhận cần hiệu chỉnh số. Đơn vị không phụ thuộc nền. Một bên tiếp nhận hiện có thể dùng một đời người thường làm ví dụ hiệu chỉnh cho ngữ cảnh người sinh học, nhưng đường cơ sở ràng là hữu tri và hiến pháp, không khóa loài.

**Cầu trạng thái hữu tri (đọc cùng Điều V-E).** Đo lường quỹ đạo **không** quyết một thực thể có phải **hữu tri** không. Tranh trạng thái định tuyến tới [Phân xử trạng thái hữu tri](core_05_band_participation.md#sentience-status-adjudication-constitutional) và [Điều V-E](core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor) (*Sàn phân xử trạng thái hữu tri*), không tới điểm LEQU hay hồ sơ phân loại. Trong khi trạng thái đang bị tranh sống dưới [Sự sống hữu tri đang tranh](core_05_band_participation.md#contested-sentient-life-constitutional), bao gồm mặc định Điều V-E giữ đủ điều kiện đo lường quỹ đạo và năng lực nộp hồ sơ quỹ đạo khi phân xử treo — người vận hành không được coi trạng thái chưa giải một mình là không đủ điều kiện quỹ đạo. Trạng thái [Hữu tri](core_05_band_participation.md#sentient) đã khẳng, hoặc thu hẹp hay khôi rà soát được sau phân xử, cập nhật nhận diện đối tượng hồ sơ quỹ đạo về phía trước; loại sai không được lùi ngày để xóa đủ điều kiện đo lường quỹ đạo tạm mà không có [Khắc phục và sửa chữa](core_05_band_accountability.md#redress-and-remediation-constitutional).

**Giới hạn quan trọng khi dùng LEQU:**

- **Không phải quy tắc điểm ròng:** Bạn không thể «hủy» vi phạm bằng đóng góp hay ngược lại. Mỗi trục đứng riêng.
- **Không phải thước đời người bắt buộc:** LEQU là chung-hữu-tri; nó áp cho mọi sinh thể có ý thức, không chỉ người.
- **Không phải thước cáo:** Cáo buộc, thẻ tiếp nhận, quyết định định tuyến, danh tiếng, trạng thái không ưa, hoặc ghét đạo đức không cung cấp lợi Trục Đóng góp hay mức nghiêm Trục Vi phạm mà không có đầu vào đã xác minh dưới **mục 3.1** và hiệu chỉnh dưới **mục 7**.
- **Không phải giấy phép đổi quyền:** Tuyên đóng khung như hiệu quả, năng lực sản xuất, đổi mới, giảm gánh, an ninh, trả đũa, đáp khẩn, hoặc sự cần thể chế phải bị chiết hoặc từ chối nơi chúng phụ thuộc:
  - cưỡng;
  - chuyển gánh phân biệt;
  - cạn sinh thái;
  - việc không lương ẩn;
  - độ mờ tránh được;
  - thu hẹp Sàn Quyền;
  - chiếm;
  - chỉ số thay thế lệch;
  - mất khả năng tranh biện; hoặc
  - gộp không rà soát được.

**Chỉ Câu hỏi 2.** Dùng những chiều này để đo sự kiện đã xác minh lập dưới **mục 2** và ghi dưới **mục 3**. Mục lục **đường-lợi** ở **mục 4.3** và mục lục **đường-hại** ở **mục 4.4** cung cấp tên chuẩn hóa cho loại giúp hoặc hại và nêu mỗi tên đếm thế nào vào *tốt đến mức nào* hoặc *xấu đến mức nào*. Quy tắc tích hợp và gắn Câu hỏi 3 nằm ở [Chương Chín §3](../../core_10_standing_integration.md#3-descriptor-integration-and-attachment-normalization), với quy tắc hệ quả ở [phía lợi](../../core_10_standing_integration.md#62-competency-bars-and-clearances) và [phía hại](../../core_10_standing_integration.md#42-prevention--general-standing-locks).

<a id="41-magnitude-input-dimensions"></a>
<a id="41-contribution-magnitude-input-dimensions"></a>

#### 4.1 Chiều đầu vào độ lớn đóng góp

<a id="contribution-table-q1-magnitude-input-dimensions"></a>
<a id="contribution-table-q2-magnitude-input-dimensions"></a>

**Bảng đóng góp — Câu hỏi 2: chiều đầu vào độ lớn (tốt đến mức nào?).** Những chiều này nuôi gán ô Trục Đóng góp và mô tả lợi xếp chồng ghi trong **hồ sơ quỹ đạo đóng góp**. Tiêu chí dải vận hành và hiệu chỉnh LEQU nằm ở **mục 7**.

| **Chiều** | **Vai trò ở Câu hỏi 2** | **Neo kho văn bản** |
| --- | --- | --- |
| **Độ lớn kết quả hiến pháp (LEQU)** | Neo lợi sơ cấp — lợi hiến pháp đã xác minh đã tích hợp | [Chương Tám §7](#7-unified-proportional-lequ-scale); `s` = 7 bắt đầu tại ≥1 LEQU được cứu hoặc biến đổi |
| **Phạm vi hữu tri (số, độ sâu, dễ tổn)** | Điều chỉnh đánh giá LEQU và tính trọng yếu | [Chương Tám §5.2](#52-shared-impact-scaling-rules); [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) |
| **Phạm vi thời gian (kéo dài, bền)** | Điều chỉnh đánh giá LEQU | Quản trị có trách nhiệm bền, lợi xuyên thế hệ, sửa thể chế bền hướng `s` = 8–9 |
| **Phạm vi không gian / thể chế** | Điều chỉnh đánh giá LEQU | Lợi xuyên cộng đồng, xuyên thể chế, hoặc quy mô văn minh |
| **Chồng đường-lợi** | Đặt tên đường lợi đã xác minh; xếp chồng được | [**Mục lục mô tả đường-lợi**](#43-route-descriptor-measurement-roles) |
| **Chồng chất lượng hành vi** | Lợi được tạo thế nào; có thể hạn lợi đếm được | Truy vết, không ngoại hóa, thận trọng, thẳng hàng hiến pháp; hại ngoại hóa hoặc gánh che trần lợi ([Chương Tám §4.1](#41-contribution-magnitude-input-dimensions)) |

**Áp dụng chất lượng hành vi đóng góp.** Áp chồng chất lượng hành vi trước khi gán ô Trục Đóng góp:

- sửa đã xác minh kịp sau thông báo có thể nâng **Thận trọng** khi nó sản lợi chứng minh được, nhưng nó không bù một hồ sơ vi phạm đang mở;
- hại ngoại hóa hoặc gánh che trần hoặc loại lợi gán cho đường dẫn được đặt tên đang tranh;
- rủi chiếm đã xác minh, phụ thuộc cấu trúc, hoặc thiết kế lối ra / khóa-trong hạn tín dụng dương quản trị có trách nhiệm;
- sửa lối vào hoặc rào tham gia đã xác minh có thể tăng tính trọng yếu và nâng mô tả đường-lợi **Lối vào và hòa nhập** dưới **mục 4.3**; và
- một thưởng có trọng nhận qua cấu trúc khuyến khích lệch hiến pháp, hành vi phản hiến pháp, hoặc quy trình khuyết có trọng mặc định không phải lợi đếm được. Áp [Chương Chín §5.4](../../core_10_standing_integration.md#54-special-violation-rules) và giới hạn chuyển ở [Điều XXVI-A](core_06_rights_part_d.md#incentive-alignment-transition-carve-out).

**Đầu ra Câu hỏi 2 (ghi trong hồ sơ quỹ đạo đóng góp; không phải hiệu ứng quỹ đạo):**

- **Ô Trục Đóng góp** áp dụng (`s` = 1–9) và dải sơ cấp (**C-BL**, **C-PC**, **C-SP**, hoặc **C-CH**)
- **Mô tả đường-lợi** xếp chồng
- Đầu vào định hướng ghi nhận mặc định dưới [Chương Chín §6](../../core_10_standing_integration.md#6-contribution-consequences-second)

**Không** tách LEQU thành điểm lợi sinh thái, hệ thống, hoặc tài nguyên song song trừ khi triển khai đã tiếp nhận cần phân rã trong suốt cho kiểm toán.

<a id="42-violation-severity-input-dimensions"></a>

#### 4.2 Chiều đầu vào mức nghiêm vi phạm

**Bảng vi phạm — Câu hỏi 2: chiều đầu vào mức nghiêm (xấu đến mức nào?).** Những chiều này nuôi gán ô Trục Vi phạm và mô tả hại xếp chồng ghi trong **hồ sơ quỹ đạo vi phạm**. Tiêu chí ô vận hành và hiệu chỉnh LEQU nằm ở thang thống nhất ở **mục 7**.

| **Chiều** | **Vai trò ở Câu hỏi 2** | **Neo kho văn bản** |
| --- | --- | --- |
| **Độ lớn kết quả hiến pháp (LEQU)** | Đầu vào ô sơ cấp và kiểm soát — mất hiến pháp đã xác minh đã tích hợp | [Chương Tám §7](#7-unified-proportional-lequ-scale); chỉ định Chương Mười vẫn riêng |
| **Phạm vi hữu tri (số, độ sâu, dễ tổn)** | Điều chỉnh đánh giá LEQU và tính trọng yếu | [Chương Tám §5.2](#52-shared-impact-scaling-rules); [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) |
| **Phạm vi thời gian (kéo dài, không đảo ngược)** | Điều chỉnh đánh giá LEQU | Chấn thương bền, mất không đảo ngược, và suy quyền năng bền tăng ước mất tích hợp |
| **Phạm vi không gian / thể chế** | Điều chỉnh đánh giá LEQU | Tầm xuyên cộng đồng, xuyên thể chế, hoặc văn minh có thể tăng ước mất tích hợp |
| **Chồng đường-hại** | Đặt tên đường hại đã xác minh; xếp chồng được | [**Mục lục mô tả đường-hại**](#44-violation-route-descriptor-measurement-roles) |
| **Chồng tính chất hành vi** | Hại được gây thế nào; ghi riêng khỏi tác động | Bổn phận, thiếu thận trọng, lừa, che giấu, cản trở trách nhiệm giải trình, cưỡng, bạo lực, ý định, tàn nhẫn, và mở đường cấu trúc thông tin gán, bảo vệ, và đáp nhưng không dịch ô LEQU |

**Áp dụng tính chất hành vi vi phạm.** Áp chồng tính chất hành vi riêng khỏi độ lớn kết quả:

- trì đáp hoặc leo thang tránh được được ghi nơi bổn phận và năng lực hành khả thi tồn tại; mọi mất cộng vào ước LEQU một lần, trong khi trì vẫn là sự kiện tính chất riêng;
- hại toàn vẹn diễn đàn đã xác minh độc lập vào ước LEQU tỷ lệ đúng một lần; bỏ sót không thành thật, thất quy trình rút cố ý, cưỡng, nguy tự do, và sự kiện tính chất hành vi khác vẫn là mô tả riêng và không dịch ô tác động;
- **cản trở trách nhiệm giải trình** — can thiệp đã xác minh vào máy phải-trả-lời như toàn vẹn bằng chứng, xác minh, quy trình diễn đàn, hồ sơ quỹ đạo, đồng hồ khắc phục, hoặc đường tranh biện và khắc phục — vẫn là sự kiện tính chất hành vi ghi riêng; mọi mất đường dẫn được đặt tên cộng vào ước LEQU một lần, trong khi nhãn cản tự nó không dịch ô tác động;
- lừa, che giấu, lẩn tránh, lặp sau thông báo, coi thường liều, mở đường cấu trúc, hoặc lạm bất đối xứng phụ thuộc có trọng vẫn là sự kiện tính chất hành vi ghi riêng;
- bạo lực, cưỡng, thao túng, hoặc nguy tự do vẫn được ghi riêng và có thể đòi bảo vệ nâng bất kể ô;
- [tàn nhẫn](core_05_band_accountability.md#cruelty) — khổ đã xác minh như mục đích tự nó, hoặc gây vô ích hay hạ phẩm vượt sự cần và tính tương xứng — vẫn là sự kiện tính chất hành vi ghi riêng; nó có thể đòi bảo vệ nâng và ràng khắc phục không hạ phẩm dưới [Chương Chín §4](../../core_10_standing_integration.md#4-violation-correction-and-prevention), và không dịch ô tác động;
- khuếch tán liên quan vai trò nhân quả phân tán, thẩm quyền, kiểm soát, khả năng thấy trước, lợi, che giấu, hoặc năng lực ngăn khả thi; nó không phải phần của **phạm vi hữu tri** và không cho phép trách theo thành viên nhóm;
- tham gia cam chịu hoặc thất kháng có thể nâng tính chất dựa-bổn-phận, tăng nặng, hoặc trách nhiệm giải trình tập thể chỉ khi liên kết riêng-tác nhân đòi bởi **mục 3.1 và 3.3** được xác minh; và
- chấp nhận hoặc giữ có hiểu một thưởng lệch có trọng mà không báo cáo được bảo vệ kịp được ghi dưới [Chương Chín §5.4](../../core_10_standing_integration.md#54-special-violation-rules), chịu [Điều XXVI-A](core_06_rights_part_d.md#incentive-alignment-transition-carve-out); chỉ mất hiến pháp đã xác minh của nó ảnh hưởng ô.

**Ranh giới thưởng lệch.** Chương này chỉ đo một thưởng lệch đã xác minh ảnh hưởng Trục Đóng góp hoặc Trục Vi phạm thế nào. [Chương Chín §5.4](../../core_10_standing_integration.md#54-special-violation-rules) nêu bổn phận báo cáo, loại trừ, hệ quả tịch thu, bổn phận sửa, và quy tắc định tuyến.

**Đầu ra Câu hỏi 2 (ghi trong hồ sơ quỹ đạo vi phạm; không phải hiệu ứng quỹ đạo):**

- **Ô Trục Vi phạm** áp dụng cao nhất (`s` = 1–9)
- **Mô tả đường-hại** xếp chồng
- Đầu vào định hướng dải khóa mặc định dưới [Chương Chín §5](../../core_10_standing_integration.md#5-lock-design-and-enforcement)

**Không** tách LEQU phía vi phạm thành điểm hại sinh thái, hại hệ thống, hoặc mất tài nguyên song song trừ khi triển khai đã tiếp nhận cần phân rã trong suốt cho kiểm toán.

<a id="43-route-descriptor-measurement-roles"></a>
<a id="43-route-descriptor-classification-roles"></a>
<a id="43-contribution-route-descriptor-measurement-roles"></a>

<a id="43-contribution-route-descriptor-catalog-and-measurement-roles"></a>
#### 4.3 Mục lục mô tả đường đóng góp và vai trò đo lường

<a id="benefit-route-descriptors-q1-measurement-role"></a>
<a id="benefit-route-descriptors-q1-classification-role"></a>
<a id="benefit-route-descriptors-q2-measurement-role"></a>

**Quy tắc mô tả chuẩn.** Mục **4.3–4.4** sở hữu mục lục mô tả chuẩn hóa cho cả hai trục. Mô tả trả lời **cách** lợi hoặc hại đã xác minh xảy ra. Chúng xếp chồng được, không loại trừ, và phụ thuộc ô áp dụng; một hồ sơ có thể mang nhiều cái nơi sự kiện đã xác minh nâng. Mục lục là nền, không phải danh sách đóng. Triển khai có thể dùng định danh ổn định ánh xạ tới nó nhưng không được tạo một phân loại độc quyền xung đột. Mô tả cáo có thể nâng bảo toàn hợp pháp, phân loại, hoặc bảo vệ tạm; chỉ mô tả đã xác minh được ghi như đầu ra Câu hỏi 2 hoặc ảnh hưởng quỹ đạo.

**Mô tả đường-lợi — vai trò đo lường Câu hỏi 2.** Vai trò ủy thác an toàn Câu hỏi 3: [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances).

| **Mô tả đường-lợi** | **Miền chuẩn hóa** | **Câu hỏi 2 (tốt đến mức nào?)** |
| --- | --- | --- |
| **Hòa bình thân thể, tâm trí, và/hoặc cộng đồng** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Lợi bình thân thể, tâm lý, và cộng đồng; điều chỉnh tính trọng yếu |
| **Quan hệ đáng tin** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Lợi quan hệ và tin cậy ủy thác trong bối cảnh bất đối xứng |
| **Chăm sóc và hỗ trợ phụ thuộc** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Chăm sóc đã xác minh cho người phụ thuộc; chăm sóc không chính thức đếm khi chứng minh được |
| **Lối vào và hòa nhập** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Lợi tham gia thực chất và khả năng tiếp cận; điều chỉnh tính trọng yếu trong bối cảnh bất đối xứng phụ thuộc |
| **Lợi khắc phục và phục hồi** | Sửa, tài sản, và tài nguyên | Lợi sửa, bồi thường, và giảm hại |
| **Quản trị có trách nhiệm về tài nguyên** | Sửa, tài sản, và tài nguyên | Quản trị có trách nhiệm vật chất và độ tin phân bổ |
| **Toàn vẹn không gian thông tin** | Tri thức, giáo dục, hồ sơ, và khám phá | Củng hồ sơ, minh bạch, và truyền thông |
| **Giáo dục và xây năng lực** | Tri thức, giáo dục, hồ sơ, và khám phá | Lợi học, biết chữ, và mở quyền năng |
| **Đóng góp STEM và khám phá** | Tri thức, giáo dục, hồ sơ, và khám phá | Khám phá tái lập được và nghiên cứu cải an toàn |
| **Tối ưu hệ thống** | Hệ thống và vận hành hiến pháp | Sửa quy trình xuyên thể chế và giảm rủi |
| **Thẳng hàng hiến pháp** | Hệ thống và vận hành hiến pháp | Lợi củng sàn và lối vào tranh biện |
| **Quản trị có trách nhiệm sinh thái** | Sinh thái và thận trọng | Lợi môi trường sống, đa dạng sinh học, và trách nhiệm khí hậu |
| **Thận trọng** | Sinh thái và thận trọng | Ngăn rủi thấy trước được và giám sát có năng lực |

**Đầy đủ mục lục.** Một hàng hiển thị gộp hoặc nhãn triển khai phải ánh xạ về mọi mô tả chuẩn hóa áp dụng. Mục lục này chỉ quản trị tên mô tả và vai trò đo lường Câu hỏi 2 của chúng. Quy tắc gắn, khắc phục, khóa, giấy phép, và hiệu ứng quỹ đạo khác Câu hỏi 3 vẫn độc quyền ở Chương Chín.

<a id="44-violation-route-descriptor-measurement-roles"></a>

<a id="44-violation-route-descriptor-catalog-and-measurement-roles"></a>
#### 4.4 Mục lục mô tả đường vi phạm và vai trò đo lường

**Mô tả đường-hại — vai trò đo lường Câu hỏi 2.** Quy tắc tích hợp và gắn Câu hỏi 3: [Chương Chín §3](../../core_10_standing_integration.md#3-descriptor-integration-and-attachment-normalization). Thiết kế ngăn và khóa Câu hỏi 3: [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks); [Chương Chín §5](../../core_10_standing_integration.md#5-lock-design-and-enforcement).

| **Mô tả đường-hại** | **Miền chuẩn hóa** | **Câu hỏi 2 (xấu đến mức nào?)** |
| --- | --- | --- |
| **Hành vi sai bạo lực** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Ghi bạo lực, cưỡng, hoặc nguy tự do riêng khỏi ô tác động LEQU; có thể đòi bảo vệ nâng |
| **Hành vi sai bổn phận giao tiếp / chăm sóc** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Tính trọng yếu cao hơn trong bối cảnh bất đối xứng phụ thuộc |
| **Hành vi sai rào lối vào và tham gia** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Tính trọng yếu cao hơn khi bất đối xứng phụ thuộc; có thể xếp chồng đặc trưng tăng nặng |
| **Hành vi sai riêng tư và tự sở hữu** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Đặc trưng tăng nặng khi che giấu hoặc bóc lột được xác minh; có thể xếp chồng `s` = 5 |
| **Hành vi sai quyền năng và thao túng** | An toàn thân thể, quan hệ, chăm sóc, và quyền năng | Ghi cưỡng, thao túng, hoặc nguy tự do riêng khỏi ô tác động |
| **Hành vi sai có thể khắc phục** | Sửa, tài sản, và tài nguyên | Ghi tính chất sửa; ô theo mất LEQU tích hợp |
| **Hành vi sai tài sản** | Sửa, tài sản, và tài nguyên | Đường mất tài sản; ô theo mất LEQU tích hợp |
| **Hành vi sai không gian thông tin** | Tri thức, giáo dục, hồ sơ, và khám phá | Suy An toàn hoặc Sự thật; che giấu và lừa vẫn là sự kiện tính chất riêng |
| **Hành vi sai giáo dục** | Tri thức, giáo dục, hồ sơ, và khám phá | Ghi hại đường dẫn giáo dục hoặc năng lực riêng khỏi ô tác động |
| **Hành vi sai nghiên cứu và khám phá** | Tri thức, giáo dục, hồ sơ, và khám phá | Ghi hại đường dẫn nghiên cứu hoặc khám phá riêng khỏi ô tác động |
| **Hành vi sai hệ thống** | Hệ thống và vận hành hiến pháp | Khuếch tán và mở đường cấu trúc vẫn được ghi riêng; ô theo mất LEQU tích hợp |
| **Hành vi sai cản trở trách nhiệm giải trình** | Hệ thống và vận hành hiến pháp | Ghi cản trở trách nhiệm giải trình như đường hại trách-nhiệm-giải-trình; sự kiện tính chất ở lại riêng; ô theo mất LEQU tích hợp; khi `s` = 7–9, có thể đồng-xếp với **Hành vi sai phản hiến pháp** cho định tuyến Chương Mười mà không thế chỉ định |
| **Hành vi sai lối ra và khóa-trong** | Hệ thống và vận hành hiến pháp | Đặc trưng Hành vi sai hệ thống; khuếch tán hoặc chiếm khi cấu trúc |
| **Hành vi sai vòng đời và không đảo ngược** | Hệ thống và vận hành hiến pháp | Không đảo ngược ảnh hưởng độ lớn LEQU; che giấu hoặc thiếu thận trọng vẫn là tính chất ghi riêng |
| **Hành vi sai phản hiến pháp** (mô tả) | Hệ thống và vận hành hiến pháp | Định tuyến một vi phạm `s` = 7–9 tới rà soát chỉ định Chương Mười mà không đổi ô tác động của nó |
| **Hành vi sai sinh thái** | Sinh thái và thận trọng | LEQU trọng Liên tục; có thể xếp chồng với đường bạo lực |
| **Hành vi sai do thiếu thận trọng** | Sinh thái và thận trọng | Ghi bổn phận, khả năng thấy trước, và khả năng ngăn riêng khỏi ô tác động |


<a id="45-dual-use-measurement-hooks"></a>
<a id="45-dual-use-classification-hooks"></a>

<a id="45-cross-question-measurement-hooks"></a>
#### 4.5 Móc đo lường xuyên câu hỏi

**Hướng dẫn xuyên câu hỏi.** Mục **4.1–4.4** giải thích mỗi đặc trưng ảnh hưởng Câu hỏi 2 thế nào: **tốt hay xấu đến mức nào?** Bảng dưới cho thấy sự kiện đã xác minh nào trong số đó cũng có thể quan trọng với Câu hỏi 3: **điều gì xảy ra vì thế?** Một đặc trưng có thể quan trọng với cả hai câu hỏi mà không áp cho cả Trục Đóng góp và Trục Vi phạm. Ghi cách dùng Câu hỏi 2 và Câu hỏi 3 của nó riêng. **Không** cộng chúng hay đếm cùng sự kiện hai lần.

| **Đặc trưng đã xác minh** | **Chủ sở hữu Câu hỏi 2 trong chương này** | **Chủ sở hữu tích hợp Câu hỏi 3** |
| --- | --- | --- |
| **Hại ngoại hóa / gánh che** | Áp dụng chất lượng hành vi đóng góp ở **§4.1** | [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) — có thể chặn hoặc thu hẹp giấy phép cho đến khi sửa |
| **Lừa / che giấu / lẩn tránh** | Áp dụng tính chất hành vi vi phạm ở **§4.2** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — khóa leo thang che giấu / lẩn tránh |
| **Cản trở trách nhiệm giải trình** | Áp dụng tính chất hành vi vi phạm ở **§4.2** và **Hành vi sai cản trở trách nhiệm giải trình** ở **§4.4** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) và [§5.4](../../core_10_standing_integration.md#54-special-violation-rules) — khóa phạm vi đường dẫn được đặt tên; [Chương Chín §10.13](../../core_10_standing_integration.md#1013-obstruction-of-accountability) (*mẫu Câu hỏi 3*); chỉ định Chương Mười chỉ qua cổng Rà soát hành vi sai phản hiến pháp dưới [Chương Chín §10.8](../../core_10_standing_integration.md#108-anti-constitutional-misconduct-allegation) |
| **Bạo lực / cưỡng / nguy tự do** | Áp dụng tính chất hành vi vi phạm ở **§4.2** và **Hành vi sai bạo lực** ở **§4.4** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — khóa bảo vệ và bảo đảm |
| **Tàn nhẫn** | Áp dụng tính chất hành vi vi phạm ở **§4.2**; [Tàn nhẫn](core_05_band_accountability.md#cruelty) | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — khóa bảo vệ và bảo đảm; [Chương Chín §4.3](../../core_10_standing_integration.md#43-voluntary-public-accountability-expression) — biểu đạt phục hồi không hạ phẩm nơi dùng |
| **Bền / mẫu / tái diễn sau thông báo** | Áp dụng tính chất hành vi vi phạm ở **§4.2** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — khóa tái diễn-bền |
| **Hại toàn vẹn diễn đàn** | Áp dụng tính chất hành vi vi phạm ở **§4.2** | [Chương Chín §5.5](../../core_10_standing_integration.md#55-special-locks) — hiệu ứng khóa quỹ đạo toàn vẹn diễn đàn |
| **Khuếch tán trách nhiệm hoặc kiểm soát** | Áp dụng tính chất hành vi vi phạm ở **§4.2**; liên kết riêng-tác nhân dưới **§§3.1 và 3.3** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — phạm vi đường dẫn được đặt tên rộng hơn hoặc xét phương tiện thể chế |
| **Mở đường hệ thống / cấu trúc** | Áp dụng chất lượng hành vi đóng góp ở **§4.1**; tính chất hành vi vi phạm ở **§4.2** và **Hành vi sai hệ thống** ở **§4.4** | [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) và [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — bảo vệ ủy thác hoặc khóa phương tiện thể chế |
| **Tham gia cam chịu / thất kháng** | Áp dụng tính chất hành vi vi phạm ở **§4.2** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — phạm vi đường dẫn được đặt tên và hiệu ứng tái diễn-bền |
| **Sửa lối vào / rào tham gia** | **Lối vào và hòa nhập** ở **§4.3** | [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) — thanh trải nghiệm hòa nhập hoặc phạm vi đường dẫn được đặt tên |
| **Đánh bại lối vào / hại rào tham gia** | **Hành vi sai rào lối vào và tham gia** ở **§4.4** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — chặn đường dẫn tham gia và khả năng tiếp cận được đặt tên |
| **Hại riêng tư / tự sở hữu** | **Hành vi sai riêng tư và tự sở hữu** ở **§4.4** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — chặn đường dẫn dữ liệu, hình dạng, công bố, hoặc trạng thái nội bộ được đặt tên |
| **Rủi lối ra / khóa-trong hoặc đóng cửa** | Áp dụng chất lượng hành vi đóng góp ở **§4.1**; **Hành vi sai lối ra và khóa-trong** ở **§4.4** | [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances) và [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — bảo vệ ủy thác hoặc chặn đường lối ra |
| **Che giấu vòng đời / không đảo ngược** | **Hành vi sai vòng đời và không đảo ngược** ở **§4.4** | [Chương Chín §4.2](../../core_10_standing_integration.md#42-prevention--general-standing-locks) — chặn thẩm quyền triển khai và vòng đời |

<a id="451-similar-looking-facts-that-must-stay-separate"></a>

##### 4.5.1 Sự kiện trông giống phải ở lại riêng

Một số sự kiện liên quan nhưng trả lời câu hỏi khác. Ghi chúng riêng:

| **Sự kiện thứ nhất** | **Sự kiện khác** | **Vì sao chúng ở lại riêng** |
| --- | --- | --- |
| **Trì đáp hoặc leo thang vấn đề gốc** | **Trì bắt đầu hoặc thực hiện khắc phục** | Cái thứ nhất giúp đo Câu hỏi 2 dưới **§§4.1–4.2**. Cái thứ hai là sự kiện Câu hỏi 3 sau dưới [Chương Chín §9.5](../../core_10_standing_integration.md#95-timely-implementation). |
| **Số hữu tri bị ảnh hưởng** | **Trách nhiệm hoặc kiểm soát được trải giữa tác nhân hoặc hệ thống thế nào** | Cái thứ nhất giúp đo lợi hoặc hại lớn đến mức nào dưới **§§4.1–4.2**. Cái thứ hai liên quan trách nhiệm riêng-tác nhân, khuếch tán, và phạm vi đường dẫn được đặt tên Câu hỏi 3 có thể. |

<a id="46-question-1-measurement-illustrations"></a>
<a id="46-question-1-classification-illustrations"></a>
<a id="46-question-2-measurement-illustrations"></a>

<a id="46-measurement-illustrations"></a>
#### 4.6 Minh họa đo lường

*Nói thẳng: những minh họa này bắt đầu với sự kiện đã xác minh của Câu hỏi 1, rồi cho thấy **mục 4** đo chúng thế nào. Chúng ghi đầu ra Câu hỏi 2 — không phải hiệu ứng quỹ đạo. Gán ô theo **mục 5–7**; Câu hỏi 3 được trả lời ở [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration). Để tiếp Câu hỏi 3 của Ví dụ 1 và 2 dưới, xem [Chương Chín §10.1](../../core_10_standing_integration.md#101-informal-ecological-stewardship-competency-clearance) và [§10.2](../../core_10_standing_integration.md#102-ecological-negligence-with-concealment).*

**Ví dụ 1 — Phục hồi hợp tác ven sông (đóng góp).**

**Tình huống.** Sau lũ xuân, bốn hữu tri trong một hợp tác ven sông không chính thức ổn định một dải đệm suối nửa kilômét suy giữa hai khu phố hạ nguồn. Việc là tương trợ không lương — không hợp đồng đô thị, không ghi danh chương trình có giấy phép, và không dấu chi trả nền tảng. Một hội đồng lưu vực sau hỏi liệu sửa đã xác minh của hợp tác có nên vào một **hồ sơ quỹ đạo đóng góp**.

**Đầu vào đã xác minh.** Nhật ký thử đất, biên lai trồng, ảnh môi trường sống trước/sau có dấu thời gian, và chứng nhận hàng xóm tranh biện được thỏa cổng đầu vào đã xác minh dưới **mục 3.1**. Cáo buộc một thành viên trước đó đổ rác thượng nguồn vẫn là một luồng định tuyến riêng, chưa xác minh và **không** vào hồ sơ này.

**Ghế dưới mục 3.7.** Bốn thành viên là đối tượng và, vì họ xin ghi nhận, bên tuyên; thành viên giữ nhật ký trồng là người ghi và nhân chứng của nó, không phải người xác minh. Văn phòng chỉ định của hội đồng lưu vực — vô tư với việc sửa và giữ thẩm quyền đã công bố để dựa vào hồ sơ — là quyền mở hồ sơ dưới *Hồ sơ không chính thức và phạm vi nhỏ*; hàng xóm là người thụ có chứng nhận vào như đầu vào. Văn phòng hồ sơ của hội đồng giữ lưu giữ; ở phạm vi này nó cũng có thể xác minh dưới một bảo vệ ghế-gộp đã công bố. Không cần diễn đàn để mở hồ sơ; một tranh biện của nó, nếu đến, đi tới làn tranh biện của hội đồng hoặc một diễn đàn dưới **mục 3.6**, không trở lại văn phòng xác minh.

**Lượt chiều Câu hỏi 2** (hồ sơ quỹ đạo đóng góp):

| **Chiều** | **Đánh giá đã xác minh** |
| --- | --- |
| Độ lớn kết quả hiến pháp (LEQU) | Lợi tích hợp có trọng nhưng dưới một LEQU — lợi sinh thái khu trú, không phải quy mô văn minh |
| Phạm vi hữu tri | Hai khu phố có dễ tổn lũ nâng; số hữu tri khiêm; không bổn phận chăm sóc bất đối xứng phụ thuộc trong mẫu sự kiện này |
| Phạm vi thời gian | Trồng bản địa, sửa bờ, và kiểm xói dự kiến chịu nhiều mùa sinh trưởng |
| Phạm vi không gian / thể chế | Lợi xuyên khu phố dọc một đoạn lưu vực chung; phối hợp không chính thức, không phải sửa xuyên thể chế |
| Chồng đường-lợi | **Quản trị có trách nhiệm sinh thái** + **Thận trọng** — kế hoạch trồng có hồ sơ, theo dõi tiếp theo lịch, và kiểm đất |
| Chồng chất lượng hành vi | Việc truy vết được; nước chảy không ngoại hóa sang thửa kề; không gánh che lên người tưới hạ nguồn |

**Đầu ra Câu hỏi 2 được ghi:** mô tả đường-lợi **Quản trị có trách nhiệm sinh thái** và **Thận trọng** xếp chồng; đầu vào LEQU và phạm vi sẵn cho hiệu chỉnh và gán ô dưới **[mục 7](#7-unified-proportional-lequ-scale)**. Không hiệu ứng quỹ đạo áp trong Chương Tám.

**Ví dụ 2 — Thiếu thận trọng người quản trị lưu vực với kết quả thử bị che (vi phạm).**

**Tình huống.** Một hữu tri giữ hợp đồng tin cậy cộng đồng để duy trì vùng đệm không thuốc trừ sâu trên cửa lấy nước tưới của ba hợp tác nông nghiệp. Thông báo cơ quan quản tám tháng trước gắn cờ bờ giữ đang thất. Người quản trị tiếp tục phun thuốc diệt cỏ hạn chế qua nhà thầu phụ, nộp xuất phòng thí nghiệm đã sửa cho hội đồng tin cậy, và nói người trồng hạ nguồn rằng chỉ số cửa lấy «trong phương sai thường».

**Đầu vào đã xác minh.** Một diễn đàn sản một phát hiện vi phạm đã xác minh → một **hồ sơ quỹ đạo vi phạm** thuần-trục mở dưới **mục 2 và 3** với chuỗi thông báo đã giữ, so sánh phòng thí nghiệm thật-với-đã-nộp, và chỉ số nhiễm cửa lấy qua hai mùa sinh trưởng. Việc tình nguyện dọn rác sau của người quản trị dọc cùng suối được định tuyến tới một **hồ sơ quỹ đạo đóng góp liên kết** dưới **mục 2.2**; nó **không** bù hồ sơ vi phạm này.

**Lượt chiều Câu hỏi 2** (hồ sơ quỹ đạo vi phạm):

| **Chiều** | **Đánh giá đã xác minh** |
| --- | --- |
| Độ lớn kết quả hiến pháp (LEQU) | Mất hiến pháp tích hợp vừa — rủi mùa, bất an nước, và chi phí sửa — dưới một LEQU bị phá |
| Phạm vi hữu tri | Ba hợp tác phụ thuộc tưới; **tính trọng yếu** nâng trong bối cảnh bất đối xứng phụ thuộc |
| Phạm vi thời gian | Nhiễm và bảo đảm sai kéo dài qua hai mùa sinh trưởng sau thông báo |
| Phạm vi không gian / thể chế | Hại lưu vực khu trú với tầm xuyên hợp tác; vai trò quản trị có trách nhiệm hợp đồng tin cậy |
| Chồng đường-hại | **Hành vi sai sinh thái** + **Hành vi sai do thiếu thận trọng** |
| Chồng tính chất hành vi | Thiếu thận trọng nơi bổn phận bảo trì tồn tại; lừa/che giấu sau thông báo |
| Đầu vào tính chất hành vi | **Lừa / che giấu / lẩn tránh**; **Kịp thời đáp / trì tránh được** (hại cộng sau bổn phận hành) |

**Đầu ra Câu hỏi 2 được ghi:** mô tả đường-hại **Hành vi sai sinh thái** và **Hành vi sai do thiếu thận trọng** xếp chồng và đầu vào tính chất hành vi che giấu. Lừa cũng được lập chỉ mục ở **mục 4.5** cho một quyết định tích hợp Câu hỏi 3 riêng; trì đáp gốc vẫn là đầu vào Câu hỏi 2, trong khi mọi trì đường khắc phục sau phải được lập riêng. **Ô Trục Vi phạm** và nhãn hiển thị được gán từ mất LEQU tích hợp dưới **[mục 7](#7-unified-proportional-lequ-scale)**.

<a id="5-slot-grammar-and-display-labels"></a>
<a id="5-slot-assignment-calibration-and-category-defaults"></a>
<a id="5-slot-grammar-and-lequ-calibration"></a>

<a id="5-slot-grammar-and-shared-scaling"></a>
### 5. Ngữ pháp ô và chia tỷ lệ chung

<a id="51-slot-grammar-and-display-labels"></a>
<a id="51-what-the-slot-grammar-does"></a>
<a id="451-what-the-slot-grammar-does"></a>
<a id="461-what-the-slot-grammar-does"></a>
<a id="471-what-the-slot-grammar-does"></a>
<a id="511-what-the-slot-grammar-does"></a>

*Nói thẳng: mục này cho tên nhất quán cho chín vị trí có thể trên mỗi trong hai trục riêng và giải thích tác động chia tỷ lệ thế nào xuyên chúng. Một trục ghi đóng góp đã xác minh; trục kia ghi vi phạm đã xác minh. Chia một số ô không gộp các trục hay bù hại bằng giúp. Thang thống nhất ở **mục 7** gán cả hai trục theo tác động LEQU tỷ lệ.*

Ngữ pháp ô dùng một số ô, `s`, từ **1** đến **9**. Mỗi trục có vị trí ô riêng:

- **Trục Đóng góp** ghi bản chất đóng góp dương; và
- **Trục Vi phạm** ghi phát hiện vi phạm đã xác minh.

Cùng số ô có thể xuất hiện trên cả hai trục, nhưng các trục vẫn riêng. Một ô đóng góp không phải ô vi phạm, và một ô vi phạm không phải ô đóng góp.

<a id="51-table-1-slot-display-labels"></a>

<a id="51-table-1--slot-display-labels"></a>
#### 5.1 Bảng 1 — nhãn hiển thị ô

**Bảng 1** đặt tên chín ô và cho nhãn hiển thị Trục Đóng góp và Trục Vi phạm cạnh nhau. Nó chỉ cung cấp ngôn ngữ hiển thị; gán ô xảy ra dưới thang thống nhất ở **mục 7**.

|  `s` | Nhãn hiển thị Trục Đóng góp | Nhãn hiển thị Trục Vi phạm |
| ---: | --- | --- |
|    1 | **Đóng góp sàn cơ bản** | **Tác động hiến pháp tối thiểu** |
|    2 | **Đóng góp sàn được củng** | **Tác động hiến pháp hạn chế** |
|    3 | **Đóng góp dương đã xác minh** | **Tác động hiến pháp có trọng** |
|    4 | **Đóng góp dương có trọng** | **Tác động hiến pháp đáng kể** |
|    5 | **Đóng góp dương quản trị có trách nhiệm đã lập** | **Tác động hiến pháp lớn** |
|    6 | **Đóng góp dương quản trị có trách nhiệm lớn** | **Tác động hiến pháp nghiêm** |
|    7 | **Nhà tiên phong được ghi nhận** | **Tác động hiến pháp nghiêm trọng** |
|    8 | **Nhà tiên phong xuất chúng** | **Tác động hiến pháp nặng** |
|    9 | **Nhà tiên phong mẫu mực** | **Tác động hiến pháp thảm họa** |

Trục Đóng góp dùng nhãn sàn, dương, dương quản trị có trách nhiệm, và tiên phong. Trục Vi phạm dùng nhãn tác động trung tính ở mọi ô. Các trục vẫn riêng và không tạo điểm ròng hay cho phép bù giữa hồ sơ đóng góp và vi phạm. Một ô Trục Vi phạm không tự phân loại hành vi sai phản hiến pháp; [Chương Mười](../../core_11_a_misconduct_designation.md#chapter-eleven-anti-constitutional-misconduct) độc lập quyết liệu chỉ định đó gắn vào một vi phạm `s` = 7–9 đã xác minh.

Triển khai có thể công bố đơn vị đo, phương pháp bằng chứng, và ví dụ để giúp ước lợi hoặc mất tương đương cả đời. Những tư liệu đó chỉ là hướng dẫn và không được ghi đè **mục 7**, **Chương Một**, hoặc Sàn Quyền **Chương Sáu**.

<a id="51-standard-contribution-measures"></a>

**Thước đóng góp chuẩn.** Triển khai đã tiếp nhận cũng có thể công bố **thước đóng góp chuẩn**: một ước Câu hỏi 2 mặc định — LEQU, phạm vi, và mô tả đường-lợi — cho hiệu năng đã xác minh của một việc lặp đã định ở một phạm vi đã định, như nhặt rác dọc một đoạn đã nêu, một đơn vị việc phục hồi đường nước, một thửa khôi đất, hoặc một vòng bảo trì. Chuẩn làm quản trị có trách nhiệm thường đọc được và đáng lặp dưới [Chương Một §2.2](core_01_a_values_principles.md#22-recognition-reinforcement-and-aspiration) (*Ghi nhận, củng, và khát vọng*) mà không cần ước riêng cho mọi lần. Một chuẩn là trợ thủ đo lường dưới **mục 3.5**, và:

- nó chỉ áp cho việc đã xác minh dưới Câu hỏi 1 qua **mục 3.7**; một chuẩn không bao giờ thế xác minh việc đã được làm, tới phạm vi đã nêu, bởi đối tượng đã đặt tên;
- nó là **sàn cho hiệu năng chuẩn, không phải trần**: việc có tác động đã xác minh vượt tác động giả định của chuẩn — phương pháp tốt hơn, kết quả bền hơn, gánh ngoại hóa ít hơn, lợi rộng hơn hoặc sâu hơn — được đo trên tác động đã xác minh thực dưới **mục 5.2**, nên khuyến khích làm việc tốt hơn chuẩn vẫn sống; việc xác minh được là thiếu phạm vi hoặc độ bền giả định của chuẩn được đo trên điều đã xác minh, không trên nhãn;
- nó được **xem lại theo nhịp đã công bố và đặt lại đường cơ sở khi hiệu quả cải**, nên chuẩn theo điều việc hiện tốn và sản chứ không đóng băng nỗ lực hôm qua thành tín dụng hôm nay; một sửa áp về phía trước, và hồ sơ đã mở giữ cơ sở đo lường dưới **mục 3.4** trừ khi cơ sở đó sai lúc ghi;
- một sửa phải dựa bằng chứng, được công bố, và tranh biện được, và không được dùng để dập ghi nhận một lớp việc, một cộng đồng, hoặc một nhóm, hoặc siết chuẩn xuống nhanh hơn lợi hiệu quả đã xác minh nó tựa ([Chương Một §11](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture));
- một chuẩn không tạo hạn ngạch, không bổn phận thực hiện, và không thanh năng lực dưới [Chương Chín §6.2](../../core_10_standing_integration.md#62-competency-bars-and-clearances); **mục 2.1** *Im lặng là mặc định* kiểm soát, và một hữu tri không bao giờ làm một việc chuẩn không có hồ sơ vì lý do đó;
- văn phòng đặt hoặc sửa một chuẩn giữ ghế hướng-và-chính-sách dưới **mục 3.7** *Phân tách nhiệm vụ*; nó không phải văn phòng xác minh hiệu năng đối với chuẩn, và không cái nào là bên mà ghi nhận chuẩn đo.

Chuẩn không được ghi đè **mục 7**, **Chương Một**, hoặc Sàn Quyền **Chương Sáu**. Một phương pháp tham chiếu và lịch đã làm nằm ở [LEQU_CALIBRATION_REFERENCE.md](../../implementation/LEQU_CALIBRATION_REFERENCE.md) (*hỗ trợ quy trình; không thể gán một hồ sơ sống*).

<a id="52-shared-impact-scaling-rules"></a>

#### 5.2 Quy tắc chia tỷ lệ tác động chung

*Nói thẳng: tác động không được đo chỉ bằng số đầu. Một lợi hoặc mất sâu ảnh hưởng một hữu tri có thể có ý nghĩa hơn một hiệu ứng nông ảnh hưởng nhiều người. Số, độ sâu, dễ tổn, kéo dài, bền, tầm, và tính chất hiến pháp phải được đánh cùng.*

Dùng các quy tắc sau để diễn giải cả hai trục ở **mục 7**:

| Chiều chia tỷ lệ | Quy tắc chung | Áp dụng riêng-trục |
| --- | --- | --- |
| **Độ lớn kết quả hiến pháp (LEQU)** | Đánh lợi hoặc mất đã xác minh đã tích hợp. LEQU là neo độ lớn sơ cấp; số đầu thô, tiền, sản lượng, hoặc cỡ thể chế thì không. | Đóng góp đếm lợi khớp quyền; vi phạm đếm mất, hại, lãng, đóng cửa, hoặc nguy hiến pháp đã xác minh. |
| **Phạm vi hữu tri** | Xét **số, độ sâu, và dễ tổn cùng**. Không ô nào dùng số đầu như yêu cầu độc lập. Một tác động đủ sâu trên một hữu tri có thể nâng cùng ô như một tác động rộng hơn nhưng nông hơn nơi độ lớn tích hợp và tiêu chí khác của hàng bằng nhau; mọi tiêu chí LEQU-tổng hoặc phạm-vi-rộng rõ vẫn phải được thỏa. | Phụ thuộc, năng lực giảm, hoặc dễ tổn bất thường có thể tăng tính trọng yếu. Cỡ nhóm một mình không lập đóng góp hay mức nghiêm. |
| **Phạm vi thời gian** | Xét kéo dài, tái diễn, bền, và, với mất, không đảo ngược. Một sự kiện ngắn nhưng biến đổi có thể nặng hơn một hiệu ứng dài tầm thường; kéo dài một mình không kiểm. | Lợi bền nâng độ lớn đóng góp cao hơn. Mất bền hoặc không đảo ngược nâng mức nghiêm vi phạm cao hơn. |
| **Phạm vi không gian hoặc thể chế** | Tầm rộng hơn có thể tăng độ lớn, nhưng tầm xuyên cộng đồng hoặc xuyên thể chế không đòi nơi độ sâu, kéo dài, dễ tổn, hoặc tính then chốt hiến pháp độc lập nâng ô. | Sửa thể chế có thể tăng độ lớn đóng góp; hại cấu trúc hoặc hệ thống có thể tăng mức nghiêm vi phạm. |
| **Chất lượng hoặc tính chất hiến pháp** | Đo kết quả được sản thế nào riêng khỏi nó lan rộng thế nào. Đừng đếm hai lần cùng sự kiện. | Hại ngoại hóa, gánh che, chiếm, hoặc phụ thuộc có thể trần hoặc loại đóng góp tuyên. Bổn phận, thiếu thận trọng, lừa, cưỡng, bạo lực, hoặc mở đường cấu trúc vẫn được ghi riêng như tính chất hành vi vi phạm và không dịch ô tác động. |
| **Sàn Quyền và bảo vệ then chốt** | Tuân Sàn Quyền không được đổi lấy lợi hoặc mất tổng. | Tuân một sàn không tự lập đóng góp cao. Đánh bại Sàn Quyền có trọng hoặc thất bảo vệ then chốt có thể nâng mức nghiêm vi phạm cao hơn dù ít hữu tri bị ảnh hưởng trực tiếp. |

Các chiều không phải danh sách kiểm đòi mọi dạng quy mô. Giải thích chiều nào kiểm, chiều nào không, và vì sao.

- **Phương pháp ô chung:**
  - Ước lợi hoặc mất đã xác minh đã tích hợp bằng LEQU dưới Tính tương xứng, rồi gán một ô có dải số chứa độ lớn đó.
  - Cùng ngưỡng áp trên cả hai trục.
  - Ô đóng góp giữ yêu cầu sàn và thẳng hàng hiến pháp áp dụng; thỏa một ngưỡng số không thể làm sản lượng ngoại hóa hoặc bị đánh bại hiến pháp đếm như đóng góp.
- **Tách tính chất:** Giữ mô tả đường-lợi, đường-hại, chất lượng hành vi, và tính chất hành vi áp dụng xếp chồng trong hồ sơ. Bổn phận, thiếu thận trọng, lừa, tăng nặng, cưỡng, bạo lực, ý định, hoặc mở đường cấu trúc có thể ảnh hưởng gán, bảo vệ, hoặc hệ quả Câu hỏi 3, nhưng không cái nào nâng hoặc hạ ô tác động LEQU.
- **Ranh giới Rà soát hành vi sai phản hiến pháp:** Mất Trục Vi phạm đã xác minh có thể tới `s` = 7–9 theo tác động dù hành vi sai phản hiến pháp có được lập hay không. Chương Mười không thế gán tác động; nó độc lập quyết liệu chỉ định hành vi sai phản hiến pháp tương ứng gắn.

Với nguy chưa hiện, ghi xác suất, thời kéo phơi, phạm vi bị ảnh hưởng, bất định, và kết quả đáng tin xấu nhất riêng. Đừng coi kết quả đáng tin xấu nhất như mất LEQU đã hiện mà không có hiệu chỉnh rủi trong suốt đã tiếp nhận.

<a id="6-constitutional-inputs-to-axis-assignment"></a>

### 6. Đầu vào hiến pháp cho gán trục

*Nói thẳng: trước khi chọn ô, nhận diện nguồn hiến pháp nói sàn, lợi, bổn phận, hại, hoặc vi phạm nào đang được đo. Dùng các liên kết dưới để áp những nguồn đó tại nhà chuẩn của chúng; đừng biến bước định tuyến này thành một điểm khác hay một định nghĩa thay.*

Trước khi gán một ô dưới **mục 7**, hồ sơ quỹ đạo phải nhận diện:

- sàn, bổn phận, ràng buộc, hoặc lợi ích được bảo vệ hiến pháp áp dụng;
- các điều khoản lập lợi, kết quả bất lợi, hại, hoặc vi phạm đã xác minh đang được đo;
- các định nghĩa, nguyên tắc, và Điều Sàn Quyền ảnh hưởng có trọng độ lớn hoặc tính chất hành vi; và
- vì sao mỗi nguồn được nhận diện áp và nó ảnh hưởng gán trục thế nào.

Các bảng định tuyến dưới không đầy đủ. Mọi định nghĩa, nguyên tắc, hoặc Điều thêm được sự kiện đã xác minh cò vẫn áp dụng và phải được nhận diện trong hồ sơ quỹ đạo. Mỗi nhà chuẩn được liên kết kiểm soát; những bảng này không nêu lại hay thu hẹp nó.

<a id="61-definition-inputs"></a>

#### 6.1 Đầu vào định nghĩa

| Nguồn chuẩn | Vai trò Trục Đóng góp | Vai trò Trục Vi phạm |
| --- | --- | --- |
| [Trạng thái quỹ đạo, đóng góp, và vi phạm](core_05_band_accountability.md#standing-state-contribution-and-violation-cluster) | Cung cấp giao diện định nghĩa chung cho bản chất đóng góp, đầu vào đã xác minh, và hồ sơ quỹ đạo thuần-trục. | Cung cấp giao diện định nghĩa chung cho bản chất vi phạm, hồ sơ quỹ đạo, và định tuyến Rà soát hành vi sai phản hiến pháp. |
| [Trách nhiệm giải trình](core_05_apex_accountability_leg.md#accountability) | Thử liệu quản trị có trách nhiệm hoặc sửa tuyên có giữ gán, phải trả lời, rà soát, khắc phục, và sửa tỷ lệ với tác động không. | Nhận diện thất gán và phải trả lời, kể cả liệu trách nhiệm vẫn chức năng qua đổi tổ chức hoặc cấu trúc hình thức. |
| [Hại](core_05_band_accountability.md#harm) | Hại ngoại hóa hoặc che có thể trần hoặc loại lợi tuyên; sửa hại đã xác minh có thể nâng lợi khi được chứng minh độc lập. | Định nghĩa hiệu ứng bất lợi trực tiếp, gián tiếp, trễ, tích lũy, xuyên hệ thống, và qua trung gian tâm lý vào đo mất và mức nghiêm. |
| [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) và [Đơn vị tương đương tuổi thọ (LEQU)](core_05_band_participation.md#lifespan-equivalent-unit-lequ) | Chia tỷ lệ lợi đã xác minh, phạm vi, dễ tổn, kéo dài, và hiệu chỉnh LEQU áp dụng. | Chia tỷ lệ mất, nguy đã xác minh, phạm vi, dễ tổn, kéo dài, không đảo ngược, và hiệu chỉnh LEQU áp dụng. |
| [Bản chất đóng góp](core_05_band_accountability.md#contribution-nature) | Cung cấp phân loại chỉ-dương và cơ sở hồ sơ đóng góp đã xác minh chứng minh được đòi cho một gán Trục Đóng góp. | Không phân loại phát hiện bất lợi hay giảm mức nghiêm vi phạm. |
| [Bản chất vi phạm](core_05_band_accountability.md#violation-nature-chapter-six) | Không trở thành đóng góp âm và không xóa lợi đã xác minh không liên quan. | Cung cấp phân loại bất lợi và cơ sở phát hiện vi phạm đã xác minh đòi cho một gán Trục Vi phạm. |
| [Ràng buộc hiến pháp](core_05_band_integrative.md#constitutional-constraint), [Chồng thẩm quyền và thứ bậc nội bộ](core_05_band_integrative.md#authority-stack), và [Khả năng kiểm toán](core_05_band_oversight.md#auditability) | Ngăn lợi tuyên tựa trên đánh bại hiến pháp, lẩn tránh, Sàn Quyền thu hẹp, hoặc tuân chỉ-giấy. | Nhận diện đánh bại ràng buộc, hiệu ứng tối thượng, chống lẩn tránh, hoặc cưỡng chế có trọng liên quan mức nghiêm thực chất. |
| [Khả năng kiểm toán](core_05_band_oversight.md#auditability) và [Khả năng tranh biện](core_05_band_accountability.md#contestability) | Đòi lợi chứng minh được, rà soát được và một đường tranh biện chức năng. | Đòi phát hiện kiểm toán được, tranh biện được và ngăn cáo buộc hoặc nhãn mờ cung cấp mức nghiêm. |

<a id="62-principle-inputs"></a>

#### 6.2 Đầu vào nguyên tắc

| Nguồn nguyên tắc | Vai trò gán trục |
| --- | --- |
| [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad), [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims), và [lợi hại vật chất](core_00_preamble.md#material-stake) | Lập kỷ luật tham gia, giám sát, trách nhiệm giải trình, và kịp thời; kết quả Hưng thịnh và Liên tục; và khung chia tỷ lệ cho mọi gán. |
| [Phúc lợi](core_01_a_values_principles.md#2-foundational-objective-wellbeing) và [Ghi nhận, củng, và khát vọng](core_01_a_values_principles.md#22-recognition-reinforcement-and-aspiration) | Nền lợi khớp quyền và ghi nhận tỷ lệ trên Trục Đóng góp mà không biến uy tín hay thưởng thành chứng đóng góp. |
| [An toàn](core_01_a_values_principles.md#31-safety-harm-constraint) và [Sự thật](core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint) | Giới hạn cả hai trục: lợi sản qua hại hoặc lừa không đếm đầy, và đánh bại an toàn hoặc sự thật đã xác minh có thể lập độ lớn hoặc tính chất bất lợi. |
| [Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding) và [Quản trị dưới kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline) | Thông tin đóng góp bền, bổn phận gắn vai trò, sửa thể chế, giám sát, và trách nhiệm nơi sự kiện đã xác minh cò những nguyên tắc đó. |
| [Nguyên tắc đánh đổi cốt](core_01_b_interaction_interpretation.md#61-core-tradeoff-principles) và [Sàn hiến pháp, an toàn, và ràng buộc tính chất quy trình](core_01_b_interaction_interpretation.md#614-constitutional-floors-safety-and-process-character-constraints) | Áp nơi hành vi được đo viện sự cần, giảm thiểu hại, tính tương xứng, va chạm quyền, hoặc hạn chế; chúng không độc lập ủy một hệ quả. |

<a id="63-rights-floor-and-article-inputs"></a>

#### 6.3 Đầu vào Sàn Quyền và Điều

| Nguồn Điều | Vai trò gán trục hoặc ranh giới |
| --- | --- |
| [Sàn Quyền Chương Sáu](core_06_rights_part_a.md#chapter-six-foundational-rights) áp dụng theo sự kiện, kể cả mọi Điều bị hồ sơ đã xác minh liên lụy có trọng | Lập sàn thực chất, lợi ích được bảo vệ, bổn phận, lợi, hoặc vi phạm. Không Điều nào bị loại vì không được liệt riêng dưới đây. |
| [Điều XVIII — Quỹ đạo và trạng thái tham gia](core_06_rights_part_c.md#article-xviii-standing-and-participation-status) | Giữ phân biệt giữa quỹ đạo, phẩm giá, tối thiểu Sàn Quyền, trạng thái bên bị ảnh hưởng, danh tiếng, và hiệu ứng trạng thái tham gia sau. |
| [Điều XII-B — Quyền tranh biện, rà soát, và khắc phục](core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress), [Điều XIV-B — Minh bạch, khả năng kiểm toán, và khả năng tranh biện](core_06_rights_part_c.md#article-xiv-b-transparency-auditability-and-contestability), và [Điều XV — Kiểm toán, minh bạch, và xác minh độc lập](core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification) | Áp nơi toàn vẹn hồ sơ, công bố, xác minh, lối vào tranh biện, hoặc sửa là phần của lợi hoặc vi phạm đã xác minh. |
| [Điều XXI — Phân tích nguyên nhân gốc và đáp thích nghi](core_06_rights_part_c.md#article-xxi-root-cause-analysis-and-adaptive-response) | Áp nơi gán nhân quả, sửa, tái diễn, hoặc đáp thích nghi có trọng với hành vi đã xác minh và tính chất hiến pháp của nó. |
| [Điều XXIII — Giải quyết xung đột, leo thang, và tính tương xứng khẩn](core_06_rights_part_d.md#article-xxiii-conflict-resolution-escalation-and-emergency-proportionality) và [Điều XXIV-C — Sàn giải quyết kịp thời và chống trì hoãn](core_06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor) | Áp cho mọi quy trình hoặc trì bị sự kiện liên lụy. Điều XXIII chủ yếu ràng hệ quả Câu hỏi 3 và không được dùng để nâng hoặc hạ một ô Câu hỏi 2 chỉ để biện minh một đáp ưa thích. |

**Giới hạn áp dụng.** Bước định tuyến này không mở lại Câu hỏi 1, nhận sự kiện chưa xác minh, thêm một chiều đo hay điểm, đếm hai lần một sự kiện qua nhiều nguồn, gộp các trục, hoặc làm mọi nguồn liệt áp cho mọi hồ sơ. Đóng góp và vi phạm vẫn được đo riêng. Hệ quả Điều XXIII vẫn ngoài Câu hỏi 2. Rà soát chỉ định Chương Mười vẫn riêng khỏi ô tác động được gán ở đây.

<a id="7-unified-proportional-lequ-scale"></a>

<a id="7-unified-proportional-lequ-scale--contribution-and-violation-axes"></a>
### 7. Thang LEQU tỷ lệ thống nhất — Trục Đóng góp và Trục Vi phạm

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): cấp số nhân năm lần làm việc thế nào</span></strong></summary>

> Hướng dẫn này giúp người đọc diễn giải thang. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc.
>
> Thang dùng cấp số nhân năm lần neo tại `s` = 7 = một LEQU. Với mỗi trục, độ lớn tối thiểu cho ô `s` là `5^(s−7)` LEQU cho ô 2 đến 9; ô 1 bắt đầu tại không. Triển khai đã tiếp nhận có thể công bố ngưỡng số kết quả và ví dụ hiệu chỉnh. Ô 1 gồm một sàn hiến pháp đã xác minh trên Trục Đóng góp và mất đã xác minh dưới ngưỡng dương đầu trên Trục Vi phạm; vắng đóng góp hoặc vắng vi phạm không tự là một hồ sơ `s` = 1.
>
> **Neo đọc được.** Dùng một đời người 80 năm làm ví dụ hiệu chỉnh, đọc cột giữa lên như lợi tương đương cả đời, thời gian dùng được, hoặc tài nguyên và năng lực khớp quyền được thêm; đọc xuống như mất, tước, lãng, hoặc đóng cửa tương đương. Số lượng tài nguyên không đếm tự nó — kết quả hiến pháp nó sản hoặc ngăn kiểm soát.

</details>

<br>

*Nói thẳng: **Bảng 2** đặt đóng góp đã xác minh và vi phạm đã xác minh trên cùng thang tác động tỷ lệ. Ô cao hơn nghĩa là lợi hoặc mất hiến pháp tích hợp lớn hơn. Hồ sơ và trục vẫn riêng: thang chung so sánh độ lớn, không phải giá trị đạo đức, và không bao giờ cho phép giúp hủy hại.*

Áp **Tính tương xứng** để ước tác động LEQU tích hợp từ độ sâu, phạm vi hữu tri, dễ tổn, kéo dài, bền hoặc không đảo ngược, tầm, và tính then chốt hiến pháp. Những chiều này định hình ước LEQU; chúng không phải thưởng ô độc lập.

- Dùng **Bảng 2** sau khi Câu hỏi 1 xác nhận điều đã xảy ra, Câu hỏi 2 đo lợi hoặc mất đã xác minh, **mục 4 và 5.2** được áp, và nguồn hiến pháp đòi bởi **mục 6** được nhận diện.
- Gán một ô từ ước LEQU tích hợp.
  - Giải thích mỗi chiều chia tỷ lệ có trọng ảnh hưởng ước thế nào và vì sao chiều bỏ không kiểm.
  - Mọi gán phải thỏa:
    - truy vết;
    - khả năng kiểm toán;
    - khả năng tranh biện; và
    - Sàn Quyền áp dụng.
  - Đóng góp cũng phải thỏa không ngoại hóa và thẳng hàng hiến pháp.
- Ghi sự kiện tính chất hành vi như mô tả truy vết riêng. Chúng có thể kiểm gán, cường độ rà soát, bảo vệ, khắc phục, hoặc một chỉ định Chương Mười; chúng ảnh hưởng ô chỉ đến mức hệ quả đã xác minh đổi tác động LEQU tích hợp.
- Đánh đầy hệ quả đã xác minh của hành động hoặc chuỗi hành vi qua các chiều chia tỷ lệ có trọng, kể cả:
  - thương tích thân thể;
  - chấn thương tâm lý;
  - hiệu ứng cưỡng;
  - tước hoặc nguy tự do;
  - hại tích lũy; và
  - lợi hoặc mất hiến pháp nhận diện được khác.
- Đừng:
  - Nâng hoặc hạ ô chỉ vì một sự kiện hoặc chuỗi hành vi được mô tả bởi:
    - bổn phận;
    - thiếu thận trọng;
    - ý định;
    - che giấu;
    - lặp;
    - tăng nặng;
    - cưỡng;
    - bạo lực;
    - nguy tự do;
    - khả năng sửa; hoặc
    - một hệ quả ưa thích.
  - Suy tính chất hành vi từ độ lớn hoặc thế tính chất hành vi cho độ lớn đã xác minh.

| `s` | Hiệu chỉnh người 80 năm — lợi thêm / mất áp | Trục Đóng góp | Trục Vi phạm |
| ---: | --- | --- | --- |
| 1 | Dưới khoảng **9 ngày** | **Đóng góp sàn cơ bản** — thỏa sàn hiến pháp đã xác minh cho phạm vi được đánh; mọi nâng đo được vẫn dưới `s` = 2. | **Tác động hiến pháp tối thiểu** — mất hoặc suy vận hành đã xác minh dưới `s` = 2, kể cả khuyết hình thức không hại thực chất đã chứng. |
| 2 | Khoảng **9–47 ngày** | **Đóng góp sàn được củng** — hiệu năng tin cậy, có giới hạn trên sàn tối thiểu trong mức tác động này. | **Tác động hiến pháp hạn chế** — mất có giới hạn đã xác minh ở mức tác động này. |
| 3 | Khoảng **47 ngày–8 tháng** | **Đóng góp dương đã xác minh** — lợi chứng minh được vượt sàn ở mức tác động này. | **Tác động hiến pháp có trọng** — mất có trọng đã xác minh ở mức tác động này. |
| 4 | Khoảng **8 tháng–3,2 năm** | **Đóng góp dương có trọng** — lợi đã xác minh sâu hơn, bền hơn, lặp, đáp dễ tổn, hoặc rộng hơn. | **Tác động hiến pháp đáng kể** — mất hiến pháp đáng kể đã xác minh. |
| 5 | Khoảng **3,2–16 năm** | **Đóng góp dương quản trị có trách nhiệm đã lập** — quản trị có trách nhiệm bền, phối hợp, bảo trì, sửa, hoặc lợi bền sánh. | **Tác động hiến pháp lớn** — mất hiến pháp lớn đã xác minh. |
| 6 | Khoảng **16–80 năm** | **Đóng góp dương quản trị có trách nhiệm lớn** — lợi đã xác minh lớn gần một LEQU. | **Tác động hiến pháp nghiêm** — mất đã xác minh nghiêm gần một LEQU. |
| 7 | Khoảng **1–5 đời** (**80–400 năm**) | **Nhà tiên phong được ghi nhận** — ít nhất một LEQU lợi đã xác minh, thẳng hàng hiến pháp. | **Tác động hiến pháp nghiêm trọng** — ít nhất một LEQU mất hiến pháp đã xác minh. |
| 8 | Khoảng **5–25 đời** (**400–2.000 năm**) | **Nhà tiên phong xuất chúng** — lợi đã xác minh vượt `s` = 7 có trọng. | **Tác động hiến pháp nặng** — mất đã xác minh vượt `s` = 7 có trọng. |
| 9 | Ít nhất **25 đời** (**2.000+ năm**) | **Nhà tiên phong mẫu mực** — lợi đã xác minh vượt `s` = 8 có trọng. | **Tác động hiến pháp thảm họa** — mất đã xác minh vượt `s` = 8 có trọng. |

<details>
<summary><strong><span style="color: #2563eb;">Ghi chú tương tác triển khai</span></strong></summary>

> Widget này chứa tư liệu tương tác hướng triển khai. Nó nâng các hạng vận hành của chương; nó không tạo một hệ hạng song song.

Trường máy-đọc được cho hiển thị ô (`sub_tier`, `sub_tier_display`, và trường hiển thị liên quan) được định nghĩa ở [CH06_NINE_SLOT_STANDING_SCALE.md](../../implementation/CH06_NINE_SLOT_STANDING_SCALE.md) và [ch06_nine_slot_constants.json](../../implementation/ch06_nine_slot_constants.json). Bản đồ bốn dải triển khai vẫn là trợ thủ tương tác và không thêm cột dải sơ cấp vào **Bảng 2** vận hành.

Một phương pháp tham chiếu và gán ô đã làm, kể cả cho hữu tri có trọng số, điểm kiểm trạng thái đã lưu, và không tử vong cố định, nằm ở [LEQU_CALIBRATION_REFERENCE.md](../../implementation/LEQU_CALIBRATION_REFERENCE.md). Những phép đó không thể thế ngưỡng chung và quy tắc gán tỷ lệ ở **mục 7**, không thể gán một hồ sơ sống, và không thể quyết ai được tính.

Triển khai đã tiếp nhận có thể công bố ước LEQU và nhãn hiển thị có khóa. Những trợ thủ đó không được thế ngưỡng chung và quy tắc gán tỷ lệ ở **mục 7** hoặc bảo vệ chỉ định Chương Mười, trừ qua một đổi **văn kiện khớp**.

</details>

---

**Tiếp.** Hiệu ứng quỹ đạo và tích hợp tiếp ở [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration), bắt đầu với **mục 1 — Hiệu ứng quỹ đạo**.

---

**Tệp trước (ngôn ngữ này):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)

**Tệp tiếp theo (vẫn tiếng Anh):** [core_09_standing_integration.md](../../core_10_standing_integration.md)

**Nguyên bản ràng buộc:** [core_08_standing_assessment.md](../../core_09_standing_assessment.md)




