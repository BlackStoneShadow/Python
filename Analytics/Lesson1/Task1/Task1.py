#отфильтровать словарь по ключам
def filter(dic, key):
  return {k: v for k, v in dic.items() if k in key}
  
dic = filter({
	"name": "John",
	"age": 25,
	"salary": 5000,
	"city": "Moscow"
}, ["name", "age"])

print(dic)