# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan +
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil) # artinya a pangkat b

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a, '%', b, '=', hasil) # artinya a dibagi oleh b maka akan menghasilkan bilangan bulat dengan sisanya seperti 10 % 3 menghasilkan bilangan bulat 3 yaitu 3 x 3 = 9 dengan sisa pembaginya adalah 1

# operasi floor division (kebalikan dari modulus atau membulatkan ke bilangan terdekat) //
hasil = a // b
print(a, '//', b, '=', hasil) # artinya sama seperti modulus akan tetapi menghasilkan nilai hasil bilangan bulatnya contoh 10 // 3 menghasilkan 3 dengan 0,333... dibulatkan ke 3 atau seperti kalau kita ingin mencari 10/3 kira2 bulatnya berapa yak?

# prioritas operasi, operational precedence
"""
Urutan prioritas operasi
-> ()
-> Eksponen **
-> Perkalian *, Pembagian /, Modulus %, Floor Division //
-> Pertambahan +, Pengurangan -
"""
x = 3
y = 2
z = 4
hasil = x ** y * ( z + x ) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
"""
hasil = x ** y * z + x / y - y % z // x
3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
9 * 4 + 3 / 2 - 2 % 4 // 3
36 + 1,5 - 0
37,5

hasil = x ** y * ( z + x ) / y - y % z // x
3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
3 ** 2 * 7 / 2 - 2 % 4 // 3
9 * 7 / 2 - 2 % 4 // 3
31,5 - 0
31,5
"""

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)