import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from typing import TypeVar
from typing import List
from pprint import pprint

class Toscrape:
    def __init__(self, **kwarg):
        self.__page__ = 0
        self.__session__ = None

    def _response_(self, url):
        if (self.__session__ == None):
            self.__session__ = requests.session()

        return self.__session__.get(url, headers = {"User-Agents": UserAgent().chrome,})


    def __iter__(self):
        return self

    def __next__(self):        
        self.__page__ += 1

        self.__response__ = self._response_(self.url + f"page-{self.__page__}.html")

        if self.text == None:
            raise StopIteration

        return self

    @property
    def url(self)->str:
        return "http://books.toscrape.com/catalogue/"

    @property
    def status(self)->bool:
        return self.__response__.ok

    @property
    def page(self)->int:
        return self.__page__

    @property
    def text(self)->str:
        if self.status:
            return self.__response__.text

    @property
    def data(self):
        if self.status:
            soup = BeautifulSoup(self.text, features="html.parser")
            return soup.find_all(name="li", attrs={'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})        

    @property
    def books(self)->List[TypeVar(str, str, int, str, str)]:
        result = []
        if self.status:
            for item in self.data:
                book = item.find(name="article", attrs={'class':'product_pod'})                
                link = self.url + book.find(name="h3").find(name='a').get("href")
                
                response = self._response_(link)
                content = BeautifulSoup(response.text, features="html.parser").find(name="div", attrs={'id':'content_inner'})                
                
                result.append({
                    "name": book.find(name="h3").find(name='a').get("title").strip(), 
                    "price": book.find(name="p", attrs={'class':'price_color'}).get_text().strip(),
                    "count": int(re.search("\d+", content.find(name="p", attrs={'class':'instock availability'}).get_text().strip())[0]),
                    "description": content.find(name="div", attrs={'id':'product_description'}).find_next("p").get_text().strip() if content.find(name="div", attrs={'id':'product_description'}) else None,                    
                    "link": link,
                    })

        return result

if __name__ == "__main__":        
    for item in Toscrape():
        pprint(item.books)