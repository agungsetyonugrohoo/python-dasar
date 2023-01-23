"""
__init__.py

__init__.py merupakan salah satu file bagian dari package yang berfungsi sebagai iinsiasi file dalam package atau merupakan suatu file yang akan dieksekusi terlebih dahulu setelah dilakukan import package

"""

# import sains.matematika # untuk percobaan module dalam package
import sains
# import sains.matematika.basic # untuk percobaan subpackage

# percobaan ketika matematika menjadi module dalam package sains
# hasil_tambah = sains.matematika.tambah(1,2,3,4,45) # akan error dikarenakan pada import sains saja, module atau package sains tidak memiliki attribute matematika sehingga error. Untuk mengatasinya diperlukan nama package dan nama module dalam mengimportnya menjadi import sains.matematika
# untuk dapat mengoperasikan fungsi tambah dapat menggunakan file init sebagai jembatan dalam mendeklarasikan nama module yaitu matematika pada package sains sehingga diisikan from . import matematika
# print(f"hasil tambah = {hasil_tambah}")

# percobaan ketika matematika menjadi subpackage
# hasil_pisika = sains.pisika.gaya(10, 9.8)
# print(f"hasil pisika = {hasil_pisika}")

# # percobaan dengan adanya subpackage yaitu matematika dalam sains
# hasil_kali = sains.matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

# hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil kali = {hasil_tambah}")

# percobaan menggunakan import * dengan __all__
# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil kali = {hasil_tambah}")

# hasil_kali = matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

# hasil_pisika = pisika.gaya(10, 9.8)
# print(f"hasil pisika = {hasil_pisika}")

# percobaan ketika menempelkan definisi terhadap subpackage sehingga menghilangkan basic dan scientific karena sudah didefinisikan pada init subpackage
# hasil_pisika = sains.pisika.gaya(10, 9.8)
# print(f"hasil pisika = {hasil_pisika}")

# hasil_kali = sains.matematika.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

# hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
# print(f"hasil kali = {hasil_tambah}")

# pangkat_3 = sains.matematika.pangkat(3)
# print(f"hasil pangkat 3 = {pangkat_3(5)}")

# percobaan ketika melakukan import terhadap subpackage dengan from import pada module scientific sehingga menghilangkan sains.matematika pada fungsi pangkat
from sains.matematika import scientific

hasil_pisika = sains.pisika.gaya(10, 9.8)
print(f"hasil pisika = {hasil_pisika}")

hasil_kali = sains.matematika.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
print(f"hasil kali = {hasil_tambah}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")
