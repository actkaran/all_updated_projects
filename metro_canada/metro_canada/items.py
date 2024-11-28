# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MetroLinks(scrapy.Item):
    product_number = scrapy.Field()
    url = scrapy.Field()


class MetroCanadaItem(scrapy.Item):
    mrp = scrapy.Field()
    product_name = scrapy.Field()
    product_number = scrapy.Field()
    product_url = scrapy.Field()
    currency = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    price_per_unit = scrapy.Field()
    quantity = scrapy.Field()
    product_image = scrapy.Field()
    product_description = scrapy.Field()
    ingredients = scrapy.Field()
    valid_date = scrapy.Field()
    serving_for_people = scrapy.Field()
