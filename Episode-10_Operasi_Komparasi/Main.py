"""
Operasi Komparasi adalah suatu operasi untuk membandingkan nilai.

Setiap hasil dari operasi komparasi adalah boolean

Operator komparasi diantaranya :
- >
- <
- >=
- <=,
- ==
- !=
- is
- is not

# untuk '=' artinya assignment sedangkan '==' artinya membandingkan dua buah nilai

# >, <, >=, <=, ==, != -> operator komparasi ini dapat bekerja pada syntax literal

# syntax literal adalah sebuah nilai yang tidak berada pada sebuah variabel ex => a == 4, a merupakan sebuah variabel yang memiliki nilai 4 dan memakan memori sedangkan 4 merupakan sebuah nilai yang tidak dimiliki oleh variabel manapun dan tidak memakan memori

# is merupakan operator yang membandingkan antara nilai yang memakan memori atau object
"""

a = 4
b = 2

# operator lebih besar dari (>)
print('='*5, 'lebih besar dari (>)', '='*5)

hasil = a > 3 # True
print(a,'>',3,'=',hasil)

hasil = b > 3 # False
print(b,'>',3,'=',hasil)

hasil = b > 2 # False
print(b,'>',2,'=',hasil)

# operator kurang dari (<)
print('='*5, 'kurang dari (<)', '='*5)

hasil = a < 3 # False
print(a,'<',3,'=',hasil)

hasil = b < 3 # True
print(b,'<',3,'=',hasil)

hasil = b < 2 # False
print(b,'<',2,'=',hasil)

# operator lebih dari sama dengan (>=)
print('='*5, 'lebih dari sama dengan (>=)', '='*5)

hasil = a >= 3 # True
print(a,'>=',3,'=',hasil)

hasil = b >= 3 # False
print(b,'>=',3,'=',hasil)

hasil = b >= 2 # True
print(b,'>=',2,'=',hasil)

# operator kurang dari sama dengan (<=)
print('='*5, 'kurang dari sama dengan (<=)', '='*5)

hasil = a <= 3 # False
print(a,'<=',3,'=',hasil)

hasil = b <= 3 # True
print(b,'<=',3,'=',hasil)

hasil = b <= 2 # True
print(b,'<=',2,'=',hasil)

# operator sama dengan (==)
print('='*5, 'sama dengan (==)', '='*5)

hasil = a == 4 # True
print(a,'==',4,'=',hasil)

hasil = b == 4 # False
print(b,'==',4,'=',hasil)

# operator tidak sama dengan (!=)
print('='*5, 'tidak sama dengan (!=)', '='*5)

hasil = a != 4 # False
print(a,'!=',4,'=',hasil)

hasil = b != 4 # True
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object (object identity)
print('='*5, 'object identity (is)', '='*5)
x = 5 # ini adalah assignment membuat object

type(x) # mendeteksi jenis class variabel x yaitu adalah int

id(x) # menelusuri address memori yang menyimpan variabel x / id adalah object identity

hex(id(x)) # menelusuri address memori dalam hex yang menyimpan variabel x 

y = 5

hex(id(y)) # menelusuri address memori dalam hex yang menyimpan variabel y dimana alamatnya dibuat setelah alamat variabel x

print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
# menghasilkan nilai id yang sama, hal ini dikarenakan nilai yang terisi pada variabel x dan y adalah sama sehingga untuk mengefisienkan memori

hasil = x is y # membandingkan nilai x dan y
print(x,'is',y,'=',hasil)

"""
x is 5 -> maka akan menghasilkan error systax warning yang berisikan operator is tidak dapat digunakan pada literal sehingga akan merekomendasikan menggunakan operator '=='
"""

x = 5
y = 6

print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))

hasil = x is y # membandingkan nilai x dan y
print(x,'is',y,'=',hasil)

# 'is not' sebagai komparasi object (object identity)
print('='*5, 'object identity (is not)', '='*5)

x = 5
y = 5

print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))

hasil = x is not y # sama seperti tidak sama dengan
print(x,'is',y,'=',hasil)

x = 5
y = 6

print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))

hasil = x is not y # sama seperti tidak sama dengan
print(x,'is',y,'=',hasil)









