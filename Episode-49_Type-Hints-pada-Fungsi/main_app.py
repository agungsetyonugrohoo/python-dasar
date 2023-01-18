"""
Type hints untuk Fungsi

Secara default, parameter dalam fungsi merupakan suatu tipe data "Any" sehingga bisa diinputkan berbagai macam tipe data. Hal inilah yang akan menjadi suatu permasalahan ketikan fungsi tersebut dispesifikkan untuk tugas tertentu yang dimana hanya membutuhkan angka saja contohnya fungsi kuadrat. Apabila diinputkan string pada parameternya maka akan menghasilkan error karena string tidak bisa dikuadratkan

Type hints => untuk memberikan informasi mengenai tipe data parameter fungsi yang harus diinputkan pada suatu fungsi

Struktur Type Hints : pada argument / parameter fungsi dideklarasikan tipe datanya seperti def fungsi_dengan_hints(argument:int) penulisan argument:int itulah yang disebut dengan type hints yang dimana mendelegasikan tipe data int pada parameter argument

Dengan menggunakan type hints, apabila kita melakukan hover mouse pada fungsi yang kita panggil maka akan muncul informasi mengenai tipe data parameter yang digunakan

Untuk informasi yang muncul selain type hints, yaitu "-> Any" itu menunjukkan tipe data keluaran (output) dari fungsi. Namun apabila pada deklarasi fungsi kita juga menentukan tipe data outputnya dengan cara def fungsi_dengan_hints(argument:int) -> int : yang dimana "-> int" merupakan pendelegasian tipe data pada output, maka informasi ketika kita melakukan hover pada fungsi akan menunjukkan tipe data output yang sesuai kita delegasikan

Apabila dalam suatu fungsi yang dibuat tidak didelegasikan adanya output (return value) maka informasi fungsi yang akan diberikan ketika di hover adalah "None" yang menandakan tidak ada keluaran

Kelemahan fungsi pada python ketika menerapkan type hints adalah tetap dijalankannya suatu operasi fungsi walaupun parameter yang diinputkan tidak sesuai sehingga baru ketahuan error ketika sudah dijalankan
"""

# bentuk standar fungsi yang udah kita pelajari tidak bisa menjelaskan jenis tipe data input parameter fungsi yang digunakan

'''
# studi kasus : fungsi dengan inputan seharusnya number diinputkan dengan string
def fungsi(parameter) :
    hasil = parameter ** 2
    print(hasil)

fungsi(1) # 1
fungsi("Ucup") # Error
fungsi(True) # Error
'''

import string

# penggunaan type hints

def sepuluh_pangkat(argument:int) -> int :
    '''FUNGSI DENGAN HINTS'''
    output = 10 ** argument
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string) :
    print(argument)

display("Ucup") # None : tidak memiliki return value

import os

hasil = os.system("clear") # memberikan return value int thd string yang diinputkan sebagai parameter
print(hasil) # 0

# hasil = os.system("cls") # cls : not found (error)
# print(hasil) # 3512