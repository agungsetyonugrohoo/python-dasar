"""
Perulangan (loop) => Suatu skema aksi pengulangan ketika suatu kondisi terpenuhi (true) dan akan berhenti ketika kondisi tidak lagi terpenuhi (false)

for kondisi :
    aksi

range adalah suatu urutan angka dari nilai nol sampai kurang dari nilai tertentu yang ditentukan.

ex range : range(5) => urutannya adalah 0,1,2,3,4 dimana angka 5 tidak diikutsertakan

untuk range(a,b) => urutannya berawal dari a hingga kurang dari b

ex range(a,b) : range(1,5) => urutannya adalah 1,2,3,4 dimana angka 5 tidak diikutsertakan

pengulangan juga dapat dilakukan pada string dimana menghasilkan perulangan per karakternya di dalam string
"""

'''
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
...

Fungsi pengulangan : menyederhanakan sintaks perulangan diatas
'''

# ini dengan list
angka2_list = [0,1,2,3,4] # ini adalah list

# Untuk i yang merupakan indeks dari data di dalam angka2, cetak i sekarang beserta data indeks ke i dalam angka2
for i in angka2_list :
    print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)

for i in angka2_range :
    print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1,10)

for i in angka2_range :
    print(f"i sekarang -> {i}")
    # print("saya keren")

print("akhir dari program 3 \n")

# menggunakan string

data_str = "saya ganteng abiees"

for huruf in data_str :
    print(huruf)

print("akhir dari program 4 \n")