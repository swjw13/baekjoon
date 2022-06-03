# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

def solution(s):
    tmp = 0
    for i in s:
        if i == "(":
            tmp += 1
        else:
            if tmp == 0:
                return False
            else:
                tmp -= 1

    if tmp == 0:
        return True
    else:
        return False