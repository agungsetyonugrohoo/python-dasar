"""
Operasi List
count data => untuk mendeteksi frekuensi kemunculan suatu data dalam suatu list (statistik)
count data dilakukan dengan method data.count(item_yang_dicari), dimana item yang dicari merupakan item yang ingin diketahui seberapa sering kemunculannya dalam suatu list
fungsi data.index(item) adalah untuk mengetahui posisi index item dalam suatu list yang berdasarkan urutan indexnya. Dimana item merupakan data yang ingin dicari posisinya dalam suatu list
data.sort() merupakan suatu method untuk mengurutkan data dalam suatu list menjadi terurut dengan defaultnya dari angka terkecil hingga terbesar atau berdasarkan urutan huruf
"""

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Ucup","Otong","Dudung","Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")

# data.index("Usep") akan error karena data tersebut tidak ada di dalam list (errornya adalah ValueError)

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik urutan list => untuk memperoleh urutan dari terbesar ke terkecil
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka}\n{data}")
