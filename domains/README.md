# 🐋 WhaleList — Wildcard Domain Lists (`personalDNSfilter`)

Folder ini menyediakan seluruh daftar blokir **WhaleList** dalam format *wildcard* polos (`*domain`) agar ringan di memori dan kompatibel penuh dengan aplikasi pemblokir DNS lokal Android seperti **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** (tersedia juga di [F-Droid](https://f-droid.org/packages/dnsfilter.android/)).

---

## 📦 Daftar Utama (*Core Lists*)

* **EazyLife Core (Wajib — Iklan harian, *pop-up*, pelacak, & iklan lokal Indonesia):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Core.txt`
* **EazyLife Security (Wajib — Anti-*phishing*, *scam*, & *malware*):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Security.txt`
* **EazyLife Router & TV (Super ringan untuk RAM terbatas & Smart TV):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-RouterTV.txt`

---

## 🛡️ Daftar Spesial, Keluarga & Power User

* **EazyLife Isekai Wall (Pemblokiran khusus situs perjudian online):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-IsekaiWall.txt`
* **EazyLife NSFW (Pemblokiran khusus konten dewasa 18+):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-NSFW.txt`
* **EazyLife Anti-Bypass (Blokir server DoH, VPN, & proxy publik):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-AntiBypass.txt`
* **EazyLife Focus (Blokir media sosial populer / *digital detox*):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Focus.txt`
* **EazyLife Family (Paket komplet keluarga — 19,9 MB, disarankan RAM lega):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Family.txt`
* **EazyLife Max (Perlindungan agresif — 34,8 MB, khusus *Power User* / RAM besar):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Max.txt`

---

## 📱 Daftar Modular per Brand (`domains/brands/`)

Pilih **hanya** sesuai merek perangkat yang digunakan agar hemat RAM:

* **Apple (iPhone, iPad, Mac, Apple TV):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Apple.txt`
* **Windows (PC/Laptop Windows 10/11 & Office):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Windows.txt`
* **Samsung (HP/Tablet Galaxy & Tizen Smart TV):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Samsung.txt`
* **Xiaomi (Xiaomi, Redmi, POCO & Mi TV):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Xiaomi.txt`
* **Oppo & Realme (HP Oppo & Realme):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Oppo-Realme.txt`
* **Vivo (HP Vivo & iQOO):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Vivo.txt`
* **Huawei (HP/Tablet Huawei & HarmonyOS):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Huawei.txt`
* **Amazon (Fire TV, Kindle, & Echo):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Amazon.txt`
* **LG webOS (LG Smart TV):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/LG-webOS.txt`
* **Roku (Perangkat Streaming Roku):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Roku.txt`

---

## ⚙️ Cara Pasang di PersonalDNSfilter

1. Unduh dan pasang **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** (tersedia juga di [F-Droid](https://f-droid.org/packages/dnsfilter.android/)).
2. Salin tautan yang dibutuhkan (disarankan **Core + Security + 1 merek HP**).
3. Buka aplikasi $\rightarrow$ ketuk **Advanced settings** $\rightarrow$ pilih **Configure additional hosts**.
4. Tempelkan tautan yang sudah disalin dan pastikan kotaknya tercentang.
5. Kembali ke layar utama aplikasi, lalu tekan tombol **RELOAD FILTER**.

---

> Coba periksa daftar kombinasi yang sudah tersedia lainnya **[di sini](./custom/README.md)**.

---

> 🙏 Terima kasih kepada **Ingo Zenz** atas proyek *open-source* **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** ([GitHub](https://github.com/IngoZenz/personaldnsfilter)).
