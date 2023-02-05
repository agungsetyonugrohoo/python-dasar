from . import Database
from .Util import random_string
import time

def create_first_data() :
    '''Untuk menginputkan data'''
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    tahun = input("Tahun : ")

    # membuat data frame
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6) # mengenerate random string untuk prime key
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) # %z berfungsi untuk GMT Time
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] # fungsi + Database ... adalah untuk melengkapi sisa karakter dalam memenuhi batas karakter yang bisa diinputkan
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    # template data ketika masuk ke database
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)

    # proses memasukkan data ke dalam database
    try :
        with open(Database.DB_NAME, "w", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("Udah lah Gagal booooos")

def read() :
    '''Membaca data dari database'''
    try :
        with open(Database.DB_NAME, 'r') as file :
            content = file.readlines() # mengakses konten menjadi list
            return content
    except :
        print("Membaca database error")
        return False
