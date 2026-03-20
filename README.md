# Meta Data Checker
Created by LAKSAMANA DZU NUR NAIN

Script Python untuk memeriksa metadata (EXIF) pada file foto dan video menggunakan ExifTool.

## Fitur
- Pemeriksaan metadata file tunggal atau seluruh isi folder.
- Filter khusus untuk GPS/Lokasi, Kamera/Device, dan Tanggal/Waktu.
- Fitur simpan hasil pemeriksaan ke file TXT.
- Cek status instalasi ExifTool secara otomatis.

## Instalasi & Persyaratan
Pastikan Anda sudah menginstal **ExifTool** di sistem Anda:

- **Ubuntu/Debian/Codespaces:** `sudo apt update && sudo apt install exiftool -y`
- **Termux:** `pkg install exiftool`
- **Windows:** Download executable dari [exiftool.org](https://exiftool.org/)

## Cara Menjalankan
1. Clone repositori ini.
2. Jalankan script:
   ```bash
   python3 metadata_checker.py
   ```

