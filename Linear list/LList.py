#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
page:85
'''


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList():
    def __init__(self):
        self._head = None

    def is_empty(self):  # 判断链表 是否为空
        return self._head is None

    def prepend(self, elem):  # 首部插入
        self._head = LNode(elem, self._head)

    def append(self, elem):  # 一般插入
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):  # 弹出元素
        if self._head is None:  # 无结点引发异常
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):     #弹出最后一个元素
        if self._head is None:
            raise LinkedListUderflow('in pop_lat')
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):   #查找元素
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):  # 打印出所有表
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print(' ')

    def for_each(self, proc):  # 链表遍历
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next


# 测试

mlist = LList()
for i in range(5):  #表首插入 5个元素
    mlist.prepend(i)    #4,3,2,1,0

for i in range(5, 10):  #表尾插入5个元素
    mlist.append(i)     #5,6,7,8,9
mlist.printall()        #4,3,2,1,0,5,6,7,8,9
print(mlist.pop())      #4
print(mlist.pop_last()) #9
print(mlist.is_empty()) #False


