"""
Package adalah sebuah tempat program yang menampung module-module. Cara memanggil atau menggunakan package sama seperti module yaitu dengan import nama packagenya apabila satu folder dan apabila di berbeda folder perlu didefinisikan dahulu alamat packagenya.

Untuk mengimport module dalam package dilakukan dengan cara memanggil nama packagenya kemudian titik dan diikuti nama modulenya contoh : import sains.matematika, dimana sains adalah packagenya dan matematika adalah modulenya

Pycache adalah file yang berisikan bytecode dari suatu package atau module. Fungsinya untuk mempercepat akses fungsi dari module atau package. Berdasarkan nama filenya, pycache ini muncul selaras dengan nama modulenya diikuti dengan versi python yang digunakan untuk mengcompile file modulenya contoh matematika.cpython-310.pyc, artinya module yang dicompile adalah matematika dengan versi python 3.10 dan pyc adalah format bytecodenya
"""

import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90, 10)
print(f"gaya adalah = {gaya}")

gaya = force(90, 10)
print(f"gaya adalah = {gaya}")
