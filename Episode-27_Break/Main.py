"""
Break => suaru aksi yang menyebabkan berakhirnya suatu operasi perulangan sehingga tidak mengeksekusi perintah selanjutnya dan langsung keluar atau mengakhiri dari suatu operasi perulangan

Fungsi break ini dapat memecahkan kondisi infinite loop hingga suatu kondisi yang terpenuhi oleh break
"""

# contoh pertama
angka = 0

while angka < 5 :
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3 :
        print("nice!")
        break

    print("wassup!")

print("cukuuup finish!")

# contoh kedua
data_int = int(input("hitung sampai = ")) # membuat batasan nilai perulangan

angka = 0

while True :
    angka += 1
    print(f"count = {angka}")

    if angka == data_int :
        print("nice!")
        break


    print("wassup!")

print("cukuuup finish!")