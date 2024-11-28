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
        # ad your headers here with the uncomment cookie.
    }
    # pt = [{'http':f"http://scraperapi:{db.scraper_proxy}@proxy-server.scraperapi.com:8001"},
    #       {'http': f"http://{db.zyte_proxy_key}:@api.zyte.com:8011"}
    #       ]
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
            proxies={'http':f"http://scraperapi:{db.scraper_proxy}@proxy-server.scraperapi.com:8001"}
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
            if temp_var["status"] == 403:
                time.sleep(2.7)
                print(temp_var["status"])
            print(temp_var["status"])
        # break
