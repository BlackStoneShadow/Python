#На складе лежат разные фрукты в разном количестве.
#Нужно написать функцию, которая на вход принимает любое количество названий фруктов и их количество, 
##а возвращает общее количество фруктов на складе
def amount(**items):
    return sum(items.values())

print(f"amount of fruit:{amount(apple=10, orange=15, peach=5)}")