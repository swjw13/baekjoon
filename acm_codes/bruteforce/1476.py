# https://www.acmicpc.net/problem/1476
# 날짜 계산

import sys

input = sys.stdin.readline

E, S, M = list(map(int, input().split()))
year = 0
e = 0
s = 0
m = 0
while True:
    e = (e) % 15 + 1
    s = (s) % 28 + 1
    m = (m) % 19 + 1
    year += 1
    if e == E and s == S and m == M:
        print(year)
        break
