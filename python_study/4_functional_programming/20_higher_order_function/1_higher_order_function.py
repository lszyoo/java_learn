#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 高阶函数

# 变量可以指向函数

# abs() 函数为例
print(abs(-10))         # 输出：10
print(abs)              # 输出：<built-in function abs>    打印函数本身

# 把函数返回值赋值给变量
x = abs(-10)
print(x)                # 输出：10
# 把函数赋值给变量
f = abs
print(f)                # 输出：<built-in function abs>    打印函数本身
print(f(-10))           # 输出：10



# 函数名也是变量：函数名作为变量，一般不使用


# 传入函数

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(5, -6, abs))        # 注意：不能写 abs()
# 输出：11
