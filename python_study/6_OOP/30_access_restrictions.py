#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，私有变量
# 在方法中，可以对参数做检查，避免传入无效的参数
# 一个下划线的变量如：_name，意思是说：虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 < score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))



bart = Student('Bart Simpson', 88)
bart.print_score()
# 输出：Bart Simpson: 88
# bart.__name 找不到这个属性
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
bart._Student__name = 'Jenny'
bart.print_score()
# 输出：Jenny: 88

# 错误写法
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
bart.__name = 'New Name'
bart.print_score()
# 输出：Jenny: 88