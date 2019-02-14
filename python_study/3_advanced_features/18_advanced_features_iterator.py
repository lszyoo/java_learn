#!/user/bin/env python3
#-*- coding: utf-8 -*-

# for 循环支持类型：（1）list、tuple、dict、set、str -> Iterable （2）generator -> Iterator
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以for循环、被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections.abc import Iterator   # from collections import Iterator 已过时
from collections.abc import Iterable   # from collections import Iterator 已过时

print(isinstance((x for x in range(10)), Iterator))
# 输出：True
print(isinstance([], Iterator))
# 输出：False


# Iterable -> Iterator
# 类型是Iterator就一定是Iterable，反之不一定，如生成器
print(isinstance(iter([]), Iterator))
# 输出：True
print(isinstance(iter([]), Iterable))
# 输出：True


# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。