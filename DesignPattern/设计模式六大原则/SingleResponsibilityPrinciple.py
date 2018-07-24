# -*- coding: utf-8 -*-

"""
单一职责原则
"""


class Person(object):

    """ 人类 """

    def duty(self, one):

        """ Coder 的职责是写代码 ，农民就负责斗地主，其余的学习 """

        return one is "Coder" and "Coding" or one is "Farmer" and "Chinese poker" or "Studying"


class Coder(Person):
 
    """ 程序员 """

    def duty(self):

        """ Coder 的职责是写代码 """

        return "Coding"


class Farmer(Person):
     
    """ 程序员 """

    def duty(self):

        """ 农民就负责斗地主 """

        return "Chinese poker"

if __name__ == '__main__':
    p = Person()
    print(p.duty("Coder"))