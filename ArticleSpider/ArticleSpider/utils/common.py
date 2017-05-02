#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/2 12:03
# Author: zhourudong
import hashlib


def get_md5(url):
    if isinstance(url, str):
        # 如果是Unicode
        url = url.encode("utf-8")

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print(get_md5("https://www.baidu.com".encode("utf-8")))
