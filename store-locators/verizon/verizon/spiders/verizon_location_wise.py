import json
from datetime import datetime
import pymysql

import verizon.DB_config as db
import scrapy
from scrapy.cmdline import execute

from verizon.items import VerizonPdp


class VerizonLocation(scrapy.Spider):
    name = 'location_verizon'
    allowed_domains = ["www.verizon.com"]
    cookies = {
        'GLOBALID': '0ba83f14z83daz47c7z91dbz7e56cd96c3e0',
        'kndctr_777B575E55828EBB7F000101_AdobeOrg_identity': 'CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D',
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
        's_vnc365': '1758186699673%26vn%3D6',
        's_ivc': 'true',
        's_inv': '68871',
        'taggingVisitStart': 'year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM',
        '_cs_mk_aa': '0.3571756274093303_1726650699719',
        'mboxEdgeCluster': '35',
        'kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster': 'or2',
        'soedc_sales': 'west',
        'SOE-XSRF-TOKEN-SALES': 'r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q',
        's_ig': 'x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208',
        'bioCustomerSessionId': 'POW-D-53f78a5a-856e-496d-9729-81b05531cef9',
        'digital_ig_session': 'POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5',
        '_tq_id.TV-5490810972-1.4dce': 'd60bef25d7191c79.1726568278.0.1726650705..',
        '_cls_s': 'a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1',
        'Q_id': 'QS1248181441457059c26aj3tq6k',
        'onesearch_pageViewUpdated': 'false',
        'randomNum': '3',
        'JSESSIONID': 'B251DC96730A4501ABC736AB3013DD5E',
        'query': 'Illinois',
        'pageNumber': '1',
        'fusion_query_id': 'myBCSftB',
        'channelId': 'VZW-DOTCOM',
        'gnavThrottleList': 'none',
        'soedc': 'west',
        'taggingPageCount': '3',
        'isLpFirstMessage': 'true',
        'lp_jwt_wireless': 'N',
        '__evo_vzw_session': '%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D',
        'LPSID-23979466': 'actTY4YISkCD5voN_6S7tA',
        'SESSION': '8eb018f7-1eb9-4cc4-b86e-4413a16a51d9',
        'NSC_xxx_tupsft_mcwt': 'ffffffff09f7172f45525d5f4f58455e445a4a4204c1',
        's_tslv': '1726650816437',
        'omni_prevPageName': 'details_illinois_forsyth_decatur%20il',
        's_nr30': '1726650816453-Repeat',
        'mbox': 'session%2322071644439846094800478135258996918273%2DtoaNAv%231726652678',
        '_cs_id': '61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.6.1726650817.1726650702.1722950785.1760732275718.1',
        '_tq_id.TV-7272187227-1.4dce': 'f6dc0bf065c03f66.1726574372.0.1726650818..',
        '_scid_r': '4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCeg',
        'uniqPageVisitDtl': '|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL',
        'uniqPageVisits': '3',
        '__ar_v4': '7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A12%7C3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A12',
        'uniqPageVisitDtl_q': '|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL',
        'uniqPageVisits_q': '3',
        'allPageVisitDtl_q': '|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL',
        'allPageVisits_q': '4',
        'POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst': '1726650818652',
        'invoca_session': '%7B%22ttl%22%3A%222024-10-18T09%3A13%3A41.812Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D',
        'cdlThrottleList': '|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726650823175',
        'vzwSandBox': 'BAU~1726650823175',
        'AWSALB': 'LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7',
        'AWSALBCORS': 'LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7',
        '_cs_s': '4.5.0.1726652648373',
        '_ga_12R1DX1LX7': 'GS1.1.1726650705.6.1.1726650860.8.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'GLOBALID=0ba83f14z83daz47c7z91dbz7e56cd96c3e0; kndctr_777B575E55828EBB7F000101_AdobeOrg_identity=CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D; AMCV_777B575E55828EBB7F000101%40AdobeOrg=MCMID|22071644439846094800478135258996918273; taggingUUID=39f3cfef-5266-4e86-9763-fb1d90214738; s_ecid=MCMID|22071644439846094800478135258996918273; _gcl_au=1.1.44941098.1726568275; _cs_c=1; lcvendor=liveperson; _scid=3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe; _cls_v=fa30b23b-4015-43c2-8edf-ff5a2890dea1; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; __adroll_fpc=69bc1f4d6faf5a713d7310a7769e603b-1726568278518; _ga=GA1.1.36865946.1726568279; _sctr=1%7C1726511400000; LPVID=llOGU4N2RjOGY1M2JiOGQ2; _fbp=fb.1.1726574353342.18860875510459388; AkaSTrackingID=995aafcb5a4bc41882418288bbb1a466; geoC=1; s_vnc365=1758186699673%26vn%3D6; s_ivc=true; s_inv=68871; taggingVisitStart=year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM; _cs_mk_aa=0.3571756274093303_1726650699719; mboxEdgeCluster=35; kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster=or2; soedc_sales=west; SOE-XSRF-TOKEN-SALES=r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q; s_ig=x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208; bioCustomerSessionId=POW-D-53f78a5a-856e-496d-9729-81b05531cef9; digital_ig_session=POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5; _tq_id.TV-5490810972-1.4dce=d60bef25d7191c79.1726568278.0.1726650705..; _cls_s=a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1; Q_id=QS1248181441457059c26aj3tq6k; onesearch_pageViewUpdated=false; randomNum=3; JSESSIONID=B251DC96730A4501ABC736AB3013DD5E; query=Illinois; pageNumber=1; fusion_query_id=myBCSftB; channelId=VZW-DOTCOM; gnavThrottleList=none; soedc=west; taggingPageCount=3; isLpFirstMessage=true; lp_jwt_wireless=N; __evo_vzw_session=%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D; LPSID-23979466=actTY4YISkCD5voN_6S7tA; SESSION=8eb018f7-1eb9-4cc4-b86e-4413a16a51d9; NSC_xxx_tupsft_mcwt=ffffffff09f7172f45525d5f4f58455e445a4a4204c1; s_tslv=1726650816437; omni_prevPageName=details_illinois_forsyth_decatur%20il; s_nr30=1726650816453-Repeat; mbox=session%2322071644439846094800478135258996918273%2DtoaNAv%231726652678; _cs_id=61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.6.1726650817.1726650702.1722950785.1760732275718.1; _tq_id.TV-7272187227-1.4dce=f6dc0bf065c03f66.1726574372.0.1726650818..; _scid_r=4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCeg; uniqPageVisitDtl=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits=3; __ar_v4=7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A12%7C3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A12; uniqPageVisitDtl_q=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits_q=3; allPageVisitDtl_q=|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL; allPageVisits_q=4; POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst=1726650818652; invoca_session=%7B%22ttl%22%3A%222024-10-18T09%3A13%3A41.812Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D; cdlThrottleList=|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726650823175; vzwSandBox=BAU~1726650823175; AWSALB=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; AWSALBCORS=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; _cs_s=4.5.0.1726652648373; _ga_12R1DX1LX7=GS1.1.1726650705.6.1.1726650860.8.0.0',
        'origin': 'https://www.verizon.com',
        'priority': 'u=1, i',
        'referer': 'https://www.verizon.com/onesearch/search?q=Illinois&lid=sayt&sayt=illinois*',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    con = pymysql.connect(user=db.USER,
                          host=db.HOST,
                          password=db.PASSWORD,
                          database=db.DATABASE)
    cur = con.cursor()


    def start_requests(self):
        self.cur.execute(f"SELECT * FROM {db.STATENAME} WHERE status='pending'")
        for row in self.cur.fetchall():
            state_name = row[1]
            lower_state_name = state_name.lower()
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'GLOBALID=0ba83f14z83daz47c7z91dbz7e56cd96c3e0; kndctr_777B575E55828EBB7F000101_AdobeOrg_identity=CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D; AMCV_777B575E55828EBB7F000101%40AdobeOrg=MCMID|22071644439846094800478135258996918273; taggingUUID=39f3cfef-5266-4e86-9763-fb1d90214738; s_ecid=MCMID|22071644439846094800478135258996918273; _gcl_au=1.1.44941098.1726568275; _cs_c=1; lcvendor=liveperson; _scid=3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe; _cls_v=fa30b23b-4015-43c2-8edf-ff5a2890dea1; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; __adroll_fpc=69bc1f4d6faf5a713d7310a7769e603b-1726568278518; _ga=GA1.1.36865946.1726568279; _sctr=1%7C1726511400000; LPVID=llOGU4N2RjOGY1M2JiOGQ2; _fbp=fb.1.1726574353342.18860875510459388; AkaSTrackingID=995aafcb5a4bc41882418288bbb1a466; geoC=1; s_vnc365=1758186699673%26vn%3D6; s_ivc=true; s_inv=68871; taggingVisitStart=year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM; _cs_mk_aa=0.3571756274093303_1726650699719; mboxEdgeCluster=35; kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster=or2; soedc_sales=west; SOE-XSRF-TOKEN-SALES=r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q; s_ig=x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208; bioCustomerSessionId=POW-D-53f78a5a-856e-496d-9729-81b05531cef9; digital_ig_session=POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5; _tq_id.TV-5490810972-1.4dce=d60bef25d7191c79.1726568278.0.1726650705..; _cls_s=a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1; Q_id=QS1248181441457059c26aj3tq6k; onesearch_pageViewUpdated=false; randomNum=3; JSESSIONID=B251DC96730A4501ABC736AB3013DD5E; query=Illinois; pageNumber=1; fusion_query_id=myBCSftB; channelId=VZW-DOTCOM; gnavThrottleList=none; soedc=west; taggingPageCount=3; isLpFirstMessage=true; lp_jwt_wireless=N; __evo_vzw_session=%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D; LPSID-23979466=actTY4YISkCD5voN_6S7tA; SESSION=8eb018f7-1eb9-4cc4-b86e-4413a16a51d9; NSC_xxx_tupsft_mcwt=ffffffff09f7172f45525d5f4f58455e445a4a4204c1; s_tslv=1726650816437; omni_prevPageName=details_illinois_forsyth_decatur%20il; s_nr30=1726650816453-Repeat; mbox=session%2322071644439846094800478135258996918273%2DtoaNAv%231726652678; _cs_id=61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.6.1726650817.1726650702.1722950785.1760732275718.1; _tq_id.TV-7272187227-1.4dce=f6dc0bf065c03f66.1726574372.0.1726650818..; _scid_r=4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCeg; uniqPageVisitDtl=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits=3; __ar_v4=7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A12%7C3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A12; uniqPageVisitDtl_q=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits_q=3; allPageVisitDtl_q=|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL; allPageVisits_q=4; POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst=1726650818652; invoca_session=%7B%22ttl%22%3A%222024-10-18T09%3A13%3A41.812Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D; cdlThrottleList=|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726650823175; vzwSandBox=BAU~1726650823175; AWSALB=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; AWSALBCORS=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; _cs_s=4.5.0.1726652648373; _ga_12R1DX1LX7=GS1.1.1726650705.6.1.1726650860.8.0.0',
                'origin': 'https://www.verizon.com',
                'priority': 'u=1, i',
                'referer': f'https://www.verizon.com/onesearch/search?q={state_name}&lid=sayt&sayt={lower_state_name}*',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }
            dump_data = json.dumps({
                'query': state_name,
                'refinements': [
                    {
                        'facet': '',
                        'labels': [],
                    },
                ],
                'sortOptions': {
                    'condition': 'best-match',
                },
                'pagination': {
                    'pageNumber': 1,
                    'recordsPerPage': 24,
                },
                'params': {
                    'q': state_name,
                    'lid': 'sayt',
                    'sayt': f'{lower_state_name}*',
                    'CITY': '',
                    'GLOBALID': '0ba83f14z83daz47c7z91dbz7e56cd96c3e0',
                    'JSESSIONID': 'lw v2',
                    'STATE': '',
                    'PLAY_SESSION': '',
                    'ZIPCODE': '',
                    'deviceType': '',
                    'encryptedUserName': '',
                    'myaccount': '',
                    'fnfRedemptionCode': '',
                    'ecpdcookie': '',
                    'role': '',
                    'greetingName': '',
                    'amID': '',
                    'loggedIn': '',
                    'HttpReferer': 'https://www.verizon.com/',
                    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                    'IPAddress': '',
                    'MobileBrand': 'none',
                    'MobileModel': 'none',
                    'OsName': 'Windows',
                    'source': None,
                    'userInfo': None,
                },
                'isMobile': False,
                'followup_ind': False,
                'turingthrottle': '',
            })
            yield scrapy.Request(method="POST",
                                 url='https://www.verizon.com/onesearch/results',
                                 body=dump_data,
                                 headers=headers,
                                 cookies=self.cookies,
                                 cb_kwargs={"page_no":1,
                                            "state_name":state_name,
                                            "lower_state_name":lower_state_name},
                                 callback=self.parse
                                 )
            # break

    def parse(self, response, **kwargs):
        page_no = kwargs["page_no"]
        state_name = kwargs["state_name"]
        lower_state_name = kwargs["lower_state_name"]
        data = json.loads(response.text)
        if data["results"]:
            item = VerizonPdp()
            for each_data in data["results"]:
                if each_data["recordContentType"] == "Stores":
                    item["store_no"] = each_data["recordId"].split("-")[-1].replace("/",'')
                    item["name"] = each_data["recordTitle"]
                    item["url"] = each_data["recordUrl"]

                    yield item

                    # next page request
                    page_no += 1
                    dump_data = json.dumps({
                        'query': state_name,
                        'refinements': [
                            {
                                'facet': '',
                                'labels': [],
                            },
                        ],
                        'sortOptions': {
                            'condition': 'best-match',
                        },
                        'pagination': {
                            'pageNumber': page_no,
                            'recordsPerPage': 24,
                        },
                        'params': {
                            'q': state_name,
                            'lid': 'sayt',
                            'sayt': f'{lower_state_name}*',
                            'CITY': '',
                            'GLOBALID': '0ba83f14z83daz47c7z91dbz7e56cd96c3e0',
                            'JSESSIONID': 'lw v2',
                            'STATE': '',
                            'PLAY_SESSION': '',
                            'ZIPCODE': '',
                            'deviceType': '',
                            'encryptedUserName': '',
                            'myaccount': '',
                            'fnfRedemptionCode': '',
                            'ecpdcookie': '',
                            'role': '',
                            'greetingName': '',
                            'amID': '',
                            'loggedIn': '',
                            'HttpReferer': 'https://www.verizon.com/',
                            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                            'IPAddress': '',
                            'MobileBrand': 'none',
                            'MobileModel': 'none',
                            'OsName': 'Windows',
                            'source': None,
                            'userInfo': None,
                        },
                        'isMobile': False,
                        'followup_ind': False,
                        'turingthrottle': '',
                    })
                    headers = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'application/json;charset=UTF-8',
                        # 'cookie': 'GLOBALID=0ba83f14z83daz47c7z91dbz7e56cd96c3e0; kndctr_777B575E55828EBB7F000101_AdobeOrg_identity=CiYyMjA3MTY0NDQzOTg0NjA5NDgwMDQ3ODEzNTI1ODk5NjkxODI3M1ISCOWc9PufMhABGAEqA09SMjAA8AHlnPT7nzI%3D; AMCV_777B575E55828EBB7F000101%40AdobeOrg=MCMID|22071644439846094800478135258996918273; taggingUUID=39f3cfef-5266-4e86-9763-fb1d90214738; s_ecid=MCMID|22071644439846094800478135258996918273; _gcl_au=1.1.44941098.1726568275; _cs_c=1; lcvendor=liveperson; _scid=3kOUTh20D8tQVC3WHoL1MdNYUMcZb3fe; _cls_v=fa30b23b-4015-43c2-8edf-ff5a2890dea1; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; __adroll_fpc=69bc1f4d6faf5a713d7310a7769e603b-1726568278518; _ga=GA1.1.36865946.1726568279; _sctr=1%7C1726511400000; LPVID=llOGU4N2RjOGY1M2JiOGQ2; _fbp=fb.1.1726574353342.18860875510459388; AkaSTrackingID=995aafcb5a4bc41882418288bbb1a466; geoC=1; s_vnc365=1758186699673%26vn%3D6; s_ivc=true; s_inv=68871; taggingVisitStart=year%3D2024%20%7C%20month%3DSeptember%20%7C%20date%3D18%20%7C%20day%3DWednesday%20%7C%20time%3D2%3A11%20AM; _cs_mk_aa=0.3571756274093303_1726650699719; mboxEdgeCluster=35; kndctr_777B575E55828EBB7F000101_AdobeOrg_cluster=or2; soedc_sales=west; SOE-XSRF-TOKEN-SALES=r/54waDcqtGRWFYGDZPJcbEt7wgdsQcqhCr0C9f9LVGq5GZ9RhZurPlui84vNXFsWFiPGKuDuAvitUvryPriwpzGzR/Wk6pDckkPD+2xt2ZrjHzswSV9+xQ9RH50Qn5Q; s_ig=x3lsPnI/twoQkhrVVDmV8yyspTt8KEaxjTfBWn5xsmYCokpErwe/ZYNLV1GD8ieF6kG3l/5Lb5E6i1aD7pCJopL7ywpIH5fBuhrM6H2D1qU=-ig2024-09-18 09:11:44.208; bioCustomerSessionId=POW-D-53f78a5a-856e-496d-9729-81b05531cef9; digital_ig_session=POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5; _tq_id.TV-5490810972-1.4dce=d60bef25d7191c79.1726568278.0.1726650705..; _cls_s=a6e235bf-3c4b-4f3d-9e89-fc0582e8ddaa:1; Q_id=QS1248181441457059c26aj3tq6k; onesearch_pageViewUpdated=false; randomNum=3; JSESSIONID=B251DC96730A4501ABC736AB3013DD5E; query=Illinois; pageNumber=1; fusion_query_id=myBCSftB; channelId=VZW-DOTCOM; gnavThrottleList=none; soedc=west; taggingPageCount=3; isLpFirstMessage=true; lp_jwt_wireless=N; __evo_vzw_session=%7B%22ip%22%3A%22b496df584439747573e24bd53296c882d9c7477b50f25%22%2C%22sid%22%3A%22htOjXzWMvgP65Yv9NCPHSf9FwP0j9CzW%22%7D; LPSID-23979466=actTY4YISkCD5voN_6S7tA; SESSION=8eb018f7-1eb9-4cc4-b86e-4413a16a51d9; NSC_xxx_tupsft_mcwt=ffffffff09f7172f45525d5f4f58455e445a4a4204c1; s_tslv=1726650816437; omni_prevPageName=details_illinois_forsyth_decatur%20il; s_nr30=1726650816453-Repeat; mbox=session%2322071644439846094800478135258996918273%2DtoaNAv%231726652678; _cs_id=61bc9127-1e05-a20f-c221-f7677ab72980.1726568275.6.1726650817.1726650702.1722950785.1760732275718.1; _tq_id.TV-7272187227-1.4dce=f6dc0bf065c03f66.1726574372.0.1726650818..; _scid_r=4cOUTh20D8tQVC3WHoL1MdNYUMcZb3fe2XoCeg; uniqPageVisitDtl=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits=3; __ar_v4=7QST7OEKE5B6HH4HSPWYDT%3A20240917%3A12%7C3N3S2ATGZBB5DNBSO4VX4R%3A20240917%3A12; uniqPageVisitDtl_q=|personal-home|searchresults|details_Illinois_Forsyth_Decatur IL; uniqPageVisits_q=3; allPageVisitDtl_q=|personal-home|searchresults|results|details_Illinois_Forsyth_Decatur IL; allPageVisits_q=4; POW-D-e3aa169c-f68f-4cd4-85c8-e5b1dd980fd5_tst=1726650818652; invoca_session=%7B%22ttl%22%3A%222024-10-18T09%3A13%3A41.812Z%22%2C%22session%22%3A%7B%22utm_medium%22%3A%22direct%22%2C%22utm_source%22%3A%22direct%22%2C%22invoca_id%22%3A%22i-cce402f2-9a30-4ffc-86d3-282f2993e22c%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22ba%22%3Atrue%7D%7D; cdlThrottleList=|VideoChatEnabled_PDP_NSE|vltmap_gw_nse|typeahead_here_gw_nse|z1_p_t_g|GW_LEFT_C_RAIL_P_D|CB_I_P|ABANDON_CART_GW|AGT_AVL_P|Digital_C_Concierge_P|NEW_C_FILTER|QUICK_VIEW_P|~1726650823175; vzwSandBox=BAU~1726650823175; AWSALB=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; AWSALBCORS=LNLKcaIOQQfAH7GUEOBSqL4hUo+HHErV9WExqzbHzVqarOSaITkg2HOfq7GMTBJA4Cr417GbYe2mSVjIRFhuWXfmYL88N/zViEjw2i+hIhuvE/kasNmUF0k3ovO7; _cs_s=4.5.0.1726652648373; _ga_12R1DX1LX7=GS1.1.1726650705.6.1.1726650860.8.0.0',
                        'origin': 'https://www.verizon.com',
                        'priority': 'u=1, i',
                        'referer': f'https://www.verizon.com/onesearch/search?q={state_name}&lid=sayt&sayt={lower_state_name}*',
                        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                    }
                    yield scrapy.Request(method="POST",
                                         url='https://www.verizon.com/onesearch/results',
                                         body=dump_data,
                                         headers=headers,
                                         cookies=self.cookies,
                                         cb_kwargs={"page_no": page_no,
                                                    "state_name": state_name,
                                                    "lower_state_name": lower_state_name},
                                         callback=self.parse
                                         )
                    print(page_no)

                else:

                    print("No stores found")
                    self.cur.execute(f"UPDATE {db.STATENAME} SET status='NA' WHERE states=%s", (state_name,))
                    self.con.commit()
                    print(f"Done scraping location {state_name}")
                    break

        else:
            print("No Data found")
            self.cur.execute(f"UPDATE {db.STATENAME} SET status='Done' WHERE states=%s", (state_name,))
            self.con.commit()
            print(f"Done scraping location {state_name}")


if __name__ == '__main__':
    execute(f"scrapy crawl {VerizonLocation.name}".split())