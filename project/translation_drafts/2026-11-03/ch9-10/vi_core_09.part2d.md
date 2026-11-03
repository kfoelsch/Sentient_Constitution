##### 3.4.2 Kỷ luật về Quyền riêng tư

Việc chứng nhận phải yêu cầu xử lý dữ liệu tuân theo kỷ luật về quyền riêng tư sau:

- *Các Loại H, I, N, S và Y.* Đối với dữ liệu **Loại H**, **Loại I**, **Loại N**, **Loại S** và **Loại Y**, chứng nhận phải xác minh cách xử lý đáp ứng các [cơ sở về quyền riêng tư](corpus_systems/cs_06.310_data_classifications.md#privacy-link) mà từng loại dữ liệu nêu trong **CS-6.305 (*Loại thông tin và cách xử lý*) và CS-6.310** (*Phân loại dữ liệu*), bao gồm [Tính cần thiết](core_05.035_band_accountability.md#necessity), [Tính tương xứng](core_05.035_band_accountability.md#proportionality), giảm thiểu dữ liệu và sự đồng ý hoặc thẩm quyền phù hợp khác.
- *Kích hoạt chung.* Khi có nhiều hơn một điểm phát sinh quyền riêng tư liên quan, [§4.1 Quyền riêng tư (thông tin) — Kích hoạt chung](#41-privacy-informational-joint-invocation) cũng áp dụng.
- *Chỉ có nhãn là chưa đủ.* Nhãn loại dữ liệu chính xác tự nó không chứng minh được việc tuân thủ quyền riêng tư.
- *Các Tác phẩm Loại W, U và T.* Đối với tác phẩm **Loại W**, **Loại U** và **Loại T**, chứng nhận phải xác minh quyền kiểm soát của người sáng tạo được tôn trọng, bao gồm:
  - rút lại một ấn phẩm công khai theo [CS-6.310 Phần B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Loại W: Tác phẩm đã công bố*);
  - giới hạn của từng giấy phép được ghi lại theo [CS-6.310 Phần B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*Giấy phép thương mại*); và
  - [các quyền được bảo lưu](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) của người sáng tạo.
- *Không suy ra sự đồng ý.* Giấy phép chỉ bao gồm những cách sử dụng được nêu, trong phạm vi, thời hạn, lãnh thổ và phương tiện được ghi rõ. Bất cứ điều gì không được nêu vẫn thuộc về người sáng tạo. Chứng nhận không được coi cài đặt mặc định, điều khoản gộp, im lặng hoặc giấy phép rộng hơn là sự đồng ý cho cách sử dụng không được ghi trong giấy phép. Ví dụ, giấy phép chung cho phép công bố hoặc bán một tác phẩm không đồng nghĩa với sự đồng ý dùng tác phẩm đó làm dữ liệu huấn luyện; việc này cần sự đồng ý riêng của chính người sáng tạo (xem [các quyền được bảo lưu](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)).

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 Lưu trữ Bảo vệ và Lưu giữ Khóa

Đối với dữ liệu thuộc các nhóm mặc định hạn chế và không thể truy cập, chứng nhận phải xác minh hệ thống đáp ứng mức tối thiểu về lưu trữ bảo vệ và lưu giữ khóa tại [CS-6.305 Phần A §5.0 Các nhóm trạng thái truy cập](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). Hồ sơ phải thể hiện:
- nơi dữ liệu hạn chế và khóa của dữ liệu thực sự được lưu, bao gồm bản sao lưu, bộ nhớ đệm, nhật ký và vùng hoán đổi;
- văn bản thuần chỉ nằm trong các quy trình cần dùng đến nó; và
- các đường dẫn kiểm toán, xuất dữ liệu và ghi đè hợp pháp vẫn hoạt động.

Tuyên bố mã hóa mà không có bằng chứng đó không đáp ứng yêu cầu này.

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 Đánh giá lại Loại Dữ liệu theo Lịch

Mỗi lần chứng nhận hoặc tái chứng nhận một hệ thống có tác động trọng yếu, việc rà soát phải kiểm tra xem các tập dữ liệu quan trọng của hệ thống đã được:

- **đánh giá lại** để phân loại phù hợp theo **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Quản trị phân loại lại và vòng đời*) và **CJS-5.130 §18** (*các điều khoản về lưu giữ dữ liệu và tính toàn vẹn vòng đời*); và
- **phân loại lại** khi việc rà soát yêu cầu.

Việc phân loại lại loại dữ liệu khi có sự kiện theo CS-6.305 (*Loại thông tin và cách xử lý*) và CS-6.310 (*Phân loại dữ liệu*) không thay thế lần kiểm tra chứng nhận theo lịch này.

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 Bảo đảm Cơ sở Hạ tầng Điều chỉnh theo Lớp Hệ thống

Theo [§2.2 Cách lớp hệ thống điều chỉnh mọi đánh giá](#22-how-system-class-scales-every-evaluation), CS-9.305 (*Cơ chế phân loại hệ thống*) và CS-9.310 (*Phân loại tác động hệ thống*), hệ thống thuộc lớp cao hơn cần bằng chứng mạnh hơn tương xứng để chứng minh cơ sở hạ tầng xử lý, lưu trữ, thao tác, truyền tải, sao lưu, phục hồi và giám sát có thể duy trì các nội dung sau khi chịu áp lực:

- tính toàn vẹn của việc phân loại;
- khả năng quy thuộc; và
- khả năng tranh biện.

Khi các mặc định về khả năng quan sát vì lợi ích công cộng của CS-6.305 (*Loại thông tin và cách xử lý*) và CS-6.310 (*Phân loại dữ liệu*) áp dụng, chứng nhận phải xác minh rằng các hạn chế:

- được giới hạn chặt chẽ về phạm vi;
- được ghi lại và có thể kiểm toán; và
- đi kèm phương án thay thế công khai mạnh nhất có thể một cách hợp lý (ví dụ bản tóm tắt, dữ liệu tổng hợp, phiên bản đã khử định danh, công bố có độ trễ hoặc quyền tiếp cận kiểm toán có điều kiện), để giải thích nội dung bị giữ lại thay vì chỉ che giấu.

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 Độ Vững chắc của Cơ sở Hạ tầng Dữ liệu

Chứng nhận phải đánh giá cơ sở hạ tầng xử lý dữ liệu có phù hợp với loại dữ liệu và lớp hệ thống liên quan hay không. Cơ sở hạ tầng đó bao gồm:

- các lớp lưu trữ bền vững và quy trình đường ống;
- các biện pháp kiểm soát truy cập;
- ranh giới mã hóa hoặc cô lập;
- đường dẫn sao lưu và khôi phục; và
- chuỗi ủy quyền cho đơn vị vận hành hoặc nhà cung cấp.

Các thiếu sót trọng yếu về tính toàn vẹn vòng đời, khả năng chống đối kháng, tính di động hoặc khả năng khôi phục phải được ghi vào hồ sơ và phản ánh trong kết quả chứng nhận, điều kiện chứng nhận hoặc giới hạn tin cậy.

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 Sai sót và Sai lệch

Mỗi trường hợp sau đây phải được xử lý như một sai sót chứng nhận:

- phân loại sai dữ liệu;
- tái cấu trúc để né tránh;
- liên kết dữ liệu không an toàn giữa các lĩnh vực;
- cách xử lý giữ nguyên nhãn loại dữ liệu đúng nhưng vẫn phá vỡ các biện pháp bảo vệ quyền riêng tư mà loại dữ liệu đó yêu cầu;
- không có hồ sơ về người đã truy cập, xử lý hoặc thay đổi dữ liệu, khiến không thể điều tra một tổn hại đáng kể;
- **đánh giá lại loại dữ liệu theo lịch bị quá hạn hoặc bị bỏ qua**;
- dữ liệu hạn chế được lưu dưới dạng văn bản thuần hoặc vượt ra ngoài ranh giới xử lý được phép, hoặc khóa có thể bị quy trình không cần dùng tới truy cập; và
- cơ sở hạ tầng mong manh đến mức có thể dự đoán sẽ làm mất hiệu lực các biện pháp bảo vệ của CS-6.305 (*Loại thông tin và cách xử lý*) và CS-6.310 (*Phân loại dữ liệu*).

Hậu quả của các sai sót này được quy định tại [§7 Kết quả Chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="4-evaluations-where-implicated"></a>
