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

side = tuple([try_castinput("Input side a:", int), try_castinput("Input side b:", int), try_castinput("Input side c:", int)])

for i in range(len(side)):    
    sum = 0
    for j in range(len(side)):        
        if i != j:
            sum += side[j]
    if side[i] > sum:
        input("Треугольник не существует")
        exit()

message = 'Треугольник разносторонний'                               

for i in range(1, len(side)):    
    if (side[i-1] == side[i]):
        if message == "Треугольник равнобедренный":
            message = "Треугольник равносторонний"                      
        else:
            message = "Треугольник равнобедренный"                      

input(message)