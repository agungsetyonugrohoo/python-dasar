"""
Module

Module adalah suatu kumpulan fungsi yang memiliki operasi spesifik tertentu. Module ini bisa kita gunakan dengan memanggil nama modulenya berdasarkan letak module itu berada, apabila satu folder maka kita hanya perlu memanggil namanya saja akan tetapi jikalau berbeda berarti kita harus mendefinisikan alamat foldernya baru nama modulenya. Secara umum, module ini sama seperti file py biasanya akan tetapi fungsi dan isinya berbeda yang dimana berisikan sekumpulan instruksi spesifik.

Dalam pemanggilan module, kita dapat menggunakan from untuk mengimport fungsi yang diperlukan tanpa harus memanggil nama modulenya. Contohnya : from matematika import tambah, dimana matematika merupakan nama modulenya dan tambah merupakan fungsi spesifik yang ingin kita gunakan. Selain fungsi tambah fungsi yang lain tidak bisa kita terapkan. Dengan menggunakan from ini kita hanya perlu menerapkannya melalui nama fungsi saja tidak perlu diikuti dengan nama modulenya.

Selain itu, dengan from ini juga bisa memanggil keseluruhan fungsi yaitu dengan mengimport * yang berarti seluruh fungsi dalam module bisa kita akses dengan namanya saja. Kelemahannya apabila terdapat import from yang menggunakan * maka akan sulit mengidentifikasi fungsi mana yang berasal dari salah satu module yang digunakan.
"""

# module matematika dengan import

# import matematika # dapat memanggil seluruh fungsi yang ada di module matematika
from matematika import tambah, kali, pangkat # hanya mengimport fungsi tertentu yaitu tambah dan kali
# from matematika import * # melakukan import seluruh fungsi yang ada di modul matematika

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"hasil pangkat3 = {pangkat_3(3)}")