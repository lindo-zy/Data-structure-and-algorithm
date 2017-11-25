#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
改进的冒泡排序
'''


def bubble_sort_advance(lists):
    count = len(lists)
    for i in range(count):
        found = False
        for j in range(1, count - i):
            if lists[j - 1] > lists[j]:
                lists[j - 1], lists[j] = lists[j], lists[j - 1]
                print("排序过程:", lists)
            found = True
            if not found:
                break

    return lists


a = [5, 10, 2, 7, 8]
print("排序前:", a)
b = bubble_sort_advance(a)
print("排序后", b)
