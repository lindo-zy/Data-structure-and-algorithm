#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
josephus问题：假设n个人围坐一圈，从第K个人开始报数，报到m个数的人退出，
                然后下一个人接着报数，直到所有人退出
使用list实现   时间开销约为O(n^2)
'''


def josephus_L(n, k, m):
    people = list(range(1, n + 1))
    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=', ' if num > 1 else '\n')
    return


josephus_L(6, 1, 3)  # 退出顺序为3,6,4,2,5,1
