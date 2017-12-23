# -*- coding: utf-8 -*-
"""
模块介绍:
    有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
    1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
　　掉不满足条件的排列。
创建者:

创建日期:
"""


def func1():
    """
    方法一
    """
    print ("======={0}start ======= ").format(func1.__doc__.replace('\n', ''))
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if( i != k ) and (i != j) and (j != k):
                    print  ("{0} {1} {2} ").format(i,j,k)
    print ("======={0}end ======= ").format(func1.__doc__.replace('\n', ''))

if __name__ == '__main__':
    func1()


