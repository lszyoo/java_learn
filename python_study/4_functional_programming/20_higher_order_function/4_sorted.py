#!/user/bin/env python3


# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

# sorted()函数就可以对list进行排序
print(sorted([23, -19, 4, 3, 10]))
# 输出：[-19, 3, 4, 10, 23]

# sort 接受 key，自定义的排序
print(sorted([23, -19, 4, 3, 10], key=abs))
# 输出：[3, 4, 10, -19, 23]


print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 输出：['Credit', 'Zoo', 'about', 'bob']

# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 输出：['about', 'bob', 'Credit', 'Zoo']

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# 输出：['Zoo', 'Credit', 'bob', 'about']



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(student):
    return student[0]

print(sorted(L, key=by_name))
# 输出：[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

def by_score(student):
    return student[1]

print(sorted(L, key=by_score))
# 输出：[('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]