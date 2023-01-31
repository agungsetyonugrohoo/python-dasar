"""
__main__ adalah top level code environment file program pertama yang akan dieksekusi ketika dijalankan.

__name__ akan berubah menjadi __main__ apabila kita panggil sebagai program utama dan akan menjadi nama lain selain main apabila dilakukan import pada file tersebut

fungsi __main__ pada package sebagai penjelasan isi konten dari suatu package. fungsi ini dapat dipanggil dengan memanggil package tersebut pada terminal yaitu python -m package. fungsi ini contohnya dapat digunakan pada python -m venv yang akan menampilkan penjelasan informasi dari package tersebut
"""

# "__" bisa disebut dengan dander atau double underscore

# __main__ adalah top level code environment

# __name__ == "__main__" akan terjadi jika ada di file program utama

## __name__ pada file program utama
print(f"nilai__name__ pada main.py = '{__name__}'")

## __name__ pada file program eksternal
import fungsi

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")

## import package
import package