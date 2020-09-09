# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaodouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url = scrapy.Field()
    carname = scrapy.Field()
    price = scrapy.Field()
    changshang = scrapy.Field()
    jibie = scrapy.Field()
    fadongji = scrapy.Field()
    biansuxiang = scrapy.Field()
    lwh = scrapy.Field()
    cheshenxingshi = scrapy.Field()
    ranliao = scrapy.Field()
    carcolor = scrapy.Field()
    incolor = scrapy.Field()
    pass
