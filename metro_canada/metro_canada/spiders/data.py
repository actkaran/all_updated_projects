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
        'METRO_ANONYMOUS_COOKIE': '3a2b998b-6e52-435d-98c0-1d030a95eee8',
        'CRITEO_RETAILER_VISITOR_COOKIE': 'ac9bab2d-7aec-4721-b0f9-10ff1c69b3c4',
        'coveo_visitorId': 'c3f5f51e-95ca-4d80-93eb-979d35c2c1ae',
        'hprl': 'en',
        '_ga': 'GA1.1.1093776326.1730877757',
        'coveo_visitorId': 'c3f5f51e-95ca-4d80-93eb-979d35c2c1ae',
        '_gcl_au': '1.1.1099375172.1730877757',
        'OptanonAlertBoxClosed': '2024-11-06T07:22:39.944Z',
        '_fbp': 'fb.1.1730877760680.653511761591064627',
        '_clck': '1i16p2g%7C2%7Cfqn%7C0%7C1771',
        '_clsk': 'obd35h%7C1730889110404%7C1%7C1%7Co.clarity.ms%2Fcollect',
        'NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei': '4afda3daa753ae5dd78f74cca9802458f780e0bd1ca2e6eb4a0239e732902253c456cfb5',
        '__cf_bm': 'mSb54gbOpAFAQ_NSwKvgtcYPbxrTuveQd2kKgPfFKhA-1730907926-1.0.1.1-3fSw5co18FCaOeeSbtAviVZzBqS34LGoIQQjJ3IhZPBn0BzWcnv7P1OxthYCB9U_uB7wZZWOi2LFNsXiMrgs709LJBxp0r4boRyTv5B4D2g',
        'SameSite': 'None',
        'JSESSIONID': '16A3D6E88F6D9EFFD6A2C5DD7A120545',
        'APP_D_USER_ID': 'yzPmkToh-2166830715',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Nov+06+2024+21%3A41%3A47+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false',
        'cf_clearance': 'gFaryeKoOreXXg.sOLemo9wpIFinlcFkn_IOvI4GhEE-1730909508-1.2.1.1-O3m8SZ.EH.4oPySqWhpuc8ejP1UDC3I3uoInkLGCa3Z4Yrewy2UB5lm.a7aGtqhIYVPRbir7JqBfxHoJZejyLABxXkM9a6i87XONmQJIQIKJPA1A3.N3SLi1p439qPtbVbVcVwqOp1pQEUovneuD4t90w1LUGIPB7C7QHMgEnMNvXxGAW3Q0AtIS3dJ98oVS3y9tSPE9vKph_TWdooi1vOGiOksp3Bf4uhU7lJ8AgP5Qv2GcHBMieaL3nunWGYNfPppKWtEnPeCwXDvpuwKokfVC8q9by4GYdezyB7PUcV9rRI0_a6qgI9rGklHe6xMn1DJc5QmdLYESOeuzn_v1qXIkh7V8g_2o4K_zHh4BKZPLiMNeUm656mJ6oydwj4G.RM36r2Kh4TbCAfFmGbuY.A',
        '_conv_v': 'vi%3A1*sc%3A12*cs%3A1730909507*fs%3A1730698428*pv%3A25*ps%3A1730907928*exp%3A%7B%7D',
        '_conv_s': 'si%3A12*sh%3A1730909507478-0.6317491576077305*pv%3A1',
        '_ga_RSMJC35YH9': 'GS1.1.1730907931.3.1.1730909508.60.0.0',
        'cto_bundle': 'UWiacV9NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QXZtYXpURCUyQmp3SUFFJTJCVVdxJTJGZk9HMXZ0aE9oOEtQNjh3R3VBVFRRcEoxeVVtbDgwbjZYWVBFQmRBSUhWRGpQRzhtVUNJQ3JnR1Y0SXFCYXlXZmpYY1ZNVHpJZXlmczRHZnhDMlZmZFlCWWVXT3JGcE16OWdOMzA3VXZKSzhtSGdOQSUzRCUzRA',
        '_uetsid': 'ead56fe09c0f11efb63d6b762397b31c',
        '_uetvid': 'ead5b7809c0f11efb0eed396762de15c',
        'forterToken': '552dd3c56da24fb2bc2f1685b5599b52_1730909506661__UDF43-m4_21ck_',
        'forter-uid': '552dd3c56da24fb2bc2f1685b5599b52_1730909506661__UDF43-m4_21ck__tt',
        'ADRUM_BTa': 'R:0|g:6e020422-39ef-4ff6-bc6e-06a7f6f8ddb3|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11',
        'ADRUM_BT1': 'R:0|i:268164|e:447',
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
    execute(f"scrapy crawl data -a start=0 -a end=25000".split())
