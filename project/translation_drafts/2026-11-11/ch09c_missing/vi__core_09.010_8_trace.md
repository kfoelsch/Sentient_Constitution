<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §8 Trace; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<details>
<summary><strong>Truy vết</strong></summary>

- Thượng nguồn:
  - [Phần B §6](core_09.005_system_alignment_certification_record_process.md#6-forum-process) (*các phát hiện của thành phần diễn đàn được tích hợp vào Hồ sơ Chứng nhận Hệ thống*);
  - [Phần B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (*kết quả và các quan ngại được nêu khi đi đến kết quả*);
  - [Phần A §1](core_09.000_system_alignment_certification_evaluation.md#1-purpose-and-role) (9.000 §1) (*mục đích chứng nhận và tổng quan quy trình*);
  - [Phần A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (*Đánh giá Phân loại Hệ thống*) (9.000 §2) đến
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*các đầu ra đánh giá được phản ánh trong Hồ sơ Chứng nhận Hệ thống*);
  - [Chương Hai đến Chương Bốn](core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*nền tảng về định nghĩa, gánh nặng, truy vết và xác minh*);
  - [Hồ sơ Chứng nhận Hệ thống](core_05.040_band_continuity.md#system-certification-record) (*ý nghĩa tại Chương Năm*);
  - [Hồ sơ Hành vi Ràng buộc Về Thực chất](core_05.035_band_accountability.md#materially-binding-act-record);
  - [Tính toàn vẹn của hồ sơ](core_05.035_band_accountability.md#record-integrity) (*quy tắc độ tin cậy áp dụng cho Hồ sơ Chứng nhận Hệ thống*);
  - [Chương Tám §8 Hồ sơ Hành vi và Chuyển giao có thể quy thuộc](core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); họ đo lường giám sát về sự thật và tính toàn vẹn nhận thức như một phép đo hiến định;
  - [**Def.O1** *Điều XVI: Kiểm toán, Minh bạch và Xác minh Độc lập*](core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- Hạ nguồn: [§9](#9-recertification-and-reopening) (*tái chứng nhận và mở lại*); [§11.3](#113-verified-input-gate) (*cổng đầu vào đã xác minh*); [Chương Mười lăm §2.3](core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*hồ sơ vụ việc của diễn đàn và tranh chấp hồ sơ tư cách*) (15.000 §2.3).
- Đọc cùng:
  - [Điều XVI: Kiểm toán, Minh bạch và Xác minh Độc lập](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Bảo toàn Chứng cứ](core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Các loại thông tin và xử lý*) và [CS-6.310 — Phân loại dữ liệu](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*Cơ chế phân loại hệ thống*) và [CS-9.310 — Phân loại tác động hệ thống](corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*Vòng đời hệ thống*);
  - **CJS-5.110 §4** (*các mức minh bạch và điều kiện truy cập kiểm toán*).
- Các tiểu mục:
  - [§8.1](#81-minimum-record-contents) (*Nội dung hồ sơ tối thiểu*), cùng với
  - [§8.1.1](#811-system-identity-scope-and-prior-system-certification-record) (*Nhận dạng, phạm vi và hồ sơ trước đó*);
  - [§8.1.2](#812-classification-and-whole-system-findings) (*Phân loại và phát hiện toàn hệ thống*);
  - [§8.1.3](#813-system-data-types-record) (*Hồ sơ Loại Dữ liệu Hệ thống*);
  - [§8.1.4](#814-rights-floor-and-domain-findings) (*Nền tảng Quyền và phát hiện theo lĩnh vực*);
  - [§8.1.5](#815-technical-evidence-and-review-findings) (*Bằng chứng kỹ thuật và phát hiện rà soát*);
  - [§8.1.6](#816-supervision-independence-and-challenge-paths) (*Giám sát, độc lập và đường khiếu nại*);
  - [§8.1.7](#817-concerns-cause-and-remediation-readiness) (*Quan ngại, nguyên nhân và mức sẵn sàng khắc phục*);
  - [§8.1.8](#818-outcome-and-reliance-limits) (*Kết quả và giới hạn phụ thuộc*);
  - [§8.1.9](#819-operating-plan) (*Kế hoạch vận hành*); và
  - [§8.1.10](#8110-completeness) (*Tính đầy đủ*);
  - [§8.2](#82-transparency-and-auditability-of-the-system-certification-record) (*Tính minh bạch và khả năng kiểm toán của Hồ sơ Chứng nhận Hệ thống*).

</details>
