# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""

#!/usr/bin/python
#coding=utf-8

"""
start python 项目
"""


import MySQLdb
db = {}
def get_table_data(i):
    # print i
    try:
        conn= MySQLdb.connect(
                host='127.0.0.1',
                port = 3306,
                user='root',
                passwd='qwer121212',
                db ='glf',
                )
        cur = conn.cursor()
        print id(conn)
        #返回数据
        cur.execute("select * from eviews_user")
        datacur = cur.fetchall()
        # print '----'
    except MySQLdb.Error as e:
            print e
    finally:
        # #关闭连接
        if conn:
            print '++++'
            cur.close()
            conn.close()
            # print dir(conn)
            # print conn.messages


import concurrent.futures
import time
import os


def work_core(message):
    time.sleep(2)
    print ('[message] %(msg)s [pid] %(pid)d' % {'msg': str(message), 'pid': os.getpid()})
    return 0


def run_works(work_core, work_args, p=None, wait=False, max_workers=2, run_method=2):
    """
    运行多进程
    :param work:
    :param salts:
    :param p:
    :param wait:
    :return:
    """
    ##########
    # 多线程 #
    ##########
    kwargs = {'max_workers': max_workers, 'work_core': work_core, 'work_args': work_args, 'wait': wait}
    # if run_method == 0:
    #     print(thread_commit(**kwargs))
    # elif run_method == 1:
    #     print(thread_map(**kwargs))
    if run_method == 2:
        thread_wait(**kwargs)
    # elif run_method == 3:
    #     print(process_commit(**kwargs))


def thread_wait(*args, **kwargs):
    max_workers = kwargs['max_workers']
    core = kwargs['work_core']
    args = kwargs['work_args']
    _wait = kwargs['wait']
    result = list()
    futures = list()
    _res = None
    RETURN_WHEN = {True: 'ALL_COMPLETED', False: 'FIRST_COMPLETED'}
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    for _arg in args:
        futures.append(pool.submit(core, _arg))
        result.append(concurrent.futures.wait(futures, return_when=_wait is None and 'FIRST_EXCEPTION' or RETURN_WHEN[_wait]))
    pool.shutdown(wait = _wait)
    return result
if __name__ == '__main__':
        import time
        data_list = [i for i in  range(1000000)]

        for i in range(100):
            run_works(max_workers = 10000, work_core = get_table_data,work_args = data_list , wait = True)
        #     get_table_data()
            # time.sleep(10)

