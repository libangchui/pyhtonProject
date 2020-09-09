# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:59
# @Author  : 神厨李富贵biubiu！！
# @FileName: xinlang.py
# @Blog    ：https://mp.csdn.net/console/article

import scrapy
from ..items import XinlangItem
import os
class Xinlang(scrapy.Spider):
    name = "xl"
    start_urls = ["http://news.sina.com.cn/guide/"]

    def parse(self, response):
        url_list = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
        for url in url_list:
            # print(url)
            yield scrapy.Request(url=url,callback=self.parse_1,dont_filter=True)

    def parse_1(self,response):
        """获取详细URL"""
        dateil_url = response.xpath('//a/@href').extract()
        for url in dateil_url:
            if "http:" in url:
                if "detail-i" in url:
                    if ".shtml" in url:
                        yield scrapy.Request(url=url, callback=self.parse_detail,dont_filter=True)
    def parse_detail(self,response):
        """获取所有新闻信息"""
        item = XinlangItem()
        title = response.xpath('//h1/text()').extract()[0]
        news_list = response.xpath('//div[@class="article-body main-body"]/p/text()').extract() #.replace(u'\u3000',u' ')
        imgs_list = response.xpath('//div[@class="img_wrapper"]/img/@src').extract()[0]
        news = ""
        for index in range(0,len(news_list)):
           news = news+news_list[index]
        # 文档存入
        new = title+"\n"+news+"\n"+imgs_list
        if os.path.exists("D:\新浪新闻") == False:
            os.mkdir("D:\新浪新闻")
        with open(f"D:\新浪新闻\{title}.txt","w",encoding="utf-8") as f:
            f.write(new)
            print(f"正在存入-->{new}")
        # 数据库存入
        # item["title"] = title
        # item["news"] = news
        # item["imgs"] = imgs_list
        # yield item









