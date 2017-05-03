# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
import MySQLdb.cursors

from twisted.enterprise import adbapi
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter


# 主要做数据存储 已经数据处理
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagePipeline(ImagesPipeline):
    """
        将下载图片的url和保存在本地图片名字进行join
    """
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path

        return item



# 自定义数据保存到json文件中
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open("article.json", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # ensure_ascii 防止中文写入不正常
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_close(self):
        self.file.close()


# json 调用scrapy导出json
class JsonItemExporterPipeline(object):
    def __init__(self):
        self.file = open('articleJsonItemExporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


# 导入mysql数据库中
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect("192.168.1.107", 'zrd', '123456', 'article_spider', port=3306, charset='utf8',
                                    use_unicode=True)
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):
        insert_sql = """ 
       INSERT INTO `article_spider`.`jobbole_article`(title,url, create_date,  fav_nums, url_object_id)
        VALUES (%s,%s, %s, %s,%s)
        """
        self.cursor.execute = (insert_sql, (item['title'], item['url'], item["create_date"], item["fav_nums"]))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        if failure:
            print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print (insert_sql, params)
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

