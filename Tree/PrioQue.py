#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
优先队列   基于线性表list实现
'''


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
'''
类似二叉树,类似广度优先遍历
[5, 6, 4, 3, 2, 1]
        5
      6    4
    3  2  1
弹出优先级高的元素1后
        5
      6    4
    3   2
'''

p = PrioQue()
p.enqueue(5)
p.peek()  # [5]
p.enqueue(6)
p.peek()  # [5, 6]
p.enqueue(1)
p.peek()  # [5, 6, 1]
p.enqueue(4)
p.peek()  # [5, 6, 4, 1]
p.enqueue(3)
p.peek()  # [5, 6, 4, 3, 1]
p.enqueue(2)
p.peek()  # [5, 6, 4, 3, 2, 1]

print('----------')
p.dequeue()
p.peek()  # [5, 6, 4, 3, 2]
p.dequeue()
p.peek()  # [5, 6, 4, 3]
p.dequeue()
p.peek()  # [5, 6, 4]
p.dequeue()
p.peek()  # [5, 6]
p.dequeue()
p.peek()  # [5]

