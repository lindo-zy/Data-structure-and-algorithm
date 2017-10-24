#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
迷宫问题
基于队列求解
ps.程序存在问题,将end改为(3,2)报错
'''


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


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东西南北方向


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2  # 给迷宫maze的位置pos标2 表示’到过了‘


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0  # 检查迷宫maze的位置pos是否可行


def maze_solver_queue(maze, start, end):
    if start == end:
        print('找到路径')
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print('找到路径')
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)
    print('迷宫无出路')


maze = [[0, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
        ]
start = (0, 0)
end = (2, 1)
maze_solver_queue(maze, start, end)
