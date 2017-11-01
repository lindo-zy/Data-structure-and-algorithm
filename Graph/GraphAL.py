#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
图，邻接表实现
ps.程序未测试，后续将进行测试
'''
# 引入邻接矩阵
inf = float('inf')  # inf的值比任何float值都大


class GraphError():
    pass


class Graph():
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError('Argument for "Graph"')
            self._mat = [mat[i][:] for i in range(vnum)]  # 做拷贝
            self._unconn = unconn
            self, _vnum = vnum

    def vertext_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError('Adj-Matrix does not support "add_vertex"')

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        return self._mat[vi][vj]

    def out_edge(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + 'is not a valid vertex')
        return self.out_edge(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
            return edges


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argument for "GraphAL"')
            self._mat = [Graph.out_edge(mat[i], unconn) for i in range(vnum)]
            self._vnum = vnum
            self._unconn = unconn

    def add_vertex(self):  # 增加新顶点时安排一个新编号
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError('Cannot add edge to empty graph')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not valid vertex')
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 修改mat[vi][vj]的值
                self._mat[vi][vj] = (vj, val)
                return
            if row[i][0] > vj:  # 原来没有到vj的边，退出循环后加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        for i, val in self._mat[vi]:
            if i == vj:
                return val
            return self._unconn

    def out_edge(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + 'is not a valid vertex')
        return self._mat[vi]
