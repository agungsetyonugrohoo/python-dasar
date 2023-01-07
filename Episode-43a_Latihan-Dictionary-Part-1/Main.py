"""
Latihan Dictionary Part-1
-> Mengambil data input dari user kemudian memasukkannya ke dalam variabel penampung data dictionary dalam nesting dictionary
- Import os merupakan suatu library yang powerful yang berguna untuk mengatur aktivitas dari laptop kita

"""

import datetime
import os

# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'skl_lulus':0,
    'lahir':datetime.datetime(1111,11,11)
}

data_mahasiswa = {}

# os.system("cls") ini berfungsi untuk menghapus riwayat hasil print dari terminal (clear screen) sehingga saat ini yang ditampilkan hanyalah bagian-bagian yang kita inginkan saja
os.system("cls") # command clear screen untuk windows
# os.system("clear") # command clear screen untuk linux dan mac
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

# membuat dictionary baru yaitu mahasiswa menggunakan key yang berada di mahasiswa_template
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa : ")
mahasiswa['nim'] = input("NIM Mahasiswa : ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus : "))
TAHUN_LAHIR = int(input("Tahun lahir (YYYY) : "))
BULAN_LAHIR = int(input("Bulan lahir (1-12) : "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

print(mahasiswa)

