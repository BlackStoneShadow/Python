#✔ Три друга взяли вещи в поход. 
#Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
#Ответьте на вопросы:
#✔ Какие вещи взяли все три друга
#✔ Какие вещи уникальны, есть только у одного друга
#✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
freinds = {
    "Петя": ("плитка", "нож", "кастрюля"),
    "Ваня": ("посуда", "нож", "кружка"),
    "Дима": ("кружка", "нож", "компас", "фонарик")
    #,"Вася": ("лодка", "нож", "компас", "кружка")        
    }

print(freinds)

#✔ Какие вещи взяли все три друга
items = iter(freinds.values())
things_common = set(next(items))
for item in items:
    things_common = set.intersection(things_common, set(item))

print(f"все друзья взяли:{things_common}")

#✔ Какие вещи уникальны, есть только у одного друга
things_unique = dict()
for i in range(len(list(freinds))):    
    differen = set()

    for j in range(len(list(freinds))):
        if i != j:
            differen = differen.union(set(freinds[list(freinds)[i]]).difference(set(freinds[list(freinds)[j]])))    

    for item in differen:
        if item in things_unique:
            things_unique[item] += 1
        else:
            things_unique[item] = 1

things_unique = set(key for key, value in things_unique.items() if value == 1)

print(f"есть только у одного:{things_unique}")

#✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
things_count = dict()

for i in range(len(list(freinds))):
    for j in range(i + 1, len(list(freinds))):
        common = tuple(set.difference(set(freinds[list(freinds)[i]]).intersection(set(freinds[list(freinds)[j]])), things_common))
        if common in things_count:
            things_count[common] += 1
        else:
            things_count[common] = 2

#у всех друзей кроме одного => count == len(freinds) - 1
things_one = set(next(key for key, value in things_count.items() if value == len(freinds) - 1))
#поиск множества без найденной вещи
things_key = tuple(key for key, value in freinds.items() if not things_one.issubset(set(value)))

print(f"{things_one} есть у всех кроме {things_key}")        