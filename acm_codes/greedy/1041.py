# https://www.acmicpc.net/problem/1041
# 주사위

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print(sum(lst) - max(lst))
else:
    one_total = ((N - 2) * (N - 1) * 4 + (N - 2) ** 2) * min(lst)

    mn = sys.maxsize
    for i in combinations([0, 1, 2, 3, 4, 5], 2):
        if sum(i) != 5:
            if lst[i[0]] + lst[i[1]] < mn:
                mn = lst[i[0]] + lst[i[1]]
    two_total = ((N - 1) * 4 + (N - 2) * 4) * mn

    mn = sys.maxsize
    available = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    for i in available:
        if lst[i[0]] + lst[i[1]] + lst[i[2]] < mn:
            mn = lst[i[0]] + lst[i[1]] + lst[i[2]]

    three_total = 4 * mn

    print(one_total + two_total + three_total)
