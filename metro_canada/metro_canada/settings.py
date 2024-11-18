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

# COOKIES_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "metro_canada (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS ={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'METRO_ANONYMOUS_COOKIE=9098b0fb-ad46-46c1-b710-25ee667ef5a5; CRITEO_RETAILER_VISITOR_COOKIE=df5eb665-4876-4413-bab6-e2fae72ec0f1; coveo_visitorId=cda1c630-7db1-48f9-9182-dd9d16fad5a8; hprl=en; coveo_visitorId=cda1c630-7db1-48f9-9182-dd9d16fad5a8; _ga=GA1.1.2076354866.1731579794; _gcl_au=1.1.1036957491.1731579794; _fbp=fb.1.1731579824105.831881357317130183; OptanonAlertBoxClosed=2024-11-14T10:29:48.448Z; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=4afda3daa753ae5dd78f74cca9802458f780e0bd1ca2e6eb4a0239e732902253c456cfb5; _clck=essm73%7C2%7Cfqw%7C0%7C1779; _uetsid=602525d0a27311efabe6073e7b3374e2; _uetvid=602561a0a27311efbaf1c94278184692; _clsk=mp2mkg%7C1731662215121%7C4%7C1%7Co.clarity.ms%2Fcollect; SameSite=None; JSESSIONID=D8EDBCAE59BD76C0AEF849BDC7E63D29; APP_D_USER_ID=GnjeZaQE-2175114804; __cf_bm=7wwbAy67XybmmNuutpxJR7ZF813ECTCE5Gf2B__RE.c-1731669821-1.0.1.1-CSt17iUYF1fZVrXkDgWHcyYeRsAN8ZpSs3Gf6or_U1ijUNbz8iaE.G5fFbfFVXuAjStKZ5rjd491K.SDGJivM2Sw1g.1i4H2HPEjoYSp.BI; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Nov+15+2024+16%3A53%3A41+GMT%2B0530+(India+Standard+Time)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6519f6a4-980f-47ba-811d-7a8650589585&interactionCount=4&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _conv_v=vi%3A1*sc%3A24*cs%3A1731669822*fs%3A1730698428*pv%3A60*ps%3A1731667412*exp%3A%7B%7D; _conv_s=si%3A24*sh%3A1731669821768-0.7435593399812148*pv%3A1; cf_clearance=cLVR0Y8PFkhPnY0jorZXTZrvTBbJ_6PxNj7nVWLC9sE-1731669822-1.2.1.1-T0xFyHXnJg.2LG3NK_s3cqugTf4ggoEUB.stjfqSYnKExJIO07xTuNnaW7Sz6JO0FzklLNGOW.Gd8l.HxbHdABbeiU77TQ9lHQRjIeKnRpSoR2lIPO.ar2wXu..pkTptf6KNkqPLbIBucoYsPs8T_4ktzUbWlkuVHFcnqyWYvxrAVW8f_HEtRrO8VL9RTsVisOlqzsnmZCjX50nnrhZQ3vqQgnGv6UXHJoU9FDKeF7VKXUyPHLQAhWLYSKxbmJi9D8f.KELHpgzMwQxSkesKfTg7FJUL81Z68QgYx_lfLIWF5v3LvSf2WbxEEC8d8Zh4MeQToaNwdiYnqFhOD20tWJoJ4YrNEffILmFymlrikTfqF63_qMZZPHUFv2ENK3xy; _ga_RSMJC35YH9=GS1.1.1731669822.5.0.1731669822.60.0.0; cto_bundle=UFXvDF9NR2NnMU4wSGNBdjhkTmVqbSUyQnI0QWxGUTNKR2dzJTJCTjRRTVNXTGRMaDFFS3Ezam1UM3R1ektyWU5Jbk9FTDBUaiUyQkZhMUxaNDR2UkEyWG5RY2tndG5XSmpmMG96T2R4VENveUlNJTJGWjFBV1ElMkY4JTJGclhWdDJqJTJGS3ZVT3lodFFHJTJGMUpXMVY2blBuN1BFRVg0S05VaVZpRFJnJTNEJTNE; forterToken=552dd3c56da24fb2bc2f1685b5599b52_1731669821503__UDF43-m4_21ck_; forter-uid=552dd3c56da24fb2bc2f1685b5599b52_1731669821503__UDF43-m4_21ck__tt; ADRUM_BTa=R:0|g:bdaa792c-ec91-4d9e-8fe3-458c720baa86|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:0|i:268240|e:412',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"130.0.6723.119"',
    'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.119", "Google Chrome";v="130.0.6723.119", "Not?A_Brand";v="99.0.0.0"',
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
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 5
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0

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
