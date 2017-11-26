#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
快速排序，时间复杂度O(n*logn)，不稳定算法
'''


def quick_sort(lists, left, right):  # left为最左元素索引0，rigth为最右元素索引len(lists)-1
    if left >= right:  # list只有一个元素或者无元素
        return lists
    pivot = lists[left]  # 设左边元素为 轴心元素
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= pivot:  # 从右开始查找第一个大于轴心元素的元素
            right -= 1  # 查找成功左移一位
        lists[left] = lists[right]  # 左边元素和当前右边元素交换
        while left < right and lists[left] <= pivot:  # 从左开始查找第一个小于轴心元素的元素
            left += 1  # 查找成功右移一位
        lists[right] = lists[left]  # 右边元素和当前左边元素交换
    lists[right] = pivot  # 查找完成，设置当前右边元素为轴心元素
    print("排序过程:", lists)
    quick_sort(lists, low, left - 1)  # 左边部分递归
    quick_sort(lists, left + 1, high)  # 右边部分递归
    return lists


a = [6, 1, 2, 7, 9, 3, 4 ,5 ,10 ,8]
print("排序前:", a)
b = quick_sort(a, 0, len(a) - 1)
print("排序后", b)
