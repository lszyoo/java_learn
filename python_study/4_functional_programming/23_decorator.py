#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 装饰器

def now():
    print("2019-02-03")

# 获取 函数名
print(now.__name__)     # 两个 _
# 输出：now


# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。
# 定义一个能打印日志的decorator

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2019-02-03")

now()
# 输出：call now():
#      2019-02-03

now = log(now)      # 等效于 @log，只是此处now，包含了 @log，先执行 log(wrapper)，在执行 log(now)，最后执行 now()
now()
# 输出：call wrapper():
#      call now():
#      2019-02-03


# decorator 的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')         # 等效于 now = log('execute')(now)
def now():
    print('2019-02-11')

now()
# 输出：execute now():
#      2019-02-11
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

print(now.__name__)
# 输出：wrapper
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的



# 一个装饰器的完整写法如下：

# 无参 decorator
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, *kw)
    return wrapper

# 有参 decorator
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print('2019-02-12')

print(now.__name__)
# 输出：now

now()
# 输出：call now():
#      2019-02-12


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        print('%s executed in %s ms' % (fn.__name__, time.time() - start))
        return fn(*args, **kw)
    return wrapper

@metric
def now():
    print('新年好')

now()
# 输出：now executed in 9.5367431640625e-07 ms
#      新年好


# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def metric(ar = None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            if ar != None:
                print('begin call %s %s' % (fn.__name__, ar))
                print('begin call %s %s' % (fn.__name__, ar))
            else:
                print('begin call %s' % fn.__name__)
                print('begin call %s' % fn.__name__)
            return fn(*args, **kw)
        return wrapper
    return decorator

@metric('execute')
def now():
    print('新年好')

now()
# 输出：begin call now execute
#      begin call now execute
#      新年好