# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""


# class MultiCallIterator:
#     """多服务调用，多服务输出"""
#
#     def __init__(self, results):
#         self.results = results



class _MultiCallService:
    # 多服务调用
    def __init__(self, call_list, name):
        self.__call_list = call_list
        self.__name = name
    def __getattr__(self, name):
        return _MultiCallService(self.__call_list, "%s.%s" % (self.__name, name))

    def __call__(self, *args):
        self.__call_list.append((self.__name, args))
        print """路由到相关的RPC请求域, 读取相关的service layer (trade)的服务层信息 （在mysql中，缓存于monogo db）"""
        """Eviews MT  --》  trade """
        print """RPC请求发起"""
        """ 发送到服务层网关"""
        print """RPC请求结果"""
        return self.__call_list,'result'

class MultiCall:
    def __init__(self, app):
        self.__app = app
        self.__call_list = []
        self.__register()
    def __repr__(self):
        return "<MultiCall at %x>" % id(self)

    __str__ = __repr__

    def __getattr__(self, name):
        return _MultiCallService(self.__call_list, name)

    def __register(self):
        # 根据路由域，获取该域的注册信息，然后通过user 获取注册服务
        pass

class HostCheck:
    """
    属于tornado的一个监听端口
        **发现主机，并注册（service）**
        **健康检查主机（service）**
    """
    pass

if __name__ == '__main__':
    """服务层网关"""
    """
    a = MultiCall('EviewsMT') -->获取该app所有的注册服务
    a.auth(username,password)
    if a.verify_token(username,token):
        模式1：
        a.trade({ module: 'tran_today',handle: 'detail' ·······})
        模式2：
        a.service_run(trade, params)

    服务层请求json
    {
        'service' : 'trade'
        'params' ：{ 'module': 'tran_today', 'handle': 'detail', 'parameter': '`````'}
    }


    """

    """服务调度层"""
    """

    根据服务调度层LB （lvs，nginx） 将服务请求分配到相应service-docker

    """