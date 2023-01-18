"""
Nested List (List Bersarang) => merupakan teknik untuk membuat suatu variabel list yang berisikan list

Nested list ini sangat berfungsi untuk mengumpulkan data-data yang yang berisi kumpulan-kumpulan data sendiri-sendiri sehingga mudah untuk terorganisir

Permasalahan Nested List dalam melakukan duplikat dengan method list yaitu .copy() menghasilkan data list yang ingin diduplikasi dalam variabel baru tidak tercopy sehingga masih memiliki address memori yang sama alias data list yang tersimpan dalam list lama yang ingin di duplikasi tidak tercopy melainkan data list bagian luarnya (list yang menampung data list) saja. Sehingga apabila data list dalam list diubah maka perubahannya akan mempengaruhi variabel data list dalam list yang baru karena data list yang berada di dalam list masih di dalam satu reference.
"""

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,data_list_biasa,6,7]

print(f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["ucup",25,"Laki-laki"]
peserta_1 = ["otong",10,"Laki-laki"]
peserta_2 = ["dedeh",50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta :
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# dengan reference

list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta_0[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")
