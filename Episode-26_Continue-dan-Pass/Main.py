"""
Control Flow terdiri dari :
- continue => suatu aksi kondisi cabang tambahan yang dimana memiliki satu tujuan yang sama dengan cabang utamanya yaitu ke akhir loop akan tetapi melalui loncatan ke step selanjutnya
- pass => sebuah aksi yang disebut sebagai dummy dimana aksi ini tidak akan dieksekusi
- break

Kondisi continue membuat step yang diloncati (step yang berada di bawah perintah continue) tidak akan dieksekusi dan akan kembali pada step perulangan awal lagi dengan masih melanjutkan nilai iterasinya
"""

# pass
# angka = 0

# while angka < 5 :
#     angka += 1

#     # pass
#     if(angka == 3) :
#         pass # ini tidak akan dieksekusi
    
#     print(angka)

# continue
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5 :
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3 :
        print("nice!")
        continue # akan membuat loop meloncat ke step selanjutnya
    
    print("whassup!") # aksi 2

print("Pinish!")