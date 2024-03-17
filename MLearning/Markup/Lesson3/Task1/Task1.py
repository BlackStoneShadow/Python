import json
from pprint import pprint
from pathlib import Path
from pymongo import MongoClient

class Books:
    def __init__(self, **kwarg):                
        self.__db__ = MongoClient(kwarg["connectStr"]).lesson3

    def load(self, fileName):                
        with open(Path().cwd() / fileName, "r") as f:                
            count = 0
            books = json.load(f)            
            for item in books: 
                book = item[0]
                try:        
                    self.__db__.books.insert_one(book)    
                    count += 1
                except Exception as e:
                    pass
        print(f"load {count} out of {len(books)} books")

    def find(self, query):
        return self.__db__.books.find(query)

if __name__ == "__main__":
    books = Books(connectStr="mongodb://192.168.1.99:27017")    
    books.load("list.json")

    for item in books.find({"name": {"$regex":"[Ll]ight"}}):
        pprint(item)

    for item in books.find({"count": {"$gt":10, "$lt": 15}}):
        pprint(item)