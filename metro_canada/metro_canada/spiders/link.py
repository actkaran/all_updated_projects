import scrapy
from scrapy.cmdline import execute
import re
from metro_canada.items import MetroLinks
import hashlib

# def generate_hash_id(url: str) -> str:
#     # Use SHA256 to generate a hash of the URL
#     hash_object = hashlib.sha256(url.encode('utf-8'))
#     # Return the hash as a hexadecimal string
#     return hash_object.hexdigest()

class DataSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["www.metro.ca"]
    # start_urls = ["https://www.metro.ca/sitemap-ecomm-en-qc.xml"] #english language products xml link
    start_urls = ["https://www.metro.ca/sitemap-ecomm-fr-qc.xml"] # french language products xml link.

    def parse(self, response):
        links = re.findall(r'<loc>(.*?)<\/loc>', response.text)
        item = MetroLinks()
        for i in links:
            if '/p/' in i:
                item["product_number"] = i.split("/p/")[-1]
                item["url"] = i
                yield item


if __name__ == "__main__":
    execute(f"scrapy crawl {DataSpider.name}".split())