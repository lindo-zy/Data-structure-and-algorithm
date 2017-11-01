#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
哈夫曼树
ps.程序无法测试，后续可能订正
'''


class BinTNdoe():  # 二叉树结点
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class HTNode(BinTNdoe):  # 哈夫曼树节点
    def __lt__(self, othernode):
        return self.data < othernode.data


# 引入优先队列
class PrioQueueError(ValueError):
    pass


class PrioQue():
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):

        i = len(self._elems) - 1
        while i > 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek()')
        print(self._elems)
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue()')

        return self._elems.pop()


class HuffmanPrioQ(PrioQue):  # 哈夫曼树类
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):  # 生成哈夫曼树
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()


