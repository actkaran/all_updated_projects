import gzip

import scrapy
import json
from datetime import datetime
import pymysql
from scrapy.cmdline import execute
import os
import verizon.DB_config as db
from verizon.items import VerizonItem


class VerizonData(scrapy.Spider):
    name = 'verizon_data_from_link'
    allowed_domains = ["www.verizon.com"]
    cookies = {
        'GLOBALID': '0ba83f14z83daz47c7z91dbz7e56cd96c3e0',
        'AMCV_777B575E55828EBB7F000101%40AdobeOrg': 'MCMID|22071644439846094800478135258996918273',
        'taggingUUID': '39f3cfef-5266-4e86-9763-fb1d90214738',
        's_ecid': 'MCMID|22071644439846094800478135258996918273',
        '_gcl_au': '1.1.44941098.1726568275',
        '_cs_c': '1',
        'lcvendor': 'liveperson',
        '_scid': '3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe',
        '_cls_v': 'fa30b23b-4015-43c2-8edf-ff5a2890dea1',
        '_pin_unauth': 'dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA',
        '_ScCbts': '%5B%5D',
        '__adroll_fpc': '69bc1f4d6faf5a713d7310a7769e603b-1726568278518',
        '_ga': 'GA1.1.36865946.1726568279',
        '_sctr': '1%7C1726511400000',
        'LPVID': 'llOGU4N2RjOGY1M2JiOGQ2',
        '_fbp': 'fb.1.1726574353342.18860875510459388',
        'AkaSTrackingID': '995aafcb5a4bc41882418288bbb1a466',
        'geoC': '1',
        'taggingVisitStart': 'year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM',
        'soedc_sales': 'west',
        'SOE-XSRF-TOKEN-SALES': 'r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q',
        's_ig': 'x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208',
        'bioCustomerSessionId': 'POW-D-53f78a5a-856e-496d-9729-81b05531cef9',
        'digital_ig_session': 'POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5',
        '_cls_s': 'a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1',
        'onesearch_pageViewUpdated': 'false',
        'randomNum': '3',
        'channelId': 'VZW-DOTCOM',
        'gnavThrottleList': 'none',
        'soedc': 'west',
        'isLpFirstMessage': 'true',
        'lp_jwt_wireless': 'N',
        '__evo_vzw_session': '%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D',
        'SESSION': '8eb018f7-1eb9-4cc4-b86e-4413a16a51d9',
        'NSC_xxx_tupsft_mcwt': 'ffffffff09f7172f45525d5f4f58455e445a4a4204c1',
        'POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst': '1726650818652',
        'pageNumber': '1',
        'kndctr_777B575E55828EBB7F000101_AdobeOrg_identity': 'CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AGIraCooDI%3D',
        'kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster': 'or2',
        's_vnc365': '1758197271542%26vn%3D7',
        's_ivc': 'true',
        's_inv': '9535',
        'mboxEdgeCluster': '35',
        'LPSID-23979466': 'FZOLVeLtTtONH94k31dADw',
        '_tq_id.TV-7272187227-1.4dce': 'f6dc0bf065c03f66.1726574372.0.1726662087..',
        'JSESSIONID': '6217883680DEFD01B843C95A6AE8905F',
        'query': 'Iowa',
        'fusion_query_id': 'rf9sgTEL',
        'taggingPageCount': '12',
        'omni_prevPageName': 'details_iowa_iowa%20city_victra%20iowa%20city',
        'uniqPageVisitDtl': '|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|details_Iowa_Iowa City_Victra Iowa City',
        'uniqPageVisits': '6',
        'uniqPageVisitDtl_q': '|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|details_Iowa_Iowa City_Victra Iowa City',
        'uniqPageVisits_q': '6',
        'Q_id': 'QS124818182410737nbjrm38ch6',
        '_tq_id.TV-5490810972-1.4dce': 'd60bef25d7191c79.1726568278.0.1726664436..',
        's_tslv': '1726664496203',
        's_nr30': '1726664496210-Repeat',
        '_cs_id': '61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.7.1726664497.1726661272.1722950785.1760732275718.1',
        '_cs_s': '12.5.0.1726666297578',
        'mbox': 'session%2322071644439846094800478135258996918273%2DtoaNAv%231726666358',
        'AWSALB': 'BzSWH3DBZTB3Te5j70pxi7anp7cK295qXbgouSF9lKiCtBQbYXqpf6G9JxZkC4E5xMIwH7tdd/EilbY7oo2ClTyD4lUzUkQxH2paI4bj5uDFp7QdVxmdZwR34osJ',
        'AWSALBCORS': 'BzSWH3DBZTB3Te5j70pxi7anp7cK295qXbgouSF9lKiCtBQbYXqpf6G9JxZkC4E5xMIwH7tdd/EilbY7oo2ClTyD4lUzUkQxH2paI4bj5uDFp7QdVxmdZwR34osJ',
        'cdlThrottleList': '|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726664497875',
        'vzwSandBox': 'BAU~1726664497875',
        '_scid_r': '4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCiQ',
        '_ga_12R1DX1LX7': 'GS1.1.1726661276.7.1.1726664501.46.0.0',
        '__ar_v4': '3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A27%7C7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A27',
        'allPageVisitDtl_q': '|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL|results|results|personal-home|results|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|personal-home|verizon-protect_alabama|results|results|details_Iowa_Iowa City_Victra Iowa City|details_Iowa_Iowa City_Victra Iowa City|details_Iowa_Iowa City_Victra Iowa City',
        'allPageVisits_q': '19',
        'invoca_session': '%7B%22ttl%22%3A%222024-10-18T13%3A01%3A44.722Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'GLOBALID=0ba83f14z83daz47c7z91dbz7e56cd96c3e0; AMCV_777B575E55828EBB7F000101%40AdobeOrg=MCMID|22071644439846094800478135258996918273; taggingUUID=39f3cfef-5266-4e86-9763-fb1d90214738; s_ecid=MCMID|22071644439846094800478135258996918273; _gcl_au=1.1.44941098.1726568275; _cs_c=1; lcvendor=liveperson; _scid=3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe; _cls_v=fa30b23b-4015-43c2-8edf-ff5a2890dea1; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; __adroll_fpc=69bc1f4d6faf5a713d7310a7769e603b-1726568278518; _ga=GA1.1.36865946.1726568279; _sctr=1%7C1726511400000; LPVID=llOGU4N2RjOGY1M2JiOGQ2; _fbp=fb.1.1726574353342.18860875510459388; AkaSTrackingID=995aafcb5a4bc41882418288bbb1a466; geoC=1; taggingVisitStart=year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM; soedc_sales=west; SOE-XSRF-TOKEN-SALES=r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q; s_ig=x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208; bioCustomerSessionId=POW-D-53f78a5a-856e-496d-9729-81b05531cef9; digital_ig_session=POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5; _cls_s=a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1; onesearch_pageViewUpdated=false; randomNum=3; channelId=VZW-DOTCOM; gnavThrottleList=none; soedc=west; isLpFirstMessage=true; lp_jwt_wireless=N; __evo_vzw_session=%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D; SESSION=8eb018f7-1eb9-4cc4-b86e-4413a16a51d9; NSC_xxx_tupsft_mcwt=ffffffff09f7172f45525d5f4f58455e445a4a4204c1; POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst=1726650818652; pageNumber=1; kndctr_777B575E55828EBB7F000101_AdobeOrg_identity=CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AGIraCooDI%3D; kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster=or2; s_vnc365=1758197271542%26vn%3D7; s_ivc=true; s_inv=9535; mboxEdgeCluster=35; LPSID-23979466=FZOLVeLtTtONH94k31dADw; _tq_id.TV-7272187227-1.4dce=f6dc0bf065c03f66.1726574372.0.1726662087..; JSESSIONID=6217883680DEFD01B843C95A6AE8905F; query=Iowa; fusion_query_id=rf9sgTEL; taggingPageCount=12; omni_prevPageName=details_iowa_iowa%20city_victra%20iowa%20city; uniqPageVisitDtl=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|details_Iowa_Iowa City_Victra Iowa City; uniqPageVisits=6; uniqPageVisitDtl_q=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|details_Iowa_Iowa City_Victra Iowa City; uniqPageVisits_q=6; Q_id=QS124818182410737nbjrm38ch6; _tq_id.TV-5490810972-1.4dce=d60bef25d7191c79.1726568278.0.1726664436..; s_tslv=1726664496203; s_nr30=1726664496210-Repeat; _cs_id=61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.7.1726664497.1726661272.1722950785.1760732275718.1; _cs_s=12.5.0.1726666297578; mbox=session%2322071644439846094800478135258996918273%2DtoaNAv%231726666358; AWSALB=BzSWH3DBZTB3Te5j70pxi7anp7cK295qXbgouSF9lKiCtBQbYXqpf6G9JxZkC4E5xMIwH7tdd/EilbY7oo2ClTyD4lUzUkQxH2paI4bj5uDFp7QdVxmdZwR34osJ; AWSALBCORS=BzSWH3DBZTB3Te5j70pxi7anp7cK295qXbgouSF9lKiCtBQbYXqpf6G9JxZkC4E5xMIwH7tdd/EilbY7oo2ClTyD4lUzUkQxH2paI4bj5uDFp7QdVxmdZwR34osJ; cdlThrottleList=|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726664497875; vzwSandBox=BAU~1726664497875; _scid_r=4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCiQ; _ga_12R1DX1LX7=GS1.1.1726661276.7.1.1726664501.46.0.0; __ar_v4=3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A27%7C7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A27; allPageVisitDtl_q=|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL|results|results|personal-home|results|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|details_Idaho_IDAHO FALLS_Victra Idaho Falls Houston Cir|verizon-protect_alabama|personal-home|verizon-protect_alabama|results|results|details_Iowa_Iowa City_Victra Iowa City|details_Iowa_Iowa City_Victra Iowa City|details_Iowa_Iowa City_Victra Iowa City; allPageVisits_q=19; invoca_session=%7B%22ttl%22%3A%222024-10-18T13%3A01%3A44.722Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    con = pymysql.connect(user=db.USER,
                          host=db.HOST,
                          password=db.PASSWORD,
                          database=db.DATABASE)
    cur = con.cursor()

    def convert_24h(self, time_string):
        # making list for storing classified time and day name
        temp_time = []
        for day in time_string:
            if "null null" in day:
                continue
            elif "Closed Closed" in day or "CLOSED CLOSED" in day:
                day_name = day.split("-")[0].strip()
                day_time = day.split("-")[-1].strip()
                temp_time.append(f"{day_name.strip()} :- {day_time}")
            elif "Closed " in day:
                day_name = day.split("-")[0].strip()
                day_time = day.split("Closed")[-1].strip()
                if "PM" in day_time:
                    if "12:00" in day_time:
                        temp_time.append(f"{day_name.strip()} :- Closed 12:00")
                    else:
                        day_time_pm = "{:.2f}".format(float(day_time.replace("PM", "").replace(':', '.')) + 12.00)
                        temp_time.append(f"{day_name.strip()} :- Closed {day_time_pm.replace('.', ':').strip()}")
                else:
                    # am calculation
                    if "12:00 AM" in day_time:
                        temp_time.append(f"{day_name.strip()} :- Closed 00:00")
                    else:
                        day_time_am = "{:.2f}".format(
                            float(day_time.replace("AM", "").strip().replace(':', '.')) + 12.00)
                        temp_time.append(
                            f"{day_name.strip()} :- Closed {day_time_am.replace('.', ':').strip()}")
            elif day.count('PM') != 2:
                day_name = day.split("-")[0].strip()
                day_time = day.split('-')[-1].strip()
                day_time_am = day_time.split('AM')[0].strip()
                day_time_pm = "{:.2f}".format(
                    float(day_time.split('AM')[-1].split('PM')[0].strip().replace(':', '.')) + 12.00)
                temp_time.append(f"{day_name.strip()} :- {day_time_am} - {day_time_pm.replace('.', ':').strip()}")
            else:
                day_name = day.split("-")[0].strip()
                day_time = day.split('-')[-1].strip()
                if "12:00 PM" in day_time:
                    pm2 = "{:.2f}".format(
                        float(day_time.replace("PM", '').strip().split()[-1].replace(':', '.')) + 12.00)
                    temp_time.append(f"{day_name.strip()} :- 12:00 - {pm2.replace('.', ':').strip()}")
                else:
                    pm1 = "{:.2f}".format(
                        float(day_time.replace("PM", '').strip().split()[0].replace(':', '.')) + 12.00)
                    pm2 = "{:.2f}".format(
                        float(day_time.replace("PM", '').strip().split()[-1].replace(':', '.')) + 12.00)
                    temp_time.append(
                        f"{day_name.strip()} :- {pm1.replace('.', ':').strip()} - {pm2.replace('.', ':').strip()}")
        if len(temp_time) == 0: return "NA"
        return ' | '.join(temp_time)

    def start_requests(self):
        self.cur.execute(f"SELECT * FROM {db.LINKDATA} WHERE status='pending'")
        for x in self.cur.fetchall():
            url = x[2]
            name = x[1]
            store_no = x[0]
            file_location = fr"C:\Users\DELL\Desktop\KARAN\verizon\verizon\PAGESAVE\{store_no}.html.gz"
            # checking if page-save is available or not
            if os.path.exists(file_location):
                yield scrapy.Request(
                    url="file:///C:/Users/DELL/AppData/Local/Temp/Rar$EXa10048.26417.rartemp/200862.html")
            else:
                # if page-save not found then send fresh request
                yield scrapy.Request(url=url,
                                     headers=self.headers,
                                     cookies=self.cookies,
                                     callback=self.parse,
                                     dont_filter=True,
                                     cb_kwargs={"url": url,
                                                "store_no": store_no})
            # break

    def parse(self, response, **kwargs):
        url = kwargs["url"]
        store_no = kwargs["store_no"]
        data = response.text.split("var storeJSON = ")[-1].split("var storeDetailsJSON = ")[0].replace(";", '').strip()
        try:
            # loading data after spiliting the response.text
            jd = json.loads(data)

            # PAGE-SAVE CODE-----------
            file_location = r"C:\Users\DELL\Desktop\KARAN\verizon\verizon\PAGESAVE"
            file_name = f"{store_no}.html.gz"
            final_path = os.path.join(file_location, file_name)
            with gzip.open(final_path, "wb") as f:
                f.write(response.text.encode('utf-8'))
            # PAGE-SAVE CODE END-----

            item = VerizonItem()
            item["store_no"] = jd["storeNumber"]
            item["name"] = jd["storeName"]
            item["longitude"] = jd["geo"]["longitude"]
            item["latitude"] = jd["geo"]["latitude"]
            try:
                item["street"] = jd["posStoreDetail"]["address1"] if jd["posStoreDetail"]["address1"] else "NA"
            except:
                item["street"] = jd["address"]["streetAddress"] if jd["address"]["streetAddress"] else "NA"
            item["city"] = jd["city"]
            item["state"] = jd["stateAbbr"]
            item["zip_code"] = jd["zip"]
            item["county"] = "NA"
            item["country"] = "USA"
            item["open_hours"] = self.convert_24h(
                jd["openingHoursSpecification"]["dayOfWeek"]) if "openingHoursSpecification" in jd else "NA"
            item["phone_number"] = jd["telephone"] if jd["telephone"] else "NA"
            item["status"] = jd["storeStatus"]
            item["url"] = url
            item["provider"] = "Verizon"
            item["category"] = "Computer And Electronics Stores"
            item["updated_date"] = str(datetime.now().strftime("%d-%m-%Y"))
            item["direction_url"] = "NA"
            if item["street"] and item["zip_code"] and item["state"]:
                edited_street_address = '+'.join(item["street"].split())
                item[
                    "direction_url"] = f"https://www.google.com/maps/dir/Current+Location/{edited_street_address},+{item['state']},+{item['zip_code']},+{item['country']}/"
            yield item
            self.cur.execute(f"UPDATE {db.LINKDATA} SET status='Done'  WHERE store_no=%s", (store_no,))
            self.con.commit()
            print(f"Done scraping store: {item['name']}")
        except json.decoder.JSONDecodeError:
            self.cur.execute(f"UPDATE {db.LINKDATA} SET status='NA'  WHERE store_no=%s", (store_no,))
            self.con.commit()
            print(f"No store data")
        except Exception as e:
            print(e)
            self.cur.execute(f"UPDATE {db.LINKDATA} SET status='pending'  WHERE store_no=%s", (store_no,))
            self.con.commit()
            print(f"pending scraping")


if __name__ == "__main__":
    execute(f"scrapy crawl {VerizonData.name}".split())
