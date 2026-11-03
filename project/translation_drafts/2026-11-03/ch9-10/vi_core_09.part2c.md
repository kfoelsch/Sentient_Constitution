#### 3.3 Ràng buộc Tính nhất quán theo Thời gian

Khi những vi phạm có thể dự đoán trong trung hoặc dài hạn chưa được xử lý, chứng nhận không được coi bất kỳ điều nào sau đây là đủ:

- chỉ số ngắn hạn;
- tuân thủ cục bộ; hoặc
- hiệu quả trong thời hạn ngắn.

Không thể chấp nhận việc chạy theo kết quả ngắn hạn nếu có thể dự đoán hợp lý rằng điều đó sẽ phá hoại một trong các nội dung sau về lâu dài, kể cả khi tổn hại tích tụ chậm, xuất hiện muộn hoặc lan qua nhiều hệ thống:

- **An toàn**;
- **Sự thật**; hoặc
- **sức khỏe và hạnh phúc**.

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 Đánh giá Loại Dữ liệu và Cách xử lý

<details>
<summary><strong><span style="color: #2563eb;">Truy xuất nguồn gốc</span></strong></summary>

- Thượng nguồn:
  - [§3](#3-whole-system-certification-evaluation) (*các yếu tố đánh giá toàn hệ thống*);
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*Áp dụng toàn hệ thống minh họa theo lớp hệ thống*);
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*nội dung hồ sơ*);
  - [§2](#2-system-class-evaluation) (*đánh giá lớp hệ thống*); nhóm đo lường Giám sát (*Sự thật và tính toàn vẹn nhận thức như một thước đo hiến pháp*);
  - [Điều XV: Tính toàn vẹn của Không gian Thông tin](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [Điều XVI: Kiểm toán, Minh bạch và Xác minh Độc lập](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Điều VII: Quyền Tự sở hữu](core_06.005_rights_part_b.md#article-vii-self-ownership).
- Hạ nguồn:
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Áp dụng xử lý dữ liệu minh họa theo lớp hệ thống*);
  - [§5.1](#51-ecological-footprint-evaluation) và
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class) (*Áp dụng dấu chân sinh thái minh họa theo lớp hệ thống*);
  - [Phần C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*tính toàn vẹn của hồ sơ*);
  - [Phần C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*yêu cầu dữ liệu đã xác minh*);
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*phân loại lại và sai lệch trong xử lý*).
- Đọc cùng với:
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Loại thông tin và cách xử lý*) và [CS-6.310 — Phân loại dữ liệu](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (bao gồm **
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Quản trị phân loại lại và vòng đời*) và **
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*Quản trị Hồ sơ Loại Dữ liệu Hệ thống*));
  - [Hồ sơ Loại Dữ liệu Hệ thống](core_05.040_band_continuity.md#system-data-types-record);
  - [Công bố Thông tin Chuẩn Sàn Giám sát Công khai](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - **CJS-5.130 §18** (*các điều khoản về lưu giữ dữ liệu và tính toàn vẹn vòng đời*),
  - **CJS-5.130 §21** (*các điều khoản về khả năng chống đối kháng và chống lạm dụng*), và
  - **CJS-5.130 §17** (*các điều khoản về khả năng tương tác, tính di động và tính toàn vẹn của quyền rút lui*) khi có liên quan trọng yếu;
  - [§4.1 Quyền riêng tư (thông tin) — Kích hoạt chung](#41-privacy-informational-joint-invocation) khi có điểm phát sinh quyền riêng tư liên quan.
- Các tiểu mục:
  - [§3.4.1](#341-type-o-baseline-disclosure) (*công bố thông tin chuẩn sàn Loại O*);
  - [§3.4.2](#342-privacy-discipline) (*kỷ luật về quyền riêng tư*);
  - [§3.4.3](#343-protective-storage-and-key-custody) (*lưu trữ bảo vệ và lưu giữ khóa*);
  - [§3.4.4](#344-scheduled-data-type-re-evaluation) (*đánh giá lại loại dữ liệu theo lịch*);
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*bảo đảm cơ sở hạ tầng điều chỉnh theo lớp hệ thống*);
  - [§3.4.6](#346-infrastructure-robustness-for-data) (*độ vững chắc của cơ sở hạ tầng dữ liệu*);
  - [§3.4.7](#347-defects-and-misalignment) (*sai sót và sai lệch*);
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Áp dụng xử lý dữ liệu minh họa theo lớp hệ thống*).

</details>

<br>

*Nói thẳng: chứng nhận cũng phải xem xét hệ thống tiếp xúc với những loại dữ liệu nào và hệ thống xử lý chúng có phù hợp hay không — kể cả loại dữ liệu còn chính xác theo chu kỳ rà soát hiện tại không và cơ sở hạ tầng nền có đủ vững chắc để xử lý dữ liệu đó ở lớp hệ thống tương ứng hay không. Quy tắc về loại dữ liệu và Hồ sơ Loại Dữ liệu Hệ thống nằm trong kho văn bản về hệ thống; chứng nhận kiểm tra xem các quy tắc đó có thực sự được áp dụng và hồ sơ có trung thực hay không.*

Chứng nhận mức độ phù hợp của hệ thống phải đánh giá **loại dữ liệu và cách xử lý** trong mọi Hồ sơ Chứng nhận Hệ thống có tác động trọng yếu. Mục này nêu những nội dung chứng nhận phải xác minh. Hệ thống phân loại loại dữ liệu và cơ chế xử lý nằm trong **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Loại thông tin và cách xử lý*) và [CS-6.310 — Phân loại dữ liệu](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, cùng với:

- các định nghĩa chuẩn tắc về loại thông tin;
- quy tắc xử lý và yêu cầu phân tách;
- chi tiết về vòng đời; và
- [Hồ sơ Loại Dữ liệu Hệ thống](core_05.040_band_continuity.md#system-data-types-record) có tính lâu bền.

**Yêu cầu đánh giá.** Quy trình chứng nhận phải xác định liệu hệ thống có:

- nhận diện được các loại dữ liệu nằm trong phạm vi trọng yếu hay không; và
- xử lý chúng theo phân loại **nghiêm ngặt nhất áp dụng**, bao gồm trong các khâu chuyển đổi, tổng hợp, ủy quyền, lưu trữ, lưu giữ và liên kết giữa các lĩnh vực.

Việc đánh giá phải phản ánh hiệu ứng chức năng, không chỉ dựa vào nhãn, định dạng hay riêng giai đoạn của quy trình.

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Công bố Thông tin Chuẩn Sàn Loại O

Khi **[chuẩn sàn Loại O tại CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)** áp dụng, chứng nhận cũng phải xác minh rằng [Công bố Thông tin Chuẩn Sàn Giám sát Công khai](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) (**Loại O**) đã công bố bao quát **phạm vi được chứng nhận**, được xác định dựa trên:

- [Điều lệ Hệ thống](core_05.040_band_continuity.md#system-charter) đang quản lý;
- lớp hệ thống được chỉ định; và
- [Ranh giới Hệ thống](core_05.040_band_continuity.md#system-boundaries) đã quan sát được.

Phần bao quát đó phải gồm các kết luận về quản trị, ưu đãi và khả năng tranh biện, cùng các vai trò được phân công theo [§3.1 Kỷ luật Quản trị, Ưu đãi và Khả năng Tranh biện](#31-governance-incentive-and-contestability-discipline).

Đối với mọi lớp hệ thống, kể cả Lớp L và Lớp P, chứng nhận cũng phải xác minh rằng Hồ sơ Chứng nhận Hệ thống được công bố dưới dạng dữ liệu chứng nhận **Loại O** theo [CS-6.310 Phần B §9.3 Loại O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data). Việc công bố hồ sơ không đòi hỏi phải có đầy đủ Công bố Thông tin Chuẩn Sàn Giám sát Công khai đối với hệ thống ngoài Lớp A, B và C.

Việc chia sẻ rủi ro đã đánh giá cũng có thể được tính vào chuẩn sàn này khi có rủi ro hệ thống. Quyền chuẩn sàn của công chúng rộng hơn phạm vi chứng nhận và không đòi hỏi lập hồ sơ riêng bên cạnh [Hồ sơ Phân loại Hệ thống](core_05.040_band_continuity.md#system-classification-record) hoặc [Hồ sơ Loại Dữ liệu Hệ thống](core_05.040_band_continuity.md#system-data-types-record).

Mỗi trường hợp giữ lại thông tin có căn cứ phải đi kèm phương án thay thế công khai mạnh nhất có thể một cách hợp lý ([§3.4.5 Bảo đảm Cơ sở Hạ tầng Điều chỉnh theo Lớp Hệ thống](#345-system-class-scaled-infrastructure-assurance) đưa ra ví dụ). Chương Năm quy định thuật ngữ; CS-6.305 (*Loại thông tin và cách xử lý*) và CS-6.310 (*Phân loại dữ liệu*) quy định nội dung chuẩn sàn và cơ chế công bố.

<a id="342-privacy-discipline"></a>
