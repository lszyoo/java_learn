#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# abs() 绝对值函数
print(abs(-10))

# max() 最大值
print(max(1, 2, 5))

# min() 最小值
print(min(1, 2, 3))

# sum() 求和
print(sum([1, 2, 3, 4]))

# 数据类型转换
int(12.3)  # 转换成整数
int('12')

float(12)  # 12.0 转换成小数

str(12)  # 转换成字符串

bool(2)  # True
bool(1)  # True
bool(0)  # False
bool('')  # False

# 函数别名
a = abs
print(a(-1))

# hex() 十进制转换成十六进制
hex(16)  # 0x10


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x  # 下边空两行


print(my_abs(-300))

from abstest import my1_abs

print(my1_abs(-111))

age = 0
if age >= 18:
    pass


def pop():  # 空函数，pass让代码能运行，否则报错
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，
# Python的函数返回多值其实就是返回一个tuple
print(move(0, 0, 5, math.pi / 2))

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。


def quadratic(a, b, c):
    if math.pow(b, 2) - 4 * a * c < 0:
        raise ValueError('math domain error')
    x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    return x1, x2


# print(quadratic(1, math.sqrt(12), 3))
m = math.sqrt(12)                # 开方后小数点后保留15位
print(math.pow(m, 2))            # 平方后不等于12
print(quadratic(2, 3, 1))


# 函数的参数

# 位置参数 和 默认参数
def power(x):                     # 平方
    return x * x


print(power(3))


def power(x, n):                  # n 次方,下面再次调用power(x)会报错
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))              # 按顺序传参
print(power(n=2, x=4))          # 不按顺序传参

def power(x, n=2):                  # n 次方,增加默认参数，即使删掉上边函数power(x)，下面再次调用power(x)就不会报错了
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。


# 可变参数：传入的参数的个数是可变的
# 计算 a² + b² + ...
def calc1(numbers):            # 表示一个参数
    sum = 0
    for n in numbers:
        sum = sum + math.pow(n, 2)
    return sum


print(calc1([1, 2, 3]))          # 先组装一个list
print(calc1((1, 2, 3)))          # 先组装一个tuple


def calc2(*numbers):             # 表示多个参数，可以是0个
    sum = 0
    for n in numbers:
        sum = sum + math.pow(n, 2)
    return sum


print(calc2(1, 2, 3, 4))
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

nums = [1, 2]
print(calc2(nums[0], nums[1]))
print(calc2(*nums))


# 关键字参数
# 作用：扩展函数的功能
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)       # 只传入必选参数
person('Ada', 45, gender='M', job='Engineer')        # 传入任意关键字参数

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jenny', 18, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def person1(name, age, **kw):
    if 'city' in kw:        # 有city参数
        pass
    if 'job' in kw:         # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person1('Jack', 24, city='Beijjing', addr='Chaoyang', zipcode='000001')           # 调用者仍可以传入不受限制的关键字参数

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数,其它参数报错。这种方式定义的函数如下：

def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jackson', 28, city='NewYork', job='Player')            # 只能这么调用，加上参数名，否则报错
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person2()函数仅接受2个位置参数。

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错

# 命名关键字参数可以有缺省值
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
person3('Lily', 23, job='Teacher')                    # job = 'Teacher' 中间没空格

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person4(name, age, *args, city, job):
    print(name, age, args, city, job)


person4('Tonny', 16, 'happy', 'beauty', city='Beijing', job='Teacher')

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过一个tuple和一个dict也可调用上边函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '12$'}
f1(*args, **kw)         # a = 1 b = 2 c = 3 args = (4,) kw = {'x': '12$', 'd': 99}
args = (1, 2, 3)
f2(*args, **kw)

# 乘法
def product(*nums):
    if len(nums) < 2:
        print('参数个数不能小于2.')
    else:
        p = 1
        for z in nums:
            p = p * z
        print(p)


product(1, 2)


def hello(greeting, *args):
    if len(args) == 0:
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ','.join(args)))


hello('Hi')                                         # Hi!
hello('Hi', 'Sarah')                                # Hi, Sarah!
hello('Hi', 'Michael', 'Bob', 'Adam')               # Hi, Michael,Bob,Adam!

names = ['Bart', 'Lisa']
hello('hello', *names)


def print_scores(**kw):
    print('      Name   Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s, %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77             # 最后加不加 逗号 都可以
}
print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('-----------------')
    print('   Name %s' % name)
    print('   Gender %s' % gender)
    print('   City %s' % city)
    print('   Age %s' % age)
    print()


print_info('Bob', gender='male', age=19)
print_info('Lisa', gender='female', city='Shanghai', age=22)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))







