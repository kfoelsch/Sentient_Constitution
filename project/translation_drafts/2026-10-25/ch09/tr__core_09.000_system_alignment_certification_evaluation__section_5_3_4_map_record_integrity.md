<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (tr)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 Harita ve Kayıt Bütünlüğü

Bağımlılık haritalarına ve kaynak akışı kayıtlarına dayanmadan önce sertifikasyon, bunların **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*) koşullarını karşılayıp karşılamadığını denetlemelidir. Bunlar:

- **Eksiksiz:** önemli yukarı ve aşağı yönlü bağımlılıkları, kaynak akışlarını ve önemli olduğu durumlarda gizli ya da dengesiz ilişkileri kapsamalıdır.
- **Güncel:** değişim hızı ve sistemin kritiklik düzeyi—[§2 System Class Evaluation](#2-system-class-evaluation)- kapsamındaki sınıfı dahil—göz önüne alınarak yeterince sık güncellenmelidir. Sistemi son sertifikasyon sırasındaki gibi değil, şu anda çalıştığı biçimde göstermelidir.
- **Denetlenebilir:** **Article XVI-A** (*Auditability and Observable Evidence*) uyarınca denetime açık olmalıdır.

Bu testlerden herhangi birini geçemeyen harita veya kayıt, sistemin yeterli desteği geri verdiği sonucunu destekleyemez. Eksiklik kayda geçirilmeli ve aşağıdaki *Defects and misalignment* uyarınca ele alınmalıdır.
