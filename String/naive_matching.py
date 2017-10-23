#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
字符串的匹配
朴素的串匹配法   效率极低O(m*n)
'''


def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:  # i==m时匹配
        if p[i] == t[j]:    #字符相同，找下一个字符
            i, j = i + 1, j + 1
        else:               #字符不同，找t中下一位置
            i, j = 0, j - i + 1
    if i == m:
        return j - 1  # 匹配成功 返回下标
    return -1  # 无匹配 返回-1


print(naive_matching('hello', 'o'))  # 4
print(naive_matching('hello', '0'))  # -1
