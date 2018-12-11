#!/user/bin/env python3
# -*- coding: utf-8 -*-


# 调用 内部函数
# http://docs.python.org/3/library/functions.html#abs

# 绝对值
print(abs(-5))
# 输出：5

# all() 如果iterable的所有元素都为True(或者iterable为空)，则返回True。
print(all([]))
# 输出：True
print(all([1, 2]))
# 输出：True
print(all([1, False]))
# 输出：False

# any() 如果iterable 存在元素为True，则返回True。如果迭代为空，返回False。
print(any([]))
# 输出：False
print(any([False]))
# 输出：False
print(any([1, False]))
# 输出：True

# ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
print(ascii('ali'))
# 输出：'ali'
print(ascii('中国'))
# 输出：'\u4e2d\u56fd'

# bin() 将数字转换成二进制
print(bin(3), bin(-10))
# 输出：0b11 -0b1010
print(format(14, '#b'), format(14, 'b'))
# 输出：0b1110 1110


# max() 返回最大值
print(max(1, 2, 5))
# 输出：5

# 数据类型转换
print(int('123'))      # 将 字符串'123'转换成 int 123
# 输出：123
print(int(12.84))      # 将 float 12.34 转换成 int 12，取整
# 输出：12
print(str(124))        # 将 int 124 转换成 str 124
# 输出：124
print(bool(1))
# 输出：True
print(bool(''))
# 输出：False

# 将整数转换成十六进制
print(hex(100))
# 输出：0x64

# 给函数起别名
a = abs                # 变量a指向abs函数
print(a(-1))
# 输出：1

