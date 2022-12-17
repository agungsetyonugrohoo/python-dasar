"""
If dan Else Statement => Control Flow Program

Konstruksi :
- if nya
- kondisinya
- aksinya

Code :
program sebelumnya
if kondisi: aksi
program selanjutnya

indentasi merupakan sebuah spasi yang menjorok ke dalam untuk menandakan suatu statement atau aksi masih dalam scope yang sama terhadap suatu operasi program contohnya if
"""

nama = input("Siapa nama anda? ")

# 1. program if inline
# if nama == "ucup" : print("Kamu Ganteng abieeez!!!")
# print(f"Terima kasih {nama}")

# 2. program if indentation
# if nama == "ucup":
#     print("kamu ganteng abieeeez!")
#     print("kamu juga keren banget!")
# print(f"Terima kasih {nama}")

# 3. Else Statement
if nama == "otong":
    print("hai otooong, si keren!!!")
else:
    print("Ah kamu bukan otong, kamu ga keren! :(")
print("akhir dari program")
