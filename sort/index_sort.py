#10989

import sys

N = int(input())
lst = [0 for i in range(10001)]

for _ in range(N):
    n = int(sys.stdin.readline())
    lst[n] += 1

for i in range(1, 10001):
    for j in range(lst[i]):
        print(i)
