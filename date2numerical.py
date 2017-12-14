
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 16:54
# @Author  : sch
# @File    : date2numerical.py

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

import pandas as pd

## date - numerical
x = data.loc[1,'openfrom']
y = pd.Timestamp(x)
z = y.strftime('%Y%m%d')
o = int(z)
y.year
y.month
y.day

df = pd.to_datetime(data['esdate'], format='%Y-%m-%d')
df_y = df.apply(lambda x: x.year)
df_m = df.apply(lambda x: x.month)
df_d = df.apply(lambda x: x.day)
df2 = df_y*10000 + df_m*100 + df_d
