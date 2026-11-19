# 🐋 WhaleList — Wildcard Domain Lists (personalDNSfilter)

Folder ini berisi daftar blokir versi *wildcard* polos (`*domain`) yang dioptimalkan agar ringan di memori untuk aplikasi pemblokir DNS lokal Android seperti **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** (tersedia juga di [F-Droid](https://f-droid.org/packages/dnsfilter.android/)).

> ⚠️ **Catatan RAM (`EazyLife-Max.txt`):** File versi *Max* berukuran **34+ MB**. Jangan dipasang di `personalDNSfilter` pada ponsel dengan RAM terbatas, karena bisa bikin berat atau *force close*. Untuk harian di ponsel, cukup pakai kombinasi **Core + Security + Indo + IsekaiWall**.

---

## 🛡️ Daftar Utama (Core & Keamanan)

* **EazyLife Core (Disarankan — Ringan & Aman):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Core.txt`
* **EazyLife Security (Disarankan — Malware & Phishing):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Security.txt`
* **EazyLife IsekaiWall (Disarankan — Judol & Scam):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-IsekaiWall.txt`
* **EazyLife Pro (Opsional — Ketat, RAM Menengah ke Atas):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Pro.txt`
* **EazyLife Max (Berat 34+ MB — Khusus Router / PC / Cloud DNS):**
  `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/EazyLife-Max.txt`

---

## 📱 Telemetri Bawaan Merek HP (Native Telemetry)

Pilih **hanya** sesuai merek HP yang dipakai agar hemat RAM:

* **Apple:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Apple.txt`
* **Windows:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Windows.txt`
* **Samsung:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Samsung.txt`
* **Xiaomi:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Xiaomi.txt`
* **Oppo & Realme:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Oppo-Realme.txt`
* **Vivo:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Vivo.txt`
* **Huawei:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Huawei.txt`
* **Amazon:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Amazon.txt`
* **LG webOS:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/LG-webOS.txt`
* **Roku:** `https://raw.githubusercontent.com/lonion-1/WhaleList/main/domains/brands/Roku.txt`

---

## ⚙️ Cara Pasang di PersonalDNSfilter

1. Unduh dan pasang **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** (atau via [F-Droid](https://f-droid.org/packages/dnsfilter.android/)).
2. Salin tautan yang dibutuhkan (disarankan **Core + Security + Indo + IsekaiWall + 1 merek HP**).
3. Buka aplikasi $\rightarrow$ ketuk **Advanced settings** $\rightarrow$ pilih **Configure additional hosts**.
4. Tempelkan tautan yang sudah disalin dan pastikan kotaknya tercentang.
5. Kembali ke layar utama, lalu tekan **RELOAD FILTER**.

---

> 🙏 Terima kasih kepada **Ingo Zenz** atas proyek *open-source* **[PersonalDNSfilter](https://www.zenz-solutions.de/personaldnsfilter-wp/)** ([GitHub](https://github.com/IngoZenz/personaldnsfilter)).
