# -*- coding: utf-8 -*-


"""
如果一个类或者其实例对象有类似list对象一样的通过 len() 函数来 获取对象的统计属性的值
即 该对象可统计元素的个数。此时，类必须提供一个特殊方法__len__()，在这个方法下定义
返回元素的个数，也就是说，只要正确实现了__len__()方法，就可以用len()返回如下 Family实例“长度”
"""


class Family(object):

    def __init__(self, *args):
        self.names = args

    def __len__(self):
        # 此处必须返回一个整数值，不管以何种方式
        return len(self.names)


if __name__ == '__main__':
    menber = Family('Dada', 'Mama', 'You')
    print len(menber)


