"""
Operasi List (Manipulasi data List)
Data dalam list diurutkan berdasarkan index yang dimulai dari 0 hingga paling akhir (sekian). Untuk dapat memperoleh index paling akhir dapat digunakan index -1 untuk merujuk pada index paling akhir dan selalu dikurangi 1 (-2,-3,-4,...) untuk dapat memperoleh urutan dari akhir ke awal
Untuk mengambil data dari sebuah list berdasarkan index maka dapat memanggil nama list tersebut diikuti oleh indexnya
Manipulasi data list => suatu aksi / operasi untuk mengubah data dari suatu list
Untuk menambahkan data dalam suatu list sesuai posisi tertentu dapat menggunakan method => data.insert(posisi,item), posisi menunjukkan letak awal posisi untuk menambahkan data baru dan item merupakan item yang ditambahkan mulai dari posisi tersebut
Untuk menambahkan data di akhir posisi suatu list dapat menggunakan method => data.append(item), dimana item merupakan data yang ingin ditambahkan di bagian akhir dari suatu list
Untuk menggabung data list pertama dengan data list kedua (atau lainnya) dapat menggunakan method => data.extend(data_yang_ditambah), dimana data merujuk pada tempat data yang menjadi lokasi penambahan dari data yang ditambah dan data yang ditambah merupakan kumpulan data yang akan ditambahkan atau dimasukkan dalam list data
Untuk mengubah suatu data dalam list dengan cara memanggil data berdasarkan data index yang ingin diubah lalu assign suatu nilai data yang baru untuk ditimpa pada data yang lama
Untuk menghapus / menghilangkan suatu data dalam list dapat menggunakan method => data.remove(nilai_item), dimana nilai item merujuk pada isi dari item pada list bukan indexnya
Untuk menghapus / menhilangkan data paling akhir dalam suatu list dapat menggunakan method => data.pop() dimana method ini pasti akan menghapus data index paling akhir
"""

# index 0(-3)   1(-2)       2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah item di akhir list
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

# menambah list dengan list (menggabungkan list)
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data ke-2 (otong) menjadi michael
data[2] = "Michael" # ditimpa
print(f"data rubah = \n{data}")

# meremove data
data.remove("Ujang")
print(f"data remove = \n{data}")
# data.remove("usep") akan error karena huruf harus sesuai yaitu "Usep"

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)