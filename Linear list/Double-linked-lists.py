#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
双链表
Double   linked   lists
'''


class LNode():  # 结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList():  # 链表类
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
        print('pop :', e)
        return e

    def pop_last(self):  # 弹出最后一个元素
        if self._head is None:
            raise LinkedListUderflow('in pop_last')
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            print('pop_last :', e)
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        print('pop_last :', e)
        return e

    def getIndex(self, elem):  # 获取元素索引
        index = 0
        p = self._head
        while p is not None:
            if p.elem == elem:
                print('元素 %s 的索引为 :%s' % (elem, index))
                return index
            p = p.next
            index += 1

    def printall(self):  # 打印出所有表
        p = self._head
        while p is not None:
            print('', p.elem, end='')
            if p.next is not None:
                print('', end='')
            p = p.next
        print('')

    def length(self):  # 获取链表长度
        p, n = self._head, 1
        while p is not None:
            n += 1
            p = p.next
        print('当前链表长度为：', n)
        return n

    def for_each(self):  # 链表遍历
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def find(self, pred):  # 查找符合要求的元素，pred为表达式
        p = self._head
        while p is not None:
            if pred(p.elem):
                print('\n符合的元素为:', p.elem)
                return p.elem
            p = p.next

    def filter(self, pred):  # 筛选生成器,pred为表达式
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


class DLNode(LNode):  # 双链表结点
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList):  # 双链表类
    def __init__(self):
        LList.__init__(self)

    def prepend(self, elem):  # 首端插入
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop of DLList')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last of DLList')
        e = self._rear.elem
        self._rear = self._rear.next
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

mlist=DLList()
for i in range(5):
    mlist.prepend(i)
mlist.printall()
for i in range(5,10):
    mlist.append(i)
mlist.printall()