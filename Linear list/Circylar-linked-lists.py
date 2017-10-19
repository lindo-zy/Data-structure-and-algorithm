#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
循环链表
Circylar   linked   lists
'''


class LNode():
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
            p.next=p
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear.next=p
    def append(self,elem):  #尾部插入
        self.prepend(elem)
        self._rear=self._rear.next
    def pop(self):      #弹出元素
        if self._rear is None:
            raise LinkedListUnderflow('in pop of LCList')
        p=self._rear.next
        if self._rear is p:
            self._rear=None
        else:
            self._rear.next=p.next
        return p.elem
    def printall(self):     #输出链表
        if self.is_empty():
            return
        p=self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p=p.next
mlist = LCList()
for i in range(5):  #表首插入 5个元素
    mlist.prepend(i)    #4,3,2,1,0

for i in range(5, 10):  #表尾插入5个元素
    mlist.append(i)     #5,6,7,8,9
mlist.printall()        #4,3,2,1,0,5,6,7,8,9
print(mlist.pop())      #4

print(mlist.is_empty()) #False

