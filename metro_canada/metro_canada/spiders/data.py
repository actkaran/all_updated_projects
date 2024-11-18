import gzip
import os.path
import random
import re
import scrapy
import pymysql
from parsel import Selector
from scrapy.cmdline import execute
import metro_canada.cookie_file as cookies_list
import metro_canada.db_config as db
from metro_canada.items import MetroCanadaItem


class DataSpider(scrapy.Spider):
    name = "data"
    # allowed_domains = ["www.metro.ca"]
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()
    # cookies = random.choice(cookies_list.list_of_cookies)
    cookies = {
    'METRO_ANONYMOUS_COOKIE': '9098b0fb-ad46-46c1-b710-25ee667ef5a5',
    'CRITEO_RETAILER_VISITOR_COOKIE': 'df5eb665-4876-4413-bab6-e2fae72ec0f1',
    'coveo_visitorId': 'cda1c630-7db1-48f9-9182-dd9d16fad5a8',
    'hprl': 'en',
    'coveo_visitorId': 'cda1c630-7db1-48f9-9182-dd9d16fad5a8',
    '_ga': 'GA1.1.2076354866.1731579794',
    '_gcl_au': '1.1.1036957491.1731579794',
    '_fbp': 'fb.1.1731579824105.831881357317130183',
    'OptanonAlertBoxClosed': '2024-11-14T10:29:48.448Z',
    'NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei': '4afda3daa753ae5dd78f74cca9802458f780e0bd1ca2e6eb4a0239e732902253c456cfb5',
    '_clck': 'essm73%7C2%7Cfqw%7C0%7C1779',
    '_uetsid': '602525d0a27311efabe6073e7b3374e2',
    '_uetvid': '602561a0a27311efbaf1c94278184692',
    '_clsk': 'mp2mkg%7C1731662215121%7C4%7C1%7Co.clarity.ms%2Fcollect',
    'SameSite': 'None',
    'JSESSIONID': 'D8EDBCAE59BD76C0AEF849BDC7E63D29',
    'APP_D_USER_ID': 'GnjeZaQE-2175114804',
    '__cf_bm': '7wwbAy67XybmmNuutpxJR7ZF813ECTCE5Gf2B__RE.c-1731669821-1.0.1.1-CSt17iUYF1fZVrXkDgWHcyYeRsAN8ZpSs3Gf6or_U1ijUNbz8iaE.G5fFbfFVXuAjStKZ5rjd491K.SDGJivM2Sw1g.1i4H2HPEjoYSp.BI',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Nov+15+2024+16%3A53%3A41+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=4&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false',
    '_conv_v': 'vi%3A1*sc%3A24*cs%3A1731669822*fs%3A1730698428*pv%3A60*ps%3A1731667412*exp%3A%7B%7D',
    '_conv_s': 'si%3A24*sh%3A1731669821768-0.7435593399812148*pv%3A1',
    'cf_clearance': 'cLVR0Y8PFkhPnY0jorZXTZrvTBbJ_6PxNj7nVWLC9sE-1731669822-1.2.1.1-T0xFyHXnJg.2LG3NK_s3cqugTf4ggoEUB.stjfqSYnKExJIO07xTuNnaW7Sz6JO0FzklLNGOW.Gd8l.HxbHdABbeiU77TQ9lHQRjIeKnRpSoR2lIPO.ar2wXu..pkTptf6KNkqPLbIBucoYsPs8T_4ktzUbWlkuVHFcnqyWYvxrAVW8f_HEtRrO8VL9RTsVisOlqzsnmZCjX50nnrhZQ3vqQgnGv6UXHJoU9FDKeF7VKXUyPHLQAhWLYSKxbmJi9D8f.KELHpgzMwQxSkesKfTg7FJUL81Z68QgYx_lfLIWF5v3LvSf2WbxEEC8d8Zh4MeQToaNwdiYnqFhOD20tWJoJ4YrNEffILmFymlrikTfqF63_qMZZPHUFv2ENK3xy',
    '_ga_RSMJC35YH9': 'GS1.1.1731669822.5.0.1731669822.60.0.0',
    'cto_bundle': 'UFXvDF9NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QWxGUTNKR2dzJTJCTjRRTVNXTGRMaDFFS3Ezam1UM3R1ektyWU5Jbk9FTDBUaiUyQkZhMUxaNDR2UkEyWG5RY2tndG5XSmpmMG96T2R4VENveUlNJTJGWjFBV1ElMkY4JTJGclhWdDJqJTJGS3ZVT3lodFFHJTJGMUpXMVY2blBuN1BFRVg0S05VaVZpRFJnJTNEJTNE',
    'forterToken': '552dd3c56da24fb2bc2f1685b5599b52_1731669821503__UDF43-m4_21ck_',
    'forter-uid': '552dd3c56da24fb2bc2f1685b5599b52_1731669821503__UDF43-m4_21ck__tt',
    'ADRUM_BTa': 'R:0|g:bdaa792c-ec91-4d9e-8fe3-458c720baa86|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11',
    'ADRUM_BT1': 'R:0|i:268240|e:412',
}
    def __init__(self, start=None, end=None):
        self.start= start
        self.end = end


    def start_requests(self):
        # header and cookies will be here...

        # self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' AND id between {self.start} AND {self.end};")
        self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE id=51182;")

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
                                     # meta={'proxy':f"http://kunal_santani577-9elgt:QyqTV6XOSp@{random.choice(pxs)}:3199"},
                                     cb_kwargs={"url": url,
                                                "id": id,
                                                "exists":0}
                                     )
            # break

    def parse(self, response, **kwargs):
        if kwargs["exists"] == 0:
            # if response.status == 404:
                # update = f"""UPDATE {db.db_link_table} SET status='NA' WHERE id=%s"""
                # self.cur.execute(update, (id,))
                # self.con.commit()
                # print("NA..............................")
                # return None
            with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'wb') as f:
                f.write(response.body)
        if kwargs["exists"] == 1:
            with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'rb') as f:
                response = Selector(text=f.read().decode('utf-8'))
        item = MetroCanadaItem()
        # item["price"] = response.xpath("string(//span[contains(@class, 'price-update')])").get()
        # else:
        '# for category'
        category_result = []
        lt_category = response.xpath("//div[contains(@class, 'breadcrumb')]//li//text()").getall()
        for cat in lt_category:
            h = cat.strip()
            if h:
                if h != "Online Grocery":
                    category_result.append(h)
        item["category"] = ' | '.join(category_result) if category_result else "NA"
        price = response.xpath("//div[@data-main-price]/@data-main-price").get()
        # product_name = response.xpath("string(//div[@class='pi--name'])").get() old xpath
        # product_name = response.xpath("//div[@data-product-name]/@data-product-name").get()
        product_name = response.xpath("//div[@class='pi--name']/h1[@class='pi--title']/text()").get()
        mrp = response.xpath("//div[@class='pricing__before-price']/span[contains(text(),'$')]/text()").get()
        quantity = response.xpath("//div[@class='pi--weight']/text()").get()
        price_per_unit = ''.join(response.xpath("//div[contains(@class, 'pricing__secondary-price')]/span[contains(text(), '/')]//text()").getall())
        serving_for_people = response.xpath("//select[contains(@class, 'select select-addToCart')]/option[contains(@default-option, 'true')]/font/font/text()").get()
        product_image = response.xpath("//picture[@id='main-img']/source[contains(@id, 'desk-img')]/@srcset").get()
        h = ''.join(response.xpath("string(//div[@class='accordion--text'])").getall())
        ingredients = response.xpath("//p[@class='pdp-ingredients-list']/text()").get()
        if ingredients:
            tt = ''.join(char for char in ingredients if ord(char) < 128)
        else:
            tt = "NA"
        item["ingredients"] = tt
        valid_till = response.xpath("string(//div[@class='pricing__until-date'])").get().strip()
        if '' == valid_till:
            valid_till = "NA"
        if mrp:
            item["mrp"] = mrp.replace('$','').strip()
        elif price:
            item["mrp"] = price.strip()

        item["price"] = price.strip() if price else "NA"
        item["currency"] = '$' if mrp or price else "NA"
        item["serving_for_people"] = serving_for_people.strip() if serving_for_people else "NA"
        item["product_url"] = kwargs["url"]
        item["o_id"] = kwargs["id"]
        item["valid_date"] = valid_till.strip()
        item["product_name"] = product_name.strip() if product_name else "NA"
        item["product_number"] = item["product_url"].split('/')[-1]
        item["product_description"] = re.sub(r'\s+', ' ', h).strip()
        item["product_image"] = product_image if product_image else "NA"
        item["price_per_unit"] = price_per_unit.strip() if price_per_unit else "NA"
        item["quantity"] = quantity.strip() if quantity else "NA"
        yield item


if __name__ == "__main__":
    execute(f"scrapy crawl data -a start=0 -a end=1000000".split())



'<div class="user__shop">'
