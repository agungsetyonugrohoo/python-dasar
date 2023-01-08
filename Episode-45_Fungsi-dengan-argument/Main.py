"""
Fungsi dengan argument (input)
Cara membuat fungsi terdiri dari beberapa hal diantaranya :
def -> definition, untuk mendefinisikan sebuah sintaks fungsi
NamaFungsi -> nama fungsi yang akan disematkan atau akan dipanggil dalam menjalankan fungsi
"(argument/parameter/input)" -> parameter/argument/input, suatu variabel yang dituju untuk dapat dioperasikan dalam badan fungsi
Badan Fungsi -> sekumpulan instruksi yang dapat mengolah parameter/argument/input untuk dapat dioperasikan sehingga menghasilkan sesuatu
Sehingg secara keseluruhan, struktur fungsi adalah sebagai berikut :
def NamaFungsi(parameter/argument/input) :
    Badan Fungsi

Tips dalam membuat fungsi :
- Usahakan nama fungsi dan argumen dapat menjelaskan tujuan dari fungsi tersebut dan keguanaan dari argumen dalam fungsi tersebut
"""

'''Fungsi dengan argument (input)'''

'''
template fungsi :
def nama_fungsi(argument):
    Badan fungsi
'''

def hello_world(nama) :
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}") # variable nama akan di pass reference dari argument nama dalam fungsi hello_world

# memanggil fungsi hello_world() dengan argument
hello_world("ucup")
hello_world("Asyep")

# program fungsi penjumlahan (tambah)
def tambah(angka_1, angka_2) :
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5) # 1 + 5 = 6
tambah(100000,1)

def say_hi(list_peserta) :
    '''fungsi say hi'''
    # list_peserta[1] = "Asyep" # akan mengubah data aslinya yang menandakan argument yang dimasukkan dalam pemanggilan fungsi sama saja dengan argument yang diinisasikan pada fungsi
    data_peserta = list_peserta.copy() # menduplikat data peserta
    for peserta in data_peserta :
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup", "Otong", "Dudung"]

say_hi(anggota_boyband) # memasukkan argument anggota_boyband akan dikenali fungsi sebagai list_peserta sehingga sama saja

print(anggota_boyband[1])