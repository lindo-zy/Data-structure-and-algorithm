#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''

简单选择排序，时间复杂度为O(n^2),不稳定
'''


def select_sort(lists):
    count = len(lists)
    for i in range(count - 1):  # 循环count-1次
        min = i
        for j in range(i, count):  # min为已知最小元素的位置
            if lists[min] > lists[j]:
                min = j
                print("当前min值为:", min)
        if i != min:  # 确定lists[min]是确定最小元素，检查是否交换
            lists[i], lists[min] = lists[min], lists[i]
        print(lists)
    return lists


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print("排序前:", a)
b = select_sort(a)
print("排序后", b)
