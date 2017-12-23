# _*_coding:utf-8_*_
import urllib
import os
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

if __name__ == '__main__':
    print urllib.urlopen('http://nginx.org/download/').read()

    # url = 'http://nginx.org/download/nginx-1.12.1.tar.gz'
    # # print url.split('/')[-1]
    # local = os.path.join(os.path.dirname(os.path.abspath(__file__)),url.split('/')[-1])
    # urllib.urlretrieve(url,local,Schedule)
    # print os.path.dirname(os.path.abspath(__file__))


