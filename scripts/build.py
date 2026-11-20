# Copyright (c) 2026 <EazyWhale>
# Licensed under the MIT License.

import argparse
import datetime
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# ---------- PENGATURAN ----------
ALLOW = Path("Allowlist.txt")
DELETE = Path("Deletelist.txt")
DNSFILTER_DIR = Path("domains")
CUSTOM_DIR = Path("custom")
RECIPES_PATH = CUSTOM_DIR / "recipes.json"
REPO_RAW = "https://raw.githubusercontent.com/lonion-1/WhaleList/main"
REPO_URL = "https://github.com/lonion-1/WhaleList"

WILDCARD = "*.{d}"
MIN_RATIO = 0.7
WAKTU = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d.%H%M")

# ---------- SUMBER HULU ----------
HZ = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/"


def hz(nama, file):
    return (f"HaGeZi {nama}", HZ + file, "abp")


ABPINDO = ("ABPindo", "https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/abpindo.txt", "abp")
ISEKAI = ("EazyWhale Isekai Wall", "https://raw.githubusercontent.com/lonion-1/EazyWeb/blocker/EazyBlock.txt", "abp")
PHISHING_ARMY = ("Phishing Army", "https://phishing.army/download/phishing_army_blocklist.txt", "domains")
URLHAUS = ("URLhaus", "https://urlhaus.abuse.ch/downloads/hostfile/", "hosts")
STEVENBLACK_SOCIAL = ("StevenBlack Social", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social-only/hosts", "hosts")

PRESETS = {
    "EazyLife Core": [hz("Pro", "pro.txt"), hz("Pop-Up Ads", "popupads.txt"), ABPINDO],
    "EazyLife Security": [hz("Fake", "fake.txt"), PHISHING_ARMY, URLHAUS],
    "EazyLife Router & TV": [
        hz("Light", "light.txt"), ABPINDO,
        hz("Native Samsung", "native.samsung.txt"),
        hz("Native LG webOS", "native.lgwebos.txt"),
        hz("Native Xiaomi", "native.xiaomi.txt"),
        hz("Native Roku", "native.roku.txt"),
        hz("Native Amazon", "native.amazon.txt"),
    ],
    "EazyLife Family": [
        hz("Light", "light.txt"), ABPINDO, hz("Fake", "fake.txt"),
        PHISHING_ARMY, URLHAUS,
        hz("Gambling", "gambling.txt"), hz("NSFW", "nsfw.txt"),
        ISEKAI,
    ],
    "EazyLife Anti-Bypass": [hz("DoH/VPN/Proxy Bypass", "doh-vpn-proxy-bypass.txt")],
    "EazyLife Max": [
        hz("Pro++", "pro.plus.txt"), hz("Pop-Up Ads", "popupads.txt"),
        ABPINDO, hz("Threat Intelligence Feeds", "tif.txt"),
    ],
    "EazyLife Focus": [STEVENBLACK_SOCIAL],
    "EazyLife Isekai Wall": [ISEKAI, hz("Gambling", "gambling.txt")],
    "EazyLife NSFW": [hz("NSFW", "nsfw.txt")],
    "Brand: Apple": [hz("Native Apple", "native.apple.txt")],
    "Brand: Windows": [hz("Native Windows & Office", "native.winoffice.txt")],
    "Brand: Samsung": [hz("Native Samsung", "native.samsung.txt")],
    "Brand: Xiaomi": [hz("Native Xiaomi", "native.xiaomi.txt")],
    "Brand: Oppo & Realme": [hz("Native Oppo & Realme", "native.oppo-realme.txt")],
    "Brand: Vivo": [hz("Native Vivo", "native.vivo.txt")],
    "Brand: Huawei": [hz("Native Huawei", "native.huawei.txt")],
    "Brand: Amazon": [hz("Native Amazon & Fire TV", "native.amazon.txt")],
    "Brand: LG webOS": [hz("Native LG webOS Smart TV", "native.lgwebos.txt")],
    "Brand: Roku": [hz("Native Roku Streaming", "native.roku.txt")],
}

ROOT_TARGETS = [
    {
        "file": "EazyLife-Core.txt",
        "title": "EazyLife Core - Daily Ad & Tracker Blocklist",
        "min_domains": 50000,
        "sources": PRESETS["EazyLife Core"],
    },
    {
        "file": "EazyLife-Security.txt",
        "title": "EazyLife Security - Anti-Phishing, Fake & Malware",
        "min_domains": 5000,
        "sources": PRESETS["EazyLife Security"],
    },
    {
        "file": "EazyLife-RouterTV.txt",
        "title": "EazyLife Router & Smart TV - Lightweight & Telemetry Blocker",
        "min_domains": 10000,
        "sources": PRESETS["EazyLife Router & TV"],
    },
    {
        "file": "EazyLife-Family.txt",
        "title": "EazyLife Family - All-in-One Safe Home Wi-Fi Blocker",
        "min_domains": 50000,
        "sources": PRESETS["EazyLife Family"],
    },
    {
        "file": "EazyLife-AntiBypass.txt",
        "title": "EazyLife Anti-Bypass - Encrypted DNS (DoH), VPN & Proxy Blocker",
        "min_domains": 500,
        "sources": PRESETS["EazyLife Anti-Bypass"],
    },
    {
        "file": "EazyLife-Max.txt",
        "title": "EazyLife Max - Aggressive Ad, Telemetry & Threat Intelligence Blocker",
        "min_domains": 100000,
        "sources": PRESETS["EazyLife Max"],
    },
    {
        "file": "EazyLife-Focus.txt",
        "title": "EazyLife Focus - Social Media & Distraction Blocker",
        "min_domains": 500,
        "sources": PRESETS["EazyLife Focus"],
    },
    {
        "file": "EazyLife-IsekaiWall.txt",
        "title": "EazyWhale Isekai Wall - Anti-Gambling Blocklist",
        "min_domains": 2000,
        "sources": PRESETS["EazyLife Isekai Wall"],
    },
    {
        "file": "EazyLife-NSFW.txt",
        "title": "EazyLife NSFW - Adult Content Blocker (Optional)",
        "min_domains": 10000,
        "sources": PRESETS["EazyLife NSFW"],
    },
]

BRANDS = [
    ("Apple", "native.apple.txt", "Apple"),
    ("Windows", "native.winoffice.txt", "Windows & Office"),
    ("Samsung", "native.samsung.txt", "Samsung"),
    ("Xiaomi", "native.xiaomi.txt", "Xiaomi"),
    ("Oppo-Realme", "native.oppo-realme.txt", "Oppo & Realme"),
    ("Vivo", "native.vivo.txt", "Vivo"),
    ("Huawei", "native.huawei.txt", "Huawei"),
    ("Amazon", "native.amazon.txt", "Amazon & Fire TV"),
    ("LG-webOS", "native.lgwebos.txt", "LG webOS Smart TV"),
    ("Roku", "native.roku.txt", "Roku Streaming"),
]
for stem, src, label in BRANDS:
    ROOT_TARGETS.append({
        "file": f"brands/{stem}.txt",
        "title": f"EazyLife Brand - {label} Native Telemetry Blocker",
        "min_domains": 10,
        "sources": [hz(f"Native {label}", src)],
    })

# ---------- PARSER ----------
OPSI_AMAN = {"third-party", "3p", "important", "all", "popup"}

RE_DOMAIN = re.compile(r"^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:xn--[a-z0-9-]{1,59}|[a-z]{2,63})$")
RE_ABP = re.compile(r"^\|\|([a-z0-9.-]+)\^(?:\$([a-z0-9,~=-]+))?$")
RE_HOSTS = re.compile(r"^(?:0\.0\.0\.0|127\.0\.0\.1|::1?)\s+([^\s#]+)")


def valid(d):
    return d if RE_DOMAIN.match(d) else None


def parse_abp(s):
    m = RE_ABP.match(s)
    if not m:
        return None
    if m.group(2) and not set(m.group(2).split(",")) <= OPSI_AMAN:
        return None
    return valid(m.group(1))


def parse_hosts(s):
    m = RE_HOSTS.match(s)
    return valid(m.group(1)) if m else None


def parse_domains(s):
    return valid(s)


def parse_auto(s):
    # Bersihkan komentar di samping baris
    s = re.split(r"\s*[#!]", s, maxsplit=1)[0].strip()
    if not s:
        return None
    if s.startswith("||"):
        return parse_abp(s)
    if s.startswith(("0.0.0.0", "127.0.0.1", "::")):
        return parse_hosts(s)
    if s.startswith("*."):
        return valid(s[2:])
    return valid(s)


PARSER = {
    "abp": parse_abp,
    "hosts": parse_hosts,
    "domains": parse_domains,
    "auto": parse_auto,
}

# ---------- FETCH & IO ----------
CACHE = {}


def fetch(url, tries=3):
    if url in CACHE:
        return CACHE[url]
    hasil = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "EazyLife-Builder/5.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                hasil = r.read().decode("utf-8", errors="ignore").splitlines()
            break
        except Exception as e:
            print(f"    percobaan {i + 1}/{tries} gagal: {e}")
            time.sleep(3 * (i + 1))
    CACHE[url] = hasil
    return hasil


def load_list(path):
    if not path.exists():
        return set()
    hasil = set()
    for l in path.read_text(encoding="utf-8").splitlines():
        s = l.strip().lower()
        if not s or s.startswith(("!", "#")):
            continue
        token = re.split(r"[\s#!]", s, maxsplit=1)[0]
        if token:
            hasil.add(token.removeprefix("||").removesuffix("^"))
    return hasil


def baca_aturan(path, komentar):
    if not path.exists():
        return []
    return [l for l in path.read_text(encoding="utf-8").splitlines() if l and not l.startswith(komentar)]


def simpan(path, header, baris, komentar):
    if baca_aturan(path, komentar) == baris:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(header + baris) + "\n", encoding="utf-8")
    return True


def fmt_angka(n):
    return f"{n:,}".replace(",", ".")


def fmt_ukuran(b):
    if b < 1024 * 1024:
        return f"{round(b / 1024)} KB"
    return f"{b / (1024 * 1024):.1f} MB".replace(".", ",")


def load_recipes():
    if not RECIPES_PATH.exists():
        return {}
    try:
        return json.loads(RECIPES_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"::warning::Gagal membaca {RECIPES_PATH}: {e}")
        return {}


def recipe_to_target(slug, recipe):
    sources = []
    for p in recipe.get("presets", []):
        if p in PRESETS:
            sources.extend(PRESETS[p])
    for idx, url in enumerate(recipe.get("external_urls", []), start=1):
        host = urllib.parse.urlparse(url).netloc or f"External-{idx}"
        sources.append((f"External ({host})", url, "auto"))

    desc = recipe.get("description", "").strip()
    title = f"EazyLife Custom ({slug}) - {desc}" if desc else f"EazyLife Custom - {slug}"
    return {
        "file": f"custom/{slug}.txt",
        "title": title,
        "min_domains": 1,
        "sources": sources,
        "is_custom": True,
    }


def build_target(target, izin, hapus):
    nama_file = target["file"]
    out_path = Path(nama_file)
    print(f"=== Membangun {nama_file} ===")
    domains = set()
    berhasil = []

    for nama, url, fmt in target["sources"]:
        print(f"  Tarik: {nama}")
        baris = fetch(url)
        if baris is None:
            print(f"    LEWATI {nama}")
            continue
        sebelum = len(domains)
        parse = PARSER[fmt]
        for b in baris:
            s = b.strip().lower()
            if not s or s[0] in "!#[" or s.startswith("@@"):
                continue
            d = parse(s)
            if d:
                domains.add(d)
        print(f"    +{len(domains) - sebelum} domain baru")
        berhasil.append(nama)

    domains -= izin
    domains -= hapus

    if not berhasil or len(domains) < target["min_domains"]:
        print(f"  GAGAL {nama_file}: hanya {len(domains)} domain dari {len(berhasil)} sumber.\n")
        return None

    # Eliminasi subdomain jika domain induk sudah ada
    hasil = []
    for d in sorted(domains):
        bagian = d.split(".")
        if any(".".join(bagian[i:]) in domains for i in range(1, len(bagian) - 1)):
            continue
        hasil.append(d)

    # Pengaman anjlok drastis (hanya untuk list bawaan yang sudah ada sebelumnya)
    if not target.get("is_custom"):
        lama_jml = sum(1 for l in baca_aturan(out_path, "!") if l.startswith("||"))
        if lama_jml and len(hasil) < lama_jml * MIN_RATIO:
            print(f"  GAGAL {nama_file}: anjlok dari {lama_jml} ke {len(hasil)} domain.\n")
            return None

    # Output 1: Format Adblock (||domain^)
    aturan = [f"||{d}^" for d in hasil]
    header_abp = [
        f"! Title: {target['title']}",
        "! License: GNU General Public License v3.0 (GPL-3.0)",
        "! Maintainer: EazyWhale",
        f"! Version: {WAKTU}",
        "! Expires: 1 day",
        f"! Total Unique Domains: {len(hasil)}",
        f"! Sources: {', '.join(berhasil)}",
        "! --------------------------------------------------",
        "",
    ]
    ubah_abp = simpan(out_path, header_abp, aturan, "!")

    # Output 2: Format personalDNSfilter (wildcard)
    baris_dns = [item for d in hasil for item in (d, WILDCARD.format(d=d))]
    header_dns = [
        f"# Title: {target['title']} (personalDNSfilter Wildcard)",
        f"# Version: {WAKTU}",
        f"# Count: {len(hasil)}",
        f"# Sources: {', '.join(berhasil)}",
        "",
    ]
    ubah_dns = simpan(DNSFILTER_DIR / nama_file, header_dns, baris_dns, "#")

    status = "diperbarui" if (ubah_abp or ubah_dns) else "tidak ada perubahan"
    print(f"  Selesai {nama_file}: {len(hasil)} domain dari {len(berhasil)} sumber ({status}).\n")
    return {
        "count": len(hasil),
        "size": fmt_ukuran(out_path.stat().st_size),
    }


def update_root_readme(all_targets):
    def isi_tag(teks, tag, nama_file, nilai):
        pola = rf"(<!-- {tag}:{re.escape(nama_file)} -->).*?(<!-- /{tag} -->)"
        return re.sub(pola, lambda m: m.group(1) + nilai + m.group(2), teks)

    readme_path = Path("README.md")
    if not readme_path.exists():
        return
    teks_awal = readme_path.read_text(encoding="utf-8")
    teks_readme = teks_awal
    for target in all_targets:
        f_out = Path(target["file"])
        if not f_out.exists():
            continue
        jml = sum(1 for l in f_out.read_text(encoding="utf-8").splitlines() if l.startswith("||"))
        teks_readme = isi_tag(teks_readme, "COUNT", target["file"], fmt_angka(jml))
        teks_readme = isi_tag(teks_readme, "SIZE", target["file"], fmt_ukuran(f_out.stat().st_size))
    if teks_readme != teks_awal:
        readme_path.write_text(teks_readme, encoding="utf-8")
    print("README.md utama: statistik diperiksa.")


def update_custom_readme(recipes):
    CUSTOM_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 🛠️ WhaleList — Daftar Custom (`custom/`)",
        "",
        "Kumpulan racikan *DNS blocklist* gabungan hasil permintaan pengguna & *maintainer* (bebas duplikasi / *Zero Redundancy* dan diperbarui otomatis setiap hari pukul `04:23 WIB`).",
        "",
        f"> **Ingin membuat kombinasi sendiri?** Buka **[Form Request Custom Blocklist]({REPO_URL}/issues/new?template=custom-list.yml)** di tab *Issues*.",
        "",
        "---",
        "",
    ]

    if not recipes:
        lines.extend([
            "*Belum ada daftar custom yang dibuat. Silakan ajukan lewat tautan di atas!*",
            "",
        ])
    else:
        lines.extend([
            "## 📦 Daftar File Custom Tersedia",
            "",
            "| File Custom | Deskripsi & Komposisi | Domain | Ukuran | Raw URL (Adblock) | Wildcard URL (`personalDNSfilter`) |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |",
        ])

        details = [
            "",
            "---",
            "",
            "## 🔍 Rincian Komposisi Tiap File Custom",
            "",
        ]

        for slug in sorted(recipes.keys()):
            info = recipes[slug]
            f_path = CUSTOM_DIR / f"{slug}.txt"
            if f_path.exists():
                jml = sum(1 for l in f_path.read_text(encoding="utf-8").splitlines() if l.startswith("||"))
                jml_str = fmt_angka(jml)
                size_str = fmt_ukuran(f_path.stat().st_size)
            else:
                jml_str = "-"
                size_str = "-"

            desc = info.get("description", "-").replace("|", "\\|").replace("\n", " ")
            presets = info.get("presets", [])
            ext_urls = info.get("external_urls", [])

            ringkasan_isi = []
            if presets:
                ringkasan_isi.append(", ".join(presets))
            if ext_urls:
                ringkasan_isi.append(f"+{len(ext_urls)} URL luar")
            isi_str = " • ".join(ringkasan_isi) if ringkasan_isi else "-"

            raw_abp = f"{REPO_RAW}/custom/{slug}.txt"
            raw_dns = f"{REPO_RAW}/domains/custom/{slug}.txt"

            lines.append(
                f"| **`{slug}.txt`** | {desc}<br><sub>*Isi: {isi_str}*</sub> | {jml_str} | {size_str} | `{raw_abp}` | `{raw_dns}` |"
            )

            req_by = info.get("requested_by", "unknown")
            issue_num = info.get("issue_number")
            issue_ref = f"([#{issue_num}]({REPO_URL}/issues/{issue_num}))" if issue_num else ""

            details.append(f"<details>")
            details.append(f"<summary><b><code>custom/{slug}.txt</code></b> — {desc} {issue_ref}</summary>")
            details.append("<br>\n")
            details.append(f"* **Diminta oleh:** `@{req_by}` {issue_ref}")
            details.append(f"* **Daftar Bawaan ({len(presets)}):** {', '.join(f'`{p}`' for p in presets) if presets else '*Tidak ada*'}")
            if ext_urls:
                details.append(f"* **URL Eksternal ({len(ext_urls)}):**")
                for u in ext_urls:
                    details.append(f"  * `{u}`")
            else:
                details.append("* **URL Eksternal:** *Tidak ada*")
            details.append("\n</details>\n")

        lines.extend(details)

    out_readme = CUSTOM_DIR / "README.md"
    out_readme.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("custom/README.md: berhasil diperbarui.")


def main():
    parser = argparse.ArgumentParser(description="EazyLife Blocklist Builder")
    parser.add_argument("--only-custom", help="Bangun hanya 1 file custom berdasarkan slug")
    args = parser.parse_args()

    izin = load_list(ALLOW)
    hapus = load_list(DELETE)
    if izin:
        print(f"Allowlist aktif: {len(izin)} domain diizinkan")
    if hapus:
        print(f"Deletelist aktif: {len(hapus)} domain dihapus")

    recipes = load_recipes()

    # Mode khusus Issue: bangun hanya 1 custom list tertentu agar cepat
    if args.only_custom:
        slug = args.only_custom
        if slug not in recipes:
            print(f"Resep '{slug}' tidak ditemukan di {RECIPES_PATH}")
            sys.exit(1)
        stats = build_target(recipe_to_target(slug, recipes[slug]), izin, hapus)
        if not stats:
            sys.exit(1)
        update_custom_readme(recipes)
        print(f"CUSTOM_RESULT={json.dumps(stats)}")
        return

    # Mode penuh (Jadwal Harian): bangun semua root, brand, dan custom
    sukses, gagal = [], []
    custom_targets = [recipe_to_target(slug, recipes[slug]) for slug in sorted(recipes.keys())]
    semua_target = ROOT_TARGETS + custom_targets

    for target in semua_target:
        res = build_target(target, izin, hapus)
        if res:
            sukses.append(target["file"])
        else:
            gagal.append(target["file"])

    update_root_readme(ROOT_TARGETS)
    update_custom_readme(recipes)

    Path("last-run.txt").write_text(f"Last check (UTC): {WAKTU}\n", encoding="utf-8")

    for f in gagal:
        print(f"::warning::{f} gagal dibangun, file lama dipertahankan")
    if not sukses:
        sys.exit(1)


if __name__ == "__main__":
    main() 
