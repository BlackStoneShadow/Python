import hashlib
from scrapy.http import Request
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline

class UnsplashPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item["image_urls"]:
            for file_url in item["image_urls"]:
                try:
                    yield Request(file_url)
                except Exception as e:
                    print(e)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f"{item['kind']}_{item['name']}_{image_guid}.jpg"    

    def item_completed(self, results, item, info):
        if results:
            item["path"] = [item[1]["path"] for item in results if item[0]]

        return item