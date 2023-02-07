import random
import string

# mengenerate nilai string random untuk digunakan pada prime key dengan anotation parameter input berupa int dan output berupa str
def random_string(panjang:int) -> str :
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang)) # membuat unik key untuk prime key berdasarkan huruf abjad acak sebanyak 6 karakter
    return hasil_string