import os
import json
from pathlib import Path
from module import controller

with open(Path().cwd() / "list.json", "w") as f:                
    json.dump([], f)         
    for item in controller.Toscrape():
        os.system("cls")
        print(f"page:{item.page}")        
       
        f.seek(0, os.SEEK_END)
        f.seek(f.tell()-1, os.SEEK_SET)
        f.truncate()
        if f.tell() > 1:
            f.write(',')
        json.dump(item.books, f)
        f.write(']')