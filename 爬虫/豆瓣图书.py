# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 9:52
# @Author  : 神厨李富贵biubiu！！
# @FileName: 李俊杰-豆瓣图书.py
# @Blog    ：https://mp.csdn.net/console/article
from selenium import webdriver
import time
from lxml import etree
import re
"""
豆瓣读书   连接  ：https://book.douban.com/subject_search?search_text=python&cat=1001&start=%25s0
任务：使用selenium获取 书名、评分、作者、出版社信息、详情url
"""
class Douban:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        self.get_html()

    def get_html(self):
        # 获取浏览器对象
        browers = webdriver.PhantomJS(executable_path=r'D:\PhantomJ\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # 用浏览器发起请求
        for i in range(0,200):
            url = f"https://book.douban.com/subject_search?search_text=python&cat=1001&start={i*15}"
            try:
                browers.get(url)
                # 降低评率，提高安全性
                time.sleep(3)
                html = browers.page_source
                print(f"=========================第{i+1}页=================================")
                self.get_data(html)
                time.sleep(1.5)
            except Exception:
                print("error")

    def get_data(self,html1):
        html = etree.HTML(html1)
        books = html.xpath('//div[contains(@class,"detail")]')
        for c,book in enumerate(books):
            # 获取封面信息
            book_name = book.xpath('.//a[@class="title-text"]/text()')[0]
            # print(c,book_name)
            #评分
            score = book.xpath('.//span[@class="rating_nums"]/text()')
            # print(c,score)
            # 作者
            author = book.xpath('.//div[@class="meta abstract"]/text()')[0]
            # print(c,author)
            # url
            book_url = book.xpath('.//a/@href')[0]
            # print(c,book_url)
            dic={
                "Book_name":book_name,
                "Book_score":score,
                "Bokk_details":author,
                "Book_url":book_url
            }
            print(c,dic)

if __name__ == '__main__':
    douban=Douban()
    douban()
