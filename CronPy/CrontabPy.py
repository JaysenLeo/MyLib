# -*- coding: utf-8 -*-
"""
模块介绍: 这是一个定时任务模块

创建者: 李成杰

联系方式: 2835347017

创建日期: 2018-2-11

地点: 西安市
"""

import datetime, os, platform


def run_task():

	"""
    这是一个单元测试
    """

	os_platform=str(platform.platform())
	if os_platform.startswith('Darwin'):
		print 'this is mac os system'
		os.system('ls')
	elif os_platform.startswith('Window'):
		print 'this is windows os system',datetime.datetime.now()
		# os.system('dir')
	elif os_platform.startswith('Linux'):
		print 'this is linux os system'
		os.system('dir')


def time_handle(sched_time):

	"""
    SDFASDF
    """
	flag=0
	while True:
		now = datetime.datetime.now()
		if now == sched_time:
			run_task()
			flag=1
		else:
			if flag == 1:
				sched_time = sched_time+datetime.timedelta(seconds=5)
				flag=0

if __name__ == '__main__':
	# schedtime=datetime.datetime(2017, 11, 17, 17, 25, 30)
	schedtime=datetime.datetime.now()
	print 'run the timer task at {}'.format(schedtime)
	time_handle(schedtime)

