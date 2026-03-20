#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Pemeriksa Metadata Foto dan Video
Created by Laksamana Dzu Nur Ain
"""

import os
import sys
import subprocess
import json
from datetime import datetime
import platform

# Warna untuk terminal
class Warna:
    HEADER = '\033[95m'
    KUNING_TERANG = '\033[93m'  # Kuning cerah
    HIJAU = '\033[92m'
    BIRU = '\033[94m'
    MERAH = '\033[91m'
    CYAN = '\033[96m'
    PUTIH = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def clear_screen():
    """Bersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_logo():
    """Tampilkan logo META DATA dengan warna kuning cerah"""
    logo = f"""
{Warna.KUNING_TERANG}{Warna.BOLD}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███╗   ███╗███████╗████████╗ █████╗     ██████╗  █████╗ ████████╗ █████╗ 
    ║   ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
    ║   ██╔████╔██║█████╗     ██║   ███████║    ██║  ██║███████║   ██║   ███████║
    ║   ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║    ██║  ██║██╔══██║   ██║   ██╔══██║
    ║   ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║    ██████╔╝██║  ██║   ██║   ██║  ██║
    ║   ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    {Warna.RESET}
    
{Warna.CYAN}{Warna.BOLD}            created by laksamana dzu nur ain{Warna.RESET}
{Warna.HIJAU}{Warna.BOLD}            ═══════════════════════════════════{Warna.RESET}
    """
    print(logo)

def tampilkan_menu():
    """Tampilkan menu pilihan"""
    menu = f"""
{Warna.BIRU}{Warna.BOLD}[ MENU PILIHAN ]{Warna.RESET}

{Warna.PUTIH}┌─────────────────────────────────────┐
│  {Warna.HIJAU}[1]{Warna.PUTIH} Periksa metadata FILE                │
│  {Warna.HIJAU}[2]{Warna.PUTIH} Periksa metadata FOLDER              │
│  {Warna.HIJAU}[3]{Warna.PUTIH} Lihat semua metadata (LENGKAP)       │
│  {Warna.HIJAU}[4]{Warna.PUTIH} Lihat metadata TANGGAL/WAKTU         │
│  {Warna.HIJAU}[5]{Warna.PUTIH} Lihat metadata GPS/LOKASI            │
│  {Warna.HIJAU}[6]{Warna.PUTIH} Lihat metadata KAMERA/DEVICE         │
│  {Warna.HIJAU}[7]{Warna.PUTIH} Simpan metadata ke file TXT          │
│  {Warna.HIJAU}[8]{Warna.PUTIH} Cek apakah EXIFTool terinstall       │
│  {Warna.HIJAU}[0]{Warna.PUTIH} KELUAR                                │
└─────────────────────────────────────┘{Warna.RESET}
    """
    print(menu)

def cek_exiftool():
    """Cek apakah exiftool sudah terinstall"""
    try:
        if platform.system() == "Windows":
            # Cek di Windows
            result = subprocess.run(['where', 'exiftool'], capture_output=True, text=True)
        else:
            # Cek di Linux/Mac
            result = subprocess.run(['which', 'exiftool'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"{Warna.HIJAU}✓ EXIFTool terinstall di: {result.stdout.strip()}{Warna.RESET}")
            
            # Cek versi
            versi = subprocess.run(['exiftool', '-ver'], capture_output=True, text=True)
            print(f"{Warna.HIJAU}✓ Versi: {versi.stdout.strip()}{Warna.RESET}")
            return True
        else:
            print(f"{Warna.MERAH}✗ EXIFTool TIDAK terinstall!{Warna.RESET}")
            print(f"{Warna.KUNING_TERANG}Silakan install EXIFTool dari: https://exiftool.org/{Warna.RESET}")
            return False
    except Exception as e:
        print(f"{Warna.MERAH}Error: {e}{Warna.RESET}")
        return False

def periksa_file():
    """Periksa metadata dari satu file"""
    file_path = input(f"{Warna.CYAN}Masukkan path file (contoh: C:/foto.jpg): {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    print(f"{Warna.KUNING_TERANG}Membaca metadata dari: {file_path}{Warna.RESET}")
    print("-" * 50)
    
    try:
        # Jalankan exiftool
        result = subprocess.run(['exiftool', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"{Warna.MERAH}Error: {result.stderr}{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal menjalankan exiftool: {e}{Warna.RESET}")

def periksa_folder():
    """Periksa metadata dari semua file dalam folder"""
    folder_path = input(f"{Warna.CYAN}Masukkan path folder: {Warna.RESET}").strip()
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"{Warna.MERAH}Folder tidak ditemukan!{Warna.RESET}")
        return
    
    # Ekstensi file yang umum untuk foto/video
    ekstensi = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.mp4', '.mov', '.avi', '.mkv', '.3gp']
    
    print(f"{Warna.KUNING_TERANG}Mencari file media di: {folder_path}{Warna.RESET}")
    print("-" * 50)
    
    file_ditemukan = False
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in ekstensi):
                file_ditemukan = True
                file_path = os.path.join(root, file)
                print(f"{Warna.HIJAU}File: {file_path}{Warna.RESET}")
                
                # Ambil info dasar (tanggal)
                try:
                    result = subprocess.run(['exiftool', '-DateTimeOriginal', '-CreateDate', '-FileModifyDate', file_path], 
                                          capture_output=True, text=True)
                    if result.stdout.strip():
                        print(result.stdout)
                    else:
                        print(f"{Warna.MERAH}  Tidak ada metadata tanggal{Warna.RESET}")
                except:
                    pass
                print("-" * 30)
    
    if not file_ditemukan:
        print(f"{Warna.KUNING_TERANG}Tidak ada file media ditemukan di folder tersebut.{Warna.RESET}")

def lihat_semua_metadata():
    """Lihat semua metadata lengkap"""
    file_path = input(f"{Warna.CYAN}Masukkan path file: {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    print(f"{Warna.KUNING_TERANG}Menampilkan SEMUA metadata...{Warna.RESET}")
    print("=" * 70)
    
    try:
        # -a: tampilkan semua tag (termasuk yang duplikat)
        # -g: group by category
        # -G: tampilkan group name
        result = subprocess.run(['exiftool', '-a', '-g', '-G', file_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"{Warna.MERAH}Error: {result.stderr}{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal: {e}{Warna.RESET}")

def lihat_tanggal_waktu():
    """Lihat hanya metadata tanggal dan waktu"""
    file_path = input(f"{Warna.CYAN}Masukkan path file: {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    print(f"{Warna.KUNING_TERANG}Metadata TANGGAL dan WAKTU:{Warna.RESET}")
    print("-" * 40)
    
    tags = [
        '-DateTimeOriginal',    # Waktu asli pengambilan
        '-CreateDate',          # Waktu pembuatan file
        '-ModifyDate',          # Waktu modifikasi
        '-FileModifyDate',      # Waktu modifikasi file
        '-FileCreateDate',      # Waktu pembuatan file (jika ada)
        '-GPSDateStamp',        # Tanggal GPS
        '-GPSTimeStamp',        # Waktu GPS
        '-TimeStamp',           # Stempel waktu umum
        '-MediaCreateDate',     # Video: waktu pembuatan
        '-MediaModifyDate',     # Video: waktu modifikasi
        '-TrackCreateDate',     # Video: track creation
        '-TrackModifyDate'      # Video: track modification
    ]
    
    try:
        result = subprocess.run(['exiftool'] + tags + [file_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout.strip():
                print(result.stdout)
            else:
                print(f"{Warna.KUNING_TERANG}Tidak ada metadata tanggal/waktu ditemukan.{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Error: {result.stderr}{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal: {e}{Warna.RESET}")

def lihat_gps():
    """Lihat metadata GPS/lokasi"""
    file_path = input(f"{Warna.CYAN}Masukkan path file: {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    print(f"{Warna.KUNING_TERANG}Metadata GPS/LOKASI:{Warna.RESET}")
    print("-" * 40)
    
    tags = [
        '-gps*',                # Semua tag GPS
        '-Geolocation*',        # Geolocation tags
        '-Location*'            # Location tags
    ]
    
    try:
        result = subprocess.run(['exiftool'] + tags + [file_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout.strip():
                print(result.stdout)
                
                # Coba extract koordinat jika ada
                coord = subprocess.run(['exiftool', '-GPSPosition', file_path], 
                                      capture_output=True, text=True)
                if coord.stdout.strip():
                    print(f"\n{Warna.HIJAU}Google Maps link:{Warna.RESET}")
                    print(f"https://www.google.com/maps?q={coord.stdout.strip()}")
            else:
                print(f"{Warna.KUNING_TERANG}Tidak ada metadata GPS ditemukan.{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Error: {result.stderr}{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal: {e}{Warna.RESET}")

def lihat_kamera():
    """Lihat metadata kamera/device"""
    file_path = input(f"{Warna.CYAN}Masukkan path file: {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    print(f"{Warna.KUNING_TERANG}Metadata KAMERA/DEVICE:{Warna.RESET}")
    print("-" * 40)
    
    tags = [
        '-Make',                # Merek
        '-Model',               # Model
        '-Lens*',               # Informasi lensa
        '-Software',            # Software yang digunakan
        '-Exposure*',           # Info exposure
        '-ISO',                 # ISO
        '-FNumber',             # Aperture
        '-FocalLength',         # Focal length
        '-Flash',               # Flash
        '-WhiteBalance'         # White balance
    ]
    
    try:
        result = subprocess.run(['exiftool'] + tags + [file_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout.strip():
                print(result.stdout)
            else:
                print(f"{Warna.KUNING_TERANG}Tidak ada metadata kamera ditemukan.{Warna.RESET}")
        else:
            print(f"{Warna.MERAH}Error: {result.stderr}{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal: {e}{Warna.RESET}")

def simpan_ke_file():
    """Simpan metadata ke file teks"""
    file_path = input(f"{Warna.CYAN}Masukkan path file yang akan diperiksa: {Warna.RESET}").strip()
    
    if not os.path.exists(file_path):
        print(f"{Warna.MERAH}File tidak ditemukan!{Warna.RESET}")
        return
    
    # Buat nama file output
    base_name = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"metadata_{base_name}_{timestamp}.txt"
    
    print(f"{Warna.KUNING_TERANG}Menyimpan metadata ke: {output_file}{Warna.RESET}")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Tulis header
            f.write("=" * 70 + "\n")
            f.write(f"METADATA FILE: {file_path}\n")
            f.write(f"DIPERIKSA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"DIBUAT OLEH: laksamana dzu nur ain\n")
            f.write("=" * 70 + "\n\n")
            
            # Jalankan exiftool dan simpan output
            result = subprocess.run(['exiftool', '-a', '-g', '-G', file_path], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                f.write(result.stdout)
                print(f"{Warna.HIJAU}✓ Metadata berhasil disimpan ke {output_file}{Warna.RESET}")
            else:
                f.write(f"ERROR: {result.stderr}")
                print(f"{Warna.MERAH}Error saat membaca metadata{Warna.RESET}")
    except Exception as e:
        print(f"{Warna.MERAH}Gagal menyimpan file: {e}{Warna.RESET}")

def main():
    """Fungsi utama program"""
    while True:
        clear_screen()
        tampilkan_logo()
        tampilkan_menu()
        
        pilihan = input(f"{Warna.BIRU}Pilih menu [0-8]: {Warna.RESET}").strip()
        
        if pilihan == '0':
            print(f"\n{Warna.HIJAU}Terima kasih telah menggunakan script ini!{Warna.RESET}")
            print(f"{Warna.KUNING_TERANG}Created by laksamana dzu nur ain{Warna.RESET}")
            sys.exit(0)
        
        elif pilihan == '1':
            periksa_file()
        
        elif pilihan == '2':
            periksa_folder()
        
        elif pilihan == '3':
            lihat_semua_metadata()
        
        elif pilihan == '4':
            lihat_tanggal_waktu()
        
        elif pilihan == '5':
            lihat_gps()
        
        elif pilihan == '6':
            lihat_kamera()
        
        elif pilihan == '7':
            simpan_ke_file()
        
        elif pilihan == '8':
            cek_exiftool()
        
        else:
            print(f"{Warna.MERAH}Pilihan tidak valid!{Warna.RESET}")
        
        input(f"\n{Warna.CYAN}Tekan Enter untuk kembali ke menu...{Warna.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Warna.HIJAU}Terima kasih telah menggunakan script ini!{Warna.RESET}")
        print(f"{Warna.KUNING_TERANG}Created by laksamana dzu nur ain{Warna.RESET}")
        sys.exit(0)
