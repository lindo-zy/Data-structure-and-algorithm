#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
表达式求解  前缀式 如：('*',3,('+',2,5)) =3*(2+5)
'''


def make_sum(a, b):
    return ('+', a, b)


def make_prod(a, b):
    return ('*', a, b)


def make_diff(a, b):
    return ('-', a, b)


def make_div(a, b):
    return ('/', a, b)


def is_basic_exp(a):
    return not isinstance(a, tuple)


def is_number(x):
    return (isinstance(x, int) or isinstance(x, float)
            or isinstance(x, complex))


def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])  # **
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError('未知操作符:', op)


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_sum(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_diff(a, b)


def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_prod(a, b)


def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 1:
        return a
    if is_number(b) and b == 0:
        return ZeroDivisionError
    return make_div(a, b)


el = make_prod(3, make_sum(2, 5))  # ('*',3,('+',2,5)) =3*(2+5)
print(eval_exp(el))  # 21
