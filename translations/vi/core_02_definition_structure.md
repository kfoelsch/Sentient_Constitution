<a id="chapter-two-definition-structure-and-component-requirements"></a>
# CHƯƠNG HAI: CẤU TRÚC ĐỊNH NGHĨA VÀ YÊU CẦU THÀNH PHẦN

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Hai tiếng Anh](../../core_02_definition_structure.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_02_definition_structure.md`](../../core_02_definition_structure.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> **Trước (ngôn ngữ này):** [core_01_c_stewardship_capacity_principles.md](core_01_c_stewardship_capacity_principles.md)
>
> **Tiếp theo (vẫn tiếng Anh):** [core_03_definition_integrity.md](../../core_03_definition_integrity.md)
> **Cung đọc:** §1 mục đích và vai trò (O/M/A/C) → §2 tính toàn vẹn định nghĩa → **§3 tính nhất quán xuyên chồng định nghĩa**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): chồng định nghĩa và nơi Chương Hai sống</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Chương **Hai đến Năm** tạo chồng định nghĩa hiến pháp; **[CJS](../../corpus_joint_structure.md)** mang các định nghĩa vận hành áp dụng chồng đó:
> - **Chương Hai (tệp này)** — cấu trúc định nghĩa O/M/A/C và thẳng hàng thành phần: mỗi định nghĩa liên kết **Bản thể (O)** (nó là gì), sổ **Đo lường (M)** đan với nghĩa vụ **Đánh giá (A)** (cách phải đo và đánh giá), và **Tuân thủ (C)** (điều phải giữ) ([§1 Mục đích và vai trò](core_02_definition_structure.md#1-purpose-and-role); [§2 Yêu cầu tính toàn vẹn định nghĩa](core_02_definition_structure.md#2-definition-integrity-requirement)).
> - **Chương Ba** — tính toàn vẹn định nghĩa, lẩn tránh, và không tuân thủ ([Chương Ba](../../core_03_definition_integrity.md#chapter-three-definition-integrity-evasion-and-non-compliance)).
> - **Chương Bốn** — gánh chứng minh, truy vết định nghĩa, khả năng quan sát, xác minh dưới giới hạn an ninh, và khả năng tiếp cận xác minh ([Chương Bốn — Gánh chứng minh, truy vết, và xác minh](../../core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification)).
> - **Chương Năm** — từ vựng chung cho đo lường, đánh giá, và tuân thủ (định nghĩa độc lập, theo cụm, và theo gói ở các mục 1–3 xuyên năm tệp dải Tứ diện và các tệp mục tiêu hiến pháp: [Mục tiêu Hưng thịnh](../../core_05_apex_flourishing_aim.md), [Giám sát](../../core_05_band_oversight.md), [Tham gia](../../core_05_band_participation.md), [Trách nhiệm giải trình](../../core_05_band_accountability.md), [Liên tục](../../core_05_band_continuity.md), [Tích hợp](../../core_05_band_integrative.md)); thứ tự đọc và bản đồ ở [Phần A](../../core_05__definitions_home.md#chapter-five-compass-and-definition-map).
> - **CJS** — định nghĩa vận hành cho thuật ngữ xuyên triển khai ([CJS-3](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map) thư viện cụm vận hành); áp dụng các nhà chuẩn Chương Năm — không định nghĩa lại chúng. Phân loại miền và giao thức ở **CS**, **CI**, và **CF** theo cùng quy tắc.
>
> Điều hướng thêm:
> - **Quy tắc chống dời chỗ:** luồng quy trình thủ tục, cơ chế cưỡng chế, và lược đồ phân loại ngoài phạm vi định nghĩa không được hút vào chương này.

</details>

<br>

Chương Hai là chủ sở hữu hiến pháp của **cấu trúc định nghĩa và thẳng hàng thành phần**.

*Nói thẳng: Chương Hai đến Năm là chồng định nghĩa hiến pháp — xây (Hai), giữ trung thực (Ba), kiểm (Bốn), đặt tên (Năm). Chương Hai xây mỗi định nghĩa từ các phần liên kết — một thuật ngữ là gì (O), cách phải đo và đánh giá (sổ đo lường đan với đánh giá, M/A), và điều phải giữ trong thực tế (C). Định nghĩa vận hành xuyên triển khai sống ở [CJS](../../corpus_joint_structure.md) ([CJS-3 — Thuật ngữ vận hành xuyên triển khai](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map)); chúng áp dụng thuật ngữ Chương Năm và không định nghĩa lại chúng.*

<br>


<a id="1-purpose-and-role"></a>
### 1. Mục đích và vai trò
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Lời nói đầu §1 Mô hình](core_00_preamble.md#the-model) — [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad), [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims), và chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake) áp dụng xuyên chương qua dấu vết mục; [Chương Một §1 Mục đích và vai trò](core_01_a_values_principles.md#1-purpose-and-role) (*giá trị và ràng buộc chồng định nghĩa này phục vụ*).
- Thượng nguồn: [Mở Chương Hai](#chapter-two-definition-structure-and-component-requirements) — phân rã O/M/A/C và yêu cầu thẳng hàng nội bộ.
- Trụ Tứ diện: **giám sát**, **trách nhiệm giải trình** (các định nghĩa phải đánh giá được và cưỡng chế được trên hành vi quan sát được). Mục tiêu chính: **Hưng thịnh** và **Liên tục**. Chia tỷ lệ theo [lợi hại vật chất](core_00_preamble.md#material-stake) áp dụng xuyên chương.
- Hạ nguồn: [§1.2 Thành phần đo lường](#12-measurement-components) và [§1.3 Thành phần đánh giá](#13-assessment-components) (*sổ Đo lường (M) đan với nghĩa vụ đánh giá; hình dạng đầu vào O/M/A/C trong chương này*); [§2 Yêu cầu tính toàn vẹn định nghĩa](#2-definition-integrity-requirement); [Chương Ba, mục 1 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](../../core_03_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints); [Chương Bốn, mục 1 — Cưỡng chế độc quyền và phân bổ gánh](../../core_04_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation); [la bàn và bản đồ định nghĩa Chương Năm](../../core_05__definitions_home.md#chapter-five-compass-and-definition-map).
- Đọc cùng: [Lời nói đầu — sổ đăng ký chủ sở hữu hiến pháp](core_00_preamble.md#4-principles-definitions-and-rights) và [Chồng thẩm quyền và thứ bậc nội bộ](../../core_05_band_integrative.md#authority-stack); [Ràng buộc hiến pháp](../../core_05_band_integrative.md#constitutional-constraint) — cưỡng chế, quản trị, triển khai, đo lường, kiểm toán, và cơ chế phân loại sau phải tuân; [CJS-3.1 La bàn hiến pháp và bản đồ cụm](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map) — các định nghĩa vận hành áp dụng, và **không được** định nghĩa lại, các nhà chuẩn Chương Năm.

</details>

<br>

*Nói thẳng: mục này là mô tả việc của Chương Hai. Nó nắm tầng đầu của chồng định nghĩa: mọi định nghĩa hiến pháp được xây từ các phần liên kết — một thuật ngữ là gì (O), cách phải đo và đánh giá (sổ Đo lường đan với đánh giá, M/E), và điều phải giữ trong thực tế (C) — và những phần đó phải giữ thẳng hàng. Thỏa một phần trong khi lách phần khác không được tính. Vận hành cưỡng chế, quản trị, và đo lường sống ở các chương sau và phải tuân điều chương này lập.*

Mọi định nghĩa hiến pháp **phải** được xây từ các phần liên kết, mỗi phần đúng một việc:
- **Bản thể (O)** — thuật ngữ nói về gì.
- **Đo lường (M)** — thước nào áp dụng ở mỗi bậc. Định tuyến đo lường chỉ hướng đánh giá; nó không đặt kết quả đạt/không đạt.
- **Đánh giá (A)** — cách thuật ngữ phải được đánh giá. Ở các định nghĩa lá Chương Năm, sổ **Đo lường (M)** được đan vào thành phần **Đánh giá (A)**. Xem [§1.3 Thành phần đánh giá](#13-assessment-components).
- **Tuân thủ (C)** — điều phải đúng trong thực tế.

Những phần đó **phải** giữ nhất quán trong mỗi định nghĩa. Cưỡng chế, quản trị, triển khai, vận hành đo lường, kiểm toán, và cơ chế phân loại ngoài phạm vi định nghĩa thuộc các chương sau; chúng **phải** tuân các [Ràng buộc hiến pháp](../../core_05_band_integrative.md#constitutional-constraint) lập ở đây.

Mọi định nghĩa **phải** được thỏa cho toàn hệ thống như nó thực sự chạy — kể cả hệ thống trải trên hữu tri, máy, và địa điểm. Các phần O, M, A, và C **phải** đều đạt cùng nhau, trên cùng phạm vi và dưới cùng điều kiện thử. Đạt một phần bằng cách cắt lát hệ thống, thu hẹp điều được tính, hoặc làm yếu phần khác thì không được tính.

<a id="11-ontological-components-o--what-it-is"></a>
<a id="11-ontological-components-o-what-it-is"></a>
#### 1.1 Thành phần bản thể (O) — Nó là gì

*Nói thẳng: phần O trả một câu hỏi đơn — **thuật ngữ này nói về gì?** Nó đặt tên sự vật và vẽ mép. Nó không nói cách đo hoặc xét thuật ngữ, và không nói điều gì được tính là đạt hoặc không đạt; những cái đó đến sau.*

Phần Bản thể (O) mô tả thuật ngữ nói về gì. Nó không được nói cách đo hoặc đánh giá thuật ngữ, và không được nói điều gì được tính là đạt hoặc không đạt — những cái đó sống ở các phần Đo lường (M), Đánh giá (A), và Tuân thủ (C). Nó cũng phải khớp cách hệ thống thực sự làm việc: một tên, một hạng mục chính thức, một phạm vi thẩm quyền, hoặc một mục đích đã nêu không chốt điều một thuật ngữ phủ khi hành vi thực hoặc hiệu ứng thực nói khác.

Trên một định nghĩa, phần O được viết như một danh sách ngắn các trường gắn nhãn. Mỗi trường trả một câu hỏi thẳng:

- **Trong phạm vi:** điều thuật ngữ *có* phủ. Mục này liệt kê các phần thực của hệ thống, cách chúng làm việc cùng nhau, chúng dựa vào gì, và các hiệu ứng thực sự quan trọng đối với thuật ngữ này.
- **Ngoài phạm vi:** điều thuật ngữ *không* phủ. Nêu khái niệm kề, nhà anh em, hoặc trường hợp thường ngoài vấn đề — không phải nhãn rỗng, thay thế trên giấy, hoặc khung không tuân thủ khác. Những cái đó thuộc C (**Thất bại sơ cấp**).
- **Phụ thuộc vào:** *(dùng chỉ khi áp dụng)* bất kỳ thứ *khác* đã định nghĩa mà thuật ngữ này xây trên — ví dụ một giới hạn, một sàn tối thiểu, hoặc một mục tiêu nó giả định đã có chỗ. Nếu thuật ngữ chỉ có nghĩa khi thứ kia đã tồn tại, nó được nêu ở đây.

Một số thứ cố ý **không** vào phần O:

- điều thuật ngữ *nuôi vào*, hoặc nhóm lớn hơn nó *nằm trong* — cái đó thuộc tham chiếu chéo của định nghĩa, không phải đây;
- cách thuật ngữ được đo hoặc đánh giá — cái đó thuộc M và A;
- điều gì được tính là thỏa hoặc phá thuật ngữ — cái đó thuộc C, kể cả nhãn hoặc giấy tờ tuyên thỏa mà không có hiệu ứng thực.

Các định nghĩa lá Chương Năm phải mang những yêu cầu O đó bằng hình dạng thành phần Bản thể nêu trong mục này.

<a id="12-measurement-components"></a>
<a id="12-measurement-components-m--how-it-must-be-measured"></a>
<a id="12-measurement-components-m-how-it-must-be-measured"></a>
#### 1.2 Thành phần đo lường (M) — Cách phải đo

*Nói thẳng: phần M trả một câu hỏi đơn — **chúng ta nên nhìn gì để xét thuật ngữ này?** Nó nêu các thước áp dụng. Nó không nói thuật ngữ đạt hay không đạt; cái đó đến sau.*

Phần Đo lường (M) nói thước nào áp dụng cho một thuật ngữ ở mỗi bậc. Nó chỉ đánh giá về bằng chứng đúng. Nó không được nói điều gì được tính là đạt hoặc không đạt — cái đó chỉ thuộc phần Tuân thủ (C).

Ở các định nghĩa lá Chương Năm, M được đan vào phần Đánh giá (A) dưới tiêu đề hướng người đọc **Cách đo và đánh giá**. Mỗi bậc nêu thước của nó trước, rồi đánh giá khớp trên dòng ngay dưới. Các trường làm việc như sau:

- **Thước sơ cấp:** thứ chính cần nhìn trước — vết bằng chứng đầu người đánh giá nên theo cho thuật ngữ này trong ngữ cảnh này.
- **Thước thứ cấp:** *(dùng khi áp dụng)* các thước thêm **phải** được gồm cạnh thước sơ cấp — không phải phần thêm tùy chọn. Chúng mở rộng kiểm để một vấn đề không thể ẩn sau một lát bằng chứng hẹp.
- **Thước tam cấp:** *(dùng khi áp dụng)* kiểm tính toàn vẹn trên chính các thước — đặc biệt nơi số, nhãn, tự báo cáo, hoặc hạng mục hình thức có thể đứng thay kết quả thực.

Không mọi định nghĩa cần cả ba bậc. Một số thuật ngữ chỉ nêu thước sơ cấp; số khác thêm thước thứ cấp hoặc tam cấp khi thuật ngữ cần kiểm rộng hơn hoặc sâu hơn.

Một số thứ cố ý **không** vào phần M:

- điều gì được tính là thỏa hoặc phá thuật ngữ — cái đó thuộc C;
- thuật ngữ nói về gì — cái đó thuộc O;
- toàn bộ nghĩa vụ đánh giá một mình — cái đó thuộc A (dù mỗi thước được ghép với đánh giá của nó trên dòng ngay dưới).

Các định nghĩa lá Chương Năm phải mang những yêu cầu M đó bằng hình dạng thành phần Đo lường nêu trong mục này.

<a id="13-assessment-components"></a>
<a id="13-assessment-components-a--how-it-must-be-assessed"></a>
<a id="13-assessment-components-a-how-it-must-be-assessed"></a>
#### 1.3 Thành phần đánh giá (A) — Cách phải đánh giá
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: [Mở Chương Hai](#chapter-two-definition-structure-and-component-requirements); [§1 Mục đích và vai trò](#1-purpose-and-role) — vai trò thành phần A trong phân rã O/M/A/C.
- Hạ nguồn: [Chương Ba, mục 1 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](../../core_03_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints); [Chương Bốn, mục 1 — Cưỡng chế độc quyền và phân bổ gánh](../../core_04_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation) — đường dẫn cưỡng chế độc quyền cho yêu cầu đánh giá định nghĩa ở Chương Hai và Ba; [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](../../core_04_burden_traceability_verification.md#5-compliance-evidence-standard) — đủ bằng chứng cho cưỡng chế đó.
- Đọc cùng: [Định nghĩa độc lập Chương Năm](../../core_05__definitions_home.md#1-interdependent-definitions) — định nghĩa áp dụng quản trị phạm vi và điều kiện đánh giá; yêu cầu đánh giá áp dụng nhất quán với mọi định nghĩa Chương Năm áp dụng trong phạm vi tiếp nhận của nó.

</details>

<br>

*Nói thẳng: phần A trả một câu hỏi đơn — **thuật ngữ này phải được xét thế nào?** Nó nói người đánh giá phải nhìn gì, dưới điều kiện nào, và cách xử bất định. Nó không nói thuật ngữ đạt hay không đạt; cái đó đến sau.*

Phần Đánh giá (A) nói một định nghĩa phải được đánh giá thế nào. Nó không được nói điều gì được tính là đạt hoặc không đạt — cái đó chỉ thuộc phần Tuân thủ (C).

Ở các định nghĩa thuật ngữ đơn lẻ Chương Năm, đo lường (M) và đánh giá (A) xuất hiện cùng nhau trong một mục mang tiêu đề **Cách đo và đánh giá**.

Trong mục đó, mỗi bậc là một cặp: thước đi trước, và đánh giá cho thước đó nằm trên dòng ngay dưới. Các trường đánh giá là:

- **Đánh giá sơ cấp:** cách xét thước sơ cấp — người đánh giá phải đánh giá gì trước, và kiểm đó phải thực sự với tới gì (nội dung, không chỉ nhãn hoặc giấy tờ).
- **Đánh giá thứ cấp:** *(dùng khi áp dụng)* cách xét các thước thứ cấp — điều phải được gồm khi thước sơ cấp trông ổn nhưng bằng chứng rộng hơn vẫn quan trọng.
- **Đánh giá tam cấp:** *(dùng khi áp dụng)* cách xét các thước tam cấp — kiểm xem chỉ số thay thế, chỉ số, hoặc hạng mục hình thức còn theo dõi kết quả thực không.

Xuyên mọi bậc, phần A phải:

- nói điều gì phải được đánh giá;
- nói dưới điều kiện nào đánh giá phải xảy ra;
- nói cách xử bất định nơi nó quan trọng.

Một số thứ cố ý **không** vào phần A:

- điều gì được tính là thỏa hoặc phá thuật ngữ — cái đó thuộc C;
- thuật ngữ nói về gì — cái đó thuộc O;
- thước nào áp dụng ở mỗi bậc một mình — cái đó thuộc M (dù mỗi thước được ghép với đánh giá của nó trên dòng ngay dưới).

Các định nghĩa lá Chương Năm phải mang những yêu cầu A đó bằng hình dạng thành phần Đánh giá nêu trong mục này.

Khi những quy tắc đánh giá này được đưa ra thử, việc xét phải dựa trên đủ bằng chứng thực — không phải trên tuyên bố hoặc giấy tờ một mình — và cùng quy tắc phải áp dụng mỗi nơi thuật ngữ áp dụng.

<a id="14-compliance-components-c--what-must-be-true-in-practice"></a>
<a id="14-compliance-components-c-what-must-be-true-in-practice"></a>
#### 1.4 Thành phần tuân thủ (C) — Điều phải đúng trong thực tế

*Nói thẳng: phần C trả một câu hỏi đơn — **điều gì phải thực sự đứng, và khi nào thuật ngữ này đã bị phá?** Nó nêu các điều kiện thế giới thực phải được thỏa và các thất bại được tính — dựa trên điều có thể thấy trong hành vi và hiệu ứng, không trên điều hệ thống tuyên về chính nó.*

Phần Tuân thủ (C) nêu các điều kiện thế giới thực phải đứng để một thuật ngữ được thỏa. Nó phải làm việc từ hành vi và hiệu ứng quan sát được — không từ tuyên của chính hệ thống, giấy tờ, hoặc ý định đã nêu.

Ở các định nghĩa thuật ngữ đơn lẻ Chương Năm, phần Tuân thủ (C) xuất hiện dưới tiêu đề **Điều phải đứng**. Các trường làm việc như sau:

- **Thất bại sơ cấp:** khi thuật ngữ bị phá ở bậc sơ cấp — ví dụ khi thước chính rỗng, không truy được, hoặc bị mâu thuẫn bởi cách hệ thống thực sự làm việc.
- **Thất bại thứ cấp:** *(dùng khi áp dụng)* khi thuật ngữ bị phá ở bậc thứ cấp — ví dụ khi kiểm sơ cấp trông ổn định nhưng thứ gì rộng hơn vẫn đánh bại thuật ngữ, như một đổ vỡ trong hệ thống nó phụ thuộc hoặc một hệ thống kết nối nó tương tác.
- **Thất bại tam cấp:** *(dùng khi áp dụng)* khi thuật ngữ bị phá ở bậc tam cấp — ví dụ khi một chỉ số thay thế hoặc chỉ số được coi đủ một mình, hoặc khi lệch đã biết bị bỏ qua hoặc để không sửa.

Không mọi định nghĩa liệt kê cả ba bậc thất bại. Một số thuật ngữ chỉ nêu thất bại sơ cấp; số khác thêm thất bại thứ cấp hoặc tam cấp khi thuật ngữ cần điều kiện phá khớp bậc.

Xuyên mọi bậc, phần C phải:

- nêu kết quả có thể quan sát và cưỡng chế;
- nêu khi định nghĩa được thỏa hoặc bị vi phạm;
- giữ gắn với hành vi và hiệu ứng thực, không với nhãn, hạng mục hình thức, hoặc mục đích đã nêu một mình.

Một số thứ cố ý **không** vào phần C:

- thuật ngữ nói về gì — cái đó thuộc O;
- thước nào áp dụng hoặc đánh giá phải chạy thế nào — cái đó thuộc M và A.

Các định nghĩa lá Chương Năm phải mang những yêu cầu C đó bằng hình dạng thành phần Tuân thủ nêu trong mục này.

<a id="2-definition-integrity-requirement"></a>
### 2. Yêu cầu tính toàn vẹn định nghĩa
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [§1 Mục đích và vai trò](#1-purpose-and-role) — cấu trúc thành phần O/M/A/C và quy tắc thỏa cùng toàn hệ thống.
- Hạ nguồn: [§2.4 Quy tắc diễn giải khi mơ hồ](#24-interpretation-rule-under-ambiguity); [§3 Tính nhất quán xuyên chồng định nghĩa](#3-consistency-across-the-definition-stack); [Chương Ba, mục 1 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](../../core_03_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints); [Chương Bốn, mục 1 — Cưỡng chế độc quyền và phân bổ gánh](../../core_04_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation); [Chương Bốn, mục 5 — Chuẩn bằng chứng tuân thủ](../../core_04_burden_traceability_verification.md#5-compliance-evidence-standard).
- Đọc cùng: [Định nghĩa cụm Chương Năm (Thận trọng khả năng thấy trước)](../../core_05_band_oversight.md#foreseeability-diligence) — nghĩa vận hành cho mọi «thấy trước được một cách hợp lý» ở Chương Hai đến Bốn.

</details>

<br>

*Nói thẳng: xây một định nghĩa đúng chưa đủ — nó phải còn nguyên khi áp dụng. Định nghĩa không thể được thỏa từng mảnh, bị làm yếu bởi diễn giải, hay bị chơi qua cắt lát phạm vi — kể cả bằng tối ưu một thước trong khi kết quả nó đại diện suy. Nơi ngôn ngữ cho hơn một cách đọc, chọn cách giữ phạm vi bảo vệ đầy đủ.*

<a id="21-core-integrity-conditions"></a>
#### 2.1 Điều kiện toàn vẹn cốt lõi
Mọi định nghĩa phải đứng cùng nhau khi áp dụng. Các phần liên kết đòi bởi [§1 Mục đích và vai trò](#1-purpose-and-role) phải:
- vẫn khớp nhau
- đều được thỏa cùng nhau; thỏa một hoặc hai phần thì chưa đủ
- được thỏa trên cùng hệ thống và dưới cùng điều kiện — không thể đạt một phần trên một lát hẹp và phần khác trên một lát khác

Thất bại bất kỳ phần nào nghĩa là định nghĩa không được thỏa.

<a id="22-non-compliance-by-structural-or-applied-weakening"></a>
#### 2.2 Không tuân thủ do làm yếu cấu trúc hoặc áp dụng
Một định nghĩa không được thỏa nếu cách nó được xây, đọc, hoặc áp dụng cho phép một phần được thỏa trong khi:
- hạ, lách, hoặc va với phần khác
- sản sinh kết quả sẽ không thỏa nghĩa đầy đủ của định nghĩa, đánh giá, và yêu cầu thế giới thực khi toàn hệ thống đang chạy
- cho phép đạt chỉ một phần, chỉ cho trường hợp chọn, hoặc chỉ dưới điều kiện nhất định — các lần đạt sẽ không đứng dưới các điều kiện định nghĩa thực sự đòi

<a id="23-construction-constraints"></a>
#### 2.3 Ràng buộc xây dựng
Các định nghĩa phải được viết sao cho:
- mọi phần (O, M, E, C) chỉ có thể được thỏa cùng nhau dưới điều kiện phản ánh cách hệ thống thực sự hành xử và điều nó thực sự sản sinh
- không phần nào có thể được thỏa bằng khái quát hóa, tách sự vật, thu hẹp phạm vi, hoặc mô tả chúng theo cách bỏ ra phần tử hệ thống, tương tác, hoặc hiệu ứng thực sự quan trọng
- không thước nào đứng thay kết quả nó nhằm nắm; một thước lệch khỏi kết quả thế giới thực nó đại diện (xem [Lệch chỉ số thay thế](../../core_05_band_oversight.md#proxy-divergence)) không thể thỏa định nghĩa, và lựa chọn thước không được co điều phải được đánh giá hay điều phải đứng trong thực tế
- không giả định không nêu, phụ thuộc ẩn, hoặc điều kiện bỏ sót được đổi hoặc làm yếu điều phải được đánh giá hay điều phải đứng trong thực tế

<a id="24-interpretation-rule-under-ambiguity"></a>
#### 2.4 Quy tắc diễn giải khi mơ hồ
Khi một định nghĩa có thể được đọc hơn một cách hợp lý, dùng cách đọc giữ nghĩa đầy đủ của nó. Cách đọc đó quản trị cách định nghĩa được áp dụng. Cách đọc cũng phải giữ đánh giá nghiêm, và phải giữ nguyên các yêu cầu thế giới thực.

Một định nghĩa không được dùng để xét hoặc quyết tuân thủ nếu áp dụng nó buộc một mâu thuẫn trong định nghĩa, một khe giữa phạm vi nó nêu và điều thực sự phải được phủ, hoặc một lần đạt trên một phần trong khi phần đòi khác bị lách.

Một định nghĩa gãy là không tuân thủ tự nó. Điều đó đứng ngay khi hệ thống trông như đang hành xử ổn và ngay khi chưa có gì sai.

Nếu một cách đọc hợp lý sẽ làm yếu bảo vệ, thu hẹp điều phải được kiểm, hoặc hạ kết quả thế giới thực đòi so với một cách đọc khác mà diễn đạt và cấu trúc cho phép, cách đọc yếu hơn đó không được phép.

<a id="3-consistency-across-the-definition-stack"></a>
### 3. Tính nhất quán xuyên chồng định nghĩa
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: [§2 Yêu cầu tính toàn vẹn định nghĩa](#2-definition-integrity-requirement); [§1 Mục đích và vai trò](#1-purpose-and-role).
- Hạ nguồn: [Chương Ba, mục 2 — Không tuân thủ từ hành vi hệ thống quan sát được](../../core_03_definition_integrity.md#2-non-compliance-from-observable-system-behavior); [Chương Bốn, mục 2 — Yêu cầu truy vết định nghĩa](../../core_04_burden_traceability_verification.md#2-definition-traceability-requirement); các mục **4.1**, **3**, **5**, và **6** của Chương Bốn nơi «thấy trước được một cách hợp lý» xuất hiện mà không có con trỏ nội tuyến tới Chương Năm.
- Đọc cùng: [Định nghĩa cụm Chương Năm (Thận trọng khả năng thấy trước)](../../core_05_band_oversight.md#foreseeability-diligence) — quy tắc quản trị mọi «thấy trước được một cách hợp lý» ở Chương Hai đến Bốn; nghĩa vận hành ở [Thấy trước được một cách hợp lý](../../core_05_band_oversight.md#reasonably-foreseeable) (Chương Năm, mục 3 — Cụm phụ thuộc (cụm Sự thật và tính toàn vẹn nhận thức; Thận trọng khả năng thấy trước)).

</details>

<strong><span style="color: #2563eb;">Định nghĩa:</span></strong> [Khả năng thấy trước](../../core_05_band_oversight.md#foreseeability-diligence) · [O](../../core_05_band_oversight.md#foreseeability-diligence) · [M](../../core_05_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05_band_oversight.md#foreseeability-diligence-c)

*Nói thẳng: một định nghĩa không chỉ phải đứng cùng nhau trên giấy — nó phải đứng cùng nhau xuyên chồng định nghĩa trong thế giới thực. Các phần của nó phải thẳng hàng cùng cách xuyên vận hành bình thường, suy giảm, và đối kháng, theo thời gian, xuyên hệ thống kết nối, trong mọi tình huống bạn có thể thấy trước hợp lý, và dưới mọi cách đọc công bằng các từ của nó.*

Mỗi nơi «thấy trước được một cách hợp lý» xuất hiện bất kỳ đâu trong **Chương Hai đến Bốn**, nó nghĩa đúng điều các định nghĩa Khả năng thấy trước ở Chương Năm, mục 3 — Cụm phụ thuộc (cụm Sự thật và tính toàn vẹn nhận thức; Thận trọng khả năng thấy trước) nói — không lỏng hơn. Mỗi lần dùng phải chỉ rõ trở lại những định nghĩa đó.

Các phần của một định nghĩa phải giữ nhất quán xuyên:
- toàn bộ dải điều kiện hệ thống chạy dưới — kể cả vận hành bình thường, vận hành suy giảm, áp lực đối kháng, thay đổi theo thời gian, và tương tác với hệ thống khác, nơi những cái đó quan trọng.
- mọi điều kiện thấy trước được một cách hợp lý, như nêu ở Chương Năm, mục 3 — Cụm phụ thuộc (cụm Sự thật và tính toàn vẹn nhận thức; Thận trọng khả năng thấy trước) (Khả năng thấy trước)
- mọi cách đọc hợp lý mà diễn đạt và cấu trúc của định nghĩa cho phép

---

**Tệp trước:** [core_01_c_stewardship_capacity_principles.md](core_01_c_stewardship_capacity_principles.md)

**Tệp tiếp theo (vẫn tiếng Anh):** [core_03_definition_integrity.md](../../core_03_definition_integrity.md)

**Nguyên bản ràng buộc:** [core_02_definition_structure.md](../../core_02_definition_structure.md)
