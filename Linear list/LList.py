#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
page:85     LList()的实现
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
        j = 0
        p = self._head
        while p is not None:
            if p.elem == elem:
                print('元素 %s 的索引为 :%s' % (elem, j))
                return j
            p = p.next
            j += 1

    def printall(self):  # 打印出所有表
        p = self._head
        while p is not None:
            print('', p.elem, end='')
            if p.next is not None:
                print('', end='')
            p = p.next
        print('')

    def for_each(self):  # 链表遍历
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def find(self, pred):   #查找符合要求的元素，pred为lambda表达式
        p = self._head
        while p is not None:
            if pred(p.elem):
                print('\n符合的元素为:', p.elem)
                return p.elem
            p = p.next

    def filter(self, pred):  # 筛选生成器
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next



# 测试

mlist = LList()
for i in range(5):  # 表首插入 5个元素
    mlist.prepend(i)  # 4,3,2,1,0

for i in range(5, 10):  # 表尾插入5个元素
    mlist.append(i)  # 5,6,7,8,9
mlist.printall()  # 4,3,2,1,0,5,6,7,8,9

mlist.pop()  # 4
mlist.pop_last()  # 9

print('链表是否为空:', mlist.is_empty())  # False
mlist.printall()  # 3 2 1 0 5 6 7
mlist.getIndex(5)

for i  in mlist.for_each():  # 遍历
    print('%s' % i, end=' ')

mlist.find(pred=lambda i:2<i<8) #3

for i in mlist.filter(lambda i: 8>i > 2):
    print('\n', i, end='')  #3 5 6 7


