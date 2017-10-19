#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
单链表  Singly linked list

'''


# 定义一个表结点类
class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


llist1 = LNode(1)
p = llist1
for i in range(2, 11):  #建立链表 元素1到10
    p.next = LNode(i)
    p = p.next
p = llist1
while p is not None:    #遍历链表
    print(p.elem)
    p = p.next

'''
表首插入  首部插入13
'''
q = LNode(13)
q.next = head.next
head = q

'''
一般插入    插入13
'''
q = LNode(13)
q.next = pre.next
pre.next = q

'''
删除元素   删除首部
'''
head = head.next

'''
一般情况删除
'''
pre.next = pre.next.next

'''
扫描链表
'''
p = head
while p is not None and other('其他条件'):
    # 对p所指结点里的数据操作
    p = p.next

'''
按下标定位扫描 
'''
p = head
while p is not None and i > 0:
    i -= 1
    p = p.next

'''
按元素定位扫描
'''
p = head
while p is not None and not pred(p.elem):
    p = p.next

'''
遍历
'''
p = head
while p is not None:
    print(p.elem)
    p = p.next

'''
求链表长度
'''

def length(head):
    p, n = head, 0
    while p is not None:
        n += 1
        p = p.next
    return n
