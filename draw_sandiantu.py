#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 15:42
# @Author  : sch
# @File    : draw_sandiantu.py

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

import numpy as np
x = np.random.rand(50, 30)
import matplotlib
import matplotlib.pyplot as plt

# basic
f1 = plt.figure(1)
plt.subplot(211)
plt.scatter(x[:, 1], x[:, 0])

# with label
plt.subplot(212)
label = list(np.ones(20)) + list(2 * np.ones(15)) + list(3 * np.ones(15))
label = np.array(label)
plt.scatter(x[:, 1], x[:, 0], 15.0 * label, 15.0 * label)

# with legend
f2 = plt.figure(2)
idx_1 = np.where(label == 1)
p1 = plt.scatter(x[idx_1, 1], x[idx_1, 0], marker='x', color='m', label='1', s=30)
idx_2 = np.where(label == 2)
p2 = plt.scatter(x[idx_2, 1], x[idx_2, 0], marker='+', color='c', label='2', s=50)
idx_3 = np.where(label == 3)
p3 = plt.scatter(x[idx_3, 1], x[idx_3, 0], marker='o', color='r', label='3', s=15)
plt.legend(loc='upper right')

import numpy as np

plt.figure(figsize=(9,6))
n = 1000
# rand:均匀分布 randn:高斯分布
x = np.random.randn(1, n)
y = np.random.randn(1, n)
T = np.arctan2(x, y)
plt.scatter(x, y, c=T, s=25, alpha=0.4, marker='o')
# T:散点的颜色 s：散点的大小 alpha：透明程度
plt.show
