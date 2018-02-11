# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""
import time


def exeTime(func):

    def wrapper(x):
        start = time.clock()
        result = func(x)
        end = time.clock()
        print("{0}  {1} {2}".format(func.__name__, '耗时',end-start))
        return result
    return wrapper




