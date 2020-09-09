# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 9:55
# @Author  : 神厨李富贵biubiu！！
# @FileName: maodou.py
# @Blog    ：https://mp.csdn.net/console/article
from ..items import MaodouspiderItem
import scrapy
import re

class Maodou(scrapy.Spider):
    name = "maodou"
    start_urls = ["https://www.maodou.com/car/list/all"]

    def parse(self, response):
        """获取最大页"""
        html = response.text
        max_page = re.findall('"page":(\d+)',html)[-1]
        for i in range(1,int(max_page)+1):
            url = f"https://www.maodou.com/car/list/all/pg{i}"
            yield scrapy.Request(url=url,callback=self.parse_detail)
        print(max_page)


    def parse_detail(self, response):
        # 缩小范围
        a_list = response.xpath('.//a[@class="car-item"]')
        if a_list.extract():
            for a in a_list:
                # 详情url
                detail_url = a.xpath('.//@href').extract()[0]
                # print(detail_url)
                # 实例化items
                item = MaodouspiderItem()
                item["detail_url"] = detail_url
                # print(item)
                yield scrapy.Request(url=detail_url,callback=self.parse_date,meta={"data":item})

    def parse_date(self,response):
        item = response.meta["data"]
        # 型号
        carname = response.xpath('//h2[@class="banner-tit"]/text()').extract()[0]

        # 价格
        price = response.xpath('//div[@class="banner-right"]/p/text()').extract()[0]
        price = re.findall("厂商指导价：(.*)万",price)[0]
        # print(price)


        # 厂商
        changshang = response.xpath('//ul[@class="config-detail"]/li[1]/p[2]/text()').extract()[0]
        # print(cahngshang)

        # 级别
        jibie = response.xpath('//ul[@class="config-detail"]/li[2]/p[2]/text()').extract()[0]
        # print(jibie)

        # 发动机
        fadongji = response.xpath('//ul[@class="config-detail"]/li[3]/p[2]/text()').extract()[0]
        # print(fadongji)

        # 变速箱
        biansuxiang = response.xpath('//ul[@class="config-detail"]/li[4]/p[2]/text()').extract()[0]
        # print(biansuxiang)

        # 长宽高
        lwh = response.xpath('//ul[@class="config-detail"]/li[5]/p[2]/text()').extract()[0]
        # print(lwh)

        # 车身形式
        cheshenxingshi = response.xpath('//ul[@class="config-detail"]/li[6]/p[2]/text()').extract()[0]
        # print(cheshenxingshi)

        # 燃料
        ranliao = response.xpath('//ul[@class="config-detail"]/li[7]/p[2]/text()').extract()[0]
        # print(ranliao)

        # 外部颜色
        carcolor = response.xpath('//ul[@class="config-detail"]/li[8]/p[2]/text()').extract()[0]
        # print(carcolor)

        # 内部颜色
        incolor = response.xpath('//ul[@class="config-detail"]/li[9]/p[2]/text()').extract()[0]
        # print(incolor)

        item["carname"] = carname
        item["changshang"] =changshang
        item["price"] = price
        item["jibie"]=jibie
        item["fadongji"] =fadongji
        item["biansuxiang"] =biansuxiang
        item["lwh"] =lwh
        item["cheshenxingshi"] =cheshenxingshi
        item["ranliao"] =ranliao
        item["carcolor"] =carcolor
        item["incolor"] =incolor
        # print(item)
        yield item