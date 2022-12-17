"""
Operator String menggunakan Method

-> upper() = untuk menjadikan string dalam huruf kapital
-> lower() = untuk menjadikan string dalam huruf kecil
-> islower() = untuk mengecek apakah stringnya dibentuk dalam huruf kecil atau tidak
-> isupper() = untuk mengecek apakah stringnya dibentuk dalam huruf besar atau tidak
-> isalpha() = untuk mengecek apakah stringnya dibentuk dalam huruf atau tidak
-> isalnum() = untuk mengecek apakah stringnya dibentuk dalam huruf dan angka atau tidak
-> isspace() = untuk mengecek apakah stringnya kosong atau dibentuk dalam spasi, tab atau newline atau tidak
-> istitle() = untuk mengecek apakah setiap kata yang dibentuk dimulai dari huruf besar atau tidak dan atau mengandung unique characters
-> startswith() = untuk mengecek suatu kata dalam suatu string di bagian kata awal secara case sensitive
-> endswith() = untuk mengecek suatu kata dalam suatu string di bagian akhir secara case sensitive
-> join() = untuk menggabungkan kata-kata dari list dengan suatu penggabungan kata tertentu
-> split = untuk memisahkan kata-kata dari string dengan suatu kata pemisah tertentu dan menghasilkan list
-> rjust = untuk mengatur rata kanan dari suatu string berdasarkan jumlah karakter yang ditentukan dan karakter penambahnya
-> ljust = untuk mengatur rata kiri dari suatu string berdasarkan jumlah karakter yang ditentukan dan karakter penambahnya
-> center = untuk mengatur rata tengah dari suatu string berdasarkan jumlah karakter yang ditentukan dan karakter penambahnya
-> strip : untuk menghilangkan karakter tertentu yang berada dalam string

"""

## mengubah case (uppercase atau lowercase) dari string

# mengubah semua ke uppercase

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# mengubah semua ke lowercase
alay = "aKu KeCe AbieezZzZZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan menggunakan isX method

# contoh pengecekan lower case
salam = "sist" # hasilnya bool
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))

# contoh pengecekan upper case
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek semuanya angka
# isspace() <-- untuk mengecek apakah string kosong yang isinya spasi, tab, newline \n
# istitle() <-- untuk mengecek apakah kata dimulai dari huruf besar

# istitle()
judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu'] # ini adalah list yang merupakan suatu kumpulan data
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")

