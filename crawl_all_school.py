#coding=utf8

import sys
import time
import urllib2
import urllib
from bs4 import BeautifulSoup

url_list = []
for i in range(134):
    num = i*20
    cur_url = 'http://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-' + str(num) + '.dhtml'
    url_list.append(cur_url)

with open("./all_school.data", "w") as fp:
    num = 0
    title = u"院校名称\t院校所在地\t院校隶属\t院校类型\t学历层次\t211院校\t985院校\t研究生院\t满意度"
    print >> fp, title.encode("utf8", "ignore")
    for url in url_list:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        html = resp.read()
        soup = BeautifulSoup(html, "html5lib")
        for table in soup.html.body.find_all('table', class_='ch-table'):
            i = 0
            for tr in table.find_all('tr'):
                if i == 0:
                    i += 1
                    continue
                if tr is None:
                    i += 1
                    continue
                #结果存储，依次是：院校名称、院校所在地、院校隶属、院校类型、学历层次、211院校、985院校、研究生院、满意度
                columns = ["" for n in range(9)]
                j = 0
                for td in tr.find_all('td'):
                    if j == 0:
                        if td.a is None:
                            columns[0] = td.text.strip()
                        else:
                            columns[0] = td.a.text.strip()
                    elif j in (1, 2, 3, 4):
                        columns[j] = td.text.strip()
                    elif j == 5:
                        school_feature = ""
                        for span in td.find_all('span'):
                            school_feature += span.text.strip() + ";"
                        if '211' in school_feature:
                            columns[5] = '1'
                        else:
                            columns[5] = '0'
                        if '985' in school_feature:
                            columns[6] = '1'
                        else:
                            columns[6] = '0'
                    elif j == 6:
                        if td.i is not None:
                            columns[7] = '1'
                        else:
                            columns[7] = '0'
                    elif j == 7:
                        if td.a is not None:
                            columns[8] = td.a.text.strip()
                        else:
                            columns[8] = '-1'
                    j += 1
                    continue
                s = "\t".join(columns)
                print >> fp, s.encode("utf8", "ignore")
        num += 1
        print >> sys.stderr, "Has Processed " + str(num)
        time.sleep(0.1)

