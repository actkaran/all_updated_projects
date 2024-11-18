import gzip
import os.path
import random
import re
import html
import chardet
import scrapy
from curl_cffi import requests
import pymysql
from parsel import Selector
from scrapy.cmdline import execute
import metro_canada.db_config as db
from metro_canada.items import MetroCanadaItem

# this code is not working... it's just made on emergency to run curl_request code in scrapy...
class CurlSpiderSpider(scrapy.Spider):
    name = "CURL_data"
    allowed_domains = ["www.metro.ca"]
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def start_requests(self):
        # header and cookies will be here...
            self.cur.execute(
                f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' AND id between {self.start} AND {self.end};")
                # f"SELECT * FROM {db.db_link_table} WHERE url='https://www.metro.ca/en/online-grocery/aisles/beer-wine/wines-cocktails-coolers/red-wine/0g-sugar-red-wine/p/056049138983';")

            data = self.cur.fetchall()
            print("Total Fetched: ", len(data))
            for i in data:
                url = i[1]
                id = i[0]

                yield scrapy.Request(url='https://books.toscrape.com/',
                                     dont_filter=True,
                                     callback=self.parse,
                                     cb_kwargs={"url": url,
                                                "id": id})
                # break

    def parse(self, response, **kwargs):

        # making request......
        url = kwargs["url"]
        id = kwargs["id"]
        header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'SameSite=None; JSESSIONID=6306EE2A0434F63F3D6A7C966DC280EA; METRO_ANONYMOUS_COOKIE=1b8d16b5-bb3d-4e6f-9981-06270b638f30; APP_D_USER_ID=tAZfFSmL-2175221513; coveo_visitorId=f6589fd5-fe78-4cad-9d60-910feac2048f; hprl=en; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=1116a3dbacfa57ebaff6b9c8b37c3deda3cf0f801e79b0cf2e8abafc1cefde95dc7a1d5d; __cf_bm=suFKDfC2wzd_NO5TrBdPT9qfKeeKmUpZ.E.qC7Gw.ms-1731589263-1.0.1.1-HjB3j3Vgtv1nALPeLsDVYa4SAyvQq2CRd7iN1dj6z8cIzFIRQenvr7jxZbygVhBy2rGQUqnW4PmdlTwjRuaLukUG8PA5qWYNGvArJyEMKBc; cf_clearance=xp0IZS008LRnADMiSyB_G0HOEBkJkhCB73zOFHF3.5E-1731589267-1.2.1.1-i6OfZfvifK80v7d.kEJq2jsa0zxYv2ggEhUXPiTRqZVNQI_b.kpwOX9QV7WwGaHiigyB9wDUF_rOd9ExXqBi7ByW8gm..yEHd0cJVF7qWYZJLeK1wK_9BPuxr5WsyjPd1n6zTQe2C0ErwolUJR.aB2FSVGmt44qcOuHLlFZVdLxO68Be_kWuc7KosZiVWAYs4_qpIe4UOOUUNVOS1lCs6fDQfAo49ZiX7kXKGySQ..BkMKCETX5UCDRnEizhXL_rm.ORMk4kRt0Xa.ABjpfQ1LAmktQ.7q_HiNcNemIqm6ce2Obq1zd5O03AFbXtBDyO4HGHf207qIn8vDkkjhsevkLiinRJPq51XJEYqj8zXZOqvS3Pnp6MbPisYrb9GRoq; OptanonAlertBoxClosed=2024-11-14T13:01:11.608Z; _gcl_au=1.1.724396755.1731589272; _ga=GA1.1.1063814152.1731589272; coveo_visitorId=f6589fd5-fe78-4cad-9d60-910feac2048f; _fbp=fb.1.1731589275597.48995421347345753; _clck=1yi3hf2%7C2%7Cfqv%7C0%7C1779; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Nov+14+2024+18%3A31%3A31+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ef942f81-d240-4de6-8aa0-bae62362ebb0&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=CA%3BON&AwaitingReconsent=false; _ga_RSMJC35YH9=GS1.1.1731589271.1.1.1731589291.40.0.0; _conv_v=vi%3A1*sc%3A1*cs%3A1731589274*fs%3A1731589274*pv%3A2; _conv_s=si%3A1*sh%3A1731589274059-0.5414178250404527*pv%3A2; _uetsid=88160e70a28811efbb225da3a52203fb; _uetvid=881613d0a28811ef9388875cc4d78fb3; cto_bundle=LAp2hF9iRHdUb3ZnR09OVlVyRWdWd0hZQWZzbE1RblVMbDdRUlpUWmdXQkRicHczTGhqTnM0Vk9mbHFWJTJCUUpmcmRyRHZjY1d4VVpvejdNRDFpU0NFJTJCU0pXUFVPYVFpM0IxTnozMmltQTFaUDgwVVQ3aWM4d0VLbmg2RUVFUWMxTHpMellwWXRnOWkzV2pLYmMxQVg3VWhydkRBJTNEJTNE; forterToken=151f34438c704bf49364338fce1ffcb1_1731589291230__UDF43-m4_21ck_; forter-uid=151f34438c704bf49364338fce1ffcb1_1731589291230__UDF43-m4_21ck__tt; _clsk=yh6mdi%7C1731589294099%7C2%7C1%7Cq.clarity.ms%2Fcollect; ADRUM_BTa=R:0|g:2979abe0-9211-45eb-81dc-20fb04ddd9f1|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:0|i:268164|e:431',
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
        # proxy = {'http': f'http://{db.zyte_proxy_key}:@api.zyte.com:8011'}
        proxy = {'http': f"http://scraperapi:{db.scraper_proxy}@proxy-server.scraperapi.com:8001"}
        path = f"{db.PAGESAVE}{id}.html.gz"
        response = None
        if not os.path.exists(path):
            mk = requests.get(
                url=url,
                headers=header,
                impersonate=random.choice(["chrome110", "edge99", "safari15_5"]),
                proxies=proxy
            )
            if mk.status_code == 200:
                with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'wb') as f:
                    f.write(mk.content)
                response = Selector(text=mk.text)
            elif mk.status_code == 404:
                update = f"""UPDATE {db.db_link_table} SET status='NA' WHERE id=%s"""
                self.cur.execute(update, (id,))
                self.con.commit()
                print("NA..............................")
                return None

        # else:
        #     with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'rb') as f:
        #         response = Selector(text=f.read().decode('utf-8'))
            # mk = requests.get(
            #     url=url,
            #     headers=header,
            #     impersonate=random.choice(["chrome110", "edge99", "safari15_5"]),
            #     proxies=proxy
            # )
            # if mk.status_code == 200:
            #     with gzip.open(f"{db.PAGESAVE}{kwargs['id']}.html.gz", 'wb') as f:
            #         f.write(mk.content)
            #     response = Selector(text=mk.text)
            # if mk.status_code == 404:
            #     update = f"""UPDATE {db.db_link_table} SET status='NA' WHERE id=%s"""
            #     self.cur.execute(update, (id,))
            #     self.con.commit()
            #     print("NA..............................")
            #     return None
            item = MetroCanadaItem()
            price = response.xpath("//div[@data-main-price]/@data-main-price").get()
            product_name = response.xpath("string(//div[@class='pi--name'])").get()
            mrp = response.xpath("//div[@class='pricing__before-price']/span[contains(text(),'$')]/text()").get()
            quantity = response.xpath("//div[@class='pi--weight']/text()").get()
            price_per_unit = ''.join(response.xpath(
                "//div[contains(@class, 'pricing__secondary-price')]/span[contains(text(), '/')]//text()").getall())
            serving_for_people = response.xpath(
                "//select[contains(@class, 'select select-addToCart')]/option[contains(@default-option, 'true')]/font/font/text()").get()
            product_image = response.xpath("//picture[@id='main-img']/source[contains(@id, 'desk-img')]/@srcset").get()
            h = ''.join(response.xpath("string(//div[@class='accordion--text'])").getall())
            ingredients = response.xpath("//p[@class='pdp-ingredients-list']/text()").get()
            valid_till = response.xpath("string(//div[@class='pricing__until-date'])").get()
            if mrp:
                item["mrp"] = mrp.replace('$', '').strip()
            elif price:
                item["mrp"] = price.strip()

            item["price"] = price.strip() if price else "NA"
            item["currency"] = '$' if mrp or price else "NA"
            item["serving_for_people"] = serving_for_people.strip() if serving_for_people else "NA"
            item["product_url"] = kwargs["url"]
            item["o_id"] = kwargs["id"]
            item["category"] = ' | '.join(response.xpath("//*[@class='b--list']/li/a/span/text()").getall()).replace(
                " | Online Grocery", '')
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
    execute(f"scrapy crawl CURL_data -a start=0 -a end=1000000".split())

'<div class="user__shop">'