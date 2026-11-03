<!-- AI-assisted translation draft; unreviewed. Source lines 443–513; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

### 7. Kết quả Chứng nhận

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn:
  - [§6](#6-forum-process) (*quy trình diễn đàn và khả năng khiếu nghị đáng tin cậy*);
  - [Phần A §2 Đánh giá Cấp Hệ thống](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) đến
  - [§5 Đánh giá Sàn Quyền và Lĩnh vực](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*phân loại sai, không căn chỉnh và khiếm khuyết phát hiện trong đánh giá*);
  - [Hai Mục tiêu Hiến định](core_00.000_preamble.md#two-constitutional-aims);
  - [Chương Ba §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1)
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*tính toàn vẹn định nghĩa và né tránh*);
  - [Chương Ba §2.1 Các Kiểu Né tránh Thường gặp](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*né tránh phạm vi và ranh giới*);
  - [Điều lệ Hệ thống](core_05.040_band_continuity.md#system-charter) (*không khớp giữa Điều lệ Hệ thống và hành vi, cùng việc xem xét quá hạn*).
- Hạ nguồn:
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*nêu kết quả trong hồ sơ*);
  - [Phần C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*mở đường khiếu nghị cùng với kết quả*);
  - [Phần C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*chứng nhận lại và mở lại*);
  - [Phần C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*cổng đầu vào đã xác minh khi sự kiện hỗ trợ phát hiện bất lợi*);
  - [Chương Mười Ba](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*giám sát diễn đàn*);
  - [Chương Mười](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Đọc cùng: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Tái phân loại và Quản trị Vòng đời*) về việc đánh giá lại loại dữ liệu theo lịch; và **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yêu cầu Tái phân loại*) về các điều kiện kích hoạt đánh giá lại cấp hệ thống và xác minh SAC.
- Các tiểu mục:
  - [§7.1](#71-go-live-gate) (*cổng đưa vào hoạt động*, gồm
    - [§7.1.1 Hệ thống đang vận hành](#711-systems-already-operating) và
    - [§7.1.2 Thí điểm](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*khiếm khuyết chứng nhận và khắc phục*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*mức sẵn sàng khắc phục: ý chí và năng lực sửa chữa*, gồm
    - [§7.3.1 Ý chí](#731-willingness),
    - [§7.3.2 Năng lực](#732-capacity),
    - [§7.3.3 Bước chứng minh](#733-proof-step),
    - [§7.3.4 Kết luận](#734-findings), và
    - [§7.3.5 Điều khoản như nhau cho mọi đơn vị vận hành](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*từ chối và thu hồi*, gồm
    - [§7.4.1 Từ chối và thu hồi là gì](#741-what-denial-and-revocation-are),
    - [§7.4.2 Khi nào phải từ chối hoặc thu hồi](#742-when-denial-or-revocation-is-required),
    - [§7.4.3 Ưu tiên bảo vệ](#743-protection-first),
    - [§7.4.4 Quy trình](#744-process),
    - [§7.4.5 Hiệu lực](#745-effect), và
    - [§7.4.6 Không phải lệnh cấm vĩnh viễn](#746-not-a-permanent-bar)).

</details>

<br>

*Nói đơn giản: mọi lần xem xét chứng nhận đều kết thúc bằng một kết quả được nêu rõ, có chứng cứ và các quan ngại nêu ra trong quá trình hỗ trợ. Không gì được đưa vào hoạt động cho đến khi hệ thống được chứng nhận, sentient bị ảnh hưởng có cơ hội thực tế để khiếu nghị kết quả đã công bố, và các biện pháp bảo vệ bắt buộc trước khi vận hành được kiểm tra.*

Phần này là **Giai đoạn IV, Quyết định**, sau [§6 Quy trình Diễn đàn](#6-forum-process) (**Giai đoạn III, Xem xét**). Phần này trình bày kết quả mà các diễn đàn đưa ra. [§7.1 Cổng Đưa vào Hoạt động](#71-go-live-gate) nêu cổng này, còn [§7.2 Khiếm khuyết Chứng nhận và Khắc phục](#72-certification-defects-and-correction) nêu việc cần làm khi phát hiện khiếm khuyết.

Quyết định chứng nhận phải được ghi trong hồ sơ theo [Phần C §8.1 Nội dung hồ sơ tối thiểu](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents), cùng với các quan ngại được nêu khi đi đến quyết định. Kết quả là một trong các loại sau:

- chứng nhận tạm thời;
- chứng nhận đầy đủ;
- chứng nhận có điều kiện;
- chứng nhận hoãn;
- không chứng nhận;
- rút lại;
- hết hạn; hoặc
- miễn điều kiện.

Hệ thống không có chứng nhận tạm thời cũng không có chứng nhận đầy đủ là **Chưa được Chứng nhận**. Điều này áp dụng khi chứng nhận:

- bị hoãn;
- bị từ chối;
- bị rút lại; hoặc
- hết hạn.

Chứng nhận tạm thời và chứng nhận đầy đủ là hai **trạng thái** của chứng nhận. [Phần C §9.2 Chứng nhận Tạm thời và Đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) giải thích cách hệ thống đạt được, duy trì và mất từng trạng thái. Điều kiện của chứng nhận có điều kiện có thể gắn với một trong hai trạng thái.

<a id="71-go-live-gate"></a>
