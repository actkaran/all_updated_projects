import requests
from parsel import Selector

cookies = {
    'zalb_be2cb13735': 'cdeb88315f53406807f7d2f632eae328',
    'csrfc': 'b48edce4-c262-4da2-84b9-eaaaf2a8d463',
    '_zcsr_tmp': 'b48edce4-c262-4da2-84b9-eaaaf2a8d463',
    'zsref': 'aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8=',
    'zabUserId': '1727354783578zabu0.48429157418933744',
    'zc_consent': '1',
    'zc_show': '0',
    '_clck': '1og53%7C2%7Cfpi%7C0%7C1730',
    '_gid': 'GA1.2.973791078.1727354786',
    'zscc676358f4dc9423cb0f361a3d0429d84': '1727354786450zsc0.2823721480717545',
    'zft-sdc': 'isef%3Dtrue-isfr%3Dtrue-source%3Dgoogle',
    'zpsfa_7742577ef0824e55a2e62154ff773406': '1727354786711psf0.379795942656147',
    'zc_cu': '3z1d3ae8c450f2eed0d69f8ff2c51d4a0e-v3z3b96e5b737ae672a5efc8abaf606d92669c4e8615170179a2c782c7d8b6f24cc',
    'automationwerksinc-_zldp': 'DmbSD8VWS5RSNuXch6RQBeEne0NWvjnS6NJqiUsVXHrgfMXOyJkfzDYjF8j8rtQvodoRkLyJC2Y%3D',
    'automationwerksinc-_zldt': '37b2dea2-a73a-4487-b051-6d3751eb09c7-0',
    'zabHMBucket': 'SZU2b2t',
    'zsrqouFuzc': '1727354792006zsrv0.0007325619535636374',
    'sales_c676358f4dc9423cb0f361a3d0429d84_1727354783578zabu0.48429157418933744': '%7B%22id%22%3A%2237b2dea2-a73a-4487-b051-6d3751eb09c7-0%22%7D',
    '_uetsid': '6eb12aa07c0511ef85128f26e9d6184a',
    '_uetvid': '6eb13bc07c0511ef8859b3c7bc42c5e7',
    'zsstssn': 'o6qsmhkd7cpeuftqclh75asig4ov7a1u21na8ujry6qz70e82',
    'zsltssn': '-wnopiw600msaqwruilkmmqeffe689tgc4yz3zf2maepo6lj84',
    'zc_tp': '3zb17671afc7e381aaf028e4b1bd988177f9eff324f87fa903e7b6d042d8fad035',
    '_gat_gtag_UA_252535601_1': '1',
    '_ga_L428BG6Q3L': 'GS1.1.1727354785.1.1.1727355619.0.0.0',
    '_ga': 'GA1.1.1500261689.1727354786',
    'zc_cu_exp': '1727382620000,1',
    '_clsk': '1unbfav%7C1727355620636%7C8%7C1%7Cx.clarity.ms%2Fcollect',
    'zps-tgr-dts': 'sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D9-sesst%3D1727354786451',
    'zsd1727354792006zsrv0.0007325619535636374': '1727354792006-15-1727355674224-intrinfosnt%3Dfalse-siqinfosnt%3Dtrue',
    'zsd1727354792006zsrv0.0007325619535636374': '1727354792006-15-1727355674224-intrinfosnt%3Dfalse-siqinfosnt%3Dtrue',
    'ps_payloadSeqId': '112',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'zalb_be2cb13735=cdeb88315f53406807f7d2f632eae328; csrfc=b48edce4-c262-4da2-84b9-eaaaf2a8d463; _zcsr_tmp=b48edce4-c262-4da2-84b9-eaaaf2a8d463; zsref=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8=; zabUserId=1727354783578zabu0.48429157418933744; zc_consent=1; zc_show=0; _clck=1og53%7C2%7Cfpi%7C0%7C1730; _gid=GA1.2.973791078.1727354786; zscc676358f4dc9423cb0f361a3d0429d84=1727354786450zsc0.2823721480717545; zft-sdc=isef%3Dtrue-isfr%3Dtrue-source%3Dgoogle; zpsfa_7742577ef0824e55a2e62154ff773406=1727354786711psf0.379795942656147; zc_cu=3z1d3ae8c450f2eed0d69f8ff2c51d4a0e-v3z3b96e5b737ae672a5efc8abaf606d92669c4e8615170179a2c782c7d8b6f24cc; automationwerksinc-_zldp=DmbSD8VWS5RSNuXch6RQBeEne0NWvjnS6NJqiUsVXHrgfMXOyJkfzDYjF8j8rtQvodoRkLyJC2Y%3D; automationwerksinc-_zldt=37b2dea2-a73a-4487-b051-6d3751eb09c7-0; zabHMBucket=SZU2b2t; zsrqouFuzc=1727354792006zsrv0.0007325619535636374; sales_c676358f4dc9423cb0f361a3d0429d84_1727354783578zabu0.48429157418933744=%7B%22id%22%3A%2237b2dea2-a73a-4487-b051-6d3751eb09c7-0%22%7D; _uetsid=6eb12aa07c0511ef85128f26e9d6184a; _uetvid=6eb13bc07c0511ef8859b3c7bc42c5e7; zsstssn=o6qsmhkd7cpeuftqclh75asig4ov7a1u21na8ujry6qz70e82; zsltssn=-wnopiw600msaqwruilkmmqeffe689tgc4yz3zf2maepo6lj84; zc_tp=3zb17671afc7e381aaf028e4b1bd988177f9eff324f87fa903e7b6d042d8fad035; _gat_gtag_UA_252535601_1=1; _ga_L428BG6Q3L=GS1.1.1727354785.1.1.1727355619.0.0.0; _ga=GA1.1.1500261689.1727354786; zc_cu_exp=1727382620000,1; _clsk=1unbfav%7C1727355620636%7C8%7C1%7Cx.clarity.ms%2Fcollect; zps-tgr-dts=sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D9-sesst%3D1727354786451; zsd1727354792006zsrv0.0007325619535636374=1727354792006-15-1727355674224-intrinfosnt%3Dfalse-siqinfosnt%3Dtrue; zsd1727354792006zsrv0.0007325619535636374=1727354792006-15-1727355674224-intrinfosnt%3Dfalse-siqinfosnt%3Dtrue; ps_payloadSeqId=112',
    # 'if-modified-since': 'Fri, 16 Aug 2024 13:38:23 GMT',
    'priority': 'u=0, i',
    'referer': 'https://www.automationwerks.com/',
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


def extract_dynamic_link(data):
    links = data.xpath("//figure[@class='zpimage-data-ref']/a[@class='zpimage-anchor']/@href").getall()
    for s in links:
        if ".pdf" in s or "javascript" in s:
            pass
        else:
            link = "https://www.automationwerks.com" + s
            print(link)


# response = requests.get('https://www.automationwerks.com/guided-actuators', cookies=cookies, headers=headers)
response = requests.get('https://www.automationwerks.com/Aluminum%20Framing/t-slot-extrusions', cookies=cookies, headers=headers)
data = Selector(text=response.text)
extract_dynamic_link(data)
