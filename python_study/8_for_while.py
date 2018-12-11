#!/user/bin/env python3
# -*- coding: utf-8 -*-


# break：结束循环
# continue：结束本轮循环，进入下一轮循环


# for

names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)
# 输出：Micheal
#      Bob
#      Tracy

# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print(range(3))
# 输出：range(0, 3)
print(list(range(5)))
# 输出：[0, 1, 2, 3, 4]

# 求和
sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)
# 输出：5050


# while

# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# 输出：2500

# 输出 1-10 的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n, end = ' ')
# 输出：1 3 5 7 9

