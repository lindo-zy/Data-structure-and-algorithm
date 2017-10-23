#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Linked-stack.py
链栈
'''


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow('in LStack top()')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow('in LStack pop()')
        p = self._top
        self._top = p.next
        return p.elem


st = LStack()
st.push(1)
st.push(2)
print(st.top())
