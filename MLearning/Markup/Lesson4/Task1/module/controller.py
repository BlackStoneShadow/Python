import re
import requests
from fake_useragent import UserAgent
from typing import TypeVar
from typing import List
from pprint import pprint
from lxml import html
from datetime import datetime
from datetime import timedelta

class CBR:
    def __init__(self, **kwarg):
        self.__page__ = 0
        self.__session__ = None

        self.__dateBegin__ = self.__date__ = datetime.strptime(kwarg["dateBegin"], "%d.%m.%Y")
        self.__dateEnd__ = datetime.strptime(kwarg["dateEnd"], "%d.%m.%Y")

    def _response_(self, url):
        if (self.__session__ == None):
            self.__session__ = requests.session()

        return self.__session__.get(url, 
                                    headers = {"User-Agents": UserAgent().chrome,}, 
                                    params = {"UniDbQuery.Posted": "True", 
                                              "UniDbQuery.To": self.__date__,})

    def __iter__(self):
        return self

    def __next__(self):                
        self.__response__ = self._response_(self.url)        
        
        if self.__date__ == self.__dateEnd__:
            raise StopIteration        

        self.__date__ += timedelta(days=1)

        return self

    @property
    def url(self)->str:
        return "https://www.cbr.ru/currency_base/daily/"

    @property
    def status(self)->bool:
        return self.__response__.ok

    @property
    def date(self)->datetime:
        return self.__date__

    @property
    def text(self)->str:
        if self.status:
            return self.__response__.text

    @property
    def data(self):
        if self.status:            
            tree = html.fromstring(self.text)    
            return tree.xpath("//table[@class='data']//descendant::tr")        

    @property
    def price(self)->List[TypeVar(int, str, int, str, float)]:
        result = []
        if self.status:
            iiter = iter(self.data)
            next(iiter)
            for item in iiter:
                try:
                    result.append({
                        "id"    : int(item[0].text),
                        "code"  : str(item[1].text),
                        "unit"  : int(item[2].text),
                        "name"  : str(item[3].text),
                        "price" : float(item[4].text.replace(",", ".")),
                        "date"  : self.date.strftime("%d.%m.%Y"),
                        })
                except ValueError as error:
                    result.append({
                        "id"    : int(item[0].text),
                        "code"  : str(item[1].text),
                        "date"  : self.date.strftime("%d.%m.%Y"),
                        "name"  : error,
                        })

        return result

if __name__ == "__main__":        
    for item in CBR(dateBegin="01.01.2024", dateEnd="31.01.2024"):
        pprint(item.price)