<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (tr)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

Bu bölüm, sertifikasyonun neleri doğrulaması gerektiğini belirtir:

- **Değerlendirme gerekliliği:**
  - atanmış sistem sınıfının CS-9.305 (*Sistem sınıflandırma mekanizması*) ve CS-9.310 (*Sistem etki sınıflandırmaları*) uyarınca gözlemlenen ve makul ölçüde öngörülebilir **etkiyi**, **bağımlılığı** ve **riski** yansıtıp yansıtmadığı; bunlara şunlar dahildir:
    - toplam etkiler;
    - etkileşim etkileri;
    - hasmane etkiler;
    - eşik etkileri;
  - sınıflandırmanın sistemin gerçek davranışı ve etkilerine göre belirlendiği, aşağıdakilere göre belirlenmediği:
    - beyan edilen niyet;
    - nominal kapsam;
    - yalnızca [Sistem Şartı](core_05.040_band_continuity.md#system-charter) metni; veya
    - yalnızca öz tanım;
  - önemli bir değişiklik gerektirdiğinde sistem sınıfının **CS-9.305 §3.5 [yeniden sınıflandırma gerekliliği](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** uyarınca yeniden kontrol edilip edilmediği; ve
  - [Sistem Sınıflandırma Kaydının](core_05.040_band_continuity.md#system-classification-record) mevcut koşullarda geçerli olan **en yüksek sistem sınıfını** gösterip göstermediği.
- **Güvence ve regresyon testleri:**
  - sistem sınıfına göre ölçeklenen güvencenin, altyapı sağlamlığının ve regresyon kapsamının atanmış sistem sınıfıyla aşağıdakiler uyarınca eşleşip eşleşmediği:
    - CS-9.305 (*Sistem sınıflandırma mekanizması*) ve CS-9.310 (*Sistem etki sınıflandırmaları*); ve
    - CS-6.345 (*Sistem yaşam döngüsü*); önemli ölçüde uygulanabildiği yerlerde aşağıdaki ortak operasyonel terimlerle birlikte okunur:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Süreklilik: kademeli bozulma ve arıza modu bütünlüğü terimleri*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Süreklilik: geri döndürülebilirlik ve sınırlama terimleri*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Süreklilik: hasmane dayanıklılık ve kötüye kullanıma direnç terimleri*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Bütünleştirici: kısıtlı gizlilik ve korunan soruşturma terimleri*), sistemin sınıfı veya işlevi bunu önemli ölçüde uygulanabilir kıldığında; ve
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Bütünleştirici: müdahale ve geçersiz kılma bütünlüğü terimleri*), sistemin sınıfı veya işlevi bunu önemli ölçüde uygulanabilir kıldığında; ve
  - CS-6.345'in (*Sistem yaşam döngüsü*) gerektirdiği üzere her yeniden sertifikasyonda regresyon testinin yapılıp yapılmadığı ve sonuçlarının [§8.1 Asgari kayıt içeriği](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents) uyarınca kayda geçirilip geçirilmediği.
