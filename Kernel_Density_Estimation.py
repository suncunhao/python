#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 9:20
# @Author  : sch
# @File    : Kernel_Density_Estimation.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.distributions.mixture_rvs import mixture_rvs

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

np.random.seed(12345)
