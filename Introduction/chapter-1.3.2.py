#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
斐波那契数列
F0=F1=1, F(n)=F(n-1)+F(n-2)
'''


# 方法1        对于计算n较大时，时间代价过大,为指数增长
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 方法2        时间代价少，线性增长
def fib(n):
    f1 = f2 = 1
    for i in range(1, n):
        f1, f2 = f2, f1 + f2
    return f2
