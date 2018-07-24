# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""


import xmlrpclib
proxy=xmlrpclib.ServerProxy("http://localhost:8000/")
multicall=xmlrpclib.MultiCall(proxy)
multicall.add(7,3)
multicall.subtract(7,3)
multicall.multiply(7,3)
multicall.divide(7,3)
result=multicall()
print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d" %tuple(result)

