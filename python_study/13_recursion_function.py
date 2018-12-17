#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# n！
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))
# 输出：120