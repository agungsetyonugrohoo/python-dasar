# latihan konversi satuan temperature

# program konversi reamur ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
reamur = float(input('Masukkan suhu dalam reamur : '))
print('suhu adalah', reamur, 'Reamur')

# celcius
# rumus konversi = (5/4) * reamur
celcius = (5/4) * reamur
print('suhu dalam celcius adalah', celcius, 'Celcius')

# fahrenheit
# rumus konversi = (9/4) * reamur + 32
fahrenheit = ((9/4) * reamur) + 32
print('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

# kelvin
# rumus konversi = (5/4) * reamur + 273
kelvin = ((5/4) * reamur) + 273
print('suhu dalam kelvin adalah', kelvin, 'Kelvin')