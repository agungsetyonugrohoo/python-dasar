from . import matematika # fungsinya untuk menempelkan atau mendefinisikan fungsi matematika dalam folder package yaitu sains untuk dapat dilakukan import sains sehingga tidak perlu menjadi sains.matematika karena proses import matematika sudah dilakukan di init. Dalam percobaan subpackage, subpackage matematika belum sepenuhnya dapat digunakan dikarenakan belum adanya penyambung dengan module-module di dalam subpackage matematika
from . import pisika # sama seperti matematika, dilakukan pendefinisian attribute module yang dapat digunakan dari import sains. Untuk tanda "." merujuk pada package yaitu sains
# # from .matematika import kali # ini merujuk pada spesifik fungsi pada module matematika yaitu kali untuk dapat dipanggil atau digunakan melalu package sehingga penggunaannya hanya dengan sains.kali yang dimana menghubungkan fungsi spesifik kali dari module matematika dengan package sains

# untuk memudahkan melakukan import module dari package atau subpackage dapat menggunakan keyword __all__ dengan melakukan list module atau subpackage apa saja yang akan digunakan

# __all__ = [
#     "matematika", # ini merupakan subpackage dalam package sains
#     "pisika" # ini adalah module dalam package sains
# ]

# __all__ ini hanya berfungsi untuk from sains import * (hal ini dikarenakan "*" dimaksudkan unutuk mencari __all__) apabila hanya import sains akan error karena attribute matematika tidak kenali oleh sains namun bisa di atasi dengan melakukan from . import matematika dan from . import pisika

# namun __all__ tidak disarankan karena tidak eksplisit