# _*_ coding:utf8 _*_
__date__ = '2017/4/25 23:12'
__author__ = 'zrd'

""" 手动创建main文件可以进行单步调试"""

from scrapy.cmdline import execute
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
# execute(["scrapy", "crawl", "lagou"])
