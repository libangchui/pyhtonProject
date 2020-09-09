# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class TencentPipeline(object):
    def __init__(self):
        self.count = 1
        self.conn_mysql()

    def conn_mysql(self):
        self.db = pymysql.connect("127.0.0.1", "root", "lh7288788sb", "taoche")
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        RecruitPostName =item["RecruitPostName"]
        LocationName=item["LocationName"]
        LastUpdateTime=item["LastUpdateTime"]
        BGName=item["BGName"]
        CategoryName=item["CategoryName"]
        Responsibility=item["Responsibility"]
        Requirement=item["Requirement"]

        try:
            sql = f"""insert into tencent(RecruitPostName,LocationName,LastUpdateTime,BGName,CategoryName,Responsibility,Requirement)VALUES ("{RecruitPostName}","{LocationName}","{LastUpdateTime}","{BGName}","{CategoryName}","{Responsibility}","{Requirement}")"""
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