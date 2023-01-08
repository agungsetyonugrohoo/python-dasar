"""
Fungsi dikenal sebagai beberapa hal diantaranya :
- Function
- Method
- Subroutine
- Routine

Alasan munculnya fungsi adalah untuk meminimalisir kode yang berulang-ulang dalam melakukan operasi yang sama (Repeated Code) seperti :
-> b = 1, c = 2
-> a = b + c
-> print(a)
-> d = 3
-> e = 4
-> f = d + e
-> print(f)
Operasi penjumlahan yang dilakukan oleh a dan f adalah sama yaitu menjumlahkan kedua nilai. Hal inilah yang menyebabkan suatu sintaks pemrograman menjadi sangat panjang sehingga perlu dilakukan efisiensi yaitu dengan cara membuat fungsi tambah.
Cara membuat fungsi sangatlah sederhana dengan menggunakan sintaks def yang diikuti oleh nama fungsinya dan juga parameternya yang ditampung dalam "()" sehingga bisa dituliskan sebagai berikut -> def NamaFungsi(parameter) :
Dalam fungsi kita dapat melakukan banyak instruksi dan operasi yang cukup kompleks sehingga dapat memudahkan pekerjaan dan mengefisiensikan penulisan kode
Dengan adanya fungsi, apabila terdapat operasi yang perlu diubah dalam suatu penulisan kode yang dimana dilakukan secara berulang kali, kita dapat mengubah hanya fungsinya saja sehingga ketika pemanggilan fungsi operasinya pun akan berubah

Aturan Pembuatan fungsi :
- Dalam membuat fungsi di Python (Interpreted Languange), fungsi harus didefinisikan terlebih dahulu sebelum dipanggil
"""

'''Membuat fungsi'''
def hello_world() :
    '''fungsi menampilkan hello world'''
    print("hello world")
    print("Kepada Ucup Surucup")
    print("Dan juga kepada Otong Surotong")

'''
cara dibawah ini untuk menampilkan hello world ke terminal:
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
'''

# cara lain dengan menggunakan fungsi hello_world()
hello_world()
hello_world()

# fungsi() -> akan error "fungsi is not defined" dikarenakan fungsi dipanggil sebelum didefinsikan

def fungsi():
    '''pemanggilan fungsi harus setelah dibuat'''
    print("Ini adalah fungsi")

fungsi() # ini baru benar untuk pemanggilan fungsi