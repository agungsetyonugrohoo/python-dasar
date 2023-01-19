""""
**kwargs

**kwargs atau keyword args merupakan suatu jenis exclusive parameter yang dapat digunakan pada fungsi yang bertipe data dictionary.

Struktur **kwargs pada fungsi diletakkan pada parameternya :
def fungsi_dengan_kwargs(**kwargs) : dimana **kwargs menunjukkan tipe data kwargs yang dapat berisikan tipe data apapun dan akan dihimpun pada suatu tipe data dictionary bernama kwargs

Dalam penggunaannya, pemanggilan fungsi dengan parameter **kwargs diperlukan pendefinisian pada parameternya seperti
def fungsi_dengan_kwargs(nama="ucup", tinggi=187, berat=79) : yang dimana key input parameter (nama, tinggi dan berat) menjadi key yang akan dihimpun dalam dictionary kwargs dan value input parameter ("ucup", 187 dan 79) menjadi value dari setiap key secara berurutan. Key input parameter (nama, tinggi dan berat) disebut juga sebagai keywords

Dalam membuat fungsi dengan kedua jenis input parameter exclusive yang berbeda (*args dan **kwargs), maka didahulukan *args dulu baru **kwargs jadinya def fungsi(*args, **kwargs)
"""

def fungsi(nama, tinggi, berat) :
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 183, 79)

def fungsi(**kwargs) :
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]

    # print(kwargs) # kwargs menghimpun semua input parameter menjadi key value (dictionary)
    # print(kwargs["nama"]) # outputnya merupakan value dari key "nama" yaitu "ucup"

    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup", tinggi=183, berat=79) # output : {'nama': 'ucup', 'tinggi': 183, 'berat': 79}

# studi kasus
def math(*args, **kwargs) :
    output = 0
    if kwargs["option"] == "tambah" :
        # print("operasi penjumlahan")
        for angka in args :
            output += angka
    elif kwargs["option"] == "kali" :
        # print("operasi perkalian")
        output = 1 # untuk menginisiasikan angka output awal yang tersimpan adalah 1 sehingga bisa dikalikan, apabila sama seperti jumlah yaitu 0 maka hasilnya akan 0
        for angka in args :
            output *= angka
    else :
        print("tidak ada operasi")
    return output


hasil = math(1,2,3,4,option="tambah")
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")