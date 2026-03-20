# 🛠️ Meta Data Checker
**Created by LAKSAMANA DZU NUR NAIN**

Script Python profesional untuk memeriksa metadata (EXIF) pada file foto dan video menggunakan **ExifTool**. Script ini mendukung pengecekan GPS, informasi kamera, tanggal asli pengambilan, dan penyimpanan laporan ke file TXT.

---

## 🚀 Cara Instalasi & Menjalankan

Pilih perangkat yang Anda gunakan di bawah ini:

### 📱 1. Android (Termux)
Buka aplikasi Termux dan jalankan perintah berikut:
```bash
pkg update && pkg upgrade
pkg install python git exiftool -y
git clone https://github.com/abuesbol74-source/meta-data-
cd meta-data-
python metadata_checker.py
```

### 🐧 2. Linux (Ubuntu / Kali Linux / Debian)
Buka terminal dan jalankan:
```bash
sudo apt update && sudo apt install python3 git exiftool -y
git clone https://github.com/abuesbol74-source/meta-data-
cd meta-data-
python3 metadata_checker.py
```

### 🖥️ 3. Windows (PowerShell / Command Prompt)
1. **Install Python:** Download di [python.org](https://www.python.org/downloads/).
2. **Install ExifTool:** Download `exiftool(-k).exe` dari [exiftool.org](https://exiftool.org/), ubah namanya menjadi `exiftool.exe`, dan masukkan ke folder `C:\Windows`.
3. Buka **Command Prompt (CMD)** atau **PowerShell**, lalu jalankan:
```powershell
git clone https://github.com/abuesbol74-source/meta-data-
cd meta-data-
python metadata_checker.py
```

---

## 📋 Fitur Utama
* **Menu 1-2:** Periksa metadata file tunggal atau seluruh folder.
* **Menu 3:** Mode Lengkap (Semua Tag EXIF).
* **Menu 4-6:** Filter khusus Tanggal, GPS (Lokasi), dan Kamera (Device).
* **Menu 7:** Simpan hasil scan ke file `.txt` secara otomatis.
* **Menu 8:** Cek status sistem apakah ExifTool sudah siap digunakan.

---

## ⚠️ Catatan Penting
Jika Anda menggunakan **Termux**, pastikan Anda memberikan izin akses penyimpanan agar script bisa membaca foto di galeri:
```bash
termux-setup-storage
```

**LAKSAMANA DZU NUR NAIN** - *Cybersecurity Enthusiast*
