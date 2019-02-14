#!/user/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

# 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
__author__ = 'Lszyoo'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')

"""
    当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，
    if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    命令行：python hello.py -> 输出：Hello, World!
    交互环境：导入 import hello -> 没输出
             调用 hello.test() -> 输出：Hello, World!
"""

if __name__ == '__main__':
    test()

"""
    sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
        运行python3 hello.py获得的sys.argv就是['hello.py']；
        运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
    
"""


# 作用域
"""
    public：普通 和 特殊变量 __author__、__name__、__doc__（访问文档注释）
    private：_
    
    private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，
    但是，从编程习惯上不应该引用private函数或变量。
"""

def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 1:
        return _private_1(name)
    else:
        return _private_2(name)
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。