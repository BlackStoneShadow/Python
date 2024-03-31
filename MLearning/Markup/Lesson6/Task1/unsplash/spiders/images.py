import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from urllib.parse import urljoin
from ..items import UnsplashItem


#class ImagesSpider(CrawlSpider):
class ImagesSpider(Spider):
    name = "images"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]
    #порядок следования правил имеет значение, если поменть местами  пропустим первую страницу
    #попытка использовать Rusles для обхода категорий не принесла успеха, все изображения грузились из раздела photos
    #пришлось перейти на стандартный шаблон spider
    #rules = (                
    #    Rule(LinkExtractor(restrict_xpaths='//figure[@itemprop="image"]//child::a[@itemprop="contentUrl"]'), callback="parse_item", follow=True),        
    #    Rule(LinkExtractor(allow=r"t/"), callback="parse", follow=True),
    #)    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, response: HtmlResponse):
        links = response.xpath('//header/following::li/a[@class!="jTN_l"]')
        
        for link in links:
            yield response.follow(link, callback=self.parse_items)

    def parse_items(self, response: HtmlResponse):
        part =  response.url.split('/')
        kind = part[4] if len(part) > 4 else None

        if kind:
            links = response.xpath('//figure[@itemprop="image"]//child::a[@itemprop="contentUrl"]')
        
            for link in links:
                yield response.follow(link, callback=self.parse_item, meta={"kind": kind})                

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashItem(), selector=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath(field_name='name', xpath='//div[@data-test="photos-route"]//child::h1[@class]/text()')                    
        loader.add_xpath(field_name='image_urls', xpath='//div[@data-test="photos-route"]//child::img[@sizes]/@srcset')                    
        loader.add_value(field_name='url', value=response.url)
        loader.add_value(field_name='kind', value=response.meta["kind"])

        yield loader.load_item()
