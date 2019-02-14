#!/user/bin/env python3
#-*- coding: utf-8 -*-

# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

# 继承的好处：子类获得了父类的全部功能
dog = Dog()
dog.run()
# 输出：Animal is running...


class Cat(Animal):
    # 子类覆盖父类的方法
    def run(self):
        print('Cat is running...')
    # 子类添加父类没有的方法
    def eat(self):
        print('Eating meat...')

cat = Cat()
cat.run()
# 输出：Cat is running...
cat.eat()
# 输出：Eating meat...


# 子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
# “开闭”原则
# 继承树

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了