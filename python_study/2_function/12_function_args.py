#!/user/env/bin python3
# -*- coding: utf-8 -*-


# 位置参数

# 计算 x² 的函数
def power_2(x):
    return x * x        # x 为位置参数

# 计算 x 的 n 次幂 的函数
def power_n(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s



# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象，List 不行
# 注意：1、必选参数在前，默认参数在后，否则Python的解释器会报错；
#      2、当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# m 为默认参数
def power_m(x, m=2):
    s = 1
    while m > 0:
        m = m -1
        s = s * x
    return s

# age、city 为默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name, ',')
    print('gender:', gender, ',')
    print('age:', age, ',')
    print('city:', city)

enroll('Micheal', 'M')
enroll('Bob', 'M', 7)       # 默认参数值 按顺序给 age，city 仍为默认
enroll('Mr.Li', 'M', 19, 'Tianjin')
enroll('Adam', 'G', city='Shanghai')    # 默认参数 不按顺序给，age 仍为默认

# 避免默认参数的坑，详解见印象笔记
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L



# 可变参数
# 即 传入的参数个数是可变的，可以是任意个或 0 个

# 计算 a + b + c + ...
def calc(*numbers):         # 在函数内部，参数numbers接收到的是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

# Python允许你在 list 或 tuple 前面加一个*号
num = [2, 5, 6]
calc(*num)



# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 可只传入必选参数
person('Michael', 30)
# 可以传入任意个数的关键字参数
extra = {'city': 'Beijing', 'sex': 'M'}
person('Bob', 34, city='Beijing', sex='M')
person('Bob', 34, city=extra['city'], sex=extra['sex'])
person('Bob', 34, **extra)



# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数

# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 只能传入 city，job
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 23, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)

person1('Jack', 23, city='Beijing', job='Engineer')
person1('Jack', 23, 'man', city='Beijing', job='Engineer')

# 结合默认参数
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person2('Jack', 25, job='Teacher')



# 参数组合
# 参数定义的顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
# 输出：a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# 输出：a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'm', 'n')
# 输出：a = 1 b = 2 c = 3 args = ('m', 'n') kw = {}
f1(1, 2, 3, 'm', 'n', x=99)
# 输出：a = 1 b = 2 c = 3 args = ('m', 'n') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
# 输出：a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 传入 tuple 和 dict
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# 输出：a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
f2(*args, **kw)
# 输出：a = 1 b = 2 c = 3 d = 99 kw = {'x': '#'}
