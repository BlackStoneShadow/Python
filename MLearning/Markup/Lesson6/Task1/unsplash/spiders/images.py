import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..items import UnsplashItem


class ImagesSpider(CrawlSpider):
    name = "images"
    allowed_domains = ["unsplash.com"]

    rules = (Rule(LinkExtractor(allow=r"t/"), callback="parse_item", follow=True),)    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        query = kwargs.get("query") if kwargs.get("query") is not None else str()

        self.start_urls = [f"https://unsplash.com/{query}"]

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashItem(), respone=response)
        loader.default_input_processor = MapCompose(str.strip)

        yield loader.load_item()
