"""
Import statement

Import merupakan suatu jalur penghubung dua source file yang berfungsi untuk mengambil program dari file external .py ke dalam program file .py yang lain

Untuk menghubungkan satu file program dengan file program yang lain, struktur import digunakan sebagai berikut :
import file_yang_ingin_diimport
dimana file_yang_ingin_diimport merupakan tempat file resource yang berisi kumpulan program yang banyak yang ingin kita terapkan di program baru kita saat ini

Untuk mengimport data dari file external diperlukan namespace. Namespace ini berfungsi untuk memberikan akses data yang ingin diambil itu berasal dari resource file yang mana sehingga apabila suatu variabel data memiliki nama variabel yang sama terhadap beberapa resource file maka kita dapat membedakannya dengan namespace ini. Namespace ini merujuk pada file external resource.

Penggunaan namespace ini dengan cara :
file_external.data_yang_ingin_diimport
"""

# import

# fungsinya adalah untuk mengambil program dari file external .py

# 1. untuk menyambung program dari external dan menjalankannya
import program_print
import program_ucup

# 2. import dengan data
import variable
import kucuy

# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4, 5)
print(hasil)