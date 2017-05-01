# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse


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

            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},callback=self.parse_detail) #回调函数

            # 提取下一页交给scrapy 下载
            next_urls = response.css(".next.page-numbers::attr(href)").extract_first("") # 两个class同时出现
            if next_urls:
                yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)  # 回调函数

    def parse_detail(self, response):
        # 提取文章具体字段
        # re_selector = response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")
        # re2_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1')
        # re3_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1')
        # title = response.xpath("//div[@class='entry-header']/h1[1]/text()").extract()[0].strip(" ")
        # create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace(" ·","")
        # praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        # praise_nums = int(praise_nums)
        # fav_num = re.match(r".*?(\d+).*",
        #                     response.xpath("//span[contains(@class, 'bookmark-btn ')]/text()").extract()[0])
        # if fav_num:
        #     fav_nums = fav_num.group(1)
        #
        # comment_num_ = response.xpath("//a[@href='#article-comment']/span").extract()[0]
        # comment_num = re.match(r".*?(\d+).*", comment_num_)
        # if comment_num:
        #     comment_nums = comment_num.group(1)
        # content = response.xpath("//div[@class='entry']").extract()[0]
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()[0]
        # tag_list = [elment for elment in tag_list if not elment.strip().endswith("评论")]
        # tags = "".join(tag_list)






        # css选择器提取字段
        front_image_url = response.meta.get("front_image_url", "") # 文章封面图
        title = response.css(".entry-header > h1::text").extract_first()
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace(" ·","")
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]

        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        fav_num = re.match(r".*?(\d+).*", fav_nums)
        if fav_num:
            fav_nums = int(fav_num.group(1))
        else:
            fav_nums = 0
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        comment_num = re.match(r".*?(\d+).*", comment_nums)
        if comment_num:
            comment_nums = int(comment_num.group(1))
        else:
            comment_nums = 0
        content = response.css("div.entry").extract()[0]
        tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()[0]
        tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        tags = ",".join(tag_list)
    pass
