"""
Width and Multiline

- kutip triplets : memberikan kebebasan untuk penulisan enter dan spasi jadi lebih mudah untuk memposisikan tanpa harus menggunakan newline (\n)
- operator ':>n' pada format string berfungsi untuk mengatur rata kanan dari suatu string dengan membatasinya berdasarkan jumalh karakter n tertentu. sehingga apabila terdapat string yang memiliki jumlah karakter < n, maka akan ditambahkan spasi di depan string tersebut untuk menyesuaikan jumlah karakternya menjadi n tertentu sehingga bisa rata kanan dan apabila melebihi akan tetap dimasukkan namun tidak menyesuaikan rata kanan
"""

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, data tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ndata tinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup Surucup"
data_tinggi = 105.17
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
