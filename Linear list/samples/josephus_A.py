#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
josephus问题：假设n个人围坐一圈，从第K个人开始报数，报到m个数的人退出，
                然后下一个人接着报数，直到所有人退出
基于数组概念实现   时间开销约为O(n*m)
'''


def josephus_A(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n
            if num < n - 1:
                print(', ', end=' ')
            else:
                print(' ')
    return


josephus_A(6, 1, 3)  # 输出 1
