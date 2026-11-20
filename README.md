<div align="center">

# 🐋 WhaleList — EazyLife DNS Blocklists

**Koleksi *DNS blocklist* terkurasi, ringan, dan bebas duplikasi (*Zero Redundancy*) untuk perlindungan iklan, pelacak, dan ancaman siber di seluruh perangkat.**

[![Build EazyLife](https://img.shields.io/github/actions/workflow/status/lonion-1/WhaleList/eazylife-zero-redudancy.yml?branch=main&label=Build%20EazyLife&style=flat)](https://github.com/lonion-1/WhaleList/actions/workflows/eazylife-zero-redudancy.yml) ![Last Commit](https://img.shields.io/github/last-commit/lonion-1/WhaleList?label=Last%20Update&style=flat&color=success)
![Update Schedule](https://img.shields.io/badge/Update-Harian%20(04%3A23%20WIB)-blue?style=flat)
![Syntax](https://img.shields.io/badge/Format-Adblock%20(%7C%7Cdomain%5E)-success?style=flat)

</div>

---

## ✨ Mengapa WhaleList?

* **Zero Redundancy:** Menggabungkan berbagai sumber tepercaya, menghapus domain kembar, dan otomatis memangkas subdomain apabila domain induknya sudah diblokir.
* **Modular & Ringan:** Dipisahkan antara kebutuhan harian, keamanan tingkat lanjut, perangkat *router*/Smart TV, hingga telemetri spesifik tiap merek perangkat (*brand*).
* **Minim *False Positive*:** Menggunakan kurasi ketat yang aman diterapkan di level DNS tanpa merusak fungsi situs maupun aplikasi sehari-hari.
* **Otomatis Setiap Hari:** Dibangun ulang setiap hari pukul `04:23 WIB` melalui GitHub Actions.
* **Transparan:** Jumlah domain dan ukuran file di setiap tabel di bawah diperbarui otomatis pada tiap *build*, jadi kamu bisa memilih daftar yang sesuai dengan kapasitas perangkatmu.

---

## 📦 Daftar Utama (*Core Lists*)

Gunakan daftar utama ini sebagai fondasi pemblokiran di DNS blocker pilihanmu:

| Daftar | Target Perangkat | Fokus Utama | Domain | Ukuran | Last Update | Tautan Langganan (*Raw URL*) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EazyLife Core** | HP, Tablet, Laptop | Iklan harian, *pop-up*, pelacak (*trackers*), & iklan lokal Indonesia. | <!-- COUNT:EazyLife-Core.txt -->243.544<!-- /COUNT --> | <!-- SIZE:EazyLife-Core.txt -->5,4 MB<!-- /SIZE --> | ![Core Update](https://img.shields.io/github/last-commit/lonion-1/WhaleList?path=EazyLife-Core.txt&label=Updated&style=flat) | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Core.txt` |
| **EazyLife Security** | Semua Perangkat | Anti-*phishing*, toko online palsu (*scam*), & penyebar *malware*. | <!-- COUNT:EazyLife-Security.txt -->136.459<!-- /COUNT --> | <!-- SIZE:EazyLife-Security.txt -->3,0 MB<!-- /SIZE --> | ![Security Update](https://img.shields.io/github/last-commit/lonion-1/WhaleList?path=EazyLife-Security.txt&label=Updated&style=flat) | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Security.txt` |
| **EazyLife Router & TV** | Router & Smart TV | Super ringan untuk RAM terbatas + blokir telemetri & iklan Smart TV. | <!-- COUNT:EazyLife-RouterTV.txt -->93.254<!-- /COUNT --> | <!-- SIZE:EazyLife-RouterTV.txt -->2,2 MB<!-- /SIZE --> | ![RouterTV Update](https://img.shields.io/github/last-commit/lonion-1/WhaleList?path=EazyLife-RouterTV.txt&label=Updated&style=flat) | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-RouterTV.txt` |

---

## 🛡️ Daftar Spesial, Keluarga & Power User

Pilih daftar tambahan berikut sesuai kebutuhan spesifik jaringan atau aktivitasmu:

| Daftar | Target Penggunaan | Fokus Utama | Domain | Ukuran | Tautan Langganan (*Raw URL*) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EazyLife Family** | Router Wi-Fi Keluarga | Paket komplet 1-klik: iklan ringan, *scam/malware*, anti-judol, & blokir konten dewasa. | <!-- COUNT:EazyLife-Family.txt -->983.911<!-- /COUNT --> | <!-- SIZE:EazyLife-Family.txt -->19,9 MB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Family.txt` |
| **EazyLife Anti-Bypass** | Router / AdGuard Home / Pi-hole (Jangan di HP/Browser) | Memblokir server *Encrypted DNS* (DoH), VPN, & proxy publik agar aturan DNS tidak diakali. | <!-- COUNT:EazyLife-AntiBypass.txt -->16.615<!-- /COUNT --> | <!-- SIZE:EazyLife-AntiBypass.txt -->338 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-AntiBypass.txt` |
| **EazyLife Max** | *Power User* (Perangkat dengan RAM besar atau Cloud) | Perlindungan agresif (*Pro++* + *Threat Intelligence Feeds*) untuk sapu bersih telemetri & ancaman siber. | <!-- COUNT:EazyLife-Max.txt -->1.748.581<!-- /COUNT --> | <!-- SIZE:EazyLife-Max.txt -->35,9 MB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Max.txt` |
| **EazyLife Focus** | Kerja & Belajar | Memblokir media sosial populer untuk mengurangi distraksi (*digital detox*). | <!-- COUNT:EazyLife-Focus.txt -->586<!-- /COUNT --> | <!-- SIZE:EazyLife-Focus.txt -->15 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-Focus.txt` |
| **EazyLife Isekai Wall** | Semua Perangkat | Pemblokiran khusus situs perjudian (*anti-gambling*). | <!-- COUNT:EazyLife-IsekaiWall.txt -->676.204<!-- /COUNT --> | <!-- SIZE:EazyLife-IsekaiWall.txt -->13,3 MB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-IsekaiWall.txt` |
| **EazyLife NSFW** | Semua Perangkat | Pemblokiran khusus konten dewasa (opsional). | <!-- COUNT:EazyLife-NSFW.txt -->86.262<!-- /COUNT --> | <!-- SIZE:EazyLife-NSFW.txt -->1,6 MB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/EazyLife-NSFW.txt` |

---

## 📱 Daftar Modular per Brand (`brands/`)

Ingin privasi lebih ketat tanpa membebani perangkat dengan aturan yang tidak relevan? Tambahkan daftar *native telemetry* berikut sesuai merek perangkat yang kamu gunakan:

| Brand | Ekosistem Perangkat | Domain | Ukuran | Tautan Langganan (*Raw URL*) |
| :--- | :--- | :--- | :--- | :--- |
| **Apple** | iPhone, iPad, Mac, Apple TV | <!-- COUNT:brands/Apple.txt -->104<!-- /COUNT --> | <!-- SIZE:brands/Apple.txt -->3 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Apple.txt` |
| **Windows** | PC/Laptop Windows 10/11 & Office | <!-- COUNT:brands/Windows.txt -->398<!-- /COUNT --> | <!-- SIZE:brands/Windows.txt -->13 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Windows.txt` |
| **Samsung** | HP/Tablet Galaxy & Tizen Smart TV | <!-- COUNT:brands/Samsung.txt -->201<!-- /COUNT --> | <!-- SIZE:brands/Samsung.txt -->6 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Samsung.txt` |
| **Xiaomi** | Xiaomi, Redmi, POCO & Mi TV | <!-- COUNT:brands/Xiaomi.txt -->410<!-- /COUNT --> | <!-- SIZE:brands/Xiaomi.txt -->12 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Xiaomi.txt` |
| **Oppo & Realme** | HP Oppo & Realme | <!-- COUNT:brands/Oppo-Realme.txt -->530<!-- /COUNT --> | <!-- SIZE:brands/Oppo-Realme.txt -->17 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Oppo-Realme.txt` |
| **Vivo** | HP Vivo & iQOO | <!-- COUNT:brands/Vivo.txt -->303<!-- /COUNT --> | <!-- SIZE:brands/Vivo.txt -->10 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Vivo.txt` |
| **Huawei** | HP/Tablet Huawei & HarmonyOS | <!-- COUNT:brands/Huawei.txt -->148<!-- /COUNT --> | <!-- SIZE:brands/Huawei.txt -->6 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Huawei.txt` |
| **Amazon** | Fire TV, Kindle, & Echo | <!-- COUNT:brands/Amazon.txt -->382<!-- /COUNT --> | <!-- SIZE:brands/Amazon.txt -->12 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Amazon.txt` |
| **LG webOS** | LG Smart TV | <!-- COUNT:brands/LG-webOS.txt -->460<!-- /COUNT --> | <!-- SIZE:brands/LG-webOS.txt -->16 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/LG-webOS.txt` |
| **Roku** | Perangkat Streaming Roku | <!-- COUNT:brands/Roku.txt -->64<!-- /COUNT --> | <!-- SIZE:brands/Roku.txt -->2 KB<!-- /SIZE --> | `https://raw.githubusercontent.com/lonion-1/WhaleList/main/brands/Roku.txt` |

---

> **Pengguna `personalDNSfilter` (Android)?** Jika format Adblock (`||domain^`) tidak terbaca, kamu bisa langsung menyalin tautan versi *wildcard* (`*domain`) di **[Panduan & Daftar URL Wildcard](./domains/README.md)**.
> **Atau filter list tidak sesuai dengan keinginan Anda?** Coba periksa daftar kombinasi yang sudah tersedia **[di sini](./custom/README.md)**.

---

## 💡 Panduan Kombinasi Sesuai Perangkat

* **HP & Laptop Pribadi (Standar Lengkap):**
  `EazyLife-Core.txt` + `EazyLife-Security.txt` + `EazyLife-IsekaiWall.txt` + *(1 file dari folder `brands/` sesuai perangkat)*
* **Profil Keluarga / Perangkat Anak (Ramah Anak & Anti-Judol):**
  `EazyLife-Core.txt` + `EazyLife-Security.txt` + `EazyLife-IsekaiWall.txt` + `EazyLife-NSFW.txt` + *(file `brands/` terkait)*
* **Router Rumah & Smart TV (Ringan & Anti-Telemetri Layar):**
  `EazyLife-RouterTV.txt` + `EazyLife-IsekaiWall.txt` *(+ `EazyLife-NSFW.txt` jika ingin memfilter seluruh jaringan Wi-Fi rumah)*

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

* **Sumber:** Menggunakan kurasi *Native Trackers* dari **HaGeZi** (`native.apple`, `native.winoffice`, `native.samsung`, `native.xiaomi`, `native.oppo-realme`, `native.vivo`, `native.huawei`, `native.amazon`, `native.lgwebos`, `native.roku`).
* **Memblokir:** *Endpoint* pengumpulan data diagnostik, pelacakan aktivitas sistem bawaan pabrikan, serta iklan tersembunyi di antarmuka sistem operasi tanpa memutus layanan inti (seperti pembaruan sistem/OTA, App Store, atau sinkronisasi cloud).

</details>

<details>
<summary><b>5. Rincian EazyLife Isekai Wall & EazyLife NSFW (Anti-Judol & Filter Keluarga)</b></summary>
<br>

* **EazyLife Isekai Wall (`EazyLife-IsekaiWall.txt`):**
  * **EazyWhale Isekai Wall (Original):** Domain judi online lokal & regional hasil kurasi organik jangka panjang untuk menutup celah domain judol yang terus berganti alamat.
  * **HaGeZi Gambling:** Daftar pemblokir situs perjudian global yang diperbarui secara berkala.
* **EazyLife NSFW (`EazyLife-NSFW.txt`):**
  * **HaGeZi NSFW:** Daftar situs konten dewasa (18+) yang dipisahkan secara khusus agar pengguna bebas memilih apakah ingin mengaktifkannya atau tidak.

</details>

<details>
<summary><b>6. Rincian Paket Spesial, Keluarga & Power User</b></summary>
<br>

* **EazyLife Family (`EazyLife-Family.txt`):**
  * **Sumber:** Gabungan `HaGeZi Light`, `ABPindo`, `HaGeZi Fake`, `Phishing Army`, `URLhaus`, `HaGeZi Gambling`, dan `HaGeZi NSFW`.
  * **Memblokir:** Iklan dasar, situs penipuan/malware, judi online, hingga konten dewasa dalam satu tautan praktis untuk router Wi-Fi rumah.
* **EazyLife Anti-Bypass (`EazyLife-AntiBypass.txt`):**
  * **Sumber:** `HaGeZi Encrypted DNS/VPN/Proxy Bypass` (`doh-vpn-proxy-bypass.txt`).
  * **Memblokir:** Server *DNS-over-HTTPS* (DoH), *DNS-over-TLS* (DoT), serta layanan VPN dan proxy publik agar pengaturan DNS router tidak dapat dilewati oleh aplikasi atau browser.
* **EazyLife Max (`EazyLife-Max.txt`):**
  * **Sumber:** `HaGeZi Pro++` (`pro.plus.txt`), `HaGeZi Pop-Up Ads`, `ABPindo`, dan `HaGeZi Threat Intelligence Feeds` (`tif.txt`).
  * **Memblokir:** Perlindungan agresif terhadap iklan, telemetri mendalam, dan infrastruktur ancaman siber aktif (C2 server, botnet, *cryptojacking*).
* **EazyLife Focus (`EazyLife-Focus.txt`):**
  * **Sumber:** `StevenBlack Social` (`alternates/social-only`).
  * **Memblokir:** Domain jejaring sosial populer untuk membantu menjaga fokus saat bekerja atau belajar (*digital detox*).

</details>

---

## ⚙️ Kompatibilitas & Kustomisasi

* **Kompatibel Penuh Dengan:** AdGuard Home, Pi-hole (v5 & v6), NextDNS, Control D, RethinkDNS, Blokada, dan aplikasi DNS blocker lain yang mendukung sintaks Adblock (`||domain^`).
* **Pengecualian Domain (`Allowlist.txt`):** Jika ada domain yang perlu dikecualikan dari pemblokiran, cukup tambahkan ke dalam file `Allowlist.txt` di repositori ini (satu domain per baris) dan sistem akan otomatis mengecualikannya pada *build* berikutnya.

---

## 📄 Lisensi

Proyek ini menggunakan pembagian lisensi sebagai berikut:
* **Daftar Blocklist (`EazyLife-*.txt`):** Dilisensikan di bawah **[GNU GPL v3.0](LICENSE)** atau mengikuti ketentuan lisensi dari sumber hulu.
* **Skrip Otomatisasi (`scripts/` & `.github/`):** Murni karya mandiri dan dilisensikan di bawah **[MIT License](.github/workflows/license)**.

---

## 🙏 Kredit & Apresiasi

Seluruh daftar ini dapat berjalan berkat kontribusi luar biasa dari para pengelola proyek sumber terbuka berikut:

| Kredit | Last Commit |
| :--- | :--- |
| [HaGeZi's DNS Blocklists](https://github.com/hagezi/dns-blocklists) | ![HaGeZi Last Commit](https://img.shields.io/github/last-commit/hagezi/dns-blocklists?label=HaGeZi&style=flat) |
| [ABPindo (Indonesian Adblock Rules)](https://github.com/ABPindo/indonesianadblockrules) | ![ABPindo Last Commit](https://img.shields.io/github/last-commit/ABPindo/indonesianadblockrules?label=ABPindo&style=flat) |
| [Phishing Army](https://phishing.army/) | ![Phishing Army](https://img.shields.io/website?url=https%3A%2F%2Fphishing.army%2Fdownload%2Fphishing_army_blocklist.txt&up_message=Online%20%28Update%206%20Jam%29&down_message=Offline&label=Phishing%20Army&style=flat) |
| [URLhaus by abuse.ch](https://urlhaus.abuse.ch/) | ![URLhaus](https://img.shields.io/website?url=https%3A%2F%2Furlhaus.abuse.ch%2Fdownloads%2Fhostfile%2F&up_message=Online%20%28Update%205%20Menit%29&down_message=Offline&label=URLhaus%20abuse.ch&style=flat) |
| [StevenBlack's Hosts](https://github.com/StevenBlack/hosts) | ![StevenBlack Last Commit](https://img.shields.io/github/last-commit/StevenBlack/hosts?label=StevenBlack&style=flat) |

---

---

### 🔗 Tautan Klien DNS Blocker
* [NextDNS](https://nextdns.io/)
* [personalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)
* [AdGuard](https://adguard.com/en/welcome.html) / [AdGuard Home](https://adguard.com/en/adguard-home/overview.html)
* [Pi-hole](https://pi-hole.net/)
