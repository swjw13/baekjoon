# https://programmers.co.kr/learn/courses/30/lessons/12985
# 예상 대진표

def solution(n, a, b):
    i = 0
    while pow(2, i) != n:
        i += 1

    start = 1
    end = n
    while True:
        mid = (start + end) // 2 + 0.5
        if (a - mid) * (b - mid) < 0:
            return i
        elif a - mid > 0:
            start = int(mid + 0.5)
            i -= 1
        else:
            end = int(mid - 0.5)
            i -= 1
