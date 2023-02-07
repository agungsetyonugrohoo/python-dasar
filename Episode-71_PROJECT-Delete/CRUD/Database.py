from . import Operasi

DB_NAME = "data.txt" # Nama dan alamat database yang digunakan
TEMPLATE = {
    "pk" : "XXXXXX", # prime key (harus unik)
    "date_add" : "yyyy-mm-dd",
    "judul" : 255 * " ", # dibatasi 255 karakter
    "penulis" : 255 * " ", # dibatasi 255 karakter
    "tahun" : "yyyy"
}
def init_console() :
    '''Melakukan pengecekan ketersediaan database'''
    try :
        with open(DB_NAME, "r") as file :
            print("Database tersedia, init done!")
    except :
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()