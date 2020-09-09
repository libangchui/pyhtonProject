# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 10:21
# @Author  : 神厨李富贵biubiu！！
# @FileName: 淘宝宝.py
# @Blog    ：https://mp.csdn.net/console/article
"""
任务：获取 图片、描述、价格
https://www.taobao.com/markets/3c/tbdc?spm=a21bo.2017.201867-main.11.5af911d9WqhgGA&qq-pf-to=pcqq.group
"""
from selenium import webdriver
from lxml import etree
import time
import re

class Taobao:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        self.get_html()
    # 获取网页
    def get_html(self):
        # 创建浏览器驱动
        driver = webdriver.PhantomJS(executable_path=r'D:\PhantomJ\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # 浏览器打开页面
        driver.get(
            "https://www.taobao.com/markets/3c/tbdc?spm=a21bo.2017.201867-main.11.5af911d9WqhgGA&qq-pf-to=pcqq.group")
        # 获取页面数据
        time.sleep(3)
        # 将滚动条移动到页面的中间
        driver.execute_script("var q=document.documentElement.scrollTop=1000")
        time.sleep(1)
        driver.execute_script("var q=document.documentElement.scrollTop=2000")
        time.sleep(1)
        driver.execute_script("var q=document.documentElement.scrollTop=3000")
        time.sleep(1)
        driver.execute_script("var q=document.documentElement.scrollTop=4000")
        time.sleep(1)
        # 将滚动条移动到页面的底部
        driver.execute_script("var q=document.documentElement.scrollTop=99999")
        time.sleep(3)
        html = driver.page_source
        #缩小范围
        htmls = re.findall('<li>([\s\S]*?)</li>',html)
        for dt in htmls:
            data = etree.HTML(dt)
            # 获取链接
            url = data.xpath('//img/@src')
            for c,u in enumerate(url,1):
                base_url = "https:"+u
                # 描述
                title = data.xpath('//p[@class="protwo-title"]//text()')
                # 价格
                price = data.xpath('//p[@class="parttwo-price"]//text()')
                dict = {
                    "img":base_url,
                    "title": title,
                    "price": price
                }
                print(c,dict)

if __name__ == '__main__':
    taobao = Taobao()
    taobao()