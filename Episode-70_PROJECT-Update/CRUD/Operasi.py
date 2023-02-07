from . import Database
from .Util import random_string
import time

def update(no_buku,pk,data_add,tahun,judul,penulis) :
    '''Untuk melakukan update terhadap data yang exist di database'''
    # membuat data frame
    data = Database.TEMPLATE.copy()
    data["pk"] = pk # menjadi data pk pada data index buku yang ingin di update
    data["date_add"] = data_add # menjadi data_add dari data index yang ingin di update
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] # fungsi + Database ... adalah untuk melengkapi sisa karakter dalam memenuhi batas karakter yang bisa diinputkan
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # template data ketika update data ke database
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str) # menghitung jumlah karakter dalam data update

    # update ke database
    try :
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file :
            file.seek(panjang_data * (no_buku-1)) # untuk memindahkan kursor dalam melakukan write update data terhadap data yang ingin di update dimana panjang data akan selalu sama sesuai template dan dikalikan dengan no_buku-1 berfungsi untuk menempatkan di data ke berapa akan dilakukan write update data
            file.write(data_str)
    except :
        print("error dalam update data")

def create(tahun,judul,penulis) :
    '''Untuk memasukkan data baru ke database'''
    # membuat data frame
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6) # mengenerate random string untuk prime key
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) # %z berfungsi untuk GMT Time
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] # fungsi + Database ... adalah untuk melengkapi sisa karakter dalam memenuhi batas karakter yang bisa diinputkan
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # template data ketika masuk ke database
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    # proses menambahkan data ke dalam database
    try :
        with open(Database.DB_NAME, "a", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("Data sulit ditambahkan boooos, gagal maning")

def create_first_data() :
    '''Untuk menginputkan data'''
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    while True :
        # untuk membuat inputan data tahun berupa angka dan apabila tidak akan disuruh masukkin datanya lagi hingga benar
        try :
            tahun = int(input("Tahun\t: "))
            # untuk membatasi inputan angka pada tahun harus berjumlah 4 angka
            if len(str(tahun)) == 4 :
                break
            else :
               print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)") 
        except :
            print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    # membuat data frame
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6) # mengenerate random string untuk prime key
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) # %z berfungsi untuk GMT Time
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] # fungsi + Database ... adalah untuk melengkapi sisa karakter dalam memenuhi batas karakter yang bisa diinputkan
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # template data ketika masuk ke database
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)

    # proses memasukkan data ke dalam database
    try :
        with open(Database.DB_NAME, "w", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("Udah lah Gagal booooos")

def read(**kwargs) :
    '''Membaca data dari database'''

    try :
        with open(Database.DB_NAME, 'r') as file :
            content = file.readlines() # mengakses konten menjadi list
            jumlah_buku = len(content) # menghitung jumlah data buku
            if "index" in kwargs :
                # untuk mencegah terjadinya pemilihan index buku melebihi jumlah data buku yang disimpan dalam database
                index_buku = kwargs["index"]-1 # untuk merujuk pada data buku yang ingin ditampilkan sebagai konten
                if index_buku < 0 or index_buku > jumlah_buku :
                    return False
                else :
                    return content[index_buku] # untuk menampilkan konten sesuai index data buku, mengapa dikurangi 1 di bagian akhir? dikarenakan indexing pada list content dihitung dari 0 sehingga data kedua menjadi 1 dst
            else :
                return content # akan mengembalikan seluruh konten apabila tidak ada index buku yang dicari
    except :
        print("Membaca database error")
        return False
