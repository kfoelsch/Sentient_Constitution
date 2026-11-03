<!-- AI-assisted translation draft; unreviewed. Source lines 693–775; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 7.4 Ret ve İptal

*Basitçe: ret ve iptal gerçek sonuçlardır, tehdit değildir. Bir sistem henüz sertifikalandırılmamışsa ve operatörü sorunu gidermek istemiyor ya da gideremiyorsa sertifikasyon reddedilir. Bir sistem sertifikalıysa ve operatörü sorunu gidermek istemiyor ya da gideremiyorsa sertifikasyon geri alınır. Her iki durumda da etkilenen sentientlere bildirim yapılır, dayanma sınırlandırılır ve bir ikame bulunmadan kimse hayatta kalmak için gerekli olanlardan mahrum bırakılmaz.*

<a id="741-what-denial-and-revocation-are"></a>

##### 7.4.1 Ret ve iptal nedir

**Ret** ([Sertifikasyon Reddi](core_05.040_band_continuity.md#certification-denial)), sertifikalandırmama sonucudur ([§7 Sertifikasyon Sonuçları](#7-certification-outcomes)) ve sertifikasyonun reddedilmesiyle ulaşılır. **İptal** ([Sertifikasyon İptali](core_05.040_band_continuity.md#certification-revocation)), geri çekme sonucudur ve hâlihazırda verilmiş bir sertifikasyonun geri alınmasıyla ulaşılır. Bunlar [§7 Sertifikasyon Sonuçları](#7-certification-outcomes) bölümünde zaten listelenmiş sonuçların sade adlarıdır.

<a id="742-when-denial-or-revocation-is-required"></a>

##### 7.4.2 Ret veya iptal ne zaman zorunludur

İlk sertifikasyonda, yeni incelemede veya herhangi bir statüsü olmayan bir sistemin değerlendirilmesinde şu durumlarda **ret zorunludur**:

1. Kontrol, operatörün muktedir ama isteksiz ya da ne istekli ne muktedir olduğunu bulursa;
2. Kontrol operatörün istekli ama muktedir olmadığını bulur ve sınıfın izin verdiği en uzun süre içinde kapsam daraltma, destek veya devir açığı kapatmazsa; veya
3. [§7.3 Giderime Hazırlık: Düzeltme İsteği ve Kapasitesi](#73-remediation-readiness-willingness-and-capacity-to-correct) kapsamındaki tek erteleme sona erdiği hâlde bulgu hâlâ gösterilmemişse.

Sertifikasyonu olan bir sistem için, yeniden sertifikasyonda veya yeniden açılmış incelemede şu durumlarda **iptal zorunludur**:

1. Bildirim ve yanıt fırsatından sonra kontrol, operatörün muktedir ama isteksiz ya da ne istekli ne muktedir olduğunu bulursa;
2. Bir koşulun süresi karşılanmadan iki kez dolmuşsa veya devam eden bir koşul esaslı biçimde ihlal edilmişse ve operatör kendi kontrolü dışındaki doğrulanmış bir nedeni gösteremiyorsa;
3. Hazırlık, düzeltme veya bir koşuldan muafiyet için sunulan kanıtın yanlış, uydurma ya da gizlenmiş olduğu ortaya çıkarsa;
4. Uyumsuzluk sürerken forumun istediği kanıtlama adımı kendi süresi içinde yapılmamışsa; veya
5. Kontrol operatörün istekli ama muktedir olmadığını bulmuşsa ve geçici koruma yürürlüğe girdikten sonra forumun belirlediği süre içinde açık kapatılmamışsa.

Forum, bu durumlardan hiçbirini koşullu sertifikasyon vererek veya sertifikasyonu sürdürerek karşılayamaz.

<a id="743-protection-first"></a>

##### 7.4.3 Önce koruma

Ret ve iptal sertifikasyon statüsüne etki eder. Tek başlarına sistemi kapatmazlar.

- **Herhangi biri yürürlüğe girmeden önce:** forum geçici korumayı ve dayanma sınırlarını belirtir ([§7.2 Sertifikasyon Kusurları ve Düzeltme](#72-certification-defects-and-correction), *Koruma, düzeltme ve doğrulama*).
- **Kesintisi, ikameler bulunmadan hayatta kalmak için gerekli unsurları kesecek Sınıf A sistemi:** statü derhâl değişir. İşletim, yalnızca [Bölüm C §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) (*Sınıf A dayanması*) uyarınca ayrıca yetkilendirilmiş geçici dayanma kapsamında sürer; ikameler veya yetkin bir sorumlu için tarihli bir plan gerekir.

<a id="744-process"></a>

##### 7.4.4 Süreç

Ret veya iptalden önce operatöre şunlar verilir:

- bulgu ve kanıtlara ilişkin bildirim;
- yanıt vermek veya kanıtlama adımını göstermek için belirtilmiş kısa bir süre ([Bölüm C §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) içindeki kademeye göre belirlenir); ve
- sertifikasyon kaydına itiraz yolları olan [itiraz edilebilirlik zinciri](#63-contestability-chain) üzerinden bulguya itiraz etme fırsatı.

Karar, isteklilik ve kapasite bulguları da dâhil olmak üzere gerekçelerini kayda geçirir ([Bölüm C §8.1 Asgari kayıt içeriği](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)). Acil koruma bunların hiçbirini beklemez ([§6.2 Gözetim sırası](#62-supervisory-sequence)).

<a id="745-effect"></a>

##### 7.4.5 Etki

Ret veya iptal şu etkilere sahiptir:

- **Statü:** Sistem Sertifikasızdır. Canlıya geçemez veya esaslı biçimde genişleyemez ve kendisini sertifikalı olarak tanımlayamaz.
- **Bildirim:** Sisteme dayananlara ve sistemi işleten ya da sorumluluğunu üstlenen her Kuruma bildirim yapılır.
- **İşletim:** Dayanmanın sürüp süremeyeceğine, [Bölüm C §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) kapsamındaki hayatta kalma açısından zorunlu koruma uyarınca ayrıca karar verilir.
- **Kurum:** Bir Kurumun atıfta bulunduğu sertifikasyonun iptali, [Bölüm E §14.3 Sistem sertifikasyonlarından kaynaklanan zincirleme sonuçlar](core_09.020_institutional_alignment_certification.md#143-cascade-from-system-certifications) için geri çekilmiş sertifikasyondur.
- **Statü kaydı:** Ret veya iptal tek başına hiç kimsenin statü kaydını değiştirmez. Buna yalnızca [Onuncu Bölüm](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) ve [On Birinci Bölüm](core_12.000_standing_integration.md#chapter-twelve-standing-effects-and-integration) karar verir. Arkasındaki olgular ihlal statüsü kaydına girdi sağlayabilir, ancak yalnızca [Bölüm C §10 Statüyle İlişki](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) ve doğrulanmış girdi kapısı aracılığıyla:
  - Gizleme, hileli kanıt, esaslı bir koşul ihlali veya sertifikalı kapsam dışı işletim nedeniyle iptal bu girdiyi sağlayabilir.
  - İstekli ancak muktedir değil bulgusu hiçbir girdi sağlamaz.
  - Hiç sertifikasyon almamış bir sistemin reddi bu bölüm yoluyla girdi sağlamaz.

<a id="746-not-a-permanent-bar"></a>

##### 7.4.6 Kalıcı engel değildir

Reddedilmiş veya iptal edilmiş bir operatör yeniden başvurabilir.

- **Yeni başvurunun göstermesi gereken:** neyin değiştiği.
  - Kanıtlama adımı önceden tamamlanmış ve doğrulanmış yeni bir hazırlık gösterimi; ve
  - neden yönetişim veya teşvik yapısındaysa, değişen yapının uygulamada olması.
- **Yeni sayılmayan:** aynı operatörü, kontrolü veya sistemi sürdüren halef, yeniden adlandırılmış, bölünmüş ya da devredilmiş bir yapı ([Bölüm C §9.3 Kaçınmama](core_09.010_system_alignment_certification_record_recertification.md#93-non-evasion); [Üçüncü Bölüm §2.1 Yaygın Kaçınma Kalıpları](core_03.000_definition_integrity.md#21-common-evasion-patterns)).
- **Bekleme süreleri:** forum sırf kendi isteği için bekleme süresi koyamaz.

---

**Önceki dosya:** [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-certification-evaluation)

**Sonraki dosya:** [core_09.010_system_alignment_certification_record_recertification.md](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-certification-record-recertification-and-standing)
