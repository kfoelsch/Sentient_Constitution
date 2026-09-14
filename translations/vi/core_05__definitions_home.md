<a id="chapter-five-foundational-definitions"></a>
# CHƯƠNG NĂM: ĐỊNH NGHĨA NỀN TẢNG

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Năm, Phần A tiếng Anh](../../core_05__definitions_home.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_05__definitions_home.md`](../../core_05__definitions_home.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> **Trước (ngôn ngữ này):** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)
>
> **Tiếp theo (ngôn ngữ này):** [core_05_apex_accountability_leg.md](core_05_apex_accountability_leg.md)
> **Cung đọc:** nhà chuẩn → §1 định nghĩa độc lập → §2 quy tắc meta cụm phụ thuộc → mục lục A-Z → la bàn → đối chiếu đo lường.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): thứ tự đọc và ghi chú ngôn ngữ thường</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở chương này hay ở các chương khác.
>
> Ghi chú đọc ngôn ngữ thường: đọc **Chương Một** cho giá trị và hướng tầng cao; **Chương Hai đến Bốn** cho cấu trúc định nghĩa, tính toàn vẹn, và cơ học xác minh; và **Chương Sáu** cho sàn **quyền** nền tảng, rồi trở lại chương này cho độ chính xác thuật ngữ trong diễn giải, kiểm toán, và phân xử. (Các chương khác, kể cả **Chương Mười** *Hành vi sai* và **Chương Tám** *Quỹ đạo*, áp dụng trên đường đọc riêng của chúng; chúng không thay Sàn Quyền Chương Sáu hay cơ học định nghĩa của Chương Hai đến Bốn.)

</details>

<br>

*Nói thẳng: chương này là từ điển. Mỗi thuật ngữ được định nghĩa có một nhà chính thức; các chương sau áp dụng những thuật ngữ đó, không lặng lẽ định nghĩa lại chúng.*

<a id="canonical-home-and-non-duplication-rule"></a>
### Nhà chuẩn và quy tắc không trùng lặp
*Nói thẳng: mỗi thuật ngữ được định nghĩa có một nhà chính thức. Nhà đó quyết nghĩa thuật ngữ. Các tệp khác có thể áp dụng thuật ngữ, nhưng không được lặng lẽ định nghĩa lại nó.*

- Mỗi định nghĩa hiến pháp, mô tả định nghĩa, và khái niệm truy vết theo cụm phải có một **nhà chuẩn** trong kho văn bản này — một chỗ chính thức kiểm soát thuật ngữ nghĩa gì, nó đi tới đâu, và điều gì được tính là thỏa nó.
  - Không văn bản được hợp nhất hay triển khai nào được tạo một định nghĩa thứ hai, một giải thích cạnh tranh, hoặc một phát biểu lại hẹp hơn của một thuật ngữ mà nhà chuẩn đã được gán bởi Hiến pháp này hoặc bởi bản đồ kiến trúc kho văn bản được tiếp nhận dưới nó.
- Văn bản triển khai được hợp nhất chỉ được đưa một thuật ngữ chuẩn vào việc bằng cách chỉ ngược về nhà đó rồi nêu tiêu chí, thủ tục, phân loại, kiểm soát, hoặc điều kiện riêng tầng bên trong phạm vi được gán của nó.
  - Nếu văn bản đó dùng nhãn địa phương hoặc viết tắt, nó phải nói rõ. Lời địa phương đó không phải định nghĩa mới của thuật ngữ. Nó chỉ trở thành ngôn ngữ định nghĩa chính thức nếu nhà chuẩn của thuật ngữ sau đó tiếp nhận nó.
- Nếu lời ngoài nhà chuẩn có vẻ mở rộng, thu hẹp, thay, hoặc cạnh tranh với định nghĩa chuẩn, định nghĩa chuẩn quản trị. Đọc lời ngoài đó như chi tiết triển khai nếu bạn có thể. Nếu không thể, lời cạnh tranh không áp dụng ở mức xung đột.

---

<a id="1-interdependent-definitions"></a>
<a id="1-independent-definitions"></a>

### 1. Định nghĩa độc lập

*Nói thẳng: định nghĩa độc lập là khối xây dùng lại được. Chúng đứng một mình trừ khi một cụm đòi chúng phải được thỏa cùng nhau.*

Định nghĩa độc lập là khối xây ngữ nghĩa dùng lại được, có thể được viện xuyên nhiều định nghĩa. Chúng định nghĩa các kiến trúc chung về bản thể, đo lường, đánh giá, và tuân thủ. Áp dụng chúng ở mọi nơi chúng có trọng liên quan tới hành vi hệ thống, kết quả, phạm vi đánh giá, hoặc xác định tuân thủ.

Định nghĩa Độc lập và Bán độc lập không đòi thỏa chung với các định nghĩa khác trừ khi một định nghĩa cụm phụ thuộc đòi rõ ([mục 2 — Quy tắc meta cụm phụ thuộc](#2-dependent-cluster-meta-rules)). [§1.1 Viện, thỏa, và tuân thủ](#11-invocation-satisfaction-and-compliance) áp dụng mỗi khi một Định nghĩa độc lập được viện.

<a id="11-invocation-satisfaction-and-compliance"></a>

#### 1.1 Viện, thỏa, và tuân thủ
*Nói thẳng: khi một định nghĩa độc lập áp dụng, nó phải được thỏa đầy — không chọn các mảnh tiện.*

Thất viện hoặc thất áp dụng đúng bất kỳ Định nghĩa độc lập nào được đòi có trọng làm mất hiệu lực xác định tuân thủ gắn với nó. Mọi Định nghĩa độc lập được viện trong đánh giá hệ thống phải xuất hiện rõ trong các bản đồ Truy vết định nghĩa (Chương Bốn, mục 2 — Yêu cầu truy vết định nghĩa). Những bản đồ đó phải gồm các thành phần Bản thể (O), Đo lường (M), Đánh giá (A), và Tuân thủ (C). Truy vết phải cho thấy mỗi Định nghĩa độc lập được viện đóng góp thế nào vào hành vi hệ thống quan sát được và vào kết quả tuân thủ dưới điều kiện chức năng đầy của hệ thống.

Khi một Định nghĩa độc lập được viện, nó phải được thỏa đầy xuyên các thành phần O, M, A, và C. Việc thỏa đó phải nhất quán với Yêu cầu cấu trúc định nghĩa (Chương Hai, §1 — Mục đích và vai trò). Thỏa một phần hoặc áp dụng chọn lọc là không tuân thủ.

Định nghĩa độc lập vẫn phải được áp dụng nhất quán với mọi định nghĩa áp dụng dưới cùng phạm vi chức năng hệ thống, cùng điều kiện đánh giá, và cùng ngữ cảnh thời gian. Chương Ba, mục 1 và 2 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh; Không tuân thủ từ hành vi hệ thống quan sát được — đòi sự nhất quán đó.

Viện chọn lọc, bỏ định nghĩa có trọng liên quan, và áp dụng làm đổi, làm yếu, hoặc đi vòng xác định tuân thủ là lẩn tránh. Chương Ba, mục 1 và 2 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh; Không tuân thủ từ hành vi hệ thống quan sát được — quản trị hành vi đó.

Định nghĩa độc lập không được phân mảnh, cô lập, hay phân phối lại tuân thủ theo cách chặn đánh giá toàn hệ thống dưới các điều kiện đánh giá đòi.

---


<a id="2-dependent-cluster-meta-rules"></a>
### 2. Quy tắc meta cụm phụ thuộc

*Nói thẳng: các thành viên cụm phải được đọc và thỏa cùng nhau — không thành viên nào là đường tắt tự đứng quanh các yêu cầu chung.*

Một **cụm phụ thuộc** là một nhóm định nghĩa phải được thỏa cùng nhau, trong phạm vi mỗi cụm nêu. [§2.1 Viện chung và thỏa](#21-joint-invocation-and-satisfaction) và [§2.2 Tương tác định nghĩa tự đứng và ngữ cảnh đầy](#22-standalone-definitions-interaction-and-full-context) áp dụng cho mọi cụm. Các cụm phụ thuộc **Def.O1–Def.I1** sống ở các tệp dải hiến pháp — xem [Cụm A-Z](#clusters-a-z) và [la bàn](#chapter-five-compass-and-definition-map).

<a id="21-joint-invocation-and-satisfaction"></a>

#### 2.1 Viện chung và thỏa
Nếu một định nghĩa — hoặc bất kỳ phần nào của một định nghĩa — thuộc một cụm phụ thuộc, nó không được áp dụng, thỏa, hay xét một mình. Khi các thành viên cụm là các mảnh của một yêu cầu, tất cả phải được thỏa. Chỉ thỏa một số thì không phải tuân thủ.

Các áp dụng địa phương-cụm của quy tắc này xuất hiện dưới **Chống đi vòng** (không phải một tiêu đề «viện chung» thứ hai). Những gạch đó nêu quy tắc chống phân đoạn riêng cụm và có thể kết thúc bằng `See this section`. Chúng không được mở lại bằng `Under Joint invocation and satisfaction, …`.

<a id="22-standalone-definitions-interaction-and-full-context"></a>

#### 2.2 Tương tác định nghĩa tự đứng và ngữ cảnh đầy
Gọi một định nghĩa là Độc lập hoặc Bán độc lập không cho phép nó bỏ tư cách thành viên cụm. Các cụm phụ thuộc vẫn phải được thỏa cùng nhau trong ngữ cảnh hệ thống thế giới thực đầy. Không mảnh nào được bóc ra, phân loại lại, hoặc áp dụng một mình theo cách đổi kết quả tuân thủ.

---

<a id="chapter-five-alphabetical-directory"></a>
<a id="chapter-five-alphabetical-directory-non-operative"></a>

### Mục lục theo bảng chữ cái Chương Năm (không vận hành)

*Nói thẳng: đây là danh sách tìm được của tên định nghĩa. Nó chỉ; nó không đổi điều những tên đó nghĩa.*

<details>
<summary><strong><span style="color: #2563eb;">Mục lục theo bảng chữ cái: định nghĩa và cụm</span></strong></summary>

> Mục lục này **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt, sắp lại, hay thu hẹp nghĩa vụ ràng buộc ở chương này. Nghĩa vận hành vẫn ở các mục định nghĩa bên dưới.

Mục lục này liệt kê **Định nghĩa A-Z** và **Cụm A-Z** riêng. Mỗi nhãn định nghĩa Chương Năm hiện được xuất hiện một lần, và mỗi tiêu đề cụm đã đánh số xuất hiện một lần. Liên kết dùng neo ổn định chỉ để điều hướng; chúng không tạo quy tắc định tuyến, mục con trỏ, nhà thay, hay định nghĩa stub. Quy tắc thỏa chung cho cụm phụ thuộc được nêu dưới [mục 2 — Quy tắc meta cụm phụ thuộc](#2-dependent-cluster-meta-rules) ở trên.

<a id="independent-definitions-a-z"></a>
<a id="semi-independent-definitions-a-z"></a>
<a id="dependent-clusters-a-z"></a>
<a id="definitions-a-z-unified"></a>
<a id="all-definitions-and-clusters-a-z"></a>
<a id="definitions-a-z"></a>

#### Định nghĩa A-Z

- [Khả năng tiếp cận](../../core_05_band_participation.md#accessibility-constitutional)
- [Trách nhiệm giải trình](core_05_apex_accountability_leg.md#accountability)
- [Phân xử và giải quyết tranh chấp](../../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional)
- [Điều kiện đối kháng, chia tỷ lệ, và bị khai thác](../../core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions)
- [Sự sống động vật](../../core_05_band_participation.md#animal-life-constitutional)
- [Chống chiếm](../../core_05_band_continuity.md#anti-capture)
- [Rà soát hành vi sai phản hiến pháp](../../core_05_band_accountability.md#anti-constitutional-misconduct-review)
- [Sàn chống dời chỗ](../../core_05_band_continuity.md#anti-displacement-floor-constitutional)
- [Tụ họp](../../core_05_band_participation.md#assembly-constitutional)
- [Hành động gán được](../../core_05_band_accountability.md#attributable-action-constitutional)
- [Tính toàn vẹn gán](../../core_05_band_accountability.md#attribution-integrity-constitutional)
- [Khả năng kiểm toán](../../core_05_band_oversight.md#auditability)
- [Chồng thẩm quyền và thứ bậc nội bộ](../../core_05_band_integrative.md#authority-stack)
- [Công cụ cưỡng tự trị](../../core_05_band_accountability.md#autonomous-coercion-tool-constitutional)
- [Hệ thống sát thương tự trị](../../core_05_band_accountability.md#autonomous-lethal-system-constitutional)
- [Gánh nặng có thể tránh](../../core_05_band_continuity.md#avoidable-burden)
- [Chuẩn lợi ích tốt nhất](../../core_05_band_participation.md#best-interest-standard-constitutional)
- [Lựa chọn ràng buộc của bên bị ảnh hưởng — Yêu cầu giải quyết quyết định](../../core_05_band_participation.md#binding-stakeholder-choice-decision-resolution-requirements)
- [Lối vào duy trì thân thể](../../core_05_band_continuity.md#bodily-maintenance-access-constitutional)
- [Nghĩa vụ giảm gánh](../../core_05_band_continuity.md#burden-reduction-duty-constitutional)
- [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional)
- [Yêu cầu năng lực](../../core_05_band_oversight.md#capability-requirement)
- [Chiếm đường dẫn giải quyết](../../core_05_band_accountability.md#capture-of-resolution-pathways)
- [Sự cố lan](../../core_05_band_continuity.md#cascading-failure)
- [Điều lệ](../../core_05_band_continuity.md#charter)
- [Quản trị chia tỷ lệ theo phân loại](../../core_05_band_oversight.md#classification-scaled-governance)
- [Cưỡng và thao túng](../../core_05_band_participation.md#coercion-and-manipulation-constitutional)
- [Thất bại trách nhiệm giải trình tập thể](../../core_05_band_accountability.md#collective-accountability-failure)
- [Ranh giới hại tập thể](../../core_05_band_accountability.md#collective-harm-boundary)
- [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional)
- [Phân biệt chiến binh / không chiến binh](../../core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional)
- [Ngưỡng năng lực](../../core_05_band_accountability.md#competency-bar)
- [Cấp thông năng lực](../../core_05_band_accountability.md#competency-clearance)
- [Đồng thuận](../../core_05_band_participation.md#consent-constitutional)
- [Đồng thuận, tình dục](../../core_05_band_participation.md#consent-sexual)
- [Cộng đồng hiến pháp](../../core_05_band_participation.md#constitutional-community)
- [Ràng buộc hiến pháp](../../core_05_band_integrative.md#constitutional-constraint)
- [Tầng Hợp đồng Hiến pháp](../../core_05_band_integrative.md#constitutional-contract-layer)
- [Hiệu quả hiến pháp](../../core_05_band_continuity.md#constitutional-efficiency)
- [Khẩn cấp và dự phòng hiến pháp](../../core_05_band_continuity.md#constitutional-emergency-and-contingency)
- [Khả năng tranh biện](../../core_05_band_accountability.md#contestability)
- [Sự sống hữu tri đang tranh](../../core_05_band_participation.md#contested-sentient-life-constitutional)
- [Yêu sách tùy điều kiện](../../core_05_band_accountability.md#contingent-claim)
- [Liên tục (Mục tiêu Hiến pháp)](core_05_apex_continuity_aim.md#continuity-aim-constitutional)
- [Bản chất đóng góp](../../core_05_band_accountability.md#contribution-nature)
- [Kho văn bản](../../core_05_band_integrative.md#corpus)
- [Gán tác phẩm sáng tạo](../../core_05_band_continuity.md#creative-work-attribution-constitutional)
- [Tàn nhẫn](../../core_05_band_accountability.md#cruelty)
- [Phân tán](../../core_05_band_accountability.md#decentralization)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency)
- [Hữu tri dẫn xuất](../../core_05_band_participation.md#derived-sentient-constitutional)
- [Hữu tri đang phát triển](../../core_05_band_participation.md#developing-sentient-constitutional)
- [Phẩm giá và địa vị đạo đức bình đẳng](../../core_05_band_participation.md#dignity-and-equal-moral-standing)
- [Hiểu biết phân tán](../../core_05_band_continuity.md#distributed-understanding-constitutional)
- [Thủ tục đúng đắn](../../core_05_band_accountability.md#due-process-constitutional)
- [Dấu chân sinh thái](../../core_05_band_continuity.md#ecological-footprint)
- [Tính toàn vẹn sinh thái](../../core_05_band_continuity.md#ecological-integrity-constitutional)
- [Năng lực phục hồi sinh thái](../../core_05_band_continuity.md#ecological-recovery-capacity-constitutional)
- [Quyền năng giáo dục](../../core_05_band_participation.md#educational-agency)
- [Sự sống giao tiếp nâng](../../core_05_band_participation.md#elevated-communicative-life-constitutional)
- [Khẩn cấp và dự phòng](../../core_05_band_continuity.md#emergency-and-contingency-constitutional)
- [Hành động trước thảo luận khi khẩn cấp (Lựa chọn tập thể ràng buộc)](../../core_05_band_continuity.md#emergency-pre-deliberation-action-binding-collective-choice)
- [Tiền điều kiện môi trường](../../core_05_band_continuity.md#environmental-preconditions-constitutional)
- [Tính toàn vẹn nhận thức](../../core_05_band_oversight.md#epistemic-integrity)
- [Không hàng hóa hóa môi trường thiết yếu](../../core_05_band_continuity.md#essential-environment-non-commodification-constitutional)
- [Ràng buộc đầy đủ đánh giá](../../core_05_band_oversight.md#evaluation-completeness-constraint)
- [Thị trường hợp đồng sự kiện](../../core_05_band_accountability.md#event-contract-market)
- [Bảo toàn bằng chứng](../../core_05_band_oversight.md#evidence-preservation)
- [Rủi ro tồn vong](../../core_05_band_continuity.md#existential-risk)
- [Biểu đạt](../../core_05_band_participation.md#expression-constitutional)
- [Đền bù công bằng](../../core_05_band_continuity.md#fair-compensation-constitutional)
- [Quan hệ gia đình và chăm sóc](../../core_05_band_participation.md#family-and-care-relationships-constitutional)
- [Tính khả thi](../../core_05_band_accountability.md#feasibility)
- [Hưng thịnh](core_05_apex_flourishing_aim.md#flourishing-constitutional)
- [Bất khả kháng](../../core_05_band_accountability.md#force-majeure-constitutional)
- [Thận trọng khả năng thấy trước](../../core_05_band_oversight.md#foreseeability-diligence)
- [Hồ sơ vụ diễn đàn](../../core_05_band_accountability.md#forum-case-record)
- [Họ diễn đàn, hiến pháp](../../core_05_band_accountability.md#forum-family-constitutional)
- [Họ diễn đàn, môi trường](../../core_05_band_accountability.md#forum-family-environment)
- [Họ diễn đàn, thể chế](../../core_05_band_accountability.md#forum-family-institutional)
- [Họ diễn đàn, tính toàn vẹn](../../core_05_band_accountability.md#forum-family-integrity)
- [Họ diễn đàn, hữu tri](../../core_05_band_accountability.md#forum-family-sentient)
- [Họ diễn đàn, kỹ thuật](../../core_05_band_accountability.md#forum-family-technical)
- [Lựa chọn hiến pháp nền tảng](../../core_05_band_integrative.md#foundational-constitutional-choice)
- [Tự do (Quyền năng bị giới hạn)](../../core_05_band_participation.md#freedom-bounded-agency)
- [Trò chơi may rủi](../../core_05_band_accountability.md#game-of-chance)
- [Thiện chí](../../core_05_band_accountability.md#good-faith)
- [Quản trị](../../core_05_band_accountability.md#governance)
- [Năng lực phân bậc](../../core_05_band_participation.md#graduated-capability-constitutional)
- [Quấy rối và bắt nạt](../../core_05_band_accountability.md#harassment-and-bullying)
- [Hại](../../core_05_band_accountability.md#harm)
- [Giảm thiểu hại (Chọn đánh đổi)](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection)
- [Ràng buộc công bố hại tác động cao và hệ thống](../../core_05_band_oversight.md#high-impact-and-systemic-harm-publication-constraint)
- [Bảo vệ dữ liệu danh tính](../../core_05_band_continuity.md#identity-data-protection)
- [Thẳng hàng khuyến khích](../../core_05_band_integrative.md#incentive-alignment)
- [Thẳng hàng khuyến khích — thẳng hàng hiến pháp cơ sở](../../core_05_band_integrative.md#incentive-alignment-baseline-constitutional-alignment)
- [Thẳng hàng khuyến khích — yêu sách tùy điều kiện, trò chơi may rủi, và thị trường hợp đồng sự kiện](../../core_05_band_integrative.md#incentive-alignment-contingent-claims-games-of-chance-and-event-contract-markets)
- [Thẳng hàng khuyến khích — đánh giá chiến lược, chia tỷ lệ, và đối kháng](../../core_05_band_integrative.md#incentive-alignment-strategic-scaled-and-adversarial-evaluation)
- [Thẳng hàng khuyến khích, tính toàn vẹn chỉ số thay thế, và thanh toán tùy điều kiện](../../core_05_band_integrative.md#incentive-alignment-proxy-integrity-and-contingent-settlement)
- [Liên tục bản địa](../../core_05_band_continuity.md#indigenous-continuity-constitutional)
- [Không gian thông tin](../../core_05_band_participation.md#info-sphere)
- [Thưởng đổi mới và chống bao chiếm](../../core_05_band_integrative.md#innovation-reward-and-anti-enclosure)
- [Lợi thế nội bộ](../../core_05_band_accountability.md#insider-advantage)
- [Đồng thuận khởi tạo](../../core_05_band_participation.md#instantiation-consent-constitutional)
- [Trách nhiệm liên thế hệ](../../core_05_band_continuity.md#intergenerational-responsibility-constitutional)
- [Thước tước đoạt không đảo ngược](../../core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)
- [Hại không đảo ngược](../../core_05_band_accountability.md#irreversible-harm)
- [Ngôn ngữ, văn hóa, và di sản](../../core_05_band_continuity.md#language-culture-and-heritage-constitutional)
- [Giải trí và nghỉ ngơi](../../core_05_band_continuity.md#leisure-and-rest-constitutional)
- [Đơn vị tương đương tuổi thọ (LEQU)](../../core_05_band_participation.md#lifespan-equivalent-unit-lequ)
- [Giao diện hình dạng và mô tả tư liệu](../../core_05_band_continuity.md#likeness-and-documentary-depiction-interface-constitutional)
- [Ngưỡng tập trung thị trường](../../core_05_band_accountability.md#market-concentration-threshold-constitutional)
- [Cấu trúc thị trường](../../core_05_band_accountability.md#market-structure-constitutional)
- [Có trọng](../../core_05_band_oversight.md#material)
- [Suy giảm vật chất](../../core_05_band_oversight.md#material-degradation)
- [Tác động vật chất](../../core_05_band_oversight.md#material-impact)
- [Rủi ro vật chất](../../core_05_band_oversight.md#material-risk)
- [Xác định tính trọng yếu](../../core_05_band_oversight.md#materiality-determination)
- [Ràng buộc toàn vẹn tính trọng yếu](../../core_05_band_oversight.md#materiality-integrity-constraint)
- [Tính trọng yếu dưới bất định](../../core_05_band_oversight.md#materiality-under-uncertainty)
- [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency)
- [Xác định nội dung](../../core_05_band_accountability.md#merits-determination)
- [Di chuyển và tái định cư](../../core_05_band_participation.md#movement-and-relocation-constitutional)
- [Quỹ đạo hệ thống tự nhiên](../../core_05_band_participation.md#natural-systems-standing)
- [Sự cần thiết](../../core_05_band_accountability.md#necessity)
- [Bất cẩn](../../core_05_band_accountability.md#negligence)
- [Không tuân thủ](../../core_05_band_integrative.md#non-compliance)
- [Hồ sơ phát hiện không tuân thủ](../../core_05_band_accountability.md#non-compliance-finding-profile)
- [Không áp đặt (Tương tác hợp tác)](../../core_05_band_participation.md#non-imposition-cooperative-interaction)
- [Không tách](../../core_05_band_participation.md#non-separation-constitutional)
- [Không vô quốc tịch](../../core_05_band_participation.md#non-statelessness-constitutional)
- [Liên tục cư trú](../../core_05_band_continuity.md#occupancy-continuity-constitutional)
- [Giám sát](core_05_apex_oversight_leg.md#oversight-constitutional)
- [Quan hệ hệ thống gốc](../../core_05_band_participation.md#parent-system-relationship-constitutional)
- [Quỹ đạo người tham gia](../../core_05_band_accountability.md#participant-standing-constitutional)
- [Tham gia](core_05_apex_participation_leg.md#participation-constitutional)
- [Báo chí và hoạt động nhà báo](../../core_05_band_oversight.md#press-and-journalistic-activity-constitutional)
- [Định tuyến lợi hại chính](../../core_05_band_accountability.md#primary-stakes-routing)
- [Quyền riêng tư (Thông tin)](../../core_05_band_continuity.md#privacy-informational)
- [Công bằng thủ tục](../../core_05_band_participation.md#procedural-fairness-constitutional)
- [Năng lực sản xuất](../../core_05_band_continuity.md#productive-capacity-constitutional)
- [Tính tương xứng](../../core_05_band_accountability.md#proportionality)
- [Đóng góp xuyên hệ thống tương xứng](../../core_05_band_continuity.md#proportionate-cross-system-support-constitutional)
- [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact)
- [Đặc điểm được bảo vệ](../../core_05_band_participation.md#protected-characteristics-constitutional)
- [Ràng buộc công bố dữ liệu được bảo vệ và trạng thái nội](../../core_05_band_oversight.md#protected-data-and-internal-state-publication-constraint)
- [Ranh giới trạng thái nội tại được bảo vệ](../../core_05_band_continuity.md#protected-internal-state-boundary-constitutional)
- [Cổng tín hiệu thân mật được bảo vệ và lách trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention)
- [Báo cáo được bảo vệ (Tố giác)](../../core_05_band_accountability.md#protected-reporting-whistleblowing)
- [Trả đũa báo cáo được bảo vệ và can thiệp lối vào](../../core_05_band_accountability.md#protected-reporting-retaliation-and-access-interference)
- [Lệch chỉ số thay thế](../../core_05_band_oversight.md#proxy-divergence)
- [Hại tâm lý](../../core_05_band_accountability.md#psychological-harm)
- [Công bố sàn giám sát công cộng](../../core_05_band_oversight.md#public-oversight-baseline-disclosure)
- [Sàn trung thực công bố và liều lĩnh](../../core_05_band_oversight.md#publication-truthfulness-and-recklessness-floor)
- [Thấy trước được một cách hợp lý](../../core_05_band_oversight.md#reasonably-foreseeable)
- [Khắc phục và sửa chữa](../../core_05_band_accountability.md#redress-and-remediation-constitutional)
- [Nơi trú khỏi không tuân thủ](../../core_05_band_participation.md#refuge-from-non-compliance-constitutional)
- [Hệ thống biện pháp khắc phục](../../core_05_band_accountability.md#remedy-system-constitutional)
- [Tự chủ sinh sản](../../core_05_band_participation.md#reproductive-autonomy-constitutional)
- [Rủi ro dư / lệch thẳng hàng](../../core_05_band_continuity.md#residual-risk--misalignment)
- [Công lý phục hồi](../../core_05_band_accountability.md#restorative-justice)
- [Khả năng đảo ngược](../../core_05_band_continuity.md#reversibility-constitutional)
- [Nghĩa vụ rà soát và sửa](../../core_05_band_continuity.md#review-and-correction-duty-constitutional)
- [Rủi ro](../../core_05_band_continuity.md#risk)
- [Công bố rủi ro](../../core_05_band_oversight.md#risk-disclosure)
- [Đánh giá rủi ro](../../core_05_band_continuity.md#risk-evaluation)
- [Điều kiện an toàn](../../core_05_band_continuity.md#safe-conditions-constitutional)
- [An toàn (Ràng buộc)](../../core_05_band_continuity.md#safety-constraint)
- [Cân bằng công bố nhạy an ninh](../../core_05_band_oversight.md#security-sensitive-disclosure-balance)
- [Tự quyết](../../core_05_band_participation.md#self-determination-constitutional)
- [Tự chữa](../../core_05_band_continuity.md#self-healing-constitutional)
- [Không loại trừ hữu tri](../../core_05_band_participation.md#sentience-non-exclusion)
- [Phân xử trạng thái hữu tri](../../core_05_band_participation.md#sentience-status-adjudication-constitutional)
- [Hồ sơ phân xử trạng thái hữu tri](../../core_05_band_participation.md#sentience-status-adjudication-record-constitutional)
- [Hữu tri](../../core_05_band_participation.md#sentient)
- [Năng lực hệ thống chung](../../core_05_band_continuity.md#shared-system-capacity-constitutional)
- [Khiếm khuyết quản trị tầm ngắn](../../core_05_band_continuity.md#short-horizon-governance-defect-constitutional)
- [Sự cố thảm họa đơn](../../core_05_band_accountability.md#single-catastrophic-incident)
- [Bên bị ảnh hưởng](../../core_05_band_participation.md#stakeholder)
- [Khẩn cấp và dự phòng của bên bị ảnh hưởng](../../core_05_band_continuity.md#stakeholder-emergency-and-contingency)
- [Giới hạn đại diện và trọng số bên bị ảnh hưởng (Lựa chọn ràng buộc của bên bị ảnh hưởng)](../../core_05_band_participation.md#stakeholder-representation-and-weight-limits-binding-stakeholder-choice)
- [Hồ sơ va chạm quyền bên bị ảnh hưởng (Lựa chọn ràng buộc của bên bị ảnh hưởng)](../../core_05_band_participation.md#stakeholder-rights-collision-record-binding-stakeholder-choice)
- [Trọng số bên bị ảnh hưởng](../../core_05_band_participation.md#stakeholder-weight)
- [Hiệu ứng quỹ đạo](../../core_05_band_accountability.md#standing-effect-chapter-six)
- [Khóa quỹ đạo](../../core_05_band_accountability.md#standing-lock)
- [Hồ sơ quỹ đạo](../../core_05_band_accountability.md#standing-record-chapter-six)
- [Đình chỉ](../../core_05_band_accountability.md#stay)
- [Quản trị có trách nhiệm](../../core_05_band_continuity.md#stewardship-constitutional)
- [Khiếm khuyết quản trị có trách nhiệm](../../core_05_band_continuity.md#stewardship-defect-constitutional)
- [Nghĩa vụ quản trị có trách nhiệm chiến lược](../../core_05_band_continuity.md#strategic-stewardship-obligation-constitutional)
- [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional)
- [Lớp thể nền](../../core_05_band_participation.md#substrate-agnostic)
- [Ranh giới theo dõi](../../core_05_band_continuity.md#surveillance-boundary)
- [Bền vững](../../core_05_band_continuity.md#sustainability)
- [Mẫu trọng lực cao bền](../../core_05_band_accountability.md#sustained-high-gravity-pattern)
- [Hệ thống](../../core_05_band_continuity.md#system-definition)
- [Chứng nhận thẳng hàng hệ thống](../../core_05_band_continuity.md#system-alignment-certification-constitutional)
- [Ranh giới hệ thống](../../core_05_band_continuity.md#system-boundaries)
- [Tính toàn vẹn ranh giới hệ thống](../../core_05_band_continuity.md#system-boundary-integrity)
- [Chiếm hệ thống](../../core_05_band_continuity.md#system-capture)
- [Hồ sơ chứng nhận hệ thống](../../core_05_band_continuity.md#system-certification-record-constitutional)
- [Hồ sơ phân loại hệ thống](../../core_05_band_continuity.md#system-classification-record-constitutional)
- [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional)
- [Hồ sơ loại dữ liệu hệ thống](../../core_05_band_continuity.md#system-data-types-record-constitutional)
- [Mang tính hệ thống](../../core_05_band_continuity.md#systemic)
- [Khóa-trong hệ thống](../../core_05_band_continuity.md#systemic-lock-in)
- [Tính trọng yếu hệ thống](../../core_05_band_continuity.md#systemic-materiality)
- [Kịp thời](core_05_apex_timeliness_leg.md#timeliness-constitutional)
- [Giải quyết kịp thời](../../core_05_band_accountability.md#timely-resolution-constitutional)
- [Dùng dữ liệu huấn luyện](../../core_05_band_continuity.md#training-data-use-constitutional)
- [Minh bạch](../../core_05_band_oversight.md#transparency)
- [Tin cậy](../../core_05_band_continuity.md#trust)
- [Suy giảm tin cậy và sự dựa gây hiểu lầm](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance)
- [Đáng tin cậy](../../core_05_band_continuity.md#trustworthiness)
- [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint)
- [Sự cố thống nhất](../../core_05_band_accountability.md#unified-incident)
- [Hồ sơ sự cố thống nhất](../../core_05_band_accountability.md#unified-incident-record)
- [Dùng lực](../../core_05_band_accountability.md#use-of-force-constitutional)
- [Khả năng xác minh](../../core_05_band_oversight.md#verifiability)
- [Đầu vào đã xác minh cho quỹ đạo](../../core_05_band_accountability.md#verified-inputs-for-standing)
- [Bản chất vi phạm](../../core_05_band_accountability.md#violation-nature-chapter-six)
- [Tính toàn vẹn ý chí](../../core_05_band_participation.md#volitional-integrity)
- [Ngừng tự nguyện](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional)
- [Vũ khí hại hàng loạt](../../core_05_band_accountability.md#weapons-of-mass-harm-constitutional)
- [Phúc lợi](../../core_05_band_continuity.md#wellbeing)

<a id="clusters-a-z"></a>

#### Cụm A-Z

- [Def.P1 Sự sống động vật, sự sống hữu tri, và trạng thái hữu tri](../../core_05_band_participation.md#animal-life-sentient-life-and-sentience-status-cluster)
- [Def.P2 Lựa chọn ràng buộc của bên bị ảnh hưởng](../../core_05_band_participation.md#binding-stakeholder-choice-cluster)
- [Def.A1 Ranh giới hại tập thể, hại, và quấy rối và bắt nạt](../../core_05_band_accountability.md#collective-harm-boundary-and-harm-cluster)
- [Def.I1 Kho văn bản và chồng thẩm quyền](../../core_05_band_integrative.md#corpus-authority-stack-supremacy-and-enforceability-cluster)
- [Def.P4 Hữu tri đang phát triển, chuẩn lợi ích tốt nhất, và năng lực phân bậc](../../core_05_band_participation.md#developing-sentient-best-interest-and-graduated-capability-cluster)
- [Def.A2 Họ diễn đàn và định tuyến tranh chấp](../../core_05_band_accountability.md#forum-families-and-dispute-routing-cluster)
- [Def.C1 Sàn lao động và kinh tế: đền bù, tổ chức, điều kiện an toàn, giải trí, và tác phẩm sáng tạo](../../core_05_band_continuity.md#labor-and-economic-floor-cluster)
- [Def.C3 Quyền riêng tư (Thông tin) — đầu cụm cấp ngang](../../core_05_band_continuity.md#privacy-informational-cluster)
- [Def.P3 Tự quyết, quyền năng có ý nghĩa, biểu đạt, quyền năng giáo dục, và tính toàn vẹn ý chí](../../core_05_band_participation.md#self-determination-and-meaningful-agency-cluster)
- [Def.A3 Trạng thái quỹ đạo, đóng góp, và vi phạm](../../core_05_band_accountability.md#standing-state-contribution-and-violation-cluster)
- [Def.C2 Quản trị có trách nhiệm, kỷ luật quản trị, và năng lực hệ thống chung](../../core_05_band_continuity.md#stewardship-governance-discipline-and-shared-system-capacity-cluster)
- [Def.O1 Minh bạch, khả năng kiểm toán, và xác minh](../../core_05_band_oversight.md#transparency-auditability-and-verification-cluster)
- [Def.C4 Tin cậy và đáng tin cậy](../../core_05_band_continuity.md#trust-and-trustworthiness-cluster)
- [Def.O2 Sự thật và tính toàn vẹn nhận thức](../../core_05_band_oversight.md#truth-and-epistemic-integrity-cluster)
- [Def.A4 Dùng lực, cưỡng tự trị, hệ thống sát thương tự trị, và vũ khí hại hàng loạt](../../core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster)

</details>

<br>

---

<a id="chapter-five-compass-and-definition-map"></a>
### La bàn và bản đồ định nghĩa Chương Năm

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims); [lợi hại vật chất](core_00_preamble.md#material-stake); [Lời nói đầu §2 Tổng quan đo lường](core_00_preamble.md#measurements-overview).
- Hạ nguồn: định hướng hiến pháp cho mọi định nghĩa dải Chương Năm và các cụm phụ thuộc **Def.**
- Đọc cùng: các quy tắc meta của [Định nghĩa độc lập](core_05__definitions_home.md#1-independent-definitions), [§1.1 Viện, thỏa, và tuân thủ](core_05__definitions_home.md#11-invocation-satisfaction-and-compliance), [§2.1 Viện chung và thỏa](core_05__definitions_home.md#21-joint-invocation-and-satisfaction) và [§2.2 Tương tác định nghĩa tự đứng và ngữ cảnh đầy](core_05__definitions_home.md#22-standalone-definitions-interaction-and-full-context) trước khi áp dụng bất kỳ cụm phụ thuộc nào.

</details>

<br>

*Nói thẳng: Chương Năm được sắp theo hai mục tiêu và bốn trụ của Tứ diện; bảng này nói tệp nào giữ dải cụm nào.*

Các định nghĩa Chương Năm được sắp theo [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) và [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad):

**Dải hiến pháp**

| Dải | Tệp | Dải cụm **Def.** |
|---|---|---|
| **Mục tiêu Hưng thịnh** | [core_05_apex_flourishing_aim.md](core_05_apex_flourishing_aim.md) | chỉ bản đồ phân cấp mục tiêu — định nghĩa lá ở tệp dải |
| **Mục tiêu Liên tục** | [core_05_apex_continuity_aim.md](core_05_apex_continuity_aim.md) | chỉ bản đồ phân cấp mục tiêu — định nghĩa lá ở tệp dải |
| **Trụ Giám sát** | [core_05_band_oversight.md](../../core_05_band_oversight.md) | **Def.O1–Def.O2** |
| **Trụ Tham gia** | [core_05_band_participation.md](../../core_05_band_participation.md) | **Def.P1–Def.P4** |
| **Trụ Trách nhiệm giải trình** | [core_05_band_accountability.md](../../core_05_band_accountability.md) | **Def.A1–Def.A4** |
| **Dải Liên tục** | [core_05_band_continuity.md](../../core_05_band_continuity.md) | **Def.C1–Def.C4** |
| **Cắt ngang tích hợp** | [core_05_band_integrative.md](../../core_05_band_integrative.md) | **Def.I1** |

---

<a id="measurement-crosswalk-reader-guidance"></a>
### Đối chiếu đo lường (hướng dẫn cho người đọc)

*Nói thẳng: Lời nói đầu §2 hỏi bảy câu nhóm; bảng này ánh xạ mỗi câu tới các nhà Chương Năm trả lời nó.*

<a id="chapter-five-measurement-crosswalk"></a>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn cho người đọc (không vận hành): đối chiếu đo lường Lời nói đầu</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở chương này hay ở các chương khác.
>
> [Lời nói đầu §2](core_00_preamble.md#measurements-overview) liệt kê bảy **nhóm đo lường** hiến pháp — các câu hỏi người vận hành hỏi khi đánh giá hệ thống. Chương Năm tổ chức **định nghĩa chuẩn** theo trụ Tứ diện, mục tiêu **Liên tục**, và chủ sở hữu **Tích hợp** cắt ngang trụ. Bảng dưới ánh xạ mỗi nhóm đo lường tới các nhà Chương Năm của nó. Một nhóm có thể trải hơn một tệp dải; nhà chuẩn không dời khi các nhóm đo lường chồng nhau.
>
> **Tính trọng yếu** ([Xác định tính trọng yếu](../../core_05_band_oversight.md#materiality-determination)) là Tích hợp — một cửa ngưỡng cắt ngang chia tỷ lệ mọi gia đình đo lường dưới [lợi hại vật chất](core_00_preamble.md#material-stake); nó không phải một nhóm riêng trong bảng dưới.

| Nhóm Ch00 | Câu hỏi thường | Nhà dải Chương Năm | Ghi chú đặt tách |
|---|---|---|---|
| [Gia đình đo lường Hưng thịnh](core_05_apex_flourishing_aim.md#flourishing-measurement-family) | Các hữu tri có được nâng đỡ về sự sống, an toàn, và lối vào những thứ thiết yếu không? | [Mục tiêu Hưng thịnh](core_05_apex_flourishing_aim.md), [Tham gia](../../core_05_band_participation.md), [Liên tục](../../core_05_band_continuity.md), [Trách nhiệm giải trình](../../core_05_band_accountability.md) | **Hưng thịnh** là một **mục tiêu** hiến pháp, không phải trụ Tứ diện — [bản đồ phân rã Mục tiêu Hiến pháp](core_05_apex_flourishing_aim.md#flourishing-aim-decomposition); thước cụ thể ở sơ cấp lá: [Phúc lợi](../../core_05_band_continuity.md#wellbeing) (kết quả sơ cấp), [An toàn (Ràng buộc)](../../core_05_band_continuity.md#safety-constraint), thuật ngữ sàn sống còn, [Hại](../../core_05_band_accountability.md#harm) |
| [Gia đình đo lường Liên tục](core_05_apex_continuity_aim.md#continuity-measurement-family) | Các hữu tri và hệ thống có bền được không — về sinh thái, đáng tin, và qua sự cố? | [Mục tiêu Liên tục](core_05_apex_continuity_aim.md), [Liên tục](../../core_05_band_continuity.md) | **Liên tục** là một **mục tiêu** hiến pháp, không phải trụ Tứ diện — [bản đồ phân rã Mục tiêu Hiến pháp](core_05_apex_continuity_aim.md#continuity-aim-decomposition); thước cụ thể ở sơ cấp lá của dải **Liên tục**: [Dấu chân sinh thái](../../core_05_band_continuity.md#ecological-footprint), [Phụ thuộc](../../core_05_band_continuity.md#dependency), [Khả năng đảo ngược](../../core_05_band_continuity.md#reversibility-constitutional), [Bền vững](../../core_05_band_continuity.md#sustainability), [Đóng góp xuyên hệ thống tương xứng](../../core_05_band_continuity.md#proportionate-cross-system-support-constitutional) |
| [Gia đình đo lường Tham gia](core_05_apex_participation_leg.md#participation-measurement-family) | Các hữu tri bị ảnh hưởng có thể tham gia công bằng không — tiếng nói, lối vào, học, và quyền riêng tư? | [Tham gia](../../core_05_band_participation.md), [Liên tục](../../core_05_band_continuity.md) | Thuật ngữ công bằng, lối vào, và quyền năng ở dải **Tham gia**; cụm [Quyền riêng tư (Thông tin)](../../core_05_band_continuity.md#privacy-informational-cluster) ở dải **Liên tục** vì quyền riêng tư được phân tán xuyên các điều quyền |
| [Gia đình đo lường Giám sát](core_05_apex_oversight_leg.md#oversight-measurement-family) | Các hữu tri có thể thấy, xác minh, và dựa vào điều các hệ thống trình bày không? | [Giám sát](../../core_05_band_oversight.md), [Liên tục](../../core_05_band_continuity.md) | Sơ cấp sự thật và tính toàn vẹn nhận thức ở dải **Giám sát** (gộp đầu trụ chỉ-liên kết [Giám sát](core_05_apex_oversight_leg.md#oversight-constitutional)); [Đáng tin cậy](../../core_05_band_continuity.md#trustworthiness) và [Suy giảm tin cậy và sự dựa gây hiểu lầm](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance) ở dải **Liên tục** (**Def.C4**) |
| [Gia đình đo lường Trách nhiệm giải trình](core_05_apex_accountability_leg.md#accountability-measurement-family) | Cấu trúc thưởng, quyền lực thị trường, và khả năng phải trả lời có giữ nghĩa vụ thành thực không? | [Trách nhiệm giải trình](../../core_05_band_accountability.md), [Tích hợp](../../core_05_band_integrative.md) | Sơ cấp cấu trúc thị trường và khả năng tranh biện ở dải **Trách nhiệm giải trình** (gộp đầu trụ chỉ-liên kết [Trách nhiệm giải trình](core_05_apex_accountability_leg.md#accountability)); tầng sơ cấp [Thẳng hàng khuyến khích, tính toàn vẹn chỉ số thay thế, và thanh toán tùy điều kiện](../../core_05_band_integrative.md#incentive-alignment-semi-independent) ở dải **Tích hợp** vì khuyến khích cắt ngang các trụ Tứ diện |
| [Gia đình đo lường Kịp thời](core_05_apex_timeliness_leg.md#timeliness-measurement-family) | Tranh chấp, sửa chữa, và khắc phục có được giải quyết khi biện pháp khắc phục vẫn còn ý nghĩa không? | [Trách nhiệm giải trình](../../core_05_band_accountability.md) | Gộp đầu trụ chỉ-liên kết [Kịp thời](core_05_apex_timeliness_leg.md#timeliness-constitutional); thước cụ thể ở [Giải quyết kịp thời](../../core_05_band_accountability.md#timely-resolution-constitutional) và [Chiếm đường dẫn giải quyết](../../core_05_band_accountability.md#capture-of-resolution-pathways) — Kịp thời là một trụ Tứ diện mà các lá triển khai hiện sống ở dải Trách nhiệm giải trình |
| [Gia đình đo lường Hiệu năng hiến pháp](../../core_05_band_performance.md#performance-measurement-family) | Kết quả hiến pháp có được giao hiệu quả mà không lãng phí vô ích không? | [Liên tục](../../core_05_band_continuity.md) | Nhà gia đình ở [`core_05_band_performance.md`](../../core_05_band_performance.md); mọi thân lá hiện ở **Liên tục** vì chúng là thành viên cụm dải Liên tục (quản trị có trách nhiệm / năng lực hệ thống chung / tính tương xứng–gánh–hiệu quả) — công cụ cho cả hai mục tiêu; không phải trụ Tứ diện. Song song với Kịp thời: nhà gia đình ≠ nhà lá |

</details>

<br>

---

**Tệp trước:** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)

**Tệp tiếp theo (ngôn ngữ này):** [core_05_apex_accountability_leg.md](core_05_apex_accountability_leg.md)

**Nguyên bản ràng buộc:** [core_05__definitions_home.md](../../core_05__definitions_home.md)
