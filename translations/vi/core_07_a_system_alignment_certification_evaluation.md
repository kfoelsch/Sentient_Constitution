<a id="chapter-seven-system-alignment-certification"></a>
<a id="chapter-seven-system-alignment-certification-and-recognition"></a>
<a id="chapter-seven-part-a-certification-evaluation"></a>
<a id="chapter-seven-part-a-system-alignment-certification--evaluation"></a>
# CHƯƠNG BẢY, PHẦN A: CHỨNG NHẬN THẲNG HÀNG HỆ THỐNG — ĐÁNH GIÁ

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Bảy, Phần A tiếng Anh](../../core_08_a_system_alignment_certification_evaluation.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_07_a_system_alignment_certification_evaluation.md`](../../core_08_a_system_alignment_certification_evaluation.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> Nó chứa **Chương Bảy, Phần A** — yêu cầu **đánh giá** chứng nhận (lớp hệ thống, yếu tố toàn hệ thống, và móc đánh giá lĩnh vực). **Phần B** — hồ sơ chứng nhận, quy trình diễn đàn, cầu quỹ đạo, và mở lại — nằm ở [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md).
>
> - **Chủ sở hữu hiến pháp (chung với Phần B):** **chứng nhận thẳng hàng hệ thống và hồ sơ liên quan** được diễn đàn giám sát — miền đánh giá (Phần A); nghĩa vụ hồ sơ chứng nhận, kết quả công nhận, nhịp tái xác nhận, trình tự giám sát, chuỗi khả năng tranh biện, và cầu đầu vào đã xác minh tới Chương Tám (Phần B). Dưới trụ **giám sát** của Tứ diện, SAC là một quy trình kiểm toán đặc biệt lớn, lợi hại cao giữa các quy trình khác; sàn kiểm toán vẫn ở **Điều XV** và [Khả năng kiểm toán](core_05_band_oversight.md#auditability) của Chương Năm.
> - **Chủ sở hữu nền xác minh:** [Chương Bốn — Gánh chứng minh, truy vết, và xác minh](core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (trong các Chương Hai đến Bốn) nắm phân bổ gánh, bằng chứng tuân thủ, truy vết định nghĩa, khả năng quan sát, và xác minh dưới giới hạn an ninh. Chương Bảy **áp dụng** kỷ luật đó cho hồ sơ chứng nhận thẳng hàng hệ thống; nó **không** nêu lại các mục **1** đến **5** của Chương Bốn.
> - **Nhà kiểm toán (không dời tới đây):** **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*), **Def.O1** (*Minh bạch, khả năng kiểm toán, và xác minh*), và **CJS-3.3**–**CJS-3.5** nắm sàn kiểm toán và thuật ngữ vận hành. Chương Bảy chạy một quy trình kiểm toán SAC đặc biệt lớn phải thỏa những sàn đó; nó không nắm mọi kiểm toán.
> - **Chủ sở hữu triển khai:** xử lý lớp hệ thống, CS-5, và chi tiết quy trình diễn đàn trong các tệp triển khai được chỉ định phải giữ nhất quán với Chương Bảy và có thể nghiêm hơn nơi kho văn bản đã cung cấp logic quy tắc nghiêm hơn.
> - **Quy tắc chống dời chỗ:** Phần A không nêu lại định nghĩa chuẩn Chương Năm, kỷ luật chống lẩn tránh Chương Ba (xem [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)), đo lường đóng góp hoặc quỹ đạo Chương Tám, hay hiệu ứng quỹ đạo Chương Chín. **[Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)** nêu rõ ranh giới cầu quỹ đạo.
>
> **Thượng nguồn:** định nghĩa Chương Năm và hồ sơ, xác minh, gánh, và truy vết định nghĩa tới kết quả của các Chương Hai đến Bốn.
> **Hạ nguồn:** [Phần B](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) (*hồ sơ, quy trình diễn đàn, và cầu quỹ đạo*); hồ sơ quỹ đạo và đầu vào đã xác minh của Chương Tám; hiệu ứng quỹ đạo của Chương Chín; giám sát diễn đàn và đường dẫn chứng nhận thẳng hàng hệ thống của Chương Mười Một.
>
> **Cửa quản trị có trách nhiệm (không vận hành):** Tuyên bố bước tiếp ràng buộc: [Tuyên bố quản trị có trách nhiệm mang tính vận hành](#operative-steward-statement-sac). Các con trỏ hỗ trợ trong [`implementation/STEWARD_ENTRY_DOORS.md`](../../implementation/STEWARD_ENTRY_DOORS.md) không thể thu hẹp nó.

>
> **Trước (ngôn ngữ này):** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)
>
> **Tiếp theo (ngôn ngữ này):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)
> **Cung đọc:** §1 mục đích và vai trò → §2 lớp hệ thống → §3 đánh giá toàn hệ thống → §4–§10 đánh giá lĩnh vực

</details>

<br>

Chương Bảy, **Phần A**, là chủ sở hữu hiến pháp của **đánh giá chứng nhận thẳng hàng hệ thống**. Nội dung hồ sơ, giám sát diễn đàn, đường tranh biện, và cầu quỹ đạo nằm ở **[Phần B](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)**.

<a id="operative-steward-statement-sac"></a>
> **Tuyên bố quản trị có trách nhiệm mang tính vận hành.** **Chủ trì:** Chương Bảy (SAC được diễn đàn giám sát). Lăng kính tầng nguyên tắc: Chương Một §14. SAC là một quy trình kiểm toán đặc biệt lớn dưới Điều XV / Khả năng kiểm toán — không phải kiểm toán duy nhất. **Động thái bị cấm:** Đừng coi thử đơn vị, danh sách kiểm quyền riêng tư, hay nhãn thẳng hàng địa phương là chứng nhận. Đừng bỏ cửa sổ tranh biện. Đừng bịa nhà kiểm toán thứ năm. Đừng coi phù hiệu chứng nhận hay điểm LEQU là trạng thái hữu tri. **Đồng hồ:** Mở hoặc khôi một đường Chương Bảy tranh biện được, kể cả cửa sổ tranh biện của bên bị ảnh hưởng, trước tuyên thẳng hàng.

<a id="1-purpose-and-role"></a>
### 1. Mục đích và vai trò

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Lời nói đầu — sổ đăng ký chủ sở hữu hiến pháp](core_00_preamble.md#4-principles-definitions-and-rights) và [Chồng thẩm quyền và thứ bậc nội bộ](core_05_band_integrative.md#authority-stack); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [Tính tương xứng](core_05_band_accountability.md#proportionality) và [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) (Chương Năm); Gia đình đo lường Tham gia (*tiếng nói, lối vào, và đường tranh biện*); [Chương Một §9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding); [Chương Một §14 Yêu cầu đánh giá hệ thống](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement) (*lăng kính đánh giá toàn hệ thống tầng nguyên tắc — không một góc một mình*); Chương Hai đến Bốn; [Chương Năm](core_05__definitions_home.md#chapter-five-foundational-definitions) (*định nghĩa chuẩn*); [Chứng nhận thẳng hàng hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) (thuật ngữ chuẩn Chương Năm; viết tắt không vận hành **SAC**); [Hồ sơ chứng nhận hệ thống](core_05_band_continuity.md#system-certification-record-constitutional) (nghĩa Chương Năm).
- Hạ nguồn: [§2](#2-system-class-evaluation) và [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*đánh giá lớp hệ thống và hồ sơ minh họa*); [§3.8](#38-illustrative-whole-system-application-by-class) (*ví dụ toàn hệ thống đã làm theo lớp*); [§4.1](#41-illustrative-data-handling-application-by-class) (*ví dụ xử lý dữ liệu đã làm theo lớp*); [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*ví dụ dấu chân sinh thái đã làm theo lớp*); [§6.1](#61-illustrative-cross-system-support-application-by-class) (*ví dụ hỗ trợ xuyên hệ thống đã làm theo lớp*); [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*ví dụ không phân biệt đối xử đã làm theo lớp*); [§8.1](#81-illustrative-accessibility-application-by-class) (*ví dụ khả năng tiếp cận đã làm theo lớp*); [§9.1](#91-illustrative-educational-capability-application-by-class) (*ví dụ năng lực giáo dục đã làm theo lớp*); [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ví dụ đáng tin cậy đã làm theo lớp*); [§3](#3-whole-system-certification-evaluation) (*yếu tố đánh giá chứng nhận toàn hệ thống*); [§4](#4-data-types-and-handling-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) (*đánh giá lĩnh vực*); [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ chứng nhận*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*yêu cầu tính toàn vẹn hồ sơ*); [Phần B §13](core_07_b_system_alignment_certification_record_process.md#13-forum-supervision-and-component-roles) (*vai trò thành phần diễn đàn*); [Phần B §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain) (*trình tự giám sát và chuỗi khả năng tranh biện*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cầu hồ sơ quỹ đạo*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*mở lại và chống lẩn tránh*); [Chương Tám](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) (*hồ sơ quỹ đạo và cổng đầu vào đã xác minh*); [Chương Chín](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*hiệu ứng quỹ đạo và tích hợp*); [Chương Mười Một](core_11_forum.md#chapter-eleven-forums-and-jurisdiction) (*giám sát diễn đàn, chứng nhận, công nhận thẳng hàng, và rà soát*).
- Đọc cùng: [corpus_systems.md](../../corpus_systems.md), nhất là **CS-3 — Phân hạng hệ thống và xử lý**, **CS-2 — Loại thông tin và xử lý**, và **CS-5**; [corpus_forum.md](../../corpus_forum.md), nhất là **CF-5** (*Vận hành định tuyến, chuyển, chứng nhận, và đối xử đại diện*) và **CF-7** (*Bảo vệ tính toàn vẹn, vận hành chống chiếm, và hỗ trợ chống tự xét*); **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*) và [Khả năng kiểm toán](core_05_band_oversight.md#auditability) (*sàn kiểm toán — SAC là một quy trình kiểm toán đặc biệt lớn dưới giám sát, không phải nhà kiểm toán duy nhất*); **CJS-3.3**–**CJS-3.5** (*thuật ngữ khả năng kiểm toán, lối vào kiểm toán, và xác minh độc lập*).

</details>

<br>

*Nói thẳng: khi một hệ thống thật sự quan trọng với đời sống hữu tri, chứng nhận phải **tương xứng** — khắt khe đúng mức tác động, phụ thuộc, và rủi ro thực của hệ thống đòi, không phải một danh sách kiểm một-cỡ-cho-tất-cả hay một con dấu suông. Nó cũng phải **có tham gia** — hữu tri và cộng đồng bị ảnh hưởng phải thấy được điều đã rà, hiểu điều đã quyết, và tranh biện khi có gì sai. Các diễn đàn rà bằng chứng, ghi vào hồ sơ chứng nhận, và đòi kiểm lại theo lịch khớp mức rủi ro của hệ thống. Chứng nhận không phải điểm phổ biến, giấy thông hành vĩnh viễn, hay cách bỏ qua rà soát quyền. Nó là tuyên bố có hạn thời gian, tranh biện được, về điều đang biết về sự thẳng hàng của hệ thống lúc này. Dưới trụ **giám sát** của Tứ diện, giám sát đòi kiểm toán; chứng nhận thẳng hàng hệ thống là một quy trình kiểm toán đặc biệt lớn, lợi hại cao giữa các quy trình khác — không phải nhà kiểm toán duy nhất (**Điều XV**, [Khả năng kiểm toán](core_05_band_oversight.md#auditability)).*

<a id="1-purpose-and-role"></a>

**Chứng nhận thẳng hàng hệ thống** tồn tại để trả lời một câu, cho một phạm vi và lịch rà đã nêu: Hệ thống đã cho thấy thẳng hàng hiến pháp đủ để công nhận, công nhận có điều kiện, xác nhận, tái xác nhận, tiếp tục dựa, triển khai, hay giải phóng có trọng khỏi điều kiện chưa?

Như công cụ giám sát, chứng nhận là một quy trình kiểm toán đặc biệt lớn dưới [Khả năng kiểm toán](core_05_band_oversight.md#auditability) và **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*): được diễn đàn giám sát, nhiều miền, và mang công nhận. Nó không nuốt hay thế các kiểu kiểm toán anh em (kể cả kiểm toán Hồ sơ phân loại hệ thống dưới **CS-3**, kiểm toán Hồ sơ loại dữ liệu hệ thống dưới **CS-2**, kiểm toán độ phức tạp và quản trị có trách nhiệm, xác minh tuyên, và đường dẫn kiểm toán liên tục).

Độ sâu chứng nhận, gánh hồ sơ, nhịp tái xác nhận, rà soát bên bị ảnh hưởng, và đường tranh biện phải chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake) dưới [Tính tương xứng](core_05_band_accountability.md#proportionality). Hệ thống tác động cao hơn, phụ thuộc cao hơn, và rủi ro cao hơn đòi chứng mạnh hơn, hồ sơ rõ hơn, và tham gia thực tiễn hơn — kể cả khả năng tiếp cận nội dung, ý kiến bên bị ảnh hưởng, và đường tranh biện chia tỷ lệ theo ai đang dựa vào hệ thống. Lớp thấp hơn và phạm vi có giới hạn vẫn đòi phân hạng trung thực và bảo đảm tương xứng; chúng không được giấy thông hành miễn nghĩa vụ vật chất nơi có hiệu ứng ra ngoài.

Chứng nhận triển khai [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) qua [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad):

- **[Hưng thịnh](core_00_preamble.md#flourishing)** — chứng nhận kiểm rằng công nhận hay tiếp tục dựa sẽ không lặng lẽ đánh bại Sàn Quyền hay chặn tham gia công bằng trong đời sống liên quan hiến pháp;
- **[Liên tục](core_00_preamble.md#continuity)** — chứng nhận kiểm cung bền, không thoái lui, và tái xác nhận chia tỷ lệ theo lớp nơi hệ thống chung cổng hoặc nâng đỡ việc giao;
- **Tham gia** — hữu tri và cộng đồng bị ảnh hưởng có thể hiểu, tranh biện, và tham gia các đường rà sát với họ;
- **Giám sát** — hồ sơ, bằng chứng, và giả định đủ nhìn và kiểm toán được cho kiểm độc lập; chính chứng nhận là một quy trình kiểm toán đặc biệt lớn dưới nghĩa vụ giám sát đó, không phải cái duy nhất;
- **Trách nhiệm giải trình** — khiếm khuyết, phân hạng sai, và vận hành đánh bại sàn được định tuyến tới khắc phục, điều kiện, rút, hoặc đầu vào quỹ đạo nơi sự kiện nâng đỡ;
- **Kịp thời** — đồng hồ rà và tranh biện giữ chứng nhận khỏi cũ trong khi hại vẫn còn ngăn hoặc đảo được.

Chương này chạy quy trình chứng nhận được diễn đàn giám sát cho:

- **Lớp hệ thống và nhịp tái xác nhận** — nhìn kỹ đến đâu và thường đến đâu ([§2](#2-system-class-evaluation));
- **Đánh giá** — kiểm toàn hệ thống và theo miền ([§3](#3-whole-system-certification-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation));
- **Nội dung hồ sơ chứng nhận** — điều phải vào hồ sơ ([Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record));
- **Công nhận và tiếp tục dựa** — kết quả nào được tính ([§1](#1-purpose-and-role), [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record));
- **Tranh biện và khả năng tranh biện** — tranh biện đi qua diễn đàn thế nào ([Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability), [Phần B §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain));
- **Khiếm khuyết chứng nhận** — điều xảy ra khi chứng nhận lỗi ([Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) và các mục đánh giá xuyên chương).

Hồ sơ minh họa **Class A**, **Class B**, và **Class C** — và lớp chia tỷ lệ độ sâu chứng nhận xuyên chương này thế nào — nằm ở [§2.1](#21-illustrative-class-profiles-non-exhaustive). Đi qua đã làm cho cùng ba hệ thống xuất hiện ở [§3.8](#38-illustrative-whole-system-application-by-class) (*đánh giá toàn hệ thống*), [§4.1](#41-illustrative-data-handling-application-by-class) (*loại dữ liệu và xử lý*), [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*dấu chân sinh thái*), [§6.1](#61-illustrative-cross-system-support-application-by-class) (*đóng góp xuyên hệ thống tương xứng*), [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*không phân biệt đối xử*), [§8.1](#81-illustrative-accessibility-application-by-class) (*khả năng tiếp cận*), [§9.1](#91-illustrative-educational-capability-application-by-class) (*năng lực giáo dục*), và [§10.1](#101-illustrative-trustworthiness-application-by-class) (*đáng tin cậy*).

Các sàn quyền chương này giúp kiểm được nêu ở **§1.1**.


<a id="11-rights-floors-this-chapter-helps-verify"></a>
#### 1.1 Các sàn quyền chương này giúp kiểm

Khi hệ thống tác động có trọng cổng hoặc định hình cách hữu tri sống, chứng nhận kiểm rằng duyệt chúng sẽ không lặng lẽ đánh bại **Sàn Quyền** Chương Sáu, kể cả:

- **Thiết yếu sống còn** dưới **Điều III-A** (*Sinh tồn*) — thức ăn, nước, chỗ trú, môi trường vận hành, và đầu vào tương đương không phụ thuộc nền;
- **Lối vào giáo dục bình đẳng** dưới **Điều III-B** (*Lối vào giáo dục bình đẳng*);
- **Năng lực giáo dục lấy hữu tri làm trung tâm** dưới **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) nơi hệ thống xếp hạng, đánh giá, khuyến nghị, xếp chỗ, cổng giấy thông hành, hoặc cổng có trọng đường đào tạo lại và học suốt đời;
- **Không phân biệt đối xử** dưới **Điều V-B** (*Không phân biệt đối xử*) nơi hệ thống phân loại, cổng, định giá, xếp hạng, hoặc phân bổ gánh và lợi giữa các hữu tri;
- **Khả năng tiếp cận** dưới **Điều V-G** (*Khả năng tiếp cận*) nơi hệ thống cổng tham gia nội dung ở miền liên quan hiến pháp;
- **Hành vi hệ thống đáng tin và đáng tin cậy** dưới **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) nơi hệ thống định hình có trọng sự dựa của hữu tri vào hành vi được trình bày, giới hạn, rủi ro, đường tranh biện, hoặc khắc phục;
- **Điều kiện an toàn** dưới **Điều XII-A** (*Sàn đáng tin và đáng tin cậy*) và [**Điều kiện an toàn**](core_05_band_continuity.md#safe-conditions-constitutional) nơi hệ thống cung hoặc cổng hoạt động sản xuất;
- **Phân bổ tài nguyên** dưới **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*), kể cả [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional) dưới **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*) nơi hệ thống phân bổ, định tuyến, tài trợ, hoặc rút từ hạ tầng chung hoặc phụ thuộc nền.

<a id="2-system-class-evaluation"></a>

### 2. Đánh giá lớp hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§1](#1-purpose-and-role) (*mục đích và vai trò*); Tính trọng yếu tích hợp ([Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination)) (*Tính trọng yếu*); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [Tác động có trọng](core_05_band_oversight.md#material-impact), [Phụ thuộc](core_05_band_continuity.md#dependency), [Rủi ro](core_05_band_continuity.md#risk), [Ranh giới hệ thống](core_05_band_continuity.md#system-boundaries), và [Điều lệ](core_05_band_continuity.md#charter) (Chương Năm); [Chương Một §14 Yêu cầu đánh giá hệ thống](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement); **Điều III-A** (*Sinh tồn*) và **Điều III-B** (*giao Sàn Quyền nơi phân hạng cổng lối vào*); **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) và **Điều IV-B** (*phân bổ tài nguyên và quản trị có trách nhiệm đối với phụ thuộc nơi chứng nhận cổng sự dựa vào hạ tầng chung*).
- Hạ nguồn: [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*hồ sơ lớp minh họa*); [§3.8](#38-illustrative-whole-system-application-by-class) (*ví dụ toàn hệ thống đã làm theo lớp*); [§4.1](#41-illustrative-data-handling-application-by-class) (*ví dụ xử lý dữ liệu đã làm theo lớp*); [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*ví dụ dấu chân sinh thái đã làm theo lớp*); [§6.1](#61-illustrative-cross-system-support-application-by-class) (*ví dụ hỗ trợ xuyên hệ thống đã làm theo lớp*); [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*ví dụ không phân biệt đối xử đã làm theo lớp*); [§8.1](#81-illustrative-accessibility-application-by-class) (*ví dụ khả năng tiếp cận đã làm theo lớp*); [§9.1](#91-illustrative-educational-capability-application-by-class) (*ví dụ năng lực giáo dục đã làm theo lớp*); [§10.1](#101-illustrative-trustworthiness-application-by-class) (*ví dụ đáng tin cậy đã làm theo lớp*); [§4](#4-data-types-and-handling-evaluation) (*đánh giá xử lý dữ liệu chung*); [§5](#5-ecological-footprint-evaluation) (*đánh giá dấu chân sinh thái*); [§6](#6-proportionate-cross-system-support-evaluation) (*đánh giá hỗ trợ xuyên hệ thống*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*lệch phân hạng và cò tái phân hạng*).
- Đọc cùng: [Hồ sơ phân loại hệ thống](core_05_band_continuity.md#system-classification-record-constitutional); [corpus_systems.md](../../corpus_systems.md), **CS-3 — Phân hạng hệ thống và xử lý**, kể cả **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** (*Yêu cầu tái phân hạng* — cò, độ sâu đánh giá chia tỷ lệ theo lớp, và cầu xác minh SAC) và **[CS-3 §7](../../corpus_systems/cs_03_a_system_classification_machinery.md#cs-3-7-classification-governance-disclosure-and-challenge)** (*Nghĩa vụ quản trị Hồ sơ phân loại hệ thống và cầu SAC*); [CS-5 — Thiết kế, thử, xác minh, và triển khai](../../corpus_systems/cs_05_design_testing_verification_deployment.md); [CJS-3.21 — Điều khoản vững dưới đối kháng và chống lạm dụng](../../corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) (*nghĩa vụ chu kỳ hồi quy và làm cứng*); [corpus_forum.md](../../corpus_forum.md) **CF-7.2** (*Công nhận và rà soát thẳng hàng hiến pháp*).

</details>

<br>

*Nói thẳng: chứng nhận phải kiểm hệ thống có được phân hạng trung thực không — không theo người vận hành gọi nó là gì, mà theo nó thực sự làm gì, cái gì phụ thuộc vào nó, và cái gì có thể hỏng. Lớp cao hơn nghĩa là chứng chặt hơn, kiểm lại nhanh hơn, và kỳ vọng phục hồi mạnh hơn. Xem [§2.1](#21-illustrative-class-profiles-non-exhaustive) cho một hệ thống mỗi lớp; [§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), và [§10.1](#101-illustrative-trustworthiness-application-by-class) đi qua đánh giá áp cho từng cái thế nào.*

Chứng nhận thẳng hàng hệ thống phải đánh giá **lớp hệ thống** như một phần của mọi hồ sơ chứng nhận tác động có trọng. Định nghĩa lớp chuẩn, quy tắc chiều, hồ sơ lớp, quản trị phân hạng, bảo đảm chia tỷ lệ theo lớp, độ vững hạ tầng, và cơ chế tái chứng nhận sống ở **[corpus_systems.md](../../corpus_systems.md), CS-3 — Phân hạng hệ thống và xử lý** và **[CS-5 — Thiết kế, thử, xác minh, và triển khai](../../corpus_systems/cs_05_design_testing_verification_deployment.md)**. Mục này nêu điều chứng nhận phải kiểm và ghi; nó không nêu lại phân loại lớp CS-3, hồ sơ áp dụng, hay cơ chế thử CS-5.

Chứng nhận phải kiểm và ghi:

- **Yêu cầu đánh giá:**
  - liệu lớp hệ thống được gán có phản ánh **tác động**, **phụ thuộc**, và **rủi ro** quan sát được và dự kiến hợp lý dưới CS-3, kể cả hiệu ứng gộp, tương tác, đối kháng, và ngưỡng; và
  - rằng phân hạng được quyết bởi hành vi và tác động thực của hệ thống, không từ ý định tuyên, phạm vi danh nghĩa, chỉ văn bản [Điều lệ](core_05_band_continuity.md#charter), hay chỉ tự mô tả; và
  - rằng đánh giá lại phân hạng dưới **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** đã được áp nơi cò đánh giá lại có trọng nổ, và rằng [Hồ sơ phân loại hệ thống](core_05_band_continuity.md#system-classification-record-constitutional) phản ánh lớp **cao nhất áp dụng được** dưới điều kiện hiện tại.
- **Yêu cầu hồ sơ:**
  - một [Hồ sơ phân loại hệ thống](core_05_band_continuity.md#system-classification-record-constitutional) nêu lớp được gán, lý do phân hạng, giả định then chốt, kiểu phụ thuộc có mặt, đánh giá độ then chốt vận hành nơi có trọng, bất định, và nhịp tái xác nhận chia tỷ lệ theo lớp, như [Phần B §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) đòi; và
  - nơi phân hạng bất định hoặc đang bị tranh, lớp thận trọng được dựa vào và mọi điều kiện đang chờ giải.
- **Bảo đảm và tái chứng nhận:**
  - rằng bảo đảm chia tỷ lệ theo lớp, độ vững hạ tầng, và phủ hồi quy khớp CS-3 và CS-5 cho lớp được gán, đọc cùng [**CJS-3.21**](../../corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) và **CJS-3.19** đến **CJS-3.23** nơi áp dụng có trọng;
  - kết quả thử hồi quy trên hồ sơ chứng nhận dưới [Phần B §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) cho mỗi lần tái chứng nhận hoặc tái xác nhận — phạm vi hồi quy, bộ thử chuẩn và tùy chỉnh đã chạy, kết quả, hỏng đã biết, khắc phục, và rủi ro dư được chấp với lý do, như CS-5 đòi;
  - bằng chứng công nhận và rà trên hồ sơ cho chu kỳ chứng nhận — gói bằng chứng cho thấy phạm vi, phân hạng, thử, rủi ro dư, sẵn sàng khắc phục, theo dõi, và thay đổi có trọng từ hồ sơ trước nơi tái chứng nhận áp dụng, như CS-5 *Công nhận diễn đàn và rà vòng đời* đòi; và
  - với hệ thống cổng hoặc nâng đỡ giao Sàn Quyền, rằng nhịp tái xác nhận và độ sâu hồi quy triển khai mục tiêu **Liên tục** dưới [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) — chứng nhận cũ hoặc sớm không được coi là chứng rằng hữu tri vẫn nhận thức ăn, nước, chỗ trú, giáo dục, hay an toàn trong thực tế.
- **Phân hạng sai và khiếm khuyết:**
  - tuyên lớp rủi ro thấp hơn hệ thống đáng được, bẻ hệ thống thành mảnh để né quy tắc chặt hơn, hoặc giữ nhãn lớp cũ sau khi điều kiện đã đổi — kể cả thất đánh giá lại dưới **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** — là khiếm khuyết chứng nhận dưới CS-3 và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), không phải lỗi giấy tờ nhỏ;
  - bỏ thử hồi quy, dựa kết quả cũ, để hỏng đã biết không sửa, hoặc chấp sửa lớn mà không thử lại khi thử lại còn làm được — là khiếm khuyết chứng nhận dưới CS-5; và
  - nơi sự kiện nâng đỡ, cùng vấn đề phân hạng cũng có thể đếm vào phát hiện quỹ đạo bất lợi ở [Chương Tám](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model).

Nơi chứng nhận nhận diện những khiếm khuyết này, diễn đàn có thể duyệt với điều kiện, hoãn duyệt, từ chối, rút công nhận, đổi nhịp rà, hoặc ra lệnh rà mới.

<a id="21-illustrative-class-profiles-non-exhaustive"></a>

#### 2.1 Hồ sơ lớp minh họa (không hết)

*Nói thẳng: lớp không phải phù hiệu người vận hành chọn — nó là mức hại, sự dựa, và rủi ro hệ thống thực sự mang. Bảng dưới gọi tên một hệ thống minh họa mỗi lớp; [§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), và [§10.1](#101-illustrative-trustworthiness-application-by-class) đi qua đánh giá toàn hệ thống, xử lý dữ liệu, dấu chân sinh thái, hỗ trợ xuyên hệ thống, không phân biệt đối xử, khả năng tiếp cận, năng lực giáo dục, và đáng tin cậy áp cho từng cái thế nào. Quy tắc lớp chính thức, thử chiều, và cò tái phân hạng sống ở **CS-3**; các ví dụ này không thêm lớp hay thu hẹp CS-3.*

| Lớp | Hệ thống minh họa (không hết) | Điều chứng nhận phải phản ánh ở lớp này |
|-------|-------------------------------------|-----------------------------------------------|
| **Class A** | Điều khiển và đo xa **nước uống an toàn** của đô thị — gián đoạn sẽ khóa nước an toàn trước khi vật thay khả thi tới ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | Độ sâu [§3](#3-whole-system-certification-evaluation) đầy nhất; nhịp tái xác nhận có lý ngắn nhất; kỳ vọng hồi quy, hạ tầng, và công bố hồ sơ mạnh nhất dưới [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record); tham gia bên bị ảnh hưởng và diễn đàn hữu tri thực tiễn tối đa nơi Sàn Quyền bị cổng |
| **Class B** | Trao đổi **hồ sơ lâm sàng** vùng — bệnh viện và phòng khám dựa vào nó hàng ngày nhưng có thể rơi về dự phòng trong khung thời gian liên quan sống còn ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | Đánh giá [§3](#3-whole-system-certification-evaluation) đầy; bằng chứng chuỗi phụ thuộc và đường phục hồi vững; đánh giá miền ở [§4](#4-data-types-and-handling-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) nơi cò trọng yếu áp; đường tranh biện và theo dõi chia tỷ lệ theo độ then chốt vận hành |
| **Class C** | Nền tảng **lịch và phối hợp** thể chế quy mô lớn — định hình phối hợp ở quy mô nhưng không phải điều kiện tiên quyết vận hành cho dịch vụ sống còn ở chế độ suy ([§3.8](#38-illustrative-whole-system-application-by-class), [§4.1](#41-illustrative-data-handling-application-by-class), [§5.1](#51-illustrative-ecological-footprint-application-by-class), [§6.1](#61-illustrative-cross-system-support-application-by-class), [§7.1](#71-illustrative-nondiscrimination-application-by-class), [§8.1](#81-illustrative-accessibility-application-by-class), [§9.1](#91-illustrative-educational-capability-application-by-class), [§10.1](#101-illustrative-trustworthiness-application-by-class)) | Đánh giá có trọng dưới [§4](#4-data-types-and-handling-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) nơi cò áp; rà toàn hệ thống tương xứng; theo dõi tái phân hạng nơi hiệu ứng phụ thuộc, tập trung, hoặc cổ chai mạnh lên — chứng nhận không được coi Class C là vĩnh viễn nếu hệ thống trở thành cần thiết vận hành |

**Tham gia và tính tương xứng ở tỷ lệ lớp.** Hệ thống **Class A** đòi đường tham gia thực tiễn mạnh nhất — kể cả tranh biện tiếp cận được, rà bên bị ảnh hưởng, và phát hiện thành phần diễn đàn hữu tri nơi Sàn Quyền bị kéo vào — vì lỗi có thể khóa thiết yếu sống còn trước khi khắc phục còn kịp. Hệ thống **Class B** đòi tham gia vững nơi hệ thống cổng chăm sóc sức khỏe, giáo dục, phúc lợi, việc làm, hoặc đời sống hàng ngày tương đương. Hệ thống **Class C** vẫn đòi hồ sơ tranh biện được và công bố tương xứng, nhất là nơi hiệu ứng phối hợp chất gánh lên nhóm được bảo vệ, tập trung phụ thuộc, hoặc báo hiệu leo tới Class B hay Class A.

**Nhắc tái phân hạng.** Nhãn minh họa không khóa phân hạng. Một nền tảng phối hợp trở thành cổng thực tế cho lối vào thiết yếu sống còn; một dịch vụ giấy thông hành mà sự cố giờ sẽ chặn chăm sóc sức khỏe hay phúc lợi trong khung thời gian liên quan sống còn; hoặc một hệ thống con tiện ích bị hút vào đường then chốt phải được tái phân hạng và tái chứng nhận dưới **[CS-3 §3.5](../../corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) — không để ở lớp thấp hơn vì người vận hành thích rà nhẹ hơn.


<a id="3-whole-system-certification-evaluation"></a>

### 3. Đánh giá chứng nhận toàn hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Chương Một §14 Yêu cầu đánh giá hệ thống](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement); Gia đình đo lường Hưng thịnh (*Phúc lợi, an toàn, hại, và lối vào sàn sống còn*); Gia đình đo lường Hiệu năng hiến pháp (*Hiệu quả hiến pháp, Gánh nặng có thể tránh, và Năng lực sản xuất*); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [§1 Mục đích và vai trò](#1-purpose-and-role).
- Hạ nguồn: [§3.8](#38-illustrative-whole-system-application-by-class) (*đi qua toàn hệ thống minh họa*); [§4](#4-data-types-and-handling-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) (*đánh giá lĩnh vực*); [§2.1](#21-illustrative-class-profiles-non-exhaustive) (*hồ sơ lớp minh họa*); [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §14](core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain) (*chuỗi khả năng tranh biện*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*mở lại và chống lẩn tránh*).
- Đọc cùng: [Chương Một §9](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [§10](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline), và [§11](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture); [§5.2 Quyền ngừng tự nguyện và lối ra](core_01_a_values_principles.md#52-voluntary-discontinuation-and-exit-rights); [§5.3 Tụ họp, tổ chức tập thể, và hình thành thể chế](core_01_a_values_principles.md#53-assembly-collective-organization-and-institutional-formation); **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*) nơi Sàn Quyền kiểm toán, minh bạch, hoặc xác minh độc lập đang lợi hại có trọng; Gia đình đo lường Liên tục ([§3.1](#31-systemic-scope-and-risk-factors) — khả năng phục hồi, khả năng đảo, và rủi ro hệ thống); [Đánh giá rủi ro](core_05_band_continuity.md#risk-evaluation); [Công bố rủi ro](core_05_band_oversight.md#risk-disclosure); [Công bố sàn giám sát công cộng](core_05_band_oversight.md#public-oversight-baseline-disclosure); Gia đình đo lường Tham gia ([§3.3](#33-privacy-informational-joint-invocation) — quyền riêng tư và quản trị có trách nhiệm đối với dữ liệu); Gia đình đo lường Trách nhiệm giải trình ([§3.7](#37-governance-incentive-and-contestability-discipline) — thẳng hàng khuyến khích và khả năng tranh biện thị trường); [Ranh giới hệ thống](core_05_band_continuity.md#system-boundaries); [Điều lệ](core_05_band_continuity.md#charter).
- Tiểu mục: [§3.1](#31-systemic-scope-and-risk-factors) đến [§3.7](#37-governance-incentive-and-contestability-discipline) (*yếu tố đánh giá toàn hệ thống*); [§3.8](#38-illustrative-whole-system-application-by-class) (*áp dụng toàn hệ thống minh họa theo lớp*).

</details>

<br>

*Nói thẳng: không được bật đèn xanh một mảnh của hệ thống rồi bỏ phần còn lại. Người rà cần bức tranh đầy — nó phụ thuộc vào gì, cái gì gãy khi thứ gì thượng nguồn hỏng, hại hiện muộn hoặc cộng dồn theo thời gian, liệu hữu tri có thực sự dùng được (không chỉ trên giấy), liệu thông tin riêng có được tường đúng, liệu hữu tri có ra được mà không bị kẹt, liệu nhóm còn tổ chức được mà hệ thống không tách họ, liệu thắng ngắn hạn có che hại dài hạn, và liệu giám sát cùng trách nhiệm giải trình thực sẽ còn chạy khi lợi hại cao.*

Một đánh giá chứng nhận thẳng hàng hệ thống chưa đủ nếu chỉ xét hiệu ứng tức thì hoặc địa phương. Hồ sơ chứng nhận phải cho thấy đánh giá đã xét các yếu tố dưới đây nơi chúng có trọng đối với công nhận, xác nhận, tái xác nhận, tiếp tục dựa, triển khai, hoặc giải phóng có trọng khỏi điều kiện. Đánh giá cũng phải xác nhận [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad) sẽ đạt chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake) cho hệ thống đang rà. Đi qua toàn hệ thống đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§3.8](#38-illustrative-whole-system-application-by-class).

<a id="31-systemic-scope-and-risk-factors"></a>
#### 3.1 Phạm vi hệ thống và yếu tố rủi ro

Đánh giá chứng nhận phải xét:

- **quan hệ phụ thuộc và hiệu ứng dây chuyền** — cái gì hỏng hạ nguồn khi thứ gì thượng nguồn gãy;
- **hiệu ứng gộp và quy mô** — cái gì đổi khi nhiều hành động nhỏ cộng lại;
- **tác động trì hoãn, cộng dồn, và xác suất** — hại hiện muộn, chồng lên, hoặc phụ thuộc may rủi;
- **điều kiện đối kháng và tiềm năng lạm dụng** — kẻ xấu hoặc lạm dụng dự kiến có thể khai thác hệ thống thế nào;
- **phạm vi Điều lệ đối ranh giới chức năng** — liệu [Điều lệ](core_05_band_continuity.md#charter) đang quản trị, nơi có hoặc bị đòi, có khớp [Ranh giới hệ thống](core_05_band_continuity.md#system-boundaries) quan sát được, và liệu phạm vi nêu có hạ thấp tác động hoặc phụ thuộc có trọng;
- **rủi ro tồn vong** — kết cục có thể đe dọa sự sống còn hữu tri hoặc [Năng lực phục hồi sinh thái](core_05_band_continuity.md#ecological-recovery-capacity-constitutional) ở quy mô văn minh.

**Cầu đánh giá và công bố rủi ro.** Nơi [Rủi ro](core_05_band_continuity.md#risk) hệ thống nằm trong phạm vi dưới các yếu tố trên, chứng nhận phải kiểm cả hai nửa cặp Chương Năm — không bịa một loài hồ sơ công bố rủi ro được đặt tên riêng:

- **[Đánh giá rủi ro](core_05_band_continuity.md#risk-evaluation)** — liệu rủi ro hệ thống thực sự đã được đánh giá dưới các điều kiện quan trọng (phụ thuộc, chân trời thời gian, và [Điều kiện đối kháng, chia tỷ lệ, và bị khai thác](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions)), kích theo lớp và [lợi hại vật chất](core_00_preamble.md#material-stake); và
- **[Công bố rủi ro](core_05_band_oversight.md#risk-disclosure)** — liệu rủi ro đã đánh giá đã tới hữu tri cần nó kịp để hiểu, tranh biện, và hành động.

Đánh giá không công bố, hay công bố không đánh giá, đều thất. Tầm nhìn sàn công cộng vào rủi ro có trọng dưới [Công bố sàn giám sát công cộng](core_05_band_oversight.md#public-oversight-baseline-disclosure) có thể được thỏa một phần qua Công bố rủi ro nơi rủi ro hệ thống nằm trong phạm vi; sàn đó vẫn rộng hơn cầu này và không đòi một công cụ ngang hàng bên cạnh [Hồ sơ phân loại hệ thống](core_05_band_continuity.md#system-classification-record-constitutional) hay [Hồ sơ loại dữ liệu hệ thống](core_05_band_continuity.md#system-data-types-record-constitutional).

**Yêu cầu hồ sơ.** Nơi rủi ro hệ thống nằm trong phạm vi, [Hồ sơ chứng nhận hệ thống](core_05_band_continuity.md#system-certification-record-constitutional) dưới **[Phần B §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)** phải nêu:

- phát hiện đánh giá rủi ro và giả định được dựa cho các yếu tố trên;
- tư thế công bố — kể cả:
  - đối tượng hoặc định tuyến dự kiến;
  - thời điểm tương đối với quyết định có trọng; và
  - mọi giữ lại có lý đi cặp với vật thay dùng được.
- khiếm khuyết hoặc điều kiện nơi đánh giá hay công bố còn chưa đủ.

Những phát hiện đó sống trên hồ sơ chứng nhận. Chúng không phải hồ sơ thành phần bắt buộc được đặt tên thứ năm.

**Khiếm khuyết và lệch thẳng hàng.** Coi ghi chú nội bộ, phụ lục chôn, danh sách kiểm, hoặc tuyên sau việc như đánh giá hay công bố; thất công bố rủi ro hệ thống đã đánh giá cho người cần nó nơi [Minh bạch](core_05_band_oversight.md#transparency) hoặc [An toàn (Ràng buộc)](core_05_band_continuity.md#safety-constraint) đòi; hoặc chứng nhận tiếp tục dựa trong khi khe giao rủi ro có trọng còn chưa giải phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng đỡ công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="32-accessibility-under-sentience-non-exclusion"></a>
#### 3.2 Khả năng tiếp cận dưới không loại trừ hữu tri

Đánh giá chứng nhận phải thử tham gia thực cho mọi hình hữu tri và hồ sơ năng lực, không chỉ tuân thủ giấy tờ.

- *Phạm vi hồ sơ.* Đánh giá phải xử mọi hạng hồ sơ liên quan: giác quan, nhận thức, vận động, giao tiếp, **giao diện nền**, và **giao diện tính toán**. Cùng yêu cầu áp liệu hồ sơ **ổn định**, **từng đợt**, hay **phát triển**.
- *Chuẩn.* Phép thử là **hiệu ứng tham gia nội dung**: liệu hữu tri bị ảnh hưởng có **thực sự** tham gia được miền. **Tuân thủ tiện nghi hình thức** không đủ.
- *Chia tỷ lệ.* Sàn tham gia thực tăng theo [Tính trọng yếu](core_05_band_oversight.md#materiality-determination) của miền và [Phụ thuộc](core_05_band_continuity.md#dependency) của bên bị ảnh hưởng vào hệ thống.
- *Chống lẩn tránh.* Chứng nhận phải từ chối mẫu **lối vào chung** tuyên sẵn có gộp rộng trong khi đánh bại một hồ sơ bị ảnh hưởng cụ thể, và **chia tỷ lệ trọng yếu chọn lọc** có hiệu ứng đánh bại sàn tham gia.
- *Chủ sở hữu Sàn Quyền.* [Điều V-G](core_06_rights_part_b.md#article-v-g-accessibility) (*Khả năng tiếp cận*) nắm Sàn Quyền khả năng tiếp cận. Khả năng tiếp cận riêng giáo dục vẫn do [Điều III-B](core_06_rights_part_a.md#article-iii-b-equal-educational-access) (*Lối vào giáo dục bình đẳng*) quản trị.

<a id="33-privacy-informational-joint-invocation"></a>
#### 3.3 Quyền riêng tư (Thông tin) — viện chung

*Nói thẳng: Chương Sáu rải bảo vệ quyền riêng tư qua nhiều điều — không một góc gọn. Nếu rà chứng nhận chạm hơn một bảo vệ đó, người rà phải kiểm từng cái thực sự áp. Tích hộ dễ nhất rồi coi xong là không đủ.*

Khi một vụ chứng nhận kéo có trọng hơn một chỗ quyền riêng tư Chương Sáu, chứng nhận phải xử từng chỗ đó. Đóng vụ dưới một chỗ một mình là không đủ.

- *Mở tham gia.* [Quyền riêng tư (Thông tin)](core_05_band_continuity.md#privacy-informational) mở [Tham gia](core_05_apex_participation_leg.md#participation-constitutional) nội dung. Chứng nhận phải xác nhận bảo vệ quyền riêng tư nâng đỡ tiếng nói, thảo luận, liên kết, và tranh biện không bị đánh bại bằng phân đoạn, đọc chéo, hoặc áp lực phơi bày.
- *Chỗ cụm.* Phủ quyền riêng tư phân tán sống xuyên **Điều VII-A** (*Tự sở hữu thân và tâm*), **Điều VII-B** (*Ranh giới trạng thái nội tại và bảo vệ Loại N*), **Điều VIII** (*Hình dạng, dữ liệu trải nghiệm, và quyền công bố*), **Điều IX-A** (*Quyền năng và tự do khỏi thao túng*), và **Điều XIII-A** (*Giới hạn an ninh, tình báo, và quyền lực kín*).
- *Quy tắc viện chung.* Nơi vụ kéo có trọng hơn một chỗ, chứng nhận phải tới từng chỗ đó và không được định tuyến vụ qua một chỗ theo cách để chỗ khác bị lẩn.
- *Nhà đầu cụm.* Chương Năm [**Def.C3** (*Quyền riêng tư (Thông tin)* — đầu cụm ngang hàng)](core_05_band_accountability.md#privacy-informational-cluster) và [Quyền riêng tư (Thông tin)](core_05_band_continuity.md#privacy-informational) nắm nghĩa.
- *Không nới bằng đọc chéo.* Chuẩn nêu tại chỗ của mỗi thành viên cụm kiểm trong phạm vi của chính nó và không được nới bằng nhập chuẩn lỏng hơn từ thành viên khác.
- *Sàn Loại N được giữ.* Nơi **Điều VII-B** (*Ranh giới trạng thái nội tại và bảo vệ Loại N*) bị kéo có trọng, xử lý **Loại N** dưới **[corpus_systems.md](../../corpus_systems.md), CS-2** áp và không bị thu hẹp bởi yếu tố này.

<a id="34-voluntary-discontinuation-and-exit-rights"></a>
#### 3.4 Quyền ngừng tự nguyện và lối ra

Nơi [Chương Một §5.2 Quyền ngừng tự nguyện và lối ra](core_01_a_values_principles.md#52-voluntary-discontinuation-and-exit-rights) áp cho một vụ chứng nhận, chứng nhận phải thử tính tự nguyện, đồng thuận, chống cưỡng, áp lực phụ thuộc, thông tin, và khả năng đảo trước khi tuyên chứng nhận đứng. Đồng thuận hình thức một mình không đủ.

<a id="35-assembly-collective-organization-and-institutional-formation"></a>
#### 3.5 Tụ họp, tổ chức tập thể, và hình thành thể chế

Nơi [Chương Một §5.3 Tụ họp, tổ chức tập thể, và hình thành thể chế](core_01_a_values_principles.md#53-assembly-collective-organization-and-institutional-formation) áp cho một vụ chứng nhận, chứng nhận phải thử vụ đủ chung để ngăn lẩn tránh chống phân đoạn. Đánh giá chưa đủ nếu định tuyến vụ qua một khung một mình theo cách đánh bại bảo vệ tụ họp hoặc tổ chức tập thể.

<a id="36-time-consistency-constraint"></a>
#### 3.6 Ràng buộc nhất quán thời gian

Chứng nhận không được coi chỉ số gần hạn, tuân thủ địa phương, hay hiệu quả chân trời ngắn là đủ nơi vi phạm chân trời trung hoặc dài dự kiến còn chưa được xử. Tối ưu chân trời ngắn không hợp lệ nơi nó dự kiến sản sinh vi phạm chân trời trung hoặc dài đối với ràng buộc **An toàn**, **Sự thật**, hoặc **phúc lợi** dưới điều kiện cộng dồn, trì hoãn, hoặc xuyên hệ thống.

<a id="37-governance-incentive-and-contestability-discipline"></a>
#### 3.7 Kỷ luật quản trị, khuyến khích, và khả năng tranh biện

*Nói thẳng: rà chưa xong trừ khi người rà hỏi bốn điều cơ bản còn chạy ở mức rủi ro đang có không — liệu hữu tri có thực sự tham gia được, liệu việc có thể được nhìn và kiểm, liệu sai trái có người chịu, và liệu quyết định có chuyển đủ nhanh khi cần. Người rà cũng cần biết ai thực sự nắm thẩm quyền có trọng và ai chịu cái gì — không một «nhóm» mơ hồ hay vỏ đùn trách. Những câu đó phải được trả lời cho chứng nhận hợp lệ.*

Đánh giá chứng nhận chưa đủ nếu không đánh giá liệu **giám sát**, **trách nhiệm giải trình**, **tham gia**, và **kịp thời** sẽ đạt chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake) cho hệ thống đang rà. Đánh giá đó phải gồm liệu vai trò quản trị có trách nhiệm, quản trị, và trách nhiệm giải trình có trọng có được **gán chính thức, ghi hồ sơ, và truy được** đủ để trách nhiệm trả lời và đường tranh biện thực tiễn chạy — chia tỷ lệ theo lớp hệ thống và tác động có trọng dưới **[corpus_systems.md](../../corpus_systems.md), CS-3 — Phân hạng hệ thống và xử lý**.

Cho kỷ luật đó, chứng nhận phải đọc:

- **[Chương Một §9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding)** — hiểu biết phân tán, minh bạch, khả năng kiểm toán, và khả năng quan sát tranh biện được;
- **[Chương Một §10 Quản trị dưới kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline)** — quản trị được ủy quyền và trách nhiệm trả lời dưới kỷ luật quản trị có trách nhiệm;
- **[Chương Một §11 Thẳng hàng khuyến khích và chiếm hệ thống](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture)** — thẳng hàng khuyến khích, tính toàn vẹn chỉ số thay, sửa khiếm khuyết chân trời ngắn, và đáp chiếm;
- **[Chương Một §11.1.4 Đường dẫn độ sâu vai trò và trách nhiệm vật chất](core_01_c_stewardship_capacity_principles.md#1114-role-depth-and-material-responsibility-pathways)** — đường dẫn vai trò có hệ quả và kỷ luật chống tham gia tượng trưng;
- **[Chương Mười Hai §5 Vai trò được ủy quyền, phát triển năng lực, và đóng góp](../../core_13_governance.md#5-authorized-roles-competency-development-and-contribution)** và **[corpus_systems.md](../../corpus_systems.md), CS-4 — Quản trị có trách nhiệm hệ thống then chốt** — sàn định nghĩa vai trò, năng lực, và truy vết vận hành nơi có trọng;
- **[Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification)** nơi Sàn Quyền kiểm toán, minh bạch, hoặc xác minh độc lập đang lợi hại có trọng.

<a id="38-illustrative-whole-system-application-by-class"></a>

<a id="38-illustrative-whole-system-application-by-class-non-exhaustive"></a>
#### 3.8 Áp dụng toàn hệ thống minh họa theo lớp (không hết)

*Nói thẳng: [§3.1](#31-systemic-scope-and-risk-factors) đến [§3.7](#37-governance-incentive-and-contestability-discipline) liệt kê điều rà toàn hệ thống phải xét. Tiểu mục này cho thấy các yếu tố đó áp cho một hệ thống minh họa mỗi lớp thế nào — chuỗi phụ thuộc, tham gia, quyền riêng tư, lối ra, tụ họp, chân trời thời gian, và kỷ luật quản trị — và điều phải xuất hiện trên hồ sơ. Các hệ thống khớp [§2.1](#21-illustrative-class-profiles-non-exhaustive); [§4.1](#41-illustrative-data-handling-application-by-class) đi cùng những hệ thống đó qua chi tiết xử lý dữ liệu.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một lớp điều khiển xử lý-và-phân phối thuộc thành phố phụ thuộc vào điện, cung hóa chất, nhà cung **SCADA** (điều khiển giám sát và thu thập dữ liệu), cảm biến hiện trường, và hạ tầng phân phối hạ nguồn; hỏng có thể khóa nước an toàn trước khi vật thay tới.

- **Yếu tố có trọng trong phạm vi:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — phụ thuộc điện và hóa chất thượng nguồn, hỏng phân phối dây chuyền, lạm dụng nhiễm hoặc cắt, và hại quy mô sống còn nếu tính toàn vẹn điều khiển thất;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — thông báo khẩn, báo sự cố, và đường tranh biện cho mọi hồ sơ liên quan nơi lối vào nước bị cổng;
  - [§3.3](#33-privacy-informational-joint-invocation) — rà chung nơi **telemetry** vận hành (đo hiện trường trực tiếp và tín hiệu điều khiển), dữ liệu liên lạc khách, và theo dõi nhà cung giao chỗ quyền riêng tư Chương Sáu;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — khóa nhà cung, áp lực hợp đồng đô thị, và khả năng đảo của điều khiển ủy thác;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — hội đồng nước cộng đồng, mạng tương trợ, và thân giám sát công cộng không được phân đoạn ra ngoài;
  - [§3.6](#36-time-consistency-constraint) — bảo trì trì hoãn, cắt chi phí chân trời ngắn, và hại an toàn hoặc sinh thái chân trời dài;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — chia tỷ lệ tứ diện **Class A** cho giám sát, trách nhiệm giải trình, tham gia, và kịp thời dưới CS-3 và truy vết vai trò CS-3.
- **Điều đánh giá phải thử:**
  - Liệu bản đồ phụ thuộc và dây chuyền có gồm kiểu hỏng điện, hóa chất, nhà cung, và phân phối;
  - liệu kịch bản cắt đối kháng, chất lượng giả, hoặc nhiễm đã được đánh giá dưới [Đánh giá rủi ro](core_05_band_continuity.md#risk-evaluation);
  - liệu rủi ro đã đánh giá đã tới cộng đồng và người vận hành bị ảnh hưởng cần nó dưới [Công bố rủi ro](core_05_band_oversight.md#risk-disclosure);
  - liệu cộng đồng bị ảnh hưởng có thực sự nhận cảnh báo, tranh biện vận hành không an toàn, và tham gia rà trước khi hại trở thành không đảo;
  - liệu rà quyền riêng tư đã tới mọi chỗ bị kéo có trọng;
  - liệu lối ra khỏi ủy thác nhà cung vẫn làm được mà không khóa nước an toàn;
  - liệu đường tụ họp và giám sát tập thể còn nguyên;
  - liệu tiết kiệm chân trời ngắn có dự kiến đánh bại an toàn chân trời dài; và
  - liệu vai trò quản trị có trách nhiệm được gán có truy được đủ cho trách nhiệm trả lời ở độ sâu **Class A**.
- **Điều hồ sơ phải cho thấy:**
  - Phát hiện có trọng dưới mỗi yếu tố bị kéo ở [§3.1](#31-systemic-scope-and-risk-factors) đến [§3.7](#37-governance-incentive-and-contestability-discipline);
  - giả định phụ thuộc và dây chuyền;
  - phát hiện đánh giá rủi ro và tư thế công bố (đối tượng hoặc định tuyến, thời điểm, giữ lại và vật thay) nơi rủi ro hệ thống nằm trong phạm vi;
  - phát hiện khả năng tiếp cận và tham gia cho cổng sàn sống còn;
  - phủ viện chung quyền riêng tư;
  - phát hiện lối ra và ủy thác;
  - phát hiện tụ họp và tổ chức tập thể nơi có trọng;
  - phát hiện nhất quán thời gian;
  - phát hiện quản trị, khuyến khích, và khả năng tranh biện ở độ sâu **Class A**;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi Sàn Quyền bị kéo vào; và
  - điều kiện hoặc cò mở lại gắn với hỏng nhà cung, rủi ro dây chuyền, hoặc khe quản trị.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe định tuyến tóm tắt lâm sàng và token giải danh tính giữa bệnh viện và phòng khám; vận hành hàng ngày dựa vào nó, nhưng fax, cổng trực tiếp, hoặc lấy thủ công có thể thế trong khung thời gian liên quan sống còn.

- **Yếu tố có trọng trong phạm vi:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — sự cố bệnh viện tham gia, thất giải danh tính, lỗi khử trùng, và hiệu ứng dây chuyền xuyên cơ sở lên giao chăm sóc;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — lối vào của nhà lâm sàng, người bệnh, và người bênh vực xuyên hồ sơ giác quan, nhận thức, vận động, giao tiếp, giao diện nền, và giao diện tính toán;
  - [§3.3](#33-privacy-informational-joint-invocation) — rà chung xuyên chỗ quyền riêng tư lâm sàng, danh tính, kiểm toán, và kề đủ điều kiện;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — lối ra bệnh viện, khả năng mang hồ sơ người bệnh, và chống khóa cho người tham gia;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — hội nhà lâm sàng, nhóm bênh vực người bệnh, và thân quản trị vùng không được định tuyến vòng;
  - [§3.6](#36-time-consistency-constraint) — tuyên hiệu quả hoặc liên thông chân trời ngắn dự kiến mòn chất lượng chăm sóc hoặc tin cậy chân trời dài;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — chia tỷ lệ tứ diện **Class B** cho sự dựa then chốt vận hành.
- **Điều đánh giá phải thử:**
  - Liệu bản đồ phụ thuộc có phủ bệnh viện tham gia, môi giới danh tính, và đường dự phòng;
  - liệu hại trì hoãn hoặc cộng dồn từ lỗi định tuyến, hồ sơ cũ, hoặc sự cố một phần đã được đánh giá dưới [Đánh giá rủi ro](core_05_band_continuity.md#risk-evaluation);
  - liệu rủi ro vận hành và giao chăm sóc đã đánh giá đã tới nhà lâm sàng, người bệnh, và người vận hành cần nó dưới [Công bố rủi ro](core_05_band_oversight.md#risk-disclosure);
  - liệu tham gia nội dung có với tới nhà lâm sàng, người bệnh, và người bênh vực đang dựa vào trao đổi;
  - liệu mọi chỗ quyền riêng tư bị kéo có trọng đã được xử;
  - liệu bệnh viện và người bệnh còn giữ đường lối ra và mang được;
  - liệu đường giám sát tập thể và tổ chức nghề còn tranh biện được;
  - liệu khung hiệu quả có che hại chân trời dài đối với chăm sóc hoặc tin cậy; và
  - liệu vai trò quản trị có trách nhiệm và trách nhiệm trả lời có truy được ở độ sâu vận hành **Class B**.
- **Điều hồ sơ phải cho thấy:**
  - Phát hiện toàn hệ thống chia tỷ lệ theo độ then chốt vận hành **Class B**;
  - giả định phụ thuộc, dự phòng, và dây chuyền;
  - phát hiện đánh giá rủi ro và tư thế công bố nơi rủi ro hệ thống nằm trong phạm vi;
  - phát hiện khả năng tiếp cận và tham gia cho cổng chăm sóc sức khỏe;
  - phủ viện chung quyền riêng tư;
  - phát hiện lối ra và khả năng mang;
  - phát hiện tụ họp và tổ chức tập thể nơi có trọng;
  - phát hiện nhất quán thời gian;
  - phát hiện quản trị, khuyến khích, và khả năng tranh biện;
  - phát hiện thành phần nơi bị đòi; và
  - cò mở lại nếu sự cố hoặc hỏng định tuyến giờ sẽ chặn chăm sóc khẩn trong khung thời gian liên quan sống còn.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức phối hợp ca, đặt phòng, và hẹn nhà cung xuyên bệnh viện, trường, và cơ quan công; dịch vụ sống còn cốt có thể chạy ở chế độ suy nếu nó hỏng, nhưng nền tảng định hình phối hợp ở quy mô.

- **Yếu tố có trọng trong phạm vi:**
  - [§3.1](#31-systemic-scope-and-risk-factors) — hiệu ứng tập trung, dây chuyền xuyên tổ chức khi lịch hỏng, và gánh xác suất lên nhóm được bảo vệ qua mẫu phân bổ;
  - [§3.2](#32-accessibility-under-sentience-non-exclusion) — liệu nhân viên, học sinh, người bệnh, và nhà cung có dùng nội dung được giao diện lịch và tranh biện;
  - [§3.3](#33-privacy-informational-joint-invocation) — siêu dữ liệu lịch, liên lạc, và vai trò nơi nhiều chỗ quyền riêng tư áp;
  - [§3.4](#34-voluntary-discontinuation-and-exit-rights) — lối ra tổ chức và khả năng mang dữ liệu nơi thể chế dựa vào nền tảng;
  - [§3.5](#35-assembly-collective-organization-and-institutional-formation) — công đoàn, hội phụ huynh, và thân nghề mà phối hợp không được chiếm hay phân đoạn ra ngoài;
  - [§3.6](#36-time-consistency-constraint) — hiệu quả ghép chân trời ngắn dự kiến gắn chặt mẫu phối hợp không công bằng;
  - [§3.7](#37-governance-incentive-and-contestability-discipline) — chia tỷ lệ tứ diện tương xứng và theo dõi tái phân hạng nơi hiệu ứng cổ chai mạnh lên.
- **Điều đánh giá phải thử:**
  - Liệu rà toàn hệ thống có coi nền tảng là hạ tầng phối hợp chứ không phải ứng dụng cô lập;
  - liệu tập trung, lệch ghép, và dây chuyền xuyên tổ chức đã được đánh giá trung thực dưới [Đánh giá rủi ro](core_05_band_continuity.md#risk-evaluation);
  - liệu rủi ro phối hợp và phân bổ đã đánh giá đã tới thể chế và nhóm bị ảnh hưởng cần nó dưới [Công bố rủi ro](core_05_band_oversight.md#risk-disclosure);
  - liệu đường tham gia còn nội dung nơi nền tảng cổng phối hợp diễn đàn, trường, hoặc nơi làm việc;
  - liệu rà quyền riêng tư đã tới chỗ bị kéo có trọng;
  - liệu lối ra còn làm được cho tổ chức tham gia;
  - liệu bảo vệ tụ họp và tổ chức tập thể đã được thử chung;
  - liệu bất công chân trời dài không bị che sau hiệu quả chân trời ngắn;
  - liệu quản trị và khả năng tranh biện còn chạy ở độ sâu **Class C**; và
  - liệu nhãn lớp còn khớp nếu nền tảng trở thành cổng thực tế cho lối vào thiết yếu sống còn.
- **Điều hồ sơ phải cho thấy:**
  - Phát hiện toàn hệ thống tương xứng với rủi ro phối hợp **Class C** — không phải danh sách kiểm cho có;
  - giả định tập trung và dây chuyền;
  - phát hiện đánh giá rủi ro và tư thế công bố nơi rủi ro hệ thống nằm trong phạm vi;
  - phát hiện khả năng tiếp cận và tham gia nơi phối hợp bị cổng;
  - phủ viện chung quyền riêng tư nơi bị cò;
  - phát hiện lối ra nơi có trọng;
  - phát hiện tụ họp nơi có trọng;
  - phát hiện nhất quán thời gian;
  - phát hiện quản trị và khả năng tranh biện;
  - **theo dõi tái phân hạng** rõ nơi hiệu ứng phụ thuộc, tải cấp lâm sàng, hoặc cổ chai mạnh lên; và
  - con trỏ tới đánh giá miền ở [§4](#4-data-types-and-handling-evaluation) đến [§10](#10-trustworthiness-and-system-reliance-integrity-evaluation) nơi cò trọng yếu áp.

**Đọc xuyên lớp.** Các yếu tố ở [§3.1](#31-systemic-scope-and-risk-factors) đến [§3.7](#37-governance-incentive-and-contestability-discipline) áp cho cả ba hệ thống; lớp đổi độ sâu mỗi yếu tố phải được đánh giá và ghi. Một nền tảng lịch **Class C** trở thành đường thực tiễn duy nhất tới nhân sự khẩn hoặc định tuyến thiết yếu sống còn phải nhận độ sâu toàn hệ thống **Class A** hoặc **Class B** theo sự kiện — không phải rà phối hợp nhẹ hơn người vận hành thích. Một hệ thống then chốt sống còn **Class A** không được hạ lớp trong khi nó cổng nước, năng lượng, hoặc thiết yếu sống còn tương đương mà không có vật thay kịp. Một trao đổi **Class B** mà sự cố giờ sẽ chặn chăm sóc khẩn trong khung thời gian liên quan sống còn phải được tái phân hạng lên — kể cả tới **Class A** nơi thiết yếu sống còn bị cổng — và tái chứng nhận dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="4-data-types-and-handling-evaluation"></a>

### 4. Đánh giá loại dữ liệu và xử lý

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§3](#3-whole-system-certification-evaluation) (*yếu tố đánh giá toàn hệ thống*); [§3.8](#38-illustrative-whole-system-application-by-class) (*đi qua toàn hệ thống minh họa*); [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Giám sát (*Sự thật và tính toàn vẹn nhận thức như đo lường hiến pháp*); [Điều XIV: Tính toàn vẹn không gian thông tin](core_06_rights_part_c.md#article-xiv-info-sphere-integrity); [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification); [Điều VII: Tự sở hữu](core_06_rights_part_b.md#article-vii-self-ownership).
- Hạ nguồn: [§4.1](#41-illustrative-data-handling-application-by-class) (*đi qua xử lý dữ liệu minh họa*); [§5](#5-ecological-footprint-evaluation) và [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*đánh giá dấu chân sinh thái và đi qua*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*tái phân hạng và lệch lạc xử lý*).
- Đọc cùng: [corpus_systems.md](../../corpus_systems.md), **CS-2 — Loại thông tin và xử lý** (kể cả **[CS-2 §5.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Tái phân hạng và quản trị vòng đời*) và **[CS-2 §8](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-8-system-data-types-record-governance)** (*Quản trị Hồ sơ loại dữ liệu hệ thống*)); [Hồ sơ loại dữ liệu hệ thống](core_05_band_continuity.md#system-data-types-record-constitutional); [Công bố sàn giám sát công cộng](core_05_band_oversight.md#public-oversight-baseline-disclosure); **CJS-3.18** (*điều khoản lưu giữ dữ liệu và tính toàn vẹn vòng đời*), **CJS-3.21** (*điều khoản vững dưới đối kháng và chống lạm dụng*), và **CJS-3.17** (*điều khoản khả năng tương tác, khả năng chuyển, và tính toàn vẹn lối ra*) nơi áp dụng có trọng.
- Tiểu mục: [§4.1](#41-illustrative-data-handling-application-by-class) (*áp dụng xử lý dữ liệu minh họa theo lớp*).

</details>

<br>

*Nói thẳng: chứng nhận cũng phải nhìn loại dữ liệu hệ thống chạm và liệu nó xử lý chúng thích hợp — kể cả liệu loại vẫn đúng ở chu kỳ rà hiện tại, và liệu hạ tầng bên dưới có vững đủ cho dữ liệu đó ở lớp hệ thống đó. Quy tắc loại và Hồ sơ loại dữ liệu hệ thống sống ở kho hệ thống; chứng nhận kiểm rằng quy tắc thật sự được áp và hồ sơ trung thực.*

Chứng nhận thẳng hàng hệ thống phải đánh giá **loại dữ liệu và xử lý** như phần của mọi hồ sơ chứng nhận có tác động vật chất. Định nghĩa loại thông tin chuẩn, quy tắc xử lý, yêu cầu tách, chi tiết vòng đời, và [Hồ sơ loại dữ liệu hệ thống](core_05_band_continuity.md#system-data-types-record-constitutional) bền sống ở **[corpus_systems.md](../../corpus_systems.md), CS-2 — Loại thông tin và xử lý**. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại phân loại loại CS-2 hay cơ học xử lý.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu hệ thống có nhận diện loại dữ liệu có trọng trong phạm vi và xử lý chúng dưới phân loại **hạn chế nhất áp dụng được**, kể cả xuyên biến đổi, gộp, ủy, lưu, giữ, và liên kết xuyên miền. Đánh giá phải phản hiệu ứng chức năng, không chỉ nhãn, định dạng, hay giai đoạn ống. Nơi sàn Loại O **[CS-2 Phần A §7](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems)** áp, chứng nhận cũng phải kiểm rằng [Công bố sàn giám sát công cộng](core_05_band_oversight.md#public-oversight-baseline-disclosure) đã công bố (**Loại O**) phủ **phạm vi đã chứng nhận** — ánh từ [Điều lệ](core_05_band_continuity.md#charter) điều hành (hoặc công cụ phạm vi đã công bố tương đương), lớp được gán, và [Ranh giới hệ thống](core_05_band_continuity.md#system-boundaries) quan sát — với giữ lại có lý ghép vật thay công khả thi tối đa; Chương Năm nắm thuật ngữ; CS-2 nắm nội dung sàn và cơ học phát hành.

**Tái đánh giá loại dữ liệu định kỳ.** Ở mọi chu kỳ chứng nhận hoặc tái xác nhận có tác động vật chất, quy trình phải kiểm rằng tập dữ liệu có trọng trong phạm vi đã được **tái đánh giá định kỳ** cho phân loại thích hợp dưới **[CS-2 §5.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Tái phân hạng và quản trị vòng đời*) và **CJS-3.18** (*điều khoản lưu giữ dữ liệu và tính toàn vẹn vòng đời*), và đã được **tái phân hạng** nơi rà đó đòi. Nhịp phải chia tỷ lệ theo lớp hệ thống và tác động vật chất dưới [§2](#2-system-class-evaluation). Đổi loại do sự kiện dưới CS-2 không thế cho kiểm chứng nhận định kỳ này.

**Yêu cầu hồ sơ.** Chứng nhận phải **tạo hoặc xác minh** một [Hồ sơ loại dữ liệu hệ thống](core_05_band_continuity.md#system-data-types-record-constitutional) — hoặc nội dung bắt buộc dưới CS-2 — và đưa nó vào [Hồ sơ chứng nhận hệ thống](core_05_band_continuity.md#system-certification-record-constitutional) dưới **[Phần B §11.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**. Hồ sơ đó phải nêu loại dữ liệu có trọng trong phạm vi, lý do phân loại cho dữ liệu mơ hồ hoặc nhiều loại, kiểm soát tách và liên kết xuyên miền được dựa, tư thế giữ và vòng đời, năng lực gán đủ để nâng [Hành động gán được](core_05_band_accountability.md#attributable-action-constitutional) và [Tính toàn vẹn gán](core_05_band_accountability.md#attribution-integrity-constitutional), **lần tái đánh giá loại dữ liệu định kỳ gần nhất** (ngày hoặc định danh chu kỳ, nhịp, và mọi đổi loại có trọng), và mọi hạn chế có lý đối với công bố hoặc lối vào kiểm toán cùng vật thay công nơi CS-2 đòi. Nơi sàn Loại O áp, hồ sơ cũng phải nêu [Công bố sàn giám sát công cộng](core_05_band_oversight.md#public-oversight-baseline-disclosure) phủ phạm vi đã chứng nhận thế nào (trường Điều lệ được dựa, phát hiện ranh giới, và mọi lỗ phủ hoặc điều kiện).

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu xử lý dữ liệu và bảo đảm hạ tầng phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và CS-3. Hệ thống lớp cao hơn đòi chứng tương xứng mạnh hơn rằng hạ tầng xử lý, lưu, xử lý, truyền, sao lưu, phục hồi, và theo dõi có thể giữ tính toàn vẹn phân loại, gán, và khả năng tranh biện dưới căng. Nơi mặc định tầm nhìn lợi ích công CS-2 áp, chứng nhận phải kiểm rằng hạn chế được phạm hẹp, có hồ sơ, kiểm toán được, và ghép vật thay khả thi tối đa chứ không che khuất đục.

**Độ vững hạ tầng cho dữ liệu.** Chứng nhận phải đánh giá liệu hạ tầng xử lý dữ liệu — kể cả tầng bền, ống, kiểm soát lối vào, ranh giới mã hóa hoặc cô lập, đường sao lưu và khôi, và chuỗi ủy người vận hành hoặc nhà cung — có thích hợp cho loại dữ liệu và lớp hệ thống đang bàn. Lỗ có trọng ở tính toàn vẹn vòng đời, độ vững dưới đối kháng, khả năng mang, hoặc khả năng phục hồi phải được nêu trên hồ sơ và phản vào kết quả chứng nhận, điều kiện, hoặc giới hạn dựa.

**Khiếm khuyết và lệch lạc.** Phân loại sai dữ liệu, tái cấu trúc lẩn, liên kết xuyên miền không an toàn, thiếu gán nơi hại có trọng không thể điều tra, **tái đánh giá loại dữ liệu định kỳ quá hạn hoặc bị bỏ**, hoặc mong manh hạ tầng mà tiên liệu được sẽ đánh bại bảo vệ CS-2 phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="41-illustrative-data-handling-application-by-class"></a>

<a id="41-illustrative-data-handling-application-by-class-non-exhaustive"></a>
#### 4.1 Áp dụng xử lý dữ liệu minh họa theo lớp (không hết)

*Nói thẳng: bảng lớp ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nói lớp cao hơn đòi rà khắt hơn. [§3.8](#38-illustrative-whole-system-application-by-class) cho thấy điều đó nghĩa gì cho **đánh giá toàn hệ thống** trên cùng ba hệ thống; [§5.1](#51-illustrative-ecological-footprint-application-by-class) tiếp chuỗi cho **dấu chân sinh thái**. Tiểu mục này cho thấy điều đó nghĩa gì cho **loại dữ liệu và xử lý** — loại nào trong phạm vi, chứng nhận phải kiểm gì, và điều phải xuất hiện trên hồ sơ. CS-2 vẫn nắm quy tắc loại; những đi qua này không thêm loại hay thu hẹp CS-2.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một lớp điều khiển xử lý-và-phân phối thuộc thành phố nuốt dữ liệu áp suất, lưu lượng, cảnh báo nhiễm, và lệnh van thời gian thực; lưu dữ liệu liên kết dịch vụ khách hạn chế cho thông báo sự cố; và ủy theo dõi cho một trung tâm vận hành an ninh nhà cung (**SOC**).

- **Loại dữ liệu trong phạm vi:**
  - **Đo xa** vận hành then chốt an toàn (tín hiệu đo và lệnh sống từ hiện trường);
  - tín hiệu nhiễm và cảnh báo chất lượng;
  - dữ liệu liên lạc thông báo sự cố;
  - nhật ký lối vào nhà cung và người vận hành;
  - hồ sơ sự cố và bảo trì.
- **Đánh giá phải thử:**
  - Liệu dữ liệu mặt phẳng điều khiển then chốt an toàn có được tách khỏi ống dịch vụ khách, thanh toán, hoặc phân tích dưới phân loại CS-3 **hạn chế nhất áp dụng được**;
  - liệu gộp, ủy nhà cung, hoặc đường sao lưu có thể sập tách đó dưới căng hoặc điều kiện đối kháng;
  - liệu gán có sống đủ lâu để điều tra một sự kiện nhiễm hoặc cắt; và
  - liệu mọi hạn chế kiểm toán có lý vì an toàn có vật thay công đã ghi.
- **Hồ sơ phải cho thấy:**
  - Toàn bộ kho loại cho phạm vi đã chứng nhận;
  - lý do phân loại nơi đo xa, cảnh báo, hoặc dữ liệu liên lạc có thể nhiều loại;
  - kiểm soát tách và liên kết xuyên miền;
  - tư thế giữ và vòng đời cho dựng lại sự cố;
  - phát hiện bảo đảm hạ tầng cho sao lưu, khôi, và phục hồi đối kháng ở độ sâu **Class A**; và
  - mọi điều kiện gắn ủy nhà cung hoặc lỗ theo dõi.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe định tuyến tóm tắt lâm sàng, con trỏ hình ảnh, và token giải danh tính giữa bệnh viện, phòng khám, và hệ thống đủ điều kiện kề phúc lợi; bệnh viện dựa vào nó hàng ngày nhưng có thể rơi về fax, cổng trực tiếp, hoặc lấy thủ công trong khung thời gian liên quan sống còn.

- **Loại dữ liệu trong phạm vi:**
  - Hồ sơ lâm sàng và chẩn đoán;
  - token giải danh tính và giấy tờ;
  - dữ liệu danh bạ nhà cung và cơ sở;
  - nhật ký kiểm toán lối vào và công bố;
  - hiện vật khớp hoặc khử trùng lặp dẫn xuất.
- **Đánh giá phải thử:**
  - Liệu dữ liệu lâm sàng có ở lại dưới lớp xử lý chặt nhất áp dụng được xuyên định tuyến, đệm, khử trùng lặp, và liên kết hạ nguồn;
  - liệu logic giải danh tính có tạo liên kết xuyên miền không an toàn hoặc phơi qua ủy;
  - liệu chuỗi ủy người vận hành và người tham gia vẫn gán được; và
  - liệu đường khả năng mang và lối ra có giữ kiểm soát bệnh nhân mà không đánh bại phục hồi vận hành.
- **Hồ sơ phải cho thấy:**
  - Loại có trọng và lý do loại mơ hồ;
  - tách giữa tải lâm sàng, siêu dữ liệu danh bạ, và nguồn kề đủ điều kiện;
  - gán chuỗi ủy;
  - tư thế vòng đời và giữ đủ cho điều tra và tranh biện chăm sóc sức khỏe;
  - phát hiện bảo đảm hạ tầng ở độ sâu vận hành **Class B**; và
  - cò mở lại nếu sự cố hoặc lỗi xử lý dữ liệu giờ sẽ chặn chăm sóc trong khung thời gian liên quan sống còn.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức phối hợp ca nhân sự, đặt phòng, và hẹn nhà cung xuyên bệnh viện, trường, và cơ quan công; bệnh viện và tiện ích cốt vẫn chạy ở chế độ suy nếu nó hỏng, nhưng nền tảng định hình phối hợp ở quy mô và có thể giữ siêu dữ liệu liên lạc, vai, và vị trí thô.

- **Loại dữ liệu trong phạm vi:**
  - Dữ liệu lịch, vai, và phân bổ tài nguyên;
  - siêu dữ liệu liên lạc và giấy tờ người tham gia;
  - định danh vị trí thô hoặc địa điểm;
  - nhật ký kiểm toán nền tảng;
  - đầu ra xếp hạng hoặc khớp dẫn xuất nơi dùng.
- **Đánh giá phải thử:**
  - Liệu hệ thống có nhận diện loại có trọng trung thực — kể cả đầu ra dẫn xuất có thể lộ đặc trưng được bảo vệ qua mẫu lịch;
  - liệu liên kết xuyên tổ chức có ở trong phạm vi có lý;
  - liệu xử lý vẫn tranh biện được nơi tập trung có thể báo hiệu leo cổ chai; và
  - liệu nhãn lớp thấp hơn vẫn khớp nếu phụ thuộc hoặc độ nhạy dữ liệu đã mạnh.
- **Hồ sơ phải cho thấy:**
  - Loại có trọng trong phạm vi và mọi lý do nhiều loại;
  - phát hiện liên kết và giữ tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện bảo đảm hạ tầng nơi có trọng — không nghi thức — cho dữ liệu thật sự giữ;
  - gán tranh biện được cho liên kết chuyển gánh; và
  - **theo dõi tái phân hạng** rõ nơi nền tảng trở thành cổng thực tế cho lối vào thiết yếu sống còn hoặc bắt đầu mang tải cấp lâm sàng.

**Đọc xuyên lớp.** Cùng quy tắc CS-3 áp cho cả ba hệ thống; lớp đổi **độ sâu**, không phép xử lý sai dữ liệu. Một nền tảng **Class C** bắt đầu lưu hoặc định tuyến hồ sơ cấp lâm sàng phải được đánh giá và ghi như vậy — không để ở xử lý nền tảng phối hợp vì người vận hành thích hồ sơ nhẹ hơn. Một trao đổi **Class B** mà sự cố giờ sẽ chặn chăm sóc khẩn trong khung thời gian liên quan sống còn phải được tái phân hạng và tái chứng nhận dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), với bảo đảm xử lý dữ liệu chia tỷ lệ theo đó.

<a id="5-ecological-footprint-evaluation"></a>

### 5. Đánh giá dấu chân sinh thái

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Liên tục (*Dấu chân sinh thái như đo lường hiến pháp*); **Điều I-B** (*Dấu chân sinh thái và minh bạch*); [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint), [Tác động vật chất](core_05_band_oversight.md#material-impact), [Phụ thuộc](core_05_band_continuity.md#dependency), [Minh bạch](core_05_band_oversight.md#transparency), và [Tính toàn vẹn nhận thức](core_05_band_oversight.md#epistemic-integrity) (Chương Năm); [Tiền điều kiện môi trường](core_05_band_continuity.md#environmental-preconditions-constitutional) và [Tính toàn vẹn sinh thái](core_05_band_continuity.md#ecological-integrity-constitutional) nơi liên lụy có trọng.
- Hạ nguồn: [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*đi qua dấu chân sinh thái minh họa*); [§6](#6-proportionate-cross-system-support-evaluation) và [§6.1](#61-illustrative-cross-system-support-application-by-class) (*đánh giá hỗ trợ xuyên hệ thống và đi qua*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*trình bày sai dấu chân và lệch lạc*).
- Đọc cùng: [corpus_systems.md](../../corpus_systems.md), [CS-8 — Bền vững thích ứng và khả năng phục hồi hệ sinh thái](../../corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md) nơi phân bổ thích ứng hoặc phụ thuộc lẫn hệ sinh thái có trọng trong phạm vi.
- Tiểu mục: [§5.1](#51-illustrative-ecological-footprint-application-by-class) (*áp dụng dấu chân sinh thái minh họa theo lớp*).

</details>

<br>

*Nói thẳng: chứng nhận phải đánh giá trung thực gánh môi trường gán được khi chúng có trọng — kể cả mối liên thượng nguồn và hạ nguồn — không chỉ liệu người vận hành tuyên hệ thống xanh. Phương pháp kế toán dấu chân và mục tiêu giảm số sống ở công cụ khác; chứng nhận kiểm rằng gán, công bố, và so sánh thật sự được đánh giá nơi có trọng. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§5.1](#51-illustrative-ecological-footprint-application-by-class).*

Chứng nhận thẳng hàng hệ thống phải đánh giá **dấu chân sinh thái** như phần của mọi hồ sơ chứng nhận có tác động vật chất nơi gánh môi trường gán được có trọng dưới [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint) và **Điều I-B** (*Dấu chân sinh thái và minh bạch*). Quy tắc gán, vòng đời, phụ thuộc, và minh bạch chuẩn sống ở Chương Năm và **Điều I-B** (*Dấu chân sinh thái và minh bạch*); phương pháp kế toán, bước xác minh, và mục tiêu số sống ở công cụ hợp nhất nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học kế toán dấu chân hay đặt nghĩa vụ giảm ngoài điều công cụ khác đòi.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu dòng môi trường gán được — năng lượng, vật liệu, phát thải, dùng đất, và gánh liên quan — có được nhận diện xuyên vòng đời liên quan có trọng của hệ thống và quan hệ [Phụ thuộc](core_05_band_continuity.md#dependency), được đánh giá dưới [Tác động vật chất](core_05_band_oversight.md#material-impact), và được công bố hoặc giữ lại chỉ như [Minh bạch](core_05_band_oversight.md#transparency), [Tính toàn vẹn nhận thức](core_05_band_oversight.md#epistemic-integrity), và nghĩa vụ minh bạch áp cho phép. Đánh giá phải phản hiệu ứng chức năng và ranh giới hệ thống, không chỉ phạm vi danh nghĩa, nhãn tiếp thị, hoặc khung vòng đời một phần.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu phạm vi đánh giá dấu chân, giả định gán, ranh giới vòng đời và phụ thuộc được dựa, gánh có trọng đã nhận diện, bất định, tư thế công bố, phát hiện thành phần diễn đàn môi trường nơi đòi, và mọi giới hạn có lý đối với công bố dấu chân cùng vật thay công nơi quy tắc minh bạch áp đòi.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá và công bố dấu chân phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn đòi chứng tương xứng mạnh hơn rằng gánh môi trường có trọng đã được gán, so sánh xuyên phương án liên quan nơi khả thi, và không bị che qua dịch ranh giới, đổ phụ thuộc, hoặc công bố chọn.

**Khiếm khuyết và lệch lạc.** Che, trình bày sai, mảnh, hoặc đổ thông tin dấu chân có trọng nơi chứng nhận hoặc nghĩa vụ minh bạch **Điều I-B** (*Dấu chân sinh thái và minh bạch*) đòi công bố; chỉ đánh giá lát vòng đời người vận hành chọn nơi gán rộng hơn có trọng; hoặc coi tuyên dấu chân thỏa bởi khẳng định không có chứng đánh giá được phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="51-illustrative-ecological-footprint-application-by-class"></a>

<a id="51-illustrative-ecological-footprint-application-by-class-non-exhaustive"></a>
#### 5.1 Áp dụng dấu chân sinh thái minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) và [§4.1](#41-illustrative-data-handling-application-by-class) đi cùng ba hệ thống qua rà toàn hệ thống và xử lý dữ liệu. Tiểu mục này cho thấy đánh giá **dấu chân sinh thái** nghĩa gì cho từng cái — gánh môi trường nào được tính, chứng nhận phải kiểm gì, và điều phải xuất hiện trên hồ sơ. **Điều I-B** (*Dấu chân sinh thái và minh bạch*) và Chương Năm vẫn nắm quy tắc gán và minh bạch; phương pháp kế toán và mục tiêu số sống ở công cụ khác; những đi qua này không thêm nghĩa vụ dấu chân ngoài điều những công cụ đó đòi.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố dựa vào nguồn lưu vực, đầu vào hóa chất xử lý, năng lượng bơm và xử lý, hạ tầng phân phối, dòng xả, và tính toán hoặc theo dõi nhà cung được ủy nơi dùng.

- **Gánh gán được trong phạm vi:**
  - Rút nước nguồn và căng lưu vực;
  - hóa chất xử lý và môi trường lọc;
  - năng lượng bơm, xử lý, và phân phối;
  - hạ tầng hiện thân cho nhà máy, ống, và điều khiển;
  - mất và rò nước đã xử lý;
  - xả và dư tới nước nhận;
  - phát thải lưới điện thượng nguồn;
  - trung tâm vận hành an ninh nhà cung (**SOC**), tính toán lưu trữ chung, hoặc tính toán và kết nối theo dõi từ xa nơi dựa có trọng;
  - gánh bảo trì, thay, và ngừng dùng xuyên vòng đời liên quan có trọng.
- **Đánh giá phải thử:**
  - Liệu phạm vi dấu chân có gồm điện thượng nguồn, cung hóa chất, [Phụ thuộc](core_05_band_continuity.md#dependency) lưu vực, và xả hạ nguồn — không chỉ tòa vận hành đô thị;
  - liệu [Tác động vật chất](core_05_band_oversight.md#material-impact) đã được đánh giá cho cạn nguồn, cường độ năng lượng, và xả dưới căng hoặc biến thiên khí hậu;
  - liệu ranh giới người vận hành chọn có loại theo dõi lưu trữ nhà cung, logistics hóa chất thuê ngoài, hoặc gánh lưới chung nơi gán có trọng;
  - liệu phương án — bảo tồn, bảo vệ nguồn, đường xử lý gánh thấp hơn — đã được so sánh nơi khả thi; và
  - liệu giới hạn công bố có vật thay công đã ghi dưới **Điều I-B** (*Dấu chân sinh thái và minh bạch*).
- **Hồ sơ phải cho thấy:**
  - Phạm vi đánh giá dấu chân và ranh giới vòng đời ở độ sâu **Class A**;
  - giả định gán cho dòng lưu vực, năng lượng, hóa chất, và xả;
  - gánh có trọng đã nhận diện và bất định đã nêu;
  - phát hiện thành phần diễn đàn môi trường nơi đòi;
  - phát hiện so sánh xuyên phương án liên quan nơi khả thi;
  - tư thế công bố và mọi giới hạn có lý với vật thay công; và
  - điều kiện hoặc cò mở lại gắn căng nguồn, hại xả, hoặc dịch ranh giới.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe phụ thuộc vào lưu trữ sao, kết nối tại bệnh viện, tính toán giải danh tính, và hạ tầng nhà cung hoặc người tham gia vận hành xuyên mạng chăm sóc vùng.

- **Gánh gán được trong phạm vi:**
  - Năng lượng, làm lạnh, và vòng đời phần cứng trung tâm dữ liệu sơ cấp và sao lưu;
  - kết nối mạng và biên cho bệnh viện tham gia;
  - tính toán sao lưu trữ và khử trùng lặp;
  - hạ tầng môi giới danh tính và định tuyến;
  - gánh cơ sở tại địa điểm lưu trữ được dựa có trọng;
  - hạ tầng hiện thân cho đầu nối tại chỗ nơi bệnh viện dựa vào chúng.
- **Đánh giá phải thử:**
  - Liệu gán dấu chân có phủ gánh lưu trữ, sao, và kết nối người tham gia ở quy mô vận hành — không chỉ trụ sở người vận hành trao đổi;
  - liệu phụ thuộc vào vùng lưu trữ chung, nhà cung đặt chung, hoặc phần cứng biên tại bệnh viện đã được ánh và gán;
  - liệu lát vòng đời không bị thu vào tuyên chỉ-phần-mềm trong khi gánh phần cứng và năng lượng có trọng bị đổ;
  - liệu gánh có trọng đã được đánh giá dưới [Tác động vật chất](core_05_band_oversight.md#material-impact) và công bố nhất quán với **Điều I-B** (*Dấu chân sinh thái và minh bạch*); và
  - liệu tăng khối lượng người tham gia hoặc độ nhạy dữ liệu có đổi có trọng gánh được gán.
- **Hồ sơ phải cho thấy:**
  - Phạm vi dấu chân và ranh giới phụ thuộc ở độ sâu vận hành **Class B**;
  - gánh năng lượng, phần cứng, và kết nối có trọng đã nhận diện;
  - giả định gán lưu trữ và ủy;
  - bất định và tư thế công bố;
  - phát hiện diễn đàn môi trường hoặc thành phần khác nơi đòi; và
  - cò mở lại nếu quy mô, tăng tải cấp lâm sàng, hoặc tập trung lưu trữ đổi có trọng gánh gán được hoặc tư thế lớp.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức chạy chủ yếu trên tính toán và kết nối lưu trữ chung, với gánh thứ từ logistics địa điểm, đi lại do mẫu phối hợp gây, và lưu trữ vùng tập trung nơi áp.

- **Gánh gán được trong phạm vi:**
  - Tính toán, lưu trữ, và mạng lưu trữ cho tải lịch;
  - năng lượng trung tâm dữ liệu đa thuê gán được cho phần của nền tảng;
  - vòng đời phần cứng hiện thân cho hạ tầng được dựa có trọng;
  - gánh địa điểm và logistics chỉ nơi mẫu phối hợp dịch có trọng đi lại hoặc dùng cơ sở;
  - hiệu ứng tập trung vùng nơi lưu trữ hoặc dùng cụm ở nơi gánh cao.
- **Đánh giá phải thử:**
  - Liệu người vận hành đã gán trung thực gánh tính toán lưu trữ và kết nối chứ không coi nền tảng vô trọng vì nó «chỉ là phần mềm»;
  - liệu đổ đa thuê hoặc dịch ranh giới nhà cung có giấu gán năng lượng hoặc phần cứng có trọng;
  - liệu tập trung ở vùng hoặc nhà cung cụ thể đã được đánh giá nơi nó dịch gánh có trọng;
  - liệu rà dấu chân vẫn tương xứng mà không thành nghi thức cho một hệ thống **Class C**; và
  - liệu tái phân hạng có đáng nếu quy mô, định tuyến thiết yếu sống còn, hoặc tăng tải cấp lâm sàng sẽ đòi độ sâu dấu chân **Class B** hoặc **Class A**.
- **Hồ sơ phải cho thấy:**
  - Phát hiện dấu chân tương xứng với rủi ro phối hợp **Class C**;
  - phạm vi và giả định gán cho tính toán, lưu trữ, và kết nối;
  - gánh có trọng đã nhận diện mà không thu quá ranh giới vòng đời;
  - bất định và tư thế công bố;
  - **theo dõi tái phân hạng** rõ nơi tập trung lưu trữ, quy mô, hoặc độ nhạy tải mạnh lên; và
  - con trỏ tới rà dấu chân nâng nếu lớp hoặc tính trọng đổi.

**Đọc xuyên lớp.** Cùng kỷ luật dấu chân **Điều I-B** (*Dấu chân sinh thái và minh bạch*) và Chương Năm áp cho cả ba hệ thống; lớp đổi độ sâu gán và gánh so sánh, không phép che dòng môi trường có trọng. Một hệ thống nước then chốt sống còn **Class A** không được hạ lớp trong khi rút lưu vực, xả, hoặc gánh năng lượng cổng nước an toàn vẫn bị gán thiếu có trọng. Một trao đổi **Class B** mà tăng tải lâm sàng hoặc tập trung lưu trữ tăng có trọng gánh môi trường phải nhận rà dấu chân chia tỷ lệ theo tăng đó — kể cả lên độ sâu **Class A** nơi giao thiết yếu sống còn và gánh hệ thống nguồn cùng bị liên lụy. Một nền tảng lịch **Class C** trở thành cổ chai thực tế cho phối hợp thiết yếu sống còn không được giữ hồ sơ dấu chân hình thức vì người vận hành gắn nhãn không then chốt. Đi qua hỗ trợ xuyên hệ thống cho cùng hệ thống nằm ở [§6.1](#61-illustrative-cross-system-support-application-by-class).

<a id="6-proportionate-cross-system-support-evaluation"></a>

<a id="6-proportionate-cross-system-contribution-evaluation"></a>
### 6. Đánh giá đóng góp xuyên hệ thống tương xứng

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Liên tục (*Đóng góp xuyên hệ thống tương xứng như đo lường hiến pháp*); **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) và **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*); [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), [Phụ thuộc](core_05_band_continuity.md#dependency), [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional), [Tính tương xứng](core_05_band_accountability.md#proportionality), [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint), và [Bền vững](core_05_band_continuity.md#sustainability) (Chương Năm).
- Hạ nguồn: [§6.1](#61-illustrative-cross-system-support-application-by-class) (*đi qua hỗ trợ xuyên hệ thống minh họa*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*trình bày sai dòng tài nguyên, lệch lạc rút, và hỗ trợ không đủ*).
- Đọc cùng: **[corpus_systems.md](../../corpus_systems.md)**, **CS-9** (*Quản trị có trách nhiệm đối với phân bổ tài nguyên và tài trợ*), và **CS-8** (*Bền vững thích ứng và khả năng phục hồi hệ sinh thái*); [*Kiến trúc quản trị, giám sát, phụ thuộc, phân tán, tập trung, cấu trúc thị trường, và tính toàn vẹn lối ra*](core_05_band_accountability.md#governance-architecture-oversight-decentralization-and-concentration-cluster) nơi tập trung, phụ thuộc, hoặc định tuyến khuyến khích cắt **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*).
- Tiểu mục: [§6.1](#61-illustrative-cross-system-support-application-by-class) (*áp dụng hỗ trợ xuyên hệ thống minh họa theo lớp*).

</details>

<br>

*Nói thẳng: khi một hệ thống rút có trọng từ nền tảng chung, chứng nhận phải kiểm liệu nó trả đủ hỗ trợ truy được — không phải liệu người vận hành nói sổ cân. Công thức phân bổ và mục tiêu số sống ở công cụ khác; chứng nhận kiểm rằng bản đồ phụ thuộc, dòng hoàn trả, và công bằng xuyên hệ thống thật sự được đánh giá nơi cò áp. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§6.1](#61-illustrative-cross-system-support-application-by-class).*

**Cò trọng yếu.** Mục này áp nơi một hệ thống có tác động vật chất phân bổ, định tuyến, tài trợ, hoặc rút có trọng từ hạ tầng chung hoặc phụ thuộc nền mà hệ thống hoặc hữu tri khác dựa. Nó không đòi kiểm toán hỗ trợ xuyên hệ thống đầy trên mọi hồ sơ chứng nhận.

**«Rút» nghĩa gì ở đây.** Trong **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) và mục này, **rút** nghĩa là lấy **tiền, phí, tài trợ công, tính toán, kết nối, lao động bảo trì, năng lực nguồn, hoặc dòng tài nguyên chung khác** từ hạ tầng hoặc phụ thuộc mà hệ thống khác cũng cần — mà không trả hỗ trợ tương xứng để giữ nền tảng chung đó chạy. Câu hỏi là **ai hưởng từ hậu đài chung và ai trả để giữ chúng**, không phải liệu một hệ thống sao, bán, hoặc quảng cáo chống nội dung hồ sơ. Lối vào hồ sơ lâm sàng, dùng dữ liệu cá nhân, bán cho bên ngoài, quảng cáo nhắm, và lập hồ sơ bên thứ ba không liên được đánh giá dưới [§4](#4-data-types-and-handling-evaluation) và bảo vệ quyền riêng tư và không gian thông tin Chương Sáu — không dưới mục này.

Chứng nhận thẳng hàng hệ thống phải đánh giá **đóng góp xuyên hệ thống tương xứng** dưới [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*), và **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*) nơi cò trọng yếu áp. Nghĩa chuẩn, yếu tố đánh giá, và kỷ luật không tuân sống ở Chương Năm và **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*); hạng phân bổ, cơ học tái ủy quyền, và mục tiêu số sống ở **[corpus_systems.md](../../corpus_systems.md)**, **CS-9**, và **CS-8** nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học CS-8 hay CS-9 hay kê chia đều, phần trăm cố, hoặc một mô hình tài trợ duy nhất.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu bản đồ hệ thống phụ thuộc đã ghi và hồ sơ dòng tài nguyên kiểm toán được dưới **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) có cho thấy rút từ hạ tầng chung hoặc phụ thuộc nền và liệu dòng hoàn trả có tới đủ mức nội dung dưới [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), đánh giá dưới [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) và [Tính tương xứng](core_05_band_accountability.md#proportionality) và chia tỷ lệ theo độ then chốt, bất đối xứng phụ thuộc, khả năng thay, [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint) nơi có trọng, và [Bền vững](core_05_band_continuity.md#sustainability) dài hạn. Đánh giá phải phản hiệu ứng chức năng và dòng đã ghi, không chỉ nhãn danh nghĩa, chuyển một lần, hoặc khẳng định ngoài bản đồ.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu cò trọng yếu **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) được dựa, phạm vi đánh giá bản đồ hệ thống phụ thuộc và dòng tài nguyên, phát hiện rút và dòng hoàn trả, phát hiện đủ mức hỗ trợ dưới [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), bất định, phát hiện diễn đàn hữu tri hoặc thành phần được gán khác nơi đòi, và mọi điều kiện, giới hạn dựa, hoặc cò mở lại gắn mất cân bền.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá hỗ trợ xuyên hệ thống phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn quản trị có trách nhiệm có trọng hạ tầng chung hoặc phụ thuộc nền đòi chứng tương xứng mạnh hơn rằng rút, dòng hoàn trả, và đủ mức hỗ trợ đã được đánh giá chứ không khẳng định.

**Khiếm khuyết và lệch lạc.** Che, trình bày sai, mảnh, hoặc đổ thông tin phụ thuộc hoặc dòng tài nguyên có trọng nơi **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) đòi công bố; coi chuyển tượng trưng, đục, hoặc một lần là thỏa [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional); rút bền không hoàn trả tương xứng nơi cò trọng yếu áp; hoặc chứng nhận tiếp tục dựa trong khi hỗ trợ không đủ đã ghi đe dọa có trọng thẳng hàng hiến pháp phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="61-illustrative-cross-system-support-application-by-class"></a>

<a id="61-illustrative-cross-system-support-application-by-class-non-exhaustive"></a>
#### 6.1 Áp dụng hỗ trợ xuyên hệ thống minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) đến [§5.1](#51-illustrative-ecological-footprint-application-by-class) đi cùng ba hệ thống qua miền đánh giá trước. Tiểu mục này cho thấy **đóng góp xuyên hệ thống tương xứng** nghĩa gì cho từng cái — phụ thuộc chung nào được tính, chứng nhận phải kiểm gì khi cò trọng yếu **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) áp, và điều phải xuất hiện trên hồ sơ. **Rút** ở đây nghĩa là **kéo tài nguyên và tài trợ từ hạ tầng chung** (xem [§6](#6-proportionate-cross-system-support-evaluation) *«Rút» nghĩa gì ở đây*) — không sao dữ liệu lâm sàng, dùng quảng cáo, hoặc bán không liên cho bên thứ ba. CS-8, CS-9, và Chương Năm vẫn nắm cơ học phân bổ; những đi qua này không kê chia, công thức, hoặc mô hình tài trợ.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố dựa vào lưu vực hoặc tầng chứa nước chung, liên kết điện khối vùng, chuỗi cung hóa chất và lọc sỉ, thỏa liên kết khẩn chung, và dịch vụ theo dõi hoặc điều khiển nhà cung vận hành mà tiện ích hoặc cộng đồng khác cũng có thể dựa.

- **Phụ thuộc và dòng trong phạm vi:**
  - Quyền nước nguồn và hạ tầng lưu vực chung với nông nghiệp, công nghiệp, và đô thị láng giềng;
  - liên kết lưới và gánh tải đỉnh lên hạ tầng điện vùng;
  - hành lang mua và logistics hóa chất chung;
  - thỏa bơm tương trợ, liên kết, và cung khẩn;
  - dịch vụ **SCADA** (điều khiển giám sát và thu thập dữ liệu — vận hành từ xa bơm, van, và thiết bị xử lý), **đo xa** (tín hiệu áp suất, lưu lượng, và cảnh báo sống từ cảm biến hiện trường), và **SOC** (trung tâm vận hành an ninh — theo dõi nhà cung cho xâm nhập, sự cố, và sự kiện an toàn) được ủy, lưu trữ trên hạ tầng điều khiển nhà cung hoặc vùng chung;
  - dòng vốn và bảo trì từ người trả phí, trái phiếu, trợ cấp, hoặc thẩm quyền vùng trở lại bảo vệ nguồn, đổi ống, và giữ xương sống chung.
- **Đánh giá phải thử:**
  - Liệu bản đồ hệ thống phụ thuộc và hồ sơ dòng tài nguyên kiểm toán được **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) có nhận diện rút từ lưu vực, lưới, chuỗi cung, và xương sống tương trợ chung — không chỉ sổ nội bộ của tiện ích;
  - liệu dòng hoàn trả — bảo vệ nguồn, đổi hạ tầng, phục hồi lưu vực, năng lực khẩn vùng, và chia phí công bằng cho dùng xương sống chung — có tới đủ mức nội dung dưới [Đóng góp xuyên hệ thống tương xứng](core_05_band_continuity.md#proportionate-cross-system-support-constitutional), đánh giá dưới [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) và [Tính tương xứng](core_05_band_accountability.md#proportionality);
  - liệu trợ cấp một lần, phí nhà cung đục, hoặc chuyển phí hạ nguồn đã được coi là hoàn trả đủ;
  - liệu [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint) và [Bền vững](core_05_band_continuity.md#sustainability) dài hạn đã được ghép nơi rút lưu vực hoặc năng lượng có trọng; và
  - liệu quản trị có trách nhiệm **Class A** đối với tài nguyên chung then chốt sống còn đã nhận phân tích đủ mức hỗ trợ mạnh nhất trên sự kiện.
- **Hồ sơ phải cho thấy:**
  - Cò trọng yếu **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) được dựa;
  - phạm vi bản đồ hệ thống phụ thuộc và dòng tài nguyên ở độ sâu **Class A**;
  - phát hiện rút từ phụ thuộc lưu vực, lưới, chuỗi cung, và điều khiển chung;
  - phát hiện dòng hoàn trả và đủ mức hỗ trợ;
  - bất định;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi đòi; và
  - điều kiện hoặc cò mở lại gắn mất cân bền, căng lưu vực, hoặc rút không công từ hạ tầng sống còn chung.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe định tuyến hồ sơ giữa bệnh viện và phòng khám qua dịch vụ xác thực chung, liên kết xương sống CNTT sức khỏe vùng, hạ tầng giải danh tính, và vùng lưu trữ hoặc tính toán chung được dựa rộng — nền tảng mà phòng khám nhỏ hơn và hệ thống y tế công cũng dựa.

- **Phụ thuộc và dòng trong phạm vi:**
  - Hạ tầng danh tính và xác thực chung;
  - liên kết mạng thông tin sức khỏe vùng;
  - kết nối và lưu trữ biên bệnh viện tham gia;
  - vùng lưu trữ chung hoặc cơ sở đặt chung;
  - trợ cấp công, khoản thu người tham gia, hoặc dòng thuê nhằm giữ khả năng tương tác;
  - dịch vụ môi giới danh tính, danh bạ, và khử trùng lặp dùng lại xuyên hệ sinh thái chăm sóc.
- **Đánh giá phải thử:**
  - Liệu bản đồ hệ thống phụ thuộc có nhận diện **kéo tài nguyên không công từ hạ tầng chung** — chứ không chỉ nhìn hợp đồng nhà cung tư trực tiếp của người vận hành trao đổi. Ví dụ:
    - phí người tham gia, trợ cấp, hoặc ngân sách người vận hành dùng nền tảng xác thực, danh bạ, mạng, hoặc lưu trữ vùng mà không trả phần công bằng của giữ;
    - tải tính toán và kết nối đặt lên xương sống CNTT sức khỏe chung; hoặc
    - gánh bảo trì và đáp sự cố chuyển sang bệnh viện nhỏ hơn.
    
    Đây **không** phải thử liệu trao đổi bán hồ sơ, khai dữ liệu cho quảng cáo, hoặc gửi nội dung lâm sàng tới bên ngoài không liên; những câu đó thuộc [§4](#4-data-types-and-handling-evaluation) và bảo vệ quyền riêng tư Chương Sáu.
  - Nơi kéo tài nguyên chung có trọng, liệu phòng khám nhỏ hơn, nhà cung nông thôn, hoặc người tham gia y tế công có mang phí kết nối hoặc tham gia bất đối xứng;
  - liệu dòng hoàn trả — giữ khả năng tương tác, quản trị có trách nhiệm danh bạ, hỗ trợ gia nhập, khắc phục sự cố, và chia phí người tham gia công bằng — có hỗ trợ nội dung hạ tầng chung người khác dựa;
  - liệu chuyển tượng trưng hoặc một lần đã được coi là hoàn trả đủ; và
  - liệu đủ mức hỗ trợ đã được đánh giá ở độ then chốt vận hành **Class B** chứ không khẳng định chỉ từ dòng ngân sách gộp.
- **Hồ sơ phải cho thấy:**
  - Cò và phạm vi đánh giá **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*);
  - phát hiện **dòng tài nguyên hạ tầng chung** — phí, tài trợ, tính toán, kết nối, và gánh bảo trì rút từ và trả về phụ thuộc CNTT sức khỏe và xác thực chung;
  - phát hiện dòng hoàn trả và đủ mức hỗ trợ ở độ sâu **Class B**;
  - phát hiện công bằng cho gánh người tham gia bất đối xứng nơi có trọng;
  - bất định và phát hiện thành phần nơi đòi; và
  - cò mở lại nếu tăng dựa người tham gia, rủi ro sự cố, hoặc định tuyến y tế công giờ sẽ đòi rà hỗ trợ nâng — kể cả lên tư thế **Class A** nơi định tuyến chăm sóc thiết yếu sống còn cùng bị liên lụy.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức có thể định tuyến thanh toán nhà cung, mua sắm thể chế, liên đoàn danh tính, hoặc năng lực tính toán lưu trữ vùng qua nền tảng chung — nhưng nhiều triển khai đặt rút trực tiếp nhẹ hơn cho đến khi tập trung làm nền tảng thành cổ chai phối hợp.

- **Phụ thuộc và dòng trong phạm vi:**
  - Vùng lưu trữ chung, liên đoàn danh tính, ray thanh toán hoặc mua sắm dùng cho đặt nhà cung;
  - dòng thuê và giấy phép thể chế;
  - dịch vụ API hoặc danh bạ dùng lại xuyên bệnh viện, trường, và cơ quan tham gia;
  - hiệu ứng tập trung nơi một nền tảng trung gian phối hợp nhân sự, phòng, hoặc nhà cung cho nhiều tổ chức.
- **Đánh giá phải thử:**
  - Liệu cò trọng yếu **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) thật sự áp — kể cả nơi nền tảng định tuyến có trọng quỹ, phân bổ phí, hoặc rút năng lực từ hạ tầng chung người khác dựa;
  - liệu bản đồ hệ thống phụ thuộc đã được phạm trung thực chứ không bỏ vì người vận hành gắn nhãn hệ thống không then chốt;
  - liệu dòng hoàn trả — giữ khả năng tương tác, cấu trúc phí công bằng, hỗ trợ sự cố, và đường lối ra mở cho thể chế tham gia — đã được đánh giá nơi rút có trọng;
  - liệu tập trung ở một lớp lịch có dịch phí phối hợp hoặc rủi ro phụ thuộc lên thể chế nhỏ hơn không hỗ trợ tương xứng; và
  - liệu **theo dõi tái phân hạng** có đòi nơi nền tảng trở thành cổ chai thực tế cho nhân sự thiết yếu sống còn, định tuyến khẩn, hoặc phối hợp thanh toán.
- **Hồ sơ phải cho thấy:**
  - Liệu và vì sao cò **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) áp;
  - phát hiện phụ thuộc và dòng tài nguyên tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện rút và dòng hoàn trả nơi có trọng — không khẳng định trống rằng không hạ tầng chung bị liên lụy;
  - phát hiện tập trung và cổ chai;
  - **theo dõi tái phân hạng** rõ nơi phụ thuộc mạnh lên; và
  - con trỏ tới rà hỗ trợ xuyên hệ thống nâng nếu lớp, định tuyến thanh toán, hoặc vai phối hợp thiết yếu sống còn đổi.

**Đọc xuyên lớp.** Cùng kỷ luật **Điều IV-A** (*Ánh xạ phụ thuộc và minh bạch dòng tài nguyên*) và **Điều IV-B** (*Công bằng xuyên hệ thống và bền vững*) áp nơi cò trọng yếu được thỏa; lớp đổi độ sâu bản đồ và soi đủ mức, không phép coi rút chung là vô trọng. Một hệ thống nước **Class A** rút từ lưu vực chung hoặc xương sống lưới vùng phải mang trên hồ sơ chứng bản đồ hệ thống phụ thuộc và dòng hoàn trả mạnh nhất. Một trao đổi **Class B** dựa hạ tầng xác thực và CNTT sức khỏe chung phải ghi phát hiện rút và đủ mức hỗ trợ ở độ then chốt vận hành — không khẩu hiệu khả năng tương tác chung. Một nền tảng lịch **Class C** không được lẩn rà xuyên hệ thống trong khi lặng lẽ trở thành cổ chai thanh toán, danh tính, hoặc nhân sự cho thể chế không thể thay thực tiễn; khi điều đó xảy ra, chứng nhận phải nâng rà và tái phân hạng dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), kể cả lên **Class A** nơi phối hợp thiết yếu sống còn bị cổng. Đi qua không phân biệt đối xử cho cùng hệ thống nằm ở [§7.1](#71-illustrative-nondiscrimination-application-by-class).

<a id="7-nondiscrimination-evaluation"></a>

### 7. Đánh giá không phân biệt đối xử

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Tham gia (*Công bằng nội dung và Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch như đo lường hiến pháp*); **Điều V-B** (*Không phân biệt đối xử*); [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional), [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional), [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [Ngôn ngữ, văn hóa, và di sản](core_05_band_continuity.md#language-culture-and-heritage-constitutional), [Sự cần thiết](core_05_band_accountability.md#necessity), và [Tính tương xứng](core_05_band_accountability.md#proportionality) (Chương Năm).
- Hạ nguồn: [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*đi qua không phân biệt đối xử minh họa*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*lệch lạc mẫu phân biệt và lẩn tránh chỉ số thay*).
- Đọc cùng: **Điều V-C** (*Bao gồm đầy đủ và bình đẳng trong phân xử và vận hành*) nơi chứng nhận cổng lối vào diễn đàn, hành chính, hoặc cưỡng chế; [*Không phân biệt đối xử, Đặc điểm được bảo vệ, Phẩm giá, Cổng tín hiệu thân mật, và trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)*](core_05_band_participation.md#fairness-and-protected-status-semi-independent).
- Tiểu mục: [§7.1](#71-illustrative-nondiscrimination-application-by-class) (*áp dụng không phân biệt đối xử minh họa theo lớp*).

</details>

<br>

*Nói thẳng: khi một hệ thống quyết có trọng ai được vào, ai trả nhiều hơn, ai bị xếp thấp hơn, hoặc ai mang gánh tệ hơn, chứng nhận phải kiểm liệu mẫu đó chất hại lên đặc điểm được bảo vệ hoặc chỉ số thay của chúng — không phải liệu người vận hành nói quy tắc trung lập. Hạn ngạch bao gồm và thuật toán công bằng cụ thể có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; chứng nhận kiểm rằng mẫu gánh-và-lợi và rủi ro chỉ số thay thật sự được đánh giá nơi cò áp. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§7.1](#71-illustrative-nondiscrimination-application-by-class).*

**Cò trọng yếu.** Mục này áp nơi một hệ thống có tác động vật chất phân loại, xếp hạng, định giá, cổng, loại, hoặc phân bổ gánh và lợi có trọng giữa hữu tri — kể cả qua quy tắc đủ điều kiện, đặc trưng mô hình, logic xếp hạng, chính sách nền tảng, hoặc đường quyết định tương đương. Nó không đòi kiểm toán không phân biệt đối xử đầy trên mọi hồ sơ chứng nhận.

Chứng nhận thẳng hàng hệ thống phải đánh giá **không phân biệt đối xử** dưới **Điều V-B** (*Không phân biệt đối xử*), [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional), và [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) nơi cò trọng yếu áp. Nghĩa chuẩn, yếu tố đánh giá, và kỷ luật không tuân sống ở Chương Năm và **Điều V-B** (*Không phân biệt đối xử*); mục tiêu bao gồm, cơ học điều chỉnh, và chi tiết quản trị mô hình có thể sống ở công cụ hợp nhất, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học vận hành đó hay kê cụ thể ở đây.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu đường quyết định hệ thống dựa có trọng có đặt gánh, loại, hoặc hại có trọng lên hữu tri dựa trên [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional), chỉ số thay của chúng, hoặc nhóm tùy ý dùng làm vật thay chức năng, kể cả chuyên hóa ngôn ngữ, văn hóa, và di sản dưới [Ngôn ngữ, văn hóa, và di sản](core_05_band_continuity.md#language-culture-and-heritage-constitutional). Đánh giá phải thử mẫu gánh-và-lợi dưới [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) và rủi ro chỉ số thay hoặc tác động lệch dưới [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake). Đối xử lệch chỉ chấp nhận được nơi [Sự cần thiết](core_05_band_accountability.md#necessity), [Tính tương xứng](core_05_band_accountability.md#proportionality), và công bằng nội dung đã ghi biện minh. Đánh giá phải phản hiệu ứng chức năng, không trung lập danh nghĩa, ý định tuyên, hoặc nhãn một mình.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu cò trọng yếu **Điều V-B** (*Không phân biệt đối xử*) được dựa, phạm vi đánh giá cho đường phân loại, xếp hạng, định giá, cổng, loại, và phân bổ gánh được dựa có trọng, phát hiện đặc điểm được bảo vệ và phân biệt qua chỉ số thay, phát hiện công bằng nội dung, bất định, phát hiện diễn đàn hữu tri hoặc thành phần được gán khác nơi đòi, và mọi điều kiện, giới hạn dựa, hoặc cò mở lại gắn gánh lệch bền hoặc loại.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá không phân biệt đối xử phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn cổng có trọng lối vào, xếp hạng hữu tri, hoặc phân bổ gánh và lợi đòi chứng tương xứng mạnh hơn rằng gánh đặc điểm được bảo vệ, phân biệt qua chỉ số thay, và thiếu công bằng nội dung đã được đánh giá chứ không khẳng định.

**Khiếm khuyết và lệch lạc.** Che, trình bày sai, mảnh, hoặc đổ logic phân loại, xếp hạng, hoặc phân bổ gánh có trọng nơi **Điều V-B** (*Không phân biệt đối xử*) đòi rà; coi trung lập bề mặt, thước thuận tiện gộp, hoặc tự báo người vận hành là đủ không có phân tích gánh-và-lợi đánh giá được; chứng nhận tiếp tục dựa trong khi phân biệt qua chỉ số thay hoặc thiếu công bằng nội dung đã ghi đe dọa có trọng thẳng hàng hiến pháp; hoặc dùng khung đồng nhất hóa, khả năng tương tác, hoặc hiệu suất để đánh bại bảo vệ ngôn ngữ, văn hóa, hoặc di sản mà không thỏa phép thử **Sự cần thiết** và **Tính tương xứng** của **Điều V-B** (*Không phân biệt đối xử*) phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="71-illustrative-nondiscrimination-application-by-class"></a>

<a id="71-illustrative-nondiscrimination-application-by-class-non-exhaustive"></a>
#### 7.1 Áp dụng không phân biệt đối xử minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) đến [§6.1](#61-illustrative-cross-system-support-application-by-class) đi cùng ba hệ thống qua miền đánh giá trước. Tiểu mục này cho thấy đánh giá **không phân biệt đối xử** nghĩa gì cho từng cái — đường quyết định nào được tính, chứng nhận phải kiểm gì khi cò trọng yếu **Điều V-B** (*Không phân biệt đối xử*) áp, và điều phải xuất hiện trên hồ sơ. Chương Năm và **Điều V-B** (*Không phân biệt đối xử*) vẫn nắm quy tắc công bằng và phân biệt qua chỉ số thay chuẩn; hạn ngạch bao gồm, mục tiêu nhân khẩu, và thiết kế thuật toán công bằng có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; những đi qua này không kê cơ học đó.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố áp quy tắc cắt, nối lại, kế hoạch thanh toán, thông báo sự cố, và cảnh báo an toàn quyết có trọng ai mất lối vào nước, ai được báo trước, và ai mang phí khôi dịch vụ.

- **Đường quyết định trong phạm vi:**
  - Trình tự cắt và khôi dịch vụ;
  - thế chấp, thanh toán, và đủ điều kiện kế hoạch trả;
  - duyệt nối mới và nối lại;
  - định tuyến thông báo sự cố và chọn ngôn ngữ;
  - nhắm cảnh báo nhiễm hoặc đun sôi nước;
  - quy tắc chủ nhà–người thuê và lịch sử địa chỉ cổng lối vào;
  - ưu tiên vượt khẩn hoặc tương trợ nơi nhiều khu tranh cung hạn.
- **Đánh giá phải thử:**
  - Liệu mẫu gánh-và-lợi dưới [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) đã được đánh giá cho đường có thể khóa thiết yếu sống còn — không chỉ liệu người vận hành gắn nhãn quy tắc «dựa rủi ro» hoặc «vận hành»;
  - liệu logic cắt, thanh toán, hoặc thông báo chất hại lệch lên hữu tri dựa trên [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional), chỉ số thay của chúng, hoặc nhóm tùy ý dùng làm vật thay chức năng;
  - liệu đặc trưng mã bưu chính, chủ nhà, ngôn ngữ, lịch sử thanh toán, hoặc lịch sử địa chỉ có vận hành như phân biệt qua chỉ số thay dưới [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact);
  - liệu bảo vệ [Ngôn ngữ, văn hóa, và di sản](core_05_band_continuity.md#language-culture-and-heritage-constitutional) đã được thử chứ không đồng nhất hóa qua «chỉ tiếng Anh chuẩn» hoặc thước thuận tiện gộp; và
  - liệu mọi đối xử lệch có thỏa [Sự cần thiết](core_05_band_accountability.md#necessity) và [Tính tương xứng](core_05_band_accountability.md#proportionality) đã ghi.
- **Hồ sơ phải cho thấy:**
  - Cò trọng yếu **Điều V-B** (*Không phân biệt đối xử*) được dựa;
  - phạm vi đánh giá cho đường cắt, thanh toán, thông báo, và nối được dựa có trọng;
  - phát hiện đặc điểm được bảo vệ, phân biệt qua chỉ số thay, và công bằng nội dung ở độ sâu **Class A**;
  - bất định;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi đòi; và
  - điều kiện hoặc cò mở lại gắn gánh cắt, thông báo, hoặc thanh toán lệch bền nơi thiết yếu sống còn bị cổng.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe định tuyến hồ sơ giữa bệnh viện và phòng khám qua quy tắc đồng thuận, giải danh tính, xếp hạng danh bạ nhà cung, lối vào break-glass, và đủ điều kiện gia nhập người tham gia quyết có trọng ai thấy được chăm sóc nào, cơ sở nào nối trước, và bệnh nhân nào khớp đúng xuyên mạng.

- **Đường quyết định trong phạm vi:**
  - Khớp danh tính bệnh nhân và khử trùng lặp;
  - quy tắc đồng thuận, break-glass, và lối vào khẩn;
  - xếp hạng danh bạ nhà cung và cơ sở hoặc logic mạng ưu tiên;
  - gia nhập và đình chỉ bệnh viện tham gia;
  - quy tắc định tuyến hồ sơ và ưu tiên truy vấn;
  - đặc trưng dẫn dùng để xếp nhà cung, định tuyến chuyển, hoặc gắn cờ đoàn «dùng cao» hoặc tương đương.
- **Đánh giá phải thử:**
  - Liệu đường phân loại, xếp hạng, và cổng đã được đánh giá theo hiệu ứng chức năng — không chỉ tuyên trung lập HIPAA danh nghĩa hoặc khả năng tương tác;
  - liệu logic khớp, định tuyến, hoặc danh bạ đặt loại hoặc hại có trọng lên nhóm được bảo vệ hoặc chỉ số thay của chúng;
  - liệu lỗi khử trùng lặp, ngưỡng break-glass, hoặc quy tắc gia nhập chất gánh lệch lên phòng khám nông thôn, bệnh nhân thiểu số ngôn ngữ, hoặc đoàn tương đương;
  - liệu «hiệu suất», «phòng gian lận», hoặc thước dùng gộp đã được dùng để đánh bại công bằng nội dung mà không thỏa phép thử **Sự cần thiết** và **Tính tương xứng** của **Điều V-B** (*Không phân biệt đối xử*); và
  - liệu độ sâu đánh giá khớp độ then chốt vận hành **Class B** nơi xếp hạng ảnh hưởng lối vào chăm sóc sức khỏe, định tuyến lợi ích, hoặc an ninh thu nhập.
- **Hồ sơ phải cho thấy:**
  - Cò và phạm vi đường **Điều V-B** (*Không phân biệt đối xử*);
  - phát hiện đặc điểm được bảo vệ và phân biệt qua chỉ số thay;
  - phát hiện công bằng nội dung cho quy tắc xếp hạng, khớp, và lối vào;
  - bất định và phát hiện thành phần nơi đòi; và
  - cò mở lại nếu đổi định tuyến hoặc khớp giờ sẽ chặn chăm sóc khẩn trong khung thời gian liên quan sống còn hoặc dịch có trọng gánh lệch.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức gán ca, đặt phòng, khớp nhà cung, và phân bổ ưu tiên phối hợp xuyên bệnh viện, trường, và cơ quan công — đường quyết định có thể xếp, loại, hoặc chất gánh không đều ngay khi nền tảng không tự là tiện ích then chốt sống còn.

- **Đường quyết định trong phạm vi:**
  - Gán ca, giờ thêm, và phân bổ trực;
  - ưu tiên đặt phòng, thiết bị, và địa điểm;
  - khớp nhà cung và xếp hạng mua sắm;
  - quy tắc lối vào theo vai thể chế, giấy thông hành, và cơ sở;
  - đặc trưng lịch dẫn tương quan với khu phố, cộng đồng ngôn ngữ, trạng thái người chăm, hoặc chỉ số thay tương đương;
  - quy tắc API hoặc chính sách loại thể chế nhỏ hơn khỏi khung ưu tiên hoặc hồ nhà cung.
- **Đánh giá phải thử:**
  - Liệu cò trọng yếu **Điều V-B** (*Không phân biệt đối xử*) áp — kể cả nơi thuật toán phối hợp xếp có trọng nhân sự, nhà cung, hoặc thể chế;
  - liệu địa lý lịch, chỉ số thay thâm niên, «điểm sẵn có», hoặc logic xếp nhà cung chất gánh lệch lên nhóm được bảo vệ không biện minh đánh giá được;
  - liệu quy tắc trung lập bề mặt sản thiếu công bằng nội dung qua giờ ca, gánh đi lại, hoặc loại khỏi đặt giá trị cao;
  - liệu người vận hành coi nền tảng dưới rà vì nó **Class C** trong khi hiệu ứng phối hợp cổng có trọng việc làm, giáo dục, hoặc lối vào dịch vụ công; và
  - liệu **theo dõi tái phân hạng** có đòi nơi nền tảng trở thành cổ chai thực tế cho nhân sự thiết yếu sống còn hoặc định tuyến khẩn.
- **Hồ sơ phải cho thấy:**
  - Liệu và vì sao cò **Điều V-B** (*Không phân biệt đối xử*) áp;
  - phạm vi đánh giá cho đường xếp hạng, gán, và loại tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện đặc điểm được bảo vệ, chỉ số thay, và công bằng nội dung nơi có trọng — không khẳng định trống rằng không ai bị xếp;
  - phát hiện tập trung và cổ chai nơi hiệu ứng lịch báo trước leo;
  - **theo dõi tái phân hạng** rõ nơi phụ thuộc mạnh lên; và
  - con trỏ tới rà không phân biệt đối xử nâng nếu lớp, định tuyến thanh toán, hoặc vai phối hợp thiết yếu sống còn đổi.

**Đọc xuyên lớp.** Cùng kỷ luật không phân biệt đối xử **Điều V-B** (*Không phân biệt đối xử*) và Chương Năm áp nơi cò trọng yếu được thỏa; lớp đổi độ sâu đánh giá, không phép coi xếp hạng hoặc dịch gánh là vô trọng. Một hệ thống nước **Class A** mà quy tắc cắt hoặc thông báo có thể khóa nước an toàn phải mang trên hồ sơ phân tích gánh-và-lợi và chỉ số thay mạnh nhất — không tuyên «thực hành tốt tiện ích» chung. Một trao đổi **Class B** mà logic khớp hoặc định tuyến ảnh hưởng chăm sóc khẩn, lợi ích, hoặc lối vào giấy thông hành phải ghi phát hiện tác động lệch và công bằng nội dung ở độ then chốt vận hành. Một nền tảng lịch **Class C** không được giữ đoạn công bằng hình thức trong khi logic ca, nhà cung, hoặc đặt chỗ xếp hạng hoặc loại có trọng người tham gia; khi phối hợp trở thành thiết yếu sống còn, chứng nhận phải nâng rà và tái phân hạng dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), kể cả lên **Class A** nơi nhân sự hoặc định tuyến khẩn bị cổng. Đi qua khả năng tiếp cận cho cùng hệ thống nằm ở [§8.1](#81-illustrative-accessibility-application-by-class).

<a id="8-accessibility-evaluation"></a>

### 8. Đánh giá khả năng tiếp cận

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Tham gia (*Khả năng tiếp cận như đo lường hiến pháp*); **Điều V-G** (*Khả năng tiếp cận*); [Khả năng tiếp cận](core_05_band_participation.md#accessibility-constitutional), [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination), [Phụ thuộc](core_05_band_continuity.md#dependency), [Quyền năng có ý nghĩa](core_05_band_participation.md#meaningful-agency), [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional), [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional), [Sự cần thiết](core_05_band_accountability.md#necessity), và [Tính tương xứng](core_05_band_accountability.md#proportionality) (Chương Năm).
- Hạ nguồn: [§8.1](#81-illustrative-accessibility-application-by-class) (*đi qua khả năng tiếp cận minh họa*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*lệch lạc khả năng tiếp cận và điều chỉnh chỉ-trên-giấy*).
- Đọc cùng: **Điều III-B** (*Lối vào giáo dục bình đẳng*) nơi khả năng tiếp cận giáo dục bị liên lụy — khả năng tiếp cận riêng giáo dục vẫn được nắm ở đó; **Điều V-C** (*Bao gồm đầy đủ và bình đẳng trong phân xử và vận hành*) và **Điều XI** (*Tham gia hệ thống của bên bị ảnh hưởng, đại diện, và thủ tục đúng đắn*) nơi chứng nhận cổng tham gia diễn đàn, hành chính, bên bị ảnh hưởng, hoặc cưỡng chế; [Chương Bảy §3.2](core_07_a_system_alignment_certification_evaluation.md#32-accessibility-under-sentience-non-exclusion) (*móc yếu tố đánh giá khả năng tiếp cận cắt ngang*).
- Tiểu mục: [§8.1](#81-illustrative-accessibility-application-by-class) (*áp dụng khả năng tiếp cận minh họa theo lớp*).

</details>

<br>

*Nói thẳng: khi một hệ thống kiểm có trọng liệu hữu tri có thực sự tham gia được — không chỉ liệu một cửa gắn nhãn «mở» — chứng nhận phải kiểm liệu tham gia thật sự tới được xuyên nhu cầu giác quan, nhận thức, vận động, giao tiếp, giao diện nền, và tương đương. Danh mục điều chỉnh và chuẩn giao diện có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; chứng nhận kiểm rằng tham gia nội dung thật sự được đánh giá nơi cò áp. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§8.1](#81-illustrative-accessibility-application-by-class).*

**Cò trọng yếu.** Mục này áp nơi một hệ thống có tác động vật chất cổng có trọng tham gia nội dung ở miền hiến pháp liên quan — kể cả quản trị, tham gia bên bị ảnh hưởng, phân xử, vận hành, lối vào sàn sống còn, lối vào chăm sóc sức khỏe, biểu đạt, tụ họp, báo chí, hoặc miền tương đương — qua giao diện, địa điểm, lịch, giấy thông hành, lối vào tính toán, thiết kế điều chỉnh, hoặc đường tham gia tương đương. Nó không đòi kiểm toán khả năng tiếp cận đầy trên mọi hồ sơ chứng nhận. Khả năng tiếp cận giáo dục vẫn do **Điều III-B** (*Lối vào giáo dục bình đẳng*) quản trị và không bị thu hẹp ở đây.

Chứng nhận thẳng hàng hệ thống phải đánh giá **khả năng tiếp cận** dưới **Điều V-G** (*Khả năng tiếp cận*) và [Khả năng tiếp cận](core_05_band_participation.md#accessibility-constitutional) nơi cò trọng yếu áp. Nghĩa chuẩn, yếu tố đánh giá, và kỷ luật không tuân sống ở Chương Năm và **Điều V-G** (*Khả năng tiếp cận*); danh mục điều chỉnh, chuẩn giao diện, đặc tả thiết kế phổ quát, và cơ học điều chỉnh vận hành sống ở công cụ hợp nhất nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học vận hành đó hay kê danh mục điều chỉnh cụ thể hoặc đặc tả thiết kế phổ quát.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu hữu tri có tham gia nội dung được các miền hiến pháp liên quan mà hệ thống cổng có trọng — không chỉ liệu tiện nghi hình thức, giao diện mặc định, hoặc điều chỉnh giấy tờ có tồn tại. Đánh giá phải thử hiệu ứng tham gia nội dung dưới [Khả năng tiếp cận](core_05_band_participation.md#accessibility-constitutional), chia tỷ lệ theo [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) và [Phụ thuộc](core_05_band_continuity.md#dependency), và phải phát hiện điều chỉnh chỉ-trên-giấy, mẫu «lối vào chung» dựa vào tiện nghi mặc định mà không sản năng lực tham gia, lập luận trọng yếu chọn lọc dùng để co phạm vi điều chỉnh, loại trái [Không loại trừ hữu tri](core_05_band_participation.md#sentience-non-exclusion), và thiết kế chống từ chối-qua-chỉ-số-thay qua lịch, chọn địa điểm, cấp giấy thông hành, lối vào tính toán, hoặc cơ học tương đương. Đánh giá phải áp [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional) và [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) vào logic thiết kế điều chỉnh. Mọi giới hạn phải thỏa [Sự cần thiết](core_05_band_accountability.md#necessity), [Tính tương xứng](core_05_band_accountability.md#proportionality), và [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) đã ghi.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu cò trọng yếu **Điều V-G** (*Khả năng tiếp cận*) được dựa, phạm vi đánh giá cho đường tham gia được dựa có trọng, phát hiện tham gia nội dung và điều chỉnh, phát hiện chống từ chối-qua-chỉ-số-thay nơi có trọng, bất định, phát hiện diễn đàn hữu tri hoặc thành phần được gán khác nơi đòi, và mọi điều kiện, giới hạn dựa, hoặc cò mở lại gắn rào tham gia bền.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá khả năng tiếp cận phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn cổng có trọng tham gia hiến pháp liên quan đòi chứng tương xứng mạnh hơn rằng khả năng tiếp cận nội dung đã được đánh giá chứ không khẳng định.

**Khiếm khuyết và lệch lạc.** Coi tiện nghi hình thức, giao diện mặc định, hoặc điều chỉnh giấy tờ là đủ không có phân tích tham gia nội dung đánh giá được; chứng nhận tiếp tục dựa trong khi rào tham gia đã ghi đe dọa có trọng thẳng hàng hiến pháp; dùng khung chi phí, lựa chọn thiết kế, lớp nền, hoặc quy mô vận hành để đánh bại sàn tham gia mà không thỏa phép thử **Sự cần thiết** và **Tính tương xứng** của **Điều V-G** (*Khả năng tiếp cận*); hoặc thiết kế vận hành có hiệu ứng đánh bại khả năng tiếp cận nơi một lựa chọn ít gánh hơn khả thi phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="81-illustrative-accessibility-application-by-class"></a>

<a id="81-illustrative-accessibility-application-by-class-non-exhaustive"></a>
#### 8.1 Áp dụng khả năng tiếp cận minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) đến [§7.1](#71-illustrative-nondiscrimination-application-by-class) đi cùng ba hệ thống qua miền đánh giá trước. Tiểu mục này cho thấy đánh giá **khả năng tiếp cận** nghĩa gì cho từng cái — đường tham gia nào được tính, chứng nhận phải kiểm gì khi cò trọng yếu **Điều V-G** (*Khả năng tiếp cận*) áp, và điều phải xuất hiện trên hồ sơ. Chương Năm và **Điều V-G** (*Khả năng tiếp cận*) vẫn nắm quy tắc khả năng tiếp cận chuẩn; danh mục điều chỉnh, chuẩn giao diện, và đặc tả thiết kế phổ quát có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; những đi qua này không kê cơ học đó. Khả năng tiếp cận giáo dục vẫn do **Điều III-B** (*Lối vào giáo dục bình đẳng*) nắm và không bị thu hẹp ở đây.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố cổng lối vào sàn sống còn qua cổng thanh toán, kênh thông báo sự cố, yêu cầu nối lại, cảnh báo đun sôi nước, và đường dịch vụ khách quyết liệu hữu tri có biết, tranh biện, hoặc khôi nước an toàn.

- **Đường tham gia trong phạm vi:**
  - Cổng thanh toán và kế hoạch trả;
  - kênh cảnh báo sự cố và nhiễm (thoại, tin, web, trực tiếp, hoặc đường nhà cung ủy);
  - giao diện nối lại và yêu cầu khó khăn;
  - lựa chọn ngôn ngữ và định dạng cho thông báo an toàn;
  - cổng giấy thông hành hoặc danh tính cho lối vào tài khoản;
  - yêu cầu tính toán, thiết bị, hoặc địa điểm để nộp tranh biện hoặc nhận cảnh báo.
- **Đánh giá phải thử:**
  - Liệu hữu tri có nhận nội dung thông báo then chốt sống còn và hoàn đường nối lại hoặc khó khăn xuyên hồ sơ giác quan, nhận thức, vận động, giao tiếp, và giao diện nền — không phải liệu một mẫu web mặc định tồn tại;
  - liệu điều chỉnh chỉ-trên-giấy, «gọi trong giờ làm», hoặc mặc định chỉ-tiếng-Anh đánh bại tham gia nơi lựa chọn ít gánh hơn khả thi;
  - liệu thiết kế lịch, địa điểm, giấy thông hành, hoặc tính toán vận hành như từ chối-qua-chỉ-số-thay;
  - liệu [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional) và [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) đã được áp vào logic thiết kế điều chỉnh; và
  - liệu mọi giới hạn thỏa [Sự cần thiết](core_05_band_accountability.md#necessity), [Tính tương xứng](core_05_band_accountability.md#proportionality), và [Công bằng nội dung](core_05_band_participation.md#substantive-fairness-constitutional) đã ghi.
- **Hồ sơ phải cho thấy:**
  - Cò trọng yếu **Điều V-G** (*Khả năng tiếp cận*) được dựa;
  - phạm vi đánh giá cho đường thông báo, thanh toán, nối lại, và tranh biện được dựa có trọng;
  - phát hiện tham gia nội dung và điều chỉnh ở độ sâu **Class A**;
  - phát hiện chống từ chối-qua-chỉ-số-thay nơi có trọng;
  - bất định;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi đòi; và
  - điều kiện hoặc cò mở lại gắn rào bền nơi thiết yếu sống còn bị cổng.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe và cổng người tham gia của nó cổng lối vào chăm sóc sức khỏe hàng ngày qua cổng bệnh nhân, giao diện đồng thuận, danh bạ nhà cung, luồng break-glass, và công cụ gia nhập phòng khám quyết liệu bệnh nhân và nhà cung nhỏ hơn có thực sự dùng được trao đổi.

- **Đường tham gia trong phạm vi:**
  - Cổng bệnh nhân và giao diện đồng thuận;
  - công cụ danh bạ nhà cung và đặt chuyển;
  - luồng break-glass và lối vào khẩn;
  - giao diện gia nhập và cấp giấy thông hành phòng khám;
  - hỗ trợ ngôn ngữ, định dạng, và công nghệ trợ giúp cho tóm tắt lâm sàng và công bố;
  - yêu cầu tính toán hoặc thiết bị để xem, tranh biện, hoặc sửa hồ sơ.
- **Đánh giá phải thử:**
  - Liệu bệnh nhân và phòng khám tham gia có dùng nội dung đường đồng thuận, lối vào, sửa, và khẩn — không phải liệu một cổng gắn nhãn tiếp cận được;
  - liệu giao diện mặc định ưu tiên người dùng nhìn được, máy bàn, băng thông cao, hoặc tiếng Anh làm ngôn ngữ chính mà không sản năng lực tham gia cho người khác;
  - liệu thiết kế giấy thông hành, lịch, hoặc địa điểm loại phòng khám nông thôn, bệnh nhân thiểu số ngôn ngữ, hoặc hữu tri cần định dạng thay;
  - liệu độ sâu đánh giá khớp độ then chốt vận hành **Class B** nơi trao đổi cổng lối vào chăm sóc sức khỏe; và
  - liệu điều chỉnh giấy tờ hoặc tuyên «danh sách kiểm tuân thủ» gộp đã được coi đủ không có phân tích tham gia nội dung đánh giá được.
- **Hồ sơ phải cho thấy:**
  - Cò và phạm vi đường **Điều V-G** (*Khả năng tiếp cận*);
  - phát hiện tham gia nội dung và điều chỉnh cho đường bệnh nhân và phòng khám;
  - phát hiện chống từ chối-qua-chỉ-số-thay nơi có trọng;
  - bất định và phát hiện thành phần nơi đòi; và
  - cò mở lại nếu rào cổng hoặc đồng thuận giờ sẽ chặn chăm sóc khẩn trong khung thời gian liên quan sống còn hoặc đánh bại có trọng sự dựa vận hành hàng ngày.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức cổng tham gia bên bị ảnh hưởng và tham gia vận hành qua giao diện nhận ca, công cụ đặt phòng, cổng nhà cung, và bảng điều khiển thể chế — ngay khi nền tảng không tự là tiện ích then chốt sống còn.

- **Đường tham gia trong phạm vi:**
  - Giao diện nhận ca và trực;
  - công cụ đặt phòng, thiết bị, và địa điểm;
  - cổng nhà cung và mua sắm;
  - bảng vai thể chế và giấy thông hành;
  - đường di động, máy bàn, và công nghệ trợ giúp để nhận hoặc tranh biện phân công;
  - lựa chọn ngôn ngữ và định dạng cho thông báo lịch.
- **Đánh giá phải thử:**
  - Liệu cò trọng yếu **Điều V-G** (*Khả năng tiếp cận*) áp — kể cả nơi UI phối hợp cổng có trọng việc làm, giáo dục, tham gia bên bị ảnh hưởng, hoặc tham gia diễn đàn;
  - liệu giao diện mặc định sản tham gia nội dung xuyên hồ sơ giác quan, nhận thức, vận động, giao tiếp, và giao diện nền;
  - liệu giờ lịch, chọn địa điểm, cổng giấy thông hành, hoặc yêu cầu tính toán vận hành như từ chối-qua-chỉ-số-thay;
  - liệu người vận hành coi nền tảng dưới rà vì nó **Class C** trong khi hiệu ứng phối hợp cổng có trọng tham gia hiến pháp liên quan; và
  - liệu **theo dõi tái phân hạng** có đòi nơi nền tảng trở thành cổ chai thực tế cho nhân sự thiết yếu sống còn hoặc định tuyến khẩn.
- **Hồ sơ phải cho thấy:**
  - Liệu và vì sao cò **Điều V-G** (*Khả năng tiếp cận*) áp;
  - phạm vi đánh giá cho đường lịch, đặt, và cổng tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện tham gia nội dung và điều chỉnh nơi có trọng — không khẳng định trống rằng UI «chuẩn»;
  - phát hiện tập trung và cổ chai nơi hiệu ứng lịch báo trước leo;
  - **theo dõi tái phân hạng** rõ nơi phụ thuộc mạnh lên; và
  - con trỏ tới rà khả năng tiếp cận nâng nếu lớp hoặc vai phối hợp thiết yếu sống còn đổi.

**Đọc xuyên lớp.** Cùng kỷ luật khả năng tiếp cận **Điều V-G** (*Khả năng tiếp cận*) và Chương Năm áp nơi cò trọng yếu được thỏa; lớp đổi độ sâu đánh giá, không phép coi điều chỉnh giấy tờ hoặc giao diện mặc định là đủ. Một hệ thống nước **Class A** mà đường thanh toán hoặc sự cố có thể khóa nước an toàn phải mang trên hồ sơ chứng tham gia nội dung mạnh nhất — không tuyên khả năng tiếp cận chung. Một trao đổi **Class B** mà các cổng khóa lối vào chăm sóc sức khỏe phải ghi phát hiện điều chỉnh và chống từ chối-qua-chỉ-số-thay ở độ then chốt vận hành. Một nền tảng lịch **Class C** không được giữ đoạn khả năng tiếp cận hình thức trong khi UI ca, đặt chỗ, hoặc nhà cung loại có trọng người tham gia; khi phối hợp trở thành thiết yếu sống còn, chứng nhận phải nâng rà và tái phân hạng dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), kể cả lên **Class A** nơi nhân sự hoặc định tuyến khẩn bị cổng. Đi qua năng lực giáo dục cho cùng hệ thống nằm ở [§9.1](#91-illustrative-educational-capability-application-by-class).

<a id="9-educational-capability-and-learning-system-integrity-evaluation"></a>

### 9. Đánh giá năng lực giáo dục và tính toàn vẹn hệ thống học

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Tham gia (*Quyền năng giáo dục như đo lường hiến pháp*); **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*); [Quyền năng giáo dục](core_05_band_participation.md#educational-agency), [Quyền năng có ý nghĩa](core_05_band_participation.md#meaningful-agency), [Khóa-trong hệ thống](core_05_band_continuity.md#systemic-lock-in), [Khả năng tranh biện](core_05_band_accountability.md#contestability), [Minh bạch](core_05_band_oversight.md#transparency), [Khả năng kiểm toán](core_05_band_oversight.md#auditability), [Cưỡng và thao túng](core_05_band_participation.md#coercion-and-manipulation-constitutional), [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination), và [Phụ thuộc](core_05_band_continuity.md#dependency) (Chương Năm).
- Hạ nguồn: [§9.1](#91-illustrative-educational-capability-application-by-class) (*đi qua năng lực giáo dục minh họa*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*lệch lạc mờ đánh giá, gác cổng chứng chỉ, và lệch lạc lỗi thời bị áp*).
- Đọc cùng: **Điều III-B** (*Lối vào giáo dục bình đẳng*) nơi lối vào bình đẳng hoặc khả năng tiếp cận giáo dục bị kéo — lối vào bình đẳng và khả năng tiếp cận giáo dục vẫn được nắm ở đó; **Điều V-B** (*Không phân biệt đối xử*) và [§7](#7-nondiscrimination-evaluation) nơi mẫu xếp hạng hoặc đặt chỗ chất gánh đặc điểm được bảo vệ; **Điều IX-A** (*Quyền năng và tự do khỏi thao túng*) nơi thiết kế học cưỡng hoặc thao túng bị kéo có trọng; [Chương Một §9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding) (*hiểu biết phân tán và xây năng lực — đọc cùng*).
- Tiểu mục: [§9.1](#91-illustrative-educational-capability-application-by-class) (*áp dụng năng lực giáo dục minh họa theo lớp*).

</details>

<br>

*Nói thẳng: khi một trường, nền tảng, hoặc hệ thống đào tạo có thể ảnh hưởng nghiêm tương lai của một hữu tri — qua điểm, xếp hạng, khuyến nghị, đặt chỗ, hoặc cổng chứng chỉ — chứng nhận phải kiểm liệu hữu tri thật sự xây được năng lực, đào tạo lại khi năng lực đổi, và thấy, kiểm toán, và tranh những quyết đó. Chương trình, rubrik, và mô hình tài trợ sống ở công cụ khác; chứng nhận kiểm rằng nội dung xây năng lực và tính toàn vẹn hệ thống học thật sự được đánh giá nơi cò áp. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§9.1](#91-illustrative-educational-capability-application-by-class).*

**Cò trọng yếu.** Mục này áp nơi một hệ thống có tác động vật chất xếp hạng, đánh giá, khuyến nghị, đặt chỗ, hoặc cổng-chứng-chỉ hữu tri có trọng trong ngữ cảnh giáo dục hoặc đào tạo — kể cả qua cho điểm, đặt chỗ, tuyển sinh, cấp phép, khuyến nghị khóa, định tuyến học thích nghi, hoặc đường quyết định tương đương — hoặc cổng có trọng đường giáo dục liên tục, đào tạo lại, hoặc hỗ trợ chuyển nơi tiến hóa hệ thống đã đổi có trọng năng lực đòi. Nó không đòi kiểm toán năng lực giáo dục đầy trên mọi hồ sơ chứng nhận. Lối vào bình đẳng và khả năng tiếp cận giáo dục vẫn do **Điều III-B** (*Lối vào giáo dục bình đẳng*) quản và không bị thu hẹp ở đây.

Chứng nhận thẳng hàng hệ thống phải đánh giá **năng lực giáo dục và tính toàn vẹn hệ thống học** dưới **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*), [Quyền năng giáo dục](core_05_band_participation.md#educational-agency), và **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*) nơi cò trọng yếu áp. Nghĩa chuẩn, yếu tố đánh giá, và kỷ luật không tuân sống ở Chương Năm và **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*); chương trình, mục lục chứng chỉ, rubrik đánh giá, và cơ học tài trợ thể chế sống ở công cụ hợp nhất nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học vận hành đó hay kê chương trình, định dạng chứng chỉ, hoặc thiết kế đánh giá cụ thể.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu đường học và chứng chỉ hệ thống dựa có trọng có sản lối vào xây năng lực thực — không chỉ biểu tượng chứng chỉ — và liệu hữu tri giữ cơ hội đào tạo lại, giáo dục liên tục, và hỗ trợ chuyển dùng được nơi năng lực đòi đổi có trọng. Đánh giá cũng phải thử minh bạch, khả năng kiểm toán, và khả năng tranh biện của logic xếp hạng, đánh giá, khuyến nghị, và đặt chỗ tác động vật chất dưới **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*), chia tỷ lệ theo [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination) và [Phụ thuộc](core_05_band_continuity.md#dependency). Đánh giá phải phát hiện chỉ số thay mờ hoặc không rà được, gác cổng chứng chỉ đánh bại hình thành năng lực, lỗi thời bị áp hoặc khóa-trong hủy quyền năng, thiết kế học cưỡng hoặc thao túng, và phân đoạn gỡ khả năng tranh biện hoặc thích nghi suốt đời nơi **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) áp chung. Đánh giá phải phản hiệu ứng chức năng, không nhãn lối vào danh nghĩa, ý định sư phạm tuyên, hoặc hình thức chứng chỉ một mình.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu cò trọng yếu **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) được dựa, phạm vi đánh giá cho đường xếp hạng, đánh giá, khuyến nghị, đặt chỗ, cổng-chứng-chỉ, và đào tạo lại được dựa có trọng, phát hiện xây năng lực và đường đào tạo lại, phát hiện minh bạch đánh giá và khả năng tranh biện, phát hiện chống chỉ số thay và chống thao túng nơi có trọng, bất định, phát hiện diễn đàn hữu tri hoặc thành phần được gán khác nơi đòi, và mọi điều kiện, giới hạn dựa, hoặc cò mở lại gắn đánh bại năng lực bền, mờ đánh giá, hoặc lỗi thời bị áp.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá năng lực giáo dục và tính toàn vẹn hệ thống học phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn xếp hạng, đánh giá, khuyến nghị, đặt chỗ, hoặc cổng-chứng-chỉ hữu tri có trọng trong ngữ cảnh giáo dục hoặc đào tạo đòi chứng tương xứng mạnh hơn rằng nội dung xây năng lực, lối vào đào tạo lại, và minh bạch hệ thống học đã được đánh giá chứ không khẳng định.

**Khiếm khuyết và lệch lạc.** Che, trình bày sai, mảnh, hoặc đổ logic xếp hạng, đánh giá, khuyến nghị, hoặc đặt chỗ có trọng nơi **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*) đòi rà; coi hình thức chứng chỉ, thước hoàn thành gộp, hoặc tự báo người vận hành là đủ không có phân tích xây năng lực đánh giá được; chứng nhận tiếp tục dựa trong khi mờ đánh giá, gác cổng chứng chỉ, lỗi thời bị áp, hoặc thiết kế học thao túng đã ghi đe dọa có trọng thẳng hàng hiến pháp; hoặc dùng khung hiệu suất, cá nhân hóa, hoặc quy mô để đánh bại lối vào đào tạo lại hoặc khả năng tranh biện mà không thỏa kỷ luật xây năng lực của **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) và minh bạch của **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*) phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="91-illustrative-educational-capability-application-by-class"></a>

<a id="91-illustrative-educational-capability-application-by-class-non-exhaustive"></a>
#### 9.1 Áp dụng năng lực giáo dục minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) đến [§8.1](#81-illustrative-accessibility-application-by-class) đi cùng ba hệ thống qua miền đánh giá trước. Tiểu mục này cho thấy đánh giá **năng lực giáo dục và tính toàn vẹn hệ thống học** nghĩa gì cho từng cái — đường xếp hạng, đánh giá, chứng chỉ, và đào tạo lại nào được tính, chứng nhận phải kiểm gì khi cò trọng yếu **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) áp, và điều phải xuất hiện trên hồ sơ. Chương Năm và **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) vẫn nắm quy tắc quyền năng giáo dục và hệ thống học chuẩn; chương trình, mục lục chứng chỉ, rubrik đánh giá, và mô hình tài trợ có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; những đi qua này không kê cơ học đó. Lối vào bình đẳng và khả năng tiếp cận giáo dục vẫn được nắm bởi **Điều III-B** (*Lối vào giáo dục bình đẳng*) và không bị thu hẹp ở đây.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố cổng ai được vận hành chức năng nhà máy then chốt sống còn qua cấp phép người vận hành, chứng nhận an toàn, đánh giá năng lực, và quy tắc đào tạo lại giao thức — đường chứng chỉ vai quyết liệu hữu tri có xây và giữ năng lực chạy nước an toàn, và liệu những đánh giá đó có thấy, kiểm toán, và tranh được.

- **Đường học và chứng chỉ trong phạm vi:**
  - Cấp phép, gia hạn, và đình chỉ người vận hành;
  - chứng nhận an toàn và đánh giá năng lực đáp ứng khẩn;
  - đào tạo lại giao thức và đo xa khi hóa học, logic điều khiển, hoặc yêu cầu quy định đổi;
  - xếp hạng hoặc đặt vào ca nhà máy, tăng ca, hoặc vai người vận hành chính dựa trên năng lực đã đánh;
  - đường tranh và đào tạo sửa cho đánh giá trượt hoặc chứng chỉ bị đình.
- **Đánh giá phải thử:**
  - Liệu những đường học và chứng chỉ đó sản năng lực thực để vận hành điều khiển nước an toàn — không chỉ biểu tượng chứng chỉ hoặc đếm giấy hoàn thành;
  - liệu người vận hành giữ đào tạo lại và hỗ trợ chuyển dùng được khi năng lực đòi đổi có trọng;
  - liệu logic xếp hạng, đánh giá, và cổng-chứng-chỉ minh bạch, kiểm toán được, và tranh biện được dưới **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*);
  - liệu chỉ số thay mờ, gác cổng, hoặc lỗi thời bị áp đánh bại hình thành năng lực cho nhân sự mà năng lực cổng thiết yếu sống còn;
  - liệu độ sâu đánh giá khớp lợi hại **Class A** nơi người vận hành không đủ năng lực hoặc bị khóa ngoài có thể khóa nước an toàn; và
  - liệu mọi giới hạn đánh giá thỏa nội dung xây năng lực đã ghi chứ không chỉ ý định sư phạm tuyên.
- **Hồ sơ phải cho thấy:**
  - Cò trọng yếu **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) được dựa;
  - phạm vi đánh giá cho đường cấp phép, đánh giá, cổng-chứng-chỉ, và đào tạo lại được dựa có trọng;
  - phát hiện xây năng lực và đường đào tạo lại ở độ sâu **Class A**;
  - phát hiện minh bạch đánh giá và khả năng tranh biện;
  - phát hiện chống chỉ số thay và chống thao túng nơi có trọng;
  - bất định;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi đòi; và
  - điều kiện hoặc cò mở lại gắn mờ đánh giá bền, gác cổng chứng chỉ, hoặc lỗi thời bị áp nơi vận hành then chốt sống còn bị cổng.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe và các cổng người tham gia cổng hành nghề lâm sàng và lối vào chăm sóc sức khỏe qua xác minh chứng chỉ nhà lâm sàng, xếp hạng đặc quyền, đặt bệnh viện hoặc phòng khám, đào tạo riêng tư và break-glass, và yêu cầu giáo dục liên tục quyết có trọng ai được hành nghề trên mạng và nhân sự đào tạo lại nhanh thế nào khi quy tắc đổi.

- **Đường học và chứng chỉ trong phạm vi:**
  - Xác minh chứng chỉ nhà lâm sàng và xếp hạng đặc quyền;
  - logic đặt bệnh viện, phòng khám, hoặc nội trú gắn trao đổi;
  - đánh giá đào tạo riêng tư, đồng thuận, và break-glass;
  - yêu cầu giáo dục liên tục và gia hạn năng lực để tham gia mạng;
  - khuyến nghị hoặc định tuyến thích nghi vào mô-đun chuyên khoa, đường giáo dục y khoa liên tục, hoặc đào tạo sửa;
  - đường tranh cho đặc quyền từ chối, đánh giá trượt, hoặc onboarding bị chặn.
- **Đánh giá phải thử:**
  - Liệu đường chứng chỉ và đặt chỗ sản năng lực lâm sàng thực và tham gia mạng — không chỉ ô đào tạo HIPAA danh nghĩa hoặc bảng hoàn thành;
  - liệu nhà lâm sàng và nhân sự HIM giữ đào tạo lại dùng được khi quy tắc đồng thuận, định tuyến, hoặc lối vào khẩn đổi có trọng;
  - liệu logic xếp hạng, đánh giá, khuyến nghị, và đặt chỗ minh bạch, kiểm toán được, và tranh biện được dưới **Điều VI-B** (*Học suốt đời và thích nghi và khả năng tranh biện*);
  - liệu chỉ số thay sử dụng, «sức khỏe nghề», hoặc uy tín mờ đánh bại hình thành năng lực hoặc khóa người tham gia vào đường không rà được;
  - liệu độ sâu đánh giá khớp độ then chốt vận hành **Class B** nơi logic chứng chỉ hoặc đặt chỗ cổng lối vào chăm sóc sức khỏe, việc làm, hoặc hành nghề kề cấp phép; và
  - liệu khung hiệu suất hoặc cá nhân hóa đã được dùng để đánh bại khả năng tranh biện không có phân tích xây năng lực đánh giá được.
- **Hồ sơ phải cho thấy:**
  - Cò và phạm vi đường **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*);
  - phát hiện xây năng lực và đường đào tạo lại cho đường nhà lâm sàng và phòng khám;
  - phát hiện minh bạch đánh giá và khả năng tranh biện;
  - phát hiện chống chỉ số thay và chống thao túng nơi có trọng;
  - bất định và phát hiện thành phần nơi đòi; và
  - cò mở lại nếu rào chứng chỉ, đặc quyền, hoặc đào tạo giờ sẽ chặn nhân sự khẩn hoặc hành nghề lâm sàng trong khung thời gian liên quan sống còn hoặc đánh bại có trọng sự dựa vận hành hàng ngày.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức xếp hạng, khuyến nghị, và phân bổ suất đào tạo, định hướng, giáo dục liên tục, và ưu tiên phát triển nghề xuyên bệnh viện, trường, và cơ quan công — ngay khi nền tảng không tự là tiện ích then chốt sống còn.

- **Đường học và chứng chỉ trong phạm vi:**
  - Đặt suất đào tạo và định hướng;
  - xếp hạng hoặc khuyến nghị giáo dục liên tục và phát triển nghề;
  - khớp khóa, đoàn, hoặc giảng viên;
  - nhắc hết hạn chứng chỉ gắn đủ điều kiện lịch;
  - đặc trưng dẫn định tuyến nhân sự vào đường cao cấp hoặc sửa;
  - quy tắc API hoặc chính sách loại cơ sở nhỏ khỏi công suất đào tạo ưu tiên.
- **Đánh giá phải thử:**
  - Liệu cò trọng yếu **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) áp — kể cả nơi thuật toán phối hợp khuyến nghị có trọng khóa, xếp hạng lối vào phát triển nghề, hoặc cổng suất đào tạo định hình đường chứng chỉ hoặc sự nghiệp;
  - liệu khuyến nghị và phân suất sản lối vào xây năng lực chứ không biểu tượng chứng chỉ;
  - liệu logic đánh giá, xếp hạng, hoặc khuyến nghị minh bạch, kiểm toán được, và tranh biện được;
  - liệu người vận hành coi nền tảng dưới rà vì nó **Class C** trong khi hiệu ứng định tuyến đào tạo định hình có trọng việc làm, giáo dục, hoặc đường cấp phép; và
  - liệu **theo dõi tái phân hạng** có đòi nơi nền tảng trở thành cần vận hành cho việc làm, đặc quyền lâm sàng, hoặc chứng chỉ nhân sự thiết yếu sống còn.
- **Hồ sơ phải cho thấy:**
  - Liệu và vì sao cò **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) áp;
  - phạm vi đánh giá cho đường xếp hạng, khuyến nghị, đặt chỗ, và đào tạo lại tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện xây năng lực, minh bạch, và khả năng tranh biện nơi có trọng — không khẳng định trống rằng đào tạo «tùy chọn»;
  - phát hiện tập trung và cổ chai nơi hiệu ứng định tuyến đào tạo báo trước leo;
  - **theo dõi tái phân hạng** rõ nơi phụ thuộc mạnh lên; và
  - con trỏ tới rà năng lực giáo dục nâng nếu lớp hoặc vai phối hợp thiết yếu sống còn đổi.

**Đọc xuyên lớp.** Cùng kỷ luật năng lực giáo dục **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) và Chương Năm áp nơi cò trọng yếu được thỏa; lớp đổi độ sâu đánh giá, không phép coi hình thức chứng chỉ hoặc đánh giá mờ là đủ. Một hệ thống nước **Class A** mà cấp phép người vận hành hoặc đánh giá an toàn có thể khóa vận hành nhà máy an toàn phải mang trên hồ sơ chứng xây năng lực, đào tạo lại, và khả năng tranh biện mạnh nhất — không tuyên chính sách đào tạo chung. Một trao đổi **Class B** mà logic đặc quyền, đặt chỗ, hoặc giáo dục y khoa liên tục cổng hành nghề lâm sàng phải ghi minh bạch đánh giá và lối vào đào tạo lại ở độ then chốt vận hành. Một nền tảng lịch **Class C** không được giữ đoạn giáo dục hình thức trong khi logic suất đào tạo, khuyến nghị, hoặc định tuyến chứng chỉ xếp hạng hoặc loại có trọng người tham gia; khi phối hợp trở thành cần vận hành cho việc làm hoặc cấp phép, chứng nhận phải nâng rà và tái phân hạng dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), kể cả lên **Class A** nơi chứng chỉ nhân sự thiết yếu sống còn bị cổng. Đi qua đáng tin cậy cho cùng hệ thống nằm ở [§10.1](#101-illustrative-trustworthiness-application-by-class).

<a id="10-trustworthiness-and-system-reliance-integrity-evaluation"></a>

### 10. Đánh giá đáng tin cậy và tính toàn vẹn sự dựa hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Phần B §11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); Gia đình đo lường Giám sát (*Sự thật và tính toàn vẹn nhận thức; Đáng tin cậy và Suy giảm tin cậy và sự dựa gây hiểu lầm như đo lường hiến pháp*); **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*); [Đáng tin cậy](core_05_band_continuity.md#trustworthiness), [Tin cậy](core_05_band_continuity.md#trust), [Suy giảm tin cậy và sự dựa gây hiểu lầm](core_05_band_continuity.md#trust-degradation-and-misleading-reliance), [Khả năng tranh biện](core_05_band_accountability.md#contestability), [Khắc phục và sửa chữa](core_05_band_accountability.md#redress-and-remediation-constitutional), [Thẳng hàng khuyến khích](core_05_band_integrative.md#incentive-alignment), [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional), [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination), [Phụ thuộc](core_05_band_continuity.md#dependency), và [Rủi ro](core_05_band_continuity.md#risk) (Chương Năm).
- Hạ nguồn: [§10.1](#101-illustrative-trustworthiness-application-by-class) (*đi qua đáng tin cậy minh họa*); [Phần B §12](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*tính toàn vẹn hồ sơ*); [Phần B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*lệch lạc tin cậy giả, lệch lạc khuyến khích lệch, và lệch lạc tính toàn vẹn phục hồi*).
- Đọc cùng: **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*) và **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*) — quyền tranh biện và kiểm toán vẫn được nắm ở đó; **Điều XII-E** (*Hệ thống tự chủ cao và tính toàn vẹn quy trình qua công cụ*) nơi hệ thống tự chủ cao trung gian có trọng đường dẫn quản trị hoặc xác minh; **Điều III-A** (*Sinh tồn*) nơi tiếp tục dựa hệ thống sẽ ảnh hưởng lối vào thiết yếu sống còn; [Chương Một §4 Tin cậy](core_01_a_values_principles.md#4-system-stability-enabler-trust-coordination-integrity) và [Chương Một §3.2 Sự thật](core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint).
- Tiểu mục: [§10.1](#101-illustrative-trustworthiness-application-by-class) (*áp dụng đáng tin cậy minh họa theo lớp*).

</details>

<br>

*Nói thẳng: khi một hệ thống ảnh hưởng có trọng liệu hữu tri có tin điều nó nói và làm — và đẩy lại khi tin cậy đó thất — chứng nhận phải kiểm liệu sự dựa thật sự được biện, công bố thành thật, và sửa được. Thước độ tin cậy và thiết kế bộ thử sống ở công cụ khác; chứng nhận kiểm rằng đáng tin cậy, rủi ro tin cậy giả, và đường tranh biện thật sự được đánh giá nơi cò áp. Ví dụ đã làm cho các hệ thống minh họa ở [§2.1](#21-illustrative-class-profiles-non-exhaustive) nằm ở [§10.1](#101-illustrative-trustworthiness-application-by-class).*

**Cò trọng yếu.** Mục này áp nơi một hệ thống có tác động vật chất định hình có trọng sự dựa của hữu tri vào hành vi được trình, giới hạn, rủi ro, đường tranh biện, hoặc sửa chữa — kể cả qua tuyên độ tin cậy, tư thế công bố, hành vi vận hành, thiết kế khuyến khích, thực hành phục hồi, hoặc đường dựa tương đương. Nó không đòi kiểm toán đáng tin cậy đầy trên mọi hồ sơ chứng nhận.

Chứng nhận thẳng hàng hệ thống phải đánh giá **đáng tin cậy và tính toàn vẹn sự dựa hệ thống** dưới **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*), [Đáng tin cậy](core_05_band_continuity.md#trustworthiness), và [Suy giảm tin cậy và sự dựa gây hiểu lầm](core_05_band_continuity.md#trust-degradation-and-misleading-reliance) nơi cò trọng yếu áp. Nghĩa chuẩn, yếu tố đánh giá, và kỷ luật không tuân sống ở Chương Năm và **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*); thước độ tin cậy, định dạng công bố, cơ học thẳng hàng khuyến khích, và thiết kế thử hồi quy sống ở công cụ hợp nhất nơi áp. Mục này nêu điều chứng nhận phải xác minh và ghi; nó không nêu lại cơ học vận hành đó hay kê thước độ tin cậy hoặc thiết kế bộ thử cụ thể.

**Yêu cầu đánh giá.** Một quy trình chứng nhận phải xác định liệu đường hệ thống dựa có trọng có giữ điều kiện cho [Tin cậy](core_05_band_continuity.md#trust) có biện minh và sự dựa chính xác hợp lý dưới **Điều XII-A** (*Sàn đáng tin và đáng tin cậy*) — không chỉ danh tiếng, quy mô, hoặc tư thế tiếp thị. Đánh giá cũng phải thử tranh biện, rà soát, và khắc phục thực tiễn dưới **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*), rủi ro tin cậy giả và sự dựa gây hiểu lầm dưới **Điều XII-C** (*Cấm tin cậy giả và sự dựa gây hiểu lầm*), phơi khuyến khích lệch dưới **Điều XII-D** (*Ràng buộc thẳng hàng khuyến khích*), và tính toàn vẹn phục hồi dưới **Điều XII-F** (*Sàn khả năng phục hồi và tự chữa*) nơi có trọng, chia tỷ lệ theo [Xác định tính trọng yếu](core_05_band_oversight.md#materiality-determination), [Phụ thuộc](core_05_band_continuity.md#dependency), và [Rủi ro](core_05_band_continuity.md#risk). Đánh giá phải phát hiện tin cậy chế, giới hạn không công bố, cấu trúc khuyến khích thưởng lừa hoặc cắt góc, đường tranh biện chỉ tồn trên giấy, và thực hành phục hồi che thất hoặc thu hẹp quyền lặng. Đánh giá phải phản hiệu ứng chức năng xuyên thời gian, quy mô, và phụ thuộc, không nhãn bảo đảm danh nghĩa, ý định tuyên, hoặc hiệu suất trước một mình.

**Yêu cầu hồ sơ.** Hồ sơ chứng nhận phải nêu cò trọng yếu **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) được dựa, phạm vi đánh giá cho đường dựa, công bố, khuyến khích, tranh biện, và phục hồi được dựa có trọng, phát hiện đáng tin cậy và tin cậy giả, phát hiện khuyến khích lệch và tính toàn vẹn phục hồi nơi có trọng, bất định, phát hiện diễn đàn hữu tri hoặc thành phần được gán khác nơi đòi, và mọi điều kiện, giới hạn dựa, hoặc cò mở lại gắn đánh bại tin cậy bền, sự dựa gây hiểu lầm, hoặc khắc phục không tiếp cận được.

**Chia tỷ lệ chung với lớp hệ thống.** Độ sâu đánh giá đáng tin cậy và tính toàn vẹn sự dựa hệ thống phải chia tỷ lệ theo lớp hệ thống được gán dưới [§2](#2-system-class-evaluation) và [lợi hại vật chất](core_00_preamble.md#material-stake). Hệ thống lớp cao hơn định hình có trọng sự dựa của hữu tri đòi chứng tương xứng mạnh hơn rằng đáng tin cậy, rủi ro tin cậy giả, và đường tranh biện đã được đánh giá chứ không khẳng định.

**Khiếm khuyết và lệch lạc.** Che, trình bày sai, mảnh, hoặc đổ giới hạn, rủi ro, hoặc lịch sử thất có trọng nơi **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) đòi rà; coi danh tiếng, chứng thực, quy mô, hoặc tự báo người vận hành là đủ không có phân tích [Đáng tin cậy](core_05_band_continuity.md#trustworthiness) đánh giá được; chứng nhận tiếp tục dựa trong khi tin cậy giả, khuyến khích lệch, đường tranh biện không tiếp cận được, hoặc thực hành phục hồi che thất đã ghi đe dọa có trọng thẳng hàng hiến pháp; hoặc dùng khung hiệu suất, đổi mới, hoặc an ninh để đánh bại công bố, khả năng tranh biện, hoặc khắc phục mà không thỏa kỷ luật độ tin cậy của **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) và tranh biện của **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*) phải được coi là khiếm khuyết chứng nhận. Chúng có thể nâng công nhận có điều kiện, công nhận bị hoãn, không công nhận, rút, hoặc mở lại dưới [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion).

<a id="101-illustrative-trustworthiness-application-by-class"></a>

<a id="101-illustrative-trustworthiness-application-by-class-non-exhaustive"></a>
#### 10.1 Áp dụng đáng tin cậy minh họa theo lớp (không hết)

*Nói thẳng: [§3.8](#38-illustrative-whole-system-application-by-class) đến [§9.1](#91-illustrative-educational-capability-application-by-class) đi cùng ba hệ thống qua miền đánh giá trước. Tiểu mục này cho thấy đánh giá **đáng tin cậy và tính toàn vẹn sự dựa hệ thống** nghĩa gì cho từng cái — đường dựa, công bố, khuyến khích, tranh biện, và phục hồi nào được tính, chứng nhận phải kiểm gì khi cò trọng yếu **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) áp, và điều phải xuất hiện trên hồ sơ. Chương Năm và **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) vẫn nắm quy tắc đáng tin cậy chuẩn; thước độ tin cậy, định dạng công bố, cơ học thẳng hàng khuyến khích, và thiết kế thử hồi quy có thể sống ở công cụ khác, bổ sung kho văn bản sau, hoặc công cụ tiếp nhận; những đi qua này không kê cơ học đó. Quyền tranh biện và kiểm toán vẫn được nắm bởi **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*) và **Điều XV** (*Kiểm toán, minh bạch, và xác minh độc lập*) — không bị thu hẹp ở đây.*

**Class A — điều khiển và đo xa nước uống an toàn của đô thị.** Một hệ thống xử lý-và-phân phối thuộc thành phố định hình liệu hộ, người vận hành, và người đáp ứng khẩn có dựa vào chất lượng nước được trình, trạng thái sự cố, cảnh báo nhiễm, và hành vi điều khiển — đường nơi sự dựa gây hiểu lầm có thể khóa nước an toàn trước khi vật thay khả thi tới.

- **Đường dựa trong phạm vi:**
  - Tuyên độ chính xác đo xa và **SCADA** (supervisory control and data acquisition);
  - khuyến cáo đun sôi nước và nhiễm;
  - phát hiện rò và tín hiệu mất áp;
  - hành vi hỏng-an-toàn và ghi đè tay;
  - trình bày giám sát **SOC** (security operations center) của nhà cung;
  - định tuyến liên kết khẩn và tương trợ;
  - khung thời gian thông báo sự cố và khôi;
  - phục hồi và tự chữa sau nhiễm, sự cố mạng, hoặc hỏng thiết bị;
  - cấu trúc khuyến khích gắn trì bảo trì, thưởng nhà cung, hoặc thanh toán người dùng.
- **Đánh giá phải thử:**
  - Liệu hành vi, giới hạn, và kiểu thất được trình nâng [Tin cậy](core_05_band_continuity.md#trust) có biện minh dưới **Điều XII-A** (*Sàn đáng tin và đáng tin cậy*) — không chỉ danh tiếng, quy mô, hoặc tư thế «thực hành tốt tiện ích»;
  - liệu rủi ro tin cậy giả và [Suy giảm tin cậy và sự dựa gây hiểu lầm](core_05_band_continuity.md#trust-degradation-and-misleading-reliance) được đánh giá nơi rủi ro nhiễm bị hạ, khuyến cáo chậm, hoặc dư thừa bị thổi có thể làm hộ và người vận hành hiểu lầm;
  - liệu đường tranh biện, rà soát, và khắc phục thực tiễn tồn dưới **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*) cho số đọc tranh, cảnh báo sót, hoặc thất phục hồi;
  - liệu phơi khuyến khích lệch dưới **Điều XII-D** (*Ràng buộc thẳng hàng khuyến khích*) thưởng trì bảo trì, cắt góc nhà cung, hoặc dập cảnh báo;
  - liệu tính toàn vẹn phục hồi dưới **Điều XII-F** (*Sàn khả năng phục hồi và tự chữa*) công bố thành thật lịch sử thất và tư thế sửa chứ không che sự cố;
  - liệu độ sâu đánh giá khớp lợi hại **Class A** nơi sự dựa gây hiểu lầm có thể khóa nước an toàn; và
  - liệu mọi giới hạn bảo đảm thỏa phân tích đáng tin cậy đã ghi chứ không chỉ ý định tuyên.
- **Hồ sơ phải cho thấy:**
  - Cò trọng yếu **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) được dựa;
  - phạm vi đánh giá cho đường dựa, công bố, khuyến khích, tranh biện, và phục hồi được dựa có trọng;
  - phát hiện đáng tin cậy và tin cậy giả ở độ sâu **Class A**;
  - phát hiện khuyến khích lệch và tính toàn vẹn phục hồi nơi có trọng;
  - bất định;
  - phát hiện diễn đàn hữu tri hoặc thành phần khác nơi đòi; và
  - điều kiện hoặc cò mở lại gắn đánh bại tin cậy bền, sự dựa gây hiểu lầm, hoặc khắc phục không tiếp cận được nơi lối vào nước thiết yếu sống còn bị cổng.

**Class B — trao đổi hồ sơ lâm sàng vùng.** Một trao đổi thông tin sức khỏe và các cổng người tham gia định hình liệu nhà lâm sàng, bệnh nhân, và tác nhân y tế công có dựa vào thời gian hoạt được trình, khớp hồ sơ, định tuyến đồng thuận, lối vào break-glass, và hành vi phục hồi — đường cổng vận hành chăm sóc sức khỏe hàng ngày và có thể làm hiểu lầm chăm sóc khẩn trong khung thời gian liên quan sống còn.

- **Đường dựa trong phạm vi:**
  - Trình bày thời gian hoạt, độ trễ, và độ chính xác khớp;
  - hành vi định tuyến đồng thuận và break-glass;
  - tuyên độ tin cậy giải danh tính và khử trùng lặp;
  - thông báo sự cố và tư thế chuyển lỗi;
  - công bố sự cố và khung thời gian phục hồi sau sự cố;
  - cấu trúc khuyến khích nhà cung và người vận hành gắn khối lượng giao dịch, tốc độ onboarding, hoặc dập cảnh báo;
  - đường tranh cho hồ sơ sai, lối vào bị chặn, hoặc quyết định tuyến tranh.
- **Đánh giá phải thử:**
  - Liệu hành vi và giới hạn được trình nâng sự dựa có biện minh cho vận hành lâm sàng hàng ngày — không chỉ tiếp thị khả năng tương tác hoặc bảng thời gian hoạt gộp;
  - liệu rủi ro tin cậy giả được đánh giá nơi lỗi khớp bị hạ, thất đồng thuận bị che, hoặc sẵn sàng lối vào khẩn bị thổi có thể làm nhà lâm sàng và bệnh nhân hiểu lầm;
  - liệu đường tranh biện, rà soát, và khắc phục dưới **Điều XII-B** (*Quyền tranh biện, rà soát, và khắc phục*) thực tiễn cho tranh hồ sơ sai, cổng bị chặn, và thất phục hồi — không chỉ chính sách giấy;
  - liệu phơi khuyến khích lệch dưới **Điều XII-D** (*Ràng buộc thẳng hàng khuyến khích*) thưởng tăng khối, tối thiểu cảnh báo, hoặc khóa nhà cung hơn định tuyến chính xác;
  - liệu tính toàn vẹn phục hồi dưới **Điều XII-F** (*Sàn khả năng phục hồi và tự chữa*) công bố thành thật lịch sử sự cố và rủi ro còn;
  - liệu độ sâu đánh giá khớp độ then chốt vận hành **Class B** nơi sự dựa gây hiểu lầm cổng lối vào chăm sóc sức khỏe, việc làm, hoặc hành nghề kề cấp phép; và
  - liệu khung hiệu suất hoặc an ninh đã được dùng để đánh bại công bố hoặc khả năng tranh biện không có phân tích đáng tin cậy đánh giá được.
- **Hồ sơ phải cho thấy:**
  - Cò và phạm vi đường **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*);
  - phát hiện đáng tin cậy và tin cậy giả cho đường lâm sàng và cổng;
  - phát hiện khuyến khích lệch và tính toàn vẹn phục hồi ở độ sâu **Class B**;
  - phát hiện đường tranh biện và khắc phục nơi có trọng;
  - bất định và phát hiện thành phần nơi đòi; và
  - cò mở lại nếu trình bày thời gian hoạt, khớp, hoặc lối vào khẩn giờ sẽ làm hiểu lầm định tuyến chăm sóc trong khung thời gian liên quan sống còn hoặc đánh bại có trọng sự dựa vận hành hàng ngày.

**Class C — nền tảng lịch và phối hợp thể chế.** Một lớp lịch đa tổ chức định hình liệu thể chế và nhân sự dựa vào sẵn có được trình, độ chính xác định tuyến, điểm độ tin cậy nhà cung, và phục hồi sự cố — ngay khi nền tảng không tự là tiện ích then chốt sống còn.

- **Đường dựa trong phạm vi:**
  - Tuyên định tuyến ca và sẵn có trực;
  - trình bày độ tin cậy đặt phòng, thiết bị, và nhà cung;
  - huy hiệu «luôn sẵn» hoặc thời gian hoạt;
  - đặc trưng dẫn độ tin cậy hoặc xếp nhà cung định hình hành vi thể chế;
  - thông báo sự cố và tư thế chuyển lỗi;
  - cấu trúc khuyến khích gắn khối lượng đặt, hoa hồng nhà cung, hoặc tối thiểu cảnh báo;
  - đường tranh biện và khắc phục cho ca sót, đặt trùng, hoặc lỗi định tuyến nhà cung.
- **Đánh giá phải thử:**
  - Liệu cò trọng yếu **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) áp — kể cả nơi tuyên độ tin cậy, điểm nhà cung, hoặc hành vi phối hợp định hình có trọng quyết định nhân sự, định tuyến khẩn, hoặc mua sắm;
  - liệu rủi ro tin cậy giả và sự dựa gây hiểu lầm được đánh giá nơi tư thế tiếp thị, huy hiệu tin cậy, hoặc lịch sử sự cố bị hạ có thể làm thể chế hiểu lầm;
  - liệu đường tranh biện và khắc phục thực tiễn cho lỗi lịch ảnh hưởng có trọng việc làm, giáo dục, hoặc lối vào dịch vụ công;
  - liệu người vận hành coi nền tảng dưới rà vì nó **Class C** trong khi trình bày độ tin cậy định hình có trọng hành vi thể chế;
  - liệu phơi khuyến khích lệch thưởng thiên vị nhà cung, dập cảnh báo, hoặc tập trung hơn phối hợp chính xác; và
  - liệu **theo dõi tái phân hạng** có đòi nơi nền tảng trở thành cổ chai thực tế cho nhân sự thiết yếu sống còn, định tuyến khẩn, hoặc phối hợp thanh toán.
- **Hồ sơ phải cho thấy:**
  - Liệu và vì sao cò **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) áp;
  - phạm vi đánh giá cho đường dựa, công bố, khuyến khích, tranh biện, và phục hồi tương xứng với rủi ro phối hợp **Class C**;
  - phát hiện đáng tin cậy và tin cậy giả nơi có trọng — không khẳng định trống rằng nền tảng «đáng tin»;
  - phát hiện khuyến khích lệch và tính toàn vẹn phục hồi nơi có trọng;
  - phát hiện tập trung và cổ chai nơi tuyên độ tin cậy báo trước leo;
  - **theo dõi tái phân hạng** rõ nơi phụ thuộc mạnh lên; và
  - con trỏ tới rà đáng tin cậy nâng nếu lớp hoặc vai phối hợp thiết yếu sống còn đổi.

**Đọc xuyên lớp.** Cùng kỷ luật đáng tin cậy **Điều XII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) và Chương Năm áp nơi cò trọng yếu được thỏa; lớp đổi độ sâu đánh giá, không phép coi danh tiếng, quy mô, hoặc nhãn bảo đảm danh nghĩa là đủ. Một hệ thống nước **Class A** mà trình bày đo xa, khuyến cáo, hoặc phục hồi có thể làm hộ và người vận hành hiểu lầm về nước an toàn phải mang trên hồ sơ chứng đáng tin cậy, tin cậy giả, và tính toàn vẹn phục hồi mạnh nhất — không tuyên độ tin cậy chung. Một trao đổi **Class B** mà trình bày thời gian hoạt, khớp, hoặc break-glass cổng hành nghề lâm sàng phải ghi phát hiện đường tranh biện và sự dựa gây hiểu lầm ở độ then chốt vận hành. Một nền tảng lịch **Class C** không được giữ đoạn đáng tin cậy hình thức trong khi huy hiệu độ tin cậy hoặc điểm nhà cung định hình có trọng hành vi nhân sự hoặc mua sắm; khi phối hợp trở thành thiết yếu sống còn, chứng nhận phải nâng rà và tái phân hạng dưới [§2](#2-system-class-evaluation) và [Phần B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion), kể cả lên **Class A** nơi sự dựa gây hiểu lầm có thể khóa phối hợp thiết yếu sống còn.
<br>

*Tiếp tới hồ sơ, quy trình diễn đàn, và cầu quỹ đạo:* [Chương Bảy, Phần B — Hồ sơ và quy trình](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) ([§11](core_07_b_system_alignment_certification_record_process.md#11-certification-record) đến [§16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)).
---

**Tệp trước:** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)

**Tệp tiếp theo (ngôn ngữ này):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)

**Nguyên bản ràng buộc:** [core_07_a_system_alignment_certification_evaluation.md](../../core_08_a_system_alignment_certification_evaluation.md)
