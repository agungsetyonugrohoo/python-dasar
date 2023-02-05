"""
Overview Project :
"Membuat Database Perpustakaan Sederhana"

Kriteria :
1. Dapat melakukan operasi Create, Read, Update and Delete (CRUD)
2. Memiliki database yang menampung operasi CRUD
3. Memiliki UI dalam menampilkan hasil operasi CRUD

"""

import os
import CRUD as CRUD

'''
Membuat program sesuai konvensi Python untuk memulai program yaitu dengan __name__ == "__main__" yang menunjukkan ini adalah program utamanya
'''

if __name__ == "__main__" :
    sistem_operasi = os.name # untuk menentukan sistem operasi yang digunakan dapat dideteksi dengan fungsi os.name sehingga untuk clear screen terminal bisa berbeda nih antara Windows dengan Unix (Mac, Linux) jadinya pakai ini dulu

    match sistem_operasi :
            case "posix" : os.system("clear") # unix
            case "nt" : os.system("cls") # windows
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # check database itu ada atau tidak
    CRUD.init_console()

    '''
    match adalah teknik yang sama seperti switch-case dari C programming dimana berkelakuan seperti if-else condition akan tetapi setiap aturan kondisinya diatur berdasarkan case yang ditentukan. Atau dalam mudahnya, match ini berfungsi untuk melihat "kecocokan" antara kondisi terhadap case yang ditentukan
    '''

    while(True) :
        # melakukan clear screen terminal berdasarkan system operasi yang telah terdeteksi
        match sistem_operasi :
            case "posix" : os.system("clear") # unix
            case "nt" : os.system("cls") # windows

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        # membuat option-option menu
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukkan opsi : ")

        # rules untuk memilih menu option dari user_option
        match user_option :
            case "1" : CRUD.read_console()
            case "2" : print("Create Data")
            case "3" : print("Update Data")
            case "4" : print("Delete Data")
        
        is_done = input("Apakah Selesai (y/n) ? ")
        if is_done == "y" or is_done == "Y" :
            break
    
    print("Program Berakhir, Terimakasih KAKAAAAAA")