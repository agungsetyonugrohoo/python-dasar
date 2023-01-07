"""
Multi Keys dan Nesting Dictionary

- Data dictionary dapat menghimpun berbagai tipe data yang lain seperti string, numbers dan juga boolean
- Import datetime untuk menunjukkan tanggal, bulan dan tahun dimana parameter dalam sintaksnya adalah datetime(tahun, bulan, tanggal)
- Untuk mengatur align dalam format string dapat menggunakan tanda operator berikut yang diikuti dengan jumlah karakternya diantaranya "<x" yaitu untuk rata kiri dalam sejumlah karakter x, ">x" yaitu untuk rata kanan dalam sejumlah karakter x dan "^x" untuk rata tengah dalam sejumlah karakter x
- Dalam menggunakan fungsi datetime() kita juga dapat mengakses data yang digenerate dari fungsi datetime dengan menggunakan method strftime("format-string") dimana strftime ini berfungsi untuk menunjukkan format string dari tanggal, bulan dan tahun yang digenerate oleh datetime dan format string juga dapat berbagai macam tipenya salah satunya "%x" dimana ini akan menampilkan bentuk tanggal, bulan dan tahun dalam bentuk "dd-mm-yy"
"""

import datetime

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'19022001',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Otong Surotong',
    'nim':'19022002',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa2 = {
    'nama':'Otong Surotong',
    'nim':'19022002',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama':'Asep Si Kasyep',
    'nim':'19022003',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

# Membuat header tabel untuk data mahasiswa
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
# KEY rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 6
# Nama rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 17
# SKS rata kiri yang tidak digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya tetap 3
# Beasiswa rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 9
# Lahir rata kiri yang digabungkan dengan sejumlah spasi sehingga jumlah karakter seluruhnya 10

print("-"*50)

for mahasiswa in data_mahasiswa: # melakukan iterasi dengan mengakses keynya
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama'] # mengakses data nama dari key tertentu
    NIM = data_mahasiswa[KEY]['nim'] # mengakses data nim dari key tertentu
    SKS = data_mahasiswa[KEY]['sks_lulus'] # mengakses data sks lulus dari key tertentu
    BEASISWA = data_mahasiswa[KEY]['beasiswa'] # mengakses data beasiswa dari key tertentu
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # mengakses data lahir dan mengkonversinya dalam format string menjadi dd-mm-yy

    # menampilkan data mahasiswa secara terurut berdasarkan header tabel
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

