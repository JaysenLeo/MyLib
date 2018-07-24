# -*- coding: utf-8 -*-
"""
__call__
在Python中，函数其实是一个对象：

# >>> f = abs
# >>> f.__name__
# 'abs'
# >>> f(-123)
123
由于 f 可以被调用，所以，f 被称为可调用对象。

所有的函数都是可调用对象。

一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。

我们把 Person 类变成一个可调用对象：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
现在可以对 Person 实例直接调用：
#
# >>> p = Person('Bob', 'male')
# >>> p('Tim')
My name is Bob...
My friend is Tim...
单看 p('Tim') 你无法确定 p 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。

任务
改进一下前面定义的斐波那契数列：

class Fib(object):
    ???
请加一个__call__方法，让调用更简单：

# >>> f = Fib()
# >>> print f(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
复制代码
可以把实例对象用类似函数的形式表示，进一步模糊了函数和对象之间的概念

复制代码
class Fib(object):
    def __init__(self):
        pass
    def __call__(self,num):
        a,b = 0,1;
        self.l=[]

        for i in range (num):
            self.l.append(a)
            a,b= b,a+b
        return self.l
    def __str__(self):
        return str(self.l)
    __rept__=__str__

f = Fib()
print f(10)
"""


class Job(object):
    def __init__(self, salary):
        self.salary = salary

    def __call__(self, salary=None):
        print 'Salary of the job about %s...' % (salary or self.salary)


if __name__ == '__main__':
    # func = len
    # print func.__name__
    # print func('asdf')

    p = Job('￥10')
    p('￥20')

