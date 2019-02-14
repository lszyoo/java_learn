#!/user/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

url = "https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={page}"
req = requests.get(url)
jsondata = req.text
data = json.loads(jsondata)
print(data)