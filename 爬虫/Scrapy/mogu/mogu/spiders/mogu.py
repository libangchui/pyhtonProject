# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:50
# @Author  : 神厨李富贵biubiu！！
# @FileName: mogu.py
# @Blog    ：https://mp.csdn.net/console/article
import scrapy
import re
from ..items import MoguItem

class Mogu(scrapy.Spider):
    name = "mogu"
    start_urls = []
    name_list = ["clothing","skirt","trousers","neiyi","shoes","bags","boyfriend","baby","home"]
    for n in name_list:
        for page in range(1,101):
            url = f"https://list.mogu.com/search?callback=jQuery211017377024602085944_1584582842655&_version=8193&ratio=3%3A4&cKey=15&page={page}&sort=pop&ad=0&fcid=&action={n}"
            start_urls.append(url)
    print(len(start_urls))


    def parse(self, response):
        res = response.text
        item = MoguItem()
        # 标题
        title = re.findall('"title":"(.*?)",', res)
        del title[0]
        del title[0]
        del title[0]
        for t in title:
            item["title"] = t
            yield item
        # # 图片
        img = re.findall('"img":"(.*?)",',res)
        for i in img:
            item["img"] = i
            yield item
        # # 价格
        price = re.findall('"price":(.*?),',res)
        for p in price:
            item["price"] = p
            yield item