#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''

prime,最小生成树算法
'''
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


def Prim(Graph):
    vnum = Graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w, in Graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst
