#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Python是动态语言，根据类创建的实例可以任意绑定属性。

class Student(object):
    # 这个属性虽然归类所有，但类的所有实例都可以访问到
    age = 15
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s.score)
# 输出：90

s.age = 30
print(s.age)
# 输出：30
print(Student.age)
# 输出：15

# 删除实例的属性
del s.age
print(s.age)     # 显示类的属性
# 输出：15

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。


# 为了统计学生人数，可以给Person类增加一个类属性，每创建一个实例，该属性自动增加
class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1

if Person.count != 0:
    print('Failed!')
else:
    bart = Person('Bart')
    if Person.count != 1:
        print('Failed!')
    else:
        bob = Person('Bob')
        if Person.count != 2:
            print('Failed!')
        else:
            print('Person:', Person.count)
            print('Success!')
# 输出：Person: 2
#      Success!