"""
Casting tipe data => mengubah dari suatu tipe data menjadi tipe data lain
"""

# Kita belajar Casting
# tipe data = int, float, str, bool

## INTEGER
print("="*5, "Integer", "="*5)
data_int = 9
print("data = ", data_int, ",type =", type(data_int))

# mengubah data_int menjadi data_float
data_float = float(data_int)
print("data = ", data_float, ",type =", type(data_float))

# mengubah data_int menjadi data_str
data_str = str(data_int)
print("data = ", data_str, ",type =", type(data_str))

# mengubah data_int menjadi data_bool
data_bool = bool(data_int)
print("data = ", data_bool, ",type =", type(data_bool))
# data_bool akan menjadi true apabila nilai yang dicasting adalah bukan nol sedangkan apabila nilai yang dicasting adalah nol maka akan menjadi false

## FLOAT
print("="*5, "Float", "="*5)
data_float = 9.5
print("data = ", data_float, ",type =", type(data_float))

# mengubah data_float menjadi data_int
data_int = int(data_float)
print("data = ", data_int, ",type =", type(data_int))
# hasil casting dari float ke int akan dibulatkan ke bawah

# mengubah data_float menjadi data_str
data_str = str(data_float)
print("data = ", data_str, ",type =", type(data_str))

# mengubah data_float menjadi data_bool
data_bool = bool(data_float)
print("data = ", data_bool, ",type =", type(data_bool))
# data_bool akan menjadi true apabila nilai yang dicasting adalah bukan nol sedangkan apabila nilai yang dicasting adalah nol maka akan menjadi false

## BOOLEAN
print("="*5, "Boolean", "="*5)
data_bool = True
print("data = ", data_bool, ",type =", type(data_bool))

# mengubah data_bool menjadi data_int
data_int = int(data_bool)
print("data = ", data_int, ",type =", type(data_int))
# True akan menghasilkan 1, false akan menghasilkan 0

# mengubah data_bool menjadi data_str
data_str = str(data_bool)
print("data = ", data_str, ",type =", type(data_str))
# True atau False akan menghasilkan teks

# mengubah data_bool menjadi data_float
data_float = float(data_bool)
print("data = ", data_float, ",type =", type(data_float))
# True akan menghasilkan 1,0, false akan menghasilkan 0.0

## STRING
print("="*5, "String", "="*5)
data_str = "10"
print("data = ", data_str, ",type =", type(data_str))

# mengubah data_str menjadi data_int
data_int = int(data_str)
print("data = ", data_int, ",type =", type(data_int))
# casting str ke int akan gagal apabila yang diinputkan bukan str angka seperti "7", "10" dsb

# mengubah data_str menjadi data_bool
data_bool = bool(data_str)
print("data = ", data_bool, ",type =", type(data_bool))
# casting dari str ke bool akan menghasilkan false ketika yang diinputkan adalah string kosong ("") selain itu akan true walaupun inputannya "False"

# mengubah data_str menjadi data_float
data_float = float(data_str)
print("data = ", data_float, ",type =", type(data_float))
# casting str ke float akan gagal apabila yang diinputkan bukan str angka seperti "7", "10" dsb
