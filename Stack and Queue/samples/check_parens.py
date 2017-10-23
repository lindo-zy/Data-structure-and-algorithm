#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
栈的应用
括号匹配问题,
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


def check_parens(text):
    parens = '()[]{}'  # 所有括号字符
    open_parens = '([{'  # 开括号字符
    oppsite = {')': '(',
               ']': '[',
               '}': '{'}


    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = Stack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != oppsite[pr]:
            print('匹配失败')
            return False
        else:
            pass
    print('所有符号匹配成功')
    return True
check_parens('{([]})')  #匹配失败