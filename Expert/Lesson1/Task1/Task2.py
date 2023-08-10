#2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
#Дано a, b, c - стороны предполагаемого треугольника. 
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

a = try_castinput("Input side a:", int)
b = try_castinput("Input side b:", int)
c = try_castinput("Input side c:", int)

#result = [1]
#for i in range(1, int(number)):
#    result.append(result[i - 1] * (i + 1))

print(f"{a}, {b}, {c}")