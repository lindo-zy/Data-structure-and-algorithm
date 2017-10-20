#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
单链表  Singly linked list

'''

class LNode():      #定义结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

    def length(self, head):  # 获取链表长度
        p, n = head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def printall(self, head):  # 遍历链表所有元素
        p = head
        while p is not None:
            print(p.elem, end=' ')
            p = p.next


list1 = LNode(13)  # 头结点元素为 13
print('\n头结点元素：', list1.elem)
p = list1
for i in range(1, 5):  # 建立链表
    p.next = LNode(i)
    p = p.next
    # 生成了 13 1 2 3 4这个链表
p.printall(list1)  # 打印链表元素
print('\n链表长度为:', list1.length(head=list1))  # 链表长度
q = LNode(66)
q.next = list1.next  # 首部插入
list1.next = q
p.printall(list1)  # 变为 13 66 1 2 3 4

n = LNode(55)
pre = list1.next.next  # 一般插入
print('\n pre元素为：', pre.elem)#pre为第3个结点  元素值为1
n.next = pre.next
pre.next = n
n.printall(head=list1)  # 变为 13 66 1 55 2 3 4

print('\n 首部元素：', list1.elem)   #13
list1 = list1.next      #删除首部元素
print(' 首部元素：', list1.elem)     #66
list1.printall(list1)   # 66 1 55 2 3 4
pre.next=pre.next.next  #删除中间元素
print('\n 删除中间结点:')
list1.printall(list1)

