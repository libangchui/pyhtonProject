# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 9:47
# @Author  : 神厨李富贵biubiu！！
# @FileName: souhu.py
# @Blog    ：https://mp.csdn.net/console/article
import os
import scrapy

class Souhu(scrapy.Spider):
    name = "souhdu"
    start_urls = ["https://www.sohu.com/"]
    n = ""

    def parse(self, response):
        """获取初始页上方类型连接"""
        type_list = response.xpath('//nav[@class="nav area"]//ul/li/a/@href').extract()
        type_name = response.xpath('//nav[@class="nav area"]//ul/li/a//text()').extract()

        for self.n in type_name:
            if os.path.exists("C:\\Users\\fugui\PycharmProjects\mode\Souhu\Souhu\spiders\搜狐新闻") == False:
                os.mkdir("C:\\Users\\fugui\PycharmProjects\mode\Souhu\Souhu\spiders\搜狐新闻")
            if os.path.exists(f"C:\\Users\\fugui\PycharmProjects\mode\Souhu\Souhu\spiders\搜狐新闻\{self.n}") == False:
                os.mkdir(f"C:\\Users\\fugui\PycharmProjects\mode\Souhu\Souhu\spiders\搜狐新闻\{self.n}")

            for type_url in type_list:
                if "http" not in type_url:
                    type_url = "http:" + type_url
                yield scrapy.Request(url=type_url,callback=self.parse_1)

    def parse_1(self,response):
        """获取文章详情URL，进行筛选"""
        detail_url = response.xpath('//a/@href').extract()
        for c,url in enumerate(detail_url,1):
            if ".com" in url:
                if "https:" not in url:
                    if "/a" and "?scm" in url:
                        if "http:" not in url:
                            url = "http:" + url
                            yield scrapy.Request(url=url,callback=self.parse_detail,dont_filter=False)
                    '''
                    scm a
                    '''
    def parse_detail(self,response):
        """获取文章详情信息"""
        news_list = response.xpath('//article[@class="article"]//p/text()').extract()
        new_list = [x.strip() for x in news_list if x.strip() != '']
        new_list.remove("责任编辑：")
        news = ""
        for index in range(1,len(new_list)):
            news = news + new_list[index]
        with open(f"C:\\Users\\fugui\PycharmProjects\mode\Souhu\Souhu\spiders\搜狐新闻\{self.n}\{new_list[0]}.text","w",encoding="utf-8") as f:
            f.write(news)
            print(f"正在存储-->{new_list[0]}")