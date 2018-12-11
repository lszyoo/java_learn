#!/user/env/bin python3
# -*- coding: utf-8 -*-

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# return None 可以简写为 return，函数执行完毕也没有return语句时，自动 return None。

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')     # 参数类型检查
    if x >= 0:
        return x
    else:
        return -x

# 如果你已经把my_abs()的函数定义保存为 abstest.py 文件了，
# 那么，可以在该文件的当前目录下启动Python解释器，用 from abstest import my_abs 来导入 my_abs() 函数，注意 abstest 是文件名


# 空函数
def nop():
    pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。


# 返回多个值，但其实这只是一种假象，Python函数返回的仍然是单一值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 输出：151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6)
print(r)
# 输出：(151.96152422706632, 70.0)

# 原来返回值是一个tuple。但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple。


# 求 ax2 + bx + c = 0 的两个解
def quadratic(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (int, float)):         # 参数检查
            raise ValueError('无效输入')
    if a == 0 & b != 0:
        return -c / b
    m = b * b - 4 * a * c
    if m > 0:
        print('有两个不等实根')
        return (-b + math.sqrt(m)) / (2 * a), (-b - math.sqrt(m)) / (2 * a)
    elif m == 0:
        print('有两个相等实根')
        return -b / (2 * a)
    else:
        print('无实根')

print(quadratic(1, 2, 1))