# Author:lijunjie
# encoding:utf-8
_date_ = "Date 9:22"
import requests
import re



class HouseKing:
    def __init__(self):
        self.base_url = "http://gz.ihk.cn/myxf/houselist/?mark=gzxf089"

    def __call__(self, *args, **kwargs):
        # self.get_html()
        self.get_data()

    def get_html(self):
        """保存网页"""
        response = requests.get(self.base_url)
        html = response.content.decode("utf-8")
        with open("houseKing.html", "w", encoding="utf-8") as f:
            f.write(html)

    def get_data(self):
        """读取网页并且取得数据"""
        with open("houseKing.html", "r", encoding="utf-8") as f:
            html = f.read()
            house_list = re.findall('<div class="ihknewconlistr">([\s\S]*?)</div>\s*?</div>\s*?</div>',html)
            for i in house_list:
                name_list = re.findall('<strong>([^\x00-\xff]+)</strong>', i)
                zaishou_state_list = re.findall(r'-red">(.*?)</span>', i)
                qita_state_list = re.findall('-orange">(.*?)</span>', i)
                price_list = re.findall(r'<strong>(\d+)</strong>',i)
                cankao_list = re.findall(r'<li>参考总价：(.*?)</li>',i)
                hux_list = re.findall(r'iconbg typeicon ihkcontext">户型：(.*?)</div>',i)
                # print(huxing_list)
                address_list = re.findall(r'<div class="iconbg addressicon ihkcontext">(.*?)</div>',i)
                huajin_list = re.findall(r'<span>(.*?)</span>',i)
                for name in name_list:
                    pass
                for price in price_list:
                    pass
                for zhuantai in zaishou_state_list:
                    pass
                for qita in qita_state_list:
                    pass
                for cankao in cankao_list:
                    pass
                for hux in hux_list:
                    # print(hux)
                    pass
                for address in address_list:
                    pass
                for huanjing in huajin_list:
                    # print(huanjing)
                    pass
                dict = {
                    "名称": name,
                    "价格": price+"元/m^2",
                    "状态": zhuantai +"-"+qita,
                    "参考价格": cankao,
                    "地址":address,
                    "环境": huanjing,
                }
                print(dict)
if __name__ == '__main__':
    houseking = HouseKing()
    houseking()
