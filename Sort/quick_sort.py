#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
快速排序，时间复杂度O(n*logn)，不稳定算法
'''


def quick_sort(lists):
    def qsort(lists, begin, end):
        if begin >= end:
            return
        pivot = lists[begin]
        i = begin
        for j in range(begin + 1, end + 1):
            if lists[j] < pivot:
                i += 1
                lists[i], lists[j] = lists[j], lists[i]
        lists[begin], lists[i] = lists[i], lists[begin]
        qsort(lists, begin, i - 1)
        qsort(lists, i + 1, end)

    qsort(lists, 0, len(lists) - 1)
    return lists


a = [5, 10, 2, 7, 8]
print("排序前:", a)
b = quick_sort(a)
print("排序后", b)
