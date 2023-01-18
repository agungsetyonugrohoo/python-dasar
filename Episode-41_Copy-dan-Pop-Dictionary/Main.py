"""
Copy dan Pop Dictionary
- apabila menggunakan assignment operator dalam melakukan duplikat dictionary maka hasilnya akan sama seperti ketika melakukan assignment operator untuk menduplikat data list yang dimana hasilnya kedua variabel yang menampung data baik data asli dan data copy memiliki address memori yang sama sehingga apabila salah satu anggota data dari salah satu variabel penampung data diubah maka perubahannya akan diterapkan ke semuanya anggota data yang menampung data tersebut
- method copy() dalam dictionary berperilaku sama seperti copy() pada list yaitu melakukan duplikasi data dengan membuat address memori baru terhadap data copynya sehingga tidak mengalami reference yang sama
- method pop("key") dengan key merujuk pada suatu data tertentu dalam dictionary berperilaku sama seperti pop() pada list dimana data yang diberikan method tersebut akan hilang.
- method lain untuk meremove data dalam dictionary adalah popitem() dimana akan meremove atau mentransfer data paling terakhir dalam suatu data dictionary dalam format berpasangan (key dan value) yang ditampung dalam bentuk tuple
"""

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

# friends = teman_teman # apabila menggunakan assignment operator dalam duplikat data maka hasilnya akan memiliki address memori data yang sama sehingga apabila terdapat salah satu perubahan pada data asli atau data copy maka perubahan tersebut akan diterapkan pada keduanya artinya hasil kejadian ini akan mengalami refrence yang sama

friends = teman_teman.copy() # untuk memperoleh hasil duplikasi dengan menghasilkan data copy yang memiliki address memori baru

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"] = "ucup si kweren"

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep") # mengambil dan meremove data yang dicari dari friends berdasarkan keynya. Atau dalam singkatnya, dengan method pop data dengan key tertentu yang dipop itu di transfer ke dalam suatu variabel tertentu sehingga data yang ditransfer itu sudah tidak lagi ada di data penampung sebelumnya
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (berdasarkan data yang paling akhir ajah)
dataTerakhir = friends.popitem() # mengambil data terakhir dalam data dictionary
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")