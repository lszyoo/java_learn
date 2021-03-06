#!/user/bin/env python3
# -*- coding: utf-8 -*-

print('Hello %s' % 'World' + '!')
# 输出：Hello World!

#   +--------------+-----------------+
#   |   占位符      |      替换内容
#   +--------------+-----------------+
#   |     %d       |        整数
#   +--------------+-----------------+
#   |     %f       |       浮点数
#   +--------------+-----------------+
#   |     %s       |       字符串
#   +--------------+-----------------+
#   |     %x       |    十六进制整数
#   +--------------+-----------------+

print('%2d-%03d' % (3, 1))
# 输出：空格3-001

print('%.2f' % 3.1415926)
# 输出：3.14

# 转义 %
print('growth rate: %d %%' % 7)
# 输出：growth rate: 7 %


# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%, {2}分'.format('小明', 17.125, 18))
