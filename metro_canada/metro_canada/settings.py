# Scrapy settings for metro_canada project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "metro_canada"

SPIDER_MODULES = ["metro_canada.spiders"]
NEWSPIDER_MODULE = "metro_canada.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "metro_canada (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'METRO_ANONYMOUS_COOKIE=3a2b998b-6e52-435d-98c0-1d030a95eee8; CRITEO_RETAILER_VISITOR_COOKIE=ac9bab2d-7aec-4721-b0f9-10ff1c69b3c4; coveo_visitorId=c3f5f51e-95ca-4d80-93eb-979d35c2c1ae; hprl=en; _ga=GA1.1.1093776326.1730877757; coveo_visitorId=c3f5f51e-95ca-4d80-93eb-979d35c2c1ae; _gcl_au=1.1.1099375172.1730877757; OptanonAlertBoxClosed=2024-11-06T07:22:39.944Z; _fbp=fb.1.1730877760680.653511761591064627; _clck=1i16p2g%7C2%7Cfqn%7C0%7C1771; _clsk=obd35h%7C1730889110404%7C1%7C1%7Co.clarity.ms%2Fcollect; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=4afda3daa753ae5dd78f74cca9802458f780e0bd1ca2e6eb4a0239e732902253c456cfb5; __cf_bm=mSb54gbOpAFAQ_NSwKvgtcYPbxrTuveQd2kKgPfFKhA-1730907926-1.0.1.1-3fSw5co18FCaOeeSbtAviVZzBqS34LGoIQQjJ3IhZPBn0BzWcnv7P1OxthYCB9U_uB7wZZWOi2LFNsXiMrgs709LJBxp0r4boRyTv5B4D2g; SameSite=None; JSESSIONID=16A3D6E88F6D9EFFD6A2C5DD7A120545; APP_D_USER_ID=yzPmkToh-2166830715; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+21%3A41%3A47+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; cf_clearance=gFaryeKoOreXXg.sOLemo9wpIFinlcFkn_IOvI4GhEE-1730909508-1.2.1.1-O3m8SZ.EH.4oPySqWhpuc8ejP1UDC3I3uoInkLGCa3Z4Yrewy2UB5lm.a7aGtqhIYVPRbir7JqBfxHoJZejyLABxXkM9a6i87XONmQJIQIKJPA1A3.N3SLi1p439qPtbVbVcVwqOp1pQEUovneuD4t90w1LUGIPB7C7QHMgEnMNvXxGAW3Q0AtIS3dJ98oVS3y9tSPE9vKph_TWdooi1vOGiOksp3Bf4uhU7lJ8AgP5Qv2GcHBMieaL3nunWGYNfPppKWtEnPeCwXDvpuwKokfVC8q9by4GYdezyB7PUcV9rRI0_a6qgI9rGklHe6xMn1DJc5QmdLYESOeuzn_v1qXIkh7V8g_2o4K_zHh4BKZPLiMNeUm656mJ6oydwj4G.RM36r2Kh4TbCAfFmGbuY.A; _conv_v=vi%3A1*sc%3A12*cs%3A1730909507*fs%3A1730698428*pv%3A25*ps%3A1730907928*exp%3A%7B%7D; _conv_s=si%3A12*sh%3A1730909507478-0.6317491576077305*pv%3A1; _ga_RSMJC35YH9=GS1.1.1730907931.3.1.1730909508.60.0.0; cto_bundle=UWiacV9NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QXZtYXpURCUyQmp3SUFFJTJCVVdxJTJGZk9HMXZ0aE9oOEtQNjh3R3VBVFRRcEoxeVVtbDgwbjZYWVBFQmRBSUhWRGpQRzhtVUNJQ3JnR1Y0SXFCYXlXZmpYY1ZNVHpJZXlmczRHZnhDMlZmZFlCWWVXT3JGcE16OWdOMzA3VXZKSzhtSGdOQSUzRCUzRA; _uetsid=ead56fe09c0f11efb63d6b762397b31c; _uetvid=ead5b7809c0f11efb0eed396762de15c; forterToken=552dd3c56da24fb2bc2f1685b5599b52_1730909506661__UDF43-m4_21ck_; forter-uid=552dd3c56da24fb2bc2f1685b5599b52_1730909506661__UDF43-m4_21ck__tt; ADRUM_BTa=R:0|g:6e020422-39ef-4ff6-bc6e-06a7f6f8ddb3|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:0|i:268164|e:447',
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
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "metro_canada.middlewares.MetroCanadaSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # "metro_canada.middlewares.MetroCanadaDownloaderMiddleware": 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
}
# -------------------------------------

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "metro_canada.pipelines.MetroCanadaPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
