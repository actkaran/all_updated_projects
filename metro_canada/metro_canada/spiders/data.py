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
    handle_httpstatus_list = [404]

    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()

    # remember to add headers in settings.py file (in -> DEFAULT_REQUEST_HEADERS )...
    cookies = cookies_list.cookies # add your cookies (dictionary) here...

    def __init__(self, start=None, end=None):
        self.start= start
        self.end = end


    def start_requests(self):

        self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE status='pending' AND a_id BETWEEN {self.start} AND {self.end};")

        data = self.cur.fetchall()
        print("Total Fetched: ", len(data))
        for i in data:
            url = i[1]
            product_number = i[2]
            # url = f"https://www.metro.ca/epicerie-en-ligne/allees/p/{product_number}"
            path = f"{db.PAGESAVE}{product_number}.html.gz"
            if os.path.exists(path):
                yield scrapy.Request(url="https://books.toscrape.com/",
                                    # url=f"file:///{db.PAGESAVE}{id}.html.gz",
                                     callback=self.parse,
                                     dont_filter=True,
                                     cb_kwargs={"url": url,
                                                "product_number": product_number,
                                                "exists":1}
                                     )
                # pass
            else:
                yield scrapy.Request(url=url,
                                     cookies=self.cookies,
                                     callback=self.parse,
                                     # dont_filter=True,
                                     # meta={"proxy":f"http://scraperapi:{db.scraper_proxy}@proxy-server.scraperapi.com:8001"},
                                     meta={'proxy':f"http://{db.zyte_proxy_key}:@api.zyte.com:8011",
                                           # 'impersonate': random.choice(["chrome110", "edge99", "safari15_5"])
                                           },
                                     cb_kwargs={"url": url,
                                                "product_number": product_number,
                                                "exists":0}
                                     )
            # break

    def parse(self, response, **kwargs):
        product_number = kwargs["product_number"]
        if response.status == 404:
            update = f"""UPDATE {db.db_link_table} SET status='NA' WHERE product_number=%s"""
            self.cur.execute(update, (product_number,))
            self.con.commit()
            print("NA..............................")
            return None
        if kwargs["exists"] == 0:
            with gzip.open(f"{db.PAGESAVE}{product_number}.html.gz", 'wb') as f:
                f.write(response.body)
        if kwargs["exists"] == 1:
            with gzip.open(f"{db.PAGESAVE}{product_number}.html.gz", 'rb') as f:
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
                # if h != "Online Grocery":
                if h != "Épicerie en ligne":
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
        item["valid_date"] = valid_till.strip()
        item["product_name"] = product_name.strip() if product_name else "NA"
        item["product_number"] = product_number
        item["product_description"] = re.sub(r'\s+', ' ', h).strip()
        item["product_image"] = product_image if product_image else "NA"
        item["price_per_unit"] = price_per_unit.strip() if price_per_unit else "NA"
        item["quantity"] = quantity.strip() if quantity else "NA"
        yield item


if __name__ == "__main__":
    execute(f"scrapy crawl data -a start=0 -a end=260000".split())



'<div class="user__shop">'
