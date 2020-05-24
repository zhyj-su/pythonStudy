# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import MySQLdb
import time
import chardet
import sys
import io

#数据库连接
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='lart',
        charset = 'utf8'
        )

cur = conn.cursor()

#header
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

#访问url
url = "https://api.lovelive.tools/api/SweetNothings/WebSite/1"


while True:
        print "start get data"
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        jsonStr = response.read()
        data = json.loads(jsonStr)[0]
        dataId = data['id']
        #.encode("GBK", 'ignore')
        content = data['content'].replace(u'\u200b','')
        likeCount = data['likeCount']
        dislikeCount = data['dislikeCount']
        dataType = data['type']
        print "id:"+dataId
        print "content:"+content

        
        #判断数据库中是否已经有本条数据
        querySql="""
        SELECT count(*) From data where id = %s
        """

        try:
                cur.execute(querySql,(dataId,))
                row=cur.fetchone()[0]

                if row>0:
                        print "has exist"
                        time.sleep(5)
                        continue
                else:
                        sql = "INSERT INTO `data` (`id`,`content`,`likeCount`,`dislikeCount`,`type`) VALUES ('%s','%s','%s','%s','%s')" % \
                        (dataId,content,likeCount,dislikeCount,dataType) 

                        try:
                                cur.execute(sql)
                                conn.commit()
                        except:
                                conn.rollback()

                        #睡眠
                        print "sleep start"
                        time.sleep(6)
                        print "sleep end"
        except:
                conn.rollback()
        
        
#关闭数据库连接
conn.close()

