#!/user/bin/env python3
# -*- coding: utf-8 -*-

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的 elif 和 else

# 标准输入 返回值是 string
s = input('birth: ')
# 强转
birth = int(s)
if birth < 1980:
    print('80前')
elif birth >= 1980 & birth < 1990:
    print('80后')
elif birth >= 1990 & birth < 2000:
    print('90后')
else:
    print('00后')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if birth:
    print('True')
# 输出：True
if not birth:
    print('False')
# 没有输出