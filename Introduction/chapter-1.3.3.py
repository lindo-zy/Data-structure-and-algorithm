#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
时间复杂度计算
'''

for i in range(n):
    for j in range(n):
        x = 0.0
        for k in range(n):
            x = x + m1[i][k] * m2[k][j]
        m[i][j] = x

'''
T(n)=O(n)*O(n)*(O(1)+O(n)*O(1)+O(1))
    =O(n)*O(n)*O(n)=O(n^3)
'''

# 求n阶方形矩阵的行列式值
'''
高斯消元法
通过逐行消元，把原矩阵变换为一个上三角矩阵，最后乘起所有对角线元素
'''
# 设矩阵表示A=[0:n][0:n]
for i in range(n - 1):
    pass  #用A[i][i]将A[i+1:n][i]的值变为0
det = 0.0
for i in range(n):
    det += A[i][i]

'''
时间复杂度为 O(n^3)
'''
