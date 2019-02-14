#!/user/bin/env python3

# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 返回 Iterator 对象

# list 中只保留奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, list(range(10)))))
# 输出：[1, 3, 5, 7, 9]


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()     # stripe() 函数只能去除首尾空格

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# 输出：['A', 'B', 'C']



# 用filter求素数

# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 5, 7, 9, 11, 13, 15, 17, 19, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 7, 11, 13, 17, 19, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 11, 13, 17, 19, ...
# 不断筛下去，就可以得到所有的素数

# 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()     # 初始序列
    while True:
        n = next(it)     # 返回序列的第一个数
        yield n
        it = filter(_not_divisible, it)     # 构造新序列

for n in primes():
    if n < 1000:
        print(n, end=',')
    else:
        break
# 输出：2,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,...

print()


# 利用filter()筛选出回数

# 生成数列
def num():
    n = 1
    while True:
        n = n + 1
        yield n

# 定义一个筛选函数
def f(n):
    return n == int(str(n)[::-1])

# 定义一个生成器，不断返回回数
def is_palindrome():
    it = num()
    while True:
        n = next(it)
        yield n
        it = filter(f, it)

for n in is_palindrome():
    if n < 1000:
        print(n, end=',')
    else:
        break

# 输出：2,3,4, ... ,989,999,