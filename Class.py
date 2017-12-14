#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/7 14:59
# @Author  : sch
# @File    : Class.py

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

import pandas as pd
import numpy as np

class FooClass(object):
    # """my very first class: FooClass"""
    version = 0.1 # class (data) attribute
    def __init__(self, nm='John Doe'):
    # """constructor"""
        self.name = nm # class instance (data) attribute
        print('Created a class instance for', nm)
    def showname(self):
    # """display instance attribute and class name"""
        print('Your name is', self.name)
        print('My name is', self.__class__.__name__)
    def showver(self):
    # """display class(static) attribute"""
        print(self.version) # references FooClass.version
    def addMe2Me(self, x): # does not use 'self'
    # """apply + operation to argument"""
        return x + x
# 类
class AddrBookEntry(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print('Created instance for:', self.name)
    def updatePhone(self,newph):
        self.phone = newph
        print('Updated phone# for:', self.name)

john = AddrBookEntry('john','8848')
john.name
john.phone
john
john.updatePhone('884')
john.phone
# 子类
class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print('Updated email address for:', self.name)

john = EmplAddrBookEntry('john', '8848', '4444', 'john@gmail.com')
john.email
john.updateEmail('johnn@gmail.com')
john.email

