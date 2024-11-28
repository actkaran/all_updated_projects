import json

import scrapy
from scrapy.cmdline import execute


class DataScaniaSpider(scrapy.Spider):
    name = "data_scania"
    allowed_domains = ["www.scania.com"]

    cookies = {
        'ConfidentialityAgreement': '{%22necessary%22:true%2C%22performance%22:true%2C%22functional%22:true%2C%22targeting%22:true%2C%22socialMedia%22:true}',
        'kndctr_BCC792C056A0AB647F000101_AdobeOrg_cluster': 'ind1',
        'kndctr_BCC792C056A0AB647F000101_AdobeOrg_consent': 'general=in',
        'kndctr_BCC792C056A0AB647F000101_AdobeOrg_identity': 'CiYzNDMxOTE3ODg2NjExMzI4MTM2MDM3OTE2MDUzNDEwNTM3Mzg3MlIRCNTyteqiMhgBKgRJTkQxMAHwAdTyteqiMg==',
        'AMCV_BCC792C056A0AB647F000101%40AdobeOrg': 'MCMID|34319178866113281360379160534105373872',
        's_ppn': 'scv:us:en:home:dealer-locator',
        'gpv_pu': 'https://www.scania.com/us/en/home/dealer-locator.html',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'ConfidentialityAgreement={%22necessary%22:true%2C%22performance%22:true%2C%22functional%22:true%2C%22targeting%22:true%2C%22socialMedia%22:true}; kndctr_BCC792C056A0AB647F000101_AdobeOrg_cluster=ind1; kndctr_BCC792C056A0AB647F000101_AdobeOrg_consent=general=in; kndctr_BCC792C056A0AB647F000101_AdobeOrg_identity=CiYzNDMxOTE3ODg2NjExMzI4MTM2MDM3OTE2MDUzNDEwNTM3Mzg3MlIRCNTyteqiMhgBKgRJTkQxMAHwAdTyteqiMg==; AMCV_BCC792C056A0AB647F000101%40AdobeOrg=MCMID|34319178866113281360379160534105373872; s_ppn=scv:us:en:home:dealer-locator; gpv_pu=https://www.scania.com/us/en/home/dealer-locator.html',
        'Referer': 'https://www.scania.com/us/en/home/dealer-locator.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    def start_requests(self):
        yield scrapy.Request(method="GET",
                             url="https://www.scania.com/api/sis.json?type=DealerV2&country=US&currentPage=/content/www/us/en/home/dealer-locator",
                             headers=self.headers,
                             cookies=self.cookies,
                             callback=self.parse)
        

    def parse(self, response):
        print("Entered parse function")
        data = json.loads(response.text)
        item = {}
        for dealer in data["dealers"]:
            item["store_no"] = dealer["dealerId"]
            item["latitude"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["coordinates"]["latitude"]
            item["longitude"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["coordinates"][
                "longitude"]
            item["country"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["country"]["countryCode"]
            item["name"] = dealer["visitingAddress"]["addressee"]
            item["status"] = "Open" if dealer["activeDealer"] else "NA"
            item["city"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["city"]["value"]
            item["street"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["street"]["streetName"][
                "value"]
            item["zip"] = dealer["visitingAddress"]["postalAddress"]["physicalAddress"]["postalCode"]
            item["url"] = "https://www.scania.com/us/en/home/dealer-locator.html"
            item["phone_number"] = dealer["visitingAddress"]["fixedPhoneNumber"]["subscriberNumber"]
            item["county"] = "NA"
            item["open_hours"] = json.dumps(dealer["openingHours"]) if dealer["openingHours"] else "NA"
            item["direction_url"] = "NA"
            if item["street"] and item["zip_code"] and item["state"]:
                edited_street_address = '+'.join(item["street"].split())
                item[
                    "direction_url"] = f"https://www.google.com/maps/dir/Current+Location/{edited_street_address},+{item['state']},+{item['zip_code']},+{item['country']}/"


if __name__ == '__main__':
    execute(f"scrapy crawl {DataScaniaSpider.name}".split())
