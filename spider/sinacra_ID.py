#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created On 20190107
    Author: Kobe
    微博用户列表爬虫
"""

import requests
import json
import time
import random
import re
import codecs

infofile = codecs.open("SinaWeibo_List.txt", 'a', 'utf-8')

def crawlDetailPage(url,page):
    global ID_get
    global num
    global infofile
    #读取微博网页的JSON信息
    req = requests.get(url)
    jsondata = req.text
    data = json.loads(jsondata)
    #获取每一条页的数据
    # print(data)
    content = data['data']['cards']
    print(content)
    #循环输出每一页的关注者各项信息
    for i in content:
        followingId = i['user']['id']
        ID_get.append(followingId)
        num=num+1
        infofile.write(str(followingId)+ '\r\n')

# def get_user_info(user_id):   #containerid和usid不一致，查看用户的关注列表需要他的containerid，usid用于获取用户主页信息
#     url = 'http://m.weibo.cn/api/container/getIndex?type=uid&value={user_id}'.format(user_id=user_id)
#     resp = requests.get(url)
#     jsondata = resp.json()
#     jsondata = jsondata['data']
#     fans_id=jsondata.get('follow_scheme')
#     items = re.findall(r"&lfid=(\w+)*", fans_id, re.M)
#     for i in items:
#          i=i.encode(encoding='UTF-8',errors='strict')
#     return i

user_oid=1005051654024040      #这个是我自己的微博 containerid,在个人主页点我的微博得到的链接里的数字，也可以换成你自己的

for cir in range(1,20):
    print("正在获取第{}位用户的粉丝信息:".format(cir))
    num = 0;
    ID_get = [];
    while True:
        i = 0
        print("正在获取第{}页的粉丝列表:".format(i))
        # 微博用户关注列表JSON链接
        url = "https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={page}".format(user_oid=user_oid, page=i)  # page=" +   #FOLOWERS关注，FANS粉丝
        crawlDetailPage(url, i)
        i = i + 1
        # 设置休眠时间
        t = random.randint(1, 5)
        print("休眠时间为:{}s".format(t))
        time.sleep(t)
    user_id = ID_get[1]
    user_oid = get_user_info(str(user_id))
