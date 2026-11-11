<!-- AI-assisted translation draft; unreviewed. Complete current-source Chapter Nine Part C §§8–11. Source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="chapter-nine-part-c-certification-record-recertification-and-standing"></a>

# CHAPTER NINE, PART C: SYSTEM ALIGNMENT CERTIFICATION — RECORD, RECERTIFICATION, AND STANDING

<a id="8-system-certification-record"></a>

### 8. Hồ sơ chứng nhận hệ thống

<details>
<summary><strong>Truy vết</strong></summary>

- Thượng nguồn:
  - [Phần B §6](core_09.005_system_alignment_certification_record_process.md#6-quy-trình-diễn-đàn) (*các phát hiện của thành phần diễn đàn được tích hợp vào Hồ sơ Chứng nhận Hệ thống*);
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận) (*kết quả và các quan ngại được nêu khi đi đến kết quả*);
  - [Phần A §1](core_09.000_system_alignment_certification_evaluation.md#1-mục-đích-và-vai-trò) (9.000 §1) (*mục đích chứng nhận và tổng quan quy trình*);
  - [Phần A §2](core_09.000_system_alignment_certification_evaluation.md#2-đánh-giá-lớp-hệ-thống) (*Đánh giá Phân loại Hệ thống*) (9.000 §2) đến
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-đánh-giá-sàn-quyền-và-lĩnh-vực) (*các đầu ra đánh giá được phản ánh trong Hồ sơ Chứng nhận Hệ thống*);
  - [Chương Hai đến Chương Bốn](../../core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*nền tảng về định nghĩa, gánh nặng, truy vết và xác minh*);
  - [Hồ sơ Chứng nhận Hệ thống](../../core_05.040_band_continuity.md#system-certification-record) (*ý nghĩa tại Chương Năm*);
  - [Hồ sơ Hành vi Ràng buộc Về Thực chất](../../core_05.035_band_accountability.md#materially-binding-act-record);
  - [Tính toàn vẹn của hồ sơ](../../core_05.035_band_accountability.md#record-integrity) (*quy tắc độ tin cậy áp dụng cho Hồ sơ Chứng nhận Hệ thống*);
  - [Chương Tám §8 Hồ sơ Hành vi và Chuyển giao có thể quy thuộc](../../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); họ đo lường giám sát về sự thật và tính toàn vẹn nhận thức như một phép đo hiến định;
  - [**Def.O1** *Điều XVI: Kiểm toán, Minh bạch và Xác minh Độc lập*](../../core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- Hạ nguồn: [§9](#9-tái-chứng-nhận-và-mở-lại) (*tái chứng nhận và mở lại*); [§11.3](#113-cổng-đầu-vào-đã-xác-minh-một-hồ-sơ-chứng-nhận-chỉ-được-nuôi-quỹ-đạo-chương-tám-khi-nó-có-giới-hạn-truy-vết-được-tranh-biện-được-và-đã-xác-minh-dưới) (*cổng đầu vào đã xác minh*); [Chương Mười lăm §2.3](../../core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*hồ sơ vụ việc của diễn đàn và tranh chấp hồ sơ tư cách*) (15.000 §2.3).
- Đọc cùng:
  - [Điều XVI: Kiểm toán, Minh bạch và Xác minh Độc lập](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Bảo toàn Chứng cứ](../../core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Các loại thông tin và xử lý*) và [CS-6.310 — Phân loại dữ liệu](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](../../corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*Cơ chế phân loại hệ thống*) và [CS-9.310 — Phân loại tác động hệ thống](../../corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*Vòng đời hệ thống*);
  - **CJS-5.110 §4** (*các mức minh bạch và điều kiện truy cập kiểm toán*).
- Các tiểu mục:
  - [§8.1](#81-nội-dung-hồ-sơ-tối-thiểu) (*Nội dung hồ sơ tối thiểu*), cùng với
  - [§8.1.1](#811-nhận-dạng-hệ-thống-phạm-vi-và-hồ-sơ-chứng-nhận-hệ-thống-trước-đó) (*Nhận dạng, phạm vi và hồ sơ trước đó*);
  - [§8.1.2](#812-phân-loại-và-kết-luận-toàn-hệ-thống) (*Phân loại và phát hiện toàn hệ thống*);
  - [§8.1.3](#813-hồ-sơ-loại-dữ-liệu-hệ-thống) (*Hồ sơ Loại Dữ liệu Hệ thống*);
  - [§8.1.4](#814-kết-luận-về-sàn-quyền-và-lĩnh-vực) (*Nền tảng Quyền và phát hiện theo lĩnh vực*);
  - [§8.1.5](#815-bằng-chứng-kỹ-thuật-và-kết-luận-xem-xét) (*Bằng chứng kỹ thuật và phát hiện rà soát*);
  - [§8.1.6](#816-giám-sát-độc-lập-và-con-đường-khiếu-nại) (*Giám sát, độc lập và đường khiếu nại*);
  - [§8.1.7](#817-quan-ngại-nguyên-nhân-và-mức-sẵn-sàng-khắc-phục) (*Quan ngại, nguyên nhân và mức sẵn sàng khắc phục*);
  - [§8.1.8](#818-kết-quả-và-giới-hạn-dựa-vào) (*Kết quả và giới hạn phụ thuộc*);
  - [§8.1.9](#819-kế-hoạch-vận-hành) (*Kế hoạch vận hành*); và
  - [§8.1.10](#8110-tính-đầy-đủ) (*Tính đầy đủ*);
  - [§8.2](#82-tính-minh-bạch-và-khả-năng-kiểm-toán-của-hồ-sơ-chứng-nhận-hệ-thống) (*Tính minh bạch và khả năng kiểm toán của Hồ sơ Chứng nhận Hệ thống*).

</details>


*Nói thẳng: hồ sơ chứng nhận là hồ sơ vụ kiểm được của một hệ thống đang rà — ai vận hành, đã kiểm gì, tìm thấy gì, quyết gì, và cách tranh biện. Nó không phải gói quảng cáo hay con dấu duyệt một dòng. Độ sâu hồ sơ, công bố, và gánh tranh biện chia tỷ lệ theo lớp hệ thống dưới [§2.1](core_07_a_system_alignment_certification_evaluation.md) — hệ thống sống còn **Class A** đòi hồ sơ đầy hơn, tranh biện được hơn một lớp phối hợp **Class C**, dù cả hai phải nêu lớp thật và phản ánh các đánh giá bắt buộc.*

Một **Hồ sơ chứng nhận hệ thống** là hồ sơ có giới hạn, rà được về một hệ thống, phiên bản, người vận hành hoặc người quản trị có trách nhiệm, phạm vi, cửa sổ thời gian, hồ sơ tác động vật chất, và ngữ cảnh quyết định cụ thể — bị buộc phạm vi, bị buộc thời gian, và tranh biện được dưới nghĩa Chương Năm ở [Hồ sơ chứng nhận hệ thống](../../core_05.040_band_continuity.md#system-certification-record).

<a id="81-minimum-record-contents"></a>

#### 8.1 Nội dung hồ sơ tối thiểu

<a id="811-system-identity-scope-and-prior-system-certification-record"></a>
##### 8.1.1 Nhận dạng hệ thống, phạm vi và Hồ sơ Chứng nhận Hệ thống trước đó

Hồ sơ phải nhận diện tối thiểu: hệ thống, Phiên bản Hệ thống, đơn vị vận hành/bên quản lý, phạm vi chứng nhận; System Charter áp dụng (hoặc lý do có căn cứ cho việc không có Charter khi điều đó không trọng yếu); cộng đồng bị ảnh hưởng và các phụ thuộc; trạng thái xem xét và việc phạm vi chứng nhận có khớp với phạm vi nêu trong Charter nếu có. Nếu đơn vị vận hành/bên quản lý là Institution có Institutional Certification Record, đính kèm liên kết theo phiên bản để truy xuất dữ kiện thể chế được dựa vào, và nêu trạng thái hệ thống. Ở lần chứng nhận sau, liên kết phiên bản tới Hồ sơ Chứng nhận Hệ thống đã hoàn tất trước đó, được lưu theo Chương Tám §8, và nêu thay đổi kể từ đó.

<a id="812-classification-and-whole-system-findings"></a>
##### 8.1.2 Phân loại và kết luận toàn hệ thống

Hồ sơ phải nhận diện Hồ sơ Phân loại Hệ thống (hoặc nội dung bắt buộc theo CS-9.305 và CS-9.310) cùng kết quả đánh giá toàn hệ thống và §4 có liên quan: loại được phân, lý do, giả định chính gồm tác động trọng yếu, loại phụ thuộc hiện có, đánh giá tính trọng yếu vận hành khi cần, bất định, khoảng chứng nhận theo loại cho từng trạng thái; nếu phân loại chưa chắc hoặc bị tranh chấp thì nêu loại thận trọng được dùng và điều kiện chờ xử lý. Ghi các phát hiện trọng yếu về phạm vi hệ thống, viện dẫn chung về quyền riêng tư, rút lui, hội họp và bất đồng, tính nhất quán thời gian, quản trị, động cơ và khả năng khiếu nại nếu có liên quan. Khi rủi ro hệ thống thuộc phạm vi, ghi kết quả đánh giá rủi ro/giả định; đối tượng/cách chuyển công khai, thời điểm so với quyết định trọng yếu, việc giữ lại có lý do cùng phương án thay thế dùng được; và khiếm khuyết/điều kiện nếu đánh giá hay công khai chưa hoàn tất. Các phát hiện này nằm trong chính Hồ sơ Chứng nhận Hệ thống; không tạo hồ sơ công khai rủi ro riêng hay hồ sơ thành phần bắt buộc thứ năm.

<a id="813-system-data-types-record"></a>
##### 8.1.3 Hồ sơ loại dữ liệu Hệ thống

Nhận diện Hồ sơ Loại Dữ liệu Hệ thống hoặc nội dung CS-6.305/CS-6.310 bắt buộc, lập/xác minh theo [§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-đánh-giá-loại-dữ-liệu-và-cách-xử-lý): loại dữ liệu trọng yếu, lý do phân loại dữ liệu mơ hồ/đa loại, kiểm soát tách biệt/liên kết giữa miền, cách xử lý/lưu giữ/vòng đời và bảo đảm hạ tầng, năng lực quy kết đủ cho Attributable Action và Attribution Integrity, lần đánh giá lại định kỳ mới nhất theo CS-6.305 §§5,8 (ngày/mã chu kỳ, tần suất theo loại và tác động, phân loại lại trọng yếu). Nêu giới hạn công khai/kiểm toán có lý do và phương án công khai thay thế bắt buộc. Nếu chuẩn Type O áp dụng, giải thích Public Oversight Baseline Disclosure bao phủ phạm vi chứng nhận thế nào, gồm trường System Charter được dựa vào, kết luận ranh giới, khoảng trống và điều kiện.

<a id="814-rights-floor-and-domain-findings"></a>
##### 8.1.4 Kết luận về sàn quyền và lĩnh vực

Với từng biện pháp bảo vệ trong [§5 Rights-Floor and Domain Evaluations](core_09.000_system_alignment_certification_evaluation.md#5-đánh-giá-sàn-quyền-và-lĩnh-vực) có kích hoạt, nêu ngưỡng trọng yếu, phạm vi đánh giá và kết luận: chứng nhận/tiếp tục dựa vào có loại trừ hoặc làm suy yếu đáng kể yếu tố thiết yếu cho sự sống, tiếp cận giáo dục hoặc Safe Conditions; dấu chân sinh thái (giả định quy kết, giới hạn vòng đời/phụ thuộc, gánh nặng, công khai và kết luận của diễn đàn Môi trường nếu cần); hỗ trợ liên hệ thống (phạm vi bản đồ/luồng tài nguyên, tính đầy đủ/cập nhật/kiểm toán được của bản đồ và hồ sơ, khai thác/hoàn trả, mức hỗ trợ và công bằng phân bổ); không phân biệt đối xử (mô hình gánh nặng/lợi ích, đặc tính được bảo vệ, phân biệt qua đại diện, công bằng thực chất); khả năng tiếp cận (tham gia thực chất, điều chỉnh hỗ trợ, chống từ chối qua đại diện); năng lực giáo dục (xây dựng năng lực/đào tạo lại, minh bạch/khả năng khiếu nại việc đánh giá, chống thao túng); độ đáng tin (niềm tin giả, động cơ sai lệch, đường khiếu nại, toàn vẹn phục hồi). Ghi cả bất định, kết luận thành phần được giao, giới hạn công khai có lý do và phương án thay thế công khai, điều kiện/giới hạn phụ thuộc/kích hoạt mở lại gắn với tổn hại dai dẳng.

<a id="815-technical-evidence-and-review-findings"></a>
##### 8.1.5 Bằng chứng kỹ thuật và kết luận xem xét

Nêu tiêu chuẩn, thử nghiệm, phép đo, bất định, biên an toàn, dạng lỗi, kết quả kiểm tra an toàn và căn cứ chứng cứ được dựa vào trọng yếu. Bao gồm kết quả kiểm thử hồi quy mỗi lần tái chứng nhận (phạm vi, bộ kiểm thử chuẩn/tùy chỉnh, kết quả, lỗi đã biết, khắc phục và rủi ro còn lại được chấp nhận kèm lý do) và gói chứng cứ chu kỳ theo CS-6.345: phạm vi, phân loại, thử nghiệm, rủi ro còn lại, sẵn sàng khắc phục, giám sát, thay đổi trọng yếu từ hồ sơ trước. Ghi cân nhắc về bên liên quan, sàn quyền, tiếp cận, phụ thuộc và tham gia; phơi nhiễm/quy kết sinh thái, phụ thuộc điều kiện môi trường, gánh nặng vòng đời, nghĩa vụ phục hồi, xem xét môi trường khi trọng yếu; nguy cơ chiếm đoạt, tự xem xét, động cơ lệch, kiểm soát chứng cứ và cản trở khiếu nại.

<a id="816-supervision-independence-and-challenge-paths"></a>
##### 8.1.6 Giám sát, độc lập và con đường khiếu nại

Nêu nhóm diễn đàn/cơ quan đã ban hành, thông qua, chuyển, gửi xin quyết định, tạm dừng hoặc xem xét từng thành phần và trình tự giám sát tại Phần B §6.2. Ghi bốn ghế theo Chương Tám (khởi xướng, xác minh/cho phép, ghi nhận, khiếu nại), người giữ/quyền hạn và phiên bản Charter Role Map có hiệu lực; mọi việc rút lui, ủy quyền, thay thế, hợp nhất được phép, ngoại lệ khẩn cấp; đủ thông tin về đường kiểm soát để chứng minh bên vận hành/đề xuất không tự xác minh yêu cầu chứng nhận hoặc kiểm soát việc khiếu nại. Nêu các đường contestability tại §10 và chuỗi Phần B §6.3, cho biết bên bị ảnh hưởng có thể khiếu nại ở từng bước thế nào.

<a id="817-concerns-cause-and-remediation-readiness"></a>
##### 8.1.7 Quan ngại, nguyên nhân và mức sẵn sàng khắc phục

Ghi mọi phản đối, bất đồng, quan ngại và khiếu nại trong quá trình xem xét/quyết định, bất kể người nêu hoặc cách nêu. Với từng mục ghi người nêu (hoặc ẩn danh/bảo mật), nội dung, cách giải quyết/lý do còn mở, điều kiện/giới hạn dựa vào/kích hoạt xem xét lại phát sinh; công bố nhật ký ý kiến theo Phần B §6.2.4. Nếu có sai lệch/khiếm khuyết, ghi nguyên nhân do thiết kế, vận hành hoặc chưa xác định và chứng cứ. Nếu cần khắc phục, ghi kết luận/chứng cứ về ý chí/năng lực, bước chứng minh, thời hạn, xác minh độc lập và kết quả theo §7.3. Nếu từ chối/thu hồi, nêu lý do, bảo vệ tạm thời và giới hạn dựa vào theo §7.4.

<a id="818-outcome-and-reliance-limits"></a>
##### 8.1.8 Kết quả và giới hạn dựa vào

Nêu tối thiểu: kết quả chứng nhận theo {link8}; hệ thống có chứng nhận tạm thời/đầy đủ hay Not Certified; khoảng chứng nhận áp dụng; yếu tố kích hoạt mở lại; giới hạn dựa vào.

<a id="819-operating-plan"></a>
##### 8.1.9 Kế hoạch vận hành

Cùng hồ sơ phải có kế hoạch vận hành ngắn gọn, tương xứng với loại hệ thống và tác động trọng yếu; không cần tài liệu riêng. Kế hoạch nêu phạm vi/dân số/thời hạn vận hành được phép; ngày hết hạn chứng nhận, lần tái chứng nhận kế tiếp, hạn kiểm toán giữa kỳ ({link91}); với lần đưa vào vận hành/mở rộng trọng yếu đầu tiên, thời điểm sớm nhất được phép, thời hạn thông báo và lý do ({link71}); từng điều kiện có thời điểm, chủ thể chịu trách nhiệm, chứng cứ hoàn thành/tuân thủ liên tục, bên xác minh độc lập và hậu quả vi phạm; người giám sát kết quả thực tế/biện pháp bảo vệ, chứng cứ/chỉ báo, tần suất kiểm tra, phát hiện/ngưỡng cần hành động hoặc mở lại; người ứng phó sự cố/khiếu nại/điều kiện chưa đạt, khung thời gian và thẩm quyền bảo vệ tạm thời, ngăn chặn, hoàn nguyên hoặc giới hạn dựa vào khi cần; đối với khiếm khuyết, việc sửa chữa, tiêu chí/kết quả xác minh, bất định còn lại và mức dựa vào tạm thời được phép. Với hệ thống Not Certified, nêu việc cấm đưa vào vận hành, mức dựa vào tạm thời được cho phép riêng, yêu cầu khắc phục và điều kiện để xem xét mới; không hàm ý được phép vận hành đã chứng nhận.

Chứng cứ vận hành và kết luận sau này rằng điều kiện đã hoàn thành được thêm dưới dạng liên kết theo {act}; không sửa trực tiếp hồ sơ đã hoàn tất. Phương pháp thử nghiệm/giám sát chi tiết vẫn thuộc chủ thể phụ trách, gồm {cs}.

<a id="8110-completeness"></a>
##### 8.1.10 Tính đầy đủ

Hồ sơ thiếu đầy đủ nếu bỏ sót kết luận của bất kỳ đánh giá áp dụng nào: Part A §§2, 3, 3.4 với mọi hệ thống có tác động trọng yếu; từng tiểu mục §4 có locus/principle liên quan; và từng lĩnh vực §5 có kích hoạt. Kết luận phải phản ánh điều đánh giá thực sự phát hiện, không chỉ tên mục hay lời xác nhận của bên vận hành. Hồ sơ cũng thiếu đầy đủ nếu bỏ qua quan ngại, phản đối hoặc bất đồng nêu trong quá trình xem xét/quyết định, dù điều đó không làm đổi kết quả.

<a id="82-transparency-and-auditability-of-the-system-certification-record"></a>
#### 8.2 Tính minh bạch và khả năng kiểm toán của Hồ sơ Chứng nhận Hệ thống
*Nói đơn giản: Hồ sơ Chứng nhận Hệ thống chỉ có tác dụng khi sentient có thể đọc và kiểm tra. Phần này đặt ra các yêu cầu cụ thể về minh bạch và khả năng kiểm toán ngay trên hồ sơ, thay vì các lý tưởng trừu tượng. Trong nhánh **giám sát** của Tứ trụ, giám sát đòi hỏi kiểm toán. Chứng nhận mức độ phù hợp của hệ thống là một quy trình kiểm toán đặc biệt lớn và phải đáp ứng các chuẩn tối thiểu ở đây. Phần này không sở hữu hoặc thay thế [Article XVI](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) (*Kiểm toán, minh bạch và xác minh độc lập*) hay các hình thức kiểm toán khác. Yêu cầu thứ ba, để sentient có thể phản hồi, nằm ở [§10 Khiếu nại chứng nhận](#10-khiếu-nại-chứng-nhận).*
Phần này áp dụng [Tính minh bạch](../../core_05.050_band_oversight.md#transparency) và [Khả năng kiểm toán](../../core_05.050_band_oversight.md#auditability) cho Hồ sơ Chứng nhận Hệ thống. Đây là phần “có thể tiếp cận” và “có thể tái dựng” của [Tính toàn vẹn hồ sơ](../../core_05.035_band_accountability.md#record-integrity), áp dụng cho toàn bộ hồ sơ ([§8 Hồ sơ Chứng nhận Hệ thống](#8-hồ-sơ-chứng-nhận-hệ-thống)). Nơi quy định các thuật ngữ chuẩn tắc và ranh giới trách nhiệm là [Lời mở đầu — Sổ đăng ký chủ thể chịu trách nhiệm theo Hiến pháp](../../core_00.000_preamble.md#4-principles-definitions-and-rights) và [Thứ bậc thẩm quyền và trật tự nội bộ](../../core_05.045_band_integrative.md#owner-non-relocation). Theo [Tứ trụ Hiến pháp](../../core_00.000_preamble.md#constitutional-tetrad):
**Khả năng kiểm toán** — sentient phải tái dựng và kiểm tra được Hồ sơ Chứng nhận Hệ thống:
  - điều gì thay đổi giữa các Phiên bản Hồ sơ, ai thực hiện mỗi thay đổi, theo thẩm quyền nào và theo yêu cầu của ai; với Hồ sơ mới, điều gì thay đổi kể từ hồ sơ hoàn tất trước đó mà nó tiếp nối;
  - [§8](#8-hồ-sơ-chứng-nhận-hệ-thống) (*Hồ sơ Chứng nhận Hệ thống hoàn tất mà mỗi lần tái chứng nhận hoặc xem xét mở lại tiếp nối*);
- Đầu ra: [§11.3](#113-cổng-đầu-vào-đã-xác-minh-một-hồ-sơ-chứng-nhận-chỉ-được-nuôi-quỹ-đạo-chương-tám-khi-nó-có-giới-hạn-truy-vết-được-tranh-biện-được-và-đã-xác-minh-dưới) và [§11.5 Hồ sơ tư cách vi phạm](#115-hồ-sơ-tư-cách-vi-phạm) (*cổng dữ liệu đã xác minh khi sự kiện hỗ trợ kết luận bất lợi*); [Chương Mười Lăm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*giám sát diễn đàn khi mở lại*); [Chương Mười Một](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
  - [§9.1](#91-lịch-tái-chứng-nhận-và-hồ-sơ-chứng-nhận-hệ-thống-mới) (*lịch tái chứng nhận và Hồ sơ Chứng nhận Hệ thống mới*);

<a id="9-recertification-and-reopening"></a>

### 9. Tái chứng nhận và mở lại

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Căn cứ trước đó:
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận) (*kết quả đang có hiệu lực*);
  - [§8](#8-hồ-sơ-chứng-nhận-hệ-thống) (*Hồ sơ Chứng nhận Hệ thống đã hoàn tất mà mỗi lần tái chứng nhận hoặc xem xét mở lại phải tuân theo*);
  - [Phần A §2](core_09.000_system_alignment_certification_evaluation.md#2-đánh-giá-lớp-hệ-thống) (9.000 §2) đến
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-đánh-giá-sàn-quyền-và-lĩnh-vực) (*phân loại sai, không phù hợp và khiếm khuyết phát hiện trong đánh giá*);
  - [§10](#10-khiếu-nại-chứng-nhận) (*khiếu nại đáng tin cậy*);
  - [Hai Mục tiêu Hiến pháp](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Chương Ba §1](../../core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) và
  - [§2](../../core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*tính toàn vẹn của định nghĩa và hành vi né tránh*);
  - [Hiến chương Hệ thống](../../core_05.040_band_continuity.md#system-charter) (*sự không khớp giữa Hiến chương Hệ thống và hành vi, cùng việc xem xét quá hạn*).
- Hệ quả tiếp theo: [§11.3](#113-cổng-đầu-vào-đã-xác-minh-một-hồ-sơ-chứng-nhận-chỉ-được-nuôi-quỹ-đạo-chương-tám-khi-nó-có-giới-hạn-truy-vết-được-tranh-biện-được-và-đã-xác-minh-dưới) và [§11.5](#115-hồ-sơ-tư-cách-vi-phạm) (*cổng đầu vào đã xác minh khi sự kiện hỗ trợ kết luận bất lợi*); [Chương Mười Lăm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*giám sát diễn đàn được mở lại*); [Chương Mười Một](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- Đọc cùng: **[CS-6.305 §5](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Phân loại lại và quản trị vòng đời*) và **[CS-9.305 §3](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yêu cầu phân loại lại*).
- Các tiểu mục:
  - [§9.1](#91-lịch-tái-chứng-nhận-và-hồ-sơ-chứng-nhận-hệ-thống-mới) (*lịch tái chứng nhận và Hồ sơ Chứng nhận Hệ thống mới*);
  - [§9.2](#92-yếu-tố-kích-hoạt-mở-lại) (*các căn cứ mở lại*);
  - [§9.3](#93-chứng-nhận-tạm-thời-và-đầy-đủ) (*chứng nhận tạm thời và đầy đủ*, gồm
  - [§9.3.1 Hai trạng thái](#931-hai-trạng-thái),
  - [§9.3.2 Thất bại và hạ cấp](#932-không-đạt-và-hạ-trạng-thái),
  - [§9.3.3 Nguyên nhân không phù hợp](#933-nguyên-nhân-sai-lệch),
  - [§9.3.4 Khoảng thời gian theo cấp](#934-thời-hạn-theo-cấp-độ),
  - [§9.3.5 Sự phụ thuộc vào Lớp A](#935-việc-dựa-vào-hệ-thống-hạng-a), và
  - [§9.3.6 Xác minh, không phải khẳng định](#936-xác-minh-không-chỉ-khẳng-định));
  - [§9.4](#94-không-lẩn-tránh) (*không được né tránh*).

</details>


*Nói đơn giản: không có kết quả nào tồn tại mãi. Khi hệ thống vận hành, chủ thể được nêu tên phải theo dõi kết quả và biện pháp bảo vệ thực tế, phản hồi sự cố và khiếu nại, đồng thời đáp ứng điều kiện chứng nhận trong Hồ sơ Chứng nhận Hệ thống. Hệ thống được chứng nhận tái chứng nhận theo lịch dựa trên loại hệ thống, với kiểm toán giữa mỗi chu kỳ. Việc xem xét mở lại khi sự kiện trọng yếu thay đổi hoặc có khiếu nại đáng tin cậy. Khiếm khuyết dẫn đến bảo vệ, sửa chữa và xác minh độc lập. Mỗi lượt xem xét bắt đầu hồ sơ mới liên kết với hồ sơ trước; hồ sơ mới không xóa hồ sơ cũ hoặc các khiếu nại đối với hồ sơ đó. Phê duyệt cũ không thay thế việc tuân thủ Sàn Quyền hiện tại.*
**Xác nhận tính phù hợp.** Chương Mười Lăm gọi việc diễn đàn xem xét hệ thống đang tồn tại là *xác nhận tính phù hợp đang diễn ra*. Trong chương này, xác nhận không phải một quy trình riêng. Đây là một lượt chứng nhận cho hệ thống đang vận hành: tái chứng nhận, xem xét mở lại hoặc xem xét mới. Lượt này đi qua [Phần B §6 Quy trình Diễn đàn](core_09.005_system_alignment_certification_record_process.md#6-quy-trình-diễn-đàn) như mọi lượt chứng nhận và kết thúc bằng kết quả theo [Phần B §7 Kết quả Chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận).
**Theo dõi và phản hồi.** Bên vận hành và quản thủ phải thực hiện kế hoạch trong Hồ sơ Chứng nhận Hệ thống theo [§8.1 Nội dung tối thiểu của hồ sơ](#81-nội-dung-hồ-sơ-tối-thiểu). Chủ thể được nêu tên phải:

- lưu giữ bằng chứng theo dõi;
- điều tra sự cố và chỉ báo trọng yếu;
- chuyển khiếu nại đến cơ quan được chỉ định; và
- thực hiện biện pháp bảo vệ tạm thời cùng công việc khắc phục bắt buộc.

Bất kỳ điều nào dưới đây nếu làm phát sinh nghi vấn trọng yếu về sự phù hợp đều cần diễn đàn xem xét kịp thời theo mục này; không được chờ đến kỳ tái chứng nhận đã lên lịch tiếp theo:

- một sự cố;
- điều kiện chứng nhận chưa được đáp ứng;
- bước chứng minh bị bỏ lỡ theo [Phần B §7.3 Mức sẵn sàng khắc phục: Thiện chí và năng lực sửa chữa](core_09.005_system_alignment_certification_record_process.md#73-mức-độ-sẵn-sàng-khắc-phục-ý-chí-và-năng-lực-khắc-phục);
- bằng chứng sẵn sàng sai lệch; hoặc
- khiếu nại đáng tin cậy.

Việc sửa chữa, hoàn thành và miễn điều kiện chứng nhận tuân theo yêu cầu xác minh độc lập tại [Phần B §7 Kết quả Chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận).

<a id="91-recertification-schedule-and-the-new-system-certification-record"></a>
#### 9.1 Lịch tái chứng nhận và Hồ sơ Chứng nhận Hệ thống mới
*Nói đơn giản: chứng nhận không có hiệu lực mãi mãi. Hệ thống đến hạn tái chứng nhận theo lịch dựa trên loại hệ thống, với kiểm toán ở giữa mỗi chu kỳ. Mỗi lượt chứng nhận mở hồ sơ mới liên kết với hồ sơ trước.*
**Hồ sơ Chứng nhận Hệ thống** phải được tái chứng nhận theo chu kỳ dành cho loại hệ thống tại [Chương Mười Lăm §6 Giải quyết kịp thời, các tầng trọng yếu và kỷ luật chống trì hoãn](../../core_15.000_forum.md#review-cadence) (*Chu kỳ xem xét*), và được kiểm toán ở giữa chu kỳ đó.
**Hồ sơ mới cho mỗi lượt chứng nhận.** Mỗi lượt chứng nhận sau (tái chứng nhận, xem xét mở lại hoặc xem xét mới) mở một Hồ sơ Chứng nhận Hệ thống mới. Hồ sơ mới:
- liên kết với hồ sơ hoàn tất trước đó mà nó tiếp nối và nêu những thay đổi kể từ đó ([§8.1.1 Nhận dạng hệ thống, phạm vi và hồ sơ trước đó](#811-nhận-dạng-hệ-thống-phạm-vi-và-hồ-sơ-chứng-nhận-hệ-thống-trước-đó)); và
Hồ sơ Chứng nhận Hệ thống đã hoàn tất giữ nguyên trạng ([§8 Hồ sơ Chứng nhận Hệ thống](#8-hồ-sơ-chứng-nhận-hệ-thống)). Hồ sơ đó vẫn là hồ sơ của giai đoạn được ghi nhận và vẫn có thể bị khiếu nại theo [Phần B §6.3 Chuỗi khả năng khiếu nại](core_09.005_system_alignment_certification_record_process.md#63-chuỗi-khả-năng-bị-phản-biện). Trạng thái chứng nhận, số lần tái chứng nhận không có vi phạm và chỉ báo theo dõi được chuyển tiếp qua liên kết. Chúng được xác minh trong hồ sơ mới theo [§9.3 Chứng nhận tạm thời và đầy đủ](#93-chứng-nhận-tạm-thời-và-đầy-đủ).

<a id="92-reopening-triggers"></a>

#### 9.2 Yếu tố kích hoạt mở lại

Một **Hồ sơ chứng nhận hệ thống** bị **buộc phạm vi** và **buộc thời gian**. Rà mở lại dưới Chương Mười Lăm và nghĩa vụ triển khai hệ thống đã hợp nhất khi bất kỳ điều nào sau có trọng:

- **Cò chung:**
  - đổi có trọng ở hệ thống, cách dùng, hoặc ngữ cảnh vận hành;
  - hành vi giấu;
  - tăng phụ thuộc;
  - phụ thuộc tăng, gồm mức dựa vào hệ thống và mức khai thác từ các nền tảng chung tăng lên, cùng với tập trung vượt ngưỡng do bên tiếp nhận đặt ra tại [Chương Một §11.4](../../core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (việc nâng cấp không chờ ngưỡng; Phần A §2.2);
  - dòng hoàn trả của hệ thống cho các nền tảng chung giảm đáng kể, theo nguyên tắc Hỗ trợ Liên hệ thống Tương xứng;
  - rủi ro mới;
  - lịch sử sự cố;
  - bằng chứng bên bị ảnh hưởng;
  - tranh biện đáng tin dưới [§14](#10-khiếu-nại-chứng-nhận);
  - phản đối sinh thái;
  - lệch lạc lớp hệ thống hoặc đánh giá lại quá hạn dưới **[CS-3 §3.5](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**;
  - lệch lạc loại dữ liệu hoặc xử lý, tái đánh giá loại dữ liệu định kỳ quá hạn hoặc bị bỏ dưới **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**;
  - lệch lạc phân loại;
  - sửa [Điều lệ](../../core_05.040_band_continuity.md), lệch Điều lệ–hành vi, vận hành có trọng ngoài phạm vi Điều lệ, hoặc rà Điều lệ định kỳ quá hạn;
  - vi phạm quản trị của một Tổ chức có Hệ thống trong danh mục của mình (xác định quản trị thất bại, từ chối hoặc thu hồi vì lý do quản trị, hoặc kết luận nguyên nhân quy sự lệch lạc của Hệ thống khác cho Tổ chức); chỉ mở lại khi có tính trọng yếu, theo [Chương Mười §9.6](../../core_10.000_institutional_alignment_certification.md#96-reopening-the-institutions-systems);
- **Lệch lạc miền** phản ánh trên hồ sơ chứng nhận, kể cả:
  - khiếm khuyết hoặc lệch lạc đánh giá rủi ro hoặc công bố rủi ro có trọng dưới [§3.1](core_07_a_system_alignment_certification_evaluation.md#31-phạm-vi-hệ-thống-và-yếu-tố-rủi-ro);
  - trình bày sai hoặc lệch lạc dấu chân có trọng dưới [§5](core_07_a_system_alignment_certification_evaluation.md#51-đánh-giá-dấu-chân-sinh-thái);
  - lệch lạc mẫu phân biệt hoặc lẩn tránh qua chỉ số thay có trọng dưới [§7](core_07_a_system_alignment_certification_evaluation.md#54-đánh-giá-không-phân-biệt-đối-xử);
  - lệch lạc khả năng tiếp cận hoặc điều chỉnh chỉ-trên-giấy có trọng dưới [§8](core_07_a_system_alignment_certification_evaluation.md#55-đánh-giá-khả-năng-tiếp-cận);
  - lệch lạc mờ đánh giá, cổng giấy thông hành, hoặc lỗi thời áp đặt có trọng dưới [§9](core_07_a_system_alignment_certification_evaluation.md#52-đánh-giá-năng-lực-giáo-dục-và-tính-toàn-vẹn-của-hệ-thống-học-tập);
  - lệch lạc tin cậy giả, khuyến khích lệch, hoặc tính toàn vẹn phục hồi có trọng dưới [§10](core_07_a_system_alignment_certification_evaluation.md#56-đánh-giá-độ-tin-cậy-và-tính-toàn-vẹn-của-sự-dựa-vào-hệ-thống);
  - lệch lạc đánh giá Phần A khác nơi cò trọng yếu tương ứng áp dụng — kể cả [§2](core_07_a_system_alignment_certification_evaluation.md#2-đánh-giá-lớp-hệ-thống), [§4](core_07_a_system_alignment_certification_evaluation.md#34-đánh-giá-loại-dữ-liệu-và-cách-xử-lý), và [§6](core_07_a_system_alignment_certification_evaluation.md#53-đánh-giá-hỗ-trợ-liên-hệ-thống-tương-xứng).

**Vì sao mở lại có trọng.** Mở lại vì lệch lạc, tăng phụ thuộc, hoặc tranh biện đáng tin bảo vệ mục tiêu **Liên tục** dưới [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims) nơi hệ thống chung cổng cung bền thiết yếu sống còn, lối vào giáo dục, đường dẫn xây năng lực, sự dựa đáng tin, hoặc an toàn. Chứng nhận cũ không được thế cho tuân thủ Sàn Quyền hiện tại.

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Chứng nhận tạm thời và đầy đủ

*Nói đơn giản: hệ thống giành được lòng tin theo từng bước. Hệ thống mới và hệ thống đã không đạt đánh giá bắt đầu với sự kiểm soát chặt hơn và được kiểm tra thường xuyên. Chỉ hệ thống hiện không có sai lệch và không có dấu hiệu sắp sai lệch mới được chuyển sang chứng nhận đầy đủ với khoảng thời gian dài hơn. Đánh giá không đạt sẽ đưa hệ thống trở lại chế độ chặt hơn.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 Hai trạng thái

Chứng nhận có một trong hai trạng thái; khoảng thời gian của từng trạng thái phải được ghi trong Hồ sơ Chứng nhận Hệ thống theo [§8.1 Nội dung tối thiểu của hồ sơ](#81-nội-dung-hồ-sơ-tối-thiểu):

- **[Chứng nhận tạm thời](../../core_05.040_band_continuity.md#provisional-certification)** áp dụng cho lần chứng nhận đầu tiên (kể cả hệ thống mới triển khai), và cho hệ thống được chứng nhận sau lần tái chứng nhận không đạt, rà soát mở lại hoặc rà soát mới phát hiện sai lệch. Khoảng thời gian tạm thời ngắn hơn khoảng thời gian chứng nhận đầy đủ của cùng hạng hệ thống. Hồ sơ nêu giới hạn được phép dựa vào hệ thống.
- **[Chứng nhận đầy đủ](../../core_05.040_band_continuity.md#full-certification)** chỉ được đạt trong lần tái chứng nhận khi hệ thống đang có chứng nhận tạm thời và đáp ứng cả ba điều kiện:
  1. hoàn thành số lần tái chứng nhận tạm thời liên tiếp đạt yêu cầu, ít nhất một lần và nhiều hơn đối với hạng hệ thống cao hơn, theo văn bản được thông qua;
  2. hiện không có sai lệch: hồ sơ không ghi sai lệch đang mở, khiếm khuyết chưa khắc phục, lần kiểm tra quá hạn hoặc kiểm thử hồi quy không đạt; và
  3. không chỉ báo giám sát nào cho thấy sai lệch sắp xảy ra: các ngưỡng và số liệu xu hướng trong hồ sơ không vượt ngưỡng và không có xu hướng tiến tới ngưỡng.

Chứng nhận đầy đủ có khoảng thời gian theo hạng hệ thống; vẫn có thời hạn và không phải phê chuẩn vĩnh viễn. Lần tái chứng nhận **đạt sạch** khi đáp ứng điều kiện 2 và 3.

<details>
<summary><strong>Hướng dẫn đọc (không có hiệu lực điều hành): trạng thái chứng nhận</strong></summary>

> Bảng này tóm tắt §9.3; nếu khác với nội dung điều khoản thì nội dung điều khoản được ưu tiên.
>
> | | Tạm thời | Đầy đủ |
> |---|---|---|
> | **Ai có trạng thái này** | Lần chứng nhận đầu tiên, kể cả hệ thống mới triển khai; hoặc hệ thống sau lần tái chứng nhận không đạt hay rà soát phát hiện sai lệch | Hệ thống đạt trạng thái này khi tái chứng nhận trong lúc có trạng thái tạm thời |
> | **Cách đạt được** | Được cấp cùng với kết quả chứng nhận | Số lần tái chứng nhận tạm thời liên tiếp đạt sạch theo yêu cầu; không có sai lệch hiện tại hay chỉ báo sai lệch sắp xảy ra |
> | **Khoảng thời gian** | Ngắn hơn khoảng thời gian đầy đủ của cùng hạng hệ thống | Theo hạng hệ thống; vẫn có thời hạn |
> | **Nếu tái chứng nhận không đạt** | Áp dụng Hợp phần B §7; lần chứng nhận tiếp theo là tạm thời và số lần đạt sạch trở về không | Như cột bên cạnh |
> | **Nếu có chỉ báo sai lệch sắp xảy ra** | Vẫn tạm thời; số lần không tăng | Hạ xuống tạm thời |
>
</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 Không đạt và hạ trạng thái

Kết quả tái chứng nhận, rà soát mở lại hoặc rà soát mới quyết định trạng thái hệ thống:

- Tái chứng nhận phát hiện sai lệch hiện tại là lần tái chứng nhận **không đạt**. Áp dụng hậu quả tại [Hợp phần B §7 Kết quả chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận). Bất kể lần kiểm tra tiếp theo sạch đến đâu, chứng nhận tiếp theo có thể đạt được chỉ là tạm thời; số lần tái chứng nhận sạch trở về không.
- Nếu không có sai lệch hiện tại nhưng có chỉ báo sai lệch sắp xảy ra, lần tái chứng nhận không phải là không đạt nhưng cũng không sạch. Trạng thái tạm thời vẫn giữ nguyên và số lần không tăng; trạng thái đầy đủ hạ xuống tạm thời.
- Rà soát mở lại theo [§9 Tái chứng nhận và mở lại](#9-tái-chứng-nhận-và-mở-lại) phát hiện sai lệch thì có hiệu lực như tái chứng nhận không đạt.
- Rà soát mới đối với hệ thống đang được chứng nhận mà phát hiện sai lệch hiện tại cũng có hiệu lực như vậy. Nếu hệ thống không có trạng thái chứng nhận, áp dụng quy tắc từ chối tại [Hợp phần B §7.4 Từ chối và thu hồi](core_09.005_system_alignment_certification_record_process.md#74-từ-chối-và-thu-hồi).

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Nguyên nhân sai lệch

Khi đánh giá, tái chứng nhận, rà soát mở lại hoặc rà soát mới phát hiện sai lệch, Hồ sơ Chứng nhận Hệ thống phải nêu nguyên nhân là:

- **do thiết kế:** hệ thống hoặc quy trình được xây dựng theo cách tạo ra kết quả sai lệch ngay cả khi vận hành đúng dự kiến;
- **do vận hành:** thiết kế nhìn bề ngoài là phù hợp, nhưng cách vận hành, cung cấp đầu vào hoặc bảo trì làm kết quả sai lệch; hoặc
- **chưa xác định:** biện pháp khắc phục cho cả thiết kế và vận hành vẫn được để ngỏ cho đến khi diễn đàn xác định nguyên nhân.

Kết luận về nguyên nhân tuân theo các giới hạn sau:

- Nếu Hệ thống tiếp tục tạo ra kết quả sai lệch thì nó sai lệch, dù thiết kế trên giấy có vẻ phù hợp. Thiết kế có vẻ phù hợp không phải là biện hộ.
- Thiết kế mà nếu thực hiện sẽ tạo ra kết quả sai lệch đã là sai lệch trước khi kết quả đó xuất hiện.
- Kết luận về nguyên nhân xác định biện pháp khắc phục cần tìm và phạm vi rà soát mở lại; kết luận đó không bao giờ quyết định hệ thống có sai lệch hay không.

Nếu sai lệch do thiết kế:

- số lần tái chứng nhận sạch vẫn bằng không cho tới khi thiết kế lại được triển khai và xác minh;
- diễn đàn xác định nguyên nhân, hoặc diễn đàn kế tiếp được phân công theo [Hợp phần B §6.2 Trình tự giám sát](core_09.005_system_alignment_certification_record_process.md#62-trình-tự-giám-sát), xác minh thiết kế lại trong [mục tiêu tiếp nhận tương ứng](../../core_05.040_band_continuity.md#tier-window), và có thể làm việc đó ngay trong lần tái chứng nhận tạm thời đầu tiên;
- **đánh giá cấu phần** (phần đánh giá chứng nhận của một cấu phần, theo định nghĩa tại [Hợp phần B §6.1 Giám sát diễn đàn và vai trò cấu phần](core_09.005_system_alignment_certification_record_process.md#61-giám-sát-diễn-đàn-và-vai-trò-thành-phần)) trước khi thiết kế lại được xác minh sẽ không tính vào số lần sạch, dù kết quả sạch; và
- thay đổi cách vận hành hệ thống không đáp ứng bước này.

Các quy tắc này bổ sung, không thay thế, các gạch đầu dòng về hạ trạng thái ở trên. Người vận hành hoặc bất kỳ chúng sinh có ảnh hưởng nào có thể yêu cầu diễn đàn rà soát kết luận nguyên nhân; nếu kết luận thay đổi, các quy tắc này không còn áp dụng.

<a id="934-tier-windows"></a>
##### 9.3.4 Thời hạn theo cấp độ

Khi đánh giá ban đầu, tái chứng nhận, rà soát mở lại hoặc rà soát mới phát hiện sai lệch:

- vụ việc được phân loại theo các cấp độ trọng yếu tại [Chương Mười lăm §6 Giải quyết đúng hạn, cấp độ trọng yếu và kỷ luật chống trì hoãn](../../core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline);
- theo giả định, vụ việc thuộc cấp độ tương ứng với hạng hệ thống (ví dụ sai lệch ở hệ thống Hạng A mặc định thuộc Cấp độ A);
- tiếp nhận, bảo toàn chứng cứ, bảo vệ tạm thời và quyết định tuân theo thời hạn và giới hạn tối đa của cấp độ đó; và
- việc quá hạn được rà soát theo yêu cầu của điều khoản đó.

<a id="935-class-a-reliance"></a>
##### 9.3.5 Việc dựa vào hệ thống Hạng A

So với chứng nhận đầy đủ, chứng nhận tạm thời có khoảng thời gian ngắn hơn nên tái chứng nhận diễn ra sớm hơn ([§9.3.1 Hai trạng thái](#931-hai-trạng-thái)); các giới hạn dựa vào hệ thống được ghi trong hồ sơ ([§8.1 Nội dung tối thiểu của hồ sơ](#81-nội-dung-hồ-sơ-tối-thiểu)). Việc gián đoạn được xử lý như sau:

- Bản thân chứng nhận tạm thời không buộc phải gián đoạn hệ thống nếu việc gián đoạn sẽ cắt nguồn cung nhu yếu phẩm sinh tồn trước khi có phương án thay thế;
- bảo vệ tạm thời và các điều kiện chứng nhận theo [Hợp phần B §7 Kết quả chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận) xử lý trường hợp đó;
- quy tắc tương tự áp dụng khi số lần bị giữ lại sau kết luận sai lệch do thiết kế: riêng việc giữ số lần không bao giờ làm gián đoạn hệ thống mà chúng sinh phụ thuộc; và
- trong suốt thời gian giữ lại, diễn đàn nêu rõ biện pháp bảo vệ tạm thời, điều kiện chứng nhận về việc dựa vào hệ thống và thông báo cho người phụ thuộc.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 Xác minh, không chỉ khẳng định

Trạng thái hệ thống, số lần tái chứng nhận sạch và chỉ báo giám sát phải được xác minh; việc xác minh phải cho phép rà soát độc lập. Chỉ lời khẳng định của hệ thống là không đủ:

- Không được chọn hoặc đặt chỉ báo theo cách khiến sai lệch không bao giờ có thể xuất hiện.
- Thiết kế lại cũng phải được xác minh bằng chứng cứ mà người khác có thể kiểm tra.
- Chứng nhận đầy đủ không loại bỏ bất kỳ lý do nào để mở lại rà soát. Mọi yếu tố kích hoạt tại [§9 Tái chứng nhận và mở lại](#9-tái-chứng-nhận-và-mở-lại) vẫn áp dụng.
- Việc né tránh được xử lý theo [§9.4 Không né tránh](#94-không-lẩn-tránh).

<a id="94-non-evasion"></a>

#### 9.4 Không lẩn tránh

**Chống lẩn tránh.** Lẩn tránh nghĩa vụ chương này được quản trị bởi Chương Ba — chương này không nêu lại kỷ luật đó:

- [Chương Ba §1 — Tính toàn vẹn định nghĩa và ràng buộc chống lẩn tránh](core_03_definition_integrity.md#1-tính-toàn-vẹn-định-nghĩa-và-ràng-buộc-chống-lẩn-tránh);
- [Chương Ba §2 — Không tuân thủ từ hành vi hệ thống quan sát được](core_03_definition_integrity.md#2-không-tuân-thủ-từ-hành-vi-hệ-thống-quan-sát-được);
- kể cả lẩn tránh phạm vi-và-ranh-giới dưới [§2.1 Mẫu lẩn tránh thường](core_03_definition_integrity.md#21-mẫu-lẩn-tránh-thường-gặp).

*Ghi đóng:* Không bước nào trong quy trình Phần B này mới hay cực đoan một mình — hồ sơ, công bố, rà, tranh biện, vai trò diễn đàn, mở lại, và đầu vào quỹ đạo là công cụ quản trị quen. Điều khác là **nhất quán**, **giám sát**, và **trách nhiệm giải trình** kéo chúng cùng dưới [Tứ diện Hiến pháp](core_00_preamble.md#constitutional-tetrad): cùng kỷ luật áp xuyên lớp hệ thống và họ diễn đàn, việc vẫn nhìn thấy và dựng lại được, và diễn viên vẫn phải trả lời khi chứng nhận sai, cũ, hoặc lẩn.

<a id="10-challenging-a-certification"></a>

### 10. Khiếu nại chứng nhận

<details>
<summary><strong><span style="color: #2563eb;">Truy nguyên</span></strong></summary>

- Nguồn trước:
  - [Phần B §6.3 Chuỗi khả năng tranh biện](core_09.005_system_alignment_certification_record_process.md#63-chuỗi-khả-năng-bị-phản-biện) (*thứ tự các đường khiếu nại vận hành*);
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận) (*kết quả có thể bị khiếu nại*);
  - [§8](#8-hồ-sơ-chứng-nhận-hệ-thống) (*Hồ sơ Chứng nhận Hệ thống nêu các đường khiếu nại*);
  - [Tứ trụ Hiến pháp](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Điều XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Giải quyết đúng hạn và mức sàn chống trì hoãn*).
- Phần sau: [§9](#9-tái-chứng-nhận-và-mở-lại) (*khiếu nại đáng tin cậy mở lại việc xem xét*); [Chương Mười Lăm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*các đường diễn đàn cho điểm bị tranh chấp*).
- Tiểu mục:
  - [§10.1](#101-khi-nào-con-đường-mở-ra) (*khi nào đường khiếu nại mở*); and
  - [§10.2](#102-các-con-đường-phản-đối) (*các đường khiếu nại*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Định nghĩa · Đánh giá · Tuân thủ</span></strong></summary>

- [khả năng tranh biện](../../core_05.035_band_accountability.md#contestability) · [O](../../core_05.035_band_accountability.md#contestability) · [M](../../core_05.035_band_accountability.md#contestability-a) · [A](../../core_05.035_band_accountability.md#contestability-a) · [C](../../core_05.035_band_accountability.md#contestability-c)

</details>


Hồ sơ Chứng nhận Hệ thống chỉ có tác dụng khi sentient có thể phản đối nếu hồ sơ sai. Khiếu nại phải có thực chất: có thể mở lại việc xem xét, tạm dừng sự phụ thuộc và đến diễn đàn có thẩm quyền với điểm tranh chấp. Hộp thư khiếu nại không làm thay đổi gì là không đủ.

Mục này thuộc tiểu giai đoạn VIa của Giai đoạn VI (Vận hành), cùng với [§9 Tái chứng nhận và mở lại](#9-tái-chứng-nhận-và-mở-lại). Mục này quy định cách bên bị ảnh hưởng khiếu nại Hồ sơ Chứng nhận Hệ thống. Đường khiếu nại hồ sơ đã công bố mở khi kết quả được công bố ([§10.1 Khi nào đường khiếu nại mở](#101-khi-nào-con-đường-mở-ra)).

Theo [Tứ trụ Hiến pháp](../../core_00.000_preamble.md#constitutional-tetrad), [khả năng tranh biện](../../core_05.035_band_accountability.md#contestability) thực hiện trách nhiệm giải trình và giữ sự tham gia rộng mở. Thời hạn khiếu nại theo [Điều XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) thực hiện yêu cầu đúng hạn.

Bên bị ảnh hưởng phải có cách thực sự để khiếu nại. Hồ sơ phải nêu các đường tại §10.2 đủ để tranh biện nội dung, phạm vi, giả định phân loại, việc dựa vào bằng chứng, tính liêm chính của giám sát, kết quả và việc tiếp tục dựa vào hệ thống. Cơ chế phải hoạt động và dễ tiếp cận, không mang tính nghi thức. Khiếu nại phải có thể mở lại xem xét; đình chỉ hoặc giới hạn sự phụ thuộc khi có bằng chứng đáng tin về sai sót trọng yếu hoặc rủi ro liêm chính; và chuyển đến nhóm diễn đàn có thẩm quyền pháp lý. Nghĩa vụ tăng theo loại hệ thống và tác động trọng yếu; không biến mất chỉ vì gắn nhãn thử nghiệm, nội bộ, cá nhân, biệt lập hoặc chỉ kỹ thuật khi vẫn có tác động trọng yếu.

<a id="101-when-the-path-opens"></a>

#### 10.1 Khi nào con đường mở ra

*Nói đơn giản: con đường phản đối phải mở trước khi bất kỳ ai được yêu cầu dựa vào chứng nhận. Với hệ thống chưa hoạt động, con đường mở khi kết quả đầu tiên được công bố. Với hệ thống đang hoạt động, con đường đã mở.*

Khi nào con đường mở và mở trong bao lâu:

- Với hệ thống chưa vận hành, con đường phản đối hồ sơ đã công bố mở khi công bố kết quả chứng nhận đầu tiên, bất kể kết quả là gì. Nhờ đó có thể nộp phản đối và tạm dừng việc dựa vào chứng nhận trước khi hệ thống vận hành theo [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-cổng-đưa-vào-hoạt-động).
- Hệ thống đang hoạt động đã có các bên liên quan. Vì vậy, con đường của nó đã mở hoặc mở khi hồ sơ hệ thống được mở. Điều này bao gồm hệ thống trong thời hạn chuyển tiếp tiếp nhận theo [Article XXVIII-A](../../core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Tiếp nhận theo giai đoạn và duy trì sàn quyền*) và lần chứng nhận sau đó.
- **Các bên liên quan** là sentients chịu ảnh hưởng đáng kể từ hệ thống hoặc phụ thuộc đáng kể vào nó, theo đánh giá xác định chứ không phải do đơn vị vận hành lựa chọn.
- Cho đến khi con đường của hệ thống chưa vận hành mở, Hồ sơ Chứng nhận Hệ thống vẫn nêu tên hệ thống ([Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-trình-tự-giám-sát)). Các con đường về thành phần, liêm chính của đầu mối và leo thang trong [§10.2 Contestability paths](#102-các-con-đường-phản-đối) có hiệu lực suốt quá trình rà soát.
- Con đường vẫn mở khi hệ thống còn các bên liên quan. Nếu có bên liên quan sau khi chứng nhận, việc rà soát mở lại theo [§9 Recertification and Reopening](#9-tái-chứng-nhận-và-mở-lại).
- Tuyên bố hệ thống phù hợp là không có cơ sở khi hệ thống có bên liên quan nhưng không có con đường mở để phản đối Hồ sơ Chứng nhận Hệ thống.

<a id="102-contestability-paths"></a>

#### 10.2 Các con đường phản đối

*Nói đơn giản: Hồ sơ Chứng nhận Hệ thống phải chỉ rõ nơi gửi ý kiến phản đối. Có bước đầu thông thường, rồi đến diễn đàn có thẩm quyền về kết luận bị tranh chấp, con đường dự phòng khi chính diễn đàn đầu mối bị nghi vấn, và con đường leo thang. Nếu chờ đợi có thể gây hại, người phản đối có thể đến thẳng diễn đàn.*

Hồ sơ Chứng nhận Hệ thống phải nêu bốn con đường phản đối dưới đây để bất kỳ ai bị ảnh hưởng biết nơi đưa tranh chấp đến. Các con đường này áp dụng [Dispute sequencing](../../core_15.000_forum.md#dispute-sequencing) của Chapter Fifteen cho Hồ sơ Chứng nhận Hệ thống. Đây là đường dẫn đến diễn đàn, không phải diễn đàn mới; Chapter Fifteen vẫn xác định diễn đàn nào có thẩm quyền. Thứ tự được nêu tại [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-chuỗi-khả-năng-bị-phản-biện).

- **Con đường phản đối hồ sơ đã công bố** — bước đầu thông thường cho tranh chấp thông thường về Hồ sơ Chứng nhận Hệ thống. Hồ sơ nêu ghế tiếp nhận phản đối ([§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-bốn-ghế-trong-một-chứng-nhận)):
  - ai nhận phản đối;
  - cách nộp; và
  - thời hạn theo [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Sàn giải quyết kịp thời và chống trì hoãn*) bắt đầu khi nhận được.

  Rà soát nội bộ của đơn vị vận hành, xác nhận của nhà cung cấp hoặc phê duyệt kỹ thuật không phải con đường này.
- **Con đường diễn đàn thành phần** — phản đối một kết luận trong Hồ sơ Chứng nhận Hệ thống sẽ được chuyển đến nhóm diễn đàn Chapter Fifteen có thẩm quyền đối với kết luận đó.
- **Con đường liêm chính của đầu mối** — phản đối cách diễn đàn đầu mối điều hành quy trình, chẳng hạn bị chi phối, che giấu thông tin, tự rà soát công việc của mình hoặc tuyên bố hoàn tất chứng nhận quá sớm. Con đường này qua Integrity routing, có diễn đàn dự phòng để diễn đàn đầu mối không tự xét mình.
- **Con đường leo thang** — chuyển tranh chấp đến diễn đàn khác hoặc cao hơn theo Chapter Fifteen. Bao gồm chuyển giao, gửi câu hỏi cho diễn đàn khác quyết định, định tuyến dự phòng hoặc leo thang giữa các nhóm diễn đàn. Áp dụng khi lợi ích chính thuộc nơi khác, tính hợp hiến bị đặt vấn đề, cần sửa chữa cơ cấu, hai nhóm diễn đàn bế tắc hoặc diễn đàn sẽ phải tự xét mình.

Quyền tiếp cận trực tiếp con đường diễn đàn vẫn tồn tại khi sự chậm trễ có thể gây nguy hiểm đáng kể cho quyền, chứng cứ, tính độc lập hoặc khả năng khôi phục thực tế. Việc chưa hoàn tất con đường phản đối hồ sơ đã công bố không được cản trở các con đường diễn đàn hoặc làm hết thời hạn theo [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor).

<a id="11-relationship-to-standing"></a>

### 11. Quan hệ với quỹ đạo

<details>
<summary><strong>Truy nguyên</strong></summary>

- Nguồn trước:
  - [Part B §6](core_09.005_system_alignment_certification_record_process.md#6-quy-trình-diễn-đàn) through
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-kết-quả-chứng-nhận) (*quy trình diễn đàn, Hồ sơ Chứng nhận Hệ thống và kết quả*);
  - [Constitutional Tetrad](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Verified Inputs for Standing](../../core_05.035_band_accountability.md#verified-inputs-for-standing).
- Phần sau: [Chương Mười Một](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (*hồ sơ quỹ đạo và cổng đầu vào đã xác minh*); [Chương Mười Ba](../../core_13.000_standing_integration.md#chapter-thirteen-standing-effects-and-integration) (*ảnh hưởng và tích hợp quỹ đạo*).
- Đọc cùng: **Article III-A** (*tiếp cận nhu yếu phẩm sinh tồn khi chứng nhận chặn việc cung cấp*).
- Tiểu mục:
  - [§11.1](#111-chứng-nhận-có-thể-cung-gì--dưới-hai-mục-tiêu-hiến-pháp-và-chỉ-qua-cổng-đầu-vào-đã-xác-minh-của-chương-tám-bên-dưới) (*Hồ sơ Chứng nhận Hệ thống có thể chuyển gì vào quỹ đạo*);
  - [§11.2](#112-dù-kết-quả-nào-hệ-thống-cung-cấp-đầu-vào-quỹ-đạo-từ-hồ-sơ-chứng-nhận-hệ-thống-chứng-nhận-tạm-thời-hoặc-đầy-đủ-có-hoặc-không-có-điều-kiện-chứng-nhận-có-điều-kiện-hoặc-hoãn-từ-chối-rút-hết-hạn-hoặc-kết-quả-khác-điều-này-bao-gồm-chứng-nhận-lần-đầu-và-hệ-thống-chưa-từng-được-chứng-nhận-các-phát-hiện-trong-quy-trình-chứng-nhận-cung-cấp-đầu-vào-quỹ-đạo-theo-cùng-điều-kiện-ở-lượt-đầu-và-các-lượt-sau-việc-rút-hết-hạn-hoặc-mất-chứng-nhận-theo-cách-khác-không-loại-bỏ-sự-kiện-đã-xác-minh-phát-sinh-trong-thời-gian-hệ-thống-được-chứng-nhận-mọi-đầu-vào-đều-chịu-cổng-đầu-vào-đã-xác-minh-dưới-đây) (*mọi kết quả chứng nhận*);
  - [§11.3](#113-cổng-đầu-vào-đã-xác-minh-một-hồ-sơ-chứng-nhận-chỉ-được-nuôi-quỹ-đạo-chương-tám-khi-nó-có-giới-hạn-truy-vết-được-tranh-biện-được-và-đã-xác-minh-dưới) (*cổng đầu vào đã xác minh*);
  - [§11.4](#114-hồ-sơ-tư-cách-đóng-góp) (*hồ sơ quỹ đạo đóng góp*); và
  - [§11.5](#115-hồ-sơ-tư-cách-vi-phạm) (*hồ sơ quỹ đạo vi phạm*).

</details>


*Nói thẳng: chứng nhận có thể nuôi quỹ đạo, nhưng nó không phải quỹ đạo. Hồ sơ chứng nhận tốt hay xấu có thể cung sự kiện đã xác minh cho Chương Tám — chỉ qua một cổng nghiêm — và chỉ Chương Tám và Chín quyết hồ sơ quỹ đạo và hiệu ứng.*

<a id="111-what-a-system-certification-record-can-pass-on-to-standing"></a>

#### 11.1 **Chứng nhận có thể cung gì** — dưới [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims), và chỉ qua cổng đầu vào đã xác minh của Chương Tám bên dưới:

- Hồ sơ xác minh thẳng hàng khớp Sàn Quyền có thể cung đầu vào phía **Hưng thịnh** đã xác minh;
- Hồ sơ ghi phân loại sai, khiếm khuyết giấu, hoặc vận hành đánh bại sàn có thể cung đầu vào phía **Trách nhiệm giải trình** đã xác minh.

<a id="112-every-certification-outcome"></a>

#### 11.2 Dù kết quả nào, hệ thống cung cấp đầu vào quỹ đạo từ Hồ sơ Chứng nhận Hệ thống: chứng nhận tạm thời hoặc đầy đủ (có hoặc không có điều kiện), chứng nhận có điều kiện hoặc hoãn, từ chối, rút, hết hạn hoặc kết quả khác. Điều này bao gồm chứng nhận lần đầu và hệ thống chưa từng được chứng nhận. Các phát hiện trong quy trình chứng nhận cung cấp đầu vào quỹ đạo theo cùng điều kiện ở lượt đầu và các lượt sau. Việc rút, hết hạn hoặc mất chứng nhận theo cách khác không loại bỏ sự kiện đã xác minh phát sinh trong thời gian hệ thống được chứng nhận. Mọi đầu vào đều chịu cổng đầu vào đã xác minh dưới đây.

Kết luận rằng hệ thống chưa phù hợp tự nó không phải là vi phạm. Lượt chứng nhận nhằm tìm và sửa vấn đề. Kết luận vi phạm khó xảy ra khi bên vận hành nhất quán, thiện chí hướng tới sự phù hợp và không sơ suất. Đầu vào quỹ đạo cần sự kiện hỗ trợ phân loại bất lợi và quy trách nhiệm cho tác nhân cụ thể ([§11.5 Hồ sơ quỹ đạo vi phạm](#115-hồ-sơ-tư-cách-vi-phạm)); kết luận sẵn sàng rằng bên vận hành muốn nhưng không thể sửa vấn đề không cung cấp các sự kiện đó ([Phần B §7.5 Hậu quả của việc từ chối và thu hồi](core_09.005_system_alignment_certification_record_process.md#75-hệ-quả-của-việc-từ-chối-và-thu-hồi)). Không điều nào trong đây bao gồm sơ suất, che giấu hoặc bằng chứng sai.

<a id="113-verified-input-gate"></a>

#### 11.3 **Cổng đầu vào đã xác minh.** Một hồ sơ chứng nhận chỉ được nuôi quỹ đạo Chương Tám khi nó có giới hạn, truy vết được, tranh biện được, và đã xác minh dưới:

- [§2](core_07_a_system_alignment_certification_evaluation.md#2-đánh-giá-lớp-hệ-thống) (*lớp hệ thống*);
- [§4](core_07_a_system_alignment_certification_evaluation.md#34-đánh-giá-loại-dữ-liệu-và-cách-xử-lý) (*loại dữ liệu và xử lý*);
- [§5](core_07_a_system_alignment_certification_evaluation.md#51-đánh-giá-dấu-chân-sinh-thái) nơi có trọng;
- [§6](core_07_a_system_alignment_certification_evaluation.md#53-đánh-giá-hỗ-trợ-liên-hệ-thống-tương-xứng) nơi cò trọng yếu **Điều IV** (*Phân bổ tài nguyên, phụ thuộc, và tài trợ hệ sinh thái*) áp dụng;
- [§7](core_07_a_system_alignment_certification_evaluation.md#54-đánh-giá-không-phân-biệt-đối-xử) nơi cò trọng yếu **Điều V-B** (*Không phân biệt đối xử*) áp dụng;
- [§8](core_07_a_system_alignment_certification_evaluation.md#55-đánh-giá-khả-năng-tiếp-cận) nơi cò trọng yếu **Điều V-G** (*Khả năng tiếp cận*) áp dụng;
- [§9](core_07_a_system_alignment_certification_evaluation.md#52-đánh-giá-năng-lực-giáo-dục-và-tính-toàn-vẹn-của-hệ-thống-học-tập) nơi cò trọng yếu **Điều VI** (*Quyền giáo dục lấy hữu tri làm trung tâm*) áp dụng;
- [§10](core_07_a_system_alignment_certification_evaluation.md#56-đánh-giá-độ-tin-cậy-và-tính-toàn-vẹn-của-sự-dựa-vào-hệ-thống) nơi cò trọng yếu **Điều XIII** (*Quyền đối với hệ thống đáng tin và đáng tin cậy*) áp dụng;
- [§12](#82-tính-minh-bạch-và-khả-năng-kiểm-toán-của-hồ-sơ-chứng-nhận-hệ-thống) và [§14](#10-khiếu-nại-chứng-nhận);
- Chương Hai đến Bốn, và quy trình Chương Mười Một áp dụng.

<a id="114-contribution-standing-record"></a>

#### 11.4 Hồ sơ tư cách đóng góp

Chứng nhận tích cực, xác nhận, tái chứng nhận, hoàn tất khắc phục hoặc hoàn thành hay được miễn một điều kiện chứng nhận có thể cung cấp dữ liệu đầu vào đã xác minh cho **hồ sơ tư cách đóng góp** khi cho thấy:

- lợi ích hiến định;
- sự quản lý có năng lực;
- mức độ sẵn sàng ủy quyền an toàn;
- tối ưu hóa hệ thống;
- sự cần mẫn; hoặc
- sự phù hợp với hiến định.

<a id="115-violation-standing-record"></a>

#### 11.5 Hồ sơ tư cách vi phạm

Các mục sau trong Hồ sơ Chứng nhận Hệ thống có thể cung cấp dữ liệu đầu vào đã xác minh cho **hồ sơ tư cách vi phạm** khi sự kiện hỗ trợ việc phân loại bất lợi và quy trách nhiệm cụ thể cho tác nhân:

- thu hồi chứng nhận;
- phân loại sai bị che giấu;
- tái chứng nhận không đạt;
- kiểm thử hồi quy không đạt hoặc bị thiếu trong lần tái chứng nhận khi được yêu cầu;
- bằng chứng chứng nhận gian lận;
- vi phạm trọng yếu một điều kiện chứng nhận;
- hoạt động đã xác minh ngoài phạm vi được chứng nhận;
- hạ tầng mong manh không phù hợp với loại hệ thống; và
- khiếm khuyết trọng yếu trong một đánh giá Phần A bắt buộc, gồm:
  - khiếm khuyết xử lý dữ liệu theo [§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-đánh-giá-loại-dữ-liệu-và-cách-xử-lý);
  - khiếm khuyết đánh giá hoặc công khai rủi ro khi rủi ro hệ thống nằm trong phạm vi, theo [§3.2.2 Defects and Misalignment](core_09.000_system_alignment_certification_evaluation.md#322-sai-sót-và-sai-lệch);
  - trình bày sai dấu chân sinh thái khi phải công khai theo [§5.1 Ecological Footprint Evaluation](core_09.000_system_alignment_certification_evaluation.md#51-đánh-giá-dấu-chân-sinh-thái);
  - khiếm khuyết về không phân biệt đối xử hoặc phân biệt đối xử qua đại diện theo [§5.4 Nondiscrimination Evaluation](core_09.000_system_alignment_certification_evaluation.md#54-đánh-giá-không-phân-biệt-đối-xử);
  - khiếm khuyết về khả năng tiếp cận hoặc tham gia thực chất theo [§5.5 Accessibility Evaluation](core_09.000_system_alignment_certification_evaluation.md#55-đánh-giá-khả-năng-tiếp-cận);
  - khiếm khuyết về năng lực giáo dục, sự không minh bạch trong đánh giá, kiểm soát bằng chứng chỉ hoặc lỗi thời bị áp đặt theo [§5.2 Educational Capability and Learning-System Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#52-đánh-giá-năng-lực-giáo-dục-và-tính-toàn-vẹn-của-hệ-thống-học-tập); hoặc
  - khiếm khuyết về độ đáng tin cậy, niềm tin giả, động cơ sai lệch, khiếu nại không thể tiếp cận hoặc tính toàn vẹn của việc khôi phục theo [§5.6 Trustworthiness and System-Reliance Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#56-đánh-giá-độ-đáng-tin-và-tính-toàn-vẹn-của-sự-phụ-thuộc-vào-hệ-thống).
