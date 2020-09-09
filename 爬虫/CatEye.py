# 李俊杰
import requests
import os
import re
import time
from lxml import etree


class Cateye:
    def __init__(self):
        self.url = 'https://maoyan.com/board'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

    def __call__(self, *args, **kwargs):
        if os.path.exists('maoyan.html') == True:
            self.get_data()
            self.show()
        else:
            self.get_html()
            self.get_data()
            self.show()


    def get_html(self):
        """获取网页"""
        response = requests.get(self.url, headers=self.header).text
        with open('maoyan.html', 'w', encoding='utf-8') as f:
            f.write(response)

    def get_data(self):
        """获取数据"""
        with open('maoyan.html', 'r', encoding='utf-8')as f:
            html = f.read()
            # 匹配<dd>中的需要数据返回一个列表
            pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<.*?data-src="(.*?)".*?<p.*?name.*?a.*?>(.*?)</a>.*?<p.*?star.*?>'
                         '(.*?)</p>.*?<p.*?releasetime.*?>(.*?)</p>.*?<p.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i></p>'
                        , re.S)
            result = pattern.findall(html)
            for i in result:
                # 用yield返回一个生成器，可以用for循环遍历
                # 如果用return返回的话，只有一个电影的数据
                # 还可以节省空间
                yield {
                    "Rank":i[0],
                    "Image":i[1],
                    "Move_name": i[2],
                    "Actor": i[3].strip()[3:] if len(i[3])>3 else '',
                    "Time": i[4],
                    "Score": i[5]+i[6],
                }
    def show(self):
        """展示数据"""
        print("猫眼电影Top10")
        for i in self.get_data():
            print('-------------------------------------------------------------------------------------------------------------')
            print('排名：',i['Rank'])
            print('电影名称：', i['Move_name'])
            print('图片：',i['Image'])
            print('演员：',i['Actor'])
            print('评分：',i['Score'])

            # html = etree.HTML(html)
            # move_name = html.xpath('//dl[@class="board-wrapper"]/dd/a[1]/@title')
            # print(move_name)
            # move_img = html.xpath('//dl[@class="board-wrapper"]/dd/a[1]/img[@class="board-img"]/@src')
            # print(move_img)
            # for i in  move_name:
            #     print(i)
        # print(result)

if __name__ == '__main__':
    s = time.time()
    cateye = Cateye()
    cateye()
    e = time.time()
    print(e-s)# 0.0009999275207519531
