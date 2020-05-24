import urllib2

http_handler = urllib2.HTTPHandler()

#http_handler = urllib2.HTTPSHandler()

request = urllib2.Request("http://www.baidu.com")

opener = urllib2.build_opener(http_handler)

response = opener.open(request)

print response.read()