#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
优先队列，基于堆实现
'''


class PrioQueueError():
    pass


class PrioQueue():
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek()')
        print(self._elems)
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue()')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)

'''
#堆排序
def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)
'''

'''
此堆为 小顶堆
[1, 3, 2, 6, 4, 5]
        1
     3      2
   6   4   5
弹出优先级最高的元素1 后，重新构成一个小顶堆
        2
     3     5
   6   4

'''
p = PrioQueue()

p.enqueue(5)
p.peek()  # [5]
p.enqueue(6)
p.peek()  # [5, 6]
p.enqueue(1)
p.peek()  # [1, 6, 5]
p.enqueue(4)
p.peek()  # [1, 4, 5, 6]
p.enqueue(3)
p.peek()  # [1, 3, 5, 6, 4]
p.enqueue(2)
p.peek()  # [1, 3, 2, 6, 4, 5]


print('----------')
p.dequeue()
p.peek()  # [2, 3, 5, 6, 4]
p.dequeue()
p.peek()  # [3, 4, 5, 6]
p.dequeue()
p.peek()  # [4, 6, 5]
p.dequeue()
p.peek()  # [5, 6]
p.dequeue()
p.peek()  # [6]
