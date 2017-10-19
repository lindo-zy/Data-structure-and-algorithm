#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
交叉路口的红绿灯安排
思路：转化为涂色问题
'''


def coloring(G):
    color = 0
    groups = set()
    verts = vertices(G)  # 取得G的所有顶点
    while verts:
        new_group=set()
        for v in list(verts):
            if not_adjacent_with_set(v,new_group,G):
                new_group.add(v)
                verts.remove(v)
            groups.add((color,new_group))
            color+=1
        return groups
