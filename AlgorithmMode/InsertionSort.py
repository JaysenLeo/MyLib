# _*_coding:utf-8_*_
"""
ModelIntroduction:

CreateDate:

ModifyDate:

ModifiedByWho:

Author:

"""

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

if __name__ == '__main__':
    lists = [2,4,1,3,72,9,34,8]
    print insert_sort(lists)


