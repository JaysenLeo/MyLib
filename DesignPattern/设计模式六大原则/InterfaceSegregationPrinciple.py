# -*- coding: utf-8 -*-
"""
接口隔离原则
"""
import abc
import time
import types

HOUR = 3600

class Person(object):

    """ 人类 """
    @abc.abstractmethod
    def duty(self):

        """ 职责 """
        pass


class Coder(Person):

    """ 程序员 """

    def duty(self):

        """ Coder 的职责是写代码 """

        return "Coding"

    def sleep(self):
  
        """ 有时睡5小时 """

        time.sleep(5*HOUR)

# 方法一
# def programme(self, language='Php'):
#     """ 实例动态方法 """
#     return language

# 方法二
# @classmethod
# def programme(cls, language='Php'):
#     """ 类动态方法 """
#     return language

# 方法三
@staticmethod
def programme(language='Php'):
    """ 静态方法 """
    return language

if __name__ == '__main__':
    
    # 方法一：给实例绑定方法
    # p = Coder()
    # p.programme = types.MethodType(programme, p)
    # print(p.programme('Python'))
    
    # 方法二：
    # p = Coder()
    # Coder.programme = programme
    # print(Coder.programme('Java'))
    # print(p.duty())

    # 方法三：静态方法
    p = Coder()
    Coder.programme = programme
    print(Coder.programme('Java'))
    print(p.programme('Golang'))
    print(p.duty())
