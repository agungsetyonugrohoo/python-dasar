# latihan konversi satuan temperature

# program konversi kelvin ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
kelvin = float(input('Masukkan suhu dalam kelvin : '))
print('suhu adalah', kelvin, 'Kelvin')

# celcius
# rumus konversi = kelvin - 273
celcius = kelvin - 273
print('suhu dalam celcius adalah', celcius, 'Celcius')

# reamur
# rumus konversi = (4/5) * (kelvin - 273)
reamur = (4/5) * (kelvin - 273)
print('suhu dalam reamur adalah', reamur, 'Reamur')

# fahrenheit
# rumus konversi = (5/9 * (kelvin - 32)) + 273
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')