# _*_coding:utf-8_*_

from socket import *
from time import ctime
import redis
import sys
import psutil
import multiprocessing

def UdpServerMain():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024

    udpSerSock = socket(AF_INET,SOCK_DGRAM)
    udpSerSock.bind((HOST,PORT))
    main_core(udpSerSock,BUFSIZ)
    # 构造进程池
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(4):
        pool.apply_async(main_core, (udpSerSock, BUFSIZ))
    pool.close()
    pool.join()

def main_core(udpSerSock,BUFSIZ):
    while True:
        print '...waiting for message..'
        all_data = ''
        # recv pre
        pre_data, pre_addr = udpSerSock.recvfrom(BUFSIZ)
        pre_data = int(pre_data)
        udpSerSock.sendto('[%s]|%s'%(ctime(), 'ok'),pre_addr)

        if int(pre_data) is not 0:
            # recv
            while sys.getsizeof(all_data) < pre_data:
                # 根据计算机本身的剩余内存，收缩接收缓冲区
                remain_mem = psutil.virtual_memory().total-psutil.virtual_memory().used
                if pre_data > BUFSIZ and sys.getsizeof(pre_data) < remain_mem :
                    BUFSIZ = int(pre_data)
                elif pre_data > BUFSIZ and sys.getsizeof(pre_data) >= remain_mem:
                    BUFSIZ = int(remain_mem)
                data, addr = udpSerSock.recvfrom(BUFSIZ)
                all_data += data
                udpSerSock.sendto('[%s] got_size: %s'%(ctime(), len(all_data)),addr)

            r = redis.Redis(host='127.0.0.1', port=6379)
            for item in str(all_data).split('|'):
                _, ID, _ = item.split(',')
                r.set(ID.split(':')[1], item)

    udpSerSock.close()

if __name__ == '__main__':
    try:
        UdpServerMain()
    except Exception as e:
        print "异常：",e

