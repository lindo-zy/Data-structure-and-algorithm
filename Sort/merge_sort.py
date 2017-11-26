#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
归并排序,时间复杂度O(n*logn)，稳定算法
'''


def merge(left, rigth):
    i, j = 0, 0
    result = []  # 缓存列表
    while i < len(left) and j < len(rigth):
        if left[i] <= rigth[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(rigth[j])
            j += 1
    result += left[i:]
    result += rigth[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:  # 判断列表长度
        return lists
    num = len(lists) // 2  # 使用//取整
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print("排序前:", a)
b = merge_sort(a)
print("排序后", b)
