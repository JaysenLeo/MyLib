# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""

_obj = dict(name='王记炒面', code=9527)


class Merchant:

    def __init__(self, _obj):
        #
        self.name = _obj['name']
        self.code = _obj['code']

    def __setattr__(self, key, value):
        self.__dict__.update(_obj)
        # print ("__setattr__ %s" % key)

    def __getattr__(self, item):
        print self.__dict__
        print ("__getattr__ %s" % item)
    # def __getattribute__(self, item):
    #     print ("__getattr__ %s" % item)

    def set_obj(self, name):
        self.name = name

    def test(self):
        pass

# class Merchant:
#
#     def __init__(self, _obj):
#         self.__dict__.update(_obj)
#
#     def __setattr__(self, key, value):
#         print ("__setattr__ %s" % key)
#
#     def set_obj(self, name):
#         self.name = name
#
#
#
#     def test(self):
#         pass

if __name__ == '__main__':

    p = Merchant(_obj)
    print p.code
    print p.name

    # print p.__dict__
    # print p.name



