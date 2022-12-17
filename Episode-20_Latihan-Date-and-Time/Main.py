"""
Date and Time (latihan)

- import library bisa dilakukan dengan dua cara yaitu dengan menginisiasikan dengan nama tertentu atau tidak. Ex. import datetime maka pemanggilan librarynya harus dengan datetime.??? kalau jadinya import datetime as dt maka pemanggilannya harus sesuai dengan inisiasinya yaitu dt jadinya dt.???
- operator %A berfungsi untuk menampilkan hari dari suatu tanggal tertentu
"""

import datetime as dt

"""
Intermezzo

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2005,10,10)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")
"""

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")