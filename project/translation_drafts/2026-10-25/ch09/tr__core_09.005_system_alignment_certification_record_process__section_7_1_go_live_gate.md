<!-- AI-assisted translation draft; unreviewed. Source lines 514–575; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 7.1 Canlıya Geçiş Kapısı

*Basitçe: canlıya geçiş ayrı bir çalışma aşaması değil, bir izindir. Sistem sertifikalandığında, bildirim süresi dolduğunda ve canlıya geçiş öncesi gerekli koşullar bağımsız biçimde doğrulandığında izin verilir. Koşullar; işletmeden önce ne yapılacağını, işletme sırasında neyin sürmesi gerektiğini ve sınırlı bir kapsam içinde hangi düzeltici çalışmaların sonradan yapılabileceğini belirtir.*

**Sertifikasyondan önce [canlıya geçiş](core_05.040_band_continuity.md#go-live) yoktur.** Sentientleri önemli ölçüde etkileyecek veya sentientlerin önemli ölçüde dayanacağı bir sistem, aşağıdakilerin tümü gerçekleşmeden canlıya geçemez:

- **Sertifikalandırılmış:** Sistem Sertifikasyon Kaydında koşullu veya koşulsuz geçici ya da tam sertifikasyon bulunur;
- **Yayımlanmış ve itiraz yolu açık:** Tamamlanmış sonuç erişilebilir biçimde yayımlanmış ve [C Kısmı §9.1 Sertifikasyona İtiraz](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) kapsamındaki yayımlanmış kayıt itiraz yolu açılmıştır. Canlıya geçiş sonuçtan sonra gelir. Dolayısıyla yol sonuç yayımlandığında açılmalı ve sistem canlıya geçmeden önce itiraz sunulup dayanmanın bekletilmesine imkân verecek süre tanımalıdır;
- **Bildirim süresi dolmuş:** Aşağıda açıklandığı üzere kayıtta belirlenen bildirim süresi tamamlanmıştır;
- **Koşullar doğrulanmış:** Canlıya geçiş öncesi gerekli her koşul bağımsız olarak doğrulanmıştır; ve
- **Bekletme veya sınırlama engeli yok:** Uygulanabilir bekletme veya dayanma sınırı yerine getirilmiştir.

Geçici ya da tam sertifikasyonu olmayan bir sistem canlıya geçemez; sertifikasyonu ertelenmiş veya reddedilmiş olanlar da buna dâhildir.

**Yayımlama ve itiraz fırsatı.** İlk canlıya geçişten veya önemli bir genişlemeden önce karar veren forum kayda iki husus koymalıdır:

- izin verilen en erken canlıya geçiş zamanı; ve
- tamamlanmış sonucun erişilebilir şekilde yayımlanması ile bu zaman arasındaki bildirim süresi.

Bildirim süresi için şu kurallar geçerlidir:

- Süre sistem sınıfı, önemli etki ve bağımlılıkla orantılı olmalıdır. Etkilenen sentientlerin sonucu anlamak, itiraz sunmak ve dayanma geri döndürülemez hâle gelmeden geçici koruma istemek için makul olarak ihtiyaç duyacağı zamanı da yansıtmalıdır.
- Forum sürenin gerekçelerini belirtmelidir. **Acil inceleme penceresi** içinde itirazları alacak makamı ve dayanmayı bekletme ya da sınırlama yetkisi olan makamı belirlemelidir ([On Üçüncü Bölüm §6 Zamanında çözüm, önemlilik kademeleri ve gecikme karşıtı disiplin](core_14.000_forum.md#prompt-review) (*Acil inceleme*)). [§6.3 İtiraz edilebilirlik zinciri](#63-contestability-chain) kapsamındaki Tier sürelerini de belirtmelidir.
- İtiraz sunulması kendiliğinden bekletme doğurmaz. Geçici koruma, uygulanabilir forum süreci uyarınca karara bağlanır.
- Bildirim süresi, [Madde XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Zamanında Çözüm ve Gecikme Karşıtı Taban*) kapsamındaki itiraza yanıt veya inceleme sürelerini uzatmaz.

**Koşullar ve sınırlı yetkilendirme.** Koşullu sertifikasyon üç gereklilik türünü birbirinden ayırmalıdır:

- **Canlıya geçiş öncesi koşullar:** Etkilenen kapsam işletilmeden önce bağımsız olarak doğrulanması gereken bulgular, düzeltici tedbirler ve korumalar;
- **Sürekli işletim koşulları:** İzin verilen işletim boyunca geçerli olması gereken sınırlar ve güvenceler; izleme ile ihlale verilecek yanıt da belirtilmelidir; ve
- **Yetkilendirme sonrası düzeltici çalışma:** Sistem işletilirken devam edebilecek çalışma, ancak korumaları doğrulanmış ve açıkça sınırlandırılmış kapsam içinde. Atanmış bileşen makamı, düzeltme beklenirken bu kapsamın uygulanabilir Hak Tabanlarını nasıl koruduğunu belirtmelidir.

Her koşul veya düzeltme işi için kayıt şunları belirtmelidir:

- sorumlu sahip;
- tamamlama son tarihi veya devam eden sıklık;
- gerekli kanıt;
- bağımsız doğrulama makamı; ve
- tamamlanmama ya da ihlalin sonucu.

Bir koşul, yetkilendirilmiş kapsamın Hak Tabanını korumak için ihtiyaç duyduğu bir korumayı erteleyemez. Bir koşulun kaldırılması için, kaldırmayı destekleyen kanıt [Sekizinci Bölüm](core_08.000_functional_independence_separation_of_duties.md#2-four-seat-constitutional-requirement) ve [§6.2 Gözetim sırası](#62-supervisory-sequence) uyarınca bağımsız doğrulamadan geçmelidir.

<a id="711-systems-already-operating"></a>

##### 7.1.1 Halihazırda işletilen sistemler

Bir kuruluş bu Anayasayı kabul ettiğinde sistem zaten çalışıyorsa, yayımlanmış geçiş süresi boyunca “canlıya geçmeden önce sertifikasyon” kuralını ihlal etmiş sayılmaz.

- [Madde XXVIII-A](core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Aşamalı Kabul ve Hak Tabanı Sürekliliği*), sistemi bu bölüm kapsamına almak için sistem sınıfına göre ölçeklendirilmiş Kabul Geçişi penceresini belirler.
- Bu Maddedeki kısıtlama görevleri yürürlük tarihinden itibaren uygulanır. Geçiş süresi yalnızca sertifika alma gibi inşa çalışmalarını erteler. “Yapmamalı” kurallarını ve sentient olabilecek bir sistemi silme veya yok etme yasağını ertelemez.
- İstisna yalnızca Kabul Geçişi süresi için geçerlidir.
- Yeni bir sistem veya işletimdeki sistemin önemli ölçüde genişletilmesi için geçiş süresi yoktur. Diğer yeni sistemlerde olduğu gibi canlıya geçmeden önce sertifikalandırılmalıdır (yukarıdaki Canlıya Geçiş Kapısı).
- Sistemin Kabul Geçişi penceresi biter ve hâlâ geçici ya da tam sertifikasyonu yoksa son tarihi kaçırmıştır. [Madde XXVIII-B](core_06.020_rights_part_e.md#article-xxviii-b-adoption-transition-authority-limits-and-reauthorization) (*Kabul Geçişi Yetki Sınırları ve Yeniden Yetkilendirme*) uyarınca belgelenmiş bir yeniden yetkilendirme yoksa bu, Kabul Geçişi kilometre taşı başarısızlığıdır ve [Onuncu Bölüm](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) kapsamındaki olağan uyum ve ihlal yolu açılır. Boşluk, sürmekle yeni normale dönüşmez.

<a id="712-pilots"></a>

##### 7.1.2 Pilotlar

Canlıya geçiş kuralı, tam dağıtım için olduğu gibi bir [pilota](core_05.040_band_continuity.md#pilot) da uygulanır. Pilot, [A Kısmı §2.3 Pilot sertifikasyonu](core_09.000_system_alignment_certification_evaluation.md#23-pilot-certification) uyarınca ölçeklendirilerek kendi kaydıyla sertifikalandırılır. Sertifikasyonu yalnızca kayıtta belirtilen kapsam, nüfus ve süreyi kapsar. Tam dağıtımın kendi sertifikasyonu gerekir; bu sertifikasyon pilot kaydından yararlanabilir.

<a id="72-certification-defects-and-correction"></a>
