# https://programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전

from collections import deque


def solution(s):
    answer = 0
    s = deque(list(s))
    length = len(s)

    def right(line):
        stack = []
        for i in line:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                word = None
                if i == "}":
                    word = "{"
                elif i == ")":
                    word = "("
                elif i == "]":
                    word = "["
                if len(stack) == 0 or stack[-1] != word:
                    return False
                else:
                    stack.pop(-1)
        if len(stack) == 0:
            return True
        else:
            return False

    for i in range(length):
        s.rotate(-1)
        if right(s):
            answer += 1

    return answer

a = "([{)}]"
print(solution(a))