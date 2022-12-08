# latihan konversi satuan temperature

# program konversi fahrenheit ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print('suhu adalah', fahrenheit, 'Fahrenheit')

# celcius
# rumus konversi = (5/9) * (fahrenheit - 32)
celcius = (5/9) * (fahrenheit - 32)
print('suhu dalam celcius adalah', celcius, 'Celcius')

# reamur
# rumus konversi = (4/9) * (fahrenheit - 32)
reamur = (4/9) * (fahrenheit - 32)
print('suhu dalam reamur adalah', reamur, 'Reamur')

# kelvin
# rumus konversi = (5/9 * (fahrenheit - 32)) + 273
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print('suhu dalam kelvin adalah', kelvin, 'Kelvin')