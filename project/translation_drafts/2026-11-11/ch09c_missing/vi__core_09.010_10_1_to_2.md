<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §§10.1–10.2; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="101-when-the-path-opens"></a>

#### 10.1 Khi nào con đường mở ra

*Nói đơn giản: con đường phản đối phải mở trước khi bất kỳ ai được yêu cầu dựa vào chứng nhận. Với hệ thống chưa hoạt động, con đường mở khi kết quả đầu tiên được công bố. Với hệ thống đang hoạt động, con đường đã mở.*

Khi nào con đường mở và mở trong bao lâu:

- Với hệ thống chưa vận hành, con đường phản đối hồ sơ đã công bố mở khi công bố kết quả chứng nhận đầu tiên, bất kể kết quả là gì. Nhờ đó có thể nộp phản đối và tạm dừng việc dựa vào chứng nhận trước khi hệ thống vận hành theo [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate).
- Hệ thống đang hoạt động đã có các bên liên quan. Vì vậy, con đường của nó đã mở hoặc mở khi hồ sơ hệ thống được mở. Điều này bao gồm hệ thống trong thời hạn chuyển tiếp tiếp nhận theo [Article XXVIII-A](core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Tiếp nhận theo giai đoạn và duy trì sàn quyền*) và lần chứng nhận sau đó.
- **Các bên liên quan** là sentients chịu ảnh hưởng đáng kể từ hệ thống hoặc phụ thuộc đáng kể vào nó, theo đánh giá xác định chứ không phải do đơn vị vận hành lựa chọn.
- Cho đến khi con đường của hệ thống chưa vận hành mở, Hồ sơ Chứng nhận Hệ thống vẫn nêu tên hệ thống ([Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence)). Các con đường về thành phần, liêm chính của đầu mối và leo thang trong [§10.2 Contestability paths](#102-contestability-paths) có hiệu lực suốt quá trình rà soát.
- Con đường vẫn mở khi hệ thống còn các bên liên quan. Nếu có bên liên quan sau khi chứng nhận, việc rà soát mở lại theo [§9 Recertification and Reopening](#9-recertification-and-reopening).
- Tuyên bố hệ thống phù hợp là không có cơ sở khi hệ thống có bên liên quan nhưng không có con đường mở để phản đối Hồ sơ Chứng nhận Hệ thống.

<a id="102-contestability-paths"></a>

#### 10.2 Các con đường phản đối

*Nói đơn giản: Hồ sơ Chứng nhận Hệ thống phải chỉ rõ nơi gửi ý kiến phản đối. Có bước đầu thông thường, rồi đến diễn đàn có thẩm quyền về kết luận bị tranh chấp, con đường dự phòng khi chính diễn đàn đầu mối bị nghi vấn, và con đường leo thang. Nếu chờ đợi có thể gây hại, người phản đối có thể đến thẳng diễn đàn.*

Hồ sơ Chứng nhận Hệ thống phải nêu bốn con đường phản đối dưới đây để bất kỳ ai bị ảnh hưởng biết nơi đưa tranh chấp đến. Các con đường này áp dụng [Dispute sequencing](core_15.000_forum.md#dispute-sequencing) của Chapter Fifteen cho Hồ sơ Chứng nhận Hệ thống. Đây là đường dẫn đến diễn đàn, không phải diễn đàn mới; Chapter Fifteen vẫn xác định diễn đàn nào có thẩm quyền. Thứ tự được nêu tại [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-contestability-chain).

- **Con đường phản đối hồ sơ đã công bố** — bước đầu thông thường cho tranh chấp thông thường về Hồ sơ Chứng nhận Hệ thống. Hồ sơ nêu ghế tiếp nhận phản đối ([§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-four-seats-in-a-certification)):
  - ai nhận phản đối;
  - cách nộp; và
  - thời hạn theo [Article XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Sàn giải quyết kịp thời và chống trì hoãn*) bắt đầu khi nhận được.

  Rà soát nội bộ của đơn vị vận hành, xác nhận của nhà cung cấp hoặc phê duyệt kỹ thuật không phải con đường này.
- **Con đường diễn đàn thành phần** — phản đối một kết luận trong Hồ sơ Chứng nhận Hệ thống sẽ được chuyển đến nhóm diễn đàn Chapter Fifteen có thẩm quyền đối với kết luận đó.
- **Con đường liêm chính của đầu mối** — phản đối cách diễn đàn đầu mối điều hành quy trình, chẳng hạn bị chi phối, che giấu thông tin, tự rà soát công việc của mình hoặc tuyên bố hoàn tất chứng nhận quá sớm. Con đường này qua Integrity routing, có diễn đàn dự phòng để diễn đàn đầu mối không tự xét mình.
- **Con đường leo thang** — chuyển tranh chấp đến diễn đàn khác hoặc cao hơn theo Chapter Fifteen. Bao gồm chuyển giao, gửi câu hỏi cho diễn đàn khác quyết định, định tuyến dự phòng hoặc leo thang giữa các nhóm diễn đàn. Áp dụng khi lợi ích chính thuộc nơi khác, tính hợp hiến bị đặt vấn đề, cần sửa chữa cơ cấu, hai nhóm diễn đàn bế tắc hoặc diễn đàn sẽ phải tự xét mình.

Quyền tiếp cận trực tiếp con đường diễn đàn vẫn tồn tại khi sự chậm trễ có thể gây nguy hiểm đáng kể cho quyền, chứng cứ, tính độc lập hoặc khả năng khôi phục thực tế. Việc chưa hoàn tất con đường phản đối hồ sơ đã công bố không được cản trở các con đường diễn đàn hoặc làm hết thời hạn theo [Article XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor).
