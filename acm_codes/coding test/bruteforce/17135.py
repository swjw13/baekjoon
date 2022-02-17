# 캐슬 디펜스
# https://www.acmicpc.net/problem/17135

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


N, M, dist = list(map(int, input().split()))
mp_tmp = []
for _ in range(N):
    mp_tmp.append(list(map(int, input().split())))
mp = [deque() for _ in range(M)]

for i in range(N):
    for j in range(M):
        mp[j].append(mp_tmp[i][j])

mp.append([i for i in range(M)])

