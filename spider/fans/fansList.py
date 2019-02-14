#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
    Create by Kobe On 2019.1.8 00:02
    说明：抓取m站粉丝列表
"""
import random
import time

import requests
import json
import codecs

fansListFile = codecs.open('D:\\PyCharm\\spider\\fansList.txt', 'a', 'utf-8')
def crawlDetailPage(url, pageId):
    global fansListFile

    # 读取m站微博网页的 json 信息
    req = requests.get(url)
    jsondata = req.text
    data = json.loads(jsondata)

    # 判断本页是否有内容
    # {'ok': 0, 'data': {'msg': '这里还没有内容', 'ok': 0, 'title': '粉丝', 'cardlistInfo': {'containerid': '1005051654024040_-_FANS', 'page': 14, 'title': None}}}
    if '这里还没有内容' in data['data']['msg']:
        return

    # 获取本页每一条数据
    content = data['data']['cards']
    for fans in content:
        user = fans['user']
        fansListFile.write(str(user) + '\r\n')

user_oid = 1005051654024040
pageId = 0
while True:
    print('正在获取第{}页的粉丝列表'.format(pageId))
    url = 'https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={pageId}'.format(user_oid=user_oid, pageId=pageId)
    crawlDetailPage(url, pageId)
    pageId = pageId + 1

    # 设置休眠时间
    t = random.randint(1, 5)
    print('休眠时间：{}s'.format(t))
    time.sleep(t)



