# https://www.acmicpc.net/problem/2750
# selection sort

import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

for i in range(N):
    min_value = 1001
    min_idx = i
    for j in range(i, N):
        if lst[j] < min_value:
            min_value = lst[j]
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

for i in lst:
    print(i)
