#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
写一个函数，求出在一个python程序里面出现的所有整数之和
'''

import re


def sumInt(fname):
    re_int = r'\b(0|[1-9]\d*)\b'
    inf = open(fname)
    if inf == None:
        return 0
    int_list = map(int, re.findall(re_int, inf.read()))
    s = 0
    for i in int_list:
        s += i
    return s
