# 회의 시간 배정

import sys

N = int(input())
times = []
for _ in range(N):
    s, e = list(map(int, sys.stdin.readline().split()))
    times.append((s, e))
times.sort(key=lambda x: (x[1], x[0]))

s = 0
c = 0
for i in range(N):
    if times[i][0] >= s:
        c += 1
        s = times[i][1]

print(c)
