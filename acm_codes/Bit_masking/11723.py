# 기본 집합 연산
# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline

N = int(input())
S = [0 for _ in range(21)]

for _ in range(N):
    tmp = input().split()
    if tmp[0] == "all":
        S = [1 for _ in range(21)]
    elif tmp[0] == "empty":
        S = [0 for _ in range(21)]
    elif tmp[0] == "add":
        S[int(tmp[1])] = 1
    elif tmp[0] == "remove":
        S[int(tmp[1])] = 0
    elif tmp[0] == "check":
        print(S[int(tmp[1])])
    elif tmp[0] == "toggle":
        S[int(tmp[1])] = S[int(tmp[1])] ^ 1
