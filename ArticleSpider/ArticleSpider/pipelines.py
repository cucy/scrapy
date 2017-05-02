# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 主要做数据存储 已经数据处理
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item
