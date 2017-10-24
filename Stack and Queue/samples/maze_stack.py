#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
迷宫问题基于栈回溯求解
ps.程序存在问题，end为(3,2)时，迷宫无出路
'''


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


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东西南北方向


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2  # 给迷宫maze的位置pos标2 表示’到过了‘


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0  # 检查迷宫maze的位置pos是否可行


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = Stack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()

        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0],pos[1] + dirs[i][0])
            if nextp == end:
                print(end, pos, st)
                return
            if passable(maze, nextp):
                st.push((pos, i + 1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print('迷宫没有出路')


maze = [[0, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 0]]
start = (0,0)
end = (3,2)
maze_solver(maze, start, end)
