"""
Operator assignment adalah operasi yang dapat dilakukan dengan penyingkatan atau kondisi dimana sebuah operasi ditambah dengan assignment
"""

a = 5 # adalah assignment
print("nilai a =",a)

# Penjumlahan
a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi",a)

# Pengurangan
a -= 2 # artinya adalah a = a - 2 
print("nilai a -= 2, nilai a menjadi",a)

# Perkalian
a *= 5 # artinya adalah a = a * 2 
print("nilai a *= 5, nilai a menjadi",a)

# Pembagian
a /= 2 # artinya adalah a = a / 2 
print("nilai a /= 1, nilai a menjadi",a)

# Modulus
b = 10
print("\nnilai b =", b)
b %= 3
print("nilai b %= 1, nilai b menjadi",b)

# Floor Division
b = 10
print("\nnilai b =", b)
b //= 3
print("nilai b //= 1, nilai b menjadi",b)

# Pangkat atau Eksponen
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3, nilai a menjadi",a)

# operasi bitwise
# operator bitwise apabila digunakan pada boolean maka hasilnya seperti operator logika biasa

# OR (|)
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi", c)

c = False
c |= False
print("nilai c |= False, nilai c menjadi", c)

# AND (&)
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi", c)

c = True
c &= True
print("nilai c &= True, nilai c menjadi", c)

# XOR (^)
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi", c)

c = True
c ^= True
print("nilai c ^= True, nilai c menjadi", c)

# shifting (geser-geser)

# shift right
d = 0b100
print("\nnilai d =",format(d,'04b')) # mengubah format nilai d menjadi binner 4-bit
d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d,'04b'))

# shift left
d <<= 1
print("nilai d <<= 1, nilai d menjadi", format(d,'04b'))

