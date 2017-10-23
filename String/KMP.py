#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
KMP算法匹配字符串
时间复杂度为O(n)
具体可参考 http://kb.cnblogs.com/page/176818/
            http://blog.csdn.net/lee18254290736/article/details/77278769

next[i]集合求法：s=abbcabcaabbcaa
next集合计算的是长度为len(s)-1的字符串的前后缀匹配长度的最大值

next[0]=-1  定义
next[1]=0   a 无匹配
next[2]=0   ab  无匹配
next[3]=0   abb 无匹配
next[4]=0   abbc 无匹配
next[5]=1   abbca 前缀:a,ab,abb,abbc
                  后缀:a,ca,bca,bbca  只有a满足，长度为1
next[6]=2   abbcab  前缀:a,ab,abb,abbc,abbca
                    后缀:a,ab,cab,bcab,bbcab  a和ab都匹配，取ab最大值为2
同理可求剩下的

'''


def KMP_matching(t, p, pnext):  # KMP算法
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1


def get_pnext(p):  # 获取next集合
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]

    return pnext


print(get_pnext('abbcabcaabbcaa'))  # [-1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 2, 3, 4, 5]


def advanced_pnext(p):  # 改进后的方法
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


print(advanced_pnext('abbcabcaabbcaa'))  # [-1, 0, 0, 0, -1, 0, 2, -1, 1, 0, 0, 0, -1, 5]

a = 'BBC ABCDAB ABCDABCDABDE'
b = 'ABCDABD'
p = 'ABCDABD'
print(KMP_matching(a, b, get_pnext(p)))  # 下标为 15
print(KMP_matching(a, b, advanced_pnext(p)))  # 下标为15
