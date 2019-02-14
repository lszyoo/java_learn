#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 迭代
# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上，如：dict、string
# 只要是可迭代对象，无论有无下标，都可以迭代

d = {'a': 1, 'b': 2, 'c': 3}
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样

# 遍历 key
for key in d:
    print(key, end=' ')
# 输出：a b c
print()     # 换行

# 遍历 value
for value in d.values():
    print(value, end=' ')
# 输出：1 2 3
print()

# 同时遍历 key 和 value
for kv in d.items():
    print(kv, end=' ')
# 输出：('a', 1) ('b', 2) ('c', 3)
print()


str = 'ABCD'
for ch in str:
    print(ch, end=' ')
# 输出：A B C D
print()


# 判断是否为可迭代对象 --- 方法是通过collections模块的Iterable类型判断
from collections.abc import Iterable

print(isinstance(123, Iterable))
# 输出：False
print(isinstance('abc', Iterable))
# 输出：True


# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value, end=',')
# 输出：0 A,1 B,2 C,
print()



# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L==[]:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i>max:
                max=i
            if i<min:
                min=i
        return (min, max)

print(findMinAndMax([1, 2, 3, 6, 4]))

min([1, 2, 3])
max([1, 2, 3])


