# https://www.acmicpc.net/problem/2750
# bubble sort

import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

for i in range(N - 1):
    for j in range(N - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in lst:
    print(i)