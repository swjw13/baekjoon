# https://www.acmicpc.net/problem/1208
# 부분수열의 합

import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, S = list(map(int, input().split()))

lst = list(map(int, input().split()))
length = len(lst)

lst_left = lst[:length // 2]
lst_right = lst[length // 2:]

left_totals = []
right_totals = []

stack = deque([(0, 0, 0)])
while stack:
    turn, total, number_count = stack.pop()
    if turn == len(lst_right):
        right_totals.append(total)
    else:
        stack.append((turn + 1, total, number_count))
        stack.append((turn + 1, total + lst_right[turn], number_count + 1))

stack = deque([(0, 0, 0)])
while stack:
    turn, total, number_count = stack.pop()
    if turn == len(lst_left):
        left_totals.append(total)
    else:
        stack.append((turn + 1, total, number_count))
        stack.append((turn + 1, total + lst_left[turn], number_count + 1))

left_totals.sort()
right_totals.sort(reverse=True)

left_idx = 0
right_idx = 0
answer = 0

while left_idx < len(left_totals) and right_idx < len(right_totals):
    tmp = left_totals[left_idx] + right_totals[right_idx]
    if tmp == S:
        bisect_left_idx = left_idx
        while bisect_left_idx < len(left_totals) and left_totals[bisect_left_idx] == left_totals[left_idx]:
            bisect_left_idx += 1

        bisect_right_idx = right_idx
        while bisect_right_idx < len(right_totals) and right_totals[bisect_right_idx] == right_totals[right_idx]:
            bisect_right_idx += 1

        answer += (bisect_right_idx - right_idx) * (bisect_left_idx - left_idx)
        left_idx = bisect_left_idx
        right_idx = bisect_right_idx
    elif tmp < S:
        left_idx += 1
    else:
        right_idx += 1

if S == 0:
    answer -= 1
print(answer)
