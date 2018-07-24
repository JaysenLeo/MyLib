# -*- coding: utf-8 -*-
"""
安装包 sckit-learn anaconda
"""

import csv
from sklearn.feature_extraction import DictVectorizer # 数据类型转化
from sklearn import (
	preprocessing,
	tree
)


all_electronics = open(r'D:\WebApp\MyLib\MachineLearningLibrary\DecisionTree\AllElectronics.csv', 'rt')
reader = csv.reader(all_electronics)
# 获取csv的表头
headers = next(reader)

feature_list = []
label_list = []
for row in reader:
	label_list.append(row[len(row) - 1]) # 去每行最后一个值
	row_dict = {}
	for i in range(1, len(row) - 1):
		row_dict[headers[i]] = row[i]
	feature_list.append(row_dict) # 将表头作为 key 和 每行row内容进行字典组装成键值化的特征列表

# 将键值化的特征列表 进行转化 将多维类型转化为二维类型
vec = DictVectorizer()
dummy_x = vec.fit_transform(feature_list).toarray()
print(vec.get_feature_names())
# print(dummy_x)

label = preprocessing.LabelBinarizer()
dummy_y = label.fit_transform(label_list)
# print(dummy_y)

# 创建决策树
clf = tree.DecisionTreeClassifier(criterion = 'entropy') # 创建分类器 用ID3的算法（即信息熵的差）
clf = clf.fit(dummy_x, dummy_y)
# print('clf: ' + str(clf)) # 打印决策树信息

# 可视化
with open("allElectronicInformationGainOri.dot", 'w') as f:
	f = tree.export_graphviz(clf, feature_names = vec.get_feature_names(), out_file = f) # 还原特征名称 vec.get_feature_names()
# Graphviz 查看 dot -T pdf allElectronicInformationGainOri.dot -o allElectronicInformationGainOri.pdf

# 预测
# 取第一行预测
one_row_x = dummy_x[0, :]
print("first row " + str(one_row_x))
pred_row_x = one_row_x

# 改动第一个值和第三个值
pred_row_x[0] = 1
pred_row_x[2] = 0
print("pred_row_x row " + str(pred_row_x))
predicted_y = clf.predict(pred_row_x.reshape(1, -1))
print('predicted_y: ', predicted_y)