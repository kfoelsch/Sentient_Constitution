<!-- AI-assisted translation draft; unreviewed. Source lines 319–387; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 6.2 Gözetim sırası

*Basitçe: **bekletme**, geçici duraklatmadır. Uygun forum incelemesini tamamlayana kadar nihai onayı, dayanmayı veya sonraki inceleme adımını bekletir. Bekletme nihai bir evet ya da hayır değildir.*

<a id="621-challenge-path-first"></a>

##### 6.2.1 Önce itiraz yolu

Herhangi bir forum sertifikasyon kaydını onaylamadan önce kayıt, [C Kısmı §9.1 Sertifikasyona İtiraz](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) uyarınca [yayımlanmış kayıt itiraz yolunu](core_09.010_system_alignment_certification_record_recertification.md#911-contestability-paths) belirtmelidir. Bu, itirazları kimin alacağını, nasıl sunulacağını ve süreleri açıklamayı gerektirir. Yol, sonuç yayımlandığında açılır. Sistem zaten işletiliyorsa yol zaten açıktır (bkz. [C Kısmı §9.1.1 İtiraz edilebilirlik yolları](core_09.010_system_alignment_certification_record_recertification.md#911-contestability-paths)). Bu yolu belirtmeyen bir kayıt onaylanamaz. Paydaşları olan bir sistemin açık ve itiraza elverişli yolu yoksa, bileşen bulguları ne derse desin sertifikasyonu sürdürülemez.

<a id="622-default-sequence"></a>

##### 6.2.2 Varsayılan sıra

**Gözetim sırası**, forumların sertifikasyon kaydını gözettiği adım adım düzendir. Birincil menfaatler, kendi kendini yargılamaya karşı koruma veya sertifikasyon yönlendirmesi söz konusu olduğunda On Üçüncü Bölüm hukuka uygun başka bir sıra gerektirebilir. Aksi hâlde varsayılan sıra şöyledir:

1. **Baş koordinasyon:** Her resmî anayasal uyum sertifikasyonu, doğrulaması veya yeniden sertifikasyonu turuna, geri çekme ya da sertifikasyon vermeme ile biten tur dâhil, **Integrity** forumu liderlik eder. Kayıt koltuğu sahibine o tur için tek koordineli sertifikasyon kaydını açmasını söyler (bkz. [§6.1 Forum gözetimi ve bileşen rolleri](#61-forum-supervision-and-component-roles)); kaydı sürdüren kayıt koltuğu sahibidir. Burada açılan kayıt Aşama V'te tamamlanır (6. adıma bkz.). On Üçüncü Bölümün birincil menfaat için başka bir hukuka uygun lider atadığı durumlar istisnadır.
2. **Bileşen bulguları:** Teknik, Çevre, Kurumsal, Sentient, Anayasal ve atanmış diğer forum aileleri, hukuka uygun yetki alanları içinde sınırlı bileşen bulguları üretir:
   - **Teknik Forumlar** şartnameler, yöntemler, testler ve teknik yeterlilik bulguları sağlar. [§6.1 Forum gözetimi ve bileşen rolleri](#61-forum-supervision-and-component-roles) bu menfaati atadığında [Sentience Durumu Kararı](core_05.055_band_participation.md#sentience-status-adjudication) bileşen bulguları da buna dâhildir;
   - Önemli ekolojik maruziyet varsa **Çevre Forumları** gerekli çevresel uyum bileşen bulgularını sağlar. Atfedilebilir çevresel yüklerin önemli olduğu yerde [§5.1 Ekolojik Ayak İzi Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) kapsamındaki [Ekolojik Ayak İzi](core_05.040_band_continuity.md#ecological-footprint) değerlendirmesi buna dâhildir;
   - [§6.1 Forum gözetimi ve bileşen rolleri](#61-forum-supervision-and-component-roles) bu menfaatleri atadığında **Kurumsal Forumlar** gerekli kurumsal yetki ve Hak Tabanı bileşen bulgularını sağlar;
   - Sistem, bir topluluğun kendi kendini yönetme biçimini önemli ölçüde etkiliyorsa **Sentient Forumları** topluluk yönetimi bulgularını ve topluluk düzeyindeki menfaatler için Hak Tabanı bileşen bulgusunu sağlar; ikisi çatıştığında son söz Kurumsal Forumlarındır ([§6.1.5 Sentient Forumları](#615-sentient-forums)); ve
   - **Anayasal** ve atanmış diğer forum aileleri, On Üçüncü Bölümün kendilerine verdiği menfaatlere ilişkin bileşen bulguları sağlar.
3. **Yönlendirme, sertifikasyon ve bekletme:** Baş forum, esas olarak başka bir forum ailesine ait her bileşen sorusunu yönlendirmeli, onaylamalı veya [bekletmelidir](core_05.035_band_accountability.md#stay). Yetkilendirmenin dayandığı zorunlu bileşen çalışması tamamlanana kadar baş forum etkilenen kapsamı yetkilendiremez; o kapsamdaki koşulları kaldıramaz veya önemli ölçüde gevşetemez. Zorunlu bileşen çalışması şunları içerir:
   - bileşen forumunun vermesi gereken her bulgu;
   - sonucu etkileyebilecek her önemli itiraz hakkında karar;
   - yetkilendirmeden önce yerine getirilmesi gereken koşulların karşılandığının doğrulanması; ve
   - yetkilendirme yanıtına bağlıysa başka bir foruma gönderilen sorunun (onaylı sorunun) yanıtı.

   Atlatmayı veya sürecin tıkanmasını önleyen iki kural vardır:
   - **Sınırlı işletme için tamamlanmış bulgu gerekir:** Bir bileşen makamı, belirtilen devam eden koşullar veya düzeltici çalışma altında tanımlı sınırlar içinde işletmeyi destekleyen tamamlanmış bir bulgu verebilir (bkz. [§7.1 Canlıya Geçiş Kapısı](#71-go-live-gate)). Bulgu, izin verilen kapsamın ilgili Hak Tabanlarını neden korumaya devam ettiğini ve nelerin doğrulanmayı beklediğini açıklamalıdır.
   - **Sessizlik onay değildir:** Yanıtsız bir itiraz, eksik bir bulgu veya bir bileşenin sessiz kalması hiçbir zaman yetkilendirme sayılmaz.
4. **Karar için bütünleştirme:** Baş forum, karar için bileşen bulgularını bütünleştirir. Kayıt koltuğu sahibi bunları 1. adımda açılan tek sertifikasyon kaydına girer. Kayıt, kararın verildiği andaki durumu esas alarak her bulguyu hangi forum veya makamın verdiğini, bulgunun ne söylediğini, çözümlenmemiş her konuyu, her koşulu ve dayanma üzerindeki her sınırı belirtir.
5. **Anayasal çözüm:** Anayasal anlam, geçerlilik veya sınıf çapındaki yapısal çözüm önemli bir mesele ise baş forum, konuyu nihai olarak çözülmüş saymadan önce On Üçüncü Bölüm uyarınca onaylamalı veya üst düzeye taşımalıdır.
6. **Aşama IV ve V'e devir:** Baş forum sonucu [§7 Sertifikasyon Sonuçları](#7-certification-outcomes) uyarınca belirtir (Aşama IV, Karar). Ardından kayıt koltuğu sahibi, sonucu ve sonuca ulaşırken dile getirilen kaygıları ekleyerek [C Kısmı §8 Sistem Sertifikasyon Kaydı](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) uyarınca kaydı tamamlar (Aşama V, Kayıt). Karar için ikinci bir kayıt açılmaz.

<a id="623-urgent-protection"></a>

##### 6.2.3 Acil koruma

Acil koruma bu sıranın tamamlanmasını beklemez. Sıra bitmeden, geri çekme kararı verilmeden önce dahi bekletme, geçici koruma veya dayanma sınırı getirilebilir. Bu tedbirleri şu bölümler düzenler:

- [§7 Sertifikasyon Sonuçları](#7-certification-outcomes);
- [§6.3 İtiraz edilebilirlik zinciri](#63-contestability-chain);
- On Üçüncü Bölüm [Geçici koruma](core_14.000_forum.md#interim-protection); ve
- On Üçüncü Bölüm [§6.1 Acil tedbirler ve devam yükü](core_14.000_forum.md#61-emergency-measures-and-continuation-burden).

Sıra işlemeye devam eder ve tedbir kayda girilir.

<a id="624-participation-during-review"></a>

##### 6.2.4 İnceleme sırasında katılım

Görevlendirilen forumlar, değerlendirme ve forum incelemesi sırasında etkilenen sentientlerin kanıt ve kaygı sunabilmesi için uygulanabilir ve erişilebilir yollar sağlamalı; bunları sistem sınıfına ve önemli etkiye göre ölçeklendirmelidir.

- Değerlendirme, dağıtımdan önce de dâhil olmak üzere fiilî ve makul ölçüde öngörülebilir etkiler ile bağımlılık üzerinden etkilenen sentientleri belirler. Henüz işletilmeyen bir sistem, hiç kimsenin etkilenmediğini göstermez.
- [§6.3 İtiraz edilebilirlik zinciri](#63-contestability-chain) kapsamındaki bileşen, baş-Integrity ve üst düzeye taşıma yolları inceleme boyunca kullanılabilir durumda kalır.
- Sonuçla birlikte olağan yayımlanmış kayıt itiraz yolunun açılması, bu katılım ve inceleme yollarını ertelemez.

İnceleme sırasında yapılan her başvuru, kayıt koltuğu sahibinin Sistem Sertifikasyon Kaydının parçası olarak tuttuğu tek bir **inceleme başvuruları günlüğüne** girer. Günlük şu şekilde işler:

- **Başvuru nereye gönderilir:** kayıt koltuğu sahibine veya görevlendirilmiş herhangi bir foruma. Başvuruyu alan forum, sistem sınıfına karşılık gelen Tier'ın alım hedef süresi içinde bunu kayıt koltuğu sahibine iletir ([CF-13.445 §3.1](corpus_forum/cf_14.445_performance_backlog_publication_accessibility.md#cf-14445-31-stage-targets-and-outer-bounds) (*Aşama hedefleri ve dış sınırlar*)).
- **Kayıt koltuğu sahibinin görevi:** başvuruyu tarihi, kaynağı ve ilgili olduğu forumla birlikte günlüğe kaydetmek. Başvurunun alındığını gönderene bildirmek, o foruma iletmek ve daha sonra forumun ne yaptığını kaydetmek.
- **Kapı tutuculuğu yasak:** kayıt koltuğu sahibi başvurunun ilgisini veya ağırlığını değerlendirmez; başvuruyu reddedemez, silip atamaz ya da geciktiremez.
- **Anonim ve gizli başvurular:** gönderen anonim veya gizli kalmayı isteyebilir. Baş forum karar verene kadar gönderenin kimliği ve bu kimliği açığa çıkarabilecek başvurudaki her şey, operatör dâhil herkesten saklanır. Baş forum, [Korunan Bildirim (İhbar)](core_05.035_band_accountability.md#protected-reporting-whistleblowing) bildireni koruduğu şekilde gizliliğin gerekli olduğuna karar verirse kimlik gizli kalır, başvuru yine kayda girip iletilir. Gizlilik gerekli değilse herhangi bir açıklama yapılmadan önce gönderene bildirilir ve gönderen başvurusunu geri çekebilir. Başvuru sahibine misilleme veya başvuruya müdahale, [Korunan Bildirime Karşı Misilleme ve Erişime Müdahale](core_05.035_band_accountability.md#protected-reporting-retaliation-and-access-interference) sayılır.
- **Günlüğü kim görebilir:** herkes. Günlük kayıtla birlikte yayımlanır ve [C Kısmı §8.2 Kaydın şeffaflığı ve denetlenebilirliği](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) açıklama kuralları uygulanır; böylece yalnızca güvenlik veya emniyet gerekçesiyle haklı gösterilen bir sınırlama bir girdiyi görünmez kılabilir.

<a id="63-contestability-chain"></a>
