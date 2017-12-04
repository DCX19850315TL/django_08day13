#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: common.py
@time: 2017/12/4 15:53
'''
def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception,e:
        arg = default
    return arg