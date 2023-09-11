#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#где ключ — значение переданного аргумента, а значение — имя аргумента.
#Если ключ не хешируем, используйте его строковое представление.
def convert(**kwargs):
  result = dict()
  for key, item in kwargs.items():
    result[item if hash(item) is not None else str(item)] = key
  return result

print(convert(auto='BMW', volume=4.4, year=1981))