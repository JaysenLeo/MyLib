# _*_coding:utf-8_*_
"""
ModelIntroduction:  无序查找算法

CreateDate:2017-10-25

ModifyDate:

ModifiedByWho:

Author:Lee

"""

#无序表查找

#就是数据不排序的线性查找，遍历数据元素。
#算法分析：最好情况是在第一个位置就找到了，此为O(1)；
# 最坏情况在最后一个位置才找到，此为O(n)；
# 所以平均查找次数为(n+1)/2。最终时间复杂度为O(n)
# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)
def sequential_search(Lis,Tgt):
    Lenght = len(Lis)
    for index in xrange(len(Lis)):
        if Lis[index]==Tgt:
            return index
    return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(LIST, 123)
    print(result)


