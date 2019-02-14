#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
    Create by Kobe On 2019.1.8 00:02
    说明：抓取m站粉丝列表
"""
import ast
import http.client
import random
import subprocess
import time
import urllib.request
import urllib.error

import json
import codecs

from urllib import request


# python3 http.client bug：时不时报异常 -- IncompleteRead，强行指定 HTTP/1.0
# http.client.HTTPConnection._http_vsn = 10
# http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

# 浏览器列表
browsers = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4763.400',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'
            'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
            'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
            ]

# 代理 ip 池
ip_proxies = [{'HTTP':'125.46.0.62:53281'},
              {'HTTPS':'219.159.38.208:56210'},
              {'HTTP':'112.95.224.58:8118'},
              {'HTTPS':'222.220.99.112:8118'},
              {'HTTPS':'222.221.11.119:3128'},
              {'HTTPS':'219.159.38.204:56210'},
              {'HTTP':'182.18.13.149:53281'},
              {'HTTP':'58.17.125.215:53281'},
              {'HTTP':'220.180.50.14:5328'},
              {'HTTP':'124.207.82.166:8008'},
              {'HTTPS':'203.86.26.9:3128'},
              {'HTTPS':'180.168.198.141:18118'},
              {'HTTPS':'180.169.186.155:1080'}
              ]

# 该 user_oid 所有粉丝列表
def fans(user_oid):
    pageId = 1
    pageIds = []
    count = 0
    while count <= 5 & pageId <=5:
        print('正在获取第{}页的粉丝列表'.format(pageId))
        url = 'https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={pageId}'.format(user_oid=user_oid, pageId=pageId)
        # 无限循环浏览器列表
        browser = next(traversal_list(browsers, pageId))
        # try:
        data = crawlDetailPage(url, browser, user_oid)
        # except urllib.error.HTTPError as e:
        #     print('urllib.error.HTTPError: HTTP Error 418')

        # 如果连续5页以上没有内容则结束循环
        if '这里还没有内容' == data['data']['msg']:
            pageIds.append(pageId)
            if len(pageIds) >= 5:
                for i in range(1, len(pageIds)):
                    if pageIds[i] - pageIds[i - 1]:
                        count += 1

        # 过滤粉丝数超过 1000000 的用户
        else:
            if data['data']['count'] > 1000000 or pageId == data['data']['maxPage']:
                break

        pageId = pageId + 1

        # 设置休眠时间
        t = random.choice([0.2, 0.3])
        print('休眠时间：{}s'.format(t))
        time.sleep(t)


# 获取该 user_oid 本页粉丝列表
def crawlDetailPage(url, browser, user_oid):
    global jsondata
    # 创建一个可写的文件对象
    fansListFile = codecs.open('/Users/gengmei/PycharmProjects/spider/fans/fans.txt', 'a', 'utf-8')
    # 读取m站微博网页的 json 信息
    # 第一种方式
    # headers = ('User-Agent', browser)
    # opener = urllib.request.build_opener()
    # opener.addheaders = [headers]
    # jsondata = opener.open(url).read()
    # 第二种方式
    # req = urllib.request.Request(url, headers)
    # jsondata = urllib.request.urlopen(req).read()

    # data = json.loads(bytes(jsondata).decode('utf-8'))

    # 第三种方式
    # 创建一个请求
    jsondata = ''
    req = urllib.request.Request(url)
    while jsondata == '':
        # 添加headers
        req.add_header('User-Agent', browser)
        # 设置代理
        proxy = urllib.request.ProxyHandler(random.choice(ip_proxies))
        # 创建一个opener
        opener = urllib.request.build_opener(proxy, urllib.request.ProxyBasicAuthHandler())
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        # 用urlopen打开网页
        try:
            jsondata = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        except urllib.error.HTTPError as e:
            print('urllib.error.HTTPError: HTTP Error 418')
            time.sleep(5)

    # 解析json
    data = json.loads(jsondata)

    # # 第四种方式
    # # 创建ProxyHandler
    # proxy_support = request.ProxyHandler(random.choice(ip_proxies))
    # # 创建Opener
    # opener = request.build_opener(proxy_support)
    # # 添加User Angent
    # opener.addheaders = [('User-Agent', browser)]
    # # 安装OPener
    # request.install_opener(opener)
    # # 使用自己安装好的Opener
    # response = request.urlopen(url)
    # # 读取相应信息并解码
    # jsondata = response.read().decode("utf-8")
    # # 解析json
    # data = json.loads(jsondata)

    # 判断本页是否有内容
    # {'ok': 0, 'data': {'msg': '这里还没有内容', 'ok': 0, 'title': '粉丝', 'cardlistInfo': {'containerid': '1005051654024040_-_FANS', 'page': 14, 'title': None}}}
    if '这里还没有内容' == data['data']['msg']:
        return data             # 此处必须返回 data，否则调用方法时，if条件句会出错

    # 过滤粉丝数超过 1000000 的用户
    if data['data']['count'] > 1000000:
        return data

    # 获取本页每一条数据
    content = data['data']['cards']
    try:
        for fans in content:
            user_id = str(user_oid)[6:] + '\t' + str(fans['user']['id'])
            # line = str(user_oid) + '\t' + str(user)
            fansListFile.write(user_id + '\r\n')
    finally:
        if fansListFile:
            fansListFile.close()    # 释放资源
    return data


# 浏览器的列表生成式
def traversal_list(alist, i):
    while True:
        length = len(alist)
        i = i % length
        yield alist[i]
        i += 1

# 用户 id 列表，用于去重爬取
user_set = set()

# 读取用户id
filename = '/Users/gengmei/PycharmProjects/spider/fans/fans.txt'

# 储存用户id
useridFile = codecs.open('/Users/gengmei/PycharmProjects/spider/fans/userid.txt', 'a+', 'utf-8')
# 读取文件所有内容
userids = useridFile.readlines()
for i in range(0, len(userids)):
    # 去除每个元素的换行符
    userid = userids[i].strip('\n')
    user_set.add(userid)

# 表示第几行
p = 0

while True:
    if subprocess.getoutput("sed -n '1p' " + filename) == '':   # user_oid 初始化
        print('读取文件第 0 行')
        user_oid = 1005051654024040
    else:
        p += 1
        print('读到文件第 {} 行'.format(p))
        line = subprocess.getoutput("sed -n '{}p' ".format(p) + filename)   # 获取第p行
        if line == '':          # 最后一行结束
            break
        else:
            id = line.split('\t')[1]
            # id = str(ast.literal_eval(s)['id'])
            if id not in user_set:
                user_oid = '100505' + id
            else:
                continue

    user_set.add(str(user_oid)[6:])
    useridFile.write(str(user_oid)[6:] + '\n')
    # try:
    fans(user_oid)
    # except urllib.error.HTTPError as e:
    #     print('urllib.error.HTTPError: HTTP Error 418')
    if len(user_set) == 1000000:
        useridFile.close()
        break
