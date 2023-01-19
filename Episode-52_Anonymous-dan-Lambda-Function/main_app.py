"""
Lambda function

Lambda function merupakan bentuk sintaks penyederhanaan terhadap suatu fungsi spesifik. Lambda function secara implisit sudah menghasilkan return value dari expressionnya sehingga tidak perli mendeklarasikan return value. Struktur fungsi lambda dibentuk sebagai berikut.
variabel_output = lambda argument : expression

Fungsi lambda expression :
- data sorting list -> sebagai key dalam proses sorting
- data filter list -> sebagai parameter dalam proses filter
"""

def f_kuadrat(angka) :
    return angka ** 2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita coba dengan lambda
# struktur lambda function -> output = lambda argument: expression
kuadrat = lambda angka : angka ** 2
print(f"hasil lambda kuadrat = {kuadrat(5)}") # fungsi yang dicari merupakan kuadrat yang merupakan fungsi lambda, 5 sebagai input parameter fungsi lambda yaitu angka dan dari angka tersebut kemudian diproses dengan expression di dalammya yaitu angka ** 2 dan kemudian di kembalikan (return value) secara otomatis melalui expressionnya

# fungsi lambda dengan dua input parameter
pangkat = lambda num,pow : num ** pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan apa bang?

# sorting untuk list biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting dia pakai panjang
def panjang_nama(nama) :
    return len(nama) # menggunakan struktur fungsi normal

data_list.sort(key=len) # parameter key dalam method sort berfungsi untuk mengatur sorting berdasarkan aturan key apa dimana dalam hal ini berdasarkan panjang karakter tiap data pada list yang akan disorting (len)
print(f"sorted list by len = {data_list}")

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama : len(nama)) # menggunakan lambda function
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka) :
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru)
data_angka_baru = list(filter(lambda x : x < 7, data_angka))
print(data_angka_baru)

# kasus genap (memfilter angka genap)
data_genap = list(filter(lambda x : (x % 2 == 0), data_angka))
print(data_genap)

# kasus genap (memfilter angka ganjil)
data_ganjil = list(filter(lambda x : (x % 2 != 0), data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x : (x % 3 == 0), data_angka))
print(data_3)

"""
Anonymous function

Anonymous function dibuat berdasarkan teknik currying oleh Haskell Curry. Anonymous function merupakan teknik fungsi currying untuk membuat fungsi tidak menjadi fixed dan kita bisa mengassign fungsi tersebut menjadi sebuah variabel. Salah satu contoh anonymous function adalah lambda yaitu fungsi yang tidak memiliki atau didefinisikan sebuah nama.

Anonymous function juga dapat dipanggil secara langsung tanpa harus membuat variabel dengan cara mendefinisikan nilai basis untuk lambda function yang kemudian diikuti dengan nilai inputan parameter untuk lambda function tsb seperti :
fungsi(basis_lambda)(input_parameter)

Pada intinya, anonymous function membuat fungsi dasar yang dapat diubah parameter-parameter operasi berdasarkan basisnya melalui assign variabel sehingga variabel yang menampung anonymous function menjadi sebuah fungsi yang memiliki basis dasar tertentu. Anonymous function biasanya digunakan untuk functional programming
"""

def pangkat(angka,n) :
    hasil = angka ** n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi
def pangkat(n) :
    return lambda angka : angka ** n

pangkat2 = pangkat(2) # mengassign n sebagai nilai basis pangkat dalam fungsi lambda
print(f"pangkat2 = {pangkat2(5)}") # dengan adanya anonymous function fungsi pangkat dapat diaplikasikan dalam variabel dan kita memanggil fungsi berdasarkan variabel tersebut

pangkat3 = pangkat(3) # mengassign n sebagai nilai basis pangkat dalam fungsi lambda
print(f"pangkat3 = {pangkat3(3)}") # menghasilkan nilai pangkat 3 dari 5

print(f"pangkat bebas = {pangkat(4)(5)}") # nilai parameter (4) dan (5) masing-masing merujuk pada basis pangkat dan nilai angkat yang ingin dipangkatkan sehingga menghasilkan 5^4