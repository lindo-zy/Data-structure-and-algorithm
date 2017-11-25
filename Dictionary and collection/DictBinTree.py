#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
二叉排序树(字典)类
'''


class DictBinTree():
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.rigth
            else:
                return entry.value
        return None
