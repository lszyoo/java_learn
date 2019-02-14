#!/user/bin/env python3
import ast
import codecs
import subprocess

import os
import urllib.request
from urllib import request

import requests
import json
req = requests.get('https://m.weibo.cn/api/container/getSecond?containerid=1005051654024040_-_FANS&page=1')
jsondata = req.text
print(jsondata)
data = json.loads(jsondata)
print(data)
if '这里还没有内容' == data['data']['msg']:
    print(data['data']['msg'])


# content = data['data']['cards']
# print(content)
# print(content[0]['user'])
# print(content[0]['user']['id'])


# import urllib.request
# url = "https://m.weibo.cn/api/container/getSecond?containerid=1005051654024040_-_FANS&page=10"
# headers = ("User-Agent","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# jsondata1 = opener.open(url).read()
# data1 = json.loads(bytes(jsondata1).decode('utf-8'))
# print(data1)

# import time
#
# def traversal_list(alist, i):
#     while True:
#         length = len(alist)
#         i = i%(length)
#         yield alist[i]
#         i += 1
#
# def traversal_list2(alist):
#     i = 0
#     f = traversal_list(alist, i)
#     while True:
#         a = next(f)
#         print(a)
#         print(i)
#         time.sleep(1)
#         i += 1
#
# while True:
#     traversal_list2(['a', 'b', 'c', 'd', 'e'])
# import time
#
# fansListFile = open('fans/fansList.txt')
#
# # 读取用户id
# i = 0
# while True:
#     line = fansListFile.readline()
#     if line == '':
#         a = 5
#         print(5)
#     if not line:
#         break
#     s = line.split('\t')[1]
#     user_oid = ast.literal_eval(s)['id']
#     # print(s)
#     print(user_oid)
#     i += 1
#     print(i)
#     time.sleep(1)



# filename = 'fans/fansList.txt'
# command = subprocess.getoutput("sed -n '2p' " + filename)
# if command == '':
#     print(1)
# # os.system(command)
# print(command)


# print('1005051654024040'[6:])
# if subprocess.getoutput("sed -n '1p' fans/fans.txt") == '':  # user_oid 初始化
#     print(1)

#
# url = 'https://m.weibo.cn/api/container/getSecond?containerid=1005055132048979_-_FANS&page=4'
# #定义代理ip
# proxy_addr="122.241.72.191:808"
# #创建一个请求
# req=urllib.request.Request(url)
# #添加headers
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)")
# #设置代理
# proxy=urllib.request.ProxyHandler({"http":proxy_addr})
# #创建一个opener
# opener=urllib.request.build_opener(proxy,urllib.request.ProxyBasicAuthHandler())
# #将opener安装为全局
# urllib.request.install_opener(opener)
# #用urlopen打开网页
# jsondata=urllib.request.urlopen(req).read().decode('utf-8','ignore')
# data = json.loads(jsondata)
#
# print(data)

# userid = codecs.open('/Users/gengmei/PycharmProjects/spider/fans/userid.txt')
# l = userid.readlines()
# print(l)
# for i in range(0, len(l)):
#     li = l[i].strip('\n')
#     print(li)


# # #访问网址
# while True:
#     url = 'https://m.weibo.cn/api/container/getSecond?containerid=1005051654024040_-_FANS&page=13'
#     #这是代理IP
#     proxy = {'http':'106.46.136.112:808'}
#     #创建ProxyHandler
#     proxy_support = request.ProxyHandler(proxy)
#     #创建Opener
#     opener = request.build_opener(proxy_support)
#     #添加User Angent
#     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#     #安装OPener
#     request.install_opener(opener)
#     #使用自己安装好的Opener
#     response = request.urlopen(url)
#     #读取相应信息并解码
#     html = response.read().decode("utf-8")
#     #打印信息
#     print(html)