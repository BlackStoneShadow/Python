import re
import scrapy
from scrapy.http import HtmlResponse
from datetime import datetime

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['ru.investing.com']
    start_urls = ['https://ru.investing.com/news/economy']    

    def parse(self, response:HtmlResponse):        
        next = response.xpath('//span[@class="hidden sm:block" and text()="След."]//parent::a/@href').get()
        if next:
            yield response.follow(next, callback=self.parse)

        items = response.xpath('//div/a[contains(@class, "text-secondary")]')
        for item in items:
            name = item.xpath(".//text()").get()
            link = item.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_article, meta={
                    "article_name": name,
                    })

    def parse_article(self, response:HtmlResponse):
        try:
            text = response.xpath('//h1[@id="articleTitle"]//parent::div//span[contains(text(), "Опубликовано")]').get()
            date = datetime.strptime(re.search("\d{2}.\d{2}.\d{4}", text)[0], "%d.%m.%Y")
        except ValueError as e:
            date = None
        
        try:
            text = response.xpath('.//div[@id="article"]//child::p/text()').getall()
            text = str().join(_ for _ in text).strip()
        except ValueError as e:
            text = None            
        
        yield {
            "date"    : date,
            "article" : response.request.meta["article_name"],
            "text"    : text,
        }