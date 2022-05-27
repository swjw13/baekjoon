# https://programmers.co.kr/learn/courses/30/lessons/12929
# 올바른 괄호 갯수

import sys

sys.setrecursionlimit(10 ** 9)
answer = 0


def solution(n):
    def find(one, two):
        global answer
        if one == n and two == n:
            answer += 1
        elif one > n or two > n:
            return
        elif one < two:
            return
        else:
            find(one + 1, two)
            find(one, two + 1)

    find(0, 0)

    return answer


a = 2
print(solution(2))
