# https://www.acmicpc.net/problem/1009
# 분산 처리

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = list(map(int, input().split()))
    b = b % 4 + 4
    a = a % 10
    answer = (a ** b) % 10
    if answer == 0:
        answer = 10
    print(answer)