#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
基数排序，时间复杂度O(m*nlogn)，稳定算法
'''

import math


def radix_sort(lists, radix=10):  # 基数为10
    k = int(math.ceil(math.log(max(lists), radix)))  # 先取对数，再向上取整，用k位可表示任意整数
    bucket = [[] for i in range(radix)]  # 建立记录桶
    for i in range(1, k + 1):  # k次循环
        for j in lists:
            bucket[int(j / (radix ** (i - 1)) % (radix ** i))].append(j)  # 取生素第K位数
        del lists[:]
        for z in bucket:
            lists += z  # 合并桶
            del z[:]
    return lists


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print("排序前：", a)
b = radix_sort(a)
print("排序后：", b)
