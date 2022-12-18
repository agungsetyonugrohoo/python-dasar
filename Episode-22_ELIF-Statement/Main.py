"""
ELIF = else if statement

ELIF merupakan penambahan suatu kondisi pada if else untuk memperoleh kondisi lain dalam suatu control flow program

Konstruksi :
if kondisi:
    aksi true
elif kondisi :
    aksi true
elif kondisi :
    aksi true
else :
    aksi
"""

nama = input("Nama kamyu siapa? ")

if nama == "ucup" : # kondisi 1
    print("Hai ganteeeeng beudhs!") # aksi true 1
elif nama == "otong" : # kondisi 2
    print("Hai si kece bangeeeets!!") # aksi true 2
elif nama == "mario" : # kondisi 3
    print("Hai, humoooreeessh!") # aksi true 3
else :
    print("au ah gak kenal!!!") # aksi false

print("ini adalah akhir dari program")