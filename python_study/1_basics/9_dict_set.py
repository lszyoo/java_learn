#!/user/ben/env python3
# -*- coding: utf-8 -*-


# dict 相当于 map

# 为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，
# 一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
# 第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。
# 无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

# dict 一对多，key唯一，value可不唯一
# dict 的 key 必须是 不可变的对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
# 那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。list 不能作为key

# 和list比较，dict有以下几个特点：
#   查找和插入的速度极快，不会随着key的增加而变慢；
#   需要占用大量的内存，内存浪费多。
# 而list相反：
#   查找和插入的时间随着元素的增加而增加；
#   占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# set 和 dict 唯一区别仅在于没有存储对应的value，原理一样，都不能放入可变对象，如：list

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 输出：95

# 通过 key 添加元素，dict内部存放的顺序和key放入的顺序是没有关系的
d['Adam'] = 67
print(d['Adam'])

# print(d['Thomas']) 报错不存在该元素，如下判断
print('Thomas' in d)
# 输出：False
print(d.get('Thomas'))
# 输出：None
print(d.get('Thomas', -1))
# 输出：-1
print(d.get('Adam'))
# 输出：67

# 删除元素
d.pop('Bob')
print(d)
# 输出：{'Michael': 95, 'Adam': 67, 'Tracy': 85}


# set

# key 不重复
s1 = {1, 2, 1, 2}
s2 = set([4, 5, 4, 3])
print(s1)
# 输出：{1, 2}
print(s2)
# 输出：{3, 4, 5}

# 添加元素
s1.add(3)
print(s1)
# 输出：{1, 2, 3}

# 删除元素
s1.remove(2)
print(s1)
# 输出：{1, 3}

# 交集
print(s1 & s2)
# 输出：{3}

# 并集
print(s1 | s2)
# 输出：{1, 3, 4, 5}


print({(1, 2, 3): 1, 'abc': 2})
# 输出：{'abc': 2, (1, 2, 3): 1}
# print({(1, 2, [2, 3]), 4}) 报错

