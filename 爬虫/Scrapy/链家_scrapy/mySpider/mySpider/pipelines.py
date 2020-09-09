# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MyspiderPipeline(object):
    def __init__(self):
        self.conn_mysql()

    def conn_mysql(self):
        # 连接数据库
        self.db = pymysql.connect('127.0.0.1',"root","lianjia","lh7288788sb",charset="utf8")
        # 创建游标
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        pic = item["pic"]
        title = item["title"]
        city_area = item["city_area"]
        business_circle = item["business_circle"]
        area = item["area"]
        toward = item["toward"]
        room = item["room"]
        hall = item["hall"]
        toilet = item["toilet"]
        publish_date = item["publish_date"]
        sign = item["sign"]
        price = item["price"]
        detail_url = item["detail_url"]
        floor = item["floor"]
        phone = item["phone"]
        refresh_time = item["refresh_time"]
        # sql 语句
        sql = f"""insert into lianjia(pic,title,city_area,business_circle,area,toward,room,hall,toilet,publish_date,sign,price,detail_url,floor,phone,refresh_time)VALUE ("{pic}","{title}","{city_area}","{business_circle}","{area}","{toward}",{room},{hall},{toilet},"{publish_date}","{sign}","{price}","{detail_url}","{floor}","{phone}","{refresh_time}")"""
        print(self.count,sql)
        self.count +=1
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        return item
    def __del__(self):
        self.cursor.close()
        self.db.close()
