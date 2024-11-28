# Scrapy settings for tiffany project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "tiffany"

SPIDER_MODULES = ["tiffany.spiders"]
NEWSPIDER_MODULE = "tiffany.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "tiffany (+http://www.yourdomain.com)"

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
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'AKA_A2=A; ak_bmsc=0A1C4C8480C538A173788883DC54AA02~000000000000000000000000000000~YAAQtiLHF5iNCDOSAQAAWMK8ahlUlisRz8uyx/ir0E7Q/eh33vFiPIBulWA91Koy9mSAxRq5E+Kji8IN5YshT7Xw4I9yghqlmRjcebitWAcWkKk1iKfZX+4qBtQ8027z8XjTjUttC6eivwAWyE7N0pEyKluz4S9liy505TjPJHdAn8RPSRRZE+3Lv7FjEt9ylx2cBn+zBzFv56bDMISlg+90dTpB6ByBGgiPSLfv0saRG9IARXg14P/kkZLNpJwh6+mVJ7ubaja4Z0OfkL5zHiFXYncDbinmKV1wCdhWA9uvGhJVEFVHuBBY1z8MD2lH8oYELRmNjfW7V59Qk9NZIseQmP1lAymmcFU8qAgoXIDRQwQyeElgcj9eX0+RRG3UoD8XdXSvTg69WLAdU8t4Vdw=; geo-location-cookie=IN; at_check=true; rr_session_id=Habb9LG1dFRLudSj422kaNOHx2WvwxoN; AMCVS_C7E83637539FFF380A490D44%40AdobeOrg=1; AMCV_C7E83637539FFF380A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C20005%7CMCMID%7C28273356572245672630999558948348479975%7CMCAAMLH-1728972411%7C12%7CMCAAMB-1728972411%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1728374811s%7CNONE%7CvVersion%7C5.2.0; _cs_c=0; _abck=E3A6D122F672F5A139DC0D6887B2D4CA~0~YAAQzDtAF85qPFmSAQAAGdO8agzvvDesAAy4GXXJx5FcOuvOoweFvldNTF7YHyqBQdbx/0c9JzYC8MuG9TqPqTQwtZBTip1gt2ImpdDD2NNyLVZzEfquy+KEoB0z/pfeFWjlvDdK43UCNc+WcWpD6eLFOGWCav0mfoMQyGqwEH+CIDfl7Mp87kQwn8Uwasr2SnNay+CpkytqugPWlHxVX0mlsoInAExnJqaJDVbD+JXywWza+J4dR8qoiLhB1T4NdBpdx2l7vpBu7VN74ESN+8yUb7YLsyXeK5OvV/PfYETS0aLozUmxJ0Igm/wmQSb752UHWaALScUL0oVvul16K13F2LbU2Wf7Nd5Ldqt+aOc4lS4SbcJw6UmCUvBzeo6Jsr3JqXhFJJmxAbbbbqM8La+Qo+yBaPPXEgXupyntPj+Qba74XkllZu8aXnjnmSxgYDpVbnyHSOsHeA==~-1~||0||~-1; __attentive_id=b145b99876094df695ff435480c2e733; _attn_=eyJ1Ijoie1wiY29cIjoxNzI4MzY3NjEzMTI2LFwidW9cIjoxNzI4MzY3NjEzMTI2LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImIxNDViOTk4NzYwOTRkZjY5NWZmNDM1NDgwYzJlNzMzXCJ9In0=; __attentive_cco=1728367613128; __attentive_ss_referrer=https://www.google.com/; __attentive_dv=1; siteVisited=true; _mibhv=anon-1728367618513-1907453424_7762; _ga=GA1.1.2060230549.1728367619; _gcl_au=1.1.1019611159.1728367619; _scid=-0DZ5MqjkACEgwTCAC6VoR1VlW4xnc8N; _tt_enable_cookie=1; _ttp=lxZY-SOpth22jMEktZS_EW60d8F; _fbp=fb.1.1728367619417.773824807784988918; _pin_unauth=dWlkPU1tWTNZelUyTjJRdE4yWTVaUzAwTVRFeUxXSmtNV1F0TXpSak9UQXdZek5tTW1ZeA; _ScCbts=%5B%5D; _sctr=1%7C1728325800000; LPVID=Y5ZjE3M2FmMDY3MTk2MjE2; LPSID-41337752=LPfKrNQNSD6va4cMZrhBlw; dntstatus=0; samebrowsersession=; langprefforca=-1; ecmid=; myeid=; hascookies1=1; assortmentid=101; dtmusersessionid=a190a65bc7414d27892b0f27c2d62d72; previoussid=; welcome_back_session_duplicate=true; bm_sz=307FE125B55DCDB24F5CB0C77EBC522A~YAAQzDtAF7etPFmSAQAA8uDMahmn8hhnv7AqC8ey3p4HDl0VZ6BTi3n/sPJq3yaA4lnoKqHt0akqVVvV7wClTqFOeipyV7Xg1fG5xydiIB759O/7rr+BVzhVjDbQuE8zx5KjWlS8C5uv71MH665H2rK3/e/wyL252sRhP955PHmYdWwN2TCt+BJ4LiLa0s211nNmnI4IsPRT1TR1BA9lh/hiMI/AUUWzAnAUip7QWTCXtpX5CYU1Nw53ARtNmgk/sGnuMLNMB9ewy/8oKybaaPQd7gZMugYXwQoQdyjYQlCLOY5BqudHKx5LDSSWfaOcKtku5RTPH45hTN90MJFRqP3Qp36jzJRXOF+WBVsgYzVBPm5vFyuUIW/619t+rYfUd+OaQkvuIr0O/eu+GNdy8ltGEkYQUfra3KfBD1KtgxOTwBEw/RpgzeVEfW/tAkStCA1TrKmFLoNFozC3qUe5XTWmGIVZ/yQtckfT2gO5JNuvhE5/TITOKus8a7wE2cr8b0QGQiKoOl9UVZc=~4536626~3617347; mbox=session#19fb3e56b9954ab289427a055dfe10c4#1728369472|PC#19fb3e56b9954ab289427a055dfe10c4.41_0#1791613466; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+08+2024+11%3A54%3A25+GMT%2B0530+(India+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2CSSPD_BG%3A1%2C4%3A1%2C2%3A1&AwaitingReconsent=false; _cs_id=d210cf8f-4686-a197-d363-c5bfd52613e0.1728367611.1.1728368665.1728367611.1712004218.1762531611928.1; _ga_6LS0S7KLVS=GS1.1.1728367618.1.1.1728368666.33.0.1218857479; _uetsid=87565da0853b11efa447a71d7b6b96f5; _uetvid=87565b80853b11ef9015c3db37c27971; _scid_r=DMDZ5MqjkACEgwTCAC6VoR1VlW4xnc8Nyxai6A; __attentive_pv=10; bm_sv=058621801FBB3B42FB77674C768FF380~YAAQzDtAF+CtPFmSAQAAsO3Mahl8WeoMSbYGWNvn0TMWZAOx1gdnGyxvfdcFsh9peUk9gZq8TxJKCH9ZQ2LXP/QRtpmUgSCpF6q3oXimkOrsah0hl45iytstfoUOuB0Oe1Zn1KUWr0s7hNuf+rkywGzdlPEt79Z9Yc0LBr+G2VvXVkBNBINp9NocnHwUSGNL+PMMSkzCJS1wIkY90QRErHxbkDaQMwlBe12WCfz+HfCBxqmnNa+snfqsVDg3GDirUJE=~1; _cs_s=10.5.0.1728370730717; RT="z=1&dm=tiffany.com&si=9eda6b8f-39da-4d6f-b219-197b7c3449a5&ss=m201g7ci&sl=6&tt=m93&bcn=%2F%2F684d0d4c.akstat.io%2F&ld=lkhh&nu=qge2ox1&cl=sfl0"',
#     'priority': 'u=0, i',
#     'referer': 'https://www.tiffany.com/jewelry-stores/',
#     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "tiffany.middlewares.TiffanySpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "tiffany.middlewares.TiffanyDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "tiffany.pipelines.TiffanyPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
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
