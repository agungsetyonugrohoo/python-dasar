"""
Latihan Fungsi

"""

import os

# Program menghitung luas dan keliling persegi panjang

# # Membuat header program
# os.system("cls") # clear screen untuk windows
# # os.system("clear") # clear screen untuk linux dan mac os
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-' * 40 : ^40}")

# # Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # Program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhtiungan luas = {LUAS}")
# print(f"hasil perhtiungan keliling = {KELILING}")

def header() :
    '''fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-' * 40 : ^40}")

def input_user() :
    '''fungsi input dari user'''
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))

    return lebar,panjang

def hitung_luas(lebar, panjang) :
    '''fungsi luas'''
    return lebar * panjang

def hitung_keliling(lebar, panjang) :
    '''fungsi keliling'''
    return 2 * (lebar + panjang)

def display(message, value) :
    '''fungsi display'''
    print(f"hasil perhtiungan {message} = {value}")

# Program utamanya
while True :
    header()

    opsi = int(input("pilih 1 untuk luas, 2 untuk keliling dan 3 untuk keduanya : "))

    LEBAR, PANJANG = input_user()

    if opsi == 1 :
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("luas", LUAS)
    
    elif opsi == 2 :
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)

    elif opsi == 3 :
        LUAS = hitung_luas(LEBAR, PANJANG)
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("luas", LUAS)
        display("keliling", KELILING)
        
    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n" :
        break

print("Program selesai, terima kasih")