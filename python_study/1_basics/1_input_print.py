#!/user/bin/env python3
# -*- coding: utf-8 -*-


# print

# 单个字符串输出
print('Hello World!')
# 输出：Hello World!

# 多个字符串输出
# 遇到逗号，输出空格
print('Today','is','okay!')
# 输出：today is okay!


# input

# 标准输入返回值是 string
name = input()
print('Hello', name)
# 输出：Hello Liu

name = input('please enter your name: ')
print(name)
# 输出：Liu

# 输出不换行
# from __future__ import print_function 必须放到代码前面，可加可不加
print('hello', end = ' ')
print('world', end = '')
