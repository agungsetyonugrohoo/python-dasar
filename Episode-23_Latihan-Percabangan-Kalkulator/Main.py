# Latihan

"""
kalkulator sederhana
1. ambil data user -> angka 1, angka 2, operator
2. percabangan berdasarkan pilihan operator (+, -, x, /) dan lakukan operasi aritmatika berdasarkan pilihan operator
3. hasilnya & tampilkan
"""

print(20*'=')
print("Kalkulator Sederhana")
print(20*'=' + "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukkan angka 2 = "))

# percabangannya (rules condition)
if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil:.2f}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil:.2f}")
elif operator == "x" or operator == "*" :
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil:.2f}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil:.2f}")
else :
    print("masukkan yang bener dong!, aku pusying")

print("Akhir dari program, terima gajih!")
