"""
Numpy merupakan salah satu package yang paling populer di Python dan ada di PyPi yang berfungsi untuk membantu kita dalam melakukan analisa dan operasi matematika seperti matrix dan sebagainya
"""

import numpy as np

list_a = [1,2,3,4] # list berbeda dengan matrix dari numpy dimana setiap anggotanya tidak bisa kita operasikan secara matematis layaknya matrix pada numpy
vector_a = np.array([1,2,3,4]) # membuat matriks vektor (1 dimensi) dengan menginputkan list sebagai nilai-nilai dalam matriksnya

print(f"list_a = {list_a}")
# print(list_a**2) # error
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}") # seluruh anggota vector_a dikuadratkan
print(f"a kali 5 = {vector_a*5}") # seluruh anggota vector_a dikalikan 5
print(list_a*2) # menghasilkan duplikasi anggota list dimana jadinya ada 2 kali anggota

matrix_b = np.array([(1,2),(3,4)]) # untuk membuat matrix dengan dimensi lebih dari satu maka dalam inputan listnya dibedakan dengan set dimana setiap set menunjukkan letak baris dan kolom dari setiap anggota dari matrix, example [(1,2),(3,4)] yg artinya 1 itu dibaris pertama kolom pertama, 2 berada di baris pertama kolom kedua dan (3,4) yg artinya 3 ada di baris kedua kolom pertama dan 4 ada di baris kedua kolom kedua
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}") # melakukan operasi kuadrat dalam matrix

zeros_c = np.zeros((2,2)) # membuat matrix dengan komponen bernilai 0 dua dimensi dengan menginputkan parameter dalam set sebagai ukuran dimensinya yaitu (baris, kolom)
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2)) # membuat matrix dengan komponen bernilai 1 dua dimensi dengan menginputkan parameter dalam set sebagai ukuran dimensinya yaitu (baris, kolom)
print(f"ones d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d # melakukan operasi penjumlahan matrix
print(jumlah)
