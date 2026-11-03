<!-- AI-assisted translation draft; unreviewed. Source lines 576–616; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 7.2 Khiếm khuyết chứng nhận và khắc phục

*Nói đơn giản: khiếm khuyết có thể dẫn đến điều kiện, hoãn, từ chối, thu hồi hoặc xem xét mới. Việc khắc phục phải được xác minh độc lập trước khi làm căn cứ cho việc cấp phép hoặc miễn điều kiện. Việc bên vận hành có sẵn lòng và có khả năng khắc phục hay không quyết định diễn đàn phải chọn phương án nào ([§7.3 Mức độ sẵn sàng khắc phục: Ý chí và năng lực khắc phục](#73-remediation-readiness-willingness-and-capacity-to-correct), [§7.4 Từ chối và thu hồi](#74-denial-and-revocation)).*

Các khiếm khuyết chứng nhận được phát hiện trong bất kỳ đánh giá nào thuộc Phần A không phải là lỗi giấy tờ nhỏ. Chúng bao gồm:

- phân loại sai theo [§2 Đánh giá phân loại hệ thống](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation);
- khiếm khuyết đánh giá rủi ro và công bố rủi ro theo [§3.2.2 Khiếm khuyết và sai lệch](core_09.000_system_alignment_certification_evaluation.md#322-defects-and-misalignment);
- khiếm khuyết xử lý dữ liệu theo [§3.4 Đánh giá loại dữ liệu và cách xử lý](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation); và
- các khiếm khuyết theo lĩnh vực được nêu từ [§5.1 Đánh giá dấu chân sinh thái](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) đến [§5.6 Đánh giá độ đáng tin cậy và tính toàn vẹn của việc dựa vào hệ thống](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation).

Khi phát hiện khiếm khuyết như vậy, các diễn đàn có thể:

- chứng nhận kèm điều kiện;
- hoãn chứng nhận;
- từ chối chứng nhận;
- thu hồi chứng nhận;
- thay đổi khoảng thời gian chứng nhận; hoặc
- mở lại việc xem xét theo [Phần C §9 Tái chứng nhận và mở lại](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) hoặc ra lệnh xem xét mới.

Việc diễn đàn chọn phương án nào tùy thuộc vào việc bên vận hành hoặc bên quản lý có sẵn lòng và có khả năng khắc phục khiếm khuyết hay không. [§7.3 Mức độ sẵn sàng khắc phục: Ý chí và năng lực khắc phục](#73-remediation-readiness-willingness-and-capacity-to-correct) nêu phép kiểm tra đó, còn [§7.4 Từ chối và thu hồi](#74-denial-and-revocation) nêu khi nào phải từ chối hoặc thu hồi.

**Bảo vệ, khắc phục và xác minh.** Khi phát hiện khiếm khuyết, diễn đàn phải nêu rõ:

- phạm vi bị ảnh hưởng;
- biện pháp bảo vệ tạm thời và giới hạn dựa vào hệ thống; và
- công việc khắc phục cần thiết.

Diễn đàn sử dụng kết luận về nguyên nhân và các khoảng thời gian theo cấp trong [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification).

Bên vận hành hoặc bên quản lý cung cấp bằng chứng khắc phục. Cơ quan được giao nhiệm vụ xác minh bằng chứng đó một cách độc lập trước khi dùng làm căn cứ cấp phép cho phạm vi ấy hoặc miễn các điều kiện của phạm vi. Việc khắc phục phải:

- xử lý khiếm khuyết và nguyên nhân đã xác định; và
- chứng minh các biện pháp bảo vệ bị ảnh hưởng vẫn có hiệu lực, bao gồm xác nhận hồi quy khi [CS-6.345 §10 Tái chứng nhận, kiểm thử hồi quy và khiếm khuyết chứng nhận](corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-10-recertification-regression-testing-and-certification-defects) yêu cầu.

Lời hứa khắc phục hoặc tuyên bố của bên vận hành rằng công việc đã hoàn tất là chưa đủ. Bên vận hành phải đưa ra bằng chứng đã được xác minh cho thấy từng biện pháp khắc phục trực tiếp xử lý vấn đề cụ thể đã xác định. Bằng chứng cho thấy bên vận hành đã thực hiện công việc hoặc hệ thống hiện chạy được sẽ không đáp ứng yêu cầu này trừ khi nó chứng minh vấn đề đã xác định thực sự được giải quyết.

Hệ thống Chưa được chứng nhận không thể bắt đầu hoạt động mới. Nếu trong thời gian đó người ta vẫn tiếp tục dựa vào một hệ thống đang hoạt động, việc này được quyết định riêng theo quy trình của diễn đàn áp dụng và biện pháp bảo vệ thiết yếu cho sự tồn tại trong [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification).

<a id="73-remediation-readiness-willingness-and-capacity-to-correct"></a>
