# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 17:14
# @Author  : 神厨李富贵biubiu！！
# @FileName: lianjia.py
# @Blog    ：https://mp.csdn.net/console/article

import scrapy
# 继承scrapy_spider类具有的scrapy类的所有特性
# 作用：可以让很多事情自动完成
class Lianjia(scrapy.Spider):
    # 定义爬虫名称
    name = "lianjia"
    # 定义起始URL,启动爬虫会遍历所有的URL，返回response 默认给parse解析
    start_urls = ["https://bj.lianjia.com/zufang"]

    def parse(self, response):
        # 解析response 数据可以直接用Xpath 不用转换xml
        # 自动化完成
        # 获取城区名和URL
        city_area_list = response.xpath('//ul[@data-target="area"]/li[position()>1]/a/@href | //ul[@data-target="area"]/li[position()>1]/a/text()').extract()
        # print(city_area_list)
        for city_area in city_area_list:
            if "zufang" in city_area:
                city_area = "https://bj.lianjia.com/zufang" + city_area
                print(city_area)
                yield scrapy.Request(url=city_area,callback=self.parese_1,dont_filter=True)

    def parese_1(self,response):
        """获取商圈URL"""
        # 获取商圈名称和商圈URL
        business_url_list = response.xpath("//div[@id='filter']/ul[4]/li[position()>1]/a/@href|//div[@id='filter']/ul[4]/li[position()>1]/a/text()").extract()
        for index in range(0,len(business_url_list),2):
            business_url = "https://bj.lianjia.com/zufang" + business_url_list[index]
            print(business_url)
            yield scrapy.Request(url=business_url,callback=self.parse_page_url,dont_filter=True)

    def parse_page_url(self,response):
        """获取分页URL"""
        # 获取最大页
        max_page = response.xpath("//div[@class='content__pg']/@data‐totalpage").extract()
        # print(max_page)
        max_page = int(max_page[0]) if max_page else  1
        for page in range(1,max_page+1):
            # 拼接分页URL
            page_url = response.url+f"pg{page}"
            yield scrapy.Request(url=page_url,callback=self.parse_page_data,dont_filter=True)

    def parse_page_data(self,response):
        div_list = response.xpath("//div[@class='content__list']/div")
        for div in div_list:
            # 图片
            pic = div.xpath(".//img/@data‐src").extract()
            pic = pic[0].replace(("250x182", "2500x1800"))
            print(pic)