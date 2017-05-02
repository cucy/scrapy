# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from scrapy.pipelines.images import ImagesPipeline

# 主要做数据存储 已经数据处理
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagepipeline(ImagesPipeline):
    """
        将下载图片的url和保存在本地图片名字进行join
    """

    def item_completed(self, results, item, info):
        """ 
            results 保存的是本地实际存储路径
        """
        for ok, values in results:
            image_file_path = values["path"]
        item["front_image_path"] = image_file_path
        return item
        pass


# 数据保存到json文件中
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open("article.json", 'w',encoding='utf-8')

    def process_item(self, item, spider):
        # ensure_ascii 防止中文写入不正常
        lines  = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_close(self):
        self.file.close()
