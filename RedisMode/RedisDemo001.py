# _*_coding:utf-8_*_
import redis
import MySQLdb
import time


def write_mysql():
    r = redis.Redis(host='127.0.0.1', port=6379)
    while True:
        if r.keys() == []:
            time.sleep(3)
        db = MySQLdb.connect("localhost","root","qwer121212","cib_localtiews" )
        cursor = db.cursor()
        for name in r.keys():
            name,id,sex = str(r.get(name)).split(',')
            sql = "INSERT INTO TESTLEE(NAME,ID, SEX) VALUES (\'%s\',%s,\'%s\')"%(
                str(name).split(':')[1],
                str(id).split(':')[1],
                str(sex).split(':')[1],
            )
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 失败回滚
                db.rollback()
        db.close()

if __name__ == '__main__':
    r = redis.Redis(host='127.0.0.1', port=6379)
    print r.keys()
    # try:
    #     write_mysql()
    # except Exception as e:
    #     print "异常：",e