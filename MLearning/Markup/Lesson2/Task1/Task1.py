import os
import json
from pathlib import Path
from module import controller

data = []
for item in controller.Toscrape():
    os.system("cls")
    print(f"page:{item.page}")
    data.append(item.books)

with open(Path().cwd() / "list.json", "w", encoding="utf-8") as f:                
    json.dump(data, f, ensure_ascii=False)         
