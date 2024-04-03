import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait 
from selenium.webdriver.support.wait import T
from typing import TypeVar
from typing import List
from pprint import pprint
import time

class Scrapy:
    def __init__(self, **kwarg):
        self.__page__ = 0
        self.__driver__ = None

        driver = self.driver(self.url)                        

        search_box = self.element_xpath('//input[@id="searchInput"]')        

        search_box.send_keys(kwarg["Search"])
        search_box.send_keys(Keys.ENTER)

        pass

    def __del__(self):
        self.__driver__.quit()        

    def __str__(self)->str:        
        return str(self.__driver__.page_source)        

    def __iter__(self):
        return self

    def __next__(self):        
        self.__page__ += 1

        next_button = self.element_xpath('//a[@class="pagination-next pagination__next j-next-page"]')

        if next_button is None:
            raise StopIteration

        next_button.click()                                

        return self

    def driver(self, url:str)->T:
        if (self.__driver__ is None):
            options = Options()            
            #options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
            options.add_argument("start-maximized")

            self.__driver__ = webdriver.Chrome(options=options)
            self.__driver__.get(self.url)            

        return self.__driver__        

    def element_xpath(self, value:str)->T:
        try:
            if self.status:            
                return WebDriverWait(self.__driver__, 3).until(EC.presence_of_element_located((By.XPATH, value)))        
        except:
            return None                

    @property
    def url(self)->str:        
        return "https://www.wildberries.ru/"

    @property
    def status(self)->bool:        
        return False if str(self) is None else True            

    @property
    def page(self)->int:
        return self.__page__

    @property
    def data(self):
        if self.status:
            soup = BeautifulSoup(str(self), features="html.parser")
            root=soup.find(name="html")
            return soup.find_all(name="div", attrs={'class':'product-card__wrapper'})                    

    @property
    def links(self)->List[TypeVar(str, str, str)]:
        result = []        

        while True:
            items = self.__driver__.find_elements(By.XPATH, '//div[@class="product-card__wrapper"]')
            count = len(items)
            self.__driver__.execute_script("window.scrollBy(0, 1000)")
            time.sleep(1)
            items = self.__driver__.find_elements(By.XPATH, '//div[@class="product-card__wrapper"]')

            if len(items) == count:
                break
            exist = set()
            for item in self.data:                
                name = item.find(name="span",attrs={'class':'product-card__name'}).get_text().replace("/", "").strip()                
                link = item.find(name="a",attrs={'class':'product-card__link j-card-link j-open-full-product-card'}).get("href")
                try:
                    price = float(item.find(name="ins",attrs={'class':'price__lower-price'}).get_text().replace(u"\xa0", u"").strip()[:-1])
                except ValueError as E:
                    price = None

                if link not in exist:
                    result.append({
                        "name": name, 
                        "price": price,
                        "url": link,
                        })
                    exist.add(link)

        return result

if __name__ == "__main__":        
    for item in Scrapy(Search="IPhone 15 Pro MAX"):
        pprint(item.links)