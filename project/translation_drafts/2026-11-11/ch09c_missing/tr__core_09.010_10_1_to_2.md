<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §§10.1–10.2; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="101-when-the-path-opens"></a>

#### 10.1 Yol ne zaman açılır

*Basitçe: Birinden sertifikasyona dayanması istenmeden önce itiraz yolu açık olmalıdır. Henüz çalışmayan bir sistemde ilk sonuç yayımlandığında açılır. Zaten çalışan bir sistemde ise zaten açıktır.*

Yol ne zaman açılır ve ne kadar süre açık kalır:

- Henüz çalışmayan bir sistem için yayımlanmış kayıt itiraz yolu, sonuç ne olursa olsun, ilk sertifikasyon sonucu yayımlandığında açılır. Böylece [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate) uyarınca sistem devreye girmeden önce itiraz edilebilir ve dayanma askıya alınabilir.
- Zaten çalışan bir sistemin paydaşları vardır. Bu nedenle yolu zaten açıktır ya da sistem kaydı açıldığında açılır. Bu, [Article XXVIII-A](core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Aşamalı Benimseme ve Haklar Tabanının Sürekliliği*) geçiş penceresindeki sistemi ve sonraki sertifikasyonu kapsar.
- **Paydaşlar**, sistemden esaslı biçimde etkilenen veya sisteme esaslı biçimde dayanan sentientlerdir; bunları işletmeci değil değerlendirme belirler.
- Henüz çalışmayan sistemin yolu açılana kadar Sistem Sertifikasyon Kaydı sistemi adlandırır ([Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence)). [§10.2 Contestability paths](#102-contestability-paths) içindeki bileşen, lider-bütünlüğü ve yükseltme yolları inceleme boyunca kullanılabilir.
- Sistem paydaşlara sahip olduğu sürece yol açık kalır. Sertifikasyondan sonra paydaşlar ortaya çıkarsa [§9 Recertification and Reopening](#9-recertification-and-reopening) uyarınca inceleme yeniden açılır.
- Paydaşları olan bir sistem için Sistem Sertifikasyon Kaydına itiraz edecek açık yol yoksa, sistemin uyumlu olduğu iddiası dayanaksızdır.

<a id="102-contestability-paths"></a>

#### 10.2 İtiraz yolları

*Basitçe: Sistem Sertifikasyon Kaydı, itirazın nereye yapılacağını söylemelidir. Önce olağan ilk adım, sonra itiraz edilen bulguda yetkili forum, forum liderinin kendisi sorgulanıyorsa yedek yol ve yükseltme gelir. Beklemek zarar verecekse itiraz eden doğrudan foruma gidebilir.*

Etkilenen herkesin uyuşmazlığı nereye götüreceğini bilmesi için Sistem Sertifikasyon Kaydı aşağıdaki dört itiraz yolunu belirtmelidir. Bunlar Chapter Fifteen'daki [Dispute sequencing](core_15.000_forum.md#dispute-sequencing) kuralını Sistem Sertifikasyon Kayıtlarına uygular. Yeni bir forum değil, forumlara giden yollardır; yetkili forumu yine Chapter Fifteen belirler. Sıralama [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-contestability-chain) içindedir.

- **Yayımlanmış kayıt itiraz yolu** — kayıt hakkındaki olağan uyuşmazlık için normal ilk adım. Kayıt, contest seat'i ([§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-four-seats-in-a-certification)) belirtir:
  - itirazı kimin aldığı;
  - nasıl sunulacağı; ve
  - [Article XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Zamanında Çözüm ve Gecikme Karşıtı Taban*) sürelerinin teslim alındığında başladığı.

  İşletmecinin iç incelemesi, satıcı tasdiki veya teknik onay bu yol değildir.
- **Bileşen forumu yolu** — kayıttaki tek bir bulguya itiraz içindir; bulguda yetkili Chapter Fifteen forum ailesine gider.
- **Lider-bütünlüğü yolu** — lider forumun sürecini yürütmesine; örneğin ele geçirilme, gizli bilgi, kendi çalışmasını inceleme veya sertifikasyonu erken bitmiş sayma durumlarına itiraz içindir. Lider forumun kendi kendisini yargılamaması için yedek forumla Integrity routing üzerinden işler.
- **Yükseltme yolu** — uyuşmazlığın Chapter Fifteen uyarınca başka veya daha üst foruma taşınmasıdır. Devir, başka foruma karar için soru gönderme, yedek yönlendirme veya forum aileleri arasında yükseltme buna dahildir. Başlıca çıkarlar başka yerdeyse, anayasal geçerlilik sorgulanıyorsa, yapısal düzeltme gerekiyorsa, iki forum ailesi çıkmaza girdiyse veya forum kendisini yargılayacaksa uygulanır.

Gecikme hakları, kanıtları, bağımsızlığı veya pratik iyileştirmeyi esaslı biçimde tehlikeye atabilecekse forum yoluna doğrudan erişim sürer. Yayımlanmış kayıt itiraz yolunun tamamlanmamış kullanımı forum yollarını engellememeli veya [Article XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) sürelerini tüketmemelidir.
