<!-- AI-assisted translation draft; unreviewed. Source lines 576–616; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 7.2 Sertifikasyon Kusurları ve Düzeltme

*Basitçe: kusurlar koşullara, ertelemeye, reddetmeye, geri çekmeye veya yeni bir incelemeye yol açabilir. Düzeltme, yetkilendirmeyi veya koşullardan muafiyeti desteklemeden önce bağımsız olarak doğrulanmalıdır. Operatörün düzeltmeye istekli ve muktedir olup olmadığı, forumun bu seçeneklerden hangisini seçmesi gerektiğini belirler ([§7.3 Giderime Hazırlık: Düzeltme İsteği ve Kapasitesi](#73-remediation-readiness-willingness-and-capacity-to-correct), [§7.4 Ret ve İptal](#74-denial-and-revocation)).*

Herhangi bir Bölüm A değerlendirmesinde bulunan sertifikasyon kusurları küçük evrak hataları değildir. Bunlar şunları içerir:

- [§2 Sistem Sınıfı Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) kapsamındaki yanlış sınıflandırma;
- [§3.2.2 Kusurlar ve Uyumsuzluk](core_09.000_system_alignment_certification_evaluation.md#322-defects-and-misalignment) kapsamındaki risk değerlendirme ve risk açıklama kusurları;
- [§3.4 Veri Türleri ve İşleme Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation) kapsamındaki veri işleme kusurları; ve
- [§5.1 Ekolojik Ayak İzi Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) ile [§5.6 Güvenilirlik ve Sisteme Dayanma Bütünlüğü Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation) arasında belirtilen alana özgü kusurlar.

Böyle bir kusur bulunduğunda forumlar:

- koşullara bağlı olarak sertifika verebilir;
- sertifikasyonu erteleyebilir;
- sertifikasyonu reddedebilir;
- sertifikasyonu geri çekebilir;
- sertifikasyon aralığını değiştirebilir; veya
- [Bölüm C §9 Yeniden Sertifikasyon ve Yeniden Açma](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) kapsamında incelemeyi yeniden açabilir ya da yeni bir inceleme yapılmasını emredebilir.

Forumun bunlardan hangisini seçeceği, operatörün veya sorumlunun kusuru düzeltmeye istekli ve muktedir olup olmadığına bağlıdır. [§7.3 Giderime Hazırlık: Düzeltme İsteği ve Kapasitesi](#73-remediation-readiness-willingness-and-capacity-to-correct) bu ölçütü, [§7.4 Ret ve İptal](#74-denial-and-revocation) ise ret veya geri çekmenin ne zaman zorunlu olduğunu belirtir.

**Koruma, düzeltme ve doğrulama.** Bir kusur bulunduğunda forum şunları belirtmelidir:

- etkilenen kapsam;
- geçici koruma ve dayanma sınırları; ve
- gerekli düzeltici çalışma.

Forum, [Bölüm C §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) bölümündeki neden bulgusunu ve kademe sürelerini kullanır.

Operatör veya sorumlu düzeltme kanıtını sunar. Görevlendirilen yetkili, bu kanıtı söz konusu kapsamın yetkilendirilmesini veya koşullarından çıkarılmasını desteklemek için kullanmadan önce bağımsız olarak doğrular. Düzeltme:

- kusuru ve belirlenen nedenini ele almalı; ve
- etkilenen güvenlik önlemlerinin geçerli olduğunu göstermeli; [CS-6.345 §10 Yeniden sertifikasyon, regresyon testi ve sertifikasyon kusurları](corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-10-recertification-regression-testing-and-certification-defects) gerektiriyorsa regresyon doğrulamasını da içermelidir.

Düzeltme sözü veya işin tamamlandığına ilişkin operatör beyanı yeterli değildir. Operatör, her düzeltmenin belirlenen özel sorunu doğrudan giderdiğini gösteren doğrulanmış kanıt sunmalıdır. Operatörün iş yaptığına veya sistemin artık çalıştığına dair kanıt, belirlenen sorunun gerçekten çözüldüğünü göstermedikçe yeterli sayılmaz.

Sertifikalandırılmamış bir sistem yeni işletime başlayamaz. Bu arada işletimdeki bir sisteme dayanılmaya devam edilirse, bu husus uygulanabilir forum süreci ve [Bölüm C §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) kapsamındaki hayatta kalma açısından zorunlu koruma uyarınca ayrıca karara bağlanır.

<a id="73-remediation-readiness-willingness-and-capacity-to-correct"></a>
