import gzip
import html
import os.path
import random
import re
import time

import chardet
from parsel import Selector

import metro_canada.db_config as db
import pymysql
from curl_cffi import requests

# insert the scraped data into dataTable...and update the status...
def insert_data(item):
    try:
        temp_id = item["o_id"]
        del item["o_id"]
        cols = ", ".join(item.keys()).strip(', ')
        values = tuple(item.values())
        insert = f"""INSERT INTO {db.db_data_table} ({cols}) VALUES {values}"""
        cur.execute(insert)
        con.commit()
        print("Inserted....", temp_id)
        update = f"""UPDATE {db.db_link_table} SET status='Done' WHERE id=%s"""
        cur.execute(update, (temp_id,))
        con.commit()
    except pymysql.err.IntegrityError:
        print("Duplicate...")
    except Exception as e:
        print(e)

#  scrape pdp data from response...
def scrape_data(response=None, url=None, id=None):
    if isinstance(response, bytes):
        detected = chardet.detect(response)
        encoding = detected['encoding']
        response = Selector(text=response.decode(encoding))
    item= {}
    price = response.xpath("//div[@data-main-price]/@data-main-price").get()
    product_name = response.xpath("string(//div[@class='pi--name'])").get()
    mrp = response.xpath("//div[@class='pricing__before-price']/span[contains(text(),'$')]/text()").get()
    quantity = response.xpath("//div[@class='pi--weight']/text()").get()
    price_per_unit = response.xpath("string(//div[contains(@class, 'pricing__secondary-price')])").get()
    serving_for_people = response.xpath(
        "//select[contains(@class, 'select select-addToCart')]/option[contains(@default-option, 'true')]/font/font/text()").get()
    product_image = response.xpath("//picture[@id='main-img']/source[contains(@id, 'desk-img')]/@srcset").get()
    h = ''.join(response.xpath("string(//div[@class='accordion--text'])").getall())
    ingredients = response.xpath("//p[@class='pdp-ingredients-list']/text()").get()
    valid_till = response.xpath("string(//div[@class='pricing__until-date'])").get()
    item["mrp"] = mrp.strip() if mrp else "NA"
    item["price"] = price.strip() if price else "NA"
    item["currency"] = '$' if mrp or price else "NA"
    item["serving_for_people"] = serving_for_people.strip() if serving_for_people else "NA"
    item["product_url"] = url
    item["o_id"] = id
    item["category"] = ' | '.join(response.xpath("//*[@class='b--list']/li/a/span/text()").getall()).replace(
        " | Online Grocery", '')
    item["valid_date"] = valid_till.strip() if valid_till else "NA"
    item["product_name"] = product_name.strip() if product_name else "NA"
    item["product_number"] = item["product_url"].split('/')[-1]
    item["ingredients"] = ingredients.strip() if ingredients else "NA"
    item["product_description"] = re.sub(r'\s+', ' ', h).strip()
    item["product_image"] = product_image if product_image else "NA"
    item["price_per_unit"] = html.unescape(price_per_unit.strip()) if price_per_unit else "NA"
    item["quantity"] = quantity.strip() if quantity else "NA"
    insert_data(item)


# this function made for saving the source code into gzip html file...if not exists then....
def save_page(response=None, id=None):
    path = f"{db.PAGESAVE}{id}.html.gz"
    if not os.path.exists(path):
        with gzip.open(f"{db.PAGESAVE}{id}.html.gz", 'wb') as f:
            f.write(response)

# this function is for sending requests and if page save exists then returning that page's source code...
def send_req(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'METRO_ANONYMOUS_COOKIE=65fa2e64-7847-4606-a2c4-a3ac7a0d2b52; coveo_visitorId=a814bba8-aa4f-4d91-ab75-7c01e0855c3a; hprl=en; OptanonAlertBoxClosed=2024-11-04T05:33:47.312Z; _gcl_au=1.1.1054953059.1730698427; _ga=GA1.1.2012213354.1730698427; _fbp=fb.1.1730698429165.546947856149314023; coveo_visitorId=a814bba8-aa4f-4d91-ab75-7c01e0855c3a; CRITEO_RETAILER_VISITOR_COOKIE=31c49437-0aef-4b74-adcd-5ba6f23f4de7; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=1116a3dbacfa57ebaff6b9c8b37c3deda3cf0f801e79b0cf2e8abafc1cefde95dc7a1d5d; __gads=ID=4420b56cdc5bd703:T=1730869930:RT=1730869930:S=ALNI_MZyjfkZefdgE4IbdwYGE2-02KT8sg; __gpi=UID=00000f5b1e8f9308:T=1730869930:RT=1730869930:S=ALNI_MY3TwvoVCDOzImJM7p1gRxh0RQVcQ; __eoi=ID=31d748cd1555f40b:T=1730869930:RT=1730869930:S=AA-Afjat65FVGf8ED9dG1VaJUSHf; _clck=1lp0cfw%7C2%7Cfqn%7C0%7C1769; _uetsid=49b9fab09b4411efb5a85f8eb239025f; _uetvid=21c5ffe095d111ef86de4598779feada; _clsk=ej1cmm%7C1730869931814%7C1%7C1%7Ck.clarity.ms%2Fcollect; JSESSIONID=9CC3440C0A47EA36B35B6D848C790819; APP_D_USER_ID=lrbMUCkN-2164996596; cf_clearance=nWvH7wsxLm2VsEbBHTD.ryMND8RtJ1n3.sMiAZiZNgw-1730874055-1.2.1.1-vcfAPqRWW8ztG..eLwY2QCgytbxvsN7bZxJ74EqtsWV5M177XtH6.f0Ia0lRG1D5Lo75QcCqMJbgNBAndFrYAlgaTlwW6KGHC4cSaTBKYa6lmLHM8.ZWHhE3W8CsAVw3PtEIgigCTs0MjAxksRKp.m_Sg6A479eEVOyiKkokP4XwBHFYw.w7z_OR2uxvSjr5P8kxpZkh40pf.xJiyXvVlPz0q_icDNP10C3ek9MZQUjx1LTH2o3S.QP5XLb9FK44_XHJrq2ChX9TAupmxxY2l7n9OSiivWLb8HzdXiwXzw00s7eioOQdqHZmCBIHedDAU_WJ2QXRo_4tj9py2ZekytVckTxHQA2CJ7YcufssM.xnpffH03xcr8R7zLV1HtoX; __cf_bm=RmSE2N28GaqNED6QYhMZBTDcsOYjrVmoUimJjjTezx0-1730874137-1.0.1.1-VdkDy24AsSumtaPLk5fZO0r_RiD6ZWKURZHmW7_PhE68D8WijJ8YOJ_YwS1oW3KEQ5CBO0t43Y9iOtdWAAl0khvgH6uHhXEWnXWkt9m8_Pc; SameSite=None; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+11%3A52%3A18+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _ga_RSMJC35YH9=GS1.1.1730874053.5.0.1730874138.59.0.0; _conv_v=vi%3A1*sc%3A6*cs%3A1730874057*fs%3A1730698428*pv%3A10*ps%3A1730869931*exp%3A%7B%7D; _conv_s=si%3A6*sh%3A1730874056957-0.6444900721288347*pv%3A2; cto_bundle=frNc-F9NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QWsySkg2bU5BbXh5S3hGM0UlMkJndlZ0Q1JlYnJHaVFkOEp2VlE3V0lHQ0NnUlZuTU9pckNDJTJCczdvd2c2NSUyRjZsV2dFMG54bVJ0OGVlb1F3U1dpMUh4ZyUyRlV3Um9sNGVNcDU3WVNtVGN0SnZOdDJKNnNEd2hONVYydVVoSUtMeTFLTTFRJTNEJTNE; forterToken=552dd3c56da24fb2bc2f1685b5599b52_1730874137877__UDF43-m4_21ck_; forter-uid=552dd3c56da24fb2bc2f1685b5599b52_1730874137877__UDF43-m4_21ck__tt; ADRUM_BTa=R:0|g:0236c686-3e88-42c9-861b-c81faad4597a|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:0|i:268164|e:319',
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
    proxy = {'http':'http://scraperapi:de51e4aafe704395654a32ba0a14494d@proxy-server.scraperapi.com:8001'}
    path = f"{db.PAGESAVE}{id}.html.gz"
    if os.path.exists(path):
        with gzip.open(f"{db.PAGESAVE}{id}.html.gz", 'rb') as f:
            content = f.read()
        return {"status": 200, 'response': content}
    else:
        response = requests.get(
            url=url,
            # cookies=cookies,
            headers=headers,
            impersonate=random.choice(["chrome110", "edge99", "safari15_5"]),
            proxies=proxy
        )
        return {"status": response.status_code, 'response': response.content}


if __name__ == "__main__":
    # this is local system's connection...
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()
    # cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' LIMIT 0, 100;")
    cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending';")
    data = cur.fetchall()
    # print("fetched", data)
    for i in data:
        url = i[1]
        id = i[0]
        temp_var = send_req(url=url)
        if temp_var["status"] == 200:
            save_page(temp_var["response"], id)
            scrape_data(temp_var["response"], url, id)
            # time.sleep(1.2)
        elif temp_var["status"] == 429:
            time.sleep(1.7)
            print("too many request...")
        else:
            print(temp_var["status"])
        # break
