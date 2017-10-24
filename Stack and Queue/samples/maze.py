#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
迷宫问题，基于递归实现
'''

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东西南北方向


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2  # 给迷宫maze的位置pos标2 表示’到过了‘


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0  # 检查迷宫maze的位置pos是否可行


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:  # 已到达出口
        print(pos, end=' ')  # 输出这个位置
        return True
    for i in range(4):  # 按四个方向探查
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=' ')
                return True
    return False


maze = [[0, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 0]]
pos = (0, 0)  # 起点
end = (3, 2)  # 终点
find_path(maze, pos, end)  # (3, 2) (3, 1) (2, 1) (1, 1) (0, 1) (0, 0)
