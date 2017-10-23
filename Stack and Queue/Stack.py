#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
栈
'''


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


st1 = Stack()
st1.push(3)
st1.push(4)
while not st1.is_empty():
    print(st1.pop())
