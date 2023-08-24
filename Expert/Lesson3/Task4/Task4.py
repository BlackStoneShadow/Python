#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант. 
#*Верните все возможные варианты комплектации рюкзака.
things = {
    "плитка"            : 5.0,
    "нож"               : 0.2,
    "кастрюля"          : 0.5,
    "посуда"            : 0.3,
    "столовые приборы"  : 0.2,
    "кружка"            : 0.1,
    "мыло"              : 0.05,
    "полотенце"         : 0.2,
    "фонарик"           : 0.3,
    "компас"            : 0.2,
    "аптечка"           : 1.0,
    "продукты"          : 10.0
}

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

capacity = try_castinput("Enter max capacity:", float)

things, backpack = dict(sorted(things.items(), key=lambda x: x[1], reverse=True)), dict()

for item in things:
    backpack[item] = things[item]
    
    if sum(backpack.values()) > capacity:
        backpack.pop(item)

print(backpack)
print(f"Total:{sum(backpack.values())}")