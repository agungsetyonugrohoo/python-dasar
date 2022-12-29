"""
Teknik menduplikat list

Pada teknik menduplikat list dengan cara assignment (b = a), apabila kita mengubah salah satu data dari satu list (contoh a) maka perubahannya juga akan diterima pada list lainnya (list b). Hal ini dikarenakan data yang tersimpan pada list a dan list b memiliki address memori yang sama sehingga apabila salah satunya berubah maka yang lainnya juga akan berubah.

Dalam melakukan duplikasi dengan assignment operator, maka disebut sebagai pass by reference. Hal ini dikarenakan, variabel yang terassignment sebenarnya tidak memiliki data tersebut akan tetapi berperan sebagai nama alias dari data yang ingin di duplikasi. Oleh karena itu, addressnya akan sama

Untuk menduplikat list dengan benar maka diperlukan salah satu method dalam list yaitu a.copy(), dimana a merupakan list data yang ingin dicopy ke dalam suatu variabel tertentu
"""

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dengan a.copy()")
# simpan hasil copy list a ke dalam variabel c
c = a.copy() # full duplikat / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data indeks-0 pada list c")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data indeks-1 pada list c")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


