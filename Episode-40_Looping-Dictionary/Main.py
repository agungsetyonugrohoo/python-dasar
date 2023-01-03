"""
Looping Dictionary

Cara mengakses data dictionary dengan looping :
- For : dalam melakukan looping biasa terhadap data dictionary, hanya baru dapat mengakses keynya saja. Untuk dapat mengakses valuenya dapat dilakukan dengan method get yang diikuti dengan keynya
- cara for juga dapat melakukan perulangan terhadap keys pada dictionary untuk menspesifikasikan bahwa data yang dilakukan iterasi merupakan dictionary dengan menggunakan method dictionary.keys() yang dimana akan menghasilkan sebuah list yang berisi key-key dari data dictionary
- dari dictionary.keys() ini kita dapat mengetahui bahwa data yang dilakukan iterasi merupakan dictionary dan bisa kita akses seluruh valuenya dengan method get yang diberi inputan key dari iterasi keys()
- cara lain untuk dapat mengakses looping dari value data dictionary adalah menggunakan dictionary.values() yang dimana akan menghasilkan sekumpulan data value dari data dictionary yang dituju sehingga dapat dilakukan perulangan untuk mengakses valuenya tanpa mengetahui atau melalui keynya terlebih dahulu untuk mengakses atau menampilkannya
- penggunaan method dictionary.items() dapat digunakan untuk mengakses key dan value sekaligus dalam bentuk tuple. Selain itu dapat dilakukan iterasi secara gabungan atau terpisan berdasarkan variabel iterasinya yaitu satu saja (bisa key atau valuenya saja) atau keduanya secara terpisan (key, value yang dipisah dengan koma) pada saat looping data dictionary
"""

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

# looping first try (dengan for) => yang keluar adalah keynya
for teman in teman_teman :
    print(teman)
# permasalahan baru muncul dikarenakan variabel teman_teman yang dilakukan iterasi menjadi teman pada loop for diatas akan dimaknai sebagai dictionary atau list sehingga kita gatau kebenerannya

# solusi : operator untuk mengambil item / iterables (data yang dapat dilakukan looping)
# cara untuk memperoleh data key apa saja dalam suatu data dictionary
# dengan method keys() => keys() hanya menampung data keynya saja
keys = teman_teman.keys() # memperoleh data key dari data dictionary dalam bentuk list yang ditampung dalam dict_keys
print(keys)

for key in teman_teman.keys() :
    print(teman_teman.get(key)) # mengakses value dari setiap key

# cara untuk memperoleh data value apa saja dalam suatu data dictionary
# dengan method values => values() hanya menampung valuenya saja
values = teman_teman.values() # memeperoleh list data value dari data dictionary yang ditampung dalam dict_values
print(values)

for value in teman_teman.values() :
    print(value) # mengakses value tanpa melalui atau mengetahui keynya namun langsung dari values()

# dengan method items => items() menampung key dan value berpasangan sekaligus yang ditampung dalam bentuk tuple
items = teman_teman.items()
print(items)

for item in teman_teman.items() :
    print(item) # mengakses data dictionary dengan menghasilkan pasangan key-value dalam bentuk tuple

# dengan items juga dapat mengakses key dan valuenya sekaligus secara terpisah
for key,value in teman_teman.items() :
    print(f"key = {key}, value = {value}")