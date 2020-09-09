# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 9:02
# @Author  : 富贵
# @FileName: Tencent_news.py

import os
import scrapy
import re
import pathlib

class Tecent(scrapy.Spider):
    name = "tencent"
    start_urls =[]
    for page in range(0,500):
        url = f"https://pacaio.match.qq.com/irs/rcd?cid=4&token=9513f1a78a663e1d25b46a826f248c3c&ext=&page={page}&expIds=&callback=__jp2"
        start_urls.append(url)
    # //div[@class="sub-nav"]/ul/li/a/@href

    def parse(self, response):
        res = response.text
        # print(res)
        news_list = re.findall(',"vurl":"(.*?)"',res)
        for new_url in news_list:
            yield scrapy.Request(url=new_url,callback=self.parse_detail,dont_filter=False)

    def parse_detail(self,response):
        # res = response.text
        # print(res)
        title = response.xpath('//h1/text()').extract()[0]
        news_list = response.xpath('//div[@class="content-article"]//text()').extract()
        new_list = [x.strip() for x in news_list if x.strip() != '']
        if os.path.exists("C:\\Users\\fugui\PycharmProjects\mode\TencentNews\TencentNews\spiders\\tencent") == False:
            os.mkdir("C:\\Users\\fugui\PycharmProjects\mode\TencentNews\TencentNews\spiders\\tencent")
        news = ""
        for index in range(0,len(new_list)):
            news = news + "\n" +new_list[index]
        # if pathlib.Path(f"C:\\Users\\fugui\PycharmProjects\mode\TencentNews\TencentNews\spiders\\tencent\{title}.text") == True:
        # if os.path.isfile(f"C:\\Users\\fugui\PycharmProjects\mode\TencentNews\TencentNews\spiders\\tencent\{title}.text") == True:
        with open(f"C:\\Users\\fugui\PycharmProjects\mode\TencentNews\TencentNews\spiders\\tencent\{title}.text","w",encoding="utf-8") as f:
            print(f"正在存储-->{title}")
            f.write(news)
"""
cmsid  
finance
auto
tech

-zt
-sports

"""