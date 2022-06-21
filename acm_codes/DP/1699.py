# https://www.acmicpc.net/problem/1699
# 제곱수의 합

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dp = [100001 for _ in range(N + 1)]
dp[0] = 0
queue = deque([0])
while queue:
    cur_point = queue.popleft()
    idx = 1
    tmp = dp[cur_point]
    while True:
        new_point = cur_point + idx * idx
        if new_point < N + 1:
            if dp[new_point] > tmp + 1:
                dp[new_point] = tmp + 1
                queue.append(new_point)
            idx += 1
        else:
            break

print(dp[N])