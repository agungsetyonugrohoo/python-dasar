# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

"""
contohnya seperti ini :
++++++3--------10+++++++
rule : 
- kurang dari 3 true
- lebih besar dari 10 true
- diantara 3 dan 10 false
"""

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# pertama : membuat daerah kurang dari 3 
# memeriksa angka kurang dari 3
# ++++++3--------
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# kedua : membuat daerah lebih besar dari 10
# memeriksa angka lebih besar dari 10
# -------10++++++++
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# menggabungkan dua area kurang dari 3 dan lebih besar dari 10
# ++++++3--------10+++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan:", isCorrect)

# kasus 2 : irisan
"""
------3+++++++10-------
rule :
- kurang dari 3 false
- lebih besar dari 10 false
- diantara 3 dan 10 true
"""

print("\n",10*'=',"\n")

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

# -----3+++++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# +++++10-------
# kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

# ------3+++++++10-------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan:", isCorrect)

