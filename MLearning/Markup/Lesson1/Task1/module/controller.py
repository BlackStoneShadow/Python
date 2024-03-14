import os
import requests

class Foursquare:   
    def __init__(self, **kwarg):
        url = "https://api.foursquare.com/v3/places/search"

        headers = {    
            "accept":"application/json",
            "Authorization": kwarg["API_KEY"],
        }

        params = {      
            "query":kwarg["category"],
            "near":"Moscow",
            "sort":"RATING",
            "fields":"fsq_id,name,rating,location",
        }

        self.__response__ = requests.get(url, params = params, headers = headers)
    
    @property
    def status(self)->bool:
        return self.__response__.ok

    @property
    def text(self)->str:
        return self.__response__.text

    @property
    def data(self):
        return self.__response__.json()["results"]

if __name__ == "__main__":    
    foursquare = Foursquare(API_KEY=os.getenv("API_KEY"), category="coffee")
    if(foursquare.status):          
        pprint(foursquare.data)