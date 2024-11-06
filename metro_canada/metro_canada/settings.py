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
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'JSESSIONID=6795DE1F54C91194C179CBF23EDBA75D; METRO_ANONYMOUS_COOKIE=2a089653-3862-4c44-88e7-c0b966b9ac90; APP_D_USER_ID=SbAxJbfW-2167009951; coveo_visitorId=6079a312-f6a6-4fe3-b36f-eeb9f22d4406; hprl=en; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=37cda3dd8480094768c32d3f812de4df3b6f3fbc19793496f46507e16debc1d0cdd83e0c; __cf_bm=IoWUNYw8ZW5LB91NST7FN0ZdPLCpjBjeKvtkAZJQEX0-1730899052-1.0.1.1-hUjNK0al7X1jLV07jBOZTpZtN9YruVatw8UhkZHMTmlqLE9V5h5TeG43pGCNRJOtK2TqImzixW_pLhzXpoyW5JvtwNLQrI.MY2n0UIYz334; cf_clearance=2On379AiO8vdsAuC6lzWWtkzNSWXT.MfdkLqcbFl5cw-1730899057-1.2.1.1-6RYL4y4IZl.3WuXBiXteL5H8A3r0AVTq4omUmpgxj9JiSy4wXGwkbrYVcvUZhWRkrMF4MfOGFX7j0A4GsnmXKoxV3YHqjqfXNhKY8SP_SeIkruYoGp9BHDStGHHDmpAMn88dlMe_L_ghwaNb_cjxWGgmsLUHTBvZAlJuz8TJ79RGDA7HKAW322YUF2b9TRltO8Alo4TzgLj.Cmz6eiTNQxMOz79jiYxZEstBLXI6zBtWaj1rE7EtbN1YSyjTvWfNESGupfh2sq94yurgaBEqgQeuK7rkaUwUYxR8FXn37pWfnJqDid8mwyZcQM4Hm5WUMa2Y.DZJqPUMUsKvs.iLTwFJYhZahpuqFW3ii4BGWWO5yf.EC24Tg0Jx0LENYALI; OptanonAlertBoxClosed=2024-11-06T13:17:44.195Z; _gcl_au=1.1.540019629.1730899064; _ga=GA1.1.647041018.1730899064; coveo_visitorId=6079a312-f6a6-4fe3-b36f-eeb9f22d4406; _fbp=fb.1.1730899068064.993329482787135454; _clck=71w9uk%7C2%7Cfqn%7C0%7C1771; _ga_RSMJC35YH9=GS1.1.1730899064.1.1.1730899102.22.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+18%3A48%3A26+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=a9798f4d-563d-42d3-9534-2f2540fd0186&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _conv_v=vi%3A1*sc%3A1*cs%3A1730899065*fs%3A1730899065*pv%3A4; _conv_s=si%3A1*sh%3A1730899064548-0.12445316273914386*pv%3A4; _uetsid=84d339509c4111ef991043720f8714d1; _uetvid=84d344d09c4111efb78dcdbab0c132ca; _clsk=1j1h5xb%7C1730899110084%7C3%7C1%7Ch.clarity.ms%2Fcollect; forterToken=8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck_; forter-uid=8a6f7b9a525045c8989973707d4353a4_1730899099333__UDF43-m4_21ck__tt; cto_bundle=dsCD1V9PQ1NlRlVoTGdETTk1QjdjaWtCc1FicWxHcWZaUkVWSjd4VnBQQyUyRlFySUhDOXU3OTJ5SjBqeE5aZVlWcm1mbXFNZUcxMUNDcHhyNmpjUE1LUFdIVjROOHlTZ1ZEaUVScHIydDJFanJpWlhBcXhrU0pXQ3Y4VkFuWGNzcnRQUUhEVW9pJTJCYXdOaHk0UmM4VTRVNE1pQmpnJTNEJTNE',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
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
