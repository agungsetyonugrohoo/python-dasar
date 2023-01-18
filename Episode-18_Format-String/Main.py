"""
Format String

-> Untuk memberikan kebebasan dalam menuliskan variabel dalam sebuah string sehingga memudahkan penulisan dan mengeditnya

Note :
- operator ':d' pada format string {} berfungsi untuk menunjukkan bahwa angka tersebut merupakan bilangan bulat dan bisanya untuk variabel bertipe data integer
- operator ':,' pada format string {} berfungsi untuk menunjukkan nilai ordo ribuan dengan memisahkannya dengan koma
- operator '.nf' pada format string {} berfungsi untuk membatasi nilai angka dibelakang koma sebanyak n dan f menunjukkan bahwa itu float atau desimal
- operator 'mn.' pada format string {} berfungsi untuk mengatur panjang angka (n) sehingga terdapat angka kosong yang mungkin menempati bagian depan angka apabila angka yang ditampilkan kurang panjang dari n yang ditentukan. m berfungsi untuk mengatur angka kosong apa yang diisikan untuk memenuhi panjang angka yang telah ditentukan
- operator ':+n' pada format string {} berfungsi untuk menampilkan simbol plus minus di depan angka yang ditampilkan. format ini juga bergantung pada tipe data (n) yang digunakan dimana apabila integer menggunakan +d dan float menggunakan +f
- operator '.n%' pada format string {} berfungsi untuk dapat menampilkan nilai angka dalam persen (%) dengan n untuk membatasi jumlah angka dibelakang koma persennya
- dalam format string {} dapat dilakukan operasi lain seperti aritmatika dan juga melakukan format dalam penulisannya
"""

# contoh generic

# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder {}
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)