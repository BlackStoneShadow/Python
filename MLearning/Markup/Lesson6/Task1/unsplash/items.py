from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst, MapCompose

def process_image(value:str)->str:        
    index = [v[:-1] for k,v in enumerate(value.split()) if k % 2 != 0]
    value = [v for k,v in enumerate(value.split()) if k % 2 == 0]

    data = {k:v for k,v in zip(index, value)}

    result = data.get("1470w")

    if result is None:
        result = value[-1] 

    return result

class UnsplashItem(Item):    
    name = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())    
    kind = Field(output_processor=TakeFirst(),)    
    image_urls = Field(input_processor=MapCompose(process_image))    
    path = Field(output_processor=TakeFirst())
