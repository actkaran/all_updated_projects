# from datetime import datetime
#
# import scrapy
# import json
#
# from scrapy.cmdline import execute
#
# from verizon.items import VerizonItem
#
#
# class VerizonStoreSpider(scrapy.Spider):
#     name = "verizon_store"
#     allowed_domains = ["www.verizon.com"]
#     start_urls = ["https://www.verizon.com"]
#
#     cookies = {
#         'AkaSTrackingID': 'ae0ddfa1a439008c8d96ad85321aca07',
#         'NSC_xxx_tupsft_mcwt': 'ffffffff09f7172b45525d5f4f58455e445a4a4204c2',
#         'GLOBALID': '0ba83f14z83daz47c7z91dbz7e56cd96c3e0',
#         'kndctr_777B575E55828EBB7F000101_AdobeOrg_identity': 'CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D',
#         'AMCV_777B575E55828EBB7F000101%40AdobeOrg': 'MCMID|22071644439846094800478135258996918273',
#         'taggingUUID': '39f3cfef-5266-4e86-9763-fb1d90214738',
#         's_ecid': 'MCMID|22071644439846094800478135258996918273',
#         'GeoCountry': 'in',
#         'geoC': '1',
#         '_gcl_au': '1.1.44941098.1726568275',
#         'taggingVisitStart': 'year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D17%20%7C%20day%3DTuesday%20%7C%20time%3D3%3A17%20AM',
#         '_cs_c': '1',
#         'soedc_sales': 'west',
#         'SOE-XSRF-TOKEN-SALES': 'vgMCjqAPiYyqJkQsyVB6XYwfyQX8kTx2enR6n/q+Z9r5Fo6GY5Ca0LUNxNRQ/davIOqzBM6a/hF72zaaFHwwhyVUvMVV45aiodm10m3unBFlQa8MirnspI8wiaNxxKQC',
#         's_ig': 'x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieFfNlVPCUqBLnAic0MiSXA2oSC7xYPhR9m+rn4b8AvQX4=-ig2024-09-17 10:17:56.298',
#         'bioCustomerSessionId': 'POW-D-f53bef79-21bc-4b11-a0f9-70b16bdacfa1',
#         'digital_ig_session': 'POW-D-d0371b30-0735-464f-95c5-8ea0d968cf56',
#         'lcvendor': 'liveperson',
#         '_scid': '3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe',
#         '_tq_id.TV-5490810972-1.4dce': 'd60bef25d7191c79.1726568278.0.1726568278..',
#         'isLpFirstMessage': 'true',
#         'lp_jwt_wireless': 'N',
#         '_cls_v': 'fa30b23b-4015-43c2-8edf-ff5a2890dea1',
#         '_cls_s': '33a5ae41-f613-4c46-8a42-45f5f4dfeb4e:0',
#         '_pin_unauth': 'dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA',
#         '_ScCbts': '%5B%5D',
#         '__adroll_fpc': '69bc1f4d6faf5a713d7310a7769e603b-1726568278518',
#         '_ga': 'GA1.1.36865946.1726568279',
#         '_sctr': '1%7C1726511400000',
#         'POW-D-d0371b30-0735-464f-95c5-8ea0d968cf56_tst': '1726568278151',
#         'cdlThrottleList': '|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726568278178',
#         'vzwSandBox': 'BAU~1726568278178',
#         'LPVID': 'llOGU4N2RjOGY1M2JiOGQ2',
#         's_vnc365': '1758110352384%26vn%3D2',
#         's_ivc': 'true',
#         's_inv': '6077',
#         '_cs_mk_aa': '0.10733992652900093_1726574352395',
#         'mboxEdgeCluster': '35',
#         'kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster': 'or2',
#         '_fbp': 'fb.1.1726574353342.18860875510459388',
#         'Q_id': 'QS124817172915506wwhavjlxxd',
#         'LPSID-23979466': 'vd8-nznsT3G4v7UZfYx42w',
#         'channelId': 'VZW-DOTCOM',
#         'gnavThrottleList': 'none',
#         'soedc': 'west',
#         's_tslv': '1726574369339',
#         'omni_prevPageName': 'searchresults',
#         's_nr30': '1726574369346-Repeat',
#         'taggingPageCount': '2',
#         'mbox': 'session%2322071644439846094800478135258996918273%2DtoaNAv%231726576230',
#         '_cs_id': '61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.3.1726574370.1726574337.1722950785.1760732275718.1',
#         '_tq_id.TV-7272187227-1.4dce': 'f6dc0bf065c03f66.1726574372.0.1726574372..',
#         '_scid_r': '2MOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCcQ',
#         '__ar_v4': '3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A3%7C7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A3',
#         'uniqPageVisitDtl': '|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults',
#         'uniqPageVisits': '3',
#         'uniqPageVisitDtl_q': '|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults',
#         'uniqPageVisits_q': '3',
#         'allPageVisitDtl_q': '|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults',
#         'allPageVisits_q': '3',
#         'invoca_session': '%7B%22ttl%22%3A%222024-10-17T11%3A59%3A39.635Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%7D%7D',
#         'AWSALB': 'vjzcuz+QdIdzIbUL2WBHmltCaSYklZn1RS+jtHrkqMQpPsPv2xeTE9/N+fKIdbvMWSSQVh3UglDJA7usqtuwmcJsnCyEU+BrIsdZs1yiM51apKO8ybK0Fa4Zw3+K',
#         'AWSALBCORS': 'vjzcuz+QdIdzIbUL2WBHmltCaSYklZn1RS+jtHrkqMQpPsPv2xeTE9/N+fKIdbvMWSSQVh3UglDJA7usqtuwmcJsnCyEU+BrIsdZs1yiM51apKO8ybK0Fa4Zw3+K',
#         '_cs_s': '3.5.0.1726576414798',
#         '_ga_12R1DX1LX7': 'GS1.1.1726574350.2.1.1726574623.60.0.0',
#     }
#
#     headers = {
#         'accept': 'application/json',
#         'accept-language': 'en-US,en;q=0.9',
#         'channelid': 'VZW-DOTCOM',
#         'content-type': 'application/json',
#         # 'cookie': 'AkaSTrackingID=ae0ddfa1a439008c8d96ad85321aca07; NSC_xxx_tupsft_mcwt=ffffffff09f7172b45525d5f4f58455e445a4a4204c2; GLOBALID=0ba83f14z83daz47c7z91dbz7e56cd96c3e0; kndctr_777B575E55828EBB7F000101_AdobeOrg_identity=CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D; AMCV_777B575E55828EBB7F000101%40AdobeOrg=MCMID|22071644439846094800478135258996918273; taggingUUID=39f3cfef-5266-4e86-9763-fb1d90214738; s_ecid=MCMID|22071644439846094800478135258996918273; GeoCountry=in; geoC=1; _gcl_au=1.1.44941098.1726568275; taggingVisitStart=year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D17%20%7C%20day%3DTuesday%20%7C%20time%3D3%3A17%20AM; _cs_c=1; soedc_sales=west; SOE-XSRF-TOKEN-SALES=vgMCjqAPiYyqJkQsyVB6XYwfyQX8kTx2enR6n/q+Z9r5Fo6GY5Ca0LUNxNRQ/davIOqzBM6a/hF72zaaFHwwhyVUvMVV45aiodm10m3unBFlQa8MirnspI8wiaNxxKQC; s_ig=x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieFfNlVPCUqBLnAic0MiSXA2oSC7xYPhR9m+rn4b8AvQX4=-ig2024-09-17 10:17:56.298; bioCustomerSessionId=POW-D-f53bef79-21bc-4b11-a0f9-70b16bdacfa1; digital_ig_session=POW-D-d0371b30-0735-464f-95c5-8ea0d968cf56; lcvendor=liveperson; _scid=3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe; _tq_id.TV-5490810972-1.4dce=d60bef25d7191c79.1726568278.0.1726568278..; isLpFirstMessage=true; lp_jwt_wireless=N; _cls_v=fa30b23b-4015-43c2-8edf-ff5a2890dea1; _cls_s=33a5ae41-f613-4c46-8a42-45f5f4dfeb4e:0; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; __adroll_fpc=69bc1f4d6faf5a713d7310a7769e603b-1726568278518; _ga=GA1.1.36865946.1726568279; _sctr=1%7C1726511400000; POW-D-d0371b30-0735-464f-95c5-8ea0d968cf56_tst=1726568278151; cdlThrottleList=|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726568278178; vzwSandBox=BAU~1726568278178; LPVID=llOGU4N2RjOGY1M2JiOGQ2; s_vnc365=1758110352384%26vn%3D2; s_ivc=true; s_inv=6077; _cs_mk_aa=0.10733992652900093_1726574352395; mboxEdgeCluster=35; kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster=or2; _fbp=fb.1.1726574353342.18860875510459388; Q_id=QS124817172915506wwhavjlxxd; LPSID-23979466=vd8-nznsT3G4v7UZfYx42w; channelId=VZW-DOTCOM; gnavThrottleList=none; soedc=west; s_tslv=1726574369339; omni_prevPageName=searchresults; s_nr30=1726574369346-Repeat; taggingPageCount=2; mbox=session%2322071644439846094800478135258996918273%2DtoaNAv%231726576230; _cs_id=61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.3.1726574370.1726574337.1722950785.1760732275718.1; _tq_id.TV-7272187227-1.4dce=f6dc0bf065c03f66.1726574372.0.1726574372..; _scid_r=2MOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCcQ; __ar_v4=3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A3%7C7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A3; uniqPageVisitDtl=|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults; uniqPageVisits=3; uniqPageVisitDtl_q=|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults; uniqPageVisits_q=3; allPageVisitDtl_q=|details_Indiana_Fort Wayne_Fort Wayne|storelocator|searchresults; allPageVisits_q=3; invoca_session=%7B%22ttl%22%3A%222024-10-17T11%3A59%3A39.635Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%7D%7D; AWSALB=vjzcuz+QdIdzIbUL2WBHmltCaSYklZn1RS+jtHrkqMQpPsPv2xeTE9/N+fKIdbvMWSSQVh3UglDJA7usqtuwmcJsnCyEU+BrIsdZs1yiM51apKO8ybK0Fa4Zw3+K; AWSALBCORS=vjzcuz+QdIdzIbUL2WBHmltCaSYklZn1RS+jtHrkqMQpPsPv2xeTE9/N+fKIdbvMWSSQVh3UglDJA7usqtuwmcJsnCyEU+BrIsdZs1yiM51apKO8ybK0Fa4Zw3+K; _cs_s=3.5.0.1726576414798; _ga_12R1DX1LX7=GS1.1.1726574350.2.1.1726574623.60.0.0',
#         'flowname': 'null',
#         'from-referrer': 'https://www.verizon.com/stores/',
#         'fromreferrer': 'https://www.verizon.com/stores/',
#         'origin': 'https://www.verizon.com',
#         'pagename': 'NA',
#         'priority': 'u=1, i',
#         'referer': 'https://www.verizon.com/sales/stores/searchresults.html?lat=39.76691&lng=-86.15012&zip=46204&sourceType=MVO',
#         'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#         'visitorid': '22071644439846094800478135258996918273',
#     }
#
#     def start_requests(self):
#         json_data = json.dumps({
#                 'locationCodes': [],
#                 'longitude': '-86.15012',
#                 'latitude': '39.76691',
#                 'filterPromoStores': False,
#                 'range': 20,
#                 'noOfStores': 25,
#                 'excludeIndirect': False,
#                 'retrieveBy': 'GEO',
#         })
#         yield scrapy.Request(method="POST", url="https://www.verizon.com/digital/nsa/nos/gw/retail/searchresultsdata",
#                              body=json_data,
#                              headers=self.headers,
#                              cookies=self.cookies,
#                              callback=self.parse)
#
#
#     def parse(self, response):
#         data = json.loads(response.text)
#         item = VerizonItem()
#         if data["body"]["data"]["stores"]:
#             for each_dic in data["body"]["data"]["stores"]:
#                 item["store_no"] = each_dic["storeNumber"]
#                 item["name"] = each_dic["storeName"]
#                 item["longitude"] = each_dic["location"]["longitude"]
#                 item["latitude"] = each_dic["location"]["latitude"]
#                 item["street"] = each_dic["address1"]
#                 item["city"] = each_dic["city"]
#                 item["state"] = each_dic["state"]
#                 item["zip_code"] = each_dic["zipCode"]
#                 item["county"] = "NA"
#                 item["country"] = "USA"
#                 item["open_hours"] = f"""sunday :- {each_dic["hoursSun"]} | monday :- {each_dic["hoursMon"]} | tuesday :- {each_dic["hoursTue"]} | wednesday :- {each_dic["hoursWed"]} | saturday :- {each_dic["hoursSat"]} | thursday :- {each_dic["hoursThu"]} | friday :- {each_dic["hoursFri"]}"""
#                 item["phone_number"] = each_dic["phoneNumber"]
#                 item["status"] = each_dic["storeStatus"]
#                 item["url"] = "https://www.verizon.com" + each_dic["storeUrl"]
#                 item["provider"] = "Verizon"
#                 item["category"] = "Computer And Electronics Stores"
#                 item["updated_date"] = str(datetime.now().strftime("%d-%m-%Y"))
#                 sp_ad = '+'.join(each_dic["address1"].split())
#                 item["direction_url"] = f"https://www.google.com/maps/dir/Current+Location/{sp_ad},+{each_dic['state']},+{each_dic['zipCode']},+USA/"
#                 yield item
#
# if __name__ == "__main__":
#     execute("scrapy crawl verizon_store".split())