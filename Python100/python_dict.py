# -*- coding: utf-8 -*-
"""
模块介绍:

创建者:

创建日期:
"""

list1 = [
	{'Denom': 100, 'Number': 15},
	{'Denom': 5, 'Number': 30},
	{'Denom': 10, 'Number': 55},
	{'Denom': 1, 'Number': 65},
	{'Denom': 50, 'Number': 1},
	{'Denom': 0.1, 'Number': 2},
	{'Denom': 0.5, 'Number': 6},
	{'Denom': 100, 'Number': 5},
	{'Denom': 100, 'Number': 4, 'Total': 400},
	{'Denom': 100, 'Number': 77, 'Total': 7700},
]


if __name__ == '__main__':
	# 将列表中的字典排序
	list1.sort(key=lambda x: (-x['Denom'], x['Number']))
	#

