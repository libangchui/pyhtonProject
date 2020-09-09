#Author:lijunjie
# encoding:utf-8
_date_ = "Date 16:55"
import requests
import re

class Huaxia:
    def __init__(self):
        self.base_url = "http://fund.chinaamc.com/portal/cn/include/newproducthome.jsp"

    def __call__(self, *args, **kwargs):
        # self.get_html()
        self.get_data()

    def get_html(self):
        """保存网页"""
        response = requests.get(self.base_url)
        html = response.text
        with open("hua.html","w",encoding="utf-8") as f:
            f.write(html)
        self.get_data()

    def get_data(self):
        """获取数据"""
        # 读取文件
        with open("hua.html","r",encoding="utf-8") as f:
            html = f.read()
        # print(html)

        # 缩小范围
        table_list = re.findall('<table.*?id="tb\d*?">[\s\S]*?</table>',html)
        # print(table_list[2])
        for c,table in enumerate(table_list):
           if c == 0:# 我们正在取第一个表格数据
            # 继续缩小范围
            tr_list = re.findall('<tr.*?id="tr\d+".*?>[\s\S]*?</tr>',table)
            del tr_list[0]
            for c,tr in enumerate(tr_list,1):
                td_list = re.findall('<td height="\d+".*?>.*?</td>',tr)
                del td_list[0]
                del td_list[9]
                name = re.findall('title="(.*?)" target', tr)
                value_list = []
                value_list.append(name)
                for i in td_list:
                    num = re.findall('<td height="30">(.*?)</td>',i)
                    value_list.append(num)
                dict = {
                    "基金简称":value_list[0],
                    "基金代码":value_list[1],
                    "净值日期":value_list[2],
                    "净值": value_list[3],
                    "累计净值": value_list[4],
                    "涨跌幅": value_list[5],
                    "成立日期": value_list[6],
                    "申购状态": value_list[7],
                    "赎回状态": value_list[8],
                    "定投状态": value_list[9],
                }
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(dict)
if __name__ == '__main__':
    huaxia = Huaxia()
    huaxia()