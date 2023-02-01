# Tuotorial Write External File

'''
Dalam mode "w" atau write, apabila file yang dibuka tidak ada di dalam suatu folder / dokumen, maka dengan otomatis python akan membuatnya sesuai dengan nama beserta format file yang diberikan. Ketika membuka file dengan mode ini, file otomatis akan "tertimpa" atau "overwrite" yang dimana apabila suatu file yang dibuka sudah ada isi kontennya akan ditimpa dengan isi konten yang baru yang berasal dari inputan koding kita. Cara menuliskan isi konten dalam file adalah menggunakan method write.
'''

# 1. mode write, dia akan membuat file baru jika tidak ada, lalu akan menimpa atau overwrite isinya
with open("data_1.txt",'w',encoding="utf-8") as file :
    # encoding="utf-8" dimaksudkan sebagai jenis karakter yang digunakan dalam file
    file.write("jon si jhonny") # untuk menuliskan isi konten dalam file (overwrite)

with open("data_1.txt",'w',encoding="utf-8") as file :
    file.write("ucup surucup")

with open("data_1.txt",'w',encoding="utf-8") as file :
    file.write("overwrite")

# 2. mode append, menambahkan isi konten dari suatu file tanpa melakukan overwrite
with open("data_2.txt",'a',encoding="utf-8") as file :
    file.write("jon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as file :
    file.write("ucup surucup\n")

with open("data_2.txt",'a',encoding="utf-8") as file :
    file.write("tambah lagi dengan append\n")

# 3. mode r+, membuka file dan menimpa isi file sesuai dengan panjang data
with open("data_3.txt","w",encoding="utf-8") as file :
    file.write("data ke 3\n")

with open("data_3.txt","r+",encoding="utf-8") as file :
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt","r+",encoding="utf-8") as file :
    data = file.read()
    print(data)

with open("data_3.txt","r+",encoding="utf-8") as file :
    file.write("otong") # akan menimpa isi text dari file sesuai dengan jumlah karakter / panjang data yang menimpanya

