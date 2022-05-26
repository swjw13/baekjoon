# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413
# kakao 2021

import sys


def solution(n, s, a, b, fares):
    lines = {j: {i: sys.maxsize for i in range(1, n + 1)} for j in range(1, n + 1)}
    for city1, city2, length in fares:
        lines[city1][city2] = length
        lines[city2][city1] = length

    for i in range(1, n + 1):
        lines[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if lines[i][j] > lines[i][k] + lines[k][j]:
                    lines[i][j] = lines[i][k] + lines[k][j]

    mn = lines[s][a] + lines[s][b]
    for i in range(1, n + 1):
        mn = min(mn, lines[s][i] + lines[i][a] + lines[i][b])

    return mn
