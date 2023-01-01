"""
Dictionary (dict) -> data collection dalam bentuk associative array yang dimana setiap data yang ditampung memiliki identifier (key) yang merujuk pada sebuah data (value). Identifier ini dianalogikan sebagai index apabila di list

Berbeda dengan list yang dapat mengakses datanya menggunakan index, dictionary menggunakan keynya sebagai rujukan terhadap data yang dituju untuk dapat diakses

Dictionary ini sangat berguna untuk sebuah data collection yang memiliki struktur tertentu

Cara membuat dictionary :
dictionary = {
    key1 : value1,
    key2 : value2,
    ...
}

Cara mengakses datanya dengan menggunakan key:
dictionary['key1']
"""

# list -> data collection dalam bentuk array, cara mengakses datanya dengan menggunakan index
data_list = ['ucup','otong','dudung']
print(data_list[0]) # mengakses data pada index-1

# dictionary (dict) -> associative array
# identifier -> key
data_dict = {
    # 'key1':'value1',
    # 'key2':'value2'

    'key':'value',
    'cp':'ucup',
    'tg':'otong',
    'dg':'dudung',
    'nmbr':100,
    'list':data_list
}

print(data_dict) # menampilkan seluruh data dalam dictionary

# mengakses sebuah data dalam dictionary dengan key
print(data_dict['tg']) # mengakses data string dict
print(data_dict['nmbr']) # mengakses data number dict
print(data_dict['list'])

