#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 元组是一个有序列表,tuple一旦初始化就不能修改,没有append()，insert()等这样的方法
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

# 定义一个 tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# 输出：('Michael', 'Bob', 'Tracy')
print(classmates[0])
# 输出：Michael
print(classmates[-1])
# 输出：Tracy

# 定义一个空 tuple
t = ()
print(t)
# 输出：()

# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
print((1))
# 输出：1
# 只有1个元素的tuple定义时必须加一个逗号，来消除歧义
print((1,))

# "可变的" tuple
t = (1, 2, ['A', 'B'])
t[2][0] = 'X'
print(t)
# 输出：(1, 2, ['X', 'B'])

# tuple里面存的其实只是指向这个元素的地址，是不可变的，但是地址所指向的内存空间里的内容是可以变的，
