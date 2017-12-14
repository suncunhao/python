#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 17:39
# @Author  : sch
# @File    : xlsx2csv.py

import xlrd
import pandas as pd
import csv
import codecs

data = pd.read_clipboard(header=None)
print data
data.head()
csvfile = open('V1_updated.csv','wb')
csvfile.write(codecs.BOM_UTF8)
data.to_csv('V1_updated.csv', index=False)
