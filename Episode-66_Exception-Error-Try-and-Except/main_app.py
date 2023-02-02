"""
Exception, Error, Try and Except

Try and Except merupakan suatu teknik dalam mengendalikan runtime error (exception). Runtime error sendiri merupakan suatu error yang dihasilkan oleh terminal dalam menjalankan program akibat tidak sesuainya perintah yang dijalankan sehingga menghasilkan error. Contohnya pembagian 10/0 menghasilkan ZeroDivisionError dikarenakan 10/0 menghasilkan tidak terdefinisi. Atau juga bisa dikarenakan penulisan yang tidak lengkap pada suatu sintaks pemrograman yang menghasilkan error SyntaxError

Struktur Try and Except :
Try :
    perintah... dimana python disuruh untuk cobain dulu script programnya dan apabila error akan dipass ke except tapi apabila berhasil perintah yang di dalam try lah yang dieksekusi
Except :
    perintah ketika terjadi error...
"""

# contoh menghasilkan runtime error (ZeroDivisionError)
# data_input = int(input("masukkan angka : "))
# hasil = 10/data_input # akan error apabila data_input yang diinputkan merupakan 0
# print(hasil)
# file = open("data.txt","r") # akan error apabila tidak ada file data.txt

# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana untuk menangkap exception
from math import nan

## contoh sederhana
# input_user = int(input("masukkan angka : "))
# hasil = nan

# try :
#     hasil = 10/input_user
# except :
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh di aplikasi
while(True) :
    angka = int(input("masukkan angka pembagi : "))
    try :
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n" :
            break
    except :
        print("pembagi nol, silahkan masukkan input lagi")

print("Akhir dari program 1")

# contoh aplikasi untuk membuat file data.txt
try :
    with open("data.txt", "r") as file :
        print(file.read())
except :
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt", "w", encoding="utf-8") as file :
        file.write("file baru")

print("Akhir dari program 2")
    