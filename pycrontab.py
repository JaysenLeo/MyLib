#_*_ utf-8 _*_
"""
asdas
"""
import datetime, os, platform


def run_task():

    """
    SDFADSF
    """
    os_platform=str(platform.platform())
    if os_platform.startswith('Darwin'):
        print 'this is mac os system'
        os.system('ls')
    elif os_platform.startswith('Window'):
        print 'this is windows os system'
        os.system('dir')


def time_handle(sched_time):
    
    """
    SDFASDF
    """
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now == sched_time:
            run_task()
            flag = 1
        else:
            if flag == 1:
                sched_time = sched_time+datetime.timedelta(weeks=1)
                flag = 0

if __name__ == '__main__':

    schedtime = datetime.datetime(2018, 5, 2, 14, 19, 30)
    print 'run the timer task at {}'.format(schedtime)
    time_handle(schedtime)
