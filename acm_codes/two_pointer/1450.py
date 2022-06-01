# https://www.acmicpc.net/problem/1450
# 냅색 문제

import sys
from collections import deque
from bisect import bisect_right

input = sys.stdin.readline

N, C = list(map(int, input().split()))
lst = list(map(int, input().split()))

length = len(lst)
lst_left = lst[:length // 2]
lst_right = lst[length // 2:]

left_totals = []
right_totals = []

stack = deque([(0, 0)])
while stack:
    turn, total = stack.pop()
    if turn == len(lst_left):
        left_totals.append(total)
    else:
        stack.append((turn + 1, total))
        tmp = total + lst_left[turn]
        if tmp <= C:
            stack.append((turn + 1, tmp))

stack = deque([(0, 0)])
while stack:
    turn, total = stack.pop()
    if turn == len(lst_right):
        right_totals.append(total)
    else:
        stack.append((turn + 1, total))
        tmp = total + lst_right[turn]
        if tmp <= C:
            stack.append((turn + 1, tmp))

left_totals.sort()
right_totals.sort()
answer = 0

for i in left_totals:
    tmp = bisect_right(right_totals, C - i)
    answer += tmp

print(answer)