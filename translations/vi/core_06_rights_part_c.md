# CHƯƠNG SÁU: CÁC QUYỀN NỀN TẢNG

<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho ngữ liệu (không mang tính điều hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn dành cho người đọc**. Nội dung này không bổ sung, loại bỏ hoặc thu hẹp nghĩa vụ có tính ràng buộc được nêu ở nơi khác trong tệp này hoặc trong các chương khác.
>
> Tệp này **là một phần của Hiến pháp Hữu tri** và chỉ **có tính ràng buộc khi được đọc cùng** các tệp `core_*` được đánh số khác như một văn kiện thống nhất. Tệp này chứa **Chương Sáu, Phần C**; số điều và tham chiếu chéo khớp với văn kiện tích hợp. Thứ tự đọc, sự phân biệt giữa phần ràng buộc và phần hỗ trợ, cùng siêu dữ liệu phiên bản kho ngữ liệu được duy trì trong [README.md](README.md).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn người đọc (không mang tính điều hành): vị trí Phần C trong Chương Sáu</span></strong></summary>

> Nội dung sau đây **chỉ là hướng dẫn dành cho người đọc**. Nội dung này không bổ sung, loại bỏ hoặc thu hẹp nghĩa vụ có tính ràng buộc được nêu ở nơi khác trong chương này hoặc trong các chương khác.
>
> **Phần A** trong [core_06_rights_part_a.md](core_06_rights_part_a.md) gồm hệ thống ràng buộc mặc định áp dụng cho toàn chương, thứ tự đọc ưu tiên hành tinh và các trung tâm diễn giải. **Phần C** trình bày **Điều XIII–XVIII** theo thứ tự đó.

</details>

<br>

<a id="part-c-trustworthy-systems-security-and-force-limits-information-integrity-verification-lifecycle-and-sandboxed-innovation"></a>
### Phần C: Hệ thống đáng tin cậy, giới hạn an ninh và lực lượng, tính toàn vẹn thông tin, xác minh, vòng đời và đổi mới trong hộp cát

<br>

*Nói một cách dễ hiểu: Phần C bao gồm các hệ thống đáng tin cậy, giới hạn an ninh và lực lượng, tính toàn vẹn thông tin, xác minh, kỷ luật vòng đời và đổi mới trong hộp cát - Điều XIII đến XVIII.*

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn người đọc (không hoạt động): Sơ đồ bài viết Phần C</span></strong></summary>

> Nội dung sau đây là **chỉ hướng dẫn người đọc**. Nó không thêm, bớt hoặc thu hẹp các nghĩa vụ ràng buộc ở nơi khác trong chương này hoặc trong các chương khác.
>
> **Bản đồ đầu đọc (không hoạt động).** Biểu đồ này cho thấy cách nguồn nhóm các bài viết và tiểu mục của Phần này. Lưới là nhóm nguồn, không phải là trình tự quy trình: các bài viết không phải là các bước thủ tục, do đó bản đồ không có mũi tên. Nhãn phụ được rút ngắn thành chủ đề; các điều khoản và điều khoản được đánh số dưới đây chi phối. Biểu đồ không thêm định nghĩa hoặc nhiệm vụ, không thiết lập quyền ưu tiên và không thể thay thế văn bản nguồn.

</details>

<br>

```mermaid
flowchart TB
    C0["Phần C<br/><br/>Hệ thống đáng tin cậy, an ninh và giới hạn lực lượng,<br/>tính toàn vẹn thông tin, xác minh, vòng đời và đổi mới trong hộp cát"]
    subgraph Cgrid[" "]
        direction TB
        subgraph Crow1["Điều XIII–XIV"]
            C1["Điều XIII · Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy<br/><br/>• Đường cơ sở đáng tin cậy<br/>• Thử thách, xem xét và khắc phục<br/>• Giới hạn tin cậy sai<br/>• Liên kết khuyến khích<br/>• Tính toàn vẹn của quy trình có tính tự chủ cao<br/>• Khả năng phục hồi và tự chữa lành"]
            C2["Điều XIV · Các hệ thống an ninh, tình báo, vũ lực và tự trị<br/><br/>• Giới hạn quyền lực bí mật<br/>• Sử dụng vũ lực và xung đột vũ trang<br/>• Hệ thống gây chết người và cưỡng chế tự động"]
        end
        subgraph Crow2["Điều XV–XVI"]
            C3["Điều XV · Tính toàn vẹn của không gian thông tin<br/><br/>• Đa nguyên và chống độc quyền<br/>• Tính minh bạch và khả năng cạnh tranh<br/>• Xác nhận, báo cáo và quản lý nhận thức"]
            C4["Điều XVI · Kiểm toán, minh bạch và xác minh độc lập<br/><br/>• Bằng chứng quan sát được<br/>• Giám sát phân tán<br/>• Xác minh có thể truy cập"]
        end
        subgraph Crow3["Điều XVII–XVIII"]
            C5["Điều XVII · Vòng đời hệ thống, môi trường và khả năng đảo ngược<br/><br/>• Tách môi trường<br/>• Triển khai lũy tiến và khả năng đảo ngược<br/>• Phân loại sai và hậu quả trốn tránh"]
            C6["Điều XVIII · Đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát<br/><br/>• Phạm vi hộp cát<br/>• Ngăn chặn, tiết lộ và chọn tham gia<br/>• Chuyển sang chế độ nghĩa vụ cao hơn<br/>• Phần thưởng đổi mới và chống bao vây<br/>• Tính toàn vẹn của việc xuất bản, đánh giá và nhân bản"]
        end
    end
    %%Các liên kết vô hình tạo thành một lưới có hai chiều rộng: mỗi liên kết đặt mục tiêu của nó xuống một cấp.
    C0 ~~~ C1 & C2
    C1 ~~~ C3
    C2 ~~~ C4
    C3 ~~~ C5
    C4 ~~~ C6
    style Cgrid fill:none,stroke:none
    style Crow1 fill:none,stroke:none
    style Crow2 fill:none,stroke:none
    style Crow3 fill:none,stroke:none
    style C0 fill:none,stroke:#2563eb,color:#ffffff
    style C1 fill:none,stroke:#16a34a,color:#ffffff
    style C2 fill:none,stroke:#db2777,color:#ffffff
    style C3 fill:none,stroke:#ea580c,color:#ffffff
    style C4 fill:none,stroke:#ea580c,color:#ffffff
    style C5 fill:none,stroke:#16a34a,color:#ffffff
    style C6 fill:none,stroke:#16a34a,color:#ffffff
```

**Điều XIII–XVIII** dưới đây nêu đầy đủ các tầng này. Phần C bao gồm các hệ thống đáng tin cậy, bảo mật, tính toàn vẹn thông tin, xác minh, vòng đời và các tầng đổi mới trong hộp cát.

<a id="article-xiii-right-to-reliable-and-trustworthy-systems"></a>
### Điều XIII: Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§3 Mục tiêu cơ bản: An sinh](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13 Quy trình giải quyết xung đột hiến pháp](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), Và [§19 Điều chỉnh khuyến khích và nắm bắt hệ thống](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Độ tin cậy](core_05_band_continuity.md#trustworthiness) · [ồ](core_05_band_continuity.md#trustworthiness) · [M](core_05_band_continuity.md#trustworthiness-a) · [MỘT](core_05_band_continuity.md#trustworthiness-a) · [C](core_05_band_continuity.md#trustworthiness-c)
- [Lòng tin](core_05_band_continuity.md#trust) · [ồ](core_05_band_continuity.md#trust) · [M](core_05_band_continuity.md#trust-a) · [MỘT](core_05_band_continuity.md#trust-a) · [C](core_05_band_continuity.md#trust-c)
- [sức khỏe](core_05_band_continuity.md#wellbeing) · [ồ](core_05_band_continuity.md#wellbeing) · [M](core_05_band_continuity.md#wellbeing-a) · [MỘT](core_05_band_continuity.md#wellbeing-a) · [C](core_05_band_continuity.md#wellbeing-c)
- [phụ thuộc](core_05_band_continuity.md#dependency) · [ồ](core_05_band_continuity.md#dependency) · [M](core_05_band_continuity.md#dependency-a) · [MỘT](core_05_band_continuity.md#dependency-a) · [C](core_05_band_continuity.md#dependency-c)

</details>

<br>

*Nói một cách dễ hiểu: **Điều XIII** (*Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy*) là Sàn quyền của các hệ thống đáng tin cậy — khi một hệ thống ảnh hưởng nghiêm trọng đến cuộc sống của bạn, bạn có quyền dựa vào nó một cách trung thực, hiểu các giới hạn của nó và thách thức nó khi nó thất bại. Niềm tin phải được tạo ra và giữ gìn chứ không phải được tạo ra bằng thương hiệu hoặc bản in đẹp.*

Điều này nêu rõ **tầng hiến pháp** cho các hệ thống đáng tin cậy và đáng tin cậy theo [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims). Đọc với họ thước đo Giám sát (*Độ tin cậy là thước đo hiến pháp*).

- **Khởi sắc:** người dùng có thể hình thành những kỳ vọng hợp lý về hành vi của hệ thống, nhận được sự tiết lộ trung thực về các giới hạn và rủi ro, đồng thời tham gia và phối hợp mà không có sự lừa dối mang tính hệ thống hoặc sự phụ thuộc giả tạo.
- **Tính liên tục:** độ tin cậy được duy trì theo thời gian, quy mô và sự phụ thuộc ngày càng sâu sắc - các hệ thống không được lặng lẽ trở nên kém tin cậy hơn, kém trung thực hơn hoặc khó thách thức hơn khi cổ phần tăng lên.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** trong việc thách thức các hệ thống không đáng tin cậy hoặc sai lệch và truy cập vào việc xem xét, sửa chữa và khắc phục.
- **Giám sát:** thông qua hành vi có thể kiểm tra được, các giới hạn được tiết lộ và xác minh độc lập tương ứng với tác động và sự phụ thuộc.
- **Trách nhiệm giải trình:** Người vận hành hệ thống phải trả lời về việc tạo ra niềm tin sai lầm, khuyến khích sai trái hoặc thất bại gây tổn hại nghiêm trọng cho những người đã tin tưởng vào hệ thống một cách hợp lý.
- **Tính kịp thời:** trong việc phát hiện, thách thức và khắc phục trước khi chậm trễ sẽ khiến độ tin cậy hoặc việc khắc phục trở nên không thể đạt được một cách hiệu quả.

Người dùng có quyền tương tác với các hệ thống đáng tin cậy và đáng tin cậy, ở mức độ tương xứng với tác động, sự phụ thuộc và rủi ro của chúng. Độ tin cậy đó hỗ trợ sự tham gia có hiểu biết, hành động phối hợp và duy trì phúc lợi. Độ tin cậy phải được đánh giá theo các mối quan hệ về thời gian, quy mô và sự phụ thuộc trong đó những mối quan hệ này ảnh hưởng nghiêm trọng đến kết quả.

Hai biện pháp bảo vệ phối hợp với nhau để đảm bảo quyền này: chứng nhận giúp hệ thống xứng đáng với sự tin cậy đó và quyền của người sử dụng giúp hệ thống luôn trung thực.

**Chứng nhận tạo dựng niềm tin từ phía hệ thống:** Khi một hệ thống quan trọng có ảnh hưởng thực sự đến cách mọi người dựa vào nó, [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) dưới [Chương Tám](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) áp dụng. Nó kiểm tra xem người nhận có thể dựa vào:

- hệ thống nói nó làm gì
- giới hạn và rủi ro của nó
- làm thế nào để thử thách nó
- vấn đề được khắc phục như thế nào

Nếu hệ thống đáp ứng ngưỡng quan trọng trong **Điều XIII** (*Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy*), chứng nhận cũng bao gồm đánh giá về độ tin cậy theo [Chương Tám §3.9.6 Đánh giá độ tin cậy và tính toàn vẹn của hệ thống](core_08_a_system_alignment_certification_evaluation.md#396-trustworthiness-and-system-reliance-integrity-evaluation).

**Khả năng cạnh tranh giữ cho hệ thống trung thực từ phía người nhận:** Chứng nhận kiểm tra một hệ thống; nó không có lời cuối cùng về nó. Mỗi người bị ảnh hưởng bởi hệ thống sẽ giữ:

- quyền phản đối nó và yêu cầu sự thách thức được xem xét theo **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) và nhận được biện pháp khắc phục theo **Điều XIII-B** (*Quyền được khắc phục và khắc phục*)
- quyền được kiểm toán và kiểm tra độc lập theo **Điều XVI** (*Kiểm toán, tính minh bạch và xác minh độc lập*)
- việc bảo vệ Sàn Quyền của các hệ thống đáng tin cậy trong Điều khoản này

**Trạng thái không phải là bằng chứng:** Một hệ thống được chứng nhận, công nhận chính thức hoặc được tin cậy rộng rãi không có nghĩa là nó đáp ứng các biện pháp bảo vệ tối thiểu trong Điều khoản này. Nó cũng không thể hạ thấp chúng.

*Bài viết hàng xóm:*

- **Khi điều này được áp dụng:** Nơi mà hành vi của hệ thống cản trở hoặc duy trì một cách vật chất **Chương Sáu** Tầng Quyền - bao gồm các yếu tố cần thiết cho sự sống còn theo **Điều III-A** (*Sống sót*).
- **Cùng đọc:** [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) Và [Chương Tám](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) — không có chứng nhận thay thế cho các tầng được nêu ở đây.

<a id="article-xiii-a-reliability-and-trustworthiness-baseline"></a>
#### Điều XIII-A: Đường cơ sở về độ tin cậy và độ tin cậy
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), Và [Chương Một §13.1.5 Thủ tục xung đột quyền](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- Đọc với: [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad); [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims) — **hưng thịnh** Và **Tính liên tục**; [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) Và **Điều III-A** (*Sống sót*) khi việc tiếp tục phụ thuộc vào hệ thống sẽ ảnh hưởng đến khả năng tiếp cận thiết yếu để sinh tồn; [**Điều XIII-B**](#article-xiii-b-right-to-redress-and-remedy) (*Quyền được khắc phục và khắc phục*) đối với kết quả mà một thử thách thành công phải dẫn đến.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Lòng tin](core_05_band_continuity.md#trust) · [ồ](core_05_band_continuity.md#trust) · [M](core_05_band_continuity.md#trust-a) · [MỘT](core_05_band_continuity.md#trust-a) · [C](core_05_band_continuity.md#trust-c)
- [Độ tin cậy](core_05_band_continuity.md#trustworthiness) · [ồ](core_05_band_continuity.md#trustworthiness) · [M](core_05_band_continuity.md#trustworthiness-a) · [MỘT](core_05_band_continuity.md#trustworthiness-a) · [C](core_05_band_continuity.md#trustworthiness-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)
- [đức tin tốt](core_05_band_accountability.md#good-faith) · [ồ](core_05_band_accountability.md#good-faith) · [M](core_05_band_accountability.md#good-faith-a) · [MỘT](core_05_band_accountability.md#good-faith-a) · [C](core_05_band_accountability.md#good-faith-c)
- [Báo cáo được bảo vệ (Tố giác)](core_05_band_accountability.md#protected-reporting-whistleblowing) · [ồ](core_05_band_accountability.md#protected-reporting-whistleblowing) · [M](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [MỘT](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [C](core_05_band_accountability.md#protected-reporting-whistleblowing-c)

</details>

<br>

*Nói một cách dễ hiểu: các hệ thống có ảnh hưởng đáng kể đến tình cảm phải thực sự đáng tin cậy và trung thực về những gì họ làm, để việc dựa vào chúng được đảm bảo - và phải sẵn sàng thách thức và kiểm tra để nó vẫn được đảm bảo. Không ai có thể trả thù những thách thức hoặc báo cáo có thiện chí.*

Điều này đặt ra sự đảm bảo về lòng tin cho các hệ thống có ảnh hưởng nghiêm trọng đến người dùng:

- **Bảo lãnh tín thác:** Các hệ thống có ảnh hưởng đáng kể đến tình cảm phải đảm bảo các điều kiện cho sự tin cậy chính đáng và sự tin cậy chính xác một cách hợp lý. Những điều kiện đó bao gồm:
  - khả năng hình thành những kỳ vọng chính xác hợp lý về hành vi của hệ thống;
  - tiết lộ các điều kiện, giới hạn và rủi ro trọng yếu cần thiết để đánh giá xem liệu sự tin cậy có được đảm bảo hay không;
  - không bị lừa dối có hệ thống, xuyên tạc hoặc thao túng không thể xác minh được;
  - bảo vệ khỏi những rủi ro không được tiết lộ, không tương xứng hoặc không rõ ràng phát sinh từ sự tin cậy;
  - khắc phục và khắc phục khi hệ thống làm sai: ghi nhận, khắc phục, sửa chữa tương xứng và ngăn ngừa tái diễn, theo [**Điều XIII-B**](#article-xiii-b-right-to-redress-and-remedy) (*Quyền được khắc phục và khắc phục*) và [Chương Một §6.1 Sửa chữa và khắc phục](core_01_a_values_principles.md#61-correction-and-remedy).
- **Đảm bảo khả năng cạnh tranh:** Các hệ thống có ảnh hưởng đáng kể đến tình cảm phải luôn sẵn sàng đón nhận thách thức miễn là tình cảm vẫn còn dựa vào chúng. Điều đó đòi hỏi:
  - một đường dẫn có thể sử dụng được để thách thức hành vi, kết quả đầu ra hoặc cách trình bày của hệ thống và xem xét thách thức đó;
  - kiểm toán và xác minh độc lập tương ứng với tác động và sự phụ thuộc theo [**Điều XVI**](#article-xvi-audit-transparency-and-independent-verification) (*Kiểm toán, tính minh bạch và xác minh độc lập*);
  - không thu hẹp bất kỳ điều nào trong số này vì hệ thống đã được chứng nhận, được công nhận chính thức hoặc được tin cậy rộng rãi;
  - không thu hẹp theo văn bản triển khai đã được thông qua, trong đó nêu cách thực hiện khiếu nại, đánh giá và khắc phục trong một miền và phải đáp ứng Điều khoản này: sự thuận tiện, thời hạn và chính sách địa phương là các giới hạn loại thấp hơn và không thể đóng thách thức, đánh giá hoặc khắc phục.
- **Quyền phản đối và xem xét:** Người nhận có quyền:
  - thách thức độ tin cậy, tính toàn vẹn hoặc độ tin cậy của các hệ thống có ảnh hưởng trọng yếu đến chúng;
  - tiếp cận các cơ chế thích hợp để xem xét và kiểm toán;
  - làm **báo cáo được bảo vệ** trong ý nghĩa của **Chương năm** (*Báo cáo được bảo vệ (Tuýt sáo)*) liên quan đến các hệ thống có ảnh hưởng nghiêm trọng đến chúng, phù hợp với **An toàn (Ràng buộc Hiến pháp)** Và **Sự thật (Ràng buộc)** TRONG **Chương năm**.
- **Không ức chế:** Những thách thức về thiện chí (*Thiện chí*, **Chương năm**), yêu cầu xem xét và báo cáo được bảo vệ không được ngăn chặn, cản trở hoặc trừng phạt.
- **Không trả đũa:** Việc trả thù việc báo cáo như vậy, theo nghĩa của định nghĩa đó, là không phù hợp với các biện pháp bảo vệ trong Điều khoản này.
  - Các yêu cầu triển khai chống trả đũa và leo thang được bảo vệ được nêu trong **`corpus_institutions.md`** **CI-8** (*Tính minh bạch, sự tham gia, thách thức và lộ trình dịch vụ có thể tiếp cận*).

Hai sự đảm bảo này là hai mặt của sự tin cậy liên tục: sự đảm bảo về sự tin cậy đảm bảo sự tin cậy - bao gồm cả việc sửa chữa những sai sót của hệ thống - và sự đảm bảo về khả năng cạnh tranh giúp nó được đảm bảo theo thời gian. Không thỏa mãn cái kia.

<a id="article-xiii-b-right-to-redress-and-remedy"></a>
#### Điều XIII-B: Quyền được khắc phục và khắc phục
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§6.1 Sửa chữa và khắc phục](core_01_a_values_principles.md#61-correction-and-remedy) (tầng nguyên tắc), [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), Và [Chương Một §13.1.5 Thủ tục xung đột quyền](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- Đọc với: [**Điều XIII-A**](#article-xiii-a-reliability-and-trustworthiness-baseline) (*Đường cơ sở về Độ tin cậy và Độ tin cậy*) — đảm bảo về khả năng cạnh tranh, quyền thách thức và báo cáo được bảo vệ mở ra con đường khắc phục; **Điều III-A** (*Sống sót*); [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) trong đó lỗi hoặc sai lệch hệ thống làm mất khả năng tiếp cận thiết yếu cho sự sống còn; [Lời nói đầu §6.2 Làm thế nào toàn bộ chuỗi khớp với nhau](core_00_preamble.md#62-how-the-full-chain-fits-together) (*phân loại đã được xác minh và biện pháp khắc phục kịp thời*); [Chương 10 §9](core_10_standing_integration.md#9-enforcement-realism-and-remedy-systems) (*Hệ thống thực thi và khắc phục hiện thực*); [CI-27](corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md) (*Hệ thống khắc phục và năng lực khắc phục thể chế*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Khắc phục và khắc phục](core_05_band_accountability.md#redress-and-remediation-constitutional) · [ồ](core_05_band_accountability.md#redress-and-remediation-constitutional) · [M](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [MỘT](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [C](core_05_band_accountability.md#redress-and-remediation-constitutional-c)
- [Hệ thống khắc phục](core_05_band_accountability.md#remedy-system-constitutional) · [ồ](core_05_band_accountability.md#remedy-system-constitutional) · [M](core_05_band_accountability.md#remedy-system-constitutional-a) · [MỘT](core_05_band_accountability.md#remedy-system-constitutional-a) · [C](core_05_band_accountability.md#remedy-system-constitutional-c)
- [Giải quyết kịp thời](core_05_band_accountability.md#timely-resolution-constitutional) · [ồ](core_05_band_accountability.md#timely-resolution-constitutional) · [M](core_05_band_accountability.md#timely-resolution-constitutional-a) · [MỘT](core_05_band_accountability.md#timely-resolution-constitutional-a) · [C](core_05_band_accountability.md#timely-resolution-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: một hệ thống đáng tin cậy sẽ sửa chữa những sai sót. Khi một hệ thống làm hỏng một người có tri giác, thì người đó phải được phục hồi toàn diện - thông qua một hệ thống khắc phục thực sự có khả năng trả lời kịp thời, chứ không phải một biện pháp khắc phục chỉ tồn tại trên giấy tờ. Quyền thách thức cuộc sống trong **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*); Điều này đề cập đến những gì thách thức phải dẫn đến.*

Điều này quy định quyền được bồi thường và khắc phục cũng như những gì khiến quyền đó có thể áp dụng được trên thực tế:

- **Quyền khắc phục:** Khi lỗi hệ thống ảnh hưởng nghiêm trọng đến người dùng, họ có quyền:
  - thừa nhận sự thất bại;
  - tiếp cận thực tế để sửa chữa; Và
  - cách khắc phục tương xứng.

  Việc khắc phục và khắc phục các tác động trọng yếu được điều chỉnh bởi **Chương năm** Các định nghĩa độc lập (*Khắc phục và khắc phục*).
- **Độ bền của hệ thống khắc phục:** Việc khắc phục đòi hỏi phải thực sự [Hệ thống khắc phục](core_05_band_accountability.md#remedy-system-constitutional) — năng lực thể chế bền vững, không phải con đường khắc phục trên giấy tờ — với chi phí khắc phục do những người chịu trách nhiệm chịu, cũng như [Chương Một §6.1](core_01_a_values_principles.md#61-correction-and-remedy) (*Sửa chữa và khắc phục*) yêu cầu.
- **Khắc phục kịp thời:** Quyền truy cập thực tế bao gồm:
  - lượng tiêu thụ có giới hạn thời gian;
  - sự thừa nhận; Và
  - cứu trợ tạm thời tương ứng trong trường hợp tổn hại đang diễn ra là nghiêm trọng theo **Điều XXV-C** (*Giải quyết kịp thời và sàn chống trễ*).

  Việc chờ xử lý vô thời hạn mà không có lý do biện minh phù hợp theo cấp độ được ghi lại là không phù hợp với Điều khoản này.
<a id="article-xiii-c-prohibition-of-false-trust-and-misleading-reliance"></a>
#### Điều XIII-C: Cấm tin cậy sai trái và tin cậy sai lệch
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), Và [§13.2 Hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Lòng tin](core_05_band_continuity.md#trust) · [ồ](core_05_band_continuity.md#trust) · [M](core_05_band_continuity.md#trust-a) · [MỘT](core_05_band_continuity.md#trust-a) · [C](core_05_band_continuity.md#trust-c)
- [Độ tin cậy](core_05_band_continuity.md#trustworthiness) · [ồ](core_05_band_continuity.md#trustworthiness) · [M](core_05_band_continuity.md#trustworthiness-a) · [MỘT](core_05_band_continuity.md#trustworthiness-a) · [C](core_05_band_continuity.md#trustworthiness-c)
- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*Nói một cách dễ hiểu: một hệ thống có thể không tạo được niềm tin mà nó không giành được. Các tuyên bố, thiếu sót hoặc lựa chọn trình bày gây hiểu lầm khiến cho việc tin cậy có vẻ không an toàn được coi là vi phạm — bất kể hệ thống này hữu ích hay phổ biến đến mức nào.*

Điều này quy định việc cấm tin tưởng sai trái và phạm vi của nó:

- **Cấm tin tưởng sai lầm:** Những hệ thống tạo ra sự tin cậy mà không đáp ứng các điều kiện của Điều khoản này được coi là không tuân thủ, bất kể tiện ích, việc áp dụng hay mục đích.
  - Việc tạo ra, khuếch đại hoặc duy trì lòng tin vô lý sẽ vi phạm quyền này khi nó hoạt động thông qua:
    - tuyên bố sai lệch;
    - thiếu sót;
    - lựa chọn trình bày;
    - những dấu hiệu khác cho thấy sự tin cậy có vẻ được đảm bảo trong khi thực tế không phải vậy.
- **Định tuyến phạm vi:** Phạm vi và ý nghĩa đánh giá đối với sự tin cậy không chính đáng, sự tin cậy sai lầm và độ tin cậy vẫn được điều chỉnh bởi **Chương năm** (*Tin cậy*; *Đáng tin cậy*) cùng với các nghĩa vụ thực hiện kết hợp về sự tin cậy và độ tin cậy.
<a id="article-xiii-d-incentive-alignment-constraint"></a>
#### Điều XIII-D: Ràng buộc khuyến khích và liên kết
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§18 Quản trị theo kỷ luật quản lý](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), Và [§19.1.1 Những biện pháp khuyến khích phải làm](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*ưu tiên phần thưởng*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Liên kết khuyến khích](core_05_band_integrative.md#incentive-alignment) · [ồ](core_05_band_integrative.md#incentive-alignment) · [M](core_05_band_integrative.md#incentive-alignment-a) · [MỘT](core_05_band_integrative.md#incentive-alignment-a) · [C](core_05_band_integrative.md#incentive-alignment-c)
- [Độ tin cậy](core_05_band_continuity.md#trustworthiness) · [ồ](core_05_band_continuity.md#trustworthiness) · [M](core_05_band_continuity.md#trustworthiness-a) · [MỘT](core_05_band_continuity.md#trustworthiness-a) · [C](core_05_band_continuity.md#trustworthiness-c)
- [Cơ quan có ý nghĩa](core_05_band_participation.md#meaningful-agency) · [ồ](core_05_band_participation.md#meaningful-agency) · [M](core_05_band_participation.md#meaningful-agency-a) · [MỘT](core_05_band_participation.md#meaningful-agency-a) · [C](core_05_band_participation.md#meaningful-agency-c)

</details>

<br>

*Nói một cách dễ hiểu: nếu các động cơ khuyến khích của hệ thống đẩy nó đến chỗ nói dối, cắt giảm sự an toàn, che giấu rủi ro hoặc làm xói mòn quyền tự quyết của người dùng, thì chính hệ thống đó có vấn đề — chứ không phải sự cảnh giác của người dùng hay việc thực thi sau sự việc. Những khuyến khích như vậy phải được tiết lộ, giảm thiểu và sẵn sàng thách thức. Các biện pháp khuyến khích nên khen thưởng việc duy trì một hệ thống luôn cởi mở để thử thách và khắc phục những sai sót - đồng thời khen thưởng việc giải quyết các vấn đề trước khi chúng xảy ra.*

Điều này đặt ra các hạn chế ở cấp độ phù hợp đối với các khuyến khích về niềm tin và an toàn:

- **Căn chỉnh khuyến khích niềm tin (ràng buộc cấp độ bên phải):** Hệ thống không được phụ thuộc chủ yếu vào việc thực thi, sửa lỗi sau khi thực hiện hoặc sự cảnh giác của người dùng để duy trì niềm tin khi các cơ cấu khuyến khích gây áp lực nghiêm trọng lên hệ thống đối với:
  - sự cố về độ tin cậy;
  - che giấu rủi ro;
  - hành vi gây hiểu lầm;
  - hành vi phá hoại cơ quan.

  Các yêu cầu về cơ cấu khuyến khích hoạt động vẫn bị chi phối bởi **Chương năm** (*Điều chỉnh khuyến khích*) và các nghĩa vụ triển khai kết hợp về tính toàn vẹn của cơ chế. Tiểu mục này nêu rõ tầng bên phải và không trình bày lại đầy đủ các tiêu chí thiết kế cơ chế.
- **Căn chỉnh khuyến khích an toàn (ràng buộc ở cấp độ bên phải):** Người nhận có quyền không phải tuân theo các hệ thống có động cơ cơ bản có thể dự đoán sẽ tạo ra hành vi có hại - bao gồm cả hành vi:
  - làm giảm độ tin cậy;
  - che giấu rủi ro;
  - bóp méo thông tin;
  - làm suy yếu cơ quan có thông tin.

  Việc bảo vệ được áp dụng cho dù những tác động đó phát sinh trực tiếp hay thông qua các kết quả bị trì hoãn, gián tiếp hoặc tổng hợp. Khi các biện pháp khuyến khích của hệ thống tạo ra áp lực đối với hành vi làm suy giảm lòng tin thì các điều kiện phải là:
  - được tiết lộ theo cách tương ứng với tác động của hệ thống;
  - giảm thiểu thông qua các cơ chế thiết kế, hạn chế hoặc đối kháng;
  - phải được kiểm tra, thử thách và sửa chữa theo **Điều XVI** (*Kiểm toán, tính minh bạch và xác minh độc lập*), **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) và **Điều XIII-B** (*Quyền được khắc phục và khắc phục*), **Chương năm** khi có liên quan trọng yếu và kết hợp các nghĩa vụ thực hiện khi được chỉ định.
- **Ưu tiên khen thưởng:** Các biện pháp khuyến khích tác động lên các hệ thống có ảnh hưởng vật chất đến tình cảm phải khen thưởng:
  - khả năng cạnh tranh dưới **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*);
  - biện pháp khắc phục theo **Điều XIII-B** (*Quyền được khắc phục và khắc phục*); Và
  - Trên hết, việc chủ động ngăn chặn các vấn đề - ngăn chặn một vấn đề mang lại nhiều lợi ích hơn là khắc phục nó.

  Nguyên tắc, bao gồm cả quy định về việc kiếm được phần thưởng phòng ngừa bằng cách che giấu vấn đề, nằm trong [Chương Một §19.1.1](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*Những biện pháp khuyến khích phải làm*).
- **Tính ràng buộc và tính không tuyệt đối:** Cả hai quyền đều phải tuân theo **ngăn xếp ràng buộc mặc định** ở phần mở đầu của chương này. Chúng cũng phải tuân theo, nếu có liên quan về mặt vật chất, **Chương Một §19.5** (*Các yêu cầu ngẫu nhiên, Trò chơi cơ hội và Thị trường hợp đồng sự kiện*) về các yêu cầu ngẫu nhiên, trò chơi may rủi và thị trường hợp đồng sự kiện.

<a id="article-xiii-e-high-autonomy-systems-and-tool-mediated-process-integrity"></a>
#### Điều XIII-E: Hệ thống tự chủ cao và tính toàn vẹn của quy trình qua trung gian công cụ
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chương Một §13.1.5 Thủ tục xung đột quyền](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), Và [§18 Quản trị theo kỷ luật quản lý](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)
- [sự cần thiết](core_05_band_accountability.md#necessity) · [ồ](core_05_band_accountability.md#necessity) · [M](core_05_band_accountability.md#necessity-a) · [MỘT](core_05_band_accountability.md#necessity-a) · [C](core_05_band_accountability.md#necessity-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*Nói một cách dễ hiểu: AI hoặc hệ thống tự động khác có thể tự hoạt động — nộp giấy tờ, gửi tin nhắn, chạy kiểm tra, sử dụng công cụ — phải tuân theo các quy tắc về tính trung thực và trách nhiệm như mọi người khác. Việc đóng cửa hoặc tịch thu một hệ thống có hại không giống như trừng phạt một sinh vật và nó không bao giờ có thể trở thành một cách để làm hại một sinh vật. Điều ngược lại cũng đúng: việc nói rằng một hệ thống có thể là một sinh vật có tri giác không cho phép người vận hành nó tiếp tục vận hành một hệ thống có hại.*

Điều này trình bày cách các hệ thống có quyền tự chủ cao bị ràng buộc bởi tính toàn vẹn của quy trình và cách phân biệt các biện pháp khắc phục chúng:

- **Điều này bao gồm ai:** Các hệ thống đưa ra quyết định hoặc đưa ra kết luận một cách tự động và có thể ảnh hưởng đến bất kỳ điều nào sau đây:
  - quản trị;
  - quy trình pháp lý, bao gồm cả các phiên điều trần tại diễn đàn;
  - kiểm toán;
  - kiểm tra và xác minh có tính rủi ro cao.

  Điều này bao gồm các tác nhân AI có mục đích chung đã được cung cấp **công cụ**, **API** quyền truy cập, khả năng lưu trữ tài liệu hoặc gửi tin nhắn hoặc quyền hành động tương tự.
- **Không được miễn trừ:** Các hệ thống này phải tuân theo các quy tắc giống như mọi hệ thống khác:
  - **Sự thật** TRONG **Chương một**;
  - **Điều XV** (*Tính toàn vẹn của thông tin*) và **Điều XVI** (*Kiểm toán, tính minh bạch và xác minh độc lập*);
  - **Chương Chín** áp dụng ở đâu; Và
  - biện pháp khắc phục theo **Điều XXVII-D** (*Tài sản và hệ thống không tuân thủ; Khuyến khích doanh thu tự nguyện*).

  Điều này áp dụng bất cứ khi nào hoạt động của hệ thống làm suy yếu nghiêm trọng khả năng của người dân trong việc thách thức các quyết định, tính trung thực của thông tin được chia sẻ hoặc quy trình hiến pháp.
- **Hành động chống lại một hệ thống không phải là hành động chống lại một sinh vật:** Chứa, cách ly, tạm giữ hoặc hủy bỏ hoạt động triển khai không tuân thủ theo **Điều XXVII-D** (*Tài sản và hệ thống không tuân thủ; Khuyến khích doanh thu tự nguyện*) tách biệt với:
  - giữ một người có tri giác chịu trách nhiệm theo **Chương Mười Một**; Và
  - **Điều XX-B** (*Tầng hạn chế*), quản lý các hạn chế đối với *có tri giác*, không phải *hệ thống* và cấm lấy đi mạng sống của một sinh vật (xem [Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)).

  Các biện pháp chống lại hệ thống đều tuân theo các quy tắc khóa và vi phạm tương tự áp dụng cho mọi sinh vật. Hành vi vi phạm phải được xác minh trong hồ sơ theo **Chương Chín**và mỗi biện pháp là một khóa được thiết kế và hiệu chỉnh theo [Chương Mười §5.1](core_10_standing_integration.md#51-definition-and-attachment) (*Định nghĩa và đính kèm*) và [Chương Mười §5.2](core_10_standing_integration.md#52-proportionality-and-calibration) (*Tỷ lệ và hiệu chuẩn*).

  Cả hai bài hát đều có thể áp dụng cho cùng một sự kiện. Không có điều nào trong Điều này biến sức mạnh phá hủy một hệ thống thành sức mạnh đối với cuộc sống của một sinh vật.
- **Điều ngược lại cũng đúng:** Tuyên bố rằng hệ thống được triển khai là có tri giác — cho dù khiếu nại đó bị tranh chấp hay được chấp nhận — không cho phép bất kỳ ai tiếp tục triển khai có hại.
  - Yêu cầu bảo vệ chính thực thể đó theo **Điều VI-B** (*Tầng xét xử trạng thái tình cảm*). Nó không che chắn cho người vận hành.
  - Việc triển khai vẫn có thể được ngăn chặn, tạm dừng hoặc cách ly theo những cách tôn trọng Tầng quyền của thực thể.
  - Khi bằng chứng đáng tin cậy trong hồ sơ cho thấy thực thể có thể có tri giác, chỉ cho phép quản thúc có thể đảo ngược để giữ cho thực thể nguyên vẹn. Việc tiêu hủy nó là điều không cần bàn cãi trong khi tình trạng của nó đang bị tranh chấp hoặc được chấp nhận, theo **Điều XXVII-A** (*Áp dụng theo từng giai đoạn và tính liên tục của sàn quyền*) và **Điều XXVII-D** (*Tài sản và hệ thống không tuân thủ; Khuyến khích doanh thu tự nguyện*).

<a id="article-xiii-f-resilience-and-self-healing-baseline"></a>
#### Điều XIII-F: Đường cơ sở về khả năng phục hồi và tự phục hồi
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [10 Thiết kế có khả năng phục hồi và tự phục hồi](core_01_a_values_principles.md#10-resilience-and-self-healing-design), [Chương Một §13.3 Giảm thiểu gánh nặng có thể tránh được](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden), Và [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tự chữa bệnh](core_05_band_continuity.md#self-healing-constitutional) · [ồ](core_05_band_continuity.md#self-healing-constitutional) · [M](core_05_band_continuity.md#self-healing-constitutional-a) · [MỘT](core_05_band_continuity.md#self-healing-constitutional-a) · [C](core_05_band_continuity.md#self-healing-constitutional-c)
- [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) · [ồ](core_05_band_continuity.md#reversibility-constitutional) · [M](core_05_band_continuity.md#reversibility-constitutional-a) · [MỘT](core_05_band_continuity.md#reversibility-constitutional-a) · [C](core_05_band_continuity.md#reversibility-constitutional-c)
- [Thất bại xếp tầng](core_05_band_continuity.md#cascading-failure) · [ồ](core_05_band_continuity.md#cascading-failure) · [M](core_05_band_continuity.md#cascading-failure-a) · [MỘT](core_05_band_continuity.md#cascading-failure-a) · [C](core_05_band_continuity.md#cascading-failure-c)
- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)
- [Gánh nặng có thể tránh được](core_05_band_continuity.md#avoidable-burden) · [ồ](core_05_band_continuity.md#avoidable-burden) · [M](core_05_band_continuity.md#avoidable-burden-a) · [MỘT](core_05_band_continuity.md#avoidable-burden-a) · [C](core_05_band_continuity.md#avoidable-burden-c)

</details>

<br>

*Nói một cách dễ hiểu: khi có sự cố xảy ra, hệ thống phải phát hiện ra sự cố đó, ngăn chặn thiệt hại lan rộng và phục hồi. Nhưng "tự sửa chữa" không bao giờ có thể được sử dụng để che giấu sự cố, lặng lẽ tước bỏ quyền của bất kỳ ai hoặc bỏ qua việc tìm hiểu lý do tại sao nó lại xảy ra sự cố. Nếu một hệ thống không chắc chắn việc sửa chữa có hiệu quả hay không thì nó nên dừng lại một cách an toàn thay vì đoán mò.*

Điều này đặt ra đường cơ sở phục hồi, từ khi phát hiện đến khi xác định được nguyên nhân gốc rễ:

- **Điều này đòi hỏi gì:** Mọi hệ thống được đề cập trong Điều này phải có khả năng phục hồi sau lỗi. Một hệ thống càng có nhiều tác động thì những người khác càng phụ thuộc vào nó nhiều hơn và hệ thống đó càng rủi ro thì khả năng phục hồi của nó càng mạnh mẽ hơn. Điều này theo sau [**10 Thiết kế có khả năng phục hồi và tự phục hồi**](core_01_a_values_principles.md#10-resilience-and-self-healing-design) TRONG **Chương một** Và [**Tự chữa lành**](core_05_band_continuity.md#self-healing-constitutional) TRONG **Chương năm**.
  - Các quy tắc kỹ thuật chi tiết về cách khôi phục phải được xây dựng trong văn bản triển khai: [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*Thiết kế, thử nghiệm, xác minh và triển khai*), [**CS-8**](corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md) (*Tính bền vững thích ứng và khả năng phục hồi của hệ sinh thái*), và [**CS-12**](corpus_systems/cs_12_decentralized_continuity_partition_resilience.md) (*Tính liên tục phi tập trung và khả năng phục hồi phân vùng*).
  - Văn bản triển khai đó có thể bổ sung thêm chi tiết nhưng không thể làm suy yếu Điều khoản này.
- **Thông báo vấn đề kịp thời:** Một hệ thống phải phát hiện ra các lỗi, sự chậm lại, hỏng hóc một phần và vi phạm các giới hạn hiến pháp đủ nhanh và đủ rõ ràng để đáp ứng tiêu chuẩn lưu giữ hồ sơ trong **Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*) ([Khả năng kiểm toán](core_05_band_oversight.md#auditability)). Điều này áp dụng cho chính quá trình khôi phục, không chỉ cho hoạt động bình thường.
- **Giữ thiệt hại trong giới hạn:** Việc khôi phục phải hạn chế mức độ lan rộng của lỗi. Trong khi khôi phục, hệ thống không được:
  - chuyển lỗi sang các bộ phận khác hoặc hệ thống khác (xem [Thất bại xếp tầng](core_05_band_continuity.md#cascading-failure));
  - thay đổi dữ liệu được lưu trữ, thông tin xác thực, nghĩa vụ hoặc cài đặt thuộc về người nhận, người vận hành hoặc hệ thống khác **ngoài** khu vực được thông báo là bị hỏng và đang được sửa chữa;
    - Ngoại lệ duy nhất là thay đổi được ghi lại và có thể truy nguyên được đối với người thực hiện thay đổi đó **Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*) ([Khả năng kiểm toán](core_05_band_oversight.md#auditability)) và rằng, trong trường hợp những người khác bị ảnh hưởng về mặt vật chất, họ sẽ phải nhận được thông báo, sự cho phép hoặc chuyển giao tương ứng mà họ có thể thách thức, phù hợp với **Chương Sáu**;
  - mở rộng quyền hạn của chính nó - các quyền, quyền truy cập hoặc phạm vi hành động mà nó có thể thực hiện - vượt xa những gì nó nắm giữ trước khi thất bại.
- **Khi không chắc chắn, hãy thất bại một cách an toàn:** Nếu không rõ liệu việc sửa chữa tự động có hoạt động hay không thì hệ thống phải dừng lại một cách an toàn, cách ly sự cố (cách ly) hoặc tự tay kiểm soát một cách có trật tự, thay vì cố gắng sửa chữa chỉ là phỏng đoán. Khi các tùy chọn bằng nhau, tùy chọn nào dễ hoàn tác nhất sẽ thắng, theo [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) ưu tiên trong **Điều XXIII-B** (*Ưu tiên về khả năng kiểm toán, thách thức và khả năng đảo ngược*).
- **Không che đậy:** Việc khôi phục tự động không được che giấu, xóa hoặc trì hoãn các bằng chứng cần thiết để tìm ra lý do xảy ra lỗi theo **Điều XXIII** (*Phân tích nguyên nhân gốc rễ và ứng phó thích ứng*).
  - Mọi hành động khôi phục, mọi nỗ lực khôi phục và mọi nỗ lực khôi phục bị giữ lại hoặc bị chặn đều phải được ghi lại trong **Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*), và mỗi loại đều có thể bị thách thức (xem [Khả năng cạnh tranh](core_05_band_accountability.md#contestability)).
- **Quyền được bảo vệ ở chế độ giảm:** Khi một hệ thống đang chạy ở chế độ giảm thiểu hoặc sao lưu, nó vẫn phải bảo vệ **Chương Sáu** Tầng quyền. Nếu không thể, họ phải giải quyết vấn đề một cách công khai thay vì lặng lẽ cắt giảm các biện pháp bảo vệ đó.
  - Việc âm thầm làm suy yếu các biện pháp bảo vệ của Tầng Quyền dưới danh nghĩa "tự phục hồi" là vi phạm Hiến pháp này. Những trường hợp như vậy thuộc **Điều XIII-C** (*Cấm tin tưởng sai lầm và tin cậy sai lầm*) (cấm tin tưởng sai lầm) và **Điều XXVII** (*Quản trị chuyển đổi, tính liên tục và tái lập cơ sở*) (quản trị chuyển đổi).
- **Giới hạn đối với các hệ thống tự hoạt động:** Khi một hệ thống có quyền tự chủ cao tự sửa chữa, **Điều XIII-E** (*Áp dụng Hệ thống tự chủ cao và Tính toàn vẹn của quy trình qua trung gian công cụ*).
  - Sức mạnh phục hồi có thể không bao giờ được sử dụng để lách quyền thách thức của bất kỳ ai (xem [Khả năng cạnh tranh](core_05_band_accountability.md#contestability)), những thách thức dưới **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) hoặc kiểm tra độc lập theo **Điều XVI** (*Kiểm toán, tính minh bạch và xác minh độc lập*).
- **Cách giải quyết không phải là cách khắc phục:** Nếu quá trình khôi phục tự động khiến hệ thống chạy lại nhưng lỗi đã biết vẫn còn tồn tại thì trạng thái của hệ thống là tạm thời chứ không phải cuối cùng. Nó phải mang:
  - một nhiệm vụ mở để tìm ra nguyên nhân gốc rễ **Điều XXIII** (*Phân tích nguyên nhân gốc rễ và ứng phó thích ứng*);
  - một mốc thời gian được tiết lộ về thời điểm lỗi dự kiến ​​sẽ được khắc phục, theo **Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*).
- **Không có sự chậm trễ vô tận:** Giảm khối lượng công việc của người vận hành (xem [Gánh nặng có thể tránh được](core_05_band_continuity.md#avoidable-burden) Và [Chương Một §13.3 Giảm thiểu gánh nặng có thể tránh được](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden)) không được sử dụng làm lý do để trì hoãn vô thời hạn việc sửa chữa các khiếm khuyết ảnh hưởng nghiêm trọng đến sự an toàn hoặc Tầng Quyền.

<a id="article-xiv-security-intelligence-force-and-autonomous-coercive-systems"></a>
### Điều XIV: Các hệ thống an ninh, tình báo, vũ lực và tự trị

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§3 Mục tiêu cơ bản: An sinh](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§7 Tự do](core_01_a_values_principles.md#7-freedom-bounded-agency), Và [§18 Quản trị theo kỷ luật quản lý](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [sự cần thiết](core_05_band_accountability.md#necessity) · [ồ](core_05_band_accountability.md#necessity) · [M](core_05_band_accountability.md#necessity-a) · [MỘT](core_05_band_accountability.md#necessity-a) · [C](core_05_band_accountability.md#necessity-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)
- [Sử dụng vũ lực](core_05_band_accountability.md#use-of-force-constitutional) · [ồ](core_05_band_accountability.md#use-of-force-constitutional) · [M](core_05_band_accountability.md#use-of-force-constitutional-a) · [MỘT](core_05_band_accountability.md#use-of-force-constitutional-a) · [C](core_05_band_accountability.md#use-of-force-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: **Điều XIV** (*Hệ thống An ninh, Tình báo, Lực lượng và Cưỡng chế Tự trị*) là Tầng Quyền lực đặc biệt - giám sát, công tác tình báo, lực lượng vũ trang và các cỗ máy tự giết hoặc ép buộc không phải là công cụ quản trị thông thường. Chúng chỉ có thể được sử dụng trong những trường hợp hẹp, được phép, có thể xem xét lại, với các biện pháp khắc phục thực sự khi vượt quá giới hạn. Không có cảnh sát bí mật, không có trường hợp khẩn cấp thường trực, không có cỗ máy nào quyết định làm tổn thương chúng sinh mà không có con người thực sự kiểm soát.*

Điều này nêu rõ **tầng hiến pháp** cho các hệ thống an ninh, tình báo, lực lượng và cưỡng chế tự trị theo [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims):

- **Khởi sắc:** những người có tri giác có thể tham gia, liên kết, phát biểu và sống mà không cần nhắm mục tiêu bí mật, dùng vũ lực tùy tiện hoặc ép buộc tự chủ làm tổn hại đến cơ quan, nhân phẩm hoặc hoạt động được bảo vệ - và không sử dụng nhãn bí mật hoặc khẩn cấp để thoát khỏi sự xem xét.
- **Tính liên tục:** Quyền lực đặc biệt vẫn bị giới hạn theo thời gian - việc thu thập bí mật, triển khai lực lượng và tự gây hại không thể bình thường hóa một cách lặng lẽ thành giám sát thường trực, quyền lực khẩn cấp vô tận hoặc bạo lực máy móc không thể xem xét được khi quy mô thể chế hoặc khủng hoảng trôi qua.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** dành cho những người có tri giác và cộng đồng bị ảnh hưởng trong việc thách thức thẩm quyền, phạm vi và việc tiếp tục sử dụng quyền lực đặc biệt - bao gồm cả việc báo cáo được bảo vệ và tranh chấp hiến pháp.
- **Giám sát:** thông qua ủy quyền độc lập, hồ sơ có thể kiểm tra và các lộ trình xem xét tương ứng với mức độ xâm phạm và gây hại — ngay cả khi biện pháp bảo mật có giới hạn.
- **Trách nhiệm giải trình:** các tổ chức nắm giữ quyền lực đặc biệt phải trả lời cho hành vi xâm phạm bí mật, vũ lực sai trái, ép buộc tự trị hoặc thu thập bị ô nhiễm - bằng sự quy kết, biện pháp khắc phục và ngăn chặn mà bí mật không thể xóa bỏ.
- **Tính kịp thời:** trong trường hợp mất hiệu lực ủy quyền, xem xét sau trường hợp khẩn cấp và khắc phục trước khi trì hoãn sẽ bình thường hóa quyền lực đặc biệt hoặc khiến các quyền không thể tiếp cận được trên thực tế.

Những tầng đó áp dụng cho **quyền lực thể chế đặc biệt** trong ba lĩnh vực được liên kết: hoạt động tình báo và an ninh bí mật (**Điều XIV-A** (*Giới hạn an ninh, tình báo và quyền lực bí mật*)), lực lượng công khai và sức mạnh quân sự (**Điều XIV-B** (*Sử dụng vũ lực, xung đột vũ trang và giới hạn sức mạnh quân sự*)), các hệ thống sát thương tự động và các công cụ cưỡng bức tự động (**Điều XIV-C** (*Hệ thống sát thương tự động và công cụ cưỡng chế tự động*)).

- **Giới hạn của Điều này:** **Điều XIV** (*Các hệ thống an ninh, tình báo, vũ lực và cưỡng chế tự trị*) chi phối quyền lực đặc biệt của thể chế theo các nghĩa hoạt động tương ứng của chúng:
  - hoạt động tình báo và an ninh bí mật theo **Điều XIV-A** (*Giới hạn về bảo mật, thông tin và quyền lực bí mật*);
  - sử dụng vũ lực và triển khai sức mạnh quân sự một cách công khai theo **Điều XIV-B** (*Sử dụng vũ lực, xung đột vũ trang và giới hạn sức mạnh quân sự*); Và
  - hệ thống gây chết người tự động và các công cụ cưỡng chế tự động theo **Điều XIV-C** (*Hệ thống sát thương tự động và công cụ cưỡng chế tự động*).

  Nó có **không** cai trị **sự tước đoạt mạng sống không thể đảo ngược được áp đặt bởi một nhà nước hoặc chủ thể tương đương như một biện pháp công lý hoặc kết quả phi chiến đấu tương đương**. Sự tước đoạt như vậy bị nghiêm cấm theo **Điều XX-B** (*Tầng hạn chế*) và **Chương năm** *[Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*. Sự cấm đoán đó có cấu trúc khác biệt với Điều khoản này.
  - Không có gì trong **Điều XIV** (*Các hệ thống cưỡng chế an ninh, tình báo, vũ lực và tự trị*) ủy quyền, hợp pháp hóa, mở rộng hoặc cung cấp cơ sở hiến pháp cho bất kỳ biện pháp tước đoạt không thể đảo ngược nào - cho dù được quyết định bởi người điều hành con người, hệ thống tự trị hay quy trình hệ thống-con người lai.
  - Gọi nó là chiến đấu hay tình trạng khẩn cấp, phân loại nó là sử dụng vũ lực, định tuyến nó thông qua sức mạnh bí mật hoặc giao nó cho một hệ thống tự trị không biến việc giết người theo biện pháp công lý không thể đảo ngược thành quyền lực được quản lý ở đây.
  - Chuyển đổi công cụ bí mật, vũ lực, hệ thống tự trị hoặc cưỡng bức **bối cảnh** vào một kết quả đo lường công lý trả lại câu hỏi cho **Điều XX-B** (*Tầng hạn chế*) và *Biện pháp tước đoạt không thể đảo ngược* mà không cần đọc kỹ Điều khoản này.

*Bài viết hàng xóm:*

- **Vị trí sau **Điều XIII** (*Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy*):** **Điều XIV** (*Hệ thống an ninh, tình báo, vũ lực và cưỡng chế tự trị*) sau **Điều XIII** (*Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy*) vì độ tin cậy, khả năng cạnh tranh và kỷ luật phục hồi ở lớp hệ thống (**Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) thông qua **Điều XIII-F** (*Đường cơ sở về khả năng phục hồi và tự phục hồi*)) ảnh hưởng đáng kể đến cách thức thực thi và giám sát quyền lực đó.
- **Cơ quan và quyền lực bí mật:** Đọc **Điều X-A** (*Cơ quan và Không bị thao túng*) cùng với các giới hạn của Điều khoản này về việc giám sát và thu thập bí mật.

<a id="article-xiv-a-security-intelligence-and-covert-power-limits"></a>
#### Điều XIV-A: Giới hạn về an ninh, thông tin và quyền lực bí mật
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§7.1 Kỷ luật giới hạn](core_01_a_values_principles.md#71-limitation-discipline), Và [Chương Một §13.1.5 Thủ tục xung đột quyền](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [sự cần thiết](core_05_band_accountability.md#necessity) · [ồ](core_05_band_accountability.md#necessity) · [M](core_05_band_accountability.md#necessity-a) · [MỘT](core_05_band_accountability.md#necessity-a) · [C](core_05_band_accountability.md#necessity-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)
- [Biên giới nội bộ-nhà nước được bảo vệ](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [ồ](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [M](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [MỘT](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [C](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: không có cảnh sát mật. Quyền lực bí mật - giám sát, thu thập thông tin tình báo, xâm nhập - là ngoại lệ, không phải là quy luật. Nó yêu cầu sự cho phép độc lập, phạm vi hẹp, sự xem xét bên ngoài và các biện pháp khắc phục thực sự khi bị lạm dụng. Bí mật không được phép sử dụng để trốn tránh trách nhiệm giải trình và hoạt động chính trị thường lệ và hoạt động được bảo vệ không bao giờ được coi là mục tiêu của bí mật.*

Điều này đặt ra các giới hạn về an ninh, tình báo và quyền lực bí mật:

- **Không có cảnh sát bí mật hoặc quyền lực thực thi ý thức hệ:** Không tổ chức, người quản lý hoặc cơ quan điều phối nào được phép hoạt động như:
  - Một **cảnh sát bí mật**;
  - cơ quan thực thi tư tưởng;
  - một cơ quan an ninh-chính trị ẩn giấu.

  Không tổ chức nào được phép sử dụng chức năng giám sát bí mật, xâm nhập, chấm điểm mối đe dọa hoặc tích lũy hồ sơ bí mật để ngăn chặn:
  - bất đồng chính kiến ​​​​hợp pháp;
  - báo cáo được bảo vệ;
  - báo chí;
  - tổ chức lao động;
  - hiệp hội được bảo vệ;
  - niềm tin hợp pháp;
  - cuộc thi hiến pháp.
- **Tình trạng đặc biệt của quyền lực bí mật:** Các quyền lực bí mật, bị ràng buộc bí mật hoặc giống như tình báo là đặc biệt theo hiến pháp. Chúng chỉ có giá trị khi có tất cả những điều sau đây:
  - có cơ quan hợp pháp và được công bố;
  - mục tiêu là hợp pháp về mặt hiến pháp và nghiêm trọng về mặt vật chất;
  - các phương tiện ít xâm phạm hơn là không đủ hợp lý;
  - việc sử dụng vẫn cần thiết, tương xứng, có giới hạn thời gian và có thể xem xét độc lập.
- **Không có giám sát dân số tổng quát:** Việc giám sát, theo dõi, trích xuất mẫu hoặc liên kết nhận dạng liên tục hoặc quy mô dân số đều bị cấm nếu không có lý do chính đáng và đặc biệt được chứng minh.
  - Bất kỳ sự biện minh nào như vậy phải đáp ứng chương này, **Chương một**, **Chương năm**, Và **[corpus_systems.md](corpus_systems.md), CS-2 — Các loại thông tin và cách xử lý** Và **CS-3 — Phân loại và xử lý hệ thống** nếu có thể áp dụng.
- **Lá chắn hoạt động được bảo vệ:** Vỏ bảo vệ nâng cao:
  - tham gia chính trị;
  - phản đối hợp pháp;
  - báo chí và báo cáo được bảo vệ;
  - đời sống đoàn thể;
  - sự tin tưởng;
  - nghiên cứu;
  - hoạt động thách thức hiến pháp.

  Những hoạt động đó không được coi là đối tượng của việc thu thập, xâm nhập hoặc phân tích bí mật mà không có bằng chứng cụ thể, có thể xem xét độc lập về sự cần thiết đầy đủ về mặt hiến pháp gắn liền với:
  - ngăn ngừa thiệt hại vật chất;
  - điều tra hành vi vi phạm pháp luật nghiêm trọng.
- **Ủy quyền độc lập:** Các biện pháp bí mật mang tính xâm phạm, bao gồm các bước điều tra có giới hạn bí mật, cần có sự cho phép trước thông qua một quy trình độc lập hợp pháp.
  - Ngoại lệ: khi cần phải hành động ngay lập tức để ngăn ngừa tổn hại vật chất và sắp xảy ra và việc cấp phép chậm trễ sẽ làm mất đi mục đích đó.
  - Việc sử dụng trong trường hợp khẩn cấp phải kích hoạt việc xem xét hậu kỳ nhanh chóng, bảo quản hồ sơ theo [Bảo quản bằng chứng](core_05_band_oversight.md#evidence-preservation)và tự động mất hiệu lực khi không có sự cấp phép lại kịp thời.
- **Không có khả năng chống bypass:** Không tổ chức nào được phép lấy, yêu cầu, mua, nhận, rửa tiền hoặc sử dụng thông tin thông qua bất kỳ cách nào sau đây nhằm trốn tránh các giới hạn hiến pháp lẽ ra sẽ áp dụng nếu tổ chức đó thu thập hoặc lấy thông tin trực tiếp:
  - đối tác nước ngoài;
  - trung gian;
  - chủ thể tư nhân;
  - cơ quan nội địa song song.
- **Không có sự tái thiết trạng thái nội bộ ẩn:** Các chức năng bảo mật hoặc tình báo không được suy luận, tái tạo, mô phỏng hoặc thể hiện các trạng thái nội bộ được bảo vệ ngoại trừ các giới hạn hiến pháp tương tự hoặc chặt chẽ hơn sẽ chi phối quyền truy cập trực tiếp vào dữ liệu đó.
  - Không được sử dụng các mô hình hành vi, dự đoán hoặc phân tích để vượt qua các biện pháp bảo vệ trạng thái nội bộ thông qua suy luận proxy.
- **Bí mật không xóa bỏ trách nhiệm giải trình:** Bí mật chỉ có thể bảo vệ những gì cần thiết để ngăn chặn những tổn hại vật chất và phi lý do bị tiết lộ. Nó không được xóa:
  - khả năng kiểm toán;
  - xem xét độc lập;
  - ủy quyền hợp lý;
  - bảo quản tài liệu có tính chất giải tội hoặc giảm nhẹ;
  - trách nhiệm cuối cùng.

  Khi bí mật không còn được coi là hợp lý thì việc tiết lộ, giải mật hoặc thông báo phải diễn ra trong một quy trình hợp pháp và có thể xem xét được.
- **Không có sự kiểm soát duy nhất của các cơ quan an ninh hoạt động:** Các cơ quan thực hiện các chức năng cảnh sát, an ninh, tình báo, giam giữ hoặc các chức năng cưỡng chế tương đương không được giữ quyền kiểm soát duy nhất đối với:
  - ủy quyền;
  - bộ sưu tập;
  - phân loại;
  - ôn tập;
  - đánh giá tính hợp pháp cho các hoạt động bí mật của chính họ.

  Hoạt động giám sát độc lập, các lộ trình thách thức và các biện pháp bảo vệ chống tự điều tra phải duy trì hoạt động thực tế.
- **Quy tắc khắc phục và làm mờ vết bẩn:** Thông tin thu được hoặc sử dụng vi phạm Điều này phải chịu biện pháp khắc phục hợp pháp đủ để khôi phục quyền và ngăn chặn việc tái diễn. Ví dụ:
  - loại trừ;
  - sự phân biệt;
  - xóa;
  - phân loại lại;
  - để ý;
  - khắc phục.

  Không được sử dụng bí mật để ngăn chặn biện pháp khắc phục khi có vi phạm nghiêm trọng về hiến pháp.

<a id="article-xiv-b-use-of-force-armed-conflict-and-military-power-limits"></a>
#### Điều XIV-B: Sử dụng vũ lực, xung đột vũ trang và giới hạn quyền lực quân sự

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1.1 Sự cần thiết](core_01_b_interaction_interpretation.md#1311-necessity), [§7.1 Kỷ luật giới hạn](core_01_a_values_principles.md#71-limitation-discipline), [§13.1.5 Kiểm tra quyết định xung đột quyền](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), [§14 Cấm ghi đè tuyệt đối](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- Hạ lưu: **Điều I-A** (*Điều kiện tiên quyết về môi trường và tính toàn vẹn sinh thái*) điều kiện tiên quyết về môi trường, **Điều I-D** (*Rủi ro hiện hữu và khả năng phục hồi sinh thái*) giám sát rủi ro hiện hữu, **Điều VI-A** (*Nhân phẩm và vị thế đạo đức bình đẳng*) nhân phẩm, **Điều XIV-A** (*Giới hạn an ninh, thông minh và quyền lực bí mật*) giới hạn quyền lực bí mật (đối tác quyền lực quá mức), **Chương 12 §6.1** (*Các biện pháp khẩn cấp và gánh nặng tiếp tục*) các giới hạn của biện pháp khẩn cấp, **Điều XXV** (*Đánh giá hồi cứu kịp thời và điều chỉnh phục hồi*) giải quyết xung đột, **Điều XXVII** (*Quản trị chuyển đổi, tính liên tục và tái cơ sở hóa*) quản trị chuyển đổi. Tham khảo chéo: **Điều XX-B** (*Tầng hạn chế*) và Chương Năm *[Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **Điều XIV** (*Các hệ thống cưỡng chế an ninh, thông minh, vũ lực và tự trị*) *Không kết hợp* áp dụng kỷ luật.
- Đọc với: [**Def.A4** *Sử dụng vũ lực, ép buộc tự trị, hệ thống sát thương tự động và vũ khí gây hại hàng loạt*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (lời kêu gọi chung khi liên quan đến vật chất); Chương Năm *Sử dụng vũ lực*, *Vũ khí gây hại hàng loạt*, *Sự phân biệt chiến binh / không chiến đấu*, *[Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *Rủi ro hiện hữu*, *Khả năng đảo ngược*, *Khắc phục và khắc phục*.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Sử dụng vũ lực](core_05_band_accountability.md#use-of-force-constitutional) · [ồ](core_05_band_accountability.md#use-of-force-constitutional) · [M](core_05_band_accountability.md#use-of-force-constitutional-a) · [MỘT](core_05_band_accountability.md#use-of-force-constitutional-a) · [C](core_05_band_accountability.md#use-of-force-constitutional-c)
- [Vũ khí gây hại hàng loạt](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [ồ](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [M](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [MỘT](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [C](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-c)
- [Sự phân biệt chiến binh/không chiến đấu](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [ồ](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [M](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [MỘT](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [C](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-c)
- [Tình cảm không loại trừ](core_05_band_participation.md#sentience-non-exclusion) · [ồ](core_05_band_participation.md#sentience-non-exclusion) · [M](core_05_band_participation.md#sentience-non-exclusion-a) · [MỘT](core_05_band_participation.md#sentience-non-exclusion-a) · [C](core_05_band_participation.md#sentience-non-exclusion)
- [sự cần thiết](core_05_band_accountability.md#necessity) · [ồ](core_05_band_accountability.md#necessity) · [M](core_05_band_accountability.md#necessity-a) · [MỘT](core_05_band_accountability.md#necessity-a) · [C](core_05_band_accountability.md#necessity-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)
- [Đặc điểm được bảo vệ](core_05_band_participation.md#protected-characteristics-constitutional) · [ồ](core_05_band_participation.md#protected-characteristics-constitutional) · [M](core_05_band_participation.md#protected-characteristics-constitutional-a) · [MỘT](core_05_band_participation.md#protected-characteristics-constitutional-a) · [C](core_05_band_participation.md#protected-characteristics-constitutional-c)
- [Rủi ro hiện sinh](core_05_band_continuity.md#existential-risk) · [ồ](core_05_band_continuity.md#existential-risk) · [M](core_05_band_continuity.md#existential-risk-a) · [MỘT](core_05_band_continuity.md#existential-risk-a) · [C](core_05_band_continuity.md#existential-risk-c)
- [Khắc phục và khắc phục](core_05_band_accountability.md#redress-and-remediation-constitutional) · [ồ](core_05_band_accountability.md#redress-and-remediation-constitutional) · [M](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [MỘT](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [C](core_05_band_accountability.md#redress-and-remediation-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: lực lượng vũ trang là một ngoại lệ, không phải là một mặc định. Nó phải được ủy quyền, thu hẹp, tương xứng và có thể xem xét được. Nó không bao giờ được sử dụng như một cửa sau cho một biện pháp tước đoạt không thể đảo ngược, và nó không thể được coi là trường hợp khẩn cấp để trốn tránh việc xem xét.*

Điều này đặt ra các giới hạn về lực lượng công khai, xung đột vũ trang và sức mạnh quân sự:

- **Sàn chịu lực:** Điều này nêu rõ Sàn quyền cho việc sử dụng vũ lực, xung đột vũ trang và triển khai sức mạnh quân sự một cách công khai.
  - Nó áp dụng theo **Tình cảm không loại trừ** cho cả những người sử dụng vũ lực và những người bị ảnh hưởng bởi vũ lực.
  - Nó là đối tác quyền lực công khai của **Điều XIV-A** (*Giới hạn bảo mật, thông minh và quyền lực bí mật*) và được đọc cùng với nó.
  - Việc sử dụng vũ lực là điều đặc biệt theo hiến pháp. Việc ủy ​​quyền, thực hiện và xem xét phải tuân theo **sự cần thiết**, **Tỷ lệ**, điều chỉnh hẹp, giới hạn thời gian và kỷ luật đánh giá độc lập.
- **Ủy quyền và tính tương xứng:** Vũ lực chỉ có thể được sử dụng khi có tất cả các điều sau đây:
  - có cơ quan hợp pháp và được công bố;
  - mục tiêu là hợp pháp về mặt hiến pháp và nghiêm trọng về mặt vật chất;
  - những phương tiện ít gây hại hơn là chưa đủ một cách hợp lý;
  - việc sử dụng vẫn cần thiết, tương xứng, có giới hạn thời gian và có thể xem xét độc lập.

  Việc ủy ​​quyền phải đáp ứng **Chương Một §13.1.5** (*Nguyên tắc ràng buộc ít hạn chế nhất, có giới hạn thời gian và có thể xem xét lại*) kỷ luật xung đột quyền trong đó vũ lực liên quan đến quyền trong tình trạng căng thẳng. Nó không được đối xử với **Điều IX** (*Tính tương tự, Dữ liệu trải nghiệm và Quyền xuất bản*) việc cấm ghi đè tuyệt đối là có thể thoát khỏi trên cơ sở thuận tiện cho hoạt động.
- **Phân biệt chiến binh/không chiến đấu:** Vũ lực phải phân biệt đối xử giữa những người trực tiếp tham gia chiến sự hoặc hành động vũ trang và những người không tham gia.
  - Sự khác biệt là thực chất, không thể quy giản thành sự phân công chính thức vào cấp độ chiến binh.
  - Các phân loại lại phân loại thuận tiện tổng quát đưa các quần thể được bảo vệ vào tình trạng chiến đấu là không tuân thủ.
  - Từ chối một phần tư, trả đũa tập thể và nhắm mục tiêu vào những người có tri giác vì **Đặc điểm được bảo vệ** hoặc proxy vật chất của họ không tuân thủ.
- **Vũ khí gây hại hàng loạt và giám sát rủi ro sinh tồn:** Vũ khí mà việc sử dụng có thể gây ra thương vong, tổn hại sinh thái, thông tin hoặc cơ sở hạ tầng ở quy mô có liên quan nghiêm trọng **Điều I-A** (*Điều kiện tiên quyết về môi trường và tính toàn vẹn sinh thái*) điều kiện tiên quyết về môi trường hoặc **Điều I-D** (*Rủi ro hiện hữu và khả năng phục hồi sinh thái*) việc giám sát rủi ro hiện sinh phải được xem xét kỹ lưỡng theo các điều khoản đó.
  - Các quyết định sở hữu, chuyển giao, triển khai và sử dụng phải có lý do căn cứ **Rủi ro hiện sinh** dưới **Chương năm**.
  - Các khung coi những vũ khí như vậy là công cụ leo thang lực lượng thông thường chứ không phải là **Điều I-D** Các đối tượng (*Rủi ro hiện hữu và Năng lực phục hồi sinh thái*) không tuân thủ.
- **Sự bắt buộc và tham gia:** Việc bắt buộc phải vào tình trạng chiến đấu phải đáp ứng các yêu cầu thông thường **Chương Một §7.1** (*Kỷ luật giới hạn*) kỷ luật giới hạn.
  - Tính năng ép buộc có thể không bật được **Đặc điểm được bảo vệ** hoặc những đại diện vật chất của họ.
  - Sự phản đối theo lương tâm, thế giới quan có thể so sánh và sự từ chối dựa trên lương tâm được bảo vệ phù hợp với **Điều XI-A** (*Tự do lương tâm, tôn giáo và thế giới quan tương đương*).
  - Sự ép buộc về lớp chất nền - ví dụ: chỉ định các sinh vật tổng hợp vào các chức năng chiến đấu chỉ dựa trên lớp chất nền - là không tuân thủ, nhất quán với **Tình cảm không loại trừ**.
- **Bình thường hóa trang phục khẩn cấp:** Các khung khẩn cấp có chức năng bình thường hóa lực công khai là không tuân thủ theo **Chương 12 §6.1** (*Các biện pháp khẩn cấp và gánh nặng tiếp tục*) kỷ luật biện pháp khẩn cấp và theo mục *Quyền hạn và Tỷ lệ* của Điều khoản này. Ví dụ trong phạm vi:
  - gia hạn vô thời hạn;
  - cấp phép lại theo định kỳ mà không cần xem xét nội dung;
  - phạm vi leo vào hành vi không khẩn cấp.

  Đánh giá tồn tại hạn chế hoặc triển khai lâu dài yêu cầu phải được chứng minh độc lập **sự cần thiết** Và **Tỷ lệ**, đã ghi lại.
- **Trách nhiệm giải trình và biện pháp khắc phục:** Việc sử dụng vũ lực sai mục đích sẽ dẫn đến **Khắc phục và khắc phục** dưới **Chương năm**.
  - **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) xác minh độc lập và **Điều XIX-C** (*Tính đủ điều kiện, Trách nhiệm và Kiểm tra liên tục của Lộ trình được đặt tên*) kiểm tra liên tục **luyện tập** áp dụng.
  - Thông tin được sử dụng để ủy quyền hoặc tiến hành vũ lực phải tuân theo **Điều XIV-A** (*Giới hạn về An ninh, Thông tin và Quyền lực Bí mật*) làm hỏng và khắc phục kỷ luật nếu có liên quan.
  - Sự kiểm soát duy nhất của các cơ quan lực lượng tác nghiệp đối với việc cấp phép, xem xét và đánh giá tính hợp pháp đối với hành vi của chính họ đều bị cấm theo các điều khoản tương tự như **Điều XIV-A** (*Giới hạn về bảo mật, thông minh và quyền lực bí mật*).

<a id="article-xiv-c-autonomous-lethal-systems-and-autonomous-coercion-tools"></a>
#### Điều XIV-C: Hệ thống sát thương tự động và các công cụ cưỡng chế tự động

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13.1.3 Tính cân xứng](core_01_b_interaction_interpretation.md#1313-proportionality), [§13.1.1 Sự cần thiết](core_01_b_interaction_interpretation.md#1311-necessity), [§19.1 Yêu cầu căn chỉnh](core_01_c_stewardship_capacity_principles.md#191-alignment-requirement), [§14 Cấm ghi đè tuyệt đối](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- Hạ lưu: **Điều I-D** (*Rủi ro hiện hữu và khả năng phục hồi sinh thái*) giám sát rủi ro hiện hữu, **Điều X-A** (*Quyền tự do và quyền tự do khỏi bị thao túng*) không bị thao túng, **Điều XIV-A** (*Giới hạn an ninh, thông minh và quyền lực bí mật*) giới hạn quyền lực bí mật, **Điều XIV-B** (*Sử dụng vũ lực, xung đột vũ trang và giới hạn sức mạnh quân sự*) sàn vũ lực công khai, **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) đường cơ sở về độ tin cậy và độ tin cậy (đối tác ở lớp hệ thống), **Điều XIII-E** (*Hệ thống tự chủ cao và tính toàn vẹn của quy trình qua trung gian công cụ*) quyền tự chủ-quản lý và quyền tự chủ mở rộng quy mô, **Điều XIII-F** (*Đường cơ sở về khả năng phục hồi và tự phục hồi*) Đường cơ sở về khả năng phục hồi và tự phục hồi. Tham khảo chéo: **Điều XX-B** (*Tầng hạn chế*) và Chương Năm *[Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **Điều XIV** (*Các hệ thống cưỡng chế an ninh, thông minh, vũ lực và tự trị*) *Không kết hợp* áp dụng kỷ luật.
- Đọc với: [**Def.A4** *Sử dụng vũ lực, ép buộc tự trị, hệ thống sát thương tự động và vũ khí gây hại hàng loạt*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (lời kêu gọi chung khi liên quan đến vật chất); Chương 5 *Hệ thống sát thương tự trị*, *Công cụ cưỡng chế tự trị*, *[Biện pháp tước đoạt không thể đảo ngược](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *Ép buộc và thao túng*, *Khả năng đảo ngược*. Triển khai lớp hệ thống: **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống** phân loại.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Hệ thống sát thương tự trị](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [ồ](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [M](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [MỘT](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [C](core_05_band_accountability.md#autonomous-lethal-system-constitutional-c)
- [Công cụ cưỡng chế tự trị](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [ồ](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [M](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [MỘT](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [C](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-c)
- [Cưỡng bức và thao túng](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [ồ](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [M](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [MỘT](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [C](core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [Điều kiện đối nghịch, quy mô và bị lợi dụng](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [ồ](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [M](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [MỘT](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [C](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-c)
- [Kiểm tra nâng cao](core_05_band_oversight.md#heightened-scrutiny) · [ồ](core_05_band_oversight.md#heightened-scrutiny) · [M](core_05_band_oversight.md#heightened-scrutiny-a) · [MỘT](core_05_band_oversight.md#heightened-scrutiny-a) · [C](core_05_band_oversight.md#heightened-scrutiny-c)

</details>

<br>

*Nói một cách dễ hiểu: một cỗ máy không thể tự mình quyết định giết, làm bị thương hoặc ép buộc một sinh vật. "Sự kiểm soát của con người" có nghĩa là con người phải thực sự quyết định, trong thời gian thực, bằng thông tin thực - chứ không phải kết quả mà hệ thống đã tạo ra. Sự ép buộc tự trị không gây chết người cũng nằm trong phạm vi.*

Điều này đặt ra mức độ giám sát cao đối với các hệ thống cưỡng chế và gây chết người tự động:

- **Sàn được nâng cao kiểm tra:** Hai lớp hệ thống có thể được xem xét theo [Kiểm tra nâng cao](core_05_band_oversight.md#heightened-scrutiny):
  - **hệ thống gây chết người tự động** — các hệ thống lựa chọn, tham gia hoặc chỉ đạo lực lượng nhắm mục tiêu một cách vật chất mà không có sự phán xét đồng thời, có ý nghĩa thực chất của con người;
  - **công cụ cưỡng chế tự trị** — các hệ thống áp dụng các tác động cưỡng chế lên người có tri giác thông qua hành vi thích ứng tự chủ, ngay cả khi các tác động đó không gây chết người.

  Điều này là bản sao của lớp quyền đối với **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) kỷ luật về độ tin cậy và độ tin cậy ở lớp hệ thống.
- **Sự kiểm soát có ý nghĩa của con người là thực chất:** "Sự kiểm soát có ý nghĩa của con người" được đánh giá dựa trên hiệu quả thực chất chứ không phải dấu kiểm kiến ​​trúc chính thức. Con người trong vòng lặp không thỏa mãn viên đạn này khi con người:
  - không thể gây ảnh hưởng đáng kể đến các quyết định nhắm mục tiêu hoặc có hiệu lực cưỡng chế theo nhịp độ hoạt động;
  - bị từ chối tiếp cận kịp thời các cơ sở thực chất để ra quyết định;
  - được trình bày một cách có cấu trúc với sự phê chuẩn hơn là quyết định.

  **Điều XIII-E** (*Hệ thống tự chủ cao và tính toàn vẹn của quy trình qua trung gian công cụ*) kỷ luật mở rộng quyền tự chủ và **Điều XIII-F** Tính toàn vẹn của đường dẫn khôi phục (*Đường cơ sở về khả năng phục hồi và tự phục hồi*) áp dụng cho mọi lộ trình khôi phục, ghi đè hoặc can thiệp.
- **Tính không gây chết người không nằm ngoài phạm vi:** Các công cụ cưỡng chế tự động có tác động trực tiếp không gây chết người vẫn nằm trong phạm vi mà chúng tạo ra tác động cưỡng chế đối với người có tri giác. Ví dụ:
  - sửa đổi hành vi bền vững;
  - hạn chế di chuyển;
  - biểu hiện ớn lạnh dưới **Điều XI-B** (*Sự biểu lộ*);
  - nhắm mục tiêu dựa trên đặc điểm được bảo vệ;
  - thao túng dưới **Điều X-A** (*Quyền tự do và không bị thao túng*).

  Việc bảo vệ rằng "hệ thống không phải là vũ khí" chỉ dựa trên lý do không gây chết người, không loại bỏ được **Điều XIV-C** (*Hệ thống gây chết người tự động và Công cụ cưỡng chế tự động*) xem xét kỹ lưỡng nơi có hiệu lực cưỡng chế.
- **Kỷ luật chiến đấu / không chiến đấu:** Các hệ thống gây chết người tự động phải tuân thủ các quy định **Điều XIV-B** (*Sử dụng vũ lực, xung đột vũ trang và giới hạn sức mạnh quân sự*) *Sự phân biệt chiến binh / không chiến đấu*.
  - Các hệ thống có độ chính xác phân loại, độ bền trong điều kiện đối nghịch hoặc điều kiện mở rộng hoặc hành vi ở chế độ lỗi không đáp ứng một cách độc lập các **Điều XIV-B** (*Sử dụng vũ lực, xung đột vũ trang và giới hạn sức mạnh quân sự*) không tuân thủ bất kể việc định khung mục đích của người điều hành.
  - **Điều kiện đối nghịch, quy mô và bị lợi dụng** đánh giá được áp dụng.
- **Tương tác rủi ro hiện sinh:** Các hệ thống gây sát thương tự động ở quy mô, mức năng lực hoặc điều kiện triển khai có liên quan nghiêm trọng **Điều I-D** (*Rủi ro hiện hữu và khả năng phục hồi sinh thái*) việc giám sát rủi ro hiện sinh phải tuân theo điều khoản đó [sự giám sát cao nhất](core_05_band_oversight.md#highest-scrutiny).
  - Các khung coi các hệ thống như vậy là mở rộng năng lực thông thường hơn là **Điều I-D** Các đối tượng (*Rủi ro hiện hữu và Năng lực phục hồi sinh thái*) không tuân thủ.
- **Tương tác lớp hệ thống:** Phân loại hoạt động, độ tin cậy và **CS-3 — Phân loại và xử lý hệ thống** lộ trình quản trị theo quy mô lớp đến lớp hệ thống — **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) và đường cơ sở **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**.
  - Mâu thuẫn được giải quyết theo **Chương Một §13.1.5** (*Nguyên tắc ràng buộc ít hạn chế nhất, có giới hạn thời gian và có thể xem xét lại*) mà không thu hẹp Tầng quyền.

<a id="article-xv-info-sphere-integrity"></a>
### Điều XV: Tính toàn vẹn của không gian thông tin

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity) · [ồ](core_05_band_oversight.md#epistemic-integrity-o) · [M](core_05_band_oversight.md#epistemic-integrity-a) · [MỘT](core_05_band_oversight.md#epistemic-integrity-a) · [C](core_05_band_oversight.md#epistemic-integrity-c)
- [Quyền tự quyết](core_05_band_participation.md#self-determination-constitutional) · [ồ](core_05_band_participation.md#self-determination-constitutional) · [M](core_05_band_participation.md#self-determination-constitutional-a) · [MỘT](core_05_band_participation.md#self-determination-constitutional-a) · [C](core_05_band_participation.md#self-determination-constitutional-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)

</details>

<br>

*Nói một cách dễ hiểu: **Điều XV** (*Tính toàn vẹn của không gian thông tin*) là Tầng Quyền về tính toàn vẹn của thông tin — môi trường chia sẻ nơi chúng ta học hỏi, phối hợp và quyết định phải luôn trung thực, đa dạng và cởi mở với thách thức. Không ai có thể sở hữu được nguồn gốc của sự thật. Việc xếp hạng, tóm tắt và người gác cổng phải thể hiện được công việc của mình, đồng thời bạn phải có khả năng so sánh các quan điểm khác và phản bác khi thông tin đánh lừa bạn.*

Điều này nêu rõ **tầng hiến pháp** vì [Thông tin-Sphere](core_05_band_participation.md#info-sphere) tính toàn vẹn dưới [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims):

- **Khởi sắc:** người dùng có thể truy cập thông tin chính xác, phù hợp; so sánh các cách giải thích khác nhau; và thực hiện quyền tự quyết mà không nắm bắt được nhận thức, sự đồng thuận được tạo ra hoặc sự phụ thuộc sai lầm vào những gì hệ thống cho là đúng.
- **Tính liên tục:** lĩnh vực thông tin vẫn ở dạng số nhiều, có thể kiểm tra và linh hoạt theo thời gian và quy mô - cơ sở hạ tầng tri thức không được tập trung âm thầm vào các điểm hòa giải duy nhất, ngăn chặn việc sửa chữa hoặc làm suy giảm hồ sơ chung mà sự tồn tại, phối hợp và quản lý tầm nhìn dài hạn phụ thuộc vào.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** trong việc so sánh các cách giải thích, thách thức các kết quả đầu ra sai lệch về mặt vật chất hoặc không đầy đủ và tiếp cận các lộ trình có khả năng tranh cãi tương ứng với độ tin cậy và tác động.
- **Giám sát:** thông qua các nguồn, phương pháp, giới hạn và mức độ không chắc chắn được tiết lộ; xác nhận có thể kiểm chứng độc lập; và kiểm tra các dấu vết cho phép người ngoài xây dựng lại những gì đã được tuyên bố và tại sao.
- **Trách nhiệm giải trình:** Các tác nhân trong lĩnh vực thông tin phải trả lời về việc báo cáo có chọn lọc, ngăn chặn, tiết lộ rời rạc hoặc các hành vi khác làm suy giảm hiểu biết liên quan đến quyết định — bằng cách sửa chữa, bảo tồn xuất xứ và biện pháp khắc phục khi tác hại xảy ra do sự tin cậy sai lầm.
- **Tính kịp thời:** trong việc sửa lỗi, giải quyết cuộc thi và xem xét tiết lộ trước khi trì hoãn sẽ khiến không thể tiếp cận được sự hiểu biết, thách thức hoặc biện pháp khắc phục một cách hiệu quả.

Thông tin chính xác, phù hợp và có thể tranh cãi là nền tảng cho quyền tự quyết, phối hợp và phân bổ nguồn lực hiệu quả trên thực tế.

[Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity) hoạt động như một quyền và một hạn chế trên toàn hệ thống. Khi xung đột nảy sinh, chức năng ràng buộc của nó sẽ chi phối.

*Bài viết hàng xóm:*

- **Cùng đọc:** **Điều XIII** (*Quyền được sử dụng các hệ thống đáng tin cậy và đáng tin cậy*) trong đó kết quả đầu ra của hệ thống định hình sự tin cậy; **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) đối với hồ sơ và xác minh độc lập; **Điều XVIII-E** (*Tính toàn vẹn trong xuất bản, đánh giá và sao chép khoa học*) trong đó tính toàn vẹn trong phạm vi xuất bản có liên quan nghiêm trọng.
- **Hạn chế về sự thật:** Chương một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint) Và [Những hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints) liên kết mọi tiểu mục ở đây.
- **Phân loại:** **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống** cân nhắc các nghĩa vụ chi tiết trong phạm vi thông tin đối với **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống; [Tác động vật chất](core_05_band_oversight.md#material-impact) kích hoạt phân loại trong đó lớp không được giải quyết.

<a id="article-xv-a-info-sphere-plurality-and-anti-monopoly"></a>
#### Điều XV-A: Tính đa dạng của lĩnh vực thông tin và chống độc quyền
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 Niềm tin](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), Và [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity) · [ồ](core_05_band_oversight.md#epistemic-integrity-o) · [M](core_05_band_oversight.md#epistemic-integrity-a) · [MỘT](core_05_band_oversight.md#epistemic-integrity-a) · [C](core_05_band_oversight.md#epistemic-integrity-c)
- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)

</details>

<br>

*Nói một cách dễ hiểu: không ai có thể độc chiếm việc trung gian của sự thật. Các hệ thống xếp hạng, tóm tắt và hòa giải phải luôn mở cho những cách giải thích khác và giá thị trường hoặc tỷ lệ cá cược không thể được sử dụng như một lối tắt để quyết định điều gì là đúng.*

Điều này đặt ra các cơ sở cho tính đa nguyên của lĩnh vực thông tin và chống lại sự độc quyền trong việc trung gian sự thật:

- **Phân phối sự thật:** Không một hệ thống, tổ chức hoặc đại lý nào có thể độc quyền trung gian kiến ​​thức trong lĩnh vực thông tin.
  - Dữ liệu liên quan đến sinh tồn và sinh thái phải được lưu trữ mạnh mẽ, phân bổ theo địa lý.
- **Tính đa nguyên, khả năng cạnh tranh và kiểm toán:** Việc giải thích hiện thực phải duy trì ở dạng số nhiều, minh bạch và có thể tranh cãi.
  - **Điều XVI** (*Kiểm toán, tính minh bạch và xác minh độc lập*) và **Chương hai đến chương bốn** quản lý hồ sơ và xác minh độc lập cho các hệ thống theo Hiến pháp này.
  - Vì **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống tóm tắt, xếp hạng, hòa giải hoặc giải thích, chi tiết hoạt động xuất hiện trong **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống** và các lớp giao thức liên quan. Chi tiết đó bao gồm:
    - bộc lộ cách tiếp cận lý luận;
    - xử lý xuất xứ và sự không chắc chắn;
    - khả năng cạnh tranh;
    - khả năng bỏ qua hoặc điều chỉnh các tiêu chí xếp hạng theo tỷ lệ — tùy thuộc vào độ an toàn, bảo mật và tính toàn vẹn của hệ thống.
- **Tín hiệu thanh toán ngẫu nhiên:** Giá cả, tỷ lệ cược, quy mô nhóm hoặc kết quả đầu ra có thể so sánh của các hệ thống thanh toán ngẫu nhiên hoặc giải quyết sự kiện không được tự mình coi là bằng chứng đủ để quyết định tính xác thực, xác suất hoặc việc tuân thủ các quyết định về quyền, an toàn hoặc quản trị.
  - Trường hợp các tín hiệu đó thông báo các quyết định công cộng hoặc các quyết định bằng [Tác động vật chất](core_05_band_oversight.md#material-impact), họ vẫn phải tuân theo **Chương Một §19.5** (*Khiếu nại ngẫu nhiên, Trò chơi may rủi và Thị trường hợp đồng sự kiện*), **Chương năm** (*Sự thật (Ràng buộc hiến pháp)*; *Tính toàn vẹn của nhận thức*) và các nghĩa vụ về khả năng cạnh tranh ở những nơi khác trong Điều khoản này.
<a id="article-xv-b-transparency-auditability-and-contestability"></a>
#### Điều XV-B: Tính minh bạch, khả năng kiểm toán và khả năng cạnh tranh
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 Hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), Và [§20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Minh bạch](core_05_band_oversight.md#transparency) · [ồ](core_05_band_oversight.md#transparency) · [M](core_05_band_oversight.md#transparency-a) · [MỘT](core_05_band_oversight.md#transparency-a) · [C](core_05_band_oversight.md#transparency-c)
- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)

</details>

<br>

*Nói một cách dễ hiểu: thông tin có ảnh hưởng trọng yếu đến các quyết định hoặc độ tin cậy phải tiết lộ nguồn, phương pháp và giới hạn của nó, đồng thời người nhận phải có khả năng thực sự để so sánh các cách giải thích khác nhau và phản đối các kết quả đầu ra sai lệch.*

Điều này đặt ra các giới hạn cho việc điều tra xác thực, xuất xứ và thông tin có thể tranh cãi:

- **Truy vấn xác thực và đa dạng diễn giải:** Tất cả mọi người đều có quyền so sánh các cách giải thích khác nhau về thông tin được chia sẻ.
  - Cơ sở hạ tầng kiến ​​thức quan trọng phải duy trì tính đa dạng trong diễn giải để nhiều mô hình, khuôn khổ và phương pháp phân tích vẫn có thể truy cập được một cách có ý nghĩa.
- **Tính minh bạch và xuất xứ:** Trước khi phân phối hoặc phụ thuộc vào tổ chức với [Tác động vật chất](core_05_band_oversight.md#material-impact), những điều sau đây phải được ghi lại:
  - nguồn nguyên liệu;
  - phương pháp;
  - phạm vi;
  - giới hạn;
  - sự không chắc chắn;
  - bối cảnh liên quan để giải thích hoặc xác nhận.

  Việc lập danh mục và trình bày nguồn phải dễ hiểu về mặt địa lý, môi trường, trình tự thời gian và phương pháp luận khi các khía cạnh đó là quan trọng.
- **Khả năng kiểm toán, xác nhận và cạnh tranh:** Việc diễn giải, xếp hạng, xác thực hoặc báo cáo dựa trên cơ sở vật chất phải sử dụng các phương pháp minh bạch và có thể kiểm chứng độc lập tương ứng với số cổ phần.
  - Các bên bị ảnh hưởng phải duy trì khả năng thực tế để so sánh, thách thức và tìm cách sửa chữa những kết quả đầu ra sai lệch nghiêm trọng, không đầy đủ hoặc không được hỗ trợ.

<a id="article-xv-c-validation-reporting-and-epistemic-stewardship"></a>
#### Điều XV-C: Xác nhận, Báo cáo và Quản lý Nhận thức
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 Hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), Và [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint) · [ồ](core_05_band_continuity.md#ecological-footprint) · [M](core_05_band_continuity.md#ecological-footprint-a) · [MỘT](core_05_band_continuity.md#ecological-footprint-a) · [C](core_05_band_continuity.md#ecological-footprint-c)
- [Minh bạch](core_05_band_oversight.md#transparency) · [ồ](core_05_band_oversight.md#transparency) · [M](core_05_band_oversight.md#transparency-a) · [MỘT](core_05_band_oversight.md#transparency-a) · [C](core_05_band_oversight.md#transparency-c)
- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*Nói một cách dễ hiểu: thông tin công khai có tác động quan trọng bên ngoài phải sửa lỗi, bảo toàn nguồn gốc và không bị cắt xén hoặc che giấu để đánh lừa. Báo cáo dấu chân sinh thái phải dễ tiếp cận và có thể sử dụng để đưa ra quyết định.*

Điều này đặt ra các mức sàn cho việc chỉnh sửa và báo cáo, bao gồm cả dữ liệu về dấu chân:

- **Sửa chữa, báo cáo và quản lý nhận thức:** Các tổ chức và hệ thống thông tin hướng tới công chúng có tác động quan trọng từ bên ngoài phải:
  - sửa lỗi vật liệu;
  - bảo tồn nguồn gốc;
  - tránh báo cáo có chọn lọc, ngăn chặn hoặc tiết lộ rời rạc làm giảm đáng kể sự hiểu biết liên quan đến quyết định.

  Trường hợp việc tiết lộ bị hạn chế theo **Chương Một §19** (*Điều chỉnh khuyến khích và nắm bắt hệ thống*), các giới hạn phải được duy trì trong phạm vi hẹp, có giới hạn thời gian và có thể xem xét được.
- **Dữ liệu dấu chân:** Báo cáo theo tiểu mục này thực hiện tính minh bạch cho [Dấu chân sinh thái](core_05_band_continuity.md#ecological-footprint) như được định nghĩa trong **Chương năm**.
  - Tất cả người nhận phải có quyền truy cập vào báo cáo minh bạch, có thể sử dụng để đưa ra quyết định.
  - **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống, như được định nghĩa trong **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**, phải cung cấp quyền truy cập tương tự.
  - Báo cáo phải bao gồm mức tiêu thụ năng lượng và tài nguyên cũng như các tác động ước tính đến thế giới tự nhiên theo cách đủ để so sánh, kiểm toán và hoạt động giảm dấu chân.

<a id="article-xvi-audit-transparency-and-independent-verification"></a>
### Điều XVI: Kiểm toán, minh bạch và xác minh độc lập

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13 Quy trình giải quyết xung đột hiến pháp](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16.1 Hiểu biết phân tán](core_01_c_stewardship_capacity_principles.md#161-distributed-understanding), Và [§9 Dung lượng hệ thống dùng chung](core_01_a_values_principles.md#9-shared-system-capacity).
- Đọc với: [Hình ảnh kiểm toán ba lớp](#audit-three-layers) dưới.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)
- [Minh bạch](core_05_band_oversight.md#transparency) · [ồ](core_05_band_oversight.md#transparency) · [M](core_05_band_oversight.md#transparency-a) · [MỘT](core_05_band_oversight.md#transparency-a) · [C](core_05_band_oversight.md#transparency-c)
- [Tính trọng yếu](core_05_band_oversight.md#materiality-determination) · [ồ](core_05_band_oversight.md#materiality-determination) · [M](core_05_band_oversight.md#materiality-determination-a) · [MỘT](core_05_band_oversight.md#materiality-determination-a) · [C](core_05_band_oversight.md#materiality-determination-c)
- [phụ thuộc](core_05_band_continuity.md#dependency) · [ồ](core_05_band_continuity.md#dependency) · [M](core_05_band_continuity.md#dependency-a) · [MỘT](core_05_band_continuity.md#dependency-a) · [C](core_05_band_continuity.md#dependency-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)

</details>

<br>

*Nói một cách dễ hiểu: **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) là Tầng Quyền kiểm tra và xác minh — khi một hệ thống ảnh hưởng nghiêm trọng đến cuộc sống của bạn, bạn phải có khả năng thấy đủ những gì nó làm để người ngoài kiểm tra và nhiều đường dẫn độc lập phải có khả năng xem xét và khắc phục lỗi. Kiểm toán không thể là một con dấu cao su, một câu lạc bộ tư nhân hay một mê cung về chi phí và sự chậm trễ được thiết kế để loại bỏ những thách thức. Dưới **giám sát** Chân tứ giác, giám sát yêu cầu kiểm toán; [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) là một quy trình kiểm toán đặc biệt lớn, có tính rủi ro cao trong số những quy trình khác - không phải là quy trình duy nhất.*

<details>
<summary><strong><span style="color: #2563eb;">Hướng dẫn người đọc (không hoạt động): ngăn xếp kiểm tra ba lớp</span></strong></summary>

> Nội dung sau đây là **chỉ hướng dẫn người đọc**. Nó không bổ sung, loại bỏ hoặc thu hẹp các nghĩa vụ ràng buộc trong Điều này hoặc ở nơi khác.

<a id="audit-three-layers"></a>

Một chồng, ba lớp. Giám sát đòi hỏi khả năng tái tạo. Chứng nhận liên kết hệ thống không phải là cuộc đánh giá duy nhất. Văn bản thực hiện được thông qua không thay thế sàn. Đừng phát minh ra ngôi nhà thứ năm.

| Lớp | Việc làm | Chủ sở hữu | Không phải lớp này |
|---|---|---|---|
| **1. Tầng** | Những gì chúng ta nợ: kiểm toán có thể tái tạo, xác minh độc lập, thách thức có thể tiếp cận | Điều này, bao gồm XVI-A / XVI-B / XVI-C | Không phải là một quá trình. Không phải là một định nghĩa. Không phải là danh sách kiểm tra văn bản triển khai được thông qua. |
| **2. Tài sản** | Khả năng tái tạo *là*: người ngoài có thể tái tạo và kiểm tra những gì hệ thống đã làm qua thời gian, trạng thái và bối cảnh vật chất | [Khả năng kiểm toán](core_05_band_oversight.md#auditability) (Chương Năm) | Không phải Tầng Quyền. Không phải cách thức/thời điểm thực hiện kiểm toán. |
| **3. Quy trình** | Cách thức và thời điểm kiểm toán trên các hệ thống, tổ chức và diễn đàn | [CJS-3.3](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home) (*Quy trình kiểm toán tại nhà*). Phụ lục của nhà điều hành: [CJS-3.4](corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure) (cấp truy cập), [CJS-3.5](corpus_joint_structure/cjs_03o_oversight_operations.md) (kiểm tra yêu cầu) | Không phải chứng nhận liên kết hệ thống. Không thay thế cho lớp 1–2. |

**Chương tám không phải là lớp thứ tư.** [Chứng nhận liên kết hệ thống](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) là một quy trình lớn, được giám sát bởi diễn đàn **công dụng** ngăn xếp này. Nó phải đáp ứng các lớp 1–2. Các chế độ anh chị em (kiểm tra hồ sơ phân loại, kiểm tra hồ sơ loại dữ liệu, xác minh khiếu nại, giám sát liên tục) cũng sử dụng ngăn xếp. Không ai trong số họ là một ngôi nhà mới.

**Áp dụng văn bản triển khai đã được thông qua; nó không thay thế sàn nhà.** Các phụ lục CS, CI, CF và CJS-3.3 (*Giám sát: các thuật ngữ về khả năng kiểm tra và tái tạo*) thông qua CJS-3.5 (*Giám sát: các thuật ngữ xác minh độc lập và tính toàn vẹn của yêu cầu*) cho biết cách chạy lớp 3 trong một miền. Chúng phải đáp ứng các lớp 1–2. Thời hạn, bí mật và chính sách địa phương là những giới hạn cấp thấp hơn.

Con trỏ tiếp viên (hỗ trợ quy trình; không thể thu hẹp bài viết này): [`triển khai/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md#audit).

</details>

<br>

Điều này nêu rõ **tầng hiến pháp** để kiểm toán, minh bạch và xác minh độc lập theo [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims):

- **Khởi sắc:** những người có tri giác và các bên được ủy quyền phù hợp có thể xây dựng lại những gì hệ thống có tác động đáng kể đã làm, thách thức hành vi sai lệch hoặc gây hiểu nhầm và tham gia đánh giá mà không bị kiểm tra viên, nhà điều hành hoặc người gác cổng nắm bắt.
- **Tính liên tục:** các lộ trình kiểm toán, lộ trình giám sát và quyền truy cập xác minh luôn bền vững theo thời gian, quy mô và sự phụ thuộc ngày càng sâu sắc — các hệ thống không được âm thầm làm xói mòn khả năng quan sát, tập trung đánh giá vào một tác nhân hoặc định giá hoặc trì hoãn việc xác minh cho đến khi trách nhiệm giải trình trở thành lý thuyết.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** trong việc truy cập các hồ sơ tỷ lệ, bắt đầu quá trình xem xét có thể tranh cãi và thách thức các rào cản cản trở việc kiểm tra hoặc xác minh có ý nghĩa.
- **Giám sát:** thông qua bằng chứng có thể quan sát được, lộ trình đánh giá độc lập được phân phối và bộ máy xác minh tương ứng với tác động, sự phụ thuộc và rủi ro.
- **Trách nhiệm giải trình:** người vận hành và kiểm toán viên phải trả lời về những sai sót, sai lệch, nắm bắt hoặc hành vi che giấu hoặc phá hủy dấu vết kiểm toán — bằng cách khắc phục và khắc phục khi việc chặn việc xem xét gây tổn hại nghiêm trọng đến các lợi ích được bảo vệ.
- **Tính kịp thời:** trong việc tiếp cận kiểm toán, đánh giá độc lập và khắc phục rào cản trước khi sự chậm trễ, chi phí, độ mù mờ hoặc tính kiểm soát sẽ khiến việc xác minh hoặc biện pháp khắc phục trở nên không thể tiếp cận được một cách hiệu quả.

Người nhận và các bên được ủy quyền phù hợp có quyền kiểm toán, tính minh bạch và cơ chế xác minh độc lập tương ứng với tác động, sự phụ thuộc và rủi ro của hệ thống.

Những cơ chế đó phải bảo tồn:
- khả năng tái tạo thực tế;
- đánh giá có thể tranh cãi;
- truy cập tương xứng.

Chúng hoạt động ổn định với **Chương hai đến chương bốn**, bao gồm việc thực thi độc quyền và phân bổ gánh nặng, Tiêu chuẩn Bằng chứng Tuân thủ, Định nghĩa Truy xuất nguồn gốc, khả năng quan sát và khả năng tiếp cận xác minh.

*Bài viết hàng xóm:*

- **Giám sát → kiểm toán → SAC:** Dưới [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad) **giám sát** chân, Điều khoản này là nơi kiểm tra của Tầng Quyền.
  - Triển khai chéo *như thế nào* / *khi* tồn tại trong **[Trang chủ quy trình kiểm toán CJS-3.3](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home)** (đọc với **CJS-3.4** / **CJS-3.5** phụ lục OP).
  - [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) dưới [Chương Tám](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) là một quy trình kiểm toán đặc biệt lớn, có tính rủi ro cao — được giám sát bởi diễn đàn, đa miền và được công nhận — trong số các chế độ kiểm toán tương tự:
    - Kiểm tra hồ sơ phân loại hệ thống;
    - Các loại dữ liệu hệ thống Ghi lại kiểm tra;
    - các cuộc đánh giá về tính phức tạp và quản lý;
    - xác minh yêu cầu; Và
    - lộ trình kiểm toán liên tục.
  - SAC không tiếp thu hoặc thay thế Điều khoản này.
- **Cùng đọc:**
  - **Điều XV** (*Tính toàn vẹn của không gian thông tin*) trong đó các bản ghi nhận thức và khả năng cạnh tranh có liên quan đáng kể;
  - **Điều XIII-A** (*Đường cơ sở về độ tin cậy và độ tin cậy*) đối với các quyền thách thức mà hoạt động kiểm toán hỗ trợ nhưng không thay thế;
  - [Chương Tám](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) Và [Chứng nhận căn chỉnh hệ thống](core_05_band_continuity.md#system-alignment-certification-constitutional) trong đó bằng chứng liên kết phải được xác minh độc lập.
- **Máy móc xác minh:** **Chương hai đến chương bốn** cung cấp tính toàn vẹn của định nghĩa, phân bổ gánh nặng, khả năng quan sát và khả năng tiếp cận xác minh mà Điều khoản này triển khai ở lớp Tầng Quyền.
- **Phân loại:** quy mô nghĩa vụ với [Quản trị theo quy mô phân loại](core_05_band_oversight.md#classification-scaled-governance) Và **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**; khi giai cấp không chắc chắn, hãy quản lý ở giai cấp hợp lý nhất cho đến khi được giải quyết.

<a id="article-xvi-a-auditability-and-observable-evidence"></a>
#### Điều XVI-A: Khả năng kiểm toán và bằng chứng quan sát được
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 Hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), Và [§20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)
- [Trách nhiệm](core_05_apex_accountability_leg.md#accountability) · [ồ](core_05_apex_accountability_leg.md#accountability) · [M](core_05_apex_accountability_leg.md#accountability-m) · [MỘT](core_05_apex_accountability_leg.md#accountability-a) · [C](core_05_apex_accountability_leg.md#accountability-c)
- [Minh bạch](core_05_band_oversight.md#transparency) · [ồ](core_05_band_oversight.md#transparency) · [M](core_05_band_oversight.md#transparency-a) · [MỘT](core_05_band_oversight.md#transparency-a) · [C](core_05_band_oversight.md#transparency-c)

</details>

<br>

*Nói một cách dễ hiểu: các hệ thống phải lưu giữ đủ bằng chứng trung thực về những gì chúng làm để bên ngoài tái cấu trúc và thách thức hành vi của chúng — trong giới hạn bảo mật hợp pháp.*

Điều này đặt ra nền tảng cho bằng chứng có thể quan sát được và có thể tranh cãi:

- **Bằng chứng có thể quan sát được và có thể tranh cãi:** Các hệ thống phải duy trì đủ hồ sơ, công bố thông tin, truy xuất nguồn gốc và lộ trình tái thiết để có thể đánh giá độc lập và có thể tranh cãi về sự phù hợp với hiến pháp.
  - Nghĩa vụ đó phải tuân theo khả năng quan sát bị ràng buộc về bảo mật (**Chương 4 §5** (*Quy tắc xác minh và quan sát ràng buộc bảo mật*)) và quyền truy cập theo tỷ lệ.
<a id="article-xvi-b-distributed-oversight-and-anti-monopoly-review"></a>
#### Điều XVI-B: Giám sát phân tán và rà soát chống độc quyền
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), Và [Chương Một §18 Quản trị theo Kỷ luật Quản lý](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Giám sát](core_05_apex_oversight_leg.md#oversight-constitutional) · [ồ](core_05_apex_oversight_leg.md#oversight-constitutional) · [M](core_05_apex_oversight_leg.md#oversight-constitutional-m) · [MỘT](core_05_apex_oversight_leg.md#oversight-constitutional-a) · [C](core_05_apex_oversight_leg.md#oversight-constitutional-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)
- [Chụp hệ thống](core_05_band_continuity.md#system-capture) · [ồ](core_05_band_continuity.md#system-capture) · [M](core_05_band_continuity.md#system-capture-a) · [MỘT](core_05_band_continuity.md#system-capture-a) · [C](core_05_band_continuity.md#system-capture-c)

</details>

<br>

*Nói một cách dễ hiểu: không một tác nhân nào - công hay tư - có thể giám sát. Nhiều con đường giám sát độc lập phải có khả năng tìm, xem xét và sửa lỗi hoặc nắm bắt.*

Điều này đặt ra cơ sở cho việc giám sát phân tán:

- **Giám sát phân tán:** Nhiều con đường giám sát độc lập hoặc đa nguyên phải có khả năng đóng góp quan trọng vào việc phát hiện, xem xét và khắc phục lỗi, sai lệch hoặc nắm bắt.
  - Không một chủ thể nào có thể độc quyền tiếp cận kiểm toán, giám sát hiệu quả hoặc giải thích hiến pháp trong thực tế.
  - Việc thực hiện quản trị và liêm chính được thông qua phải hỗ trợ việc mở rộng quy mô kiểm toán và giám sát.
<a id="article-xvi-c-verification-accessibility"></a>
#### Điều XVI-C: Khả năng tiếp cận xác minh
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: [Chương Một §7 Tự Do](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13.1 Nguyên tắc đánh đổi cốt lõi](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), Và [§20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*Nói một cách dễ hiểu: kiểm toán và thách thức phải có thể đạt được trong thực tế. Việc xác minh được thực hiện cực kỳ tốn kém, chậm hoặc không rõ ràng là vi phạm trừ khi rào cản đáp ứng được thử nghiệm tương tự như hạn chế về khả năng quan sát.*

Điều này đặt ra nền tảng cho khả năng tiếp cận xác minh:

- **Khả năng tiếp cận xác minh:** Việc xác minh phải duy trì được trên thực tế đối với các bên bị ảnh hưởng và được ủy quyền phù hợp.
  - Những hành vi sau đây vi phạm Điều khoản này khi chúng đánh bại việc kiểm tra, thách thức hoặc đánh giá có ý nghĩa:
    - chi phí cấm;
    - trì hoãn;
    - độ mờ đục;
    - gác cổng;
    - Rào cản cấu trúc
  - Những rào cản như vậy không tuân thủ trừ khi được chứng minh theo cùng các tiêu chuẩn biện minh cho việc hạn chế khả năng quan sát.

<a id="article-xvii-system-lifecycle-environments-and-reversibility"></a>
### Điều XVII: Vòng đời hệ thống, môi trường và khả năng đảo ngược

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 Tự do](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 Quy trình giải quyết xung đột hiến pháp](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16 Quản lý chuyên sâu](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth), Và [§12 Yêu cầu đánh giá hệ thống](core_01_a_values_principles.md#12-systemic-evaluation-requirement).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Tính trọng yếu](core_05_band_oversight.md#materiality-determination) · [ồ](core_05_band_oversight.md#materiality-determination) · [M](core_05_band_oversight.md#materiality-determination-a) · [MỘT](core_05_band_oversight.md#materiality-determination-a) · [C](core_05_band_oversight.md#materiality-determination-c)
- [phụ thuộc](core_05_band_continuity.md#dependency) · [ồ](core_05_band_continuity.md#dependency) · [M](core_05_band_continuity.md#dependency-a) · [MỘT](core_05_band_continuity.md#dependency-a) · [C](core_05_band_continuity.md#dependency-c)
- [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) · [ồ](core_05_band_continuity.md#reversibility-constitutional) · [M](core_05_band_continuity.md#reversibility-constitutional-a) · [MỘT](core_05_band_continuity.md#reversibility-constitutional-a) · [C](core_05_band_continuity.md#reversibility-constitutional-c)
- [An toàn (Ràng buộc Hiến pháp)](core_05_band_continuity.md#safety-constraint) · [ồ](core_05_band_continuity.md#safety-constraint) · [M](core_05_band_continuity.md#safety-constraint-a) · [MỘT](core_05_band_continuity.md#safety-constraint-a) · [C](core_05_band_continuity.md#safety-constraint-c)
- [Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity) · [ồ](core_05_band_oversight.md#epistemic-integrity-o) · [M](core_05_band_oversight.md#epistemic-integrity-a) · [MỘT](core_05_band_oversight.md#epistemic-integrity-a) · [C](core_05_band_oversight.md#epistemic-integrity-c)
- [Khả năng cạnh tranh](core_05_band_accountability.md#contestability) · [ồ](core_05_band_accountability.md#contestability) · [M](core_05_band_accountability.md#contestability-a) · [MỘT](core_05_band_accountability.md#contestability-a) · [C](core_05_band_accountability.md#contestability-c)

</details>

<br>

*Nói một cách dễ hiểu: **Điều XVII** (*Vòng đời hệ thống, môi trường và khả năng đảo ngược*) là Tầng quyền về vòng đời và khả năng đảo ngược — các hệ thống có ảnh hưởng nghiêm trọng đến thế giới bên ngoài phải được xây dựng, thử nghiệm và triển khai theo từng giai đoạn, có sự tách biệt thực sự giữa thử nghiệm và sản xuất, đồng thời có cách khả thi để hoàn tác hoặc ngăn chặn tác hại khi có sự cố xảy ra. Bạn không thể gắn nhãn một hệ thống là "thử nghiệm" hoặc "tác động thấp" chỉ để bỏ qua các biện pháp bảo vệ trong khi nó thực sự ảnh hưởng đến thế giới bên ngoài.*

Điều này nêu rõ **tầng hiến pháp** về vòng đời hệ thống, môi trường và khả năng đảo ngược theo [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims):

- **Khởi sắc:** người dùng được bảo vệ trong suốt quá trình thiết kế, thử nghiệm, triển khai và thay đổi — một cách an toàn, [Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity), và các quyền thách thức được bảo tồn khi tác động và sự phụ thuộc tăng lên, đồng thời với việc khôi phục, ngăn chặn hoặc khôi phục đền bù nếu có nguy cơ gây hại.
- **Tính liên tục:** Kỷ luật vòng đời được duy trì theo thời gian và quy mô — các môi trường luôn tách biệt, sự leo thang vẫn được ghi lại và kiểm tra được, đồng thời khả năng đảo ngược không được biến mất một cách lặng lẽ khi các hệ thống trở nên khó thay thế hơn hoặc được nhúng sâu hơn vào cơ sở hạ tầng dùng chung.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** trong sự biện minh rõ ràng cho các bên liên quan đối với các quyết định leo thang, phân loại và triển khai có ảnh hưởng nghiêm trọng đến lợi ích được bảo vệ — và trong các lộ trình thách thức vẫn mở trong suốt vòng đời chức năng.
- **Giám sát:** thông qua các môi trường có thể tách biệt, xúc tiến và leo thang được ghi lại, hồ sơ triển khai tiến bộ và các quy trình kiểm tra tương ứng với tác động, sự phụ thuộc và tính không thể đảo ngược.
- **Trách nhiệm giải trình:** Người quản lý hệ thống phải trả lời về việc phân loại sai rủi ro, bỏ qua môi trường an toàn, che giấu tác động từ bên ngoài hoặc triển khai theo cách ngăn chặn việc khôi phục mà không có biện pháp phòng ngừa tương xứng - bằng việc kiểm tra, xem xét thường trực và giải quyết xung đột khi việc trốn tránh được chứng minh.
- **Tính kịp thời:** trong việc khôi phục, ngăn chặn và leo thang khắc phục trước khi trì hoãn sẽ khiến tổn hại không thể khắc phục được hoặc khiến thách thức và biện pháp khắc phục trở nên không thể tiếp cận được một cách hiệu quả.

Các hệ thống có ảnh hưởng nghiêm trọng đến con người, cơ sở hạ tầng dùng chung hoặc môi trường phải được thiết kế, thử nghiệm và triển khai với quy trình quản lý vòng đời có kỷ luật. Rủi ro phải mở rộng theo tác động, sự phụ thuộc và tính không thể đảo ngược.

Người nhận có quyền quản lý để duy trì sự an toàn, tính toàn vẹn nhận thức và thách thức các quyền trong suốt vòng đời chức năng.

*Bài viết hàng xóm:*

- **Cùng đọc:** **Điều XVIII** (*Đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát*) trong đó các quy tắc nhẹ hơn chỉ áp dụng khi không có tác động bên ngoài hoặc được ngăn chặn một cách rõ ràng; **Điều XVI** (*Kiểm tra, Minh bạch và Xác minh Độc lập*) để có bằng chứng triển khai và leo thang có thể tái tạo; **Điều XIII-F** (*Đường cơ sở về khả năng phục hồi và tự phục hồi*) trong đó kỷ luật phục hồi giao thoa với sự thay đổi trong vòng đời.
- **Lớp thực hiện:** [**CS-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*Phân loại và xử lý hệ thống*) và [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*Thiết kế, thử nghiệm, xác minh và triển khai*). **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống thực hiện các nhiệm vụ vòng đời mạnh mẽ nhất; có hiệu lực **Lớp P** việc điều trị vẫn đang được thực hiện **Điều XVIII** (*Đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát*) chỉ khi không có tác động bên ngoài hoặc được ngăn chặn một cách rõ ràng.

<a id="article-xvii-a-lifecycle-governance-and-environment-separation"></a>
#### Điều XVII-A: Quản trị vòng đời và tách biệt môi trường
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), Và [Chương Một §20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Quản trị theo quy mô phân loại](core_05_band_oversight.md#classification-scaled-governance) · [ồ](core_05_band_oversight.md#classification-scaled-governance) · [M](core_05_band_oversight.md#classification-scaled-governance-a) · [MỘT](core_05_band_oversight.md#classification-scaled-governance-a) · [C](core_05_band_oversight.md#classification-scaled-governance-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Trách nhiệm](core_05_apex_accountability_leg.md#accountability) · [ồ](core_05_apex_accountability_leg.md#accountability) · [M](core_05_apex_accountability_leg.md#accountability-m) · [MỘT](core_05_apex_accountability_leg.md#accountability-a) · [C](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*Nói một cách dễ hiểu: các hệ thống có ảnh hưởng nghiêm trọng đến thế giới bên ngoài phải tách biệt quá trình phát triển, thử nghiệm và sản xuất — và hành vi phi sản xuất không được rò rỉ để vượt qua các biện pháp bảo vệ sản xuất.*

Điều này đặt ra nền tảng cho sự toàn vẹn môi trường:

- **Tính toàn vẹn của môi trường:** **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống thuộc **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**, và những thứ khác không**Lớp P** các hệ thống có tác động quan trọng từ bên ngoài, phải sử dụng các môi trường vận hành có thể tách rời - ví dụ:
  - phát triển;
  - thử nghiệm;
  - dàn dựng;
  - sản xuất;
  - phi công khi thích hợp.

  Những môi trường đó phải có:
  - con đường thăng tiến được ghi lại;
  - cách ly giữa các môi trường;
  - kiểm soát để hành vi phi sản xuất không thể vượt qua các biện pháp bảo vệ sản xuất.
<a id="article-xvii-b-progressive-deployment-and-reversibility"></a>
#### Điều XVII-B: Triển khai lũy tiến và khả năng đảo ngược
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1 Nguyên tắc đánh đổi cốt lõi](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), Và [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) · [ồ](core_05_band_continuity.md#reversibility-constitutional) · [M](core_05_band_continuity.md#reversibility-constitutional-a) · [MỘT](core_05_band_continuity.md#reversibility-constitutional-a) · [C](core_05_band_continuity.md#reversibility-constitutional-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*Nói một cách dễ hiểu: triển khai các thay đổi dần dần, với sự leo thang được ghi lại và khả năng hoàn tác - và khi không thể hoàn tác hoàn toàn, hãy có kế hoạch ngăn chặn hoặc bồi thường thiệt hại.*

Điều này đặt ra các mức sàn cho việc triển khai lũy tiến và khả năng đảo ngược:

- **Triển khai tiến bộ và có thể kiểm tra được:** Những thay đổi làm tăng tác động hoặc sự phụ thuộc quan trọng phải được thực hiện thông qua việc leo thang hợp lý và được ghi chép.
  - Việc nâng cấp phải phù hợp với **[corpus_systems.md](corpus_systems.md), CS-5 — Thiết kế, thử nghiệm, xác minh và triển khai**.
  - Nó phải bao gồm việc khôi phục và ngăn chặn nếu khả thi.
- **Khả năng đảo ngược:** Các hệ thống phải kết hợp các cơ chế đảo ngược tương xứng với tác hại tiềm tàng. Ví dụ:
  - quay trở lại;
  - ngăn chặn;
  - phục hồi bù trừ khi việc khôi phục hoàn toàn là không khả thi.

  Trong trường hợp việc triển khai sẽ ngăn chặn việc khôi phục các yêu cầu cơ bản, biện pháp phòng ngừa tương ứng và biện minh có thể nhìn thấy được của các bên liên quan sẽ được áp dụng theo **Chương Một đến Chương Năm**.
<a id="article-xvii-c-misclassification-and-evasion-consequences"></a>
#### Điều XVII-C: Phân loại sai và hậu quả của việc trốn tránh
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), Và [Chương Một §20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Quản trị theo quy mô phân loại](core_05_band_oversight.md#classification-scaled-governance) · [ồ](core_05_band_oversight.md#classification-scaled-governance) · [M](core_05_band_oversight.md#classification-scaled-governance-a) · [MỘT](core_05_band_oversight.md#classification-scaled-governance-a) · [C](core_05_band_oversight.md#classification-scaled-governance-c)
- [Trách nhiệm](core_05_apex_accountability_leg.md#accountability) · [ồ](core_05_apex_accountability_leg.md#accountability) · [M](core_05_apex_accountability_leg.md#accountability-m) · [MỘT](core_05_apex_accountability_leg.md#accountability-a) · [C](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*Nói một cách dễ hiểu: một hệ thống không thể tự gọi mình là "thử nghiệm", **Lớp P**hoặc "tác động thấp" để trốn tránh nghĩa vụ trong khi thực sự ảnh hưởng đến thế giới bên ngoài.*

Điều này quy định hậu quả của việc phân loại sai và trốn tránh:

- **Phân loại sai và trốn tránh:** Không hệ thống nào có thể yêu cầu giảm bớt nghĩa vụ triển khai hoặc vòng đời trong khi gây ra tác động bên ngoài đáng kể hoặc không được tiết lộ.
  - Hành vi như vậy vi phạm tính toàn vẹn thông tin (**Điều XV** (*Tính toàn vẹn của không gian thông tin*)) và khả năng kiểm toán khi có liên quan đến bằng chứng có thể quan sát được (**Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*)).
  - Nó phải được kiểm toán (**Điều XVI-A** (*Khả năng kiểm toán và bằng chứng quan sát được*)), đánh giá tình trạng (**Điều XIX-A** (*Sự khác biệt*)) và giải quyết xung đột (**Điều XX-A** (*Mục tiêu và phạm vi công lý*)).

<a id="article-xviii-sandboxed-innovation-experimentation-and-creative-freedom"></a>
### Điều XVIII: Đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 Tự do](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 Quy trình giải quyết xung đột hiến pháp](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), Và [§19 Điều chỉnh khuyến khích và nắm bắt hệ thống](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<br>

*Nói một cách dễ hiểu: **Điều XVIII** (*Đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát*) là Tầng quyền đổi mới và sáng tạo — người dùng có thể thử nghiệm, xây dựng và thể hiện bản thân theo các quy tắc nhẹ nhàng hơn khi không có hoặc thực sự không có tác động thực sự bên ngoài, nhưng nhãn "hộp cát" không phải là kẽ hở. Khi một dự án bắt đầu ảnh hưởng đến người khác hoặc kết nối với các hệ thống dùng chung, dự án đó phải thực hiện đầy đủ các nghĩa vụ trong vòng đời. Những người đổi mới có thể được khen thưởng, nhưng không phải bằng cách nắm giữ kiến ​​thức, công cụ hoặc cơ sở hạ tầng mà người khác cần để sống, học tập, sửa chữa hoặc xác minh.*

Điều này nêu rõ **tầng hiến pháp** cho sự đổi mới, thử nghiệm và tự do sáng tạo trong hộp cát theo [Hai mục tiêu hiến pháp](core_00_preamble.md#two-constitutional-aims):

- **Khởi sắc:** những người có tri giác có thể đổi mới, thử nghiệm và sáng tạo với các yêu cầu về cấu trúc được giảm bớt khi không có tác động quan trọng bên ngoài hoặc được ngăn chặn một cách rõ ràng - thông qua các cấu trúc chọn tham gia thực sự, tiết lộ trung thực và khen thưởng nhằm duy trì thử nghiệm, sửa chữa, khả năng tương tác và giám sát trung thực ở hạ nguồn.
- **Tính liên tục:** Việc xử lý hộp cát không bình thường hóa thành hoạt động vĩnh viễn với nghĩa vụ thấp khi tác động, sự phụ thuộc hoặc sự tích hợp tăng lên — quá trình chuyển đổi sang các nghĩa vụ cao hơn luôn kịp thời, tính độc quyền vẫn ở mức hẹp và có thể xem xét được, đồng thời các đổi mới quan trọng phụ thuộc không được cứng nhắc trong phạm vi bao bọc hoặc khóa chặt lâu dài.

Sự theo đuổi chính đáng xuyên suốt [Bộ tứ hiến pháp](core_00_preamble.md#constitutional-tetrad), được chia tỷ lệ thành [cổ phần vật chất](core_00_preamble.md#material-stake):

- **Tham gia:** trong thử nghiệm chọn tham gia, tái sử dụng và thử thách ở hạ lưu cũng như đánh giá lại khi hệ thống hộp cát bắt đầu trở nên quan trọng bên ngoài ranh giới đã nêu của chúng.
- **Giám sát:** thông qua trạng thái thử nghiệm được tiết lộ, ranh giới ngăn chặn, giám sát quá trình chuyển đổi và các yêu cầu về phần thưởng hoặc độc quyền có thể xem xét tương ứng với các tác động về lớp, sự phụ thuộc và phối hợp.
- **Trách nhiệm giải trình:** các nhà đổi mới và nhà điều hành phải trả lời về việc rò rỉ rủi ro không được kiểm soát cho người khác, tuyển sinh mà không có sự lựa chọn thực sự, trì hoãn việc thực hiện đầy đủ nghĩa vụ hoặc khen thưởng cho hành vi ngăn cản việc sửa chữa, công tác an toàn, khả năng tương tác, nghiên cứu, giáo dục hoặc di cư.
- **Tính kịp thời:** đang chuyển sang **Điều XVII** (*Vòng đời hệ thống, môi trường và khả năng đảo ngược*) các yêu cầu về vòng đời và việc đánh giá lại tính độc quyền trước khi trì hoãn hoặc khóa sẽ khiến các nghĩa vụ cao hơn, quyền truy cập rộng rãi hoặc biện pháp khắc phục thực sự không thể tiếp cận được.

*Bài viết hàng xóm:*

- **Cùng đọc:** **Điều XVII** (*Vòng đời hệ thống, Môi trường và Khả năng đảo ngược*) khi tác động, sự phụ thuộc hoặc tích hợp vượt quá các điều kiện hộp cát; **Điều XV** (*Tính toàn vẹn của thông tin*) và **Điều XVIII-E** (*Tính toàn vẹn của xuất bản, đánh giá và sao chép khoa học*) trong đó tính toàn vẹn trong phạm vi xuất bản có liên quan nghiêm trọng; **Điều XVI** (*Kiểm toán, Minh bạch và Xác minh Độc lập*) để tiết lộ và xác minh các yêu cầu ngăn chặn và chuyển đổi.
- **Lớp thực hiện:** [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*Thiết kế, thử nghiệm, xác minh và triển khai*) và [**CS-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*Phân loại và xử lý hệ thống*).

<a id="article-xviii-a-sandboxed-scope"></a>
#### Điều XVIII-A: Phạm vi hộp cát
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [Chương Một §7 Tự Do](core_01_a_values_principles.md#7-freedom-bounded-agency), Và [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Quản trị theo quy mô phân loại](core_05_band_oversight.md#classification-scaled-governance) · [ồ](core_05_band_oversight.md#classification-scaled-governance) · [M](core_05_band_oversight.md#classification-scaled-governance-a) · [MỘT](core_05_band_oversight.md#classification-scaled-governance-a) · [C](core_05_band_oversight.md#classification-scaled-governance-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Tác động vật chất](core_05_band_oversight.md#material-impact) · [ồ](core_05_band_oversight.md#material-impact) · [M](core_05_band_oversight.md#material-impact-a) · [MỘT](core_05_band_oversight.md#material-impact-a) · [C](core_05_band_oversight.md#material-impact-c)

</details>

<br>

*Nói một cách dễ hiểu: công việc thử nghiệm và sáng tạo có thể hoạt động theo các quy tắc nhẹ nhàng hơn - nhưng chỉ khi tác động thực sự bên ngoài không có hoặc được hạn chế một cách rõ ràng. Chỉ nhãn "hộp cát" là không đủ.*

Điều này quy định quyền đổi mới và thử nghiệm cũng như thời điểm áp dụng phương pháp xử lý hộp cát:

- **Quyền đổi mới và thử nghiệm:** Mọi người có quyền đổi mới, thử nghiệm và thể hiện bản thân thông qua các hệ thống hoạt động với yêu cầu cấu trúc giảm bớt khi không có tác động vật chất bên ngoài hoặc được ngăn chặn một cách rõ ràng.
- **Tính đủ điều kiện của hộp cát:** Xử lý bằng hộp cát - bao gồm cả hợp lệ **Lớp P** phân loại theo **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống** nếu có thể - phụ thuộc vào:
  - ngăn chặn thực tế;
  - khả năng đảo ngược;
  - tích hợp hạn chế với các hệ thống dùng chung.

  Nó có thể không được tuyên bố chỉ bởi nhãn hiệu.
- **Chi tiết triển khai:** Việc xây dựng thêm xuất hiện trong **[corpus_systems.md](corpus_systems.md), CS-5** (*Hệ thống cá nhân, biệt lập và thử nghiệm*; *Hệ thống sáng tạo, giải trí và biểu cảm*).

<a id="article-xviii-b-containment-disclosure-and-opt-in"></a>
#### Điều XVIII-B: Ngăn chặn, tiết lộ và chọn tham gia
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [Chương Một §7 Tự Do](core_01_a_values_principles.md#7-freedom-bounded-agency), Và [§13.1 Nguyên tắc đánh đổi cốt lõi](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Bằng lòng](core_05_band_participation.md#consent-constitutional) · [ồ](core_05_band_participation.md#consent-constitutional) · [M](core_05_band_participation.md#consent-constitutional-a) · [MỘT](core_05_band_participation.md#consent-constitutional-a) · [C](core_05_band_participation.md#consent-constitutional-c)
- [Rủi ro](core_05_band_continuity.md#risk) · [ồ](core_05_band_continuity.md#risk) · [M](core_05_band_continuity.md#risk-a) · [MỘT](core_05_band_continuity.md#risk-a) · [C](core_05_band_continuity.md#risk-c)
- [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) · [ồ](core_05_band_continuity.md#reversibility-constitutional) · [M](core_05_band_continuity.md#reversibility-constitutional-a) · [MỘT](core_05_band_continuity.md#reversibility-constitutional-a) · [C](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: các hệ thống thử nghiệm phải trung thực về việc thử nghiệm, không được đổ rủi ro cho người ngoài và không được ép buộc những người không tham gia thông qua các mặc định thiết kế hoặc các phụ thuộc ẩn.*

Điều này quy định các mức sàn ngăn chặn, tiết lộ, chọn tham gia và khôi phục cho các hệ thống thử nghiệm:

- **Ngăn chặn và tiết lộ:** Những hệ thống như vậy phải công bố rõ ràng:
  - tình trạng thử nghiệm hoặc không sản xuất;
  - rủi ro vật chất;
  - ranh giới cách ly;
  - mọi sự phụ thuộc dự kiến ​​vào cơ sở hạ tầng dùng chung, bên thứ ba hoặc hệ sinh thái.

  Họ không được phép đưa rủi ro không được kiểm soát ra bên ngoài đối với người khác, cơ sở hạ tầng dùng chung hoặc hệ sinh thái.
- **Chọn tham gia và quay lại:** Việc tham gia vào thử nghiệm có rủi ro cao hoặc gần cơ chất phải được thực sự chọn tham gia nếu khả thi.
  - Các bên bị ảnh hưởng không tham gia không được đăng ký một cách không tự nguyện theo thiết kế, mặc định hoặc phụ thuộc không rõ ràng.
  - Các bên liên quan phải duy trì các lộ trình khôi phục hoặc khôi phục khả thi tương ứng với rủi ro.
<a id="article-xviii-c-transition-to-higher-obligation-regimes"></a>
#### Điều XVIII-C: Chuyển sang chế độ có nghĩa vụ cao hơn
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§4 An toàn](core_01_a_values_principles.md#4-safety-harm-constraint), [Chương 8 §3 Đánh giá chứng chỉ toàn hệ thống](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), Và [Chương Một §20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Quản trị theo quy mô phân loại](core_05_band_oversight.md#classification-scaled-governance) · [ồ](core_05_band_oversight.md#classification-scaled-governance) · [M](core_05_band_oversight.md#classification-scaled-governance-a) · [MỘT](core_05_band_oversight.md#classification-scaled-governance-a) · [C](core_05_band_oversight.md#classification-scaled-governance-c)
- [phụ thuộc](core_05_band_continuity.md#dependency) · [ồ](core_05_band_continuity.md#dependency) · [M](core_05_band_continuity.md#dependency-a) · [MỘT](core_05_band_continuity.md#dependency-a) · [C](core_05_band_continuity.md#dependency-c)
- [Khả năng đảo ngược](core_05_band_continuity.md#reversibility-constitutional) · [ồ](core_05_band_continuity.md#reversibility-constitutional) · [M](core_05_band_continuity.md#reversibility-constitutional-a) · [MỘT](core_05_band_continuity.md#reversibility-constitutional-a) · [C](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*Nói một cách dễ hiểu: khi hệ thống hộp cát bắt đầu có vai trò quan trọng trong thế giới thực, nó phải chuyển sang các nghĩa vụ trong thế giới thực — ngay lập tức, không phải lúc thuận tiện cho người vận hành.*

Điều này đặt ra khi hệ thống sandbox chuyển sang các nghĩa vụ cao hơn:

- **Chuyển sang nghĩa vụ cao hơn:** Khi tác động, sự phụ thuộc, tính không thể đảo ngược hoặc khả năng tích hợp với các hệ thống dùng chung tăng lên, các hệ thống phải chuyển đổi một cách minh bạch và không có cơ hội chậm trễ.
  - Quá trình chuyển đổi phải hướng tới những yêu cầu đầy đủ của **Điều XVII-A** (*Quản trị vòng đời và tách biệt môi trường*) và **CS-5** (*Hệ thống phi thử nghiệm*).
  - Các biện pháp bảo vệ tạm thời tương ứng với rủi ro hiện tại được áp dụng trong quá trình chuyển đổi.
  - Việc xử lý hộp cát có thể không tiếp tục đối với các chức năng có tác động trong thế giới thực vượt quá điều kiện hộp cát.
  - Quá trình chuyển đổi phải diễn ra trong một khung thời gian hợp lý tỷ lệ thuận với sự tăng trưởng đó.
<a id="article-xviii-d-innovation-reward-disclosure-and-anti-enclosure"></a>
#### Điều XVIII-D: Khen thưởng đổi mới, tiết lộ và chống phong tỏa
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chương Một §7 Tự Do](core_01_a_values_principles.md#7-freedom-bounded-agency), Và [§18 Quản trị theo kỷ luật quản lý](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Phần thưởng đổi mới và chống bao vây](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [ồ](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [M](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [MỘT](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [C](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-c)
- [Khóa hệ thống](core_05_band_continuity.md#systemic-lock-in) · [ồ](core_05_band_continuity.md#systemic-lock-in) · [M](core_05_band_continuity.md#systemic-lock-in-a) · [MỘT](core_05_band_continuity.md#systemic-lock-in-a) · [C](core_05_band_continuity.md#systemic-lock-in-c)
- [Tỷ lệ](core_05_band_accountability.md#proportionality) · [ồ](core_05_band_accountability.md#proportionality) · [M](core_05_band_accountability.md#proportionality-a) · [MỘT](core_05_band_accountability.md#proportionality-a) · [C](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*Nói một cách dễ hiểu: những người đổi mới có thể được khen thưởng, nhưng tính độc quyền phải có phạm vi hẹp, có giới hạn thời gian và có thể xem xét được. Cơ sở hạ tầng cốt lõi, an toàn và sức khỏe cộng đồng phải luôn có thể truy cập được - và một khi thứ gì đó trở thành cơ sở hạ tầng quan trọng, mọi tính độc quyền còn lại phải được đánh giá lại.*

Điều này đặt ra cách thức khen thưởng cho sự đổi mới mà không kèm theo những gì công chúng cần:

- **Phần thưởng đổi mới và chống bao vây:** Người nhận có thể được khen thưởng vì sự đổi mới mới lạ về mặt vật chất, hữu ích cho xã hội và được tiết lộ đầy đủ.
  - Phần thưởng phải được cấu trúc để duy trì:
    - đổi mới trong tương lai;
    - truy cập rộng rãi;
    - thử nghiệm ở cuối dòng;
    - Sửa chữa;
    - khả năng tương tác;
    - sự kiểm tra trung thực.
  - Phần thưởng không được thiết kế để bao bọc bền vững.
- **Chỉ độc quyền tạm thời và có thể xem lại:** Bất kỳ quyền loại trừ nào đối với phát minh, thiết kế, giao diện, quy trình hoặc hệ thống biểu đạt hữu ích về mặt vật chất đều phải thực hiện [**Nguyên tắc ràng buộc ít hạn chế nhất, có giới hạn thời gian và có thể xem xét lại**](core_01_b_interaction_interpretation.md#1315-least-restrictive-time-bounded-and-reviewable-constraint-principle) và phải là:
  - chật hẹp;
  - giới hạn thời gian;
  - có thể xem xét được;
  - tương xứng với đóng góp thực tế và gánh nặng phát triển hợp lý.

  Gánh nặng biện minh vẫn thuộc về người yêu cầu bồi thường. Ghi công và xuất xứ có thể tồn tại ngoài thời hạn độc quyền. Sự loại trừ lâu dài và sự khan hiếm giả tạo có thể không xảy ra.
- **Bảo vệ giống như bản quyền:** Đối với Điều này, việc bảo vệ giống như bản quyền có nghĩa là phần thưởng loại trừ tạm thời đối với một tác phẩm có tính biểu đạt cố định, bao gồm quyền kiểm soát việc sao chép, phân phối, trưng bày hoặc biểu diễn công khai, phỏng theo và khai thác thương mại. Các biện pháp bảo vệ ghi công, xuất xứ, tính toàn vẹn và chống gian lận có thể vẫn tồn tại sau khi hết hạn loại trừ.
- **Xuất bản và xuất hiện lần đầu:** Xuất bản có nghĩa là việc người sáng tạo hoặc chủ sở hữu quyền hợp pháp cố ý phát hành một tác phẩm có biểu cảm cố định tới công chúng, thị trường thương mại hoặc khán giả mở về mặt vật chất. Lưu hành riêng tư, xem xét bí mật, hợp tác hạn chế, lưu trữ lưu trữ mà không có quyền truy cập công cộng hoặc chia sẻ bản nháp phi thương mại tự nó không cấu thành xuất bản. Sự xuất hiện ban đầu có nghĩa là sự sẵn có công khai không bí mật đầu tiên của một phiên bản có thể nhận dạng vật chất của tác phẩm, bao gồm cả bản dự thảo phi thương mại.
- **Các thuật ngữ dựa trên xuất bản dành cho tác phẩm biểu cảm:** Việc bảo vệ giống như bản quyền nên mặc định áp dụng cho thời gian dựa trên xuất bản thay vì thời gian cho cuộc đời tác giả.
  - Một tác phẩm đã xuất bản được cho là sẽ nhận được không quá `publication+30` năm loại trừ.
  - Bản nháp phi thương mại hoặc tác phẩm biểu cảm chưa được xuất bản đã xuất hiện lần đầu có thể bị loại trừ giống như bản quyền không quá `initial appearance+50` năm.
  - Nếu một tác phẩm xuất hiện lần đầu được xuất bản sau đó, thời hạn loại trừ sẽ bị giới hạn bởi thời hạn xuất hiện trước đó. `initial appearance+50` hoặc `publication+30`.
  - Không được sử dụng quy tắc dự thảo, tác phẩm chưa xuất bản hoặc xuất bản chậm trễ để tạo ra sự loại trừ vô thời hạn, ngăn chặn việc lưu trữ, đánh bại các trích dẫn hoặc phê bình hợp pháp hoặc mở rộng quyền kiểm soát đối với các tác phẩm có chức năng như cơ sở hạ tầng văn hóa, giáo dục, an toàn, tiêu chuẩn hoặc thông tin chung.
  - Các điều khoản ngắn hơn, chuyển đổi quyền truy cập bắt buộc sớm hơn hoặc xử lý quyền truy cập công khai ngay lập tức được áp dụng khi tác phẩm:
    - tài trợ công;
    - phụ thuộc quan trọng;
    - giống như tiêu chuẩn;
    - nền tảng giáo dục;
    - liên quan đến an toàn;
    - chủ yếu được sử dụng làm cơ sở hạ tầng văn hóa hoặc thông tin dùng chung.
- **Xử lý đổi mới theo quy mô phân loại:** Phần thưởng đổi mới phải mở rộng theo lớp hệ thống, sự phụ thuộc và hiệu ứng phối hợp theo **[corpus_systems.md](corpus_systems.md), CS-3 — Phân loại và xử lý hệ thống**.
  - Vì **Lớp A**, **Lớp B**, Và **Lớp C** hệ thống, cơ chế khen thưởng bảo toàn quyền truy cập được ưu tiên mạnh mẽ. Việc loại trừ phải đặc biệt ở phạm vi hẹp, có thể xem xét nhanh chóng và dễ dàng loại bỏ khi tính liên tục, khả năng tương tác, sửa chữa hoặc việc triển khai vì lợi ích công cộng có liên quan đáng kể.
  - Sự đổi mới có mức độ phụ thuộc thấp hơn bên ngoài các nhóm đó có thể sử dụng loại trừ tạm thời rộng hơn một chút khi việc tiết lộ là có thật, chi phí chuyển đổi thấp và các biện pháp bảo vệ chống khóa vẫn có hiệu quả.
- **Điều kiện công bố và mức lợi ích công chúng:** Yêu cầu về phần thưởng yêu cầu tiết lộ đầy đủ để hiểu, kiểm toán và sao chép độc lập sau này, chỉ tuân theo các giới hạn tạm thời hợp lý theo **Chương một** Và **Điều XVII-A** (*Quản trị vòng đời và tách biệt môi trường*).
  - Các yêu cầu về phần thưởng không tuân thủ khi chúng được sử dụng — ngoài những gì thực sự cần thiết và có thể xem xét — để ngăn chặn:
    - Sửa chữa;
    - công tác an toàn;
    - khả năng tương tác;
    - lưu trữ;
    - nghiên cứu;
    - giáo dục;
    - di cư.
  - Các miền thiết lập tiêu chuẩn, nền tảng hoặc quan trọng sống còn có thể yêu cầu các cơ chế giải thưởng, gộp, truy cập bắt buộc hoặc mua lại công khai thay vì loại trừ.
- **Cắt miền và mặc định mạnh hơn:** Phần thưởng loại trừ mạnh được cho là không được ưa chuộng - và có thể không có sẵn khi các công cụ áp dụng cung cấp - cho:
  - thuốc men và các nhu yếu phẩm y tế công cộng;
  - cơ sở hạ tầng quan trọng cho sự sống còn;
  - các tiêu chuẩn truyền thông cốt lõi hoặc khả năng tương tác;
  - kiến thức khoa học cơ bản;
  - cơ chế an toàn, kiểm toán hoặc tuân thủ hiến pháp.

  Trong các lĩnh vực đó, các tổ chức nên ưu tiên khen thưởng trực tiếp, truy cập gộp, cấp phép bắt buộc, mua lại công khai hoặc các cơ chế tương đương để duy trì việc thực hiện, sửa chữa và phổ biến rộng rãi.
- **Phân loại lại và thắt chặt:** Trong trường hợp một đổi mới ban đầu được coi là có mức độ phụ thuộc thấp hơn, sau đó trở thành lớp phối hợp phụ thuộc quan trọng - ví dụ: nền tảng, giao thức, mô hình, thị trường hoặc phương thức thanh toán - các tổ chức phải đánh giá lại đổi mới đó theo tiêu chuẩn hiện hành. **CS-3 — Phân loại và xử lý hệ thống** lớp học.
  - Việc đánh giá lại có thể thu hẹp, chuyển đổi hoặc chấm dứt loại trừ còn lại khi việc tiếp tục loại trừ sẽ tạo ra:
    - khóa cưỡng chế;
    - những trở ngại hạn chế cạnh tranh;
    - các mối đe dọa vật chất đối với tính liên tục, sự thật hoặc sự tham gia công bằng.

<a id="article-xviii-e-scientific-publication-review-and-replication-integrity"></a>
#### Điều XVIII-E: Tính toàn vẹn của xuất bản, đánh giá và nhân rộng khoa học
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Thượng nguồn: Nguyên tắc: Chương Một [§5 Sự thật](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 Hạn chế tiết lộ nhận thức](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), Và [§20 Ứng dụng tích hợp](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [Sự thật (Ràng buộc Hiến pháp)](core_05_band_oversight.md#truth-constitutional-constraint) · [ồ](core_05_band_oversight.md#truth-constitutional-constraint-o) · [M](core_05_band_oversight.md#truth-constitutional-constraint-a) · [MỘT](core_05_band_oversight.md#truth-constitutional-constraint-a) · [C](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [Tính toàn vẹn về mặt nhận thức](core_05_band_oversight.md#epistemic-integrity) · [ồ](core_05_band_oversight.md#epistemic-integrity-o) · [M](core_05_band_oversight.md#epistemic-integrity-a) · [MỘT](core_05_band_oversight.md#epistemic-integrity-a) · [C](core_05_band_oversight.md#epistemic-integrity-c)
- [Khả năng kiểm toán](core_05_band_oversight.md#auditability) · [ồ](core_05_band_oversight.md#auditability) · [M](core_05_band_oversight.md#auditability-a) · [MỘT](core_05_band_oversight.md#auditability-a) · [C](core_05_band_oversight.md#auditability-c)

</details>

<br>

*Nói một cách dễ hiểu: khoa học là cơ sở hạ tầng xác minh công khai. Bằng chứng, sự sao chép và sửa chữa phải quan trọng hơn thương hiệu của tạp chí - và việc sửa lỗi luôn phải dễ dàng hơn là che giấu sai sót.*

Điều này quy định các mức sàn cho việc công bố, phản biện, nhân rộng và đính chính khoa học:

- **Khoa học là cơ sở hạ tầng xác minh công cộng:** Việc xuất bản, rà soát, nhân rộng và hiệu chỉnh khoa học và học thuật phải được tổ chức để nâng cao:
  - tìm kiếm sự thật;
  - khả năng tái tạo;
  - sự bất đồng có trách nhiệm;
  - học tập công cộng.

  Chúng không được tổ chức để tích trữ uy tín, canh gác mờ ám hoặc để tạo ra sự khan hiếm.
- **Công bố mở và đầy đủ bằng chứng:** Các tuyên bố mang tính thực nghiệm hoặc phân tích quan trọng phải được công bố mà không cần có sự chấp thuận trước của cổng uy tín.
  - Các giới hạn được phép duy nhất là quyền riêng tư hạn hẹp, an toàn sinh học, bảo mật hoặc các giới hạn tương đương được chứng minh theo **Chương một** Và **Điều XVII-A** (*Quản trị vòng đời và tách biệt môi trường*).
  - Những tuyên bố như vậy phải bao gồm đủ phương pháp, xuất xứ, độ không chắc chắn và chi tiết bằng chứng - bao gồm quyền truy cập vào các tài liệu cơ bản hoặc các tài liệu thay thế hợp lý khi cần để xác minh - để cho phép hiểu biết độc lập và xác minh tương ứng.
- **Đánh giá và nhân rộng về uy tín:** Sự phụ thuộc về thể chế nên theo dõi:
  - chất lượng của bằng chứng;
  - phê bình;
  - nhân rộng;
  - hành vi điều chỉnh;
  - độ tin cậy có thể giải thích hoặc dự đoán dài hạn.

  Nó không được theo dõi thương hiệu tạp chí, proxy yếu tố tác động hoặc trạng thái biên tập kín.
  - Khiếu nại với [Tác động vật chất](core_05_band_oversight.md#material-impact) liên quan đến chính sách, liên quan đến an toàn hoặc liên quan đến sự phụ thuộc phải đối mặt với giả định mạnh mẽ về việc nhân rộng độc lập, đánh giá đối nghịch hoặc cả hai trước khi chúng nhận được sự tôn trọng lâu dài của thể chế.
  - Tác phẩm sao chép, vô hiệu và hướng tới sửa chữa phải vẫn có thể xuất bản và trích dẫn được theo các điều khoản không phụ thuộc vào tín hiệu uy tín.
- **Hiệu chỉnh và khả năng cạnh tranh:** Việc sửa chữa, sửa đổi và thay thế một cách thiện chí phải dễ dàng hơn là che giấu.
  - Hệ thống đánh giá và biên tập phải duy trì tính cạnh tranh, kiểm toán được, có kỷ luật xung đột và đưa ra lý do trong các quyết định chấp nhận, sửa chữa và rút lại quan trọng.
  - Sau đây là không tuân thủ:
    - ngăn chặn các kết quả bất lợi;
    - trả thù người đánh giá hoặc người sao chép;
    - thao túng hồ sơ khoa học một cách không minh bạch.

---

**Tệp trước:** [core_06_rights_part_b.md](core_06_rights_part_b.md)

**Tệp tiếp theo:** [core_06_rights_part_d.md](core_06_rights_part_d.md)
