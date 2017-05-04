# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
import re
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import JobBoleArticlesItem, ArticleItemLoader
from ArticleSpider.tools.common import get_md5
from scrapy.loader import ItemLoader


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
            1、获取文章列表页中的文章url并交给解析函数进行字段解析 
            2、获取下一页的url交给scrapy进行下载
        :param response: 
        :return: 
        """
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # response.url + post_url
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")

            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self.parse_detail)  # 回调函数

            # 提取下一页交给scrapy 下载
            next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")  # 两个class同时出现
            if next_urls:
                yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)  # 回调函数

    def parse_detail(self, response):

        # article_item = JobBoleArticlesItem()  # 实例化items
        #
        # # css选择器提取字段
        # front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        # title = response.css(".entry-header > h1::text").extract_first()
        # create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace(" ·", "")
        # praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        #
        # fav_nums = response.css(".bookmark-btn::text").extract()[0]
        # fav_num = re.match(r".*?(\d+).*", fav_nums)
        # if fav_num:
        #     fav_nums = int(fav_num.group(1))
        # else:
        #     fav_nums = 0
        # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        # comment_num = re.match(r".*?(\d+).*", comment_nums)
        # if comment_num:
        #     comment_nums = int(comment_num.group(1))
        # else:
        #     comment_nums = 0
        # content = response.css("div.entry").extract()[0]
        # tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()[0]
        # tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        # tags = "".join(tag_list)
        #
        # article_item["url_object_id"] = get_md5(response.url)
        # article_item["title"] = title
        # article_item["url"] = response.url
        #
        # try:
        #     create_date = datetime.strptime(create_date, "%Y/%m/%d").date()
        #
        # except Exception as e:
        #     create_date = datetime.now().date()
        # article_item["create_date"] = create_date
        # article_item["front_image_url"] = [front_image_url, ]
        # article_item["praise_nums"] = praise_nums
        # article_item["comment_nums"] = comment_nums
        # article_item["fav_nums"] = fav_nums
        # article_item["tags"] = tags
        # article_item["content"] = content

        # 通过ItemLoader加载item
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = ArticleItemLoader(item=JobBoleArticlesItem(), response=response)
        item_loader.add_css("title", ".entry-header > h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url, ])
        item_loader.add_css('praise_nums', ".vote-post-up h10::text")
        item_loader.add_css('comment_nums', "a[href='#article-comment'] span::text")
        item_loader.add_css('fav_nums', ".bookmark-btn::text")
        item_loader.add_css('tags', "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css('content', "div.entry")

        article_item = item_loader.load_item()

        yield article_item  # yield以后会传递到pipelines中

    pass
