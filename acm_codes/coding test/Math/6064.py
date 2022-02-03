# 카잉 달력?
# https://www.acmicpc.net/problem/6064

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = list(map(int, input().split()))
    a, b, c = [1,1,1]
    
    ans = -1
    while True:
        if a == x and b == y:
            ans = c
            break
        if a == M and b == N:
            break

        a, b, c = (a % M + 1, b % N + 1, c + 1)

    print(ans)
