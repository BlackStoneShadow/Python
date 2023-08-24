#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
#Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
import re
import unicodedata
import urllib.request
from typing import Dict

def load(url: str) -> str:
    article = urllib.request.urlopen(url)

    text = article.read().decode("utf-8")
    
    return re.sub(r"[^А-яё]", " ", text, flags=re.S)

def parse(text: str) -> Dict[str, int]:
    result = dict()

    words = text.split()
    words.sort()

    for word in words:
        if len(word) > 3:        
            word = word.lower()
            if word in result:
                result[word] = result[word] + 1
            else:
                result[word] = 1

    return result
#Python
print("Python\n", sorted(parse(load("https://ru.wikipedia.org/wiki/Python")).items(), key=lambda x: x[1], reverse=True)[:10])
#CSharp
print("CSharp\n",sorted(parse(load("https://ru.wikipedia.org/wiki/C_Sharp")).items(), key=lambda x: x[1], reverse=True)[:10])