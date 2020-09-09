# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 9:32
# @Author  : 神厨李富贵biubiu！！
# @FileName: 李俊杰-35318618.py
# @Blog    ：https://mp.csdn.net/console/article
import requests
from lxml import etree
class Baixing:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
    def __call__(self, *args, **kwargs):
        self.get_html()

    def get_html(self):
        url = "https://beijing.baixing.com/chongwujiaoyi/m177986/?entities=%E6%80%A7%E5%88%AB_%E5%85%AC&page=1&%E4%BB%B7%E6%A0%BC%5B0%5D=1000&%E4%BB%B7%E6%A0%BC%5B1%5D=1100&%E5%B9%B4%E9%BE%84%5B0%5D=0&%E5%B9%B4%E9%BE%84%5B1%5D=3"
        response = requests.get(url, headers=self.headers).text
        html = etree.HTML(response, etree.HTMLParser())
        dog_message = html.xpath('(//li[@data-service="regular"]/a/img/@data-originsource) | (//div[@class="media-body-title"]/span/text()) | (//div[@class="media-body-title"]/a[1]/text()) | (//div[@class="ad-item-detail"][1]/text() | //div[@class="ad-item-detail"][2]/text())')
        for i in dog_message:
            print(i)
        # dic = {}
        # dog_img = html.xpath('//li[@data-service="regular"]/a/img/@data-originsource')
        # dog_details = html.xpath('//div[@class="media-body-title"]/a[1]/text()')
        # dog_money = html.xpath('//div[@class="media-body-title"]/span/text()')
        # dog_address = html.xpath('//div[@class="ad-item-detail"][1]/text()')
        # dog_kind = html.xpath('//div[@class="ad-item-detail"][2]/text()')
        # for img in dog_img:
        #     pass
        # for details in dog_details:
        #     pass
        # for money in dog_money:
        #     pass
        # for address in dog_address:
        #     pass
        # for kind in dog_kind:
        #     pass
        # dic["Dog_img"] = dog_img
        # dic["Dog_Details"] = dog_details
        # dic["Dog_money"] = dog_money
        # dic['Dog_address'] = dog_address
        # dic['Dog_Kind'] = dog_kind
        # for a in dic:
        #     print(a)
if __name__ == '__main__':
    baixing = Baixing()
    baixing()
