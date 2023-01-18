# 1. -----0+++++5------8++++++11-------
inputUser = float(input("masukkan angka yang bernilai lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11 : "))

# -----0++++++
isLebihDari0 = (inputUser > 0)
print("Lebih dari 0 =", isLebihDari0)

# +++++5------
isKurangDari5 = (inputUser < 5)
print("Kurang dari 5 =", isKurangDari5)

# -----8++++++
isLebihDari8 = (inputUser > 8)
print("Lebih dari 8 =", isLebihDari8)

# +++++11------
isKurangDari11 = (inputUser < 11)
print("Kurang dari 11 =", isKurangDari11)

"""
-----0+++++5------8++++++11-------
rule :
- kurang dari 0 -> false
- lebih dari 0 dan kurang dari 5 -> true
- lebih dari 5 dan kurang dari 8 -> false
- lebih dari 8 dan kurang dari 11 -> true
- lebih dari 11 -> false
"""

# -----0+++++5------8++++++11-------
isCorrect = ((isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11))
print("angka yang anda masukkan :", isCorrect)

print("\n",10*'=',"\n")

# 2. +++++0-----5++++++8------11+++++++
inputUser = float(input("masukkan angka yang bernilai kurang dari 0 atau lebih dari 5 dan kurang dari 8 atau lebih dari 11 : "))

# +++++0------
isKurangDari0 = (inputUser < 0)
print("Kurang dari 0 =", isKurangDari0)

# -----5++++++
isLebihDari5 = (inputUser > 5)
print("Lebih dari 5 =", isLebihDari5)

# +++++8------
isKurangDari8 = (inputUser < 8)
print("Kurang dari 8 =", isKurangDari8)

# -----11++++++
isLebihDari11 = (inputUser > 11)
print("Lebih dari 11 =", isLebihDari11)

"""
+++++0-----5++++++8------11+++++++
rule :
- kurang dari 0 -> true
- lebih dari 0 dan kurang dari 5 -> false
- lebih dari 5 dan kurang dari 8 -> true
- lebih dari 8 dan kurang dari 11 -> false
- lebih dari 11 -> true
"""

# +++++0-----5++++++8------11+++++++
isCorrect = (isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11)
print("angka yang anda masukkan :", isCorrect)
