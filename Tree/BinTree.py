#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
二叉树  列表实现
'''


def BinTree(data, left=None, right=None):
    return [data, left, right]


def is_empty(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, left):
    btree[1] = left


def set_right(btree, right):
    btree[2] = right()

t1=BinTree(2,BinTree(4),BinTree(8))
#相当于 t1=[2,[4,None,None],[8,None,None]]
