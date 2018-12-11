#!/user/bin/env python3
# -*- coding: utf-8 -*-


# list是一个可变的有序表

# 定义一个list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 输出：['Michael', 'Bob', 'Tracy']

# list 的长度
print(len(classmates))
# 输出：3

# 用索引访问 list 元素
print(classmates[0])        # 输出：Michael
print(classmates[-1])       # 输出：Tracy

# 追加元素
# 追加到末尾
classmates.append('Adam')
print(classmates)           # 输出：['Michael', 'Bob', 'Tracy', 'Adam']
# 把元素插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)           # 输出：['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

# 删除元素
# 删除末尾元素
classmates.pop()
print(classmates)           # 输出：['Michael', 'Jack', 'Bob', 'Tracy']
# 删除指定位置元素
classmates.pop(1)
print(classmates)           # 输出：['Michael', 'Bob', 'Tracy']

# 给某个元素赋值
classmates[1] = 'Sarah'
print(classmates)           # 输出：['Michael', 'Sarah', 'Tracy']


# list 里的数据类型可以不同
s = [1, True, 'Apple', ['asp', 'php']]
print(s)                    # 输出：[1, True, 'Apple', ['asp', 'php']]

# 类似二维数组，三维、四维、...
print(s[3][0])              # 输出：asp

# 空 list
L = []
print(len(L))               # 输出：0
