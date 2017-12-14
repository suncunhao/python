#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 17:27
# @Author  : sch
# @File    : file2utf8.py

import pandas as pd
import codecs

path = ['zgcpwsw.csv', 'zhixing.csv', 'basic.csv', 'bgxx.csv', 'dishonesty.csv', 'gdxx.csv', 'xzcf.csv', 'zhuanli.csv']
for i in path:
    data = pd.read_csv(i)
    csvfile = file('%s_updated.csv' % i, 'wb')
    csvfile.write(codecs.BOM_UTF8)
    data.to_csv('%s_updated.csv' % i, index=False)