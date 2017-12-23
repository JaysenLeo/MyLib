# _*_coding:utf-8_*_
"""
ModelIntroduction:

CreateDate:

ModifyDate:

ModifiedByWho:

Author:

"""

if __name__ == '__main__':
    import socket

    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    print myaddr


