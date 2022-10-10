#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def read_data(file_name):
    with open(file_name, 'r') as data:
        return data.readline()

def write_data(file_name, text):
    with open(file_name, 'w') as data:
        return data.write(text)

def encode(data):
    result = str()

    if len(data) == 0:
        return result

    char = data[0]
    for i in range(1, len(data)):
        result = str(i) + char
        if data[i] != char:
            result += encode(data[i:])
            break
    else:
        result = str(i + 1) + char
                    
    return  result

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
