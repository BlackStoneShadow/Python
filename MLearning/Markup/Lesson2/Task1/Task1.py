import json
from pathlib import Path
from module import controller

with open(Path().cwd() / "list.json", "x", encoding="utf-8") as f:            
    for item in controller.Toscrape():
        print(f"page:{item.page}")
        json.dump(item.books, f, ensure_ascii=False)
        for item in item.books:
            print(f"Name\t\t:{item['name']}")
            print(f"Price\t\t:{item['price']}")
            print(f"Count\t\t:{item['count']}")
            print(f"Description\t:{item['description']}")
