import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from urllib.parse import urljoin
from ..items import UnsplashItem


class ImagesSpider(CrawlSpider):
    name = "images"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]
    #порядок следования правил имеет значение, если поменть местами  пропустим первую страницу
    rules = (        
        Rule(LinkExtractor(restrict_xpaths='//figure[@itemprop="image"]//child::a[@itemprop="contentUrl"]'), callback="parse_item", follow=True),
        Rule(LinkExtractor(allow=r"t/")),
    )    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse_class(self, response: HtmlResponse):
        self._class_ = response.url.split("/")[-1]

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashItem(), selector=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath(field_name='name', xpath='//div[@data-test="photos-route"]//child::h1[@class]/text()')                    
        loader.add_xpath(field_name='image_urls', xpath='//div[@data-test="photos-route"]//child::img[@sizes]/@srcset')                    
        loader.add_value(field_name='url', value=response.url)
        loader.add_value(field_name='kind', value=response.url)

        yield loader.load_item()
