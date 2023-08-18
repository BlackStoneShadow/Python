#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.def printable(start: int, end: int):
    for i in range(1, 11):
        for j in range(start, end):
            print(f"{j} x {i} = {j*i}", end='\n' if j == end - 1 else '\t')

printable(2, 6)
print()
printable(6, 10)
