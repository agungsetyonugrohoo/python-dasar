"""
Pengenalan String

String merupakan suatu object class dalam python yang berisi dari kumpulan karakter termasuk juga spasi dan simbol unik lainnya (!,?,~, dll)

Penggunaan single quote dan double quote secara bersamaan dimana apabila didahului single quote maka double quote akan menjadi string. Dan apabila didahului single quote dan ditutup oleh double qoute akan error

Error Unicodespace => merupakan error dimana penggunaan backslash (karakter khusus '\') terhadap suatu operasi tidak dikenali sehingga menimbulkan error syntaxerror

CRLF, LF, CR merupakan jenis line of sequence yang bisa digunakan pada operating system tertentu dimana biasanya LF digunakan untuk unix based system, CR untuk system os cukup lama seperti acorn dan CRLF digunakan untuk system operasi windows. Konvensi line of sequence ini digunakan sebagai pendeteksi dimana spasi atau baris baru yang akan ditambahkan

Multiline literal string berfungsi untuk melakukan pencetakan string dengan lebih bebas dan lebih banyak
"""

data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '<...>'
    2. dengan menggunakan double quote "<...>"

'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

# menggunakan single quote dan double quote secara bersamaan
print('"Halo, apa kabar?"') # double quote menjadi string
print("'Halo, apa kabar?'") # single quote menjadi string
print("ini adalah hari jum'at")

# 2. menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ucup") # penggunaan double backslash ('\\') digunakan untuk menghindari error syntax dikarenakan \ tidak mengetahui operasi terhadap string

# tab
print("ucup\t\t\totong, jauhan") #\t berfungsi untuk menambahkan spasi jauh (tab)

# backspace
print("ucup \botong, jadi deketan") #\b berfungsi untuk menghapus karakter sebelumnya sebanyak 1 kali

# newline
print("baris pertama.\nbaris kedua.") #\n berfungsi untuk menambahkan baris baru (enter) pada tipe line of sequence LF -> LF => Line Feed, biasanya dipakai pada Unix system
print("baris pertama.\rbaris kedua") #\r berfungsi sama seperti \n yaitu untuk menambahkan baris baru hanya saja bergantung pada tipe line of sequence CR -> CR => Carriage Return, biasanya digunakan untuk commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> biasanya dipakai oleh windows

# 3. String literal atau raw

# hati-hati dalam mengantisipasi adanya operator string seperti \n dsb dalam menuliskan path file yang menyebabkan hasilnya tidak sesuai yang diinginkan, ex :
print('C:\new folder')

# solusinya menggunakan metode raw string
print(r'C:\new \t\r\b\\ folder') # seluruh operator string akan di print dengan menganggap sebagai string biasa

# multiline literal string
print(""" 
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r""" 
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")



