"""
Menggunakan standard library python

Python memiliki standard library yang sudah ada dan tersedia semenjak diinstall dan bersifat gratis. Fungsi standard library ini adalah untuk membantu dalam melakukan operasi algoritma pemrograman. Salah satu contoh standard library python adalah datetime yang berfungsi untuk menampilkan waktu, tanggal, bulan dan tahun. Selain datetime, masih terdapat library-library lain yang bisa kita gunakan seperti tkinter untuk GUI, html, JSON dsb untuk web dan web server. Seluruh kumpulan standard library python dapat ditinjau pada laman website python.org dengan key searchnya adalah The Python Standard Library

Datetime merupakan suatu library yang dibentuk berdasarkan object-object. Karena berbentu object maka setiap datanya dapat dipecah menjadi object-object kecil contohnya data hari, data bulan dan data tahun. Selain itu, data object ini dapat kita akses berdasarkan format tampilan datanya seperti '%A' untuk menampilkan data hari berdasarkan nama-nama hari

library collections merupakan suatu library yang berfungsi sebagai kumpulan-kumpulan data seperti array, list dsb. Dalam library collection ini terdapat istilah "helper" seperti Counter untuk membantu menghitung jumlah data/member dalam collections
"""

# standar library untuk menunjukkan keterangan waktu
import datetime

data_waktu = datetime.datetime.now() # ini merupakan object dari datetime yang diambil dari fromtimestamp
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}") # karena merupakan object maka bisa diakses beberapa object di dalamnya salah satunya adalah data tahun.
print(f"hari : {data_waktu.strftime('%A')}")

# standard library untuk menghitung jumlah karakter yang muncul dalam suatu data
from collections import Counter

data = ["a","b","c","d","a","d","a"]

# cara konvensional dalam menghitung jumlah karakter yang muncul dalam suatu kumpulan data
# count = 0
# for i in data :
#     if i == "a" :
#         count += 1

# print(count)

data_count = Counter(data) # fungsi counter ini menghitung setiap jumlah karakter yang muncul dalam satu data dan dihimpun dalam dictionary dari setiap karakternya sebagai key dan valuenya sebagai jumlah karaketer tersebut muncul dalam suatu data
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

# standard library untuk baca teks
import io # merupakan standard library python tentang input output file

file = io.open("Episode-58_Menggunakan-Standard-Library/file_text.txt", "r")
# dalam sintaks di atas penjelasannya sebagai berikut. Variabel file merupakan variabel yang berfungsi sebagai rujukan terhadap suatu file yaitu namanya adalah file_text.txt dimana harus mendefinisikan alamat file itu berada, io.open merupakan suatu module dalam library io untuk dapat mengakses file yang dimana filenya adalah file_text.txt dan "r" merupakan mode dalam mengakses file yang disebut sebagai "read" jadi hanya bisa membaca saja tanpa bisa mengubah isi dari file tersebut

print(file.read()) # file.read() merupakan suatu fungsi dalam library io untuk membaca isi dari file