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



# link: https://zhuanlan.zhihu.com/p/27570774
#       https://zhuanlan.zhihu.com/p/27593869
#       https://zhuanlan.zhihu.com/p/27683042
#       https://zhuanlan.zhihu.com/p/27816821


# 第三章 分布数据集的可视化
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as pip
import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, 'distributions')))

# # 单变量分布
x = np.random.normal(size=100)
sns.distplot(x)
# # 直方图
sns.distplot(x, kde=False, rug=True)
sns.distplot(x, bins=20, kde=False, rug=True)
# # 核密度估计KDE
sns.distplot(x, hist=False, rug=True)
# # 散点图
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x='x', y='y', data=df)
# # HexBin图
x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k")
# #核密度估计
sns.jointplot(x='x', y='y', data=df, kind='kde')

f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax)

f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)

g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$")

# #呈现数据集中成对的关系
iris = sns.load_dataset('iris')
sns.pairplot(iris)

g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6)


# 第四章 线性关系的可视化
tips = sns.load_dataset("tips")

# # 绘制线性回归模型的函数
sns.regplot(x='total_bill', y='tip', data=tips)
sns.lmplot(x="total_bill", y="tip", data=tips)
sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05)
sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)

# 不同模型的线性拟合
anscombe = sns.load_dataset("anscombe")
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80})

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80})

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80})

# #调节其他变量
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1")

sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips)

sns.lmplot(x="total_bill", y="tip", hue="smoker",
           col="time", row="sex", data=tips)

# 分类数据的绘制
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# #分类散点图
sns.stripplot(x='day', y='total_bill', data=tips)
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)

sns.swarmplot(x="total_bill", y="day", hue="time", data=tips)

# #分类内的观测分布
# #箱线图
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
# #提琴图
sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)

# #类别内的统计估计
# #条形图
sns.barplot(x='sex', y='survived', hue='class', data=titanic)
sns.countplot(x="deck", data=titanic, palette="Greens_d")
sns.countplot(y="deck", hue="class", data=titanic, palette="Greens_d")
# #点图
sns.pointplot(x="sex", y="survived", hue="class", data=titanic)

# #绘制多层面板分类图
sns.factorplot(x='day', y='total_bill', hue='smoker', data=tips)
sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar")

sns.factorplot(x="day", y="total_bill", hue="smoker",
               col="time", data=tips, kind="swarm")
'''
seaborn.factorplot(x=None, y=None, hue=None, data=None, row=None, col=None, col_wrap=None, estimator=<function mean>, ci=95, n_boot=1000, units=None, order=None, hue_order=None, row_order=None, col_order=None, kind='point', size=4, aspect=1, orient=None, color=None, palette=None, legend=True, legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, **kwargs)

Parameters：

x,y,hue                     数据集变量 变量名
date                        数据集 数据集名
row,col                     更多分类变量进行平铺显示 变量名
col_wrap                    每行的最高平铺数 整数
estimator                   在每个分类中进行矢量到标量的映射 矢量
ci                          置信区间 浮点数或None
n_boot                      计算置信区间时使用的引导迭代次数 整数
units                       采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
order, hue_order            对应排序列表 字符串列表
row_order, col_order        对应排序列表 字符串列表
kind :                      可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，swarm 分散点（具体图形参考文章前部的分类介绍）
size                        每个面的高度（英寸） 标量
aspect                      纵横比 标量
orient                      方向 "v"/"h"
color                       颜色 matplotlib颜色
palette                     调色板 seaborn颜色色板或字典
legend                      hue的信息面板 True/False
legend_out                  是否扩展图形，并将信息框绘制在中心右边 True/False
share{x,y}                  共享轴线 True/False
facet_kws                   FacetGrid的其他参数 字典
'''

# 第六章 绘制数据网格
# 用FaceGrid子集数据
g = sns.FacetGrid(tips, col="time")

g = sns.FacetGrid(tips, col="time")
g.map(plt.hist, "tip")

g = sns.FacetGrid(tips, col="sex", hue="smoker")
g.map(plt.scatter, "total_bill", "tip", alpha=.7)
g.add_legend()

# #用PairGrid and pairplot()绘制成对的关系
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter)

g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

g = sns.PairGrid(iris, hue="species")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()

g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
g.map(plt.scatter)

g = sns.PairGrid(iris)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_diag(sns.kdeplot, lw=3, legend=False)