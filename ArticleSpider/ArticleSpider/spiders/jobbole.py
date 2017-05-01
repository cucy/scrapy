# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        """ 
            路径分析 title
            xpath 索引从1开始
            html下的body下第三个div下的第三个div
            /html/body/div[3]/div[3]/div[1]/div[1]/h1
            /html/body/div[3]/div[3]/div[1]/div[1]/h1
        """
        re_selector = response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")
        re2_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1')
        re3_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1')
        title = response.xpath("//div[@class='entry-header']/h1[1]/text()").extract()[0].strip(" ")
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace(" ·","")
        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        praise_nums = int(praise_nums)
        fav_num = re.match(r".*?(\d+).*",
                            response.xpath("//span[contains(@class, 'bookmark-btn ')]/text()").extract()[0])
        if fav_num:
            fav_nums = fav_num.group(1)

        comment_num_ = response.xpath("//a[@href='#article-comment']/span").extract()[0]
        comment_num = re.match(r".*?(\d+).*", comment_num_)
        if comment_num:
            comment_nums = comment_num.group(1)
        content = response.xpath("//div[@class='entry']").extract()[0]
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()[0]
        tag_list = [elment for elment in tag_list if not elment.strip().endswith("评论")]
        tags = "".join(tag_list)






        # css选择器提取字段
        title = response.css(".entry-header > h1::text").extract_first()
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace(" ·","")
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]

        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        fav_num = re.match(r".*?(\d+).*", fav_nums)
        if fav_num:
            fav_nums = fav_num.group(1)
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        comment_num = re.match(r".*?(\d+).*", comment_nums)
        if comment_num:
            comment_nums = comment_num.group(1)
        content = response.css("div.entry").extract()[0]
        tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()[0]
        tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        tags = "".join(tag_list)
        pass
