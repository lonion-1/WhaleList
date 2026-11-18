# 🐋 WhaleList — EazyLife DNS Blocklists

Koleksi *DNS blocklist* terkurasi yang dibangun secara otomatis setiap hari dengan prinsip **Zero Redundancy** (tanpa duplikasi domain dan otomatis memangkas subdomain jika domain induknya sudah diblokir). Dirancang agar ringan, minim *false positive*, dan mudah disesuaikan untuk berbagai jenis perangkat.

---

## 📦 Daftar File & Kegunaan

| Nama File | Target Perangkat | Fokus Utama |
| :--- | :--- | :--- |
| **`EazyLife-Core.txt`** | HP, Tablet, Laptop | Pemblokiran iklan harian, *pop-up*, pelacak (*trackers*), dan iklan lokal Indonesia. |
| **`EazyLife-Security.txt`** | Semua Perangkat | Proteksi keamanan dari situs *phishing*, toko online palsu (*scam*), dan penyebar *malware*. |
| **`EazyLife-RouterTV.txt`** | Router & Smart TV | Super ringan untuk RAM terbatas + membungkam iklan & telemetri bawaan Smart TV. |

> 💡 **Tips Penggunaan:** Gunakan **`EazyLife-Core.txt` + `EazyLife-Security.txt`** secara bersamaan di perangkat pribadi (AdGuard Home, Pi-hole, NextDNS, atau Control D). Untuk jaringan Wi-Fi rumah satu pintu di router, cukup gunakan **`EazyLife-RouterTV.txt`** agar seluruh anggota keluarga tetap nyaman berselancar tanpa gangguan.

---

## 🔗 Tautan Langganan (Raw URL)

Salin dan tempel tautan berikut ke menu *Blocklists / Filters* pada DNS blocker pilihanmu *(ganti `<USERNAME>` dengan username GitHub-mu)*:

* **EazyLife Core:**
  ```text
  https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Core.txt
  ```
* **EazyLife Security:**
  ```text
  https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Security.txt
  ```
* **EazyLife Router & Smart TV:**
  ```text
  https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Security.txt
  ```

---

## 🧩 Rincian Sumber & Cakupan Blokir

### 1. `EazyLife-Core.txt` (Iklan & Pelacak Harian)
Dirancang untuk penggunaan sehari-hari dengan keseimbangan optimal antara kebersihan iklan dan kelancaran akses situs/aplikasi.

* **HaGeZi Pro**
  * **Memblokir:** Iklan web & dalam aplikasi (*in-app ads*), pelacak aktivitas, analitik perilaku, telemetri sistem, serta *malvertising* ringan.
  * **Cakupan Sumber:** *Meta-list* terkurasi yang merangkum puluhan daftar populer seperti *OISD, StevenBlack, AdGuard DNS Filter, EasyList, EasyPrivacy, Disconnect,* dan *Peter Lowe’s List*.
* **HaGeZi Pop-Up Ads**
  * **Memblokir:** Jaringan iklan *pop-up*, *pop-under*, dan halaman pengalihan (*redirect*) agresif pada situs streaming atau unduhan.
  * **Cakupan Sumber:** Kurasi mandiri tim HaGeZi yang dipadukan dengan jaringan iklan *pop-up* (*PopAds, PopCash, PropellerAds, ExoClick*) serta laporan komunitas.
* **ABPindo**
  * **Memblokir:** Iklan lokal Indonesia, *banner* portal berita lokal, *pop-up* situs berbahasa Indonesia, dan skrip pelacak lokal.
  * **Cakupan Sumber:** Daftar independen yang dikelola komunitas pemblokir iklan Indonesia.

---

### 2. `EazyLife-Security.txt` (Keamanan, Scam & Malware)
Dipisahkan dari daftar utama agar profil keamanan dapat dinonaktifkan sementara dengan mudah apabila suatu saat terjadi *false positive* pada domain baru.

* **HaGeZi Fake**
  * **Memblokir:** Toko online palsu (*fake shops*), situs penipuan (*scam*), investasi bodong, *typosquatting* (domain plesetan merek resmi), dan *phishing* komersial.
  * **Cakupan Sumber:** Gabungan kurasi HaGeZi dengan database pengawas konsumen global (*Watchlist Internet, Fake Shop Detector, StopForumSpam*).
* **Phishing Army**
  * **Memblokir:** Domain aktif yang bertujuan mencuri kredensial login (perbankan, email, media sosial, hingga dompet kripto).
  * **Cakupan Sumber:** Agregasi otomatis dari feed intelijen ancaman seperti *PhishTank, OpenPhish,* dan *CERT.pl*.
* **URLhaus (abuse.ch)**
  * **Memblokir:** Domain yang terbukti aktif mendistribusikan *malware*, *ransomware*, *trojan*, dan muatan berbahaya lainnya.
  * **Cakupan Sumber:** Riset keamanan siber nirlaba *abuse.ch* berdasarkan laporan peneliti keamanan global dan sistem *honeypot*.

---

### 3. `EazyLife-RouterTV.txt` (Ringan untuk Router & Smart TV)
Dioptimalkan untuk perangkat router berkapasitas memori terbatas sekaligus menghentikan pelacakan dan iklan bawaan pada Smart TV.

* **HaGeZi Light**
  * **Memblokir:** Iklan dasar dan pelacak utama tanpa menyentuh domain abu-abu, sehingga nyaris nol risiko memutus fungsi aplikasi keluarga di rumah.
  * **Cakupan Sumber:** Versi ringkas (*subset*) dari HaGeZi Pro yang mengambil komponen paling aman dari *OISD Basic, AdGuard DNS, EasyList,* dan *Peter Lowe’s List*.
* **ABPindo**
  * **Memblokir:** Iklan dan *redirect* situs lokal Indonesia untuk seluruh perangkat yang terhubung ke Wi-Fi rumah.
* **HaGeZi Native Trackers (Samsung, LG webOS, Xiaomi, Roku, Amazon)**
  * **Memblokir:** Telemetri tingkat sistem operasi (*OS-level*), pelacakan riwayat tontonan (*Automatic Content Recognition*), dan iklan di layar utama (*home screen ads*) pada ekosistem TV populer.
  * **Cakupan Sumber:** Pemetaan khusus oleh tim HaGeZi terhadap *endpoint* pelacakan bawaan masing-masing pabrikan.

---

## ⚙️ Fitur Otomatisasi

* **Pembaruan Harian:** Diperbarui otomatis setiap hari pukul `00:00 UTC` melalui GitHub Actions.
* **Kompresi & Optimasi Aturan:** Menghapus baris komentar, menyaring sintaks yang tidak kompatibel dengan DNS, menggabungkan domain kembar, dan mengeliminasi subdomain jika domain induknya sudah diblokir.
* **Dukungan `Allowlist.txt`:** Domain yang ditulis di dalam file `Allowlist.txt` (satu domain per baris) akan otomatis dikecualikan dari seluruh hasil *build*.
* **Format Standar Adblock (`||domain^`):** Kompatibel langsung dengan **AdGuard Home, Pi-hole (v5/v6), NextDNS, Control D, RethinkDNS**, dan **dnsmasq** (dengan konversi standar).

---

## 🙏 Kredit & Apresiasi

Seluruh daftar ini tidak akan terwujud tanpa kerja keras para pengelola sumber terbuka di balik layar:
* [HaGeZi's DNS Blocklists](https://github.com/hagezi/dns-blocklists)
* [ABPindo (Indonesian Adblock Rules)](https://github.com/ABPindo/indonesianadblockrules)
* [Phishing Army](https://phishing.army/)
* [URLhaus by abuse.ch](https://urlhaus.abuse.ch/)
