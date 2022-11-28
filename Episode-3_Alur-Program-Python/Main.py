import time
start_time = time.time()

# python merupakan bahasa interpreted sehingga setiap baris perintah akan dieksekusi satu persatu dari atas ke bawah berurutan
print("Hello") # eksekusi pertama baris pertama
print("World") # eksekusi kedua membuat baris baru menjadi baris kedua
print("Hello World") # ekseskusi ketiga membuat baris baru menjadi baris ketiga

print("Halo Chantiiek")
# ini adalah comment dan tidak akan ditampilkan
a = 10 # istilahnya assignment dan akan dimasukkan ke dalam memori
print(a) # menampilkan isi dari variabel a

for i in range(1, 1000):
    a = 10
    
print(time.time() - start_time, "detik")

"""
ada apa dengan ucup
dan otong si ganteng
dalam comment multiline
"""

# kita bisa mengcompile python ke yang namanya bytecode yaitu dengan cara :

"""
Cara mengcompile :
- buka terminal
- tuliskan : python3 -m py_compile ./Episode-3_Alur-Program-Python/Main.py
"""

# tujuan compile ini adalah untuk membuat proses eksekusi file python bisa menjadi lebih cepat
