#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
冒泡排序，时间复杂度为O(n^2)，稳定排序
'''


def bubble_sort(lists):
    count = len((lists))
    for i in range(count):  # 从0开始排序
        for j in range(1, count - i):
            if lists[j - 1] > lists[j]:
                lists[j - 1], lists[j] = lists[j], lists[j - 1]
                print("排序过程", lists)
    return lists


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print("排序前:", a)
b = bubble_sort(a)
print("排序后", b)
