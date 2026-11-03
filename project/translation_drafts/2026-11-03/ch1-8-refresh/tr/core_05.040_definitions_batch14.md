# Chapter Five definition batch 14 — Full Certification (tr)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Full Certification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### Tam Sertifikasyon

<details>
<summary><strong>İzleme</strong></summary>

- Kanonik sahip: Dokuzuncu Bölüm C §9.3 Geçici ve tam sertifikasyon. Sistem Uyum Sertifikasyonu grubunun yanında durur, ona katılmaz. Geçici sertifikasyon, yeniden sertifikasyon, Sistem/Sınıflandırma kayıtları ve vekil sapmasıyla okuyun.

</details>

*Basitçe: temiz geçici yeniden sertifikasyonlardan sonra, mevcut sorun veya yaklaşan sorun işareti yokken Sistemin kazandığı daha uzun aralıklı statüdür. Kalıcı değildir; başarısız değerlendirme ya da izleme uyarısı statüyü kaldırır.*

- **What it is**
  - **In scope / out of scope / dependencies:** Kapsam: geçici sertifikalı Sistem gerekli ardışık temiz geçici yeniden sertifikasyonları tamamlamış ve sonuncusunda mevcut uyumsuzluk/ yaklaşan gösterge bulmamış olmalı. Sınıfa göre aralık, süre sınırı ve yeniden açılabilirlik vardır. Kapsam dışı: geçici sertifikasyon; iki statüye de eklenebilen koşullu sertifikasyon; kalıcı izin, itibar puanı veya statü etkisi (yalnız On Birinci Bölüm karar verir). Geçici sertifikasyon ve yeniden sertifikasyona bağlıdır. Temiz asgari sayı, düşürme ve tier pencereleri Dokuzuncu Bölüm C §9.3’te. Bu madde yalnız Beşinci Bölüm anlamıdır.
<a id="full-certification-a"></a>
- **How to measure and assess**
  - Süreklilik ölçümüyle değerlendirin: sınıfa göre ardışık temiz geçici yeniden sertifikasyon sayısı tamamlandı mı; açık uyumsuzluk, giderilmemiş kusur, gecikmiş kontrol ya da başarısız regresyon yok mu; kayıttaki izleme tetikleri/eğilimleri eşiği aşmıyor veya yaklaşmıyor mu, bağımsız incelenebilir mi ve sorun görünmesin diye daraltılmadı mı.
<a id="full-certification-c"></a>
- **What must hold**
  - **Primary failure:** Başlıca başarısızlık: asgari sayıdan önce veya mevcut/yaklaşan sorun varken tam statü vermek; başarısız yeniden sertifikasyon ya da uyumsuzluk bulunan yeniden incelemeden sonra sürdürmek; hiçbir sorun gösteremeyecek kadar dar göstergeler; yeniden açma tetikleyicisini atlamak/geciktirmek için tam statüyü gerekçe yapmak.
