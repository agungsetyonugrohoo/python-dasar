"""
Operator dictionary
-> mengetahui panjang dictionary dengan "len"
-> mengetahui apakah terdapat suatu key dalam suatu data dictionary dengan "in" dengan menghasilkan boolean
-> method dictionary.get("key") dalam dictionary berfungsi untuk mengakses value data dalam dictionary melalui keynya
-> dengan method get juga kita dapat set default terhadap data yang tidak ada keynya di dalam suatu dictionary sehingga yang default bawaannya akan menampilkan None diubah menjadi lainnya sesuka kita
-> cara mengupdate data pada dictionary dapat dilakukan dengan operator assignment dimana memanggil data dictionary berdasarkan keynya lalu mengisi valuenya dengan baru sehingga menimpa value yang lama
-> cara lain adalah dengan menggunakan method update({key:value}) dimana akan secara otomatis mengupdate data sesuai key dan menimpa value yang lama dengan yang baru dan apabila tidak ada key yang sesuai dengan yang ada di dalam data dictionary maka akan dilakukan penambahan data
-> cara untuk menghapus data pada dictionary adalah dengan menggunakan del yang diikuti oleh keynya
"""

data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict) # penamaan LENDICT dalam huruf kapital dikarenakan mengikuti aturan pylint
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict # cara untuk mengetahui apakah KEY ada di data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"]) # penggunaan metode akses data atau membaca data dari dictionary ini hampir sama seperti list jadi secara samar sulit membedakan apakah data yang ditampung itu bertipe list atau dictionary
# print(data_dict["kis"]) # akan menghasilkan error KeyError dikarenakan tidak ada key kis dalam data_dict

# cara lain mengakses data dictionary dengan method .get("key")
print(data_dict.get("cup"))

# casenya tidak ada key "kis" sehingga akan menghasilkan output "None". Cek key ini juga bisa menampilkan pesan lain selain None dengan menampilkan pesan lain
print(data_dict.get("kis", "key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep" # penambahan dilakukan dengan melakukan assign nama key baru beserta value barunya
print(data_dict)

data_dict.update({"cup":"ucup surucup"}) # untuk melakukan update data pada data dictionary
data_dict.update({"faqih":"faqihza si kweren"}) # kalau ga ada di add aja
# salah satu fitur dari update() dimana apabila dalam suatu variabel dictionary tidak memiliki data key dan value yang akan digunakan untuk update atau data key dan value yang dilakukan untuk update merupakan data baru maka akan langsung ditambahkan sebagai data baru
print(data_dict)

# mendelet data pada dictionary
del data_dict["faqih"]
print(data_dict)