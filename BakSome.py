# -*- coding: utf-8 -*-
import shutil
import datetime
import os
import sys
from functools import wraps


def blank_check(func):
	@wraps(func)
	def wrap(self):
		if not os.path.exists(self.src_full_name):
			raise ValueError('源文件目录不存在')
		else:
			return func(self)
	return wrap


class BackUpsBase(object):
	"""
		镜像备份文件目录 （可指定目录下的那些文件可选）
	"""
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			orig = super(BackUpsBase, cls)
			cls._instance = orig.__new__(cls)
		return cls._instance

	def __init__(self, src_full_name=None, filter_list=None, value_list=None):
		"""

		:param src_full_name: 带绝对路径的源文件
		:param filter_list: 要过滤掉的文件
		:param value_list: 要指定复制的文件
		"""
		self.src_full_name = src_full_name
		self.file_full_name_str = self.src_full_name or r'C:\Users\lenovo\Desktop\test'
		self.file_full_name_lis, self.file_name = self._sys()

		# 需要忽略的那些文件
		self.filter_list = [
			'*.pyc', 'tmp*'
		] + list(filter_list or [])

		# 需要复制那些文件
		self.value_list = [
			'device.html'
		] + list(value_list or [])
		self.src_full_name = self._src_full_dir()
		self._filter_file()
		# 生成带绝对路径的目标
		self.dest_full_name = self._dest_full_dir()

	def _sys(self):
		# 根据系统组织路径 以及 取 文件名
		if sys.platform.startswith('win'):
			self.file_full_name_lis = self.file_full_name_str.split('\\')
			self.file_name = self.file_full_name_lis[-1]
		if sys.platform.startswith('linux'):
			self.file_full_name_lis = self.file_full_name_str.split('/')
			self.file_name = self.file_full_name_lis[-1]
		return self.file_full_name_lis, self.file_name

	def _src_full_dir(self):
		# 生成源文件的绝对路径
		return os.path.join(*self.file_full_name_lis)

	def _dest_full_dir(self):
		# 生成目标文件的绝对路径
		return os.path.join(os.path.abspath('.'), self.file_name + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

	def _filter_file(self):
		for root, dirs, files in os.walk(self.src_full_name, topdown=False):
			for name in files:
				if '*' in self.value_list:
					self.filter_list = []
					break
				# 复制时忽略 哪些文件
				if name not in self.value_list:
					self.filter_list.append(name)

	@blank_check
	def copy_file(self):
		# print (os.path.exists(self.src_full_name))
		# 将源文件复制到目标文件
		try:
			shutil.copytree(self.src_full_name, self.dest_full_name, ignore=shutil.ignore_patterns(*self.filter_list))
		except Exception as e:
			print (e)
		# 递归删除空文件
		for root, dirs, files in os.walk(self.dest_full_name, topdown=False):
			# print (root, dirs, files)
			for name in dirs:
				dir_full_name = os.path.join(root, name)
				if not os.listdir(dir_full_name):
					os.rmdir(dir_full_name)
		return self.dest_full_name

	def make_archive(self):
		# 生成压缩包 在当目录
		shutil.make_archive(self.dest_full_name, 'zip', root_dir = self.dest_full_name)
		# bztar
		return self.dest_full_name+'.zip'

	def __call__(self, *args, **kwargs):
		return


if __name__ == '__main__':
	# print ('D:\\WebApp\MyLib\\Tviews_X_dev_20180417150034\\'.rsplit('/' or '\\'))
	# bak_select(r'C:\Users\lenovo\Desktop\test')
	b = BackUpsBase(src_full_name = r'C:\Users\lenovo\Desktop\workfile\EasyPay_Dev\Tviews_X_dev', value_list = [
		'device.html'])
	print (b.copy_file())
	print (b.make_archive())
	# shutil.make_archive('Tviews_X_dev_20180417150034', 'zip', root_dir ='D:\\WebApp\MyLib\\Tviews_X_dev_20180417150034\\')
