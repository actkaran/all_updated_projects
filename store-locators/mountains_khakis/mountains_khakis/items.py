# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MountainsKhakisItem(scrapy.Item):
    store_no = scrapy.Field()
    name = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    street = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip_code = scrapy.Field()
    county = scrapy.Field()
    country = scrapy.Field()
    open_hours = scrapy.Field()
    phone_number = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
    provider = scrapy.Field()
    category = scrapy.Field()
    updated_date = scrapy.Field()
    direction_url = scrapy.Field()
