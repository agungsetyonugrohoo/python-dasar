"""
Looping List dan Enumerate

Looping List => Teknik untuk menelusuri atau mengakses setiap data dalam list.
Teknik Looping List :
- For loop
Teknik for loop dapat digunakan untuk melakukan iterasi data dalam suatu list yang dilakukan dengan dua cara yaitu dengan menggunakan range atau tanpa range.
Dengan menggunakan range, kita harus menentukan indeks terakhirnya dulu yang dimana bisa kita peroleh melalui len(list)
Untuk tanpa range kita bisa menggunakan variabel list yang ingin kita iterasi sebagai objek yang akan kita lakukan iterasi dalam perintah for loopnya

- While loop
Penggunaan while loop dalam melakukan iterasi data pada list dengan cara menentukan terlebih dulu panjang iterasinya yaitu dengan len(list) selanjutnya lakukan iterasi dengan mendasar pada variabel iterasi (example : i) sebagai dasar perulangannya dalam melakukan iterasi sebanyak len(list). Lalu jangan lupa incrementnya dari variabel iterasi (i += 1)

- List comprehension
Teknik list comprehension ini merupakan shortcut untuk dapat melakukan iterasi data dalam list. Caranya dengan menggunakan simbol "[]" yang kemudian melakukan perintah mencetak datanya akan tetapi dengan inline for yang dimana terdapat perulangan namun dapat ditulis dengan satu baris. Perintah cetak tersebut harus terlink dengan operasi inline for tersebut agar data yang telah dilakukan iterasi dapat dicetak
Teknik list comprehension ini juga dapat membuat list baru dari list lama dengan melakukan operasi tertentu pada setiap datanya

- Enumerate
Teknik enumerate akan melakukan iterasi dengan mengambil indeks dan datanya. Dengan teknik ini kita dapat mencetak indeks beserta data yang ada di dalam list tanpa seperti cara loop dan while sekaligus.

"""

# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka :
    print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "diding", "dudung"]

for nama in peserta :
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka) # menentukan panjang list untuk menentukan indeks terakhir dari list

for i in range(panjang) :
    print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nWhile Loop")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)

i = 0
while i < panjang :
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"]
[print(f"data={i}") for i in data ]

# Tambahan list comprehension
angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka] # melakukan operasi kuadrat dari setiap data dalam list angka
print(angka_kuadrat)


# enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index, data in enumerate(data_list) :
    print(f"index = {index}, data = {data}")