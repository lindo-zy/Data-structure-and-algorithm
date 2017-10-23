#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
josephus问题：假设n个人围坐一圈，从第K个人开始报数，报到m个数的人退出，
                然后下一个人接着报数，直到所有人退出
使用循环单链表实现   时间开销约为O(n)
'''


class LNode():  # 定义结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:  # 循环单链表
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):  # 尾部插入
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  # 弹出元素
        if self._rear is None:
            raise LinkedListUnderflow('in pop of LCList')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem


class josepthus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while not self.is_empty():
            self.turn(m - 1)
            print(self.pop(), end='\n' if self.is_empty() else ', ')


test = josepthus(6, 1, 3)
