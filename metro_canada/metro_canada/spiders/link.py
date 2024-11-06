import scrapy
from scrapy.cmdline import execute
import re
from metro_canada.items import MetroLinks


class DataSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["www.metro.ca"]
    start_urls = ["https://www.metro.ca/sitemap-ecomm-en-qc.xml"]

    def parse(self, response):
        links = re.findall(r'<loc>(.*?)<\/loc>', response.text)
        item = MetroLinks()
        for i in links:
            item["url"] = i
            yield item


if __name__ == "__main__":
    execute(f"scrapy crawl {DataSpider.name}".split())