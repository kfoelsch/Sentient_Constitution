<!-- Bản dịch có hỗ trợ AI; chưa được rà soát. Chương Chín Phần C §9.3 theo nguồn hiện tại; SHA-256 nguồn 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Commit cơ sở 247e2180509e5e029c1106878cf225067339e010; SHA-256 cơ sở faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Chỉ là bản nháp; không đồng bộ vào translations/. -->

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Chứng nhận tạm thời và đầy đủ

*Nói đơn giản: hệ thống giành được lòng tin theo từng bước. Hệ thống mới và hệ thống đã không đạt đánh giá bắt đầu với sự kiểm soát chặt hơn và được kiểm tra thường xuyên. Chỉ hệ thống hiện không có sai lệch và không có dấu hiệu sắp sai lệch mới được chuyển sang chứng nhận đầy đủ với khoảng thời gian dài hơn. Đánh giá không đạt sẽ đưa hệ thống trở lại chế độ chặt hơn.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 Hai trạng thái

Chứng nhận có một trong hai trạng thái; khoảng thời gian của từng trạng thái phải được ghi trong Hồ sơ Chứng nhận Hệ thống theo [§8.1 Nội dung tối thiểu của hồ sơ](#81-minimum-record-contents):

- **[Chứng nhận tạm thời](core_05.040_band_continuity.md#provisional-certification)** áp dụng cho lần chứng nhận đầu tiên (kể cả hệ thống mới triển khai), và cho hệ thống được chứng nhận sau lần tái chứng nhận không đạt, rà soát mở lại hoặc rà soát mới phát hiện sai lệch. Khoảng thời gian tạm thời ngắn hơn khoảng thời gian chứng nhận đầy đủ của cùng hạng hệ thống. Hồ sơ nêu giới hạn được phép dựa vào hệ thống.
- **[Chứng nhận đầy đủ](core_05.040_band_continuity.md#full-certification)** chỉ được đạt trong lần tái chứng nhận khi hệ thống đang có chứng nhận tạm thời và đáp ứng cả ba điều kiện:
  1. hoàn thành số lần tái chứng nhận tạm thời liên tiếp đạt yêu cầu, ít nhất một lần và nhiều hơn đối với hạng hệ thống cao hơn, theo văn bản được thông qua;
  2. hiện không có sai lệch: hồ sơ không ghi sai lệch đang mở, khiếm khuyết chưa khắc phục, lần kiểm tra quá hạn hoặc kiểm thử hồi quy không đạt; và
  3. không chỉ báo giám sát nào cho thấy sai lệch sắp xảy ra: các ngưỡng và số liệu xu hướng trong hồ sơ không vượt ngưỡng và không có xu hướng tiến tới ngưỡng.

Chứng nhận đầy đủ có khoảng thời gian theo hạng hệ thống; vẫn có thời hạn và không phải phê chuẩn vĩnh viễn. Lần tái chứng nhận **đạt sạch** khi đáp ứng điều kiện 2 và 3.

<details>
<summary><strong>Hướng dẫn đọc (không có hiệu lực điều hành): trạng thái chứng nhận</strong></summary>

> Bảng này tóm tắt §9.3; nếu khác với nội dung điều khoản thì nội dung điều khoản được ưu tiên.
>
> | | Tạm thời | Đầy đủ |
> |---|---|---|
> | **Ai có trạng thái này** | Lần chứng nhận đầu tiên, kể cả hệ thống mới triển khai; hoặc hệ thống sau lần tái chứng nhận không đạt hay rà soát phát hiện sai lệch | Hệ thống đạt trạng thái này khi tái chứng nhận trong lúc có trạng thái tạm thời |
> | **Cách đạt được** | Được cấp cùng với kết quả chứng nhận | Số lần tái chứng nhận tạm thời liên tiếp đạt sạch theo yêu cầu; không có sai lệch hiện tại hay chỉ báo sai lệch sắp xảy ra |
> | **Khoảng thời gian** | Ngắn hơn khoảng thời gian đầy đủ của cùng hạng hệ thống | Theo hạng hệ thống; vẫn có thời hạn |
> | **Nếu tái chứng nhận không đạt** | Áp dụng Hợp phần B §7; lần chứng nhận tiếp theo là tạm thời và số lần đạt sạch trở về không | Như cột bên cạnh |
> | **Nếu có chỉ báo sai lệch sắp xảy ra** | Vẫn tạm thời; số lần không tăng | Hạ xuống tạm thời |
>
</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 Không đạt và hạ trạng thái

Kết quả tái chứng nhận, rà soát mở lại hoặc rà soát mới quyết định trạng thái hệ thống:

- Tái chứng nhận phát hiện sai lệch hiện tại là lần tái chứng nhận **không đạt**. Áp dụng hậu quả tại [Hợp phần B §7 Kết quả chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes). Bất kể lần kiểm tra tiếp theo sạch đến đâu, chứng nhận tiếp theo có thể đạt được chỉ là tạm thời; số lần tái chứng nhận sạch trở về không.
- Nếu không có sai lệch hiện tại nhưng có chỉ báo sai lệch sắp xảy ra, lần tái chứng nhận không phải là không đạt nhưng cũng không sạch. Trạng thái tạm thời vẫn giữ nguyên và số lần không tăng; trạng thái đầy đủ hạ xuống tạm thời.
- Rà soát mở lại theo [§9 Tái chứng nhận và mở lại](#9-recertification-and-reopening) phát hiện sai lệch thì có hiệu lực như tái chứng nhận không đạt.
- Rà soát mới đối với hệ thống đang được chứng nhận mà phát hiện sai lệch hiện tại cũng có hiệu lực như vậy. Nếu hệ thống không có trạng thái chứng nhận, áp dụng quy tắc từ chối tại [Hợp phần B §7.4 Từ chối và thu hồi](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation).

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Nguyên nhân sai lệch

Khi đánh giá, tái chứng nhận, rà soát mở lại hoặc rà soát mới phát hiện sai lệch, Hồ sơ Chứng nhận Hệ thống phải nêu nguyên nhân là:

- **do thiết kế:** hệ thống hoặc quy trình được xây dựng theo cách tạo ra kết quả sai lệch ngay cả khi vận hành đúng dự kiến;
- **do vận hành:** thiết kế nhìn bề ngoài là phù hợp, nhưng cách vận hành, cung cấp đầu vào hoặc bảo trì làm kết quả sai lệch; hoặc
- **chưa xác định:** biện pháp khắc phục cho cả thiết kế và vận hành vẫn được để ngỏ cho đến khi diễn đàn xác định nguyên nhân.

Kết luận về nguyên nhân tuân theo các giới hạn sau:

- Nếu Hệ thống tiếp tục tạo ra kết quả sai lệch thì nó sai lệch, dù thiết kế trên giấy có vẻ phù hợp. Thiết kế có vẻ phù hợp không phải là biện hộ.
- Thiết kế mà nếu thực hiện sẽ tạo ra kết quả sai lệch đã là sai lệch trước khi kết quả đó xuất hiện.
- Kết luận về nguyên nhân xác định biện pháp khắc phục cần tìm và phạm vi rà soát mở lại; kết luận đó không bao giờ quyết định hệ thống có sai lệch hay không.

Nếu sai lệch do thiết kế:

- số lần tái chứng nhận sạch vẫn bằng không cho tới khi thiết kế lại được triển khai và xác minh;
- diễn đàn xác định nguyên nhân, hoặc diễn đàn kế tiếp được phân công theo [Hợp phần B §6.2 Trình tự giám sát](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), xác minh thiết kế lại trong [mục tiêu tiếp nhận tương ứng](core_05.040_band_continuity.md#tier-window), và có thể làm việc đó ngay trong lần tái chứng nhận tạm thời đầu tiên;
- **đánh giá cấu phần** (phần đánh giá chứng nhận của một cấu phần, theo định nghĩa tại [Hợp phần B §6.1 Giám sát diễn đàn và vai trò cấu phần](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles)) trước khi thiết kế lại được xác minh sẽ không tính vào số lần sạch, dù kết quả sạch; và
- thay đổi cách vận hành hệ thống không đáp ứng bước này.

Các quy tắc này bổ sung, không thay thế, các gạch đầu dòng về hạ trạng thái ở trên. Người vận hành hoặc bất kỳ chúng sinh có ảnh hưởng nào có thể yêu cầu diễn đàn rà soát kết luận nguyên nhân; nếu kết luận thay đổi, các quy tắc này không còn áp dụng.

<a id="934-tier-windows"></a>
##### 9.3.4 Thời hạn theo cấp độ

Khi đánh giá ban đầu, tái chứng nhận, rà soát mở lại hoặc rà soát mới phát hiện sai lệch:

- vụ việc được phân loại theo các cấp độ trọng yếu tại [Chương Mười lăm §6 Giải quyết đúng hạn, cấp độ trọng yếu và kỷ luật chống trì hoãn](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline);
- theo giả định, vụ việc thuộc cấp độ tương ứng với hạng hệ thống (ví dụ sai lệch ở hệ thống Hạng A mặc định thuộc Cấp độ A);
- tiếp nhận, bảo toàn chứng cứ, bảo vệ tạm thời và quyết định tuân theo thời hạn và giới hạn tối đa của cấp độ đó; và
- việc quá hạn được rà soát theo yêu cầu của điều khoản đó.

<a id="935-class-a-reliance"></a>
##### 9.3.5 Việc dựa vào hệ thống Hạng A

So với chứng nhận đầy đủ, chứng nhận tạm thời có khoảng thời gian ngắn hơn nên tái chứng nhận diễn ra sớm hơn ([§9.3.1 Hai trạng thái](#931-the-two-statuses)); các giới hạn dựa vào hệ thống được ghi trong hồ sơ ([§8.1 Nội dung tối thiểu của hồ sơ](#81-minimum-record-contents)). Việc gián đoạn được xử lý như sau:

- Bản thân chứng nhận tạm thời không buộc phải gián đoạn hệ thống nếu việc gián đoạn sẽ cắt nguồn cung nhu yếu phẩm sinh tồn trước khi có phương án thay thế;
- bảo vệ tạm thời và các điều kiện chứng nhận theo [Hợp phần B §7 Kết quả chứng nhận](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) xử lý trường hợp đó;
- quy tắc tương tự áp dụng khi số lần bị giữ lại sau kết luận sai lệch do thiết kế: riêng việc giữ số lần không bao giờ làm gián đoạn hệ thống mà chúng sinh phụ thuộc; và
- trong suốt thời gian giữ lại, diễn đàn nêu rõ biện pháp bảo vệ tạm thời, điều kiện chứng nhận về việc dựa vào hệ thống và thông báo cho người phụ thuộc.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 Xác minh, không chỉ khẳng định

Trạng thái hệ thống, số lần tái chứng nhận sạch và chỉ báo giám sát phải được xác minh; việc xác minh phải cho phép rà soát độc lập. Chỉ lời khẳng định của hệ thống là không đủ:

- Không được chọn hoặc đặt chỉ báo theo cách khiến sai lệch không bao giờ có thể xuất hiện.
- Thiết kế lại cũng phải được xác minh bằng chứng cứ mà người khác có thể kiểm tra.
- Chứng nhận đầy đủ không loại bỏ bất kỳ lý do nào để mở lại rà soát. Mọi yếu tố kích hoạt tại [§9 Tái chứng nhận và mở lại](#9-recertification-and-reopening) vẫn áp dụng.
- Việc né tránh được xử lý theo [§9.4 Không né tránh](#94-non-evasion).
