"""
Default Argument Fungsi
-> Suatu cara dalam mengantisipasi inputan argumen kosong pada suatu fungsi sehingga apabila suatu fungsi yang memerlukan argument diinputkan kosong (tanpa argument) dapat menggunakan default argument agar tidak terjadi error
-> Default argument dapat dibuat dengan melakukan assign pada argument yang terdapat pada "()" dalam fungsi dengan memberi inisiasi nilai sebagai nilai defaultnya apabila tidak ada argument yang diberikan
-> Apabila argument diinputkan, maka inputan argument tersebut akan menimpa default argument sehingga argument yang digunakan adalah argument yang diinputkan
-> Dalam fungsi juga urutan argument sangat diperhatikan dimana apabila kita salah mendefinisikan argument terhadap urutannya akan menghasilkan error dalam pengoperasian dalam fungsinya. Sehingga untuk mengantisipasi kejadian tersebut, dalam penggunaan argument dapat kita assign terhadap argumentnya sehingga dapat kita panggil lalu kita assign value argumetnya yang dimana hal ini tidak memedulikan urutan pada argument fungsi dan juga meminimalisir terjadinya salah input value argument
-> Dengan adanya default argumen, kita dapat mengakses salah satu argument spesifik yang ingin kita ubah tanpa harus kita inputkan argument-argument lainnya
"""

'''Default argument'''

"""
def fungsi(argument):
def fungsi(argument = nilai defaultnya): # nilai default berfungsi sebagai nilai inputan statis yang dimana apabila fungsi tidak diberikan argument
"""

# contoh 1
def say_hello(nama = "Ganteng") :
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")

say_hello("Ucup") # Output : Hallo Ucup
# say_hello() # akan menghasilkan TypeError dimana harusnya fungsi say_hello() membutuhkan satu argument dalam operasinya. Nah disinilah peran default argument sebagai solusinya

# setelah adanya default argument (nama = "Ganteng")
say_hello() # Output : Hallo Ganteng

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?") :
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Dudung", "Hai Ganteeeng") # hai Dudung, Hai Ganteeng
sapa_dia("Otong") # hai Otong, Apa kabar?

# contoh 3
def hitung_pangkat(angka, pangkat) :
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)

# contoh 4
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4) :
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3 = 10)) # melakukan perubahan hanya pada parameter input3 sehingga parameter lain tidak perlu dipanggil
