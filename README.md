<div align="center">

# 🐋 WhaleList — EazyLife DNS Blocklists

**Koleksi *DNS blocklist* terkurasi, ringan, dan bebas duplikasi (*Zero Redundancy*) untuk perlindungan iklan, pelacak, dan ancaman siber di seluruh perangkat.**

[![Build EazyLife](https://github.com/lonion-1/WhaleList/actions/workflows/build-eazylife.yml/badge.svg)](https://github.com/lonion-1/WhaleList/actions/workflows/build-eazylife.yml)
![Update Schedule](https://img.shields.io/badge/Update-Harian%20(00%3A00%20UTC)-blue?style=flat)
![Syntax](https://img.shields.io/badge/Format-Adblock%20(%7C%7Cdomain%5E)-success?style=flat)

</div>

---

## ✨ Mengapa WhaleList?

* **Zero Redundancy:** Menggabungkan berbagai sumber tepercaya, menghapus domain kembar, dan otomatis memangkas subdomain apabila domain induknya sudah diblokir.
* **Modular & Ringan:** Dipisahkan antara kebutuhan harian, keamanan tingkat lanjut, perangkat *router*/Smart TV, hingga telemetri spesifik tiap merek perangkat (*brand*).
* **Minim *False Positive*:** Menggunakan kurasi ketat yang aman diterapkan di level DNS tanpa merusak fungsi situs maupun aplikasi sehari-hari.
* **Otomatis Setiap Hari:** Dibangun ulang setiap hari pukul `00:00 UTC` melalui GitHub Actions.

---

## 📦 Daftar Utama (*Core Lists*)

Gunakan daftar utama ini sebagai fondasi pemblokiran di DNS blocker pilihanmu:

| Daftar | Target Perangkat | Fokus Utama | Tautan Langganan (*Raw URL*) |
| :--- | :--- | :--- | :--- |
| **EazyLife Core** | HP, Tablet, Laptop | Iklan harian, *pop-up*, pelacak (*trackers*), & iklan lokal Indonesia. | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Core.txt` |
| **EazyLife Security** | Semua Perangkat | Anti-*phishing*, toko online palsu (*scam*), & penyebar *malware*. | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Security.txt` |
| **EazyLife Router & TV** | Router & Smart TV | Super ringan untuk RAM terbatas + blokir telemetri & iklan Smart TV. | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-RouterTV.txt` |

---

## 📱 Daftar Modular per Brand (`brands/`)

Ingin privasi lebih ketat tanpa membebani perangkat dengan aturan yang tidak relevan? Tambahkan daftar *native telemetry* berikut sesuai merek perangkat yang kamu gunakan:

| Brand | Ekosistem Perangkat | Tautan Langganan (*Raw URL*) |
| :--- | :--- | :--- |
| **Apple** | iPhone, iPad, Mac, Apple TV | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Apple.txt` |
| **Windows** | PC/Laptop Windows 10/11 & Office | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Windows.txt` |
| **Samsung** | HP/Tablet Galaxy & Tizen Smart TV | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Samsung.txt` |
| **Xiaomi** | Xiaomi, Redmi, POCO & Mi TV | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Xiaomi.txt` |
| **Oppo & Realme** | HP Oppo & Realme | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Oppo-Realme.txt` |
| **Vivo** | HP Vivo & iQOO | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Vivo.txt` |

---

## 💡 Rekomendasi Kombinasi Penggunaan

Agar performa perangkat tetap gesit dan seimbang, kamu bisa mengikuti pola kombinasi berikut:

* **📱 Pengguna HP Pribadi (misal: iPhone atau Samsung):**
  Aktifkan **`EazyLife-Core.txt`** + **`EazyLife-Security.txt`** + **`brands/Apple.txt`** *(atau `brands/Samsung.txt`)*.
* **💻 Pengguna Laptop/PC Windows:**
  Aktifkan **`EazyLife-Core.txt`** + **`EazyLife-Security.txt`** + **`brands/Windows.txt`**.
* **🌐 Router Wi-Fi Rumah & Smart TV:**
  Cukup aktifkan **`EazyLife-RouterTV.txt`** saja agar memori router tetap lega, Smart TV bebas iklan layar utama, dan seluruh anggota keluarga dapat berselancar dengan nyaman.

---

## 🔍 Rincian Sumber & Cakupan Blokir

Klik bagian di bawah untuk melihat detail fungsi dan sumber hulu (*upstream*) dari setiap file:

<details>
<summary><b>1. Rincian EazyLife-Core.txt (Iklan & Pelacak Harian)</b></summary>
<br>

* **HaGeZi Pro (`pro.txt`)**
  * **Memblokir:** Iklan web & dalam aplikasi (*in-app ads*), pelacak aktivitas, analitik perilaku, telemetri sistem, serta *malvertising* ringan.
  * **Sumber di Dalamnya:** *Meta-list* terkurasi yang merangkum puluhan daftar populer seperti *OISD, StevenBlack, AdGuard DNS Filter, EasyList, EasyPrivacy, Disconnect,* dan *Peter Lowe’s List*.
* **HaGeZi Pop-Up Ads (`popupads.txt`)**
  * **Memblokir:** Jaringan iklan *pop-up*, *pop-under*, dan halaman pengalihan (*redirect*) agresif pada situs streaming atau unduhan.
  * **Sumber di Dalamnya:** Kurasi mandiri tim HaGeZi yang dipadukan dengan jaringan iklan *pop-up* (*PopAds, PopCash, PropellerAds, ExoClick*) serta laporan komunitas.
* **ABPindo (`abpindo.txt`)**
  * **Memblokir:** Iklan lokal Indonesia, *banner* portal berita lokal, *pop-up* situs berbahasa Indonesia, dan skrip pelacak lokal.
  * **Sumber di Dalamnya:** Daftar independen yang dikelola komunitas pemblokir iklan Indonesia.

</details>

<details>
<summary><b>2. Rincian EazyLife-Security.txt (Keamanan, Scam & Malware)</b></summary>
<br>

* **HaGeZi Fake (`fake.txt`)**
  * **Memblokir:** Toko online palsu (*fake shops*), situs penipuan (*scam*), investasi bodong, *typosquatting* (domain plesetan merek resmi), dan *phishing* komersial.
  * **Sumber di Dalamnya:** Gabungan kurasi HaGeZi dengan database pengawas konsumen global (*Watchlist Internet, Fake Shop Detector, StopForumSpam*).
* **Phishing Army (`phishing_army_blocklist.txt`)**
  * **Memblokir:** Domain aktif yang bertujuan mencuri kredensial login (perbankan, email, media sosial, hingga dompet kripto).
  * **Sumber di Dalamnya:** Agregasi otomatis dari feed intelijen ancaman seperti *PhishTank, OpenPhish,* dan *CERT.pl*.
* **URLhaus by abuse.ch (`hostfile`)**
  * **Memblokir:** Domain yang terbukti aktif mendistribusikan *malware*, *ransomware*, *trojan*, dan muatan berbahaya lainnya.
  * **Sumber di Dalamnya:** Riset keamanan siber nirlaba *abuse.ch* berdasarkan laporan peneliti keamanan global dan sistem *honeypot*.

</details>

<details>
<summary><b>3. Rincian EazyLife-RouterTV.txt (Router & Smart TV)</b></summary>
<br>

* **HaGeZi Light (`light.txt`)**
  * **Memblokir:** Iklan dasar dan pelacak utama tanpa menyentuh domain abu-abu, sehingga nyaris nol risiko memutus fungsi aplikasi keluarga di rumah.
  * **Sumber di Dalamnya:** Versi ringkas (*subset*) dari HaGeZi Pro yang mengambil komponen paling aman dari *OISD Basic, AdGuard DNS, EasyList,* dan *Peter Lowe’s List*.
* **ABPindo (`abpindo.txt`)**
  * **Memblokir:** Iklan dan *redirect* situs lokal Indonesia untuk seluruh perangkat yang terhubung ke Wi-Fi rumah.
* **HaGeZi Native Trackers (`Samsung, LG webOS, Xiaomi, Roku, Amazon`)**
  * **Memblokir:** Telemetri tingkat sistem operasi (*OS-level*), pelacakan riwayat tontonan (*Automatic Content Recognition*), dan iklan di layar utama (*home screen ads*) pada ekosistem TV populer.

</details>

<details>
<summary><b>4. Rincian Daftar Modular per Brand (<code>brands/</code>)</b></summary>
<br>

* **Sumber:** Menggunakan kurasi *Native Trackers* dari **HaGeZi** (`native.apple`, `native.winoffice`, `native.samsung`, `native.xiaomi`, `native.oppo-realme`, `native.vivo`).
* **Memblokir:** *Endpoint* pengumpulan data diagnostik, pelacakan aktivitas sistem bawaan pabrikan, serta iklan tersembunyi di antarmuka sistem operasi tanpa memutus layanan inti (seperti pembaruan sistem/OTA, App Store, atau sinkronisasi cloud).

</details>

---

## ⚙️ Kompatibilitas & Kustomisasi

* **Kompatibel Penuh Dengan:** AdGuard Home, Pi-hole (v5 & v6), NextDNS, Control D, RethinkDNS, Blokada, dan aplikasi DNS blocker lain yang mendukung sintaks Adblock (`||domain^`).
* **Pengecualian Domain (`Allowlist.txt`):** Jika ada domain yang perlu dikecualikan dari pemblokiran, cukup tambahkan ke dalam file `Allowlist.txt` di repositori ini (satu domain per baris) dan sistem akan otomatis mengecualikannya pada *build* berikutnya.

---

## 📄 Lisensi

Proyek ini menggunakan pembagian lisensi sebagai berikut:
* **Daftar Blocklist (`EazyLife-*.txt`):** Dilisensikan di bawah **[GNU GPL v3.0](LICENSE)** atau mengikuti ketentuan lisensi dari sumber hulu.
* **Skrip Otomatisasi (`scripts/` & `.github/`):** Murni karya mandiri dan dilisensikan di bawah **[MIT License](scripts/LICENSE)**.

---

## 🙏 Kredit & Apresiasi

Seluruh daftar ini dapat berjalan berkat kontribusi luar biasa dari para pengelola proyek sumber terbuka berikut:

* [HaGeZi's DNS Blocklists](https://github.com/hagezi/dns-blocklists)
* [ABPindo (Indonesian Adblock Rules)](https://github.com/ABPindo/indonesianadblockrules)
* [Phishing Army](https://phishing.army/)
* [URLhaus by abuse.ch](https://urlhaus.abuse.ch/)
