"""
List => Suatu variabel yang menampung kumpulan data
Biasanya dinotasikan dengan "[]"
Tipe data List ini bisa diisi oleh tipe data lainnya dan tidak hanya satu tipe data saja bisa jadi gabungan dari beberapa tipe data seperti numbers, string dan boolean
Untuk dapat menampilkan hasil data range, perlu dilakukan casting dari range menjadi list agar dapat dicetak dalam bentuk kumpulan angka
"""

# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range) # menghasilkan bukan kumpulan range dari 0 sampai 10 akan tetapi range(0,10) karena tidak dikumpul nilainya dalam list
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)] # nilai i untuk i di dalam range 0 hingga 10, tolong kuadratkan
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] # nilai i untuk i di dalam range 0 hingga 10 yang memenuhi kondisi jika i bukan 5, tolong masukkan dalam list
print(list_pake_for_if)

# membuat list pake for if untuk bilangan genap
list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)

# membuat list pake for if untuk bilangan ganjil
list_pake_for_if = [i**2 for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if)

