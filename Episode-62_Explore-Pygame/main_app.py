"""
Pygame

Pygame adalah sebuah package library untuk membuat game dalam bahasa pemrograman python. Pygame ini dapat kita lihat dokumentasinya di pygame.org. Dalam membuat game dengan pygame terdapat beberapa langkah-langkah atau struktur gamenya diantaranya :
1. init => membuat dunia gamenya dan karakternya
2. user input, database input => perintah-perintah yang dimasukkan untuk bermain bisa dari stik ps, mouse, keyboard dsb
3. update asset => untuk melakukan update inventory semisal kalau di game
4. render ke display => ini proses paling berat dimana prosenya tuh ngerender tiga step sebelumnya yang akan menentukan besar fps gamenya
"""

import pygame

## init => inisiasi game
pygame.init() # untuk memulai gamenya namun akan secara otomatis ter-quit akibat tidak adanya main loop sehingga harus ditangkap main loopnya. Main loop ini berisi event-event yang dijalankan dalam gamenya. Namun, pada saat dijalankan akan tidak terlihat gamenya karena belum dikonfigurasi untuk ukuran window gamenya. pygame.init ini juga berfungsi untuk menjalankan engine gamenya

# mengatur variable running game sebagai close button untuk quit dari pygame sehingga ketika false akan menutup pygame
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))
# akan muncul sebuah window pygame namun tidak menampilkan apa-apa dan belum bisa di close sehingga perlu di terminate via terminal. Apabila sudah diatur kondisi quitnya dengan mengatur variable runnya sehingga ketika ada event close button di window pygamenya di klik maka keluar dari gamenya

# object game
# koordinat / posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

# menangkap main loopnya agar tidak otomatis ter-quit
while isRun :
    # membuat delay untuk mengatur fps
    pygame.time.delay(10)

    # menangkap event-event yang terjadi pada pygame window
    # user input, database input
    for event in pygame.event.get() :
        # apabila tipe event yang terjadi adalah quit maka break
        if event.type == pygame.QUIT :
            # print("YOTOOONG komiing") # untuk menandakan event quit sukses terjadi yaitu ketika melakukan klik pada close button di window pygame akan menampilkan ini
            isRun = False # mengubah state isRun untuk menutup window pygame

        # ambil semua keyboard press
        keys = pygame.key.get_pressed() # mengambil semua hasil inputan dari keyboard dan disimpan pada variabel keys

        # ambil ke kiri (button press arrow left pd keyboard)
        # karena keys yang dihimpu merupakan dictionary maka ketika keysnya adalah arrow kiri maka kotak akan bergerak ke kiri sejauh speed sehingga setiap satu kali klik arrow kiri posisi kota akan berubah secara sumbu-x ke kiri sebanyak nilai speed step
        if keys[pygame.K_LEFT] and x > 0 :
            x -= speed

        # sama seperti arrow kiri, ketika arrow kanan di klik maka memindahkan kotak ke kanan sejauh nilai speed step
        if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
            x += speed

        # sama seperti arrow kanan, ketika arrow bawah di klik maka memindahkan kotak ke bawah sejauh nilai speed step
        if keys[pygame.K_DOWN] and y < window_panjang - panjang:
            y += speed

        # sama seperti arrow bawah, ketika arrow atas di klik maka memindahkan kotak ke atas sejauh nilai speed step
        if keys[pygame.K_UP] and y > 0 :
            y -= speed

        # game dynamic

        # update asset
        # membuat layar background window jadi warna putih
        window.fill((255,255,255)) # nilai warnanya berdasarkan hex
        # membuat kotak dengan method rect
        pygame.draw.rect(window, (255,120,0),(x,y,lebar,panjang)) # dalam sintaks ini penjelasan parameternya diantaranya : window yaitu sebagai alamat untuk menempatkan gambar rectangle ini di window, (255,120,0) adalah warna untuk rectangle yang dibuat berdasarkan (r,g,b), (x,y,lebar,panjang) untuk menentukan posisi serta ukuran dari rectanglenya

        # render ke display
        pygame.display.update() # untuk menerapkan update display setelah dilakukan edit
pygame.quit()