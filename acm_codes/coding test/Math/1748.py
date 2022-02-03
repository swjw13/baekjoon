# 수 이어쓰기
# https://www.acmicpc.net/problem/1748

import sys

input = sys.stdin.readline

N = int(input())
tmp = 0


def check(i, num):
    checkpoint1 = pow(10, i - 1)
    checkpoint2 = pow(10, i)
    if checkpoint1 <= num < checkpoint2:
        return i * (N - checkpoint1 + 1)
    elif num < checkpoint1:
        return 0
    else:
        return 9 * i * checkpoint1

for i in range(1, 9):
    tmp += check(i, N)

if N == 100000000:
    tmp += 9

print(tmp)