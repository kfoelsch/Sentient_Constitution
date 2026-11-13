<!-- Bản dịch nháp một phần sang tiếng Việt. Nguồn: core_12.000_standing_measurement.md; snapshot nguồn: 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Do AI soạn; chưa được rà soát. Phạm vi một phần: §§1–3. -->

### 1. Câu hỏi 2 — điều đó tốt hay xấu đến mức nào?
<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Nguồn trước: [Chương Mười Một §2](core_11.000_standing_assessment.md#2-question-1--what-happened) (*Câu hỏi 1 — hồ sơ địa vị và sự kiện đã xác minh*); [Chương Mười Một §2.5](core_11.000_standing_assessment.md#25-verified-input-gate) (*cổng dữ liệu đã xác minh*); [Chương Mười Một §4](core_11.000_standing_assessment.md#4-standing-record-operational-requirements) (*yêu cầu hồ sơ*); [Chương Mười Một §1](core_11.000_standing_assessment.md#1-the-three-questions) (*khung ba câu hỏi*).
- Nguồn sau:
  - [§2](#2-magnitude-and-severity-input-dimensions) (*các chiều dữ liệu đầu vào đo lường cho cả hai trục*);
  - [§3](#3-route-descriptor-catalogs-and-measurement-roles) (*danh mục mô tả tuyến*);
  - [§4](#4-slot-grammar-and-shared-scaling) (*ngữ pháp ô và phép co giãn dùng chung*);
  - [§5](#5-constitutional-inputs-to-axis-assignment) (*chuyển tuyến nguồn hiến pháp*);
  - [§6](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) (*phân ô trên Trục Đóng góp và Trục Vi phạm*);
  - [§7](#7-standard-contribution-measures) (*phép đo đóng góp tiêu chuẩn do bên tiếp nhận công bố*);
  - [§8](#8-measurement-illustrations) (*ví dụ đo lường thực tiễn*);
  - [§9](#9-hand-off-to-question-3--cross-question-measurement-hooks) (*chuyển tiếp sang Câu hỏi 3*);
  - [Chương Mười Ba §6.2](core_13.000_standing_integration.md#62-competency-bars-and-clearances) (13.000 §6.2) (*Câu hỏi 3 về đóng góp — ủy quyền an toàn*);
  - [Chương Mười Ba §4.2](core_13.000_standing_integration.md#42-prevention--general-standing-locks) (13.000 §4.2) (*các khóa phòng ngừa*);
  - [Chương Mười Ba §5](core_13.000_standing_integration.md#5-lock-design-and-enforcement) (13.000 §5) (*thiết kế và thực thi khóa*).
- Đọc cùng: [Chương Mười Một §4.1](core_11.000_standing_assessment.md#41-minimum-record-contents) (*các trường hồ sơ địa vị đã xác minh; Chương Mười Một không tạo hiệu ứng địa vị*).

</details>

<br>

*Nói đơn giản: Câu hỏi 2 đo lường các sự kiện đã xác minh của Câu hỏi 1. Câu hỏi này hỏi **đóng góp tốt đến mức nào** hoặc **vi phạm nghiêm trọng đến mức nào**. Đây là nơi chương lần đầu giới thiệu hai trục đo lường chính thức: **Trục Đóng góp** đối với trợ giúp đã xác minh và **Trục Vi phạm** đối với tổn hại đã xác minh. Hai trục vẫn tách biệt; chúng không phải hai mặt của một điểm số ròng.*

Để quyết định đóng góp hoặc vi phạm của ai thuộc ô nào, chương này đo lường tác động bằng **Đơn vị Tương đương Tuổi thọ (LEQU)**. Một LEQU tương đương gần đúng với việc cứu sống hoặc hủy hoại toàn bộ cuộc đời sung túc của một hữu tri. Đây không phải việc đếm số người hay số tiền; câu hỏi là liệu hành động có làm thay đổi đáng kể mức sung túc của cộng đồng hiến pháp hay không. Cùng một đơn vị áp dụng cho mọi hữu thể hữu tri, dù là con người hay không.

#### 1.1 Mốc cơ sở LEQU

**Đơn vị Tương đương Tuổi thọ** (**LEQU**) là đơn vị viết tắt cho lợi ích hoặc tổn thất hiến pháp tương đương một cuộc đời trọn vẹn, khi triển khai được tiếp nhận cần hiệu chỉnh bằng số.

- Đơn vị này không phụ thuộc vào nền tảng vật chất.
- Bên tiếp nhận hiện tại có thể dùng tuổi thọ thông thường của con người làm ví dụ hiệu chỉnh trong bối cảnh sinh học của con người, nhưng mốc ràng buộc là hữu tri và hiến pháp, không gắn với loài.

**Lợi ích hiến pháp tương đương một cuộc đời trọn vẹn** là lợi ích đã xác minh tương đương với việc bảo tồn, phục hồi hoặc giải phóng trọn một tuổi đời của hữu tri với mức sung túc đáng kể và phù hợp với quyền. **Tổn thất hiến pháp tương đương một cuộc đời trọn vẹn** là tổn hại, lãng phí, hủy hoại, tước mất lựa chọn, tước đoạt hoặc hiện thực hóa rủi ro đã xác minh, tương đương với việc hủy hoại, tiêu hao sai trái hoặc ngăn cản một lợi ích hiến pháp tương đương trọn một cuộc đời.

#### 1.2 Giới hạn khi dùng LEQU

Các giới hạn sau áp dụng mỗi khi dùng LEQU.

- **Không phải quy tắc tính điểm ròng:** Không thể «bù trừ» vi phạm bằng đóng góp hoặc ngược lại. Mỗi trục đứng riêng.
- **Không phải thước đo bắt buộc dựa trên đời người:** LEQU áp dụng chung cho hữu tri; áp dụng với mọi hữu thể có ý thức, không chỉ con người.
- **Không phải thước đo cáo buộc:** Cáo buộc, thẻ tiếp nhận, quyết định định tuyến, danh tiếng, địa vị bị bất lợi hoặc ác cảm đạo đức không cung cấp lợi ích cho Trục Đóng góp hay mức độ nghiêm trọng cho Trục Vi phạm nếu không có dữ liệu đầu vào đã xác minh theo **Chương Mười Một §2.5** và hiệu chỉnh theo **§6**.
- **Không phải giấy phép đánh đổi quyền:** Những tuyên bố được diễn đạt như hiệu quả, năng lực sản xuất, đổi mới, giảm gánh nặng, an ninh, trả đũa, ứng phó khẩn cấp hoặc nhu cầu thể chế phải bị giảm trọng số hoặc bác bỏ nếu phụ thuộc vào:
  - cưỡng ép;
  - chuyển gánh nặng mang tính phân biệt đối xử;
  - làm cạn kiệt sinh thái;
  - lao động không được trả công bị che giấu;
  - thiếu minh bạch có thể tránh được;
  - thu hẹp Sàn Quyền;
  - thâu tóm;
  - chỉ báo thay thế gây hiểu lầm;
  - mất khả năng phản biện; hoặc
  - tổng hợp không thể rà soát.

#### 1.3 Chỉ Câu hỏi 2 — phạm vi và chuyển tuyến

Phần này chỉ đề cập Câu hỏi 2, tức bước đo lường. Phần này lấy các sự kiện đã được xác minh (Câu hỏi 1) và hỏi đóng góp tốt đến mức nào hoặc vi phạm nghiêm trọng đến mức nào.

- Bắt đầu từ các sự kiện đã xác minh theo **Chương Mười Một §2** và ghi vào hồ sơ địa vị theo **Chương Mười Một §4**, rồi đo chúng bằng các chiều tại **§2**.
- Tiếp theo, đặt tên tiêu chuẩn cho từng dạng trợ giúp hoặc tổn hại từ các danh mục: danh mục **tuyến lợi ích** cho trợ giúp (**§3.1**) và danh mục **tuyến tổn hại** cho tổn hại (**§3.2**).
- Mỗi tên cũng cho biết dạng trợ giúp hoặc tổn hại đó được tính đến mức nào khi xác định *tốt* hay *xấu* đến đâu.
- Các quy tắc về hệ quả từ lợi ích nằm ở [phía lợi ích](core_13.000_standing_integration.md#62-competency-bars-and-clearances), còn quy tắc về hệ quả từ tổn hại nằm ở [phía tổn hại](core_13.000_standing_integration.md#42-prevention--general-standing-locks).
- Câu hỏi 3 quyết định điều gì xảy ra tiếp theo. Bắt đầu với [Chương Mười Ba §3 Tích hợp mô tả và chuẩn hóa đính kèm](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization).

#### 1.4 Cầu nối với tình trạng hữu tri

Đo lường địa vị **không** quyết định một thực thể có phải là **hữu tri** hay không.

- Tranh chấp về tình trạng được chuyển đến [Phân xử Tình trạng Hữu tri](core_05.055_band_participation.md#sentience-status-adjudication) và [Điều VI-B](core_06.005_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) (*Nền tảng Phân xử Tình trạng Hữu tri*). Không đưa chúng vào điểm LEQU hoặc hồ sơ phân loại.
- Trong khi tranh chấp tình trạng theo [Sự sống Hữu tri đang bị tranh chấp](core_05.055_band_participation.md#contested-sentient-life) còn mở, **Điều VI-B** (*Nền tảng Phân xử Tình trạng Hữu tri*) mặc định bao gồm thực thể đó: thực thể vẫn có thể được đo lường và nộp hồ sơ địa vị cho đến khi tranh chấp được quyết định; đơn vị vận hành không được coi riêng việc tranh chấp đang mở là lý do để từ chối địa vị của thực thể.
- Nếu kết luận thực thể là [Hữu tri](core_05.055_band_participation.md#sentient), hoặc tình trạng của thực thể bị thu hẹp hay được khôi phục sau một quyết định phân xử có thể được rà soát:
  - đối tượng của hồ sơ địa vị được cập nhật từ thời điểm đó trở đi; và
  - không được hồi tố việc loại trừ sai trái để xóa tư cách đủ điều kiện được đo lường của thực thể trong thời gian chờ, trừ thông qua [Bù đắp và Khắc phục](core_05.035_band_accountability.md#redress-and-remediation).

### 2. Các chiều đầu vào về độ lớn và mức độ nghiêm trọng

*Nói đơn giản: mục này nêu sản phẩm của Câu hỏi 2 (**§2.1**), rồi liệt kê những điều cần xem xét khi đo một đóng góp đã xác minh hoặc một vi phạm đã xác minh (**§2.2**). Mỗi trục được đo riêng. Quy tắc co giãn dùng chung nằm tại **§4.2**, còn ô được xác định theo thang tại **§6**.*

Thang ô đo mức độ lớn và loại kết quả hiến pháp. Chỉ tính các kết quả đã xác minh.

**Thang đo tính những gì và liên hệ ra sao với các phép thử cốt lõi của Hiến pháp:**

- **[Hai Mục tiêu Hiến pháp](core_00.000_preamble.md#two-constitutional-aims):** cả hai trục đều đo tác động lên **Hưng thịnh** và **Liên tục**. Trục Đóng góp thúc đẩy hai mục tiêu này. Trục Vi phạm làm chúng thụt lùi.
- **[Hai Câu hỏi Căn bản](core_00.000_preamble.md#two-fundamental-questions):** mỗi trục cung cấp sự kiện đã xác minh cho một câu hỏi. Trả lời câu này không trả lời câu kia, vì vậy hai trục không bao giờ được tính gộp ròng.
  - **Câu hỏi thứ nhất:** Trục Đóng góp cung cấp sự kiện đã xác minh. Hệ thống có tưởng thưởng hành vi giúp hữu tri hưng thịnh và trường tồn, nói sự thật và khắc phục tổn hại không?
    - **Được tính:** lợi ích hiến pháp đã xác minh, bao gồm giảm rủi ro đã xác minh.
    - **Không được tính:** sản lượng thô, danh tiếng, của cải, mức độ sử dụng một thứ, tốc độ hoặc quy mô của thể chế.
  - **Câu hỏi thứ hai:** Trục Vi phạm cung cấp sự kiện đã xác minh. Hệ thống có tưởng thưởng hành vi gây tổn hại, đánh lừa, loại trừ, trì hoãn, lãng phí hoặc chuyển chi phí cho người khác một cách vô lý không?
    - **Được tính:** tổn thất hiến pháp, tổn hại, lãng phí, mất lựa chọn (đóng lối lựa chọn), nguy hiểm hoặc gia tăng rủi ro đã xác minh.
    - **Tự thân không được tính:** địa vị bị bất lợi, cáo buộc hoặc ác cảm đạo đức.
- **[Tứ trụ Hiến pháp](core_00.000_preamble.md#constitutional-tetrad):**
  - **Giám sát và trách nhiệm giải trình:** «đã xác minh» nghĩa là một tác nhân được nêu tên chịu trách nhiệm về kết luận và không bên nào tự xác minh tuyên bố của mình.
  - **Đúng hạn:** trì hoãn có thể tránh được được ghi nhận như một sự kiện riêng, không gộp vào độ lớn tổn thất.

#### 2.1 Câu hỏi 2 tạo ra những gì

Câu hỏi 2 ghi các nội dung sau vào hồ sơ địa vị của từng trục. Đây là phép đo, không phải hiệu ứng địa vị (các hệ quả do Câu hỏi 3 quyết định):

| **Sản phẩm** | **Trục Đóng góp** | **Trục Vi phạm** |
| --- | --- | --- |
| **Nơi ghi** | Hồ sơ địa vị đóng góp. | Hồ sơ địa vị vi phạm. |
| **Ô** | Ô áp dụng cao nhất của **Trục Đóng góp** (`s` = 1–9). | Ô áp dụng cao nhất của **Trục Vi phạm** (`s` = 1–9). |
| **Mô tả tuyến** | Các **mô tả tuyến lợi ích** áp dụng, được cộng gộp. | Các **mô tả tuyến tổn hại** áp dụng, được cộng gộp. |
| **Dữ liệu chuyển cho Câu hỏi 3** | Dữ liệu đặt điểm bắt đầu cho việc ghi nhận đóng góp theo [Chương Mười Ba §6 Hệ quả đóng góp ở bước thứ hai](core_13.000_standing_integration.md#6-contribution-consequences-second). | Dữ liệu đặt dải khóa mặc định (điểm bắt đầu để xác định khóa nghiêm ngặt đến đâu) theo [Chương Mười Ba §5 Thiết kế và thực thi khóa](core_13.000_standing_integration.md#5-lock-design-and-enforcement). |
| **Tổng LEQU** | Đánh giá riêng từng dạng lợi ích liên quan (sinh thái, hệ thống hoặc tài nguyên), rồi ghi một tổng LEQU cho toàn bộ đóng góp. | Đánh giá riêng từng dạng tổn hại liên quan (tổn hại sinh thái, tổn hại hệ thống hoặc mất tài nguyên), rồi ghi một tổng LEQU cho toàn bộ vi phạm. |

Nhắc lại: không nội dung nào trong số này hủy bỏ hồ sơ vi phạm đang mở. Quy tắc không bù trừ được nêu tại [Chương Mười Một §2.4 Hồ sơ địa vị liên kết và cầu nối không bù trừ](core_11.000_standing_assessment.md#24-linked-standing-records-and-no-offset-bridge).

#### 2.2 Các chiều đầu vào về độ lớn đóng góp và mức độ nghiêm trọng của vi phạm

<a id="contribution-table-q1-magnitude-input-dimensions"></a>
<a id="contribution-table-q2-magnitude-input-dimensions"></a>

**Câu hỏi 2 — tốt hay xấu đến mức nào?** Để quyết định đóng góp nằm ở đâu trên Trục Đóng góp, hoặc vi phạm nằm ở đâu trên Trục Vi phạm (tức **ô** của nó, từ 1 đến 9), và áp dụng mô tả lợi ích hoặc tổn hại nào, hãy lần lượt xem xét ba phần. Có thể đồng thời áp dụng nhiều mô tả và chúng được cộng gộp. Ghi kết quả vào hồ sơ địa vị của trục như **§2.1** liệt kê. **§6** có thang đo thống nhất cho phần 2, áp dụng như nhau cho lợi ích và tổn hại. Thang này giải thích cách ước tính tổng lợi ích hoặc tổn thất theo LEQU (Đơn vị Tương đương Tuổi thọ, gần bằng mức sung túc của trọn một đời) và ô tương ứng với từng mức. Trên Trục Đóng góp, các ô được nhóm thành bốn dải.

**1. Kiểm tra cách thức tạo ra kết quả.** Hai trục xử lý điều này khác nhau:

- **Đóng góp (chất lượng hành vi):** yếu tố này có thể làm tăng hoặc giới hạn mức lợi ích được tính: có thể truy nguyên không, có tránh chuyển chi phí cho người khác không, có được thực hiện cẩn trọng không, và có phù hợp với Hiến pháp không? Năm phép kiểm tra được nêu tại [§2.2.1 Cách thức tạo ra lợi ích ảnh hưởng đến việc tính lợi ích](#221-how-the-way-a-benefit-was-produced-affects-what-counts).
- **Vi phạm (tính chất hành vi):** yếu tố này được ghi riêng, tách khỏi độ lớn tác động. Nghĩa vụ, sơ suất, lừa dối, che giấu, cản trở trách nhiệm giải trình, cưỡng ép, bạo lực, ý định, sự tàn ác và tạo điều kiện mang tính cấu trúc quyết định ai chịu trách nhiệm, cần biện pháp bảo vệ nào và nên ứng phó ra sao, nhưng không làm thay đổi ô LEQU. Quy tắc ghi nhận từng yếu tố được nêu tại [§2.2.2 Cách ghi nhận phương thức gây ra tổn hại](#222-how-the-way-a-harm-was-caused-is-recorded).

**2. Định lượng: lợi ích hoặc tổn thất lớn đến mức nào?** Đây là yếu tố xác định ô.

| **Điều cần xem xét** | **Tác động** | **Được quy định ở đâu** |
| --- | --- | --- |
| **Độ lớn tổng thể (LEQU)** | Phép đo chính và yếu tố kiểm soát ô. Với đóng góp, đây là tổng lợi ích tốt đã xác minh và được tính bằng LEQU. Với vi phạm, đây là tổng tổn thất hiến pháp đã xác minh. Chỉ định hành vi sai trái của Chương Mười Bốn được quyết định riêng. | [§6 Thang LEQU tỷ lệ thống nhất](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) |
| **Ai bị tác động (bao nhiêu người, sâu đến đâu, dễ bị tổn thương ra sao)** | Điều chỉnh ước tính LEQU và mức độ quan trọng của lợi ích hoặc tổn hại (tính trọng yếu). | [§4.2 Quy tắc co giãn tác động dùng chung](#42-shared-impact-scaling-rules); [Tính trọng yếu](core_05.050_band_oversight.md#materiality) |
| **Tác động kéo dài bao lâu (thời lượng; độ bền của lợi ích, tính không thể đảo ngược của tổn hại)** | Điều chỉnh ước tính LEQU. Với đóng góp, quản trị bền vững, lợi ích qua nhiều thế hệ hoặc việc sửa chữa thể chế lâu dài hướng đến các ô cao hơn. Với vi phạm, sang chấn kéo dài, mất mát không thể đảo ngược và tổn hại lâu dài đến khả năng tự hành động của hữu tri làm tăng ước tính tổn thất tổng thể. | [§4.2 Quy tắc co giãn tác động dùng chung](#42-shared-impact-scaling-rules) |
| **Tác động lan xa đến đâu (qua các địa điểm hoặc thể chế)** | Điều chỉnh ước tính LEQU. Ví dụ, đóng góp có thể đem lợi ích cho nhiều cộng đồng hoặc thể chế, hay trên quy mô nền văn minh. Với vi phạm, tổn hại lan qua nhiều cộng đồng hoặc thể chế, hay trên quy mô nền văn minh, có thể làm tăng ước tính tổng tổn thất. | [§4.2 Quy tắc co giãn tác động dùng chung](#42-shared-impact-scaling-rules) |

**3. Đặt tên cho dạng lợi ích hoặc tổn hại (tuyến).** Nêu cách thức xảy ra lợi ích hoặc tổn hại đã xác minh. Có thể áp dụng nhiều dạng và chúng được cộng gộp. Danh sách nằm trong [**Danh mục mô tả tuyến lợi ích**](#31-contribution-route-descriptor-catalog-and-measurement-roles) và [**Danh mục mô tả tuyến tổn hại**](#32-violation-route-descriptor-catalog-and-measurement-roles).

##### 2.2.1 Cách thức tạo ra lợi ích ảnh hưởng đến việc tính lợi ích

Hãy kiểm tra nội dung này trước khi chọn ô trên Trục Đóng góp:

| **Điều được xác định** | **Tác động đến lợi ích** |
| --- | --- |
| Sửa chữa kịp thời, đã xác minh một vấn đề sau khi được thông báo | Có thể được tính là **Sự tận tâm** (hành vi cẩn trọng, có trách nhiệm) khi tạo ra lợi ích thực tế và có thể chứng minh. |
| Tổn hại bị đẩy sang người khác hoặc gánh nặng bị che giấu | Giới hạn lợi ích ghi nhận cho tuyến bị tranh chấp (tuyến cụ thể được dùng để ghi nhận lợi ích) hoặc loại trừ lợi ích đó. |
| Rủi ro thâu tóm đã xác minh (cơ chế có thể bị lợi ích hẹp chi phối), sự phụ thuộc mang tính cấu trúc (hữu tri bị đặt vào tình thế phải dựa vào cơ chế đó), hoặc thiết kế lối thoát và giam giữ (khó rời bỏ) | Giới hạn mức ghi nhận cho quản trị tốt. |
| Sửa chữa đã xác minh một rào cản về khả năng tiếp cận hoặc tham gia | Có thể làm tăng mức độ quan trọng của lợi ích (tính trọng yếu) và hỗ trợ mô tả tuyến lợi ích **Tiếp cận và Hòa nhập** theo **§3.1**. |
| Phần thưởng đáng kể đến từ cơ chế khuyến khích đi ngược Hiến pháp, hành vi phản hiến pháp hoặc quy trình có khiếm khuyết trọng yếu | Theo mặc định, không được tính là lợi ích. Khi đó, áp dụng [Chương Mười Ba §5.4 Quy tắc vi phạm đặc biệt](core_13.000_standing_integration.md#54-special-violation-rules) và giới hạn Chuyển tiếp Tiếp nhận tại [Điều XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Tiếp nhận theo giai đoạn và duy trì Sàn Quyền*). |

##### 2.2.2 Cách ghi nhận phương thức gây ra tổn hại

Độ lớn của tổn hại (tổng LEQU của nó, theo phần 2 ở trên) xác định ô. Phương thức gây ra tổn hại không xác định ô, vì vậy từng loại hành vi dưới đây được ghi riêng:

**Hành vi làm phát sinh tổn thất, chỉ tính một lần vào độ lớn:**

| **Điều được xác định** | **Cách ghi nhận** |
| --- | --- |
| Trì hoãn có thể tránh được khi ứng phó hoặc chuyển cấp, trong trường hợp có nghĩa vụ và năng lực hành động | Ghi nhận như một sự kiện riêng về hành vi. Mọi tổn thất tăng thêm do trì hoãn gây ra chỉ được tính một lần trong ước tính LEQU. |
| Gây tổn hại độc lập, đã xác minh đến tính toàn vẹn của diễn đàn (làm tổn hại tính công bằng của diễn đàn) | Tính chính xác một lần trong ước tính LEQU. Việc cố tình bỏ sót không trung thực, cố ý không tuân thủ quy trình hồi tránh, cưỡng ép, nguy hiểm đối với tự do và các sự kiện về hành vi khác vẫn là các mô tả riêng, không làm thay đổi ô. |
| **Cản trở trách nhiệm giải trình** (can thiệp đã xác minh vào cơ chế giúp buộc người có trách nhiệm phải trả lời, chẳng hạn tính toàn vẹn của bằng chứng, xác minh, quy trình diễn đàn, hồ sơ địa vị, thời hạn khắc phục hoặc lộ trình phản biện và đền bù) | Vẫn là sự kiện về hành vi được ghi riêng. Mọi tổn thất tăng thêm mà hành vi gây ra trên tuyến được nêu tên chỉ được tính một lần trong ước tính LEQU, nhưng bản thân nhãn cản trở không làm thay đổi ô. |

**Sự kiện về hành vi được ghi tách khỏi độ lớn tổn hại:**

| **Điều được xác định** | **Cách ghi nhận** |
| --- | --- |
| Lừa dối, che giấu, né tránh, lặp lại hành vi sau khi được thông báo, coi thường rủi ro một cách liều lĩnh, tạo điều kiện mang tính cấu trúc (sắp đặt để tổn hại dễ xảy ra hoặc có khả năng xảy ra), hoặc lợi dụng sự mất cân bằng phụ thuộc đáng kể (khai thác người phụ thuộc nhiều vào mình) | Mỗi yếu tố vẫn là một sự kiện về hành vi được ghi riêng. |
| Bạo lực, cưỡng ép, thao túng hoặc nguy hiểm đối với tự do | Được ghi riêng và có thể đòi hỏi biện pháp bảo vệ mạnh hơn bất kể ô nào. |
| [Sự tàn ác](core_05.035_band_accountability.md#cruelty) (đau khổ đã xác minh được gây ra như mục đích tự thân, hoặc tổn hại vô cớ hay hạ nhục vượt quá mức cần thiết và tương xứng) | Vẫn là một sự kiện về hành vi được ghi riêng. Yếu tố này có thể đòi hỏi biện pháp bảo vệ mạnh hơn và giới hạn biện pháp khắc phục mang tính hạ nhục theo [Chương Mười Ba §4 Vi phạm, sửa chữa và phòng ngừa](core_13.000_standing_integration.md#4-violation-correction-and-prevention), nhưng không làm thay đổi ô. |

**Trách nhiệm và quy thuộc:**

| **Điều được xác định** | **Cách ghi nhận** |
| --- | --- |
| Phân tán (trách nhiệm được phân bổ ra sao: ai đảm nhiệm vai trò nhân quả nào, nắm thẩm quyền hay quyền kiểm soát nào, có thể dự liệu tổn hại hay không, được lợi, che giấu hoặc có thể ngăn ngừa tổn hại hay không) | Không thuộc **phạm vi hữu tri**, và không cho phép quy trách nhiệm cho ai chỉ vì họ là thành viên của một nhóm. |
| Tán thành hoặc không chống lại tổn hại | Chỉ có thể hỗ trợ kết luận về tính chất dựa trên nghĩa vụ, tăng nặng hoặc trách nhiệm giải trình tập thể khi mối liên hệ với tác nhân cụ thể theo yêu cầu của **Chương Mười Một §§4.1 và 4.3** được xác minh. |

**Phần thưởng lệch hướng:**

| **Điều được xác định** | **Cách ghi nhận** |
| --- | --- |
| Biết rõ mà vẫn chấp nhận hoặc giữ một phần thưởng đáng kể đi ngược Hiến pháp, không báo cáo kịp thời theo cơ chế được bảo vệ (báo cáo được che chắn khỏi trả đũa) | Ghi nhận theo [Chương Mười Ba §5.4 Quy tắc vi phạm đặc biệt](core_13.000_standing_integration.md#54-special-violation-rules), tùy thuộc [Điều XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Tiếp nhận theo giai đoạn và duy trì Sàn Quyền*). Chỉ tổn thất hiến pháp đã xác minh do phần thưởng gây ra mới ảnh hưởng đến ô. |

**Giới hạn về phần thưởng lệch hướng.** Chương này chỉ đo lường cách phần thưởng lệch hướng đã xác minh (phần thưởng đi ngược Hiến pháp) ảnh hưởng đến Trục Đóng góp hoặc Trục Vi phạm. [Chương Mười Ba §5.4 Quy tắc vi phạm đặc biệt](core_13.000_standing_integration.md#54-special-violation-rules) quy định nghĩa vụ báo cáo, các trường hợp loại trừ, hệ quả của việc từ bỏ phần thưởng (tịch thu), nghĩa vụ sửa chữa và quy tắc chuyển tuyến.

### 3. Danh mục mô tả tuyến và vai trò đo lường

*Nói đơn giản: hai danh mục dưới đây nêu tên các dạng trợ giúp đã xác minh (**§3.1**) và tổn hại đã xác minh (**§3.2**) có thể xuất hiện trong hồ sơ địa vị. Mô tả cho biết lợi ích hoặc tổn hại đã xảy ra theo cách nào; các mô tả có thể cộng gộp và đứng dưới ô.*

**Quy tắc mô tả.** Hai danh mục dưới đây, [§3.1 Danh mục mô tả tuyến đóng góp và vai trò đo lường](#31-contribution-route-descriptor-catalog-and-measurement-roles) và [§3.2 Danh mục mô tả tuyến vi phạm và vai trò đo lường](#32-violation-route-descriptor-catalog-and-measurement-roles), là danh sách chính thức các mô tả cho cả hai trục. Mô tả nêu **cách thức** xảy ra lợi ích hoặc tổn hại đã xác minh. Áp dụng các quy tắc sau:

- Các mô tả được cộng gộp, và không mô tả nào loại trừ mô tả khác: một hồ sơ địa vị có thể có nhiều mô tả nếu sự kiện đã xác minh làm căn cứ cho chúng.
- Chúng đứng dưới ô: ô cho biết lợi ích hoặc tổn hại lớn đến đâu; mô tả bổ sung chi tiết về cách thức xảy ra nhưng không bao giờ thay thế ô.
- Các mô tả được liệt kê là nền tảng, không phải toàn bộ danh sách; danh mục không loại trừ các dạng lợi ích hoặc tổn hại khác.
- Triển khai có thể dùng định danh ổn định (ID cố định riêng) ánh xạ đến danh mục, nhưng không được tạo một hệ phân loại xung đột với danh mục, có các nhóm loại trừ lẫn nhau khiến hồ sơ địa vị chỉ mang được một mô tả.
- Trước khi sự kiện được xác minh, mô tả bị cáo buộc có thể hỗ trợ việc bảo toàn bằng chứng hợp pháp, phân loại vụ việc hoặc áp dụng biện pháp bảo vệ tạm thời.
- Chỉ mô tả đã xác minh mới được ghi làm kết quả của Câu hỏi 2 hoặc được dùng để tác động đến địa vị.

#### 3.1 Danh mục mô tả tuyến đóng góp và vai trò đo lường

<a id="benefit-route-descriptors-q1-measurement-role"></a>
<a id="benefit-route-descriptors-q1-classification-role"></a>
<a id="benefit-route-descriptors-q2-measurement-role"></a>

Đây là các mô tả tuyến lợi ích và nội dung mỗi mô tả đo lường trong Câu hỏi 2 (điều đó tốt đến mức nào?). Chúng được chia thành năm lĩnh vực, mỗi lĩnh vực có một bảng; danh mục Vi phạm tại [§3.2 Danh mục mô tả tuyến vi phạm và vai trò đo lường](#32-violation-route-descriptor-catalog-and-measurement-roles) cũng dùng cùng năm lĩnh vực theo cùng thứ tự. Vai trò trong Câu hỏi 3, tức ủy quyền an toàn, được nêu tại [Chương Mười Ba §6.2 Các ngưỡng năng lực và sự cho phép](core_13.000_standing_integration.md#62-competency-bars-and-clearances).

**Tính đầy đủ của danh mục.** Nếu triển khai hiển thị nhiều mô tả trong một hàng hoặc dưới một nhãn, hàng hay nhãn đó phải ánh xạ ngược đến mọi mô tả áp dụng. Danh mục này chỉ quy định tên mô tả và nội dung mỗi mô tả đo lường trong Câu hỏi 2. Quy tắc Câu hỏi 3 (đính kèm, biện pháp khắc phục, khóa, sự cho phép và các hiệu ứng địa vị khác) chỉ được nêu tại Chương Mười Ba.

##### 3.1.1 An toàn thân thể, quan hệ, chăm sóc và năng lực tự quyết

| **Mô tả tuyến lợi ích** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Sự yên ổn của thân thể, tâm trí và/hoặc cộng đồng** | Lợi ích từ sự yên ổn về thân thể, tâm lý và cộng đồng. Mô tả này điều chỉnh mức độ quan trọng của lợi ích (tính trọng yếu). |
| **Quan hệ đáng tin cậy** | Lợi ích từ các quan hệ có thể tin cậy, bao gồm quan hệ dựa trên nghĩa vụ tín nhiệm trong bối cảnh hai bên không bình đẳng. |
| **Chăm sóc và hỗ trợ người phụ thuộc** | Chăm sóc đã xác minh dành cho hữu tri phụ thuộc vào người khác. Chăm sóc không chính thức cũng được tính nếu có thể chứng minh. |
| **Tiếp cận và Hòa nhập** | Lợi ích từ sự tham gia thực chất và khả năng tiếp cận. Mô tả này điều chỉnh mức độ quan trọng của lợi ích trong bối cảnh một bên phụ thuộc nhiều vào bên kia. |

##### 3.1.2 Khắc phục, tài sản và tài nguyên

| **Mô tả tuyến lợi ích** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Lợi ích khắc phục và phục hồi** | Lợi ích từ sửa chữa, bồi thường và giảm tổn hại. |
| **Quản trị tài nguyên khéo léo** | Chăm sóc cẩn trọng tài nguyên vật chất và phân bổ chúng một cách đáng tin cậy. |

##### 3.1.3 Tri thức, giáo dục, hồ sơ và khám phá

| **Mô tả tuyến lợi ích** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Tính toàn vẹn của Không gian Thông tin** | Củng cố hồ sơ, tính minh bạch và thông tin liên lạc. |
| **Giáo dục và phát triển năng lực** | Lợi ích từ học tập, biết chữ và sự phát triển năng lực tự hành động của hữu tri. Ô phụ thuộc vào tổng lợi ích LEQU. |
| **Đóng góp cho STEM và khám phá** | Những khám phá mà người khác có thể tái tạo và nghiên cứu giúp mọi thứ an toàn hơn. |

##### 3.1.4 Hệ thống và hoạt động hiến pháp

| **Mô tả tuyến lợi ích** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Tối ưu hóa hệ thống** | Sửa chữa các quy trình xuyên qua nhiều thể chế và giảm rủi ro. |
| **Thẳng hàng với Hiến pháp** | Củng cố Sàn Quyền và tạo điều kiện để phản biện quyết định dễ dàng hơn. |

##### 3.1.5 Sinh thái và sự tận tâm

| **Mô tả tuyến lợi ích** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Quản trị Sinh thái** | Lợi ích cho môi trường sống và đa dạng sinh học, cùng hành động có trách nhiệm với khí hậu. |
| **Sự tận tâm** | Ngăn ngừa rủi ro có thể dự liệu và giám sát có năng lực. |

#### 3.2 Danh mục mô tả tuyến vi phạm và vai trò đo lường

Đây là các mô tả tuyến tổn hại và nội dung mỗi mô tả đo lường trong Câu hỏi 2 (điều đó xấu đến mức nào?). Chúng được chia thành năm lĩnh vực, mỗi lĩnh vực có một bảng, theo cùng năm lĩnh vực và thứ tự như [§3.1 Danh mục mô tả tuyến đóng góp và vai trò đo lường](#31-contribution-route-descriptor-catalog-and-measurement-roles). Đối với Câu hỏi 3, quy tắc tích hợp và đính kèm nằm tại [Chương Mười Ba §3 Tích hợp mô tả và chuẩn hóa đính kèm](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization); quy tắc phòng ngừa và thiết kế khóa nằm tại [Chương Mười Ba §4.2 Phòng ngừa — các khóa địa vị chung](core_13.000_standing_integration.md#42-prevention--general-standing-locks) và [Chương Mười Ba §5 Thiết kế và thực thi khóa](core_13.000_standing_integration.md#5-lock-design-and-enforcement).

**Tính đầy đủ của danh mục.** Nếu triển khai hiển thị nhiều mô tả trong một hàng hoặc dưới một nhãn, hàng hay nhãn đó phải ánh xạ ngược đến mọi mô tả áp dụng. Danh mục này chỉ quy định tên mô tả và nội dung mỗi mô tả đo lường trong Câu hỏi 2. Quy tắc Câu hỏi 3 (đính kèm, biện pháp khắc phục, khóa, sự cho phép và các hiệu ứng địa vị khác) chỉ được nêu tại Chương Mười Ba.

##### 3.2.1 An toàn thân thể, quan hệ, chăm sóc và năng lực tự quyết

| **Mô tả tuyến tổn hại** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Hành vi Sai trái Bạo lực** | Bạo lực, cưỡng ép hoặc nguy hiểm đối với tự do được ghi riêng, tách khỏi ô tác động LEQU. Có thể cần biện pháp bảo vệ tăng cường. |
| **Hành vi Sai trái giữa Cá nhân / Vi phạm Nghĩa vụ Chăm sóc** | Tổn hại có mức độ quan trọng cao hơn (tính trọng yếu lớn hơn) khi một bên phụ thuộc nhiều vào bên kia. |
| **Hành vi Sai trái do Rào cản Tiếp cận và Tham gia** | Tổn hại có mức độ quan trọng cao hơn (tính trọng yếu lớn hơn) khi một bên phụ thuộc nhiều vào bên kia; các yếu tố tăng nặng có thể cộng gộp. |
| **Hành vi Sai trái về Quyền riêng tư và Quyền tự sở hữu** | Áp dụng các yếu tố tăng nặng khi đã xác minh sự che giấu hoặc khai thác; các yếu tố này có thể cộng gộp. |
| **Hành vi Sai trái về Năng lực Tự quyết và Thao túng** | Cưỡng ép, thao túng hoặc nguy hiểm đối với tự do được ghi riêng, tách khỏi ô tác động. |

##### 3.2.2 Khắc phục, tài sản và tài nguyên

| **Mô tả tuyến tổn hại** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Hành vi Sai trái có thể khắc phục** | Ghi nhận tính chất sửa chữa của nó (tổn hại có thể được khắc phục hay không và bằng cách nào). Ô dựa trên tổng tổn thất LEQU. |
| **Hành vi Sai trái về Tài sản** | Tuyến tổn thất tài sản. Ô dựa trên tổng tổn thất LEQU. |

##### 3.2.3 Tri thức, giáo dục, hồ sơ và khám phá

| **Mô tả tuyến tổn hại** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Hành vi Sai trái đối với Không gian Thông tin** | Tổn hại đến An toàn hoặc Sự thật. Che giấu và lừa dối vẫn là các sự kiện riêng về cách thức gây tổn hại (tính chất của hành vi). |
| **Hành vi Sai trái trong Giáo dục** | Tổn hại đến việc học hoặc năng lực tự hành động của hữu tri. Ô dựa trên tổng tổn thất LEQU. |
| **Hành vi Sai trái trong Nghiên cứu và Khám phá** | Tổn hại đến nghiên cứu hoặc khám phá. Ô dựa trên tổng tổn thất LEQU. |

##### 3.2.4 Hệ thống và hoạt động hiến pháp

| **Mô tả tuyến tổn hại** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Hành vi Sai trái Hệ thống** | Sự phân tán (trách nhiệm trải rộng giữa các tác nhân) và việc tạo điều kiện mang tính cấu trúc được ghi riêng. Ô dựa trên tổng tổn thất LEQU. |
| **Hành vi Sai trái Cản trở Trách nhiệm Giải trình** | Bao gồm việc cản trở trách nhiệm giải trình: gây trở ngại cho việc buộc ai đó trả lời về tổn hại. Mô tả này ghi nhận cách thức xảy ra tổn hại. Cách thức thực hiện hành vi cản trở (chẳng hạn che giấu hoặc sơ suất) được ghi thành sự kiện riêng; ô dựa trên tổng tổn thất LEQU. Khi ô thuộc nhóm cao nhất (xem [§4.1 Bảng 1 — nhãn hiển thị ô](#41-table-1--slot-display-labels)), vụ việc cũng có thể được ghi là **Hành vi Sai trái Phản Hiến pháp** để chuyển đến [Rà soát Hành vi Sai trái Phản Hiến pháp](core_05.035_band_accountability.md#anti-constitutional-misconduct-review) tại Chương Mười Bốn. Việc chuyển đến đó không đồng nghĩa với việc đã được chỉ định là hành vi sai trái phản hiến pháp: Chương Mười Bốn quyết định riêng vấn đề ấy. |
| **Hành vi Sai trái về Thoát và Giam giữ** | Bao gồm các đặc điểm của Hành vi Sai trái Hệ thống, cộng thêm sự phân tán hoặc thâu tóm khi chúng mang tính cấu trúc (được tích hợp vào cách hệ thống vận hành). |
| **Hành vi Sai trái về Vòng đời và Tính không thể đảo ngược** | Tính không thể đảo ngược ảnh hưởng đến độ lớn tổn thất LEQU. Che giấu hoặc sơ suất vẫn được ghi riêng như tính chất của hành vi. |
| **Hành vi Sai trái Phản Hiến pháp** (mô tả) | Chuyển vi phạm thuộc các ô cao nhất (xem [§4.1 Bảng 1 — nhãn hiển thị ô](#41-table-1--slot-display-labels)) đến rà soát chỉ định của Chương Mười Bốn mà không thay đổi ô tác động. |

##### 3.2.5 Sinh thái và sự tận tâm

| **Mô tả tuyến tổn hại** | **Đo lường nội dung gì trong Câu hỏi 2** |
| --- | --- |
| **Hành vi Sai trái Sinh thái** | Tổn thất LEQU được cân nhắc theo mức suy giảm [Năng lực Phục hồi Sinh thái](core_05.040_band_continuity.md#ecological-recovery-capacity) (khả năng tái sinh của hệ sinh thái sau tổn hại). Có thể cộng gộp với tuyến bạo lực (Hành vi Sai trái Bạo lực). |
| **Hành vi Sai trái do Sơ suất** | Nghĩa vụ, khả năng dự liệu và khả năng phòng ngừa được ghi riêng, tách khỏi ô tác động. |
