# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 声明要爬取的字段名称，需要存入数据库
class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic = scrapy.Field()
    title = scrapy.Field()
    city_area = scrapy.Field()
    business_circle = scrapy.Field()
    area = scrapy.Field()
    toward = scrapy.Field()
    room = scrapy.Field()
    hall = scrapy.Field()
    toilet = scrapy.Field()
    publish_date = scrapy.Field()
    sign = scrapy.Field()
    price = scrapy.Field()
    detail_url = scrapy.Field()
    floor = scrapy.Field()
    phone = scrapy.Field()
    refresh_time = scrapy.Field()
