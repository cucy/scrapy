# -*- coding: utf-8 -*-
import re
import json
import datetime

try:
    import urlparse as parse
except:
    from urllib import parse

import scrapy
from scrapy.loader import ItemLoader


# from items import ZhihuQuestionItem, ZhihuAnswerItem

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    # 头部
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    def parse(self, response):
        pass

    def start_requests(self):
        # 获取xsrf参数 传给login 使用回调函数
        return [scrapy.Request("https://www.zhihu.com/#signin", headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        # re.DOTALL匹配全文 默认是匹配一行
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf = (match_obj.group(1))

        post_url = "https://www.zhihu.com/login/phone_num"
        if xsrf:
            post_data = {
                "_xsrf": xsrf,
                "phone_num": '18519509255',
                "password": '181171aa',
                "captcha": '',
            }
            import time
            t = str(int(time.time() * 1000))
            captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
            yield scrapy.Request(captcha_url, meta={"post_data": post_data}, headers=self.headers,
                                 callback=self.login_after_captcha)

    def login_after_captcha(self, response):

        # 保存验证码图片
        with open("captcha.jpg", 'wb') as f:
            f.write(response.body)
            f.close()

        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except Exception as e:
            print(e)
            pass
        captcha = input("输入验证码\n>")

        post_data = response.meta.get("post_data", {})
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data["captcha"] = captcha

        return [scrapy.FormRequest(
            # FormRequest可以进行表单的提交
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login,
        )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功(验证是否登录成功)
        text_json = json.loads(response.text)
        if "msg" in text_json and text_json["msg"] == "登录成功":
            # 登录成功后 延后执行
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)
