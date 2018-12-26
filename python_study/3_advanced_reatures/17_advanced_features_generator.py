#!/user/bin/env python3
#-*- coding: utf-8 -*-


# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可
# 以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 两种方式：（1）[] -> () （2）函数中有 yield 关键字

# list
L = [x * x for x in range(10)]
print(L)
# 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# generator
g = (x * x for x in range(10))
print(g)
# 输出：<generator object <genexpr> at 0x10ec06930>

# generator保存的是算法，每次调用next(g)
print(next(g))      # 输出：0
print(next(g))      # 输出：1

for n in g:
    print(n, end=' ')
# 输出：4 9 16 25 36 49 64 81
print()


# 斐波拉契数列：1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# 普通方法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 生成器
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b         # 此处是唯一区别
        a, b = b, a + b
        n = n + 1
    return 'done'

# 最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# generator函数的“调用”实际返回一个generator对象

for n in fib1(6):
    print(n, end=' ')
# 输出：1 1 2 3 5 8
print()

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib1(6)
while True:
    try:
        x = next(g)              # 此处 g 不能替换成 fib1(6)，否则每次循环调用一次 fib1(6)，x 只会等于 1
        print('g:', x, end=' ')  # 输出：g: 1 g: 1 g: 2 g: 3 g: 5 g: 8
    except StopIteration as e:
        print()
        print('Generator return value:', e.value)   # 输出：Generator return value: done
        break



# 杨辉三角
# yield 相当于 return，只是再次执行时从上次返回的yield语句处继续执行，while True 后的循环外边不接return，因为永远循环走不到外边
def triangles():
    b = [1]
    while True:
        yield b
        n = 0
        a = []
        for i in b:
            a.append(n+i)
            n = i
        a.append(1)
        b = a

# 测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')