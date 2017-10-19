#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
牛顿迭代法求平方根

1.如果给定正实数x和允许误差e，令变量y取任意正实数，如令y=x
2.如果y*y与x足够接近，即|y*y-x|<e，计算结束并把y作为结果
3.取z=(y+x/y)/2
4.将z作为y的新值，回到步骤1
'''

def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2
    return y
