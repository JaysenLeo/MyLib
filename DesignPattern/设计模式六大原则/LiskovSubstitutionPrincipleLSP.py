# -*- coding: utf-8 -*-
import abc
import time
"""
里氏替换原则
"""
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


class Farmer(Person):
     
    """ 程序员 """

    def duty(self):

        """ 农民就负责斗地主 """

        return "Chinese poker"

    def sleep(self):
        
        """ 农民可以睡八小时 """
        
        time.sleep(8*HOUR)

if __name__ == '__main__':
    p = Coder()
    print(p.duty())