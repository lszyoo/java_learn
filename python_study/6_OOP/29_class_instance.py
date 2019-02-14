#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 定义类是通过class关键字,类名首字母大写
# Student 类继承 object 类
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
class Person():
    pass

print(Person)
# <class '__main__.Person'>

# 创建实例
print(Person())
# <__main__.Person object at 0x103121cc0>


# 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
class Student(object):
    """
        将 name、score 属性绑定到实例上，self 表示实例本身，
        有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
        但self不需要传，Python解释器自己会把实例变量传进去
        注意：特殊方法“__init__”前后分别有两个下划线！！！
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 数据封装
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 数据访问
bart = Student('Jenny', 95)
bart.print_score()
# 输出：Jenny: 95
bart.name = 'Micheal'
bart.print_score()
# 输出：Micheal: 95


