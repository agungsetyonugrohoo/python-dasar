"""
Module

Module adalah suatu kumpulan fungsi yang memiliki operasi spesifik tertentu. Module ini bisa kita gunakan dengan memanggil nama modulenya berdasarkan letak module itu berada, apabila satu folder maka kita hanya perlu memanggil namanya saja akan tetapi jikalau berbeda berarti kita harus mendefinisikan alamat foldernya baru nama modulenya. Secara umum, module ini sama seperti file py biasanya akan tetapi fungsi dan isinya berbeda yang dimana berisikan sekumpulan instruksi spesifik.

Dalam pemanggilan module, kita dapat menggunakan from untuk mengimport fungsi yang diperlukan tanpa harus memanggil nama modulenya. Contohnya : from matematika import tambah, dimana matematika merupakan nama modulenya dan tambah merupakan fungsi spesifik yang ingin kita gunakan. Selain fungsi tambah fungsi yang lain tidak bisa kita terapkan. Dengan menggunakan from ini kita hanya perlu menerapkannya melalui nama fungsi saja tidak perlu diikuti dengan nama modulenya.

Selain itu, dengan from ini juga bisa memanggil keseluruhan fungsi yaitu dengan mengimport * yang berarti seluruh fungsi dalam module bisa kita akses dengan namanya saja. Kelemahannya apabila terdapat import from yang menggunakan * maka akan sulit mengidentifikasi fungsi mana yang berasal dari salah satu module yang digunakan.

Memanggil fungsi dari module menggunakan alias berfungsi untuk memberikan nama lain dari fungsi yang akan kita gunakan. Contoh fungsi dalam matematika kan ada tambah bisa kita aliaskan dengan add sehingga dalam memanggil fungsi tambah bisa kita "alias"kan dengan nama add
"""

# module matematika dengan import

import matematika as math # <-- bisa dilakukan untuk memberikan alias dalam penamanaan atau pemanggilan suatu module

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as terserah_kalian_mau_apa

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = terserah_kalian_mau_apa(3)
print(f"hasil pangkat3 = {pangkat_3(3)}")