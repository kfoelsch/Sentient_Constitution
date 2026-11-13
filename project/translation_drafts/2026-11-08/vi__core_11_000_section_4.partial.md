<!-- Bản dịch nháp một phần sang tiếng Việt. Nguồn: core_11.000_standing_assessment.md; snapshot nguồn: 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Do AI soạn; chưa được rà soát. Phạm vi một phần: §4. -->

### 4. Yêu cầu xác minh và hồ sơ

<details>
<summary><strong><span style="color: #2563eb;">Dấu vết</span></strong></summary>

- Nguồn trước: [§2](#2-question-1--what-happened) (*hồ sơ Câu hỏi 1 và hướng dẫn phân loại loại sự kiện*); [Các Chương Hai đến Bốn](core_02.000_definition_structure.md) (*hồ sơ, xác minh và khả năng truy nguyên định nghĩa đến kết quả*).
- Nguồn sau:
  - [§4.1](#41-minimum-record-contents) (*nội dung tối thiểu*);
  - [§4.2](#42-related-standing-record-cross-references) (*tham chiếu chéo*);
  - [§5](#5-record-custody-and-opening-authority) (*quyền lưu giữ hồ sơ và quyền mở hồ sơ*);
  - [§6](#6-handling-a-standing-record) (*xử lý hồ sơ địa vị*);
  - [Chương Mười Hai §1](core_12.000_standing_measurement.md#1-question-2--how-good-or-bad-was-it) (*Câu hỏi 2*).
- Đọc cùng: [CF-15.415 §8 Thẩm quyền đối với thông tin bị hạn chế](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-8-restricted-information-authority) (*điểm đến đầu tiên khi có tranh chấp về giới hạn tiết lộ được nêu theo [§4.1](#41-minimum-record-contents)*).

</details>

<br>

*Nói đơn giản: mục này nêu những nội dung mỗi hồ sơ địa vị phải có, cách các hồ sơ địa vị liên quan tham chiếu lẫn nhau và cách lập phiên bản hồ sơ. Ai có thể mở và lưu giữ hồ sơ địa vị, cũng như cách phản biện hoặc sửa hồ sơ, được quy định tại [§5 Quyền lưu giữ hồ sơ và quyền mở hồ sơ](#5-record-custody-and-opening-authority). Chỉ được bổ sung các phép đo của Câu hỏi 2 sau khi đã ghi nhận căn cứ sự kiện được xác minh.*

Chi tiết về bằng chứng và hồ sơ có thể tăng theo mức lợi ích trọng yếu và cấp của hệ thống. Việc điều chỉnh theo mức độ này không loại bất kỳ hữu thể hữu tri, thể chế hay hệ thống nào thuộc phạm vi khỏi quy trình địa vị.

<a id="41-minimum-record-contents"></a>

#### 4.1 Nội dung tối thiểu của hồ sơ

Hồ sơ địa vị phải có các trường dưới đây; hai tiểu mục cuối bổ sung trường cho từng trục. Cổng dữ liệu đã xác minh, quy định dữ liệu nào được phép đưa vào hồ sơ địa vị, được nêu tại [§2.5 Cổng dữ liệu đã xác minh](#25-verified-input-gate). Quy tắc tách riêng sự kiện của Câu hỏi 1 khỏi phép đo của Câu hỏi 2 được nêu tại [§2.6 Ranh giới giai đoạn](#26-stage-boundary).

<a id="411-fields-every-standing-record-must-carry"></a>

##### 4.1.1 Các trường bắt buộc trong mọi hồ sơ địa vị

Tối thiểu, mọi hồ sơ địa vị phải bao gồm:

- loại hồ sơ địa vị — **hồ sơ địa vị đóng góp** hoặc **hồ sơ địa vị vi phạm**;
- đối tượng hoặc sự việc được đánh giá và phạm vi đánh giá, bao gồm ranh giới hệ thống, ranh giới vai trò, cộng đồng bị ảnh hưởng và quan hệ phụ thuộc liên quan;
- hành vi hoặc phát hiện được đánh giá, bao gồm hành động, thiếu sót, nghĩa vụ, tác động, sự kiện có giới hạn, mô thức trong phạm vi, hồ sơ đóng góp hoặc phát hiện vi phạm mà hồ sơ địa vị dựa vào;
- khoảng thời gian của hồ sơ và trạng thái rà soát hiện tại — chẳng hạn sơ bộ, chung cuộc cho mục đích đã nêu, đang bị phản biện, đã bị thay thế hoặc đến hạn đánh giá lại theo lịch;
- mọi hồ sơ địa vị liên quan được tham chiếu chéo theo yêu cầu tại **§4.2**;
- hồ sơ chính thức, nhân chứng, phép đo, cuộc kiểm toán, quyết định của diễn đàn hoặc tài liệu xác minh khác giúp chứng minh, rà soát và phản biện hồ sơ địa vị theo các Chương Hai đến Bốn;
- **thẩm quyền mở hồ sơ** đã xác minh căn cứ sự kiện và cho phép ghi nhận, cùng với **đơn vị lưu giữ hồ sơ** riêng biệt đã nhập và lưu giữ hồ sơ địa vị; mỗi bên phải được nêu tên theo **§5**;
- cách phản biện hồ sơ địa vị, bao gồm:
  - diễn đàn hoặc thẩm quyền nào sẽ rà soát;
  - mọi giới hạn tiết lộ; và
  - các điều kiện để:
    - sửa chữa;
    - khôi phục;
    - hết hạn; hoặc
    - rà soát theo lịch;
- các trường phép đo của Câu hỏi 2 riêng cho từng trục được yêu cầu dưới đây, khi việc đo lường diễn ra.

<a id="412-inspectable-attributable-action"></a>

##### 4.1.2 Hành động quy thuộc có thể kiểm tra

Bằng chứng về hành động quy thuộc liên quan đến hồ sơ địa vị như sau:

- Đối với nhân sự/đại diện thực hiện Hoạt động Quản trị Hệ thống Trọng yếu hoặc thẩm quyền vận hành trọng yếu, bằng chứng hành động quy thuộc có thể tái dựng được quy định tại **[CS-16.305 §10 Hành động quy thuộc có thể kiểm tra](corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action)** làm hợp đồng ghi nhật ký mặc định cho các đội hỗn hợp.
- Bằng chứng đó có thể được đưa vào hồ sơ địa vị này.
- Nó không thay thế hồ sơ địa vị này.
- Hồ sơ địa vị không bao gồm trọng số của mô hình AI (các con số bên trong mô hình) hoặc lập luận riêng tư của mô hình. Ngoại lệ duy nhất là khi không còn cách nào khác để xác định ai hoặc điều gì chịu trách nhiệm.
- Một vụ việc không nằm ngoài phép đo địa vị chỉ vì liên quan đến quyền riêng tư của ai đó hoặc trạng thái nội bộ được bảo vệ của một hệ thống. Vụ việc vẫn được đo lường khi có liên quan đến vấn đề địa vị.

<a id="413-no-privacy-or-opacity-exemption"></a>

##### 4.1.3 Không miễn trừ vì quyền riêng tư hoặc tính thiếu minh bạch

Quyền riêng tư, tính bảo mật hoặc tính thiếu minh bạch của nội bộ hệ thống không miễn trừ một vụ việc khỏi phép đo địa vị. Khi các yếu tố này xung đột với yêu cầu về hồ sơ đã xác minh, xung đột được giải quyết theo [Chương Một §13.1 Các Nguyên tắc Đánh đổi Cốt lõi](core_01.005_interaction_interpretation.md#131-core-tradeoff-principles) và kỷ luật lập hồ sơ quyết định của mục đó, đồng thời vẫn bảo đảm quyền tiếp cận của người rà soát độc lập.

<a id="414-additional-fields-for-contribution-standing-records"></a>

##### 4.1.4 Trường bổ sung cho hồ sơ địa vị đóng góp

**Hồ sơ địa vị đóng góp** cũng phải nêu:

- phép đo đóng góp của Câu hỏi 2, bao gồm:
  - dải chính;
  - ô `s` nếu được chỉ định (xem [Chương Mười Hai §4 Ngữ pháp ô và quy tắc co giãn dùng chung](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - căn cứ bằng chứng;
  - lập luận về tính trọng yếu; và
  - mọi phép hiệu chỉnh LEQU được thông qua hoặc phép hiệu chỉnh tương đương được dùng để hỗ trợ minh bạch;
- nếu đóng góp được chia sẻ, cách phân bổ ghi nhận, bao gồm xem xét:
  - thời gian;
  - công sức;
  - phối hợp;
  - duy trì;
  - đóng góp nhân quả; và
  - công việc hỗ trợ ít được nhìn thấy;
- phép đo đóng góp được ghi tại đây làm căn cứ cho mọi hiệu ứng địa vị sau này của Chương Mười Ba.

<a id="415-additional-fields-for-violation-standing-records"></a>

##### 4.1.5 Trường bổ sung cho hồ sơ địa vị vi phạm

**Hồ sơ địa vị vi phạm** cũng phải nêu:

- phép đo vi phạm của Câu hỏi 2, bao gồm:
  - thẩm quyền đưa ra phát hiện hoặc căn cứ hồ sơ;
  - tác động LEQU;
  - ô `s` nếu được chỉ định (xem [Chương Mười Hai §4 Ngữ pháp ô và quy tắc co giãn dùng chung](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - tính chất quy trình / phản hồi nếu phù hợp; và
  - trạng thái chỉ định theo Chương Mười Bốn;
- nếu nhiều tác nhân cùng chia sẻ hoặc phân chia trách nhiệm đối với vi phạm, các lý do đã xác minh cho mọi ghi nhận bất lợi về địa vị đối với một tác nhân cụ thể, bao gồm:
  - vai trò nhân quả;
  - nghĩa vụ;
  - thẩm quyền;
  - quyền kiểm soát;
  - khả năng dự liệu;
  - lợi ích;
  - sự che giấu; hoặc
  - năng lực phòng ngừa khả thi;
- nếu phát hiện vi phạm liên quan đến việc diễn đàn bỏ sót thông tin cần tiết lộ hoặc cố ý không tuân thủ quy trình hồi tránh (đọc **§8.2.2** (*Cách ghi nhận phương thức gây ra tổn hại*) để biết kỷ luật đo lường):
  - căn cứ đã xác minh cho việc bỏ sót hoặc không tuân thủ;
  - nghĩa vụ tiết lộ hoặc hồi tránh chưa được thực hiện;
  - hiểu biết, sự liều lĩnh hoặc ý định của tác nhân nếu đã được xác định; và
  - liệu hành vi đó có ảnh hưởng trọng yếu đến:
    - tính hợp pháp của hội đồng;
    - tính độc lập;
    - việc phản biện hồi tránh;
    - tính toàn vẹn của bằng chứng;
    - thời điểm khắc phục;
    - phương án chuyển tuyến dự phòng; hoặc
    - khả năng phản biện trên thực tế hay không;
- phép đo vi phạm được ghi tại đây làm căn cứ cho mọi hiệu ứng địa vị sau này của Chương Mười Ba.

<a id="42-related-standing-record-cross-references"></a>

#### 4.2 Tham chiếu chéo giữa các hồ sơ địa vị liên quan

Nếu một hồ sơ địa vị đóng góp và một hồ sơ địa vị vi phạm nói về cùng một đối tượng, có khoảng thời gian trùng nhau hoặc liên quan đến cùng sự kiện, mô thức hay quyết định, thì mỗi hồ sơ phải dẫn chiếu đến hồ sơ kia.

Mỗi tham chiếu chéo tối thiểu phải xác định:

- hồ sơ địa vị liên quan và đó là hồ sơ đóng góp hay hồ sơ vi phạm;
- lý do liên kết hai hồ sơ địa vị, bao gồm trường hợp phát hiện vi phạm bác bỏ, sửa chữa hoặc giới hạn đóng góp được tuyên bố theo **§2.4**;
- điểm chung giữa hai hồ sơ địa vị: đối tượng, sự kiện, mô thức hoặc quyết định; và
- cách các khoảng thời gian hoặc vấn đề được đề cập giao nhau.

Tham chiếu chéo:

- phải giữ được khả năng kiểm toán và phản biện;
- không được thay thế việc đo lường riêng biệt;
- không được tạo điểm số gộp; và
- không được khiến hai hồ sơ địa vị trông như bao quát cùng vấn đề hoặc khoảng thời gian khi thực tế không phải vậy.

<a id="43-collective-and-actor-specific-records"></a>

#### 4.3 Hồ sơ tập thể và hồ sơ riêng cho từng tác nhân

Khi nhiều hữu thể hữu tri hoặc thực thể cùng chia sẻ một lợi ích hoặc vi phạm, hệ thống có thể lưu cả hồ sơ địa vị tập thể lẫn các hồ sơ riêng cho từng tác nhân. Áp dụng các quy tắc sau:

- Phát hiện đóng góp và vi phạm phải nằm trong các hồ sơ địa vị riêng biệt theo **§2.1**.
- Khi chia sẻ công lao, việc ghi nhận nên phản ánh những gì mỗi hữu thể hữu tri thực sự đóng góp:
  - vai trò;
  - thời gian;
  - công sức;
  - rủi ro;
  - kỹ năng;
  - phối hợp;
  - duy trì; và
  - tác động nhân quả.
- Khi nhiều hữu thể hữu tri cùng hỗ trợ và không thể phân định rõ phần đóng góp của từng cá nhân, nên ưu tiên phân bổ rộng.
- Đối với vi phạm chung, không được quy trách nhiệm chỉ dựa trên tư cách thành viên của một nhóm.
- Bất lợi về địa vị quy cho một tác nhân cụ thể phải có mối liên hệ đã xác minh với:
  - vai trò nhân quả;
  - nghĩa vụ;
  - thẩm quyền;
  - quyền kiểm soát;
  - khả năng dự liệu;
  - lợi ích;
  - sự che giấu; hoặc
  - năng lực phòng ngừa khả thi.

<a id="44-versioning"></a>

#### 4.4 Quản lý phiên bản

Phải lập phiên bản mới cho hồ sơ địa vị khi có thay đổi ở bất kỳ yếu tố nào sau đây:

- sự kiện quan trọng;
- phát hiện;
- kết quả rà soát;
- trạng thái khắc phục;
- bằng chứng đóng góp;
- phép hiệu chỉnh triển khai; hoặc
- quy tắc hiến pháp.

Phiên bản sau có thể:

- cập nhật hồ sơ địa vị cho thời gian tiếp theo;
- sửa hồi tố nếu hồ sơ trước đó sai;
- hết hiệu lực đối với một bối cảnh quyết định đã hoàn tất; hoặc
- thay thế hồ sơ cho bối cảnh quyết định mới.

Phiên bản sau phải bảo toàn dấu vết kiểm toán trước đó và giải thích điều gì đã thay đổi, ai thực hiện thay đổi, theo thẩm quyền mở hồ sơ hoặc lưu giữ nào quy định tại **§5**, dựa trên tài liệu xác minh nào và theo yêu cầu của ai.

<a id="45-implementation-tools"></a>

#### 4.5 Công cụ triển khai

Các đội có thể xây dựng công cụ thực tiễn cho hồ sơ địa vị, bao gồm:

- trường dữ liệu;
- thẻ;
- ngưỡng;
- biểu mẫu;
- bảng điều khiển;
- các bước rà soát; và
- **các phép đo đóng góp tiêu chuẩn** cho nhiệm vụ định kỳ theo **§13**.

Các công cụ đó phải giữ cho những trường bắt buộc theo **§4.1** hiển thị riêng biệt và có thể bị phản biện. Không được chôn các trường đó trong một điểm số duy nhất thiếu minh bạch hoặc một nhãn ẩn.
