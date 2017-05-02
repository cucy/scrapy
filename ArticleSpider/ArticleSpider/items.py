# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 类似Django中的from
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime, re

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    # 等价于 lambda x : x + "jobbole"
    return value + "-jobbole"


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


class ArticleItemLoader(ItemLoader):
    # 自定义 ItemLoader
    default_output_processor = TakeFirst()


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def remove_comment_tags(value):
    #去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    return value


class JobBoleArticlesItem(scrapy.Item):
    title = scrapy.Field(
        # 预处理
        # lambda x : x + "jobbole"
        input_processor=MapCompose(add_jobbole)
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )  # 封面图
    front_image_path = scrapy.Field()  # 封面图本地存放路径
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )  # 点赞数量
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )  # 评论数量
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )  # 收藏数量
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(","),
    )  # 标签
    content = scrapy.Field()  # 正文
