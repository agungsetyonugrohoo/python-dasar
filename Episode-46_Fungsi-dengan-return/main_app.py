"""
Fungsi dengan kembalian (return value)
-> Fungsi dengan kembalian adalah suatu skema sama seperti fungsi biasa akan tetapi memiliki output yang dapat disimpan atau diassign dalam suatu variabel penampung

Struktur fungsi dengan kembalian
def kuadrat(x) :
    hasil = input ** 2
    return hasil # inilah yang disebut return value yang menjadi output dalam fungsi

y = kuadrat(4) # hasil return value akan disimpan pada variabel y yang dimana hasilnya adalah hasil kuadrat dari 4

Sehingga secara sederhana fungsi dengan kembalian dapat dijelaskan sebagai berikut :
Input -> Fungsi -> Output

Fungsi dengan kembalian ini juga dapat mengembalikan (return) beberapa nilai dan dapat disimpan setiap isi kembaliannya dengan melakukan assign pada setiap return valuenya yang dimana hasil kembaliannya akan selalu terurut pada setiap assignment variabelnya
"""

'''Fungsi dengan kembalian'''

"""
Template fungsi dengan kembalian
def nama_fungsi(argument) :
    badan fungsi
    return output
"""

# fungsi kuadrat

def kuadrat(input_angka) :
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1, angka_2) :
    return angka_1 + angka_2

a = fungsi_tambah(10, 8)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1, angka_2) :
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 /  angka_2

    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(9,5)
# dalam assignment di atas, setiap variabel mewakili setiap hasil return fungsi secara berurutan sesuai urutan return value dari fungsi operasi_matematika diantaranya k untuk tambah, l untuk kurang, m untuk kali dan n untuk bagi

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")