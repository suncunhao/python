#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 17:15
# @Author  : sch
# @File    : About_seaborn.py
# data:https://github.com/mwaskom/seaborn-data
# from:http://blog.csdn.net/qq_34264472/article/details/53814653
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import datasets

# 柱状图以及密度曲线图
df_iris = datasets.load_iris()
data = df_iris.data[:,3]
fig, axes = plt.subplots(1, 2)
sns.distplot(data, ax=axes[0], kde=True, rug=True)
sns.kdeplot(data, ax=axes[1], shade=True)
plt.show()

rs = np.random.RandomState(10)
d = rs.normal(size=100)
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
sns.distplot(d, color="m", ax=axes[1, 1])
plt.show()

# 箱型图
sns.boxplot(x=df_iris.target, y=df_iris.data[:,0])
plt.show()

sns.set(style="ticks")
sns.boxplot(x=df_iris.data[:, 0], y=df_iris.data[:, 1], hue=df_iris.target, data=data, palette="PRGn")   #palette 调色板
plt.show()

# 联合分布jointplot()
sns.jointplot("total_bill", "tip", tips)
plt.show()

sns.jointplot("total_bill", "tip", tips, kind='reg')
plt.show()

# pairplot()
# var主要适用于分类变量，hue为想进行分类的指标
sns.pairplot(iris, hue="species")   #hue 选择分类列
plt.show()

sns.pairplot(iris, vars=["sepal_width", "sepal_length"],hue='species',palette="husl")
plt.show()

# FacetGrid()
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill",  color="r")
plt.show()

mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
data['new_credit_rating_2014'] = data['credit_rating_2014'].map(mapping)
data['new_credit_rating_2015'] = data['credit_rating_2015'].map(mapping)
sns.jointplot('new_credit_rating_2014', 'new_credit_rating_2015', data, kind='reg')
sns.jointplot('credit_ration_2015', 'credit_ration_2016', data, kind='reg')
sns.jointplot('goal_2015', 'goal_2016', data, kind='reg')

