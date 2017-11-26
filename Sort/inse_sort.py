#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''

插入排序，时间复杂为O(n^2),稳定算法
'''


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i
        while j > 0 and lists[j - 1] > key:
            lists[j] = lists[j - 1]  # 反序逐个后移元素，确定插入位置
            j -= 1
        lists[j] = key
        print(lists)
    return lists


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print("排序前:", a)
b = insert_sort(a)
print("排序后", b)
