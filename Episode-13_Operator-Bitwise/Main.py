"""
Operasi bitwise adalah operasi pada masing-masing bit

Overview Binary 8-bit
int 2 -> 00000010
int 1 -> 00000001
int 9 -> 00001001

Operator bitwise :
- OR (|) => operasi OR antar bit
- AND (&) => operasi AND antar bit
- XOR (^) => operasi XOR antar bit
- NOT (~) => operasi NOT antar bit menghasilkan bit minus
- Shifting
-> Shift right (>>) => menggeser nilai bit ke kanan sejauh n tertentu
-> Shift left (<<) => menggeser nilai bit ke kiri sejauh n tertentu

Contoh OR
2 (00000010) | 1 (00000001) = 3 (00000011) => di jumlahkan masing-masing bitnya
"""

# episode operator bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('='*5, 'OR', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
# 08b maksudnya adalah memformat nilai a menjadi 8 bit binner
print('-'*30, '(|)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('='*5, 'AND', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
print('-'*30, '(&)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise XOR(^)
c = a ^ b
print('='*5, 'XOR', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
print('-'*30, '(^)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise NOT(~)
c = ~a
print('='*5, 'XOR', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('-'*30, '(^)')
print('nilai :',c,', binary :',format(c,'08b'))
# Hasilnya -10, mengapa? Hal ini dikarenakan nilai bit variabel a yaitu 5 dimirrorkan dengan nilai pada sumbu negatif. Dikarenakan nilai 0 termasuk ke dalam nilai positif dimana 0 tidak memiliki mirror yaitu -0, maka nilai 0 dimirrorkan menghasilkan -1, dan 1 menghasilkan -2, dst yang dimana proses mirroring dimulai dari kurang dari 0

# Cara flip nilai dari NOT supaya tidak bertanda minus di nilai bitnya
d = 0b0000001001
e = 0b1111111111
print('nilai flip (XOR) dari NOT 9 adalah', e^d, ', binary : ', format(e^d, '08b'))

# shifting

# shift right
c = a >> 2 # menggeser bit a yaitu 9 ke kanan sebesar 2 nilai bit
print('='*5, '>>', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('-'*30, '(^)')
print('nilai :',c,', binary :',format(c,'08b'))

# shift right
c = a << 2 # menggeser bit a yaitu 9 ke kanan sebesar 2 nilai bit
print('='*5, '<<', '='*5)
print('nilai :',a,', binary :',format(a,'08b'))
print('-'*30, '(^)')
print('nilai :',c,', binary :',format(c,'08b'))


