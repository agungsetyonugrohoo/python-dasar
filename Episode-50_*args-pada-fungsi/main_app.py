'''
*args

*args merupakan suatu jenis parameter exclusive pada fungsi yang memiliki tipe data seperti list namun penggunaannya seperti tipe data parameter biasanya dalam penggunaannya. Contoh :

def fungsi_dengan_args(*args) :
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_dengan_args("dadang", 120, 120)

Pada contoh di atas, parameter *args dapat diakses seperti list dan dapat digunakan seperti pada parameter biasa

Secara umum, fungsi *args adalah untuk mensimplifikasi deklarasi jumlah input parameter dalam suatu fungsi yang memerlukan inputan yang banyak dan tidak ada batas untuk jumlah inputan parameter untuk *args. Selain itu, penggunaan *args juga dapat digunakan dengan kata lain selain args contohnya "*data" dsb. Kemudian, *args merupakan tipe data tuple sehingga bisa dilakukan iterasi (iterable)
'''

# memasukkan data/argument

def fungsi(nama, tinggi, berat) :
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

print("ucup", 170, 40)

def fungsi(data_list) :
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong", 100, 120])

# kenalan dengan *args

def fungsi(*args) :
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung", 120, 120)

# studi kasus

def tambah(*data) :
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10, 5, 15)
print(f"hasil = {hasil}")
