# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 类似Django中的from
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticlesItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field() # 封面图
    front_image_path = scrapy.Field() # 封面图本地存放路径
    praise_nums = scrapy.Field() # 点赞数量
    comment_nums = scrapy.Field() # 评论数量
    fav_nums = scrapy.Field() # 收藏数量
    tags = scrapy.Field() # 标签
    content = scrapy.Field() # 正文

