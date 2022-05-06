# https://www.acmicpc.net/problem/2750
# insertion sort

import sys

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

for i in range(1, N):
    j = i - 1
    key = lst[i]

    while j >= 0 and lst[j] > key:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

for i in lst:
    print(i)
