import json
import hashlib
import pandas as pd
from pprint import pprint
from pathlib import Path
from clickhouse_driver import Client

class Books:
    def __init__(self, **kwarg):                
        self.__client__ = Client(host = kwarg["host"], port=kwarg["port"], user="default", secure=False, settings={'use_numpy': True})
        self.__client__.execute("DROP TABLE IF EXISTS books")
        self.__client__.execute('''
        CREATE TABLE books
        (
            `id`    UInt16,
            `name`  String,
            `count` UInt16,
            `price` String
        )
        ENGINE = MergeTree
        ORDER BY id;
        ''')

    def load(self, fileName):                
        with open(Path().cwd() / fileName, "r") as f:                
            count = 0
            books = json.load(f)            
            for item in books:                 
                book = pd.DataFrame([
                        [int(hashlib.md5(item[0]["name"].encode("utf-8")).hexdigest()[:8], 16), item[0]["name"], item[0]["count"], item[0]["price"]]
                    ],
                    columns = ["id", "name", "count", "price"])
                try:                                                                                                            
                    self.__client__.insert_dataframe(f"INSERT INTO books VALUES", book)    
                    
                    count += 1
                except Exception as e:
                    pass
        print(f"load {count} out of {len(books)} books")

    def execute(self, query):
        return self.__client__.execute(query)

if __name__ == "__main__":
    books = Books(host="ubuntu", port=9000)    
    books.load("list.json")

    for item in books.execute("SELECT * FROM books"):
        pprint(item)

    for item in books.execute("SELECT MAX(count), AVG(count) FROM books"):
        pprint(item)