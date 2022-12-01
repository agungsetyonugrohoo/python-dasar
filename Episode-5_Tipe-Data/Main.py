"""
Tipe Data adalah macam-macam data yang bisa digunakan dalam variabel
"""

# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 11
print(type(data_integer))
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup 10" # angka 10 di dalam data_string termasuk juga string
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool, ", bertipe : ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6) # 5 + 6j
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa C
## penggunaan tipe data dari bahasa C diharuskan mengimpor package atau library agar dapat menggunakan tipe data dari bahasa C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))