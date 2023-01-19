"""
Global dan Local Scope

- Variabel global berdasarkan namanya yaitu global merupakan sebuah variabel yang dapat diakses dimana saja

- Variabel local berdasarkan namanya yaitu local merupakan sebuah variabel yang hanya dapat diakses di area operasi tertentu saja seperti dalam fungsi sehingga scopenya dibatasi

Perbedaan variabel global dan variabel local terletak dimana variabel tersebut dideklarasikan dimana variabel global di deklarasikan di luar operasi lain atau tidak dalam operasi tertentu (fungsi) sehingga dapat diakses dimana saja bahkan di dalam area tertentu seperti fungsi sedangkan variabel local hanya di definisikan di area spesifik tertentu saja sehingga akses variabel hanya berlaku di area spesifik tersebut

Dalam penggunaan variabel global, jangan pernah mendeklarasikan variabel global setelah variabel global tersebut dipanggil atau digunakan. Hal ini dikarenakan python merupakan bahasa interpreted language dan juga sekuensial dari atas ke bawah dalam melakukan operasinya sehingga apabila kita memanggil variabel global sebelum variabel tsb dideklarasikan maka akan menghasilkan error (NameError) yang dimana variabel tsb belum di deklarasikan (not found)

Dalam penggunaan variabel global juga, kita tidak mengubah nilainya sesuka hati kita contohnya mengubah nilai global melalui fungsi dengan variabel local. Alhasil, variabel perubahan yang diubah nilainya hanya tersimpan di variabel local saja tidak mempengaruhi variabel global. Contoh :
var_global = 0
def ubah_var_global(var_local) :
    var_global = var_local # tidak akan mengubah value dari var_global

sehingga solusinya adalah dengan mendeklarasikan variabel global atau mengacknowledge variabel global dalam suatu area operasi spesifik tertentu yang memperbolehkan mengubah nilai var_global dengan cara mendeklarasikan var_global dalam fungsi menjadi global var_global seperti :
var_global = 0
def ubah_var_global(var_local) :
    global var_global
    var_global = var_local # mengakses var_global secara global sehingga bisa diubah valuenya

Note : area spesifik yang tidak bisa mengakses variabel global seperti mengubahnya yaitu hanya dalam fungsi dan variabel local dalam fungsi tidak dapat di akses di luar fungsi. Untuk dapat diberikan askses dalam mengubah variabel global dalam suatu fungsi diperlukan deklarasi global terhadap variabel global tersebut di dalam fungsi

Note : variabel global dapat diakses dan diubah di dalam for dan if serta variabel local yang dibentuk dalam for dan if masih bisa diakses di luar for dan if
"""
## Global dan Local Scope

nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi1() :
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5) :
    print(f"loop {i} - {nama_global}")

# percabangan
if True :
    print(f"if menampilkan {nama_global}")

## Variabel Local Scope
def fungsi2() :
    nama_local = "Ucup" # <- ini variabel local scope

fungsi2()
# print(nama_local) # NameError karena nama_local is not defined

## Contoh 1: penggunaan akses variabel
def say_otong() :
    print(f"Hello {nama}")

nama = "Otong"
say_otong()
# nama = "Otong" akan error dikarenakan variabel global dipanggil sebelum dideklarasikan

## contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru) :
    global angka # fungsi ini mendapat akses merubah angka
    global name # fungsi ini mendapat akses merubah name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka, name}")
ubah(10, "Otong")
print(f"Sesudah {angka, name}")

## contoh 3:
angka = 0

for i in range(0, 5) :
    angka += i # var global masih bisa di akses dalam for
    angka_dummy = 0

print(angka)
print(angka_dummy) # var local dalam for masih bisa diakses dari luar for

if True :
    angka = 10 # var global masih bisa di akses dalam if
    angka_dummy = 10

print(angka)
print(angka_dummy) # var local dalam for masih bisa diakses dari luar if