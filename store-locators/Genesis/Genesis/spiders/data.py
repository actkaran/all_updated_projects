import json
import os.path
import Genesis.DB_CONFIG as db
import scrapy
from scrapy.cmdline import execute
from Genesis.items import GenesisItem


class DataSpider(scrapy.Spider):
    name = "data_genesis"
    allowed_domains = ["www.genesis.com"]
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.genesis.com/us/en/retailer-locator',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'Referrer-Policy': 'origin',
    }

    def start_requests(self):
        data = db.location.find({"status": "pending"})
        for a in data:
            zip_code = a["zipcode"]
            yield scrapy.Request(method="GET",
                                 url=f"https://www.genesis.com/bin/api/v2/dealers",
                                 headers=self.headers,
                                 dont_filter=True,
                                 cb_kwargs=a,
                                 meta={'zip': zip_code},
                                 callback=self.parse)

    def parse(self, response, **kwargs):
        zipe_code = kwargs["zipcode"]
        file_location = fr"C:\Users\DELL\Desktop\KARAN\Genesis\Genesis\pagesave\{zipe_code}.html"
        with open(file_location, 'w') as f:
            f.write(response.text)
        data_json = json.loads(response.text)
        item = GenesisItem()

        for dealer in data_json["result"]["dealers"]:
            item["store_no"] = dealer["dealerCd"]
            item["name"] = dealer["dealerNm"]
            item["latitude"] = dealer["latitude"]
            item["longitude"] = dealer["longitude"]
            item['street'] = dealer["address1"]
            item["city"] = dealer["city"]
            item["state"] = dealer["state"]
            item["zip_code"] = dealer["zipCd"]
            item["county"] = 'NA'
            item["country"] = 'USA'
            item["open_hours"] = json.dumps(dealer["showroom"]) if "showroom" in dealer else "NA"
            item["phone_number"] = dealer["phone"]
            item["status"] = "Open" if dealer["isLocatorActive"] else "NA"
            item["url"] = 'https://www.genesis.com/us/en/retailer-locator'
            item["direction_url"] = "NA"
            if item["street"] and item["zip_code"] and item["state"]:
                edited_street_address = '+'.join(item["street"].split())
                item[
                    "direction_url"] = f"https://www.google.com/maps/dir/Current+Location/{edited_street_address},+{item['state']},+{item['zip_code']},+{item['country']}/"
            item["db_zip"] = zipe_code
            yield item


if __name__ == "__main__":
    execute(f"scrapy crawl {DataSpider.name}".split())
