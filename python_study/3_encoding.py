#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在最新的Python 3版本中，字符串是以Unicode编码的

print('天天向上')
# 输出：天天向上

# ord()函数获取字符的整数表示
print(ord('A'))
# 输出：65
print(ord('帅'))
# 输出：24069

# chr()函数把编码转换为对应的字符
print(chr(66))
# 输出：B
print(chr(24069))
# 输出：帅

# 十六进制
print('\u4e2d\u6587')
# 输出：中文

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# 对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
# 输出：b'ABC'
print('刘帅'.encode('utf-8'))
# 输出：b'\xe5\x88\x98\xe5\xb8\x85'
# '中文'.encode('ascii')  报错，中文编码的范围超过了ASCII编码的范围
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示

# 把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
# 输出：ABC
print(b'\xe5\x88\x98\xe5\xb8\x85'.decode('utf-8'))
# 输出：刘帅
# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe5\x88\x98\xe5\xb8\x10'.decode('utf-8', errors='ignore'))
# 输出：刘

# 计算 str 包含多少个字符
print(len('abc'))
# 输出：3

# 计算 bytes 中含有多少字节
print(len(b'abc'))
# 输出：3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# 输出：6
print(len('刘帅'.encode('utf-8')))
# 输出：6
