## Tutorial membaca file eksternal

print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt", mode="r") # untuk read
# file = open("data.txt", mode="w") # untuk write
'''
Untuk membuka suatu file, dapat menggunakan open("file", mode="r")

dimana open berfungsi untuk membukan file dengan parameternya :
- file : merupakan file yang ingin dibuka
- mode : merupakan opsi pembukaan file apakah di read/write untuk read pakainya "r" dan write pakainya "w"

apabila berhasil dibuka maka ketika diprint variabel filenya akan muncul seperti berikut "<_io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>" yang menandakan file berhasil dibuka.

apabila menggunakan mode="w" pada file yang sudah ada isinya dan tidak mengisi apapun, maka sebenarnya yang dilakukan adalah membuka file tersebut lalu menimpa file tersebut dengan sesuatu yang diisikan namun apabila tidak ada yang diisikan berarti jadinya kosong filenya
'''

# cara mengetahui suatu file bisa dibaca atau ditulis
print(f"status read : {file.readable()}") # untuk mengetahui bahwa file bisa dibaca (read)
print(f"status write : {file.writable()}") # untuk mengetahui bahwa file bisa ditulis (write)

# print(file) # untuk mengetahui kondisi file sudah terbuka apa belom

## baca seluruh file
# print(file.read()) # untuk membaca isi konten dalam file

## baca per baris
# print(file.readline()) # baca baris pertama
# print(file.readline()) # membaca baris kedua dan melakukan enter karena pada fungsi print sudah ada otomatis enter
print(file.readline(),end="") # untuk menghilangkan fungsi enter (\n) dengan menggantinya dengan string kosong ""
print(file.readline(),end="")

## baca semua baris sebagai list
# print(file.readlines())

# setiap setelah open file jangan lupa harus di close agar bisa dibuka kembali setelahnya
print(f"apakah file sudah di close : {file.closed}") # untuk mengetahui status file sudah di close apa belom

file.close() # untuk close file
print(f"apakah file sudah di close : {file.closed}")

## salah satu teknik membuka file di python
print("\n",3*"=", " Membaca file txt dengan with ", 3*"=")

'''
metode buka file dengan with open ini sama seperti open akan tetapi dengan adanya with ini akan langsung tertutup apabila sudah tidak beroperasi di dalam file tersebut lagi. dengan adanya with ini jadinya tidak ribet untuk open dan close file karena bisa langsung tidak seperti teknik open
'''
with open("data.txt",mode="r") as file :
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close : {file.closed}")

print(f"apakah file sudah di close : {file.closed}")