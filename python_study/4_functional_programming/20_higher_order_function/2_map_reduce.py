#!/user/bin/env python3
#-*- coding: utf-8 -*-

from collections.abc import Iterator

# map

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, list(range(10)))
print(isinstance(r, Iterator))
# 输出：True
print(list(r))
# 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 把list所有数字转为字符串
print(list(map(str, list(range(10)))))
# 输出：['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



# reduce

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add(x, y):
    return x + y

sum([x for x in range(10) if x % 2 == 1])
print(reduce(add, [x for x in range(10) if x % 2 == 1]))
# 输出：25

# 13579
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))
# 输出：13579


# 将 str 转换为 int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))
# 输出：13579

# 整理成一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))
# 输出：13579

# 使用 lambda 简化
def char2num(s):
    return DIGITS[s]

def str3int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str3int('13579'))
# 输出：13579

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.capitalize()

print(list(map(normalize, ['lisa', 'ADAM', 'mArry'])))
# 输出：['Lisa', 'Adam', 'Marry']


# 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def fm(x, y):
        return x * y
    return reduce(fm, L)

print(prod([1, 2, 3]))
# 输出：6


# 把字符串 '123.456' 转换成浮点数 123.456
DIGITS1 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
def str2float(s):
    def integer(x, y):
        return x * 10 + y
    def decimals(x, y):
        return x * 0.1 + y
    def char2num(s):
        return DIGITS1[s]
    A = s.split('.')
    return reduce(integer, map(char2num, A[0])) + reduce(decimals, map(char2num, A[1][::-1])) / 10

print(str2float('123.456'))