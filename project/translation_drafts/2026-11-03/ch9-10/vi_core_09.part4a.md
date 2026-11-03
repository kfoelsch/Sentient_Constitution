##### 5.3.4 Tính toàn vẹn của Bản đồ và Hồ sơ

Trước khi dựa vào bản đồ sự phụ thuộc và hồ sơ luồng tài nguyên, chứng nhận phải kiểm tra xem chúng có đáp ứng **Điều V-A** (*Lập bản đồ Sự phụ thuộc và Minh bạch Luồng Tài nguyên*) hay không. Chúng phải:

- **Đầy đủ:** bao quát các sự phụ thuộc đáng kể ở thượng nguồn và hạ nguồn, các luồng tài nguyên và mọi quan hệ bị che khuất hoặc mất cân bằng khi những nội dung đó có ý nghĩa.
- **Cập nhật:** được cập nhật đủ thường xuyên xét theo tốc độ thay đổi và mức độ trọng yếu của hệ thống, kể cả lớp hệ thống theo [§2 Đánh giá Lớp Hệ thống](#2-system-class-evaluation). Bản đồ thể hiện hệ thống đang vận hành hiện nay, không phải cách hệ thống vận hành vào lần chứng nhận trước.
- **Có thể kiểm toán:** cho phép kiểm toán theo **Điều XVI-A** (*Khả năng Kiểm toán và Bằng chứng Có thể Quan sát*).

Bản đồ hoặc hồ sơ không vượt qua bất kỳ phép thử nào trong số này không thể làm căn cứ cho kết luận rằng hệ thống hoàn trả đủ. Phải ghi lại thiếu sót và xử lý theo phần *Sai sót và sai lệch* bên dưới.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 Điều chỉnh và Nâng cấp Xử lý theo Lớp Hệ thống

Lớp của hệ thống quyết định mức độ sâu của việc rà soát và mức độ chặt chẽ khi đánh giá tính đầy đủ. Lớp hệ thống không bao giờ khiến việc khai thác tài nguyên dùng chung không còn đáng kể; việc khai thác được chia giữa nhiều đơn vị, hồ sơ hoặc giai đoạn được đánh giá như một hoạt động thống nhất theo [Chương Một §15.1.1 Nguyên tắc Chống Chia tách](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle). Mỗi khi gatilho trọng yếu được đáp ứng:

- Hệ thống dựa vào nền tảng dùng chung mà hữu tri cần để sinh tồn — chẳng hạn lưu vực nước dùng chung hoặc trục xương sống của lưới điện khu vực — phải ghi vào hồ sơ bằng chứng mạnh nhất về bản đồ sự phụ thuộc và luồng hoàn trả. Đây là các hệ thống dùng chung có năng lực lâu dài được [Chương Một §9 Năng lực Hệ thống Dùng chung](core_01.000_values_principles.md#9-shared-system-capacity) bảo vệ, và **Điều III-A** (*Sinh tồn*) là lý do cần bằng chứng mạnh nhất ở đây.
- Hệ thống dựa vào cơ sở hạ tầng xác thực dùng chung, CNTT y tế hoặc cơ sở hạ tầng tương tự phải ghi lại những gì mình khai thác và mức hỗ trợ có đầy đủ hay không, với độ sâu tương xứng với mức độ trọng yếu của hoạt động. Khẩu hiệu mơ hồ về “khả năng tương tác” không được tính: sự phụ thuộc phải thể hiện rõ trong bản đồ và hồ sơ, theo yêu cầu của [Chương Một §18.5 Kiến trúc Mô-đun và Kỷ luật Sự phụ thuộc](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline).
- Hệ thống không được né tránh rà soát liên hệ thống trong khi âm thầm trở thành điểm nghẽn về thanh toán, danh tính hoặc nhân sự của các tổ chức không thể chuyển đổi nhà cung cấp một cách thực tế.
  - **Ai không thể chuyển đổi:** đánh giá theo các yếu tố về khả năng thay thế tại [§5.3.3 Yêu cầu Đánh giá](#533-evaluation-requirement).
  - **Vì sao điều đó quan trọng:** đây là dạng tập trung được mô tả trong [Chương Một §11.4 Tập trung Tài nguyên và Sự phụ thuộc](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Mục đó yêu cầu bên tiếp nhận đặt ngưỡng cho tình trạng này, chẳng hạn số hữu tri hoặc hệ thống phải phụ thuộc vào một nhà cung cấp duy nhất mà không có phương án thay thế thực chất, hoặc chủ thể nào kiểm soát giao diện và điểm truy cập vào cơ sở hạ tầng dùng chung. Chứng nhận không đợi vượt ngưỡng do bên tiếp nhận đặt ra mới tăng mức độ rà soát (xem bên dưới).
  - **Chứng nhận phải làm gì:** tăng mức độ rà soát và xem xét lại lớp hệ thống theo [§2.2 Cách Lớp Hệ thống Điều chỉnh Mọi Đánh giá](#22-how-system-class-scales-every-evaluation), tối đa lên **Lớp A** khi hệ thống kiểm soát quyền tiếp cận hoạt động phối hợp thiết yếu cho sinh tồn.

Việc nâng cấp xử lý không chờ vượt ngưỡng tập trung theo [Chương Một §11.4 Tập trung Tài nguyên và Sự phụ thuộc](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Ngưỡng do bên tiếp nhận đặt ra mà hệ thống đã vượt qua là bằng chứng bổ sung. Ngưỡng chưa được đặt hoặc đặt quá cao không trì hoãn việc nâng cấp; việc vượt ngưỡng tự nó không đồng nghĩa với kết luận có hành vi sai trái.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 Sai sót và Sai lệch

Các sai sót tại [§5](#5-rights-floor-and-domain-evaluations) (*Đánh giá Sàn Quyền và Lĩnh vực*) áp dụng cho đánh giá này, kể cả đối với thông tin về sự phụ thuộc hoặc luồng tài nguyên mà **Điều V-A** (*Lập bản đồ Sự phụ thuộc và Minh bạch Luồng Tài nguyên*) yêu cầu hệ thống công bố. Ngoài ra, mỗi trường hợp sau đây đều được tính là sai sót chứng nhận:

- coi bất kỳ điều nào sau đây là đủ để đáp ứng [Hỗ trợ Liên Hệ thống Tương xứng](core_05.040_band_continuity.md#proportionate-cross-system-support):
  - chuyển giao mang tính hình thức, không minh bạch, không có trong bản đồ hoặc chỉ diễn ra một lần;
  - hệ thống đáp ứng chuẩn sàn sinh tồn theo **Điều III-A** (*Sinh tồn*); hoặc
  - hệ thống nằm trong giới hạn tập trung thị trường tại [Chương Một §11 Cấu trúc Thị trường](core_01.000_values_principles.md#11-market-structure);
- liên tục khai thác nền tảng dùng chung mà không hoàn trả tương xứng khi gatilho trọng yếu được đáp ứng;
- hỗ trợ chủ yếu củng cố sự chiếm dụng hoặc tập trung quyền lực; và
- hỗ trợ kèm điều kiện nhằm vô hiệu hóa tính minh bạch theo yêu cầu của **Điều V-A** (*Lập bản đồ Sự phụ thuộc và Minh bạch Luồng Tài nguyên*).

Thiếu sót hỗ trợ được ghi lại sẽ được tính theo [Chương Một §6 Niềm tin và Độ đáng tin](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Đánh giá Không phân biệt đối xử

<details>
<summary><strong><span style="color: #2563eb;">Truy xuất nguồn gốc</span></strong></summary>

- Thượng nguồn:
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*nội dung hồ sơ*);
  - [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường Sự tham gia (*Công bằng Thực chất và việc Dùng Đặc điểm được Bảo vệ làm Biến Đại diện cùng Tác động Khác biệt như một thước đo hiến pháp*); **Điều VI-C** (*Không phân biệt đối xử*);
  - [Công bằng Thực chất](core_05.055_band_participation.md#substantive-fairness),
  - [Đặc điểm được Bảo vệ](core_05.055_band_participation.md#protected-characteristics),
  - [Dùng Đặc điểm được Bảo vệ làm Biến Đại diện và Tác động Khác biệt](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Ngôn ngữ, Văn hóa và Di sản](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Tính cần thiết](core_05.035_band_accountability.md#necessity), và
  - [Tính tương xứng](core_05.035_band_accountability.md#proportionality) (Chương Năm).
- Thượng nguồn: Nguyên tắc: Chương Một
  - [§3.1 Công bằng](core_01.000_values_principles.md#31-fairness) (đặc biệt là [§3.1.2 Lợi ích và Gánh nặng](core_01.000_values_principles.md#312-benefits-and-burdens)) và
  - [§11.4 Tập trung Tài nguyên và Sự phụ thuộc](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*kiểm soát điều kiện; việc nâng cấp xử lý tại §5.4.2*).
- Hạ nguồn:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Áp dụng không phân biệt đối xử minh họa theo lớp hệ thống*);
  - [Phần C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*tính toàn vẹn của hồ sơ*);
  - [Phần C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*yêu cầu dữ liệu đã xác minh*);
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*sai lệch theo mô hình phân biệt đối xử và né tránh qua biến đại diện*).
- Đọc cùng với: nghĩa vụ phân xử và vận hành theo **Điều VI-C** (*Không phân biệt đối xử*) khi chứng nhận là điều kiện tiếp cận diễn đàn, hành chính hoặc thực thi; [*Không phân biệt đối xử, Đặc điểm được Bảo vệ, Phẩm giá, Kiểm soát Điều kiện theo Tín hiệu Thân mật và Trạng thái theo **Điều VII-E** (*Dịch vụ tình dục thương mại có sự đồng thuận giữa người trưởng thành và bóc lột tình dục*)*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Các tiểu mục:
  - [§5.4.1](#541-evaluation-requirement) (*yêu cầu đánh giá*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*điều chỉnh và nâng cấp xử lý theo lớp hệ thống*);
  - [§5.4.3](#543-defects-and-misalignment) (*sai sót và sai lệch*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Áp dụng không phân biệt đối xử minh họa theo lớp hệ thống*).

</details>

<br>

*Nói thẳng: một số hệ thống quyết định ai được tiếp cận. Một số quyết định ai phải trả nhiều hơn. Một số quyết định ai bị xếp hạng thấp hơn hoặc phải gánh nặng hơn. Khi hệ thống đưa ra các quyết định như vậy theo cách có ý nghĩa trọng yếu, chứng nhận đặt ra một câu hỏi: tổn hại chủ yếu rơi vào các hữu tri có đặc điểm được bảo vệ, hay vào các đặc điểm thay thế cho những đặc điểm đó? Lời khẳng định của đơn vị vận hành rằng quy tắc của mình trung lập không trả lời được câu hỏi này. Ví dụ thực hành: [CS-9.320 §9 Áp dụng không phân biệt đối xử minh họa theo lớp hệ thống](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class).* 

Mục này áp dụng khi một hệ thống có tác động trọng yếu phân loại, xếp hạng, định giá, kiểm soát điều kiện, loại trừ hoặc phân bổ gánh nặng và lợi ích giữa các hữu tri theo cách có ý nghĩa trọng yếu — bao gồm thông qua quy tắc về điều kiện, đặc tính mô hình, logic xếp hạng, chính sách nền tảng hoặc lộ trình quyết định tương tự.

Khi gatilho trọng yếu được đáp ứng, chứng nhận mức độ phù hợp của hệ thống phải đánh giá **việc không phân biệt đối xử** theo **Điều VI-C** (*Không phân biệt đối xử*), [Công bằng Thực chất](core_05.055_band_participation.md#substantive-fairness) và [Dùng Đặc điểm được Bảo vệ làm Biến Đại diện và Tác động Khác biệt](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

<a id="541-evaluation-requirement"></a>
##### 5.4.1 Yêu cầu Đánh giá

*Nói thẳng: chương này không đặt hạn ngạch hòa nhập. Chương này không chọn công thức công bằng. Tài liệu khác có thể quy định những điều đó, cũng như các nội dung bổ sung sau này của kho văn bản hoặc tài liệu do bên tiếp nhận soạn thảo. Chứng nhận chỉ kiểm tra xem có ai thực sự xem xét ai nhận được lợi ích, ai gánh chịu gánh nặng và liệu có dùng đặc điểm thay thế cho đặc điểm được bảo vệ hay không. Đánh giá này áp dụng ở mọi nơi đáp ứng gatilho.*

Quy trình chứng nhận phải xác định liệu các lộ trình quyết định mà hệ thống dựa vào ở mức trọng yếu có áp đặt gánh nặng, loại trừ hoặc tổn hại trọng yếu lên hữu tri dựa trên bất kỳ căn cứ nào sau đây hay không:

- [Đặc điểm được Bảo vệ](core_05.055_band_participation.md#protected-characteristics);
- các biến đại diện của chúng; hoặc
- các nhóm tùy tiện được sử dụng làm vật thay thế về chức năng, bao gồm chuyên biệt hóa ngôn ngữ, văn hóa và di sản theo [Ngôn ngữ, Văn hóa và Di sản](core_05.040_band_continuity.md#language-culture-and-heritage).

Đánh giá phải tương xứng với [lợi hại vật chất](core_00.000_preamble.md#material-stake), và phải:

- kiểm tra mô hình gánh nặng và lợi ích theo [Công bằng Thực chất](core_05.055_band_participation.md#substantive-fairness); và
- kiểm tra rủi ro dùng đặc điểm làm biến đại diện hoặc tác động khác biệt theo [Dùng Đặc điểm được Bảo vệ làm Biến Đại diện và Tác động Khác biệt](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

Chỉ chấp nhận cách đối xử khác biệt khi được chứng minh bằng [Tính cần thiết](core_05.035_band_accountability.md#necessity), [Tính tương xứng](core_05.035_band_accountability.md#proportionality) và công bằng thực chất đã ghi lại. Đánh giá phải phản ánh hiệu ứng chức năng, không chỉ sự trung lập danh nghĩa, ý định được tuyên bố hoặc nhãn gọi.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 Điều chỉnh và Nâng cấp Xử lý theo Lớp Hệ thống

Lớp hệ thống quyết định mức độ sâu của việc đánh giá. Lớp hệ thống không cho phép coi việc xếp hạng hoặc chuyển gánh nặng là không trọng yếu. Khi gatilho trọng yếu được đáp ứng, áp dụng các nội dung sau:

- **Hệ thống có quy tắc ngắt, thông báo hoặc quy tắc tương tự có thể làm mất quyền tiếp cận nhu cầu thiết yếu cho sinh tồn:**
  - hồ sơ phải có phân tích mạnh nhất về gánh nặng, lợi ích và biến đại diện, không chỉ là tuyên bố chung chung về thông lệ tốt; và
  - chuyển chi phí ẩn không đáp ứng [Chương Một §3.1.2 Lợi ích và Gánh nặng](core_01.000_values_principles.md#312-benefits-and-burdens).
- **Hệ thống có logic ghép nối hoặc định tuyến ảnh hưởng tới chăm sóc khẩn cấp, trợ cấp hoặc quyền tiếp cận chứng chỉ:**
  - hồ sơ phải ghi lại kết luận về tác động khác biệt và công bằng thực chất ở mức độ trọng yếu về vận hành; và
  - lý do là công bằng theo [Chương Một §3.1 Công bằng](core_01.000_values_principles.md#31-fairness) có nghĩa hữu tri không bị đối xử theo quy tắc không được giải thích hoặc bị buộc gánh chi phí mà người khác tránh được.
- **Hệ thống có logic phân ca, nhà cung cấp hoặc đặt lịch xếp hạng hay loại người tham gia ở mức trọng yếu:**
  - hệ thống không được dùng một đoạn văn hình thức về công bằng thay cho phân tích thực chất;
  - khi phối hợp trở thành yếu tố thiết yếu cho sinh tồn, chứng nhận phải tăng cường rà soát và phân loại lại theo [§2.2 Cách Lớp Hệ thống Điều chỉnh Mọi Đánh giá](#22-how-system-class-scales-every-evaluation), bao gồm phân loại lại thành **Lớp A** khi hệ thống kiểm soát nhân sự hoặc định tuyến khẩn cấp; và
  - việc kiểm soát điều kiện kiểu này là chỉ dấu tập trung theo [Chương Một §11.4 Tập trung Tài nguyên và Sự phụ thuộc](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable), vì nhiều hữu tri hoặc hệ thống phụ thuộc vào một nhà cung cấp duy nhất mà không có phương án thay thế thực chất; đó là lý do chứng nhận tăng mức độ rà soát ở đây.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 Sai sót và Sai lệch

Hai nhóm sai sót áp dụng cho đánh giá này:

- **Sai sót áp dụng cho toàn mục:**
  - các sai sót tại [§5](#5-rights-floor-and-domain-evaluations) (*Đánh giá Sàn Quyền và Lĩnh vực*) áp dụng cho đánh giá này; và
  - chúng áp dụng cho logic phân loại, xếp hạng hoặc phân bổ gánh nặng có ý nghĩa trọng yếu khi **Điều VI-C** (*Không phân biệt đối xử*) yêu cầu rà soát.
- **Sai sót về không phân biệt đối xử:** mỗi trường hợp sau đây cũng phải được xử lý như một sai sót chứng nhận:
  - coi vẻ ngoài trung lập, chỉ số tiện lợi tổng hợp hoặc báo cáo của chính đơn vị vận hành là đủ mà không có phân tích đánh giá được về gánh nặng và lợi ích; và
  - viện dẫn sự đồng nhất hóa, khả năng tương tác hoặc hiệu quả để vô hiệu hóa biện pháp bảo vệ ngôn ngữ, văn hóa hoặc di sản mà không đáp ứng các phép thử về **Tính cần thiết** và **Tính tương xứng** của **Điều VI-C** (*Không phân biệt đối xử*).

Phân biệt đối xử qua biến đại diện hoặc bất công thực chất được ghi lại sẽ được tính theo [Chương Một §6 Niềm tin và Độ đáng tin](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="55-accessibility-evaluation"></a>
