#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:11
# @Author  : sch
# @File    : read.py

import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
import pylab as pl
import datetime
import time
import os
import codecs

path = 'basic.csv'
path2 = 'data/basic.csv'
data1 = pd.read_csv(path2)
# print data1

data1.to_csv('basic_updated.csv', index=False)
#
# plt.figure()
# data1_counts = data1['company_enterprise_status'].value_counts()
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# data1_counts.plot(kind='barh')


# data1_counts2 = data1['enterprise_status'].value_counts()
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# data1_counts2.plot(kind='bar')

#es_kind =