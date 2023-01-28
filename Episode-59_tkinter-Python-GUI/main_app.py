"""
Tkinter adalah standard library yang ada di python yang fungsinya untuk pengenalan tentang Graphical User Interface (GUI). Selain Tkinter, GUI Python adalagi diantaranya PyQt dan PyGame.

Cara membuat GUI di tkinter :
1. Membuat variabel untuk menampung aplikasi GUI yang akan dibuat, example : window
2. Membuat object beserta factorynya melalui library tkinter, example : window = tk.Tk()
3. Membuat variabel app melakukan looping secara terus menerus dan akan berhenti ketika di close, example : window.mainloop()
4. Setelah itu, buat frame untuk menampung konten yang ingin diisi pada window
"""

# GUI -> Graphical User Interface

import tkinter as tk # mengaliaskan pemanggilan library tkinter dengan tk (biasanya)
from tkinter import ttk # untuk mengubah tema dari subwindow / sekunder window
from tkinter.messagebox import showinfo # untuk membuat messagebox dalam fungsi showinfo

# init
window = tk.Tk() # menginisiasi pembuatan GUI app window
window.configure(bg="white") # melakukan konfigurasi terhadap layar window baik dari warna background dsb
window.geometry("300x200") # untuk melakukan konfigurasi terhadap ukuran window
window.resizable(False, False) # untuk membuat window tidak bisa di resize baik dari sumbu-x (parameter-1) dan sumbu-y (parameter-2)
window.title("Sapa Dia!") # mengubah judul program

# Variabel data (textvariable) dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# fungsi action ketika tombol di klik
def tombol_click() :
    '''fungsi ini akan dipanggil oleh tombol'''
    # print("Ucup ganteeeng beuds")
    # print(NAMA_BELAKANG.get()) # untuk menampilkan isi dari variabel NAMA_BELAKANG. Dan alasan mengapa menggunakan stringVar() adalah agar mudah untuk diproses karakter inputnya
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!" # sebagai template dalam menampilkan pesan pada showinfo
    showinfo(title="Whazzup",message=pesan)

# membuat frame input
input_frame = ttk.Frame(window) # membuat frame yang ditempatkan di window
# jenis penempatan frame ada 3 diantaranya Grid, Pack dan Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True) # mengatur layout frame berdasarkan padding sb-x dan sb-y dengan fillnya yaitu horizontal dari kiri ke kanan dan bisa di expand

# komponen-komponen pada frame
# input pertama : 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan :") # membuat label dengan menempatkannya pada input_frame yang memiliki text "Nama Depan :"
nama_depan_label.pack(padx=10, fill="x",expand=True) # menampilkan label dengan ukuran tertentu sesuai dengan framenya
# input kedua : 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN) # untuk membuat textbox  pada input_frame untuk dapat diisi oleh karakter tertentu dan menyimpan isinya (textvariable) pada variabel tertentu dalam hal ini adalah NAMA_DEPAN
nama_depan_entry.pack(padx=10, fill="x",expand=True) # untuk menampilkan textboxnya pada frame
# input pertama : 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang :") # membuat label dengan menempatkannya pada input_frame yang memiliki text "Nama belakang :"
nama_belakang_label.pack(padx=10, fill="x",expand=True) # menampilkan label dengan ukuran tertentu sesuai dengan framenya
# input kedua : 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG) # untuk membuat textbox  pada input_frame untuk dapat diisi oleh karakter tertentu dan menyimpan isinya (textvariable) pada variabel tertentu dalam hal ini adalah NAMA_BELAKANG
nama_belakang_entry.pack(padx=10, fill="x",expand=True) # untuk menampilkan textboxnya pada frame
# 5. input Tombol untuk bisa di klik
tombol_sapa = ttk.Button(input_frame, text="Sapa Dia!",command=tombol_click) # membuat tombol untuk bisa diklik yang dimana akan menjalankan suatu fungsi melalui command
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10) # menampilkan tombol pada window

# Main Loop Window()
window.mainloop() # untuk melakukan looping terhadap window yang sudah dibuat sehingga tidak akan otomatis close apabila di jalankan dan akan close ketika di click pada bagian exit pada jendela app yang sudah dibuat