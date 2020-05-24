# -*- coding: utf-8 -*-

import urllib
import urllib2

url = "http://baidu.com/s?"

keyword = raw_input("请输入要查询的关键词:")

wd = {"wd":keyword}

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(url+urllib.urlencode(wd),headers=headers)
response = urllib2.urlopen(request)
print response.read()