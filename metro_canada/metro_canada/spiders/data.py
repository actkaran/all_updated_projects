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
    # cookies = {
    #     'JSESSIONID': 'BE3B3C05B595DB280EE14F9ABA86D03E',
    #     'METRO_ANONYMOUS_COOKIE': '3a2b998b-6e52-435d-98c0-1d030a95eee8',
    #     'CRITEO_RETAILER_VISITOR_COOKIE': 'ac9bab2d-7aec-4721-b0f9-10ff1c69b3c4',
    #     'APP_D_USER_ID': 'qyyREHVE-2166830715',
    #     'coveo_visitorId': 'c3f5f51e-95ca-4d80-93eb-979d35c2c1ae',
    #     'hprl': 'en',
    #     'NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei': '7ce2a3d962d27f5ea1cd1e3db6635daedc41859d2c02429002b6bf78a132ae009a39533e',
    #     '_ga': 'GA1.1.1093776326.1730877757',
    #     'coveo_visitorId': 'c3f5f51e-95ca-4d80-93eb-979d35c2c1ae',
    #     '_gcl_au': '1.1.1099375172.1730877757',
    #     'OptanonAlertBoxClosed': '2024-11-06T07:22:39.944Z',
    #     '_fbp': 'fb.1.1730877760680.653511761591064627',
    #     '__cf_bm': 'VHvYbJuwGCMC2vvVU2.gtx.0SzGQd86HrpyZyqacYos-1730878037-1.0.1.1-t_SpBbAvi_Ps6YydsFx796gSluOpfdvJpzJFVZluR5hbO4d5WoryHy9nXtctTclipicR88p6Z5OEY1RbTbZ1J3HLyGalZG3qzUqC4.ePB1c',
    #     'cf_clearance': 'qC2ZygsiCIdVOfB8vTEmXPEmfUX0Niqpf7Nd.vPici0-1730878038-1.2.1.1-Gj4IxLP3yS8RR6.PsGPnB4aE4nARyNz0hq0uw2AqgvoZFdpUyYo2ikHyvdz.H5_.Bc.G62R0ft5hKXISnZ9W57cSHGz2PoPJlUjDh2fSJuizAxZFR8c7Bmn0AAUd8sj5KgJxQqLFX51vJ9j_Ymwll65Y_W7n_XSV_SlqcZjHTL5fqiEGEUItoj3RQRT53g7TMjIhMw1ZxiqrAWP2vIJ3ZszZErfE1x.kn8hH4BzmPvg1zGk3D0ZXtZntQow5b9cnOCGfJlNriaeGSfGNruHnNx2UxzmxkSVcK7_lCcRQm4NmJComHSzM.MjzidLqG2MtN4EqVDR4G4a6pPQqPDOJYYGDuw4keRHx4gkADIe7AFcURqA880oWI7WA11H2xGdC',
    #     '_clck': '1i16p2g%7C2%7Cfqn%7C0%7C1771',
    #     'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Nov+06+2024+13%3A01%3A42+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false',
    #     '_ga_RSMJC35YH9': 'GS1.1.1730877757.1.1.1730878302.59.0.0',
    #     '_uetsid': 'ead56fe09c0f11efb63d6b762397b31c',
    #     '_uetvid': 'ead5b7809c0f11efb0eed396762de15c',
    #     '_conv_v': 'vi%3A1*sc%3A9*cs%3A1730877757*fs%3A1730698428*pv%3A21*ps%3A1730877733*exp%3A%7B%7D',
    #     '_conv_s': 'si%3A9*sh%3A1730877757419-0.7900692276254371*pv%3A7',
    #     'cto_bundle': 'MepNo19NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QXFrREElMkJZdmUyWFZUWE5CZFFVaDFJcUROeVA4WmVIU2lHMlZSTlNscDZrNERhWjQ5TTBTek1DU3daaSUyQk1aWW9ZJTJCTVlKdE1DS0JkWU56MW9RdjdxMkY2Q2MyRERqclg2UVh5RFZ5JTJGeHRpMzE1YUs4THR3NHZ3QjBCd0dGUHZhJTJGc1ElM0QlM0Q',
    #     '_clsk': 'svc2ui%7C1730878306065%7C3%7C1%7Co.clarity.ms%2Fcollect',
    #     'forterToken': '552dd3c56da24fb2bc2f1685b5599b52_1730878301568__UDF43-m4_21ck_',
    #     'forter-uid': '552dd3c56da24fb2bc2f1685b5599b52_1730878301568__UDF43-m4_21ck__tt',
    # }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'JSESSIONID=BE3B3C05B595DB280EE14F9ABA86D03E; METRO_ANONYMOUS_COOKIE=3a2b998b-6e52-435d-98c0-1d030a95eee8; CRITEO_RETAILER_VISITOR_COOKIE=ac9bab2d-7aec-4721-b0f9-10ff1c69b3c4; APP_D_USER_ID=qyyREHVE-2166830715; coveo_visitorId=c3f5f51e-95ca-4d80-93eb-979d35c2c1ae; hprl=en; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=7ce2a3d962d27f5ea1cd1e3db6635daedc41859d2c02429002b6bf78a132ae009a39533e; _ga=GA1.1.1093776326.1730877757; coveo_visitorId=c3f5f51e-95ca-4d80-93eb-979d35c2c1ae; _gcl_au=1.1.1099375172.1730877757; OptanonAlertBoxClosed=2024-11-06T07:22:39.944Z; _fbp=fb.1.1730877760680.653511761591064627; __cf_bm=VHvYbJuwGCMC2vvVU2.gtx.0SzGQd86HrpyZyqacYos-1730878037-1.0.1.1-t_SpBbAvi_Ps6YydsFx796gSluOpfdvJpzJFVZluR5hbO4d5WoryHy9nXtctTclipicR88p6Z5OEY1RbTbZ1J3HLyGalZG3qzUqC4.ePB1c; cf_clearance=qC2ZygsiCIdVOfB8vTEmXPEmfUX0Niqpf7Nd.vPici0-1730878038-1.2.1.1-Gj4IxLP3yS8RR6.PsGPnB4aE4nARyNz0hq0uw2AqgvoZFdpUyYo2ikHyvdz.H5_.Bc.G62R0ft5hKXISnZ9W57cSHGz2PoPJlUjDh2fSJuizAxZFR8c7Bmn0AAUd8sj5KgJxQqLFX51vJ9j_Ymwll65Y_W7n_XSV_SlqcZjHTL5fqiEGEUItoj3RQRT53g7TMjIhMw1ZxiqrAWP2vIJ3ZszZErfE1x.kn8hH4BzmPvg1zGk3D0ZXtZntQow5b9cnOCGfJlNriaeGSfGNruHnNx2UxzmxkSVcK7_lCcRQm4NmJComHSzM.MjzidLqG2MtN4EqVDR4G4a6pPQqPDOJYYGDuw4keRHx4gkADIe7AFcURqA880oWI7WA11H2xGdC; _clck=1i16p2g%7C2%7Cfqn%7C0%7C1771; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+13%3A01%3A42+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _ga_RSMJC35YH9=GS1.1.1730877757.1.1.1730878302.59.0.0; _uetsid=ead56fe09c0f11efb63d6b762397b31c; _uetvid=ead5b7809c0f11efb0eed396762de15c; _conv_v=vi%3A1*sc%3A9*cs%3A1730877757*fs%3A1730698428*pv%3A21*ps%3A1730877733*exp%3A%7B%7D; _conv_s=si%3A9*sh%3A1730877757419-0.7900692276254371*pv%3A7; cto_bundle=MepNo19NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QXFrREElMkJZdmUyWFZUWE5CZFFVaDFJcUROeVA4WmVIU2lHMlZSTlNscDZrNERhWjQ5TTBTek1DU3daaSUyQk1aWW9ZJTJCTVlKdE1DS0JkWU56MW9RdjdxMkY2Q2MyRERqclg2UVh5RFZ5JTJGeHRpMzE1YUs4THR3NHZ3QjBCd0dGUHZhJTJGc1ElM0QlM0Q; _clsk=svc2ui%7C1730878306065%7C3%7C1%7Co.clarity.ms%2Fcollect; forterToken=552dd3c56da24fb2bc2f1685b5599b52_1730878301568__UDF43-m4_21ck_; forter-uid=552dd3c56da24fb2bc2f1685b5599b52_1730878301568__UDF43-m4_21ck__tt',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"130.0.6723.93"',
        'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.93", "Google Chrome";v="130.0.6723.93", "Not?A_Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        # header and cookies will be here...

        self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' LIMIT 10;")
        # self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='saved' LIMIT 10;")
        # self.cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND id='11023';")
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
                api_key = ''
                url_final = f'http://api.scraperapi.com?api_key=de51e4aafe704395654a32ba0a14494d&url={url}&keep_headers=true'
                yield scrapy.Request(url=url_final,
                                     headers=self.headers,
                                     # cookies=self.cookies,
                                     callback=self.parse,
                                     dont_filter=True,
                                     # meta={'proxy':"http://scraperapi.country_code=ca&keep_headers=true:de51e4aafe704395654a32ba0a14494d@proxy-server.scraperapi.com:8001"},
                                     # meta={'impersonate': random.choice(["chrome110", "edge99", "safari15_5"])},
                                     cb_kwargs={"url": url,
                                                "id": id,
                                                "exists":0}
                                     )
            break

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
        price_per_unit = response.xpath("string(//div[contains(@class, 'pricing__secondary-price')])").get()
        serving_for_people = response.xpath("//select[contains(@class, 'select select-addToCart')]/option[contains(@default-option, 'true')]/font/font/text()").get()
        product_image = response.xpath("//picture[@id='main-img']/source[contains(@id, 'desk-img')]/@srcset").get()
        h = ''.join(response.xpath("string(//div[@class='accordion--text'])").getall())
        ingredients = response.xpath("//p[@class='pdp-ingredients-list']/text()").get()
        valid_till = response.xpath("string(//div[@class='pricing__until-date'])").get()
        item["mrp"] = mrp.strip() if mrp else "NA"
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
        item["price_per_unit"] = html.unescape(price_per_unit.strip()) if price_per_unit else "NA"
        item["quantity"] = quantity.strip() if quantity else "NA"
        yield item


if __name__ == "__main__":
    execute(f"scrapy crawl {DataSpider.name}".split())
