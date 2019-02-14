#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 匿名函数

# f(x)=x^2
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
# 输出：[1, 4, 9, 16, 25]
""" 
    匿名函数lambda x: x * x实际上就是：
    def f(x):
        return x * x
        
    关键字lambda表示匿名函数
    匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
"""

# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 匿名函数也可赋值给一个变量

f = lambda x: x * x
print(f)
# 输出：<function <lambda> at 0x103226950>
print(f(5))
# 输出：25


# 匿名函数作为返回值返回
def build(x, y):
    return lambda x, y: x * x + y * y
f = build(1, 2)
print(f(1, 2))
# 输出：5


print(list(filter(lambda n: n % 2 == 1, range(1, 20))))
# 输出：[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]