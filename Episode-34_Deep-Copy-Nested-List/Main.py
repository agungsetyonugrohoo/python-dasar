"""
Deep Copy Nested List

-> Cara mengambil data tunggal dalam nested list adalah menggunakan dua indeks beraturan. Maksudnya adalah dengan menelusuri terlebih dahulu list paling luarnya baru list terdalamnya hingga dapat menemukan posisi indeks dari data yang ingin diambil. Contoh data[x][y] yang dimana data merupakan list yang menampung data list, x merupakan indeks data list di dalam list data dan y merupakan indeks data dalam data list yang ditampung oleh data

-> Pada method copy() dalam menduplikat list yang menampung list. Address list asli akan menghasilkan perbedaan dengan hasil address list yang telah dicopy. Akan tetapi untuk setiap list yang berada di dalam listnya, untuk list asli dan list copy memiliki address memori yang sama sehingga yang membedakan adalah address memori luarnya saja

-> Penggunaan address yang sama dalam list yang di dalam list terluar mengakibatkan apabila salah satu baik list asli atau list copy mengubah isi data dari data list yang di dalam list maka akan mengubah keduanya karena addressnya sama

-> Namun apabila mengubah data yang tidak tertampung list dapat diubah tanpa mempengaruhi list yang lain. Intinya yang di tipe data dalam listnya bukan list juga bisa di copy akan tetapi apabila sebaliknya tidak bisa

-> Method copy() melakukan duplikasi address apabila isi data dalam list berupa tipe data list dan melakukan duplikasi value apabila isi tipe datanya bukan list sehingga copy() disebut sebagai shallow copy (tidak bisa di copy lebih dalam)

-> Fungsi deepcopy() merupakan solusi untuk melakukan duplikasi nested list (list yang memiliki data list juga di dalamnya). Deepcopy ini dilakukan dengan cara melakukan import copy dengan menggunakan toolsnya yaitu deepcopy
"""

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list
data = data_2D[1][0]
print(f"data = {data}")

# address dari data 2D dan data 2D copy
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5 # pada index-1 dalam list index-0
data_2D[2] = 9 # pada index-2 pada list terluar
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengatasi permasalahan copy() karena bertipe shallow copy dengan deepcopy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

# address dari data 2D dan data 2D deepcopy
print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deep = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")