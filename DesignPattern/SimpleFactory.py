# -*- coding: utf-8 -*-
"""
模块介绍: 简单工厂模式

创建者:

创建日期:
"""

"""
1.如下，非简单工厂 要记住住各种调用接口，子类的名字都要记住,直接实例化子类
"""

#
# class Shape(object):
# 	pass
#
#
# class Triangle(Shape):
#
# 	def draw(self):
# 		print "三角形"
#
#
# class Square(Shape):
#
# 	def draw(self):
# 		print "正方形"


"""
简单工厂方法
"""


class Shape(object):

    def draw(self):
        # 子类如果不重构这个方法就报这个错
        raise NotImplementedError


class Circle(Shape):

    def draw(self):
        print "圆"


class Triangle(Shape):

    def draw(self):
        print "三角"


class ShapeFactory(object):
    # 仅这一个图形工厂
    @classmethod
    def create(cls, shape):
        # 绝对路径导入，优于相对路径
        try:
            import importlib
            router = importlib.import_module('DesignPattern.SimpleFactory')
            return getattr(router, shape)()
            # 此处可以反射获取，缺点也再此，需要新图形时，需要再次新加代码
        except AttributeError as at:
            print '无 %s 图形' % shape


if __name__ == '__main__':
    # t = Triangle()
    # s = Square()
    # t.draw()
    # s.draw()

    fac = ShapeFactory()
    # 想画图
    obj = fac.create('Triagle')
    # 画什么  用这个统一的接口创建
    # 将类的实例化延迟到了子类，比起上一个，又跟好的用户体验
    # 用户不需要修改代码
    obj.draw()  # 开始画
