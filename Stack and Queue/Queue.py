#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Queue 队列
基于顺序表实现
'''


class SQueue():
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):  # 判断队列是否为空
        return self._num == 0

    def peek(self):  # 查看当前队首元素
        if self._num == 0:
            raise QueueUnderflow('Error in peek()')
        return self._elems[self._head]

    def dequeue(self):  # 出队列
        if self._num == 0:
            raise QueueUnderflow('Error in dequeue()')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):  # 入队列
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


s = SQueue()
for i in range(1, 10):  # 1-9进入队列
    s.enqueue(i)
for i in range(1, 5):  # 1-4出队列
    s.dequeue()
print(s.peek())  # 当前队列第一个为5
