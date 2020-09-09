# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MoguPipeline(object):
    def __init__(self):
        self.count = 1
        self.conn_mysql()

    def conn_mysql(self):
        self.db = pymysql.connect("127.0.0.1", "root", "lh7288788sb", "taoche")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        title = item["title"]
        img = item["img"]
        price = item["price"]

        try:
            sql = f"""insert into mogu(title,img,price)VALUES ("{title}","{img}","{price}")"""
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
