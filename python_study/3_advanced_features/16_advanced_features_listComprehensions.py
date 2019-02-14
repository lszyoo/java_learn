#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 列表生成式

print(list(range(1, 11)))
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10)))
# 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 上边循环太繁琐，使用列表生成式
print([x * x for x in range(1, 11)])
# 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 加 if 条件句
print([x * x for x in range(1, 11) if x % 2 == 0])
# 输出：[4, 16, 36, 64, 100]

# 两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 输出：['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])
# 输出：['17_advanced_features_generator.py', '15_advanced_features_Iteration.py', '2_python基础', '11_self_define_function.py', '3_encoding.py', '14_advanced_features_slices.py', '1_input_print.py', 'advanceFeature.py', '6_tuple.py', '10_build_in_function.py', 'tk', '__pycache__', '8_for_while.py', '9_dict_set.py', '7_if.py', '16_advanced_features_listComprehensions.py', 'venv', '12_function_args.py', '13_recursion_function.py', '4_format.py', '5_list.py', '2_function.py', 'metadata_monitor.py', '.idea']


# 列表生成式也可以使用两个变量来生成list
d = {'A': 'X', 'B': 'Y', 'C': 'Z'}
print([k + '=' + v for k, v in d.items()])         # value不能是int
# 输出：['A=X', 'B=Y', 'C=Z']


# 把一个 list 中的所有字符串变成小写
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World']
print([s.lower() for s in L])
# 输出：['hello', 'world']

print([s.lower() for s in L if isinstance(s,str)])
