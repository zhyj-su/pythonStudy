# -*- coding: utf-8 -*-

import urllib
import urllib2

url = "http://tieba.baidu.com/f?"

keyword = raw_input("please input keyword:")
page = input("请输入要查询的页码数目:")

kw = {"kw":keyword}

records= (page-1)*50
if page>1:
    full_url = url+urllib.urlencode(kw)+"&pn="+str(records)
else:
    full_url = url+urllib.urlencode(kw)

headers={
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

print full_url

request = urllib2.Request(full_url,headers=headers)

response = urllib2.urlopen(request)

html = response.read()

f=open('1.html','w')
f.write(html)
f.close()
