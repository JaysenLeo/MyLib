# _*_coding:utf-8_*_
#!/usr/bin/env python

from socket import *
import sys

def UdpCliMain():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024

    ADDR = (HOST, PORT)
    udpCliSock = socket(AF_INET,SOCK_DGRAM)

    while True:
        # 以字符串的形式接收报文
        Msg_data = raw_input('>')
        Len_data = str(sys.getsizeof(Msg_data))
        if not Msg_data:
            break
        # send pre
        udpCliSock.sendto(Len_data, ADDR)
        recv_pre_data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not recv_pre_data:
            break
        if str(recv_pre_data).split('|')[1] == 'ok':
            udpCliSock.sendto(Msg_data, ADDR)
            recv_end_data, ADDR = udpCliSock.recvfrom(BUFSIZ)
            if not recv_end_data:
                break
    udpCliSock.close()


if __name__ == '__main__':
    # 报文形式如下：
    #  'Name:Lee,ID:9527,Sex:male|Name:Aximov,ID:1233,Sex:male|Name:Beater,ID:6666,Sex:female'
    try:
        UdpCliMain()
    except Exception as e:
        print "异常：",e