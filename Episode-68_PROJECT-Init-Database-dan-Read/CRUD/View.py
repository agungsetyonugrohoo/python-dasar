from . import Operasi

def read_console() :
    '''Membuat fungsi Read Database dan menampilkannya melalui konsol'''
    data_file = Operasi.read()
    
    # styling dalam menampilkan data dari database
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}") # buat header
    print("-"*100)

    # Data
    for index, data in enumerate(data_file) :
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="") # arti .40 adalah memberikan spasi sebanyak jumlah karakter yang diperlukan agar jumlahnya sesuai contohnya judul karena sudah ada nama judulnya untuk menjadi jumlah karakternya 40 maka diperlukan spasi tambahan



    # Footer
    print("="*100+"\n")
