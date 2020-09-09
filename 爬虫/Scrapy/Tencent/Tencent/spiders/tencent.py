# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 11:34
# @Author  : 神厨李富贵biubiu！！
# @FileName: tencent.py
# @Blog    ：https://mp.csdn.net/console/article
import scrapy
import re
from ..items import TencentItem
class Tencent(scrapy.Spider):
    name = "tencent"
    start_urls = []

    for i in range(1,490):
        url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1584505719665&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={i}&pageSize=10&language=zh-cn&area=cn"
        start_urls.append(url)
    print(len(start_urls))


    def parse(self, response):
        # """获取详情url"""
        try:
            r = response.text
            Post_id = re.findall(r'"PostId":"(.*?)"',r)
            for id in Post_id:
                detail_url = f"https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1584509839422&postId={id}&language=zh-cn"
                yield scrapy.Request(url=detail_url,callback=self.parse_date,dont_filter=True)
        except Exception as e:
            print(e)

    def parse_date(self,response):
        rea = response.text
        # 公司名称
        RecruitPostName = re.findall(r'"RecruitPostName":"(.*?)"',rea)[0]

        #所在地
        LocationName = re.findall(r'"LocationName":"(.*?)"',rea)[0]


        # 时间
        LastUpdateTime = re.findall(r'"LastUpdateTime":"(.*?)"', rea)[0]

        # BGName
        BGName = re.findall(r'"BGName":"(.*?)"',rea)[0]

        # CategoryName
        CategoryName = re.findall(r'"CategoryName":"(.*?)"',rea)[0]

        # 工作职责
        Responsibility = re.findall(r'"Responsibility":"(.*?)"',rea)[0]


        # 工作要求
        Requirement = re.findall(r'"Requirement":"(.*?)"', rea)


        item = TencentItem()
        item["RecruitPostName"] =RecruitPostName
        item["LocationName"] =LocationName
        item["LastUpdateTime"] =LastUpdateTime
        item["BGName"] =BGName
        item["CategoryName"] =CategoryName
        item["Responsibility"] =Responsibility
        item["Requirement"] = Requirement
        yield item
        # print(item)





