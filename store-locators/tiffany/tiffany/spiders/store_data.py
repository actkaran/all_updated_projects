import json
import os.path
import random
from datetime import datetime
import scrapy
from scrapy.cmdline import execute

import tiffany.db_config as db
from tiffany.items import TiffanyData


class StoreDataSpider(scrapy.Spider):
    name = "store_data"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def start_requests(self):
        cookies = {
            'at_check': 'true',
            'rr_session_id': 'Habb9LG1dFRLudSj422kaNOHx2WvwxoN',
            'AMCVS_C7E83637539FFF380A490D44%40AdobeOrg': '1',
            'AMCV_C7E83637539FFF380A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C20005%7CMCMID%7C28273356572245672630999558948348479975%7CMCAAMLH-1728972411%7C12%7CMCAAMB-1728972411%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1728374811s%7CNONE%7CvVersion%7C5.2.0',
            '_cs_c': '0',
            '_abck': 'E3A6D122F672F5A139DC0D6887B2D4CA~0~YAAQzDtAF85qPFmSAQAAGdO8agzvvDesAAy4GXXJx5FcOuvOoweFvldNTF7YHyqBQdbx/0c9JzYC8MuG9TqPqTQwtZBTip1gt2ImpdDD2NNyLVZzEfquy+KEoB0z/pfeFWjlvDdK43UCNc+WcWpD6eLFOGWCav0mfoMQyGqwEH+CIDfl7Mp87kQwn8Uwasr2SnNay+CpkytqugPWlHxVX0mlsoInAExnJqaJDVbD+JXywWza+J4dR8qoiLhB1T4NdBpdx2l7vpBu7VN74ESN+8yUb7YLsyXeK5OvV/PfYETS0aLozUmxJ0Igm/wmQSb752UHWaALScUL0oVvul16K13F2LbU2Wf7Nd5Ldqt+aOc4lS4SbcJw6UmCUvBzeo6Jsr3JqXhFJJmxAbbbbqM8La+Qo+yBaPPXEgXupyntPj+Qba74XkllZu8aXnjnmSxgYDpVbnyHSOsHeA==~-1~||0||~-1',
            '__attentive_id': 'b145b99876094df695ff435480c2e733',
            '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzI4MzY3NjEzMTI2LFwidW9cIjoxNzI4MzY3NjEzMTI2LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImIxNDViOTk4NzYwOTRkZjY5NWZmNDM1NDgwYzJlNzMzXCJ9In0=',
            '__attentive_cco': '1728367613128',
            '__attentive_dv': '1',
            'siteVisited': 'true',
            '_mibhv': 'anon-1728367618513-1907453424_7762',
            '_ga': 'GA1.1.2060230549.1728367619',
            '_gcl_au': '1.1.1019611159.1728367619',
            '_scid': '-0DZ5MqjkACEgwTCAC6VoR1VlW4xnc8N',
            '_tt_enable_cookie': '1',
            '_ttp': 'lxZY-SOpth22jMEktZS_EW60d8F',
            '_fbp': 'fb.1.1728367619417.773824807784988918',
            '_pin_unauth': 'dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA',
            '_ScCbts': '%5B%5D',
            '_sctr': '1%7C1728325800000',
            'LPVID': 'Y5ZjE3M2FmMDY3MTk2MjE2',
            'dntstatus': '0',
            'samebrowsersession': '',
            'langprefforca': '-1',
            'ecmid': '',
            'myeid': '',
            'hascookies1': '1',
            'assortmentid': '101',
            'dtmusersessionid': 'a190a65bc7414d27892b0f27c2d62d72',
            'previoussid': '',
            'welcome_back_session_duplicate': 'true',
            'AKA_A2': 'A',
            'bm_sz': '307FE125B55DCDB24F5CB0C77EBC522A~YAAQzDtAF2P5PVmSAQAA4gUoaxlqZpOCh2rFiVTTXSYbGPCvpP26wfFO29dILwVS/APxfV0YTmgJug4lyavV1Wmuuma3zWQ4SN/5qfT3Z4LkflMTLXoWXpgYT1WkwdAatditMrvmMDuZfml0O1J1iesVTVRR10uEZbBBNO7vrYVAaU9MuhFoGyoESzS1mWS6hbSL8S1sEjQjdk/52hSbcqoeNT53DgcJqOXgpJ81V2+AX1gkbzlo77Dc+1YwB7Oa7wWmgWhdtt9yyUn28B+J5OzdkZSih060nHO/Vkh0+f6OQ/Vtyrv3aiMHR9x2X03HE2GZH/kbm6t2bBEthW2OZzksYqJMPzywjN0m5Gvgmllka8SPQI6l4UwalBN2IXjhAzmhxXT3ADV0XEiervrXFsV6aYx2L0HaPTHxVuOYsmBOVQElr2HhlexojC4OTsrTnD/AibwTEBSrrazCMDLxxk1NM2QlIBcM4kx62hTyxw0bjCSv3G28cdwkYkdTo5i+p4+xzAPBkjSSk3wnypF5dTdKFIVmACW/jNI=~4536626~3617347',
            '_ga_6LS0S7KLVS': 'GS1.1.1728374637.3.1.1728374645.52.0.2036183587',
            '_uetsid': '87565da0853b11efa447a71d7b6b96f5',
            '_uetvid': '87565b80853b11ef9015c3db37c27971',
            '_scid_r': 'D8DZ5MqjkACEgwTCAC6VoR1VlW4xnc8Nyxai6w',
            'LPSID-41337752': 'IlyK5mglQQ6IroQdD7lImw',
            'geo-location-cookie': 'US',
            '_cs_id': 'd210cf8f-4686-a197-d363-c5bfd52613e0.1728367611.4.1728378001.1728378001.1712004218.1762531611928.1',
            '_cs_s': '1.0.0.1728379801858',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Oct+08+2024+14%3A30%3A02+GMT%2B0530+(India+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSSPD_BG%3A1%2C4%3A1%2C2%3A1&AwaitingReconsent=false',
            'mbox': 'PC#19fb3e56b9954ab289427a055dfe10c4.34_0#1791622803|session#f2c414d41dfb4d3dbed16cfc2bf7114e#1728379862',
            'RT': '"z=1&dm=tiffany.com&si=9eda6b8f-39da-4d6f-b219-197b7c3449a5&ss=m205mta1&sl=0&tt=0&bcn=%2F%2F684d0d48.akstat.io%2F&hd=2052u"',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'at_check=true; rr_session_id=Habb9LG1dFRLudSj422kaNOHx2WvwxoN; AMCVS_C7E83637539FFF380A490D44%40AdobeOrg=1; AMCV_C7E83637539FFF380A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C20005%7CMCMID%7C28273356572245672630999558948348479975%7CMCAAMLH-1728972411%7C12%7CMCAAMB-1728972411%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1728374811s%7CNONE%7CvVersion%7C5.2.0; _cs_c=0; _abck=E3A6D122F672F5A139DC0D6887B2D4CA~0~YAAQzDtAF85qPFmSAQAAGdO8agzvvDesAAy4GXXJx5FcOuvOoweFvldNTF7YHyqBQdbx/0c9JzYC8MuG9TqPqTQwtZBTip1gt2ImpdDD2NNyLVZzEfquy+KEoB0z/pfeFWjlvDdK43UCNc+WcWpD6eLFOGWCav0mfoMQyGqwEH+CIDfl7Mp87kQwn8Uwasr2SnNay+CpkytqugPWlHxVX0mlsoInAExnJqaJDVbD+JXywWza+J4dR8qoiLhB1T4NdBpdx2l7vpBu7VN74ESN+8yUb7YLsyXeK5OvV/PfYETS0aLozUmxJ0Igm/wmQSb752UHWaALScUL0oVvul16K13F2LbU2Wf7Nd5Ldqt+aOc4lS4SbcJw6UmCUvBzeo6Jsr3JqXhFJJmxAbbbbqM8La+Qo+yBaPPXEgXupyntPj+Qba74XkllZu8aXnjnmSxgYDpVbnyHSOsHeA==~-1~||0||~-1; __attentive_id=b145b99876094df695ff435480c2e733; _attn_=eyJ1Ijoie1wiY29cIjoxNzI4MzY3NjEzMTI2LFwidW9cIjoxNzI4MzY3NjEzMTI2LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImIxNDViOTk4NzYwOTRkZjY5NWZmNDM1NDgwYzJlNzMzXCJ9In0=; __attentive_cco=1728367613128; __attentive_dv=1; siteVisited=true; _mibhv=anon-1728367618513-1907453424_7762; _ga=GA1.1.2060230549.1728367619; _gcl_au=1.1.1019611159.1728367619; _scid=-0DZ5MqjkACEgwTCAC6VoR1VlW4xnc8N; _tt_enable_cookie=1; _ttp=lxZY-SOpth22jMEktZS_EW60d8F; _fbp=fb.1.1728367619417.773824807784988918; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; _sctr=1%7C1728325800000; LPVID=Y5ZjE3M2FmMDY3MTk2MjE2; dntstatus=0; samebrowsersession=; langprefforca=-1; ecmid=; myeid=; hascookies1=1; assortmentid=101; dtmusersessionid=a190a65bc7414d27892b0f27c2d62d72; previoussid=; welcome_back_session_duplicate=true; AKA_A2=A; bm_sz=307FE125B55DCDB24F5CB0C77EBC522A~YAAQzDtAF2P5PVmSAQAA4gUoaxlqZpOCh2rFiVTTXSYbGPCvpP26wfFO29dILwVS/APxfV0YTmgJug4lyavV1Wmuuma3zWQ4SN/5qfT3Z4LkflMTLXoWXpgYT1WkwdAatditMrvmMDuZfml0O1J1iesVTVRR10uEZbBBNO7vrYVAaU9MuhFoGyoESzS1mWS6hbSL8S1sEjQjdk/52hSbcqoeNT53DgcJqOXgpJ81V2+AX1gkbzlo77Dc+1YwB7Oa7wWmgWhdtt9yyUn28B+J5OzdkZSih060nHO/Vkh0+f6OQ/Vtyrv3aiMHR9x2X03HE2GZH/kbm6t2bBEthW2OZzksYqJMPzywjN0m5Gvgmllka8SPQI6l4UwalBN2IXjhAzmhxXT3ADV0XEiervrXFsV6aYx2L0HaPTHxVuOYsmBOVQElr2HhlexojC4OTsrTnD/AibwTEBSrrazCMDLxxk1NM2QlIBcM4kx62hTyxw0bjCSv3G28cdwkYkdTo5i+p4+xzAPBkjSSk3wnypF5dTdKFIVmACW/jNI=~4536626~3617347; _ga_6LS0S7KLVS=GS1.1.1728374637.3.1.1728374645.52.0.2036183587; _uetsid=87565da0853b11efa447a71d7b6b96f5; _uetvid=87565b80853b11ef9015c3db37c27971; _scid_r=D8DZ5MqjkACEgwTCAC6VoR1VlW4xnc8Nyxai6w; LPSID-41337752=IlyK5mglQQ6IroQdD7lImw; geo-location-cookie=US; _cs_id=d210cf8f-4686-a197-d363-c5bfd52613e0.1728367611.4.1728378001.1728378001.1712004218.1762531611928.1; _cs_s=1.0.0.1728379801858; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+08+2024+14%3A30%3A02+GMT%2B0530+(India+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSSPD_BG%3A1%2C4%3A1%2C2%3A1&AwaitingReconsent=false; mbox=PC#19fb3e56b9954ab289427a055dfe10c4.34_0#1791622803|session#f2c414d41dfb4d3dbed16cfc2bf7114e#1728379862; RT="z=1&dm=tiffany.com&si=9eda6b8f-39da-4d6f-b219-197b7c3449a5&ss=m205mta1&sl=0&tt=0&bcn=%2F%2F684d0d48.akstat.io%2F&hd=2052u"',
            'priority': 'u=0, i',
            'referer': 'https://www.tiffany.com/jewelry-stores/store-list/united-states/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        query = f"SELECT * FROM {db.db_link_table} WHERE status='save'"
        db.cur.execute(query)
        rows = db.cur.fetchall()
        for row in rows:
            url = row[1]
            sku = row[2]
            hash_url = row[3]

            if os.path.exists(f"{db.PAGESAVE}{hash_url}.html"):
                yield scrapy.Request(url=f"file:///C:/PAGESAVE/TIFFANY/{hash_url}.html",
                                     callback=self.parse,
                                     cb_kwargs={"url": url,
                                                "sku": sku,
                                                "hash_url": hash_url,
                                                }
                                     )
            # break

    def parse(self, response, **kwargs):
        url = kwargs["url"]
        sku = kwargs["sku"]
        hash_url = kwargs["hash_url"]
        try:
            data = response.xpath('''// script[ @ type = "application/ld+json"]/text()''').getall()[0]
            jd = json.loads(data)
        except:
            db.cur.execute(f"UPDATE {db.db_link_table} SET status='NA' WHERE hash_url=%s", (hash_url,))
            db.con.commit()
            print("NA")
            return None
        if jd["@type"] == "Store":
            opening_hours = jd["openingHours"].split("<br>")
            temp = []
            if opening_hours:
                for line in opening_hours:
                    if "AM" in line or "PM" in line or "Closed" in line:
                        temp.append(line.strip())
            address = jd["address"] if "address" in jd else None
            gmap_url = jd["hasMap"]
            try:
                lat = gmap_url.split("sll=")[-1].split(',')[0]
                lng = gmap_url.split("sll=")[-1].split(',')[1]
            except:
                lat = lng = None

            item = TiffanyData()
            item["store_no"] = 'NA'
            item["name"] = jd["name"]
            item["latitude"] = lat if lat else 'NA'
            item["longitude"] = lng.rstrip("'") if lng else 'NA'
            item["street"] = address["streetAddress"]
            item["city"] = address["addressLocality"]
            item["state"] = address["addressRegion"] if address["addressRegion"] else "NA"
            item["zip_code"] = address["postalCode"]
            item["county"] = 'NA'
            item["phone"] = jd["telephone"]
            item["open_hours"] = ' | '.join(temp).strip("|") if temp else "NA"
            item["url"] = url
            item["provider"] = 'Tiffany & Co.'
            item["category"] = 'Jewelry and Gift Engraving'
            item["updated_date"] = "NA"
            item["country"] = address["addressCountry"] if address else None
            item["status"] = 'Open'
            item["direction_url"] = gmap_url
            item["hash_url"] = hash_url

            yield item


if __name__ == "__main__":
    execute(f"scrapy crawl {StoreDataSpider.name} --nolog".split())
