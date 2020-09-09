# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MaodouspiderPipeline(object):
    def __init__(self):
        self.count = 1
        self.conn_mysql()

    def conn_mysql(self):
        self.db = pymysql.connect("127.0.0.1","root","lh7288788sb","taoche")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        detail_url = item["detail_url"]
        carname = item["carname"]
        price = item["price"]
        changshang = item["changshang"]
        jibie = item["jibie"]
        fadongji = item["fadongji"]
        biansuxiang = item["biansuxiang"]
        lwh =  item["lwh"]
        cheshenxingshi =  item["cheshenxingshi"]
        ranliao = item["ranliao"]
        carcolor = item["carcolor"]
        incolor = item["incolor"]

        try:
            sql = f"""insert into maodou(detail_url,carname,price,changshang,jibie,fadongji,biansuxiang,lwh,cheshenxingshi,ranliao,carcolor,incolor)VALUES ("{detail_url}","{carname}","{price}","{changshang}","{jibie}","{fadongji}","{biansuxiang}","{lwh}","{cheshenxingshi}","{ranliao}","{carcolor}","{incolor}")"""
            print(self.count, sql)
            self.count += 1
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        return item
    def __del__(self):
        self.db.close()
        self.cursor.close()

