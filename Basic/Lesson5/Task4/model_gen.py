#алгоритм основанный на генераторе
from itertools import groupby

def encode(data):                          
    return str().join(['{}{}'.format(len(list(items)), char) for char, items in groupby(data)])

def decode(data):    
    return str().join(map(lambda item: item[0] * int(data[item[1] - 1]), [(char, index) for index, char in enumerate(data) if not char.isdigit()]))
    #Вариант для разбора более 9 повтров символа
    #data = ' ' + data
    #items = list([(char, index) for index, char in enumerate(data) if not char.isdigit()]) 
    #return str().join(map(lambda index: items[index][0] * int(data[items[index - 1][1] + 1:items[index][1]]), [index for index in range(1, len(items))]))   
