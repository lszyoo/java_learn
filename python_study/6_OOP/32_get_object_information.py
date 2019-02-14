#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 获取对象信息用 type() 方法

# 基本类型
print(type(123))
# 输出：<class 'int'>
print(type(None))
# 输出：<class 'NoneType'>

# 函数
print(type(abs))
# 输出：<class 'builtin_function_or_method'>

# 无法引包 6_OOP.31_inheritance_polymorphism，因为目录下没有 __init__.py 模块
# 类
class Animal(object):
    pass

print(type(Animal()))
# 输出：<class '__main__.Animal'>

# type() 返回 对应的 class 类型
print(type('123') == type('abc'))
# 输出：True
print(type(Animal()) == Animal)
# 输出：True


# isinstance()

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print(isinstance(123, int))
# 输出：True

# isinstance()判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))     # 输出：True
print(isinstance((1, 2, 3), (list, tuple)))     # 输出：True



# dir()

# 获得一个对象的所有属性和方法，使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))
# 输出：['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ...]

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如：
# 在len()函数内部，它自动去调用该对象的__len__()方法，以下等价
len('abc')
'abc'.__len__()

# 自建类调用len()方法，需自己定义
class Dog(Animal):
    def __len__(self):
        return 100

print(len(Dog()))
# 输出：100


# 其余的都是普通方法，如：
'ABC'.lower()



# getattr()、setattr()、hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# 判断类是否有某属性
print(hasattr(obj, 'x'))
# 输出：True
print(hasattr(obj, 'y'))
# 输出：False

# 为类设置一个属性
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
# 输出：True

# 获取属性
print(getattr(obj, 'y'))
# 输出：19

# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))
# 输出：404


# 获取对象的方法
print(hasattr(obj, 'power'))
# 输出：True
print(getattr(obj, 'power'))
# 输出：<bound method MyObject.power of <__main__.MyObject object at 0x102a922b0>>
fn = getattr(obj, 'power')
print(fn)
# 输出：<bound method MyObject.power of <__main__.MyObject object at 0x1032922e8>>


# 文件流、网络流、字节流
def readData(fn):
    pass
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

