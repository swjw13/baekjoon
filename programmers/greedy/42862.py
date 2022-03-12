# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n
    lost.sort()
    no_clear = []
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        elif i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            no_clear.append(i)
    return answer - len(no_clear)
