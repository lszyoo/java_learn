#!/usr/bin/env python3
# -*- encoding -*-

from collections import Iterable,Iterator
import os

# 切片

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)


L = ['Lisa', 'Bob', 'Jenny', 'Sarah']
# 取前n个元素（切片）
print(L[0], L[1], L[2])

r = []
for i in range(3):
    r.append(L[i])
print(r)

print(L[0:4])
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略
print(L[:2])

print(L[1:2])

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片,记住倒数第一个元素的索引是-1。
print(L[-2:-1])


l = list(range(100))
print(l)
# 前10个数
print(l[:10])
# 后10个数
print(l[-10:])
# 前11-20个数
print(l[10:20])
# 前10个数，每两个取一个
print(l[:10:2])
# 所有数，每5个取一个
print(l[::5])
# 只写[:]就可以原样复制一个list
print(l[:])


# tuple  也可用切片(tuple也是一种list),返回仍是tuple
t = (1, 3, 5, 7, 9)
print(t[:3])


# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。切片后仍是 字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::3])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if not isinstance(s, str):
        raise TypeError('%s: is not a string' %s)
    elif len(s) == 0:
        return 'empty input!'
    else:
        a = s[0]
        b = s[-1]
        while a == ' ':
            s = s[1:]
            a = s[0]            # 只要字符串前边有空格就一直循环
        while b == ' ':
            s = s[:-1]
            b = s[-1]
        print(s)


trim('   hello world   ')
print(trim(''))


# 迭代
# python 中不管有无坐标，都可以迭代

# dict迭代
dict = {'a': 1, 'b': 2, 'c': 3}
for key in dict:                # 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
    print(key)                  # 输出：b c a

for value in dict.values():
    print(value)

for k, v in dict.items():
    print(k, v)

# 字符串 迭代
for ch in 'AB':
    print(ch)

# 判断是否为可迭代对象
if isinstance(12, Iterable):
    print('整数', 'yes')
if isinstance('acv', Iterable):
    print('str', 'yes')

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate('WXYZ'):
    print(i, value)

for x, y in [(1,2), (2, 3), (3, 6)]:
    print(x, y)


# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) <= 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for x in L[1:]:
            if x < min:
                min = x
            if x > max:
                max = x
        return (min, max)


print(findMinAndMax([2, -3, 34, 23, 12]))


def g():
    yield 1
    yield 2
    yield 3

print(g().__next__())   # 遍历函数----？
for i in g():           # 迭代函数里的值
    print(i)
print('Iterable? [1, 2, 3]', isinstance([1, 2, 3], Iterable))       # True
print('Iterable? \'abc\'', isinstance('abc', Iterable))     # True
print('Iterable? 123:', isinstance(123, Iterable))      # False
print('Iterable? g():', isinstance(g(), Iterable))      # True

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))      # False
print('Iterator? iter[1, 2, 3]:', isinstance(iter([1, 2, 3]), Iterator))        # True
print('Iterator? \'abc\':', isinstance('abc', Iterator))        # False
print('Iterator? 123:', isinstance(123, Iterator))      # False
print('Iterator? g():', isinstance(g(), Iterator))      # True


# iter list
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter[1, 2, 3, 4, 5]:')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


d = {'a': 1, 'b': 2, 'c': 3}

# iter each key
print('iter key:', d)
for k in d.keys():
    print('key', k)

# iter each value
print('iter value:', d)
for v in d.values():
    print('value', v)

print('iter item:', d)
for item in d.items():
    print('item', k , v)
    print('item', item)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\'])')
for k, v in enumerate(['A', 'B', 'C']):           # 索引从零开始
    print(k, v)

# iter complex list:
print('iter [(1, 2), (2, 4), (3, 9), (4, 8)]:')
for x, y in [(1, 2), (2, 4), (3, 9), (4, 8)]:
    print(x, y)


# 列表生成式

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 上边繁琐，使用列表生成式
print([x * x for x in range(1, 11)])
# 添加判断句
print([x * x for x in range(1, 11) if x % 2 ==0])
# 两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量
d = {'A': 'x', 'B': 'y', 'C': 'z'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'Python']
print([s.lower() for s in L])
L = ['Hello', 'World', 18, 'Python']
print([s.lower() for s in L if isinstance(s, str)])


# 生成器

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

L = [x * x for x in range(10)]      # 列表生成式
g = (x * x for x in range(10))      # 生成器

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，
# 抛出StopIteration的错误。但几乎不用next()遍历，直接用for循环

for n in g:
    print(n)
