# # https://www.acmicpc.net/problem/1049
# # 기타줄
#
# import sys
# input = sys.stdin.readline
#
# N, M = list(map(int, input().split()))
# dp = [sys.maxsize for _ in range(200)]
# dp[0] = 0
# money = {1: sys.maxsize, 6: sys.maxsize}
# for _ in range(M):
#     six, one = list(map(int, input().split()))
#     money[6] = min(money[6], six)
#     money[1] = min(money[1], one)
#
# for i in range(N):
#     if i + 1 < 200:
#         dp[i + 1] = min(dp[i + 1], dp[i] + money[1])
#     if i + 6 < 200:
#         dp[i + 6] = min(dp[i + 6], dp[i] + money[6])
#
# print(min(dp[N:]))
from itertools import combinations
cnt = 0
for _ in combinations([i for i in range(26)], 13):
    cnt += 1
print(cnt)