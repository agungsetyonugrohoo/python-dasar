"""
Latihan Dictionary Part-1
-> Mengambil data input dari user kemudian memasukkannya ke dalam variabel penampung data dictionary dalam nesting dictionary
- Import os merupakan suatu library yang powerful yang berguna untuk mengatur aktivitas dari laptop kita

"""

import datetime
import os
import string
import random

# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'skl_lulus':0,
    'lahir':datetime.datetime(1111,11,11)
}

data_mahasiswa = {}

while True :
    # os.system("cls") ini berfungsi untuk menghapus riwayat hasil print dari terminal (clear screen) sehingga saat ini yang ditampilkan hanyalah bagian-bagian yang kita inginkan saja
    os.system("cls") # command clear screen untuk windows
    # os.system("clear") # command clear screen untuk linux dan mac
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    # membuat dictionary baru yaitu mahasiswa menggunakan key yang berada di mahasiswa_template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM Mahasiswa : ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus : "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) # mengenerate key dengan nilai string random yang dipilih berdasarkan 6 iterasi sehingga menghasilkan 6 karakter string random

    data_mahasiswa.update({KEY:mahasiswa}) # untuk menambahkan data template mahasiswa yang sudah diisi ke dalam data_mahasiswa

    # dari tutorial multi keys dan nesting dictionary, hilangkan beasiswa
    # Membuat header tabel untuk data mahasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS':<3} {'Lahir':<10}")
    # KEY rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 6
    # Nama rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 17
    # SKS rata kiri yang tidak digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya tetap 3
    # Lahir rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 10

    print("-"*50)

    for mahasiswa in data_mahasiswa: # melakukan iterasi dengan mengakses keynya
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama'] # mengakses data nama dari key tertentu
        NIM = data_mahasiswa[KEY]['nim'] # mengakses data nim dari key tertentu
        SKS = data_mahasiswa[KEY]['sks_lulus'] # mengakses data sks lulus dari key tertentu
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # mengakses data lahir dan mengkonversinya dalam format string menjadi dd-mm-yy

        # menampilkan data mahasiswa secara terurut berdasarkan header tabel
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == 'n' :
        break

print("\nAkhir dari program, terimakasih")




