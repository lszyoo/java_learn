#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 通常，求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 4, 5)
print(f)
# 输出：<function lazy_sum.<locals>.sum at 0x10d979268>

print(f.__code__)
# <code object sum at 0x103234ed0, file "/Users/gengmei/PycharmProjects/python_study/4_functional_programming/21_return_function.py", line 14>

print(f())
# 输出：13


# 在上边例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
# f1, f2 = lazy_sum(1, 3, 4, 5)       # TypeError: 'function' object is not iterable
f2 = lazy_sum(1, 3, 4, 5)
print(f == f2)
# 输出：False

# f()和f2()的调用结果互不影响。



# 闭包

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)       # list 里保存的是 f 函数的逻辑，外层循环结束才开始执行 f 的逻辑
    return fs

f1, f2, f3 = count()       # list 可以这样赋值
print(f1(), f2(), f3())
# 输出：9 9 9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
fnn = count()
print(fnn[0]())
# 输出：9

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 对比，缺点是代码较长，可利用lambda函数缩短代码。
def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))         # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count1()

print(f1(), f2(), f3())
# 输出：1 4 9


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    i = 0
    def counter():
        nonlocal i      # nonlocal适用于嵌套函数中内部函数修改外部变量的值
        i += 1
        return i
    return counter

ct = createCounter()
print(ct(), ct())
# 输出：1 2