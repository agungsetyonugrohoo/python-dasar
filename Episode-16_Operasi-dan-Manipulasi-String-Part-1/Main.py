"""
Operasi dan manipulasi string

=> String Concatenate : operasi penggabungan beberapa string menjadi satu dengan menggunakan operator '+'
=> String length : operasi untuk menghitung jumlah karakter dalam suatu string
=> String indexing : operasi untuk melakukan pengambilan data tertentu dalam suatu string dengan menggunakan [] yang diisikan oleh nilai index yang ingin diambil dan indexing dimulai dari 0


Note :
- string concatenate hanya diperuntukkan untuk variabel string sehingga apabila digabungkan dengan sebuah variabel dengan tipe data lain maka harus diubah ke tipe data string dahulu (casting) atau akan menerima error TypeError
- operator 'in' dalam mengecek suatu string di dalam sebuah string tertentu berfungsi untuk melakukan indexing tiap huruf pada string tertentu kemudian mencocokannya dengan string yang dijadikan sebagai kunci penentu apakah ada atau tidaknya string penentu dalam suatu string tertentu
- string indexing apabila dilakukan pada index minus seperti -1, -2 dsb maka indexing akan dimulai dari paling akhir dari sebuah string menuju paling awal sebuah string dimulai
- string indexing range yaitu suatu operasi dalam mengambil sekumpulan n tertentu. operasi ini dapat dilakukan menggunakan operator index dengan memasukkan nilai indexing dengan tanda ':' yang berarti 'sampai' akan tetapi sampai tersebut tidak mengambil nilai terakhir sampai tersebut. operator sampai ini juga bisa gunakan sebuah operasi tambahan dalam menyeleksi rangenya yaitu seperti '0:10:2' artinya membuat indexing dari 0 hingga 10 dengan increment 2
- operator min dan max string berfungsi untuk menentukan nilai paling kecil dan nilai paling besar pada suatu string berdasarkan nilai ascii codenya
- operator ord berfungsi untuk mengubah suatu karakter menjadi dalam bentuk ascii code
- method string adalah suatu function yang ada di dalam class string yang bisa kita gunakan dengan cara menempelkannya terhadap suatu variabel string
"""

# 1. menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap # mengecek apakah ada huruf d pada nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap # operator not in berfungsi untuk menyatakan bahwa tidak ada huruf tertentu pada suatu string
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
# melakukan pengulangan string sebanyak n kali
print("wk"*10)
print(15*"wk")

# indexing => mengambil data (trimming) dari string
print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0,3] : " + nama_lengkap[0:4]) # ucup
print("index ke-[3,7] : " + nama_lengkap[3:8]) # p D'f
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2]) # uu 'ae

# item paling kecil
print("paling kecil : " + min(nama_lengkap)) # 32

# item paling besar
print("paling besar : " + max(nama_lengkap)) # 117

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))




