x = str()
y = str()

def init(a, b):
    global x
    global y
    x = a
    y = b

def parse(data):

    data = data.replace(" ", "")
    for n, x in enumerate(data):
        if x == "+" or x == "-":
            data_real = data[:n]
        elif x == "i":
            data_complex = data[len(data_real)+1:len(data)-1]
    return float(data_real), float(data_complex)

def sum():
    list1 = parse(x)
    list2 = parse(y)

    real =  list1[0] +  list2[0]
    complex =  list1[1] + list2[1]
    return f'{real} + {complex} * i'
   
def sub():
    list1 = parse(x)
    list2 = parse(y)

    real =  list1[0] -  list2[0]
    complex =  list1[1] - list2[1]
    return f'{real} + {complex} * i'

def div():
    list1 = parse(x)
    list2 = parse(y)

    real =  list1[0] +  list2[0]
    complex =  list1[1] + list2[1]
    return f'{real} + {complex} * i'

def mult():
    list1 = parse(x)
    list2 = parse(y)

    real =  list1[0] * list2[0] - list1[1] * list2[1] 
    complex =  list1[0] * list2[1] + list2[0] * list1[1]

    return f'{real} + {complex} * i'

