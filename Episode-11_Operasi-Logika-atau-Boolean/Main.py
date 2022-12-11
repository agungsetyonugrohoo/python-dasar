"""
operato logika atau boolean

operator ini terdiri dari :
- not -> menghasilkan kebalikan dari state awal
- or -> jika salah satu true, maka hasilnya adalah true (seperti operasi penjumlahan)
- and -> jika dua buah nilai true, maka hasil true (seperti operasi perkalian)
- xor -> akan bernilai true jika salah satu nilai bernilai true
"""

# not
print('='*5, 'NOT', '='*5)
a = True
c = not a # False
print('data a =', a)
print('-'*5, 'NOT', '-'*5)
print('data c =', c)

# or
print('='*5, 'OR', '='*5)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,'=',c)

# and
print('='*5, 'AND', '='*5)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,'=',c)

# XOR (operator bitwise)
print('='*5, 'XOR', '='*5)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,'=',c)