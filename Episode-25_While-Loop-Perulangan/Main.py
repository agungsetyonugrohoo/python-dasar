"""
While loop => suatu skema perulangan berdasarkan suatu kondisi tertentu dimana pengecekan akan dilakukan terlebih dahulu. Apabila memenuhi maka dilakukan pengulangan dan apabila tidak diberhentikan

Kondisi while kadang dapat terjadi suatu kondisi pengulangan tak berhingga (infinite loop) dimana hasil pengecekan kondisi selalu bernilai true yang menyebabkan pengulangan dilakukan secara terus menerus tanpa henti

Untuk dapat mengantisipasi kondisi infinite loop perlu dilakukan suatu rules tambahan untuk melakukan increment atau decrement terhadap status nilai kondisi agar dapat menuju false

Struktur kode
awal dari program

while kondisi (boolean) :
    aksi

akhir dari program
"""

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    print("otong ganteng maxsyimaal!")

print("cukuuup")
