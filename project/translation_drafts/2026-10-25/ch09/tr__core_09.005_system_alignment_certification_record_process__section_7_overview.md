<!-- AI-assisted translation draft; unreviewed. Source lines 443–513; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

### 7. Sertifikasyon Sonuçları

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst akış:
  - [§6](#6-forum-process) (*forum süreci ve inandırıcı itiraz*);
  - [A Kısmı §2 Sistem Sınıfı Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) ile
  - [§5 Hak Tabanı ve Alan Değerlendirmeleri](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*değerlendirmede bulunan yanlış sınıflandırma, uyumsuzluk ve kusurlar*) arası;
  - [İki Anayasal Amaç](core_00.000_preamble.md#two-constitutional-aims);
  - [Üçüncü Bölüm §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1)
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*tanım bütünlüğü ve kaçınma*);
  - [Üçüncü Bölüm §2.1 Yaygın Kaçınma Biçimleri](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*kapsam ve sınırdan kaçınma*);
  - [Sistem Tüzüğü](core_05.040_band_continuity.md#system-charter) (*Sistem Tüzüğü-davranış uyuşmazlığı ve gecikmiş inceleme*).
- Alt akış:
  - [C Kısmı §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*sonuç kayıtta belirtilir*);
  - [C Kısmı §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*itiraz yolu sonuçla açılır*);
  - [C Kısmı §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*yeniden sertifikasyon ve yeniden açma*);
  - [C Kısmı §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*olumsuz bulguları destekleyen olgular bulunduğunda doğrulanmış girdi kapısı*);
  - [On Üçüncü Bölüm](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*forum gözetimi*);
  - [Onuncu Bölüm](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Birlikte okuyun: zamanlanmış veri türü yeniden değerlendirmesi için **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Yeniden Sınıflandırma ve Yaşam Döngüsü Yönetişimi*); sistem sınıfı yeniden değerlendirme tetikleyicileri ve SAC doğrulaması için **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yeniden sınıflandırma gerekliliği*).
- Alt bölümler:
  - [§7.1](#71-go-live-gate) (*canlıya geçiş kapısı*; with
    - [§7.1.1 Halihazırda işletilen sistemler](#711-systems-already-operating) and
    - [§7.1.2 Pilotları](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*sertifikasyon kusurları ve düzeltme*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*iyileştirmeye hazırlık: düzeltme isteği ve kapasitesi*; with
    - [§7.3.1 İstek](#731-willingness),
    - [§7.3.2 Kapasite](#732-capacity),
    - [§7.3.3 Kanıtlama adımı](#733-proof-step),
    - [§7.3.4 Bulgular](#734-findings), and
    - [§7.3.5 Her operatör için aynı koşullar](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*ret ve geri alma*; with
    - [§7.4.1 Ret ve geri alma nedir](#741-what-denial-and-revocation-are),
    - [§7.4.2 Ret veya geri alma ne zaman gerekir](#742-when-denial-or-revocation-is-required),
    - [§7.4.3 Önce koruma](#743-protection-first),
    - [§7.4.4 Süreç](#744-process),
    - [§7.4.5 Etki](#745-effect), and
    - [§7.4.6 Kalıcı bir yasak değildir](#746-not-a-permanent-bar)).

</details>

<br>

*Basitçe: her sertifikasyon incelemesi, kanıtlarla ve süreç içinde dile getirilen kaygılarla desteklenen açık bir sonuçla biter. Sistem sertifikalandırılana, yayımlanan sonuca karşı etkilenen sentientlere uygulanabilir bir itiraz fırsatı verilene ve canlıya geçiş öncesi gerekli korumalar denetlenene kadar hiçbir şey canlıya geçmez.*

Bu bölüm, [§6 Forum Sürecinden](#6-forum-process) (**Aşama III, İnceleme**) sonra gelen **Aşama IV, Karar Verme** aşamasıdır. Forumların vardığı sonucu ele alır. [§7.1 Canlıya Geçiş Kapısı](#71-go-live-gate) canlıya geçiş kapısını belirtir; bir kusur bulunduğunda ne olacağını [§7.2 Sertifikasyon Kusurları ve Düzeltme](#72-certification-defects-and-correction) açıklar.

Bir sertifikasyon kararı, karara ulaşılırken dile getirilen kaygılarla birlikte [C Kısmı §8.1 Asgari kayıt içeriği](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) uyarınca kayıtta belirtilmelidir. Sonuç şunlardan biridir:

- geçici sertifikasyon;
- tam sertifikasyon;
- koşullu sertifikasyon;
- ertelenmiş sertifikasyon;
- sertifikasyon verilmemesi;
- geri çekme;
- sürenin dolması; veya
- koşulların kaldırılması.

Ne geçici ne de tam sertifikasyona sahip bir sistem **Sertifikalandırılmamıştır**. Sertifikasyon şu hâllerde böyledir:

- ertelenmiş;
- reddedilmiş;
- geri çekilmiş; veya
- süresi dolmuş.

Geçici ve tam sertifikasyon, sertifikasyonun iki **statüsüdür**. Bir sistemin her birini nasıl kazandığı, koruduğu ve kaybettiği [C Kısmı §9.2 Geçici ve tam sertifikasyon](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) bölümünde açıklanır. Koşullu sertifikasyondaki koşullar bu statülerden herhangi birine bağlanabilir.

<a id="71-go-live-gate"></a>
