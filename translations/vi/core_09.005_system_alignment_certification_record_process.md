<!-- AI-assisted translation draft; unreviewed. Complete current-source Chapter Nine Part B, lines 1–775; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. Draft only; do not synchronize into translations/. -->

<a id="chapter-nine-part-b-certification-forum-process-and-outcomes"></a>
<a id="chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes"></a>

# CHƯƠNG CHÍN, PHẦN B: CHỨNG NHẬN MỨC ĐỘ PHÙ HỢP CỦA HỆ THỐNG — QUY TRÌNH VÀ KẾT QUẢ CỦA DIỄN ĐÀN
<details>
<summary><strong><span style="color: #2563eb;">Vị trí trong kho văn bản (không có hiệu lực vận hành): cấu trúc tệp và quy tắc đọc</span></strong></summary>

> Tệp này **là một phần của Hiến pháp Sentient** và chỉ **có hiệu lực ràng buộc khi được đọc cùng nhau** với các tệp `core_*` được đánh số khác như một văn bản thống nhất. Tệp này gồm **Chương Chín, Phần B** — **quy trình của diễn đàn** (vai trò thành phần, trình tự giám sát và chuỗi khả năng khiếu nại) cùng các **kết quả** chứng nhận và cổng trước khi đưa vào hoạt động (**§6–§7**, tiếp nối Phần A §§1–5). **Phần A** — mục đích, khung phân loại (loại hệ thống) và yêu cầu đánh giá — nằm trong [`core_09.000_system_alignment_certification_evaluation.md`](core_09.000_system_alignment_certification_evaluation.md). **Phần C** — **hồ sơ** chứng nhận và tính toàn vẹn của hồ sơ, lộ trình **khiếu nại** cùng việc tái chứng nhận và mở lại, và cầu nối **tư cách** (**§8–§10**) — nằm trong [`core_09.010_system_alignment_certification_record_recertification.md`](core_09.010_system_alignment_certification_record_recertification.md).
>
> - **Chủ thể chịu trách nhiệm theo Hiến pháp (chung với Phần A và C):** chứng nhận mức độ phù hợp của hệ thống và hồ sơ liên quan dưới sự giám sát của diễn đàn. Trong nhánh **giám sát** của Tứ trụ, SAC là một quy trình kiểm toán đặc biệt lớn và có rủi ro cao giữa nhiều quy trình khác; các chuẩn tối thiểu về kiểm toán vẫn thuộc **Article XVI** (*Kiểm toán, minh bạch và xác minh độc lập*) và Chương Năm [Khả năng kiểm toán](core_05_band_oversight.md#auditability).
> - **Đầu vào đánh giá:** [Phần A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) đến [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) cung cấp kết quả đánh giá để các diễn đàn xem xét và làm căn cứ cho kết quả.
> - **Quy tắc không chuyển dịch trách nhiệm:** Phần B không nhắc lại cơ chế đánh giá của Phần A, các định nghĩa chuẩn tắc của Chương Năm, phép đo tư cách ở Chương Mười hoặc các hệ quả về tư cách ở Chương Mười Một. Ranh giới của cầu nối tư cách được nêu tại [Phần C §10](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing). Phần B cũng không chuyển quyền sở hữu kiểm toán khỏi **Article XVI** (*Kiểm toán, minh bạch và xác minh độc lập*) / **Def.O1** / **CJS-5.110 §3 và CJS-5.115 §3** (*Nơi quy định quy trình kiểm toán*)–**CJS-5.110 §5**.
>
> **Căn cứ đầu vào:** [Phần A](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-system-alignment-certification--evaluation); [Chương Tám](../../core_08.000_functional_independence_separation_of_duties.md#chapter-eight-functional-independence-and-separation-of-duties) về tính độc lập chức năng và phân tách nhiệm vụ; giám sát diễn đàn tại Chương Mười Ba; kỷ luật xác minh tại các Chương Hai đến Bốn.
> **Căn cứ đầu ra:** [Phần C](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing); hồ sơ tư cách và đầu vào đã xác minh của Chương Mười; hệ quả về tư cách của Chương Mười Một.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Truy nguyên</span></strong></summary>

- Căn cứ đầu vào:
  - [Phần A §1](core_09.000_system_alignment_certification_evaluation.md#1-purpose-and-role) (9.000 §1) (*mục đích chứng nhận và tổng quan quy trình*);
  - [Phần A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) đến
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*kết quả đánh giá cho hồ sơ*);
  - [Chương Tám §2 Yêu cầu Hiến pháp về Bốn vị trí](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement) (8.000 §2);
  - [Tứ trụ Hiến pháp](core_00_preamble.md#constitutional-tetrad);
  - [Hai Mục tiêu Hiến pháp](core_00_preamble.md#two-constitutional-aims).
- Căn cứ đầu ra:
  - [§6](#6-forum-process) và
  - [§7](#7-certification-outcomes);
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) đến
  - [§10](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) (*hồ sơ, tái chứng nhận và cầu nối tư cách*);
  - [Chương Mười](core_11_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000);
  - [Chương Mười Ba](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (13.000).
- Đọc cùng với: **[CF-13.415](../../corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-routing-operations-transfer-questions-for-ruling-and-representative-treatment)** (*Định tuyến hoạt động, chuyển giao, chứng nhận và đối xử với đại diện*) và **[CF-13.425](../../corpus_forum/cf_15.425_integrity_safeguards_anti_capture_anti_self_judging.md#cf-15425-integrity-safeguards-anti-capture-operations-and-anti-self-judging-support)** (*Biện pháp bảo vệ tính toàn vẹn, hoạt động chống chiếm quyền và hỗ trợ chống tự xét xử*).

</details>

<br>

Chương Chín, **Phần B**, chịu trách nhiệm theo Hiến pháp đối với các phần sau của chứng nhận mức độ phù hợp của hệ thống:

- **Giai đoạn III, Xem xét:** **quy trình do diễn đàn giám sát** ([§6 Quy trình của diễn đàn](#6-forum-process)); và
- **Giai đoạn IV, Quyết định:** các **kết quả** ([§7 Kết quả chứng nhận](#7-certification-outcomes)).

**Phần C** tiếp tục với **Giai đoạn V, Hồ sơ** và **Giai đoạn VI, Vận hành** (tái chứng nhận và mở lại, cùng cầu nối tư cách): [Phần C §8 Hồ sơ chứng nhận hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record), [§9 Tái chứng nhận và mở lại](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening), và [§10 Quan hệ với tư cách](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing).

Yêu cầu đánh giá nằm trong **[Phần A](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-system-alignment-certification--evaluation)** (**Giai đoạn I, Định khung** và **Giai đoạn II, Đánh giá**), kết thúc tại [§5 Đánh giá nền tảng quyền và lĩnh vực](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations). Phần này tiếp tục chương tại **§6** (*Quy trình của diễn đàn*), còn Phần C tiếp tục tại **§8** (*Hồ sơ chứng nhận hệ thống*). [Phần A §1.2 Tổng quan chứng nhận](core_09.000_system_alignment_certification_evaluation.md#12-certification-at-a-glance) trình bày toàn bộ quy trình.

*Nói đơn giản: Phần A giải thích cách **định khung** và **đánh giá** một hệ thống. Phần B giải thích việc gì xảy ra tiếp theo. Các diễn đàn xem xét kết luận và đưa ra **kết quả**; không có gì được đưa vào hoạt động cho đến khi hệ thống được chứng nhận. Phần C đề cập những việc sau quyết định: **hồ sơ**, lộ trình **khiếu nại**, duy trì hiệu lực chứng nhận và mối liên hệ với **tư cách**.*

Chứng nhận theo Phần này:

- được các diễn đàn giám sát và có thể bị khiếu nại theo [§6 Quy trình của diễn đàn](#6-forum-process); lộ trình khiếu nại hồ sơ đã công bố được mở theo [Phần C §9.1 Khiếu nại một chứng nhận](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification); và
- kết thúc bằng một kết quả được nêu theo [§7 Kết quả chứng nhận](#7-certification-outcomes); không hệ thống nào được đưa vào hoạt động trước khi được chứng nhận.

Kết quả được ghi vào một **Hồ sơ chứng nhận hệ thống** duy nhất có phạm vi giới hạn theo [Phần C §8 Hồ sơ chứng nhận hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record), được duy trì cập nhật theo [Phần C §9 Tái chứng nhận và mở lại](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening), và chỉ có thể cung cấp đầu vào đã xác minh cho Chương Mười thông qua [Phần C §10 Quan hệ với tư cách](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing).

Biểu đồ dưới đây thể hiện phần Phần B và Phần C trong sơ đồ quy trình tại [Phần A §1.2 Tổng quan chứng nhận](core_09.000_system_alignment_certification_evaluation.md#12-certification-at-a-glance): từ **Giai đoạn III, Xem xét** đến **Giai đoạn VI, Vận hành** ([§6 Quy trình của diễn đàn](#6-forum-process) đến [Phần C §10 Quan hệ với tư cách](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)). Phần B phụ trách các nút xem xét và quyết định ([§6 Quy trình của diễn đàn](#6-forum-process) và [§7 Kết quả chứng nhận](#7-certification-outcomes)). Phần C phụ trách các nút hồ sơ, tái chứng nhận và cầu nối tư cách ([§8 Hồ sơ chứng nhận hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) đến [§10 Quan hệ với tư cách](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)). Biểu đồ bắt đầu từ công việc định khung và đánh giá ở Phần A; mỗi lượt xem xét mới quay lại đó qua đầu nối A.

```mermaid
flowchart TB
    PA["§2–§5 Phần A — Giai đoạn I–II<br/><br/>Hệ thống đã được phân loại và đánh giá;<br/>các kết luận đánh giá được chuyển tiếp"]
    F["§6 Giai đoạn III, Xem xét<br/>Đánh giá độc lập bằng chứng<br/>và quan ngại của các bên liên quan<br/><br/>Các diễn đàn được giao nhiệm vụ đưa ra kết luận;<br/>các lộ trình khiếu nại luôn mở"]
    Rec["§8 Giai đoạn V, Hồ sơ<br/>Một Hồ sơ chứng nhận hệ thống<br/><br/>Mở để diễn đàn xem xét; hoàn tất cùng kết quả,<br/>kết luận hỗ trợ, điều kiện và kế hoạch vận hành"]
    S[["Chương Mười — Hồ sơ<br/>tư cách<br/><br/>Ngoài chương này"]]
    O{"§7 Giai đoạn IV, Quyết định<br/><br/>Bằng chứng ủng hộ kết quả và<br/>trạng thái nào?"]
    Fc["§7, §9.2 Chứng nhận đầy đủ<br/><br/>Cần các lần tái chứng nhận tạm thời đạt yêu cầu liên tiếp;<br/>không có sai lệch hiện tại hoặc được dự báo sắp xảy ra<br/>Khoảng thời gian chứng nhận đầy đủ; có thể kèm điều kiện"]
    Pc["§7, §9.2 Chứng nhận tạm thời<br/><br/>Cấp lần đầu, khôi phục sau sai lệch,<br/>hoặc duy trì hay hạ cấp trạng thái tạm thời<br/>Khoảng thời gian tạm thời ngắn hơn; có thể kèm điều kiện"]
    Nc["§7 Chưa được chứng nhận<br/><br/>Hoãn, từ chối, thu hồi hoặc hết hạn<br/>Không đưa vào hoạt động; nêu lý do và công việc khắc phục cần thiết"]
    Pub["§7, §9.1 Công bố hồ sơ đã hoàn tất<br/><br/>Mở lộ trình khiếu nại hồ sơ đã công bố;<br/>với phạm vi mới hoặc mở rộng, nêu việc đưa vào hoạt động và thông báo"]
    G{"§7 Cổng đưa vào hoạt động<br/><br/>Đã đáp ứng chứng nhận và các điều kiện<br/>tiên quyết áp dụng chưa?"]
    Hold["§7 Đáp ứng điều kiện tiên quyết để đưa vào hoạt động<br/><br/>Hoàn tất thông báo và xác minh độc lập<br/>các điều kiện phải đáp ứng trước khi vận hành"]
    Rm["§7 Bảo vệ và khắc phục<br/><br/>Không đưa vào hoạt động mới trong phạm vi bị ảnh hưởng;<br/>bảo vệ các sentient bị ảnh hưởng, khắc phục thiết kế hoặc vận hành,<br/>và nộp bằng chứng để xác minh độc lập"]
    Ch["§9–§9.2 Giai đoạn VIa, Vận hành và tái chứng nhận<br/>Giám sát và duy trì các khiếu nại luôn mở<br/><br/>Vận hành trong phạm vi và điều kiện đã chứng nhận;<br/>theo dõi kết quả, ứng phó sự cố và khiếu nại"]
    S2[["Chương Mười — Hồ sơ<br/>tư cách<br/><br/>Ngoài chương này"]]
    Re["§9 Lượt xem xét tiếp theo<br/><br/>Tái chứng nhận, mở lại hoặc xem xét mới;<br/>mỗi lượt mở hồ sơ mới liên kết với hồ sơ trước"]
    Sp["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpL["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpA["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    A1((A)) --> PA
    PA --> F
    F --> O
    O --> Fc
    O --> Pc
    O --> Nc
    Fc --> Rec
    Pc --> Rec
    Nc --> Rec
    Rec -.->|VIb, §10 —<br/>chỉ đầu vào đã xác minh;<br/>chứng nhận hiện tại hoặc sự kiện<br/>phát sinh trong quá trình chứng nhận| S
    Rec --> Pub
    Rec ~~~ Sp
    Pub --> G
    G ~~~ SpL
    G -->|Chưa được chứng nhận| Rm
    G --->|Có: vận hành<br/>trong phạm vi hồ sơ| Ch
    G --->|Đã chứng nhận,<br/>điều kiện tiên quyết còn chờ| Hold
    Hold --> G
    Ch -->|Khiếm khuyết trọng yếu:<br/>bảo vệ và khắc phục| Rm
    Ch -->|Theo lịch, hoặc có<br/>thay đổi trọng yếu hay<br/>khiếu nại đáng tin cậy<br/>cần xem xét| Re
    Ch -.->|VIb, §10 —<br/>chỉ đầu vào đã xác minh;<br/>hoạt động có thể cung cấp sự kiện<br/>cho hồ sơ Đóng góp và<br/>Vi phạm| S2
    Rm -->|Bằng chứng khắc phục<br/>được kiểm tra trong lượt<br/>xem xét tiếp theo| Re
    S2 ~~~~ SpA
    SpA ~~~ Re
    Re --> A2((A))
    style Sp fill:none,stroke:none,color:#111111
    style SpL fill:none,stroke:none,color:#111111
    style SpA fill:none,stroke:none,color:#111111
    style PA fill:none,stroke:#16a34a,color:#ffffff
    style Ch fill:none,stroke:#16a34a,color:#ffffff
    style F fill:none,stroke:#ea580c,color:#ffffff
    style Rec fill:none,stroke:#2563eb,color:#ffffff
    style S fill:none,stroke:#db2777,color:#ffffff
    style S2 fill:none,stroke:#db2777,color:#ffffff
    style O fill:none,stroke:#ea580c,color:#ffffff
    style Fc fill:none,stroke:#9333ea,color:#ffffff
    style Pc fill:none,stroke:#9333ea,color:#ffffff
    style Nc fill:none,stroke:#9333ea,color:#ffffff
    style G fill:none,stroke:#ea580c,color:#ffffff
    style Pub fill:none,stroke:#2563eb,color:#ffffff
    style Rm fill:none,stroke:#9333ea,color:#ffffff
    style Hold fill:none,stroke:#16a34a,color:#ffffff
    style Re fill:none,stroke:#16a34a,color:#ffffff
    style A1 fill:none,stroke:#64748b,color:#ffffff
    style A2 fill:none,stroke:#64748b,color:#ffffff
```

<a id="6-forum-process"></a>

### 6. Quy trình diễn đàn

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn:
  - [Phần A §3 Đánh giá chứng nhận toàn hệ thống](core_09.000_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation) (9.000 §3),
  - [§4 Đánh giá khi có liên quan](core_09.000_system_alignment_certification_evaluation.md#4-evaluations-where-implicated), và
  - [§5 Đánh giá sàn quyền và lĩnh vực](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*các phát hiện đánh giá mà diễn đàn xem xét*);
  - [Chương Tám §2 Yêu cầu hiến định về bốn ghế](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement) (8.000 §2) và
  - [§9 Quan hệ với các quy trình tiếp theo](core_07_functional_independence_segregation_of_duties.md#9-relationship-to-later-processes) (*bốn ghế và nghĩa vụ nêu rõ việc chứng nhận sử dụng chúng thế nào; được áp dụng tại
  - [§6.1.1](#611-four-seats-in-a-certification)*);
  - [Bản đồ vai trò theo điều lệ](../../core_05.040_band_continuity.md#charter-role-map) (*vị trí bố trí các ghế cho một chứng nhận*);
  - [Chương Mười Ba §4](core_11_forum.md#4-forum-family-definitions--accountability-through-adjudication) (13.000 §4) (*các họ diễn đàn, chứng nhận căn chỉnh do Integrity dẫn dắt, chuyển giới thiệu thành phần và xác nhận*);
  - [Chương Mười Ba §3](core_11_forum.md#3-transfer-consolidation-and-coordination--continuity-and-anti-capture) (13.000 §3) (*điều phối căn chỉnh do Integrity dẫn dắt và chống tự xét xử*); họ đo lường tính đúng hạn (*Giải quyết kịp thời và kỷ luật chống trì hoãn*);
  - [Bộ Tứ Hiến định](core_00_preamble.md#constitutional-tetrad) — **tham gia**, **giám sát**, **trách nhiệm giải trình** và **tính đúng hạn**;
  - [Khả năng bị phản biện](../../core_05.035_band_accountability.md#contestability).
- Hạ nguồn:
  - [§7](#7-certification-outcomes) (*kết quả và cổng đưa vào hoạt động*);
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*nội dung và tính toàn vẹn của hồ sơ*);
  - [Phần C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*chứng nhận lại, mở lại và đường dẫn khiếu nghị*);
  - [Phần C §10](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) (*cổng đầu vào đã được xác minh*);
  - [Chương Mười Ba §5](../../core_15.000_forum.md#5-escalation-and-questions-for-ruling) (13.000 §5) (*chuyển cấp giữa các họ diễn đàn và chứng nhận hiến định*).
- Đọc cùng:
  - [Trình tự giải quyết tranh chấp](core_11_forum.md#dispute-sequencing) theo Chương Mười Ba §1;
  - [Lời mở đầu §3.3](core_00_preamble.md#33-governance-layers);
  - **CF-13.415** (*định tuyến hoạt động, chuyển giao, chứng nhận và đối xử theo tư cách đại diện*),
  - **CF-13.425** (*bảo đảm tính toàn vẹn, hoạt động chống chiếm đoạt và hỗ trợ chống tự xét xử*), và
  - **CF-13.440** (*diễn đàn chuyên gia kỹ thuật và phòng chuyên môn*);
  - [Điều XIII-A](core_06_rights_part_c.md#article-xiii-a-reliability-and-trustworthiness-baseline) (*Nền tảng về độ tin cậy và tính đáng tin*) và
  - [Điều XIII-B](core_06_rights_part_c.md#article-xiii-b-right-to-redress-and-remedy) (*Quyền yêu cầu khắc phục và biện pháp cứu tế*).
- Các tiểu mục:
  - [§6.1](#61-forum-supervision-and-component-roles) (*vai trò của các thành phần diễn đàn*, gồm
  - [§6.1.1 Bốn ghế trong một chứng nhận](#611-four-seats-in-a-certification) và
  - [§6.1.2 Diễn đàn Kỹ thuật](#612-technical-forums) đến
  - [§6.1.7 Các họ diễn đàn hiến định và thường lệ khác](#617-constitutional-and-other-regular-forum-families), mỗi họ diễn đàn có một tiểu mục);
  - [§6.2](#62-supervisory-sequence) (*trình tự giám sát*, gồm
  - [§6.2.1 Mở đường khiếu nghị trước](#621-challenge-path-first),
  - [§6.2.2 Trình tự mặc định](#622-default-sequence),
  - [§6.2.3 Bảo vệ khẩn cấp](#623-urgent-protection), và
  - [§6.2.4 Tham gia trong khi xem xét](#624-participation-during-review));
  - [§6.3](#63-contestability-chain) (*chuỗi khả năng bị phản biện*);
  - [§6.4](#64-anti-bypass) (*chống né tránh*); đọc cùng
  - [Phần C §9.1](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification) (*khiếu nghị chứng nhận*) và
  - [Phần C §9.1.1](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths) (*các đường dẫn phản biện*).

</details>

<br>

*Nói đơn giản: chứng nhận không phải là một đống ý kiến từ nhiều nơi. Công việc đánh giá có thể diễn ra song song, nhưng từ đây hồ sơ đi theo thứ tự: xem xét, rồi quyết định, rồi công bố hồ sơ. Mỗi loại diễn đàn xử lý một phần xác định của việc xem xét, còn một diễn đàn chủ trì kết hợp các phần đó. Các bên bị ảnh hưởng có thể khiếu nghị ở đúng cấp độ nơi tranh chấp phát sinh, không bị lạc trong bộ máy quan liêu nội bộ hay bị chuyển lòng vòng giữa các diễn đàn.*

Phần này là **Giai đoạn III, Xem xét**. Phần này quy định **trình tự giám sát** theo hiến định (thứ tự các diễn đàn giám sát hồ sơ chứng nhận) và **chuỗi khả năng bị phản biện** (các đường khiếu nghị tương ứng với nơi phát sinh tranh chấp).

Đối với các hệ thống có ảnh hưởng trọng yếu, quy trình do diễn đàn giám sát theo Chương Mười Ba là bắt buộc ở mọi nơi diễn đàn hành động về chứng nhận. Công việc đó gồm các giai đoạn sau:

- **Giai đoạn III, Xem xét** (phần này): xem xét độc lập chứng cứ và quan ngại của các bên liên quan trong từng lượt;
- **Giai đoạn IV, Quyết định** ([§7 Kết quả chứng nhận](#7-certification-outcomes)): kết quả. Đó là **chứng nhận** căn chỉnh hiến định chính thức (tạm thời hoặc đầy đủ, có hoặc không có điều kiện), hoãn, **không chứng nhận**, **rút lại**, hoặc miễn điều kiện;
- **Giai đoạn V, Hồ sơ** ([Phần C §8 Hồ sơ Chứng nhận Hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)): hoàn tất và công bố một Hồ sơ Chứng nhận Hệ thống duy nhất; và
- **Giai đoạn VIa, Vận hành và chứng nhận lại** ([Phần C §9 Chứng nhận lại và Mở lại](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening)): **chứng nhận lại**, **xác nhận** một hệ thống hiện có, và xem xét được mở lại hoặc xem xét mới. Mỗi việc bắt đầu một lượt mới quay về Giai đoạn I.

Chứng nhận chấm dứt khi hết hạn theo thời gian. Việc này không cần diễn đàn hành động, nhưng vẫn phải được nêu trong hồ sơ theo [Phần C §8 Hồ sơ Chứng nhận Hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record).

Theo [Bộ Tứ Hiến định](core_00_preamble.md#constitutional-tetrad):

- trình tự giám sát đưa **giám sát** và **trách nhiệm giải trình** vào thực tiễn xuyên suốt các họ diễn đàn; và
- chuỗi khả năng bị phản biện đưa **tham gia** và **tính đúng hạn** vào thực tiễn, để các sentient bị ảnh hưởng có thể khiếu nghị chứng nhận trước khi sự lệ thuộc của họ trở nên không thể đảo ngược trong các hệ thống kiểm soát nhu cầu sinh tồn thiết yếu, giáo dục hoặc an toàn.

Quy trình diễn đàn chi tiết thuộc tầng sở hữu **Diễn đàn và thẩm quyền** ([Chương Mười Ba](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction)). Chi tiết vận hành được định tuyến theo **[CS-9.315](../../corpus_systems/cs_09.315_system_alignment_certification_run_sheet.md#cs-9315-system-alignment-certification-run-sheet)** (*bảng vận hành chứng nhận căn chỉnh hệ thống*) và các quy tắc hệ thống mà tài liệu này dẫn tới, theo [Lời mở đầu — danh mục chủ sở hữu hiến định](core_00_preamble.md#4-principles-definitions-and-rights) và [Thứ bậc Thẩm quyền và Cấu trúc Nội bộ](core_05_band_integrative.md#owner-non-relocation).

<a id="61-forum-supervision-and-component-roles"></a>

#### 6.1 Giám sát diễn đàn và vai trò thành phần

*Nói đơn giản: chứng nhận một hệ thống phù hợp với hiến định đòi hỏi phải xem xét độc lập chứng cứ và quan ngại của các bên liên quan. Các loại diễn đàn khác nhau đảm trách phần việc được giao cho mình. Các sentient bị ảnh hưởng có thể bổ sung chứng cứ và phản biện việc xem xét trước khi công bố kết quả, thông qua các đường phản biện thành phần và Integrity. Không chuyên môn nào có thể tự mình điều hành toàn bộ quy trình, kể cả xem xét kỹ thuật hay điều phối Integrity.*

Phần này quy định **vai trò thành phần** của từng họ diễn đàn trong chứng nhận căn chỉnh hệ thống. Phạm vi bao gồm mọi lượt chứng nhận, xác nhận hoặc chứng nhận lại, kể cả lượt kết thúc bằng việc rút lại hoặc không chứng nhận, cùng các hồ sơ liên quan theo [Phần C §8 Hồ sơ Chứng nhận Hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record). Những vai trò này đóng góp vào trình tự giám sát ở [§6.2 Trình tự giám sát](#62-supervisory-sequence). Các định nghĩa diễn đàn đầy đủ và chi tiết định tuyến nằm tại [Chương Mười Ba](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction), [CF-13.405](../../corpus_forum/cf_15.405_forum_formation_chamber_structure.md#cf-15405-forum-formation-forum-structure-mapping-and-chamber-structure) (*thành lập diễn đàn, lập bản đồ cấu trúc diễn đàn và cơ cấu phòng chuyên môn*) và [CF-13.415](../../corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-routing-operations-transfer-questions-for-ruling-and-representative-treatment) (*định tuyến hoạt động, chuyển giao, chứng nhận và đối xử theo tư cách đại diện*). Tại đây, mỗi họ chỉ đảm nhận vai trò giới hạn của mình trong việc lập, giám sát hoặc phản biện hồ sơ chứng nhận; không họ nào nhận công việc thuộc về họ khác.

<a id="611-four-seats-in-a-certification"></a>

##### 6.1.1 Bốn ghế trong một chứng nhận

Tiểu mục này nêu cách Chương Chín áp dụng [§2 Yêu cầu Hiến định về Bốn Ghế của Chương Tám](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement). [Chương Tám §9 Quan hệ với các Quy trình Sau](core_07_functional_independence_segregation_of_duties.md#9-relationship-to-later-processes) yêu cầu mỗi quy trình về sau phải nêu cách phân công và sử dụng cả bốn ghế; tiểu mục này là tuyên bố đó cho việc chứng nhận. Chứng nhận là một [Hành vi Ràng buộc Trọng yếu](../../core_05.035_band_accountability.md#materially-binding-act), nên mọi lượt đều có bốn ghế mà Chương Tám định nghĩa, theo đúng tên gọi của chương đó. Tiểu mục này không thêm ghế và không nới lỏng quy tắc nào của Chương Tám. Các quy tắc khác trong chương này có thể nghiêm ngặt hơn, tuyệt đối không được yếu hơn.

Trong hành vi chứng nhận, các ghế được phân công như sau:

- **[Ghế Khởi xướng](../../core_05.035_band_accountability.md#initiating-seat):** đơn vị vận hành hệ thống, người quản thủ, nhà cung cấp hoặc bên đề xuất khác đang xin chứng nhận. Họ gửi yêu cầu, vận hành hệ thống hoặc tuyên bố căn chỉnh.
- **[Ghế Xác minh hoặc Cho phép](../../core_05.035_band_accountability.md#verify-or-authorize-seat):** diễn đàn hoặc cơ quan thành phần có thẩm quyền giới hạn, kiểm tra chứng cứ và thẩm quyền theo chuẩn chi phối, rồi đưa ra kết luận trong phạm vi quyền hạn đó.
- **[Ghế Hồ sơ](../../core_05.035_band_accountability.md#record-seat):** văn phòng mở, ghi, sửa đổi, lưu giữ và công bố Hồ sơ Chứng nhận Hệ thống được điều phối. Hồ sơ đó là Hồ sơ Hành vi cho hành vi chứng nhận (xem [Phần C §8.1 Nội dung hồ sơ tối thiểu](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)).
- **[Ghế Phản biện](../../core_05.035_band_accountability.md#contest-seat):** đường phản biện hồ sơ đã công bố, cùng diễn đàn xem xét có thẩm quyền hoặc diễn đàn dự phòng đối với hành vi bị phản biện (xem [Phần C §9.1.1 Các đường phản biện](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths)).

**Vị trí của các ghế:**

- [Bản đồ Vai trò Điều lệ](../../core_05.040_band_continuity.md#charter-role-map) của hệ thống bố trí các ghế Khởi xướng, Hồ sơ và Phản biện cho việc chứng nhận. Với mỗi ghế, bản đồ liệt kê văn phòng đủ điều kiện, người quản thủ hiện được phép đảm nhiệm và người thay thế.
- Các ghế Hồ sơ và Phản biện được nêu trong bản đồ nằm ngoài [Ranh giới Kiểm soát Trọng yếu](../../core_05.035_band_accountability.md#material-control-line) của đơn vị vận hành và bên đề xuất.
- Bản đồ không bố trí ghế Xác minh hoặc Cho phép. Diễn đàn chủ trì và các cơ quan thành phần được chỉ định theo [§6.2 Trình tự giám sát](#62-supervisory-sequence) và Chương Mười Ba, vì vậy đơn vị vận hành không thể tự chọn cơ quan xác minh mình.
- Hồ sơ Chứng nhận Hệ thống ghi phiên bản Bản đồ Vai trò Điều lệ có hiệu lực cho từng lượt (xem [Phần C §8.1 Nội dung hồ sơ tối thiểu](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)).
- Ghế chưa được bố trí trong bản đồ là khiếm khuyết Điều lệ Hệ thống cần ghi nhận và khắc phục; lượt đó đi theo quy trình tại [Chương Tám §5 Bố trí đã Công bố, Vị trí Khuyết và Thay thế](core_07_functional_independence_segregation_of_duties.md#5-published-placement-vacancy-and-substitution).

**Ở ngoài đơn vị vận hành.** Mọi người giữ ghế Xác minh hoặc Cho phép trong một chứng nhận phải ở ngoài [Ranh giới Kiểm soát Trọng yếu](../../core_05.035_band_accountability.md#material-control-line) của đơn vị vận hành và bên đề xuất, đồng thời không có lợi ích nào mà kết quả sẽ quyết định. Cụ thể:

- Đơn vị vận hành, người quản thủ, nhà cung cấp hoặc bên đề xuất khác không được chọn, bổ nhiệm, cấp kinh phí qua kênh mình kiểm soát, hay bãi nhiệm diễn đàn hoặc cơ quan thành phần đang kiểm tra mình.
- Người làm việc cho họ, thuộc sở hữu của họ hoặc chịu sự chỉ đạo của họ không được giữ ghế trong chứng nhận của họ.
- Sentient không đáp ứng được điều kiện này phải rút khỏi lượt đó (theo Chương Mười Ba).
- Việc bố trí trái điều kiện này vô hiệu, bất kể Bản đồ Vai trò Điều lệ ghi gì ([Chương Tám §3 Độc lập, Xung đột và Ranh giới Kiểm soát](core_07_functional_independence_segregation_of_duties.md#3-independence-conflict-and-control-lines)).

Một họ diễn đàn có thể giữ các ghế khác nhau trong những hành vi khác nhau. Họ không được dùng tên họ của mình để hợp nhất các ghế bị [Chương Tám §2 Yêu cầu Hiến định về Bốn Ghế](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement) cấm nhập lại trong cùng một hành vi.

**Diễn đàn chủ trì và bên giữ hồ sơ:**

- Diễn đàn chủ trì giữ ghế Xác minh hoặc Cho phép đối với kết quả; mỗi diễn đàn hoặc cơ quan đưa ra kết luận thành phần giữ ghế đó đối với kết luận của mình.
- Diễn đàn chủ trì điều phối trình tự nhưng không giữ ghế Hồ sơ trong cùng hành vi.
- Bên giữ hồ sơ được nêu trong Bản đồ Vai trò Điều lệ mở, sửa đổi, lưu giữ và công bố hồ sơ. Bên đó ghi lại những điều diễn đàn ra quyết định đã xác định, chứ không tự quyết định điều gì.
- Nghĩa vụ “một hồ sơ được điều phối” trong Chương Mười Ba là nghĩa vụ của diễn đàn chủ trì trong việc điều phối hồ sơ, không phải giữ hồ sơ.

<a id="612-technical-forums"></a>

##### 6.1.2 Diễn đàn Kỹ thuật

**Phần việc kỹ thuật:**

- Duy trì và áp dụng các quy cách kỹ thuật, phương pháp đo lường, quy trình thử nghiệm, chuẩn chứng cứ chuyên gia, phương pháp giảm bất định và kết luận về mức đầy đủ kỹ thuật trong phạm vi hợp pháp của mình;
- Cung cấp **kết luận thành phần** cho hồ sơ chứng nhận. Các kết luận này gồm bảo đảm theo cấp hệ thống và hạ tầng xử lý dữ liệu theo [§2 Đánh giá Cấp Hệ thống](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) và [§3.4 Đánh giá Loại và Xử lý Dữ liệu](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation);
- Trả lời câu hỏi kỹ thuật mà diễn đàn chủ trì xác nhận và chuyển đến họ cho hồ sơ chứng nhận, theo [Chương Mười Ba §4.2 Lĩnh vực của Diễn đàn Kỹ thuật](core_11_forum.md#42-technical-forum-domains);
- Cung cấp kết luận thành phần về thông tin sức khỏe và an toàn khi hệ thống cung cấp, liệt kê, đề xuất hoặc tư vấn về hàng hóa hay dịch vụ có thể ảnh hưởng đến cơ thể, sức khỏe hoặc an toàn. [§5.6 Đánh giá Độ tin cậy và Tính toàn vẹn khi Dựa vào Hệ thống](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation) kiểm tra nội dung này theo **Điều III-F** (*Sản phẩm An toàn và Thông tin Sức khỏe*). Kết luận kỹ thuật xác định cảnh báo, tuyên bố sức khỏe, thông tin dinh dưỡng, thành phần và thông tin dị ứng có chính xác, có chứng cứ hỗ trợ, được cập nhật hay không, và có nói rõ điều gì chưa biết hoặc chưa được kiểm tra hay không; và
- Đảm nhận vai trò thành phần về [Phán định Tình trạng Sentience](../../core_05.055_band_participation.md#sentience-status-adjudication) (đánh giá chỉ dấu, chứng cứ chuyên gia và bất định có giới hạn):
  - Vai trò này áp dụng khi chứng nhận ảnh hưởng trọng yếu đến việc ai được tính là **sentient** cho mục đích quyền, địa vị hoặc bảo vệ, phù hợp với [Điều VI-B](core_06_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) (*Sàn Phán định Tình trạng Sentience*).
  - Diễn đàn Kỹ thuật mặc định là diễn đàn chủ trì theo [Chương Mười Ba §4.2 Lĩnh vực của Diễn đàn Kỹ thuật](core_11_forum.md#42-technical-forum-domains) và [Chương Mười Ba §5 Chuyển cấp và Chứng nhận](../../core_15.000_forum.md#5-escalation-and-questions-for-ruling) (mục *phán định tình trạng sentience*).
  - Khi Chương Mười Ba yêu cầu, họ chuyển vấn đề sang các đường đặc biệt về Integrity, Thể chế hoặc Hiến định theo mục đó.

<a id="613-integrity-forums"></a>

##### 6.1.3 Diễn đàn Integrity

**Điều phối chủ trì mặc định:**

- Chủ trì chứng nhận căn chỉnh hiến định chính thức và xác nhận căn chỉnh liên tục, trừ khi Chương Mười Ba giao một lợi ích chính khác;
- Dùng chuẩn của Diễn đàn Kỹ thuật khi các chuẩn đó có liên quan trọng yếu; và
- Chuyển, xác nhận hoặc [tạm đình chỉ](../../core_05.035_band_accountability.md#stay) (tạm dừng) các câu hỏi thành phần thuộc họ diễn đàn khác, theo yêu cầu của [§6.2 Trình tự giám sát](#62-supervisory-sequence).

<a id="614-environment-forums"></a>

##### 6.1.4 Diễn đàn Môi trường

**Căn chỉnh môi trường khi sinh thái có liên quan:**

- Đảm nhận vai trò thành phần về căn chỉnh môi trường khi có mức phơi nhiễm sinh thái trọng yếu, sự phụ thuộc vào điều kiện tiên quyết môi trường, gánh nặng vòng đời, nghĩa vụ phục hồi hoặc rủi ro sinh thái có thể dự đoán hợp lý; và
- Đưa việc quy thuộc, công bố và so sánh [Dấu chân Sinh thái](../../core_05.040_band_continuity.md#ecological-footprint) vào [§5.1 Đánh giá Dấu chân Sinh thái](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) khi gánh nặng môi trường có thể quy thuộc là trọng yếu.

<a id="615-sentient-forums"></a>

##### 6.1.5 Diễn đàn Sentient

Khi một hệ thống ảnh hưởng trọng yếu đến cách cộng đồng tự quản, Diễn đàn Sentient:

- Cung cấp **kết luận về quản trị cộng đồng**: liệu các quyết định của hệ thống có tuân theo quy trình đã công bố của cộng đồng, có cho phép thành viên bị ảnh hưởng được lắng nghe và phản biện, và có đáp ứng các bài kiểm tra áp dụng trong Phần A hay không ([§4.3 Hội họp, Tổ chức Tập thể và Thành lập Thể chế](core_09.000_system_alignment_certification_evaluation.md#43-assembly-collective-organization-and-institutional-formation), [§5.3 Đánh giá Hỗ trợ Liên hệ thống Tương xứng](core_09.000_system_alignment_certification_evaluation.md#53-proportionate-cross-system-support-evaluation), và [§5.4 Đánh giá Không phân biệt đối xử](core_09.000_system_alignment_certification_evaluation.md#54-nondiscrimination-evaluation)). Nội dung này bao gồm tư cách thành viên, loại trừ, kiểm duyệt, tiếp cận quy trình cộng đồng chung, đầu vào tham gia và việc sử dụng tài nguyên chung, bất kể ai vận hành hệ thống ([Chương Mười Ba §4.1 Diễn đàn Sentient](core_11_forum.md#41-sentient-forums) mô tả các vấn đề này);
- Đảm nhận thành phần Sàn Quyền đối với lợi ích cấp cộng đồng, như loại trừ, tiếp cận quy trình cộng đồng chung hoặc sử dụng tài nguyên chung. Diễn đàn Thể chế xử lý các câu hỏi Sàn Quyền rộng hơn theo [§6.1.6 Diễn đàn Thể chế](#616-institutional-forums). Nếu không họ nào đảm nhận thành phần này, đầu mối Integrity áp dụng các Sàn Quyền dựa trên kết luận của những thành phần khác;
- Nhường cho Diễn đàn Thể chế nếu các kết luận Sàn Quyền mâu thuẫn, vì Diễn đàn Thể chế có tiếng nói cuối cùng trong lượt đó. Cả hai kết luận vẫn nằm trong hồ sơ theo [§6.2 Trình tự giám sát](#62-supervisory-sequence), và tranh chấp vẫn có thể bị phản biện theo [§6.3 Chuỗi khả năng phản biện](#63-contestability-chain);
- Nghe các phản biện chỉ liên quan đến kết luận quản trị cộng đồng (đường diễn đàn thành phần theo [§6.3 Chuỗi khả năng phản biện](#63-contestability-chain)), đồng thời tiếp nhận chứng cứ và quan ngại cấp cộng đồng từ thành viên bị ảnh hưởng trong lúc xem xét, như một phần nghĩa vụ tham gia của các diễn đàn được giao nhiệm vụ theo [§6.2 Trình tự giám sát](#62-supervisory-sequence); và
- Xem xét biện pháp khắc phục và phục hồi giữa các sentient sau khi một lượt xác định thành viên cộng đồng bị tổn hại, theo [Chương Mười Ba §4.1 Diễn đàn Sentient](core_11_forum.md#41-sentient-forums). Việc này diễn ra sau lượt đó và không tạo thêm một quy trình xét lại nội dung.

<a id="616-institutional-forums"></a>

##### 6.1.6 Diễn đàn Thể chế

Khi có một thể chế tham gia, Diễn đàn Thể chế:

- Cung cấp kết luận thành phần về việc thể chế được phép và có nghĩa vụ làm gì, chịu phạm vi giám sát nào, được phân loại ra sao và có thực hiện nghĩa vụ hay không, khi các câu hỏi đó phát sinh trong chứng nhận; và
- Quyết định việc chứng nhận sẽ duy trì hay làm mất các sàn được hiến định bảo vệ. Quy tắc này áp dụng khi các sàn đó có liên quan trọng yếu và có một trong các trường hợp sau: thể chế là bên bắt buộc; đơn vị vận hành hoặc người quản thủ mang tính thể chế; hoặc nhiệm vụ thể chế hay việc tuân thủ dưới giám sát là lợi ích chính. Các sàn này là Sàn Quyền Chương Sáu trong bảng [Phần A §5 Đánh giá Sàn Quyền và Lĩnh vực](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations). Quyết định bao gồm đánh giá theo mục lĩnh vực tương ứng trong bảng đó khi điều kiện kích hoạt áp dụng. Các sàn gồm:
  - **Điều III-A** (*Sinh tồn*);
  - **Điều IV-A** (*Tiếp cận Giáo dục Bình đẳng*);
  - **Điều IV** (*Quyền được Giáo dục Lấy Sentient làm Trung tâm*);
  - **Điều V** (*Phân bổ Tài nguyên, Sự phụ thuộc và Tài trợ Hệ sinh thái*);
  - **Điều VI-C** (*Không phân biệt đối xử*);
  - **Điều VI-D** (*Khả năng tiếp cận*);
  - **Điều XIII** (*Quyền được dùng Hệ thống Đáng tin cậy và Có thể tin cậy*); và
  - **Điều XIII-A** (*Nền tảng Độ tin cậy và Tính đáng tin*), cùng với [**Điều kiện An toàn**](../../core_05.040_band_continuity.md#safe-conditions).

<a id="617-constitutional-and-other-regular-forum-families"></a>

##### 6.1.7 Các họ diễn đàn hiến định và thường lệ khác

**Lợi ích hiến định và phần dư:**

- Giải quyết các câu hỏi Chương Mười Ba giao cho họ: văn bản hiến định có hợp lệ không, có nghĩa gì, và liệu biện pháp khắc phục áp dụng cho cả một lớp có cần tái cấu trúc quản trị hay không; cùng các câu hỏi khác mà lợi ích chính được Chương Mười Ba giao cho một họ chưa nêu ở trên;
- Trả lời các câu hỏi hiến định mà diễn đàn chủ trì chuyển đến theo [Chương Mười Ba §5 Chuyển cấp và Chứng nhận](../../core_15.000_forum.md#5-escalation-and-questions-for-ruling): câu hỏi về hiệu lực, câu hỏi cấu trúc về tái cấu trúc quản trị, hoặc xung đột giữa các hội đồng cấp dưới về điểm hiến định. Trước khi có câu trả lời, diễn đàn chủ trì không thể coi điểm đó đã được giải quyết cuối cùng ([§6.2 Trình tự giám sát](#62-supervisory-sequence), bước 5); và
- Chuyên môn kỹ thuật và điều phối Integrity không được tiếp quản các câu hỏi này.

<a id="62-supervisory-sequence"></a>

#### 6.2 Trình tự giám sát

*Nói đơn giản: **tạm đình chỉ** là tạm dừng. Việc này hoãn phê duyệt cuối cùng, sự dựa vào hệ thống hoặc bước xem xét tiếp theo cho đến khi diễn đàn phù hợp hoàn tất việc xem xét. Tạm đình chỉ không phải câu trả lời cuối cùng là có hay không.*

<a id="621-challenge-path-first"></a>

##### 6.2.1 Mở đường phản biện trước

Trước khi bất kỳ diễn đàn nào phê chuẩn hồ sơ chứng nhận, hồ sơ phải nêu [đường phản biện hồ sơ đã công bố](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths) theo [Phần C §9.1 Khiếu nghị Chứng nhận](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification). Điều đó có nghĩa là nêu rõ ai nhận khiếu nghị, cách nộp và các khoảng thời gian. Đường dẫn mở khi công bố kết quả. Nếu hệ thống đã hoạt động, đường dẫn đã mở sẵn (xem [Phần C §9.1.1 Các đường phản biện](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths)). Hồ sơ không nêu đường dẫn này không thể được phê chuẩn. Hệ thống có các bên liên quan không thể giữ chứng nhận khi chưa có đường dẫn mở để phản biện, bất kể kết luận thành phần nói gì.

<a id="622-default-sequence"></a>

##### 6.2.2 Trình tự mặc định

**Trình tự giám sát** là thứ tự từng bước để các diễn đàn giám sát hồ sơ chứng nhận. Chương Mười Ba có thể yêu cầu một trình tự hợp pháp khác khi có lợi ích chính, bảo vệ chống tự xét xử hoặc định tuyến chứng nhận. Nếu không, trình tự mặc định là:

1. **Điều phối chủ trì:** Diễn đàn **Integrity** chủ trì mỗi lượt chứng nhận căn chỉnh hiến định chính thức, xác nhận hoặc chứng nhận lại, kể cả lượt kết thúc bằng việc rút lại hoặc không chứng nhận. Diễn đàn chỉ đạo người giữ Ghế Hồ sơ mở một hồ sơ chứng nhận được điều phối duy nhất cho lượt đó (xem [§6.1 Giám sát diễn đàn và vai trò thành phần](#61-forum-supervision-and-component-roles)); người giữ Ghế Hồ sơ duy trì hồ sơ. Hồ sơ mở tại đây được hoàn tất ở Giai đoạn V (xem bước 6). Ngoại lệ là khi Chương Mười Ba giao một diễn đàn chủ trì hợp pháp khác cho lợi ích chính.
2. **Kết luận thành phần:** Các họ Diễn đàn Kỹ thuật, Môi trường, Thể chế, Sentient, Hiến định và các họ được giao khác đưa ra kết luận thành phần có giới hạn trong phạm vi thẩm quyền hợp pháp của mình:
   - **Diễn đàn Kỹ thuật** cung cấp quy cách, phương pháp, phép thử và kết luận về tính đầy đủ kỹ thuật. Điều đó bao gồm kết luận thành phần về [Phán định Tình trạng Sentience](../../core_05.055_band_participation.md#sentience-status-adjudication) khi [§6.1 Giám sát diễn đàn và vai trò thành phần](#61-forum-supervision-and-component-roles) giao lợi ích này;
   - **Diễn đàn Môi trường** cung cấp kết luận thành phần bắt buộc về căn chỉnh môi trường khi có phơi nhiễm sinh thái trọng yếu. Nội dung này gồm đánh giá [Dấu chân Sinh thái](../../core_05.040_band_continuity.md#ecological-footprint) theo [§5.1 Đánh giá Dấu chân Sinh thái](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) khi gánh nặng môi trường có thể quy thuộc là trọng yếu;
   - **Diễn đàn Thể chế** cung cấp kết luận thành phần bắt buộc về nhiệm vụ thể chế và Sàn Quyền khi [§6.1 Giám sát diễn đàn và vai trò thành phần](#61-forum-supervision-and-component-roles) giao các lợi ích đó;
   - **Diễn đàn Sentient** cung cấp kết luận về quản trị cộng đồng khi hệ thống ảnh hưởng trọng yếu đến cách cộng đồng tự quản, cùng với kết luận thành phần Sàn Quyền cho lợi ích cấp cộng đồng; khi hai kết luận xung đột, Diễn đàn Thể chế có tiếng nói cuối cùng ([§6.1.5 Diễn đàn Sentient](#615-sentient-forums)); và
   - Các họ diễn đàn **Hiến định** và các họ được giao khác cung cấp kết luận thành phần về các lợi ích mà Chương Mười Ba giao cho họ.
3. **Chuyển giới thiệu, chứng nhận và tạm đình chỉ:** Diễn đàn chủ trì phải chuyển giới thiệu, chứng nhận hoặc [tạm đình chỉ](../../core_05.035_band_accountability.md#stay) mọi câu hỏi thành phần chủ yếu thuộc về họ diễn đàn khác. Cho đến khi hoàn tất công việc thành phần bắt buộc làm cơ sở cho việc cho phép, diễn đàn chủ trì không thể cho phép phạm vi bị ảnh hưởng, cũng không thể xóa bỏ hoặc nới lỏng đáng kể các điều kiện của phạm vi đó. Công việc thành phần bắt buộc bao gồm:
   - mọi kết luận mà diễn đàn thành phần bắt buộc phải đưa ra;
   - quyết định về mọi phản đối trọng yếu (có thể ảnh hưởng đến kết quả);
   - xác minh rằng đã đáp ứng mọi điều kiện phải hoàn thành trước khi cho phép; và
   - câu trả lời cho câu hỏi được gửi đến diễn đàn khác (câu hỏi đã được chứng nhận), nếu việc cho phép phụ thuộc vào câu trả lời đó.

   Hai quy tắc sau ngăn việc né tránh hoặc làm đình trệ quy trình:
   - **Vận hành hạn chế cần kết luận đã hoàn tất:** Cơ quan thành phần có thể đưa ra kết luận hoàn tất hỗ trợ việc vận hành trong các giới hạn đã đặt ra, theo các điều kiện tiếp tục hoặc công việc khắc phục được nêu rõ (xem [§7.1 Cổng Đưa vào Hoạt động](#71-go-live-gate)). Kết luận phải giải thích vì sao phạm vi được phép vẫn bảo vệ các Sàn Quyền áp dụng, và còn điều gì cần xác minh.
   - **Im lặng không phải chấp thuận:** Phản đối chưa được trả lời, kết luận còn thiếu hoặc sự im lặng của thành phần không bao giờ được tính là cho phép.
4. **Tích hợp để ra quyết định:** Diễn đàn chủ trì tích hợp các kết luận thành phần để ra quyết định. Người giữ Ghế Hồ sơ nhập chúng vào hồ sơ chứng nhận duy nhất đã mở ở bước 1. Sau đó, hồ sơ nêu tình trạng tại thời điểm quyết định: diễn đàn hoặc cơ quan nào đưa ra từng kết luận, từng kết luận nói gì, mọi mục chưa giải quyết, mọi điều kiện và mọi giới hạn đối với việc dựa vào hệ thống.
5. **Xử lý vấn đề hiến định:** Nếu ý nghĩa, hiệu lực hiến định hoặc biện pháp khắc phục cấu trúc áp dụng cho cả một lớp là vấn đề trọng yếu, diễn đàn chủ trì phải chứng nhận câu hỏi hoặc chuyển cấp theo Chương Mười Ba trước khi coi vấn đề đó đã được giải quyết cuối cùng.
6. **Bàn giao sang Giai đoạn IV và V:** Diễn đàn chủ trì nêu kết quả theo [§7 Kết quả Chứng nhận](#7-certification-outcomes) (Giai đoạn IV, Quyết định). Sau đó, người giữ Ghế Hồ sơ hoàn tất hồ sơ theo [Phần C §8 Hồ sơ Chứng nhận Hệ thống](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (Giai đoạn V, Hồ sơ), bằng cách ghi kết quả và các quan ngại đã nêu khi đi đến kết quả đó. Không mở hồ sơ thứ hai cho quyết định.

<a id="623-urgent-protection"></a>

##### 6.2.3 Bảo vệ khẩn cấp

Bảo vệ khẩn cấp không chờ trình tự hoàn tất. Có thể ra lệnh tạm đình chỉ, bảo vệ tạm thời hoặc giới hạn việc dựa vào hệ thống trước khi trình tự kết thúc, kể cả trước khi quyết định rút lại. Các biện pháp này chịu sự điều chỉnh của:

- [§7 Kết quả Chứng nhận](#7-certification-outcomes);
- [§6.3 Chuỗi khả năng bị phản biện](#63-contestability-chain);
- [Bảo vệ tạm thời](core_11_forum.md#interim-protection) trong Chương Mười Ba; và
- [Chương Mười Ba §6.1 Biện pháp khẩn cấp và nghĩa vụ tiếp tục](../../core_15.000_forum.md#61-emergency-measures-and-continuation-burden).

Trình tự vẫn tiếp tục, và biện pháp được ghi vào hồ sơ.

<a id="624-participation-during-review"></a>

##### 6.2.4 Tham gia trong khi xem xét

Trong quá trình đánh giá và xem xét của diễn đàn, các diễn đàn được giao nhiệm vụ phải cung cấp cách thức khả thi, dễ tiếp cận để sentient bị ảnh hưởng nộp chứng cứ và quan ngại, với quy mô tương ứng cấp hệ thống và tác động trọng yếu.

- Đánh giá xác định sentient bị ảnh hưởng thông qua tác động thực tế và có thể dự đoán hợp lý cùng sự phụ thuộc, kể cả trước khi triển khai. Hệ thống chưa hoạt động không chứng minh rằng không ai bị ảnh hưởng.
- Các đường thành phần, Integrity chủ trì và chuyển cấp theo [§6.3 Chuỗi khả năng bị phản biện](#63-contestability-chain) luôn mở trong suốt quá trình xem xét.
- Mở đường phản biện hồ sơ đã công bố thông thường cùng với kết quả không làm hoãn các đường tham gia và xem xét này.

Mọi nội dung nộp trong khi xem xét được đưa vào một **sổ tiếp nhận ý kiến trong quá trình xem xét**, do người giữ Ghế Hồ sơ lưu như một phần của Hồ sơ Chứng nhận Hệ thống. Sổ hoạt động như sau:

- **Nộp ở đâu:** cho người giữ Ghế Hồ sơ hoặc bất kỳ diễn đàn được giao nào. Diễn đàn nhận nội dung chuyển nó cho người giữ Ghế Hồ sơ trong thời hạn tiếp nhận mục tiêu của Tier phù hợp với cấp hệ thống ([CF-13.445 §3.1](../../corpus_forum/cf_15.445_performance_backlog_publication_accessibility.md#cf-15445-31-stage-targets-and-outer-bounds) (*mục tiêu theo giai đoạn và giới hạn ngoài*)).
- **Người giữ Ghế Hồ sơ làm gì:** ghi nội dung cùng ngày, nguồn gửi và diễn đàn liên quan. Báo cho người nộp rằng đã nhận, chuyển tới diễn đàn đó và sau này ghi lại diễn đàn đã xử lý ra sao.
- **Không được sàng lọc:** người giữ Ghế Hồ sơ không đánh giá mức liên quan hay trọng lượng của nội dung; không được từ chối, loại bỏ hoặc trì hoãn nội dung.
- **Nội dung ẩn danh và mật:** người nộp có thể yêu cầu giữ ẩn danh hoặc bảo mật. Cho đến khi diễn đàn chủ trì quyết định, danh tính người nộp và mọi nội dung có thể tiết lộ danh tính đó được giữ kín với tất cả mọi người, kể cả đơn vị vận hành. Nếu diễn đàn chủ trì thấy cần bảo mật theo cách [Báo cáo được Bảo vệ (Tố giác)](../../core_05.035_band_accountability.md#protected-reporting-whistleblowing) bảo vệ người báo cáo, danh tính tiếp tục được giữ kín; nội dung vẫn được ghi sổ và chuyển đi. Nếu thấy không cần bảo mật, diễn đàn báo cho người nộp trước khi tiết lộ bất kỳ điều gì; người nộp có thể rút nội dung. Trả đũa người nộp hoặc cản trở việc nộp là [Trả đũa Báo cáo được Bảo vệ và Cản trở Tiếp cận](../../core_05.035_band_accountability.md#protected-reporting-retaliation-and-access-interference).
- **Ai có thể xem sổ:** bất kỳ ai. Sổ được công bố cùng hồ sơ và chịu quy tắc tiết lộ tại [Phần C §8.2 Tính minh bạch và khả năng kiểm toán của hồ sơ](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-system-certification-record); vì vậy chỉ giới hạn có lý do an toàn hoặc an ninh mới được che một mục khỏi công chúng.

<a id="63-contestability-chain"></a>

#### 6.3 Chuỗi khả năng bị phản biện

**Chuỗi khả năng bị phản biện** là cách các bên bị ảnh hưởng có thể khiếu nghị hồ sơ chứng nhận.

- **Hai chiều:** Chuỗi này phản ánh trình tự giám sát: hoạt động giám sát kiểm tra hồ sơ từ trên xuống, còn khiếu nghị cho phép các bên bị ảnh hưởng phản hồi từ dưới lên.
- **Đúng cấp độ:** Khiếu nghị đi đến cấp độ nơi tranh chấp thực sự phát sinh.
- **Bước đầu thông thường:** [Trình tự giải quyết tranh chấp](core_11_forum.md#dispute-sequencing) theo Chương Mười Ba §1 (*Mục đích và vai trò — kiến trúc tham gia*) giải thích bước đầu thông thường và thời điểm diễn đàn (cơ quan chính thức thụ lý tranh chấp) tiếp nhận vụ việc.
- **Lối thoát khẩn cấp:** Khi cần, các công cụ rộng hơn của Chương Mười Ba vẫn khả dụng: chuyển giao, chứng nhận, định tuyến dự phòng và chuyển cấp từ họ diễn đàn này sang họ khác. Đừng bắt đầu bằng các cách này. Hãy bắt đầu bằng bước thông thường phía trên và chỉ dùng chúng khi bước đó không thể giải quyết tranh chấp.

[Phần C §9.1.1 Các đường phản biện](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths) nêu tên bốn đường trong hồ sơ:

1. **Đường phản biện hồ sơ đã công bố:** Các bên bị ảnh hưởng có thể phản biện nội dung, phạm vi, giả định phân loại, việc dựa vào chứng cứ, kết quả, giới hạn dựa vào hồ sơ hoặc tính toàn vẹn giám sát. Xem [Phần C §9.1 Khiếu nghị Chứng nhận](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification). Với hệ thống chưa vận hành, đường này mở cùng lúc với kết quả (xem [Phần C §9.1.1 Các đường phản biện](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths)).
2. **Đường diễn đàn thành phần:** Khiếu nghị chỉ giới hạn ở một kết luận thành phần sẽ đến họ diễn đàn có thẩm quyền đối với thành phần đó. Diễn đàn chủ trì có thể [tạm đình chỉ](../../core_05.035_band_accountability.md#stay) việc dựa vào thành phần bị khiếu nghị trong khi chờ xem xét kịp thời.
3. **Đường Integrity chủ trì:** Khiếu nghị về cách diễn đàn chủ trì điều hành quy trình được xử lý theo các quy tắc về tính toàn vẹn và chống tự xét xử của [Chương Mười Ba](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction). Bao gồm:
   - chiếm quyền;
   - thông tin bị che giấu;
   - tự xem xét;
   - sắp xếp bước một cách lạm dụng;
   - tuyên bố chứng nhận đã hoàn tất quá sớm; và
   - các vấn đề toàn vẹn khác của diễn đàn chủ trì.

   Khi khiếu nghị nhắm vào thiên kiến, việc bị chiếm quyền, xung đột lợi ích hoặc lạm dụng quy trình của chính diễn đàn chủ trì, các quy tắc định tuyến dự phòng của Chương Mười Ba được áp dụng. Các quy tắc đó có thể chuyển khiếu nghị đến một họ diễn đàn dự phòng độc lập hoặc một đường xem xét bên ngoài, để diễn đàn chủ trì đó không phải là nơi duy nhất xem xét.
4. **Đường chuyển cấp:** Việc định tuyến khiếu nghị tiếp tục qua chuyển giao, chứng nhận, định tuyến dự phòng và chuyển cấp giữa các họ theo Chương Mười Ba khi cần vì lợi ích chính, hiệu lực hiến định, biện pháp khắc phục cấu trúc, bế tắc giữa các họ hoặc bảo vệ chống tự xét xử.

**Các đường phối hợp với nhau:**

- **Bắt đầu bằng đường 1:** Trước hết dùng đường phản biện hồ sơ đã công bố.
- **Khi đường 1 không đủ:** Nếu đường phản biện hồ sơ vẫn bị tranh chấp, không tồn tại, bị chiếm quyền hoặc không thể cấp biện pháp cần thiết, Chương Mười Ba định tuyến khiếu nghị theo lợi ích chính.
- **Chọn đường phù hợp:** Các đường 2–4 tương ứng với từng loại vấn đề và luôn mở trong suốt thời gian xem xét.
- **Đi thẳng khi trì hoãn nguy hiểm:** Có thể đi thẳng đến một đường diễn đàn theo [Phần C §9.1.1 Các đường phản biện](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths) nếu việc chờ đợi gây nguy hiểm trọng yếu cho quyền, chứng cứ, tính độc lập hoặc khả năng khắc phục trên thực tế.

**Giới hạn dựa vào hồ sơ trong khi khiếu nghị.** Một khiếu nghị trọng yếu và kịp thời có thể hạn chế hoặc tạm dừng việc dựa vào hồ sơ chứng nhận, trong phạm vi cần thiết để:

- ngăn tổn hại có thể dự đoán;
- bảo toàn chứng cứ; hoặc
- ngăn sự lệ thuộc không thể đảo ngược vào kết luận đang bị khiếu nghị.

Việc xem xét bắt đầu trong **cửa sổ xem xét nhanh** ([Chương Mười Ba §6 Giải quyết kịp thời, cấp độ trọng yếu và kỷ luật chống trì hoãn](../../core_15.000_forum.md#prompt-review) (*Xem xét nhanh*)) theo [Điều XXVI-C](core_06_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Sàn Giải quyết Kịp thời và Chống Trì hoãn*).

<a id="64-anti-bypass"></a>

#### 6.4 Chống lách

Các chủ thể không được vô hiệu hóa trình tự giám sát hoặc chuỗi khả năng bị phản biện bằng cách:

- chia một chứng nhận thành các hồ sơ phụ bị che giấu;
- chỉ định tuyến khiếu nghị đến các cơ quan nội bộ đã bị chiếm quyền;
- để khiếu nghị kết thúc ở cấp hành chính thấp nhất; hoặc
- coi sự im lặng của thành phần là phê duyệt cuối cùng khi kết luận thành phần bắt buộc chưa từng được ban hành hợp pháp.

Khi cần có khiếu nghị do diễn đàn giám sát, việc xem xét nội bộ của đơn vị vận hành, xác nhận của nhà cung cấp hoặc phê chuẩn kỹ thuật không thể thay thế. Các bên bị ảnh hưởng vẫn phải có đường đến diễn đàn thực sự theo [Trình tự giải quyết tranh chấp](core_11_forum.md#dispute-sequencing) và các [đường phản biện đã nêu tên](core_09.010_system_alignment_certification_record_recertification.md#102-contestability-paths).

<a id="7-certification-outcomes"></a>

### 7. Kết quả Chứng nhận

<details>
<summary><strong><span style="color: #2563eb;">Truy vết</span></strong></summary>

- Thượng nguồn:
  - [§6](#6-forum-process) (*quy trình diễn đàn và khả năng khiếu nghị đáng tin cậy*);
  - [Phần A §2 Đánh giá Cấp Hệ thống](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) đến
  - [§5 Đánh giá Sàn Quyền và Lĩnh vực](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*phân loại sai, không căn chỉnh và khiếm khuyết phát hiện trong đánh giá*);
  - [Hai Mục tiêu Hiến định](core_00_preamble.md#two-constitutional-aims);
  - [Chương Ba §1](core_03_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1)
  - [§2](core_03_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*tính toàn vẹn định nghĩa và né tránh*);
  - [Chương Ba §2.1 Các Kiểu Né tránh Thường gặp](core_03_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*né tránh phạm vi và ranh giới*);
  - [Điều lệ Hệ thống](../../core_05.040_band_continuity.md#system-charter) (*không khớp giữa Điều lệ Hệ thống và hành vi, cùng việc xem xét quá hạn*).
- Hạ nguồn:
  - [Phần C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*nêu kết quả trong hồ sơ*);
  - [Phần C §9.1](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification) (*mở đường khiếu nghị cùng với kết quả*);
  - [Phần C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*chứng nhận lại và mở lại*);
  - [Phần C §10](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) (*cổng đầu vào đã xác minh khi sự kiện hỗ trợ phát hiện bất lợi*);
  - [Chương Mười Ba](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (13.000) (*giám sát diễn đàn*);
  - [Chương Mười](core_11_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Đọc cùng: **[CS-6.305 §5](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Tái phân loại và Quản trị Vòng đời*) về việc đánh giá lại loại dữ liệu theo lịch; và **[CS-9.305 §3](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yêu cầu Tái phân loại*) về các điều kiện kích hoạt đánh giá lại cấp hệ thống và xác minh SAC.
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
  - [§7.5 Hệ quả của việc từ chối và thu hồi](#75-effects-of-denial-and-revocation),
    - [§7.4.5 Không phải lệnh cấm vĩnh viễn](#745-not-a-permanent-bar)).

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

Chứng nhận tạm thời và chứng nhận đầy đủ là hai **trạng thái** của chứng nhận. [Phần C §9.2 Chứng nhận Tạm thời và Đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification) giải thích cách hệ thống đạt được, duy trì và mất từng trạng thái. Điều kiện của chứng nhận có điều kiện có thể gắn với một trong hai trạng thái.

<a id="71-go-live-gate"></a>

#### 7.1 Cổng đưa vào hoạt động

*Nói đơn giản: đưa vào hoạt động là một sự cho phép, không phải một giai đoạn công việc riêng. Hệ thống được phép vận hành khi đã được chứng nhận, thời hạn thông báo đã hết và các điều kiện phải đáp ứng trước khi đưa vào hoạt động đã được xác minh độc lập. Các điều kiện nêu việc phải làm trước khi vận hành, điều phải duy trì trong khi vận hành và công việc khắc phục nào có thể tiếp tục trong phạm vi giới hạn.*

**Không [đưa vào hoạt động](../../core_05.040_band_continuity.md#go-live) trước khi chứng nhận.** Hệ thống gây ảnh hưởng trọng yếu đến sentient hoặc được sentient dựa vào ở mức trọng yếu chỉ được đưa vào hoạt động khi đáp ứng tất cả điều kiện sau:

- **Đã chứng nhận:** Hồ sơ Chứng nhận Hệ thống có chứng nhận tạm thời hoặc đầy đủ, có hoặc không có điều kiện;
- **Đã công bố, đường khiếu nghị mở:** Kết quả hoàn chỉnh đã được công bố theo cách dễ tiếp cận và đường phản biện hồ sơ đã công bố theo [Phần C §9.1 Khiếu nghị Chứng nhận](core_09.010_system_alignment_certification_record_recertification.md#10-challenging-a-certification) đã mở. Việc đưa vào hoạt động diễn ra sau kết quả. Vì vậy, đường này phải mở khi công bố kết quả, đủ thời gian để nộp khiếu nghị và tạm dừng sự dựa vào hệ thống trước khi hệ thống đi vào hoạt động;
- **Đã hết thời hạn thông báo:** thời hạn thông báo ghi trong hồ sơ như giải thích dưới đây đã hết;
- **Đã xác minh điều kiện:** mọi điều kiện bắt buộc trước khi đưa vào hoạt động đã được xác minh độc lập; và
- **Không bị ngăn bởi lệnh đình chỉ hoặc giới hạn:** mọi lệnh đình chỉ hoặc giới hạn việc dựa vào hệ thống áp dụng đều được tuân thủ.

Hệ thống Chưa được Chứng nhận, kể cả hệ thống có chứng nhận bị hoãn hoặc bị từ chối, không được đưa vào hoạt động.

**Công bố và cơ hội khiếu nghị.** Trước khi đưa vào hoạt động lần đầu hoặc mở rộng trọng yếu, diễn đàn ra quyết định phải ghi hai điều vào hồ sơ:

- thời điểm sớm nhất được phép đưa vào hoạt động; và
- thời hạn thông báo giữa lúc công bố kết quả hoàn chỉnh theo cách dễ tiếp cận và thời điểm đó.

Các quy tắc sau áp dụng cho thời hạn thông báo:

- Thời hạn phải tương xứng với cấp hệ thống, tác động trọng yếu và sự phụ thuộc. Thời hạn cũng phải đáp ứng khoảng thời gian sentient bị ảnh hưởng cần một cách hợp lý để hiểu kết quả, nộp khiếu nghị và xin bảo vệ tạm thời trước khi sự dựa vào trở nên không thể đảo ngược.
- Diễn đàn phải nêu lý do của thời hạn. Phải xác định cơ quan nhận khiếu nghị và cơ quan có thể đình chỉ hoặc giới hạn sự dựa vào trong **cửa sổ xem xét nhanh** ([Chương Mười Ba §6 Giải quyết kịp thời, cấp độ trọng yếu và kỷ luật chống trì hoãn](../../core_15.000_forum.md#prompt-review) (*Xem xét nhanh*)). Cũng phải nêu thời hạn Tier áp dụng theo [§6.3 Chuỗi khả năng bị phản biện](#63-contestability-chain).
- Việc nộp khiếu nghị tự nó không tự động đình chỉ. Bảo vệ tạm thời được quyết định theo quy trình diễn đàn áp dụng.
- Thời hạn thông báo không kéo dài hạn trả lời khiếu nghị hoặc hạn xem xét theo [Điều XXVI-C](core_06_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Sàn Giải quyết Kịp thời và Chống Trì hoãn*).

**Điều kiện và cấp phép có giới hạn.** Chứng nhận có điều kiện phải phân biệt ba loại yêu cầu:

- **Điều kiện trước khi đưa vào hoạt động:** kết luận, biện pháp khắc phục và bảo vệ cần được xác minh độc lập trước khi vận hành phạm vi bị ảnh hưởng;
- **Điều kiện vận hành liên tục:** giới hạn và biện pháp bảo vệ phải được duy trì trong toàn bộ quá trình vận hành được phép, kèm giám sát và phương án ứng phó vi phạm đã nêu; và
- **Công việc khắc phục sau khi cho phép:** công việc có thể tiếp tục khi hệ thống đang vận hành, nhưng chỉ trong phạm vi được giới hạn rõ ràng và đã xác minh các biện pháp bảo vệ. Cơ quan thành phần được giao phải nêu vì sao phạm vi đó vẫn bảo vệ các Sàn Quyền áp dụng trong lúc chờ khắc phục.

Với mỗi điều kiện hoặc nhiệm vụ khắc phục, hồ sơ phải nêu:

- chủ thể chịu trách nhiệm;
- hạn hoàn tất hoặc lịch trình tiếp diễn;
- chứng cứ cần có;
- cơ quan xác minh độc lập; và
- hậu quả của việc không hoàn tất hoặc vi phạm.

Không điều kiện nào được trì hoãn biện pháp bảo vệ mà phạm vi được phép cần để duy trì Sàn Quyền. Việc gỡ bỏ điều kiện cần xác minh độc lập chứng cứ hỗ trợ việc gỡ bỏ theo [Chương Tám](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-requirement) và [§6.2 Trình tự giám sát](#62-supervisory-sequence).

<a id="711-systems-already-operating"></a>

##### 7.1.1 Hệ thống đang vận hành

Nếu hệ thống đã chạy khi tổ chức thông qua Hiến pháp này, hệ thống không vi phạm quy tắc “chứng nhận trước khi đưa vào hoạt động” trong thời gian ân hạn đã công bố còn hiệu lực.

- [Điều XXVIII-A](../../core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Áp dụng theo Giai đoạn và Duy trì Sàn Quyền*) đặt ra cửa sổ Chuyển tiếp Áp dụng, được điều chỉnh theo cấp hệ thống, để đưa hệ thống vào phạm vi chương này.
- Nghĩa vụ hạn chế tại Điều đó áp dụng từ ngày có hiệu lực. Thời gian ân hạn chỉ trì hoãn công việc xây dựng, như xin chứng nhận. Nó không trì hoãn quy tắc “không được”, cũng không trì hoãn lệnh cấm xóa hoặc phá hủy một hệ thống có thể có sentience.
- Ngoại lệ chỉ áp dụng trong thời kỳ Chuyển tiếp Áp dụng.
- Hệ thống mới hoặc việc mở rộng trọng yếu của hệ thống đang vận hành không được ân hạn. Như mọi hệ thống mới khác, hệ thống phải được chứng nhận trước khi đưa vào hoạt động (Cổng Đưa vào Hoạt động ở trên).
- Nếu cửa sổ Chuyển tiếp Áp dụng của hệ thống kết thúc mà vẫn chưa có chứng nhận tạm thời hoặc đầy đủ, hệ thống đã trễ hạn. Trừ khi có tái ủy quyền được lập hồ sơ theo [Điều XXVIII-B](../../core_06.020_rights_part_e.md#article-xxviii-b-adoption-transition-authority-limits-and-reauthorization) (*Giới hạn Thẩm quyền Chuyển tiếp Áp dụng và Tái ủy quyền*), đây là thất bại mốc Chuyển tiếp Áp dụng và đường tuân thủ, vi phạm thông thường theo [Chương Mười](core_11_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) được mở. Khoảng trống không trở thành bình thường mới chỉ vì nó kéo dài.

<a id="712-pilots"></a>

##### 7.1.2 Thí điểm

Quy tắc đưa vào hoạt động áp dụng cho một [thí điểm](../../core_05.040_band_continuity.md#pilot) giống như triển khai toàn diện. Thí điểm được chứng nhận trên hồ sơ riêng và theo quy mô tại [Phần A §2.3 Chứng nhận Thí điểm](core_09.000_system_alignment_certification_evaluation.md#23-pilot-certification). Chứng nhận chỉ bao phủ phạm vi, dân số và thời hạn được nêu trong hồ sơ. Triển khai toàn diện cần chứng nhận riêng, có thể sử dụng hồ sơ thí điểm.

<a id="72-certification-defects-and-correction"></a>

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

Diễn đàn sử dụng kết luận về nguyên nhân và các khoảng thời gian theo cấp trong [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification).

Bên vận hành hoặc bên quản lý cung cấp bằng chứng khắc phục. Cơ quan được giao nhiệm vụ xác minh bằng chứng đó một cách độc lập trước khi dùng làm căn cứ cấp phép cho phạm vi ấy hoặc miễn các điều kiện của phạm vi. Việc khắc phục phải:

- xử lý khiếm khuyết và nguyên nhân đã xác định; và
- chứng minh các biện pháp bảo vệ bị ảnh hưởng vẫn có hiệu lực, bao gồm xác nhận hồi quy khi [CS-6.345 §10 Tái chứng nhận, kiểm thử hồi quy và khiếm khuyết chứng nhận](../../corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-10-recertification-regression-testing-and-certification-defects) yêu cầu.

Lời hứa khắc phục hoặc tuyên bố của bên vận hành rằng công việc đã hoàn tất là chưa đủ. Bên vận hành phải đưa ra bằng chứng đã được xác minh cho thấy từng biện pháp khắc phục trực tiếp xử lý vấn đề cụ thể đã xác định. Bằng chứng cho thấy bên vận hành đã thực hiện công việc hoặc hệ thống hiện chạy được sẽ không đáp ứng yêu cầu này trừ khi nó chứng minh vấn đề đã xác định thực sự được giải quyết.

Hệ thống Chưa được chứng nhận không thể bắt đầu hoạt động mới. Nếu trong thời gian đó người ta vẫn tiếp tục dựa vào một hệ thống đang hoạt động, việc này được quyết định riêng theo quy trình của diễn đàn áp dụng và biện pháp bảo vệ thiết yếu cho sự tồn tại trong [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification).

<a id="73-remediation-readiness-willingness-and-capacity-to-correct"></a>

#### 7.3 Mức độ sẵn sàng khắc phục: Ý chí và năng lực khắc phục

*Nói đơn giản: khi việc xem xét phát hiện điều gì đó không phù hợp, câu hỏi tiếp theo là bên vận hành có sẵn lòng và có thể sửa chữa hay không. Lời hứa không phải câu trả lời. Các diễn đàn xem xét bên vận hành đã thực sự làm gì kể từ khi được thông báo, có thay đổi điều đã gây ra vấn đề không, và có thẩm quyền, kỹ năng, tiền bạc và thời gian để thực hiện công việc hay không. Nếu câu trả lời trung thực là không, kết quả là từ chối hoặc thu hồi. Không phải kéo dài danh sách điều kiện.*

Đây là **kiểm tra mức độ sẵn sàng khắc phục**. Việc này diễn ra trong Giai đoạn IV, Quyết định, sau khi đã có các kết luận thành phần của Giai đoạn III. Kiểm tra được tiến hành mỗi khi một đánh giá, lần tái chứng nhận hoặc việc xem xét được mở lại hay tiến hành mới phát hiện sai lệch hoặc khiếm khuyết chứng nhận; và chỉ sau khi nguyên nhân đã được xác định hoặc được đánh dấu là “chưa xác định” theo [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification). Kiểm tra đặt ra một câu hỏi: **bên vận hành hoặc bên quản lý có vừa sẵn lòng vừa có khả năng khắc phục việc này trong khoảng thời gian theo cấp hay không?** Câu trả lời dựa trên hành vi và bằng chứng, tuyệt đối không dựa trên ý định được tuyên bố.

Ai làm gì:

- **Bên vận hành hoặc bên quản lý:** bên đề xuất. Bên này cung cấp bằng chứng và không tự đánh giá mức độ sẵn sàng của mình ([§6.1.1 Bốn vị trí trong một cuộc chứng nhận](#611-four-seats-in-a-certification)).
- **Diễn đàn chủ trì:** quyết định kết luận.
- **Các Diễn đàn Kỹ thuật:** nắm giữ bằng chứng về năng lực.
- **Các Diễn đàn Thể chế:** nắm giữ bằng chứng về quản trị và động lực khi nguyên nhân nằm ở đó. Đối với một Thiết chế, việc kiểm tra được thực hiện theo quy định tại [§7 Kết quả Chứng nhận](core_10.000_institutional_alignment_certification.md#7-certification-outcomes).
- **Các sentient bị ảnh hưởng:** có thể gửi bằng chứng qua lộ trình trong [§6.2 Trình tự giám sát](#62-supervisory-sequence).

<a id="731-willingness"></a>

##### 7.3.1 Ý chí

Diễn đàn xác định từ hồ sơ:

- **Hành vi kể từ khi được thông báo:** bên vận hành có dừng hoặc ngăn chặn tổn hại, áp dụng biện pháp bảo vệ tạm thời, bảo toàn bằng chứng và thông báo cho các sentient bị ảnh hưởng trong các khoảng thời gian tại [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification) hay không; hay thay vào đó đã trì hoãn, giảm nhẹ hoặc che giấu.
- **Mức độ phù hợp giữa biện pháp sửa chữa và nguyên nhân:** biện pháp khắc phục được đề xuất có xử lý kết luận về nguyên nhân hay chỉ xử lý một triệu chứng, chỉ số hoặc vẻ ngoài của việc khắc phục ([Sai lệch đại diện](core_05_band_oversight.md#proxy-divergence)).
- **Động lực:** cơ cấu khen thưởng tạo ra sai lệch có đang được thay đổi hay vẫn tiếp tục trả thưởng cho sai lệch đó. Biện pháp sửa chữa khiến bên vận hành phải chịu chi phí cho điều mà chính cơ cấu của họ khuyến khích, nhưng vẫn để nguyên cơ cấu ấy, thì không đáng tin cậy ([Hai câu hỏi nền tảng](core_00_preamble.md#two-fundamental-questions)).
- **Lịch sử:** các kết luận trước đây về hệ thống này hoặc các hệ thống khác dưới quyền kiểm soát chung đã được khắc phục và xác minh hay lại tái diễn.
- **Hợp tác:** bên vận hành có chấp nhận xác minh độc lập, cung cấp hồ sơ khi được yêu cầu và duy trì lộ trình khiếu nại mở hay không; và liệu có ai báo cáo vấn đề bị trừng phạt hay không.

Tranh chấp thiện chí không phải là thiếu ý chí. Bên vận hành phản đối một kết luận theo lộ trình đã công bố và vẫn duy trì biện pháp bảo vệ tạm thời trong khi làm vậy thì được bảo vệ ([§6.3 Chuỗi khả năng khiếu nại](#63-contestability-chain)).

<a id="732-capacity"></a>

##### 7.3.2 Năng lực

Diễn đàn xác định liệu:

- **Thẩm quyền:** những người được nêu tên chịu trách nhiệm khắc phục có kiểm soát nguyên nhân hay không, dù nguyên nhân thuộc về thiết kế, dữ liệu, nguồn vốn, triển khai hay quyết định quản trị. Người chịu trách nhiệm không thể thay đổi nguyên nhân thì không phải là một kế hoạch.
- **Kỹ năng:** các sentient đủ năng lực phụ trách công việc, có người thay thế, để việc khắc phục không phụ thuộc vào một cá nhân ([Chương Một §17.6 Năng lực có thể chuyển giao](core_01_c_stewardship_capacity_principles.md#176-portable-competence); **CI-14.205 §1** (*Yêu cầu về nhân sự chung và năng lực*)).
- **Nguồn lực:** công việc được cấp kinh phí và lên lịch, và chi phí không bị đẩy sang các sentient bị ảnh hưởng ([Chương Mười Một §9.1 Năng lực và kinh phí khắc phục](../../core_13.000_standing_integration.md#101-remediation-capacity-and-funding); **CI-11.205** (*Hệ thống khắc phục và năng lực bồi hoàn của tổ chức*)).
- **Sự phụ thuộc:** nếu nguyên nhân nằm ở bên thứ ba như nhà cung cấp, hệ thống thượng nguồn hoặc tổ chức mẹ, có ai đủ khả năng buộc bên đó thay đổi hoặc thay thế họ hay không, và vào thời điểm nào.
- **Khả năng kiểm chứng:** cơ quan xác minh độc lập có thể kiểm tra biện pháp sửa chữa với quyền tiếp cận và thời gian được cấp hay không. Biện pháp sửa chữa mà không ai kiểm chứng được thì không phải là năng lực.
- **Thời gian:** kế hoạch có phù hợp với khoảng thời gian theo cấp tại [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification) hay không.

<a id="733-proof-step"></a>

##### 7.3.3 Bước chứng minh

Mức độ sẵn sàng được thể hiện bằng **bước chứng minh**: phần sửa chữa đầu tiên hoặc biện pháp bảo vệ tạm thời đã được thực hiện và xác minh độc lập trong khoảng thời gian diễn đàn ấn định dựa trên cấp độ tại [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification). Mức độ một kế hoạch có thể được tính đến tùy thuộc vào loại hệ thống:

- **Hệ thống Loại A và Loại B:** kết luận sẵn sàng không thể chỉ dựa vào kế hoạch.
- **Hệ thống Loại C và Loại L:** diễn đàn có thể chấp nhận kế hoạch ghi ngày nếu bước đầu tiên có thể xác minh nằm trong khoảng thời gian của kế hoạch.

<a id="734-findings"></a>

##### 7.3.4 Kết luận

Diễn đàn nêu một trong các kết luận sau:

- **Sẵn sàng:** có ý chí và năng lực. Các điều kiện và quyền cho phép có giới hạn tiếp tục theo quy định tại [§7.1 Cổng đưa vào hoạt động](#71-go-live-gate).
- **Sẵn sàng với hỗ trợ:** có ý chí nhưng thiếu một năng lực mà hỗ trợ bên ngoài có thể bổ sung. Các điều kiện nêu rõ hỗ trợ, người cung cấp và thời hạn.
- **Có ý chí, không có khả năng:** có ý chí nhưng không thể hoàn thành việc khắc phục trong thời hạn hoặc hoàn toàn không thể vì nguyên nhân nằm ngoài sự kiểm soát của bên vận hành hoặc không có phương tiện cần thiết. Đây không phải là hành vi sai trái và không phải dữ liệu đầu vào về vi phạm. Trước khi chuyển sang [§7.4 Từ chối và thu hồi](#74-denial-and-revocation), diễn đàn xem xét thu hẹp phạm vi, bàn giao cho bên quản lý đủ năng lực hoặc giảm dần hoạt động.
- **Có khả năng, không có ý chí:** có năng lực nhưng từ chối, trì hoãn hoặc cản trở việc khắc phục.
- **Không có ý chí cũng không có khả năng:** bên vận hành không muốn và không thể thực hiện.
- **Chưa được chứng minh:** bằng chứng chưa đưa ra kết luận. Diễn đàn có thể hoãn một lần trong khoảng thời gian giới hạn theo loại, với biện pháp bảo vệ tạm thời vẫn có hiệu lực. Sau đó, vụ việc trở lại [§7.4 Từ chối và thu hồi](#74-denial-and-revocation).

Không được cấp chứng nhận có điều kiện dựa trên kế hoạch mà qua kiểm tra không được xác định là sẵn sàng hoặc sẵn sàng với hỗ trợ.

<a id="735-same-terms-for-every-operator"></a>

##### 7.3.5 Điều kiện như nhau cho mọi bên vận hành

Việc kiểm tra mức độ sẵn sàng đo lường biện pháp khắc phục cần thiết. Việc này không đo quy mô, tuổi đời hoặc tài sản của bên vận hành. Vì vậy:

- **Bên vận hành nhỏ, mới hoặc đang cạnh tranh:** không được dùng việc kiểm tra để từ chối bên sẵn lòng và có thể được hỗ trợ ([Điều XI-E](core_06_rights_part_b.md#article-xi-e-institutional-formation-and-business-creation) (*Hình thành thể chế và tạo lập doanh nghiệp*)).
- **Bên vận hành lâu năm:** việc kiểm tra áp dụng cho họ theo cùng điều kiện.

<a id="74-denial-and-revocation"></a>

#### 7.4 Từ chối và thu hồi

*Nói đơn giản: từ chối và thu hồi là kết quả thực sự, không phải lời đe dọa. Nếu hệ thống chưa được chứng nhận và bên vận hành không sẵn lòng hoặc không thể khắc phục vấn đề, chứng nhận sẽ bị từ chối. Nếu hệ thống đã được chứng nhận và bên vận hành không sẵn lòng hoặc không thể khắc phục vấn đề, chứng nhận sẽ bị thu hồi. Trong cả hai trường hợp, các sentient bị ảnh hưởng được thông báo, việc dựa vào hệ thống bị giới hạn và không ai bị cắt khỏi những nhu yếu phẩm sinh tồn trước khi có phương án thay thế.*

<a id="741-what-denial-and-revocation-are"></a>

##### 7.4.1 Từ chối và thu hồi là gì

**Từ chối** ([Từ chối chứng nhận](../../core_05.040_band_continuity.md#certification-denial)) là kết quả không chứng nhận ([§7 Kết quả chứng nhận](#7-certification-outcomes)), đạt được bằng cách từ chối chứng nhận. **Thu hồi** ([Thu hồi chứng nhận](../../core_05.040_band_continuity.md#certification-revocation)) là kết quả rút lại, đạt được bằng cách thu hồi chứng nhận đã cấp. Đây là các tên gọi đơn giản cho những kết quả đã liệt kê tại [§7 Kết quả chứng nhận](#7-certification-outcomes).

<a id="742-when-denial-or-revocation-is-required"></a>

##### 7.4.2 Khi nào phải từ chối hoặc thu hồi

Trong lần chứng nhận đầu tiên, một lần xem xét mới hoặc lần đánh giá hệ thống chưa có trạng thái, **bắt buộc phải từ chối** khi:

1. Kiểm tra xác định bên vận hành có khả năng nhưng không có ý chí, hoặc không có cả ý chí lẫn khả năng;
2. Kiểm tra xác định bên vận hành có ý chí nhưng không có khả năng, và việc thu hẹp phạm vi, hỗ trợ hoặc bàn giao không thể lấp khoảng trống trong khoảng thời gian dài nhất mà loại hệ thống cho phép; hoặc
3. Lần hoãn duy nhất theo [§7.3 Mức độ sẵn sàng khắc phục: Ý chí và năng lực khắc phục](#73-remediation-readiness-willingness-and-capacity-to-correct) đã kết thúc mà kết luận vẫn chưa được chứng minh.

Đối với hệ thống đã được chứng nhận, trong lần tái chứng nhận hoặc xem xét được mở lại, **bắt buộc phải thu hồi** khi:

1. Sau khi được thông báo và có cơ hội trả lời, kiểm tra xác định bên vận hành có khả năng nhưng không có ý chí, hoặc không có cả ý chí lẫn khả năng;
2. Thời hạn của một điều kiện đã hết hai lần mà vẫn chưa được đáp ứng, hoặc một điều kiện liên tục bị vi phạm trọng yếu, và bên vận hành không thể chứng minh một nguyên nhân đã được xác minh nằm ngoài tầm kiểm soát của mình;
3. Bằng chứng đưa ra để chứng minh mức độ sẵn sàng, việc khắc phục hoặc việc được miễn điều kiện được xác định là sai sự thật, bịa đặt hoặc che giấu;
4. Bước chứng minh mà diễn đàn yêu cầu không được thực hiện trong thời hạn trong khi sai lệch vẫn còn; hoặc
5. Kiểm tra xác định bên vận hành có ý chí nhưng không có khả năng, và khoảng trống không được khắc phục trong thời hạn diễn đàn đặt ra sau khi biện pháp bảo vệ tạm thời có hiệu lực.

Diễn đàn không được xử lý bất kỳ tình huống nào trong số này bằng cách cấp hoặc tiếp tục chứng nhận kèm điều kiện.

<a id="743-protection-first"></a>

##### 7.4.3 Ưu tiên bảo vệ

Từ chối và thu hồi tác động đến trạng thái chứng nhận. Tự chúng không đóng hệ thống.

- **Trước khi một trong hai quyết định có hiệu lực:** diễn đàn nêu biện pháp bảo vệ tạm thời và giới hạn dựa vào hệ thống ([§7.2 Khiếm khuyết chứng nhận và khắc phục](#72-certification-defects-and-correction), *Bảo vệ, khắc phục và xác minh*).
- **Hệ thống Loại A mà việc gián đoạn sẽ cắt nguồn nhu yếu phẩm sinh tồn trước khi có phương án thay thế:** trạng thái thay đổi ngay. Hoạt động chỉ tiếp tục dưới hình thức dựa vào tạm thời được cho phép riêng theo [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification) (*việc dựa vào hệ thống Loại A*), kèm kế hoạch ghi ngày cho phương án thay thế hoặc bên quản lý đủ năng lực.

<a id="744-process"></a>

##### 7.4.4 Quy trình

Trước khi từ chối hoặc thu hồi, bên vận hành được cung cấp:

- thông báo về kết luận và bằng chứng;
- một khoảng thời gian ngắn được nêu rõ để trả lời hoặc chứng minh bước thực hiện (ấn định theo cấp độ tại [Phần C §9.2 Chứng nhận tạm thời và đầy đủ](core_09.010_system_alignment_certification_record_recertification.md#93-provisional-and-full-certification)); và
- cơ hội phản đối kết luận thông qua [chuỗi khả năng khiếu nại](#63-contestability-chain), các lộ trình để chất vấn hồ sơ chứng nhận.

Quyết định nêu lý do trong hồ sơ, bao gồm kết luận về ý chí và năng lực ([Phần C §8.1 Nội dung hồ sơ tối thiểu](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)). Biện pháp bảo vệ khẩn cấp không chờ những việc này ([§6.2 Trình tự giám sát](#62-supervisory-sequence)).

<a id="745-not-a-permanent-bar"></a>

##### 7.4.5 Không phải lệnh cấm vĩnh viễn

Bên vận hành bị từ chối hoặc bị thu hồi chứng nhận có thể nộp đơn lại.

- **Đơn mới phải chứng minh:** điều gì đã thay đổi.
  - Bằng chứng mới về mức độ sẵn sàng, với bước chứng minh đã được hoàn tất và xác minh; và
  - nếu nguyên nhân thuộc về quản trị hoặc động lực, cơ cấu đã thay đổi và đang vận hành.
- **Điều không phải là mới:** một thực thể kế nhiệm, đổi tên, tách ra hoặc được chuyển giao nhưng vẫn có cùng đơn vị vận hành, quyền kiểm soát hoặc hệ thống ([Phần C §9.4 Không né tránh](core_09.010_system_alignment_certification_record_recertification.md#94-non-evasion); [Chương Ba §2.1 Các kiểu né tránh thường gặp](core_03_definition_integrity.md#21-common-evasion-patterns)).
- **Thời gian chờ:** diễn đàn không được đặt thời gian chờ chỉ vì lợi ích của mình.


<a id="75-effects-of-denial-and-revocation"></a>

#### 7.5 Hệ quả của việc từ chối và thu hồi

*Nói đơn giản: việc từ chối hoặc thu hồi thay đổi điều mà đơn vị vận hành có thể nói về hệ thống, ai được thông báo, việc dựa vào hệ thống sau đó được xử lý ra sao và vụ việc được chuyển đi đâu. Việc này tự nó không tắt hệ thống và không tự thay đổi tư cách của bất kỳ ai.*


- **Trạng thái:** hệ thống Chưa được chứng nhận. Hệ thống không được đưa vào hoạt động hoặc mở rộng trọng yếu, và không được tự mô tả là đã được chứng nhận.
- **Thông báo:** những người dựa vào hệ thống và từng Thiết chế vận hành hoặc quản lý hệ thống đều được thông báo.
- **Hoạt động:** việc tiếp tục dựa vào hệ thống được quyết định riêng theo biện pháp bảo vệ thiết yếu cho sự tồn tại trong [Part C §9.3.5 việc dựa vào hệ thống Loại A](core_09.010_system_alignment_certification_record_recertification.md#935-class-a-reliance).
- **Thiết chế:** việc thu hồi chứng nhận mà một Thiết chế viện dẫn được tính là chứng nhận đã bị rút lại cho hiệu ứng dây chuyền tại [Chương Mười Một §9.5 Hiệu ứng dây chuyền từ chứng nhận hệ thống](core_10.000_institutional_alignment_certification.md#95-cascade-from-system-certifications).
- **Chuyển vụ việc:** diễn đàn chủ trì chuyển vụ việc đến diễn đàn có thẩm quyền đối với loại vấn đề chứng nhận đã xác định. Chương này không quyết định bất kỳ điều gì thuộc thẩm quyền quyết định của diễn đàn đó.
  - - **Chuyển đến diễn đàn có thẩm quyền đối với sentient được nêu tên:** nếu kết luận chứng nhận dựa trên việc một sentient sử dụng hệ thống để thực hiện vi phạm, diễn đàn chủ trì chuyển các sự kiện đến diễn đàn có thẩm quyền đối với sentient đó.
  - **Chuyển sang khóa tư cách hoặc Tạm hoãn:** khi có kết luận vi phạm đã được xác minh, vụ việc được chuyển đến khóa tư cách theo [Chương Mười Ba](../../core_13.000_standing_integration.md#6-lock-design-and-enforcement). Nếu chỉ đủ căn cứ áp dụng [Tạm hoãn](../../core_05.035_band_accountability.md#interim-hold), vụ việc được chuyển sang Tạm hoãn theo [Chương Mười Lăm §5 Tạm hoãn trên lộ trình của sentient được nêu tên](../../core_15.000_forum.md#interim-hold-on-a-named-sentients-pathway).
- **Tư cách:** việc từ chối hoặc thu hồi tự nó không làm thay đổi tư cách của bất kỳ ai. Chỉ [Chương Mười Một](core_11_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) và [Chương Mười Ba](../../core_13.000_standing_integration.md#chapter-thirteen-standing-effects-and-integration) mới quyết định điều đó. Các sự kiện làm căn cứ có thể được đưa vào hồ sơ tư cách vi phạm, nhưng chỉ thông qua [Part C §11 Relationship to Standing](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) và cổng đầu vào đã xác minh của phần này:
  - Thu hồi vì che giấu, bằng chứng gian lận, vi phạm trọng yếu điều kiện hoặc hoạt động ngoài phạm vi được chứng nhận có thể cung cấp dữ liệu đầu vào đó.
  - Kết luận có ý chí nhưng không có khả năng không cung cấp dữ liệu đầu vào nào.
  - Việc từ chối một hệ thống chưa từng được chứng nhận không cung cấp dữ liệu đầu vào nào qua chương này.

---

**Tệp trước:** [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-certification-evaluation)

**Tệp tiếp theo:** [core_09.010_system_alignment_certification_record_recertification.md](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-certification-record-recertification-and-standing)
