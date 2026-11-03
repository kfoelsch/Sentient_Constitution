<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (vi)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*Nói đơn giản: chứng nhận cũng phải xem hệ thống tiếp xúc với những loại dữ liệu nào và có xử lý chúng phù hợp hay không — bao gồm việc các loại dữ liệu còn chính xác trong chu kỳ rà soát hiện tại không, và hạ tầng nền có đủ vững chắc để xử lý dữ liệu đó ở cấp hệ thống ấy không. Các quy tắc về loại dữ liệu và [Hồ sơ Loại Dữ liệu Hệ thống](core_05.040_band_continuity.md#system-data-types-record) nằm trong kho ngữ liệu hệ thống; chứng nhận kiểm tra việc áp dụng quy tắc trên thực tế và tính trung thực của hồ sơ.*

Chứng nhận căn chỉnh hệ thống phải đánh giá **loại dữ liệu và cách xử lý** như một phần của mọi hồ sơ chứng nhận có tác động trọng yếu. Phần này nêu những nội dung chứng nhận phải xác minh. Hệ phân loại và cơ chế xử lý dữ liệu nằm trong **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Loại và xử lý thông tin*) và [CS-6.310 — Phân loại dữ liệu](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, cùng với:

- định nghĩa chuẩn tắc về loại thông tin;
- quy tắc xử lý và yêu cầu tách biệt;
- chi tiết vòng đời; và
- [Hồ sơ Loại Dữ liệu Hệ thống](core_05.040_band_continuity.md#system-data-types-record) bền vững.

**Yêu cầu đánh giá.** Quy trình chứng nhận phải xác định liệu hệ thống:

- có nhận diện các loại dữ liệu nằm trong phạm vi một cách trọng yếu hay không; và
- có xử lý chúng theo phân loại **nghiêm ngặt nhất có thể áp dụng**, bao gồm trong quá trình chuyển đổi, tổng hợp, ủy quyền, lưu trữ, lưu giữ và liên kết xuyên miền hay không.

Đánh giá phải phản ánh hiệu quả chức năng, chứ không chỉ nhãn, định dạng hoặc giai đoạn của quy trình xử lý.
