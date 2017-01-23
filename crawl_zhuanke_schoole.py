#coding=utf8

import sys
import time
import urllib2
import urllib
from bs4 import BeautifulSoup

url_list = []
for i in range(58):
    num = i*20
    cur_url = 'http://gaokao.chsi.com.cn/sch/search--bxlx-14,searchType-1,start-' + str(num) + '.dhtml'
    url_list.append(cur_url)

with open("./zhiyejishu_xuexiao.data", "w") as fp:
    for url in url_list:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        html = resp.read()
        soup = BeautifulSoup(html)
        i = 0
        for tr in soup.html.body.find_all('table')[3].find_all('tr'):
            if i == 0:
                i += 1
                continue
            if tr is None:
                continue
            if tr.td is None:
                continue
            if tr.td.a is None:
                continue
            if tr.td.a.text is None:
                continue
            print >> fp, tr.td.a.text.encode("utf8", "ignore")
            i += 1
        time.sleep(1)


url_list = []
for i in range(9):
    num = i*20
    cur_url = 'http://gaokao.chsi.com.cn/sch/search--bxlx-13,searchType-1,start-' + str(num) + '.dhtml'
    url_list.append(cur_url)

with open("./gaodengzhuanke_xuexiao.data", "w") as fp:
    for url in url_list:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        html = resp.read()
        soup = BeautifulSoup(html)
        i = 0
        for tr in soup.html.body.find_all('table')[3].find_all('tr'):
            if i == 0:
                i += 1
                continue
            if tr is None:
                continue
            if tr.td is None:
                continue
            if tr.td.a is None:
                continue
            if tr.td.a.text is None:
                continue
            print >> fp, tr.td.a.text.encode("utf8", "ignore")
            i += 1
        time.sleep(1)


print >> sys.stderr, "haha"
print >> sys.stderr, "fuck1"
