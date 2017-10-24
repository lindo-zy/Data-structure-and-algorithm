#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
栈的应用，背包问题
递归实现
一个背包里可放入重量为weight的物品，现有n件物品的集合S，其中物品的
重量分别为，W0，W1，W2....W(n-1)。能否从中选出若干件物品，其重量和
为weight
'''

#weight   背包重量
#wlist    物品重量序列
#n         可选择个数

def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n - 1], wlist, n - 1):
        print('Item' + str(n) + ':', wlist[n - 1])
        return True
    if knap_rec(weight, wlist, n - 1):
        return True
    else:
        return False


print(knap_rec(10, [1, 2, 3, 4, 5], 5))#1 4 5
