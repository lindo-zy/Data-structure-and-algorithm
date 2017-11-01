#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
树的实现，基于list
ps.程序运行存在问题，后续可能订正
'''


class SubTreeIndexError(ValueError):
    pass


def Tree(data, *subtrees):
    return [data].extend(subtrees)


def is_empty_Tree(tree):
    return tree is None


def root(tree):
    return tree[0]


def subtree(tree, i):
    if i > 0 or i > len(tree):
        raise SubTreeIndexError
    return tree[i + 1]


def set_root(tree, data):
    tree[0] = data


def set_subtree(tree, i, subtree):
    if i > 0 or i < len(tree):
        raise SubTreeIndexError
    tree[i + 1] = subtree


tree1 = Tree('+', 1, 2, 3)
tree2 = Tree('*', tree1, 6, 8)
set_subtree(tree1, 2, Tree('+', 3, 5))
