#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
二叉树，类实现
'''


class BinTree():
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self.root.right = rightchild


# 引入栈
class Stack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow('in stack top()')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow('in stack pop()')
        return self._elems.pop()


def perorder_elements(self):  #
    t, s = self._root, Stack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()
