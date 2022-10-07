#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.
def read_data(file_name):
    with open(file_name, 'r') as data:
        return data.readline()

def write_data(file_name, text):
    with open(file_name, 'w') as data:
        return data.write(text)

def set_operand(fun):
    result = list()

    for operand in fun.split('+'):        
        operand = operand.replace('x ', 'x^1').replace(' = ', 'x^0')
        result.append(reversed(list(map(lambda item: int(item), operand.split('x^')))))
        
    return dict(result)

def get_operand(num, pwr):
    if pwr == 0:
        return str(num)
    elif pwr == 1:
        return str(num) + "x"
    else:
        return str(num) + "x^" + str(pwr)

def sum_operand(fun1, fun2):
    result = dict()

    for i in range(max(len(fun1), len(fun2)) - 1, -1, -1):
        a , b = 0, 0
        if i in fun1.keys():
            a = fun1[i]
        if i in fun2.keys():
            b = fun2[i]        
        
        result[i] = a + b

    return result

fun1 = read_data('File1.txt')
fun2 = read_data('File2.txt')

list_operands = [get_operand(num, pwr) for pwr, num in sum_operand(set_operand(fun1), set_operand(fun2)).items()]

result = " + ".join(list_operands) + ' = 0'

write_data('File3.txt', result)
