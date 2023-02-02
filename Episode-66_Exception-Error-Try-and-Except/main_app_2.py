# contoh membuat exception
from numbers import Number # library untuk memberitahu bahwa variabel digolongkan sebagai Number atau bukan

'''
isinstance(a,Number) berfungsi untuk mengecek apakah input a merupakan number atau tidak

fungsi raise untuk menampilkan pesan error yang kita inginkan berdasarkan aturan yang kita buat sebelumnya
'''

def tambah(a,b) :
    if  not isinstance(a,Number) or not isinstance(b,Number) :
        raise "input pertama harus angka" # akan muncul apabila salah satu atau kedua inputan bukan angka sebagai pesan error
    return a + b

print(tambah(5,6))
# print(tambah(5,"v")) # akan error dikarenakan inputan kedua bukan angka

# menangkap berdasarkan tipe exceptionnya
# angka = 0
# try :
#     hasil = 10/angka
# except Exception as error_message :
#     print(error_message) # untuk menampilkan error apa yang terjadi. Dengan adanya Exception ini, kita bisa juga mengklasifikasikan error apa saja yang bisa terjadi seperti ZeroDivisionError, SyntaxError dsb

angka = 0
try :
    hasil = 10/angka
except ZeroDivisionError as error_message :
    print(error_message) # menampilkan error apabila errornya ZeroDivisionError