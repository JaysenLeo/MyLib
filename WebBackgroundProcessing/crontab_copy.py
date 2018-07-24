# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""

import datetime
import threading
import time
import shutil
import os

class CrontabBase(object):

	def __init__(self, task_contain):
		"""

		:param task_contain: {
			'任务一': {
			'task_start_time': '2018-05-02';
			'task_end_time': '2018-05-02';
			'task_interval_time': weeks;
			'task_name': task1
			},
			'任务二': {
			'task_start_time': '2018-05-02';
			'task_interval_func': weeks;
			'task_name': task1
			},
		}
		"""
		self.task_contain = task_contain or dict()

	def valid_type(self):
		if isinstance(self.task_contain, dict):
			raise ValueError

	def add_task(self, task, task_prop):
		raise NotImplementedError

	def add_interval_function(self):
		pass


class Crontab(CrontabBase):

	def __init__(self, task_contain):
		super(Crontab, self).__init__(task_contain=task_contain)

	def add_task(self, task, task_prop):
		print '正在执行', task
		if 'task_start_time' not in self.task_contain[task].keys():
			raise ValueError('need task_start_time')
		else:
			# 开始执行
			flag = 0
			while True:
				now = datetime.datetime.now()
				if now == self.task_contain[task]['task_start_time']:
					self.task_contain[task]['task_name']()
					flag = 1
					time.sleep(1)  # 此处最好停一秒 一秒内容易 可能会多次 在
					continue
				else:
					if flag == 1:
						self.task_contain[task]['task_start_time'] = self.task_contain[task]['task_start_time']+datetime.timedelta(
							**self.task_contain[task]['task_interval_time'])
						flag = 0

	def run_cron(self):
		for (task, task_prop) in self.task_contain.items():
			sthread = threading.Thread(target = self.add_task, args = (task, task_prop))
			sthread.start()

	def add_interval_function(self):
		pass


def task1():

	"""
	SDFADSF
	"""
	dest_file = 'crontab_copy.py'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	shutil.copy(r'D:\WebApp\MyLib\WebBackgroundProcessing\crontab_copy.py', dest_file)
	# with open(dest_file, 'wb+') as f:
	# 	f.truncate()

def task2():
	"""
	SDFADSF
	"""

	print '这是任务二', datetime.datetime.now()


if __name__ == '__main__':
	c = Crontab(
		{
			'任务一':{
				'task_start_time': datetime.datetime(2018, 5, 2, 17, 54, 10),
				'task_interval_time': {'seconds': 30},
				'task_name': task1,
				'pass': True
			},
			'任务二':{
				'task_start_time': datetime.datetime(2018, 5, 2, 17, 54, 10),
				'task_interval_time': {'seconds': 30},
				'task_name': task2,
				'pass': True
			},
		}

	)
	c.run_cron()


