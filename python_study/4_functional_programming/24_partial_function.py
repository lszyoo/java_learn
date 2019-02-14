#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 通过设定参数的默认值，可以降低函数调用的难度，偏函数也可以做到这一点

# int() 将字符串以 base 进制的形式转换成 十进制 返回
print(int('12345'))
# 输出：12345

# int()函数还提供额外的base参数，默认值为10
print(int('12345', base=8))
# 输出：5349

# 定义函数，将十进制转换成二进制
def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))
# 输出：64

# functools.partial就是帮助我们创建一个偏函数，不需要我们自己定义int2()
import functools
int16 = functools.partial(int, base=16)
print(int16('F'))
# 输出：15

# 总结：functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数

print(int16('1010', base=2))
# 输出：10

# 将 10 自动添加到 max() 中
max2 = functools.partial(max, 11)
print(max2(2, 3))
# 输出：11