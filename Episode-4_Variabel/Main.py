"""
variabel => sebuah variabel yang berperilaku sama seperti di matematika
contoh : x = 2
dimana x adalah variabel dan 2 adalah value

variabel adalah tempat menyimpan data
variabel dapat diisi ulang sehingga nilai awal dapat ditimpa dengan nilai yang baru
penamaan variabel tidak boleh menggunakan angka di awal dan tidak boleh dipisahkan oleh spasi
"""

# menaruh / assignment nilai
a = 10
x = 5
panjang = 1000

# pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 10000000 # ini boleh
nilaiZ = 17.5 # ini boleh

# pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

# assignment indirect
b = a
print("Nilai b = ", b)