# -*- coding: utf-8 -*-
"""
 class Student(object):
...     pass
...
然后，尝试给实例绑定一个属性：

# >>> s = Student()
# >>> s.name = 'Michael' # 动态给实例绑定一个属性
# >>> print s.name
# Michael
# 还可以尝试给实例绑定一个方法：
#
# >>> def set_age(self, age): # 定义一个函数作为实例方法
# ...     self.age = age
# ...
# >>> from types import MethodType
# >>> s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
# >>> s.set_age(25) # 调用实例方法
# >>> s.age # 测试结果
# 25
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
#
# >>> s2 = Student() # 创建新的实例
# >>> s2.set_age(25) # 尝试调用方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
为了给所有实例都绑定方法，可以给class绑定方法：

# >>> def set_score(self, score):
# ...     self.score = score
# ...
# >>> Student.set_score = MethodType(set_score, None, Student)
# 给class绑定方法后，所有实例均可调用：
#
# >>> s.set_score(100)
# >>> s.score
# 100
# >>> s2.set_score(99)
# >>> s2.score
99
通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性

在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。

然而，对于有着已知属性的小类来说，它可能是个瓶颈。这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。
不过还是有一个方法来规避这个问题。这个方法需要使用__slots__来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。

"""


class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


"""使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的："""


class GraduateStudent(Student):
     pass


"""除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__"""


class Doctor(Student):
    __slots__ = Student.__slots__

if __name__ == '__main__':
    s = Student() # 创建新的实例
    s.name = 'Michael' # 绑定属性'name'
    s.age = 25 # 绑定属性'age'
    # s.score = 99 # 绑定属性'score'
    # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

    g = GraduateStudent()
    g.score = 9999

    g = Doctor()
    g.score = 9999
