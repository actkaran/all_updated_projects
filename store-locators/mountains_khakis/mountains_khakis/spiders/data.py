from scrapy import Request
import scrapy
from scrapy.cmdline import execute
import mountains_khakis.db_config as db
from mountains_khakis.items import MountainsKhakisItem


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.mountainkhakis.com"]
    cookies = {
        '__blockify::referrer': '%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D',
        '__blockify::analyzer': '%7B%22startTime%22%3A1732775757030%2C%22sessionId%22%3A%22fac344c9-2355-4efd-8212-0768c76d865d%22%7D',
        'secure_customer_sig': '',
        'localization': 'US',
        'cart_currency': 'USD',
        '_vwo_uuid_v2': 'D9CC68B464E1DB7805B01D172CCDFA689|9437c5382b0c730e2b2859ed62d4261f',
        'shopify_pay_redirect': 'pending',
        '_pin_unauth': 'dWlkPU0yUmtOamMwWTJVdE16QTVOUzAwWmprMUxXRmtZV1V0TlRaaVlqSTBZV0UwWWpsaw',
        '_fbp': 'fb.1.1732775754887.917924044281777603',
        '_clck': '2h3s2t%7C2%7Cfr9%7C0%7C1793',
        '_cmp_a': '%7B%22purposes%22%3A%7B%22p%22%3Atrue%2C%22a%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Atrue%2C%22sale_of_data_region%22%3Afalse%7D',
        '_orig_referrer': 'https%3A%2F%2Fwww.google.com%2F',
        '_landing_page': '%2Fpages%2Foutlet-stores%3Fsrsltid%3DAfmBOorn55UrGRq6XyNrSyxdexWcDUa4JqVFMHxj9Iee2sXUqb8RI0Ft',
        '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%221%22%2C%22m%22%3A%221%22%2C%22p%22%3A%221%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22INGJ%22%2C%22reg%22%3A%22%22%2C%22purposes%22%3A%7B%22p%22%3Atrue%2C%22a%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Atrue%2C%22sale_of_data_region%22%3Afalse%2C%22consent_id%22%3A%22F410DE73-f2bf-4333-9a2d-0ac08079123a%22%7D',
        '_shopify_y': 'eae72757-4d39-4d0e-a8ea-d5dabc0eeb41',
        '_shopify_s': '0df79a19-8385-434c-abc8-07bad318c83b',
        '_gcl_au': '1.1.396729576.1732775756',
        '_shopify_sa_t': '2024-11-28T06%3A35%3A56.250Z',
        '_shopify_sa_p': '',
        '_gid': 'GA1.2.1902048060.1732775756',
        '_ps_session': 'ZAFZZ3_ng7fHI3jLmKve1',
        '_rsession': 'aca1b280cd8dbfe6',
        '_ruid': 'eyJ1dWlkIjoiZDYwYjMwMDAtNWNjZC00ZjUxLWFjY2UtZDdjNmM3YzUxNGRjIn0%3D',
        '_pin_unauth': 'dWlkPU0yUmtOamMwWTJVdE16QTVOUzAwWmprMUxXRmtZV1V0TlRaaVlqSTBZV0UwWWpsaw',
        '_tt_enable_cookie': '1',
        '_ttp': '1_7xPHJXu0NvCzsoqYRGwop4rMk.tt.0',
        'cart': 'Z2NwLWFzaWEtc291dGhlYXN0MTowMUpEUlFRSk03WEZNQ00xNk5QVzdUNVY0Wg%3Fkey%3D63105ec86e61c52494f4b08472fef987',
        'cart_ts': '1732775758',
        'cart_sig': '4ba2d1d738e1e2aedcdc35538a19ef4b',
        '_ps_pop_86c3ca54-1277-44ac-8242-6c19d20334d4': 'r',
        '_shopify_sa_p': '',
        'keep_alive': 'd995697d-0ac4-4891-b857-d0d939090339',
        '_shopify_s': '0df79a19-8385-434c-abc8-07bad318c83b',
        '_shopify_sa_t': '2024-11-28T06%3A38%3A05.014Z',
        '_ga': 'GA1.1.2039332568.1732775755',
        '_ga_Y8L2H62S0K': 'GS1.1.1732775754.1.1.1732775885.1.0.0',
        '_ga_J64DEJ39X0': 'GS1.1.1732775756.1.1.1732775885.0.0.0',
        '_uetsid': '04f3f450ad5311ef99671bdcf968cd47',
        '_uetvid': '04f41c80ad5311efaea02d7af30c4c6b',
        'landingPage': 'refresh',
        'logState': 'loggedOut',
        '__kla_id': 'eyJjaWQiOiJOakprTldVeE16a3ROVE0xWVMwME5XRmtMVGs0T0RFdE1UVmpNemhpTmpBMFl6RmoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MzI3NzU3NTYsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW91bnRhaW5raGFraXMuY29tL3BhZ2VzL291dGxldC1zdG9yZXM/c3JzbHRpZD1BZm1CT29ybjU1VXJHUnE2WHlOclN5eGRleFdjRFVhNEpxVkZNSHhqOUllZTJzWFVxYjhSSTBGdCJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTczMjc3NTg4NiwidmFsdWUiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tb3VudGFpbmtoYWtpcy5jb20vcGFnZXMvb3V0bGV0LXN0b3Jlcz9zcnNsdGlkPUFmbUJPb3JuNTVVckdScTZYeU5yU3l4ZGV4V2NEVWE0SnFWRk1IeGo5SWVlMnNYVXFiOFJJMEZ0In19',
        '_clsk': '1y6j0xz%7C1732775886035%7C7%7C1%7Co.clarity.ms%2Fcollect',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '__blockify::referrer=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; __blockify::analyzer=%7B%22startTime%22%3A1732775757030%2C%22sessionId%22%3A%22fac344c9-2355-4efd-8212-0768c76d865d%22%7D; secure_customer_sig=; localization=US; cart_currency=USD; _vwo_uuid_v2=D9CC68B464E1DB7805B01D172CCDFA689|9437c5382b0c730e2b2859ed62d4261f; shopify_pay_redirect=pending; _pin_unauth=dWlkPU0yUmtOamMwWTJVdE16QTVOUzAwWmprMUxXRmtZV1V0TlRaaVlqSTBZV0UwWWpsaw; _fbp=fb.1.1732775754887.917924044281777603; _clck=2h3s2t%7C2%7Cfr9%7C0%7C1793; _cmp_a=%7B%22purposes%22%3A%7B%22p%22%3Atrue%2C%22a%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Atrue%2C%22sale_of_data_region%22%3Afalse%7D; _orig_referrer=https%3A%2F%2Fwww.google.com%2F; _landing_page=%2Fpages%2Foutlet-stores%3Fsrsltid%3DAfmBOorn55UrGRq6XyNrSyxdexWcDUa4JqVFMHxj9Iee2sXUqb8RI0Ft; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%221%22%2C%22m%22%3A%221%22%2C%22p%22%3A%221%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22INGJ%22%2C%22reg%22%3A%22%22%2C%22purposes%22%3A%7B%22p%22%3Atrue%2C%22a%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Atrue%2C%22sale_of_data_region%22%3Afalse%2C%22consent_id%22%3A%22F410DE73-f2bf-4333-9a2d-0ac08079123a%22%7D; _shopify_y=eae72757-4d39-4d0e-a8ea-d5dabc0eeb41; _shopify_s=0df79a19-8385-434c-abc8-07bad318c83b; _gcl_au=1.1.396729576.1732775756; _shopify_sa_t=2024-11-28T06%3A35%3A56.250Z; _shopify_sa_p=; _gid=GA1.2.1902048060.1732775756; _ps_session=ZAFZZ3_ng7fHI3jLmKve1; _rsession=aca1b280cd8dbfe6; _ruid=eyJ1dWlkIjoiZDYwYjMwMDAtNWNjZC00ZjUxLWFjY2UtZDdjNmM3YzUxNGRjIn0%3D; _pin_unauth=dWlkPU0yUmtOamMwWTJVdE16QTVOUzAwWmprMUxXRmtZV1V0TlRaaVlqSTBZV0UwWWpsaw; _tt_enable_cookie=1; _ttp=1_7xPHJXu0NvCzsoqYRGwop4rMk.tt.0; cart=Z2NwLWFzaWEtc291dGhlYXN0MTowMUpEUlFRSk03WEZNQ00xNk5QVzdUNVY0Wg%3Fkey%3D63105ec86e61c52494f4b08472fef987; cart_ts=1732775758; cart_sig=4ba2d1d738e1e2aedcdc35538a19ef4b; _ps_pop_86c3ca54-1277-44ac-8242-6c19d20334d4=r; _shopify_sa_p=; keep_alive=d995697d-0ac4-4891-b857-d0d939090339; _shopify_s=0df79a19-8385-434c-abc8-07bad318c83b; _shopify_sa_t=2024-11-28T06%3A38%3A05.014Z; _ga=GA1.1.2039332568.1732775755; _ga_Y8L2H62S0K=GS1.1.1732775754.1.1.1732775885.1.0.0; _ga_J64DEJ39X0=GS1.1.1732775756.1.1.1732775885.0.0.0; _uetsid=04f3f450ad5311ef99671bdcf968cd47; _uetvid=04f41c80ad5311efaea02d7af30c4c6b; landingPage=refresh; logState=loggedOut; __kla_id=eyJjaWQiOiJOakprTldVeE16a3ROVE0xWVMwME5XRmtMVGs0T0RFdE1UVmpNemhpTmpBMFl6RmoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MzI3NzU3NTYsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW91bnRhaW5raGFraXMuY29tL3BhZ2VzL291dGxldC1zdG9yZXM/c3JzbHRpZD1BZm1CT29ybjU1VXJHUnE2WHlOclN5eGRleFdjRFVhNEpxVkZNSHhqOUllZTJzWFVxYjhSSTBGdCJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTczMjc3NTg4NiwidmFsdWUiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5tb3VudGFpbmtoYWtpcy5jb20vcGFnZXMvb3V0bGV0LXN0b3Jlcz9zcnNsdGlkPUFmbUJPb3JuNTVVckdScTZYeU5yU3l4ZGV4V2NEVWE0SnFWRk1IeGo5SWVlMnNYVXFiOFJJMEZ0In19; _clsk=1y6j0xz%7C1732775886035%7C7%7C1%7Co.clarity.ms%2Fcollect',
        'if-none-match': '"cacheable:75feb35e8be589f0d7fbbabcb84ac320"',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        yield Request(
            url = 'https://www.mountainkhakis.com/pages/stores',
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse
        )
        
    def parse(self, response):
        with open(f"{db.PAGESAVE}demo.html", "w") as f:
            f.write(response.text)
        item = MountainsKhakisItem()
        item["store_no"] = 'NA'
        item["longitude"] = 'NA'
        item["latitude"] = 'NA'
        item["city"] = 'NA'
        item["state"] = 'NA'
        item["zip_code"] = 'NA'
        item["county"] = 'NA'
        item["country"] = 'USA'
        item["status"] = 'Open'
        item["url"] = 'https://www.mountainkhakis.com/pages/stores'
        item["provider"] = 'Mountain Khakis'
        item["category"] = 'outdoor apparel'
        item["updated_date"] = 'NA'

        # above info will be static because there is no such information found in the html page.
        # looping over the container of each store...
        for abc in response.xpath("//div[@class='core__blocks']/div[@class='core__blocks--body']"):
            name = abc.xpath(".//h2[@class='ecom__heading ecom-db']/text()").get()
            if name:
                item["name"] = name
                # both xpath for address is working..
                # address = ', '.join(abc.xpath(".//u//text()").getall())
                address = ', '.join(abc.xpath(
                    ".//a[contains(@href, '/g.') or contains(@href, 'https://goo.gl/maps/')]//text()").getall())
                temp_address = '+'.join(address.split())
                # temp_address = address.replace(",", '').strip().split()

                # direction_url = abc.xpath(".//a[contains(@href, '/g.') or contains(@href, 'https://goo.gl/maps/')]/@href").get()
                item["direction_url"] = f"https://www.google.com/maps/dir/Current+Location/{temp_address},+{item['country']}/"
                item["street"] = address
                del temp_address
                item["phone_number"] = abc.xpath(".//div[contains(., '(' ) and contains(., ')')]/text() | .//span[contains(., '(' ) and contains(., ')')]/text()").get()
                item["open_hours"] = ' | '.join(abc.xpath(".//div[contains(@class, 'element__text') and (contains(., 'AM') or contains(., 'PM') or contains(translate(., 'CLOSED', 'closed'), 'closed'))]//text()").getall()).replace("xa0",'').strip()
                yield item

if __name__ == '__main__':
    execute("scrapy crawl data".split())