# https://programmers.co.kr/learn/courses/30/lessons/12936
# 줄 서는 방법

import math


def solution(n, k):
    answer = []
    k -= 1

    tmp = [i for i in range(1, n + 1)]
    while len(tmp) > 0:
        length = len(tmp)
        num = math.factorial(length - 1)
        idx = k // num
        answer.append(tmp[idx])
        tmp.pop(idx)
        k = k % num

    return answer

n = 3
k = 5
print(solution(n, k))