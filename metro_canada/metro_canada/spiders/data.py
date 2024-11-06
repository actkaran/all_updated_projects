import gzip
import os.path
import random
import re
import html
import chardet
import scrapy
import pymysql
from parsel import Selector
from scrapy.cmdline import execute

import metro_canada.db_config as db
from metro_canada.items import MetroCanadaItem


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.metro.ca"]
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()
    cookies = {
        'JSESSIONID': '6795DE1F54C91194C179CBF23EDBA75D',
        'METRO_ANONYMOUS_COOKIE': '2a089653-3862-4c44-88e7-c0b966b9ac90',
        'APP_D_USER_ID': 'SbAxJbfW-2167009951',
        'coveo_visitorId': '6079a312-f6a6-4fe3-b36f-eeb9f22d4406',
        'hprl': 'en',
        'NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei': '37cda3dd8480094768c32d3f812de4df3b6f3fbc19793496f46507e16debc1d0cdd83e0c',
        '__cf_bm': 'IoWUNYw8ZW5LB91NST7FN0ZdPLCpjBjeKvtkAZJQEX0-1730899052-1.0.1.1-hUjNK0al7X1jLV07jBOZTpZtN9YruVatw8UhkZHMTmlqLE9V5h5TeG43pGCNRJOtK2TqImzixW_pLhzXpoyW5JvtwNLQrI.MY2n0UIYz334',
        'cf_clearance': '2On379AiO8vdsAuC6lzWWtkzNSWXT.MfdkLqcbFl5cw-1730899057-1.2.1.1-6RYL4y4IZl.3WuXBiXteL5H8A3r0AVTq4omUmpgxj9JiSy4wXGwkbrYVcvUZhWRkrMF4MfOGFX7j0A4GsnmXKoxV3YHqjqfXNhKY8SP_SeIkruYoGp9BHDStGHHDmpAMn88dlMe_L_ghwaNb_cjxWGgmsLUHTBvZAlJuz8TJ79RGDA7HKAW322YUF2b9TRltO8Alo4TzgLj.Cmz6eiTNQxMOz79jiYxZEstBLXI6zBtWaj1rE7EtbN1YSyjTvWfNESGupfh2sq94yurgaBEqgQeuK7rkaUwUYxR8FXn37pWfnJqDid8mwyZcQM4Hm5WUMa2Y.DZJqPUMUsKvs.iLTwFJYhZahpuqFW3ii4BGWWO5yf.EC24Tg0Jx0LENYALI',
        'OptanonAlertBoxClosed': '2024-11-06T13:17:44.195Z',
        '_gcl_au': '1.1.540019629.1730899064',
        '_ga': 'GA1.1.647041018.1730899064',
        'coveo_visitorId': '6079a312-f6a6-4fe3-b36f-eeb9f22d4406',
        '_fbp': 'fb.1.1730899068064.993329482787135454',
        '_clck': '71w9uk%7C2%7Cfqn%7C0%7C1771',
        '_ga_RSMJC35YH9': 'GS1.1.1730899064.1.1.1730899102.22.0.0',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Nov+06+2024+18%3A48%3A26+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=a9798f4d-563d-42d3-9534-2f2540fd0186&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false',
        '_conv_v': 'vi%3A1*sc%3A1*cs%3A1730899065*fs%3A1730899065*pv%3A4',
        '_conv_s': 'si%3A1*sh%3A1730899064548-0.12445316273914386*pv%3A4',
        '_uetsid': '84d339509c4111ef991043720f8714d1',
        '_uetvid': '84d344d09c4111efb78dcdbab0c132ca',
        '_clsk': '1j1h5xb%7C1730899110084%7C3%7C1%7Ch.clarity.ms%2Fcollect',
        'forterToken': '8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck_',
        'forter-uid': '8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck__tt',
        'cto_bundle': 'dsCD1V9PQ1NlRlVoTGdETTk1QjdjaWtCc1FicWxHcWZaUkVWSjd4VnBQQyUyRlFySUhDOXU3OTJ5SjBqeE5aZVlWcm1mbXFNZUcxMUNDcHhyNmpjUE1LUFdIVjROOHlTZ1ZEaUVScHIydDJFanJpWlhBcXhrU0pXQ3Y4VkFuWGNzcnRQUUhEVW9pJTJCYXdOaHk0UmM4VTRVNE1pQmpnJTNEJTNE',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'JSESSIONID=6795DE1F54C91194C179CBF23EDBA75D; METRO_ANONYMOUS_COOKIE=2a089653-3862-4c44-88e7-c0b966b9ac90; APP_D_USER_ID=SbAxJbfW-2167009951; coveo_visitorId=6079a312-f6a6-4fe3-b36f-eeb9f22d4406; hprl=en; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=37cda3dd8480094768c32d3f812de4df3b6f3fbc19793496f46507e16debc1d0cdd83e0c; __cf_bm=IoWUNYw8ZW5LB91NST7FN0ZdPLCpjBjeKvtkAZJQEX0-1730899052-1.0.1.1-hUjNK0al7X1jLV07jBOZTpZtN9YruVatw8UhkZHMTmlqLE9V5h5TeG43pGCNRJOtK2TqImzixW_pLhzXpoyW5JvtwNLQrI.MY2n0UIYz334; cf_clearance=2On379AiO8vdsAuC6lzWWtkzNSWXT.MfdkLqcbFl5cw-1730899057-1.2.1.1-6RYL4y4IZl.3WuXBiXteL5H8A3r0AVTq4omUmpgxj9JiSy4wXGwkbrYVcvUZhWRkrMF4MfOGFX7j0A4GsnmXKoxV3YHqjqfXNhKY8SP_SeIkruYoGp9BHDStGHHDmpAMn88dlMe_L_ghwaNb_cjxWGgmsLUHTBvZAlJuz8TJ79RGDA7HKAW322YUF2b9TRltO8Alo4TzgLj.Cmz6eiTNQxMOz79jiYxZEstBLXI6zBtWaj1rE7EtbN1YSyjTvWfNESGupfh2sq94yurgaBEqgQeuK7rkaUwUYxR8FXn37pWfnJqDid8mwyZcQM4Hm5WUMa2Y.DZJqPUMUsKvs.iLTwFJYhZahpuqFW3ii4BGWWO5yf.EC24Tg0Jx0LENYALI; OptanonAlertBoxClosed=2024-11-06T13:17:44.195Z; _gcl_au=1.1.540019629.1730899064; _ga=GA1.1.647041018.1730899064; coveo_visitorId=6079a312-f6a6-4fe3-b36f-eeb9f22d4406; _fbp=fb.1.1730899068064.993329482787135454; _clck=71w9uk%7C2%7Cfqn%7C0%7C1771; _ga_RSMJC35YH9=GS1.1.1730899064.1.1.1730899102.22.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+18%3A48%3A26+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=a9798f4d-563d-42d3-9534-2f2540fd0186&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _conv_v=vi%3A1*sc%3A1*cs%3A1730899065*fs%3A1730899065*pv%3A4; _conv_s=si%3A1*sh%3A1730899064548-0.12445316273914386*pv%3A4; _uetsid=84d339509c4111ef991043720f8714d1; _uetvid=84d344d09c4111efb78dcdbab0c132ca; _clsk=1j1h5xb%7C1730899110084%7C3%7C1%7Ch.clarity.ms%2Fcollect; forterToken=8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck_; forter-uid=8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck__tt; cto_bundle=dsCD1V9PQ1NlRlVoTGdETTk1QjdjaWtCc1FicWxHcWZaUkVWSjd4VnBQQyUyRlFySUhDOXU3OTJ5SjBqeE5aZVlWcm1mbXFNZUcxMUNDcHhyNmpjUE1LUFdIVjROOHlTZ1ZEaUVScHIydDJFanJpWlhBcXhrU0pXQ3Y4VkFuWGNzcnRQUUhEVW9pJTJCYXdOaHk0UmM4VTRVNE1pQmpnJTNEJTNE',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    def __init__(self, start=None, end=None):
        self.start= start
        self.end = end


    def start_requests(self):
        # header and cookies will be here...

        self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' AND id between {self.start} AND {self.end};")

        data = self.cur.fetchall()
        print("Total Fetched: ", len(data))
        for i in data:
            url = i[1]
            id = i[0]
            path = f"{db.PAGESAVE}{id}.html.gz"
            if os.path.exists(path):
                yield scrapy.Request(url=f"file:///{db.PAGESAVE}{id}.html.gz",
                                     callback=self.parse,
                                     dont_filter=True,
                                     cb_kwargs={"url": url,
                                                "id": id,
                                                "exists":1}
                                     )
            else:
                yield scrapy.Request(url=url,
                                     cookies=self.cookies,
                                     callback=self.parse,
                                     dont_filter=True,
                                     meta={'proxy':f"http://{db.zyte_proxy_key}:@api.zyte.com:8011"},
                                     cb_kwargs={"url": url,
                                                "id": id,
                                                "exists":0}
                                     )
            # break

    def parse(self, response, **kwargs):
        if kwargs["exists"] == 0:
            with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'wb') as f:
                f.write(response.body)
        if kwargs["exists"] == 1:
            with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'rb') as f:
                content = f.read()
                detected = chardet.detect(content)
                encoding = detected['encoding']
            response = Selector(text=content.decode(encoding))
        item = MetroCanadaItem()
        # item["price"] = response.xpath("string(//span[contains(@class, 'price-update')])").get()
        # else:
        price = response.xpath("//div[@data-main-price]/@data-main-price").get()
        product_name = response.xpath("string(//div[@class='pi--name'])").get()
        mrp = response.xpath("//div[@class='pricing__before-price']/span[contains(text(),'$')]/text()").get()
        quantity = response.xpath("//div[@class='pi--weight']/text()").get()
        price_per_unit = ''.join(response.xpath("//div[contains(@class, 'pricing__secondary-price')]/span[contains(text(), '/')]//text()").getall())
        serving_for_people = response.xpath("//select[contains(@class, 'select select-addToCart')]/option[contains(@default-option, 'true')]/font/font/text()").get()
        product_image = response.xpath("//picture[@id='main-img']/source[contains(@id, 'desk-img')]/@srcset").get()
        h = ''.join(response.xpath("string(//div[@class='accordion--text'])").getall())
        ingredients = response.xpath("//p[@class='pdp-ingredients-list']/text()").get()
        valid_till = response.xpath("string(//div[@class='pricing__until-date'])").get()
        if mrp:
            item["mrp"] = mrp.replace('$','').strip()
        elif price:
            item["mrp"] = price.strip()

        item["price"] = price.strip() if price else "NA"
        item["currency"] = '$' if mrp or price else "NA"
        item["serving_for_people"] = serving_for_people.strip() if serving_for_people else "NA"
        item["product_url"] = kwargs["url"]
        item["o_id"] = kwargs["id"]
        item["category"] = ' | '.join(response.xpath("//*[@class='b--list']/li/a/span/text()").getall()).replace(" | Online Grocery",'')
        item["valid_date"] = valid_till.strip() if valid_till else "NA"
        item["product_name"] = product_name.strip() if product_name else "NA"
        item["product_number"] = item["product_url"].split('/')[-1]
        item["ingredients"] = ingredients.strip() if ingredients else "NA"
        item["product_description"] = re.sub(r'\s+', ' ', h).strip()
        item["product_image"] = product_image if product_image else "NA"
        item["price_per_unit"] = price_per_unit.strip() if price_per_unit else "NA"
        item["quantity"] = quantity.strip() if quantity else "NA"
        yield item


if __name__ == "__main__":
    execute(f"scrapy crawl data -a start=0 -a end=12000".split())
