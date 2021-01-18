# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标签字段
    link = scrapy.Field()  # 名言内容
    author = scrapy.Field()  # 名言内容
    tags = scrapy.Field()  # 名言内容
    date = scrapy.Field()  # 名言内容
    pass
