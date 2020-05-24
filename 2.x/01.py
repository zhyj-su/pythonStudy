# -*- coding: utf-8 -*-
import urllib2
import urllib

#response = urllib2.urlopen('http://www.baidu.com')

#print response.read()

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request=urllib2.Request('http://www.baidu.com',headers = headers)

#%e8%8c%83%e7%a5%af%e5%a6%82

#print urllib2.urlopen(request).read()

wd={"wd":"范祯如"}

request=urllib2.Request("http://baidu.com?"+urllib.urlencode(wd),headers=headers)

html = urllib2.urlopen(request).read()
print html