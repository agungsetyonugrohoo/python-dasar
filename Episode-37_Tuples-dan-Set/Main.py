"""
Tuples dan Set

- Tuples dan set merupakan bagian dari data collection sama seperti list yang juga bagian dari data collection
- Tuples merupakan salah satu tipe variabel data collection dalam python yang sama seperti list yaitu berfungsi untuk menampung data akan tetapi karakteristiknya tidak bisa mengubah data-data yang sudah tersimpan dalam variabel tuples sehingga kita tidak dapat mengubahnya lagi apabila sudah tersimpan
- Tuples juga tidak bisa kita gunakan method penambahan data seperti dalam list yaitu append() untuk menambahkan data di belakang urutan indeksnya
- Tuples ini berfungsi untuk representatif data kuantitatif yang bersifat strict atau tidak bisa diubah atas kehendak tertentu. Hal ini dimaksudkan seperti perhitungan matematika layaknya 1+1 yang menghasilkan 2 sehingga tidak bisa kita ubah menjadi hasilnya 3 dsb sehingga hasil data yang tersimpan dalam tuples tidak bisa kita ubah apapun

- Sets adalah suatu tipe variabel data collection yang berfungsi untuk menampung data akan tetapi dalam penggunaannya tidak memiliki indeks
- Sets memiliki keterbatasan dimana data dalam sets tidak bisa diambil melalui indexing yang dimana akan menghasilkan error. Akan tetapi untuk fungsi lainnya seperti list yaitu append, count dsb masih bisa
- Sets biasanya diperuntukkan untuk kumpulan angka atau himpunan angka dan biasanya untuk data yang tidak terpaku dengan index atau urutan datanya
"""

# list
data_list = [10,2,4,3,2] # menggunakan kurung siku
print(data_list)

# tuples
data_tuples = (7,8,9,10) # menggunakan kurung
print(data_tuples)
print(data_tuples[1]) # mencetak data tuples dengan indeks ke-1 yaitu 8

# tidak bisa mengubah data yang berada di dalam tuples
# data_tuples[1] = "ucup" # akan menghasilkan error TypeError dimana data variabel tuple tidak support dengan assignment
# tidak bisa menambahkan data baru yang berada di dalam tuples
# data_tuples.append(1) # akan menghasilkan error AttributeError yang dimana menyatakan bahwa variabel tuple tidak memiliki attribute append

# sets (himpunan)
data_sets = {10,4,3,2,4,7,6,5} # menggunaka kurung kurawal
print(data_sets)

# tidak bisa mengambil data secara indexing
# print(data_sets[0]) # akan menghasilkan error TypeError yang menyatakan bahwa variabel sets tidak bersifat subscriptable