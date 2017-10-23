#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
表达式计算
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


class EStack(Stack):
    def depth(self):
        return len(self._elems)

    def suf_exp_evaluator(self, exp):
        operators = '+-*/'
        st = EStack()

        for x in exp:
            if x not in operators:
                st.push(float(x))
                continue
            if st.depth() < 2:
                raise SyntaxError('short of operand(s)')
            a = st.pop()
            b = st.pop()

            if x == '+':
                c = b + a

            elif x == '-':
                c = b - a
            elif x == '*':
                c = b * a
            elif x == '/':
                c = b / a
            else:
                break
            st.push(c)
        if st.depth() == 1:
            return st.pop()
        raise SyntaxError('Extra operand(s)')


def suffix_exp_calculator():
    while True:
        try:
            line = input('Suffix Expression:')
            if line == 'end': return
            res = suffix_exp_calculator(line)
            print(res)
        except Exception as e:
            print('Error', type(e), e.args)
