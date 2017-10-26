#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
二叉树结点类
ps.广度优先遍历存在问题，后续可能订正
'''


class BinTNdoe():  # 二叉树结点
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_BinTNodes(t):  # 统计树中结点个数
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNodes(t):  # 求二叉树结点数值和
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


def preoder(t):  # 先根遍历,递归的方式
    if t is None:
        return
    print(t.data, end=',')
    preoder(t.left)
    preoder(t.right)


def print_BinTNodes(t):  # 打印二叉树
    if t is None:
        print('^', end='')  # 空树用^表示
        return
    print('(' + str(t.data), end='')
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(')', end='')


'''
树如图
        1
     2     3
   5   ^  ^  ^
  ^  ^

'''
t = BinTNdoe(1, BinTNdoe(2, BinTNdoe(5)), BinTNdoe(3))
print_BinTNodes(t)  # (1(2(5^^)^)(3^^))
print('\n', count_BinTNodes(t))  # 4
print('\n', sum_BinTNodes(t))  # 11
preoder(t)  # 1,2,5,3


# 引入队列
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


def levelorder(t, proc):  # 广度优先遍历
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)


# 引入栈
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


def preorder_nonrec(t):  # 先根遍历，非递归
    s = Stack()
    while t is not None or not s.is_empty():
        while t is not None:
            print(t.data, end=',')
            s.push(t.right)
            t = t.left
        t = s.pop()


print('\n')
preorder_nonrec(t)


def preorder_elements(t):  # 先根遍历，生成器
    s = Stack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()
        print(t)


def postorder_nonrec(t):  # 后根遍历，非递归
    s = Stack()
    while t is not None or s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        print(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None
