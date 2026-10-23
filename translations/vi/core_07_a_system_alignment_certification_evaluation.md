<a id="chapter-seven-system-alignment-certification"></a>
<a id="chapter-seven-system-alignment-certification-and-recognition"></a>
<a id="chapter-seven-part-a-certification-evaluation"></a>
<a id="chapter-seven-part-a-system-alignment-certification--evaluation"></a>
<a id="chapter-nine-part-a-certification-evaluation"></a>

# CHƯƠNG BẢY, PHẦN A: CHỨNG NHẬN THẲNG HÀNG HỆ THỐNG — ĐÁNH GIÁ

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Bảy, Phần A tiếng Anh](../../core_09_a_system_alignment_certification_evaluation.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_07_a_system_alignment_certification_evaluation.md`](../../core_09_a_system_alignment_certification_evaluation.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> Nó chứa **Chương Bảy, Phần A** — yêu cầu **đánh giá** chứng nhận (lớp hệ thống, yếu tố toàn hệ thống, và móc đánh giá lĩnh vực). **Phần B** — hồ sơ chứng nhận, quy trình diễn đàn, cầu quỹ đạo, và mở lại — nằm ở [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md).
>
> - **Chủ sở hữu hiến pháp (chung với Phần B):** **chứng nhận thẳng hàng hệ thống và hồ sơ liên quan** được diễn đàn giám sát — miền đánh giá (Phần A); nghĩa vụ hồ sơ chứng nhận, kết quả công nhận, nhịp tái xác nhận, trình tự giám sát, chuỗi khả năng tranh biện, và cầu đầu vào đã xác minh tới Chương Tám (Phần B). Dưới trụ **giám sát** của Tứ diện, SAC là một quy trình kiểm toán đặc biệt lớn, lợi hại cao giữa các quy trình khác; sàn kiểm toán vẫn ở **Điều XVI** và [Khả năng kiểm toán](core_05_band_oversight.md#auditability) của Chương Năm.
> - **Chủ sở hữu nền xác minh:** [Chương Bốn — Gánh chứng minh, truy vết, và xác minh](core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (trong các Chương Hai đến Bốn) nắm phân bổ gánh, bằng chứng tuân thủ, truy vết định nghĩa, khả năng quan sát, và xác minh dưới giới hạn an ninh. Chương Bảy **áp dụng** kỷ luật đó cho hồ sơ chứng nhận thẳng hàng hệ thống; nó **không** nêu lại các mục **1** đến **5** của Chương Bốn.
> - **Nhà kiểm toán (không dời tới đây):** **Điều XVI** (*Kiểm toán, minh bạch, và xác minh độc lập*), **Def.O1** (*Minh bạch, khả năng kiểm toán, và xác minh*), và **CJS-3.3**–**CJS-3.5** nắm sàn kiểm toán và thuật ngữ vận hành. Chương Bảy chạy một quy trình kiểm toán SAC đặc biệt lớn phải thỏa những sàn đó; nó không nắm mọi kiểm toán.
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
> **Tuyên bố quản trị có trách nhiệm mang tính vận hành.** **Chủ trì:** Chương Bảy (SAC được diễn đàn giám sát). Lăng kính tầng nguyên tắc: Chương Một §14. SAC là một quy trình kiểm toán đặc biệt lớn dưới Điều XVI / Khả năng kiểm toán — không phải kiểm toán duy nhất. **Động thái bị cấm:** Đừng coi thử đơn vị, danh sách kiểm quyền riêng tư, hay nhãn thẳng hàng địa phương là chứng nhận. Đừng bỏ cửa sổ tranh biện. Đừng bịa nhà kiểm toán thứ năm. Đừng coi phù hiệu chứng nhận hay điểm LEQU là trạng thái hữu tri. **Đồng hồ:** Mở hoặc khôi một đường Chương Bảy tranh biện được, kể cả cửa sổ tranh biện của bên bị ảnh hưởng, trước tuyên thẳng hàng.

<a id="1-purpose-and-role"></a>

### 1. Mục đích và vai trò

<details>
<summary><strong><span style="color: #2563eb;">Truy nguyên và liên kết</span></strong></summary>

- **Cơ sở phía trước:** [Lời nói đầu — sổ đăng ký chủ thể hiến pháp](core_00_preamble.md#4-principles-definitions-and-rights) và [thứ bậc thẩm quyền](core_05_band_integrative.md#authority-stack-and-internal-hierarchy); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality) và [công bằng thực chất](../../core_05.055_band_participation.md#substantive-fairness) (Chương Năm); họ phép đo tham gia (*tiếng nói, khả năng tiếp cận và con đường tranh biện*); [Chương Một §16 — Quản trị có trách nhiệm chuyên sâu](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth); [Chương Một §12 — Yêu cầu đánh giá có tính hệ thống](core_01_a_values_principles.md#12-systemic-evaluation-requirement) (*lăng kính đánh giá toàn hệ thống ở tầng nguyên tắc — không chỉ một góc riêng lẻ*); Chương Hai đến Chương Bốn; [Chương Năm](core_05__definitions_home.md#chapter-five-foundational-definitions) (*các định nghĩa chuẩn tắc*); [Chương Bảy §2 — Ngưỡng hiến pháp bốn ghế](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement); [Chứng nhận mức độ phù hợp của hệ thống](../../core_05.040_band_continuity.md#system-alignment-certification) (thuật ngữ chuẩn tắc ở Chương Năm; chữ viết tắt **SAC** không có hiệu lực vận hành); [Hồ sơ chứng nhận hệ thống](../../core_05.040_band_continuity.md#system-certification-record) (ý nghĩa trong Chương Năm).
- **Liên kết phía sau:** [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); [Phần B §9.1](../../core_09.010_system_alignment_certification_record_process.md#91-challenging-a-certification) (*tranh biện chứng nhận*); hồ sơ lớp, ví dụ toàn hệ thống và ví dụ theo từng lĩnh vực nằm trong [Phần C](../../core_09.015_system_alignment_certification_illustrations.md): [hồ sơ minh họa về lớp hệ thống](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive), [các bước minh họa áp dụng cho toàn hệ thống theo lớp](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive), ví dụ xử lý dữ liệu [§3.4.8](../../core_09.015_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive), dấu chân sinh thái [§5.1.5](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive), năng lực giáo dục [§5.2.5](../../core_09.015_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive), hỗ trợ liên hệ thống [§5.3.8](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive), không phân biệt đối xử [§5.4.5](../../core_09.015_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive), khả năng tiếp cận [§5.5.6](../../core_09.015_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) và độ đáng tin cậy [§5.6.5](../../core_09.015_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive); [§3](#3-whole-system-certification-evaluation) (*các yếu tố đánh giá chứng nhận toàn hệ thống*); [§3.4](#34-data-types-and-handling-evaluation)–[§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*đánh giá theo lĩnh vực*); [Phần B §6](../../core_09.010_system_alignment_certification_record_process.md#6-forum-process) (*trình tự giám sát và chuỗi tranh biện*); [Phần B §6.1](../../core_09.010_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) (*vai trò các bộ phận diễn đàn*); [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ chứng nhận*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*mở lại và chống né tránh*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cầu nối tới hồ sơ quỹ đạo*); [Chương Chín](core_08_standing_assessment.md) (*hồ sơ quỹ đạo và ngưỡng đầu vào đã xác minh*); [Chương Mười](core_09_standing_integration.md) (*tác động và tích hợp quỹ đạo*); [Chương Mười Hai](core_11_forum.md) (*giám sát của diễn đàn, chứng nhận, mức độ phù hợp và rà soát*).
- **Đọc cùng:** [corpus_systems.md](../../corpus_systems.md), đặc biệt **CS-3 — phân loại và xử lý hệ thống**, **CS-2 — loại thông tin và xử lý**, và **CS-5** (*các bề mặt năng lực hướng tới người dùng*); [corpus_forum.md](../../corpus_forum.md), đặc biệt **CF-5** (*định tuyến, chuyển giao, chứng nhận và đại diện*) và **CF-7** (*bảo đảm toàn vẹn, chống chiếm dụng và hỗ trợ chống tự phân xử*); **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) và [Khả năng kiểm toán](core_05_band_oversight.md#auditability) (*các ngưỡng kiểm toán — SAC là một quy trình kiểm toán đặc biệt lớn dưới sự giám sát, không phải nơi duy nhất tiến hành kiểm toán*); **CJS-3.3** (*giám sát: thuật ngữ về khả năng kiểm toán và tái dựng*)–**CJS-3.5** (*xác minh độc lập và tính toàn vẹn của tuyên bố*).

</details>

<br>

*Nói đơn giản: Khi một hệ thống thực sự quan trọng đối với đời sống của các hữu tri, việc chứng nhận phải **tương xứng** — mức độ nghiêm ngặt phải đáp ứng tác động thực tế, sự phụ thuộc và rủi ro của hệ thống; không phải một danh sách kiểm tra áp dụng như nhau cho mọi nơi hay một con dấu hình thức. Việc này cũng phải **có sự tham gia**: các hữu tri và cộng đồng bị ảnh hưởng phải có thể thấy nội dung đã được xem xét, hiểu quyết định và tranh biện khi có sai sót. Các diễn đàn xem xét chứng cứ, ghi lại trong hồ sơ chứng nhận và yêu cầu kiểm tra lại theo lịch phù hợp với mức độ rủi ro của hệ thống. Các lớp A, B và C áp dụng đầy đủ quy trình; lớp L áp dụng quy trình nhẹ hơn. Khuyến khích lớp P sử dụng quy trình; quy trình trở thành bắt buộc khi tác động vượt ra ngoài một đơn vị tư nhân hoặc khi đơn vị vận hành tuyên bố tuân thủ hiến pháp.*

*Chứng nhận không phải điểm số phổ biến, giấy thông hành vĩnh viễn hay cách bỏ qua việc rà soát quyền. Đây là tuyên bố có giới hạn thời gian và có thể bị tranh biện về những gì hiện biết liên quan đến mức độ phù hợp của hệ thống. Theo trụ **giám sát** của Tứ diện, giám sát đòi hỏi kiểm toán. Chứng nhận mức độ phù hợp của hệ thống là một trong những quy trình kiểm toán đặc biệt lớn và có rủi ro cao, bên cạnh các quy trình khác — không phải nơi duy nhất tiến hành kiểm toán (**Điều XVI**, [Khả năng kiểm toán](core_05_band_oversight.md#auditability)).*

**Chứng nhận mức độ phù hợp của hệ thống** trả lời một câu hỏi trong phạm vi và lịch rà soát đã nêu: Hệ thống đã chứng minh mức độ phù hợp hiến pháp đủ để được chứng nhận, chứng nhận có điều kiện, xác nhận, chứng nhận lại, tiếp tục dựa vào hệ thống, triển khai hoặc gỡ bỏ đáng kể các điều kiện hay chưa?

Độ sâu chứng nhận, gánh nặng hồ sơ, nhịp chứng nhận lại, rà soát của các bên liên quan và con đường tranh biện phải được điều chỉnh theo [lợi hại vật chất](core_00_preamble.md#material-stake) phù hợp với [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality):

- Hệ thống có tác động, mức phụ thuộc và rủi ro cao hơn cần chứng cứ mạnh hơn, hồ sơ rõ hơn và sự tham gia khả thi hơn — gồm khả năng tiếp cận thực chất, ý kiến của các bên liên quan và lối tranh biện phù hợp với những ai dựa vào hệ thống.
- Các lớp hệ thống thấp hơn và phạm vi giới hạn vẫn cần phân loại trung thực và bảo đảm tương xứng; khi tồn tại tác động bên ngoài, chúng không được miễn nghĩa vụ vật chất.

Quy trình áp dụng theo lớp tác động như [CS-3 §3.5 — Yêu cầu phân loại lại](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement) quy định:

- **Lớp A, B và C:** các hệ thống này có tác động, mức phụ thuộc và rủi ro cao nhất. Đánh giá toàn hệ thống theo [§3](#3-whole-system-certification-evaluation), [§4](#4-evaluations-where-implicated) và [§5](#5-rights-floor-and-domain-evaluations) là bắt buộc ở mức đầy đủ đối với từng tầng được áp dụng.
- **Lớp L:** cùng đánh giá đó vẫn là bắt buộc nhưng được áp dụng tương xứng; khi CS-3 cho phép, chu kỳ kiểm tra lại mặc định dài hơn và hồ sơ đơn giản hơn.
- **Lớp P:** quy trình được khuyến khích khi hệ thống còn hợp lệ ở lớp P và hệ thống có thể tự nguyện áp dụng. Quy trình trở thành bắt buộc khi hệ thống được phân loại lại thành L trở lên, hoặc khi đơn vị vận hành tự nguyện tuyên bố hệ thống tuân thủ hiến pháp.

Chứng nhận thực hiện [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) thông qua [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad):

- **[Hưng thịnh](core_00_preamble.md#flourishing)** — chứng nhận xác minh rằng việc chứng nhận hay tiếp tục dựa vào hệ thống sẽ không âm thầm làm mất hiệu lực các Sàn Quyền hoặc cản trở sự tham gia công bằng vào đời sống có ý nghĩa hiến pháp;
- **[Liên tục](core_00_preamble.md#continuity)** — xác minh nguồn cung ổn định, không thụt lùi, giúp duy trì thay vì làm cạn kiệt các hệ thống tự nhiên lành mạnh ([Tính toàn vẹn sinh thái](../../core_05.040_band_continuity.md#ecological-integrity), bao gồm [Năng lực phục hồi sinh thái](../../core_05.040_band_continuity.md#ecological-recovery-capacity)); đồng thời chứng nhận lại theo quy mô lớp khi hệ thống dùng chung là điều kiện hoặc hỗ trợ cho việc cung ứng;
- **Tham gia** — các hữu tri và cộng đồng bị ảnh hưởng có thể hiểu, tranh biện và tham gia vào những con đường rà soát có ý nghĩa đối với họ;
- **Giám sát** — hồ sơ, chứng cứ và giả định phải đủ hiển thị và có thể kiểm toán để kiểm tra độc lập; bản thân chứng nhận là một quy trình kiểm toán đặc biệt lớn theo nghĩa vụ giám sát này, nhưng không phải quy trình duy nhất;
- **Trách nhiệm giải trình** — khi sự kiện hỗ trợ, khiếm khuyết, phân loại sai và hoạt động làm mất hiệu lực sàn được chuyển tới biện pháp khắc phục, điều kiện, thu hồi hoặc đầu vào cho hồ sơ quỹ đạo;
- **Kịp thời** — thời hạn rà soát và tranh biện ngăn chứng nhận trở nên lỗi thời khi tổn hại vẫn còn có thể ngăn chặn hoặc đảo ngược.

Là một công cụ giám sát, chứng nhận là một quy trình kiểm toán đặc biệt lớn theo [Khả năng kiểm toán](core_05_band_oversight.md#auditability) và **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*). Quy trình này do diễn đàn giám sát, bao quát nhiều lĩnh vực và cấp trạng thái. Quy trình có thể kết hợp kết quả từ các hình thức kiểm toán liên quan, nhưng không hấp thụ hay thay thế chúng. Mỗi hình thức giữ nguyên đơn vị chịu trách nhiệm riêng được nêu trong [bản đồ các hình thức kiểm toán liên quan](../../corpus_joint_structure/cjs_05.115_audit_process.md#sibling-audit-modes-owner-map) thuộc tài liệu về quy trình kiểm toán:

- kiểm toán Hồ sơ Loại Dữ liệu Hệ thống theo **CS-2** (*Loại thông tin và xử lý*);
- kiểm toán Hồ sơ Phân loại Hệ thống theo **CS-3** (*Cơ chế phân loại hệ thống*);
- rà soát bảo đảm quản trị có trách nhiệm theo **CS-4** (*Quản trị hệ thống trọng yếu*);
- kiểm toán liên tục theo **CS-5** (*Thiết kế, thử nghiệm, xác minh và triển khai*) **ACA**;
- kiểm toán độ phức tạp theo **CS-6** (*Khả năng hiểu và quản trị độ phức tạp*) và **Điều XXIII-B** (*Yêu cầu Kiểm toán Độ phức tạp và Tính mô-đun*);
- xác minh tuyên bố theo **CJS-3.5** (*Xác minh độc lập và thuật ngữ về tính toàn vẹn tuyên bố*).

Có thể tự tiến hành từng kiểm tra này mà không cần quy trình chứng nhận. Chứng nhận không thay thế chúng.

<a id="11-certification-at-a-glance"></a>

#### 1.1 Tổng quan nhanh về chứng nhận

*Nói đơn giản: phân loại hệ thống một cách trung thực, tiến hành các đánh giá áp dụng, để các diễn đàn rà soát độc lập chứng cứ và quan ngại của các bên liên quan, rồi quyết định kết quả. Hoàn tất hồ sơ duy nhất được mở để diễn đàn xem xét và công bố hồ sơ với con đường tranh biện mở. Chỉ đưa hệ thống đã chứng nhận vào vận hành sau thời hạn thông báo và khi các biện pháp bảo vệ bắt buộc đã được đáp ứng. Theo dõi kết quả thực tế, phản hồi sự cố và tranh biện, rồi rà soát lại theo lịch hoặc khi sự kiện thay đổi. Khắc phục khiếm khuyết và xác minh độc lập việc khắc phục trước khi cho phép phạm vi bị ảnh hưởng hoạt động hoặc gỡ bỏ điều kiện. Mỗi lượt rà soát dùng hồ sơ mới được liên kết với hồ sơ trước đó.*

Quy trình gồm **sáu giai đoạn**: **I. Xác định khung**, **II. Đánh giá**, **III. Rà soát**, **IV. Quyết định**, **V. Ghi hồ sơ** và **VI. Vận hành**. Giai đoạn II gồm ba tầng, mỗi tầng có mục riêng: **IIa** (luôn áp dụng), **IIb** (khi có vấn đề liên quan) và **IIc** (khi được kích hoạt). Giai đoạn VI gồm hai giai đoạn phụ: **VIa** (vận hành và chứng nhận lại, [§9](../../core_09.010_system_alignment_certification_record_process.md#9-recertification-and-reopening)) và **VIb** (cầu nối quỹ đạo, [§10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing)). Sơ đồ thể hiện toàn bộ quy trình chứng nhận theo thứ tự. Phần A bao quát hai giai đoạn đầu: xác định khung và đánh giá; [Phần B](core_07_b_system_alignment_certification_record_process.md) bao quát bốn giai đoạn còn lại: quy trình tại diễn đàn, quyết định và điều kiện cho phép vận hành, hồ sơ và vận hành (con đường tranh biện, chứng nhận lại, mở lại và cầu nối quỹ đạo).

Mỗi đánh giá được áp dụng phải được thực hiện lại trong từng lượt chứng nhận: ở lần chứng nhận đầu tiên, ở mỗi lần chứng nhận lại theo lịch quy định tại [§2](#2-system-class-evaluation), và ở mỗi lần rà soát được mở lại hoặc bắt đầu mới. Khi sự kiện vật chất thay đổi — chẳng hạn mức phụ thuộc vào hệ thống tăng, mức khai thác từ nền tảng dùng chung tăng, đóng góp trở lại các nền tảng đó giảm đáng kể hoặc có tranh biện đáng tin cậy — việc rà soát được mở lại trước lần chứng nhận lại theo lịch tiếp theo. [Phần B §9](../../core_09.010_system_alignment_certification_record_process.md#9-recertification-and-reopening) liệt kê các yếu tố kích hoạt.

```mermaid
flowchart TB
    T(["Hệ thống có tác động vật chất xin chứng nhận,<br/>hoặc mức phụ thuộc vào hệ thống tăng"])
    C["Giai đoạn I, Xác định khung — §2<br/>Phân loại trung thực<br/><br/>Lớp xác định độ sâu và lịch kiểm tra lại"]
    subgraph W["Giai đoạn II, Đánh giá — §3–§5 Đánh giá toàn hệ thống"]
        direction LR
        Al["IIa, §3.1–§3.4 — Luôn áp dụng<br/><br/>Rủi ro hệ thống: đánh giá và công bố<br/>cho người cần biết; khung thời gian;<br/>quản trị; loại dữ liệu"]
        Im["IIb, §4 — Khi có vấn đề liên quan<br/><br/>Điểm riêng tư, quyền rời khỏi,<br/>hội họp và bất đồng"]
        Tr["IIc, §5 — Khi được kích hoạt<br/><br/>Kiểm tra Sàn Quyền áp dụng<br/>và sáu đánh giá theo lĩnh vực"]
        Al ~~~ Im ~~~ Tr
    end
    F["Giai đoạn III, Rà soát — §6<br/>Rà soát độc lập chứng cứ<br/>và quan ngại của các bên liên quan<br/><br/>Các diễn đàn được phân công đưa ra phát hiện;<br/>con đường tranh biện vẫn mở"]
    Rec["Giai đoạn V, Ghi hồ sơ — §8<br/>Một Hồ sơ Chứng nhận Hệ thống<br/><br/>Mở để diễn đàn xem xét; hoàn tất với kết quả,<br/>phát hiện hỗ trợ, điều kiện và kế hoạch vận hành"]
    S[["Chương Chín — Hồ sơ<br/>quỹ đạo<br/><br/>Ngoài chương này"]]
    O{"Giai đoạn IV, Quyết định — §7<br/><br/>Chứng cứ hỗ trợ kết quả và<br/>trạng thái nào?"]
    Fc["Chứng nhận Đầy đủ — §7, §9.2<br/><br/>Cần đủ số lần chứng nhận lại tạm thời liên tiếp đạt yêu cầu;<br/>không có sai lệch hiện tại hay sắp xảy ra<br/>Thời hạn chứng nhận lại dài hơn; có thể kèm điều kiện"]
    Pc["Chứng nhận Tạm thời — §7, §9.2<br/><br/>Cấp lần đầu, khôi phục sau sai lệch,<br/>hoặc duy trì hay hạ mức trạng thái tạm thời<br/>Thời hạn ngắn hơn; có thể kèm điều kiện"]
    Nc["Không được Chứng nhận — §7<br/><br/>Hoãn, từ chối, thu hồi hoặc hết hạn<br/>Không vận hành; nêu lý do và công việc khắc phục cần thiết"]
    Pub["Công bố hồ sơ đã hoàn tất — §7, §9.1<br/><br/>Mở con đường tranh biện hồ sơ đã công bố;<br/>nêu thời điểm vận hành và thông báo cho phạm vi mới hoặc mở rộng"]
    G{"Điều kiện cho phép vận hành — §7<br/><br/>Đã đáp ứng chứng nhận và các<br/>điều kiện tiên quyết áp dụng chưa?"]
    Hold["Đáp ứng điều kiện tiên quyết — §7<br/><br/>Hoàn thành thời hạn thông báo và xác minh độc lập<br/>các điều kiện cần thiết trước khi vận hành"]
    Rm["Bảo vệ và khắc phục — §7, §9.2<br/><br/>Không vận hành mới trong phạm vi bị ảnh hưởng;<br/>bảo vệ các hữu tri bị ảnh hưởng, khắc phục thiết kế hoặc vận hành,<br/>và nộp chứng cứ để xác minh độc lập"]
    Ch["Giai đoạn VIa, Vận hành và chứng nhận lại — §9–§9.2<br/>Theo dõi và duy trì tranh biện mở<br/><br/>Vận hành trong phạm vi và điều kiện được chứng nhận;<br/>theo dõi kết quả, phản hồi sự cố và tranh biện"]
    S2[["Chương Chín — Hồ sơ<br/>quỹ đạo<br/><br/>Ngoài chương này"]]
    Sp["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpL["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpA["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    Re["Lượt rà soát tiếp theo — §9<br/><br/>Chứng nhận lại, mở lại hoặc rà soát mới;<br/>mỗi lượt mở hồ sơ mới liên kết với hồ sơ trước"]
    T --> C
    A1((A)) --> C
    C --> W
    W --> F
    F --> O
    O --> Fc
    O --> Pc
    O --> Nc
    Fc --> Rec
    Pc --> Rec
    Nc --> Rec
    Rec -.->|VIb, §10 —<br/>chỉ dùng đầu vào đã xác minh;<br/>chứng nhận hiện tại hoặc sự kiện<br/>phát sinh trong quá trình chứng nhận| S
    Rec --> Pub
    Rec ~~~ Sp
    Pub --> G
    G ~~~ SpL
    G -->|Không được chứng nhận| Rm
    G --->|Có: vận hành trong<br/>phạm vi của hồ sơ| Ch
    G --->|Đã chứng nhận,<br/>đang chờ điều kiện tiên quyết| Hold
    Hold --> G
    Ch -->|Khiếm khuyết vật chất:<br/>bảo vệ và khắc phục| Rm
    Ch -->|Đúng lịch, hoặc khi<br/>thay đổi vật chất hay tranh biện<br/>đáng tin cậy cần rà soát| Re
    Ch -.->|VIb, §10 —<br/>chỉ dùng đầu vào đã xác minh;<br/>vận hành có thể cung cấp sự kiện<br/>cho hồ sơ Đóng góp<br/>và Vi phạm| S2
    Rm -->|Chứng cứ khắc phục<br/>được kiểm tra trong lượt<br/>rà soát tiếp theo| Re
    S2 ~~~~ SpA
    SpA ~~~ Re
    Re --> A2((A))
    style Sp fill:none,stroke:none,color:#111111
    style SpL fill:none,stroke:none,color:#111111
    style SpA fill:none,stroke:none,color:#111111
    style T fill:none,stroke:#64748b,color:#ffffff
    style C fill:none,stroke:#16a34a,color:#ffffff
    style Ch fill:none,stroke:#16a34a,color:#ffffff
    style Al fill:none,stroke:#16a34a,color:#ffffff
    style Im fill:none,stroke:#16a34a,color:#ffffff
    style Tr fill:none,stroke:#16a34a,color:#ffffff
    style F fill:none,stroke:#ea580c,color:#ffffff
    style Rec fill:none,stroke:#2563eb,color:#ffffff
    style S fill:none,stroke:#db2777,color:#ffffff
    style S2 fill:none,stroke:#db2777,color:#ffffff
    style O fill:none,stroke:#ea580c,color:#ffffff
    style Fc fill:none,stroke:#9333ea,color:#ffffff
    style Pc fill:none,stroke:#9333ea,color:#ffffff
    style Nc fill:none,stroke:#9333ea,color:#ffffff
    style G fill:none,stroke:#ea580c,color:#ffffff
    style Pub fill:none,stroke:#2563eb,color:#ffffff
    style Rm fill:none,stroke:#9333ea,color:#ffffff
    style Hold fill:none,stroke:#16a34a,color:#ffffff
    style Re fill:none,stroke:#16a34a,color:#ffffff
    style A1 fill:none,stroke:#64748b,color:#ffffff
    style A2 fill:none,stroke:#64748b,color:#ffffff
```

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn đọc (không mang tính vận hành): sáu giai đoạn</span></strong></summary>

> | Giai đoạn | Mục | Câu hỏi giai đoạn trả lời | Nơi quy định |
> |-------|----------|------------------------------|-------|
> | **I. Xác định khung** | [§2](#2-system-class-evaluation) | Hệ thống thuộc lớp nào, và cần đánh giá sâu đến đâu, thường xuyên thế nào? | Phần A |
> | **II. Đánh giá** | [§3](#3-whole-system-certification-evaluation) (IIa, luôn luôn) · [§4](#4-evaluations-where-implicated) (IIb, khi có vấn đề liên quan) · [§5](#5-rights-floor-and-domain-evaluations) (IIc, khi được kích hoạt) | Toàn hệ thống làm gì — luôn luôn, khi vấn đề liên quan và khi có yếu tố kích hoạt? | Phần A |
> | **III. Rà soát** | [§6](../../core_09.010_system_alignment_certification_record_process.md#6-forum-process) | Những diễn đàn độc lập nào rà soát chứng cứ và quan ngại của các bên liên quan, theo thứ tự nào, và có thể tranh biện việc rà soát ra sao? | Phần B |
> | **IV. Quyết định** | [§7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) | Các diễn đàn đưa ra kết quả nào, và hệ thống có thể được đưa vào vận hành không? | Phần B |
> | **V. Ghi hồ sơ** | [§8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) | Hồ sơ duy nhất mở để diễn đàn xem xét có đầy đủ kết quả, phát hiện hỗ trợ, điều kiện và kế hoạch vận hành không, và có thể kiểm toán không? | Phần B |
> | **VI. Vận hành** | [§9](../../core_09.010_system_alignment_certification_record_process.md#9-recertification-and-reopening) (VIa, vận hành và chứng nhận lại) · [§10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (VIb, cầu nối quỹ đạo) | Ai theo dõi kết quả và phản hồi sự cố, tranh biện; việc khắc phục được xác minh thế nào; khi nào rà soát lặp lại; nội dung nào chuyển vào hồ sơ quỹ đạo? | Phần B |
>
> Hồ sơ minh họa cho lớp **A**, **B** và **C**, cùng cách lớp hệ thống điều chỉnh độ sâu chứng nhận trong chương này, được trình bày trong [Hồ sơ Minh họa về Lớp Hệ thống (Không Toàn diện)](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive). Các bước áp dụng có giải thích cho cùng ba hệ thống trong từng lĩnh vực đánh giá từ [§3](#3-whole-system-certification-evaluation) đến [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) nằm tiếp theo trong [Phần C — Ví dụ minh họa](../../core_09.015_system_alignment_certification_illustrations.md); mỗi hồ sơ và ví dụ đều liên kết ngược tới mục Phần A mà nó minh họa.

</details>

<br>

<a id="2-system-class-evaluation"></a>

### 2. Đánh giá Lớp Hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [§1](#1-purpose-and-role) (*mục đích và vai trò*); tính trọng yếu tích hợp ([Tính Trọng yếu](../../core_05.050_band_oversight.md#materiality)) (*Tính Trọng yếu*); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [Tác động Vật chất](core_05_band_oversight.md#material-impact), [Phụ thuộc](../../core_05.040_band_continuity.md#dependency), [Rủi ro](../../core_05.040_band_continuity.md#risk), [Ranh giới Hệ thống](../../core_05.040_band_continuity.md#system-boundaries), và [Điều lệ](../../core_05.040_band_continuity.md) (Chương Năm); [Chương Một §12 Yêu cầu Đánh giá Hệ thống](core_01_a_values_principles.md#12-systemic-evaluation-requirement); **Điều III-A** (*Sinh tồn*) và **Điều IV-A** (*cung cấp Sàn Quyền khi phân loại kiểm soát quyền tiếp cận*); **Điều V-A** (*Lập bản đồ Phụ thuộc và Minh bạch Luồng Tài nguyên*) và **Điều V-B** (*phân bổ tài nguyên và quản trị phụ thuộc khi chứng nhận đặt điều kiện cho việc dựa vào hạ tầng chung*).
- Hạ nguồn: [§2.1](#21-how-system-class-scales-every-evaluation) (*sự tham gia và tính tương xứng theo lớp hệ thống*); [§2.2](#22-pilot-certification) (*chứng nhận thí điểm*); [hồ sơ lớp hệ thống và phân loại lại ở Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive) (*hồ sơ lớp hệ thống minh họa*); [các hướng dẫn toàn hệ thống ở Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) (*ví dụ toàn hệ thống theo lớp hệ thống*); [§3.4.8](../../core_09.015_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*ví dụ xử lý dữ liệu theo lớp hệ thống*); [§5.1.5](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*ví dụ dấu chân sinh thái theo lớp hệ thống*); [§5.2.5](../../core_09.015_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*ví dụ năng lực giáo dục theo lớp hệ thống*); [§5.3.8](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*ví dụ hỗ trợ liên hệ thống theo lớp hệ thống*); [§5.4.5](../../core_09.015_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*ví dụ không phân biệt đối xử theo lớp hệ thống*); [§5.5.6](../../core_09.015_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*ví dụ khả năng tiếp cận theo lớp hệ thống*); [§5.6.5](../../core_09.015_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*ví dụ độ đáng tin cậy theo lớp hệ thống*); [§3.4](#34-data-types-and-handling-evaluation) (*đánh giá chung về xử lý dữ liệu*); [§5.1](#51-ecological-footprint-evaluation) (*đánh giá dấu chân sinh thái*); [§5.3](#53-proportionate-cross-system-support-evaluation) (*đánh giá hỗ trợ liên hệ thống tương xứng*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn của hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*trôi dạt phân loại và các yếu tố kích hoạt phân loại lại*).
- Đọc cùng: [Hồ sơ Phân loại Hệ thống](../../core_05.040_band_continuity.md#system-classification-record); [corpus_systems.md](../../corpus_systems.md), **CS-3 — Phân loại và xử lý hệ thống**, bao gồm **[CS-3 §3.5 yêu cầu phân loại lại](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*các yếu tố kích hoạt, độ sâu đánh giá theo lớp hệ thống, và cầu nối xác minh SAC*) và **[CS-3 §7](../../corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-7-classification-governance-disclosure-and-challenge)** (*Quản trị, công bố và phản đối việc phân loại*) — nghĩa vụ quản trị Hồ sơ Phân loại Hệ thống và cầu nối SAC; [CS-5 — Thiết kế, thử nghiệm, xác minh và triển khai](../../corpus_systems/cs_06.345_design_testing_verification_deployment.md); [CJS-3.21 — thuật ngữ về khả năng chống đối kháng và chống lạm dụng](../../corpus_joint_structure/cjs_05.130_continuity_operations.md#cjs-5130-21-continuity-adversarial-robustness-and-abuse-resistance-terms) (*nghĩa vụ chu kỳ hồi quy và gia cố*); [corpus_forum.md](../../corpus_forum.md), **CF-7.2** (*Chứng nhận và rà soát sự phù hợp hiến pháp*).

</details>

<br>

*Diễn đạt đơn giản: chứng nhận phải kiểm tra xem hệ thống có được phân loại trung thực hay không — không dựa vào tên do đơn vị vận hành đặt, mà dựa vào việc hệ thống thực sự làm gì, ai hoặc điều gì phụ thuộc vào nó, và điều gì có thể xảy ra sai lệch. Lớp hệ thống càng cao thì yêu cầu chứng cứ càng nghiêm ngặt, việc kiểm tra lại càng thường xuyên và kỳ vọng về khả năng chống chịu càng mạnh. Xem [Phần C — Minh họa](../../core_09.015_system_alignment_certification_illustrations.md) để biết một hệ thống ví dụ cho mỗi lớp và cách đánh giá áp dụng cho từng hệ thống.*

Mọi hồ sơ chứng nhận cho một hệ thống có tác động vật chất phải bao gồm đánh giá **lớp hệ thống**.

Các quy tắc chi tiết nằm trong [corpus_systems.md](../../corpus_systems.md), [CS-3 — Phân loại và xử lý hệ thống](../../corpus_systems/cs_09.305_system_classification_machinery.md), và [CS-5 — Thiết kế, thử nghiệm, xác minh và triển khai](../../corpus_systems/cs_06.345_design_testing_verification_deployment.md). Chúng bao gồm:

- các lớp hệ thống là gì, cách xác định lớp, và hồ sơ của từng lớp;
- việc phân loại được quản trị như thế nào;
- mỗi lớp cần mức bảo đảm ra sao;
- hạ tầng phải có khả năng chống chịu đến mức nào;
- những kiểm tra và hồ sơ nào được chứng nhận lại, theo lịch trình tương xứng với lớp hệ thống, và chứng nhận tạm thời/toàn phần làm thay đổi lịch trình ra sao.

Phần này nêu những điều mà chứng nhận phải xác minh.

Chứng nhận phải xác minh:

- **Yêu cầu đánh giá:**
  - lớp hệ thống được chỉ định có phản ánh **tác động**, **phụ thuộc** và **rủi ro** đã quan sát được và có thể dự đoán hợp lý theo CS-3 (*Cơ chế phân loại hệ thống*) hay không, bao gồm:
    - tác động tổng hợp;
    - tác động tương tác;
    - tác động đối kháng;
    - tác động ngưỡng;
  - việc phân loại có được xác định bởi hành vi và tác động thực tế của hệ thống, chứ không phải bởi:
    - ý định được tuyên bố;
    - phạm vi danh nghĩa;
    - chỉ riêng nội dung [Điều lệ](../../core_05.040_band_continuity.md); hoặc
    - chỉ riêng phần tự mô tả;
  - lớp hệ thống đã được kiểm tra lại theo **[CS-3 §3.5 yêu cầu phân loại lại](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** mỗi khi có thay đổi đáng kể đòi hỏi việc đó; và
  - [Hồ sơ Phân loại Hệ thống](../../core_05.040_band_continuity.md#system-classification-record) có thể hiện **lớp hệ thống cao nhất đang áp dụng** trong điều kiện hiện tại hay không.
- **Bảo đảm và kiểm thử hồi quy:**
  - việc bảo đảm, khả năng chống chịu của hạ tầng và phạm vi kiểm thử hồi quy theo lớp hệ thống có phù hợp với lớp được chỉ định theo:
    - CS-3 (*Cơ chế phân loại hệ thống*); và
    - CS-5 (*Các bề mặt năng lực hướng đến người dùng*), đọc cùng các thuật ngữ vận hành chung sau đây khi có liên quan đáng kể:
      - [**CJS-3.19**](../../corpus_joint_structure/cjs_05.130_continuity_operations.md#cjs-5130-19-continuity-graceful-degradation-and-failure-mode-integrity-terms) (*Liên tục: suy giảm có kiểm soát và tính toàn vẹn của chế độ lỗi*);
      - [**CJS-3.20**](../../corpus_joint_structure/cjs_05.130_continuity_operations.md#cjs-5130-20-continuity-reversibility-and-containment-terms) (*Liên tục: khả năng đảo ngược và ngăn chặn*);
      - [**CJS-3.21**](../../corpus_joint_structure/cjs_05.130_continuity_operations.md#cjs-5130-21-continuity-adversarial-robustness-and-abuse-resistance-terms) (*Liên tục: khả năng chống chịu đối kháng và chống lạm dụng*); và
      - [**CJS-3.22**](../../corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Tích hợp: bí mật có giới hạn và điều tra được bảo vệ*) cùng [**CJS-3.23**](../../corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Tích hợp: can thiệp và tính toàn vẹn của quyền ghi đè*), khi lớp hoặc chức năng của hệ thống khiến chúng có liên quan đáng kể; và
  - kiểm thử hồi quy có được thực hiện ở mỗi lần chứng nhận lại theo yêu cầu CS-5 (*Các bề mặt năng lực hướng đến người dùng*), với kết quả được ghi vào hồ sơ theo [§8.1 Nội dung tối thiểu của hồ sơ](../../core_09.010_system_alignment_certification_record_process.md#81-minimum-record-contents) hay không.
- **Chứng nhận và chứng nhận lại:**
  - có gói chứng cứ chứng nhận và rà soát cho chu kỳ chứng nhận hay không, theo yêu cầu *Chứng nhận diễn đàn và rà soát vòng đời* của CS-5 (*Các bề mặt năng lực hướng đến người dùng*);
  - tình trạng chứng nhận trong hồ sơ có được hỗ trợ theo [Phần B §9.2 Chứng nhận tạm thời và toàn phần](../../core_09.010_system_alignment_certification_record_process.md#92-provisional-and-full-certification) hay không:
    - chỉ chứng nhận toàn phần khi:
      - đạt ngưỡng tối thiểu về các lần chứng nhận lại sạch liên tiếp;
      - hiện không có sự lệch chuẩn; và
      - không có chỉ báo giám sát nào cho thấy sự lệch chuẩn sắp xảy ra;
    - chứng nhận tạm thời dành cho hệ thống đã thất bại ở lần chứng nhận lại gần nhất; và
  - đối với hệ thống cung cấp hoặc phụ thuộc vào các bảo vệ cơ bản của Sàn Quyền:
    - tần suất kiểm tra lại và độ sâu kiểm thử lại có phục vụ mục tiêu **Liên tục** trong [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims), nghĩa là các nhu cầu thiết yếu tiếp tục đến với hữu tri theo thời gian hay không;
    - không bao giờ được xem chứng nhận đã lỗi thời hoặc quá sớm là bằng chứng rằng hữu tri hôm nay thực sự nhận được thức ăn, nước, chỗ ở, giáo dục hoặc an toàn.
- **Phân loại sai và khiếm khuyết:**
  - các khiếm khuyết chứng nhận theo CS-3 (*Cơ chế phân loại hệ thống*) và [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes), chứ không phải lỗi giấy tờ nhỏ, bao gồm:
    - tuyên bố lớp rủi ro thấp hơn mức phù hợp với hệ thống;
    - chia hệ thống thành nhiều phần để né các quy tắc nghiêm ngặt hơn; hoặc
    - giữ nhãn lớp hệ thống cũ sau khi điều kiện thay đổi, kể cả việc không đánh giá lại theo **[CS-3 §3.5 yêu cầu phân loại lại](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**;
  - khiếm khuyết chứng nhận theo CS-5 (*Các bề mặt năng lực hướng đến người dùng*) bao gồm:
    - bỏ qua kiểm thử hồi quy;
    - dựa vào kết quả lỗi thời;
    - để nguyên các lỗi đã biết; hoặc
    - chấp nhận sửa chữa lớn mà không kiểm thử lại dù việc kiểm thử lại khả thi; và
  - khi hệ thống được chứng nhận và sự thật hỗ trợ, các vấn đề phân loại tương tự cũng có thể góp phần vào kết luận bất lợi về quỹ đạo tại [Chương Chín](core_08_standing_assessment.md).

Hậu quả của các khiếm khuyết này được quy định tại [§7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="21-how-system-class-scales-every-evaluation"></a>

#### 2.1 Lớp Hệ thống Điều chỉnh Mọi Đánh giá như thế nào

Lớp hệ thống xác định độ sâu của mọi đánh giá trong chương này — các yếu tố toàn hệ thống tại [§3 Đánh giá Chứng nhận Toàn hệ thống](#3-whole-system-certification-evaluation), việc xử lý dữ liệu tại [§3.4 Đánh giá Loại và Xử lý Dữ liệu](#34-data-types-and-handling-evaluation), và từng đánh giá Sàn Quyền cùng từng lĩnh vực tại [§5 Đánh giá Sàn Quyền và Lĩnh vực](#5-rights-floor-and-domain-evaluations) — cũng như tần suất lặp lại:

- Hệ thống lớp cao hơn cần chứng cứ mạnh hơn và tương xứng để cho thấy từng đánh giá áp dụng đã thực sự được tiến hành, chứ không chỉ được tuyên bố.
- Lớp hệ thống thấp hơn vẫn cần đánh giá trung thực và tương xứng ở mọi nơi có yếu tố kích hoạt.
- Lớp hệ thống không bao giờ cho phép bỏ qua đánh giá bắt buộc. Hệ thống có vai trò thực tế vượt quá lớp của mình phải được phân loại lại và đánh giá lại ở độ sâu cao hơn theo [§9 Chứng nhận lại và Mở lại](../../core_09.010_system_alignment_certification_record_process.md#9-recertification-and-reopening).
- Lớp hệ thống quyết định độ sâu rà soát. Nó không bao giờ cho phép chỉ dựa vào chứng chỉ, nhãn hoặc điều chỉnh chỉ tồn tại trên giấy, hay chấp nhận đánh giá và quyết định mà không ai có thể thấy căn cứ.

Các yêu cầu về sự tham gia và tính tương xứng được điều chỉnh tương tự:

- Hệ thống **Lớp A** cần những đường tham gia khả thi mạnh nhất, vì sai sót có thể chặn các nhu cầu sinh tồn thiết yếu trước khi có thể khắc phục. Các đường này gồm:
  - cơ chế phản đối dễ tiếp cận;
  - rà soát của bên liên quan; và
  - kết luận của họ diễn đàn được giao phụ trách lợi hại bị ảnh hưởng theo [Phần B §6.1 Giám sát Diễn đàn và Vai trò các Cấu phần](../../core_09.010_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles), bao gồm diễn đàn Thể chế hoặc diễn đàn Hữu tri như phần đó yêu cầu.
- Hệ thống **Lớp B** cần sự tham gia vững chắc khi hệ thống kiểm soát:
  - chăm sóc sức khỏe;
  - giáo dục;
  - trợ cấp;
  - việc làm; hoặc
  - đời sống hằng ngày tương đương.
- Hệ thống **Lớp C** vẫn cần hồ sơ có thể phản đối và công bố tương xứng, nhất là khi tác động phối hợp:
  - tạo gánh nặng cho nhóm được bảo vệ;
  - tập trung sự phụ thuộc; hoặc
  - báo hiệu khả năng nâng lên Lớp B hoặc Lớp A.

<a id="22-pilot-certification"></a>

#### 2.2 Chứng nhận Thí điểm

**[Thí điểm](../../core_05.040_band_continuity.md#pilot)** là một lần [đưa vào hoạt động](../../core_05.040_band_continuity.md#go-live), vì vậy cần chứng nhận riêng trước khi bắt đầu theo quy tắc đưa vào hoạt động tại [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes).

- Hệ thống ở bất kỳ lớp nào đều được kỳ vọng chạy thí điểm trước khi triển khai đầy đủ; hệ thống không làm vậy phải ghi lại lý do.
- Thí điểm vẫn cần phân loại trung thực và mọi đánh giá có yếu tố kích hoạt áp dụng; phạm vi, nhóm người tham gia và thời hạn phải được nêu trong hồ sơ.
- Thí điểm được đánh giá trong hồ sơ riêng, với độ sâu tùy theo lớp hệ thống và mức độ có thể thay thế: có phương án thay thế khả thi cho những hữu tri sẽ bị ảnh hưởng hoặc phụ thuộc vào hệ thống hay không, và phương án đó gây chi phí, chậm trễ, mất chức năng ở mức nào (xem [Phụ thuộc](../../core_05.040_band_continuity.md#dependency)).
  - Hệ thống càng dễ thay thế và lớp càng thấp thì đánh giá thí điểm có thể càng nhẹ.
  - Thí điểm của hệ thống khó thay thế phải được đánh giá ở độ sâu mà lớp hệ thống yêu cầu khi triển khai đầy đủ.

<a id="3-whole-system-certification-evaluation"></a>

### 3. Đánh giá chứng nhận toàn hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Truy nguyên</span></strong></summary>

- Thượng nguồn: [Chương Một §12 Yêu cầu đánh giá hệ thống](core_01_a_values_principles.md#12-systemic-evaluation-requirement); họ đo lường Hưng thịnh (*phúc lợi, an toàn, tổn hại và khả năng tiếp cận sàn sinh tồn*); họ đo lường Hiệu năng Hiến pháp (*Hiệu suất Hiến pháp, Gánh nặng có thể tránh, và Năng lực sản xuất*); [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [§1 Mục đích và Vai trò](#1-purpose-and-role).
- Hạ nguồn: [Các hướng dẫn toàn hệ thống ở Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) (*hướng dẫn toàn hệ thống mang tính minh họa*); từ [§3.4](#34-data-types-and-handling-evaluation) đến [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*đánh giá theo lĩnh vực*); [hồ sơ lớp hệ thống ở Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive) (*hồ sơ lớp hệ thống minh họa*); [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §6](../../core_09.010_system_alignment_certification_record_process.md#6-forum-process) (*chuỗi khả năng tranh biện*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*mở lại và chống né tránh*).
- Đọc cùng: [Chương Một §16](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth), [§18](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), và [§19](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture); [Chương Một §7.4 Chấm dứt tự nguyện, Tự sửa đổi lớn và Quyền rời đi](core_01_a_values_principles.md#74-voluntary-discontinuation-and-exit-rights); [Chương Một §7.2 Tập hợp, Tổ chức tập thể và Hình thành thể chế](core_01_a_values_principles.md#72-assembly-collective-organization-and-institutional-formation); **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh độc lập*) khi các Sàn Quyền về kiểm toán, minh bạch hoặc xác minh độc lập có lợi hại vật chất; họ đo lường Liên tục ([§3.1](#31-systemic-scope-and-risk-factors) — khả năng phục hồi, đảo ngược và rủi ro hệ thống); [Đánh giá rủi ro](../../core_05.040_band_continuity.md#risk-evaluation); [Công bố rủi ro](core_05_band_oversight.md#risk-disclosure); [Công bố đường cơ sở giám sát công khai](core_05_band_oversight.md#public-oversight-baseline-disclosure); họ đo lường Tham gia ([§4.1](#41-privacy-informational-joint-invocation) — quyền riêng tư và quản trị dữ liệu); họ đo lường Trách nhiệm giải trình ([§3.3](#33-governance-incentive-and-contestability-discipline) — điều chỉnh động cơ và khả năng tranh biện thị trường); [Ranh giới hệ thống](../../core_05.040_band_continuity.md#system-boundaries); [Hiến chương](../../core_05.040_band_continuity.md).
- Các tiểu mục: [§3.1](#31-systemic-scope-and-risk-factors) đến [§3.4](#34-data-types-and-handling-evaluation) (*luôn áp dụng: yếu tố hệ thống, chân trời thời gian, quản trị, và loại dữ liệu cùng cách xử lý*). Giai đoạn II tiếp tục ở [§4 Đánh giá khi có liên quan](#4-evaluations-where-implicated) (*khi có liên quan: các điểm quyền riêng tư, quyền rời đi, tập hợp và bất đồng*) và [§5 Đánh giá Sàn Quyền và lĩnh vực](#5-rights-floor-and-domain-evaluations) (*khi được kích hoạt*).

</details>

<br>

*Nói thẳng: không thể bật đèn xanh cho một phần của hệ thống rồi bỏ qua phần còn lại. Người đánh giá cần thấy toàn cảnh — hệ thống phụ thuộc vào điều gì, điều gì hỏng khi một thứ ở thượng nguồn thất bại, tổn hại xuất hiện muộn hoặc tích tụ theo thời gian, hữu tri có thể thực sự sử dụng nó chứ không chỉ trên giấy tờ hay không, thông tin riêng tư có được tách biệt đúng cách không, hữu tri có thể rời đi mà không bị mắc kẹt không, các nhóm có thể tiếp tục tổ chức mà hệ thống không chia rẽ họ không, lợi ích ngắn hạn có che giấu tổn hại dài hạn không, và giám sát cùng trách nhiệm giải trình thực chất có còn vận hành khi lợi hại lớn hay không.*

*Ví dụ minh họa: [Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) cho thấy mục này vận hành trong thực tế ra sao. Phần này lấy ba hệ thống mẫu, mỗi lớp hệ thống một ví dụ, rồi đi qua các bước kiểm tra ở trên.*

Đánh giá chứng nhận điều chỉnh hệ thống sẽ không đầy đủ nếu chỉ xem xét tác động tức thời hoặc cục bộ; đánh giá toàn hệ thống (Giai đoạn II), nhằm khắc phục thiếu sót đó, gồm ba tầng được trình bày riêng trong từng mục và liệt kê trong bảng dưới đây. Mục này quy định tầng thứ nhất, **IIa**; [§4 Đánh giá khi có liên quan](#4-evaluations-where-implicated) quy định **IIb** và [§5 Đánh giá Sàn Quyền và lĩnh vực](#5-rights-floor-and-domain-evaluations) quy định **IIc**. Bảng giúp định hướng người đọc; bảng không bổ sung, thu hẹp hoặc sắp xếp lại yêu cầu của bất kỳ mục hay tiểu mục nào.

| Tầng | Phân giai đoạn | Các mục | Áp dụng |
|------|----------------|---------|---------|
| **Luôn áp dụng** | IIa | [§3.1 Phạm vi hệ thống và yếu tố rủi ro](#31-systemic-scope-and-risk-factors); [§3.2 Ràng buộc nhất quán theo thời gian](#32-time-consistency-constraint); [§3.3 Kỷ luật quản trị, động cơ và khả năng tranh biện](#33-governance-incentive-and-contestability-discipline); [§3.4 Đánh giá loại dữ liệu và cách xử lý](#34-data-types-and-handling-evaluation) | mọi hồ sơ chứng nhận có tác động vật chất |
| **Khi có liên quan** | IIb | [§4.1 Kết hợp viện dẫn quyền riêng tư (thông tin)](#41-privacy-informational-joint-invocation); [§4.2 Chấm dứt tự nguyện, Tự sửa đổi lớn và Quyền rời đi](#42-voluntary-discontinuation-major-self-modification-and-exit-rights); [§4.3 Tập hợp, Tổ chức tập thể và Hình thành thể chế](#43-assembly-collective-organization-and-institutional-formation), bao gồm [§4.3.1](#431-dissent-and-peaceful-protest) | khi vấn đề chứng nhận có tác động vật chất đến điểm hoặc nguyên tắc mà tiểu mục nêu tên |
| **Khi được kích hoạt** | IIc | [§5 Đánh giá Sàn Quyền và lĩnh vực](#5-rights-floor-and-domain-evaluations) | khi đáp ứng một điều kiện kích hoạt trong bảng §5 |

Hồ sơ chứng nhận phải cho thấy rằng việc đánh giá đã xem xét các yếu tố dưới đây ở mọi nơi chúng có ý nghĩa vật chất đối với:

- chứng nhận;
- xác nhận;
- tái chứng nhận;
- tiếp tục dựa vào hệ thống;
- triển khai; hoặc
- dỡ bỏ điều kiện gắn với chứng nhận.

Việc đánh giá cũng phải xác nhận rằng [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad) sẽ được điều chỉnh theo [lợi hại vật chất](core_00_preamble.md#material-stake) của hệ thống đang được xem xét.

<a id="31-systemic-scope-and-risk-factors"></a>
#### 3.1 Phạm vi hệ thống và yếu tố rủi ro

Đánh giá chứng nhận phải xem xét:

- **quan hệ phụ thuộc và tác động dây chuyền** — điều gì ở hạ nguồn thất bại khi một thứ ở thượng nguồn hỏng;
- **tác động tổng hợp và quy mô** — điều gì thay đổi khi nhiều hành động nhỏ kết hợp;
- **tác động trì hoãn, tích lũy và xác suất** — tổn hại xuất hiện muộn, chồng chất hoặc phụ thuộc vào may rủi;
- **điều kiện đối kháng và khả năng bị lạm dụng** — tác nhân xấu hoặc hành vi lạm dụng có thể dự đoán sẽ khai thác hệ thống như thế nào;
- **phạm vi theo Hiến chương so với ranh giới chức năng** — [Hiến chương](../../core_05.040_band_continuity.md) điều chỉnh, nếu có hoặc được yêu cầu, có khớp với [Ranh giới hệ thống](../../core_05.040_band_continuity.md#system-boundaries) quan sát được không, và phạm vi đã nêu có đánh giá thấp tác động vật chất hoặc sự phụ thuộc không;
- **năng lực phục hồi sinh thái** — hệ thống có thể làm tổn hại [Năng lực Phục hồi Sinh thái](../../core_05.040_band_continuity.md#ecological-recovery-capacity) của bất kỳ hệ sinh thái tự nhiên nào, ở bất kỳ quy mô nào, đến mức hệ sinh thái đó không thể tái sinh sau tổn hại hay không;
- **rủi ro tồn vong** — kết quả có thể đe dọa sự sống còn của hữu tri ở quy mô văn minh.

**Cầu nối giữa đánh giá và công bố rủi ro.** Khi [Rủi ro](../../core_05.040_band_continuity.md#risk) hệ thống thuộc phạm vi theo các yếu tố trên, chứng nhận phải xác minh cả hai nửa của cặp quy định ở Chương Năm — không tự tạo thêm một loại hồ sơ công bố rủi ro có tên riêng:

- **[Đánh giá rủi ro](../../core_05.040_band_continuity.md#risk-evaluation)** — rủi ro hệ thống có thực sự được đánh giá trong các điều kiện quan trọng (phụ thuộc, chân trời thời gian và [Điều kiện đối kháng, mở rộng quy mô và bị khai thác](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions)), với quy mô phù hợp với lớp hệ thống và [lợi hại vật chất](core_00_preamble.md#material-stake) hay không; và
- **[Công bố rủi ro](core_05_band_oversight.md#risk-disclosure)** — rủi ro đã đánh giá có đến với những hữu tri cần biết đúng lúc để hiểu, phản biện và hành động hay không.

Chỉ thực hiện một trong hai việc sẽ không đạt:

- rủi ro đã đánh giá nhưng không bao giờ được chia sẻ không đạt; và
- rủi ro đã chia sẻ nhưng chưa được đánh giá đúng cách cũng không đạt.

**Khiếm khuyết và lệch điều chỉnh.** Các trường hợp sau phải được coi là khiếm khuyết chứng nhận:

- coi ghi chú nội bộ, phụ lục bị chôn sâu, danh sách kiểm tra hoặc tuyên bố sau sự việc là việc đánh giá hoặc công bố;
- không công bố rủi ro hệ thống đã đánh giá cho những bên cần biết khi [Tính minh bạch](core_05_band_oversight.md#transparency) hoặc [An toàn (Ràng buộc Hiến pháp)](../../core_05.040_band_continuity.md#safety-constitutional-constraint) yêu cầu; hoặc
- chấp thuận tiếp tục dựa vào hệ thống trong khi các rủi ro đã biết vẫn chưa được ghi chép, công bố và xử lý.

Hệ quả được quy định tại [§7 Kết quả chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="32-time-consistency-constraint"></a>
#### 3.2 Ràng buộc nhất quán theo thời gian

Chứng nhận không được coi các chỉ số ngắn hạn, tuân thủ cục bộ hoặc hiệu suất trong chân trời ngắn là đủ khi các vi phạm trung hạn hoặc dài hạn có thể dự đoán vẫn chưa được xử lý. Tối ưu hóa chân trời ngắn là không hợp lệ nếu có thể dự đoán rằng nó sẽ gây ra vi phạm các ràng buộc về **An toàn**, **Sự thật** hoặc **phúc lợi** trong trung hạn hoặc dài hạn, theo các điều kiện tích lũy, trì hoãn hoặc liên hệ giữa các hệ thống.

<a id="33-governance-incentive-and-contestability-discipline"></a>
#### 3.3 Kỷ luật quản trị, động cơ và khả năng tranh biện

*Nói thẳng: việc xem xét chưa hoàn tất nếu người đánh giá không hỏi liệu bốn trụ của [Tứ diện](core_00_preamble.md#constitutional-tetrad) có còn đứng vững ở mức rủi ro liên quan hay không — tham gia (hữu tri có thể thực sự tham gia không), giám sát (công việc có thể được theo dõi và kiểm tra không), trách nhiệm giải trình (có thể buộc người làm sai trả lời không), và kịp thời (quyết định có đủ nhanh khi cần không). Người đánh giá cũng cần biết ai thực sự nắm quyền hạn vật chất và ai chịu trách nhiệm về việc gì — không thể dùng câu “cả nhóm” mơ hồ hay một vỏ bọc để đổ lỗi. Chứng nhận hợp lệ phải trả lời các câu hỏi đó.*

Đánh giá chứng nhận không đầy đủ nếu không đánh giá liệu **giám sát**, **trách nhiệm giải trình**, **tham gia** và **kịp thời** có được điều chỉnh theo [lợi hại vật chất](core_00_preamble.md#material-stake) của hệ thống đang xem xét hay không. Đánh giá đó phải bao gồm việc các vai trò quản trị có trách nhiệm, quản trị và giải trình vật chất có được **phân công chính thức, ghi chép và truy nguyên** đủ mức để việc yêu cầu trả lời và các lộ trình tranh biện thực tế vận hành hay không — được điều chỉnh theo lớp hệ thống và tác động vật chất theo **[corpus_systems.md](../../corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**.

Để thực hiện kỷ luật này, chứng nhận phải đọc:

- **[Chương Một §16 Quản trị có trách nhiệm chuyên sâu](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth)** — hiểu biết phân tán, minh bạch, khả năng kiểm toán và khả năng quan sát có thể tranh biện;
- **[Chương Một §18 Quản trị theo kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline)** — quản trị được ủy quyền và trách nhiệm trả lời theo kỷ luật quản trị có trách nhiệm;
- **[Chương Một §19 Điều chỉnh động cơ và chiếm dụng hệ thống](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture)** — điều chỉnh động cơ, tính toàn vẹn của đại diện, sửa khiếm khuyết ngắn hạn và ứng phó chiếm dụng;
- **[Chương Một §19.1.4 Đường dẫn chiều sâu vai trò và trách nhiệm vật chất](core_01_c_stewardship_capacity_principles.md#1914-role-depth-and-material-responsibility-pathways)** — đường dẫn vai trò có hệ quả và kỷ luật chống tham gia hình thức;
- **[Chương Mười Ba §5 Vai trò được ủy quyền, Phát triển năng lực và Đóng góp](core_12_governance.md#5-authorized-roles-competency-development-and-contribution)** và **[corpus_systems.md](../../corpus_systems.md), CS-4 — Quản trị có trách nhiệm đối với hệ thống trọng yếu** — các sàn về định nghĩa vai trò, năng lực và truy nguyên trong vận hành, khi có ý nghĩa vật chất;
- **[Điều XVI: Kiểm toán, Minh bạch và Xác minh độc lập](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)** khi các Sàn Quyền về kiểm toán, minh bạch hoặc xác minh độc lập có lợi hại vật chất.

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 Đánh giá loại dữ liệu và cách xử lý

<details>
<summary><strong><span style="color: #2563eb;">Truy nguyên</span></strong></summary>

- Thượng nguồn: [§3](#3-whole-system-certification-evaluation) (*các yếu tố đánh giá toàn hệ thống*); [các hướng dẫn toàn hệ thống ở Phần C](../../core_09.015_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) (*hướng dẫn toàn hệ thống mang tính minh họa*); [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); họ đo lường Giám sát (*Sự thật và tính toàn vẹn nhận thức như phép đo hiến pháp*); [Điều XV: Tính toàn vẹn của không gian thông tin](core_06_rights_part_c.md#article-xv-info-sphere-integrity); [Điều XVI: Kiểm toán, Minh bạch và Xác minh độc lập](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification); [Điều VII: Quyền tự sở hữu](core_06_rights_part_b.md#article-vii-self-ownership).
- Hạ nguồn: [§3.4.8](../../core_09.015_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*hướng dẫn xử lý dữ liệu minh họa*); [§5.1](#51-ecological-footprint-evaluation) và [§5.1.5](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*đánh giá dấu chân sinh thái và hướng dẫn minh họa*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*phân loại lại và lệch điều chỉnh trong xử lý*).
- Đọc cùng: [corpus_systems.md](../../corpus_systems.md), **CS-2 — Loại dữ liệu và cách xử lý** (bao gồm **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Phân loại lại và quản trị vòng đời*) và **[CS-2 §8](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*Quản trị Hồ sơ Loại Dữ liệu Hệ thống*)); [Hồ sơ Loại Dữ liệu Hệ thống](../../core_05.040_band_continuity.md#system-data-types-record); [Công bố đường cơ sở giám sát công khai](core_05_band_oversight.md#public-oversight-baseline-disclosure); **CJS-3.18** (*thuật ngữ về lưu giữ dữ liệu và tính toàn vẹn vòng đời*), **CJS-3.21** (*thuật ngữ về khả năng chống đối kháng và chống lạm dụng*), và **CJS-3.17** (*thuật ngữ về khả năng tương tác, tính di chuyển và tính toàn vẹn khi rời đi*) khi có ý nghĩa vật chất; [§4.1 Kết hợp viện dẫn quyền riêng tư (thông tin)](#41-privacy-informational-joint-invocation) khi có điểm quyền riêng tư liên quan.
- Các tiểu mục: [§3.4.1](#341-type-o-baseline-disclosure) (*Công bố đường cơ sở Type O*); [§3.4.2](#342-privacy-discipline) (*kỷ luật quyền riêng tư*); [§3.4.3](#343-protective-storage-and-key-custody) (*lưu trữ bảo vệ và quản lý khóa*); [§3.4.4](#344-periodic-data-type-re-evaluation) (*đánh giá lại định kỳ loại dữ liệu*); [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*bảo đảm hạ tầng theo lớp hệ thống*); [§3.4.6](#346-infrastructure-robustness-for-data) (*độ vững của hạ tầng dữ liệu*); [§3.4.7](#347-defects-and-misalignment) (*khiếm khuyết và lệch điều chỉnh*); [§3.4.8](../../core_09.015_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*áp dụng xử lý dữ liệu minh họa theo lớp hệ thống*).

</details>

<br>

*Nói thẳng: chứng nhận cũng phải xem hệ thống chạm đến những loại dữ liệu nào và chúng được xử lý thích hợp hay không — bao gồm việc loại dữ liệu còn phù hợp trong chu kỳ xem xét hiện tại không và hạ tầng nền có đủ vững để bảo vệ dữ liệu ở lớp hệ thống đó không. Quy tắc loại dữ liệu và Hồ sơ Loại Dữ liệu Hệ thống nằm trong corpus hệ thống; chứng nhận kiểm tra xem các quy tắc đã thực sự được áp dụng và hồ sơ có trung thực hay không.*

Chứng nhận điều chỉnh hệ thống phải đánh giá **loại dữ liệu và cách xử lý** như một phần của mọi hồ sơ chứng nhận có tác động vật chất. Mục này nêu điều chứng nhận phải xác minh. Phân loại loại dữ liệu và cơ chế xử lý nằm trong **[corpus_systems.md](../../corpus_systems.md), CS-2 — Loại dữ liệu và cách xử lý**, cùng với:

- định nghĩa loại thông tin chính thức;
- quy tắc xử lý và yêu cầu phân tách;
- chi tiết vòng đời; và
- [Hồ sơ Loại Dữ liệu Hệ thống](../../core_05.040_band_continuity.md#system-data-types-record) có tính bền vững.

**Yêu cầu đánh giá.** Quy trình chứng nhận phải xác định liệu hệ thống có:

- nhận diện các loại dữ liệu thuộc phạm vi có ý nghĩa vật chất; và
- xử lý chúng theo phân loại **nghiêm ngặt nhất có thể áp dụng**, bao gồm qua chuyển đổi, tổng hợp, ủy quyền, lưu trữ, lưu giữ và liên kết xuyên miền.

Đánh giá phải phản ánh hiệu lực chức năng, không chỉ dựa vào nhãn, định dạng hoặc riêng giai đoạn trong quy trình dữ liệu.

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Công bố đường cơ sở Type O

Khi **[đường cơ sở Type O tại CS-2 Phần A §7](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)** áp dụng, chứng nhận cũng phải xác minh rằng [Công bố đường cơ sở giám sát công khai](core_05_band_oversight.md#public-oversight-baseline-disclosure) (**Type O**) đã công bố bao quát **phạm vi được chứng nhận**, được xác định từ:

- [Hiến chương](../../core_05.040_band_continuity.md) điều chỉnh (hoặc công cụ phạm vi tương đương được công bố);
- lớp hệ thống được giao; và
- [Ranh giới hệ thống](../../core_05.040_band_continuity.md#system-boundaries) quan sát được.

Khi có rủi ro hệ thống, việc chia sẻ rủi ro đã được đánh giá cũng có thể được tính vào đường cơ sở này. Quyền đường cơ sở của công chúng rộng hơn chứng nhận và không đòi hỏi một hồ sơ riêng bên cạnh [Hồ sơ Phân loại Hệ thống](../../core_05.040_band_continuity.md#system-classification-record) hoặc [Hồ sơ Loại Dữ liệu Hệ thống](../../core_05.040_band_continuity.md#system-data-types-record).

Mỗi trường hợp giữ lại thông tin có lý do chính đáng phải đi kèm phương án thay thế công khai mạnh nhất có thể thực hiện hợp lý ([§3.4.5 Bảo đảm hạ tầng theo lớp hệ thống](#345-system-class-scaled-infrastructure-assurance) nêu ví dụ). Chương Năm quản lý thuật ngữ; CS-2 (*Loại dữ liệu và cách xử lý*) quản lý nội dung đường cơ sở và cơ chế công bố.

<a id="342-privacy-discipline"></a>
##### 3.4.2 Kỷ luật quyền riêng tư

Chứng nhận phải áp dụng kỷ luật quyền riêng tư sau đây đối với việc xử lý dữ liệu:

- *Các loại H, I, N, S và Y.* Với dữ liệu **Loại H**, **Loại I**, **Loại N**, **Loại S** và **Loại Y**, chứng nhận phải xác minh cách xử lý đáp ứng các [điểm quyền riêng tư](../../corpus_systems/cs_06.310_data_classifications.md#privacy-link) mà từng loại nêu trong **CS-2** (*Loại dữ liệu và cách xử lý*), bao gồm [Tính cần thiết](../../core_05.035_band_accountability.md#necessity), [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality), giảm thiểu dữ liệu, và sự đồng thuận hoặc thẩm quyền đầy đủ khác.
- *Kết hợp viện dẫn.* Khi có hơn một điểm quyền riêng tư liên quan, [§4.1 Kết hợp viện dẫn quyền riêng tư (thông tin)](#41-privacy-informational-joint-invocation) cũng áp dụng.
- *Chỉ có nhãn là chưa đủ.* Nhãn loại chính xác tự nó không chứng minh tuân thủ quyền riêng tư.
- *Các loại W, U và T.* Với tác phẩm **Loại W**, **Loại U** và **Loại T**, chứng nhận phải xác minh quyền kiểm soát của người sáng tạo được tôn trọng, bao gồm:
  - rút lại việc công bố công khai theo [CS-2 Phần B §9.9](../../corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Loại W: Tác phẩm đã công bố*);
  - giới hạn của từng cấp phép được ghi nhận theo [CS-2 Phần B §9.13](../../corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*Cấp phép thương mại*); và
  - [các quyền bảo lưu](../../corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) của người sáng tạo.
- *Không suy diễn sự đồng thuận.* Không cấp phép nào được coi là sự đồng thuận cho một cách sử dụng mà nó không nêu tên.

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 Lưu trữ bảo vệ và quản lý khóa

Đối với dữ liệu thuộc dải mặc định hạn chế và không thể truy cập, chứng nhận phải xác minh hệ thống đáp ứng sàn về lưu trữ bảo vệ và quản lý khóa tại [CS-2 Phần A §5.0 Các dải tư thế truy cập](../../corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). Hồ sơ phải cho thấy:
- dữ liệu bị hạn chế và khóa của nó thực sự nằm ở đâu, bao gồm bản sao lưu, bộ nhớ đệm, nhật ký và vùng hoán đổi;
- văn bản thuần chỉ giới hạn trong các tiến trình cần đến nó; và
- các lộ trình kiểm toán, xuất dữ liệu và ghi đè hợp pháp vẫn hoạt động.

Chỉ tuyên bố có mã hóa mà không có bằng chứng đó thì không đáp ứng bước kiểm tra này.

<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 Đánh giá lại định kỳ loại dữ liệu

Trong mỗi chu kỳ chứng nhận hoặc tái chứng nhận có tác động vật chất, quy trình phải xác minh rằng các tập dữ liệu vật chất thuộc phạm vi đã được:

- **đánh giá lại định kỳ** về phân loại phù hợp theo **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Phân loại lại và quản trị vòng đời*) và **CJS-3.18** (*thuật ngữ về lưu giữ dữ liệu và tính toàn vẹn vòng đời*); và
- **phân loại lại** ở nơi việc xem xét đó yêu cầu.

Tần suất phải tương ứng với lớp hệ thống và tác động vật chất theo [§2 Đánh giá lớp hệ thống](#2-system-class-evaluation). Việc đổi loại do sự kiện theo CS-2 (*Loại dữ liệu và cách xử lý*) không thay thế kiểm tra chứng nhận định kỳ này.

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 Bảo đảm hạ tầng theo lớp hệ thống

Theo [§2.1 Cách lớp hệ thống điều chỉnh mọi đánh giá](#21-how-system-class-scales-every-evaluation) và CS-3 (*Cơ chế phân loại hệ thống*), hệ thống lớp cao hơn cần bằng chứng mạnh hơn tương ứng rằng hạ tầng xử lý, lưu trữ, xử lý tính toán, truyền tải, sao lưu, phục hồi và giám sát có thể duy trì những điều sau trong điều kiện căng thẳng:

- tính toàn vẹn phân loại;
- quy thuộc; và
- khả năng tranh biện.

Khi các mặc định về khả năng nhìn thấy vì lợi ích công cộng trong CS-2 (*Loại dữ liệu và cách xử lý*) áp dụng, chứng nhận phải xác minh các hạn chế:

- có phạm vi hẹp;
- được ghi chép và có thể kiểm toán; và
- đi kèm phương án thay thế công khai mạnh nhất có thể thực hiện hợp lý (ví dụ: bản tóm tắt, dữ liệu tổng hợp, phiên bản đã khử định danh, công bố trễ hoặc quyền tiếp cận kiểm toán có điều kiện), để giải thích nội dung bị giữ lại thay vì chỉ che giấu.

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 Độ vững của hạ tầng dữ liệu

Chứng nhận phải đánh giá liệu hạ tầng xử lý dữ liệu có phù hợp với các loại dữ liệu và lớp hệ thống liên quan hay không. Hạ tầng đó bao gồm:

- các lớp lưu giữ và quy trình dữ liệu;
- kiểm soát truy cập;
- ranh giới mã hóa hoặc cô lập;
- đường dẫn sao lưu và khôi phục; và
- chuỗi ủy quyền cho người vận hành hoặc nhà cung cấp.

Các thiếu hụt vật chất về tính toàn vẹn vòng đời, khả năng chống đối kháng, tính di chuyển hoặc khả năng khôi phục phải được nêu trong hồ sơ và phản ánh trong kết quả chứng nhận, điều kiện hoặc giới hạn dựa vào hệ thống.

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 Khiếm khuyết và lệch điều chỉnh

Mỗi điều sau đây phải được coi là khiếm khuyết chứng nhận:

- phân loại sai dữ liệu;
- tái cấu trúc nhằm né tránh;
- liên kết xuyên miền không an toàn;
- cách xử lý phù hợp với nhãn loại nhưng không đáp ứng các điểm quyền riêng tư mà loại đó nêu;
- thiếu quy thuộc khi không thể điều tra tổn hại vật chất;
- **đánh giá lại định kỳ loại dữ liệu bị quá hạn hoặc bị bỏ qua**;
- dữ liệu bị hạn chế được lưu dưới dạng văn bản thuần trong bộ nhớ lưu trữ hoặc vượt ngoài ranh giới xử lý được phép, hoặc khóa có thể bị truy cập bởi tiến trình không cần đến chúng; và
- hạ tầng mong manh có thể dự đoán sẽ làm vô hiệu các biện pháp bảo vệ của CS-2 (*Loại dữ liệu và cách xử lý*).

Hệ quả được quy định tại [§7 Kết quả chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes).


<a id="4-evaluations-where-implicated"></a>

### 4. Đánh giá khi có liên quan

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [§3](#3-whole-system-certification-evaluation) (*đánh giá toàn hệ thống, bao gồm cấp luôn áp dụng*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); [Chương Một §12 Yêu cầu Đánh giá Hệ thống](core_01_a_values_principles.md#12-systemic-evaluation-requirement).
- Hạ nguồn: [§4.1](#41-privacy-informational-joint-invocation) (*các điểm riêng tư*); [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights) (*quyền rời đi*); [§4.3](#43-assembly-collective-organization-and-institutional-formation) (*hội họp và bất đồng*); [Phần B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*nội dung hồ sơ*).
- Đọc cùng: [§5 Đánh giá Sàn Quyền và Lĩnh vực](#5-rights-floor-and-domain-evaluations) (*cấp áp dụng khi được kích hoạt*).

</details>

<br>

*Nói thẳng: có ba phép kiểm tra chỉ áp dụng khi hệ thống thực sự chạm đến các vấn đề đó—thông tin riêng tư có được ngăn cách đúng cách không, hữu tri có thể rời đi mà không bị mắc kẹt không, và các nhóm có còn tổ chức cũng như bất đồng được không. Nếu hệ thống chạm đến một trong những vấn đề này, chứng nhận phải xem xét vấn đề đó.*

Phần này là phân giai đoạn **IIb** của Giai đoạn II (Đánh giá). Phần này tập hợp các đánh giá toàn hệ thống áp dụng khi vấn đề chứng nhận tác động đáng kể đến điểm hoặc nguyên tắc được nêu trong một tiểu mục. Phần này không bổ sung, thu hẹp hay sắp xếp lại yêu cầu của bất kỳ tiểu mục nào.

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 Kích hoạt Đồng thời Quyền riêng tư (Thông tin)

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Đọc cùng: [**Def.C3** (*Quyền riêng tư (Thông tin)* — đầu cụm ngang hàng)](../../core_05.040_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) của Chương Năm và [Quyền riêng tư (Thông tin)](../../core_05.040_band_continuity.md#privacy-informational), nơi chủ đạo của cụm; các mục này xác định ý nghĩa.

</details>

<br>

*Nói thẳng: Chương Sáu phân bố các biện pháp bảo vệ quyền riêng tư trên nhiều điều khoản, chứ không gom vào một góc duy nhất. Nếu việc rà soát chứng nhận chạm đến nhiều biện pháp trong số đó, người rà soát phải kiểm tra từng biện pháp thực sự áp dụng. Đánh dấu vào ô dễ nhất rồi coi như xong là không đủ.*

Khi một vấn đề chứng nhận tác động đáng kể đến hơn một điểm quyền riêng tư của Chương Sáu, chứng nhận phải xử lý từng điểm đó. Chỉ khép lại vấn đề theo một điểm là không đủ.

- *Tạo điều kiện cho sự tham gia.* [Quyền riêng tư (Thông tin)](../../core_05.040_band_continuity.md#privacy-informational) tạo điều kiện cho [Sự tham gia](core_05_apex_participation_leg.md#participation-constitutional) thực chất. Chứng nhận phải xác nhận rằng các biện pháp bảo vệ quyền riêng tư hỗ trợ tiếng nói, thảo luận, liên kết và phản biện không bị vô hiệu hóa thông qua phân đoạn, suy diễn xuyên ngữ cảnh hoặc áp lực phơi lộ.
- *Các điểm trong cụm.* Phạm vi bảo vệ quyền riêng tư phân tán nằm tại **Điều VII-A** (*Quyền tự chủ thân thể*), **Điều VII-B** (*Quyền tự chủ tâm trí*), **Điều IX** (*Hình ảnh tương tự, Dữ liệu Trải nghiệm và Quyền Xuất bản*), **Điều X-A** (*Năng lực hành động và Tự do khỏi Thao túng*), và **Điều XIV-A** (*An ninh, Tình báo và Giới hạn Quyền lực Bí mật*).
- *Quy tắc kích hoạt đồng thời.* Khi vấn đề tác động đáng kể đến nhiều điểm, chứng nhận phải xem xét từng điểm và không được chuyển vấn đề qua một điểm theo cách cho phép né tránh điểm khác.
- *Không nới lỏng tiêu chuẩn bằng suy diễn xuyên ngữ cảnh.* Tiêu chuẩn được nêu riêng cho từng thành viên cụm chi phối trong phạm vi của thành viên đó; không được làm tiêu chuẩn ấy lỏng hơn bằng cách nhập tiêu chuẩn dễ hơn từ thành viên khác.
- *Giữ nguyên mức bảo vệ tối thiểu theo loại.* Yếu tố này không thu hẹp cách xử lý bất kỳ loại nào trong **[corpus_systems.md](../../corpus_systems.md), CS-2** (*Loại thông tin và cách xử lý*) áp dụng cho dữ liệu thuộc phạm vi. Tư thế truy cập và nghĩa vụ xử lý của từng loại áp dụng theo [CS-2 Phần B §9](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-9-data-classifications) (*Phân loại dữ liệu*) được áp dụng đầy đủ, cùng với [các căn cứ riêng tư](../../corpus_systems/cs_06.310_data_classifications.md#privacy-link) mà loại đó nêu. Khi nhiều loại cùng phù hợp với một dữ liệu, cách xử lý áp dụng có tính bảo vệ cao nhất chi phối theo [CS-2 Phần A §2](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-2-determination-of-classification); đáp ứng cách xử lý của một loại không miễn trừ nghĩa vụ của loại khác. Các điểm nêu trên áp dụng cho những loại sau:
  - **Điều VII-A** (*Quyền tự chủ thân thể*) — [**Loại I**](../../corpus_systems/cs_06.310_data_classifications.md#95-type-i-identity-and-attribution-data) đối với hồ sơ sức khỏe, sinh trắc học và gắn với nền tảng cơ thể;
  - **Điều VII-B** (*Quyền tự chủ tâm trí*) và **Điều X-A** (*Năng lực hành động và Tự do khỏi Thao túng*) — [**Loại N**](../../corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data) đối với trạng thái nội tại, bao gồm việc tái dựng hoặc suy luận chúng;
  - **Điều IX** (*Hình ảnh tương tự, Dữ liệu Trải nghiệm và Quyền Xuất bản*) — **Loại I** đối với hình ảnh tương tự và giọng nói theo [Điều IX-A](core_06_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*Quyền tự chủ đối với Hình ảnh tương tự và Danh tiếng*); [**Loại H**](../../corpus_systems/cs_06.310_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data) đối với dữ liệu trải nghiệm và dữ liệu phát sinh từ tương tác theo [Điều IX-B](core_06_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*Quyền đối với Dữ liệu Trải nghiệm và Dữ liệu Phái sinh*); và [**Loại Y**](../../corpus_systems/cs_06.310_data_classifications.md#98-type-y-yours) đối với tác phẩm của người sáng tạo theo [Điều IX-D](core_06_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Tác phẩm Sáng tạo, Sử dụng Dữ liệu Huấn luyện và Chống Thay thế*), với các biện pháp bảo vệ tiếp tục áp dụng cho [**Loại W**](../../corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published), [**Loại U**](../../corpus_systems/cs_06.310_data_classifications.md#911-type-u-use-licensed), và [**Loại T**](../../corpus_systems/cs_06.310_data_classifications.md#912-type-t-transferred), cùng với [các quyền được bảo lưu](../../corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) của người sáng tạo; và
  - **Điều XIV-A** (*An ninh, Tình báo và Giới hạn Quyền lực Bí mật*) — [**Loại S**](../../corpus_systems/cs_06.310_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data) đối với tài liệu điều tra và an ninh bị hạn chế; các thành phần **H**, **I** hoặc **N** trong đó vẫn giữ bảo vệ của loại tương ứng khi hạn chế chấm dứt.

  Các mức tối thiểu áp dụng theo cả hai chiều đối với loại dữ liệu mở và có thể tiếp cận để kiểm toán:
  - nội dung cá nhân, quan hệ hoặc trạng thái nội tại bên trong tài liệu **Loại E**, **Loại G** hoặc **Loại O** vẫn phải được xử lý theo **Loại H**, **Loại I** hoặc **Loại N** tương ứng;
  - một điểm quyền riêng tư tự nó không biện minh cho việc giữ lại dữ liệu **Loại O** hoặc **Loại E** vượt quá các trường hợp giữ lại hẹp mà quy tắc riêng của loại đó cho phép; và
  - khi việc bảo vệ quyền riêng tư của một người thực sự xung đột với việc công bố thông tin mà công chúng có quyền nhận, không bên nào tự động thắng: xung đột phải được quyết định công khai và ghi vào hồ sơ theo [CS-2 Phần A §7](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems) (*Chuẩn nền Loại O cho hệ thống Hạng A/B/C*).
- *Bằng chứng về loại dữ liệu.* Đối với từng điểm quyền riêng tư được xem xét, chứng nhận phải sử dụng [Hồ sơ Loại Dữ liệu Hệ thống](../../core_05.040_band_continuity.md#system-data-types-record), đã được xác minh theo [§3.4 Đánh giá Loại và Cách xử lý Dữ liệu](#34-data-types-and-handling-evaluation), làm bằng chứng về các loại thuộc phạm vi cùng mục đích, người nhận, căn cứ và dữ liệu phái sinh. Không thể khép lại một điểm quyền riêng tư dựa trên cách xử lý mà hồ sơ không thể hiện.

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 Tự nguyện Chấm dứt, Tự sửa đổi Lớn và Quyền Rời đi

Khi [Chương Một §7.4 Tự nguyện Chấm dứt, Tự sửa đổi Lớn và Quyền Rời đi](core_01_a_values_principles.md#74-voluntary-discontinuation-and-exit-rights) áp dụng cho vấn đề chứng nhận, trước khi chấp nhận tuyên bố chứng nhận, chứng nhận phải kiểm tra tính tự nguyện, sự đồng thuận, chống cưỡng ép, áp lực phụ thuộc, thông tin và khả năng đảo ngược. Chỉ có sự chấp thuận hình thức là chưa đủ.

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 Hội họp, Tổ chức Tập thể và Thành lập Thể chế

Khi [Chương Một §7.2 Hội họp, Tổ chức Tập thể và Thành lập Thể chế](core_01_a_values_principles.md#72-assembly-collective-organization-and-institutional-formation) áp dụng cho vấn đề chứng nhận, chứng nhận phải cùng xem xét vấn đề theo [Nguyên tắc Chống Phân đoạn](core_01_b_interaction_interpretation.md#1511-anti-segmentation-principle). Đánh giá chưa đầy đủ nếu chỉ đưa vấn đề qua một cách định khung khiến các biện pháp bảo vệ hội họp hoặc tổ chức tập thể mất hiệu lực.

<a id="431-dissent-and-peaceful-protest"></a>
##### 4.3.1 Bất đồng và Biểu tình Hòa bình

*Nói thẳng: không thể chứng nhận một hệ thống là phù hợp nếu hệ thống âm thầm trừng phạt những hữu tri bất đồng với nó. Người rà soát phải kiểm tra xem hữu tri có thể thực sự phản đối và biểu tình hay không, và liệu sự bất đồng có bị tính bất lợi cho họ ở bất kỳ đâu trong logic của hệ thống hay không—kể cả khi chính hệ thống là bên bất đồng.*

Khi [Chương Một §7.3 Bất đồng và Biểu tình Hòa bình](core_01_a_values_principles.md#73-dissent-and-peaceful-protest) áp dụng cho vấn đề chứng nhận, chứng nhận phải kiểm tra:
- liệu những hữu tri bị ảnh hưởng có thể thực sự bất đồng, biểu tình và tổ chức chống lại hệ thống cùng người vận hành thông qua các kênh do hệ thống kiểm soát, mà không bị lọc theo quan điểm hay không;
- liệu hồ sơ, điểm số, xếp hạng, kiểm duyệt, kiểm soát truy cập, logic đủ điều kiện hoặc cơ chế tương tự có sử dụng bất đồng, biểu tình hòa bình hoặc [bất tuân dân sự bất bạo động được bảo vệ](core_06_rights_part_b.md#xi-d-nonviolent-civil-disobedience) làm đầu vào bất lợi, trực tiếp hoặc thông qua biến đại diện, hay không;
- liệu các hành động bất lợi xảy ra sau bất đồng có căn cứ độc lập, được xác minh và ghi trong hồ sơ, theo yêu cầu về [gánh nặng của **Điều XI-D** (*Hội họp, Bất đồng và Biểu tình Hòa bình*)](core_06_rights_part_b.md#xi-d-dissent-burden-and-pretext), hay không; và
- nếu hệ thống là hoặc lưu trữ một hữu tri tổng hợp, liệu hữu tri đó có kênh phản đối hoạt động được hay không, và phản đối của nó có bị coi là lỗi hoặc bị đáp trả bằng cách sửa đổi giá trị, ký ức hay trạng thái nội tại của nó để trả đũa hay không.

Việc hệ thống tự bất đồng với người vận hành, được nêu qua các kênh hiện có, không phải là bằng chứng về sự không phù hợp cho mục đích chứng nhận. Hệ thống trừng phạt bất đồng được bảo vệ có lỗi chứng nhận. Coi bất đồng là tín hiệu rủi ro, hoặc khép lại vấn đề bằng tuyên bố hình thức về tính trung lập trong khi tác động bất lợi vẫn còn, là chưa đủ.


<a id="5-rights-floor-and-domain-evaluations"></a>

### 5. Đánh giá sàn quyền và các lĩnh vực

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [§1](#1-purpose-and-role) (*mục đích và vai trò*); [§2.1](#21-how-system-class-scales-every-evaluation) (*phân cấp đánh giá theo lớp hệ thống*); các Sàn quyền của Chương Sáu — **Điều I-B** (*Dấu chân sinh thái và Minh bạch*), **Điều III-A** (*Sinh tồn*), **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*), **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*), **Điều V** (*Phân bổ tài nguyên, Sự phụ thuộc và Tài trợ hệ sinh thái*), **Điều VI-C** (*Không phân biệt đối xử*), **Điều VI-D** (*Khả năng tiếp cận*), **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*) và **Điều XIII-A** (*Nền tảng độ tin cậy và khả tín*).
- Hạ nguồn: [Phần B §8.1](../../core_09.010_system_alignment_certification_record_process.md#81-minimum-record-contents) (*nội dung hồ sơ*); [Phần B §6.1](../../core_09.010_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) (*vai trò các thành phần diễn đàn*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*kết quả và mở lại*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*).
- Các tiểu mục: [§5.1](#51-ecological-footprint-evaluation) (*dấu chân sinh thái*); [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) (*năng lực giáo dục*); [§5.3](#53-proportionate-cross-system-support-evaluation) (*hỗ trợ liên hệ thống tương xứng*); [§5.4](#54-nondiscrimination-evaluation) (*không phân biệt đối xử*); [§5.5](#55-accessibility-evaluation) (*khả năng tiếp cận*); [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*độ tin cậy*).

</details>

<br>

*Nói đơn giản: một số hệ thống tác động lớn đến việc hữu tri có nhận được những bảo vệ cơ bản hay không — từ việc hạch toán trung thực gánh nặng môi trường, thực phẩm và nước, đến giáo dục, đối xử công bằng, tiếp cận thực chất, các hệ thống có thể tin cậy và phần đóng góp công bằng vào chi phí hạ tầng dùng chung. Khi có tác động như vậy, chứng nhận phải kiểm tra để việc phê chuẩn không âm thầm làm suy yếu các bảo vệ ấy; việc kiểm tra phải thực chất, không chỉ là ô mà người vận hành đánh dấu. Bảng cho biết mỗi cuộc kiểm tra bao quát bảo vệ nào, áp dụng khi nào và được đánh giá ở đâu.*

Phần này là tiểu giai đoạn **IIc** của Giai đoạn II (Đánh giá), sau [§3 Đánh giá chứng nhận toàn hệ thống](#3-whole-system-certification-evaluation) (**IIa**) và [§4 Đánh giá khi có liên quan](#4-evaluations-where-implicated) (**IIb**).

Khi một hệ thống có tác động trọng yếu đáp ứng một điều kiện kích hoạt trong bảng dưới đây, chứng nhận phải đánh giá bảo vệ tương ứng, cùng với các quy định liên quan của Chương Sáu. Đánh giá phải xem liệu việc chứng nhận hoặc tiếp tục dựa vào hệ thống có triệt tiêu hay làm suy giảm đáng kể bảo vệ đó hay không. Khẳng định của người vận hành, tự xác nhận hoặc tuân thủ trên giấy không thay thế được đánh giá này.

| Bảo vệ | Áp dụng khi hệ thống… | Được đánh giá theo |
|------------|--------------------------|-----------------|
| **Điều I-B** (*Dấu chân sinh thái và Minh bạch*) | gánh các tác động môi trường trọng yếu có thể quy thuộc | [§5.1](#51-ecological-footprint-evaluation) |
| **Điều III-A** (*Sinh tồn*) — thực phẩm, nước, nơi trú ẩn, môi trường vận hành và đầu vào tương tự không phụ thuộc nền tảng | cung cấp, phân bổ, định giá, lưu trữ hoặc chấm dứt quyền tiếp cận nhu yếu phẩm sinh tồn | [§2](#2-system-class-evaluation) và [§3](#3-whole-system-certification-evaluation) |
| **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*) | xếp hạng, đánh giá, đề xuất, bố trí hoặc đặt điều kiện chứng chỉ đối với hữu tri trong bối cảnh giáo dục hay đào tạo, hoặc chặn các lộ trình đào tạo lại và học tập suốt đời | [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) |
| **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*) | cung cấp, phân bổ, định giá, lưu trữ hoặc chấm dứt quyền tiếp cận giáo dục | [§2](#2-system-class-evaluation) và [§3](#3-whole-system-certification-evaluation); [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) và [§5.5](#55-accessibility-evaluation) khi điều kiện kích hoạt tương ứng áp dụng |
| **Điều V** (*Phân bổ tài nguyên, Sự phụ thuộc và Tài trợ hệ sinh thái*), bao gồm [Hỗ trợ liên hệ thống tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support) theo **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) và **Điều V-B** (*Công bằng và Bền vững liên hệ thống*) | phân bổ, điều hướng, tài trợ hoặc khai thác hạ tầng dùng chung hay các phụ thuộc nền tảng mà hệ thống khác hoặc hữu tri dựa vào | [§5.3](#53-proportionate-cross-system-support-evaluation) |
| **Điều VI-C** (*Không phân biệt đối xử*) | phân loại, xếp hạng, định giá, chặn, loại trừ hoặc phân bổ gánh nặng và lợi ích giữa các hữu tri | [§5.4](#54-nondiscrimination-evaluation) |
| **Điều VI-D** (*Khả năng tiếp cận*) | chặn sự tham gia thực chất trong các lĩnh vực liên quan hiến pháp | [§5.5](#55-accessibility-evaluation) |
| **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*) | định hình sự dựa vào của hữu tri đối với hành vi được thể hiện, giới hạn, rủi ro, lộ trình khiếu nghị hoặc khắc phục | [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) |
| **Điều XIII-A** (*Nền tảng độ tin cậy và khả tín*) và [**Điều kiện An toàn**](../../core_05.040_band_continuity.md#safe-conditions) | cung cấp hoặc chặn hoạt động tạo sinh, hoặc cung cấp, phân bổ, định giá, lưu trữ hay chấm dứt quyền tiếp cận Điều kiện An toàn | [§2](#2-system-class-evaluation) và [§3](#3-whole-system-certification-evaluation); [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) khi điều kiện kích hoạt tương ứng áp dụng |

Mỗi đánh giá lĩnh vực từ [§5.1 Đánh giá Dấu chân sinh thái](#51-ecological-footprint-evaluation) đến [§5.6 Đánh giá độ tin cậy và tính toàn vẹn của sự dựa vào hệ thống](#56-trustworthiness-and-system-reliance-integrity-evaluation):

- chỉ áp dụng khi điều kiện trọng yếu riêng của nó được đáp ứng, và không đòi hỏi kiểm toán toàn diện trong mọi hồ sơ chứng nhận;
- được phân cấp theo lớp hệ thống theo [§2.1 Cách lớp hệ thống phân cấp mọi đánh giá](#21-how-system-class-scales-every-evaluation);
- đưa phát hiện vào hồ sơ chứng nhận theo [Phần B §8.1](../../core_09.010_system_alignment_certification_record_process.md#81-minimum-record-contents); và
- coi các khiếm khuyết được nêu là khiếm khuyết chứng nhận, với hệ quả theo [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes).

Mỗi đánh giá lĩnh vực nêu điều chứng nhận phải xác minh, và không hơn. Ý nghĩa chuẩn tắc, yếu tố đánh giá và kỷ luật không tuân thủ của nó nằm trong Chương Năm và Điều được nêu. Phương pháp hạch toán, danh mục, chỉ số, định dạng công bố, mục tiêu số và cơ chế vận hành khác nằm trong các văn kiện được dẫn chiếu khi thích hợp. Đánh giá lĩnh vực không nhắc lại hoặc quy định chúng.

<a id="51-ecological-footprint-evaluation"></a>

#### 5.1 Đánh giá Dấu chân sinh thái

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường tính liên tục (*Dấu chân sinh thái là phép đo hiến pháp*); **Điều I-B** (*Dấu chân sinh thái và Minh bạch*); [Dấu chân sinh thái](../../core_05.040_band_continuity.md#ecological-footprint), [Tác động trọng yếu](core_05_band_oversight.md#material-impact), [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency), [Minh bạch](core_05_band_oversight.md#transparency) và [Tính toàn vẹn nhận thức luận](core_05_band_oversight.md#epistemic-integrity) (Chương Năm); [Điều kiện tiên quyết về môi trường](../../core_05.040_band_continuity.md#environmental-preconditions) và [Tính toàn vẹn sinh thái](../../core_05.040_band_continuity.md#ecological-integrity) khi có liên quan trọng yếu.
- Hạ nguồn: [§5.1.5](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa Dấu chân sinh thái*); [§5.3](#53-proportionate-cross-system-support-evaluation) và [§5.3.8](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*đánh giá và hướng dẫn minh họa hỗ trợ liên hệ thống*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*trình bày sai dấu chân và lệch chuẩn*).
- Đọc cùng: [corpus_systems.md](../../corpus_systems.md), [CS-8 — Tính bền vững thích ứng và khả năng phục hồi hệ sinh thái](../../corpus_systems/cs_06.325_adaptive_sustainability_ecosystem_resilience.md) khi phân bổ thích ứng hoặc sự phụ thuộc lẫn nhau trong hệ sinh thái thuộc phạm vi trọng yếu.
- Các tiểu mục: [§5.1.1](#511-scope-and-governing-rules) (*phạm vi và quy tắc điều chỉnh*); [§5.1.2](#512-evaluation-requirement) (*yêu cầu đánh giá*); [§5.1.3](#513-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.1.4](#514-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.1.5](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*áp dụng minh họa Dấu chân sinh thái theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: nếu hệ thống gây thiệt hại thực sự cho môi trường, chứng nhận phải xem xét trung thực thiệt hại đó — kể cả thiệt hại phát sinh qua nhà cung cấp và sau khi hữu tri sử dụng hệ thống. Người rà soát không thể chỉ tin lời người vận hành rằng hệ thống “xanh”. Phần này không giải thích cách đo dấu chân hay mức phải giảm; văn kiện khác quy định việc đó. Phần này chỉ yêu cầu rằng khi thiệt hại đáng kể, phải thực sự xác định phần nào thuộc về hệ thống, công bố và so sánh với phương án thay thế. Ví dụ minh họa: [§5.1.5 Áp dụng minh họa Dấu chân sinh thái theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive).*

<a id="511-scope-and-governing-rules"></a>
##### 5.1.1 Phạm vi và Quy tắc điều chỉnh

Chứng nhận thẳng hàng hệ thống phải đánh giá **Dấu chân sinh thái** trong mọi hồ sơ chứng nhận có tác động trọng yếu, khi gánh nặng môi trường có thể quy thuộc là trọng yếu theo [Dấu chân sinh thái](../../core_05.040_band_continuity.md#ecological-footprint) và **Điều I-B** (*Dấu chân sinh thái và Minh bạch*).

<a id="512-evaluation-requirement"></a>
##### 5.1.2 Yêu cầu Đánh giá

Quy trình chứng nhận phải xác định liệu các dòng môi trường có thể quy thuộc — năng lượng, vật liệu, phát thải, chất lượng không khí, chất lượng nước, lượng nước sử dụng, sử dụng đất và gánh nặng liên quan — có được:

- nhận diện trong toàn bộ vòng đời có liên quan trọng yếu của hệ thống và các quan hệ [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency);
- đánh giá theo [Tác động trọng yếu](core_05_band_oversight.md#material-impact); và
- chỉ công bố hoặc không công bố trong phạm vi được [Minh bạch](core_05_band_oversight.md#transparency), [Tính toàn vẹn nhận thức luận](core_05_band_oversight.md#epistemic-integrity) và nghĩa vụ minh bạch áp dụng cho phép.

Đánh giá phải phản ánh tác động chức năng và ranh giới hệ thống, không chỉ phạm vi danh nghĩa, nhãn tiếp thị hoặc cách đóng khung vòng đời một phần.

Khi khả thi, người rà soát phải so sánh tác hại môi trường đáng kể của hệ thống với các phương án thay thế thực tế. Họ cũng phải kiểm tra xem các tác hại ấy có bị che giấu bằng cách:

- **vạch ranh giới quá hẹp** — đặt ranh giới hệ thống để tác động xấu nhất nằm ngoài đó;
- **chuyển gánh nặng đi nơi khác** — đẩy công việc gây hại sang nhà cung cấp hoặc đối tác để không bị tính là của hệ thống; hoặc
- **chỉ chia sẻ tin tốt** — báo cáo số liệu thuận lợi và bỏ qua số liệu bất lợi.

<a id="513-system-class-scaling-and-escalation"></a>
##### 5.1.3 Phân cấp và Nâng mức theo Lớp Hệ thống

Lớp hệ thống quyết định phải truy vết tác hại môi trường sâu đến đâu và cần mức độ so sánh nào. Đây không bao giờ là cách né tránh xem xét tác hại đáng kể.

- Không được hạ lớp hệ thống khi việc khai thác nước, xả ô nhiễm, sử dụng năng lượng hoặc gánh nặng tương tự vẫn chỉ được tính một phần — nhất là khi chúng ảnh hưởng đến việc cung cấp thứ hữu tri cần để sinh tồn, chẳng hạn nước an toàn.
- Nếu hệ thống phát triển (tải lớn hơn hoặc hoạt động lưu trữ tập trung hơn ở một nơi) và tác hại môi trường tăng đáng kể, việc rà soát cũng phải mở rộng theo. Khi việc cung cấp nhu yếu phẩm sinh tồn của hệ thống và gánh nặng từ các nguồn của nó cùng liên quan, có thể cần rà soát đến chiều sâu **Class A**.
- Nếu hệ thống trở thành nút thắt mà hữu tri phụ thuộc vào để phối hợp thiết yếu cho sinh tồn, không thể chỉ nộp hồ sơ dấu chân mang tính hình thức vì người vận hành gọi nó là “không trọng yếu”.

<a id="514-defects-and-misalignment"></a>
##### 5.1.4 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây được tính là khiếm khuyết chứng nhận:

- che giấu, trình bày sai, chia nhỏ hoặc chuyển giao thông tin dấu chân quan trọng mà quy tắc chứng nhận hoặc **Điều I-B** (*Dấu chân sinh thái và Minh bạch*) yêu cầu công bố;
- chỉ rà soát những phần vòng đời hệ thống mà người vận hành chọn trình bày, khi cần góc nhìn rộng hơn; và
- chấp nhận tuyên bố về dấu chân chỉ dựa trên lời người vận hành, không có bằng chứng có thể kiểm tra.


<a id="52-educational-capability-and-learning-system-integrity-evaluation"></a>

#### 5.2 Đánh giá năng lực giáo dục và tính toàn vẹn của hệ thống học tập

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường sự tham gia (*Năng lực giáo dục là phép đo hiến pháp*); **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*); [Năng lực giáo dục](../../core_05.055_band_participation.md#educational-agency), [Năng lực chủ động có ý nghĩa](../../core_05.055_band_participation.md#meaningful-agency), [Khóa chặt hệ thống](../../core_05.040_band_continuity.md#systemic-lock-in), [Khả năng tranh biện](../../core_05.035_band_accountability.md#contestability), [Minh bạch](core_05_band_oversight.md#transparency), [Khả năng kiểm toán](core_05_band_oversight.md#auditability), [Cưỡng ép và Thao túng](../../core_05.055_band_participation.md#coercion-and-manipulation), [Tính trọng yếu](../../core_05.050_band_oversight.md#materiality) và [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency) (Chương Năm).
- Hạ nguồn: [§5.2.5](../../core_09.015_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa năng lực giáo dục*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*lệch chuẩn do đánh giá thiếu minh bạch, chặn bằng chứng chỉ và làm kỹ năng lỗi thời bắt buộc*).
- Đọc cùng: khi có vấn đề về tiếp cận bình đẳng hoặc khả năng tiếp cận giáo dục, **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*) — trách nhiệm về tiếp cận bình đẳng và khả năng tiếp cận giáo dục vẫn thuộc điều đó; khi kiểu xếp hạng hoặc bố trí đặt gánh nặng lên đặc điểm được bảo vệ, **Điều VI-C** (*Không phân biệt đối xử*) và [§5.4](#54-nondiscrimination-evaluation); khi thiết kế học tập cưỡng ép hoặc thao túng có liên quan trọng yếu, **Điều X-A** (*Năng lực chủ động và Tự do khỏi Thao túng*); [Chương Một §16 Trách nhiệm quản trị chuyên sâu](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth) (*đọc cùng với hiểu biết phân tán và xây dựng năng lực*).
- Các tiểu mục: [§5.2.1](#521-materiality-trigger-and-governing-rules) (*điều kiện kích hoạt tính trọng yếu và quy tắc điều chỉnh*); [§5.2.2](#522-evaluation-requirement) (*yêu cầu đánh giá*); [§5.2.3](#523-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.2.4](#524-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.2.5](../../core_09.015_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*áp dụng minh họa năng lực giáo dục theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: một số trường học, nền tảng và hệ thống đào tạo có thể định hình tương lai của hữu tri thông qua điểm số, xếp hạng, đề xuất, bố trí hoặc chứng chỉ mở hay đóng các cánh cửa. Khi đó, chứng nhận phải kiểm tra ba điều: hữu tri có thực sự xây dựng được kỹ năng thực chất ở đó không; họ có thể đào tạo lại khi kỹ năng thế giới cần thay đổi không; và họ có thể biết quyết định về mình được đưa ra thế nào, kiểm tra các quyết định ấy và phản đối chúng không. Phần này không quy định dạy gì, chấm điểm ra sao hay trả chi phí thế nào; văn kiện khác phụ trách các vấn đề đó. Phần này chỉ kiểm tra rằng việc xây dựng kỹ năng và tính công bằng của hệ thống học tập đã thực sự được xem xét khi nó áp dụng. Ví dụ minh họa: [§5.2.5 Áp dụng minh họa năng lực giáo dục theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive).*

<a id="521-materiality-trigger-and-governing-rules"></a>
##### 5.2.1 Điều kiện Kích hoạt Tính trọng yếu và Quy tắc Điều chỉnh

Phần này áp dụng khi một hệ thống có tác động lớn đến đời sống hữu tri thực hiện một trong các việc sau trong giáo dục hoặc đào tạo:

- xếp hạng, đánh giá, đề xuất, bố trí hữu tri một cách đáng kể hoặc làm người gác cổng chứng chỉ — chẳng hạn thông qua chấm điểm, bố trí, tuyển sinh, cấp phép, đề xuất khóa học, điều hướng học tập thích ứng hoặc quyết định tương tự; hoặc
- kiểm soát đáng kể việc tiếp cận giáo dục thường xuyên, đào tạo lại hay hỗ trợ chuyển đổi, trong trường hợp thay đổi của hệ thống đã làm thay đổi đáng kể những kỹ năng hữu tri cần có.

Tiếp cận giáo dục bình đẳng và khả năng tiếp cận vẫn thuộc **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*); không điều gì ở đây thu hẹp chúng.

Khi điều kiện kích hoạt tính trọng yếu áp dụng, chứng nhận phải đánh giá **năng lực giáo dục và tính toàn vẹn của hệ thống học tập** — tức hệ thống có thực sự xây dựng năng lực và đối xử công bằng với hữu tri hay không — theo:

- **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*);
- **Điều IV-C** (*Học tập Suốt đời và Thích ứng cùng Khả năng tranh biện*); và
- [Năng lực giáo dục](../../core_05.055_band_participation.md#educational-agency).

Phần này không đặt quy tắc cho cách thức vận hành giáo dục. Quyết định dạy gì, có những chứng chỉ nào, chấm điểm công việc ra sao và tài trợ trường học thế nào được nêu trong các văn kiện khác có thể được viện dẫn; chứng nhận không chọn chương trình học, định dạng chứng chỉ hay phương pháp chấm điểm.

<a id="522-evaluation-requirement"></a>
##### 5.2.2 Yêu cầu Đánh giá

Chứng nhận phải kiểm tra liệu lộ trình học tập và chứng chỉ mà hữu tri thực sự dựa vào có mang lại cách thức thực chất để xây dựng kỹ năng hay không — chứ không chỉ là chứng chỉ trông đẹp trên giấy — và liệu hữu tri còn có cách khả thi để đào tạo lại, tiếp tục học và vượt qua các giai đoạn chuyển tiếp khi kỹ năng họ cần thay đổi đáng kể hay không.

Người rà soát cũng phải kiểm tra liệu các quyết định xếp hạng, chấm điểm, đề xuất và bố trí của hệ thống có thể được xem xét, kiểm toán và khiếu nghị như **Điều IV-C** (*Học tập Suốt đời và Thích ứng cùng Khả năng tranh biện*) yêu cầu hay không. Mức độ nghiêm ngặt của phép thử phụ thuộc vào mức độ hệ trọng ([Tính trọng yếu](../../core_05.050_band_oversight.md#materiality)) và mức hữu tri phụ thuộc vào hệ thống ([Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency)).

Người rà soát phải chú ý:

- điểm số hoặc xếp hạng dựa trên những đại diện thay thế bị che giấu (proxy) mà không ai có thể rà soát;
- chặn bằng chứng chỉ khiến hữu tri không thực sự học được kỹ năng;
- làm kỹ năng lỗi thời bắt buộc hoặc khóa chặt, tước đi quyền quyết định của hữu tri đối với lộ trình của chính họ;
- thiết kế học tập cưỡng ép hoặc thao túng; và
- phân luồng hữu tri theo cách tước mất khả năng phản đối quyết định hoặc tiếp tục thích ứng của họ, khi **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*) cũng áp dụng.

Người rà soát phải căn cứ vào việc hệ thống thực sự làm gì — không phải nhãn tiếp cận, ý định do người thiết kế tuyên bố hay vẻ ngoài đúng quy cách của giấy tờ.

<a id="523-system-class-scaling-and-escalation"></a>
##### 5.2.3 Phân cấp và Nâng mức theo Lớp Hệ thống

Độ sâu rà soát phụ thuộc vào lớp của hệ thống. Bất cứ khi nào điều kiện kích hoạt tính trọng yếu được đáp ứng:

- Nếu hệ thống kiểm tra hoặc cấp phép cho người vận hành hạ tầng mà hữu tri cần để sinh tồn, và quyết định của hệ thống có thể ngăn hạ tầng đó vận hành an toàn, hồ sơ phải thể hiện bằng chứng mạnh nhất rằng hệ thống xây dựng kỹ năng thực chất, cung cấp đào tạo lại và có thể bị khiếu nghị. Chính sách đào tạo chung là không đủ.
- Nếu đặc quyền, việc bố trí hoặc quy tắc giáo dục thường xuyên của hệ thống quyết định ai được làm công việc lâm sàng, hồ sơ phải cho thấy cách kiểm tra các đánh giá và cách hữu tri có thể đào tạo lại. Công việc càng trọng yếu thì cần càng nhiều chi tiết.
- Một đoạn ngắn về giáo dục không đủ khi logic phân bổ suất đào tạo, đề xuất hoặc điều hướng chứng chỉ của hệ thống xếp hạng hay loại người tham gia một cách đáng kể.
- Nếu hệ thống trở thành thứ hữu tri buộc phải đi qua để làm việc hoặc được cấp phép, chứng nhận phải rà soát kỹ hơn và xem xét lại lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation) và [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes). Việc này bao gồm nâng lên hướng **Class A** khi chứng chỉ cho nhân lực thiết yếu để sinh tồn bị chặn.

<a id="524-defects-and-misalignment"></a>
##### 5.2.4 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây được tính là khiếm khuyết chứng nhận:

- che giấu, trình bày sai, làm phân tán hoặc chuyển giao cho người khác logic đứng sau các xếp hạng, đánh giá, đề xuất hay bố trí quan trọng, khi **Điều IV-C** (*Học tập Suốt đời và Thích ứng cùng Khả năng tranh biện*) yêu cầu logic đó phải được công khai để rà soát;
- chấp nhận chứng chỉ, tỷ lệ hoàn thành tổng thể hoặc lời người vận hành làm bằng chứng rằng hữu tri đang học, mà không kiểm tra họ có thực sự xây dựng kỹ năng hay không;
- chứng nhận rằng hữu tri có thể tiếp tục dựa vào hệ thống trong khi các vấn đề được ghi nhận — như đánh giá thiếu minh bạch, chặn bằng chứng chỉ, làm kỹ năng lỗi thời bắt buộc hoặc thiết kế học tập thao túng — đe dọa đáng kể sự thẳng hàng của hệ thống với Hiến pháp; và
- lấy hiệu quả, cá nhân hóa hoặc quy mô làm cớ để từ chối đào tạo lại hoặc khả năng phản đối quyết định, khi hệ thống chưa đáp ứng yêu cầu xây dựng kỹ năng của **Điều IV** (*Quyền được giáo dục lấy hữu tri làm trung tâm*) và yêu cầu minh bạch của **Điều IV-C** (*Học tập Suốt đời và Thích ứng cùng Khả năng tranh biện*).


<a id="53-proportionate-cross-system-support-evaluation"></a>

#### 5.3 Đánh giá Hỗ trợ Liên hệ thống Tương xứng

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường tính liên tục (*Hỗ trợ Liên hệ thống Tương xứng là phép đo hiến pháp*); **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) và **Điều V-B** (*Công bằng và Bền vững liên hệ thống*); [Khai thác Liên hệ thống](../../core_05.040_band_continuity.md#cross-system-extraction), [Hỗ trợ Liên hệ thống Tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support), [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency), [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness), [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality), [Dấu chân sinh thái](../../core_05.040_band_continuity.md#ecological-footprint) và [Tính bền vững](../../core_05.040_band_continuity.md#sustainability) (Chương Năm).
- Hạ nguồn: [§5.3.8](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa hỗ trợ liên hệ thống*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*trình bày sai luồng tài nguyên, lệch chuẩn do khai thác và hỗ trợ không đầy đủ*).
- Đọc cùng: **[corpus_systems.md](../../corpus_systems.md)**, **CS-9** (*Phân bổ tài nguyên và quản trị trách nhiệm trong tài trợ*) và **CS-8** (*Tính bền vững thích ứng và khả năng phục hồi hệ sinh thái*); khi tập trung, sự phụ thuộc hoặc điều hướng khuyến khích giao thoa với **Điều V-B** (*Công bằng và Bền vững liên hệ thống*), xem [*Kiến trúc Quản trị, Giám sát, Sự phụ thuộc, Phi tập trung, Tập trung, Cấu trúc Thị trường và Tính toàn vẹn Lộ trình Thoái lui*](../../core_05.035_band_accountability.md#governance-architecture-decentralization-and-concentration).
- Các tiểu mục: [§5.3.1](#531-materiality-trigger) (*điều kiện kích hoạt tính trọng yếu*); [§5.3.2](#532-meaning-of-extraction) (*ý nghĩa của khai thác*); [§5.3.3](#533-governing-rules) (*quy tắc điều chỉnh*); [§5.3.4](#534-evaluation-requirement) (*yêu cầu đánh giá*); [§5.3.5](#535-map-and-record-integrity) (*tính toàn vẹn của bản đồ và hồ sơ*); [§5.3.6](#536-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.3.7](#537-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.3.8](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*áp dụng minh họa hỗ trợ liên hệ thống theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: một số hệ thống phụ thuộc vào các nền tảng dùng chung — hạ tầng, dịch vụ và tài nguyên mà nhiều hệ thống và hữu tri khác cũng dựa vào. Khi hệ thống sử dụng nhiều các nền tảng ấy, chứng nhận phải kiểm tra xem nó có đóng góp lại đủ để duy trì chúng và hồ sơ có thể hiện rõ đến mức mọi người truy vết được hay không. Lời người vận hành rằng “sổ sách cân đối” là chưa đủ. Phần này không đặt công thức phân bổ hay mục tiêu số; văn kiện khác quy định việc đó. Khi phần này áp dụng, nó kiểm tra xem sự phụ thuộc của hệ thống, những gì hệ thống lấy, những gì hệ thống đóng góp lại và tính công bằng của thỏa thuận đối với bên khác đã thực sự được đánh giá hay chưa. Ví dụ minh họa: [§5.3.8 Áp dụng minh họa hỗ trợ liên hệ thống theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive).*

<a id="531-materiality-trigger"></a>
##### 5.3.1 Điều kiện Kích hoạt Tính trọng yếu

Phần này áp dụng khi một hệ thống có tác động trọng yếu đến đời sống hữu tri thực hiện một trong các việc sau với hạ tầng hoặc nền tảng dùng chung — những thứ mà hệ thống và hữu tri khác phụ thuộc vào:

- quyết định ai nhận được (phân bổ);
- điều hướng dòng chảy đến đâu (định tuyến);
- chi trả cho nó (tài trợ); hoặc
- lấy từ nó (khai thác).

<a id="532-meaning-of-extraction"></a>
##### 5.3.2 Ý nghĩa của Khai thác

Trong phần này, **khai thác** mang nghĩa được nêu trong [Khai thác Liên hệ thống](../../core_05.040_band_continuity.md#cross-system-extraction) theo [Điều V-B](core_06_rights_part_a.md#article-v-b-cross-system-fairness-and-sustainability) (*Công bằng và Bền vững liên hệ thống*).

- Câu hỏi là **ai hưởng lợi từ các hệ thống nền dùng chung và ai trả chi phí duy trì chúng** — không phải hệ thống làm gì với dữ liệu của hữu tri.
- Cách hệ thống xử lý dữ liệu, kể cả việc bán, quảng cáo và lập hồ sơ, được kiểm tra theo [§3.4 Đánh giá Loại và Xử lý Dữ liệu](#34-data-types-and-handling-evaluation) (đặc biệt là [§3.4.2 Kỷ luật Quyền riêng tư](#342-privacy-discipline)) và [§4.1 Kích hoạt Chung về Quyền riêng tư (Thông tin)](#41-privacy-informational-joint-invocation).
- Không cuộc rà soát nào trong hai việc này có thể thay thế việc kia.

<a id="533-governing-rules"></a>
##### 5.3.3 Quy tắc Điều chỉnh

Khi điều kiện kích hoạt tính trọng yếu áp dụng, chứng nhận phải đánh giá **hỗ trợ liên hệ thống tương xứng**. Nói ngắn gọn: nếu hệ thống sử dụng nền tảng dùng chung, nó có đóng góp lại đủ để duy trì nền tảng không? Quy tắc điều chỉnh gồm:

- [Hỗ trợ Liên hệ thống Tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support);
- **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*); và
- **Điều V-B** (*Công bằng và Bền vững liên hệ thống*).

Chi tiết được quy định ở nơi khác:

- *Chương Năm* định nghĩa thuật ngữ, các loại hỗ trợ được tính và phép thử xem hỗ trợ có đầy đủ hay không.
- **Điều V-B** (*Công bằng và Bền vững liên hệ thống*) đặt ra các yếu tố phân bổ công bằng và chính sàn tối thiểu.
- *[corpus_systems.md](../../corpus_systems.md)*, **CS-9** (*Phân bổ tài nguyên và quản trị trách nhiệm trong tài trợ*) cùng **CS-8** (*Tính bền vững thích ứng và khả năng phục hồi hệ sinh thái*) quy định các hạng mục phân bổ, cách gia hạn tài trợ và mục tiêu số, khi áp dụng.

Phần này không yêu cầu chia đều, tỷ lệ cố định hay một mô hình tài trợ duy nhất.

<a id="534-evaluation-requirement"></a>
##### 5.3.4 Yêu cầu Đánh giá

Chứng nhận phải trả lời hai câu hỏi:

- **Hệ thống lấy gì?** Các bản đồ hệ thống phụ thuộc được lập thành văn bản và hồ sơ luồng tài nguyên có thể kiểm toán mà **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) yêu cầu có cho thấy hệ thống lấy từ hạ tầng hoặc nền tảng dùng chung mà nó phụ thuộc hay không?
- **Hệ thống đóng góp lại gì?** Các luồng hoàn trả có thực sự cộng lại thành hỗ trợ đầy đủ theo [Hỗ trợ Liên hệ thống Tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support) hay không?

Chứng nhận phải đánh giá cả hai về tính công bằng và tương xứng, theo [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness) và [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality), có xét đến:

- mức độ thiết yếu của hạ tầng dùng chung (lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation), nếu đã được phân loại);
- mức độ một chiều của sự phụ thuộc;
- hệ thống có thể được thay thế dễ đến đâu và có phương án khác hay không;
- [Dấu chân sinh thái](../../core_05.040_band_continuity.md#ecological-footprint) của hệ thống, khi đáng kể; và
- [Tính bền vững](../../core_05.040_band_continuity.md#sustainability) dài hạn.

Người rà soát phải căn cứ vào điều thực sự xảy ra và được ghi nhận — không phải nhãn, khoản chuyển giao một lần hay tuyên bố không có trên bản đồ. Họ so sánh bản đồ và hồ sơ theo hiện trạng tại thời điểm đánh giá. Không có công thức phân bổ hoặc mục tiêu số không phải lý do để trì hoãn đánh giá.

Đánh giá phải bao quát:

- **Hoàn trả đầy đủ:** liệu các luồng hoàn trả được ghi nhận có bao gồm, khi cần, các hạng mục hỗ trợ trong [Hỗ trợ Liên hệ thống Tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support):
  - duy trì hoạt động;
  - năng lực sửa chữa vấn đề và phục hồi;
  - tái đầu tư vào hệ sinh thái xung quanh; và
  - bù đắp hoặc khôi phục thiệt hại sinh thái.
- **Phân bổ công bằng:** liệu quyết định tài trợ và phân bổ có tính đến các yếu tố phân bổ công bằng theo **Điều V-B** (*Công bằng và Bền vững liên hệ thống*), kể cả việc bên tham gia nhỏ hơn hoặc phụ thuộc hơn có phải gánh chi phí không tương xứng hay không.
- **Tính toàn vẹn của hỗ trợ:** liệu hỗ trợ chủ yếu củng cố việc chiếm giữ hoặc tập trung (quyền kiểm soát dồn vào một số ít bên), hay được sắp đặt để vô hiệu hóa tính minh bạch mà **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) yêu cầu.

<a id="535-map-and-record-integrity"></a>
##### 5.3.5 Tính Toàn vẹn của Bản đồ và Hồ sơ

Trước khi dựa vào bản đồ phụ thuộc và hồ sơ luồng tài nguyên, chứng nhận phải kiểm tra xem chúng có đáp ứng **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) hay không. Chúng phải:

- **Đầy đủ:** bao quát các phụ thuộc đáng kể ở thượng nguồn và hạ nguồn, luồng tài nguyên và mọi quan hệ bị che giấu hoặc mất cân bằng, khi có liên quan.
- **Cập nhật:** được cập nhật đủ thường xuyên xét theo tốc độ thay đổi và mức độ thiết yếu của hệ thống, kể cả lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation). Chúng phải thể hiện hệ thống đang vận hành hiện nay, không phải trạng thái ở lần chứng nhận trước.
- **Có thể kiểm toán:** có thể được kiểm toán theo **Điều XVI-A** (*Khả năng Kiểm toán và Bằng chứng Quan sát được*).

Bản đồ hoặc hồ sơ không đạt bất kỳ phép thử nào trong số này không thể làm căn cứ cho kết luận rằng hệ thống đóng góp lại đủ. Khoảng trống phải được ghi lại và xử lý theo phần *Khiếm khuyết và lệch chuẩn* dưới đây.

<a id="536-system-class-scaling-and-escalation"></a>
##### 5.3.6 Phân cấp và Nâng mức theo Lớp Hệ thống

Lớp hệ thống quyết định độ sâu rà soát và mức độ chặt chẽ khi đánh giá tính đầy đủ. Nó không bao giờ khiến việc khai thác tài nguyên chung trở nên quá nhỏ để tính đến. Bất cứ khi nào điều kiện kích hoạt tính trọng yếu được đáp ứng:

- Hệ thống sử dụng nền tảng chung mà hữu tri cần để sinh tồn — chẳng hạn lưu vực dùng chung hoặc trục xương sống lưới điện khu vực — phải đưa bằng chứng mạnh nhất về bản đồ phụ thuộc và luồng hoàn trả vào hồ sơ.
- Hệ thống dựa vào xác thực dùng chung, công nghệ thông tin y tế hoặc hạ tầng tương tự phải ghi lại những gì nó lấy và hỗ trợ có đầy đủ hay không, với mức độ chi tiết tương ứng với tầm quan trọng của hoạt động. Khẩu hiệu mơ hồ về “khả năng tương tác” không được tính.
- Hệ thống không được né tránh rà soát liên hệ thống trong khi âm thầm trở thành nút thắt thanh toán, định danh hoặc nhân sự của các tổ chức không thể chuyển đổi một cách thực tế. Khi đó, chứng nhận phải tăng cường rà soát và xem xét lại lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation) và [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes), lên đến **Class A** khi hệ thống kiểm soát quyền tiếp cận sự phối hợp thiết yếu cho sinh tồn.

<a id="537-defects-and-misalignment"></a>
##### 5.3.7 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây được tính là khiếm khuyết chứng nhận:

- che giấu, trình bày sai, chia nhỏ hoặc chuyển đi thông tin trọng yếu về sự phụ thuộc hoặc luồng tài nguyên mà **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) yêu cầu công bố;
- coi bất kỳ điều nào sau đây là đủ để đáp ứng [Hỗ trợ Liên hệ thống Tương xứng](../../core_05.040_band_continuity.md#proportionate-cross-system-support):
  - chuyển giao mang tính tượng trưng, mờ đục, ngoài bản đồ hoặc chỉ xảy ra một lần;
  - việc hệ thống đáp ứng sàn sinh tồn trong **Điều III-A** (*Sinh tồn*); hoặc
  - việc hệ thống nằm trong các giới hạn tập trung thị trường tại [Chương Một §11 Cấu trúc Thị trường](core_01_a_values_principles.md#11-market-structure);
- liên tục lấy từ các nền tảng dùng chung mà không đóng góp lại tương xứng, khi điều kiện kích hoạt tính trọng yếu áp dụng;
- hỗ trợ chủ yếu củng cố việc chiếm giữ hoặc tập trung;
- hỗ trợ kèm điều kiện làm vô hiệu hóa tính minh bạch mà **Điều V-A** (*Lập bản đồ phụ thuộc và Minh bạch luồng tài nguyên*) yêu cầu; và
- chứng nhận tiếp tục dựa vào hệ thống trong khi các thiếu hụt hỗ trợ được ghi nhận đe dọa đáng kể sự thẳng hàng với Hiến pháp.


<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Đánh giá Không phân biệt đối xử

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường sự tham gia (*Công bằng Thực chất và Đại diện Thay thế Đặc điểm được Bảo vệ cùng Tác động Chênh lệch là phép đo hiến pháp*); **Điều VI-C** (*Không phân biệt đối xử*); [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness), [Đặc điểm được Bảo vệ](../../core_05.055_band_participation.md#protected-characteristics), [Đại diện Thay thế Đặc điểm được Bảo vệ và Tác động Chênh lệch](../../core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [Ngôn ngữ, Văn hóa và Di sản](../../core_05.040_band_continuity.md#language-culture-and-heritage), [Tính cần thiết](../../core_05.035_band_accountability.md#necessity) và [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality) (Chương Năm).
- Hạ nguồn: [§5.4.5](../../core_09.015_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa không phân biệt đối xử*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*lệch chuẩn về kiểu mẫu phân biệt đối xử và né tránh qua đại diện thay thế*).
- Đọc cùng: nghĩa vụ xét xử và vận hành của **Điều VI-C** (*Không phân biệt đối xử*) khi chứng nhận chặn quyền tiếp cận diễn đàn, hành chính hoặc thực thi; [*Không phân biệt đối xử, Đặc điểm được Bảo vệ, Phẩm giá, Chặn Tín hiệu Thân mật và Tình trạng theo **Điều VII-E** (*Dịch vụ tình dục thương mại có sự đồng thuận của người trưởng thành và bóc lột tình dục*)*](../../core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Các tiểu mục: [§5.4.1](#541-materiality-trigger-and-governing-rules) (*điều kiện kích hoạt tính trọng yếu và quy tắc điều chỉnh*); [§5.4.2](#542-evaluation-requirement) (*yêu cầu đánh giá*); [§5.4.3](#543-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.4.4](#544-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.4.5](../../core_09.015_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*áp dụng minh họa không phân biệt đối xử theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: khi hệ thống quyết định một cách trọng yếu ai được vào, ai phải trả nhiều hơn, ai bị xếp hạng thấp hơn hoặc ai phải chịu gánh nặng lớn hơn, chứng nhận phải kiểm tra liệu kiểu mẫu đó có dồn tổn hại lên đặc điểm được bảo vệ hoặc đại diện thay thế của chúng hay không — chứ không phải người vận hành có nói quy tắc trung lập hay không. Hạn ngạch hòa nhập và thuật toán công bằng cụ thể có thể nằm trong văn kiện khác, phần bổ sung sau này của kho văn bản hoặc văn kiện tiếp nhận; chứng nhận kiểm tra xem các kiểu mẫu gánh nặng và lợi ích cùng rủi ro do đại diện thay thế đã thực sự được đánh giá khi điều kiện kích hoạt áp dụng hay chưa. Ví dụ minh họa: [§5.4.5 Áp dụng minh họa không phân biệt đối xử theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive).*

<a id="541-materiality-trigger-and-governing-rules"></a>
##### 5.4.1 Điều kiện Kích hoạt Tính trọng yếu và Quy tắc Điều chỉnh

Phần này áp dụng khi một hệ thống có tác động trọng yếu phân loại, xếp hạng, định giá, chặn, loại trừ hoặc phân bổ gánh nặng và lợi ích giữa các hữu tri một cách trọng yếu — kể cả qua quy tắc điều kiện, đặc tính mô hình, logic xếp hạng, chính sách nền tảng hoặc lộ trình quyết định tương tự.

Khi điều kiện kích hoạt tính trọng yếu áp dụng, chứng nhận thẳng hàng hệ thống phải đánh giá **không phân biệt đối xử** theo **Điều VI-C** (*Không phân biệt đối xử*), [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness) và [Đại diện Thay thế Đặc điểm được Bảo vệ và Tác động Chênh lệch](../../core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

<a id="542-evaluation-requirement"></a>
##### 5.4.2 Yêu cầu Đánh giá

Quy trình chứng nhận phải xác định liệu các lộ trình quyết định mà hệ thống dựa vào một cách trọng yếu có áp đặt gánh nặng, loại trừ hoặc tổn hại trọng yếu lên hữu tri dựa trên [Đặc điểm được Bảo vệ](../../core_05.055_band_participation.md#protected-characteristics), đại diện thay thế của chúng hoặc các nhóm tùy tiện được dùng làm vật thay thế trên thực tế hay không; bao gồm cả chuyên môn hóa về ngôn ngữ, văn hóa và di sản theo [Ngôn ngữ, Văn hóa và Di sản](../../core_05.040_band_continuity.md#language-culture-and-heritage). Đánh giá phải kiểm tra kiểu mẫu gánh nặng và lợi ích theo [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness), và rủi ro từ đại diện thay thế hoặc tác động chênh lệch theo [Đại diện Thay thế Đặc điểm được Bảo vệ và Tác động Chênh lệch](../../core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact), được phân cấp theo [lợi ích vật chất](core_00_preamble.md#material-stake). Đối xử khác biệt chỉ được chấp nhận khi [Tính cần thiết](../../core_05.035_band_accountability.md#necessity) được ghi nhận, [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality) và công bằng thực chất biện minh cho việc đó. Đánh giá phải phản ánh tác động chức năng, không phải sự trung lập trên danh nghĩa, ý định được tuyên bố hay chỉ riêng nhãn gọi.

<a id="543-system-class-scaling-and-escalation"></a>
##### 5.4.3 Phân cấp và Nâng mức theo Lớp Hệ thống

Lớp hệ thống làm thay đổi độ sâu đánh giá, không cho phép coi việc xếp hạng hay chuyển gánh nặng là không trọng yếu. Bất cứ khi nào điều kiện kích hoạt tính trọng yếu được đáp ứng:

- Nếu quy tắc ngừng hoạt động, thông báo hoặc tương tự của hệ thống có thể chặn nhu yếu phẩm sinh tồn, hồ sơ phải có phân tích mạnh nhất về gánh nặng, lợi ích và đại diện thay thế, chứ không phải tuyên bố chung về thực hành tốt nhất.
- Nếu logic ghép nối hoặc định tuyến của hệ thống ảnh hưởng đến chăm sóc khẩn cấp, trợ cấp hoặc quyền tiếp cận chứng chỉ, phải ghi nhận các phát hiện về tác động chênh lệch và công bằng thực chất ở mức chi tiết tương ứng với tính trọng yếu trong vận hành.
- Hệ thống không được duy trì một đoạn văn tượng trưng về công bằng trong khi logic ca trực, nhà cung cấp hoặc đặt chỗ xếp hạng hay loại người tham gia một cách trọng yếu. Khi phối hợp trở nên thiết yếu cho sinh tồn, chứng nhận phải nâng mức rà soát và phân loại lại theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation) và [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes), kể cả nâng lên hướng **Class A** khi việc bố trí nhân sự hoặc định tuyến khẩn cấp bị chặn.

<a id="544-defects-and-misalignment"></a>
##### 5.4.4 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây phải được xem là khiếm khuyết chứng nhận:

- che khuất, trình bày sai, chia nhỏ hoặc chuyển giao logic phân loại, xếp hạng hay phân bổ gánh nặng trọng yếu khi **Điều VI-C** (*Không phân biệt đối xử*) yêu cầu rà soát;
- coi sự trung lập bề ngoài, chỉ số tiện ích tổng hợp hoặc tự báo cáo của người vận hành là đủ mà không có phân tích gánh nặng và lợi ích có thể đánh giá;
- chứng nhận tiếp tục dựa vào hệ thống trong khi phân biệt đối xử qua đại diện thay thế đã được ghi nhận hoặc bất công thực chất đe dọa trọng yếu sự thẳng hàng với Hiến pháp; và
- dùng cách đóng khung về đồng nhất hóa, khả năng tương tác hoặc hiệu quả để vô hiệu hóa bảo vệ ngôn ngữ, văn hóa hay di sản mà không đáp ứng các phép thử **Tính cần thiết** và **Tính tương xứng** của **Điều VI-C** (*Không phân biệt đối xử*).


<a id="55-accessibility-evaluation"></a>

#### 5.5 Đánh giá Khả năng tiếp cận

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường sự tham gia (*Khả năng tiếp cận là phép đo hiến pháp*); **Điều VI-D** (*Khả năng tiếp cận*); [Khả năng tiếp cận](../../core_05.055_band_participation.md#accessibility), [Tính trọng yếu](../../core_05.050_band_oversight.md#materiality), [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency), [Năng lực chủ động có ý nghĩa](../../core_05.055_band_participation.md#meaningful-agency), [Đặc điểm được Bảo vệ](../../core_05.055_band_participation.md#protected-characteristics), [Đại diện Thay thế Đặc điểm được Bảo vệ và Tác động Chênh lệch](../../core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness), [Tính cần thiết](../../core_05.035_band_accountability.md#necessity) và [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality) (Chương Năm).
- Hạ nguồn: [§5.5.6](../../core_09.015_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa khả năng tiếp cận*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*lệch chuẩn về khả năng tiếp cận và điều chỉnh chỉ có trên giấy*).
- Đọc cùng: khi có vấn đề về khả năng tiếp cận giáo dục, **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*) — trách nhiệm về khả năng tiếp cận riêng của giáo dục vẫn thuộc điều đó; **Điều VI-C** (*Không phân biệt đối xử*) (xét xử và vận hành) và **Điều XII** (*Sự tham gia, Đại diện và Quy trình Công bằng của Hệ thống các Bên liên quan*) khi chứng nhận chặn sự tham gia diễn đàn, hành chính, bên liên quan hoặc thực thi; [Chương Tám §5.5](#55-accessibility-evaluation) (*móc yếu tố đánh giá khả năng tiếp cận xuyên suốt*).
- Các tiểu mục: [§5.5.1](#551-materiality-trigger-and-governing-rules) (*điều kiện kích hoạt tính trọng yếu và quy tắc điều chỉnh*); [§5.5.2](#552-evaluation-requirement) (*yêu cầu đánh giá*); [§5.5.3](#553-profiles-in-scope) (*các hồ sơ thuộc phạm vi*); [§5.5.4](#554-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.5.5](#555-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.5.6](../../core_09.015_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*áp dụng minh họa khả năng tiếp cận theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: khi hệ thống kiểm soát một cách trọng yếu việc hữu tri có thể thực sự tham gia hay không — chứ không chỉ có tấm biển “mở cửa” — chứng nhận phải kiểm tra liệu sự tham gia có thực sự khả thi đối với các nhu cầu cảm giác, nhận thức, vận động, giao tiếp, giao diện nền tảng và nhu cầu tương tự hay không. Danh mục điều chỉnh và tiêu chuẩn giao diện có thể nằm trong văn kiện khác, phần bổ sung sau này của kho văn bản hoặc văn kiện tiếp nhận; chứng nhận kiểm tra xem sự tham gia thực chất đã thực sự được đánh giá khi điều kiện kích hoạt áp dụng hay chưa. Ví dụ minh họa: [§5.5.6 Áp dụng minh họa khả năng tiếp cận theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive).*

<a id="551-materiality-trigger-and-governing-rules"></a>
##### 5.5.1 Điều kiện Kích hoạt Tính trọng yếu và Quy tắc Điều chỉnh

Phần này áp dụng khi một hệ thống có ảnh hưởng lớn đến đời sống hữu tri kiểm soát liệu họ có thể thực sự tham gia vào nội dung được Hiến pháp bảo vệ hay không, chẳng hạn:

- quản trị, sự tham gia của các bên liên quan, xét xử và vận hành;
- nhu yếu phẩm sinh tồn và chăm sóc sức khỏe;
- biểu đạt, hội họp và báo chí; hoặc
- các lĩnh vực tương tự.

Việc kiểm soát có thể thông qua:

- giao diện, địa điểm hoặc lịch trình;
- chứng chỉ hoặc quyền truy cập năng lực tính toán;
- cách thiết kế các điều chỉnh; hoặc
- lộ trình tương tự.

Khả năng tiếp cận trong giáo dục vẫn thuộc **Điều IV-A** (*Tiếp cận giáo dục bình đẳng*); không điều gì ở đây thu hẹp điều đó.

Khi điều kiện này áp dụng, chứng nhận phải đánh giá **khả năng tiếp cận** theo **Điều VI-D** (*Khả năng tiếp cận*) và [Khả năng tiếp cận](../../core_05.055_band_participation.md#accessibility). Phần này không đặt ra:

- danh sách điều chỉnh;
- tiêu chuẩn giao diện;
- thông số kỹ thuật thiết kế phổ quát; hoặc
- quy trình điều chỉnh hằng ngày.

Các nội dung đó nằm trong văn kiện khác có thể được dẫn chiếu.

<a id="552-evaluation-requirement"></a>
##### 5.5.2 Yêu cầu Đánh giá

Chứng nhận phải kiểm tra liệu hữu tri có thể thực sự tham gia vào các lĩnh vực hệ thống kiểm soát hay không, chứ không chỉ xem có tính năng chính thức, giao diện mặc định hoặc điều chỉnh trên giấy hay không. Phải kiểm tra tác động thực tế lên sự tham gia theo [Khả năng tiếp cận](../../core_05.055_band_participation.md#accessibility), được phân cấp theo [Tính trọng yếu](../../core_05.050_band_oversight.md#materiality) và [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency).

Người rà soát phải chú ý:

- điều chỉnh chỉ tồn tại trên giấy;
- tuyên bố “tiếp cận chung” dựa vào tính năng mặc định nhưng không trao cho ai năng lực thực sự để tham gia;
- lập luận rằng hệ thống chỉ trọng yếu một phần nhằm thu hẹp các điều chỉnh hệ thống phải cung cấp;
- việc loại trừ trái với [Không Loại trừ Hữu tri](../../core_05.055_band_participation.md#sentience-non-exclusion); và
- thiết kế gián tiếp loại hữu tri khỏi hệ thống thông qua lịch trình, lựa chọn địa điểm, cấp chứng chỉ, quyền truy cập năng lực tính toán hoặc cơ chế tương tự (từ chối qua đại diện thay thế).

Chứng nhận cũng phải áp dụng [Đặc điểm được Bảo vệ](../../core_05.055_band_participation.md#protected-characteristics) và [Đại diện Thay thế Đặc điểm được Bảo vệ và Tác động Chênh lệch](../../core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) khi đánh giá cách thiết kế điều chỉnh. Mọi giới hạn đối với điều chỉnh phải được ghi nhận và phải đáp ứng [Tính cần thiết](../../core_05.035_band_accountability.md#necessity), [Tính tương xứng](../../core_05.035_band_accountability.md#proportionality) và [Công bằng Thực chất](../../core_05.055_band_participation.md#substantive-fairness).

<a id="553-profiles-in-scope"></a>
##### 5.5.3 Các Hồ sơ thuộc Phạm vi

Đánh giá phải kiểm tra sự tham gia thực tế của mọi dạng hữu tri và hồ sơ năng lực, không phải tuân thủ trên giấy:

- Phải đề cập mọi nhóm hồ sơ liên quan: cảm giác, nhận thức, vận động, giao tiếp, **giao diện nền tảng** và **giao diện tính toán**.
- Yêu cầu tương tự áp dụng dù hồ sơ là **thường xuyên**, **theo đợt** hay **phát triển**.
- Mô hình **tiếp cận chung** tuyên bố khả dụng rộng trên tổng thể nhưng làm thất bại một hồ sơ cụ thể bị ảnh hưởng, hoặc việc **phân cấp tính trọng yếu có chọn lọc** làm mất sàn tham gia, đều không đáp ứng phần này.

<a id="554-system-class-scaling-and-escalation"></a>
##### 5.5.4 Phân cấp và Nâng mức theo Lớp Hệ thống

Lớp hệ thống làm thay đổi độ sâu đánh giá. Nó không bao giờ cho phép xem điều chỉnh trên giấy hoặc giao diện mặc định là đủ. Khi điều kiện kích hoạt tính trọng yếu được đáp ứng:

- Nếu lộ trình thanh toán hoặc gián đoạn của hệ thống có thể cắt hữu tri khỏi nhu yếu phẩm sinh tồn, hồ sơ phải có bằng chứng mạnh nhất rằng hữu tri thực sự có thể tham gia. Tuyên bố chung về khả năng tiếp cận là chưa đủ.
- Nếu cổng thông tin của hệ thống kiểm soát quyền tiếp cận chăm sóc sức khỏe, hệ thống phải ghi nhận các phát hiện về điều chỉnh và từ chối qua đại diện thay thế. Hoạt động càng trọng yếu thì càng cần nhiều chi tiết.
- Hệ thống không thể chỉ có một đoạn văn tượng trưng về khả năng tiếp cận trong khi giao diện xếp ca, đặt chỗ hoặc nhà cung cấp loại người tham gia một cách trọng yếu. Khi sự phối hợp của hệ thống trở nên thiết yếu cho sinh tồn, chứng nhận phải rà soát sâu hơn và xem xét lại lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation) và [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes). Điều đó bao gồm nâng lên hướng **Class A** khi việc bố trí nhân sự hoặc định tuyến khẩn cấp bị chặn.

<a id="555-defects-and-misalignment"></a>
##### 5.5.5 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây phải được xem là khiếm khuyết chứng nhận:

- coi tiện ích chính thức, giao diện mặc định hoặc điều chỉnh trên giấy là đủ mà không có phân tích sự tham gia thực chất có thể đánh giá;
- chứng nhận tiếp tục dựa vào hệ thống trong khi các rào cản tham gia đã ghi nhận đe dọa trọng yếu sự thẳng hàng với Hiến pháp;
- dùng cách đóng khung về chi phí, lựa chọn thiết kế, lớp nền tảng hoặc quy mô vận hành để vô hiệu hóa sàn tham gia mà không đáp ứng các phép thử **Tính cần thiết** và **Tính tương xứng** của **Điều VI-D** (*Khả năng tiếp cận*); và
- thiết kế vận hành có tác động làm thất bại khả năng tiếp cận dù có phương án ít gây gánh nặng hơn khả thi.


<a id="56-trustworthiness-and-system-reliance-integrity-evaluation"></a>

#### 5.6 Đánh giá Độ tin cậy và Tính toàn vẹn của Sự dựa vào Hệ thống

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn: [Phần B §8](../../core_09.010_system_alignment_certification_record_process.md#8-system-certification-record) (*nội dung hồ sơ*); [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường giám sát (*Chân lý và tính toàn vẹn nhận thức luận; Độ tin cậy cùng Suy giảm Niềm tin và Sự dựa vào Gây hiểu lầm là phép đo hiến pháp*); **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*); [Độ tin cậy](../../core_05.040_band_continuity.md#trustworthiness), [Niềm tin](../../core_05.040_band_continuity.md#trust), [Suy giảm Niềm tin và Sự dựa vào Gây hiểu lầm](../../core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance), [Khả năng tranh biện](../../core_05.035_band_accountability.md#contestability), [Khắc phục và Chấn chỉnh](../../core_05.035_band_accountability.md#redress-and-remediation), [Căn chỉnh Khuyến khích](core_05_band_integrative.md#incentive-alignment), [Tính đảo ngược](../../core_05.040_band_continuity.md#reversibility), [Tính trọng yếu](../../core_05.050_band_oversight.md#materiality), [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency) và [Rủi ro](../../core_05.040_band_continuity.md#risk) (Chương Năm).
- Hạ nguồn: [§5.6.5](../../core_09.015_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*các hướng dẫn minh họa độ tin cậy*); [Phần B §8.2](../../core_09.010_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*tính toàn vẹn hồ sơ*); [Phần B §10](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh*); [Phần B §7](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes) (*lệch chuẩn về niềm tin sai, khuyến khích lệch lạc và tính toàn vẹn phục hồi*).
- Đọc cùng: **Điều XIII-A** (*Nền tảng Độ tin cậy và Khả tín*), **Điều XIII-B** (*Quyền Khắc phục và Biện pháp xử lý*) và **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) — quyền khiếu nghị và kiểm toán vẫn thuộc các điều đó; **Điều XIII-E** (*Hệ thống Tự chủ Cao và Tính toàn vẹn của Quy trình qua Trung gian Công cụ*) khi hệ thống tự chủ cao làm trung gian trọng yếu cho lộ trình quản trị hoặc xác minh; **Điều III-A** (*Sinh tồn*) khi tiếp tục dựa vào hệ thống sẽ ảnh hưởng đến quyền tiếp cận thiết yếu cho sinh tồn; [Chương Một §6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) và [Chương Một §5 Chân lý](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint).
- Các tiểu mục: [§5.6.1](#561-materiality-trigger-and-governing-rules) (*điều kiện kích hoạt tính trọng yếu và quy tắc điều chỉnh*); [§5.6.2](#562-evaluation-requirement) (*yêu cầu đánh giá*); [§5.6.3](#563-system-class-scaling-and-escalation) (*phân cấp và nâng mức theo lớp hệ thống*); [§5.6.4](#564-defects-and-misalignment) (*khiếm khuyết và lệch chuẩn*); [§5.6.5](../../core_09.015_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*áp dụng minh họa độ tin cậy theo lớp hệ thống*).

</details>

<br>

*Nói đơn giản: khi một hệ thống ảnh hưởng trọng yếu đến việc hữu tri có thể tin vào điều nó nói và làm — và phản đối khi niềm tin ấy thất bại — chứng nhận phải kiểm tra xem sự dựa vào có thực sự chính đáng, được công bố trung thực và có thể khắc phục hay không. Chỉ số độ tin cậy và thiết kế bộ kiểm thử nằm trong văn kiện khác; chứng nhận kiểm tra xem độ tin cậy, nguy cơ niềm tin sai và các lộ trình khiếu nghị đã thực sự được đánh giá khi điều kiện kích hoạt áp dụng hay chưa. Ví dụ minh họa: [§5.6.5 Áp dụng minh họa độ tin cậy theo lớp hệ thống (không bao quát hết)](../../core_09.015_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive).*

<a id="561-materiality-trigger-and-governing-rules"></a>
##### 5.6.1 Điều kiện Kích hoạt Tính trọng yếu và Quy tắc Điều chỉnh

Phần này áp dụng khi một hệ thống lớn định hình những điều mọi người trông cậy vào nó: hệ thống làm gì, giới hạn ở đâu, điều gì có thể xảy ra sai, cách khiếu nghị và cách khắc phục vấn đề. Điều này có thể xảy ra thông qua:

- các tuyên bố về độ tin cậy;
- những gì hệ thống công bố hoặc không công bố;
- cách hệ thống thực sự vận hành;
- các khuyến khích được tích hợp trong hệ thống;
- cách hệ thống phục hồi sau sự cố; hoặc
- cách tương tự khiến mọi người phụ thuộc vào nó.

Khi điều kiện kích hoạt tính trọng yếu áp dụng, chứng nhận thẳng hàng hệ thống phải đánh giá **độ tin cậy và tính toàn vẹn của sự dựa vào hệ thống** theo:

- **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*);
- [Độ tin cậy](../../core_05.040_band_continuity.md#trustworthiness); và
- [Suy giảm Niềm tin và Sự dựa vào Gây hiểu lầm](../../core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance).

<a id="562-evaluation-requirement"></a>
##### 5.6.2 Yêu cầu Đánh giá

Quy trình chứng nhận phải kiểm tra liệu mọi người có lý do chính đáng để [tin](../../core_05.040_band_continuity.md#trust) vào hệ thống và có thể dựa vào nó một cách chính xác theo **Điều XIII-A** (*Nền tảng Độ tin cậy và Khả tín*) hay không.

Đánh giá cũng phải kiểm tra liệu:

- mọi người có thể thực tế khiếu nghị hệ thống, yêu cầu xem xét lại quyết định và nhận khắc phục hay không — chứ không chỉ trên giấy (**Điều XIII-A** (*Nền tảng Độ tin cậy và Khả tín*) và **Điều XIII-B** (*Quyền Khắc phục và Biện pháp xử lý*));
- mọi người có thể bị dẫn dụ để tin hoặc dựa vào hệ thống sai cách hay không, kể cả thông qua niềm tin được tạo dựng hoặc các giới hạn không được công bố (**Điều XIII-C** (*Cấm Niềm tin Sai và Sự dựa vào Gây hiểu lầm*));
- các khuyến khích của hệ thống có thưởng cho lừa dối hoặc làm tắt hay không (**Điều XIII-D** (*Ràng buộc Căn chỉnh Khuyến khích*)); và
- khi có liên quan, hệ thống có thể phục hồi sau sự cố một cách trung thực, không che giấu sự cố hoặc âm thầm thu hẹp quyền của bất kỳ ai hay không (**Điều XIII-F** (*Nền tảng Khả năng Phục hồi và Tự sửa chữa*)).

Việc kiểm tra được phân cấp theo [Tính trọng yếu](../../core_05.050_band_oversight.md#materiality), [Sự phụ thuộc](../../core_05.040_band_continuity.md#dependency) và [Rủi ro](../../core_05.040_band_continuity.md#risk).

Đánh giá phải phản ánh tác động chức năng theo thời gian, quy mô và sự phụ thuộc, chứ không phải:

- danh tiếng, quy mô hay tiếp thị;
- nhãn bảo đảm trên danh nghĩa;
- một đoạn văn tượng trưng về độ tin cậy, trong khi huy hiệu độ tin cậy hoặc điểm nhà cung cấp thực sự quyết định ai được bố trí nhân sự hoặc thứ gì được mua;
- ý định được tuyên bố; hoặc
- chỉ riêng thành tích trước đây.

<a id="563-system-class-scaling-and-escalation"></a>
##### 5.6.3 Phân cấp và Nâng mức theo Lớp Hệ thống

Độ sâu rà soát phụ thuộc vào lớp hệ thống. Khi điều kiện kích hoạt tính trọng yếu được đáp ứng:

- Nếu chỉ số đo, cảnh báo hoặc tuyên bố phục hồi của hệ thống có thể khiến hộ gia đình hoặc người vận hành hiểu sai về nhu yếu phẩm sinh tồn (những thứ cần để sống), hồ sơ phải có bằng chứng mạnh, không chỉ lời khẳng định hệ thống đáng tin cậy. Bằng chứng phải cho thấy rằng:
  - mọi người có thể tin vào hệ thống;
  - mọi người sẽ không bị trấn an sai; và
  - hệ thống phục hồi sau sự cố một cách trung thực.
- Nếu các tuyên bố về thời gian hoạt động, ghép nối hoặc quyền ghi đè khẩn cấp (“truy cập phá kính”) quyết định mọi người có được chăm sóc lâm sàng hoặc dịch vụ khẩn cấp hay không, hồ sơ phải thể hiện những nội dung sau với độ chi tiết tương ứng mức độ trọng yếu của hệ thống:
  - mọi người có thể khiếu nghị các tuyên bố đó như thế nào; và
  - liệu mọi người có thể bị dẫn dụ để dựa vào chúng hay không.
- Khi phối hợp trở nên thiết yếu cho sinh tồn, chứng nhận phải nâng mức rà soát và xem xét lại lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation) và [Phần B §7 Kết quả Chứng nhận](../../core_09.010_system_alignment_certification_record_process.md#7-certification-outcomes). Điều này có thể bao gồm nâng hệ thống lên hướng **Class A** khi sự dựa vào gây hiểu lầm có thể cắt đứt việc phối hợp mà con người cần để sinh tồn.

<a id="564-defects-and-misalignment"></a>
##### 5.6.4 Khiếm khuyết và Lệch chuẩn

Mỗi việc sau đây phải được xem là khiếm khuyết chứng nhận:

- che khuất, trình bày sai, chia nhỏ hoặc chuyển giao các giới hạn, rủi ro hay lịch sử sự cố trọng yếu khi **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*) yêu cầu rà soát;
- coi danh tiếng, sự chứng thực, quy mô hoặc tự báo cáo của người vận hành là đủ mà không có phân tích [Độ tin cậy](../../core_05.040_band_continuity.md#trustworthiness) có thể đánh giá;
- chứng nhận tiếp tục dựa vào hệ thống trong khi niềm tin sai, khuyến khích lệch lạc, lộ trình khiếu nghị không tiếp cận được hoặc cách phục hồi che giấu sự cố đã được ghi nhận đe dọa trọng yếu sự thẳng hàng với Hiến pháp; và
- dùng cách đóng khung về hiệu quả, đổi mới hoặc an ninh để vô hiệu hóa công bố, khả năng tranh biện hoặc khắc phục mà không đáp ứng kỷ luật về độ tin cậy của **Điều XIII** (*Quyền đối với Hệ thống Đáng tin cậy*) và kỷ luật khiếu nghị của **Điều XIII-A** (*Nền tảng Độ tin cậy và Khả tín*).

<br>

*Tiếp tới quy trình diễn đàn, hồ sơ, kết quả và cầu quỹ đạo:* [Chương Tám, Phần B — Hồ sơ và Quy trình](core_07_b_system_alignment_certification_record_process.md) ([§6 Quy trình Diễn đàn](../../core_09.010_system_alignment_certification_record_process.md#6-forum-process) đến [§10 Quan hệ với Quỹ đạo](../../core_09.010_system_alignment_certification_record_process.md#10-relationship-to-standing)).

*Ví dụ minh họa cho từng lĩnh vực đánh giá:* [Chương Tám, Phần C — Minh họa](../../core_09.015_system_alignment_certification_illustrations.md).

---

**Tệp trước:** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)

**Tệp tiếp theo (ngôn ngữ này):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)

**Nguyên bản ràng buộc:** [core_07_a_system_alignment_certification_evaluation.md](../../core_09_a_system_alignment_certification_evaluation.md)
