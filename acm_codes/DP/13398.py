# https://www.acmicpc.net/problem/13398
# 연속 합 2

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(2)]

for i in range(n):
    if lst[i] >= 0:
        dp[1][i + 1] = dp[1][i] + lst[i]
        dp[0][i + 1] = dp[0][i] + lst[i]
    else:
        dp[1][i + 1] = max(0, dp[1][i] + lst[i])
        dp[0][i + 1] = max(0, dp[0][i] + lst[i], dp[1][i])

a = max(max(dp[0]), max(dp[1]))
if a == 0:
    print(max(lst))
else:
    print(a)
