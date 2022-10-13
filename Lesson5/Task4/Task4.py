#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#from model_rec import encode
from model_gen import encode

def read_data(file_name):
    with open(file_name, 'r') as data:
        return data.readline()

def write_data(file_name, text):
    with open(file_name, 'w') as data:
        return data.write(text)

def decode(data):
    result = str()
    number = str()

    if not data: return str()

    for char in data:
        if char.isdigit():
            number += char
        else:
            result += char * int(number)
            number = str()

    return result

write_data('FileEncode.txt', encode(read_data('FileDecode.txt')))
write_data('FileDecode.txt', decode(read_data('FileEncode.txt')))
