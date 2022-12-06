# Episode input user
# Tipe data yang diinput akan selalu bertipe data string walaupun yang diinputkan angka seperti 10, 10,78
data = input("masukkan nama: ")
print("data = ", data, ", type = ", type(data))

# jika kita ingin mengambil int, maka
angka = int(input("masukkan angka: "))
angka = float(input("masukkan angka: "))
print("data = ", angka, ", type = ", type(angka))

# bagaimana dengan boolean
biner = bool(int(input('masukkan nilai boolean: ')))
# penerapan bool cukup tricky dimana ketika kita menginputkan true maka akan mengasilkan true, akan tetapi ketika menginputkan false akan tetap menghasilkan true sehingga solusinya perlu dicasting terlebih dahulu inputannya ke int baru ke bool
print("data = ", biner, ", type = ", type(biner))