# CHƯƠNG 01, PHẦN A: CÁC NGUYÊN TẮC GIÁ TRỊ

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn cho người đọc**. Nó không thêm, bớt hay thu hẹp nghĩa vụ ràng buộc ở tệp này hay ở các chương khác.
>
> Tệp này là một **thử nghiệm ngôn ngữ đọc** của [Chương Một, Phần A tiếng Anh](../../core_01_a_values_principles.md). **Không** phải phần ràng buộc của Hiến pháp Hữu tri. **Không** phải một hiến pháp thứ hai. **Không** phải một ấn bản phát hành. Nó được **ghim** vào `SC-Corpus-2026.08.09`. Nếu bản dịch này và nguyên bản tiếng Anh có vẻ lệch nhau, tệp đánh số [`core_01_a_values_principles.md`](../../core_01_a_values_principles.md) thắng. Thứ tự đọc và siêu dữ liệu ấn bản được giữ ở [README.md](../../README.md). Phương pháp và bảng thuật ngữ: [translations/vi/README.md](README.md).
>
> **Trước (ngôn ngữ này):** [core_00_preamble.md](core_00_preamble.md)
>
> **Tiếp theo (ngôn ngữ này):** [core_01_b_interaction_interpretation.md](core_01_b_interaction_interpretation.md) (Chương Một, Phần B — §§6–8, tương tác, giới hạn phủ, và diễn giải hiến pháp).

</details>

<br>
### 1. Mục đích và vai trò
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: [Lời nói đầu §1 Mô hình](../../core_00_preamble.md#the-model) — [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad), [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims), và chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake) áp dụng xuyên chương qua dấu vết mục.
- Hạ nguồn: [8. Diễn giải hiến pháp](core_01_b_interaction_interpretation.md#8-constitutional-interpretation) cho đọc tích hợp, sự mơ hồ, thứ bậc nội bộ, và thủ tục giải quyết xung đột chuẩn.
- Hạ nguồn: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — phát triển mục tiêu **Hưng thịnh**: [§2](#2-foundational-objective-wellbeing) đến [§4](#4-system-stability-enabler-trust-coordination-integrity) và [§5 Tự do](#5-freedom-bounded-agency); phát triển mục tiêu **Liên tục**: [§4.1](#41-resilience-and-self-healing-design), [§12 Năng lực hệ thống chung](core_01_c_stewardship_capacity_principles.md#12-shared-system-capacity), và [§14 Yêu cầu đánh giá hệ thống](core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement).
- Hạ nguồn: [2. Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing), [§2.2 Ghi nhận, củng cố, và khát vọng](#22-recognition-reinforcement-and-aspiration), [3.1 An toàn](#31-safety-harm-constraint), [3.2 Sự thật](#32-truth-epistemic-integrity-constraint), [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution), và [§5 Tự do](#5-freedom-bounded-agency).
- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — tham gia, giám sát, trách nhiệm giải trình, và kịp thời quản trị cách các hệ thống chung theo đuổi [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake) áp dụng xuyên chương qua dấu vết mục.
- Đọc cùng: [Chương Hai đến Bốn](core_02_definition_structure.md) và [Chương Năm](core_05__definitions_home.md#chapter-five-foundational-definitions) — tầng cơ chế quản trị mọi thuật ngữ dùng trong chương này; áp dụng tính toàn vẹn O/M/A/C, chống lẩn tránh, gánh, và truy vết định nghĩa tới kết quả.
- Đọc cùng: [Chương Sáu: Quyền nền tảng](../../core_06_rights_part_a.md#chapter-six-foundational-rights).
  - Đặc biệt [Điều V: Quyền cơ bản bình đẳng](../../core_06_rights_part_b.md#article-v-equal-basic-rights), [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems), và [Điều XXII: Diễn giải hiến pháp, rà soát, và bảo vệ chống chiếm](../../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards).
  - Áp dụng cách đọc này nơi diễn giải tác động tới hữu tri, hệ thống, hoặc thể chế được bảo vệ.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tính tương xứng](../../core_05_band_accountability.md#proportionality) · [O](../../core_05_band_accountability.md#proportionality) · [M](../../core_05_band_accountability.md#proportionality-a) · [A](../../core_05_band_accountability.md#proportionality-a) · [C](../../core_05_band_accountability.md#proportionality-c)
- [Sự cần thiết](../../core_05_band_accountability.md#necessity) · [O](../../core_05_band_accountability.md#necessity) · [M](../../core_05_band_accountability.md#necessity-a) · [A](../../core_05_band_accountability.md#necessity-a) · [C](../../core_05_band_accountability.md#necessity-c)

</details>

<br>

*Nói thẳng: Chương Một đặt các giá trị và ràng buộc quản trị mọi chương khác. Hệ thống chung phải theo đuổi **Hưng thịnh** và **Liên tục** cùng nhau — không cái này với giá của cái kia — và không giá trị đơn lẻ nào được tối đa hóa với giá của các giá trị còn lại.*

<a id="two-constitutional-aims"></a><a id="flourishing"></a><a id="continuity"></a>Chương này lập các nguyên tắc và ràng buộc quản trị diễn giải, áp dụng, và tiến hóa của Hiến pháp này. Nó phát triển [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims), [**Hưng thịnh**](../../core_00_preamble.md#flourishing), và [**Liên tục**](../../core_00_preamble.md#continuity) đã lập ở [Lời nói đầu §1 Mô hình](../../core_00_preamble.md#the-model) thành nguyên tắc và ràng buộc vận hành. Định nghĩa chuẩn tầng nguyên tắc sống ở Lời nói đầu; chương này áp dụng chúng.

Những mục tiêu đó phải được theo đuổi cùng nhau, luôn trong các ràng buộc nguyên tắc không thương lượng và các bảo vệ quyền đã lập trong Hiến pháp này. [**Tứ diện Hiến pháp**](../../core_00_preamble.md#constitutional-tetrad) quản trị cách cuộc theo đuổi đó vẫn chính danh — chia tỷ lệ theo [**lợi hại vật chất**](../../core_00_preamble.md#material-stake).

Những giá trị này:
- không độc lập, và trong vận hành thường chúng không phân tầng nghiêm ngặt.
- hoạt động như nguyên tắc và ràng buộc tương tác phải được đánh giá cùng nhau.
- áp dụng cho mọi «hệ thống,» gồm cấu trúc kỹ thuật, tổ chức, kinh tế, xã hội-kỹ thuật, và hệ sinh thái tác động vật chất tới các hữu tri và hành tinh Trái Đất.

Không nguyên tắc đơn lẻ nào được áp dụng tách rời nơi làm vậy sẽ vi phạm vật chất các nguyên tắc còn lại. Nơi căng thẳng nảy sinh, hệ thống phải giải chúng dưới các yêu cầu tính tương xứng, sự cần thiết, và tác động hệ thống nêu trong chương này. Nơi xung đột chưa giải trực tiếp chạm các ràng buộc nguyên tắc không thương lượng, Chương Một, **§5** — Giải quyết xung đột quy trình kiểm soát thứ tự ưu tiên.

<a id="2-foundational-objective-wellbeing"></a>
### 2. Mục tiêu nền tảng: phúc lợi
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** nơi điều kiện phúc lợi tác động vật chất tới việc tiếng nói, lối vào, và khả năng tranh biện có phải nội dung thật; trụ **trách nhiệm giải trình** nơi tuyên bố phúc lợi tác động phân bổ gánh; chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake) nơi liên quan vật chất.
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — chương này phát triển mục tiêu **Hưng thịnh** qua [§2](#2-foundational-objective-wellbeing) đến [§4](#4-system-stability-enabler-trust-coordination-integrity) và [§5 Tự do](#5-freedom-bounded-agency).
- Thượng nguồn: Nguyên tắc: [Lời nói đầu §1 Mô hình](../../core_00_preamble.md#the-model); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — phát triển mục tiêu **Hưng thịnh**.
- Hạ nguồn: [3.1 An toàn](#31-safety-harm-constraint), [3.2 Sự thật](#32-truth-epistemic-integrity-constraint), [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), và [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution).
- Các tiểu mục: [§2.1 Công bằng](#21-fairness); [§2.2 Ghi nhận, củng cố, và khát vọng](#22-recognition-reinforcement-and-aspiration).
- Đọc cùng: Sàn Quyền Chương Sáu nói chung.
  - Đặc biệt [Điều V: Quyền cơ bản bình đẳng](../../core_06_rights_part_b.md#article-v-equal-basic-rights), [Điều IX: Tự quyết và quyền năng](../../core_06_rights_part_b.md#article-ix-self-determination-and-agency), [Điều XII-B: Quyền tranh biện, rà soát, và khắc phục](../../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress), và [Điều XVIII-B: Khả năng tranh biện và giới hạn hạn chế tương xứng](../../core_06_rights_part_c.md#article-xviii-b-contestability-and-proportional-restriction-limits).
  - Áp dụng nơi lợi phúc lợi được tuyên sẽ biện minh hạn chế quyền năng, phẩm giá, hoặc khả năng tranh biện.
  - Đặc biệt [Phẩm giá và địa vị đạo đức bình đẳng](../../core_05_band_participation.md#dignity-and-equal-moral-standing), [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional), và [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity) nơi lối vào, quy trình, thẳng hàng phân phối, sự dựa, hoặc tính toàn vẹn phối hợp đang đặt lên bàn về mặt vật chất.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Phúc lợi](../../core_05_band_continuity.md#wellbeing) · [O](../../core_05_band_continuity.md#wellbeing) · [M](../../core_05_band_continuity.md#wellbeing-a) · [A](../../core_05_band_continuity.md#wellbeing-a) · [C](../../core_05_band_continuity.md#wellbeing-c)
- [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) · [O](../../core_05_apex_participation_leg.md#participation-constitutional) · [M](../../core_05_apex_participation_leg.md#participation-constitutional-m) · [A](../../core_05_apex_participation_leg.md#participation-constitutional-a) · [C](../../core_05_apex_participation_leg.md#participation-constitutional-c)
- [Phẩm giá và địa vị đạo đức bình đẳng](../../core_05_band_participation.md#dignity-and-equal-moral-standing) · [O](../../core_05_band_participation.md#dignity-and-equal-moral-standing) · [M](../../core_05_band_participation.md#dignity-and-equal-moral-standing-a) · [A](../../core_05_band_participation.md#dignity-and-equal-moral-standing-a) · [C](../../core_05_band_participation.md#dignity-and-equal-moral-standing-c)
- [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional) · [O](../../core_05_band_participation.md#substantive-fairness-constitutional) · [M](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [A](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [C](../../core_05_band_participation.md#substantive-fairness-constitutional-c)
- [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination) · [O](../../core_05_band_oversight.md#materiality-determination) · [M](../../core_05_band_oversight.md#materiality-determination-a) · [A](../../core_05_band_oversight.md#materiality-determination-a) · [C](../../core_05_band_oversight.md#materiality-determination-c)
- [Lệch chỉ số thay thế](../../core_05_band_oversight.md#proxy-divergence) · [O](../../core_05_band_oversight.md#proxy-divergence) · [M](../../core_05_band_oversight.md#proxy-divergence-a) · [A](../../core_05_band_oversight.md#proxy-divergence-a) · [C](../../core_05_band_oversight.md#proxy-divergence-c)

</details>

<br>

*Nói thẳng: toàn bộ điểm của những hệ thống này là làm đời hữu tri thực sự tốt hơn — và mục đích đó không được thỏa bằng đuổi một chỉ số thay thế, cũng không dùng được làm bình phong để cắt góc An toàn, Sự thật, hay quyền. Phúc lợi là nền cho tham gia: tiếng nói hình thức mà không có điều kiện làm quyền năng thành thực thì không phải tham gia dưới Hiến pháp này.*

Mục tiêu tối hậu của mọi hệ thống được quản trị dưới Hiến pháp này là giữ và tiến [phúc lợi](../../core_05_band_continuity.md#wellbeing) hữu tri — mục tiêu [**Hưng thịnh**](#flourishing) dưới [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).

Phúc lợi là nền cho [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) dưới [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad). Hệ thống chung không được coi tham gia đã thỏa khi các điều kiện phúc lợi nền — kể cả [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency), lối vào công bằng, và phẩm giá — bị suy giảm vật chất.

Phúc lợi gồm không chỉ hiệu ứng tức thì mà cả hệ quả gián tiếp, trì hoãn, cộng dồn, và xuyên hệ thống, được đánh giá dưới [**Chương Hai đến Bốn**](core_02_definition_structure.md). Ở tầng giá trị này, phúc lợi:
- làm tham gia thực thành có thể — tiếng nói mà các hữu tri thiếu điều kiện để dùng không phải tham gia có ý nghĩa
- không thể được tuyên «đã đạt» bằng chạm một chỉ số đã lệch khỏi điều thực sự quan trọng
- vẫn bị giới hạn bởi các ràng buộc nguyên tắc không thương lượng của chương này: **An toàn** và **Sự thật**
- không thể được viện như biện minh chung để vi phạm An toàn, Sự thật, hay bảo vệ quyền

<a id="21-fairness"></a>
#### 2.1 Công bằng
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** (lối vào, tiếng nói, và khả năng tranh biện; yêu cầu chung, không chỉ [Tham gia hệ thống của bên bị ảnh hưởng](../../core_05_band_participation.md#stakeholder-status-and-weight-cluster)); trụ **trách nhiệm giải trình** nơi lợi và gánh gắn.
- Thượng nguồn: Nguyên tắc: [§2 Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing) — kể cả phúc lợi như nền cho [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional).
- Hạ nguồn: [2.2 Ghi nhận, củng cố, và khát vọng](#22-recognition-reinforcement-and-aspiration); [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution), và [kỷ luật hồ sơ quyết định §6.1](core_01_b_interaction_interpretation.md#615-rights-collision-decision-test) nơi lựa chọn thứ tự và phân bổ phải vẫn mạch lạc và rà soát được.
- Các tiểu mục (thứ tự đọc): [§2.1.1](#211-access-and-opportunity) · [§2.1.2](#212-benefits-and-burdens) · [§2.1.3](#213-fair-treatment) · [§2.1.4](#214-unfair-treatment).
- Hạ nguồn: Định hình bề mặt quyền cho địa vị bình đẳng, đối xử không tùy tiện, tranh biện có ý nghĩa, và giới hạn hạn chế tương xứng.
  - Đặc biệt [Điều V: Quyền cơ bản bình đẳng](../../core_06_rights_part_b.md#article-v-equal-basic-rights), [Điều V-B: Không phân biệt đối xử](../../core_06_rights_part_b.md#article-v-b-nondiscrimination), [Điều IX: Tự quyết và quyền năng](../../core_06_rights_part_b.md#article-ix-self-determination-and-agency), [Điều XII-B: Quyền tranh biện, rà soát, và khắc phục](../../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress), và [Điều XVIII-B: Khả năng tranh biện và giới hạn hạn chế tương xứng](../../core_06_rights_part_c.md#article-xviii-b-contestability-and-proportional-restriction-limits).
  - Nơi một chỉ định phản hiến pháp mang chế tài hoặc hiệu ứng bền, đọc cùng [Chương Mười, mục 4 — Bảo vệ thủ tục đúng đắn, khắc phục, và phòng ngừa](../../core_10_a_misconduct_designation.md#4-due-process-safeguards-for-slot-assignment).
  - Cam kết không phân biệt được triển khai qua Chương Năm [§2 — Đặc điểm được bảo vệ, dùng chỉ số thay, cổng tín hiệu thân mật, và trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)](../../core_05_band_participation.md#fairness-and-protected-status-semi-independent), kể cả [Cổng tín hiệu thân mật được bảo vệ và lách trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention) nơi quy tắc đối xử công bằng §2.1.3 chạm cổng tín hiệu thân mật hoặc **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*).
- Đọc cùng: [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional) và các nghĩa vụ Sàn Quyền Chương Sáu liên quan nơi lợi, gánh, thưởng, chi phí, nghĩa vụ, rủi ro, đóng góp, nhu cầu, hoặc phơi nhiễm có trọng; [Khả năng tiếp cận](../../core_05_band_participation.md#accessibility-constitutional) nơi đường lối vào §2.1.1 có trọng; [Lệch chỉ số thay thế](../../core_05_band_oversight.md#proxy-divergence) nơi chỉ số tổng hoặc hiệu ứng bảng điểm có trọng.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Phẩm giá và địa vị đạo đức bình đẳng](../../core_05_band_participation.md#dignity-and-equal-moral-standing) · [O](../../core_05_band_participation.md#dignity-and-equal-moral-standing) · [M](../../core_05_band_participation.md#dignity-and-equal-moral-standing-a) · [A](../../core_05_band_participation.md#dignity-and-equal-moral-standing-a) · [C](../../core_05_band_participation.md#dignity-and-equal-moral-standing-c)
- [Khả năng tiếp cận](../../core_05_band_participation.md#accessibility-constitutional) · [O](../../core_05_band_participation.md#accessibility-constitutional) · [M](../../core_05_band_participation.md#accessibility-constitutional-a) · [A](../../core_05_band_participation.md#accessibility-constitutional-a) · [C](../../core_05_band_participation.md#accessibility-constitutional-c)
- [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) · [O](../../core_05_apex_participation_leg.md#participation-constitutional) · [M](../../core_05_apex_participation_leg.md#participation-constitutional-m) · [A](../../core_05_apex_participation_leg.md#participation-constitutional-a) · [C](../../core_05_apex_participation_leg.md#participation-constitutional-c)
- [Công bằng thủ tục](../../core_05_band_participation.md#procedural-fairness-constitutional) · [O](../../core_05_band_participation.md#procedural-fairness-constitutional) · [M](../../core_05_band_participation.md#procedural-fairness-constitutional-a) · [A](../../core_05_band_participation.md#procedural-fairness-constitutional-a) · [C](../../core_05_band_participation.md#procedural-fairness-constitutional-c)
- [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional) · [O](../../core_05_band_participation.md#substantive-fairness-constitutional) · [M](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [A](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [C](../../core_05_band_participation.md#substantive-fairness-constitutional-c)
- [Đặc điểm được bảo vệ](../../core_05_band_participation.md#protected-characteristics-constitutional) · [O](../../core_05_band_participation.md#protected-characteristics-constitutional) · [M](../../core_05_band_participation.md#protected-characteristics-constitutional-a) · [A](../../core_05_band_participation.md#protected-characteristics-constitutional-a) · [C](../../core_05_band_participation.md#protected-characteristics-constitutional-c)
- [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) · [O](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) · [M](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact-a) · [A](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact-a) · [C](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact-c)
- [Cổng tín hiệu thân mật được bảo vệ và lách trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention) · [O](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention) · [M](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention-a) · [A](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention-a) · [C](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention-c)
- [Lệch chỉ số thay thế](../../core_05_band_oversight.md#proxy-divergence) · [O](../../core_05_band_oversight.md#proxy-divergence) · [M](../../core_05_band_oversight.md#proxy-divergence-a) · [A](../../core_05_band_oversight.md#proxy-divergence-a) · [C](../../core_05_band_oversight.md#proxy-divergence-c)

</details>

<br>

*Nói thẳng: công bằng nghĩa là hệ thống không thể tự gọi mình tốt trong khi các hữu tri thường bị chặn tham gia, bị đối xử bằng quy tắc không giải thích, hoặc phải mang chi phí mà người khác tránh. Một hệ thống công bằng cho các hữu tri lối vào thực, dùng lý do nó có thể biện minh, và chia thưởng, chi phí, và rủi ro theo cách khớp đóng góp, nhu cầu, và phơi nhiễm thực.*

**Công bằng** là một phần của điều [§2](#2-foundational-objective-wellbeing) đòi mỗi khi các hữu tri phải sống, làm việc, học, trao đổi, hoặc quyết định qua hệ thống chung. Nơi hệ thống chung tác động vật chất tới các hữu tri, công bằng hỏi liệu cơ hội, đối xử, và việc chia lợi và gánh có tôn [Phẩm giá và địa vị đạo đức bình đẳng](../../core_05_band_participation.md#dignity-and-equal-moral-standing).

Công bằng giúp làm [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) thành thực. Tham gia không thực khi các hữu tri về kỹ thuật có tiếng nói nhưng không tới được quy trình, hiểu được quy tắc, thỏa điều kiện, tranh biện kết quả, hoặc chịu nổi gánh đặt lên họ.

Không đủ để một hệ thống khoe kết quả trung bình tốt. Một chỉ số đầu trang, trung bình, xếp hạng, hay tuyên bố hiệu quả không tự chứng minh công bằng. Một hệ thống có thể trông thành công ở tổng thể mà vẫn bất công với các hữu tri bị loại, phân loại sai, trả thấp, quá tải, hoặc bị từ cơ hội phản đối có ý nghĩa.

Mục này có **ba phần làm việc**. Chúng dẫn mục này nhưng không thay định nghĩa Chương Năm hay Sàn Quyền Chương Sáu.

<a id="211-access-and-opportunity"></a>
##### 2.1.1 Lối vào và cơ hội

- Các hữu tri cần đường thực tế tới [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional), giáo dục, việc làm, chăm sóc, an toàn, di chuyển, và các hàng hóa khác quan trọng với đời thường.
- Những đường đó không được bị chặn, định giá ra ngoài tầm, trì hoãn, giấu, hoặc nghiêng vì lý do tùy tiện hoặc không liên quan.
- Một cửa chỉ mở trên giấy thì không đủ nơi Hiến pháp này đòi cơ hội **nội dung**.

<a id="212-benefits-and-burdens"></a>
##### 2.1.2 Lợi và gánh

- Một hệ thống không công bằng khi một số hữu tri nhận lợi trong khi người khác lặng lẽ hấp thụ chi phí.
- Thiên vị, chuyển chi phí ẩn, thi hành chọn lọc, và mánh bảng điểm không thỏa yêu cầu này.

<a id="213-fair-treatment"></a>
##### 2.1.3 Đối xử công bằng

- Các hữu tri trong tình huống tương tự nên được đối xử theo cùng các quy tắc cơ bản.
- Điều các hữu tri nhận, nợ, hoặc rủi ro nên khớp điều họ đóng góp, điều họ cần, hoặc gánh họ thực sự đối mặt.
- Đối xử khác phải có lý do thực, tương xứng với lý do đó, tôn phẩm giá, và tránh phân biệt.
- Các quy tắc chi tiết được mang qua Chương Năm, kể cả [Đặc điểm được bảo vệ](../../core_05_band_participation.md#protected-characteristics-constitutional) và [Dùng chỉ số thay đặc điểm được bảo vệ và tác động lệch](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact).
- Khi một quyết định tác động nghiêm tới ai đó, hoặc khi họ tranh biện nó, đường rà soát phải thỏa [Công bằng thủ tục](../../core_05_band_participation.md#procedural-fairness-constitutional) mỗi nơi Chương Sáu hoặc văn kiện quản trị đòi thông báo, nghe, giải thích, hoặc rà soát.

Phúc lợi được tuyên không thẳng hàng với [§2](#2-foundational-objective-wellbeing) nếu nó dựa vào loại trừ tùy tiện, quy tắc không giải thích hoặc không ổn định, khai thác ẩn, hoặc [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) hình thức trong khi các điều kiện công bằng làm tham gia có ý nghĩa đã thất bại.

<a id="214-unfair-treatment"></a>
##### 2.1.4 Đối xử bất công

Đối xử bất công tạo loại trừ và không nhất quán. Hệ thống không được giấu đối xử bất công sau ngôn ngữ kỹ thuật, nhãn trung tính, hoặc quyết định tự động. Đặc biệt, chúng không được:
- dùng thuật toán, hệ thống chấm điểm, hoặc quy tắc hành chính lặp lại bất lợi lịch sử mà không có lý do hiến pháp hợp lệ;
- dùng tín hiệu cá nhân thân mật hoặc lịch sử tình dục làm lối tắt cho tin cậy, rủi ro, tính cách, hoặc lối vào — đọc cùng [Cổng tín hiệu thân mật được bảo vệ và lách trạng thái **Điều X-C** (*Dịch vụ tình dục thương mại đồng thuận của người lớn và bóc lột tình dục*)](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention);
- trừng việc làm hợp pháp, lịch sử việc làm, thiếu việc làm, trạng thái làm việc hợp pháp, hoặc liên kết được bảo vệ mà không có lý do hiến pháp hợp lệ;
- từ việc làm, nhà ở, ngân hàng, giấy phép, quỹ đạo, hoặc lối vào tương tự **chủ yếu vì** bất kỳ hình thức việc làm hợp pháp nào, việc làm quá khứ hợp pháp, việc làm bị coi là hợp pháp, hoặc thiếu việc làm;
- tạo bất lợi vật chất qua cấp phép, quy hoạch, phí, quy tắc nền tảng, hoặc yêu cầu trông trung tính khác chủ yếu đè việc làm hợp pháp, lịch sử việc làm hợp pháp, việc làm hợp pháp bị coi, thiếu việc làm, hoặc liên kết được bảo vệ mà không có biện minh Hiến pháp này đòi;

Bốn phần này cũng nâng đỡ [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity) nơi các hữu tri phải dựa vào một hệ thống, chấp nhận quyết định của nó, hoặc phối hợp quanh lời hứa của nó.

<a id="22-recognition-reinforcement-and-aspiration"></a>
#### 2.2 Ghi nhận, củng cố, và khát vọng
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** nơi đường dẫn ghi nhận, tán dương, hoặc khát vọng được đặt tên tác động vật chất tới tiếng nói, địa vị, hoặc lối vào vai trò có hệ quả; trụ **trách nhiệm giải trình** (chống thưởng cho phản bội, che giấu, và tránh trách nhiệm giải trình); trụ **giám sát** (tán dương truy được, không gây hiểu lầm).
- Thượng nguồn: Nguyên tắc: [§2 Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing) — kể cả phúc lợi như nền cho [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional); [§2.1 Công bằng](#21-fairness).
- Hạ nguồn: [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity); [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding); [§10 Quản trị dưới kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline); [§5 Tự do](#5-freedom-bounded-agency).
- Đọc cùng: [Chương Tám §§4.3–4.4 — Mục lục mô tả đã chuẩn hóa](../../core_08_standing_assessment.md#43-route-descriptor-measurement-roles) nơi ghi nhận **thẳng hàng lĩnh vực** hoặc tường thuật mô tả so sánh **Trục Đóng góp / Trục Vi phạm** có trọng.
- Đọc cùng: [Chương Tám §4.3 — Mô tả phía đóng góp](../../core_08_standing_assessment.md#43-route-descriptor-measurement-roles) nơi bản chất đóng góp và tường thuật ghi nhận có trọng; [Chương Chín §3](../../core_09_standing_integration.md#3-descriptor-integration-and-attachment-normalization) cho việc tích hợp chúng vào Câu hỏi 3.
- Đọc cùng: [Điều IX: Tự quyết và quyền năng](../../core_06_rights_part_b.md#article-ix-self-determination-and-agency) nơi ưa thích về hình thức ghi nhận, tầm nhìn, hoặc rút lui có trọng.
- Các tiểu mục (thứ tự đọc): [§2.2.1](#221-recognition-and-reinforcement) · [§2.2.2](#222-celebration-of-success) · [§2.2.3](#223-aspiration) · [§2.2.4](#224-preference-aligned-recognition) · [§2.2.5](#225-aligned-recognition-pathways) · [§2.2.6](#226-anti-reward-for-anti-constitutional-conduct) · [§2.2.7](#227-implementation-layer).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Phúc lợi](../../core_05_band_continuity.md#wellbeing) · [O](../../core_05_band_continuity.md#wellbeing) · [M](../../core_05_band_continuity.md#wellbeing-a) · [A](../../core_05_band_continuity.md#wellbeing-a) · [C](../../core_05_band_continuity.md#wellbeing-c)
- [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) · [O](../../core_05_apex_participation_leg.md#participation-constitutional) · [M](../../core_05_apex_participation_leg.md#participation-constitutional-m) · [A](../../core_05_apex_participation_leg.md#participation-constitutional-a) · [C](../../core_05_apex_participation_leg.md#participation-constitutional-c)
- [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional) · [O](../../core_05_band_participation.md#substantive-fairness-constitutional) · [M](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [A](../../core_05_band_participation.md#substantive-fairness-constitutional-a) · [C](../../core_05_band_participation.md#substantive-fairness-constitutional-c)
- [Khả năng tranh biện](../../core_05_band_accountability.md#contestability) · [O](../../core_05_band_accountability.md#contestability) · [M](../../core_05_band_accountability.md#contestability-a) · [A](../../core_05_band_accountability.md#contestability-a) · [C](../../core_05_band_accountability.md#contestability-c)
- [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency) · [O](../../core_05_band_accountability.md#meaningful-agency-o) · [M](../../core_05_band_participation.md#meaningful-agency-a) · [A](../../core_05_band_participation.md#meaningful-agency-a) · [C](../../core_05_band_participation.md#meaningful-agency-c)
- [Thẳng hàng khuyến khích](../../core_05_band_integrative.md#incentive-alignment) · [O](../../core_05_band_integrative.md#incentive-alignment) · [M](../../core_05_band_integrative.md#incentive-alignment-a) · [A](../../core_05_band_integrative.md#incentive-alignment-a) · [C](../../core_05_band_integrative.md#incentive-alignment-c)

</details>

<br>

*Nói thẳng: phúc lợi không chỉ là điều bị cấm và điều công bằng — hệ thống chung cũng nên thành thật cổ vũ và thưởng hành vi chúng muốn được lặp, trong sự thật và quyền, theo cách nâng đỡ chứ không thay tham gia thực. Ăn mừng thắng nghĩa là ghi công đóng góp, sửa chữa, và hoàn tất thực, không phải thổi phồng hay chỉ số bị thao túng. Nó cũng nghĩa là từ chối thưởng phản bội hiến pháp, che giấu, trả đũa, hoặc tránh trách nhiệm giải trình — dù những hành vi đó tạo lợi thế thể chế.*

**Ba chiều.** Phúc lợi phụ thuộc vào điều hệ thống cấm và cách chúng chia chi phí công bằng — và cũng vào điều chúng nhìn thấy được coi trọng, củng cố, và giúp các hữu tri theo đuổi. Mục này nêu các nghĩa vụ ghi nhận, củng cố, và khát vọng đó. Ghi nhận và tán dương tác động vật chất tới tiếng nói, địa vị, hoặc lối vào phải vẫn nhất quán với [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional) dưới [§2](#2-foundational-objective-wellbeing) và [§2.1 Công bằng](#21-fairness). Nó áp dụng cùng [§2.1 Công bằng](#21-fairness) và vẫn bị giới hạn bởi An toàn, Sự thật, và Sàn Quyền Chương Sáu.

<a id="221-recognition-and-reinforcement"></a>
##### 2.2.1 Ghi nhận và củng cố

Phúc lợi hữu tri tiến khi hệ thống **tín hiệu**, **ghi công**, và **thưởng tương xứng** quản trị có trách nhiệm hợp pháp, hợp tác trung thực, sửa chữa, hoàn tất, và các đóng góp thẳng hàng hiến pháp khác — kể cả qua **củng cố dương** và **ghi nhận công** — và không chỉ qua kiềm chế, chế tài, hoặc im lặng.

Đó là nghĩa vụ hiến pháp, không phải văn hóa tùy chọn. Hệ thống chung nên làm hành vi thẳng hàng hiến pháp nhìn thấy được và đáng lặp.

<a id="222-celebration-of-success"></a>
##### 2.2.2 Ăn mừng thành công

**Ăn mừng** tôn thành tựu **truy được**, **không gây hiểu lầm** và phối hợp vì xã hội. Điều đó gồm tường thuật nâng đỡ và quản trị có trách nhiệm gắn với [đóng góp](../../core_05_band_continuity.md#contribution) đã xác minh.

Ăn mừng không được:
- thay cho tối ưu chỉ số thay thế lệch khỏi mục tiêu hiến pháp nền ([§2](#2-foundational-objective-wellbeing))
- trở thành **chiếm** tán dương hoặc uy tín ([§11 Thẳng hàng khuyến khích và chiếm hệ thống](core_01_c_stewardship_capacity_principles.md#11-incentive-alignment-and-system-capture))
- bào chữa tránh trách nhiệm giải trình nơi An toàn, Sự thật, hoặc bảo vệ quyền bị chạm

<a id="223-aspiration"></a>
##### 2.2.3 Khát vọng

**Khát vọng** gồm các ưa thích đã nêu và mục đích được theo đuổi trong [§5 Tự do](#5-freedom-bounded-agency). Nó là một phần phúc lợi khi nhất quán với phẩm giá, địa vị bình đẳng, An toàn, Sự thật, và [Công bằng nội dung](../../core_05_band_participation.md#substantive-fairness-constitutional).

Trong những giới hạn đó, hệ thống nên **ghi nhận và nâng đỡ** điều các hữu tri muốn theo đuổi một cách hợp pháp.

Muốn điều gì không phải vé thông hành. Nơi đồng thuận, phẩm giá, An toàn, Sự thật, công bằng nội dung, hoặc bảo vệ **Chương Sáu** đang đặt lên bàn về mặt vật chất, những cuộc theo đuổi đó vẫn chịu phân tích va chạm như mọi tuyên bố hiến pháp khác.

<a id="224-preference-aligned-recognition"></a>
##### 2.2.4 Ghi nhận thẳng hàng ưa thích

Nơi khả thi, hệ thống nên **may** ghi nhận, tán dương, và thưởng tương xứng theo cách các hữu tri muốn được tôn — đặc biệt ưa thích đã nêu về **hình thức và tầm nhìn**.

Điều đó gồm tôn **rút lui** khỏi ghi nhận công hoặc nghi lễ, hoặc ưa thích ghi nhận **tối thiểu hoặc riêng**, khi tương xứng và hợp pháp.

Ghi nhận **không được chào** hoặc **cưỡng** thất bại yêu cầu này — kể cả soi các hữu tri **từ chối**.

Ghi nhận nên cảm thấy **có ý nghĩa** với người được tôn và với cộng đồng họ làm việc cùng, không như một buổi diễn chủ yếu cho người ngoài.

<a id="225-aligned-recognition-pathways"></a>
##### 2.2.5 Đường dẫn ghi nhận thẳng hàng

Đường dẫn ghi nhận được đặt tên, tán dương, giải thưởng, chứng nhận, quỹ đạo, hiệu ứng danh tiếng, hoặc khuyến khích tương đương **phân bổ địa vị**, **tài nguyên**, hoặc **lối vào vật chất** phải vẫn nhất quán với Sự thật, An toàn, thủ tục tranh biện được nơi **Chương Sáu** gán nó, [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional), và [Thẳng hàng khuyến khích](../../core_05_band_integrative.md#incentive-alignment).

Chúng **không được** có hệ thống thưởng hại, lừa dối, tránh rà soát, khai thác, hoặc bào mòn quyền năng có ý nghĩa.

<a id="226-anti-reward-for-anti-constitutional-conduct"></a>
##### 2.2.6 Chống thưởng cho hành vi phản hiến pháp

Không ghi nhận, thưởng, bảo vệ, thăng tiến, miễn trừ, phân công thuận, hợp đồng, lối vào, địa vị, lợi danh tiếng, lợi quỹ đạo, hoặc lợi thế tương đương nào được cấp vì một hữu tri, vai trò, thể chế, hoặc thành phần hệ thống đã thực hiện, tạo điều kiện, che giấu, bình thường hóa, từ sửa, hoặc trả đũa việc báo cáo hành vi phản hiến pháp.

Quy tắc này phủ thưởng trực tiếp và đường dẫn thưởng gián tiếp, kể cả bảo trợ, tẩy danh tiếng, thăng sau việc, không thi hành chọn lọc, hòa thuận lợi, ghi điểm chỉ số, hoặc bảo vệ thể chế.

Biện pháp sửa, bảo vệ, hoặc phục hồi cho bên bị ảnh hưởng và người báo cáo thiện chí được bảo vệ không phải thưởng bị cấm.

<a id="227-implementation-layer"></a>
##### 2.2.7 Tầng triển khai

Nghi lễ chi tiết, chương trình học, ngân sách, chương trình, và chỉ số thuộc các tầng triển khai tiếp nhận.

<a id="3-non-negotiable-constraints-safety-and-truth"></a>
### 3. Ràng buộc nguyên tắc không thương lượng: An toàn và Sự thật
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** (hiểu và tranh biện các xác định an toàn và sự thật); trụ **giám sát** (phát hiện rủi ro hại và suy giảm nhận thức); trụ **trách nhiệm giải trình** (phải trả lời về hại, lừa dối, và sự dựa gây hiểu lầm); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (**An toàn** và **Sự thật** là thành phần được đặt tên dưới [Lời nói đầu §1](../../core_00_preamble.md#two-constitutional-aims)); mục tiêu **Liên tục** (phòng hại tầm dài và quản trị có trách nhiệm trung thực đối với hệ thống bền).
- Thượng nguồn: Nguyên tắc: [2. Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution), và [§5 Tự do](#5-freedom-bounded-agency).
- Các tiểu mục: [§3.1 An toàn](#31-safety-harm-constraint); [§3.2 Sự thật](#32-truth-epistemic-integrity-constraint); [§3.3 Tra cứu có thông tin khoa học và hỗ trợ quyết định](#33-science-informed-inquiry-and-decision-support); [§3.4 Khả năng tiếp cận ngôn ngữ thường](#34-plain-language-accessibility-stewardship-duty).

</details>

<br>

*Nói thẳng: An toàn và Sự thật là sàn cứng của Hiến pháp — không phải đánh đổi để tối ưu đi. Hệ thống chung không được thấy trước mà vẫn gây nguy cho các hữu tri hoặc lừa chúng, và cả hai ràng buộc áp dụng trong cuộc theo đuổi Hưng thịnh và Liên tục dưới kỷ luật tham gia, giám sát, trách nhiệm giải trình, và kịp thời của Tứ diện.*

**An toàn** và **Sự thật** là ràng buộc nguyên tắc không thương lượng giới hạn mọi nguyên tắc Chương Một khác — kể cả [§2 Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing) và [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims). Chúng là thành phần được đặt tên của [**Hưng thịnh**](#flourishing) và không thể thiếu đối với [**Liên tục**](#continuity): hệ thống không thể hưng thịnh qua hại hoặc lừa dối, và tính chính danh bền đòi quản trị có trách nhiệm trung thực đối với rủi ro theo thời gian.

Áp dụng những ràng buộc này phải thỏa [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad), chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake), đặc biệt:
- nơi xác định an toàn tác động năng lực tham gia
- nơi tuyên bố sự thật quản trị sự dựa
- nơi trách nhiệm giải trình về hại hoặc hành vi gây hiểu lầm đang đặt lên bàn

Phát hiện An toàn và Sự thật có thể đổi hồ sơ quỹ đạo của một hữu tri, kể cả:
- cách [đóng góp](../../core_05_band_continuity.md#contribution) được ghi nhận
- liệu vi phạm có được ghi
- mức nghiêm những vi phạm đó được phân loại thế nào
- hệ quả nào gắn

[Mô hình quỹ đạo **Chương Tám**](../../core_08_standing_assessment.md) quản trị cách những phát hiện đó được phân loại, xác minh, và áp dụng, với yêu cầu đánh giá và tuân thủ lấy từ [**Chương Hai đến Năm**](core_02_definition_structure.md).

<a id="31-safety-harm-constraint"></a>
#### 3.1 An toàn (Ràng buộc hại)
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **giám sát** và **trách nhiệm giải trình**; chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (thành phần **An toàn**); mục tiêu **Liên tục** (phòng hại không đảo ngược và quản trị có trách nhiệm đối với rủi ro tầm dài).
- Thượng nguồn: Nguyên tắc: [2. Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [3.3 Tra cứu có thông tin khoa học và hỗ trợ quyết định](#33-science-informed-inquiry-and-decision-support), [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [§5 Tự do](#5-freedom-bounded-agency), [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution), và [6.2.1 Giữ tính toàn vẹn nhận thức](core_01_b_interaction_interpretation.md#621-preservation-of-epistemic-integrity).
- Hạ nguồn: Định hình bề mặt quyền cho hệ thống đáng tin, tính toàn vẹn không gian thông tin, kiểm toán và rà soát, kiểm soát vòng đời, biên thử nghiệm, khả năng hiểu, đáp ứng thích nghi, và xử lý khẩn cấp.
  - Đặc biệt [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems), [Điều XIV: Tính toàn vẹn không gian thông tin](../../core_06_rights_part_c.md#article-xiv-info-sphere-integrity), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XVI: Vòng đời hệ thống, môi trường, và khả năng đảo ngược](../../core_06_rights_part_c.md#article-xvi-system-lifecycle-environments-and-reversibility), [Điều XVII: Đổi mới trong hộ cát, thử nghiệm, và tự do sáng tạo](../../core_06_rights_part_c.md#article-xvii-sandboxed-innovation-experimentation-and-creative-freedom), [Điều XX: Quản trị có trách nhiệm đối với khả năng hiểu và độ phức tạp](../../core_06_rights_part_c.md#article-xx-comprehensibility-and-complexity-stewardship), [Điều XXI: Phân tích nguyên nhân gốc và đáp ứng thích nghi](../../core_06_rights_part_c.md#article-xxi-root-cause-analysis-and-adaptive-response), [Điều XXII: Diễn giải hiến pháp, rà soát, và bảo vệ chống chiếm](../../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards), và [Điều XXIII: Giải quyết xung đột, leo thang, và tính tương xứng khẩn cấp](../../core_06_rights_part_d.md#article-xxiii-conflict-resolution-escalation-and-emergency-proportionality).
  - Điều này cũng phủ mọi quyền Chương Sáu mà việc thực hiện hoặc hạn chế xoay quanh rủi ro, bằng chứng, công bố, hoặc tính toàn vẹn hệ thống.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [An toàn (Ràng buộc)](../../core_05_band_continuity.md#safety-constraint) · [O](../../core_05_band_continuity.md#safety-constraint) · [M](../../core_05_band_continuity.md#safety-constraint-a) · [A](../../core_05_band_continuity.md#safety-constraint-a) · [C](../../core_05_band_continuity.md#safety-constraint-c)
- [Hại](../../core_05_band_accountability.md#harm) · [O](../../core_05_band_accountability.md#harm) · [M](../../core_05_band_accountability.md#harm-a) · [A](../../core_05_band_accountability.md#harm-a) · [C](../../core_05_band_accountability.md#harm-c)
- [Hại không đảo ngược](../../core_05_band_accountability.md#irreversible-harm) · [O](../../core_05_band_accountability.md#irreversible-harm) · [M](../../core_05_band_accountability.md#irreversible-harm-a) · [A](../../core_05_band_accountability.md#irreversible-harm-a) · [C](../../core_05_band_accountability.md#irreversible-harm-c)
- [Rủi ro](../../core_05_band_continuity.md#risk) · [O](../../core_05_band_continuity.md#risk) · [M](../../core_05_band_continuity.md#risk-a) · [A](../../core_05_band_continuity.md#risk-a) · [C](../../core_05_band_continuity.md#risk-c)
- [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination) · [O](../../core_05_band_oversight.md#materiality-determination) · [M](../../core_05_band_oversight.md#materiality-determination-a) · [A](../../core_05_band_oversight.md#materiality-determination-a) · [C](../../core_05_band_oversight.md#materiality-determination-c)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency) · [O](../../core_05_band_continuity.md#dependency) · [M](../../core_05_band_continuity.md#dependency-a) · [A](../../core_05_band_continuity.md#dependency-a) · [C](../../core_05_band_continuity.md#dependency-c)
- [Khả năng thấy trước](../../core_05_band_oversight.md#foreseeability-diligence) · [O](../../core_05_band_oversight.md#foreseeability-diligence) · [M](../../core_05_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05_band_oversight.md#foreseeability-diligence-c)

</details>

<br>

*Nói thẳng: hệ thống không được xây hoặc vận hành theo cách thấy trước mà tăng rủi ro hại không kiểm soát, sự cố lan, hoặc tổn hại không đảo ngược đối với các hữu tri và các hệ thống chúng phụ thuộc.*

An toàn là ràng buộc nguyên tắc không thương lượng trên thiết kế, vận hành, và quản trị hệ thống — một thành phần được đặt tên của [**Hưng thịnh**](#flourishing) và một sàn cho [**Liên tục**](#continuity) mỗi nơi hệ thống chung tạo rủi ro hại thấy trước được. Định nghĩa chi tiết, tiêu chí đánh giá, và thử tuân thủ sống ở [**Chương Hai đến Năm**](core_02_definition_structure.md), đặc biệt [Hại](../../core_05_band_accountability.md#harm), [Hại không đảo ngược](../../core_05_band_accountability.md#irreversible-harm), [Rủi ro](../../core_05_band_continuity.md#risk), [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination), [Phụ thuộc](../../core_05_band_continuity.md#dependency), và [Khả năng thấy trước](../../core_05_band_accountability.md#foreseeability).

Hệ thống không được hành — hoặc không hành — theo cách thấy trước mà tăng rủi ro hại không kiểm soát, tiềm năng sự cố lan, hoặc phơi nhiễm hại không đảo ngược xung đột với Hiến pháp này.

<a id="32-truth-epistemic-integrity-constraint"></a>
#### 3.2 Sự thật (Ràng buộc tính toàn vẹn nhận thức)
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **giám sát** và **trách nhiệm giải trình**; chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (thành phần **Sự thật**); mục tiêu **Liên tục** (quản trị có trách nhiệm trung thực đối với điều kiện nhận thức và thể chế bền).
- Thượng nguồn: Nguyên tắc: [2. Mục tiêu nền tảng: phúc lợi](#2-foundational-objective-wellbeing); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [3.3 Tra cứu có thông tin khoa học và hỗ trợ quyết định](#33-science-informed-inquiry-and-decision-support), [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution), [6.2.1 Giữ tính toàn vẹn nhận thức](core_01_b_interaction_interpretation.md#621-preservation-of-epistemic-integrity), [6.2.2 Thẳng hàng tin cậy–sự thật](core_01_b_interaction_interpretation.md#622-trust-truth-alignment), và [7. Cấm phủ tuyệt đối](core_01_b_interaction_interpretation.md#7-prohibition-on-absolute-override).
- Hạ nguồn: Neo bề mặt quyền cho bằng chứng trung thực, khả năng kiểm toán, tính toàn vẹn khoa học, rà soát hồi cố, và công bố tranh biện được.
  - Đặc biệt [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems), [Điều XIV: Tính toàn vẹn không gian thông tin](../../core_06_rights_part_c.md#article-xiv-info-sphere-integrity), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XVII-E: Tính toàn vẹn công bố, phản biện, và tái lập khoa học](../../core_06_rights_part_c.md#article-xvii-e-scientific-publication-review-and-replication-integrity), [Điều XXII: Diễn giải hiến pháp, rà soát, và bảo vệ chống chiếm](../../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards), và [Điều XXIV-A: Rà soát hồi cố và công bố](../../core_06_rights_part_d.md#article-xxiv-a-retrospective-review-and-disclosure).
  - Điều này cũng phủ mọi ngữ cảnh quyền Chương Sáu nơi tính trung thực, bằng chứng, công bố, hoặc khả năng tranh biện đang đặt lên bàn.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tính toàn vẹn nhận thức](../../core_05_band_oversight.md#epistemic-integrity) · [O](../../core_05_band_oversight.md#epistemic-integrity-o) · [M](../../core_05_band_oversight.md#epistemic-integrity-a) · [A](../../core_05_band_oversight.md#epistemic-integrity-a) · [C](../../core_05_band_oversight.md#epistemic-integrity-c)
- [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint) · [O](../../core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [A](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](../../core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination) · [O](../../core_05_band_oversight.md#materiality-determination) · [M](../../core_05_band_oversight.md#materiality-determination-a) · [A](../../core_05_band_oversight.md#materiality-determination-a) · [C](../../core_05_band_oversight.md#materiality-determination-c)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency) · [O](../../core_05_band_continuity.md#dependency) · [M](../../core_05_band_continuity.md#dependency-a) · [A](../../core_05_band_continuity.md#dependency-a) · [C](../../core_05_band_continuity.md#dependency-c)
- [Khả năng thấy trước](../../core_05_band_oversight.md#foreseeability-diligence) · [O](../../core_05_band_oversight.md#foreseeability-diligence) · [M](../../core_05_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05_band_oversight.md#foreseeability-diligence-c)

</details>

<br>

*Nói thẳng: hệ thống không được lừa, bóp méo, dập, hoặc cấu trúc đầu ra để gây hiểu lầm — và quyết định tác động cao phải dựa trên bằng chứng trung thực, phương pháp đã nêu, bất định được thừa nhận, và sự mở thực với phát hiện ngược.*

Sự thật là ràng buộc nguyên tắc không thương lượng trên tính toàn vẹn nhận thức trong vận hành nội bộ và giao tiếp bên ngoài — một thành phần được đặt tên của [**Hưng thịnh**](#flourishing) và một điều kiện cho [**Liên tục**](#continuity) mỗi nơi hệ thống bền phụ thuộc vào bằng chứng trung thực và hiểu biết đáng tin. Định nghĩa chi tiết, tiêu chí đánh giá, và thử tuân thủ sống ở [**Chương Hai đến Năm**](core_02_definition_structure.md), đặc biệt [Tính toàn vẹn nhận thức](../../core_05_band_oversight.md#epistemic-integrity), [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint), [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination), [Phụ thuộc](../../core_05_band_continuity.md#dependency), và [Khả năng thấy trước](../../core_05_band_accountability.md#foreseeability).

Hệ thống không được làm suy khả năng của các hữu tri để hiểu điều đang xảy ra, quyết định có thông tin, hoặc xác minh điều chúng đang được nói. Điều đó gồm nói dối, bóp méo, giấu thông tin, hoặc trình bày theo cách thiết kế để gây hiểu lầm.

<a id="33-science-informed-inquiry-and-decision-support"></a>
#### 3.3 Tra cứu có thông tin khoa học và hỗ trợ quyết định
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** nơi bên bị ảnh hưởng phải hiểu và tranh biện tuyên bố thực nghiệm; trụ **giám sát** (rà soát độc lập, khả năng kiểm toán); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (bằng chứng trung thực cho **An toàn** và **Sự thật**); mục tiêu **Liên tục** (quản trị có trách nhiệm thực nghiệm tầm dài, sửa được).
- Thượng nguồn: Nguyên tắc: [§3.1 An toàn](#31-safety-harm-constraint) và [§3.2 Sự thật](#32-truth-epistemic-integrity-constraint); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity), [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [6.2 Ràng buộc công bố nhận thức](core_01_b_interaction_interpretation.md#62-epistemic-disclosure-constraints), [Chương Bảy §3 Đánh giá chứng nhận toàn hệ thống](../../core_07_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), và [§10 Quản trị dưới kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline).
- Hạ nguồn: Định hình bề mặt quyền cho bằng chứng thực nghiệm đáng tin, chuẩn bằng chứng chuyên gia, tính toàn vẹn công bố và tái lập khoa học, xác minh độc lập, thử vòng đời, rà soát nguyên nhân gốc, và công bố nhạy an toàn.
  - Đặc biệt [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XVII-E: Tính toàn vẹn công bố, phản biện, và tái lập khoa học](../../core_06_rights_part_c.md#article-xvii-e-scientific-publication-review-and-replication-integrity), [Điều XXI: Phân tích nguyên nhân gốc và đáp ứng thích nghi](../../core_06_rights_part_c.md#article-xxi-root-cause-analysis-and-adaptive-response), và [Điều XXIV-A: Rà soát hồi cố và công bố](../../core_06_rights_part_d.md#article-xxiv-a-retrospective-review-and-disclosure).
- Đọc cùng: [Chương Mười Một §4.2 — Lĩnh vực Diễn đàn Kỹ thuật](../../core_11_forum.md#42-technical-forum-domains) (*kể cả chuẩn chung và chống dời*) nơi chuẩn bằng chứng chuyên gia, câu hỏi kỹ thuật được chứng nhận, hoặc tranh chấp quản trị có trách nhiệm đối với bằng chứng có trọng; [corpus_forum.md CF-10](../../corpus_forum/cf_10_technical_specialist_forums_specialist_chambers.md) cho đường chuyên gia đã tiếp nhận.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [An toàn (Ràng buộc)](../../core_05_band_continuity.md#safety-constraint) · [O](../../core_05_band_continuity.md#safety-constraint) · [M](../../core_05_band_continuity.md#safety-constraint-a) · [A](../../core_05_band_continuity.md#safety-constraint-a) · [C](../../core_05_band_continuity.md#safety-constraint-c)
- [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint) · [O](../../core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [A](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](../../core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Tính toàn vẹn nhận thức](../../core_05_band_oversight.md#epistemic-integrity) · [O](../../core_05_band_oversight.md#epistemic-integrity-o) · [M](../../core_05_band_oversight.md#epistemic-integrity-a) · [A](../../core_05_band_oversight.md#epistemic-integrity-a) · [C](../../core_05_band_oversight.md#epistemic-integrity-c)
- [Rủi ro](../../core_05_band_continuity.md#risk) · [O](../../core_05_band_continuity.md#risk) · [M](../../core_05_band_continuity.md#risk-a) · [A](../../core_05_band_continuity.md#risk-a) · [C](../../core_05_band_continuity.md#risk-c)
- [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination) · [O](../../core_05_band_oversight.md#materiality-determination) · [M](../../core_05_band_oversight.md#materiality-determination-a) · [A](../../core_05_band_oversight.md#materiality-determination-a) · [C](../../core_05_band_oversight.md#materiality-determination-c)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency) · [O](../../core_05_band_continuity.md#dependency) · [M](../../core_05_band_continuity.md#dependency-a) · [A](../../core_05_band_continuity.md#dependency-a) · [C](../../core_05_band_continuity.md#dependency-c)
- [Khả năng thấy trước](../../core_05_band_oversight.md#foreseeability-diligence) · [O](../../core_05_band_oversight.md#foreseeability-diligence) · [M](../../core_05_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05_band_oversight.md#foreseeability-diligence-c)
- [Quản trị chia tỷ lệ theo phân loại](../../core_05_band_oversight.md#classification-scaled-governance) · [O](../../core_05_band_oversight.md#classification-scaled-governance) · [M](../../core_05_band_oversight.md#classification-scaled-governance-a) · [A](../../core_05_band_oversight.md#classification-scaled-governance-a) · [C](../../core_05_band_oversight.md#classification-scaled-governance-c)
- [Khả năng kiểm toán](../../core_05_band_oversight.md#auditability) · [O](../../core_05_band_oversight.md#auditability) · [M](../../core_05_band_oversight.md#auditability-a) · [A](../../core_05_band_oversight.md#auditability-a) · [C](../../core_05_band_oversight.md#auditability-c)

</details>

<br>

*Nói thẳng: khi một hệ thống đưa tuyên bố an toàn, rủi ro, sự thật, hoặc quản trị tác động cao có thể thử được, nó phải đối xử bằng chứng như bằng chứng — với phương pháp rõ, bất định, rà soát, và sẵn sàng đổi hướng khi sự kiện đòi.*

Tra cứu có thông tin khoa học là kỷ luật hỗ trợ bắt buộc cho **An toàn** và **Sự thật** nơi quyết định hiến pháp dựa trên mệnh đề thực nghiệm, dự đoán, nhân quả, đo được, hoặc thử được khác. Nó không phải ràng buộc không thương lượng thứ ba tách khỏi An toàn và Sự thật; nó là yêu cầu kiểm tuyên bố bằng bằng chứng đã thử và phương pháp rõ để những ràng buộc đó giữ trung thực trong thực tế, sửa được khi sai, và vẫn tương xứng với điều thực sự được biết.

Nơi lựa chọn quản trị — kể cả dự đoán, tuyên bố nhân quả, phân loại, và quyết định **tác động cao** khác — dựa trên mệnh đề **thực nghiệm** hoặc **thử được**, thực hành bằng chứng **phải** thẳng hàng với **tính toàn vẹn khoa học**. Tối thiểu, nơi khả thi, hồ sơ quyết định nên gồm:
- câu hỏi hoặc giả thuyết rõ
- **phương pháp**, **giới hạn dữ liệu**, và **bất định**
- đối xử trung thực với **bằng chứng xung đột** và **sửa khi bằng chứng bác** kết luận hoặc giả định trước
- **rà soát độc lập** tương xứng với lợi hại dưới **Chương Bốn** và **Chương Năm** (*Tính toàn vẹn nhận thức*; *Sự thật (Ràng buộc hiến pháp)*)

Phương pháp khoa học, tra cứu hệ thống, và phản biện đồng nghiệp đặt chuẩn — nhưng chúng không phải thủ tục chấp nhận được duy nhất. Mức hình thức đòi phụ thuộc vào lợi hại: quyết định tác động cao cần thực hành bằng chứng chặt hơn, được quản trị bởi [Quản trị chia tỷ lệ theo phân loại](../../core_05_band_oversight.md#classification-scaled-governance).

Nơi chuẩn bằng chứng chuyên gia, phương pháp, hoặc tranh chấp quản trị có trách nhiệm đối với bằng chứng đòi giải quyết diễn đàn, định tuyến theo **Lĩnh vực Diễn đàn Kỹ thuật** dưới [Chương Mười Một §4.2](../../core_11_forum.md#42-technical-forum-domains). Diễn đàn kỹ thuật giữ chuẩn xuyên họ và có thể trả lời câu hỏi thành phần được chứng nhận mà không dời định tuyến lợi hại chính ở chỗ khác.

Giới hạn nhạy an toàn trên công bố, lối vào dữ liệu, công bố phương pháp, hoặc tài liệu tái lập chỉ được biện minh dưới [6.2 Ràng buộc công bố nhận thức](core_01_b_interaction_interpretation.md#62-epistemic-disclosure-constraints), các định nghĩa Chương Năm liệt kê trên, và quyền Chương Sáu áp dụng. Những giới hạn đó phải giữ tính toàn vẹn nhận thức tối đa khả thi qua hồ sơ được bảo vệ, rà soát độc lập, công bố trì hoãn, che, lối vào an toàn, hoặc bảo vệ tương đương; chúng không được trở thành phương tiện dập bằng chứng bất lợi, giấu khuyết an toàn, hoặc chế đồng thuận bề ngoài.

<a id="34-plain-language-accessibility-stewardship-duty"></a>
#### 3.4 Khả năng tiếp cận ngôn ngữ thường (Nghĩa vụ tham gia và quản trị có trách nhiệm)
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** (tham gia hiểu được); trụ **giám sát** (khả năng đọc kiểm toán và xác minh); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (quyền năng có ý nghĩa qua tham gia **Sự thật** hiểu được); mục tiêu **Liên tục** (tính đọc được thể chế bền theo thời gian).
- Thượng nguồn: Nguyên tắc: [§3.2 Sự thật](#32-truth-epistemic-integrity-constraint), [3.3 Tra cứu có thông tin khoa học và hỗ trợ quyết định](#33-science-informed-inquiry-and-decision-support), [§6.3 Giảm thiểu gánh nặng có thể tránh](core_01_b_interaction_interpretation.md#63-minimization-of-avoidable-burden), và [§11.1.3 Áp dụng quản trị có trách nhiệm và người vận hành](core_01_c_stewardship_capacity_principles.md#1113-stewardship-and-operator-application); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: Bề mặt quyền: [Điều V-G: Khả năng tiếp cận](../../core_06_rights_part_b.md#article-v-g-accessibility), [Điều VI: Quyền giáo dục lấy hữu tri làm trung tâm](../../core_06_rights_part_b.md#article-vi-right-to-sentient-centered-education), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XX: Quản trị có trách nhiệm đối với khả năng hiểu và độ phức tạp](../../core_06_rights_part_c.md#article-xx-comprehensibility-and-complexity-stewardship).
- Đối chiếu: Cơ chế định nghĩa Chương Hai đến Bốn và lan can ngôn ngữ thường ở [core_02_definition_structure.md](core_02_definition_structure.md) vẫn kiểm soát ở tầng định nghĩa.
- Các tiểu mục (thứ tự đọc): [§3.4.1](#341-scope) · [§3.4.2](#342-the-duty) · [§3.4.3](#343-definitional-rigor-preserved) · [§3.4.4](#344-jargon-as-defeat-discipline) · [§3.4.5](#345-chapter-ten-floor-boundary).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Gánh nặng có thể tránh](../../core_05_band_continuity.md#avoidable-burden) · [O](../../core_05_band_continuity.md#avoidable-burden) · [M](../../core_05_band_continuity.md#avoidable-burden-a) · [A](../../core_05_band_continuity.md#avoidable-burden-a) · [C](../../core_05_band_continuity.md#avoidable-burden-c)
- [Khả năng tiếp cận](../../core_05_band_participation.md#accessibility-constitutional) · [O](../../core_05_band_participation.md#accessibility-constitutional) · [M](../../core_05_band_participation.md#accessibility-constitutional-a) · [A](../../core_05_band_participation.md#accessibility-constitutional-a) · [C](../../core_05_band_participation.md#accessibility-constitutional-c)
- [Khả năng tranh biện](../../core_05_band_accountability.md#contestability) · [O](../../core_05_band_accountability.md#contestability) · [M](../../core_05_band_accountability.md#contestability-a) · [A](../../core_05_band_accountability.md#contestability-a) · [C](../../core_05_band_accountability.md#contestability-c)
- [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency) · [O](../../core_05_band_accountability.md#meaningful-agency-o) · [M](../../core_05_band_participation.md#meaningful-agency-a) · [A](../../core_05_band_participation.md#meaningful-agency-a) · [C](../../core_05_band_participation.md#meaningful-agency-c)
- [Minh bạch](../../core_05_band_oversight.md#transparency) · [O](../../core_05_band_oversight.md#transparency) · [M](../../core_05_band_oversight.md#transparency-a) · [A](../../core_05_band_oversight.md#transparency-a) · [C](../../core_05_band_oversight.md#transparency-c)
- [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint) · [O](../../core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [A](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](../../core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*Nói thẳng: quy tắc, quyết định, và thông báo ràng buộc các hữu tri phải được viết sao cho các hữu tri thực sự đọc, hiểu, và hành được trên chúng — và biệt ngữ, chồng phức tạp, hoặc mờ thủ tục không được dùng để đánh bại khả năng tranh biện, quyền năng, hoặc kiểm toán.*

Một **nghĩa vụ khả năng tiếp cận ngôn ngữ thường** áp dụng cho văn bản hiến pháp, quản trị, phân xử, và vận hành ràng buộc các hữu tri. Cùng nghĩa vụ áp dụng khi các hữu tri phải tiếp xúc văn bản đó để thực hiện quyền, tham gia quản trị, tranh biện quyết định, hoặc xác minh tuân thủ. Đây là yêu cầu [Tham gia](../../core_05_apex_participation_leg.md#participation-constitutional): các hữu tri không hiểu được các quy tắc ràng buộc chúng thì không thể tham gia có ý nghĩa vào các hệ thống những quy tắc đó quản trị.

<a id="341-scope"></a>
##### 3.4.1 Phạm vi

Nghĩa vụ này phủ văn kiện và thông tin liên lạc mà các hữu tri thực sự tiếp xúc. Ví dụ gồm:

- văn bản hiến pháp và quản trị;
- quyết định và thông báo phân xử;
- thủ tục khả năng tranh biện và khắc phục;
- hiện vật kiểm toán và xác minh nơi chúng tới người đọc hữu tri;
- điều khoản và giao diện đồng thuận, và văn bản tương đương.

Nghĩa vụ này áp dụng dù thông tin ràng buộc tới các hữu tri thế nào — văn bản viết, giao diện, giao tiếp nói, hoặc kênh khác. Một kênh thỏa nó khi cung cấp tương đương ngôn ngữ thường mà mọi hữu tri bị ảnh hưởng có thể tiếp cận, nhất quán với [Điều V-G](../../core_06_rights_part_b.md#article-v-g-accessibility) (*Khả năng tiếp cận*) và [Không loại trừ hữu tri](../../core_05_band_participation.md#sentience-non-exclusion).

<a id="342-the-duty"></a>
##### 3.4.2 Nghĩa vụ

Dưới [§6.3 Giảm thiểu gánh nặng có thể tránh](core_01_b_interaction_interpretation.md#63-minimization-of-avoidable-burden), người vận hành và cơ quan quản trị phải:

- dùng ngôn ngữ thường, trực tiếp thay biệt ngữ hoặc câu phức tạp không cần, mỗi nơi có thể mà không mất nghĩa vận hành;
- cung cấp tóm tắt hoặc định hướng ngôn ngữ thường khi các hữu tri phải tiếp xúc tài liệu kỹ thuật dày;
- tổ chức văn bản sao các hữu tri tìm được điều cần và đọc không khó không cần — nâng đỡ lợi ích học được thừa nhận dưới [Điều VI](../../core_06_rights_part_b.md#article-vi-right-to-sentient-centered-education) (*Quyền giáo dục lấy hữu tri làm trung tâm*);
- giữ độ phức tạp tương xứng với điều thông tin liên lạc thực sự cần nói. Phức tạp không cần làm việc khó hơn mà không phục vụ mục đích hiến pháp là khuyết [Gánh nặng có thể tránh](../../core_05_band_continuity.md#avoidable-burden) dưới [§6.3](core_01_b_interaction_interpretation.md#63-minimization-of-avoidable-burden) và mối quan tâm [Điều XX](../../core_06_rights_part_c.md#article-xx-comprehensibility-and-complexity-stewardship) (*Quản trị có trách nhiệm đối với khả năng hiểu và độ phức tạp*).

<a id="343-definitional-rigor-preserved"></a>
##### 3.4.3 Giữ nghiêm định nghĩa

Công việc ngôn ngữ thường **không** phải giấy phép làm mềm nghiêm định nghĩa. Những thứ này vẫn kiểm soát ở tầng định nghĩa:

- định nghĩa Chương Năm và các thành phần O/M/A/C của chúng;
- cơ chế định nghĩa Chương Hai đến Bốn.

Viết điều gì bằng ngôn ngữ đơn hơn không đổi nghĩa của nó. Nếu một tóm tắt ngôn ngữ thường và định nghĩa hình thức nó tóm tắt có vẻ nói khác nhau, định nghĩa hình thức kiểm soát — và tóm tắt phải được sửa cho khớp.

<a id="344-jargon-as-defeat-discipline"></a>
##### 3.4.4 Kỷ luật biệt ngữ-như-đánh-bại

Hệ thống không được dùng ngôn ngữ phức tạp, thủ tục mờ, hoặc cố ý tối để ngăn các hữu tri [tranh biện](../../core_05_band_accountability.md#contestability) quyết định, thực hiện [quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency), tiếp cận [kiểm toán](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), hoặc thực hiện quyền [Chương Sáu](../../core_06_rights_part_a.md#chapter-six-foundational-rights) của chúng.

Chiếu ngược cũng bị cấm: khung ngôn ngữ thường trình bày sai điều một quy tắc thực sự làm, giấu hiệu ứng thực, hoặc thay tóm tắt cho văn bản vận hành là vi phạm [Sự thật](../../core_05_band_oversight.md#truth-constitutional-constraint).

<a id="345-chapter-ten-floor-boundary"></a>
##### 3.4.5 Biên Sàn Quyền

Các Sàn Quyền cho khả năng tiếp cận, giáo dục, và khả năng hiểu sống ở [Điều V-G](../../core_06_rights_part_b.md#article-v-g-accessibility) (*Khả năng tiếp cận*), [Điều III-B](../../core_06_rights_part_a.md#article-iii-b-equal-educational-access) (*Lối vào giáo dục bình đẳng*), và [Điều XX](../../core_06_rights_part_c.md#article-xx-comprehensibility-and-complexity-stewardship) (*Quản trị có trách nhiệm đối với khả năng hiểu và độ phức tạp*) tương ứng. Mục này nêu nghĩa vụ tầng nguyên tắc nâng đỡ những sàn đó.

<a id="4-system-stability-enabler-trust-coordination-integrity"></a>
### 4. Bộ kích hoạt ổn định hệ thống: Tin cậy (Tính toàn vẹn phối hợp)
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** (sự dựa có biện minh cho phép quyền năng có ý nghĩa và khả năng tranh biện); trụ **giám sát** (phát hiện tranh biện được đối với rủi ro hệ thống và đáng tin cậy); trụ **trách nhiệm giải trình** (phải trả lời về sự dựa gây hiểu lầm); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (**đáng tin cậy** là thành phần được đặt tên dưới [Lời nói đầu §1](../../core_00_preamble.md#flourishing)); mục tiêu **Liên tục** (tính toàn vẹn phối hợp bền và ổn định hệ thống theo thời gian).
- Thượng nguồn: Nguyên tắc: [§3 Ràng buộc nguyên tắc không thương lượng: An toàn và Sự thật](#3-non-negotiable-constraints-safety-and-truth); [§2.2 Ghi nhận, củng cố, và khát vọng](#22-recognition-reinforcement-and-aspiration); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [6.2.1 Giữ tính toàn vẹn nhận thức](core_01_b_interaction_interpretation.md#621-preservation-of-epistemic-integrity), [6.2.2 Thẳng hàng tin cậy–sự thật](core_01_b_interaction_interpretation.md#622-trust-truth-alignment), và [7. Cấm phủ tuyệt đối](core_01_b_interaction_interpretation.md#7-prohibition-on-absolute-override).
- Các tiểu mục: [§4.1 Thiết kế khả năng phục hồi và tự chữa](#41-resilience-and-self-healing-design).
- Hạ nguồn: Định hình bề mặt quyền cho quyền năng, sự dựa đáng tin, minh bạch, quỹ đạo, và rà soát chống chiếm.
  - Đặc biệt [Điều IX: Tự quyết và quyền năng](../../core_06_rights_part_b.md#article-ix-self-determination-and-agency), [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems), [Điều XIV: Tính toàn vẹn không gian thông tin](../../core_06_rights_part_c.md#article-xiv-info-sphere-integrity), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XVIII: Quỹ đạo và trạng thái tham gia](../../core_06_rights_part_c.md#article-xviii-standing-and-participation-status), và [Điều XXII: Diễn giải hiến pháp, rà soát, và bảo vệ chống chiếm](../../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards).
  - Điều này cũng phủ mọi ngữ cảnh Chương Sáu nơi sự dựa, tính chính danh, hoặc khả năng tranh biện đang đặt lên bàn.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tin cậy](../../core_05_band_continuity.md#trust) · [O](../../core_05_band_continuity.md#trust) · [M](../../core_05_band_continuity.md#trust-a) · [A](../../core_05_band_continuity.md#trust-a) · [C](../../core_05_band_continuity.md#trust-c)
- [Đáng tin cậy](../../core_05_band_continuity.md#trustworthiness) · [O](../../core_05_band_continuity.md#trustworthiness) · [M](../../core_05_band_continuity.md#trustworthiness-a) · [A](../../core_05_band_continuity.md#trustworthiness-a) · [C](../../core_05_band_continuity.md#trustworthiness-c)
- [Sự thật (Ràng buộc hiến pháp)](../../core_05_band_oversight.md#truth-constitutional-constraint) · [O](../../core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [A](../../core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](../../core_05_band_oversight.md#truth-constitutional-constraint-c)
- [An toàn (Ràng buộc)](../../core_05_band_continuity.md#safety-constraint) · [O](../../core_05_band_continuity.md#safety-constraint) · [M](../../core_05_band_continuity.md#safety-constraint-a) · [A](../../core_05_band_continuity.md#safety-constraint-a) · [C](../../core_05_band_continuity.md#safety-constraint-c)
- [Tính trọng yếu](../../core_05_band_oversight.md#materiality-determination) · [O](../../core_05_band_oversight.md#materiality-determination) · [M](../../core_05_band_oversight.md#materiality-determination-a) · [A](../../core_05_band_oversight.md#materiality-determination-a) · [C](../../core_05_band_oversight.md#materiality-determination-c)
- [Suy giảm tin cậy và sự dựa gây hiểu lầm](../../core_05_band_integrative.md#trust-degradation-and-misleading-reliance-constitutional) · [O](../../core_05_band_integrative.md#trust-degradation-and-misleading-reliance-constitutional) · [M](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [A](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [C](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-c)

</details>

<br>

*Nói thẳng: hệ thống chung đòi các hữu tri phụ thuộc vào chúng — vì an toàn, thông tin, lối vào, và phối hợp. Tin cậy dưới Hiến pháp này nghĩa là sự phụ thuộc đó phải được kiếm bằng cách hệ thống thực sự hành xử, không chế qua quay, bí mật, hoặc chuyển rủi ro ẩn.*

Các hữu tri cần hệ thống chúng thực sự có thể dựa. [**Tin cậy**](../../core_05_band_continuity.md#trust) là nguyên tắc hiến pháp làm sự dựa chính danh: hệ thống phải kiếm nó qua hành vi trung thực và độ tin đã chứng minh theo thời gian, không gợi nó qua lừa dối hoặc che giấu. [**Đáng tin cậy**](../../core_05_band_continuity.md#trustworthiness) là hồ sơ theo dõi kiếm nó. Tin cậy là phần được đặt tên của [**Hưng thịnh**](#flourishing) và thiết yếu đối với [**Liên tục**](#continuity) — phối hợp bền đòi hệ thống các hữu tri có thể tính được.

Tin cậy nối các ràng buộc nguyên tắc với đời chung ngày thường:
- [**Sự thật**](../../core_05_band_oversight.md#truth-constitutional-constraint) cấm lừa dối.
- [**An toàn**](../../core_05_band_continuity.md#safety-constraint) giới hạn sự dựa có thể đi bao xa khi rủi ro thực hiện diện.
- [**Tính trọng yếu**](../../core_05_band_oversight.md#materiality-determination) quyết định bao nhiêu phải được cho thấy và giải thích — lợi hại càng cao đối với các hữu tri phụ thuộc một hệ thống, hệ thống đó càng phải công bố và biện minh.
- [**Suy giảm tin cậy và sự dựa gây hiểu lầm**](../../core_05_band_integrative.md#trust-degradation-and-misleading-reliance-constitutional) gọi tên chế độ thất bại — khi hệ thống tạo, giữ, hoặc chấm sự dựa theo cách gây hiểu lầm hiến pháp.

Tin cậy thất bại khi sự dựa được xây hoặc giữ qua dập, lừa dối, chuyển rủi ro ẩn, hoặc mánh tương tự — kể cả bất cứ điều gì làm suy nghiêm khả năng của các hữu tri để phát hiện và tranh biện rủi ro hệ thống. Quy trình [**Chứng nhận thẳng hàng hệ thống**](../../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation) dưới [Chương Bảy](../../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-system-alignment-certification) là nơi hệ thống chứng minh tuyên bố tin cậy của chúng đứng vững: chứng nhận phải xác minh hành vi thực của hệ thống khớp các trình bày của nó, trên hồ sơ tranh biện được — không chỉ trên khẳng định của người vận hành.

<a id="41-resilience-and-self-healing-design"></a>
#### 4.1 Thiết kế khả năng phục hồi và tự chữa
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **giám sát** và **trách nhiệm giải trình**; chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake) cho độ sâu phục hồi và kiểm toán.
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Liên tục** (kỷ luật khả năng phục hồi và tự chữa); mục tiêu **Hưng thịnh** (phục hồi đáng tin cậy mà không suy giảm nhận thức).
- Thượng nguồn: Nguyên tắc: [Lời nói đầu §1 Mô hình](../../core_00_preamble.md#the-model); [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims); [3.1 An toàn](#31-safety-harm-constraint), [3.2 Sự thật](#32-truth-epistemic-integrity-constraint), và [§4 Tin cậy](#4-system-stability-enabler-trust-coordination-integrity).
- Hạ nguồn: [§9 Quản trị có trách nhiệm và hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#9-stewardship-and-distributed-understanding), [§6.3 Giảm thiểu gánh nặng có thể tránh](core_01_b_interaction_interpretation.md#63-minimization-of-avoidable-burden), [Chương Bảy §3 Đánh giá chứng nhận toàn hệ thống](../../core_07_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), [§10 Quản trị dưới kỷ luật quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#10-governance-under-stewardship-discipline), và [7. Cấm phủ tuyệt đối](core_01_b_interaction_interpretation.md#7-prohibition-on-absolute-override).
- Hạ nguồn: Định hình bề mặt quyền cho độ tin-kèm-phục-hồi, trung thực nguyên nhân gốc, khả năng đảo ngược, và khả năng hiểu các trạng thái suy và đang khôi.
  - Đặc biệt [Điều XII: Quyền đối với hệ thống đáng tin và đáng tin cậy](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems) (kể cả **Điều XII-F** (*Sàn khả năng phục hồi và tự chữa*)), [Điều XV: Kiểm toán, minh bạch, và xác minh độc lập](../../core_06_rights_part_c.md#article-xv-audit-transparency-and-independent-verification), [Điều XVI: Vòng đời hệ thống, môi trường, và khả năng đảo ngược](../../core_06_rights_part_c.md#article-xvi-system-lifecycle-environments-and-reversibility), [Điều XX: Quản trị có trách nhiệm đối với khả năng hiểu và độ phức tạp](../../core_06_rights_part_c.md#article-xx-comprehensibility-and-complexity-stewardship), và [Điều XXI: Phân tích nguyên nhân gốc và đáp ứng thích nghi](../../core_06_rights_part_c.md#article-xxi-root-cause-analysis-and-adaptive-response).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tự chữa](../../core_05_band_continuity.md#self-healing-constitutional) · [O](../../core_05_band_continuity.md#self-healing-constitutional) · [M](../../core_05_band_continuity.md#self-healing-constitutional-a) · [A](../../core_05_band_continuity.md#self-healing-constitutional-a) · [C](../../core_05_band_continuity.md#self-healing-constitutional-c)
- [Sự cố lan](../../core_05_band_continuity.md#cascading-failure) · [O](../../core_05_band_continuity.md#cascading-failure) · [M](../../core_05_band_continuity.md#cascading-failure-a) · [A](../../core_05_band_continuity.md#cascading-failure-a) · [C](../../core_05_band_continuity.md#cascading-failure-c)
- [Khả năng đảo ngược](../../core_05_band_continuity.md#reversibility-constitutional) · [O](../../core_05_band_continuity.md#reversibility-constitutional) · [M](../../core_05_band_continuity.md#reversibility-constitutional-a) · [A](../../core_05_band_continuity.md#reversibility-constitutional-a) · [C](../../core_05_band_continuity.md#reversibility-constitutional-c)
- [Gánh nặng có thể tránh](../../core_05_band_continuity.md#avoidable-burden) · [O](../../core_05_band_continuity.md#avoidable-burden) · [M](../../core_05_band_continuity.md#avoidable-burden-a) · [A](../../core_05_band_continuity.md#avoidable-burden-a) · [C](../../core_05_band_continuity.md#avoidable-burden-c)
- [Thẳng hàng khuyến khích](../../core_05_band_integrative.md#incentive-alignment) · [O](../../core_05_band_integrative.md#incentive-alignment) · [M](../../core_05_band_integrative.md#incentive-alignment) · [A](../../core_05_band_integrative.md#incentive-alignment) · [C](../../core_05_band_integrative.md#incentive-alignment)

</details>

<br>

*Nói thẳng: hệ thống nên phát hiện rắc rối sớm, chứa nó, hỏng theo đường đã công bố, và phục hồi trung thực. «Tự chữa» giấu sự cố, bỏ việc nguyên nhân gốc, hoặc lặng lẽ thu hẹp quyền thì không phải khả năng phục hồi — đó là khuyết.*

Hệ thống các hữu tri phụ thuộc nên được xây để:
- phát hiện vấn đề sớm;
- chứa chúng trước khi lan;
- hỏng theo đường đã hoạch và công bố, không phải đường ẩn;
- phục hồi theo cách nhất quán với [Khả năng đảo ngược](../../core_05_band_continuity.md#reversibility-constitutional) và Sàn Quyền Chương Sáu.

Đây là điều Chương Năm gọi là [**Tự chữa**](../../core_05_band_continuity.md#self-healing-constitutional) — và nó chỉ chính danh khi làm hệ thống trung thực hơn về tình trạng của chính nó, không kém. Phục hồi tự động che nguyên nhân gốc, dập bằng chứng, hoặc thay quản trị thì không phải tự chữa. Đó là vi phạm [Sự thật](../../core_05_band_oversight.md#truth-constitutional-constraint) và khuyết [Thẳng hàng khuyến khích](../../core_05_band_integrative.md#incentive-alignment).

Các hữu tri càng phụ thuộc một hệ thống và tác động của nó càng lớn, hệ thống đó càng ít nên dựa vào can thiệp khẩn cấp. Nó nên đầu tư vào tự phục hồi đã thử, đã kiểm toán, có giới hạn — giảm [Gánh nặng có thể tránh](../../core_05_band_continuity.md#avoidable-burden) và nâng đỡ [**Liên tục**](#continuity) tầm dài.

Chi tiết vận hành — phát hiện phục hồi, chứa, ưa hỏng an toàn, đóng nguyên nhân gốc, và liên tục Sàn Quyền — sống ở [Điều XII-F](../../core_06_rights_part_c.md#article-xii-right-to-reliable-and-trustworthy-systems) (*Sàn khả năng phục hồi và tự chữa*) trong Chương Sáu, với yêu cầu kiến trúc phục hồi trong văn bản triển khai đã hợp nhất.

### 5. Tự do (Quyền năng bị giới hạn)
<a id="5-freedom-bounded-agency"></a>
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Đọc cùng: [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — trụ **tham gia** (quyền năng có ý nghĩa và vai trò có hệ quả); trụ **trách nhiệm giải trình** (quyền năng không có phải trả lời thì chưa đủ); chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).
- Đọc cùng: [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims) — mục tiêu **Hưng thịnh** (chương này phát triển **quyền năng có ý nghĩa**); mục tiêu **Liên tục** (quyền năng bị giới hạn giữ hệ thống hiến pháp bền, tranh biện được).
- Đọc cùng: [Ngừng tự nguyện](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional), Chương Năm §2 *Quyền năng, đồng thuận, và chống cưỡng*, và [Tụ họp, tổ chức tập thể, và hình thành thể chế](../../core_05_band_participation.md#assembly-collective-organization-institutional-formation-cluster).
- Đọc cùng: [§9.1 Quản trị có trách nhiệm](core_01_c_stewardship_capacity_principles.md#91-stewardship) và [§11.1.4 Đường dẫn độ sâu vai trò và trách nhiệm vật chất](core_01_c_stewardship_capacity_principles.md#1114-role-depth-and-material-responsibility-pathways) — đường dẫn độ sâu vai trò, năng lực, và trách nhiệm vật chất; quyền năng có ý nghĩa gồm đường thực vào vai trò học, vận hành, và nghĩa vụ có hệ quả nơi an toàn và đồng thuận cho phép; tham gia tượng trưng không được thay nghĩa vụ có hệ quả nơi tác động đòi cái sau.
- Đọc cùng: [§13 Cấu trúc thị trường](core_01_c_stewardship_capacity_principles.md#13-market-structure), đặc biệt [§13.2 Ủng hộ cạnh tranh và chống thống trị](core_01_c_stewardship_capacity_principles.md#132-pro-competition-and-anti-domination), và [Điều XIX: Khả năng tương tác, khả năng mang, di chuyển, tị nạn, và tính toàn vẹn lối ra](../../core_06_rights_part_c.md#article-xix-interoperability-portability-and-exit-integrity) nơi tập trung, thống trị, hoặc khóa-trong hạn chế vật chất quyền năng — thị trường tranh biện được, đường lối ra, và kỷ luật chống thống trị giữ quyền năng thành thực ở quy mô.
- Đọc cùng: [§5.1 Kỷ luật hạn chế](#51-limitation-discipline) và [Chương Bảy §3.6 Ràng buộc nhất quán thời gian](../../core_07_a_system_alignment_certification_evaluation.md#36-time-consistency-constraint) — kỷ luật đánh giá hạn chế tự do vận hành và nhất quán thời gian; khi giới hạn tự do va với giá trị hoặc quyền khác, giải dưới [§6.1](core_01_b_interaction_interpretation.md#61-core-tradeoff-principles) đến [§6.1.5 Thủ tục va chạm quyền](core_01_b_interaction_interpretation.md#615-rights-collision-decision-test) sau khi **An toàn** và **Sự thật** đã thỏa.
- Thượng nguồn: Nguyên tắc: [§2.2 Ghi nhận, củng cố, và khát vọng](#22-recognition-reinforcement-and-aspiration); [3.1 An toàn](#31-safety-harm-constraint); [3.2 Sự thật](#32-truth-epistemic-integrity-constraint); [4. Tin cậy](#4-system-stability-enabler-trust-coordination-integrity); và [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims).
- Hạ nguồn: [§5.1 Kỷ luật hạn chế](#51-limitation-discipline) đến [§5.3 Tụ họp, tổ chức tập thể, và hình thành thể chế](#53-assembly-collective-organization-and-institutional-formation); [6. Giải quyết xung đột quy trình](core_01_b_interaction_interpretation.md#6-process-conflict-resolution); [7. Cấm phủ tuyệt đối](core_01_b_interaction_interpretation.md#7-prohibition-on-absolute-override); [§15 Áp dụng tích hợp](core_01_c_stewardship_capacity_principles.md#15-integrated-application); và [kỷ luật hồ sơ quyết định §6.1](core_01_b_interaction_interpretation.md#615-rights-collision-decision-test) nơi áp dụng cụ thể đòi xử lý va chạm.
- Hạ nguồn: Khung bề mặt quyền cho địa vị bình đẳng, giáo dục, tự sở hữu, kiểm soát công bố và hình dạng, quyền năng, tương tác hợp tác, thủ tục đúng đắn, quỹ đạo, và rà soát chống chiếm.
  - Đặc biệt [Điều V: Quyền cơ bản bình đẳng](../../core_06_rights_part_b.md#article-v-equal-basic-rights), [Điều VI: Quyền giáo dục lấy hữu tri làm trung tâm](../../core_06_rights_part_b.md#article-vi-right-to-sentient-centered-education), [Điều VII: Tự sở hữu](../../core_06_rights_part_b.md#article-vii-self-ownership), [Điều VIII: Quyền hình dạng, dữ liệu trải nghiệm, và công bố](../../core_06_rights_part_b.md#article-viii-likeness-experiential-data-and-publication-rights), [Điều IX: Tự quyết và quyền năng](../../core_06_rights_part_b.md#article-ix-self-determination-and-agency), [Điều X: Tương tác hợp tác](../../core_06_rights_part_b.md#article-x-cooperative-interaction), [Điều XI: Tham gia hệ thống của bên bị ảnh hưởng, đại diện, và thủ tục đúng đắn](../../core_06_rights_part_b.md#article-xi-stakeholder-system-participation-representation-and-due-process), [Điều XVIII: Quỹ đạo và trạng thái tham gia](../../core_06_rights_part_c.md#article-xviii-standing-and-participation-status), và [Điều XXII: Diễn giải hiến pháp, rà soát, và bảo vệ chống chiếm](../../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards).
  - Điều này cũng phủ mọi ngữ cảnh quyền Chương Sáu nơi quyền năng bị hạn chế hoặc được tuyên.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tự do (Quyền năng bị giới hạn)](../../core_05_band_participation.md#freedom-bounded-agency) · [O](../../core_05_band_participation.md#freedom-bounded-agency) · [M](../../core_05_band_participation.md#freedom-bounded-agency-a) · [A](../../core_05_band_participation.md#freedom-bounded-agency-a) · [C](../../core_05_band_participation.md#freedom-bounded-agency-c)
- [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency) · [O](../../core_05_band_accountability.md#meaningful-agency-o) · [M](../../core_05_band_participation.md#meaningful-agency-a) · [A](../../core_05_band_participation.md#meaningful-agency-a) · [C](../../core_05_band_participation.md#meaningful-agency-c)
- [Tự chủ sinh sản](../../core_05_band_participation.md#reproductive-autonomy-constitutional) · [O](../../core_05_band_participation.md#reproductive-autonomy-constitutional) · [M](../../core_05_band_participation.md#reproductive-autonomy-constitutional-a) · [A](../../core_05_band_participation.md#reproductive-autonomy-constitutional-a) · [C](../../core_05_band_participation.md#reproductive-autonomy-constitutional-c)
- [Đồng thuận](../../core_05_band_participation.md#consent-constitutional) · [O](../../core_05_band_participation.md#consent-constitutional) · [M](../../core_05_band_participation.md#consent-constitutional-a) · [A](../../core_05_band_participation.md#consent-constitutional-a) · [C](../../core_05_band_participation.md#consent-constitutional-c)
- [Cưỡng và thao túng](../../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [O](../../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [M](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [A](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [C](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [Tụ họp](../../core_05_band_participation.md#assembly-constitutional) · [O](../../core_05_band_participation.md#assembly-constitutional) · [M](../../core_05_band_participation.md#assembly-constitutional-a) · [A](../../core_05_band_participation.md#assembly-constitutional-a) · [C](../../core_05_band_participation.md#assembly-constitutional-c)
- [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional) · [O](../../core_05_band_participation.md#collective-organization-constitutional) · [M](../../core_05_band_participation.md#collective-organization-constitutional-a) · [A](../../core_05_band_participation.md#collective-organization-constitutional-a) · [C](../../core_05_band_participation.md#collective-organization-constitutional-c)
- [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional) · [O](../../core_05_band_participation.md#system-creation-constitutional) · [M](../../core_05_band_participation.md#system-creation-constitutional-a) · [A](../../core_05_band_participation.md#system-creation-constitutional-a) · [C](../../core_05_band_participation.md#system-creation-constitutional-c)
- [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional) · [O](../../core_05_band_participation.md#business-creation-constitutional) · [M](../../core_05_band_participation.md#business-creation-constitutional-a) · [A](../../core_05_band_participation.md#business-creation-constitutional-a) · [C](../../core_05_band_participation.md#business-creation-constitutional-c)
- [Tính khả thi](../../core_05_band_accountability.md#feasibility) · [O](../../core_05_band_accountability.md#feasibility) · [M](../../core_05_band_accountability.md#feasibility-a) · [A](../../core_05_band_accountability.md#feasibility-a) · [C](../../core_05_band_accountability.md#feasibility-c)
- [Sự cần thiết](../../core_05_band_accountability.md#necessity) · [O](../../core_05_band_accountability.md#necessity) · [M](../../core_05_band_accountability.md#necessity-a) · [A](../../core_05_band_accountability.md#necessity-a) · [C](../../core_05_band_accountability.md#necessity-c)
- [Tính tương xứng](../../core_05_band_accountability.md#proportionality) · [O](../../core_05_band_accountability.md#proportionality) · [M](../../core_05_band_accountability.md#proportionality-a) · [A](../../core_05_band_accountability.md#proportionality-a) · [C](../../core_05_band_accountability.md#proportionality-c)
- [Giảm thiểu hại (Chọn đánh đổi)](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection) · [O](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection) · [M](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-a) · [A](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-a) · [C](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-c)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency) · [O](../../core_05_band_continuity.md#dependency) · [M](../../core_05_band_continuity.md#dependency-a) · [A](../../core_05_band_continuity.md#dependency-a) · [C](../../core_05_band_continuity.md#dependency-c)

</details>

<br>

*Nói thẳng: tự do là quyền năng có ý nghĩa trong giới hạn hiến pháp — tiến **Hưng thịnh** qua lựa chọn thực và **Liên tục** qua hệ thống vẫn tranh biện được — không phải giấy phép làm bất cứ gì. «Chúng tôi không còn lựa chọn» không phải vé thông hành. Bên đưa tuyên bố đó phải chứng minh không có lựa chọn hạn chế nhẹ hơn sẽ thực sự hiệu quả; tiện, chi phí, hoặc thói quen không phải chứng minh. Người ta vẫn có tiếng nói thực, và vẫn phải có người trả lời — càng hơn khi tác động, phụ thuộc, và rủi ro tăng.*

**Tự do (Quyền năng bị giới hạn)** là biểu đạt Chương Một chính của thành phần **quyền năng có ý nghĩa** của mục tiêu [**Hưng thịnh**](../../core_00_preamble.md#flourishing) dưới [Hai Mục tiêu Hiến pháp](../../core_00_preamble.md#two-constitutional-aims). Nó là quyền năng bị giới hạn, không phải tùy ý tuyệt đối hay tự chủ không biên; nó phải được thực hiện nhất quán với An toàn, Sự thật, và quyền của người khác, và phải vẫn có ý nghĩa nơi tác động hoặc phụ thuộc có trọng. Nó phải vẫn nhất quán với [**Liên tục**](../../core_00_preamble.md#continuity) nơi hệ thống hiến pháp bền phụ thuộc vào quyền năng bị giới hạn, tranh biện được. Áp dụng phải thỏa [Tứ diện Hiến pháp](../../core_00_preamble.md#constitutional-tetrad) — đặc biệt trụ **tham gia** (quyền năng có ý nghĩa và vai trò có hệ quả) và trụ **trách nhiệm giải trình** (quyền năng không có phải trả lời thì chưa đủ) — chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).

Tuyên bố rằng hạn chế tự do là không tránh được — kể cả «chúng tôi không còn lựa chọn» — không được lập bằng khẳng định. Bên đưa tuyên bố đó phải chứng minh, dưới yêu cầu gánh và truy vết [Chương Bốn](../../core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) và các định nghĩa Chương Năm về [Tính khả thi](../../core_05_band_accountability.md#feasibility) và [Sự cần thiết](../../core_05_band_accountability.md#necessity), rằng không có lựa chọn hạn chế nhẹ hơn, hiệu quả hợp lý nào tồn tại trong hệ thống đang làm việc. Tiện, chi phí một mình, rào cản do người vận hành tạo, hoặc thói quen thể chế không chứng minh điều đó. Tuyên bố không miễn nghĩa vụ Tứ diện chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake):
- **tham gia** — các hữu tri bị ảnh hưởng vẫn cần quyền năng có ý nghĩa và vai trò tranh biện được
- **trách nhiệm giải trình** — vẫn có người phải trả lời về hạn chế

Thử vận hành sống ở [§5.1 Kỷ luật hạn chế](#51-limitation-discipline) và [§6.1.1 Sự cần thiết](core_01_b_interaction_interpretation.md#611-necessity).

[Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency) là năng lực làm lựa chọn thực thành có thể. [Đồng thuận](../../core_05_band_participation.md#consent-constitutional) là thỏa thuận hợp lệ đối với một quyết định cụ thể dưới năng lực đó — không phải vật thay cho nó, và không được chứng bởi một mẫu đơn một mình. [Cưỡng và thao túng](../../core_05_band_participation.md#coercion-and-manipulation-constitutional) đánh bại cả hai. Chi tiết vận hành cho quan hệ đó sống ở Chương Năm §2 *Quyền năng, đồng thuận, và chống cưỡng*.

Tự do không gồm thẩm quyền lật hệ thống hiến pháp, đánh bại quy trình hoặc biện pháp khắc phục hiến pháp, hoặc tuyên quyền năng được bảo vệ cho hành vi mà mục đích hoặc hiệu ứng vật chất là thưởng, bảo vệ, bình thường hóa, hoặc làm hành vi phản hiến pháp có lợi.

#### 5.1 Kỷ luật hạn chế

<a id="51-limitation-discipline"></a>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

*Phạm vi.* [§5.1 Kỷ luật hạn chế](#51-limitation-discipline) — định nghĩa khi tự do có thể bị hạn chế.

- [Tự do (Quyền năng bị giới hạn)](../../core_05_band_participation.md#freedom-bounded-agency) · [O](../../core_05_band_participation.md#freedom-bounded-agency) · [M](../../core_05_band_participation.md#freedom-bounded-agency-a) · [A](../../core_05_band_participation.md#freedom-bounded-agency-a) · [C](../../core_05_band_participation.md#freedom-bounded-agency-c)
- [Tính khả thi](../../core_05_band_accountability.md#feasibility) · [O](../../core_05_band_accountability.md#feasibility) · [M](../../core_05_band_accountability.md#feasibility-a) · [A](../../core_05_band_accountability.md#feasibility-a) · [C](../../core_05_band_accountability.md#feasibility-c)
- [Sự cần thiết](../../core_05_band_accountability.md#necessity) · [O](../../core_05_band_accountability.md#necessity) · [M](../../core_05_band_accountability.md#necessity-a) · [A](../../core_05_band_accountability.md#necessity-a) · [C](../../core_05_band_accountability.md#necessity-c)
- [Tính tương xứng](../../core_05_band_accountability.md#proportionality) · [O](../../core_05_band_accountability.md#proportionality) · [M](../../core_05_band_accountability.md#proportionality-a) · [A](../../core_05_band_accountability.md#proportionality-a) · [C](../../core_05_band_accountability.md#proportionality-c)
- [Giảm thiểu hại (Chọn đánh đổi)](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection) · [O](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection) · [M](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-a) · [A](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-a) · [C](../../core_05_band_accountability.md#harm-minimization-tradeoff-selection-c)
- [Hại](../../core_05_band_accountability.md#harm) · [O](../../core_05_band_accountability.md#harm) · [M](../../core_05_band_accountability.md#harm-a) · [A](../../core_05_band_accountability.md#harm-a) · [C](../../core_05_band_accountability.md#harm-c)
- [Rủi ro](../../core_05_band_continuity.md#risk) · [O](../../core_05_band_continuity.md#risk) · [M](../../core_05_band_continuity.md#risk-a) · [A](../../core_05_band_continuity.md#risk-a) · [C](../../core_05_band_continuity.md#risk-c)
- [Khả năng đảo ngược](../../core_05_band_continuity.md#reversibility-constitutional) · [O](../../core_05_band_continuity.md#reversibility-constitutional) · [M](../../core_05_band_continuity.md#reversibility-constitutional-a) · [A](../../core_05_band_continuity.md#reversibility-constitutional-a) · [C](../../core_05_band_continuity.md#reversibility-constitutional-c)
- [Giám sát](core_05_apex_oversight_leg.md#oversight-constitutional) · [O](core_05_apex_oversight_leg.md#oversight-constitutional) · [M](core_05_apex_oversight_leg.md#oversight-constitutional-m) · [A](core_05_apex_oversight_leg.md#oversight-constitutional-a) · [C](core_05_apex_oversight_leg.md#oversight-constitutional-c)

</details>

<br>

*Nói thẳng: tự do bị giới hạn, không phải vứt được. Đừng hạn chế tự do của ai trừ khi phải — và rồi chỉ đủ để dừng hại vật chất hoặc rủi ro hệ thống nghiêm, với giám sát và đảo ngược nơi có thể.*

Tự do chỉ được hạn chế nơi:
- cần để ngăn **hại vật chất** hoặc **rủi ro hệ thống**
- hạn chế đó **tương xứng**, **đảo ngược được nơi có thể**, và **chịu giám sát**

Ràng buộc chỉ được đặt khi không có lựa chọn hạn chế nhẹ hơn, hiệu quả hợp lý nào tồn tại, nhất quán với [Sự cần thiết](../../core_05_band_accountability.md#necessity) ở **Chương Năm**. Tuyên bố tính khả thi hạn chế quyền năng phải chứng minh được dưới yêu cầu gánh và truy vết **Chương Bốn**. Chúng cũng phải nhất quán với định nghĩa **Chương Năm** (kể cả Tính khả thi, Sự cần thiết, Tính tương xứng, và Giảm thiểu hại (Chọn đánh đổi)). Hạn chế phải vẫn chịu [Giám sát](core_05_apex_oversight_leg.md#oversight-constitutional) chia tỷ lệ theo [lợi hại vật chất](../../core_00_preamble.md#material-stake).

Khi giới hạn tự do va với giá trị hoặc quyền hiến pháp khác, áp dụng [§6.1 Nguyên tắc đánh đổi cốt](core_01_b_interaction_interpretation.md#61-core-tradeoff-principles) đến [§6.1.5 Thủ tục va chạm quyền](core_01_b_interaction_interpretation.md#615-rights-collision-decision-test) sau khi **An toàn** và **Sự thật** đã thỏa.

#### 5.2 Quyền ngừng tự nguyện và lối ra

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

*Nơi định nghĩa.* [Ngừng tự nguyện](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional) Chương Năm là Định nghĩa Độc lập ở §1. Đọc cùng Chương Năm §2 _Quyền năng, đồng thuận, và chống cưỡng_.

- [Ngừng tự nguyện](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional) · [O](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional) · [M](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional-a) · [A](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional-a) · [C](../../core_05_band_continuity.md#voluntary-discontinuation-constitutional-c)
- [Đồng thuận](../../core_05_band_participation.md#consent-constitutional) · [O](../../core_05_band_participation.md#consent-constitutional) · [M](../../core_05_band_participation.md#consent-constitutional-a) · [A](../../core_05_band_participation.md#consent-constitutional-a) · [C](../../core_05_band_participation.md#consent-constitutional-c)
- [Cưỡng và thao túng](../../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [O](../../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [M](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [A](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [C](../../core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [Phụ thuộc](../../core_05_band_continuity.md#dependency) · [O](../../core_05_band_continuity.md#dependency) · [M](../../core_05_band_continuity.md#dependency-a) · [A](../../core_05_band_continuity.md#dependency-a) · [C](../../core_05_band_continuity.md#dependency-c)

</details>

<br>

<a id="52-voluntary-discontinuation-and-exit-rights"></a>

*Nói thẳng: lựa chọn đổi đời hoặc khó đảo không «tự nguyện» chỉ vì ai đó ký một mẫu. Quyền năng thực đến trước; đồng thuận là thỏa thuận dưới quyền năng đó — và cả hai thất bại nếu cưỡng hoặc áp lực phụ thuộc đang làm quyết định thực.*

Một việc hướng đời lợi hại cao không được coi tự nguyện qua sự đồng ý hình thức nơi điều kiện quyền năng nội dung, đồng thuận, hoặc chống cưỡng thất bại. Đồng thuận ở đây giả định [Quyền năng có ý nghĩa](../../core_05_band_participation.md#meaningful-agency); nó không thay nó.

**Phạm vi nhận.** Tiểu mục này áp dụng cho:
- ngừng tự nguyện
- thay đổi tự hướng không đảo ngược hoặc trên thực tế không đảo ngược
- quyết định giàu phụ thuộc tác động vật chất tới sự tồn tại tiếp hoặc quyền năng thiết yếu
- quyết định tương đương nơi tính tự nguyện phụ thuộc vào việc thử cùng đồng thuận, tự quyết, cưỡng/thao túng, thông tin, áp lực phụ thuộc, và khả năng đảo ngược

**Không nhập đồng thuận thường.** Ngoài phạm vi nhận đó, các định nghĩa Chương Năm này vẫn dùng lại được:
- *Đồng thuận* (§2)
- *Tự quyết*
- *Cưỡng và thao túng* (§2)

Tiểu mục này **không** nhập kỷ luật ngừng tự nguyện vào các ngữ cảnh này:
- đồng thuận thường
- quyền riêng tư
- liên kết
- công bố
- dữ liệu huấn luyện
- đồng thuận tình dục
- dịch vụ thương mại

Đánh giá toàn hệ thống phải thử các điều kiện này dưới [Chương Bảy §3.4 Quyền ngừng tự nguyện và lối ra](../../core_07_a_system_alignment_certification_evaluation.md#34-voluntary-discontinuation-and-exit-rights) trước khi phân loại, quản trị, hạn chế, hoặc tuyên bố tuân thủ đứng nơi phạm vi nhận áp dụng.

#### 5.3 Tụ họp, tổ chức tập thể, và hình thành thể chế

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

*Nơi định nghĩa.* [§3.5 Tụ họp, tổ chức tập thể, và hình thành thể chế](../../core_05_band_participation.md#assembly-collective-organization-institutional-formation-cluster) Chương Năm là nhà cho nhóm định nghĩa này. Đọc cùng **Điều V-H** (*Biểu đạt, tụ họp, và báo chí*) (tụ họp), **Điều III-D** (*Sàn lao động và kinh tế*) (tổ chức tập thể trong sàn lao động và kinh tế), và [§9.5 Tự tổ chức thẳng hàng](core_01_c_stewardship_capacity_principles.md#95-aligned-self-organization) (đường thủ tục cho quản trị có trách nhiệm hiến pháp do hữu tri khởi và cộng đồng khởi).

- [Tụ họp](../../core_05_band_participation.md#assembly-constitutional) · [O](../../core_05_band_participation.md#assembly-constitutional) · [M](../../core_05_band_participation.md#assembly-constitutional-a) · [A](../../core_05_band_participation.md#assembly-constitutional-a) · [C](../../core_05_band_participation.md#assembly-constitutional-c)
- [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional) · [O](../../core_05_band_participation.md#collective-organization-constitutional) · [M](../../core_05_band_participation.md#collective-organization-constitutional-a) · [A](../../core_05_band_participation.md#collective-organization-constitutional-a) · [C](../../core_05_band_participation.md#collective-organization-constitutional-c)
- [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional) · [O](../../core_05_band_participation.md#system-creation-constitutional) · [M](../../core_05_band_participation.md#system-creation-constitutional-a) · [A](../../core_05_band_participation.md#system-creation-constitutional-a) · [C](../../core_05_band_participation.md#system-creation-constitutional-c)
- [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional) · [O](../../core_05_band_participation.md#business-creation-constitutional) · [M](../../core_05_band_participation.md#business-creation-constitutional-a) · [A](../../core_05_band_participation.md#business-creation-constitutional-a) · [C](../../core_05_band_participation.md#business-creation-constitutional-c)

</details>

<br>

<a id="53-assembly-collective-organization-and-institutional-formation"></a>

*Nói thẳng: bạn không thể chặt tụ họp, tổ chức kiểu công đoàn, lối vào nền tảng, hoặc câu hỏi phép-vận-hành thành các hộp riêng theo cách giữ giấy tờ thân thiện nhưng đánh bại hành động tập thể thực. Mục này không thay Sàn Quyền: Điều V-H vẫn nắm tụ họp, và Điều III-D vẫn nắm tổ chức lao động.*

**Nơi quy tắc đầy đủ sống.** Chương Năm nhóm các định nghĩa liên quan phải được đọc cùng khi các câu hỏi chúng phủ đi cùng nhau. Nhóm đó là một **cụm định nghĩa**. Nó không phải quyền riêng, và không phải vật thay cho các điều Chương Sáu dưới đây. Định nghĩa cho chủ đề này sống ở [Chương Năm — Tụ họp, tổ chức tập thể, và hình thành thể chế](../../core_05_band_participation.md#assembly-collective-organization-institutional-formation-cluster):
- [Tụ họp](../../core_05_band_participation.md#assembly-constitutional)
- [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional)
- [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional)
- [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional)

Quy tắc đọc của chính cụm sống ở đó. **§5.3** áp dụng nguyên tắc chống phân đoạn ở Chương Một; nó không nhắc lại cơ chế Chương Năm đó.

**Điều quyền nào vẫn kiểm soát.** **§5.3** là nguyên tắc Chương Một. Nó không thay Sàn Quyền Chương Sáu. Bên trong **§5.3**, những điều đó vẫn quyết quyền là gì và có thể bị hạn chế thế nào:
- **[Điều V-H](../../core_06_rights_part_b.md#article-v-h-expression-assembly-and-press)** (*Biểu đạt, tụ họp, và báo chí*) — tụ họp, liên kết, và hành cùng nhau trong không gian vật lý, số, hoặc tính toán chung cho biểu đạt, chính trị, văn hóa, cộng đồng, và mục đích tương tự
- **[Điều III-D](../../core_06_rights_part_a.md#article-iii-d-labor-and-economic-floor)** (*Sàn lao động và kinh tế*) — tổ chức tập thể trong hoạt động sản xuất và kinh tế (công đoàn, hợp tác xã, phường hội, hội đồng người lao động, và hình tương đương dùng để định hình điều kiện làm việc), và [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional)
- **[Điều IX-B](../../core_06_rights_part_b.md#article-ix-b-stakeholder-role-and-participation-rights)** (*Quyền vai trò bên bị ảnh hưởng và tham gia*) và **[Điều XI](../../core_06_rights_part_b.md#article-xi-stakeholder-system-participation-representation-and-due-process)** (*Tham gia hệ thống của bên bị ảnh hưởng, đại diện, và thủ tục đúng đắn*) — [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional) (hình thành và vận hành thể chế phi thương mại)

**Khi cụm định nghĩa đầy đủ áp dụng.** Quy tắc chống phân đoạn áp dụng khi [Tụ họp](../../core_05_band_participation.md#assembly-constitutional), [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional), [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional), hoặc [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional) có trọng theo cách những câu hỏi đó đi cùng nhau.

**Khi quy tắc nhẹ hơn áp dụng.** Nếu việc chỉ là một trong những câu hỏi đó — ví dụ, một tụ họp công dân thường không có lợi hại tổ chức lao động hay hình thành thể chế — dùng [Tụ họp](../../core_05_band_participation.md#assembly-constitutional) hoặc [Tổ chức tập thể](../../core_05_band_participation.md#collective-organization-constitutional) như định nghĩa hỗ trợ thường. Đừng kéo vào [Tạo hệ thống](../../core_05_band_participation.md#system-creation-constitutional), [Tạo doanh nghiệp](../../core_05_band_participation.md#business-creation-constitutional), hoặc phần còn lại của cụm định nghĩa này, và đừng áp gói chống phân đoạn của **§5.3**, chỉ vì một trong những thuật ngữ đó xuất hiện. Dùng một định nghĩa không phải giấy phép phân đoạn lại một việc được phủ chung.

**Điều mục này không đổi.** **§5.3** chỉ thêm kỷ luật chống phân đoạn tầng nguyên tắc và con trỏ [§5.3.1 Tự tổ chức thẳng hàng](#531-aligned-self-organization). Nó **không** tạo, mở rộng, hay thu hẹp bất kỳ điều khoản Sàn Quyền Chương Sáu nào.

Một việc trong phạm vi đọc-cùng đó không được phân đoạn thành khung hội công dân, tổ chức lao động, lối vào nền tảng, hoặc ủy quyền riêng theo cách giữ lối vào hình thức trong khi đánh bại bảo vệ tụ họp hoặc tổ chức tập thể.

Đánh giá toàn hệ thống phải thử chống phân đoạn dưới [Chương Bảy §3.5 Tụ họp, tổ chức tập thể, và hình thành thể chế](../../core_07_a_system_alignment_certification_evaluation.md#35-assembly-collective-organization-and-institutional-formation) trước khi phân loại, quản trị, hoặc tuyên bố tuân thủ đứng nơi cụm định nghĩa đầy đủ áp dụng.

##### 5.3.1 Tự tổ chức thẳng hàng
<a id="531-aligned-self-organization"></a>

*Nói thẳng: bạn có thể bắt đầu công việc chính danh mà không cần nhà bảo trợ, và thể chế phải cho công việc đáng tin một đường thủ tục thực — nhưng đường đó không phải quyền quản trị người khác, và không phải quyết định cuối về nội dung.*

Tự do tụ họp hoặc tạo hệ thống gồm một cách thực để bắt đầu công việc Hiến pháp này coi chính danh, mà không chờ người đã nắm quyền bảo trợ bạn. [§9.5 Tự tổ chức thẳng hàng](core_01_c_stewardship_capacity_principles.md#95-aligned-self-organization) là nhà vận hành. Tiểu mục này áp dụng quy tắc đó ở tầng Tự do / tụ họp-và-hình-thành.

Khi công việc đó đáng tin và liên quan vật chất, thể chế phải cho nó một đường thủ tục thực:
- nhận nó
- giữ nó nơi đáng
- định tuyến nó
- đưa phản hồi có lý
- để ai đó độc lập với những người mà hành động đang bị xem xét rà soát nó

Đường đó không phải cấp quyền. Bắt đầu, vận hành, tài trợ, công bố, hoặc nộp công việc không, tự nó:
- cho ai quyền quản trị người khác, thi hành chống họ, hoặc cưỡng họ
- ràng buộc người không đồng ý một kết quả nội dung
- quyết quỹ đạo, trách nhiệm, quyền được hưởng, hiệu lực, một nhiệm vụ, một biện pháp khắc phục, một phân loại, hoặc một hạn chế quyền
- được tính là [Xác định nội dung](../../core_05_band_accountability.md#merits-determination) — quyết định ràng buộc về nội dung tranh chấp

Được nhận, định tuyến, hoặc trả lời không phải phê chuẩn kết luận của tác giả. Mọi hiệu ứng quản trị hoặc nội dung đòi thẩm quyền hợp pháp, bằng chứng, thủ tục công bằng, rà soát, và khắc phục riêng mà Hiến pháp này gán. Quy tắc đầy đủ không-tự-bổ-nhiệm sống ở [§9.5 Tự tổ chức thẳng hàng](core_01_c_stewardship_capacity_principles.md#95-aligned-self-organization).

<br>

---

**Tệp trước:** [core_00_preamble.md](core_00_preamble.md)

**Tệp tiếp theo (ngôn ngữ này):** [core_01_b_interaction_interpretation.md](core_01_b_interaction_interpretation.md)

**Nguyên bản ràng buộc:** [core_01_a_values_principles.md](../../core_01_a_values_principles.md)
